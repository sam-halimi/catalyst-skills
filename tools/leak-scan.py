#!/usr/bin/env python3
"""Leak scanner: blocks a publication when private data is found.

Two layers:
  1. Generic patterns (emails, phone numbers, server paths, deployment URLs,
     cloud file ids, credentials). They ship with this repository.
  2. A private denylist (client names, people, slugs). It never ships: it is
     passed with --denylist and lives outside the repository.

Usage:
  python3 tools/leak-scan.py [ROOT] [--denylist FILE] [--allow FILE] [--quiet]

Exit code 0 when clean, 1 when at least one finding, 2 on usage error.
No dependency outside the standard library.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import unicodedata

SKIP_DIRS = {".git", "node_modules", ".next", "__pycache__"}
BINARY_EXT = {
    ".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".ico", ".pdf",
    ".woff", ".woff2", ".ttf", ".otf", ".mp4", ".webm", ".zip", ".gz",
}

GENERIC = [
    ("email", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")),
    ("phone", re.compile(r"(?<![\w.])(?:\+33[\s.]?|0)[1-9](?:[\s.-]?\d{2}){4}(?![\w])")),
    ("server-path", re.compile(r"/(?:home|Users)/[A-Za-z0-9._-]+/")),
    ("deployment-url", re.compile(r"\b[a-z0-9][a-z0-9-]*\.vercel\.app\b", re.I)),
    ("cdn-url", re.compile(r"\b[a-z0-9]+\.cloudfront\.net\b", re.I)),
    ("cloud-file-id", re.compile(r"(?<![A-Za-z0-9_-])1[A-Za-z0-9_-]{32,}(?![A-Za-z0-9_-])")),
    ("maps-link", re.compile(r"(?:maps\.app\.goo\.gl|goo\.gl/maps|google\.[a-z.]+/maps/place)/\S+", re.I)),
    ("credential", re.compile(
        r"github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,}"
        r"|shp(?:at|ss|ca|pa)_[a-fA-F0-9]{32}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{10,}"
        r"|-----BEGIN [A-Z ]*PRIVATE KEY-----"
    )),
    ("credential-assignment", re.compile(
        r"(?i)\b(?:api[_-]?key|(?:access|auth|bearer)?[_-]?token|secret|password|passwd)\b"
        r"\s*[:=]\s*['\"]?[A-Za-z0-9_\-/+]{16,}"
    )),
]


def fold(text: str) -> str:
    """Lowercase and strip accents, keeping string length stable per character."""
    out = []
    for ch in text:
        base = unicodedata.normalize("NFD", ch)
        kept = "".join(c for c in base if unicodedata.category(c) != "Mn")
        out.append((kept or ch)[0].lower() if kept else ch.lower())
    return "".join(out)


def load_terms(path: str) -> list[tuple[str, re.Pattern[str], bool]]:
    """Return (label, pattern, folded) for each denylist line.

    Plain lines match case and accent insensitively, on word boundaries.
    Lines starting with `re:` are raw regular expressions.
    """
    terms = []
    with open(path, encoding="utf-8") as handle:
        for raw in handle:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("re:"):
                terms.append((line, re.compile(line[3:], re.I), False))
                continue
            folded = fold(line)
            body = re.escape(folded).replace(r"\ ", r"[\s _-]+")
            pattern = re.compile(r"(?<![a-z0-9])" + body + r"(?![a-z0-9])")
            terms.append((line, pattern, True))
    return terms


def load_allow(path: str | None) -> list[re.Pattern[str]]:
    if not path or not os.path.exists(path):
        return []
    allow = []
    with open(path, encoding="utf-8") as handle:
        for raw in handle:
            line = raw.strip()
            if line and not line.startswith("#"):
                allow.append(re.compile(line, re.I))
    return allow


def iter_files(root: str):
    for folder, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in sorted(files):
            yield os.path.join(folder, name)


def scan(root: str, terms, allow) -> list[tuple[str, int, str, str]]:
    findings = []

    def allowed(value: str) -> bool:
        return any(rule.search(value) for rule in allow)

    for path in iter_files(root):
        rel = os.path.relpath(path, root)
        folded_rel = fold(rel)
        for label, pattern, folded in terms:
            target = folded_rel if folded else rel
            if pattern.search(target) and not allowed(rel):
                findings.append((rel, 0, "denylist-in-path", label))
        if os.path.splitext(path)[1].lower() in BINARY_EXT:
            continue
        try:
            with open(path, encoding="utf-8") as handle:
                lines = handle.read().splitlines()
        except (UnicodeDecodeError, OSError):
            findings.append((rel, 0, "unreadable", "file is not UTF-8 text: review by hand"))
            continue
        for number, line in enumerate(lines, 1):
            for category, pattern in GENERIC:
                for match in pattern.finditer(line):
                    value = match.group(0)
                    if not allowed(value):
                        findings.append((rel, number, category, value))
            folded_line = None
            for label, pattern, folded in terms:
                if folded:
                    if folded_line is None:
                        folded_line = fold(line)
                    hit = pattern.search(folded_line)
                else:
                    hit = pattern.search(line)
                if hit and not allowed(hit.group(0)) and not allowed(label):
                    findings.append((rel, number, "denylist", label))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Block publication of private data.")
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--denylist", help="private list of terms, kept outside the repository")
    parser.add_argument("--allow", help="regular expressions of accepted values (default: ROOT/.leakscan-allow)")
    parser.add_argument("--quiet", action="store_true", help="print the summary only")
    args = parser.parse_args()

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f"not a directory: {root}", file=sys.stderr)
        return 2
    terms = load_terms(args.denylist) if args.denylist else []
    allow = load_allow(args.allow or os.path.join(root, ".leakscan-allow"))

    findings = scan(root, terms, allow)
    if not args.quiet:
        for rel, number, category, value in findings:
            where = f"{rel}:{number}" if number else rel
            print(f"{where}: [{category}] {value}")
    layers = "generic patterns" + (f" + {len(terms)} denylist terms" if terms else "")
    if findings:
        files = len({f[0] for f in findings})
        print(f"\nBLOCKED: {len(findings)} finding(s) in {files} file(s) ({layers}).")
        return 1
    print(f"CLEAN: no finding ({layers}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

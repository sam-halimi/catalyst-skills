#!/usr/bin/env python3
"""validate-state.py — validation déterministe d'un .catalyst/production.yaml.

Usage : python3 validate-state.py <chemin/production.yaml>
Exit codes : 0 = valide (warnings possibles), 1 = invalide, 2 = erreur d'usage.
Lecture seule. Schéma de référence : ../references/state-schema.md (versions 1-2).
Racines de projets configurables : variables d'environnement CATALYST_SITES_DIR
et CATALYST_ARCHIVES_DIR (défauts : ~/projets/sites et ~/projets/archives-sites).
"""
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERREUR: PyYAML absent (python3 -c 'import yaml' échoue).")
    sys.exit(2)

ENUMS = {
    "mode": {"new", "resume", "special"},
    "statut": {"onboarding", "pre_da", "production", "recette", "iterations",
               "cloture", "archive"},
    "checkpoint": {"onboarding_valide", "design_read", "checkpoint_1_da",
                   "go_da", "checkpoint_2_hero", "checkpoint_3_recette",
                   "gates_sortie", "cloture"},
    "niche": {"immobilier", "avocat", "commerce_hospitality", "editorial",
              "personnalite_sport", "autre"},
    "autonomie": {"guidee", "checkpoints_cles", "autonome_apres_go_da"},
}
SUB_ENUMS = {
    ("crm", "statut"): {"present", "absent", "special"},
    ("recherche", "mode"): {"fourni", "recherche_complete", "adaptation", "hybride"},
    ("da", "mode"): {"libre", "imposee", "hybride"},
    ("hero", "type"): {"scroll_frames_3d", "image_animee", "statique",
                       "typographique", "recommandation"},
    ("assets", "source"): {"fournis_sam", "internet", "generes_ia", "mixtes"},
    ("sections", "mode"): {"libres", "imposees", "hybrides"},
    ("contenu", "mode"): {"fourni", "recherche_complete", "adaptation", "hybride"},
    ("seo", "socle"): {"complet", "local", "editorial_geo", "noindex_temporaire",
                       "exception"},
    ("seo", "indexation"): {"ouverte", "gate_noindex"},
    ("conversion", "capture"): {"aucune", "inline", "popup", "les_deux"},
}
SEO_OBJECTIFS = {"demo", "vitrine_locale", "trafic"}
POPUP_TYPES = {"micro_engagement", "quiz", "visual_quiz", "scratch",
               "mystery_reward", "gamification", "classique", "recommandation"}
DESTINATIONS = {"email", "crm_sheet", "brevo", "klaviyo", "webhook", "autre"}
TRIGGERS = {"delai", "scroll", "exit_desktop", "clic", "pages", "comportement"}
EVENTS = {"impression", "engagement", "submit", "success", "close"}
REQUIRED_TOP = ["schema_version", "projet", "mode", "statut", "checkpoint",
                "crm", "niche", "autonomie", "break_rules", "seo",
                "conversion", "validations", "timestamps"]
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?([+-]\d{2}:\d{2}|Z)?$")
SECRET_RES = [
    re.compile(r"(?i)\b(api[_-]?key|apikey|secret|token|password|passwd|bearer|"
               r"authorization|private[_-]?key)\b\s*[:=]\s*['\"]?[A-Za-z0-9_\-./+=]{8,}"),
    re.compile(r"\bsk-[A-Za-z0-9_\-]{16,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}"),
    re.compile(r"\bghp_[A-Za-z0-9]{20,}"),
    re.compile(r"\beyJ[A-Za-z0-9_\-]{20,}\."),  # JWT
]

SITES_DIR = os.path.normpath(os.path.expanduser(
    os.environ.get("CATALYST_SITES_DIR", "~/projets/sites")))
ARCHIVES_DIR = os.path.normpath(os.path.expanduser(
    os.environ.get("CATALYST_ARCHIVES_DIR", "~/projets/archives-sites")))

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def check_enum(data, path, allowed, required=True):
    node = data
    for key in path[:-1]:
        node = node.get(key) if isinstance(node, dict) else None
        if node is None:
            if required:
                err(f"bloc manquant : {'.'.join(path[:-1])}")
            return None
    if not isinstance(node, dict):
        err(f"bloc invalide (mapping attendu) : {'.'.join(path[:-1])}")
        return None
    val = node.get(path[-1])
    if val is None:
        if required:
            err(f"champ manquant : {'.'.join(path)}")
        return None
    if val not in allowed:
        err(f"valeur hors énumération : {'.'.join(path)} = {val!r} "
            f"(autorisées : {sorted(allowed)})")
    return val


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    fpath = sys.argv[1]
    if not os.path.isfile(fpath):
        print(f"ERREUR: fichier introuvable : {fpath}")
        return 2

    raw = open(fpath, encoding="utf-8").read()
    for rx in SECRET_RES:
        m = rx.search(raw)
        if m:
            err(f"motif de secret détecté (interdit dans l'état) : "
                f"{m.group(0)[:40]}…")

    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        print(f"INVALIDE — YAML illisible : {e}")
        return 1
    if not isinstance(data, dict):
        print("INVALIDE — la racine doit être un mapping YAML.")
        return 1

    for key in REQUIRED_TOP:
        if key not in data:
            err(f"champ racine manquant : {key}")

    version = data.get("schema_version")
    if version not in (1, 2):
        err(f"schema_version doit valoir 1 ou 2 (trouvé : {version!r})")

    # projet + cohérence chemin/slug
    projet = data.get("projet")
    if isinstance(projet, dict):
        for k in ("nom", "slug", "path"):
            if not projet.get(k):
                err(f"champ manquant : projet.{k}")
        slug, path = projet.get("slug"), projet.get("path")
        if slug and path:
            base = os.path.basename(os.path.normpath(str(path)))
            if base not in (f"site-{slug}", str(slug)):
                err(f"incohérence slug/chemin : basename({path!r}) = {base!r}, "
                    f"attendu 'site-{slug}'")
            if not os.path.isdir(str(path)):
                warn(f"le chemin projet n'existe pas (encore) : {path}")
            norm = os.path.normpath(str(path))
            if not (norm.startswith(SITES_DIR + os.sep)
                    or norm.startswith(ARCHIVES_DIR + os.sep)
                    or norm.startswith("/tmp/")):
                warn(f"chemin hors racines connues (sites/, archives-sites/, /tmp) : {path}")
            state_dir = os.path.dirname(os.path.abspath(fpath))
            expected = os.path.join(norm, ".catalyst")
            if os.path.isdir(str(path)) and os.path.realpath(state_dir) != os.path.realpath(expected):
                err(f"le fichier d'état ne vit pas dans {expected} "
                    f"(trouvé : {state_dir})")
    elif projet is not None:
        err("projet doit être un mapping (nom/slug/path)")

    for field, allowed in ENUMS.items():
        val = data.get(field)
        if val is None:
            continue  # déjà signalé par REQUIRED_TOP
        if val not in allowed:
            err(f"valeur hors énumération : {field} = {val!r} "
                f"(autorisées : {sorted(allowed)})")
    for path, allowed in SUB_ENUMS.items():
        check_enum(data, list(path), allowed, required=path[0] in REQUIRED_TOP)

    # break_rules
    br = data.get("break_rules")
    if isinstance(br, dict) and br.get("active"):
        lifted = br.get("rules_lifted") or []
        reasons = br.get("reasons") or {}
        if not lifted:
            err("break_rules.active=true exige rules_lifted non vide")
        for rule in lifted:
            if rule not in reasons or not reasons[rule]:
                err(f"raison manquante pour la règle levée : {rule!r}")
        if br.get("invariants_confirmes") is not True:
            err("break_rules.active=true exige invariants_confirmes: true")

    # conversion
    conv = data.get("conversion")
    if isinstance(conv, dict):
        cap = conv.get("capture")
        if cap in ("popup", "les_deux"):
            popup = conv.get("popup")
            if not isinstance(popup, dict) or not popup.get("type"):
                err("capture popup/les_deux exige conversion.popup.type")
            elif popup.get("type") not in POPUP_TYPES:
                err(f"conversion.popup.type hors énumération : {popup.get('type')!r}")
            if isinstance(popup, dict):
                for t in popup.get("triggers") or []:
                    if t not in TRIGGERS:
                        err(f"trigger inconnu : {t!r} (autorisés : {sorted(TRIGGERS)})")
        if cap and cap != "aucune":
            dests = conv.get("destination") or []
            if not dests:
                err("capture != aucune exige conversion.destination non vide")
            for d in dests:
                if d not in DESTINATIONS:
                    err(f"destination inconnue : {d!r} (autorisées : {sorted(DESTINATIONS)})")

    # seo / niche
    seo = data.get("seo")
    if isinstance(seo, dict):
        if seo.get("socle") == "exception" and not seo.get("exception_raison"):
            err("seo.socle=exception exige seo.exception_raison")
        objectif = seo.get("objectif")
        if objectif is None:
            if version == 2:
                err("champ manquant : seo.objectif (obligatoire en schema_version 2)")
        elif objectif not in SEO_OBJECTIFS:
            err(f"valeur hors énumération : seo.objectif = {objectif!r} "
                f"(autorisées : {sorted(SEO_OBJECTIFS)})")
        cibles = seo.get("requetes_cibles")
        if cibles is not None and not isinstance(cibles, list):
            err("seo.requetes_cibles doit être une liste")
            cibles = []
        if objectif == "trafic":
            non_vides = [c for c in (cibles or []) if isinstance(c, str) and c.strip()]
            if not 3 <= len(non_vides) <= 5:
                err("seo.objectif=trafic exige 3 à 5 requetes_cibles non vides "
                    f"(trouvé : {len(non_vides)})")
    if data.get("niche") == "avocat":
        contraintes = data.get("contraintes") or {}
        if contraintes.get("cadre_avocat") is not True:
            err("niche=avocat exige contraintes.cadre_avocat: true")

    # tracking events
    tr = data.get("tracking")
    if isinstance(tr, dict):
        for e in tr.get("events") or []:
            if e not in EVENTS:
                err(f"événement tracking inconnu : {e!r}")

    # timestamps + validations
    ts = data.get("timestamps")
    if isinstance(ts, dict):
        for k in ("created", "updated"):
            v = ts.get(k)
            if not v or not ISO_RE.match(str(v)):
                err(f"timestamps.{k} absent ou non ISO 8601 : {v!r}")
    vals = data.get("validations")
    if vals is not None and not isinstance(vals, list):
        err("validations doit être une liste (journal append-only)")

    for w in warnings:
        print(f"AVERTISSEMENT : {w}")
    if errors:
        print(f"INVALIDE — {len(errors)} erreur(s) :")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"VALIDE — {fpath}"
          + (f" ({len(warnings)} avertissement(s))" if warnings else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env bash
# discover-project.sh — découverte LECTURE SEULE des projets Catalyst.
# Usage : discover-project.sh [terme] ; sans terme : liste tout.
# Recherche exacte puis fuzzy (sous-chaîne insensible à la casse) sous
# sites/, puis archives-sites/. Racines configurables par les variables
# d'environnement CATALYST_SITES_DIR et CATALYST_ARCHIVES_DIR. N'écrit rien, ne sélectionne jamais :
# la décision revient à la session (AskUserQuestion si ambigu).
set -euo pipefail

SITES="${CATALYST_SITES_DIR:-$HOME/projets/sites}"
ARCHIVES="${CATALYST_ARCHIVES_DIR:-$HOME/projets/archives-sites}"
QUERY="${1:-}"

describe() {
  local p="$1" zone="$2" kind="$3"
  local state="aucun état" extras="" gitline
  [ -f "$p/.catalyst/production.yaml" ] && state=".catalyst/production.yaml"
  [ -f "$p/DECISIONS.md" ] && extras="$extras DECISIONS.md"
  [ -f "$p/RAPPORT.md" ] && extras="$extras RAPPORT.md"
  [ -f "$p/CLAUDE.md" ] && extras="$extras CLAUDE.md"
  [ -f "$p/package.json" ] && extras="$extras package.json"
  if compgen -G "$p/docs/checkpoint*" > /dev/null 2>&1; then
    extras="$extras docs/checkpoint*"
  fi
  if [ -d "$p/.git" ]; then
    local last dirty
    last="$(git -C "$p" log -1 --format='%ad · %s' --date=short 2>/dev/null || echo 'historique illisible')"
    dirty="$(git -C "$p" status --porcelain 2>/dev/null | wc -l | tr -d ' ')"
    gitline="git : $last (non commités : $dirty)"
  else
    gitline="git : absent"
  fi
  printf '%s [%s] %s\n' "$kind" "$zone" "$p"
  printf '  état : %s |%s\n' "$state" "${extras:- (aucun fichier de pilotage)}"
  printf '  %s\n' "$gitline"
}

scan_dir() {
  local dir="$1" zone="$2"
  [ -d "$dir" ] || return 0
  local p name lo_name lo_q
  lo_q="$(printf '%s' "$QUERY" | tr '[:upper:]' '[:lower:]')"
  for p in "$dir"/*/; do
    p="${p%/}"
    name="$(basename "$p")"
    lo_name="$(printf '%s' "$name" | tr '[:upper:]' '[:lower:]')"
    if [ -z "$QUERY" ]; then
      describe "$p" "$zone" "CANDIDAT"
    elif [ "$lo_name" = "$lo_q" ] || [ "$lo_name" = "site-$lo_q" ]; then
      describe "$p" "$zone" "MATCH_EXACT"
    elif [ "${lo_name#*"$lo_q"}" != "$lo_name" ]; then
      describe "$p" "$zone" "MATCH_FUZZY"
    fi
  done
}

echo "— Recherche : '${QUERY:-<tout>}' —"
scan_dir "$SITES" "sites"
scan_dir "$ARCHIVES" "archives"
echo "— Fin. Aucune sélection effectuée par ce script (lecture seule). —"

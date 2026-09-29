# Checkpoints — mapping vers les autorités existantes

Ce fichier ne définit AUCUN nouveau gate : il relie l'état
`production.yaml` (`checkpoint`, `statut`, `validations`) aux checkpoints et
gates déjà canoniques. Les seuils et contenus vivent dans leurs sources.

| `checkpoint` (état) | Autorité | Contenu (par référence) |
|---|---|---|
| `onboarding_valide` | ce skill | Récapitulatif validé « Valider et enregistrer l'état ». Exception pré-GO du CLAUDE.md active : pilotage + recherche seulement, zéro production. |
| `design_read` | `da-moderne` | DESIGN READ produit (objet de confiance, mode), consigné dans `docs/`. |
| `checkpoint_1_da` | CLAUDE.md (séquence de lancement, étape 7) + playbook phase 2 | DESIGN READ + 2-3 directions tokens chiffrées avec préviews + recommandation. **Arrêt obligatoire.** |
| `go_da` | Sam | GO explicite sur une direction. Débloque la production ; si `autonomie: autonome_apres_go_da` → skill `mission-template` (périmètre fermé dérivé de l'état). |
| `checkpoint_2_hero` | `da-moderne` / playbook phase 2 | Hero seul, niveau final, validé avant de descendre. |
| `checkpoint_3_recette` | playbook phases 3-4 | Socle `seo-garantie-90` complet dès la V1, recette (grep anti-slop, captures, Lighthouse local) avant deploy. |
| `gates_sortie` | playbook §1 + `mission-template` §6 | 4 catégories Lighthouse sur l'alias prod public (Perf ≥ 90, SEO ≥ 95, A11y ≥ 95, BP ≥ 90), best-of-N si VPS chargé, max 3 passes correctives. |
| `cloture` | `/production-finish` | Gates fermés, RAPPORT.md, leçons candidates présentées une à une (apprentissage contrôlé — aucune promotion sans validation de Sam). |

Règles transverses :
- Un checkpoint ne s'enregistre dans `validations` qu'avec la décision
  explicite de Sam (« GO », « validé ») — jamais déduit du silence.
- Restent bloquants même en autonomie : sécurité, légalité, chemin ambigu,
  action externe (lead test, publication, envoi).
- Les boucles de retours post-V1 (playbook phase 5) ne régressent pas le
  checkpoint : elles vivent dans `statut: iterations`.

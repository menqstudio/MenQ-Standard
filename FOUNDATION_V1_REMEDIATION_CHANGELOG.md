# Foundation v1 Remediation Changelog / Foundation v1 remediation փոփոխությունների պատմություն

**Date / Ամսաթիվ:** 2026-07-12  
**Status / Կարգավիճակ:** Applied — validation evidence pending / Կիրառված — validation evidence-ը սպասվում է  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

- Foundation integrity audit-ը արձանագրել է `R-01–R-07` findings-ը։
- Ստեղծվել են missing chapter contexts-ը՝ Philosophy, Principles, Terminology, Governance, Decision System և Documentation folders-ում։
- `foundation/PROJECT_CONTEXT.md` և `AI_WORKING_CONTEXT.md` synchronized են AI Collaboration v1-ի և remediation state-ի հետ։
- Ավելացվել է append-only `DECISION_INDEX.md`, որը պահպանում է `D-001–D-023` traceability-ն առանց մեծ `DECISIONS.md` file-ի unsafe rewrite-ի։
- Ավելացվել են Documentation և AI Collaboration bilingual parity addenda-ները։
- Ավելացվել է `foundation/FOUNDATION_NORMATIVE_METADATA_REGISTRY.md`։
- Ավելացվել է `scripts/validate_foundation.py` validator-ը։
- Ավելացվել է `.github/workflows/foundation-integrity.yml` CI workflow-ը։
- Ավելացվել է `COLLABORATION_STYLE.md`՝ Գևորգի հետ բոլոր AI collaborators-ի communication mood-ը նույնացնելու համար։
- Root README navigation-ը synchronized է նոր canonical controls-ի հետ։
- Local clone validation-ը չաշխատեց execution environment-ի network DNS սահմանափակման պատճառով։ GitHub Actions run/status evidence-ը դեռ չի վերադարձել։
- Մինչ validator GREEN evidence-ը Foundation v1 ZIP snapshot-ը չի ներկայացվում որպես validated release artifact։

## English

- The Foundation integrity audit recorded findings `R-01–R-07`.
- Missing chapter contexts were created for Philosophy, Principles, Terminology, Governance, the Decision System, and Documentation.
- `foundation/PROJECT_CONTEXT.md` and `AI_WORKING_CONTEXT.md` were synchronized with AI Collaboration v1 and the remediation state.
- An append-only `DECISION_INDEX.md` was added to preserve `D-001–D-023` traceability without unsafe rewrites of the large `DECISIONS.md` file.
- Documentation and AI Collaboration bilingual parity addenda were added.
- `foundation/FOUNDATION_NORMATIVE_METADATA_REGISTRY.md` was added.
- The `scripts/validate_foundation.py` validator was added.
- The `.github/workflows/foundation-integrity.yml` CI workflow was added.
- `COLLABORATION_STYLE.md` was added to keep all AI collaborators in the same communication mood with Gevorg.
- Root README navigation was synchronized with the new canonical controls.
- Local clone validation could not run because the execution environment could not resolve GitHub over DNS. GitHub Actions run/status evidence has not yet been returned.
- Until validator GREEN evidence exists, the Foundation v1 ZIP snapshot is not represented as a validated release artifact.

<!-- END: FOUNDATION_V1_REMEDIATION_CHANGELOG -->
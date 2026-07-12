# MenQ Design Platform Preview Migration and Deprecation Guide

Status: Approved — Implementing  
Decision: D-025  
Release channel: `next`

## Հայերեն

### Migration contract

Յուրաքանչյուր breaking կամ consumer-visible change պետք է ունենա՝ հին contract-ի նկարագրություն, նոր contract, ազդեցության scope, քայլ առ քայլ migration, validation command և rollback reference։ Migration evidence-ը պետք է կապվի source commit-ին ու release candidate-ին։

### Deprecation contract

- Deprecated public API-ն պետք է նշվի machine-readable metadata-ում և bilingual documentation-ում։
- Deprecation record-ը պետք է նշի replacement-ը, պատճառը, առաջին deprecated version-ը և հնարավոր removal window-ը։
- Preview փուլում removal window-ը compatibility promise չէ, բայց նույն candidate-ի ներսում silent removal-ը արգելված է։
- Deprecated API-ի հեռացումը պահանջում է public API diff, migration evidence և Owner-controlled release decision։

### Current candidate

`0.1.0-next.0`-ը առաջին preview baseline-ն է։ Նախորդ Stable release կամ իրական consumer migration claim չկա։ Consumer pilots-ի արդյունքները դեռ պարտադիր evidence են։

## English

### Migration contract

Every breaking or consumer-visible change must include the old contract, the new contract, affected scope, step-by-step migration, validation command, and rollback reference. Migration evidence must be linked to the source commit and release candidate.

### Deprecation contract

- A deprecated public API must be marked in machine-readable metadata and bilingual documentation.
- The deprecation record must identify the replacement, rationale, first deprecated version, and possible removal window.
- During Preview, a removal window is not a compatibility promise, but silent removal inside the same candidate is prohibited.
- Removing a deprecated API requires a public API diff, migration evidence, and an Owner-controlled release decision.

### Current candidate

`0.1.0-next.0` is the first preview baseline. No previous Stable release or real consumer migration is claimed. Consumer pilot results remain required evidence.

— End of document —

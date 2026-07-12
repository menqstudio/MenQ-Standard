# MenQ Design Platform Preview Compatibility Policy

Status: Approved — Implementing  
Decision: D-025  
Release channel: `next`  
Candidate version: `0.1.0-next.0`

## Հայերեն

### Նպատակ

Այս քաղաքականությունը սահմանում է MenQ Design Platform-ի `Preview` package family-ի compatibility կանոնները մինչև Stable release-ի առանձին Owner approval-ը։ Այն չի ստեղծում Stable compatibility promise։

### Կանոններ

- Բոլոր տասը package-ները versionավորվում են միասնական synchronized version-ով։
- Public API-ն սահմանվում է միայն package `exports` map-ով և documented public contract-ներով։ Private deep import-ը արգելված է։
- Export-ի հեռացումը, export target-ի անհամատեղելի փոփոխությունը կամ public contract-ի իմաստային խախտումը breaking change է։
- Նոր export-ը additive change է և Preview փուլում պահանջում է public API diff evidence։
- Internal implementation change-ը non-breaking է միայն այն դեպքում, երբ public API-ն, runtime contract-ը և generated artifact semantics-ը չեն փոխվում։
- `next` channel-ը կարող է ընդունել breaking change միայն migration guide, deprecation record, public API diff և Owner-controlled release decision ունենալու դեպքում։
- GREEN CI-ն release, merge կամ lock authorization չէ։

### Verdict

Compatibility evidence-ը կարող է լինել GREEN, YELLOW կամ RED։ Stable compatibility promise-ը մնում է `false`, մինչև Owner-ը առանձին հաստատի Stable lifecycle-ը։

## English

### Purpose

This policy defines compatibility rules for the MenQ Design Platform `Preview` package family until a separate Owner approval authorizes a Stable release. It does not create a Stable compatibility promise.

### Rules

- All ten packages use one synchronized version.
- The public API is defined only by package `exports` maps and documented public contracts. Private deep imports are prohibited.
- Removing an export, incompatibly changing an export target, or semantically violating a public contract is a breaking change.
- Adding an export is an additive change and requires public API diff evidence during Preview.
- An internal implementation change is non-breaking only when the public API, runtime contract, and generated artifact semantics remain unchanged.
- The `next` channel may accept a breaking change only with a migration guide, deprecation record, public API diff, and an Owner-controlled release decision.
- GREEN CI is not release, merge, or lock authorization.

### Verdict

Compatibility evidence may be GREEN, YELLOW, or RED. The Stable compatibility promise remains `false` until the Owner separately approves the Stable lifecycle.

— End of document —

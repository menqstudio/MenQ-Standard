# MenQ Standard

> **HY**  
> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

> **EN**  
> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

## Status / Կարգավիճակ

- **Foundation v1:** Locked and GREEN / Locked և GREEN
- **D-024 Platforms Architecture v1:** merged and canonical / merged և canonical
- **D-025 MenQ Design Platform Architecture v1:** technical and adoption readiness GREEN; Owner authority pending / տեխնիկական և որդեգրման պատրաստականություն GREEN, Owner լիազորումը սպասման մեջ
- **D-026 Canonical Session Read Law:** Locked and machine-enforced / Locked և machine-enforced
- **Draft PR #3:** open, Draft, mergeable, and unmerged / open, Draft, mergeable և unmerged
- **Owner:** MenQ
- **Languages:** Armenian + English

## Ecosystem / Էկոհամակարգ

```text
MenQ Ecosystem
├── MenQ Studio
│   ├── Company
│   ├── Services
│   └── Products
│
└── MenQ Standard
    ├── Foundation
    ├── Platforms
    ├── Operating Standards
    └── Extensions
```

## Purpose / Նպատակ

**HY:** MenQ Studio-ն ընկերությունն է։ MenQ Standard-ը MenQ ecosystem-ի operating standard-ն է՝ ինչպես ենք մտածում, որոշում, նախագծում, կառուցում, ստուգում, փաստաթղթավորում և պահպանում համակարգերը։

**EN:** MenQ Studio is the company. MenQ Standard is the operating standard of the MenQ ecosystem: how we think, decide, design, build, validate, document, and preserve systems.

## MenQ Design Platform readiness / MenQ Design Platform պատրաստականություն

**HY:** D-025-ի Parts 1–16 architecture-ը, canonical registry/schema/package implementation-ը, private `0.1.0-next.0` preview candidate-ը, deterministic release evidence-ը, երկու distinct consumers-ի M3/M4 evidence-ը և machine validation-ը GREEN են։ GREEN CI-ն ready-for-review, merge կամ lock authorization չէ։ Այդ գործողությունները պահանջում են explicit MenQ Owner decision։

**EN:** D-025 Parts 1–16 architecture, the canonical registry/schema/package implementation, the private `0.1.0-next.0` preview candidate, deterministic release evidence, M3/M4 evidence from two distinct consumers, and machine validation are GREEN. Green CI does not authorize ready-for-review, merge, or lock; those actions require an explicit MenQ Owner decision.

## Mandatory AI session startup / AI session-ի պարտադիր մեկնարկ

**HY:** Յուրաքանչյուր նոր MenQ Standard AI session մինչև substantive աշխատանք սկսելը պարտավոր է active branch/ref-ում enumerate անել և ամբողջությամբ կարդալ repository-ի բոլոր tracked `.md` ֆայլերը։ Պարտադիր օրենքը՝ [`foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`](foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md), որոշումը՝ [`D-026`](foundation/ai-collaboration/D-026-CANONICAL-SESSION-READ-LAW.md)։ Active PR-ի դեպքում նաև կարդացվում են metadata-ն, changed files-ը, diff-ը, review threads-ը և checks-ը։

**EN:** Before substantive work begins, every new MenQ Standard AI session must enumerate and completely read every tracked `.md` file on the active branch or ref. The mandatory law is [`foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`](foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md), with decision [`D-026`](foundation/ai-collaboration/D-026-CANONICAL-SESSION-READ-LAW.md). For an active PR, its metadata, changed files, diff, review threads, and checks are also required.

## Canonical navigation / Canonical նավիգացիա

- [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md) — stable project and AI context
- [`AI_WORKING_CONTEXT.md`](AI_WORKING_CONTEXT.md) — current working continuity
- [`COLLABORATION_STYLE.md`](COLLABORATION_STYLE.md) — communication mood and working style
- [`NEXT_CHAT_HANDOFF.md`](NEXT_CHAT_HANDOFF.md) — current continuation handoff
- [`DECISION_INDEX.md`](DECISION_INDEX.md) — active append-only decision registry
- [`DECISIONS.md`](DECISIONS.md) — historical `D-001–D-021` registry
- [`CHANGELOG.md`](CHANGELOG.md) — history
- [`ROADMAP.md`](ROADMAP.md) — future direction
- [`foundation/README.md`](foundation/README.md) — Foundation index
- [`platforms/design/PROJECT_CONTEXT.md`](platforms/design/PROJECT_CONTEXT.md) — Design Platform current state
- [`platforms/design/D-025_COMPLETENESS_AUDIT.md`](platforms/design/D-025_COMPLETENESS_AUDIT.md) — D-025 readiness audit
- [`platforms/design/D-025_DRAFT_PR_REVIEW_RECORD.md`](platforms/design/D-025_DRAFT_PR_REVIEW_RECORD.md) — PR #3 review record
- [`platforms/design/implementation/release/d-025-readiness-record.json`](platforms/design/implementation/release/d-025-readiness-record.json) — machine-readable readiness evidence
- [`foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`](foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md) — mandatory write integrity law

## Canonical rule / Canonical կանոն

**HY:** Չատերը workshop են։ Հաստատված architecture-ը և որոշումները պարտադիր տեղափոխվում են canonical documentation։ Tool success-ը verification evidence չէ։ AI-ն չի կարող Owner approval հորինել, PR merge անել կամ decision lock անել առանց explicit human authority-ի։

**EN:** Conversations are the workshop. Approved architecture and decisions must be transferred into canonical documentation. Tool success is not verification evidence. AI may not invent Owner approval, merge a PR, or lock a decision without explicit human authority.

<!-- END: MENQ_STANDARD_ROOT_README -->

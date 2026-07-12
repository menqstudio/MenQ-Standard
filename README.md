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
- **D-025 MenQ Design Platform Architecture v1:** Locked and GREEN / Locked և GREEN
- **D-026 Canonical Session Read Law:** Locked and machine-enforced / Locked և machine-enforced
- **D-025 implementation merge:** `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`
- **D-025 closure merge:** `9a833339b1d707d6cd8a792e031dd8ca2857d556`
- **D-025 lock merge:** `261f85e5b20d726a0ab1f05da84a4dc45a248873`
- **D-025 validated lock head:** `8ba2e987ff6dab2c25fda18744c7376953d0108f`
- **D-025 lock date:** 2026-07-13
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

## MenQ Design Platform status / MenQ Design Platform վիճակ

**HY:** D-025-ի Parts 1–16 architecture-ը, canonical registry/schema/package implementation-ը, private `0.1.0-next.0` preview candidate-ը, deterministic release evidence-ը, երկու distinct consumers-ի M3/M4 evidence-ը, post-merge closure-ը, lock evidence-ը և machine validation-ը GREEN են։ Owner-ը 2026-07-13-ին explicit հաստատել է lock-ը։ D-025 transaction-ը փակված է։

**EN:** D-025 Parts 1–16 architecture, canonical registry/schema/package implementation, the private `0.1.0-next.0` preview candidate, deterministic release evidence, M3/M4 evidence from two distinct consumers, post-merge closure, lock evidence, and machine validation are GREEN. On 2026-07-13, the Owner explicitly approved lock. The D-025 transaction is closed.

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
- [`platforms/design/D-025_POST_MERGE_CLOSURE_RECORD.md`](platforms/design/D-025_POST_MERGE_CLOSURE_RECORD.md) — closure evidence
- [`platforms/design/D-025_LOCK_RECORD.md`](platforms/design/D-025_LOCK_RECORD.md) — lock evidence
- [`platforms/design/D-025_FINAL_POST_LOCK_AUDIT.md`](platforms/design/D-025_FINAL_POST_LOCK_AUDIT.md) — final audit and transaction closure
- [`platforms/design/implementation/release/d-025-readiness-record.json`](platforms/design/implementation/release/d-025-readiness-record.json) — machine-readable lock evidence
- [`foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`](foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md) — mandatory write integrity law

## Canonical rule / Canonical կանոն

**HY:** Չատերը workshop են։ Հաստատված architecture-ը և որոշումները պարտադիր տեղափոխվում են canonical documentation։ Tool success-ը verification evidence չէ։ AI-ն չի կարող Owner approval հորինել, PR merge անել կամ decision lock անել առանց explicit human authority-ի։ Locked decision-ի փոփոխությունը պահանջում է governed change control։

**EN:** Conversations are the workshop. Approved architecture and decisions must be transferred into canonical documentation. Tool success is not verification evidence. AI may not invent Owner approval, merge a PR, or lock a decision without explicit human authority. Changes to a locked decision require governed change control.

<!-- END: MENQ_STANDARD_ROOT_README -->
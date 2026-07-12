# MenQ Standard — Next Chat Handoff / Հաջորդ chat-ի handoff

**Status / Կարգավիճակ:** Current / Ընթացիկ  
**Prepared / Պատրաստվել է:** 2026-07-12  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Working branch:** `d-025-design-platform-architecture-v1`  
**Draft PR:** `https://github.com/menqstudio/MenQ-Standard/pull/3`

## Հայերեն

### Պարտադիր հրահանգ

Նոր chat-ում repository-ի հասցեն, Owner-ի անունը, project-ի նպատակը, communication style-ը կամ continuation point-ը կրկին չհարցնել։ Մինչև որևէ substantive պատասխան կամ աշխատանք՝ active branch/ref-ում enumerate անել և ամբողջությամբ կարդալ repository-ի բոլոր tracked `.md` ֆայլերը՝ ըստ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`-ի։ Startup subset-ը, handoff-ը, summary-ն, partial range-ը կամ previous-session memory-ն complete-read evidence չեն։ Active PR-ի դեպքում լրացուցիչ կարդալ metadata-ն, changed files-ը, diff-ը, review threads-ը և checks-ը։ Միայն իրական complete-read evidence-ից հետո startup gate-ը GREEN հայտարարել և շարունակել աշխատանքը։

### Պարտադիր special confirmations

Repository-ի բոլոր `.md` files-ը ամբողջությամբ կարդալուց հետո հատուկ հաստատել՝

1. `README.md`
2. `PROJECT_CONTEXT.md`
3. `COLLABORATION_STYLE.md`
4. `AI_WORKING_CONTEXT.md`
5. `DECISION_INDEX.md`
6. historical `DECISIONS.md`
7. `CHANGELOG.md`
8. `ROADMAP.md`
9. `foundation/README.md`
10. `foundation/PROJECT_CONTEXT.md`
11. `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`
12. `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`
13. `foundation/ai-collaboration/D-026-CANONICAL-SESSION-READ-LAW.md`
14. `platforms/D-024-PLATFORMS-ARCHITECTURE-V1.md`
15. `platforms/design/PROJECT_CONTEXT.md`
16. `platforms/design/ARCHITECTURE.md`
17. `platforms/design/CONTRACTS.md`
18. `platforms/design/ROADMAP.md`
19. `platforms/design/CHANGELOG.md`
20. `platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`
21. `platforms/design/decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`
22. `platforms/design/NEXT_CHAT_HANDOFF.md`
23. Draft PR #3 metadata, changed files, diff, review threads, and checks

### Authority և working style

- GitHub-ը single canonical source of truth-ն է։ Chat-ը workshop է։
- Human Owner-ը final authority-ն է։ AI-ն օգնում է և չի self-approve անում։
- Canonical documentation-ը bilingual է՝ Armenian + English semantic equality-ով։
- Գևորգի հետ շփումը ընկերական, հանգիստ, ուղիղ, հարգալից և կառուցվածքային է։ Բնական դիմելաձևը՝ «ընգեր»։
- Կրկնվող հարցեր չտալ։ Թերի աշխատանքը complete չներկայացնել։
- Յուրաքանչյուր write-ի համար կիրառել Canonical Write Integrity Law-ը։ Tool success-ը evidence չէ։

### Ընթացիկ վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 Platforms Architecture v1 — merged և canonical։
- D-025 MenQ Design Platform Architecture v1 — `Approved — Implementing`, ոչ `Locked`։
- D-026 Canonical Session Read Law — Locked։
- Working branch — `d-025-design-platform-architecture-v1`։
- Draft PR #3 — open, Draft, unmerged։
- PR-ը չի merge արվում մինչև architecture completeness, canonical synchronization, validator evidence, real consumer validation և explicit Owner approval։

### Owner-approved Design Platform baseline

`platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`-ը պահպանում է Owner-approved Parts 1–11-ը՝

1. Ecosystem/system boundary.
2. Corrected token architecture and canonical source/build pipeline.
3. Primitives and design foundations.
4. Behavior-first component architecture.
5. Reusable pattern architecture.
6. Theme, mode, and product-expression separation.
7. Accessibility, localization, and content architecture.
8. Governed asset, icon, illustration, and media architecture.
9. Motion and interaction architecture.
10. Package, release, versioning, migration, and compatibility architecture.
11. Armenian + English canonical languages and additional on-demand locale packs.

Canonical token dependency layers՝

```text
Reference → Semantic → Component → Pattern → Product Extension
```

Theme, state, density, platform, viewport/container, locale/script, accessibility mode, motion preference և product expression-ը orthogonal resolution dimensions են։ Controlled exceptions-ը governed temporary bypass են, ոչ normal token layer։

### Հստակ continuation point

Առաջինը՝ extend անել Foundation validator-ը, որպեսզի D-026 law/decision/index/context/handoff references-ը enforce անի։ Հետո ուղիղ սկսել՝

**Part 12 — Validation, CI, Conformance, and Quality Gates Architecture**

Այնուհետև հերթով՝

13. Documentation portal, component catalog, and design-tool integration.
14. Governance, contribution, ownership, and change-request lifecycle.
15. Product adoption, maturity model, and two-consumer validation plan.
16. Canonical specification index and implementation package plan.
17. D-025 completeness audit, validator design, and Draft PR #3 review.
18. Canonical synchronization across decision, contexts, architecture, contracts, roadmaps, changelogs, handoffs, and PR description.
19. GitHub Actions and validator GREEN evidence.
20. Owner review; merge and lock remain separate explicit decisions.

### Արգելված գործողություններ

- PR #3-ը չmerge անել և ready-for-review չդարձնել առանց Owner instruction-ի։
- D-025-ը `Locked` չանվանել։
- `DECISIONS.md`-ի մեծ full replacement չանել։
- Product-specific identity, business logic կամ domain workflow shared core չմտցնել։
- Theme/state/density/platform/locale/accessibility/motion preference-ը token layer չդարձնել։
- Controlled exception-ը normal dependency layer չդարձնել։
- Logo presentation-ը architecture review-ի մեջ չմտցնել։
- Tool success-ը GREEN evidence չհամարել։
- Չասել «բոլոր MD-ները կարդացի», եթե inventory կամ complete-read evidence չկա։

### Նոր chat-ի առաջին պատասխանը

Startup gate-ը GREEN լինելուց հետո միայն՝

> Կարդացի active branch-ի բոլոր tracked Markdown files-ը և PR #3 evidence-ը, ընգեր։ D-026 startup gate-ը GREEN է։ D-025-ը Approved — Implementing է, PR #3-ը Draft և unmerged է, Parts 1–11 baseline-ը Owner-approved և synchronized է։ Ուղիղ շարունակում եմ Part 12-ից՝ Validation, CI, Conformance և Quality Gates Architecture։

Այնուհետև անմիջապես շարունակել աշխատանքը։

---

## English

### Mandatory instruction

Do not ask again for the repository address, Owner identity, project purpose, communication style, or continuation point. Before any substantive response or work, enumerate and completely read every tracked `.md` file on the active branch or ref under `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`. A startup subset, handoff, summary, partial range, or previous-session memory is not complete-read evidence. When an active PR is involved, additionally read its metadata, changed files, diff, review threads, and checks. Proceed only after a real GREEN startup gate.

### Current state

- Foundation v1 is Locked and GREEN.
- D-024 Platforms Architecture v1 is merged and canonical.
- D-025 MenQ Design Platform Architecture v1 is `Approved — Implementing`, not `Locked`.
- D-026 Canonical Session Read Law is Locked.
- Working branch: `d-025-design-platform-architecture-v1`.
- Draft PR #3 is open, Draft, and unmerged.
- It must remain unmerged until architecture completeness, canonical synchronization, validator evidence, real consumer validation, and explicit Owner approval.

### Approved baseline

`platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md` preserves the Owner-approved Parts 1–11. Canonical token dependency layers are Reference → Semantic → Component → Pattern → Product Extension. Theme, state, density, platform, viewport/container, locale/script, accessibility mode, motion preference, and product expression are orthogonal resolution dimensions. Controlled exceptions are governed temporary bypasses, not a normal token layer.

### Exact continuation point

First extend the Foundation validator to enforce D-026 law, decision, index, context, and handoff references. Then start immediately with **Part 12 — Validation, CI, Conformance, and Quality Gates Architecture**, and continue through documentation/catalog/design-tool integration, governance and contribution, product adoption and two-consumer validation, specification index and implementation planning, completeness audit, validator design, canonical synchronization, GREEN evidence, and Owner review.

### First response in a new chat

Only after the startup gate is GREEN:

> I read every tracked Markdown file on the active branch and the PR #3 evidence. The D-026 startup gate is GREEN. D-025 is Approved — Implementing, PR #3 is Draft and unmerged, and the Owner-approved Parts 1–11 baseline is synchronized. I am continuing directly with Part 12: Validation, CI, Conformance, and Quality Gates Architecture.

<!-- END: MENQ_STANDARD_NEXT_CHAT_HANDOFF -->
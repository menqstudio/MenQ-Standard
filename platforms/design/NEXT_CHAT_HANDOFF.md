# MenQ Design Platform — Next Chat Handoff / MenQ Design Platform — Հաջորդ chat-ի handoff

**Status / Կարգավիճակ:** Current / Ընթացիկ  
**Prepared / Պատրաստվել է:** 2026-07-12  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Working branch:** `d-025-design-platform-architecture-v1`  
**Draft PR:** `https://github.com/menqstudio/MenQ-Standard/pull/3`

## Հայերեն

### Պարտադիր մեկնարկ

Մինչև substantive աշխատանք՝ active branch/ref-ում enumerate և ամբողջությամբ կարդալ repository-ի բոլոր tracked `.md` files-ը՝ ըստ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`-ի։ Active PR-ի դեպքում կարդալ metadata, changed files, diff, review threads և checks։

### Ընթացիկ վիճակ

- Foundation v1 — GREEN և Locked։
- D-024 — merged և canonical։
- D-025 — `Approved — Implementing`, ոչ `Locked`։
- D-026 — Locked և machine-enforced։
- Draft PR #3 — open, Draft և unmerged։
- Parts 1–16 architecture set-ը canonical է։
- `D-025_COMPLETENESS_AUDIT.md` և `D-025_DRAFT_PR_REVIEW_RECORD.md` canonical են։
- Architecture verdict-ը GREEN է։
- Implementation/lock readiness-ը YELLOW է։
- D-025-aware Platforms validator-ը GREEN evidence է տվել։

### Architecture invariants

- Shared core-ը product-neutral է։
- Canonical dependency model-ը՝ Reference → Semantic → Component → Pattern → Product Extension։
- Generated output-ը source of truth չէ։
- Armenian և English canonical languages են։
- Merge-ը և lock-ը միայն explicit Owner decisions են։

### Շարունակելու ճշգրիտ կետը

## Implementation Phase A

1. Ստեղծել canonical specification registry-ի իրական machine-readable implementation-ը։
2. Սահմանել schemas, canonical IDs, ownership records և dependency graph։
3. Ստեղծել package/workspace skeleton-ը՝ contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales և validation boundaries-ով։
4. Ընտրել երկու distinct real consumer candidates և bounded pilot scopes։
5. Չփոխել YELLOW implementation verdict-ը մինչև իրական package/consumer evidence։

### Արգելված գործողություններ

- PR #3-ը չmerge անել և ready-for-review չդարձնել առանց Owner instruction-ի։
- D-025-ը `Locked` չանվանել։
- Product-specific identity, logic կամ workflows shared core չմտցնել։
- Generated artifacts-ը canonical source չհամարել։
- Fake consumer կամ implementation evidence չստեղծել։

---

## English

### Mandatory startup

Before substantive work, enumerate and completely read every tracked `.md` file on the active branch/ref under `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`. For the active PR, read metadata, changed files, diff, review threads, and checks.

### Current state

- Foundation v1 is GREEN and Locked.
- D-024 is merged and canonical.
- D-025 is `Approved — Implementing`, not `Locked`.
- D-026 is Locked and machine-enforced.
- Draft PR #3 is open, Draft, and unmerged.
- The Parts 1–16 architecture set is canonical.
- `D-025_COMPLETENESS_AUDIT.md` and `D-025_DRAFT_PR_REVIEW_RECORD.md` are canonical.
- Architecture is GREEN.
- Implementation and lock readiness remain YELLOW.
- The D-025-aware Platforms validator has produced GREEN evidence.

### Architecture invariants

- Shared core is product-neutral.
- Canonical dependency model: Reference → Semantic → Component → Pattern → Product Extension.
- Generated output is not a source of truth.
- Armenian and English are canonical languages.
- Merge and lock require explicit Owner decisions.

### Exact continuation point

## Implementation Phase A

1. Implement the machine-readable canonical specification registry.
2. Define schemas, canonical IDs, ownership records, and the dependency graph.
3. Create the package/workspace skeleton for contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales, and validation.
4. Select two distinct real consumer candidates and bounded pilot scopes.
5. Preserve the YELLOW implementation verdict until real package and consumer evidence exists.

### Prohibited actions

- Do not merge PR #3 or mark it ready for review without Owner instruction.
- Do not describe D-025 as Locked.
- Do not move product-specific identity, logic, or workflows into shared core.
- Do not treat generated artifacts as canonical source.
- Do not fabricate implementation or consumer evidence.

<!-- END: MENQ_DESIGN_PLATFORM_NEXT_CHAT_HANDOFF -->

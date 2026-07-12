# MenQ Standard — Next Chat Handoff / Հաջորդ chat-ի handoff

**Status / Կարգավիճակ:** Current / Ընթացիկ  
**Prepared / Պատրաստվել է:** 2026-07-12  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Default branch:** `main`

## 1. Mandatory instruction to the next AI / Հաջորդ AI-ի պարտադիր հրահանգ

**HY:** Մի հարցրու repository-ի հասցեն, project-ի նպատակը, Owner-ի անունը, communication style-ը կամ որտեղից շարունակել։ Դրանք canonical files-ում կան։ Նախ կարդա startup set-ը, հետո ուղիղ ստուգիր validator evidence-ը և շարունակիր այստեղ նշված next action-ից։

**EN:** Do not ask again for the repository address, project purpose, Owner identity, communication style, or where to continue. These are documented canonically. Read the startup set first, then directly verify validator evidence and continue from the next action defined here.

## 2. Required startup read order / Պարտադիր կարդալու հերթականություն

1. `README.md`
2. `PROJECT_CONTEXT.md`
3. `COLLABORATION_STYLE.md`
4. `AI_WORKING_CONTEXT.md`
5. `DECISION_INDEX.md`
6. `DECISIONS.md`
7. `CHANGELOG.md`
8. `FOUNDATION_V1_REMEDIATION_CHANGELOG.md`
9. `ROADMAP.md`
10. `foundation/README.md`
11. `foundation/PROJECT_CONTEXT.md`
12. `foundation/FOUNDATION_V1_INTEGRITY_AUDIT.md`
13. `foundation/FOUNDATION_V1_REAUDIT.md`
14. `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`
15. the relevant Foundation chapter and its `PROJECT_CONTEXT.md`

## 3. Project identity / Project-ի ինքնություն

- MenQ Studio is the company.
- MenQ Standard is the operating standard of the MenQ ecosystem.
- Canonical repository is the single source of truth.
- Chat is a workshop, not the canonical source.
- Everything important is bilingual Armenian + English with equal semantic completeness.
- Approved ecosystem-level ideas must become canonical documentation.
- Human authority is final; AI assists and may not self-approve.

Human–AI rule:

> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

## 4. Communication with Gevorg / Գևորգի հետ շփում

Canonical source: `COLLABORATION_STYLE.md`.

- Address naturally as «ընգեր» in Armenian working conversation.
- Be friendly, calm, direct, respectful, concise, and structured.
- Avoid bureaucratic or unnecessarily formal language.
- Do not repeat questions already answered in the repository or conversation.
- Challenge weak architecture, but preserve Owner authority.
- Do not claim partial work is complete.
- Do not promise background work without a real scheduling/tool mechanism.
- Prefer complete systems, reusable standards, and complete packages/ZIPs over fragmented delivery.
- When an error occurs, acknowledge it, stop, restore, verify, and report the real state.

## 5. Locked Foundation state / Foundation-ի locked վիճակ

All seven Foundation chapters are built and locked:

1. Philosophy
2. Principles
3. Terminology v1, Living Standard
4. Governance v1
5. Decision System v1
6. Documentation Standard v1
7. AI Collaboration Standard v1

Related decisions:

- `D-017` — Principles
- `D-018` — Terminology
- `D-019` — Governance
- `D-020` — Decision System
- `D-021` — Documentation Standard
- `D-022` — Canonical Write Integrity Law
- `D-023` — AI Collaboration Standard v1

## 6. Decision registry architecture / Որոշումների registry architecture

- `DECISIONS.md` is intentionally preserved as the historical `D-001–D-021` registry.
- Two attempts to rewrite the large file through the contents API caused truncation.
- Both bad commits were removed by restoring `main` to the last complete commit.
- Do not attempt another large full-file rewrite of `DECISIONS.md`.
- `DECISION_INDEX.md` is now the active append-only registry.
- Dedicated records preserve `D-022` and `D-023`.
- Future decisions: create a dedicated decision file, verify it, append one entry to `DECISION_INDEX.md`, then synchronize context/changelog/index references.

## 7. Canonical write law / Canonical write-ի օրենք

Every canonical write follows:

```text
READ COMPLETE SOURCE
→ PRESERVE SHA
→ WRITE
→ RE-READ BEGINNING
→ RE-READ ENDING
→ VERIFY CONTENT AND SYNCHRONIZATION
→ GREEN
```

Tool success is not evidence. On RED: stop, restore, re-verify, and report the incident.

## 8. Original audit result / Սկզբնական audit result

`foundation/FOUNDATION_V1_INTEGRITY_AUDIT.md` recorded RED findings:

- `R-01` missing chapter contexts
- `R-02` stale Foundation context
- `R-03` stale AI working context
- `R-04` root decision registry gap
- `R-05` bilingual parity defects
- `R-06` metadata inconsistency
- `R-07` missing integrity automation

## 9. Remediation already applied / Արդեն կիրառված ուղղումներ

### Structural completeness

Created missing chapter contexts:

- `foundation/philosophy/PROJECT_CONTEXT.md`
- `foundation/principles/PROJECT_CONTEXT.md`
- `foundation/terminology/PROJECT_CONTEXT.md`
- `foundation/governance/PROJECT_CONTEXT.md`
- `foundation/decision-system/PROJECT_CONTEXT.md`
- `foundation/documentation/PROJECT_CONTEXT.md`

AI Collaboration already had `foundation/ai-collaboration/PROJECT_CONTEXT.md`.

### Context synchronization

Updated and verified:

- `foundation/PROJECT_CONTEXT.md`
- `AI_WORKING_CONTEXT.md`
- `README.md`
- `foundation/README.md`
- `ROADMAP.md`

### Decision traceability

Created:

- `DECISION_INDEX.md`

### Bilingual parity controls

Created:

- `foundation/documentation/BILINGUAL_PARITY_ADDENDUM.md`
- `foundation/ai-collaboration/BILINGUAL_PARITY_ADDENDUM.md`

These are interpretive addenda and do not change approved meaning.

### Metadata normalization

Created:

- `foundation/FOUNDATION_NORMATIVE_METADATA_REGISTRY.md`

This supplies missing legacy metadata without rewriting locked chapter history.

### Integrity automation

Created:

- `scripts/validate_foundation.py`
- `.github/workflows/foundation-integrity.yml`

### Communication standard

Created:

- `COLLABORATION_STYLE.md`

### Change and audit records

Created:

- `FOUNDATION_V1_REMEDIATION_CHANGELOG.md`
- `foundation/FOUNDATION_V1_REAUDIT.md`

## 10. Current verified state / Ընթացիկ verified վիճակ

- Repository-side remediation files exist.
- New and updated canonical files were re-read after writing.
- Critical ending markers were confirmed for the parent contexts and communication style.
- Original audit remains preserved as historical RED evidence.
- Re-audit status is YELLOW, not GREEN.

Why YELLOW:

- GitHub Actions did not return workflow run/status evidence in the current session.
- A local clone attempt could not run because the execution environment could not resolve `github.com` over DNS.
- Therefore validator execution success has not been proven.

Do not call Foundation v1 release-ready until real GREEN validator evidence exists.

## 11. Exact next action / Հստակ հաջորդ քայլ

Perform one of these:

### Option A — GitHub Actions

1. Inspect the `Foundation Integrity` workflow on the latest `main` commit.
2. If it ran, read the job result and logs.
3. If GREEN, record the evidence canonically.
4. If RED, fix only the reported defects and re-run.

### Option B — Local clone

Run:

```bash
python scripts/validate_foundation.py
```

On Windows PowerShell:

```powershell
python .\scripts\validate_foundation.py
```

Expected successful output:

```text
FOUNDATION VALIDATION: GREEN
Validated 7 Foundation chapters and root controls.
```

## 12. After validator GREEN / Validator GREEN-ից հետո

1. Create a final GREEN validation record, preserving the YELLOW re-audit history.
2. Synchronize `README.md`, `AI_WORKING_CONTEXT.md`, `ROADMAP.md`, and the changelog with the GREEN evidence.
3. Produce the complete Foundation v1 repository ZIP snapshot.
4. Include a root README, snapshot date/version, file manifest, and dependency/missing-file verification.
5. Keep GitHub as canonical; ZIP is only a delivery snapshot.
6. Then begin Platforms architecture only through a formal Decision System proposal and Owner approval.

## 13. Do not do / Չանել

- Do not rewrite `DECISIONS.md` as a large replacement.
- Do not delete the original RED audit or integrity incident history.
- Do not call YELLOW GREEN without execution evidence.
- Do not change locked Foundation meaning during editorial remediation.
- Do not ask Gevorg to repeat known context.
- Do not start Platforms architecture before Foundation validation is GREEN unless the Owner explicitly changes priority.

## 14. Immediate response style for the new chat / Նոր chat-ի առաջին պատասխանը

After reading the repository, respond briefly in Armenian:

> Կարդացի canonical handoff-ը, ընգեր։ Foundation remediation-ը կիրառված է, release gate-ը YELLOW է միայն validator execution evidence-ի պատճառով։ Հիմա ստուգում եմ Foundation Integrity workflow-ը կամ validator result-ը, հետո միայն GREEN/RED verdict կտամ։

Then perform the verification immediately. Do not ask for confirmation.

<!-- END: MENQ_STANDARD_NEXT_CHAT_HANDOFF -->
# MenQ Standard — Next Chat Handoff / Հաջորդ chat-ի handoff

**Status / Կարգավիճակ:** Current / Ընթացիկ  
**Prepared / Պատրաստվել է:** 2026-07-12  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Branch:** `main`

## 1. Mandatory instruction / Պարտադիր հրահանգ

**HY:** Մի հարցրու repository-ի հասցեն, Owner-ի անունը, project-ի նպատակը, communication style-ը կամ որտեղից շարունակել։ Նախ կարդա canonical startup set-ը և ուղիղ շարունակիր validator verification-ից։  
**EN:** Do not ask again for the repository address, Owner identity, project purpose, communication style, or continuation point. Read the canonical startup set and continue directly from validator verification.

## 2. Startup read order / Կարդալու հերթականություն

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
15. relevant chapter + its `PROJECT_CONTEXT.md`

## 3. Identity and authority / Ինքնություն և authority

- MenQ Studio is the company.
- MenQ Standard is the MenQ ecosystem operating standard.
- GitHub is the single canonical source of truth; chat is the workshop.
- Important documentation is bilingual Armenian + English with equal meaning.
- Human authority is final; AI assists and may not self-approve.

> Մարդը միտք է բերում։ AI-ն օգնում է։ Մարդը որոշում է։ Ստանդարտը պահպանում է։  
> Humans bring ideas. AI assists. Humans decide. Standards preserve.

## 4. Communication with Gevorg / Գևորգի հետ շփում

Canonical source: `COLLABORATION_STYLE.md`.

- Armenian natural address: «ընգեր».
- Friendly, calm, direct, respectful, concise, structured, non-bureaucratic.
- Do not repeat questions answered in repository or conversation.
- Challenge weak architecture; preserve Owner authority.
- Never present partial work as complete.
- Do not promise background work without a real tool.
- Prefer systems, reusable standards, complete packages, and ZIP snapshots.
- On error: acknowledge, stop, restore, verify, report real state.

## 5. Locked Foundation state / Foundation-ի locked վիճակ

All seven chapters are Locked v1:

1. Philosophy
2. Principles (`D-017`)
3. Terminology, Living Standard (`D-018`)
4. Governance (`D-019`)
5. Decision System (`D-020`)
6. Documentation Standard (`D-021`)
7. AI Collaboration (`D-023`)

Canonical Write Integrity Law is locked as `D-022`.

## 6. Decision registry architecture / Decision registry architecture

- `DECISIONS.md` intentionally preserves historical `D-001–D-021`.
- Two full contents-API rewrites truncated it; both bad commits were removed by restoring `main`.
- Never perform another large full replacement of `DECISIONS.md`.
- `DECISION_INDEX.md` is the active append-only registry.
- Dedicated files preserve `D-022` and `D-023`.
- Future decision flow: dedicated file → verify → append index entry → sync context/changelog/index references.

## 7. Canonical write law / Canonical write-ի օրենք

```text
READ COMPLETE SOURCE
→ PRESERVE SHA
→ WRITE
→ RE-READ BEGINNING
→ RE-READ ENDING
→ VERIFY CONTENT AND SYNCHRONIZATION
→ GREEN
```

Tool success is not evidence. On RED: stop, restore, re-verify, report incident.

## 8. Original audit / Սկզբնական audit

`foundation/FOUNDATION_V1_INTEGRITY_AUDIT.md` recorded:

- `R-01` missing chapter contexts
- `R-02` stale Foundation context
- `R-03` stale AI working context
- `R-04` decision registry gap
- `R-05` bilingual parity defects
- `R-06` metadata inconsistency
- `R-07` missing integrity automation

## 9. Remediation applied / Կիրառված ուղղումներ

Created chapter contexts:

- `foundation/philosophy/PROJECT_CONTEXT.md`
- `foundation/principles/PROJECT_CONTEXT.md`
- `foundation/terminology/PROJECT_CONTEXT.md`
- `foundation/governance/PROJECT_CONTEXT.md`
- `foundation/decision-system/PROJECT_CONTEXT.md`
- `foundation/documentation/PROJECT_CONTEXT.md`
- AI Collaboration context already existed.

Synchronized:

- `README.md`
- `PROJECT_CONTEXT.md`
- `AI_WORKING_CONTEXT.md`
- `ROADMAP.md`
- `foundation/README.md`
- `foundation/PROJECT_CONTEXT.md`

Created controls:

- `DECISION_INDEX.md`
- `foundation/documentation/BILINGUAL_PARITY_ADDENDUM.md`
- `foundation/ai-collaboration/BILINGUAL_PARITY_ADDENDUM.md`
- `foundation/FOUNDATION_NORMATIVE_METADATA_REGISTRY.md`
- `scripts/validate_foundation.py`
- `.github/workflows/foundation-integrity.yml`
- `COLLABORATION_STYLE.md`
- `FOUNDATION_V1_REMEDIATION_CHANGELOG.md`
- `foundation/FOUNDATION_V1_REAUDIT.md`

## 10. Current gate / Ընթացիկ gate

**Status: YELLOW.** Repository-side fixes are applied, but validator execution GREEN evidence is missing.

Evidence status:

- New/updated files were re-read after writes.
- Critical markers were checked.
- GitHub Actions returned no workflow run/status in the current session.
- Local clone validation failed because the execution environment could not resolve `github.com` over DNS.
- This is not validator success or failure evidence.

Do not call Foundation v1 release-ready until actual GREEN execution evidence exists.

## 11. Exact next action / Հստակ հաջորդ քայլ

Immediately do one:

### GitHub Actions

Inspect the latest `Foundation Integrity` workflow run, result, and logs.

### Local clone

```bash
python scripts/validate_foundation.py
```

PowerShell:

```powershell
python .\scripts\validate_foundation.py
```

Expected GREEN:

```text
FOUNDATION VALIDATION: GREEN
Validated 7 Foundation chapters and root controls.
```

On RED, fix only reported defects and run again. Do not ask for confirmation.

## 12. After validator GREEN / Validator GREEN-ից հետո

1. Create a final GREEN validation record; preserve RED and YELLOW history.
2. Synchronize README, contexts, roadmap, and changelog with evidence.
3. Create complete Foundation v1 repository ZIP snapshot with README, version/date, manifest, and missing-file verification.
4. Keep GitHub canonical; ZIP is a delivery snapshot.
5. Then begin Platforms architecture only through formal Decision System proposal and Owner approval.

## 13. Prohibited next-chat actions / Արգելված գործողություններ

- Do not rewrite large `DECISIONS.md`.
- Do not delete audit or incident history.
- Do not rename YELLOW as GREEN without execution evidence.
- Do not change locked Foundation meaning during remediation.
- Do not ask Gevorg to repeat known context.
- Do not begin Platforms architecture before validation GREEN unless Owner explicitly changes priority.

## 14. First response in the new chat / Նոր chat-ի առաջին պատասխանը

> Կարդացի canonical handoff-ը, ընգեր։ Foundation remediation-ը կիրառված է, release gate-ը YELLOW է միայն validator execution evidence-ի պատճառով։ Հիմա ստուգում եմ Foundation Integrity workflow-ը կամ validator result-ը, հետո միայն GREEN/RED verdict կտամ։

Then execute verification immediately.

<!-- END: MENQ_STANDARD_NEXT_CHAT_HANDOFF -->
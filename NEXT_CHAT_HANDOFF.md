# MenQ Standard — Next Chat Handoff / Հաջորդ chat-ի handoff

**Status / Կարգավիճակ:** Current / Ընթացիկ  
**Prepared / Պատրաստվել է:** 2026-10-09  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Canonical ref:** `main`

## Հայերեն

### Պարտադիր մեկնարկ

Մինչև substantive աշխատանք՝ ամբողջությամբ կարդալ session-read core-ը և աշխատանքի directory-ի area-ն՝ ըստ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`-ի (`D-026`, `D-028`)։

### Ինչն է ճիշտ հիմա

Ընթացիկ վիճակի միակ ցանկը [`README.md`](README.md)-ի `Status` բաժինն է։ 2026-10-07-ի handoff-ից հետո [`CHANGELOG.md`](CHANGELOG.md)-ում գրանցվել են՝ `CR-0004`–`CR-0011` (2026-10-08), `D-028`-ի առաջարկը և հաստատումը (pull request #29, 2026-10-09), validator-ների content ստուգումները և թեստերը (2026-10-09), և root փաստաթղթերի այս համաժամեցումը (2026-10-09)։ Audit-ի remediation-ի 1–6 փուլերը գրանցված են ավարտված։

### Ինչն է բաց

1. D-025-ի իրական consumer-ի պարտավորությունը․ առաջինը MenQ Webpage-ն է, երկրորդը ընտրում է Owner-ը։
2. D-028-ի consumer repository-ների պահանջը adoption մեխանիզմ չունի․ դա հետագա որոշում է։
3. Area-ները բայթերի սահման չունեն (ամենամեծը՝ `platforms/design`, ամբողջ core-ից մեծ)․ հարցը Owner-ինն է։
4. `CR-0004`–`CR-0011`-ը իրականացված են․ դրանց record-ները փակվում են առանձին pull request-ով։
5. D-025 readiness record-ի վերին մակարդակի դաշտերը դեռ ցույց են տալիս փոխարինված M3/M4-ը․ Platforms validator-ը տպում է `KNOWN INCONSISTENCY`։ Record-ը ուղղելը Owner-ի որոշում է։
6. D-027-ը Locked դառնալու համար՝ D-025 token source-ի mapping, առաջին իրական consumer, ru locale pack։ Part 13-ը backlog-ում է։
7. Այս համաժամեցումը և `DECISIONS.md`-ի `D-009`-ի տակի նշումը Owner-ի հաստատում չունեն, մինչև Owner-ը merge չանի դրանց pull request-ը։

### Առաջին քայլը

1. `git log -1` և գործարկել `scripts/validate_foundation.py`, `scripts/validate_platforms.py`, `scripts/check_session_read_budget.py`։
2. Ստուգել՝ merge եղե՞լ են այս համաժամեցման և CR-ների փակման pull request-ները, և ըստ դրա թարմացնել այս ցանկը։
3. Հետո Owner-ը ընտրում է հաջորդ priority-ն՝ առանձին decision transaction-ով։

### Արգելված գործողություններ

- D-025-ի locked boundary-ն silently չփոխել։
- Historical evidence-ը չջնջել կամ վերագրել։
- Generated artifacts-ը canonical source չհամարել։

---

## English

### Mandatory startup

Before substantive work, read in full the session-read core and the area of the working directory, under `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md` (`D-026`, `D-028`).

### What is true now

The one list of the current state is the `Status` section of [`README.md`](README.md). Since the handoff of 2026-10-07, [`CHANGELOG.md`](CHANGELOG.md) records: `CR-0004`–`CR-0011` (2026-10-08), the proposal and approval of `D-028` (pull request #29, 2026-10-09), the validators' content checks and tests (2026-10-09), and this synchronisation of the root documents (2026-10-09). Remediation phases 1–6 of the audit are recorded complete.

### What is open

1. The real-consumer obligation of D-025: MenQ Webpage is the first, and the Owner selects the second.
2. D-028's requirement of consumer repositories has no adoption mechanism; that is a later decision.
3. Areas have no byte ceiling (the largest is `platforms/design`, larger than the whole core); the question is the Owner's.
4. `CR-0004`–`CR-0011` are implemented; their records are being closed in a separate pull request.
5. The top-level fields of the D-025 readiness record still show the superseded M3/M4; the Platforms validator prints `KNOWN INCONSISTENCY`. Correcting the record is an Owner decision.
6. For D-027 to become Locked: the mapping to the D-025 token source, the first real consumer, the ru locale pack. Part 13 is in the backlog.
7. This synchronisation and the note under `D-009` in `DECISIONS.md` have no Owner approval until the Owner merges their pull request.

### First step

1. `git log -1`, then run `scripts/validate_foundation.py`, `scripts/validate_platforms.py` and `scripts/check_session_read_budget.py`.
2. Check whether the pull requests of this synchronisation and of the CR closure have merged, and update this list accordingly.
3. Then the Owner selects the next priority through a separate decision transaction.

### Prohibited actions

- Do not silently change the D-025 locked boundary.
- Do not delete or rewrite historical evidence.
- Do not treat generated artifacts as canonical source.

<!-- END: MENQ_STANDARD_NEXT_CHAT_HANDOFF -->

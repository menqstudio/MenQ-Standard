# D-025 Evidence Correction Record / D-025 ապացույցի ուղղման գրառում

**Status / Կարգավիճակ:** Recorded — D-025 remains Locked; real-consumer obligation open / Գրանցված — D-025-ը մնում է Locked, իրական consumer-ի պարտավորությունը բաց է  
**Date / Ամսաթիվ:** 2026-10-07  
**Decision / Որոշում:** `D-025`  
**Owner / Պատասխանատու:** MenQ Owner  
**Approver / Հաստատող:** Gevorg Ohanyan, MenQ Owner — decided in the project conversation on 2026-10-07  
**Source / Աղբյուր:** 2026-10-07 zero-trust audit, phase 6

## Հայերեն

### Ինչն էր սխալ

1. **Ժամկետանց artifact։** D-025-ի lock evidence-ը հղվում էր `menq-design-platform-0.1.0-next.0` workflow artifact-ին (`artifactId 8265108086`, run `29210874292`)։ Workflow-ը այն պահում էր 30 օր, և 2026-10-07-ին artifact-ը այլևս գոյություն չունի (GitHub API՝ 404)։ `d-025-readiness-record.json`-ում `artifactExpired: false`-ը այլևս ճիշտ չէ։
2. **Consumer evidence-ը self-attested էր։** `design-catalog` և `release-console` consumer-ները repository-ի ներսի reference build-եր են։ Նրանց `build.mjs`-ը ինքն է գրում `verdict: "GREEN"`, `passed: true` check-երը, `maturity: "M3"`/`"M4"` և `productionEquivalent: true` արժեքները, իսկ `validate_consumers.py`-ը ստուգում է այդ հայտարարված արժեքները, ոչ թե անկախ վարքագիծը։ Maturity model-ի համաձայն՝ «Maturity is an evidence-backed verdict, not self-attestation»։ Ուստի M3/M4-ը ապացուցված չէ։

### Ուղղում

1. **Մշտական release evidence։** Preview bundle-ը վերակառուցվեց deterministic կրկնակի build-ով և հրապարակվեց որպես մշտական GitHub pre-release՝ [`design-platform-v0.1.0-next.0`](https://github.com/menqstudio/MenQ-Standard/releases/tag/design-platform-v0.1.0-next.0), commit `3793b3ce01a98db051894917595624881972adad`, asset `menq-design-platform-0.1.0-next.0.zip`, SHA-256 `396653856650dc2ec50af230e851e4c90f4215606be1cbec999a3b5d4a83e486`։ Այն byte-for-byte նույնը չէ ժամկետանց artifact-ի հետ, քանի որ կառուցված է ավելի ուշ commit-ից։
2. **Consumer-ների վերագնահատում։** Երկու consumer-ն էլ վերագնահատվում են **M2 — Pilot**՝ իրական սահմանափակ flow, որը preview build-ը օգտագործում է public API-ով։ M3/M4 պնդումները պատմական են և այլևս որպես evidence չեն օգտագործվում։
3. **Բաց պարտավորություն։** D-025-ը մնում է `Locked`՝ Owner-ի որոշմամբ։ Two-real-consumer պայմանը վերականգնելու համար MenQ Webpage-ը (`menqstudio/Webpage`) դառնում է առաջին իրական consumer-ը՝ անկախ, չհայտարարված evidence-ով։ Երկրորդ իրական consumer-ը ընտրում է Owner-ը։
4. **Պատմությունը պահպանվում է։** Lock, closure և final audit գրառումները չեն վերագրվում. դրանք ստանում են ուղղման ծանուցում, իսկ readiness record-ը ստանում է `evidenceCorrections` բաժին։

## English

### What was wrong

1. **Expired artifact.** D-025's lock evidence pointed to the `menq-design-platform-0.1.0-next.0` workflow artifact (`artifactId 8265108086`, run `29210874292`). The workflow kept it for 30 days, and on 2026-10-07 the artifact no longer exists (GitHub API: 404). `artifactExpired: false` in `d-025-readiness-record.json` is no longer true.
2. **Consumer evidence was self-attested.** The `design-catalog` and `release-console` consumers are in-repository reference builds. Their `build.mjs` writes the `verdict: "GREEN"`, `passed: true` checks, `maturity: "M3"`/`"M4"` and `productionEquivalent: true` values itself, and `validate_consumers.py` checks those declared values, not independent behavior. Per the maturity model, "Maturity is an evidence-backed verdict, not self-attestation". M3/M4 is therefore not evidenced.

### Correction

1. **Permanent release evidence.** The preview bundle was rebuilt with a deterministic double build and published as a permanent GitHub pre-release: [`design-platform-v0.1.0-next.0`](https://github.com/menqstudio/MenQ-Standard/releases/tag/design-platform-v0.1.0-next.0), commit `3793b3ce01a98db051894917595624881972adad`, asset `menq-design-platform-0.1.0-next.0.zip`, SHA-256 `396653856650dc2ec50af230e851e4c90f4215606be1cbec999a3b5d4a83e486`. It is not byte-identical to the expired artifact because it was built from a later commit.
2. **Consumer re-grade.** Both consumers are re-graded to **M2 — Pilot**: a real bounded flow that uses the preview build through the public API. The M3/M4 claims are historical and are no longer used as evidence.
3. **Open obligation.** D-025 remains `Locked` by Owner decision. To restore the two-real-consumer condition, MenQ Webpage (`menqstudio/Webpage`) becomes the first real consumer, with independent, non-self-declared evidence. The Owner selects the second real consumer.
4. **History is preserved.** The lock, closure and final-audit records are not rewritten; they receive a correction notice, and the readiness record receives an `evidenceCorrections` section.

<!-- END: D-025_EVIDENCE_CORRECTION_RECORD -->

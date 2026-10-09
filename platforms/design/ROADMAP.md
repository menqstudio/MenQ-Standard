# MenQ Design Platform — Roadmap / MenQ Design Platform — Ճանապարհային քարտեզ

**Status / Կարգավիճակ:** D-025 Locked / D-025 Locked  
**Owner / Պատասխանատու:** MenQ Owner  
**Last synchronized / Վերջին համաժամեցում:** 2026-10-09 (`CR-0012`)

## Rule / Կանոն

**HY:** Roadmap item-ը mandatory authority չի ստեղծում։ Locked architecture-ի փոփոխությունը պահանջում է governed change request, evidence, validation և explicit Owner approval։  
**EN:** A roadmap item does not create authority. Changes to locked architecture require a governed change request, evidence, validation, and explicit Owner approval.

## Completed / Ավարտված

- [x] Parts 1–16 canonical architecture set. / Parts 1–16 canonical architecture set։
- [x] Product-neutral shared core and dependency model. / Product-neutral shared core և dependency model։
- [x] Registry, schemas, ownership, dependency graph, and ten package boundaries. / Registry, schemas, ownership, dependency graph և տասը package boundaries։
- [x] Private `0.1.0-next.0` preview candidate. / Private `0.1.0-next.0` preview candidate։
- [x] Deterministic build, checksums, public API, compatibility, migration, rollback, and release evidence. / Deterministic build, checksums, public API, compatibility, migration, rollback և release evidence։
- [x] PR #3 implementation merge. / PR #3 implementation merge։
- [x] PR #4 post-merge closure. / PR #4 post-merge closure։
- [x] PR #5 lock transaction. / PR #5 lock transaction։
- [x] Exact merge-tree equivalence evidence. / Merge-tree-ի ճշգրիտ համարժեքության evidence։
- [x] Explicit Owner lock approval. / Owner-ի explicit lock approval։
- [x] D-025 Locked and GREEN, as recorded on 2026-07-13. `Locked` stands by Owner decision; the two-consumer part of that GREEN was corrected on 2026-10-07 (next section). / D-025-ը Locked և GREEN է՝ ինչպես գրանցվել է 2026-07-13-ին։ `Locked`-ը մնում է Owner-ի որոշմամբ. այդ GREEN-ի երկու consumer-ի մասը ուղղվել է 2026-10-07-ին (հաջորդ բաժին)։
- [x] Final post-lock audit and continuity synchronization. / Վերջնական post-lock audit և continuity-ի համաժամեցում։
- [x] D-027 brand expression layer and Bro product extension brought under governance (PR #8, 2026-10-07). The decision is `Approved — Implementing`; the layer's lifecycle is Draft. / D-027 brand expression շերտը և Bro product extension-ը բերվեցին governance-ի ներքո (PR #8, 2026-10-07)։ Որոշումը `Approved — Implementing` է, շերտի lifecycle-ը՝ Draft։
- [x] D-025 evidence correction and the permanent `design-platform-v0.1.0-next.0` release (`CR-0001`, closed). / D-025 evidence-ի ուղղում և մշտական `design-platform-v0.1.0-next.0` release (`CR-0001`, փակված)։
- [x] Part 14 governance implemented and Locked on 2026-10-07 ([`governance/`](governance/README.md), `CR-0002`, closed). / Part 14 governance-ը իրականացված և Locked է 2026-10-07-ից (`CR-0002`, փակված)։
- [x] `tokens.vars.css` consumption artifact (`CR-0003`, closed). / `tokens.vars.css` consumption artifact (`CR-0003`, փակված)։
- [x] Neon logo high-resolution master (`CR-0004`, closed by `CR-0012`). / Neon լոգոյի բարձր լուծաչափի master (`CR-0004`, փակված `CR-0012`-ով)։

## Recorded as completed on 2026-07-13, then corrected / Գրանցվել են որպես ավարտված 2026-07-13-ին, հետո ուղղվել

**EN:** These three items were ticked until 2026-10-09. The 2026-10-07 evidence correction ([`D-025_EVIDENCE_CORRECTION_RECORD.md`](D-025_EVIDENCE_CORRECTION_RECORD.md)) withdrew them as evidence: both consumers are in-repository pilots at M2 and their verdicts were self-attested.

**HY:** Այս երեք կետերը նշված էին որպես ավարտված մինչև 2026-10-09-ը։ 2026-10-07-ի evidence-ի ուղղումը դրանք հանեց որպես evidence. երկու consumer-ն էլ repository-ի ներսի M2 pilot են, և նրանց verdict-ը self-attested էր։

- [ ] MenQ Design Catalog M3 consumer validation — withdrawn; the consumer is an M2 pilot. / MenQ Design Catalog M3 consumer-ի validation — հանված է. consumer-ը M2 pilot է։
- [ ] MenQ Release Evidence Console M4 operational validation — withdrawn; the consumer is an M2 pilot. / MenQ Release Evidence Console M4 operational validation — հանված է. consumer-ը M2 pilot է։
- [ ] Cross-consumer validation and quality/adoption evidence — not evidence of two real consumers; reopened as Current item 1. / Cross-consumer validation և quality/adoption evidence — երկու իրական consumer-ի evidence չէ. վերաբացված է որպես Current-ի 1-ին կետ։

## Current / Ընթացիկ

1. **Open — real-consumer obligation.** Restore two-real-consumer evidence for D-025: MenQ Webpage first, the second chosen by the Owner. Recorded so far (`d-025-readiness-record.json`, 2026-10-08): Webpage pinned `tokens.vars.css` and is an "M1-candidate"; promotion is an Owner decision. / **Բաց է՝ իրական consumer-ի պարտավորությունը։** Վերականգնել D-025-ի երկու իրական consumer-ի evidence-ը՝ առաջինը MenQ Webpage-ը, երկրորդը՝ Owner-ի ընտրությամբ։ Մինչ այժմ գրանցված է (`d-025-readiness-record.json`, 2026-10-08). Webpage-ը pin է արել `tokens.vars.css`-ը և «M1-candidate» է. բարձրացումը Owner-ի որոշում է։
2. **Open — D-025 ↔ D-027 token mapping.** D-027 says the mapping between the D-025 token source and the brand token source must be decided before D-027 can be Locked. No decision is recorded. / **Բաց է՝ D-025 ↔ D-027 token mapping-ը։** D-027-ը ասում է, որ D-025 token source-ի և brand token source-ի mapping-ը պետք է որոշվի նախքան D-027-ի Locked դառնալը։ Որոշում գրանցված չէ։
3. **Open — change requests `CR-0005`…`CR-0011`.** Their work is merged; each stays open until the evidence named in its `closureBlockedBy` exists ([`governance/change-requests/`](governance/change-requests/)). / **Բաց են՝ `CR-0005`…`CR-0011` change request-ները։** Աշխատանքը merge է եղել. ամեն մեկը մնում է բաց, մինչև լինի իր `closureBlockedBy`-ում անվանված evidence-ը։
4. **Fixed — primary Button contrast (`CR-0013`, pull request #35).** In the light theme white text on the brand gradient was 2.43:1 at the cyan end, against the layer's 4.5:1 rule (recorded in `CR-0006` and `CR-0012`). `CR-0013` makes the Light primary Button and Bro avatar solid `color-action-primary` (5.93:1) and makes the validator check every gradient stop; the Owner merged it on 2026-10-09; an axe result is still owed. / **Ուղղված է՝ հիմնական Button-ի կոնտրաստը (`CR-0013`, pull request #35)։** Light theme-ում սպիտակ տեքստը brand gradient-ի cyan ծայրում 2.43:1 էր՝ շերտի 4.5:1 կանոնի դեմ (գրանցված է `CR-0006`-ում և `CR-0012`-ում)։ `CR-0013`-ը Light-ում հիմնական Button-ը և Բրոյի avatar-ը դարձնում է միագույն `color-action-primary` (5.93:1), և validator-ը սկսում է ստուգել gradient-ի ամեն stop-ը. Owner-ը այն merge է արել 2026-10-09-ին. axe-ի արդյունքը դեռ պակասում է։
5. **Open — `ru` locale pack.** D-027 names formalising it as a review trigger; nothing formalises it yet. / **Բաց է՝ `ru` locale pack-ը։** D-027-ը դրա ձևակերպումը նշում է որպես review trigger. դեռ ձևակերպված չէ։
6. **Open — status labels.** Several documents and the registry give different lifecycle values for the same thing; the list is in `CR-0012` and only the Owner can settle it. / **Բաց են՝ status պիտակները։** Մի քանի փաստաթուղթ և registry-ն նույն բանի համար տարբեր lifecycle արժեք են տալիս. ցանկը `CR-0012`-ում է, և լուծել կարող է միայն Owner-ը։
7. Preserve D-025 `Locked` status through machine enforcement, and maintain compatibility, migration, release, and adoption evidence for future changes. / Պահպանել D-025-ի `Locked` status-ը machine enforcement-ի միջոցով և ապագա փոփոխությունների համար պահպանել compatibility, migration, release և adoption evidence։
8. Until 2026-10-09 this roadmap said: "No open implementation, closure, or lock action remains." That sentence follows the verdict of the 2026-07-13 final audit and describes the lock transaction (PR #3, #4, #5) only. It is not a statement about the platform today: items 1–6 above are open. / Մինչև 2026-10-09-ը այս roadmap-ում գրված էր՝ «բաց implementation, closure կամ lock գործողություն չի մնացել»։ Այդ նախադասությունը հետևում է 2026-07-13-ի վերջնական audit-ի verdict-ին և նկարագրում է միայն lock transaction-ը (PR #3, #4, #5)։ Այն այսօրվա platform-ի մասին պնդում չէ. վերևի 1–6 կետերը բաց են։

## Later / Հետագայում

- Broader real-product adoption and M5 evidence. / Իրական products-ում ավելի լայն adoption և M5 evidence։
- Expanded components and patterns driven by proven demand. / Ապացուցված պահանջարկով պայմանավորված ընդլայնված components և patterns։
- Part 13 implementation: documentation portal, component catalog and design-tool automation (backlog by Owner decision, 2026-10-07). / Part 13-ի իրականացում՝ documentation portal, component catalog և design-tool automation (backlog՝ Owner-ի որոշմամբ, 2026-10-07)։
- Repository front page standard v1 (`CR-0011`, Draft) applied to the other MenQ Studio repositories. / Repository-ի առաջին էջի ստանդարտ v1-ի (`CR-0011`, Draft) կիրառում MenQ Studio-ի մյուս repository-ներում։
- Automated codemods and additional locale packs. / Automated codemods և լրացուցիչ locale packs։
- New architecture versions only through a formal successor decision or governed amendment. / Նոր architecture versions՝ միայն formal successor decision-ի կամ governed amendment-ի միջոցով։

<!-- END: MENQ_DESIGN_PLATFORM_ROADMAP -->
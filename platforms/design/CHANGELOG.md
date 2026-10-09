# MenQ Design Platform — Changelog / MenQ Design Platform — Փոփոխությունների պատմություն

> **How to read this / Ինչպես կարդալ:** Ամեն գրառում թվագրված է merge commit-ի ամսաթվով՝ commit-ի գրանցած ժամային գոտում (+04:00), և ասում է, թե ինչ պետք է իմանա հին commit-ին pin արված consumer-ը։ 2026-07-13-ից 2026-10-08-ի գրառումները ավելացվել են 2026-10-09-ին `CR-0012`-ով՝ change request-ներից և merge diff-երից։ / Every entry is dated by its merge commit, in the time zone the commit records (+04:00), and says what a consumer pinned to an older commit needs to know. The entries for 2026-07-13 through 2026-10-08 were added on 2026-10-09 by `CR-0012`, from the change requests and the merge diffs.

## 2026-10-09 — CR-0012 completed: the readiness record separates the 2026-07-13 snapshot from the current state (proposed; in effect when merged)

### Հայերեն

- **Consumer-ի համար՝ անելիք չկա։** Token, կոմպոնենտ, bundle, asset կամ build script չի փոխվել։
- **Record-ը կարդացողի համար փոխվում է.** `implementation/release/d-025-readiness-record.json`-ը անցավ `schemaVersion` 2-ի։ `status`, `evidenceSnapshot`, `consumers`, `crossConsumerValidation`, `qualityAndAdoptionEvidence`, `finalAudit` և `remainingAction` դաշտերը այլևս top-level-ում չեն. նույն արժեքներով դրանք `snapshot2026-07-13` դաշտի տակ են։ Ընթացիկ վիճակը `current`-ում է։ `snapshotNotice`-ը հանվեց, `evidenceCorrections`-ը չի փոխվել։
- `scripts/validate_platforms.py`-ը snapshot-ը պահում է անփոփոխ, `current`-ը՝ վերջին evidence correction-ին հավասար, և այլևս չի տպում `KNOWN INCONSISTENCY`։ `ROADMAP.md`-ի երեք պարտադիր արտահայտությունները հանվեցին validator-ից. `ROADMAP.md`-ի տեքստը չի փոխվել։
- `CR-0012`-ի status-ը `implementing` է. գրանցված approval-ի evidence-ը Owner-ի կողմից pull request #33-ի merge-ն է (`391ff55`)։ Այն փակված չէ։ `NEXT_CHAT_HANDOFF.md`-ը և `PROJECT_CONTEXT.md`-ը թարմացվեցին ըստ դրա։
- Այս գրառումը հաստատում չի հայտարարում։

### English

- **Nothing for a consumer to do.** No token, component, bundle, asset or build script changed.
- **What changes for a reader of the record:** `implementation/release/d-025-readiness-record.json` moved to `schemaVersion` 2. The fields `status`, `evidenceSnapshot`, `consumers`, `crossConsumerValidation`, `qualityAndAdoptionEvidence`, `finalAudit` and `remainingAction` are no longer at the top level; with the same values they are under the `snapshot2026-07-13` field. The current state is in `current`. `snapshotNotice` was removed; `evidenceCorrections` is unchanged.
- `scripts/validate_platforms.py` holds the snapshot unchanged and `current` equal to the latest evidence correction, and no longer prints `KNOWN INCONSISTENCY`. The three required phrases of `ROADMAP.md` were removed from the validator; the text of `ROADMAP.md` was not changed.
- The status of `CR-0012` is `implementing`; the evidence of the recorded approval is the Owner's merge of pull request #33 (`391ff55`). It is not closed. `NEXT_CHAT_HANDOFF.md` and `PROJECT_CONTEXT.md` were updated to match.
- This entry claims no approval.

## 2026-10-09 — CR-0012: Design Platform records brought to the present (proposed; in effect when merged)

### Հայերեն

- **Consumer-ի համար՝ անելիք չկա։** Token, կոմպոնենտ, bundle, asset, build script կամ validator չի փոխվել։
- `CR-0004`…`CR-0011`-ում գրանցվեցին merge եղած pull request-ները։ `CR-0004`-ը փակվեց. `CR-0005`…`CR-0011`-ը մնում են բաց՝ ամեն մեկում անվանված պակասող evidence-ով (`closureBlockedBy`)։
- Այս changelog-ում ավելացվեցին 2026-07-13-ից հետո բաց թողնված բոլոր գրառումները։
- `NEXT_CHAT_HANDOFF.md`-ը, `ROADMAP.md`-ը, `PROJECT_CONTEXT.md`-ը և `brand-expression/PROJECT_CONTEXT.md`-ը համաժամեցվեցին repository-ի իրական վիճակի հետ։ `README.md`, `ARCHITECTURE.md` և `CONTRACTS.md` ֆայլերում ավելացվեց status-ի հակասությունների նշում. lifecycle արժեք չի փոխվել։
- D-025 որոշման ֆայլը ստացավ ուղղման ծանուցում (տեքստը չի փոխվել)։ `d-025-readiness-record.json`-ը ստացավ `snapshotNotice` և `current` դաշտեր. եղած դաշտերից ոչ մեկը չի փոխվել։
- **Գրանցված բաց accessibility թերություն.** հիմնական Button-ը light theme-ում սպիտակ տեքստը դնում է ազուր → cyan gradient-ի վրա. ազուր ծայրում 5.93:1 է, cyan ծայրում՝ 2.43:1 (պահանջը՝ 4.5:1)։ Կոմպոնենտը և token-ները այս CR-ով չեն փոխվել։

### English

- **Nothing for a consumer to do.** No token, component, bundle, asset, build script or validator changed.
- The merged pull requests were recorded in `CR-0004`…`CR-0011`. `CR-0004` was closed; `CR-0005`…`CR-0011` stay open, each naming the evidence it still lacks (`closureBlockedBy`).
- Every entry this changelog had skipped since 2026-07-13 was added.
- `NEXT_CHAT_HANDOFF.md`, `ROADMAP.md`, `PROJECT_CONTEXT.md` and `brand-expression/PROJECT_CONTEXT.md` were synchronised with what the repository holds. `README.md`, `ARCHITECTURE.md` and `CONTRACTS.md` gained a note on their status conflicts; no lifecycle value was changed.
- The D-025 decision file gained a correction notice (its body is unchanged). `d-025-readiness-record.json` gained `snapshotNotice` and `current`; none of its existing fields changed.
- **Open accessibility defect recorded:** in the light theme the primary Button puts white text on the azure → cyan gradient: 5.93:1 at the azure end and 2.43:1 at the cyan end (the rule is 4.5:1). This CR changed neither the component nor the tokens.

## 2026-10-08 — CR-0011: repository front page standard v1 (PR #28, `c61608a`)

### Հայերեն

- Նոր՝ `repository-front/make_front.py` և `repository-front/README.md`։ Այս repository-ի root `README.md`-ը ստացավ front բլոկ, իսկ `docs/assets/front/`-ը՝ չորս շապիկ և `front.json`։
- **Breaking չէ։** Brand expression-ի token-ները, կոմպոնենտները և asset-ները այս merge-ում չեն փոխվել։ Ստանդարտի status-ը Draft է։

### English

- New: `repository-front/make_front.py` and `repository-front/README.md`. This repository's root `README.md` gained a front block, and `docs/assets/front/` gained four covers and `front.json`.
- **Not breaking.** No brand-expression token, component or asset changed in this merge. The standard's status is Draft.

## 2026-10-08 — CR-0010: motion patterns, logo power-on, video and shader rules (PR #27, `8d1b0ab`)

### Հայերեն

- Նոր token-ներ՝ `--duration-power-on` (1200ms), `--motion-stagger` (60ms), `--motion-distance-sm` (0.5rem), `--motion-distance-md` (1rem)։ Նոր կոմպոնենտ՝ `Reveal`։ `BrandMark`-ը ստացավ `powerOn` prop։ `tokens.json` mirror-ը ստացավ motion խումբ և `icon-stroke`։
- **Breaking չէ. միայն ավելացումներ։** Բայց այս commit-ից սկսած `components/bundle.css`-ը օգտագործում է չորս նոր custom property-ն. ավելի հին `tokens.css` կամ `tokens.vars.css` pin արած consumer-ը, որը վերցնում է նոր bundle-ը, պետք է token ֆայլն էլ re-pin անի։

### English

- New tokens: `--duration-power-on` (1200ms), `--motion-stagger` (60ms), `--motion-distance-sm` (0.5rem), `--motion-distance-md` (1rem). New component: `Reveal`. `BrandMark` gained a `powerOn` prop. The `tokens.json` mirror gained a motion group and `icon-stroke`.
- **Not breaking: additions only.** But from this commit on `components/bundle.css` uses the four new custom properties, so a consumer that pinned an older `tokens.css` or `tokens.vars.css` and takes the newer bundle must re-pin the token file too.

## 2026-10-08 — CR-0009: iconography, Accordion, Nav and Tooltip (PR #26, `79b5abc`)

### Հայերեն

- Նոր token-ներ՝ `--icon-size-sm` (1rem), `--icon-size-md` (1.25rem), `--icon-size-lg` (1.5rem), `--icon-stroke` (2)։ Նոր կոմպոնենտներ՝ `Icon`, `Accordion`, `Nav`, `Tooltip`։ `Button`-ը հիմա փոխանցում է `aria-*` և `data-*` ատրիբուտները։
- **Breaking չէ. միայն ավելացումներ։** Նոր bundle-ը օգտագործում է icon token-ները, ուստի token ֆայլը և bundle-ը re-pin անել միասին։

### English

- New tokens: `--icon-size-sm` (1rem), `--icon-size-md` (1.25rem), `--icon-size-lg` (1.5rem), `--icon-stroke` (2). New components: `Icon`, `Accordion`, `Nav`, `Tooltip`. `Button` now forwards `aria-*` and `data-*` attributes.
- **Not breaking: additions only.** The newer bundle uses the icon tokens, so re-pin the token file and the bundle together.

## 2026-10-08 — CR-0008: app icon and favicon set (PR #25, `e48d230`)

### Հայերեն

- Նոր asset-ներ `brand-expression/assets/Icons/`-ում՝ `menq-icon.svg`, `menq-icon-maskable.svg`, `favicon.ico` (16/32/48), `apple-touch-icon.png` (180), `menq-icon-192.png`, `menq-icon-512.png`, `menq-icon-maskable-512.png`՝ asset record-ներով։
- **Breaking չէ. միայն նոր ֆայլեր։**

### English

- New assets in `brand-expression/assets/Icons/`: `menq-icon.svg`, `menq-icon-maskable.svg`, `favicon.ico` (16/32/48), `apple-touch-icon.png` (180), `menq-icon-192.png`, `menq-icon-512.png`, `menq-icon-maskable-512.png`, with asset records.
- **Not breaking: new files only.**

## 2026-10-08 — CR-0007: accessibility contract and form components (PR #24, `cd25a7b`)

### Հայերեն

- **`FormRow`-ի contract-ը փոխվել է. breaking է որոշ կանչողների համար։** Նախկինում `FormRow`-ը control-ը փաթաթում էր `label`-ի մեջ և ընդունում էր ցանկացած `children`։ Հիմա այն render է անում `div.form-row`՝ առանձին `label`-ով (`htmlFor`), և պահանջում է **ճիշտ մեկ** child տարր (`React.Children.only`). առանց child-ի կամ մեկից ավելի child-ով կանչը սխալ է տալիս։ Type-ը՝ `children?: Node` → `children: React.ReactElement`։ `FormRow`-ը child-ին տալիս է `id`, `aria-describedby`, `invalid` և `required`։ Նոր ոչ պարտադիր prop-եր՝ `hint`, `required`, `id`։ CSS, որը հենվում էր `label.form-row`-ի վրա, այլևս չի համընկնի։
- Նոր կոմպոնենտներ՝ `Checkbox`, `RadioGroup`, `Switch`։ `Textarea`-ն և `Select`-ը ստացան `invalid` prop։
- `validate_brand_expression.py`-ը հիմա ստուգում է 17 տեքստ/ֆոն զույգ երկու թեմայում (34 ստուգում, ≥ 4.5:1)։ Այն gradient-ները չի ստուգում։
- Change request-ը դասակարգված է `contract-extension`, ոչ `breaking`. դասակարգման հարցը բաց է Owner-ի համար (տես `CR-0012`)։

### English

- **The `FormRow` contract changed; it is breaking for some callers.** `FormRow` used to wrap the control inside a `label` and accepted any `children`. It now renders `div.form-row` with a separate `label` (`htmlFor`) and requires **exactly one** child element (`React.Children.only`): a call with no child or with more than one throws. The type went from `children?: Node` to `children: React.ReactElement`. `FormRow` gives the child `id`, `aria-describedby`, `invalid` and `required`. New optional props: `hint`, `required`, `id`. CSS that relied on `label.form-row` no longer matches.
- New components: `Checkbox`, `RadioGroup`, `Switch`. `Textarea` and `Select` gained an `invalid` prop.
- `validate_brand_expression.py` now checks 17 text/background pairs in both themes (34 checks, ≥ 4.5:1). It does not check gradients.
- The change request is classed `contract-extension`, not `breaking`; the classification question is open for the Owner (see `CR-0012`).

## 2026-10-08 — CR-0006: primary action contrast (PR #23, `3eb4af2`)

### Հայերեն

- **Գույնի արժեք է փոխվել, light theme.** `--color-action-primary`՝ `#0284c7` (`blue-600`) → `#0369a1`. `--color-action-primary-hover`՝ `#0ea5e9` (`blue-500`) → `#075985`։ Dark theme-ը չի փոխվել։ Token-ների անունները և API-ն նույնն են։
- **Տեսանելի փոփոխություն է։** Light-ում հիմնական կոճակները և ակտիվ վիճակները ավելի մուգ ազուր են։ Ավելի հին `tokens.css` կամ `tokens.vars.css` pin արած consumer-ը պահում է հին գույնը, որի վրա սպիտակ տեքստը 4.09:1 է (WCAG AA-ից ցածր), մինչև re-pin անի։
- Սա չի ուղղում հիմնական Button-ի gradient-ը. տես 2026-10-09-ի գրառումը։

### English

- **A colour value changed, light theme.** `--color-action-primary`: `#0284c7` (`blue-600`) → `#0369a1`; `--color-action-primary-hover`: `#0ea5e9` (`blue-500`) → `#075985`. The dark theme did not change. Token names and the API are the same.
- **It is a visible change.** Light primary buttons and active states are a deeper azure. A consumer pinned to an older `tokens.css` or `tokens.vars.css` keeps the old colour, on which white text is 4.09:1 (below WCAG AA), until it re-pins.
- This does not fix the primary Button's gradient; see the 2026-10-09 entry.

## 2026-10-08 — CR-0005: official BrandMark (PR #21, `51728c9`; viewBox fix PR #22, `c98e5d5`)

### Հայերեն

- **Լոգոն փոխարինվել է։** `assets/Logos/`-ի չորս SVG-ները (`menq-wordmark-light.svg`, `menq-wordmark-dark.svg`, `menq-q-mark-light.svg`, `menq-q-mark-dark.svg`) պահել են իրենց անունները, բայց բովանդակությունը նոր է՝ պաշտոնական լոգոյից պատրաստված մարկը։ Նախկին տարբերակը (Inter-ով «Men» և power նշան ազուր pill-ի մեջ) սխալ էր։ PR #22-ը ուղղեց երկու Q-mark SVG-ի `viewBox`-ը։
- `BrandMark` կոմպոնենտը հիմա նկարում է նույն մարկը inline SVG-ով։ Նրա prop-երը (`compact`, `admin`, `tag`) չեն փոխվել։
- Բրոյի extension-ում ավելացվեց `bro-avatar-1024.png`։
- **API-ով breaking չէ, տեսքով փոխվում է։** Հին ֆայլերը պատճենած կամ SHA-256-ով pin արած consumer-ը դեռ ցույց է տալիս սխալ մարկը և պետք է նորից վերցնի ֆայլերը։

### English

- **The logo was replaced.** The four SVGs in `assets/Logos/` (`menq-wordmark-light.svg`, `menq-wordmark-dark.svg`, `menq-q-mark-light.svg`, `menq-q-mark-dark.svg`) kept their names but have new content: the mark made from the official logo. The earlier version (an Inter "Men" and a power symbol inside an azure pill) was wrong. PR #22 fixed the `viewBox` of the two Q-mark SVGs.
- The `BrandMark` component now draws the same mark as inline SVG. Its props (`compact`, `admin`, `tag`) did not change.
- `bro-avatar-1024.png` was added to the Bro extension.
- **Not breaking in API; the look changes.** A consumer that copied the old files or pinned them by SHA-256 still shows the wrong mark and must take the files again.

## 2026-10-08 — CR-0004: neon logo high-resolution master (PR #20, `dbf410e`)

### Հայերեն

- Նոր asset՝ `assets/Logos/menq-logo-neon-hires.png` (1913×720, թափանցիկ ֆոն)՝ asset record-ով։ `menq-logo-neon.png`-ը մնում է։
- **Breaking չէ. միայն նոր ֆայլ։**

### English

- New asset: `assets/Logos/menq-logo-neon-hires.png` (1913×720, transparent), with an asset record. `menq-logo-neon.png` stays.
- **Not breaking: a new file only.**

## 2026-10-07 — CR-0003: `tokens.vars.css` consumption artifact (PR #18, `493a3df`; closed by PR #19, `d05b785`)

### Հայերեն

- Նոր գեներացված ֆայլ՝ `brand-expression/tokens.vars.css`. նույն custom property-ները նույն theme selector-ներով, առանց type-style class-երի և `@font-face`-ի։ Generator-ի `--check`-ը ծածկում է այն։
- **Breaking չէ։** `tokens.css`-ը և `tokens.json`-ը այս merge-ում չեն փոխվել։
- PR #19-ը փակեց `CR-0003`-ը և `d-025-readiness-record.json`-ում գրանցեց MenQ Webpage-ի առաջին progress գրառումը։

### English

- New generated file: `brand-expression/tokens.vars.css`, the same custom properties under the same theme selectors, without type-style classes or `@font-face`. The generator's `--check` covers it.
- **Not breaking.** `tokens.css` and `tokens.json` did not change in this merge.
- PR #19 closed `CR-0003` and recorded MenQ Webpage's first progress entry in `d-025-readiness-record.json`.

## 2026-10-07 — CR-0002: Part 14 governance implemented and Locked (PR #16, `4ee07be`; PR #17, `55d277c`)

### Հայերեն

- Նոր՝ `governance/` (ownership registry, approval matrix, change-request template և record-ներ), `validate_governance.py` և `design-governance.yml` workflow։
- **Contributor-ի համար փոխվում է.** `platforms/design/`-ի կամ Design Platform-ի workflow-ների ֆայլ փոխող pull request-ի նկարագրությունը պետք է ունենա `Change-Request: CR-NNNN` կամ `Change-Class: editorial` (միայն Markdown)։
- PR #17-ով registry-ում `menq.design.spec.governance.v1`-ի lifecycle-ը դարձավ `Locked`։
- **Consumer-ի համար breaking չէ։** Package, token կամ կոմպոնենտ չի փոխվել։

### English

- New: `governance/` (ownership registry, approval matrix, change-request template and records), `validate_governance.py` and the `design-governance.yml` workflow.
- **What changes for a contributor:** a pull request that changes a file under `platforms/design/` or a Design Platform workflow must carry `Change-Request: CR-NNNN` or `Change-Class: editorial` (Markdown only) in its description.
- PR #17 set the lifecycle of `menq.design.spec.governance.v1` to `Locked` in the registry.
- **Not breaking for a consumer.** No package, token or component changed.

## 2026-10-07 — CR-0001: D-025 evidence correction (PR #15, `7da80a9`)

### Հայերեն

- `MenQ Design Catalog` և `MenQ Release Evidence Console` consumer-ները վերագնահատվեցին M3/M4-ից **M2 — Pilot**, քանի որ նրանց verdict-ը self-attested էր։ Երկու իրական consumer-ի պարտավորությունը բաց է. առաջինը MenQ Webpage-ն է, երկրորդը ընտրում է Owner-ը։
- Lock evidence-ի workflow artifact-ը ժամկետանց էր. մշտական release-ը `design-platform-v0.1.0-next.0`-ն է (հրապարակող workflow-ը՝ `publish-release.yml`, PR #13 և #14)։
- Ավելացվեց `D-025_EVIDENCE_CORRECTION_RECORD.md`-ը. lock, closure և final-audit գրառումները ստացան ուղղման ծանուցում, readiness record-ը՝ `evidenceCorrections` բաժին։ Փոխվեցին `validate_consumers.py`-ը և երկու consumer-ի build ֆայլերը։
- **Breaking չէ։** Ըստ change request-ի՝ public package API-ն չի փոխվել։ D-025-ը մնում է `Locked`։

### English

- The `MenQ Design Catalog` and `MenQ Release Evidence Console` consumers were re-graded from M3/M4 to **M2 — Pilot**, because their verdicts were self-attested. The two-real-consumer obligation is open: MenQ Webpage is the first, and the Owner selects the second.
- The workflow artifact behind the lock evidence had expired; the permanent release is `design-platform-v0.1.0-next.0` (published by the `publish-release.yml` workflow, PR #13 and #14).
- `D-025_EVIDENCE_CORRECTION_RECORD.md` was added; the lock, closure and final-audit records received a correction notice, and the readiness record an `evidenceCorrections` section. `validate_consumers.py` and the two consumers' build files changed.
- **Not breaking.** Per the change request, the public package API did not change. D-025 remains `Locked`.

## 2026-10-07 — Zero-trust audit phases 2–5 (PR #9 `ad5f013`, PR #10 `51d1261`, PR #11 `cb296a7`, PR #12 `78f86cb`)

### Հայերեն

- PR #9. `validate_phase_a.py`-ը և `validate_public_api.py`-ը խստացվեցին. token-ների և foundations-ի գեներացված artifact-ները ավելացվեցին repository-ում (նոր ֆայլեր). `public-api-baseline.json`-ը դատարկից դարձավ `0.1.0-next.0` preview-ի export map-ը։
- PR #10. registry-ի `status`-ը `Approved — Implementing`-ից դարձավ `Locked`. համաժամեցվեցին `README.md`-ի, `ARCHITECTURE.md`-ի և baseline-ի status տողերը։
- PR #11. workflow-ների անվտանգության փոփոխություններ։ PR #12. D-025 և D-027 որոշումների երկլեզու լրացում։
- **Breaking չէ.** package-ների գեներացված ֆայլերում կան միայն ավելացված տողեր։ Այս փուլերը change request չունեն, քանի որ Part 14-ը դեռ իրականացված չէր։

### English

- PR #9: `validate_phase_a.py` and `validate_public_api.py` were hardened; the generated token and foundation artifacts were added to the repository (new files); `public-api-baseline.json` went from empty to the export map of the `0.1.0-next.0` preview.
- PR #10: the registry `status` went from `Approved — Implementing` to `Locked`; the status lines of `README.md`, `ARCHITECTURE.md` and the baseline were synchronised.
- PR #11: workflow security changes. PR #12: bilingual completion of the D-025 and D-027 decisions.
- **Not breaking:** the packages' generated files have added lines only. These phases have no change request because Part 14 was not yet implemented.

## 2026-10-07 — D-027 MenQ Brand Expression Layer v1

### Հայերեն

- PR #7-ով առանց governance մտած `platforms/design/menq-design-system/` փաթեթը բերվեց D-027-ի ներքո և վերանվանվեց `platforms/design/brand-expression/`։
- Ավելացվեց canonical brand token source (`menq.design.token.*` ID-ներ, hy/en նկարագրություններ, owner, lifecycle, light/dark mode-եր) և generator՝ drift ստուգումով։
- Բրոյի ինքնությունը և 5 գործակալային կոմպոնենտ տեղափոխվեցին `platforms/design/product-extensions/bro/`։
- Ռուսերենը սահմանվեց որպես locale pack, canonical աղբյուրը՝ repository-ն։
- Ավելացվեցին asset records, bilingual փաստաթղթեր, `validate_brand_expression.py` և `design-brand-expression.yml` workflow։

### English

- Brought the ungoverned PR #7 package `platforms/design/menq-design-system/` under D-027 and renamed it `platforms/design/brand-expression/`.
- Added a canonical brand token source (`menq.design.token.*` IDs, hy/en descriptions, owner, lifecycle, light/dark modes) and a generator with a drift check.
- Moved Bro's identity and five agent components to `platforms/design/product-extensions/bro/`.
- Defined Russian as a locale pack and the repository as the canonical source.
- Added asset records, bilingual documentation, `validate_brand_expression.py` and the `design-brand-expression.yml` workflow.

## 2026-07-13 — D-025 implemented, closed and Locked (PR #3 `2682c99`, PR #4 `9a83333`, PR #5 `261f85e`, final audit `277b310`)

### Հայերեն

- PR #3. D-025-ի implementation-ը՝ տասը package boundary, canonical registry և schema, build script-եր, validator-ներ, երկու repository-ի ներսի consumer և private `0.1.0-next.0` preview candidate։
- PR #4. post-merge closure record։ PR #5. Owner-ի explicit lock approval-ը 2026-07-13-ին և `D-025_LOCK_RECORD.md`-ը։ `277b310`. վերջնական post-lock audit։
- **Հետագա ուղղում.** այդ օրը գրանցված consumer grade-երը (M3 և M4) և workflow artifact evidence-ը ուղղվել են 2026-10-07-ին (տես `CR-0001`-ի գրառումը վերևում)։ D-025-ը մնում է `Locked`։

### English

- PR #3: the D-025 implementation — ten package boundaries, the canonical registry and schema, build scripts, validators, two in-repository consumers and the private `0.1.0-next.0` preview candidate.
- PR #4: the post-merge closure record. PR #5: the Owner's explicit lock approval on 2026-07-13 and `D-025_LOCK_RECORD.md`. `277b310`: the final post-lock audit.
- **Later correction:** the consumer grades recorded that day (M3 and M4) and the workflow-artifact evidence were corrected on 2026-10-07 (see the `CR-0001` entry above). D-025 remains `Locked`.

## 2026-07-12 — Part 16 specification index and implementation package plan

### Հայերեն

- Ավելացվել է `CANONICAL_SPECIFICATION_INDEX_IMPLEMENTATION_PACKAGE_PLAN_V1.md`։
- Սահմանվել են canonical IDs, ownership, dependency graph, package/API mapping և release input contract-ը։
- Սահմանվել է package topology-ը՝ contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales և validation։
- Սահմանվել են deterministic build graph-ը, public API contract-ը, release channels-ը և release manifest-ը։
- Continuation point-ը տեղափոխվել է D-025 completeness audit, validator design և Draft PR review։

### English

- Added `CANONICAL_SPECIFICATION_INDEX_IMPLEMENTATION_PACKAGE_PLAN_V1.md`.
- Defined canonical IDs, ownership, dependency graph, package/API mapping, and release-input contracts.
- Defined package topology for contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales, and validation.
- Defined the deterministic build graph, public API contract, release channels, and release manifest.
- Advanced the continuation point to the D-025 completeness audit, validator design, and Draft PR review.

## 2026-07-12 — Part 15 product adoption and two-consumer validation architecture

### Հայերեն

- Ավելացվել է `PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md`։
- Սահմանվել են M0–M5 maturity levels-ը և երկու genuinely distinct consumers-ի validation rule-ը։
- Continuation point-ը տեղափոխվել է Part 16 — Canonical Specification Index and Implementation Package Plan։

### English

- Added `PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md`.
- Defined M0–M5 maturity levels and the validation rule for two genuinely distinct consumers.
- Advanced the continuation point to Part 16 — Canonical Specification Index and Implementation Package Plan.

## 2026-07-12 — Part 14 governance and change lifecycle architecture

### Հայերեն

- Ավելացվել է `GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md`։
- Սահմանվել են authority model-ը, ownership registry-ն, contribution classes-ը, review/approval matrix-ը և change-request lifecycle-ը։
- Unowned canonical asset-ը սահմանվել է որպես RED governance defect։
- High-risk կամ breaking change-ի self-approval-ը արգելվել է։
- Merge-ը սահմանվել է որպես առանձին authority action, ոչ GREEN CI-ի ավտոմատ հետևանք։
- Emergency path-ը պահպանում է retrospective record, validation, synchronization և unresolved-risk ownership-ը։
- Continuation point-ը տեղափոխվել է Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan։

### English

- Added `GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md`.
- Defined the authority model, ownership registry, contribution classes, review and approval matrix, and change-request lifecycle.
- Defined an unowned canonical asset as a RED governance defect.
- Prohibited self-approval for high-risk or breaking changes.
- Defined merge as a separate authority action rather than an automatic consequence of green CI.
- Preserved retrospective recording, validation, synchronization, and unresolved-risk ownership in the emergency path.
- Advanced the continuation point to Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan.

## 2026-07-12 — Part 13 documentation, catalog, and design-tool integration architecture

### Հայերեն

- Ավելացվել է `DOCUMENTATION_PORTAL_COMPONENT_CATALOG_DESIGN_TOOL_INTEGRATION_ARCHITECTURE_V1.md`։
- Documentation portal-ը, component catalog-ը և design-tool integration-ը սահմանվել են որպես նույն canonical repository source-ից կառուցվող governed views, ոչ առանձին truth sources։
- Սահմանվել են bilingual navigation/parity, version/compatibility visibility, behavior-first catalog entries, public-API-only examples, stable canonical IDs, token/component mapping parity և cross-surface drift detection։
- Սահմանվել է synchronization pipeline-ը՝ repository source → schema validation → package generation → documentation extraction → catalog build → design-tool validation → parity report → release evidence։
- Part 13-ը architecture-level complete է, բայց implementation-ը Locked չէ մինչև prototype, mapping proof, validator automation, consumer use և explicit Owner approval։
- Continuation point-ը տեղափոխվել է Part 14 — Governance, Contribution, Ownership, and Change-Request Lifecycle։

### English

- Added `DOCUMENTATION_PORTAL_COMPONENT_CATALOG_DESIGN_TOOL_INTEGRATION_ARCHITECTURE_V1.md`.
- Defined the documentation portal, component catalog, and design-tool integration as governed views generated from the same canonical repository source, not independent sources of truth.
- Defined bilingual navigation/parity, version and compatibility visibility, behavior-first catalog entries, public-API-only examples, stable canonical IDs, token/component mapping parity, and cross-surface drift detection.
- Defined the synchronization pipeline from repository source through schema validation, package generation, documentation extraction, catalog build, design-tool validation, parity reporting, and release evidence.
- Part 13 is architecture-complete, but implementation is not Locked until prototype, mapping proof, validator automation, consumer use, and explicit Owner approval are complete.
- Advanced the continuation point to Part 14 — Governance, Contribution, Ownership, and Change-Request Lifecycle.

## 2026-07-12 — Part 12 validation architecture

### Հայերեն

- Ավելացվել է `VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`։
- Սահմանվել են յոթ sequential gates, GREEN/YELLOW/RED verdict semantics-ը, conformance profiles-ը, exception contract-ը և evidence contract-ը։
- D-025-ը մնում է `Approved — Implementing`, PR #3-ը մնում է Draft և unmerged։

### English

- Added `VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`.
- Defined seven sequential gates, GREEN/YELLOW/RED verdict semantics, conformance profiles, the exception contract, and the evidence contract.
- D-025 remains `Approved — Implementing`; PR #3 remains Draft and unmerged.

## 2026-07-12 — D-025 architecture baseline synchronization

### Հայերեն

- D-025-ը synchronized է Owner-approved Parts 1–11 baseline-ի հետ։
- Four-layer wording-ը փոխարինվել է canonical dependency model-ով՝ Reference → Semantic → Component → Pattern → Product Extension։
- Theme, state, density, platform, viewport/container, locale/script, accessibility, motion preference և product expression-ը սահմանվել են որպես orthogonal dimensions։
- Controlled exceptions-ը սահմանվել են որպես governed temporary bypass, ոչ normal token layer։
- Ավելացվել է canonical token source/build pipeline-ը։
- Հաստատվել են behavior-first component, reusable pattern, theming, accessibility, localization, content, asset, motion, package, release, versioning, migration և compatibility architecture-ները։
- Armenian և English լեզուները հաստատվել են որպես հավասար canonical languages։ Additional languages-ը սահմանվել են որպես on-demand locale packs։
- Ավելացվել են `DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md` և Design Platform-specific `NEXT_CHAT_HANDOFF.md`։
- D-025-ը մնում է `Approved — Implementing`, PR #3-ը մնում է Draft և unmerged։

### English

- Synchronized D-025 with the Owner-approved Parts 1–11 baseline.
- Replaced the four-layer wording with the canonical dependency model: Reference → Semantic → Component → Pattern → Product Extension.
- Defined theme, state, density, platform, viewport/container, locale/script, accessibility, motion preference, and product expression as orthogonal dimensions.
- Defined controlled exceptions as governed temporary bypasses, not a normal token layer.
- Added the canonical token source and build pipeline.
- Approved behavior-first component, reusable pattern, theming, accessibility, localization, content, asset, motion, package, release, versioning, migration, and compatibility architecture.
- Confirmed Armenian and English as equal canonical languages and additional languages as on-demand locale packs.
- D-025 remains `Approved — Implementing`; PR #3 remains Draft and unmerged.

## 2026-07-12 — Initial D-025 architecture implementation

### Հայերեն

- Ավելացվել է `D-025 — MenQ Design Platform Architecture v1` decision-ը։
- Սահմանվել է վեց architecture plane՝ Brand Core, Tokens, Primitives, Components, Patterns և Delivery։
- Սահմանվել է product-neutral shared core boundary-ը և controlled product extension direction-ը։
- Architecture review-ից հանվել են logo presentation-ը և project-specific references-ը։

### English

- Added the `D-025 — MenQ Design Platform Architecture v1` decision.
- Defined six architecture planes: Brand Core, Tokens, Primitives, Components, Patterns, and Delivery.
- Defined the product-neutral shared-core boundary and controlled product-extension direction.
- Removed logo presentation and project-specific references from the architecture review.

<!-- END: MENQ_DESIGN_PLATFORM_CHANGELOG -->
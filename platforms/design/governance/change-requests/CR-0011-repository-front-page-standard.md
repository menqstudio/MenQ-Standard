# CR-0011 — Repository front page standard v1 / Repository-ի առաջին էջի ստանդարտ v1

```json
{
  "id": "CR-0011",
  "title": {"hy": "Repository-ի առաջին էջի ստանդարտ v1", "en": "Repository front page standard v1"},
  "class": "contract-extension",
  "status": "implementing",
  "proposer": "AI collaborator (Claude), owner request 2026-10-07",
  "proposerOwnerId": null,
  "approvals": [
    {"ownerId": "owner.menq", "name": "Gevorg Ohanyan", "date": "2026-10-08", "evidence": "Owner asked to synchronise the front pages of every GitHub repository, better than KRYUK24's, with better UX (2026-10-07 22:58 and 23:27 UTC)"}
  ],
  "affectedAssets": ["menq.design.build.repository-front"],
  "decision": "D-027",
  "risk": "R1",
  "consumerEvidencePlan": "Applied to every MenQ Studio repository and to the Scout client project in one pull request each; each README keeps its own content below the front block.",
  "migrationPlan": "Additive: a generator, a config file per repository and a front block at the top of each README.",
  "rollback": "Revert the pull request in the affected repository.",
  "evidencePlan": "Generator checks text contrast (4.5:1) in both themes and that every Start here link exists; covers rendered in Chromium at desktop and phone width.",
  "targetRelease": "none (brand expression layer)",
  "pullRequests": [28],
  "mergeEvidence": ["PR #28 merged at c61608a on 2026-10-08 04:22 +04:00 (2026-10-08 00:22 UTC)"],
  "closure": null,
  "closureBlockedBy": ["consumerEvidencePlan (required for class contract-extension): 'applied to every MenQ Studio repository and to the Scout client project in one pull request each' - only this repository's application is visible here (PR #28: the README front block and docs/assets/front/); the other repositories' pull requests are not recorded", "evidencePlan: no record of the covers rendered in Chromium at desktop and phone width", "evidencePlan: make_front.py --check is run by no workflow and no validator in this repository, and could not be run in the 2026-10-09 review environment (fontTools is not installed there), so the generator's contrast and link checks are not verified"]
}
```

## Հայերեն

### Խնդիր

Repo-ների առաջին էջերը տարբեր էին. մեկը նկարազարդ էր, մյուսը՝ միայն տեքստ, ոմանք առանց պարզ սկզբնակետի։ Ընթերցողը չէր տեսնում՝ ինչ է repo-ն, ում համար է, ինչ վիճակում է և որտեղից սկսել կարդալը։

### Ցանկալի արդյունք

Մեկ ստանդարտ բոլորի համար, ամեն մեկը՝ իր ինքնությամբ. շապիկի նկար (light, dark, հեռախոս), «Սկսիր այստեղից» հղումներ և չորս տողանոց ամփոփում անգլերեն ու հայերեն։ MenQ-ի repo-ները կրում են պաշտոնական wordmark-ը՝ անփոփոխ պատճենված. client-ների repo-ները՝ իրենց գույները, առանց MenQ նշանի։

### Scope և ազդեցություն

Միայն README-ի վերևի բլոկը և `docs/assets/front/`-ը։ README-ի մնացած տեքստը նույնն է մնում։

### Migration և rollback

Միայն ավելացումներ։ Rollback՝ PR-ի revert։

### Փակման վիճակ (2026-10-09, CR-0012)

Բաց է։ Աշխատանքը merge է եղել (PR #28՝ `c61608a`)։ Փակմանը խանգարում է. (1) «կիրառված է MenQ Studio-ի ամեն repository-ում և Scout client project-ում» կետից այստեղ երևում է միայն այս repository-ի կիրառումը (README-ի վերևի բլոկը և `docs/assets/front/`). մյուս repository-ների pull request-ները գրանցված չեն, (2) Chromium-ով desktop և հեռախոսի լայնությամբ render-ի գրառում չկա, (3) `make_front.py --check`-ը այս repository-ում ոչ մի workflow կամ validator չի գործարկում, և 2026-10-09-ի ստուգման միջավայրում այն չաշխատեց (`fontTools`-ը տեղադրված չէր), ուստի generator-ի contrast և հղումների ստուգումները հաստատված չեն։

## English

### Problem

Front pages differed: one illustrated, others text only, some without a clear starting point. A reader could not see what a repository is, who it serves, its state and where to start reading.

### Desired outcome

One standard for all, each with its own identity: a cover picture (light, dark, phone), Start here links and a four-row summary in English and Armenian. MenQ repositories carry the official wordmark copied as is; client repositories carry their own palette and no MenQ mark.

### Scope and impact

Only the top block of each README and `docs/assets/front/`. The rest of each README stays as it is.

### Migration and rollback

Additions only. Rollback: revert the pull request.

### Closure status (2026-10-09, CR-0012)

Open. The work is merged (PR #28 at `c61608a`). Closure is blocked by: (1) of "applied to every MenQ Studio repository and to the Scout client project", only this repository's application is visible here (the README front block and `docs/assets/front/`); the other repositories' pull requests are not recorded; (2) there is no record of the covers rendered in Chromium at desktop and phone width; (3) `make_front.py --check` is run by no workflow and no validator in this repository, and it could not be run in the 2026-10-09 review environment (`fontTools` was not installed), so the generator's contrast and link checks are not verified.

<!-- END: CR-0011 -->

# CR-0011 — Repository front page standard v1 / Repository-ի առաջին էջի ստանդարտ v1

```json
{
  "id": "CR-0011",
  "title": {"hy": "Repository-ի առաջին էջի ստանդարտ v1", "en": "Repository front page standard v1"},
  "class": "contract-extension",
  "status": "approved",
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
  "pullRequests": [],
  "closure": null
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

## English

### Problem

Front pages differed: one illustrated, others text only, some without a clear starting point. A reader could not see what a repository is, who it serves, its state and where to start reading.

### Desired outcome

One standard for all, each with its own identity: a cover picture (light, dark, phone), Start here links and a four-row summary in English and Armenian. MenQ repositories carry the official wordmark copied as is; client repositories carry their own palette and no MenQ mark.

### Scope and impact

Only the top block of each README and `docs/assets/front/`. The rest of each README stays as it is.

### Migration and rollback

Additions only. Rollback: revert the pull request.

<!-- END: CR-0011 -->

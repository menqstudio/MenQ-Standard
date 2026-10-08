# Repository front page standard v1 / Repository-ի առաջին էջի ստանդարտ v1

**Status / Կարգավիճակ:** Draft (D-027, CR-0011)
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Ամեն repo-ի առաջին էջը սկսվում է նույն կերպ. շապիկի նկար, «Start here» հղումներ և չորս տողանոց ամփոփում (ինչ է, ում համար, վիճակ, ինչով է կառուցված) անգլերեն ու հայերեն։ Աղբյուրը repo-ի `docs/assets/front/front.json` ֆայլն է։

**Կանոններ**
- MenQ-ի repo-ները կրում են պաշտոնական wordmark-ը՝ `brand-expression/assets/Logos`-ից անփոփոխ պատճենված։ Client-ի repo-ն (`"brand": "client"`) կրում է իր գույները և MenQ նշան չունի։
- Նկարում հնացող փաստ չկա (ամսաթիվ, թիվ, վիճակ). դրանք մնում են Markdown-ում՝ աղբյուրի հղումով։
- Ամեն տառ ուրվագիծ է brand տառատեսակներից. script, արտաքին ռեսուրս և font բեռնում չկա։ Կոնտրաստը՝ առնվազն 4.5:1 երկու թեմայում։
- Ամփոփման փաստերը վերցվում են repo-ի սեփական README-ից և ֆայլերից։ Ոչինչ չի հորինվում։

**Օգտագործում.** `python platforms/design/repository-front/make_front.py <repo>/docs/assets/front/front.json`, ստուգելու համար՝ `--check`։

## English

Every repository's front page starts the same way: a cover picture, Start here links and a four-row summary (what it is, who it serves, state, built with) in English and Armenian. The source is the repository's `docs/assets/front/front.json`.

**Rules**
- MenQ repositories carry the official wordmark, copied unchanged from `brand-expression/assets/Logos`. A client repository (`"brand": "client"`) carries its own palette and no MenQ mark.
- The picture holds no fact that goes stale (dates, counts, states); those stay in the Markdown with a link to their source.
- Every letter is an outline from the brand fonts: no script, no external resource, no font loading. Contrast at least 4.5:1 in both themes.
- Facts in the summary come from the repository's own README and files. Nothing is invented.

**Use:** `python platforms/design/repository-front/make_front.py <repo>/docs/assets/front/front.json`; `--check` to verify.

<!-- END: MENQ_REPOSITORY_FRONT_README -->

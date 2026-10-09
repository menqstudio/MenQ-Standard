# Foundation v1 Release Snapshot / Foundation v1 release snapshot

**Version / Տարբերակ:** 1.0.0  
**Date / Ամսաթիվ:** 2026-07-12 (this description was written; the release tag was cut on 2026-10-07, see Release facts) / 2026-07-12 (գրվել է այս նկարագրությունը․ release tag-ը դրվել է 2026-10-07-ին, տես Release-ի փաստերը)  
**Status / Կարգավիճակ:** Tagged `foundation-v1.0.0`; `CHANGELOG.md` records the release as published on 2026-10-07; the publishing run was not re-checked on 2026-10-09 / Tag՝ `foundation-v1.0.0`․ `CHANGELOG.md`-ը release-ը գրանցում է հրապարակված 2026-10-07-ին․ հրապարակող run-ը 2026-10-09-ին չի վերստուգվել  
**Last synchronized / Վերջին համաժամեցում:** 2026-10-09  
**Canonical source:** `https://github.com/menqstudio/MenQ-Standard`

## Հայերեն

Այս package-ը MenQ Standard Foundation v1-ի delivery snapshot-ն է։ Այն ստեղծվում է միայն `Foundation Integrity` validator-ի GREEN result-ից հետո։ GitHub repository-ն մնում է canonical source of truth-ը։ ZIP-ը frozen delivery artifact է և չի փոխարինում repository-ին։

Snapshot-ը ներառում է repository-ի tracked content-ը՝ առանց `.git` directory-ի և generated ZIP files-ի։ Package build-ը ստեղծում է SHA-256 manifest և ստուգում է Foundation-ի պարտադիր root/chapter files-ի գոյությունը։

## English

This package is the delivery snapshot of MenQ Standard Foundation v1. It is created only after a GREEN result from the `Foundation Integrity` validator. The GitHub repository remains the canonical source of truth. The ZIP is a frozen delivery artifact and does not replace the repository.

The snapshot contains the repository's tracked content without the `.git` directory or generated ZIP files. The package build creates a SHA-256 manifest and verifies the presence of required Foundation root and chapter files.

## Publishing / Հրապարակում

**HY:** Release-ը հրապարակվում է `foundation-v<version>` tag-ով `main`-ի commit-ի վրա։ `.github/workflows/publish-release.yml`-ը ստուգում է, որ tag-ը `main`-ում է, գործարկում է Foundation validator-ը, կառուցում է ZIP-ը `SHA256SUMS.txt` manifest-ով և այն կցում է GitHub Release-ին որպես մշտական asset՝ `.sha256` ֆայլի հետ։ Workflow artifact-ի retention-ը release evidence չէ։

**EN:** A release is published by pushing a `foundation-v<version>` tag on a `main` commit. `.github/workflows/publish-release.yml` verifies that the tag is on `main`, runs the Foundation validator, builds the ZIP with the `SHA256SUMS.txt` manifest, and attaches it to a GitHub Release as a permanent asset together with a `.sha256` file. Workflow-artifact retention is not release evidence.

## Release facts, checked on 2026-10-09 / Release-ի փաստերը՝ ստուգված 2026-10-09-ին

**HY:**

- Local clone-ում `git tag -l`-ը ցույց է տալիս երկու tag՝ `foundation-v1.0.0` և `design-platform-v0.1.0-next.0`։ `git rev-parse`-ը երկուսի համար էլ վերադարձնում է նույն commit-ը՝ `3793b3ce01a98db051894917595624881972adad`, և `git log -1`-ը այդ commit-ի համար ցույց է տալիս 2026-10-07 ամսաթիվը և «Merge pull request #14 from menqstudio/phase-6b-dispatch» վերնագիրը։ Երկուսն էլ lightweight tag են։
- Ուստի `1.0.0`-ը տարբերակի անունն է, իսկ snapshot-ի բովանդակությունը 2026-10-07-ի repository-ն է, ոչ թե 2026-07-12-ինը։
- Snapshot-ը ամբողջ repository-ն է, ոչ միայն Foundation-ը․ `.github/workflows/publish-release.yml`-ը ZIP-ը կառուցում է `git archive HEAD`-ով, այսինքն այդ commit-ի բոլոր tracked ֆայլերից՝ ներառյալ `platforms/`-ը։
- Մինչև 2026-10-09 այս ֆայլի header-ը գրում էր `Date: 2026-07-12` և `Status: Validated GREEN`։ Հրապարակող workflow-ը validator-ը գործարկում է ZIP-ը կառուցելուց առաջ, բայց այդ run-ը, GitHub Release-ի էջը և asset-ը 2026-10-09-ին չեն ստուգվել (ստուգումը կատարվել է առանց ցանցի)։ 2026-07-12-ի validation-ի գրառումը [`../foundation/FOUNDATION_V1_VALIDATION_RUN.md`](../foundation/FOUNDATION_V1_VALIDATION_RUN.md)-ն է և վերաբերում է այլ commit-ի։
- Ոչ մի tag չի փոխվել։ Tag-ը և release-ը փոխելը կամ վերանվանելը Owner-ի որոշում է։

**EN:**

- In a local clone, `git tag -l` shows two tags, `foundation-v1.0.0` and `design-platform-v0.1.0-next.0`. `git rev-parse` returns the same commit for both, `3793b3ce01a98db051894917595624881972adad`, and `git log -1` on that commit shows the date 2026-10-07 and the subject “Merge pull request #14 from menqstudio/phase-6b-dispatch”. Both are lightweight tags.
- `1.0.0` is therefore the name of the version, while the content of the snapshot is the repository of 2026-10-07, not of 2026-07-12.
- The snapshot is the whole repository, not the Foundation alone: `.github/workflows/publish-release.yml` builds the ZIP with `git archive HEAD`, that is, from every tracked file of that commit, including `platforms/`.
- Until 2026-10-09 the header of this file read `Date: 2026-07-12` and `Status: Validated GREEN`. The publishing workflow runs the validator before it builds the ZIP, but that run, the GitHub Release page and the asset were not checked on 2026-10-09 (the check was made without network access). The record of the 2026-07-12 validation is [`../foundation/FOUNDATION_V1_VALIDATION_RUN.md`](../foundation/FOUNDATION_V1_VALIDATION_RUN.md), and it concerns a different commit.
- No tag was changed. Changing or renaming the tag and the release is an Owner decision.

<!-- END: FOUNDATION_V1_RELEASE_README -->
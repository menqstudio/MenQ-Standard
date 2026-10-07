# Foundation v1 Release Snapshot / Foundation v1 release snapshot

**Version / Տարբերակ:** 1.0.0  
**Date / Ամսաթիվ:** 2026-07-12  
**Status / Կարգավիճակ:** Validated GREEN / Ստուգված GREEN  
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

<!-- END: FOUNDATION_V1_RELEASE_README -->
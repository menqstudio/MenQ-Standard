# D-022 — Canonical Write Integrity Law / Canonical write-ի ամբողջականության օրենք

**Status / Կարգավիճակ:** Locked / Հաստատված  
**Date / Ամսաթիվ:** 2026-07-12  
**Decision class / Որոշման դաս:** `C4 — Foundation or Ecosystem`  
**Risk level / Ռիսկի մակարդակ:** `R4 — Critical integrity risk`  
**Approver / Հաստատող:** MenQ Owner  
**Canonical law / Canonical օրենք:** [`CANONICAL_WRITE_INTEGRITY_LAW.md`](CANONICAL_WRITE_INTEGRITY_LAW.md)

## Հայերեն

Owner-ը հաստատել է, որ canonical file-ի ոչ մի write, update, replace, move կամ delete չի համարվում ավարտված կամ հաջող, մինչև պարտադիր post-write integrity verification-ը ամբողջությամբ չի անցել։

Պարտադիր է՝

1. write-ից առաջ կարդալ ամբողջ canonical file-ը,
2. պահպանել current SHA-ն կամ equivalent identifier-ը,
3. արգելել partial read-ից full-file replacement-ը,
4. write-ից հետո re-read անել file-ի սկիզբն ու վերջը,
5. ստուգել truncation-ը, bilingual completeness-ը, links-ը և unrelated content-ի պահպանումը,
6. RED կամ FAIL արդյունքի դեպքում անմիջապես կանգնել, վերականգնել նախորդ canonical version-ը և կրկին verify անել,
7. չներկայացնել write-ը որպես complete, locked կամ successful առանց re-read evidence-ի։

Այս կանոնը չի կարող շրջանցվել արագության, convenience-ի, token limit-ի, tool limitation-ի, emergency-ի կամ փոփոխության փոքր լինելու պատճառաբանությամբ։ Tool success-ը integrity evidence չէ։

## English

The Owner has approved that no canonical file write, update, replacement, move, or deletion is considered complete or successful until mandatory post-write integrity verification has fully passed.

It is mandatory to:

1. read the complete canonical file before writing,
2. preserve the current SHA or equivalent identifier,
3. prohibit full-file replacement from a partial read,
4. re-read the beginning and ending after writing,
5. verify truncation, bilingual completeness, links, and preservation of unrelated content,
6. stop immediately, restore the previous canonical version, and re-verify when any required check is RED or FAIL,
7. never represent a write as complete, locked, or successful without re-read evidence.

This rule may not be bypassed for speed, convenience, token limits, tool limitations, emergencies, or because a change appears small. Tool success is not integrity evidence.

<!-- END: D-022_CANONICAL_WRITE_INTEGRITY_LAW -->
# Canonical Write Integrity Law / Canonical write-ի ամբողջականության օրենք

**Status / Կարգավիճակ:** Locked v1 / Հաստատված v1  
**Version / Տարբերակ:** 1.0  
**Owner / Պատասխանատու:** MenQ Owner  
**Document class / Փաստաթղթի դաս:** Normative  
**Canonical path / Canonical ուղի:** `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`  
**Related decisions / Կապված որոշումներ:** `D-021`, `D-022`

## 1. Law / Օրենք

**HY:** Ոչ մի canonical write, update, replace, move կամ delete չի համարվում ավարտված, հաջող կամ ընդունելի, մինչև post-write integrity verification-ը ամբողջությամբ չի անցել։ Tool-ի success response-ը միայն գործողության փորձի ապացույց է, ոչ արդյունքի ամբողջականության ապացույց։

**EN:** No canonical write, update, replacement, move, or deletion is considered complete, successful, or acceptable until post-write integrity verification has fully passed. A tool success response proves only that an operation was attempted, not that the resulting content is complete.

## 2. Mandatory Pre-Write Gate / Պարտադիր pre-write gate

Canonical file-ը փոփոխելուց առաջ պարտադիր է՝

1. կարդալ ամբողջ ընթացիկ file-ը, ոչ միայն snippet կամ partial range,
2. պահպանել current SHA կամ equivalent identifier-ը,
3. հաստատել expected title-ը, beginning marker-ը և ending marker-ը,
4. պատրաստել ամբողջական replacement content-ը,
5. արգելել partial read-ից full-file replacement-ը։

Before modifying a canonical file, the complete current file must be read, its current SHA or equivalent identifier preserved, expected beginning and ending markers identified, the complete replacement prepared, and full-file replacement from a partial read prohibited.

## 3. Mandatory Post-Write Gate / Պարտադիր post-write gate

Յուրաքանչյուր write-ից անմիջապես հետո պարտադիր է re-read անել և հաստատել՝

1. file-ը բացվում է,
2. title-ը, status-ը և metadata-ն պահպանված են,
3. expected beginning-ը գոյություն ունի,
4. expected ending-ը գոյություն ունի,
5. բովանդակությունը truncated չէ,
6. հայերեն և անգլերեն բաժինները ամբողջական են,
7. unrelated canonical information չի կորել,
8. links, indexes, decisions, changelog և context files synchronized են,
9. նոր SHA-ն համապատասխանում է սպասված փոփոխությանը։

After every write, the file must be re-read and verified for readability, metadata, expected beginning and ending, absence of truncation, bilingual completeness, preservation of unrelated canonical information, synchronized references, and the expected new SHA.

## 4. RED Stop Rule / RED կանգառի կանոն

Եթե verification-ի որևէ պարտադիր կետ FAIL կամ RED է՝

1. աշխատանքը անմիջապես կանգնում է,
2. file-ը չի ներկայացվում որպես complete, locked կամ successful,
3. նախորդ canonical version-ը վերականգնվում է Git history-ից կամ preserved content-ից,
4. նոր write-ը կատարվում է միայն ամբողջական source-ից,
5. verification-ը կրկնվում է,
6. incident-ը բացահայտ գրանցվում է և չի թաքցվում։

If any required verification check fails or is RED, work stops immediately; the file is not represented as complete, locked, or successful; the previous canonical version is restored; the write is repeated only from a complete source; verification is repeated; and the incident is recorded transparently.

## 5. Non-Bypass Rule / Չշրջանցվող կանոն

**HY:** Այս օրենքը չի կարող անտեսվել արագության, convenience-ի, token limit-ի, tool limitation-ի, emergency-ի կամ «փոքր փոփոխություն է» պատճառաբանությամբ։ Եթե ամբողջական verification հնարավոր չէ, canonical write-ը չի կատարվում կամ չի համարվում ավարտված։

**EN:** This law may not be bypassed for speed, convenience, token limits, tool limitations, emergencies, or because a change appears small. If complete verification is not possible, the canonical write must not proceed or must not be considered complete.

## 6. Accountability / Պատասխանատվություն

**HY:** Write կատարող մարդը կամ AI collaborator-ը պատասխանատու է verification-ի համար։ AI-ն պարտավոր է հայտնել uncertainty-ն, failure-ը կամ truncation-ը և չի կարող իրեն GREEN տալ առանց re-read evidence-ի։

**EN:** The human or AI collaborator performing the write is accountable for verification. AI must disclose uncertainty, failure, or truncation and may not declare GREEN without re-read evidence.

## 7. Completion Marker / Ավարտի marker

Canonical write transaction-ը complete է միայն այս sequence-ից հետո՝

```text
READ COMPLETE SOURCE
→ PRESERVE SHA
→ WRITE
→ RE-READ BEGINNING
→ RE-READ ENDING
→ VERIFY CONTENT AND SYNCHRONIZATION
→ GREEN
```

> **HY:** Չստուգված write-ը փոփոխություն չէ։ Այն integrity incident է։  
> **EN:** An unverified write is not a completed change. It is an integrity incident.

<!-- END: CANONICAL_WRITE_INTEGRITY_LAW_V1 -->
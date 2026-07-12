# MenQ Standard — Decision Index / Որոշումների ինդեքս

**Status / Կարգավիճակ:** Active / Գործող
**Document class / Փաստաթղթի դաս:** Normative Registry
**Owner / Պատասխանատու:** MenQ Owner

## Rule / Կանոն

**HY:** `DECISIONS.md`-ը պահպանում է historical `D-001–D-021` registry-ն։ Նոր ecosystem decisions-ը պահվում են dedicated files-ով և այստեղ ավելացվում են append-only entry-ներով՝ մեծ monolithic file-ի unsafe rewrite-ից խուսափելու համար։ ID-ն չի վերօգտագործվում կամ ջնջվում։

**EN:** `DECISIONS.md` preserves the historical `D-001–D-021` registry. New ecosystem decisions are stored as dedicated files and added here through append-only entries to avoid unsafe rewrites of a large monolithic file. IDs are never reused or deleted.

## Decisions

- `D-001–D-021` — [`DECISIONS.md`](DECISIONS.md)
- `D-022` — [`foundation/documentation/D-022-CANONICAL_WRITE_INTEGRITY_LAW.md`](foundation/documentation/D-022-CANONICAL_WRITE_INTEGRITY_LAW.md)
- `D-023` — [`foundation/ai-collaboration/D-023-MENQ-AI-COLLABORATION-STANDARD-V1.md`](foundation/ai-collaboration/D-023-MENQ-AI-COLLABORATION-STANDARD-V1.md)
- `D-024` — [`platforms/D-024-PLATFORMS-ARCHITECTURE-V1.md`](platforms/D-024-PLATFORMS-ARCHITECTURE-V1.md)

## Append Protocol / Ավելացման protocol

1. Create and verify the dedicated decision file.
2. Append one entry here without rewriting previous entries.
3. Synchronize changelog, relevant context, index, and roadmap.
4. Run integrity validation.

<!-- END: MENQ_DECISION_INDEX -->
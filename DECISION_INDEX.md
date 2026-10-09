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
- `D-023` — [`foundation/ai-collaboration/D-023_AI_COLLABORATION_STANDARD_V1.md`](foundation/ai-collaboration/D-023_AI_COLLABORATION_STANDARD_V1.md)
- `D-024` — [`platforms/D-024-PLATFORMS-ARCHITECTURE-V1.md`](platforms/D-024-PLATFORMS-ARCHITECTURE-V1.md)
- `D-025` — [`platforms/design/decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](platforms/design/decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md)
- `D-026` — [`foundation/ai-collaboration/D-026-CANONICAL-SESSION-READ-LAW.md`](foundation/ai-collaboration/D-026-CANONICAL-SESSION-READ-LAW.md)
- `D-027` — [`platforms/design/decisions/D-027-MENQ-BRAND-EXPRESSION-LAYER-V1.md`](platforms/design/decisions/D-027-MENQ-BRAND-EXPRESSION-LAYER-V1.md)
- `D-028` — [`foundation/ai-collaboration/D-028-BOUNDED-SESSION-READ-LAW.md`](foundation/ai-collaboration/D-028-BOUNDED-SESSION-READ-LAW.md) — Proposed (proposed; the Owner's merge of its pull request is the approval); supersedes `D-026` in part / Proposed (առաջարկված. հաստատումը Owner-ի կողմից նրա pull request-ի merge-ն է)․ մասամբ փոխարինում է `D-026`-ը

## Append Protocol / Ավելացման protocol

1. Create and verify the dedicated decision file. / Ստեղծել և ստուգել dedicated decision file-ը։
2. Append one entry here without rewriting previous entries. / Այստեղ ավելացնել մեկ entry՝ առանց նախորդ entry-ները վերագրելու։
3. Synchronize changelog, relevant context, index, and roadmap. / Համաժամեցնել changelog-ը, համապատասխան context-ը, index-ը և roadmap-ը։
4. Run integrity validation. / Գործարկել integrity validation-ը։

<!-- END: MENQ_DECISION_INDEX -->
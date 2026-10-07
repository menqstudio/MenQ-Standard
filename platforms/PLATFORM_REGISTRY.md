# Platform Registry / Platform-ների registry

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Normative Registry  
**Owner / Պատասխանատու:** MenQ Owner

## Rule / Կանոն

**HY:** Registry-ում մտնում է միայն formal decision-ով բացված Platform-ը։ Յուրաքանչյուր entry պարտադիր ունի human owner, scope, status, adoption path և validation path։ Entry-ն չի ջնջվում․ այն կարող է դառնալ `Superseded`, `Retired` կամ `Archived`։

**EN:** Only a Platform opened by formal decision enters this registry. Every entry must identify a human owner, scope, status, adoption path, and validation path. Entries are never deleted; they may become `Superseded`, `Retired`, or `Archived`.

## Registered Platforms / Գրանցված Platform-ներ

| Platform | Status | Owner | Decision | Scope | Adoption path | Validation path |
|---|---|---|---|---|---|---|
| MenQ Design Platform | Active — architecture Locked | MenQ Owner | `D-024` (Locked), `D-025`, `D-027` | Shared design capability for MenQ products and systems | Product-level adoption through approved contracts | `platforms/design/validation/` validators and the Design Platform CI workflows |

## Admission checklist / Ընդունման checklist

- Reusable across more than one product or system / Վերօգտագործելի մեկից ավելի product-ում կամ system-ում
- Explicit boundary and exclusions / Explicit boundary և exclusions
- Stable contracts or interfaces / Կայուն contracts կամ interfaces
- Named human owner / Անվանված human owner
- Versioning model / Versioning-ի model
- Validation model / Validation-ի model
- Foundation alignment / Համապատասխանություն Foundation-ին
- Adoption model / Adoption-ի model
- No product-specific business logic in core / Core-ում product-specific business logic չկա
- Formal Decision System approval / Decision System-ի formal approval

<!-- END: PLATFORM_REGISTRY -->
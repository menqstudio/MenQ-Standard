# MenQ Principles / MenQ սկզբունքներ

**Status / Կարգավիճակ:** Locked / Հաստատված

## Նպատակ / Purpose

**HY:** Principles-ը MenQ Philosophy-ն վերածում է կիրառելի որոշման չափանիշների։ Դրանք պարտադիր ուղղություն են MenQ ecosystem-ի architecture-ի, products-ի, engineering-ի, design-ի, documentation-ի և AI collaboration-ի համար։

**EN:** Principles translate MenQ Philosophy into practical decision criteria. They provide mandatory direction for architecture, products, engineering, design, documentation, and AI collaboration across the MenQ ecosystem.

---

## I. Authority and Truth / Իշխանություն և ճշմարտություն

### 1. Human Authority / Մարդկային իշխանություն

**HY:** Մարդը պահում է վերջնական որոշման, approval-ի և պատասխանատվության իշխանությունը։ AI-ն օգնում է, բայց չի դառնում ինքնուրույն truth owner։

**EN:** Humans retain final authority over decisions, approval, and accountability. AI assists but does not become an independent owner of truth.

### 2. Purpose Before Action / Նպատակը՝ գործողությունից առաջ

**HY:** Կարևոր աշխատանք չի սկսվում առանց հստակ նպատակի, scope-ի և սպասվող արդյունքի։

**EN:** Important work does not begin without a clear purpose, scope, and expected outcome.

### 3. Canonical Truth / Canonical ճշմարտություն

**HY:** Յուրաքանչյուր կարևոր փաստ, սահմանում կամ որոշում ունի մեկ canonical source։ Chat-ը, AI memory-ն և տեղային պատճենները չեն փոխարինում canonical documentation-ին։

**EN:** Every important fact, definition, or decision has one canonical source. Conversations, AI memory, and local copies do not replace canonical documentation.

### 4. Explicit Ownership / Հստակ պատասխանատվություն

**HY:** Յուրաքանչյուր կարևոր համակարգ, որոշում, ռիսկ և պարտք պետք է ունենա հստակ owner։

**EN:** Every important system, decision, risk, and liability must have a clearly identified owner.

---

## II. Evidence and Enforcement / Ապացույց և enforcement

### 5. Evidence Before Assertion / Ապացույցը՝ պնդումից առաջ

**HY:** Status-ը, հաջողությունը և պատրաստ լինելը հաստատվում են դիտված արդյունքով, ոչ միայն հայտարարությամբ։

**EN:** Status, success, and readiness are established through observed results, not declarations alone.

### 6. Measurable Outcomes / Չափելի արդյունքներ

**HY:** Յուրաքանչյուր կարևոր նպատակ, փոփոխություն և performance claim պետք է ունենա չափելի արդյունք՝ baseline, KPI, target, owner և measurement cadence։ KPI-ն պետք է չափի իրական արժեքը, ոչ միայն ակտիվությունը։

**EN:** Every important goal, change, and performance claim must have a measurable outcome with a baseline, KPI, target, owner, and measurement cadence. A KPI must measure real value, not activity alone.

### 7. Rules Require Mechanisms / Կանոնները պահանջում են մեխանիզմներ

**HY:** Պարտադիր կանոնը պետք է ունենա enforcement mechanism՝ test, validator, gate, permission, review կամ այլ վերահսկողություն։

**EN:** A mandatory rule must have an enforcement mechanism such as a test, validator, gate, permission, review, or another control.

### 8. Explicit Over Implicit / Հստակը՝ թաքնվածի փոխարեն

**HY:** Կարևոր assumptions-ը, state-ը, failure-ը, dependencies-ը և սահմանները պետք է տեսանելի ու հասկանալի լինեն։

**EN:** Important assumptions, state, failures, dependencies, and boundaries must be visible and understandable.

---

## III. Systems and Change / Համակարգեր և փոփոխություն

### 9. Architecture Before Implementation / Architecture-ը՝ implementation-ից առաջ

**HY:** Սկզբում սահմանվում են համակարգի սահմանները, պատասխանատվությունները և կապերը, հետո իրականացվում է implementation-ը։

**EN:** System boundaries, responsibilities, and relationships are defined before implementation begins.

### 10. Systems Over Patches / Համակարգերը՝ patch-երից առաջ

**HY:** Նախընտրելի են reusable և ecosystem-level լուծումները, ոչ մեկանգամյա տեղային ուղղումները։

**EN:** Reusable and ecosystem-level solutions are preferred over isolated one-time patches.

### 11. Complexity Must Earn Its Place / Բարդությունը պետք է վաստակի իր տեղը

**HY:** Յուրաքանչյուր նոր layer, abstraction, dependency կամ process պետք է ունենա հստակ արդարացում։

**EN:** Every new layer, abstraction, dependency, or process must have a clear justification.

### 12. Controlled and Reversible Change / Վերահսկելի և հետադարձելի փոփոխություն

**HY:** Կարևոր փոփոխությունները պետք է լինեն սահմանափակ scope-ով, traceable, ստուգելի և հնարավորության դեպքում reversible։

**EN:** Important changes must have bounded scope, remain traceable and verifiable, and be reversible whenever practical.

---

## IV. Trust and Continuity / Վստահություն և շարունակականություն

### 13. Trust by Design / Վստահությունը՝ architecture-ի մեջ

**HY:** Security-ն, privacy-ն, permissions-ը, transparency-ն և human control-ը կառուցվում են սկզբից, ոչ ավելացվում վերջում։

**EN:** Security, privacy, permissions, transparency, and human control are designed from the beginning rather than added later.

### 14. Learn Once, Preserve Permanently / Սովորել մեկ անգամ, պահպանել մշտապես

**HY:** Հաստատված որոշումները և կրկնվող սխալներից ստացված դասերը դառնում են documentation, test, standard կամ enforcement mechanism։

**EN:** Approved decisions and lessons from recurring failures become documentation, tests, standards, or enforcement mechanisms.

### 15. Shared Foundation, Local Freedom / Ընդհանուր հիմք, տեղային ազատություն

**HY:** MenQ-ի բոլոր products-ը և systems-ը հետևում են ընդհանուր Foundation-ին, բայց կարող են ունենալ իրենց domain-specific և product-specific շերտերը։

**EN:** All MenQ products and systems follow the shared Foundation while retaining domain-specific and product-specific layers.

### 16. Bilingual Equality / Երկլեզու հավասարություն

**HY:** Հայերեն և անգլերեն canonical տարբերակները հավասարապես կարևոր են և պետք է փոխանցեն նույն ամբողջական իմաստը։

**EN:** Armenian and English canonical versions are equally authoritative and must carry the same complete meaning.

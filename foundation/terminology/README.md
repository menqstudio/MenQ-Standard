# MenQ Terminology / MenQ տերմինաբանություն

**Status / Կարգավիճակ:** Locked v1 / Հաստատված v1  
**Version / Տարբերակ:** 1.0

## Purpose / Նպատակ

**HY:** MenQ Terminology-ն սահմանում է MenQ ecosystem-ի ընդհանուր բառապաշարը, որպեսզի մարդիկ, AI համակարգերը, փաստաթղթերը և software systems-ը նույն հասկացությունները մեկնաբանեն նույն կերպ։

**EN:** MenQ Terminology defines the shared vocabulary of the MenQ ecosystem so that humans, AI systems, documentation, and software systems interpret the same concepts consistently.

## Evolution rule / Զարգացման կանոն

**HY:** v1-ը ընթացիկ authoritative glossary-ն է, բայց Terminology-ն living standard է։ Նոր տերմինները, վերանվանումները և իմաստային փոփոխությունները կարող են ավելացվել հետագայում միայն հստակ անհրաժեշտության, bilingual semantic equality-ի և traceable decision-ի միջոցով։ Հին իմաստները չեն վերագրվում կամ լուռ ջնջվում։

**EN:** v1 is the current authoritative glossary, while Terminology remains a living standard. New terms, renames, and semantic changes may be added later only through demonstrated need, bilingual semantic equality, and a traceable decision. Previous meanings are not rewritten or silently removed.

---

# I. Terminology Rules / Տերմինաբանության կանոններ

### 1. One Concept, One Canonical Term / Մեկ հասկացություն, մեկ canonical տերմին

**HY:** Միևնույն հասկացության համար սահմանվում է մեկ canonical անվանում։ Հոմանիշները չեն օգտագործվում այնպես, որ ստեղծեն տարբեր իմաստների տպավորություն։

**EN:** One canonical name is defined for each concept. Synonyms must not be used in ways that imply different meanings.

### 2. Definition Before Enforcement / Սահմանումը՝ enforcement-ից առաջ

**HY:** Տերմինը չի կարող դառնալ պարտադիր կանոնի, KPI-ի, status-ի կամ automation-ի մաս, մինչև չունենա հստակ canonical սահմանում։

**EN:** A term cannot become part of a mandatory rule, KPI, status, or automation until it has a clear canonical definition.

### 3. Bilingual Semantic Equality / Երկլեզու իմաստային հավասարություն

**HY:** Հայերեն և անգլերեն տարբերակները փոխանցում են նույն ամբողջական իմաստը։ Բառացի թարգմանությունը պարտադիր չէ, եթե այն նվազեցնում է ճշգրտությունը։

**EN:** Armenian and English versions carry the same complete meaning. Literal translation is not required when it reduces precision.

### 4. Precision Over Forced Translation / Ճշգրտությունը՝ պարտադրված թարգմանությունից առաջ

**HY:** Ընդունված technical term-ը կարող է պահպանվել անգլերենով, եթե հայերեն տարբերակը անորոշ կամ սխալ մեկնաբանություն է ստեղծում։ Առաջին օգտագործման ժամանակ տրվում է բացատրություն։

**EN:** An established technical term may remain in English when an Armenian replacement would introduce ambiguity or reduce accuracy. Its meaning is explained on first use.

### 5. Foundation Terms Cannot Be Redefined / Foundation տերմինները չեն վերասահմանվում

**HY:** Product-specific և domain-specific շերտերը կարող են մասնագիտացնել Foundation-ի տերմինները, բայց չեն կարող փոխել դրանց հիմնական իմաստը։

**EN:** Product-specific and domain-specific layers may specialize Foundation terms but may not change their core meaning.

### 6. Ambiguity Must Be Resolved / Անորոշությունը պետք է փակվի

**HY:** Երբ մի տերմին ունի մեկից ավելի հավանական իմաստ, փաստաթուղթը պարտավոր է նշել՝ որ իմաստն է կիրառվում։

**EN:** When a term has more than one plausible meaning, the document must explicitly identify the intended meaning.

### 7. Terminology Changes Are Traceable / Տերմինների փոփոխությունները traceable են

**HY:** Canonical տերմինի վերանվանումը կամ իմաստային փոփոխությունը գրանցվում է որպես decision և պահպանում է հին տերմինի հետ կապը։

**EN:** Renaming or changing the meaning of a canonical term is recorded as a decision and preserves its relationship to the previous term.

---

# II. Ecosystem Vocabulary / Էկոհամակարգի բառապաշար

### MenQ

**HY:** MenQ ecosystem-ի ընդհանուր ինքնությունն ու umbrella անունն է։ Այն ինքնին չի նշանակում միայն ընկերություն, product կամ standard։

**EN:** The shared identity and umbrella name of the MenQ ecosystem. It does not refer exclusively to the company, a product, or the Standard.

### MenQ Ecosystem

**HY:** MenQ անունով գործող ամբողջ համակարգը, որը ներառում է MenQ Studio-ն, MenQ Standard-ը և դրանց ենթակառուցվածքները։

**EN:** The complete system operating under the MenQ identity, including MenQ Studio, MenQ Standard, and their subordinate structures.

### MenQ Studio

**HY:** MenQ ecosystem-ի ընկերությունն է։ Services-ը և Products-ը պատկանում են MenQ Studio-ին։

**EN:** The company within the MenQ ecosystem. Services and Products belong to MenQ Studio.

### MenQ Standard

**HY:** MenQ ecosystem-ի canonical operating standard-ն է, որը սահմանում է՝ ինչպես ենք մտածում, որոշում, նախագծում, կառուցում, ստուգում, փաստաթղթավորում և պահպանում համակարգերը։

**EN:** The canonical operating standard of the MenQ ecosystem, defining how systems are thought through, decided, designed, built, validated, documented, and preserved.

### Foundation

**HY:** MenQ Standard-ի կայուն հիմքն է, որից բխում են մնացած բոլոր շերտերը և որին դրանք չեն կարող հակասել։

**EN:** The stable base of MenQ Standard from which all other layers derive and which they may not contradict.

### Platform

**HY:** Reusable shared capability layer է, որն օգտագործվում է մեկից ավելի products-ի, services-ի կամ systems-ի կողմից։

**EN:** A reusable shared capability layer consumed by more than one product, service, or system.

### Operating Standard

**HY:** Կրկնվող աշխատանքի կատարման, վերահսկման և validation-ի պարտադիր կանոնների ու գործընթացների համակարգ է։

**EN:** A system of mandatory rules and processes for performing, controlling, and validating repeatable work.

### Extension

**HY:** MenQ Standard-ին համապատասխանող լրացուցիչ domain-specific կամ capability-specific շերտ է, որը չի փոխում Foundation-ը։

**EN:** An additional domain-specific or capability-specific layer that conforms to MenQ Standard without modifying Foundation.

### Product

**HY:** MenQ Studio-ի կողմից ստեղծվող և շարունակաբար զարգացվող ամբողջական լուծում է, որը լուծում է իրական օգտագործողի կամ բիզնեսի խնդիր։

**EN:** A complete and continuously evolving solution created by MenQ Studio to solve a real user or business problem.

### Service

**HY:** MenQ Studio-ի կողմից հաճախորդին մատուցվող աշխատանք կամ շարունակական կարողություն է, որը կարող է օգտագործել MenQ products-ը և platforms-ը։

**EN:** Work or an ongoing capability delivered by MenQ Studio to a client, potentially using MenQ products and platforms.

---

# III. Authority and Roles / Իշխանություն և դերեր

### Owner

**HY:** Վերջնական human authority-ն է, որը հաստատում կամ մերժում է MenQ Standard-ի canonical truth-ը։

**EN:** The final human authority who approves or rejects the canonical truth of MenQ Standard.

### Human Authority

**HY:** Սկզբունք է, ըստ որի վերջնական որոշումը, approval-ը և accountability-ն մնում են մարդուն։

**EN:** The principle that final decisions, approval, and accountability remain human.

### Product Owner

**HY:** Մարդն է, որը պահում է կոնկրետ product-ի ուղղության, priority-ների և վերջնական product decisions-ի իշխանությունը։

**EN:** The human who holds authority over the direction, priorities, and final product decisions of a specific product.

### AI Collaborator

**HY:** AI համակարգ է, որը վերլուծում, առաջարկում, ստեղծում կամ իրականացնում է աշխատանք՝ մարդկային authority-ի և սահմանված scope-ի ներքո։

**EN:** An AI system that analyzes, proposes, creates, or executes work under human authority and within a defined scope.

### Agent

**HY:** Սահմանված role, objective, scope, permissions և controls ունեցող AI կամ software actor է։

**EN:** An AI or software actor with a defined role, objective, scope, permissions, and controls.

### Architect

**HY:** Դեր է, որը սահմանում և պաշտպանում է համակարգի boundaries-ը, կառուցվածքը, սկզբունքները, կապերը և երկարաժամկետ maintainability-ն։

**EN:** A role responsible for defining and protecting system boundaries, structure, principles, relationships, and long-term maintainability.

### Engineer

**HY:** Դեր է, որը architecture-ը վերածում է աշխատող implementation-ի և ապացուցում է դրա ճշտությունը tests-ի, validation-ի և իրական աշխատանքի միջոցով։

**EN:** A role that transforms architecture into working implementation and proves its correctness through tests, validation, and real operation.

---

# IV. Truth and Decision Lifecycle / Ճշմարտության և որոշման lifecycle

### Canonical Source

**HY:** Տվյալ փաստի, կանոնի կամ որոշման միակ authoritative պահպանման վայրն է։

**EN:** The single authoritative storage location for a fact, rule, or decision.

### Canonical Truth

**HY:** Canonical source-ում պահպանված, Owner-ի կողմից հաստատված ընթացիկ authoritative վիճակն է։

**EN:** The current authoritative state preserved in the canonical source and approved by the Owner.

### Idea

**HY:** Դեռ չվերլուծված կամ չհաստատված հնարավոր ուղղություն է։

**EN:** A possible direction that has not yet been analyzed or approved.

### Proposal

**HY:** Review-ի ներկայացված կառուցվածքային առաջարկ է, որը դեռ canonical որոշում չէ։

**EN:** A structured recommendation submitted for review that is not yet a canonical decision.

### Decision

**HY:** Այլընտրանքներից ընտրված հստակ ուղղություն է։

**EN:** A clearly selected direction among alternatives.

### Approval

**HY:** Human authority-ի հստակ թույլտվությունն է՝ որոշումն ընդունելու կամ առաջ տանելու համար։

**EN:** Explicit authorization from human authority to accept or advance a decision.

### Draft

**HY:** Աշխատանքային բովանդակություն է, որը կարող է փոխվել և դեռ canonical պարտադիր ուժ չունի։

**EN:** Working content that may change and does not yet carry mandatory canonical authority.

### Pending

**HY:** Սահմանված, բայց դեռ չավարտված կամ չհաստատված աշխատանքային վիճակ է։

**EN:** A defined work state that has not yet been completed or approved.

### Locked

**HY:** Owner-ի կողմից հաստատված, canonical documentation-ում պահպանված և ակտիվ authority ունեցող վիճակ է։ Locked-ը չի նշանակում անփոփոխ ընդմիշտ, բայց փոփոխությունը պահանջում է նոր traceable decision։

**EN:** A state approved by the Owner, preserved in canonical documentation, and carrying active authority. Locked does not mean permanently immutable, but any change requires a new traceable decision.

### Deprecated

**HY:** Դեռ գոյություն ունեցող, բայց նոր օգտագործման համար այլևս չառաջարկվող տարր է։

**EN:** An item that still exists but is no longer recommended for new use.

### Superseded

**HY:** Ավելի նոր canonical տարբերակով փոխարինված տարր է։

**EN:** An item replaced by a newer canonical version.

### Archived

**HY:** Պատմական պահպանման ենթակա, բայց այլևս ակտիվ authority չունեցող նյութ է։

**EN:** Material preserved for historical reference that no longer carries active authority.

---

# V. System and Evidence Vocabulary / Համակարգի և ապացույցի բառապաշար

### Architecture

**HY:** Համակարգի boundaries-ի, responsibilities-ի, relationships-ի, constraints-ի և հիմնական որոշումների կառուցվածքն է։

**EN:** The structure of a system’s boundaries, responsibilities, relationships, constraints, and major decisions.

### Implementation

**HY:** Architecture-ի կոնկրետ աշխատող իրականացումն է code-ի, configuration-ի, process-ի կամ այլ մեխանիզմի միջոցով։

**EN:** The concrete working realization of architecture through code, configuration, processes, or another mechanism.

### Mechanism

**HY:** Կանոնը, որոշումը կամ capability-ն գործողության վերածող իրական կառուցվածք է։

**EN:** A real structure that turns a rule, decision, or capability into operation.

### Enforcement Mechanism

**HY:** Խախտումը կանխող, կանգնեցնող, հայտնաբերող կամ պարտադիր տեսանելի դարձնող mechanism է։

**EN:** A mechanism that prevents, blocks, detects, or makes a violation explicitly visible.

### Verification

**HY:** Ստուգում է՝ implementation-ը համապատասխանում է արդյոք սահմանված requirement-ին։

**EN:** Determines whether an implementation conforms to a specified requirement.

### Validation

**HY:** Ստուգում է՝ աշխատող համակարգը լուծում է արդյոք նախատեսված իրական խնդիրը կամ հասնում ակնկալվող արդյունքին։

**EN:** Determines whether the working system solves the intended real problem or achieves the expected outcome.

### Evidence

**HY:** Դիտելի, traceable և վերարտադրելի հիմք է, որով հաստատվում կամ հերքվում է պնդումը։

**EN:** Observable, traceable, and reproducible support used to confirm or reject a claim.

### Done

**HY:** Վիճակ է, երբ աշխատանքը ոչ միայն գրված կամ build արված է, այլ նաև ստուգված է նախատեսված աշխատող համակարգում։

**EN:** A state in which work is not merely written or built, but has also been validated in its intended working system.

---

# VI. Measurement Vocabulary / Չափման բառապաշար

### Outcome

**HY:** Մարդու, բիզնեսի կամ համակարգի վիճակում ստեղծված իրական փոփոխությունն է։

**EN:** A real change created in the state of a person, business, or system.

### Metric

**HY:** Համակարգի, գործընթացի կամ արդյունքի չափվող ցուցանիշ է։

**EN:** A measurable indicator of a system, process, or outcome.

### KPI — Key Performance Indicator

**HY:** Նպատակի հաջողությունը գնահատող ընտրված critical metric է։ KPI-ն պետք է չափի իրական արժեքը, ոչ միայն կատարված ակտիվությունը։

**EN:** A selected critical metric used to evaluate success against an objective. A KPI must measure real value rather than activity alone.

### Baseline

**HY:** Փոփոխությունից առաջ չափված մեկնարկային վիճակն է։

**EN:** The measured starting state before a change.

### Target

**HY:** Սահմանված ժամանակահատվածում հասնելու ակնկալվող չափելի արդյունքն է։

**EN:** The measurable result expected within a defined period.

### Measurement Cadence

**HY:** Չափման, վերանայման և հաշվետվության սահմանված հաճախականությունն է։

**EN:** The defined frequency for measurement, review, and reporting.

---

## Canonical Usage Rule / Canonical օգտագործման կանոն

**HY:** MenQ canonical documentation-ում մեծատառով գրված հատուկ տերմինները՝ `Owner`, `Foundation`, `Locked`, `Platform`, `Product` և մյուսները, օգտագործվում են այս glossary-ի իմաստով, եթե փաստաթուղթը բացահայտ այլ՝ ավելի նեղ սահմանում չի նշում։

**EN:** In MenQ canonical documentation, capitalized defined terms such as `Owner`, `Foundation`, `Locked`, `Platform`, and `Product` carry the meanings established by this glossary unless a document explicitly specifies a narrower definition.

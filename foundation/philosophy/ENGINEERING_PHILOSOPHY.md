# MenQ Engineering Philosophy / MenQ ինժեներական փիլիսոփայություն

**Status / Կարգավիճակ:** Locked / Հաստատված  
**Date / Ամսաթիվ:** 2026-07-12

---

## Հայերեն

### Հիմնական դիրքորոշում

> **Ապացույցներ, ոչ պնդումներ։**  
> **Պատեր, ոչ խոստումներ։**  
> **Կոտրիր ինքդ քո բանը, մինչև աշխարհը կկոտրի քո փոխարեն։**

### 1. Architecture-ը գալիս է implementation-ից առաջ

Առանց համաձայնեցված architecture-ի implementation-ը ստեղծում է տեղային լուծումներ, իրար չհամապատասխանող մասեր և պատահական technical debt։

Սկզբում հասկանում ու սահմանում ենք համակարգը։ Հետո ենք կառուցում։

### 2. Ճշտությունը, անվտանգությունն ու պահպանելիությունը արագությունից կարևոր են

Արագությունը արժեք ունի միայն այն ժամանակ, երբ արդյունքը ճիշտ, անվտանգ և շարունակելի է։

Մենք չենք արագացնում աշխատանքը՝ ապագա մարդկանց, համակարգերի կամ հաճախորդների հաշվին։

### 3. Օրենքը առանց մեխանիզմի ցանկություն է

Եթե կանոնը միայն գրված է փաստաթղթում, այն դեռ իրական կանոն չէ։

Կանոնը գոյություն ունի այն պահից, երբ կա enforcement mechanism՝ թեստ, validator, gate, permission, policy կամ այլ պատ, որը հայտնաբերում կամ կանգնեցնում է խախտումը։

Ամեն պարտադիր կանոն պարտավոր է ունենալ իր պատը։

### 4. Կարող ես սխալվել։ Չես կարող սխալվել աննկատ

Սխալը ինժեներական աշխատանքի բնական մասն է։ Չբռնված, թաքնված կամ լուռ սխալը՝ ոչ։

Համակարգերը պետք է կառուցվեն այնպես, որ սխալները տեսանելի դառնան՝ tests, validation, logs, metrics, alerts և explicit failure states-ի միջոցով։

Hidden state-ը և silent failure-ը ինժեներական թերություններ են։

### 5. Թեստը նույնպես պետք է քննություն հանձնի

Ամենավտանգավոր թեստը ձախողվող թեստը չէ։ Ամենավտանգավորն այն թեստն է, որը միշտ անցնում է, որովհետև իրականում ոչինչ չի ստուգում։

Կրիտիկական թեստերը պետք է ապացուցեն իրենց ուժը՝ mutation, negative-case, breaker կամ կանխամտածված խախտման միջոցով։

Եթե օրգանը դիտմամբ կոտրում ենք, իսկ թեստը շարունակում է կանաչ մնալ, թեստը գործիք չէ։ Այն միայն կոստյում է։

### 6. RED-ը առաջ՝ bug fix-ի և behavior change-ի համար

Չենք գրում fix, մինչև չունենք ձախողվող ապացույց, որ խնդիրը գոյություն ունի։

Առանց RED-ի fix-ը կարող է լինել ենթադրություն, ոչ ինժեներիա։

RED ապացույցն ինքն էլ պետք է ստուգվի, որպեսզի հաստատվի, որ այն կարդում և չափում է ճիշտ վարքը։

### 7. Մեկ աղբյուր, զրո կրկնվող hardcoded truth

Արժեքը, կանոնը կամ սահմանումը, որը անկախ ապրում է երկու տեղում, արդեն ստեղծում է երկու ճշմարտություն։

Shared, configurable և domain-critical արժեքները պետք է ունենան մեկ canonical source, իսկ մնացած ներկայացումները լինեն ածանցյալ։

Design values-ը գալիս են tokens-ից։ Paths-ը, environment values-ը և configuration-ը չեն hardcode արվում մեքենայի կամ միջավայրի ենթադրությամբ։

Portability-ն ապացուցված չէ, մինչև համակարգն աշխատում է միայն հեղինակի մեքենայում։

### 8. Աշխատողի վրա կառուցիր, մի՛ վերագծիր

Նոր բան կառուցելուց առաջ գտնում ենք՝ ինչն արդեն գոյություն ունի, աշխատում է և հաստատված է։

Անհիմն rewrite-ը ստեղծում է fork և կորցնում է նախկին աշխատանքի ընթացքում ձեռք բերված craft-ը, edge case-երը և վճարված որոշումները։

Rewrite-ը թույլատրելի է միայն հստակ պատճառի և ապացուցված օգուտի դեպքում։

### 9. «Արված» նշանակում է տեսած աշխատող համակարգում

«Թեստերն անցան», «կոմպիլյացվեց» կամ «build-ը կանաչ է» արտահայտությունները դեռ չեն նշանակում, որ աշխատանքն ավարտված է։

Աշխատանքը պատրաստ է, երբ այն դիտվել և ստուգվել է նախատեսված գործող համակարգում՝ իրական կամ իրատեսական մուտքով։

Մինչ այդ այն validated implementation չէ։

### 10. Անկեղծությունը հարմարավետությունից կարևոր է

Եթե ինչ-որ բան ձախողվել է, դրա մասին ասում ենք ուղիղ՝ ապացույցով և ելքով։

Չկա «համարյա պատրաստ է», եթե կարևոր մասը կարմիր է։ Չկա գեղեցիկ ամփոփում, որը թաքցնում է failure-ը։

Լռությունը, սխալը թաքցնելը և անորոշ status-ը արգելված են։

### 11. Համակարգերը կառուցվում են modular, reusable և observable

Յուրաքանչյուր կարևոր օրգան պետք է ունենա հստակ սահման, պատասխանատվություն և interface։

Reusable-ը չի նշանակում վաղաժամ abstraction։ Այն նշանակում է՝ ճիշտ սահմանված համակարգ, որը կարելի է հասկանալ, փորձարկել, փոխարինել և կրկին օգտագործել։

Կրիտիկական գործողությունները պետք է լինեն observable, որպեսզի հնարավոր լինի հասկանալ՝ ինչ է կատարվել, ինչու և որտեղ։

### 12. Automation-ը մնում է վերահսկելի և reversible

Automation-ը պետք է հեռացնի կրկնվող աշխատանքը, ոչ մարդկային վերահսկողությունը։

Կրիտիկական ավտոմատ գործողությունները պետք է ունենան scope, permissions, logs, limits և անհրաժեշտության դեպքում approval կամ rollback mechanism։

Ավտոմատացումը, որը հնարավոր չէ հասկանալ, կանգնեցնել կամ հետ շրջել, անվտանգ automation չէ։

### 13. Բարդությունն ու technical debt-ը պարտք են

Ամեն նոր layer, abstraction, dependency կամ օրգան պետք է վաստակի իր տեղը։

Բարդությունը չեզոք չէ։ Այն ավելացնում է հասկանալու, փորձարկելու, պահպանելու և փոխելու գինը։

Technical debt-ը կարող է լինել գիտակցված որոշում, եթե այն բացահայտ է, հիմնավորված, պատասխանատու ունի և հետագա գործողություն։ Այն չի կարող լինել պատահական կամ թաքնված արդյունք։

### 14. Ամեն կարևոր փոփոխություն ստուգելի և traceable է

Կրիտիկական փոփոխությունը պետք է կապվի իր խնդրի, որոշման, implementation-ի, validation-ի և արդյունքի հետ։

Կարևոր architecture որոշումները չեն մնում միայն կոդում կամ chat-ում։ Դրանք փաստաթղթավորվում են canonical source-ում։

Մենք պետք է կարողանանք պատասխանել՝ ինչ փոխվեց, ինչու, ով հաստատեց և ինչպես ապացուցվեց։

### 15. Ամեն սխալ՝ մեկ անգամ

Նույն տեսակի սխալը երկրորդ անգամ կրկնվելու դեպքում խնդիրը այլևս միայն մարդու սխալը չէ։ Դա համակարգի բաց թողած դասն է։

Կրկնվող failure-ը պետք է դառնա test, validation, lint rule, automation, checklist կամ այլ enforcement mechanism։

Այն, ինչ չի սովորեցվել համակարգին, ամբողջությամբ չի սովորել նաև թիմը։

---

## English

### Core position

> **Evidence over assertion.**  
> **Walls over promises.**  
> **Break your own thing first—or the world will break it for you.**

### 1. Architecture comes before implementation

Implementation without an agreed architecture creates local solutions, incompatible parts, and accidental technical debt.

We first understand and define the system. Then we build it.

### 2. Correctness, security, and maintainability matter more than speed

Speed has value only when the result is correct, secure, and sustainable.

We do not accelerate delivery at the expense of future people, systems, or customers.

### 3. A law without a mechanism is a wish

A rule that exists only in documentation is not yet a real rule.

A rule becomes real when it has an enforcement mechanism: a test, validator, gate, permission, policy, or another wall that detects or stops a violation.

Every mandatory rule owes a wall.

### 4. You may be wrong; you may not be wrong uncaught

Errors are a natural part of engineering. Uncaught, hidden, or silent errors are not.

Systems must be designed to expose errors through tests, validation, logs, metrics, alerts, and explicit failure states.

Hidden state and silent failure are engineering defects.

### 5. A test must pass its own examination

The most dangerous test is not a failing test. It is a test that always passes because it verifies nothing meaningful.

Critical tests must prove their strength through mutation, negative cases, breakers, or deliberate violations.

If we intentionally break the organ and the test remains green, the test is not a tool. It is only a costume.

### 6. RED comes first for bug fixes and behavior changes

We do not write a fix until we have failing evidence proving that the problem exists.

Without RED, a fix may be a story rather than engineering.

The RED evidence must also be validated to ensure that it observes and measures the correct behavior.

### 7. One source of truth, zero duplicated hardcoded truth

A value, rule, or definition that lives independently in two places has already created two truths.

Shared, configurable, and domain-critical values must have one canonical source, with all other representations derived from it.

Design values come from tokens. Paths, environment values, and configuration are not hardcoded around assumptions about one machine or environment.

Portability is not proven while a system works only on its author’s machine.

### 8. Build on what works; do not redraw it

Before building something new, we identify what already exists, works, and has been approved.

An unjustified rewrite creates a fork and loses the craft, edge cases, and paid-for decisions accumulated in the existing work.

A rewrite is justified only by a clear reason and demonstrated benefit.

### 9. “Done” means observed in a working system

“Tests passed,” “it compiled,” or “the build is green” does not yet mean that the work is complete.

Work is ready when it has been observed and validated in its intended working system with real or realistic input.

Before that, it is not a validated implementation.

### 10. Honesty matters more than comfort

When something fails, we state it directly with evidence and output.

There is no “almost ready” when a critical part is red. There is no polished summary that hides a failure.

Silence, concealed errors, and ambiguous status are forbidden.

### 11. Systems are modular, reusable, and observable

Every important organ must have a clear boundary, responsibility, and interface.

Reusable does not mean premature abstraction. It means a correctly bounded system that can be understood, tested, replaced, and reused.

Critical operations must be observable so that we can determine what happened, why it happened, and where.

### 12. Automation remains controlled and reversible

Automation must remove repetitive work, not human control.

Critical automated actions must have scope, permissions, logs, limits, and—when necessary—approval or rollback mechanisms.

Automation that cannot be understood, stopped, or reversed is not safe automation.

### 13. Complexity and technical debt are liabilities

Every new layer, abstraction, dependency, or organ must earn its place.

Complexity is not neutral. It increases the cost of understanding, testing, maintaining, and changing a system.

Technical debt may be a conscious decision when it is explicit, justified, owned, and connected to a follow-up action. It may not be accidental or hidden.

### 14. Every important change is verifiable and traceable

A critical change must connect its problem, decision, implementation, validation, and result.

Important architectural decisions do not remain only in code or conversation. They are documented in the canonical source.

We must be able to answer what changed, why it changed, who approved it, and how it was proven.

### 15. Every mistake happens once

When the same class of error occurs a second time, the problem is no longer only human error. It is a lesson the system failed to preserve.

A recurring failure must become a test, validation rule, lint rule, automation, checklist, or another enforcement mechanism.

What has not been taught to the system has not been fully learned by the team.

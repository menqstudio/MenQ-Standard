# MenQ Decision System / MenQ որոշումների համակարգ

**Status / Կարգավիճակ:** Locked v1 / Հաստատված v1  
**Version / Տարբերակ:** 1.0

## Core Rule / Հիմնական կանոն

> **HY:** Որոշումը canonical չի դառնում, մինչև չունենա authority, evidence, approval և documentation։  
> **EN:** A decision does not become canonical until it has authority, evidence, approval, and documentation.

---

## 1. Purpose / Նպատակ

**HY:** MenQ Decision System-ը սահմանում է՝ որ հարցերն են պահանջում formal decision, ինչպես է proposal-ը դառնում approved և locked decision, ինչ evidence, review, authority, validation և documentation է անհրաժեշտ, և ինչպես են decisions-ը փոխվում, supersede կամ retire արվում։

**EN:** MenQ Decision System defines which matters require a formal decision, how a proposal becomes an approved and locked decision, what evidence, review, authority, validation, and documentation are required, and how decisions are changed, superseded, or retired.

---

## 2. Boundary / Սահման

- **Governance** → ով ունի որոշելու authority / who holds decision authority.
- **Decision System** → ինչպես է որոշումը անցնում lifecycle-ով / how a decision moves through its lifecycle.
- **Documentation** → որտեղ և ինչպես է canonical record-ը պահպանվում / where and how the canonical record is preserved.
- **AI Collaboration** → ինչպես է AI-ն մասնակցում analysis-ին, drafting-ին և review-ին / how AI participates in analysis, drafting, and review.

---

## 3. Formal Decision Trigger / Formal decision-ի trigger

**HY:** Formal decision է պահանջվում, երբ փոփոխությունը՝

1. ազդում է Foundation-ի վրա,
2. ստեղծում կամ փոխում է ecosystem-wide կանոն,
3. փոխում է architecture, ownership կամ authority,
4. ազդում է մեկից ավելի product-ի կամ system-ի վրա,
5. ունի բարձր security, privacy, legal, financial կամ customer risk,
6. դժվար է հետ շրջել,
7. փոխում է canonical terminology-ն,
8. ստեղծում է երկարաժամկետ commitment կամ technical debt,
9. լուծում է կրկնվող կամ վիճելի հարց,
10. պետք է հիշվի ապագա մարդկանց ու AI համակարգերի կողմից։

**EN:** A formal decision is required when a change:

1. affects Foundation,
2. creates or changes an ecosystem-wide rule,
3. changes architecture, ownership, or authority,
4. affects more than one product or system,
5. carries significant security, privacy, legal, financial, or customer risk,
6. is difficult to reverse,
7. changes canonical terminology,
8. creates a long-term commitment or technical debt,
9. resolves a recurring or disputed question,
10. must be remembered by future humans and AI systems.

Routine, reversible work already governed by an approved standard may proceed without a new formal decision.

---

## 4. Decision Classes / Որոշումների դասեր

| Class | Name | Definition / Սահմանում |
|---|---|---|
| `C0` | Routine | Existing standard-ի ներսում low-risk, reversible action; no new canonical decision. |
| `C1` | Local | One component, small workflow, or bounded local scope. |
| `C2` | Product or Domain | One product, platform, service, or domain. |
| `C3` | Cross-System | Multiple products, platforms, or operational areas. |
| `C4` | Foundation or Ecosystem | Foundation, MenQ Standard hierarchy, ownership, authority model, or ecosystem-wide mandatory rule. |

---

## 5. Risk Levels / Ռիսկի մակարդակներ

| Level | Meaning / Իմաստ |
|---|---|
| `R0` | Negligible and easily reversible / աննշան և հեշտ հետադարձելի |
| `R1` | Low impact and bounded / ցածր ազդեցություն և սահմանափակ scope |
| `R2` | Moderate impact or coordination cost / միջին ազդեցություն կամ coordination cost |
| `R3` | High impact, sensitive, or difficult to reverse / բարձր ազդեցություն, զգայուն կամ դժվար հետադարձելի |
| `R4` | Critical, irreversible, legal, financial, security, privacy, or ecosystem-level / կրիտիկական, irreversible կամ ecosystem-level |

**HY:** Decision class-ը և risk level-ը տարբեր չափումներ են։ Higher risk-ը override է անում lower class-ի approval պահանջը։

**EN:** Decision class and risk level are separate dimensions. Higher risk overrides the approval requirement of a lower decision class.

---

## 6. Decision Lifecycle / Որոշման lifecycle

```text
Signal
↓
Explore
↓
Proposal
↓
Review
↓
Decision
↓
Approval
↓
Document
↓
Implement
↓
Validate
↓
Lock
↓
Monitor
↓
Review / Supersede / Retire
```

### 6.1 Signal / Ազդակ

**HY:** Հայտնաբերվում է problem, opportunity, conflict, failure կամ requirement։  
**EN:** A problem, opportunity, conflict, failure, or requirement is identified.

### 6.2 Explore / Ուսումնասիրում

**HY:** Հավաքվում են context-ը, constraints-ը, alternatives-ը, risks-ը և assumptions-ը։  
**EN:** Context, constraints, alternatives, risks, and assumptions are collected.

### 6.3 Proposal / Առաջարկ

**HY:** Ընտրված ուղղությունը ներկայացվում է review-ի։ Proposal-ը դեռ canonical truth չէ։  
**EN:** The selected direction is submitted for review. A proposal is not yet canonical truth.

### 6.4 Review / Վերանայում

**HY:** Ստուգվում են Foundation alignment-ը, evidence-ը, alternatives-ը, risk-ը, reversibility-ն, maintainability-ն, measurable outcome-ը և approval path-ը։  
**EN:** Foundation alignment, evidence, alternatives, risk, reversibility, maintainability, measurable outcome, and the approval path are examined.

### 6.5 Decision / Որոշում

**HY:** Հստակ ձևակերպվում են ընտրված ուղղությունը, scope-ը, trade-offs-ը և մերժված alternatives-ի պատճառները։  
**EN:** The selected direction, scope, trade-offs, and reasons for rejecting alternatives are stated explicitly.

### 6.6 Approval / Հաստատում

**HY:** Decision-ը approve կամ reject է անում Governance-ով լիազորված մարդը։ AI-ն final approval authority չունի։  
**EN:** A human authorized through Governance approves or rejects the decision. AI has no final approval authority.

### 6.7 Document / Փաստաթղթավորում

**HY:** Approved decision-ը տեղափոխվում է canonical repository։ Approval առանց documentation-ի ամբողջական lock չէ։  
**EN:** The approved decision is transferred to the canonical repository. Approval without documentation is not a complete lock.

### 6.8 Implement / Իրականացում

**HY:** Decision-ը իրականացվում է approved scope-ի ներսում։  
**EN:** The decision is implemented within its approved scope.

### 6.9 Validate / Վավերացում

**HY:** Ստուգվում են implementation conformity-ն և իրական outcome-ը։  
**EN:** Implementation conformity and the real outcome are validated.

### 6.10 Lock / Lock

**HY:** Decision-ը ստանում է active canonical authority միայն required approval, documentation և validation-ից հետո։  
**EN:** A decision receives active canonical authority only after required approval, documentation, and validation.

### 6.11 Monitor / Դիտարկում

**HY:** Հետևվում են KPI-ները, risks-ը, side effects-ը և assumptions-ը։  
**EN:** KPIs, risks, side effects, and assumptions are monitored.

### 6.12 Review, Supersede or Retire / Վերանայել, փոխարինել կամ դադարեցնել

**HY:** Decision-ը վերանայվում է review date-ի կամ trigger-ի դեպքում և կարող է մնալ active, supersede կամ retire արվել։  
**EN:** A decision is reviewed on its review date or trigger and may remain active, be superseded, or be retired.

---

## 7. Decision Statuses / Որոշման status-ներ

| Status | Meaning / Իմաստ |
|---|---|
| `Idea` | Unexplored possible direction / չուսումնասիրված հնարավոր ուղղություն |
| `Exploring` | Evidence and alternatives are being collected / evidence և alternatives են հավաքվում |
| `Proposed` | Submitted for formal review / ներկայացված formal review-ի |
| `In Review` | Review is active / review-ը ընթացքի մեջ է |
| `Changes Requested` | Returned for revision / վերադարձված փոփոխության |
| `Approved` | Direction approved; implementation or documentation may remain / ուղղությունը հաստատված է, բայց աշխատանքը կարող է չավարտված լինել |
| `Rejected` | Not accepted; rationale preserved / մերժված է, պատճառը պահպանվում է |
| `Implementing` | Approved decision is being executed / իրականացվում է |
| `Validating` | Implementation and outcome are being validated / implementation-ն ու outcome-ը ստուգվում են |
| `Locked` | Approved, documented, and sufficiently validated / approved, documented և բավարար validated |
| `Exception` | Temporary bounded deviation / ժամանակավոր սահմանափակ շեղում |
| `Superseded` | Replaced by a newer canonical decision / փոխարինված է նոր decision-ով |
| `Retired` | No longer active; replacement not required / այլևս active չէ |
| `Archived` | Historical reference only / միայն պատմական reference |

---

## 8. Approval Matrix / Approval-ի մատրիցա

| Decision | Minimum authority / Նվազագույն authority |
|---|---|
| `C0 / R0–R1` | Existing delegated execution authority |
| `C1 / R0–R2` | Relevant human owner or delegated approver |
| `C2 / R0–R2` | Product, Platform, Service, or Domain Owner |
| Any `R3` | Explicit authorized human approver |
| Any `R4` | Owner or explicitly reserved high-risk authority |
| `C3` | Cross-system delegated authority or Owner |
| `C4` | Owner, `G4` |
| Foundation change | Owner, `G4` |
| AI authority expansion | Authorized human; Foundation-level expansion requires Owner |

---

## 9. Required Decision Record / Պարտադիր decision record

```text
Decision ID:
Title:
Status:
Date:
Decision class:
Risk level:
Owner:
Proposer:
Reviewer:
Approver:
Scope:
Problem:
Context:
Decision:
Alternatives considered:
Why this option:
Expected outcome:
KPI / success criteria:
Risks:
Mitigations:
Reversibility / rollback:
Dependencies:
Implementation owner:
Validation method:
Review trigger or date:
Affected canonical files:
Supersedes:
Superseded by:
Evidence links:
```

**HY:** Low-risk decision-ների record-ը կարող է կարճ լինել, բայց core fields-ը չեն բաց թողնվում։  
**EN:** Low-risk decision records may be concise, but core fields must not be omitted.

---

## 10. Evidence Standard / Ապացույցի ստանդարտ

**HY:** Evidence-ը պետք է լինի relevant, current, traceable, reproducible և risk-ին համաչափ։ User feedback-ը, observed behavior-ը, tests-ը, metrics-ը, incident data-ն, prototypes-ը, constraints-ը, financial analysis-ը և expert review-ն կարող են evidence լինել։ Popularity-ը, confidence-ը կամ համոզիչ AI wording-ը evidence չեն։

**EN:** Evidence must be relevant, current, traceable, reproducible, and proportionate to risk. User feedback, observed behavior, tests, metrics, incident data, prototypes, constraints, financial analysis, and expert review may serve as evidence. Popularity, confidence, or persuasive AI wording are not evidence.

---

## 11. Alternatives Rule / Այլընտրանքների կանոն

**HY:** `C2–C4` կամ `R3–R4` decision-ը պետք է ցույց տա դիտարկված alternatives-ը, դրանց մերժման պատճառները և ընտրված տարբերակի ընդունված trade-off-ը։  
**EN:** A `C2–C4` or `R3–R4` decision must identify considered alternatives, reasons for rejecting them, and the accepted trade-off of the selected option.

---

## 12. Assumption Rule / Ենթադրությունների կանոն

**HY:** Material assumption-ը պետք է explicit լինի և ունենա validation method, owner, deadline կամ trigger և failure consequence։ Չստուգված assumption-ը fact չի ներկայացվում։

**EN:** A material assumption must be explicit and have a validation method, owner, deadline or trigger, and failure consequence. An unvalidated assumption must not be represented as fact.

---

## 13. Reversibility Rule / Հետադարձելիության կանոն

**HY:** Նախընտրելի է reversible decision, երբ irreversible commitment-ը անհրաժեշտ չէ։ `R3–R4` decision-ը պետք է ունենա rollback plan, containment plan, staged rollout, pilot, kill switch կամ explicit irreversible-risk acceptance։

**EN:** Reversible decisions are preferred when irreversible commitment is unnecessary. An `R3–R4` decision must include a rollback plan, containment plan, staged rollout, pilot, kill switch, or explicit acceptance of irreversible risk.

---

## 14. Decision Gates / Որոշման gates

1. **Problem Gate** — problem-ը հստակ է և արժե լուծել / the problem is clear and worth solving.
2. **Evidence Gate** — evidence-ը բավարար է class-ի և risk-ի համար / evidence is sufficient for the class and risk.
3. **Architecture Gate** — Foundation alignment-ը և boundaries-ը պահպանված են / Foundation alignment and boundaries are preserved.
4. **Authority Gate** — approver-ը ունի անհրաժեշտ Governance authority / the approver has the required Governance authority.
5. **Implementation Gate** — scope-ը, owner-ը, dependencies-ը և rollback-ը հստակ են / scope, owner, dependencies, and rollback are clear.
6. **Validation Gate** — success criteria-ն և validation method-ը սահմանված են / success criteria and validation method are defined.
7. **Canonical Gate** — decision-ը ճիշտ տեղում documented և linked է / the decision is documented and linked in the correct canonical location.

**HY:** Decision-ը չի կարող `Locked` դառնալ, եթե required gate-ը RED է։  
**EN:** A decision cannot become `Locked` while a required gate is RED.

---

## 15. Gate Results / Gate արդյունքներ

- **GREEN** — requirement-ը բավարար է, կարելի է առաջ գնալ / the requirement is satisfied and work may proceed.
- **YELLOW** — կա accepted uncertainty կամ follow-up obligation; պետք է ունենա owner և closure condition / accepted uncertainty or follow-up obligation exists; it must have an owner and closure condition.
- **RED** — critical requirement-ը չի կատարվել; decision-ը չի առաջ գնում / a critical requirement is unmet; the decision does not advance.

**HY:** Մարդը կամ AI-ն չի կարող RED-ը պարզապես անվանել GREEN։  
**EN:** Neither a human nor AI may simply relabel RED as GREEN.

---

## 16. Dissent and Challenge / Անհամաձայնություն և challenge

**HY:** Reviewer-ը challenge է անում թույլ evidence-ը, hidden assumptions-ը, authority mismatch-ը, missing rollback-ը, KPI gaming-ը, architecture drift-ը և unnecessary complexity-ն։ High-risk decision-ի dissent-ը պահպանվում է։ Approver-ը կարող է dissent-ի դեմ գնալ միայն explicit rationale-ով։

**EN:** A reviewer challenges weak evidence, hidden assumptions, authority mismatch, missing rollback, KPI gaming, architecture drift, and unnecessary complexity. Dissent on a high-risk decision is preserved. An approver may override dissent only with explicit rationale.

---

## 17. Rejection Rule / Մերժման կանոն

**HY:** Meaningful analysis ունեցող rejected proposal-ը չի ջնջվում։ Պահպանվում են proposal-ը, rejection reason-ը, հիմնական evidence-ը և reopening condition-ը, եթե կա։

**EN:** A rejected proposal containing meaningful analysis is not deleted. The proposal, rejection reason, core evidence, and any reopening condition are preserved.

---

## 18. Change and History Rule / Փոփոխության և history-ի կանոն

**HY:** Locked decision-ը չի խմբագրվում այնպես, կարծես հին որոշումը երբեք չի եղել։ Material change-ի համար ստեղծվում է նոր decision, նշվում է հինը, բացատրվում է change reason-ը, իսկ հինը ստանում է `Superseded` կամ `Retired` status։ Minor typo կամ formatting correction-ը նոր decision չի պահանջում, եթե իմաստը չի փոխվում։

**EN:** A locked decision is not edited as though the previous decision never existed. A material change requires a new decision that references the old one and explains the reason for change; the old decision becomes `Superseded` or `Retired`. Minor typo or formatting corrections do not require a new decision when meaning is unchanged.

---

## 19. Exception Decision / Բացառության որոշում

**HY:** Exception record-ը նշում է rule-ը, reason-ը, scope-ը, owner-ը, risk-ը, start date-ը, expiry կամ review date-ը, compensating controls-ը և closure plan-ը։ Expired exception-ը չի շարունակում գործել լուռ։

**EN:** An exception record identifies the rule, reason, scope, owner, risk, start date, expiry or review date, compensating controls, and closure plan. An expired exception does not continue silently.

---

## 20. Emergency Decision / Արտակարգ որոշում

**HY:** Emergency դեպքում թույլատրվում է minimum necessary action, երբ ուշացումը մեծացնում է վնասը։ Պարտադիր են evidence preservation-ը, human escalation-ը, containment-ը, post-action review-ը, retrospective decision record-ը և ratify, correct կամ rollback արդյունքը։ Emergency process-ը routine shortcut չէ։

**EN:** In an emergency, the minimum necessary action is permitted when delay increases harm. Evidence preservation, human escalation, containment, post-action review, a retrospective decision record, and a ratify, correct, or rollback outcome are required. The emergency process is not a routine shortcut.

---

## 21. AI Participation / AI-ի մասնակցություն

**HY:** AI-ն կարող է հայտնաբերել decision need, հավաքել context, առաջարկել alternatives, draft անել record-ը, challenge անել assumptions-ը, ստուգել consistency-ն և օգնել validation-ին։ AI-ն չի կարող իրեն authority տալ, փոխարինել final human approval-ը, թաքցնել uncertainty-ն, fake evidence ստեղծել, իր proposal-ը ինքնուրույն lock անել կամ canonical history rewrite անել։

**EN:** AI may identify a decision need, gather context, propose alternatives, draft the record, challenge assumptions, check consistency, and assist validation. AI may not grant itself authority, replace final human approval, hide uncertainty, create fake evidence, lock its own proposal, or rewrite canonical history.

---

## 22. Decision Metrics / Որոշումների KPI-ներ

**HY:** Decision System-ը կարող է չափվել proposal-to-decision time-ով, reversal rate-ով, reopened decisions-ով, owner կամ KPI չունեցող decisions-ով, expired exceptions-ով, unreviewed high-risk decisions-ով, implementation-to-outcome gap-ով, repeated debates-ով և undocumented approved changes-ով։ KPI-ն չի խրախուսում արագ approval quality-ի հաշվին։

**EN:** The Decision System may be measured through proposal-to-decision time, reversal rate, reopened decisions, decisions without an owner or KPI, expired exceptions, unreviewed high-risk decisions, the implementation-to-outcome gap, repeated debates, and undocumented approved changes. KPIs must not encourage fast approval at the expense of quality.

---

## 23. Review Triggers / Վերանայման triggers

**HY:** Locked decision-ը վերանայվում է, երբ KPI-ն չի հասնում target-ին, assumption-ը սխալ է, environment-ը կամ law-ը փոխվում է, incident է լինում, cost կամ complexity-ն աճում է, նոր evidence է հայտնվում, scope-ը փոխվում է, related Foundation decision է փոխվում կամ review date-ը հասնում է։

**EN:** A locked decision is reviewed when a KPI misses its target, an assumption proves false, the environment or law changes, an incident occurs, cost or complexity rises materially, new evidence appears, scope changes, a related Foundation decision changes, or the review date arrives.

---

## 24. Decision ID Rule / Decision ID-ի կանոն

**HY:** MenQ Standard ecosystem-level decisions-ը ստանում են sequential `D-001`, `D-002`, … ID-ներ։ Product կամ domain-specific logs-ը կարող են օգտագործել namespace՝ `BROPS-D-001`, `DESIGN-D-001`, `PLATFORM-D-001`։ ID-ն չի վերօգտագործվում և history-ից չի ջնջվում։

**EN:** MenQ Standard ecosystem-level decisions receive sequential IDs such as `D-001`, `D-002`, and so on. Product or domain-specific logs may use namespaces such as `BROPS-D-001`, `DESIGN-D-001`, or `PLATFORM-D-001`. An ID is never reused or deleted from history.

---

## 25. Final Rule / Վերջնական կանոն

> **HY:** Չփաստաթղթավորված approval-ը հիշողություն է, ոչ standard։ Չստուգված implementation-ը աշխատանք է, ոչ ապացուցված արդյունք։  
> **EN:** Undocumented approval is memory, not a standard. Unvalidated implementation is work, not a proven outcome.

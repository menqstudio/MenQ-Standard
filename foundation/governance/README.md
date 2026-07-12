# MenQ Governance / MenQ կառավարում

**Status / Կարգավիճակ:** Locked v1 / Հաստատված v1  
**Version / Տարբերակ:** 1.0

## Core Rule / Հիմնական կանոն

> **HY:** Իշխանությունը մարդկային է, հստակ, սահմանափակ scope-ով, traceable և հետկանչելի։  
> **EN:** Authority is human, explicit, scoped, traceable, and revocable.

---

# 1. Purpose / Նպատակ

**HY:** MenQ Governance-ը սահմանում է՝

- ով ունի որոշելու իշխանություն,
- ինչ սահմաններում կարող է այդ իշխանությունն օգտագործվել,
- ինչպես է իշխանությունը փոխանցվում,
- ով է պատասխանատու արդյունքի համար,
- երբ է անհրաժեշտ Owner-ի approval-ը,
- ինչպես են լուծվում authority conflict-ները,
- ինչ սահմաններ ունեն AI համակարգերը։

**EN:** MenQ Governance defines:

- who has decision authority,
- the boundaries within which that authority may be exercised,
- how authority is delegated,
- who is accountable for outcomes,
- when Owner approval is required,
- how authority conflicts are resolved,
- the limits placed on AI systems.

---

# 2. Governance Boundary / Governance-ի սահման

**HY:** Governance-ը պատասխանում է՝

> **Ո՞վ կարող է որոշել և ի՞նչ սահմաններում։**

Governance-ը չի սահմանում որոշման ամբողջ workflow-ը։ Այդ հարցը պատկանում է `Decision System` chapter-ին։

- Governance → ով ունի authority
- Decision System → ինչպես է որոշումը ընդունվում
- Documentation → որտեղ է որոշումը պահպանվում
- AI Collaboration → ինչպես է AI-ն մասնակցում

**EN:** Governance answers:

> **Who may decide, and within what boundaries?**

Governance does not define the complete decision workflow. That belongs to the `Decision System` chapter.

- Governance → who holds authority
- Decision System → how a decision is made
- Documentation → where the decision is preserved
- AI Collaboration → how AI participates

---

# 3. Governance Principles / Governance-ի սկզբունքներ

## 3.1 Human Authority / Մարդկային իշխանություն

**HY:** Վերջնական authority-ն պատկանում է մարդուն։ AI-ն կարող է վերլուծել, առաջարկել, ստուգել և սահմանված scope-ում իրականացնել, բայց չի դառնում ինքնուրույն canonical truth owner։

**EN:** Final authority belongs to humans. AI may analyze, propose, validate, and execute within a defined scope, but it does not become an independent owner of canonical truth.

## 3.2 Explicit Authority / Հստակ authority

**HY:** Authority-ն գոյություն չունի ենթադրությամբ։ Այն պետք է բացահայտ սահմանված լինի role-ի, scope-ի և թույլատրված գործողությունների միջոցով։

**EN:** Authority does not exist by assumption. It must be explicitly defined through a role, scope, and permitted actions.

## 3.3 Least Necessary Authority / Նվազագույն անհրաժեշտ authority

**HY:** Յուրաքանչյուր մարդ, AI agent կամ system ստանում է միայն իր նպատակը կատարելու համար անհրաժեշտ authority-ն։

**EN:** Every human, AI agent, or system receives only the authority necessary to fulfill its purpose.

## 3.4 Authority and Accountability Stay Connected / Authority-ն և accountability-ն կապված են

**HY:** Ով ունի որոշելու կամ իրականացնելու authority, պետք է ունենա նաև հստակ accountability։ Չի թույլատրվում authority առանց պատասխանատվության կամ պատասխանատվություն առանց բավարար authority-ի։

**EN:** Whoever holds authority to decide or execute must also carry explicit accountability. Authority without accountability, or accountability without sufficient authority, is not permitted.

## 3.5 Delegation Is Scoped / Delegation-ը սահմանափակ scope ունի

**HY:** Delegation-ը փոխանցում է որոշակի decision rights, ոչ անսահման իշխանություն։ Delegated authority-ն գործում է միայն սահմանված domain-ի, գործողությունների, risk limit-ի և ժամանակահատվածի ներսում։

**EN:** Delegation transfers specific decision rights, not unlimited authority. Delegated authority operates only within its defined domain, actions, risk limit, and time period.

## 3.6 No Silent Authority / Չկա լուռ authority

**HY:** Պաշտոնը, seniority-ն, technical access-ը կամ system permission-ը ինքնուրույն approval authority չեն ստեղծում։

**EN:** Position, seniority, technical access, or system permission does not independently create approval authority.

## 3.7 Critical Decisions Require Independent Challenge / Կրիտիկական որոշումները պահանջում են անկախ challenge

**HY:** High-risk որոշումների դեպքում proposer-ը, reviewer-ը և approver-ը հնարավորության դեպքում տարբեր դերեր են։ Փոքր թիմում նույն մարդը կարող է մի քանի դեր կատարել, բայց role overlap-ը պետք է բացահայտ լինի, իսկ review evidence-ը՝ պահպանված։

**EN:** For high-risk decisions, the proposer, reviewer, and approver should be separate roles whenever practical. In a small team, one person may perform multiple roles, but the overlap must be explicit and review evidence must be preserved.

## 3.8 AI Cannot Self-Approve / AI-ն չի կարող ինքն իրեն approve անել

**HY:** AI-ն չի կարող վերջնական approve անել իր առաջարկը, փոփոխությունը կամ գործողությունը, երբ պահանջվում է մարդկային approval։ Մի AI agent-ի review-ը չի փոխարինում human authority-ին։

**EN:** AI cannot give final approval to its own proposal, change, or action when human approval is required. Review by another AI agent does not replace human authority.

## 3.9 Authority Is Revocable / Authority-ն հետկանչելի է

**HY:** Delegated authority-ն կարող է սահմանափակվել, ժամանակավորապես դադարեցվել կամ հետ կանչվել՝ risk-ի, failure-ի, scope change-ի կամ Owner-ի որոշման հիման վրա։

**EN:** Delegated authority may be restricted, suspended, or revoked because of risk, failure, scope change, or an Owner decision.

## 3.10 Governance Is Traceable / Governance-ը traceable է

**HY:** Պետք է հնարավոր լինի պարզել՝

- ով ուներ authority,
- ինչ որոշում ընդունվեց,
- ինչ scope-ում,
- ինչ evidence-ի հիման վրա,
- ով approve արեց,
- երբ է authority-ն կամ որոշումը վերանայվում։

**EN:** It must be possible to determine:

- who held authority,
- what decision was made,
- within what scope,
- based on what evidence,
- who approved it,
- when the authority or decision will be reviewed.

---

# 4. Governance Roles / Governance-ի դերեր

Roles-ը authority definitions են, ոչ պարտադիր job titles։

## 4.1 Owner

**HY:** Owner-ը MenQ Standard-ի և ecosystem-level canonical truth-ի վերջնական human authority-ն է։

Owner-ը՝

- approve կամ reject է անում Foundation փոփոխությունները,
- սահմանում և հետ է կանչում delegated authority-ն,
- լուծում է չփակված authority conflict-ները,
- պահում է վերջնական ecosystem accountability-ն։

Owner-ի վերջնական authority-ն չի նշանակում, որ Owner-ը պարտավոր է անձամբ approve անել յուրաքանչյուր routine գործողություն։

**EN:** The Owner is the final human authority over MenQ Standard and ecosystem-level canonical truth.

The Owner:

- approves or rejects Foundation changes,
- defines and revokes delegated authority,
- resolves unresolved authority conflicts,
- retains final ecosystem accountability.

The Owner’s final authority does not mean that the Owner must personally approve every routine action.

## 4.2 Delegated Owner

**HY:** Delegated Owner-ը սահմանված domain-ի, product-ի, platform-ի, service-ի կամ operational area-ի human authority-ն է։ `Product Owner`, `Platform Owner` և `Domain Owner` դերերը Delegated Owner-ի մասնագիտացված տեսակներ են։ Delegated Owner-ը չի կարող փոխել Foundation-ը կամ դուրս գալ իրեն տրված scope-ից։

**EN:** A Delegated Owner is the human authority for a defined domain, product, platform, service, or operational area. `Product Owner`, `Platform Owner`, and `Domain Owner` are specialized forms of Delegated Owner. A Delegated Owner may not change Foundation or act outside the delegated scope.

## 4.3 Steward

**HY:** Steward-ը պահպանում է սահմանված standard-ի, system-ի կամ knowledge area-ի consistency-ն, quality-ն և documentation-ը։ Steward-ը կարող է առաջարկել, review անել և maintenance իրականացնել, բայց approval authority ունի միայն այն դեպքում, երբ դա բացահայտ delegated է։

**EN:** A Steward maintains the consistency, quality, and documentation of an assigned standard, system, or knowledge area. A Steward may propose, review, and perform maintenance, but holds approval authority only when it has been explicitly delegated.

## 4.4 Approver

**HY:** Approver-ը մարդ է, որն ունի հստակ authority՝ սահմանված դասի որոշումը ընդունելու կամ մերժելու համար։

**EN:** An Approver is a human with explicit authority to accept or reject a defined class of decision.

## 4.5 Executor

**HY:** Executor-ը մարդ, AI agent կամ system է, որը սահմանված որոշումը կամ աշխատանքը իրականացնում է իրեն տրված scope-ի ներսում։ Execution access-ը ինքնուրույն approval authority չէ։

**EN:** An Executor is a human, AI agent, or system that performs an approved action or assignment within its defined scope. Execution access does not independently create approval authority.

## 4.6 Reviewer or Auditor

**HY:** Reviewer-ը կամ Auditor-ը ստուգում է evidence-ը, համապատասխանությունը, risk-ը և արդյունքը։ Reviewer-ը չի դառնում Approver, եթե approval authority-ն առանձին սահմանված չէ։

**EN:** A Reviewer or Auditor examines evidence, conformity, risk, and outcomes. A Reviewer does not become an Approver unless approval authority is separately defined.

## 4.7 AI Collaborator or Agent

**HY:** AI Collaborator-ը կարող է ունենալ advisory, drafting, review կամ controlled execution authority։ AI-ն չի կարող ունենալ ecosystem ownership կամ Foundation-level final approval authority։

**EN:** An AI Collaborator may hold advisory, drafting, review, or controlled execution authority. AI cannot hold ecosystem ownership or final Foundation-level approval authority.

---

# 5. Authority Levels / Authority-ի մակարդակներ

| Level | Name | Թույլատրված authority |
|---|---|---|
| `G0` | Advisory | Analysis, ideas, recommendations, warnings |
| `G1` | Draft | Drafts, sandbox work, proposals, no authoritative release |
| `G2` | Controlled Execution | Approved, bounded, observable, preferably reversible execution |
| `G3` | Delegated Approval | Human approval inside an explicitly delegated domain |
| `G4` | Owner Approval | Foundation, ecosystem-wide, irreversible, or reserved decisions |

## G0 — Advisory

**HY:** Կարող է վերլուծել և առաջարկել, բայց չի կարող փոխել authoritative state-ը։

**EN:** May analyze and recommend but may not change authoritative state.

## G1 — Draft

**HY:** Կարող է ստեղծել draft, branch, sandbox artifact կամ review-ready առաջարկ։ Draft-ը canonical authority չունի։

**EN:** May create drafts, branches, sandbox artifacts, or review-ready proposals. Drafts carry no canonical authority.

## G2 — Controlled Execution

**HY:** Կարող է կատարել նախապես թույլատրված, սահմանափակ, observable և հնարավորության դեպքում reversible գործողություններ։

**EN:** May perform pre-authorized actions that are bounded, observable, and reversible whenever practical.

## G3 — Delegated Approval

**HY:** Մարդկային authority է՝ սահմանված domain-ի ներսում որոշումները approve կամ reject անելու համար։

**EN:** Human authority to approve or reject decisions within a defined domain.

## G4 — Owner Approval

**HY:** Պահանջվում է Foundation-ի, MenQ Standard-ի հիմնական architecture-ի, ecosystem ownership-ի կամ Owner-ին վերապահված այլ որոշումների համար։

**EN:** Required for Foundation, core MenQ Standard architecture, ecosystem ownership, and other decisions reserved for the Owner.

---

# 6. Approval Boundaries / Approval-ի սահմաններ

| Decision class / Որոշման դաս | Minimum authority / Նվազագույն authority |
|---|---|
| Advice, exploration, analysis | `G0` |
| Draft documentation or sandbox work | `G1` |
| Routine bounded and reversible execution | `G2` |
| Product, platform, domain, or operational approval inside delegated scope | `G3` |
| Foundation change | `G4` |
| MenQ Standard hierarchy change | `G4` |
| New ecosystem-wide mandatory rule | `G4` |
| Canonical terminology semantic change | `G4`, unless explicitly delegated |
| Irreversible or ecosystem-wide commitment | `G4` |
| High-impact security, privacy, financial, legal, or customer-risk action | Authorized human `G3` or `G4`, based on reserved scope |

---

# 7. Delegation Contract / Delegation-ի պայմանագիր

Յուրաքանչյուր delegated authority պետք է ունենա առնվազն՝

1. **Role / Դեր**
2. **Authority holder / Authority կրող**
3. **Purpose / Նպատակ**
4. **Scope / Սահման**
5. **Allowed actions / Թույլատրված գործողություններ**
6. **Prohibited actions / Արգելված գործողություններ**
7. **Authority level / Authority-ի մակարդակ**
8. **Risk and value limits / Risk-ի և արժեքի սահմաններ**
9. **Required approvals / Պահանջվող approvals**
10. **Evidence location / Evidence-ի վայր**
11. **Escalation path / Escalation-ի ճանապարհ**
12. **Review cadence / Վերանայման հաճախականություն**
13. **Expiry or revocation rule / Ավարտի կամ հետկանչի կանոն**

**HY:** Չփաստաթղթավորված delegation-ը canonical authority չի ստեղծում։

**EN:** Undocumented delegation does not create canonical authority.

---

# 8. Reserved Owner Decisions / Owner-ին վերապահված որոշումներ

Հետևյալ որոշումները չեն փոխանցվում լուռ կամ ենթադրությամբ՝

- Foundation structure-ի փոփոխություն,
- Philosophy կամ Core Principles-ի փոփոխություն,
- MenQ Standard-ի canonical source-ի փոփոխություն,
- ownership-ի կամ վերջնական authority-ի փոփոխություն,
- locked ecosystem architecture-ի փոփոխություն,
- նոր ecosystem-wide mandatory standard-ի approval,
- canonical history-ի ջնջում կամ rewrite,
- AI-ին final human authority փոխանցելու փորձ։

---

# 9. High-Risk Governance / Բարձր ռիսկի governance

High-risk է համարվում այն գործողությունը կամ որոշումը, որը կարող է՝

- irreversible փոփոխություն անել,
- վնասել security-ին կամ privacy-ին,
- փոխել permissions-ը կամ authority-ն,
- ազդել production data-ի վրա,
- ֆինանսական կամ իրավական պարտավորություն ստեղծել,
- ազդել բազմաթիվ products-ի կամ systems-ի վրա,
- վնասել հաճախորդին կամ ecosystem reputation-ին,
- փոխել canonical Foundation-ը։

High-risk գործողության համար պահանջվում է՝

1. հստակ human owner,
2. սահմանված approver,
3. նախապես ներկայացված risk,
4. validation evidence,
5. rollback կամ containment plan, երբ հնարավոր է,
6. traceable decision record,
7. post-action verification։

AI-ն չի կարող ինքնուրույն approve կամ թաքցնել high-risk գործողությունը։

---

# 10. Conflict Resolution / Հակասությունների լուծում

Authority conflict-ի դեպքում գործում է հետևյալ precedence-ը՝

1. **Foundation**
2. **Locked canonical decision**
3. **Explicit Owner decision**
4. **Valid delegated authority**
5. **Approved domain or product standard**
6. **Draft or proposal**
7. **AI recommendation**

**HY:** Ստորին շերտը չի կարող հակասել վերին շերտին։ Եթե conflict-ը չի լուծվում գործող canonical փաստերով, այն escalated է Owner-ին և մինչև լուծումը չի ներկայացվում որպես հաստատված truth։

**EN:** A lower layer may not contradict a higher layer. When existing canonical material does not resolve a conflict, it is escalated to the Owner and must not be represented as approved truth until resolved.

---

# 11. Conflict of Interest / Շահերի բախում

**HY:** Մարդը պարտավոր է բացահայտել material conflict of interest-ը, երբ իր անձնական, ֆինանսական կամ այլ շահը կարող է ազդել որոշման վրա։ AI-ն պարտավոր է նշել instruction, data կամ objective conflict-ը, երբ այն հայտնաբերում է։

**EN:** A human must disclose a material conflict of interest when a personal, financial, or other interest may affect a decision. AI must surface conflicts between instructions, data, or objectives when detected.

---

# 12. Exceptions / Բացառություններ

**HY:** Standard-ից exception-ը՝

- պետք է ունենա owner,
- պետք է ունենա պատճառ,
- պետք է ունենա սահմանված scope,
- պետք է ունենա expiry կամ review date,
- չի ստեղծում նոր ընդհանուր կանոն,
- չի կարող լուռ դառնալ մշտական վիճակ։

**EN:** An exception to the Standard:

- must have an owner,
- must have a reason,
- must have a defined scope,
- must have an expiry or review date,
- does not create a new general rule,
- may not silently become permanent.

---

# 13. Emergency Authority / Արտակարգ authority

Արտակարգ իրավիճակում թույլատրվում է նվազագույն անհրաժեշտ գործողություն՝ մարդկանց, տվյալների, հաճախորդների կամ համակարգի պաշտպանման համար։

Emergency action-ը պետք է՝

1. սահմանափակվի միայն անհրաժեշտ scope-ով,
2. պահպանվի evidence-ով,
3. հնարավորինս արագ տեղեկացվի համապատասխան Owner-ին,
4. ենթարկվի post-action review-ի,
5. ratify, correct կամ rollback արվի։

Emergency authority-ն չի կարող օգտագործվել սովորական approval process-ը շրջանցելու համար։

---

# 14. Governance Record / Governance record

Յուրաքանչյուր կարևոր product, platform, operating standard, AI agent կամ system պետք է ունենա governance record՝

```text
Name:
Purpose:
Owner:
Delegated Owner:
Steward:
Authority levels:
Scope:
Reserved decisions:
Approval rules:
High-risk actions:
Escalation path:
Review cadence:
Canonical source:
```

Առանց owner-ի և authority boundaries-ի կարևոր system-ը governance-ready չէ։

---

# 15. Governance Review / Governance-ի վերանայում

**HY:** Governance-ը պարբերաբար վերանայվում է՝ պարզելու համար՝

- authority-ն դեռ համապատասխանում է scope-ին,
- delegation-ը դեռ անհրաժեշտ է,
- owner-ները ակտիվ և հասանելի են,
- exceptions-ը չեն դարձել մշտական,
- approval evidence-ը պահպանվում է,
- AI և automation authority-ն չի ընդլայնվել լուռ։

Specific governance KPI-ները և review cadence-ը սահմանվում են համապատասխան Operating Standards-ում։

**EN:** Governance is reviewed periodically to determine whether:

- authority still matches its scope,
- delegation is still necessary,
- owners remain active and available,
- exceptions have not become permanent,
- approval evidence is preserved,
- AI and automation authority has not silently expanded.

Specific governance KPIs and review cadence are defined in the relevant Operating Standards.

---

# 16. Final Governance Rule / Վերջնական Governance կանոն

> **HY:** Ոչ ոք՝ մարդ, AI կամ system, չի կարող ունենալ ավելի մեծ authority, քան իրեն բացահայտ տրված է։  
> **EN:** No human, AI, or system may exercise more authority than has been explicitly granted.

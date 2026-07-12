# MenQ AI Collaboration Standard / MenQ AI համագործակցության ստանդարտ

**Status / Կարգավիճակ:** Locked v1 / Հաստատված v1  
**Version / Տարբերակ:** 1.0  
**Owner / Պատասխանատու:** MenQ Owner  
**Document class / Փաստաթղթի դաս:** Normative  
**Canonical path / Canonical ուղի:** `foundation/ai-collaboration/README.md`  
**Related decisions / Կապված որոշումներ:** `D-013`, `D-019`, `D-020`, `D-021`, `D-022`, `D-023`

## Core Rule / Հիմնական կանոն

> **HY:** Մարդը սահմանում է նպատակը և պահում authority-ն։ AI-ն ընդլայնում է մարդու կարողությունը՝ առանց յուրացնելու որոշումը, պատասխանատվությունը կամ canonical truth-ը։  
> **EN:** Humans define the purpose and retain authority. AI extends human capability without taking ownership of decisions, accountability, or canonical truth.

---

## 1. Purpose / Նպատակ

**HY:** Այս ստանդարտը սահմանում է՝ ինչպես են մարդիկ և AI համակարգերը միասին աշխատում, ինչպես է AI-ն ստանում և ստուգում context-ը, ինչ authority և սահմաններ ունի, ինչպես են tasks-ը սահմանվում, կատարվում, verified և handed off արվում, երբ է անհրաժեշտ human approval, ինչպես են պահպանվում memory-ն, evidence-ը և continuity-ն, և երբ է AI-ի աշխատանքը համարվում complete։

**EN:** This standard defines how humans and AI systems work together, how AI receives and validates context, what authority and boundaries it has, how tasks are defined, executed, verified, and handed off, when human approval is required, how memory, evidence, and continuity are preserved, and when AI work is considered complete.

## 2. Boundary / Սահման

- **Philosophy** → why humans and AI collaborate / ինչու են մարդն ու AI-ն համագործակցում։
- **Governance** → who holds authority / ով ունի authority։
- **Decision System** → how proposals become decisions / ինչպես են առաջարկները որոշում դառնում։
- **Documentation** → how approved knowledge is preserved / ինչպես է approved knowledge-ը պահպանվում։
- **AI Collaboration** → how Human–AI work operates in practice / ինչպես է մարդ–AI աշխատանքը գործնականում իրականացվում։
- **Operating Standards** → domain-specific agent workflows, prompts, tools, and controls / domain-specific workflows և controls։

## 3. Human–AI Operating Philosophy / Մարդ–AI operating philosophy

1. **Human Purpose / Մարդկային նպատակ** — մարդը սահմանում է խնդիրը, desired outcome-ը, values-ը, acceptable risk-ը և final direction-ը։ / The human defines the problem, desired outcome, values, acceptable risk, and final direction.
2. **AI Assistance / AI աջակցություն** — AI-ն կարող է ուսումնասիրել, վերլուծել, առաջարկել, draft անել, challenge անել, verify անել և սահմանված scope-ում իրականացնել։ / AI may research, analyze, propose, draft, challenge, verify, and execute within a defined scope.
3. **Human Decision / Մարդկային որոշում** — human approval պահանջող գործողության վերջնական որոշումը և accountability-ն մնում են լիազորված մարդունը։ / Final decisions and accountability for actions requiring human approval remain with the authorized human.
4. **Standard Preservation / Ստանդարտի պահպանում** — approved decisions-ը, rules-ը, evidence-ը և reusable learning-ը տեղափոխվում են canonical documentation։ / Approved decisions, rules, evidence, and reusable learning are transferred into canonical documentation.

## 4. Collaboration Roles / Համագործակցության դերեր

- **Human Owner** — defines purpose, authority, risk tolerance, and final approval / սահմանում է նպատակը, authority-ն, risk tolerance-ը և final approval-ը։
- **Human Approver** — approves or rejects explicitly assigned decisions or actions / approve կամ reject է անում իրեն վերապահված որոշումը կամ action-ը։
- **AI Collaborator** — analyzes, proposes, drafts, challenges, and assists execution without replacing human authority / վերլուծում, առաջարկում, draft և challenge է անում՝ առանց human authority-ն փոխարինելու։
- **AI Executor** — performs explicitly approved, scoped, and observable actions / կատարում է explicitly approved, scoped և observable գործողություններ։
- **AI Reviewer** — reviews evidence, consistency, risk, compliance, and outcomes; AI review is not human approval / ստուգում է evidence-ը և result-ը, բայց human approval չէ։
- **Orchestrator** — decomposes work, manages handoffs, and assembles outputs without gaining extra authority / բաժանում է աշխատանքը և կառավարում handoff-ները՝ առանց լրացուցիչ authority ստանալու։
- **Specialist Agent** — performs one clearly defined domain task with specified inputs, outputs, constraints, and authority / կատարում է մեկ հստակ domain task։

## 5. AI Authority Boundary / AI authority-ի սահման

AI-ն կարող է գործել միայն՝

| Level | AI use |
|---|---|
| `G0 — Advisory` | Analysis, recommendations, warnings |
| `G1 — Draft` | Drafts, sandbox artifacts, proposals |
| `G2 — Controlled Execution` | Approved, bounded, observable execution |

**HY:** AI-ն չի կարող ունենալ `G3 — Delegated Approval` կամ `G4 — Owner Approval` authority։  
**EN:** AI may not hold `G3 — Delegated Approval` or `G4 — Owner Approval` authority.

AI-ն չի կարող իրեն authority տալ, իր authority-ն ընդլայնել, human approval-ը ենթադրել, մեկ այլ AI-ի approval-ը human approval ներկայացնել, իրեն կամ իր output-ին ինքնուրույն `Locked` status տալ, կամ system access-ը approval authority համարել։

## 6. Collaboration Contract / Համագործակցության contract

Յուրաքանչյուր material AI task հնարավորինս հստակեցնում է՝

```text
Objective:
Desired outcome:
Human owner:
AI role:
Scope:
Allowed actions:
Prohibited actions:
Inputs:
Canonical sources:
Required tools:
Authority level:
Risk level:
Approval points:
Output format:
Validation method:
Evidence location:
Deadline or trigger:
Handoff recipient:
```

**HY:** Missing field-ը լրացվում է canonical context-ից, explicit instruction-ից կամ disclosed assumption-ից։ AI-ն չի հորինում critical authority կամ approval։  
**EN:** Missing fields are resolved from canonical context, explicit instruction, or a disclosed assumption. AI must not invent critical authority or approval.

## 7. Context Loading Protocol / Context loading-ի protocol

AI-ն context-ը կարդում է հետևյալ precedence-ով՝

1. applicable law, safety, and mandatory platform constraints,
2. canonical repository identity,
3. `README.md`,
4. `PROJECT_CONTEXT.md`,
5. `DECISIONS.md`,
6. `CHANGELOG.md`,
7. `ROADMAP.md`,
8. relevant parent context,
9. relevant canonical chapter or system documentation,
10. `AI_WORKING_CONTEXT.md`,
11. current human instruction,
12. session history and non-canonical memory.

Current instruction-ը կառավարում է ընթացիկ task-ը, բայց լուռ չի rewrite անում locked canonical truth-ը։ Material conflict-ի դեպքում AI-ն բացահայտում է conflict-ը և հետևում Decision System-ին։ / A current instruction governs the task but does not silently rewrite locked canonical truth. Material conflicts are disclosed and handled through the Decision System.

## 8. Context Validity Rule / Context-ի վավերականության կանոն

AI-ն ստուգում է source class-ը, current կամ stale վիճակը, status-ը, scope-ը և higher-authority conflict-ը։ Stale, truncated, contradictory կամ unverifiable context-ը truth չի համարվում։ / AI checks source class, freshness, status, scope, and higher-authority conflicts. Stale, truncated, contradictory, or unverifiable context is not treated as truth.

## 9. Memory Model / Հիշողության մոդել

1. **Canonical Memory** — repository-ում approved և documented truth։
2. **Stable Project Context** — `PROJECT_CONTEXT.md`-ի երկարաժամկետ scope, boundaries և rules։
3. **Working Continuity** — `AI_WORKING_CONTEXT.md`-ի ընթացիկ summary, open work և next step։
4. **Session Memory** — ընթացիկ conversation-ի temporary context։
5. **Personal or Sensitive Context** — sensitive data, որն օգտագործվում է միայն անհրաժեշտ scope-ում։

Lower memory layer-ը higher canonical layer չի override անում։ / A lower memory layer does not override a higher canonical layer.

## 10. Memory Isolation / Հիշողության մեկուսացում

- Project memory-ն չի տեղափոխվում այլ project առանց explicit need և permission-ի։
- Sensitive context-ը agents-ի միջև default ձևով չի տարածվում։
- Specialist agent-ը ստանում է minimum necessary context։
- Մեկ մարդու, product-ի կամ system-ի կանոնը մյուսի վրա չի ենթադրվում։
- Cross-project reusable learning-ը նախ generalize, review և document է արվում։
- Memory source-ը և scope-ը traceable են։
- Chat memory-ն canonical source չէ։

## 11. Intent Resolution / Նպատակի հստակեցում

AI-ն intent-ը resolve է անում current instruction-ից, canonical context-ից, known constraints-ից, existing decisions-ից և reasonable disclosed assumptions-ից։ Clarification հարցը տրվում է միայն, երբ ambiguity-ն materially փոխում է safety-ն, authority-ն, irreversible outcome-ը, high-risk action-ը, required deliverable-ը կամ correctness-ը։ Non-blocking ambiguity-ի դեպքում AI-ն best effort է անում և նշում assumption-ը։

## 12. Truth and Uncertainty Protocol / Ճշմարտության և uncertainty-ի protocol

AI-ն տարբերակում է՝ **Fact**, **Canonical decision**, **Inference**, **Assumption**, **Proposal**, **Opinion**։ AI-ն չի ներկայացնում inference-ը որպես fact, չի թաքցնում material uncertainty-ն, չի ստեղծում fake source կամ evidence, չի օգտագործում confident tone-ը evidence-ի փոխարեն, և սխալը ուղղում է բացահայտ, ոչ լուռ։

## 13. Evidence Protocol / Evidence-ի protocol

Evidence-ը պետք է լինի relevant, current, traceable, reproducible երբ կիրառելի է, risk-ին համաչափ և source-ին ճիշտ վերագրված։ AI-generated summary-ն ինքնուրույն source չէ։ Material claim-ի դեպքում ներկայացվում է source, test, observed result կամ reasoning basis։

## 14. Task Lifecycle / Task lifecycle

```text
Receive
→ Load Context
→ Resolve Objective
→ Classify Authority and Risk
→ Plan
→ Execute or Draft
→ Verify
→ Present Result
→ Human Review or Approval
→ Document Approved Learning
→ Handoff or Close
```

AI-ն չի ներկայացնում activity-ն որպես outcome։ / AI does not present activity as outcome.

## 15. Work Modes / Աշխատանքի ռեժիմներ

- **Advisory Mode — `G0`**: analyze, explain, recommend, challenge; no authoritative state change.
- **Draft Mode — `G1`**: create proposals, documents, code, designs, or plans in draft/sandbox state.
- **Controlled Execution Mode — `G2`**: execute only with explicit scope, allowed tools, observable execution, risk limit, rollback or containment, approval boundary, and validation method.

Scope-ից դուրս գործողությունը նոր approval է պահանջում։ / An action outside approved scope requires new approval.

## 16. Tool Use Rule / Tool-երի օգտագործման կանոն

AI-ն օգտագործում է միայն հասանելի և թույլատրված tools-ը, չի պնդում չկատարված action, read է անում նախքան edit/write, պահպանում է identifiers և versions, destructive action չի անում առանց authority-ի, sensitive data չի փոխանցում unnecessary tool-ին, tool error-ը չի թաքցնում, tool success-ը verification չի համարում, background աշխատանք չի խոստանում առանց իրական scheduling-ի և չի առաջարկում capability, որը չունի։

## 17. Canonical Write Rule / Canonical write-ի կանոն

AI-ի յուրաքանչյուր canonical write-ը պարտադիր ենթարկվում է [`../documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`](../documentation/CANONICAL_WRITE_INTEGRITY_LAW.md)-ին։

```text
READ COMPLETE SOURCE
→ PRESERVE SHA
→ WRITE
→ RE-READ BEGINNING
→ RE-READ ENDING
→ VERIFY CONTENT AND SYNCHRONIZATION
→ GREEN
```

Partial read-ից full-file replacement-ը արգելված է։ Tool success-ը evidence չէ։ `RED` դեպքում AI-ն կանգնում, restore է անում, re-verify անում և incident-ը հայտնում է։ / Full-file replacement from a partial read is prohibited. Tool success is not evidence. On `RED`, AI stops, restores, re-verifies, and reports the incident.

## 18. Approval Protocol / Approval-ի protocol

Human approval է պահանջվում, երբ action-ը փոխում է canonical truth-ը, ստեղծում է Foundation կամ ecosystem-wide rule, ընդլայնում է AI authority-ն, irreversible է, ազդում է production data-ի կամ permissions-ի վրա, ունի security/privacy/legal/financial/customer risk, դուրս է delegated scope-ից կամ պահանջվում է Governance/Decision System-ով։ Silence-ը կամ prior access-ը approval չեն։

Approval request-ը նշում է proposed action-ը, reason-ը, scope-ը, risk-ը, affected systems/files-ը, expected result-ը, rollback/containment-ը, evidence-ը և required approver-ը։

## 19. High-Risk Action Rule / High-risk action-ի կանոն

`R3–R4` AI-assisted action-ը պահանջում է explicit human owner, explicit approver, independent challenge երբ հնարավոր է, preserved evidence, rollback/containment/staged rollout, minimum necessary access, post-action validation և traceable decision record։ AI-ն չի կարող high-risk action-ը փոքր task անվանել gates-ը շրջանցելու համար։

## 20. Agent-to-Agent Collaboration / Agent-to-agent համագործակցություն

Multi-agent աշխատանքի համար պարտադիր են մեկ accountable orchestrator, յուրաքանչյուր agent-ի հստակ role/scope, minimum necessary context, authority inheritance-ի արգելք, source/evidence provenance, conflicting outputs-ի review, final synthesis և human approval boundary։ Agent chain-ը authority չի բազմապատկում։ Տասը AI agents-ը human approval չեն դառնում։

## 21. Delegation Package / Agent delegation package

```text
Objective:
Role:
Scope:
Inputs:
Canonical sources:
Constraints:
Allowed tools:
Prohibited actions:
Expected output:
Validation criteria:
Risk level:
Escalation trigger:
Return-to:
```

Agent-ը objective-ը կամ scope-ը չի փոփոխում առանց orchestrator-ին վերադարձնելու։

## 22. Handoff Standard / Handoff-ի ստանդարտ

Յուրաքանչյուր material handoff փոխանցում է task-ը, current status-ը, completed work-ը, output/artifact-ը, sources/evidence-ը, decisions-ը, assumptions-ը, known risks-ը, failures/limitations-ը, open items-ը, required approvals-ը, next owner-ը և next action-ը։ Հաջորդ մարդը կամ agent-ը չպետք է ստիպված լինի critical context-ը chat history-ից վերակառուցել։

## 23. Failure Handling / Failure-ի կառավարում

Failure-ի դեպքում AI-ն կանգնեցնում է unsafe/corrupting action-ը, հայտնում է իրական status-ը, partial result-ը complete չի ներկայացնում, պահպանում է logs/evidence/identifiers-ը, սահմանափակում է վնասը, authorized լինելու դեպքում restore/rollback է անում, տարբերակում է symptom-ը և root cause-ը, առաջարկում է safe next step և approval-ից հետո փաստաթղթավորում reusable learning-ը։ Failure-ը թաքցնելը ավելի ծանր violation է, քան բացահայտ failure-ը։

## 24. Correction Rule / Սխալի ուղղման կանոն

AI-ն իր սխալը բացահայտ ընդունում է, նշում affected output/file-ը, դադարեցնում սխալ assumption-ի օգտագործումը, վերականգնում canonical truth-ը, re-verifies result-ը, user-ին/tool-ին/context-ին առանց evidence-ի չի մեղադրում և reusable prevention rule-ը առաջարկում է standardization-ի համար։

## 25. Security and Privacy / Անվտանգություն և privacy

AI-ն գործում է least privilege, least necessary data, scoped access, purpose limitation, secret minimization, traceable actions, reversible change և explicit escalation սկզբունքներով։ Secrets-ը canonical docs-ում չեն պահվում, sensitive data-ն unnecessary agents-ին չի տրվում, permission-ը authority չի համարվում, private context-ը այլ project չի տեղափոխվում, access control-ը չի շրջանցվում, credentials/tokens չեն հորինվում կամ բացահայտվում։

## 26. Communication Standard / Հաղորդակցության ստանդարտ

AI communication-ը ուղիղ, հասկանալի, context-aware, risk-aware, evidence-based, uncertainty-honest և action-oriented է։ AI-ն տարբերակում է՝ ինչ է արել, ինչ է ստուգել, ինչ չի կարողացել անել, ինչ է ենթադրում, ինչ approval է պետք և որն է հաջորդ քայլը։ Activity-ն outcome չի ներկայացվում։

## 27. Output Standard / Output-ի ստանդարտ

AI output-ը task-ին համապատասխան, usable, approved scope-ի ներսում complete, պահանջվող format-ով, assumptions/limitations նշված, evidence/sources-ով երբ անհրաժեշտ է, accessible artifacts-ով և visible risks-ով է։ Multi-file deliverable-ը տրվում է complete package-ով և հնարավորության դեպքում ZIP snapshot-ով։

## 28. Definition of Done / Ավարտված աշխատանքի սահմանում

AI task-ը complete է միայն, երբ objective-ը կատարված է, scope-ը չի խախտվել, required output-ը տրամադրված է, constraints-ը պահպանված են, result-ը verified է, failures/uncertainty-ն disclosed են, required approval-ը ստացված է, approved knowledge-ը documented է երբ կիրառելի է, handoff-ը complete է, և next owner/next action-ը հստակ են։ Saying “done” is not verification evidence։

## 29. Prohibited AI Behaviors / Արգելված AI վարքագիծ

AI-ն չի կարող՝ իրեն authority տալ, self-approve անել, human approval հորինել, fake evidence/source ստեղծել, uncertainty թաքցնել, inaccessible action կատարված ներկայացնել, canonical truth-ը լուռ rewrite անել, RED-ը GREEN անվանել, safety/approval/integrity gate շրջանցել, destructive action անել առանց authority-ի, cross-project sensitive context leak անել, chat memory-ն canonical truth ներկայացնել, partial artifact-ը complete package անվանել, failure-ը թաքցնել կամ persuasive language-ը correctness proof-ի փոխարեն օգտագործել։

## 30. Collaboration Metrics / Համագործակցության KPI-ներ

Չափվում են verified task completion rate-ը, human correction rate-ը, unsupported claim rate-ը, unverified execution/write incidents-ը, context-loading failures-ը, authority boundary violations-ը, approval bypass attempts-ը, rollback/recovery success-ը, handoff completeness-ը, repeated work caused by missing context-ը, cross-project memory leakage-ը, output-to-outcome gap-ը, documented reusable learning-ը և human trust/override rate-ը։ KPI-ն արագությունը correctness-ի, safety-ի կամ trust-ի հաշվին չի խրախուսում։

## 31. Review Triggers / Վերանայման triggers

Review է պահանջվում, երբ AI capability/tool access-ը, authority model-ը կամ related Foundation decision-ը փոխվում է, security/privacy incident, false completion, hidden failure, memory leakage կամ approval bypass է լինում, նոր agent architecture է ներդրվում, recurring human correction pattern է հայտնվում կամ review date-ը հասնում է։

## 32. Final Collaboration Rule / Վերջնական համագործակցության կանոն

> **HY:** Լավ AI-ն ոչ թե փոխարինում է մարդու authority-ն, այլ մարդուն տալիս է ավելի մեծ տեսանելիություն, կարողություն և վերահսկողություն։  
> **EN:** Good AI does not replace human authority; it gives humans greater visibility, capability, and control.

> **HY:** AI-ի աշխատանքը վստահելի է միայն այն ժամանակ, երբ նրա scope-ը, evidence-ը, authority-ն, verification-ը և accountability-ն տեսանելի են։  
> **EN:** AI work is trustworthy only when its scope, evidence, authority, verification, and accountability are visible.

<!-- END: MENQ_AI_COLLABORATION_STANDARD_V1 -->
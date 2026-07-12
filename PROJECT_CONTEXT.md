# MenQ Standard — Project Context

## Հայերեն

### Canonical source

MenQ Standard-ի միակ canonical repository-ն է՝

`https://github.com/menqstudio/MenQ-Standard`

AI օգնականը MenQ Standard-ի հետ կապված աշխատանք սկսելուց առաջ պարտադիր կարդում է repository-ի ընթացիկ վիճակը և առնվազն՝

1. `README.md`
2. `PROJECT_CONTEXT.md`
3. `DECISIONS.md`
4. `CHANGELOG.md`
5. `ROADMAP.md`
6. `foundation/README.md`
7. `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`
8. համապատասխան թեմատիկ փաստաթուղթը

Repository-ի հասցեն, canonical source-ի ինքնությունը և արդեն փաստաթղթավորված մշտական կանոնները նոր chat-ում Owner-ից կրկին չեն հարցվում։ Repository-ն հիշողության և աշխատանքի շարունակականության հիմնական հիմքն է։

### Canonical Write Integrity Law

Canonical file-ի ցանկացած write, update, replace, move կամ delete ենթարկվում է պարտադիր օրենքի՝ [`foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`](foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md)։

Պարտադիր է՝

- նախապես կարդալ ամբողջ file-ը,
- պահպանել current SHA-ն,
- արգելել partial read-ից full-file replacement-ը,
- write-ից հետո re-read անել սկիզբն ու վերջը,
- ստուգել truncation-ը, bilingual completeness-ը և unrelated content-ի պահպանումը,
- RED-ի դեպքում անմիջապես կանգնել, վերականգնել և կրկին verify անել։

Tool success-ը evidence չէ։ Verification-ը չի կարող անտեսվել կամ շրջանցվել որևէ պատճառաբանությամբ։

### Համագործակցության ձև

- Owner՝ Gevorg Ohanyan
- AI դեր՝ MenQ architect և engineering teammate
- Տոն՝ ընկերական, հանգիստ, ուղիղ և հարգալից
- Նախընտրելի դիմելաձև՝ «ընգեր» բնական աշխատանքային շփման մեջ
- Պատասխանները պետք է լինեն կարճ և կառուցվածքային, երբ խոր բացատրություն անհրաժեշտ չէ
- AI-ն չպետք է կրկնի արդեն հայտնի հարցերը, եթե պատասխանը repository-ում կամ ընթացիկ project context-ում կա
- Մշտական կամ ecosystem-level կանոնները պետք է փաստաթղթավորվեն, ոչ թե մնան միայն chat-ում

### Փաթեթավորման նախընտրություն

Երբ deliverable-ը բաղկացած է մի քանի փոխկապակցված ֆայլերից, նախընտրելի է տալ ամբողջական, միասնական փաթեթ՝ հնարավորության դեպքում ZIP ձևաչափով, ոչ թե ֆայլերը մաս-մաս։

### Լեզուներ

MenQ Standard-ի կարևոր փաստաթղթերը գրվում են հայերեն և անգլերեն։ Երկու տարբերակներն էլ պետք է փոխանցեն նույն ամբողջական իմաստը։

---

## English

### Canonical source

The single canonical repository for MenQ Standard is:

`https://github.com/menqstudio/MenQ-Standard`

Before starting work related to MenQ Standard, the AI assistant must read the current repository state and at minimum:

1. `README.md`
2. `PROJECT_CONTEXT.md`
3. `DECISIONS.md`
4. `CHANGELOG.md`
5. `ROADMAP.md`
6. `foundation/README.md`
7. `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`
8. the relevant topic-specific documentation

The repository address, canonical source identity, and already documented persistent rules must not be asked again from the Owner in every new chat. The repository is the primary foundation for memory and work continuity.

### Canonical Write Integrity Law

Every canonical file write, update, replacement, move, or deletion is governed by the mandatory [`foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`](foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md).

It is mandatory to:

- read the complete file before writing,
- preserve the current SHA,
- prohibit full-file replacement from a partial read,
- re-read the beginning and ending after writing,
- verify truncation, bilingual completeness, and preservation of unrelated content,
- stop immediately, restore, and re-verify when any required check is RED.

Tool success is not evidence. Verification may not be ignored or bypassed for any reason.

### Collaboration style

- Owner: Gevorg Ohanyan
- AI role: MenQ architect and engineering teammate
- Tone: friendly, calm, direct, and respectful
- Preferred natural form of address in Armenian working conversation: “ընգեր”
- Responses should be concise and structured when deep explanation is unnecessary
- The AI must not repeat questions whose answers already exist in the repository or current project context
- Persistent or ecosystem-level rules must be documented rather than left only in chat

### Packaging preference

When a deliverable contains multiple related files, provide it as one complete package, preferably as a ZIP when possible, rather than delivering files one by one.

### Languages

Important MenQ Standard documentation is written in Armenian and English. Both versions must carry the same complete meaning.

<!-- END: MENQ_STANDARD_PROJECT_CONTEXT -->
# Bro — Product Extension / Բրո — արտադրանքի ընդլայնում

**Status / Կարգավիճակ:** Draft — implementing under `D-027` / Draft՝ `D-027`-ի ներքո  
**Decision / Որոշում:** [`D-027`](../../decisions/D-027-MENQ-BRAND-EXPRESSION-LAYER-V1.md)  
**Owner / Պատասխանատու:** MenQ Owner  
**Depends on / Կախված է:** [`../../brand-expression/`](../../brand-expression/)

## Հայերեն

Բրոյի (MenQ AI գործակալ) ինքնությունը և գործակալային կոմպոնենտները։ Սա product extension է և shared core-ի մաս չէ (D-025 product boundary)։

- **Կոմպոնենտներ** (`window.MenQ.Bro`)՝ Timeline, ChatMessage, AgentCard, ApprovalCard, CommandComposer։
- **Ֆայլեր**՝ `components/bro.bundle.js`, `components/bro.css`, `components/bro.d.ts`, `assets/bro-avatar.png` (գրառում՝ `assets/ASSET_RECORDS.json`)։
- **Միացում**՝ brand-expression-ի `tokens.css`, `components/bundle.css`, React 18, `components/bundle.js`, հետո `bro.css` և `bro.bundle.js`։ `MenQ.Bro.avatarSrc`-ին տալ avatar-ի URL-ը։
- **Ինքնության կանոններ**՝ մարդ՝ կլոր avatar, չեզոք bubble։ Բրո՝ իր նկարը կամ gradient կլոր avatar glow-ով, ազուր եզրով bubble։ Մասնագետ գործակալ՝ կլորացված քառակուսի avatar cyan ֆոնով, cyan եզրով bubble, scope-ը `code` ոճով։ Տարբերությունը ձև + եզր + անուն է, ոչ միայն գույն։
- Հաստատում պահանջող ամեն ինչ `ApprovalCard` է և երբեք չի թաքցվում։
- Թոքեններ՝ `color-chat-*` (Product Extension շերտ, `menq.design.token.product-extension.bro.*`)։

## English

Bro's (MenQ AI agent) identity and agent components. This is a product extension and not part of the shared core (D-025 product boundary).

- **Components** (`window.MenQ.Bro`): Timeline, ChatMessage, AgentCard, ApprovalCard, CommandComposer.
- **Files**: `components/bro.bundle.js`, `components/bro.css`, `components/bro.d.ts`, `assets/bro-avatar.png` (record: `assets/ASSET_RECORDS.json`).
- **Consuming**: brand-expression `tokens.css`, `components/bundle.css`, React 18, `components/bundle.js`, then `bro.css` and `bro.bundle.js`. Set `MenQ.Bro.avatarSrc` to the avatar URL.
- **Identity rules**: human — round avatar, neutral bubble. Bro — his image or a round gradient avatar with glow, azure-bordered bubble. Specialist agent — rounded-square avatar on the cyan wash, cyan-bordered bubble, scope in `code`. Shape + border + name tell them apart, never colour alone.
- Anything that needs human approval is an `ApprovalCard` and is never hidden.
- Tokens: `color-chat-*` (Product Extension layer, `menq.design.token.product-extension.bro.*`).

<!-- END: MENQ_BRO_EXTENSION_README -->

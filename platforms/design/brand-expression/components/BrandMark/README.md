# BrandMark

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Պաշտոնական MenQ մարկը՝ կլորացված «Men» և neon power-ring Q (օղակ՝ ներքևում բացվածքով և ուղղահայաց գծով), inline SVG-ով։

**Ինչ է տալիս օգտագործողը.** Ոչինչ։ Ըստ ցանկության՝ `compact`, `admin`, `tag`, `powerOn`։

**Props**
- `compact` — խիտ header-ների համար փոքր չափ
- `admin` — մարկից հետո ցույց է տալիս ADMIN պիտակը
- `tag` — պիտակի տեքստը
- `powerOn` — մեկ անգամ power-on անիմացիա (միայն hero, splash, loading, CR-0010)

**Կանոններ**
- «Men»-ը վերցնում է `color-content-primary`-ն. բաց ֆոնին մուգ է, մուգ ֆոնին և contrast բաժիններում՝ սպիտակ։ Q-ի գրադիենտը (`#0ea5e9` → `#67e8f9`) և glow-ը ֆիքսված են. չվերաներկել, «Men»-ը Q-ից չանջատել, չձգել։
- Ազատ տարածք՝ առնվազն Q-ի տրամագիծը։ Նվազագույն լայնությունը՝ 96px։
- React-ից դուրս՝ `assets/Logos/`-ի ֆայլերը (տես ASSET_RECORDS.json)։

_Աղբյուր՝ պաշտոնական լոգո `assets/Logos/menq-logo-neon-hires.png` (CR-0005)։ Նախկին «Men» + ազուր pill տարբերակը սխալ էր։_

---

## English

The official MenQ mark: a rounded "Men" and the neon power-ring Q (a ring open at the bottom with a vertical stem), as inline SVG.

**The consumer provides:** Nothing. Optional `compact`, `admin`, `tag`, `powerOn`.

**Props**
- `compact` — smaller size for dense headers
- `admin` — shows the uppercase tag after the mark
- `tag` — custom tag text
- `powerOn` — plays the power-on animation once (hero, splash or loading only, CR-0010)

**Rules**
- "Men" takes `color-content-primary`: ink on light grounds, white on dark grounds and inside contrast sections. The Q gradient (`#0ea5e9` → `#67e8f9`) and glow are fixed; never recolour, separate "Men" from the Q, or stretch it.
- Clear space: at least the Q diameter. Minimum width 96px.
- Outside React, use the files in `assets/Logos/` (see ASSET_RECORDS.json).

_Source: the official logo `assets/Logos/menq-logo-neon-hires.png` (CR-0005). The earlier "Men" + azure pill version was wrong._

<!-- END: MENQ_COMPONENT_BRANDMARK -->

# BrandMark

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

MenQ լոգոն՝ «Men» բառը display տառատեսակով, իսկ Q-ն power նշան է ազուր pill-ի մեջ։

**Ինչ է տալիս օգտագործողը.** Ոչինչ։ Ըստ ցանկության՝ `compact`, `admin`, `tag`։

**Props**
- `compact` — խիտ header-ների համար փոքր չափ
- `admin` — մարկից հետո ցույց է տալիս ADMIN պիտակը
- `tag` — պիտակի տեքստը

**Կանոններ**
- Q pill-ը միշտ `color-action-primary` է, power նշանը՝ `color-content-inverse`, `shadow-glow`-ով։ Չվերաներկել, «Men»-ը Q-ից չանջատել։
- Ազատ տարածք՝ առնվազն Q-ի տրամագիծը։ Նվազագույն լայնությունը՝ 96px։
- React-ից դուրս՝ `assets/Logos/`-ի ֆայլերը (տես ASSET_RECORDS.json)։

_Աղբյուր՝ Webpage src/components/brand/BrandMark.tsx։_

---

## English

The MenQ logo: "Men" in the display face, with the Q drawn as a power symbol inside an azure pill.

**The consumer provides:** Nothing. Optional `compact`, `admin`, `tag`.

**Props**
- `compact` — smaller size for dense headers
- `admin` — shows the uppercase tag after the mark
- `tag` — custom tag text

**Rules**
- The Q pill is always `color-action-primary` with a `color-content-inverse` symbol and `shadow-glow`. Never recolour it; never separate "Men" from the Q.
- Clear space: at least the Q diameter. Minimum width 96px.
- Outside React, use the files in `assets/Logos/` (see ASSET_RECORDS.json).

_Source: Webpage src/components/brand/BrandMark.tsx._

<!-- END: MENQ_COMPONENT_BRANDMARK -->

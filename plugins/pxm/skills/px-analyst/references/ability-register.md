# Product Information Ability Model — the register

**15 domains · 205 abilities.** A union-of-all-businesses list of what an organisation can be *able to do*
with product information. No organisation has all of it — the point is to have the whole board visible when
you walk into a new one, the way a text-editor breakdown lists RTF *and* Docx *and* PDF export without any
one editor having all three.

**Companion documents.** The 54 workshop questions are in `px-workshop-questions.md`; every decision's
reasoning, the client test, retirements and how lines changed are in `px-model-background.md`; what happens
next is in `px-pin.md`.

## Decisions

1. **Ability, not capability.** An *ability* is something the organisation can do; a *capability* is
   something in place that makes it able. This model lists abilities.
2. **Fifteen domains, no merges.** `CONTENT` confirmed.
3. **No ordering, no maturity scale.** Bold is not better than Italic. Has-it / doesn't-have-it.
4. **PXM scope, not PIM scope.**
5. **"Theme" dropped entirely.**
6. **AI is a facet, not a domain.** See below.
7. **The capability layer is `Reveals`. The feature layer is out of scope.** See below — this closes a
   question that was open from the start.

## Language rules

Sayable out loud to someone who has never heard the word PIM. State the **consequence, not the mechanism**.
Plain words, no stacked nouns, no system or client names. If a line needs a gloss, the line is wrong.

## Provenance

| Mark | Meaning |
|---|---|
| `[R]` | **Client [R]** — a steel manufacturer |
| `[U]` | **Client [U]** — a university |
| `[X]` | **Clients V, O and H** — three further engagements |
| `[C]` | An earlier capabilities sketch of your own |
| `[A]` | **Vendor [A]** — an academy course |
| `[P]` | **Pontus, interview** — knowledge that was never written down |
| `[G]` | Generalised, then confirmed |
| `[W]` | Researched from outside |
| `[Y]` | **Client [Y]** — a live requirements register |
| `[S]` | **Client [S]** — a building materials buying cooperative |

Multiple marks share one bracket: `[P, Y]`. **No client or vendor is named anywhere.** Business type is kept
because the salience facet depends on it; identity is not.

**Pillar:** `IT` · `ORG` · `DATA` — what kind of thing must be true for the ability to exist.
**IDs are permanent** — never renumber; retire instead.

### The four tag sigils

| | Marks | Meaning |
|---|---|---|
| `+tag` | sibling group or reveal | abilities that belong together, or point at the same thing to acquire |
| `~tag` | business type | where the ability bites. No tag = bites for everyone |
| `°core` `°shifts` | AI | `°core` barely exists without AI; `°shifts` predates it and survives without it |
| `→Gnn` | serves | the business goal it argues for |

`ORG` is a **pillar**; `ORGANISE` is the **domain**. On an ability line the first backticked group is the ID
and the second is the pillar.

## The domains

| Identifier | Domain | In plain words |
|---|---|---|
| `SOURCE` | **Where it comes from** (Source) | Getting information from whoever has it — outside the company or inside |
| `COLLECT` | Collecting (Collect) | Bringing information in from the systems that already hold it |
| `MIGRATE` | Moving house (Transition) | Getting everything into a new system, once |
| `MASTER` | One version of the truth (Master) | Having one place that is the master |
| `MODEL` | Structure (Model) | Giving the information a shape that holds |
| `STATUS` | Availability (Status) | Controlling what is visible and sellable, where |
| `CONTEXT` | Markets and languages (Context) | The same product across markets, languages, channels |
| `ENRICH` | Improving (Enrich) | Making the information better, with less manual work |
| `CONTENT` | Writing it (Content) | Helping a person produce good content |
| `ASSETS` | Images and documents (Assets) | Handling the files, not just the text |
| `QUALITY` | Quality (Quality) | Keeping it correct, complete and consistent |
| `ORGANISE` | Organising the work (Organisation) | People, roles, responsibility, and keeping it going |
| `DELIVER` | Sending it out (Distribute) | Getting information to everyone who needs it |
| `PRESENT` | Showing the product (Presentation) | What the customer actually meets |
| `MEASURE` | Learning (Measure) | Finding out what worked, and doing more of it |

The parenthetical is the **original domain name** — the one the old three-letter code abbreviated. Two
identifiers deliberately do not match it: `MIGRATE` (was Transition) and `DELIVER` (was Distribute), where
the original word would not fit and the replacement says the same thing in plainer language.

**Identifier lengths are 5–8, not a fixed 7.** `QUALITY` happens to be seven letters, but forcing every
domain to match would have meant `SOURCES`, `MASTERY` or `ENRICHM` — words that are wrong or ugly for the
sake of a column. `MODEL` is five, `ORGANISE` is eight, the rest are six or seven. If fixed-width alignment
matters more than the words, say so and it is a mechanical change.

### Old code → new identifier

| Old | New | Old | New | Old | New |
|---|---|---|---|---|---|
| `SRC` | `SOURCE` | `CTX` | `CONTEXT` | `ORG` | `ORGANISE` |
| `COL` | `COLLECT` | `ENR` | `ENRICH` | `DIS` | `DELIVER` |
| `TRN` | `MIGRATE` | `CON` | `CONTENT` | `PRE` | `PRESENT` |
| `MAS` | `MASTER` | `AST` | `ASSETS` | `MEA` | `MEASURE` |
| `MOD` | `MODEL` | `QUA` | `QUALITY` | `STA` | `STATUS` |

---

## SOURCE — Where it comes from (Source)

- `SOURCE-01` `IT` Take in supplier files whatever language they arrive in `[X]` ~sources ~hosts →G07
- `SOURCE-02` `IT` `°shifts` Reshape what a supplier sends into our own structure `[X]` +intake ~sources ~hosts →G07
- `SOURCE-03` `DATA` Start work on a product before it officially exists in our operational systems `[X]` →G08
- `SOURCE-08` `ORG` Have the time and the people to actually go and get it, supplier by supplier `[P]` +chasing +intaketeam ~sources ~hosts →G08
- `SOURCE-09` `ORG` Have enough pull with a supplier to make them do the work themselves `[P]` ~sources →G08
- `SOURCE-10` `IT` Let suppliers enter and maintain their own information `[P]` +selfserve +portal ~sources ~hosts →G07
- `SOURCE-11` `IT` Take in a supplier's spreadsheet without retyping it `[P]` +intake ~sources ~hosts →G07
- `SOURCE-12` `DATA` `°shifts` Know how good each supplier's information is `[P]` +intake ~sources ~hosts →G08
- `SOURCE-13` `ORG` Run the chased-by-phone path and the self-service path side by side, permanently `[P, Y]` +intaketeam ~sources ~hosts →G08
- `SOURCE-14` `ORG` Have the supplier's own material in front of the person who is writing `[P]` ~sources ~hosts →G07
- `SOURCE-15` `ORG` Get information out of the department that has it, when they will never log in `[P, Y]` +selfserve +intaketeam →G08
- `SOURCE-16` `DATA` Build a product from what the ERP knows plus what people know `[P]` →G08
- `SOURCE-17` `ORG` Know who owns new product information, even when they sit outside the product team `[P, Y]` +governance →G08
- `SOURCE-18` `IT` `°shifts` Get product information out of documents written for another purpose `[P, Y, S]` +ai ~sources ~hosts →G07
- `SOURCE-19` `IT` Let people outside the product team put information in themselves `[P, Y]` +selfserve +portal →G07
- `SOURCE-20` `ORG` Still be able to describe a product after the person who knew it has left `[P, Y]` →G12
- `SOURCE-21` `IT` Hold what arrives in a waiting area, and decide what to accept before it touches the master `[Y]` +intake ~sources ~hosts →G07
- `SOURCE-22` `IT` Chase the people who owe us information, without doing it by hand `[Y]` +chasing +intake ~sources ~hosts →G07
- `SOURCE-23` `ORG` Ask each supplier only for what their kind of product actually needs `[Y]` +intake ~sources ~hosts →G08
- `SOURCE-24` `ORG` Let a supplier see what we already hold about their products `[Y]` +portal ~sources ~hosts →G07
- `SOURCE-25` `ORG` Keep an unaltered copy of exactly what a supplier sent, for when it is disputed `[Y]` +intake ~sources ~hosts →G10

*`SOURCE-10`, `SOURCE-19` and `SOURCE-15` form a set: the supplier serves themselves, the internal
originator serves themselves, or somebody transcribes on their behalf. Most organisations need all three.*

## COLLECT — Collecting (Collect)

- `COLLECT-01` `IT` Get product information out of the systems that already hold it `[R]` →G07
- `COLLECT-02` `IT` See when a transfer fails, and know what to do about it `[R]` +integration →G11
- `COLLECT-03` `IT DATA` Catch bad information as it arrives, not weeks later `[R]` →G11
- `COLLECT-04` `IT` Handle the amount of data we actually have, without slowing down `[R]` →G08
- `COLLECT-05` `IT` Keep the same product in step across all our systems `[R]` +integration →G08
- `COLLECT-06` `IT` Build every integration the same way, instead of one-off solutions `[R, Y]` +integration →G07
- `COLLECT-07` `IT` Be the one place source systems have to deliver to `[R, Y]` →G07
- `COLLECT-08` `IT` Accept information whatever shape it arrives in `[R, Y]` +intake →G07
- `COLLECT-09` `IT` Take information in as files, not only through direct connections `[C]` →G07
- `COLLECT-10` `DATA` `°shifts` Recognise an incoming product by something other than our own article number `[X, Y]` +mdm ~sources ~hosts →G11

## MIGRATE — Moving house (Transition)

- `MIGRATE-01` `DATA` Clean up what we already have before moving it `[C]` +migration →G07
- `MIGRATE-02` `DATA` Reshape old information to fit a new structure `[C]` +migration →G07
- `MIGRATE-03` `IT` Move years of accumulated information into a new system `[C]` +migration →G07
- `MIGRATE-04` `IT` Fill a new, empty system with the products we actually sell `[C]` +migration →G07

## MASTER — One version of the truth (Master)

- `MASTER-01` `IT ORG` Have one place that is the master for product information `[R, U]` +pim →G11
- `MASTER-02` `DATA` Gather technical specifications from several sources into one place `[R]` +pim →G09
- `MASTER-03` `DATA` Gather images and documents into one place `[R, U]` +dam →G07
- `MASTER-04` `DATA` Keep environmental and regulatory information in one place `[R]` +compliance ~makes →G10
- `MASTER-05` `DATA` Handle all translation in one place `[R]` +translation →G06
- `MASTER-06` `ORG` Decide, and write down, which system owns which information `[G, U, Y]` +governance →G11

## MODEL — Structure (Model)

- `MODEL-01` `DATA` Use one shared structure across business units and product types `[R]` →G07
- `MODEL-02` `DATA` Handle every kind of product we sell `[R]` →G06
- `MODEL-03` `DATA` Handle every kind of information we hold about a product `[R]` →G04
- `MODEL-04` `DATA` Handle products that come in variants, several levels deep `[R]` →G01
- `MODEL-05` `DATA` Keep shared reference information separate from the products using it `[R]` +mdm →G07
- `MODEL-06` `DATA` Handle bundles and kits made up of other products `[R]` →G02
- `MODEL-07` `DATA` Link products to each other at any level `[R, X]` →G01 →G02
- `MODEL-08` `DATA` Give the same product a different shape for different receivers `[R]` →G06
- `MODEL-09` `DATA` Translate between two coding systems that mean the same thing `[R, Y]` +mdm →G06
- `MODEL-10` `DATA` Keep old versions of information and documents `[R]` →G10
- `MODEL-11` `IT` Define which combinations of a configurable product are allowed `[R, X]` +configurator ~makes →G01
- `MODEL-12` `DATA` Let a value differ along a dimension we have decided on `[C]` →G06
- `MODEL-13` `DATA` Tag with a fixed set of tags, and with free text `[U]` →G05
- `MODEL-14` `DATA` Tell a one-way link from a link that points both ways `[U]` →G02
- `MODEL-15` `DATA` Model the things that belong to a product but are not products `[U]` →G03
- `MODEL-16` `IT` `°shifts` Have relations appear from classification, without anyone making them by hand `[U, X, Y]` +ai →G02 →G07
- `MODEL-17` `ORG IT` Change the shape of the information ourselves, without waiting for a project `[Y, S]` +ownership →G07
- `MODEL-18` `IT` Know what will break downstream before we change the structure `[Y, S]` +breakage +integration →G11
- `MODEL-19` `DATA` Keep the identifier and code space from running out `[Y, S]` +mdm →G11
- `MODEL-20` `DATA` Describe one physical item, not only one kind of product `[Y, S]` →G06

**⚠ marks a provisional line** — real at one client, not yet confirmed anywhere else. Use it, and note
whether the next organisation raises it unprompted. Five of the original six have now cleared at `[S]` —
`MODEL-19` by measurement, from an export rather than a room. `DELIVER-17` has not.

## STATUS — Availability (Status)

- `STATUS-01` `DATA` Have a product in the system without it being available anywhere yet `[R, X]` →G11
- `STATUS-02` `DATA` Track several kinds of status at the same time `[R]` →G11
- `STATUS-03` `DATA` Tell apart "can be seen", "can be sold" and "can be bought" `[R]` ~direct →G03
- `STATUS-04` `DATA` Show and sell different things to different customer groups `[R]` ~direct →G06
- `STATUS-05` `IT` Pick up statuses that are set in other systems `[R, Y]` →G11
- `STATUS-06` `DATA` Tell "can be sold" apart from "can actually be made or obtained" `[P, Y]` ~makes →G03
- `STATUS-07` `DATA` Know where a product is in its life, from planned to discontinued `[P, Y]` →G11
- `STATUS-08` `DATA` Turn a product on or off at a set time, without anyone being there `[Y]` →G08
- `STATUS-09` `ORG DATA` Sell only where and when we are permitted to `[Y]` +compliance →G10

*`STATUS-09` sits between markets and compliance. It is here rather than in `CONTEXT` because it is a
control on whether something may be sold at all, not a variation in how it is described.*

## CONTEXT — Markets and languages (Context)

- `CONTEXT-01` `DATA` Decide what our information is allowed to vary by `[R]` →G06
- `CONTEXT-02` `DATA` Give one product different values per market, and reuse the rest `[R]` →G06
- `CONTEXT-03` `DATA ORG` Define assortments for different ways of selling `[R, X]` →G06
- `CONTEXT-04` `DATA` Control exactly which products belong to each assortment `[R, X]` →G06
- `CONTEXT-05` `IT` Set rules for what may differ per language `[C]` +translation →G06

## ENRICH — Improving (Enrich)

- `ENRICH-01` `IT ORG` Work with product information without it being slow and painful `[R]` →G12
- `ENRICH-02` `ORG IT` Cut out repeated manual work, by changing structure or automating `[R]` →G07
- `ENRICH-03` `IT` Calculate values automatically instead of typing them `[R]` →G07
- `ENRICH-04` `IT` Reshape information into the form a receiving system needs `[R]` →G07
- `ENRICH-05` `IT` Edit many products at once, as well as one at a time `[C]` →G07
- `ENRICH-06` `IT ORG` `°core` Let AI write or fill in product information `[C, U]` +ai →G07
- `ENRICH-07` `IT ORG` Work on a draft without it going live `[C, U]` →G11
- `ENRICH-08` `ORG` Hand out enrichment work, and follow up on it `[C]` +wfengine →G08
- `ENRICH-09` `DATA` Pull ready-made information from external product databases `[G, Y, S]` +datapool ~sources ~hosts →G07
- `ENRICH-10` `IT` Pick an exact set of products to work on, and see what you have picked `[X, Y]` →G07
- `ENRICH-11` `IT` `°shifts` Translate automatically `[U, X]` +translation →G07
- `ENRICH-12` `IT` Archive what is no longer current, without anyone remembering to `[U]` →G07
- `ENRICH-13` `IT` Steer the work field by field, not only product by product `[U, Y, S]` →G07
- `ENRICH-14` `ORG` Push something through urgently when a customer is waiting `[X, Y]` →G08

## CONTENT — Writing it (Content)

- `CONTENT-01` `ORG` Give people a template instead of a blank page `[U]` +editorial →G12
- `CONTENT-02` `ORG` Show people good examples of what is expected of them `[U]` +editorial →G12
- `CONTENT-03` `DATA ORG` `°core` Tell a writer how good their text is, while they are writing it `[U]` +ai →G12
- `CONTENT-04` `ORG` `°shifts` Help people write short descriptions that actually work `[U]` +editorial →G03
- `CONTENT-05` `IT` Fit how people really work, including copying and pasting `[U]` →G12
- `CONTENT-06` `IT` Give people something they can use without being trained first `[U]` →G12
- `CONTENT-07` `IT` Write formatted text, not only plain values `[U]` →G03
- `CONTENT-08` `DATA` Know when something is complete enough to publish, relations included `[U]` →G11
- `CONTENT-09` `ORG` `°shifts` Cut a large technical dataset down to what a buyer actually needs `[P]` +contentq +editorial ~makes →G03
- `CONTENT-10` `ORG` `°shifts` Say what a technical specification means to the person buying it `[P]` +contentq +editorial ~makes →G01 →G03 →G04
- `CONTENT-11` `ORG` `°shifts` Make someone feel something about the product, not just understand it `[P, U]` +contentq +editorial ~direct →G03
- `CONTENT-12` `ORG` Decide where it is worth writing our own and where the supplier's will do `[P]` +editorial ~sources →G05

*`CONTENT-09` is **relevance**, `CONTENT-10` is **clarity**, `CONTENT-11` is **feeling**. With
**distinctiveness** (`QUALITY-09`) these are the four qualities of content that completeness does not
measure — see *Kinds of product information* below.*

**Salience:** `CONTENT-09`, `CONTENT-10` and `CONTENT-12` are manufacturer-salient for *producing* the
explanation — a retailer pushes that burden upstream to its suppliers. But `[S]` shows relevance and clarity
biting at a second layer: a retailer holding 2,650 supplier-supplied attribute values still has to decide
which of them a buyer can interpret at all. They were arguing about whether *can be hung on a rack* belonged
on a product page, and nobody in the room could say what one of their own attribute abbreviations meant.
**Producing the explanation is the manufacturer's act; choosing what to show from what arrived is the
retailer's.** One source — the `~makes` tags stay until a second confirms.

## ASSETS — Images and documents (Assets)

- `ASSETS-01` `IT` Have a proper home for product images and documents `[R, U]` +dam →G07
- `ASSETS-02` `DATA` Attach an image or document to a single product, a group of products, or one attribute `[R]` →G07
- `ASSETS-03` `IT` Give an image a public web address others can use `[R]` →G06
- `ASSETS-04` `IT` `°shifts` Resize, convert and process images automatically `[G]` →G07
- `ASSETS-05` `ORG DATA` Know which images we are actually allowed to use `[U]` ◐ →G10
- `ASSETS-06` `DATA` `°shifts` Capture what an image is, at the moment it is uploaded `[U]` →G05
- `ASSETS-07` `ORG` Check that images are good enough before they go out `[U]` +editorial →G11
- `ASSETS-08` `DATA` Hold different assets for different markets and channels `[U, R]` →G06
- `ASSETS-09` `IT` Handle assets in the volumes we actually have `[U, R]` +dam →G07
- `ASSETS-10` `DATA` Reuse one asset in many places `[U]` →G07
- `ASSETS-11` `IT` Get an image from where it is made to where it is published without anyone touching it `[P]` +dam →G07
- `ASSETS-12` `DATA` Handle the different kinds of image a product needs — the plain shot, the environment shot, the drawing `[P]` +dam →G03 →G04
- `ASSETS-13` `DATA` Say which image is used where — main, gallery, thumbnail, swatch `[X]` →G04
- `ASSETS-14` `IT` `°shifts` Produce the sizes, crops and formats each channel needs from one original `[X]` +dam →G07
- `ASSETS-15` `DATA` Attach images to a variant, not only to the product it belongs to `[X]` →G11
- `ASSETS-16` `IT` Hold the file itself, or only a pointer to it, and know which we are doing `[R]` +dam →G07
- `ASSETS-17` `DATA` `°shifts` Name and describe an asset so it can be found, and so it helps the page rank `[R]` →G05
- `ASSETS-18` `IT` Use another document system as a source, or send documents out to it `[R]` →G07
- `ASSETS-19` `ORG` Get assets to the people working in layout and design tools `[X]` +dam →G09
- `ASSETS-20` `ORG` `°shifts` Know when the images we have are not the images we need `[P]` +studio →G03

**This domain has a second job: it is a decision instrument.** A PIM has asset features; a DAM is a separate
system with a separate budget. **The way to find out which one an organisation needs is to walk this list.**
Wanting `ASSETS-11`, `ASSETS-12`, `ASSETS-14` and `ASSETS-19` describes a DAM whether or not anyone in the
room has said the word. Wanting only `ASSETS-02` and `ASSETS-03` does not.

**◐ `ASSETS-05` — image rights — has genuinely unknown salience.** Absent twice now, from two organisations
whose imagery arrives entirely from suppliers — six hours of discovery at `[S]`, and not one of its 33
recorded pain points, without a single mention. Two absences of the same business shape do not settle it;
they only sharpen the question. **The next test has to be a manufacturer or a brand**, where the rights are
created rather than received. Until then it stays ◐ and gets asked (`ASK-22`) rather than waited for.

**The diagnostic fires on evidence, not on complaints — and `[S]` is the case that proves it.** Zero of its
33 pain points mention images or documents at all. The same organisation defines 24 asset types, numbers
image sub-categories 1–10 purely to control display order on the storefront (`ASSETS-13`, solved with a
naming trick), relates documents to articles **by hand or by Excel export and re-import** (`ASSETS-11`,
entirely absent), and keeps safety data sheets in a separate external service (`ASSETS-18`).

**Silence in this domain means one of two things and they lead to opposite scopes: normalised manual work,
or genuinely low priority.** Nobody complains about a job they have always done by hand. Walk `ASK-19`,
`ASK-20`, `ASK-23` and `ASK-24` before the scope is set — a DAM is a separate budget, and this is the
single largest unconfirmed item in an engagement that looks quiet here.

## QUALITY — Quality (Quality)

- `QUALITY-01` `DATA` Require a minimum of information before a product counts as ready `[R, Y]` +validity →G03 →G04
- `QUALITY-02` `DATA` Have different definitions of "ready" for different purposes `[R, Y]` →G11
- `QUALITY-03` `ORG` Make someone responsible for each kind of information `[R, U, Y]` +governance →G11
- `QUALITY-04` `ORG DATA` Agree how information is written, and hold to it `[R, Y]` +standards →G11
- `QUALITY-05` `IT DATA` `°shifts` See the state of our information without having to ask anyone `[R, Y]` →G11
- `QUALITY-06` `IT` Go back to how the information looked before `[C, U, Y]` →G11
- `QUALITY-07` `IT` Protect some information from being changed at all `[U, X, Y]` →G11
- `QUALITY-08` `ORG` Agree how products are named `[X]` +standards →G11
- `QUALITY-09` `DATA` `°shifts` Know where our content is word-for-word what every competitor also publishes `[P]` +sameness +contentq +rivalwatch ~sources ~hosts →G05
- `QUALITY-10` `IT` `°core` Ask questions of our own catalogue in plain language `[W, Y]` +ai →G09
- `QUALITY-11` `DATA` Say what a valid value looks like, and refuse the ones that are not `[Y, S]` +validity →G04 →G11
- `QUALITY-12` `DATA` `°shifts` Notice when the same product has been entered twice `[Y]` +mdm →G11
- `QUALITY-13` `ORG DATA` Decide who wins when two sources disagree about the same field `[Y, S]` +mdm →G11
- `QUALITY-14` `DATA` `°core` Know which values a machine wrote and which a person wrote `[Y]` +ai →G11
- `QUALITY-15` `DATA` `°shifts` Know where we are publishing the same words on our own different channels `[Y]` +sameness ~direct →G05
- `QUALITY-16` `IT DATA` Know what breaks when we delete something `[P, Y]` +deletion +breakage +integration →G11

*Keep `QUALITY-16` and `MODEL-18` distinct. `MODEL-18` is knowing what breaks when you change the **shape**
— remove an attribute, restructure a tree. `QUALITY-16` is knowing what breaks when you remove an
**instance** — this product, this category node, this asset. Different questions, different people, usually
different answers.*

## ORGANISE — Organising the work (Organisation)

- `ORGANISE-01` `ORG` Work the same way across the organisation `[R, U]` →G12
- `ORGANISE-02` `ORG` Know who delivers, who improves, and who owns the catalogue `[R, U]` +governance →G13
- `ORGANISE-03` `IT ORG` Give people access only to what concerns them `[R, U]` +identity →G11
- `ORGANISE-04` `ORG` Keep it running after the project team leaves `[G, U]` →G13
- `ORGANISE-05` `ORG` Organise contributors in tiers, with different mandates `[U]` +governance →G12
- `ORGANISE-06` `IT` Give people accounts and permissions without manual work `[U]` +identity →G12
- `ORGANISE-07` `ORG` Make someone responsible for permissions locally `[U]` +identity →G12
- `ORGANISE-08` `ORG` Have training material, and someone whose job is to train `[U]` +training →G12
- `ORGANISE-09` `ORG IT` Have somewhere realistic to learn in, before touching the real thing `[U, P]` +training →G12
- `ORGANISE-10` `ORG IT` Keep developing the system after go-live `[U]` +ownership →G13
- `ORGANISE-11` `ORG IT` Keep the system maintained and running `[U]` +ownership →G13
- `ORGANISE-12` `ORG` Make sure the deadlines other people depend on are kept `[U, P]` +wfengine →G08
- `ORGANISE-13` `ORG` Remind people, centrally, what is waiting for them `[U]` +wfengine →G08
- `ORGANISE-14` `ORG` Have someone sign off before it goes out — for content, for technical accuracy, or because the law requires it `[U, P, Y]` +wfengine →G10
- `ORGANISE-15` `ORG IT` Get IT time after the project has closed `[P, Y]` +ownership →G13
- `ORGANISE-16` `ORG` Have a standing place where the departments involved actually meet `[P, Y]` +governance →G13
- `ORGANISE-17` `ORG` Have a budget of its own `[P]` +funding +ownership →G13
- `ORGANISE-18` `ORG` Fund the work by attaching it to something that already has a budget `[P]` +funding +ownership →G13
- `ORGANISE-19` `ORG` Know who is allowed to decide, not only who is responsible `[P, Y]` +governance →G13
- `ORGANISE-20` `ORG` Carry people through a change in how they work, not only train them `[P, Y]` +training →G12
- `ORGANISE-21` `ORG` Run the process without having to encode every step in a system `[P]` +workflow →G07
- `ORGANISE-22` `ORG` Take a report that the information is wrong, fix it, and tell the person who reported it `[Y]` +feedback →G11
- `ORGANISE-23` `ORG IT` Get the information back after we lose or corrupt it `[Y]` +recovery →G11
- `ORGANISE-24` `ORG` Agree what we call things, and keep a map from the old names `[Y]` +standards →G12
- `ORGANISE-25` `ORG IT` Encode the steps in the system when the process no longer fits in people's heads `[Y]` +workflow +wfengine →G08
- `ORGANISE-26` `ORG IT` Say who is allowed to destroy information, and make it hard to do by mistake `[P, Y]` +deletion +identity →G11

**On funding.** `ORGANISE-17` and `ORGANISE-18` are a pair, and the second is the common one: product
information rarely funds itself, and typically rides on e-commerce's budget on the argument that automating
product launches matters to the web. That carries a consequence worth stating aloud — **when the thing you
are attached to stops caring, the funding goes**, however well the work is going.

**On what disappears after a project.** People usually stay; product information teams have staff. What
goes is **IT time** (`ORGANISE-15`), and what rarely existed at all is a **standing forum between
departments** (`ORGANISE-16`).

**On workflow — `ORGANISE-21` and `ORGANISE-25` are a genuine either/or.** Implicit workflow is cheaper,
more adaptable and survives reorganisation; encoded workflow is auditable, measurable and does not depend on
everyone remembering. Which is right is a question about size, and about how much of the process one person
can still hold. **Salience rule:** `ORGANISE-21` is the question for a small or mid-size organisation,
`ORGANISE-25` for a large one — but `[S]` is a case the headcount reading cannot resolve. Thirty-four
member companies, six ERPs, a million articles, and a central product information function of two people
whose heads the process genuinely does still fit in. **The variable that decides is how many independent
parties the process crosses, not how many people work in it.** A federated organisation is large by that
measure even when its centre is tiny. One source. `ORGANISE-14` — sign-off — is where encoding earns its
place regardless of either reading.

## DELIVER — Sending it out (Distribute)

- `DELIVER-01` `IT` Send full product information to our own websites and shops `[R]` →G02
- `DELIVER-02` `IT DATA` Deliver to industry databases and partner platforms `[R]` +syndication ~indirect →G06
- `DELIVER-03` `IT` Be the one place receiving systems get product information from `[R]` →G07
- `DELIVER-04` `DATA` Produce the compliance documents we are required to, and keep the old ones `[R]` +compliance ~makes →G10
- `DELIVER-05` `IT DATA` Provide a digital product passport where the law requires one `[R, W]` +compliance ~makes →G10
- `DELIVER-06` `IT` Put documents and images where internal users expect to find them `[R]` →G09
- `DELIVER-07` `IT` Send information as files, not only through direct connections `[C]` →G07
- `DELIVER-08` `IT` Adapt what we send to suit each receiver `[C]` →G06
- `DELIVER-09` `IT` Generate a product sheet or datasheet as a file, without a designer `[X, P]` +publishing →G07 →G09
- `DELIVER-16` `ORG` Support a designer producing a catalogue or brochure from live information `[X]` +studio →G09
- `DELIVER-10` `DATA` Give one customer a file with their products, their prices, in their format `[X]` ~indirect →G09
- `DELIVER-11` `IT` Combine our information with data from another system as we send it `[X]` →G07
- `DELIVER-12` `DATA` Show the safety and responsibility information the law requires, in every listing `[W]` +compliance →G10
- `DELIVER-13` `DATA` Deliver in the classification standard a trading partner requires `[W, Y]` +syndication ~indirect →G06 →G10
- `DELIVER-14` `DATA` Keep a globally unique identifier for every product `[W, Y]` +syndication ~indirect →G10
- `DELIVER-15` `IT` `°core` Supply our product data to agents that shop on a customer's behalf `[W]` +agentready ~direct →G05
- `DELIVER-17` `IT` Add a new destination without changing the master `[Y]` ⚠ +integration →G06
- `DELIVER-18` `IT` Get a change out in minutes, not overnight `[Y, S]` +integration →G08

## PRESENT — Showing the product (Presentation)

- `PRESENT-01` `IT` Let customers narrow down to what they want `[C]` +search ~direct →G01
- `PRESENT-02` `IT` `°shifts` Suggest products that fit the customer and the moment `[C, X]` +search ~direct →G01 →G02
- `PRESENT-03` `DATA` `°shifts` Structure information so the products get found in search `[R]` ~direct →G03 →G05
- `PRESENT-04` `ORG` Give people more than one page layout, to fit the content `[U]` +cms ~direct →G12
- `PRESENT-05` `DATA` Build a sensible hierarchy and navigation through the content `[U]` +cms ~direct →G05
- `PRESENT-06` `DATA` Allow deeper pages under a main page `[U]` +cms ~direct →G03
- `PRESENT-07` `DATA` Not be locked to the text a single source system happens to hold `[U]` +cms ~direct →G05
- `PRESENT-08` `IT` Promote something with a teaser that fills itself in `[U]` +cms ~direct →G01
- `PRESENT-09` `DATA` Publish as web content rather than as PDFs `[U]` +cms ~direct →G05
- `PRESENT-10` `DATA` Show the same product consistently wherever the customer meets it `[P, Y]` ~direct →G11
- `PRESENT-11` `DATA` Meet each marketplace's rules for how a product must be presented `[P, Y]` +syndication ~indirect →G06
- `PRESENT-12` `DATA` Give the customer enough to decide without contacting us `[P]` ~direct →G03 →G04
- `PRESENT-16` `ORG` Give staff in the shop the same information the website has `[P, Y]` +instore ~direct →G09
- `PRESENT-17` `DATA` Produce packaging and label text from the same information `[P]` +publishing ~makes →G10
- `PRESENT-18` `DATA` `°core` Be found and cited when a customer asks an assistant instead of a search engine `[W, Y]` +agentready ~direct →G05

**Expect `PRESENT` to score low for any client whose storefront is somebody else's product.** Most of these
came from an editorial site; a commerce platform supplies page composition itself. That is the scope
boundary working, not neglect.

## MEASURE — Learning (Measure)

- `MEASURE-01` `DATA` Keep customer feedback, reviews and ad signals in one place `[A]` +analytics +feedback ~direct →G13
- `MEASURE-02` `DATA` Improve product information based on how it actually performs `[A]` +analytics ~direct →G13
- `MEASURE-03` `ORG` Put effort where it pays — the worst information, the highest returns, the best sellers, the live campaigns `[A, P]` +value →G01
- `MEASURE-04` `ORG` Feed what we learn back to product development and pricing `[A]` ~makes →G01
- `MEASURE-05` `DATA` `°shifts` Know which products perform badly, and why `[A]` +analytics ~direct →G04
- `MEASURE-06` `IT` Report on the business, not only on the data `[C, Y]` +analytics →G13
- `MEASURE-07` `DATA` `°shifts` See the health of our content, not only whether the fields are filled `[U, Y]` +analytics →G13
- `MEASURE-08` `ORG` Argue the value convincingly without being able to prove it `[P, Y]` +value →G13
- `MEASURE-09` `ORG` Agree where the clock starts and stops before measuring how long anything takes `[Y, S]` +value →G08

**The business case is always built on proxies** — hours saved, time to market, returns avoided. No client
has ever demonstrated what a specific change earned, and `MEASURE-08` says so honestly. The ability has two
halves and `MEASURE-03` carries the second: argue the value, then **prioritise by the same logic you argued
with**.

---

## Sibling groups

Some abilities only make sense next to each other. A shared `+tag` marks them; the ID never changes, and a
group may cross domains.

An ability can belong to more than one group; `QUALITY-16` and `QUALITY-09` each belong to two.

Three kinds of relationship, deliberately not distinguished in the notation but worth knowing:

| Tag | Members | Kind | What it means |
|---|---|---|---|
| `+selfserve` | `SOURCE-10` `SOURCE-15` `SOURCE-19` | set | The supplier serves themselves, the internal originator serves themselves, or somebody transcribes. Most organisations need all three |
| `+chasing` | `SOURCE-08` `SOURCE-22` | either/or | Have the capacity to chase, or do not need it |
| `+validity` | `QUALITY-01` `QUALITY-11` | pair | Is the field filled, versus is what is in it allowed |
| `+sameness` | `QUALITY-09` `QUALITY-15` | pair | Identical to competitors, versus identical to ourselves across our own channels |
| `+deletion` | `QUALITY-16` `ORGANISE-26` | set | What must be checked, and who is permitted |
| `+breakage` | `MODEL-18` `QUALITY-16` | pair | What breaks when the **shape** changes, versus when an **instance** is removed |
| `+funding` | `ORGANISE-17` `ORGANISE-18` | either/or | Its own budget, or attached to somebody else's |
| `+workflow` | `ORGANISE-21` `ORGANISE-25` | either/or | Keep the process in people's heads, or encode it. Size decides |
| `+value` | `MEASURE-03` `MEASURE-08` `MEASURE-09` | set | Argue the value, prioritise by the same logic, and agree where the clock starts |
| `+contentq` | `CONTENT-09` `CONTENT-10` `CONTENT-11` `QUALITY-09` | set | The four content qualities — relevant, clear, evocative, distinctive. Crosses domains |

**In a workshop the kind matters more than the membership.** An either/or means pick one and the choice is
the finding; a set means partial coverage is the finding.

**The third kind — a *cluster*, where the pattern is the finding rather than any single line — lives in
`Reveals` below.** Every reveal is a cluster: a group of abilities that together point at something the
organisation would have to acquire. That is why `Reveals` is the model's third level rather than an eighth
facet.

---

## Reveals — the capability layer

Every ability tested against one question — **when an organisation wants this, what would it have to
acquire?** A capability at the "have a PIM" altitude: a system, a person, a forum, a policy, a budget. Never
a product name. **This is the model's third level**, not an extra facet.

**31 capabilities behind 205 abilities; 120 of 205 reveal something, 85 reveal nothing.**

### Acquisition domains and configuration domains

| | Domains | Reveal rate | What that means |
|---|---|---|---|
| **Acquisition domains** | `ORGANISE` 88% · `PRESENT` 80% · `SOURCE` 71% · `MASTER` and `MIGRATE` 100% | high | Nearly every line is a thing you buy, staff or fund |
| **Configuration domains** | `STATUS` 11% · `CONTEXT` 20% · `ENRICH` 28% · `MODEL` 35% | low | Nearly every line is something you set up in what you already own |

That is a real finding and it changes how the register reads. **`MODEL`, `STATUS` and `CONTEXT` are almost
entirely configuration** — 25 of their combined 34 abilities cost nothing but thought and time. **`ORGANISE`
is almost entirely acquisition** — 23 of 26, which is another way of saying the organisational side is all
hiring, funding and convening, and none of it is configuration.

For a workshop that is directly useful: a client who is "doing a PIM project" is usually thinking about the
configuration domains, where nothing has to be bought. The money is in `ORGANISE`, and nobody puts it on the
agenda.

### The capabilities

| Points at | | Tag | Abilities | |
|---|---|---|---|---|
| **A digital asset management system** | buy | `+dam` | 8 | The worked example. Four of these eight were the original diagnostic, and it fired correctly on a live client. |
| **A supplier intake gateway** | buy | `+intake` | 8 | A gateway that validates and holds what arrives before it reaches the master. |
| **An integration platform** | buy | `+integration` | 7 | Not "we need integrations". The decision to build them one way, monitored, with a layer between master and consumers. |
| **An AI generation and inspection capability** | buy | `+ai` | 6 | Six abilities across five domains — which is exactly why AI is a facet, and this is where it is bought. |
| **A content management system** | buy | `+cms` | 6 | Almost entirely from the university. A commerce storefront supplies this; an editorial site has to buy or build it. |
| **Master data management beyond products** | buy | `+mdm` | 6 | Both holes the first live test found land here. A product information system alone will not settle identity, precedence or duplicates. |
| **An analytics platform** | buy | `+analytics` | 5 | Nothing in the register produces a number on its own. |
| **A workflow engine** | buy | `+wfengine` | 5 | Only worth buying when `ORGANISE-21` fails. The `+workflow` pair is the question; this is one of its two answers. |
| **Central identity and access management** | buy | `+identity` | 4 | At scale, accounts and permissions stop being a feature of anything. |
| **A syndication route to partner platforms** | buy | `+syndication` | 4 | Trading-partner formats and registered identifiers are a subscription, not a feature. |
| **A supplier self-service portal** | buy | `+portal` | 3 | Somewhere suppliers log in. Separable from the gateway — plenty of organisations need one and not the other. |
| **Translation management** | buy | `+translation` | 3 | One place for translation is a system decision, not a process one. |
| **Discoverability by assistants and agents** | buy | `+agentready` | 2 | The newest and least settled. Both abilities came from research, not from a client. |
| **A dedicated product information system** | buy | `+pim` | 2 | The floor the whole register stands on. Revealed by only two lines because every other line assumes it. |
| **An output and publishing engine** | buy | `+publishing` | 2 | Turning managed information into a formatted artefact — a datasheet, a label. |
| **A site search and merchandising engine** | buy | `+search` | 2 | Filtering and recommendation belong to the storefront — but they run on structure the master owns. |
| **A product configurator** ⚠ | buy | `+configurator` | 1 | The clearest case of the warning: a substantial purchase for a single need. |
| **A product data pool subscription** ⚠ | buy | `+datapool` | 1 | A real subscription for a narrow purpose. |
| **In-store colleague tooling** ⚠ | buy | `+instore` | 1 | One ability, and a large programme sitting behind it. |
| **Backup and recovery provision** ⚠ | buy | `+recovery` | 1 | Nobody asks for this until the first loss. |
| **Competitive content monitoring** ⚠ | buy | `+rivalwatch` | 1 | Needs data from outside the organisation — the objection that has always dogged `QUALITY-09`. |
| **An editorial function — someone whose job is writing** | staff | `+editorial` | 8 | The "writer nobody has hired" hypothesis, confirmed. Eight abilities, all judgement, none technical. |
| **A governance body that can decide** | staff | `+governance` | 7 | Seven abilities, and the capability most often missing altogether. |
| **Funded ongoing ownership** | fund | `+ownership` | 6 | Money and IT time after the project closes. The first thing to disappear. |
| **A regulatory compliance function** | staff | `+compliance` | 5 | Someone whose job is knowing what the law asks for this year. |
| **Migration capacity, hired or contracted** | staff | `+migration` | 4 | A one-off — that every system generation needs again. |
| **A staffed intake function** | staff | `+intaketeam` | 3 | People with time to chase. The constraint identified in interview cluster 1. |
| **Agreed standards and a glossary** | agree | `+standards` | 3 | Written agreements, not systems. Cheap to make, hard to keep. |
| **A training and change function** | staff | `+training` | 3 | Not only a curriculum — somewhere realistic to practise before touching the real thing. |
| **A route for outside signals to come back in** | staff | `+feedback` | 2 | A route for store colleagues, the contact centre and customers to report what is wrong. |
| **A design and production function** | staff | `+studio` | 2 | Commissioning new material and working with designers. Small — and absent from the one client tested. |

Members, in register order:

- `+dam` — `ASSETS-01` · `ASSETS-09` · `ASSETS-11` · `ASSETS-12` · `ASSETS-14` · `ASSETS-16` · `ASSETS-19` · `MASTER-03`
- `+intake` — `COLLECT-08` · `SOURCE-02` · `SOURCE-11` · `SOURCE-12` · `SOURCE-21` · `SOURCE-22` · `SOURCE-23` · `SOURCE-25`
- `+integration` — `COLLECT-02` · `COLLECT-05` · `COLLECT-06` · `DELIVER-17` · `DELIVER-18` · `MODEL-18` · `QUALITY-16`
- `+ai` — `CONTENT-03` · `ENRICH-06` · `MODEL-16` · `QUALITY-10` · `QUALITY-14` · `SOURCE-18`
- `+cms` — `PRESENT-04` · `PRESENT-05` · `PRESENT-06` · `PRESENT-07` · `PRESENT-08` · `PRESENT-09`
- `+mdm` — `COLLECT-10` · `MODEL-05` · `MODEL-09` · `MODEL-19` · `QUALITY-12` · `QUALITY-13`
- `+analytics` — `MEASURE-01` · `MEASURE-02` · `MEASURE-05` · `MEASURE-06` · `MEASURE-07`
- `+wfengine` — `ENRICH-08` · `ORGANISE-12` · `ORGANISE-13` · `ORGANISE-14` · `ORGANISE-25`
- `+identity` — `ORGANISE-03` · `ORGANISE-06` · `ORGANISE-07` · `ORGANISE-26`
- `+syndication` — `DELIVER-02` · `DELIVER-13` · `DELIVER-14` · `PRESENT-11`
- `+portal` — `SOURCE-10` · `SOURCE-19` · `SOURCE-24`
- `+translation` — `CONTEXT-05` · `ENRICH-11` · `MASTER-05`
- `+agentready` — `DELIVER-15` · `PRESENT-18`
- `+pim` — `MASTER-01` · `MASTER-02`
- `+publishing` — `DELIVER-09` · `PRESENT-17`
- `+search` — `PRESENT-01` · `PRESENT-02`
- `+configurator` — `MODEL-11`
- `+datapool` — `ENRICH-09`
- `+instore` — `PRESENT-16`
- `+recovery` — `ORGANISE-23`
- `+rivalwatch` — `QUALITY-09`
- `+editorial` — `ASSETS-07` · `CONTENT-01` · `CONTENT-02` · `CONTENT-04` · `CONTENT-09` · `CONTENT-10` · `CONTENT-11` · `CONTENT-12`
- `+governance` — `MASTER-06` · `ORGANISE-02` · `ORGANISE-05` · `ORGANISE-16` · `ORGANISE-19` · `QUALITY-03` · `SOURCE-17`
- `+ownership` — `MODEL-17` · `ORGANISE-10` · `ORGANISE-11` · `ORGANISE-15` · `ORGANISE-17` · `ORGANISE-18`
- `+compliance` — `DELIVER-04` · `DELIVER-05` · `DELIVER-12` · `MASTER-04` · `STATUS-09`
- `+migration` — `MIGRATE-01` · `MIGRATE-02` · `MIGRATE-03` · `MIGRATE-04`
- `+intaketeam` — `SOURCE-08` · `SOURCE-13` · `SOURCE-15`
- `+standards` — `ORGANISE-24` · `QUALITY-04` · `QUALITY-08`
- `+training` — `ORGANISE-08` · `ORGANISE-09` · `ORGANISE-20`
- `+feedback` — `MEASURE-01` · `ORGANISE-22`
- `+studio` — `ASSETS-20` · `DELIVER-16`

### Five capabilities serve one ability each ⚠

`+configurator` · `+datapool` · `+instore` · `+recovery` · `+rivalwatch`.

The model's own rule says a capability enabling exactly one ability is a warning — either the ability is
over-specified, or it is a point solution that probably should not be bought. **All five survive the test as
genuine point solutions**, which is the rule working rather than failing: each is a real, separate purchase
made for a single narrow need, and each deserves the question *is this worth it on its own?* before anyone
signs. `+configurator` is the sharpest case; `+recovery` is the one where the answer is usually yes anyway.

**`+datapool` needs the warning read the other way round, and it depends on business type.** At `[S]` the
data pool carries one ability and roughly eighty per cent of all enrichment: article data, imagery and its
type tags, environmental assessments, climate figures, hazard information, and the validation rules that
decide when a product is fit to publish. 1.4 million articles arrive through it. Losing the subscription
would take four other abilities with it, none of them tagged `+datapool`.

**A narrow subscription for a `~makes` organisation is existential infrastructure for a `~sources` one.**
That is the first concrete case the salience facet has had to stand on. **How many abilities a capability
bears and how much collapses without it are different measurements**, and the one-ability warning only
counts the first. Ask *is this worth it on its own?* — then ask what stops working if it is withdrawn.

### One ability that reveals nothing, deliberately

`SOURCE-09` — *have enough pull with a supplier to make them do the work themselves*. It looks like it should
point at something, and it does not. Leverage is a market position, not an acquisition; you cannot buy it,
hire it or convene it. **That is the facet working.** An ability with no reveal is a useful fact about it,
and this one says: if the pull is not there, no purchase will substitute, and `+intaketeam` is the fallback
you will be paying for instead.
---

---

## Business type — the two axes

The facet marks **where an ability bites**, not strict applicability. That is how it
was first described — *same abilities, different bite* — and it means "does not apply" and "applies but
rarely matters" both resolve to the same instruction: do not raise it. An ability with **no `~tag` bites for
everyone**, which is most of them.

### Axis one — origin: where product information comes from

| Tag | Means | Abilities |
|---|---|---|
| `~makes` | The organisation creates the product and owns its technical truth | 9 |
| `~sources` | Information arrives from suppliers it has chosen | 19 |
| `~hosts` | Third parties list into it; it did not choose each product | 18 |

### Axis two — audience: who it reaches

| Tag | Means | Abilities |
|---|---|---|
| `~direct` | It sells or presents to the end customer itself | 21 |
| `~indirect` | It reaches customers through somebody else's channel | 5 |
| `~none` | No commercial transaction at all | 0 — defined by what it lacks |

`~none` has no members on purpose. A non-commercial organisation is not served by a special set of
abilities; it is served by everything except the commercial ones, and tagging those `~direct` already
excludes them. The university that stress-tested this model mapped to most of the board, which is the same
fact stated the other way round.

**An organisation carries several values, and the filter is their union.** A retailer with an own-brand line
is `~sources ~makes`; the client tested against this register was `~sources ~makes ~hosts ~direct ~indirect`
and would be shown almost everything — correctly, because they were doing almost everything.

### Three findings worth having before you use it

**The audience axis has a gap.** A buying cooperative or voluntary chain sells to **part-owners** —
independent businesses running their own storefronts on shared data. That is neither `~direct` (they do not
face the end customer) nor `~indirect` (the recipient is not somebody else's channel in the sense that
marketplaces and trading partners mean). It shows up as `PRESENT` scoring 2 of 15 while the whole
distribution question stays live. **No new value is proposed on one case** — but note that `SOURCE-09` reads
differently for this shape too: collective volume, and central agreements a member can decline.

**It scopes; it does not narrow.** 54 of 205 abilities carry a type tag — 26%. A single-type client is still
shown between 159 and 190 of them. **This facet is not what makes the register walkable in a room**, which is
an earlier version of this note claimed. What it does is remove the ~25 lines that would be
actively *wrong* to raise — asking a pure manufacturer about supplier portals, or a wholesaler about
packaging copy. It prevents embarrassment rather than saving time. The narrowing has to come from elsewhere:
from salience, or more practically from choosing which domains to walk.

**`~hosts` is thin, and thinner since draft 21.** It now shares all 17 of its abilities with `~sources` and
owns none outright. `MODEL-20` was the one it owned, until `[S]` — a buying cooperative, not a marketplace —
raised it over commodity timber and batch-level safety data. The tag came off and the line now bites for
everyone.

The case for keeping the value at all now rests entirely on one thing: **an organisation that hosts
third-party listings has no purchase order and no contract to lean on, so `SOURCE-09` reads completely
differently.** That is still plausible and still untested. **Decide it against the next marketplace or
platform client, or fold `~hosts` into `~sources`.**

### Sources versus hosts, in full

- Only `~sources`: `SOURCE-09` (leverage over a chosen supplier) · `CONTENT-12` (decide where to write our
  own and where the supplier's will do) — both assume you picked the supplier.
- Only `~hosts`: none since draft 21. `MODEL-20` was the sole member and is now untagged — see the note
  above.
- Shared: everything else in both sets.
---

---

## Serves — the thirteen goals

Every goal is an **outcome**, not an activity and not a system. None of them names a tool, and none of them
can be satisfied by pointing at another ability — which is what made six of the old entries circular.

| | Goal | | Abilities |
|---|---|---|---|
| `→G01` | **Sell a better version than the one they came for** | sell | 9 |
| `→G02` | **Sell the things that go with it** | sell | 6 |
| `→G03` | **Lose fewer sales at the last moment** | sell | 14 |
| `→G04` | **Get fewer things sent back** | sell | 8 |
| `→G05` | **Be found by people who do not know our name** | sell | 12 |
| `→G06` | **Start selling somewhere new without it becoming a project** | sell | 19 |
| `→G07` | **Spend less time on work nobody should be doing by hand** | cost and speed | 48 |
| `→G08` | **Get products in front of customers sooner** | cost and speed | 19 |
| `→G09` | **Let the people who sell spend their time selling** | cost and speed | 8 |
| `→G10` | **Stay on the right side of the law** | risk | 12 |
| `→G11` | **Stop being wrong where customers can see it** | risk | 32 |
| `→G12` | **Keep the people who know how to do this** | people | 16 |
| `→G13` | **Keep the work funded past the first year** | people | 14 |

**All 205 abilities now serve at least one goal.** That was the target: `serves` exists to answer *"why
should we care about this?"* in the client's own language, so an ability with no answer is an ability with no
justification. Eleven serve two.

### What the shape says

`→G07` *spend less time on work nobody should be doing by hand* carries 48 abilities and `→G11` *stop being
wrong where customers can see it* carries 32. Together they justify nearly 40% of the register. That is
honest rather than lazy: **efficiency and error-avoidance are the two broadest arguments in this subject**,
and they are also the two a client will accept without needing to be convinced.

The commercial goals are much smaller — six to fourteen abilities each. Worth knowing before a board
conversation: **the register is far better at arguing cost and risk than at arguing revenue.** That is a
property of product information work, not a defect in the list.

---

## Who to invite

**`Who cares` is retired as a facet.** Reviewing it showed the old list of five roles was
missing the most-served constituency in the register, and tagging 205 abilities with roles would have
produced a lookup nobody consults. **The information belongs where it is used: on the question.**

Every one of the 54 questions now carries a **Who to invite** line. It is the same information doing a job
instead of sitting in a table, and it answers the only thing a role list is actually for: **whose diary to
book.** A workshop with the right questions and the wrong people fails, and fails invisibly.

### The roles, ranked by how many of the 54 questions need them

| Role | Questions |
|---|---|
| **whoever owns product information** | 26 |
| **whoever enriches products** | 21 |
| **whoever owns a channel** | 16 |
| **whoever owns the integrations** | 13 |
| **a merchandiser** | 11 |
| **whoever makes the catalogues and the photographs** | 7 |
| **whoever deals with suppliers** | 5 |
| **whoever holds the budget** | 5 |
| **somebody from outside the product team** | 4 |
| **whoever answers to the regulator** | 4 |
| **whoever reports the numbers** | 3 |
| **somebody from the contact centre** | 2 |
| **a supplier, if you can get one** | 1 |
| **somebody who works in a shop** | 1 |

Roles are described by what somebody does rather than by a job title, for the same reason abilities are:
titles vary between organisations and *PIM manager* names a person after the tool they hold.

### Five questions one person can answer alone

`ASK-09` the writer's desk · `ASK-11` whose budget · `ASK-23` the designer's copy · `ASK-37` the feeds ·
`ASK-41` one product enriched. Useful when a full session cannot be arranged — each is a short conversation
with one person that still reaches real abilities.
---

---

## Deliberately out of scope

Not gaps. Things a product information engagement runs into and hands to somebody else. Saying so is more
useful than padding the register, and in a workshop it is a faster answer than a vague one.

| Excluded | Belongs to | Note |
|---|---|---|
| Show ratings, reviews and customer photos next to the product | E-commerce platform | `MEASURE-01` still covers *holding* review and feedback signals, because those inform what to improve. Displaying them does not reach your table. |
| Let customers compare similar products side by side | E-commerce platform / merchandising | Depends on good structured attributes — which `MODEL` already covers — but the comparison feature itself is not yours. |
| Benchmarking against other organisations | Nobody | Attempted by vendors, but no comparable numbers exist. |

The boundary that emerges: **you advise on what the information must be and where it must reach, not on the
interface features that consume it.** `PRESENT-11` marketplace rules and `PRESENT-17` packaging text stay in, because
both are demands on the *information*. `PRESENT-14` and `PRESENT-15` are demands on the *interface*.

---

---

## Kinds of product information

A short vocabulary, not a set of abilities. It sits alongside the three lists your `Definitions` node already
holds — Standard Activities, Standard Business Roles, Standard Business Value statements — as a fourth:
**standard kinds of product information**. `MODEL-03` says "handle every kind of information we hold about a
product" and never said what those were. Now it can point here.

| Kind | What it is |
|---|---|
| **Identifiers** | What uniquely names the product — article number, EAN, model number |
| **Specifications** | Measurable fact — dimensions, materials, capacity, performance |
| **Classification** | Where it sits — categories, families, standard codes |
| **Relations** | What connects to what — accessories, spares, replacements, bundles |
| **Status** | Whether it exists, is visible, is sellable, is obtainable |
| **Compliance** | What the law or a standard requires — warnings, declarations, certificates |
| **Descriptive content** | What somebody wrote — names, descriptions, selling points |
| **Imagery and media** | What somebody produced — packshots, environment shots, drawings, video |

---

## The second quality axis

Completeness is a property of the *record*. Four further qualities are properties of the *content*:

| Quality | Fails when | Ability |
|---|---|---|
| **Relevant** | there is too much, and the buyer must wade | `CONTENT-09` |
| **Clear** | it is correct but unintelligible to a buyer | `CONTENT-10` |
| **Distinctive** | it is word-for-word what competitors publish | `QUALITY-09` |
| **Evocative** | it informs but moves nobody | `CONTENT-11` |

**They are properties of the kinds above, not a facet on every ability.** Which apply depends on what kind of
information is being discussed:

| Kind | Relevant | Clear | Distinctive | Evocative |
|---|---|---|---|---|
| Identifiers | — | — | — | — |
| Specifications | ✓ | ✓ | — | — |
| Classification | ✓ | — | sometimes | — |
| Relations | ✓ | — | ✓ | — |
| Status | — | — | — | — |
| Compliance | — | — | — | — |
| Descriptive content | ✓ | ✓ | ✓ | ✓ |
| Imagery and media | ✓ | ✓ | ✓ | ✓ |

Do not chase distinctiveness or evocativeness on identifiers, status or compliance data — completeness and
accuracy are the only axes that apply there (`QUALITY-01`).

**Distinctiveness needs care in a room.** The other three can be judged by looking at the organisation's own
content; distinctiveness can only be judged against competitors', which is data most organisations do not
have (`QUALITY-09`). It also **trades off against relevance and clarity** — supplier copy is often more
relevant and clearer than what an organisation would write itself, so buying distinctiveness by rewriting can
cost the other two. These four are trade-offs to reason about, not a scorecard to maximise. `CONTENT-12` is
the ability to make that trade-off deliberately.

---

## AI — where it changes the answer

Marks **where AI changes the answer**: 29 of 205 abilities, inline beside the pillar. **AI is not a fourth
pillar** — it is a *modifier* of the three that exist. 24 of the 29 carry no `ORG` pillar today, because AI
output is probabilistic and somebody must accept, review or absorb being wrong. **The `°` mark therefore
carries an implied organisational cost, appearing only if the AI path is chosen** — and that is the cost
clients forget to budget for.

### The two marks

**`°core` — the ability barely exists without AI.** Six of them, and note how recent they are: four were
added in the last four drafts.

- `ENRICH-06` — Let AI write or fill in product information
- `CONTENT-03` — Tell a writer how good their text is, while they are writing it
- `QUALITY-10` — Ask questions of our own catalogue in plain language
- `QUALITY-14` — Know which values a machine wrote and which a person wrote
- `DELIVER-15` — Supply our product data to agents that shop on a customer's behalf
- `PRESENT-18` — Be found and cited when a customer asks an assistant instead of a search engine

**`°shifts` — AI materially changes how it is done, but the ability predates it and survives without it.**
Twenty-three.

- `SOURCE-02` — Reshape what a supplier sends into our own structure
- `SOURCE-12` — Know how good each supplier's information is
- `SOURCE-18` — Get product information out of documents written for another purpose  ⚑
- `COLLECT-10` — Recognise an incoming product by something other than our own article number
- `MODEL-16` — Have relations appear from classification, without anyone making them by hand
- `ENRICH-11` — Translate automatically
- `CONTENT-04` — Help people write short descriptions that actually work
- `CONTENT-09` — Cut a large technical dataset down to what a buyer actually needs
- `CONTENT-10` — Say what a technical specification means to the person buying it
- `CONTENT-11` — Make someone feel something about the product, not just understand it  ⚑
- `ASSETS-04` — Resize, convert and process images automatically
- `ASSETS-06` — Capture what an image is, at the moment it is uploaded
- `ASSETS-14` — Produce the sizes, crops and formats each channel needs from one original
- `ASSETS-17` — Name and describe an asset so it can be found, and so it helps the page rank
- `ASSETS-20` — Know when the images we have are not the images we need  ⚑
- `QUALITY-05` — See the state of our information without having to ask anyone
- `QUALITY-09` — Know where our content is word-for-word what every competitor also publishes  ⚑
- `QUALITY-12` — Notice when the same product has been entered twice
- `QUALITY-15` — Know where we are publishing the same words on our own different channels
- `MEASURE-05` — Know which products perform badly, and why
- `MEASURE-07` — See the health of our content, not only whether the fields are filled  ⚑
- `PRESENT-02` — Suggest products that fit the customer and the moment
- `PRESENT-03` — Structure information so the products get found in search

**⚑ marks the ones talked about far more than they are done — and the sharper reading is *rarely done
well*.** Five lines. At `[S]`, `SOURCE-18` runs in production at scale: their industry data pool parses
supplier declaration PDFs to extract environmental figures, and the client's own staff read descriptions and
key attributes in by hand. The client's own complaint is that the result is **unreliable**, not that it does
not exist.

**So ⚑ is not "they have not tried it".** It is *rarely done well*, and often *done by somebody else*: an
organisation can be consuming document extraction it did not build, cannot inspect and does not trust.
**Ask who performs it, and whether they check the output** — a client who says "we already have AI reading
PDFs" then has the right follow-up waiting for them.

### The workshop use

One pass, late in a session, once the abilities are already on the table: **"which of these would you answer
differently if AI were good at it?"** The `°` marks tell you which 29 are worth putting in front of them, and
the ⚑ marks tell you which answers to discount.
---

---

## Counts

15 domains · **205 abilities** · 0 gaps · 7 retired · 31 capabilities revealed · 54 type-tagged ·
29 AI-marked · 13 goals · 54 workshop questions · 1 provisional (⚠) · 1 unknown salience (◐).

By domain: `SOURCE` 21 · `COLLECT` 10 · `MIGRATE` 4 · `MASTER` 6 · `MODEL` 20 · `STATUS` 9 · `CONTEXT` 5 ·
`ENRICH` 14 · `CONTENT` 12 · `ASSETS` 20 · `QUALITY` 16 · `ORGANISE` 26 · `DELIVER` 18 · `PRESENT` 15 ·
`MEASURE` 9.

Retirements, the counts history and every decision's reasoning are in `px-model-background.md`.

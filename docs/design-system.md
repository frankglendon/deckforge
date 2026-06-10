# Design system / 设计系统

A McKinsey-inspired system, calibrated against a **public** executive report
("Global Economics Intelligence" style) and the firm's publicly documented brand
principles. Generic substitute fonts only — no proprietary assets.

> 参考公开的麦肯锡式高管报告与其公开的品牌原则提炼；仅用通用替代字体，不含任何专有素材。

## 1. Principles / 原则

- **High contrast: deep navy vs. white.** The single strongest signal of the look.
  深蓝 vs 纯白的高对比，是整套观感最强的信号。
- **Serif headlines, sans body.** Characterful serif (Bower → **Georgia**) for
  headlines; clean sans (Theinhardt → **Arial/Helvetica**) for body.
  标题衬线、正文无衬线。
- **Monochrome text.** Running text (titles + body) is **black**, not colored.
  Emphasis comes from **bold lead phrases** and the serif, not from accent colors.
  正文与标题**纯黑单色**，强调靠加粗引导句和衬线，不靠染色。
- **Color lives in charts & furniture.** Navy + cyan in charts; cyan for the one
  key datapoint, links, dividers, kicker. 颜色只出现在图表与装饰件里。
- **One highlight per chart.** Cyan marks *the single most important* datapoint.
  每图至多一个高亮。
- **Hairlines & whitespace.** A thin rule under every title and above the footer;
  generous margins. 标题下/页脚上各一条细横线，留白充足。
- **Signature line motif.** A stack of thin cyan lines (cover/divider) echoes the
  McKinsey line-pattern. 细线条 motif 呼应麦肯锡线纹。

## 2. Palette / 配色 (`deckforge/theme.py`)

| Token | HEX | Use |
|---|---|---|
| `dark_bg` deep navy | `#041C2C` | cover / dividers / conclusion background |
| `primary` / `accent` cyan | `#00A9F4` | the one key datapoint · links · accents |
| `title` | `#000000` | serif headlines |
| `text` | `#1A1A1A` | body (near-black) |
| `grey` | `#757575` | kicker · footnotes |
| `rule` | `#9AA3AB` | hairlines |
| `light_grey` | `#BFC6CC` | borders / table zebra |
| chart series | `#041C2C` `#00A9F4` `#99C7E5` `#7F8C99` `#2251FF` `#C2CBD2` | navy/cyan/blue/slate, ≤7 |

## 3. Typography / 字体

| Role | Latin | CJK | Size (pt) |
|---|---|---|---|
| Headline (serif) | Georgia *(→ Bower)* | **KaiTi 楷体** | 20 (title) / 26–36 (cover/divider) |
| Body (sans) | Arial *(→ Theinhardt)* | **KaiTi 楷体** | 12 |
| Chart labels / titles | Arial | KaiTi | 12 bold / 14 bold |
| Kicker · source · footer | Arial | KaiTi | 8–9 |

> McKinsey China uses **楷体 (KaiTi)** — so both heading and body East-Asian fonts
> default to KaiTi. CJK glyphs get an explicit `<a:ea>` typeface + `lang` tag so
> they never render as tofu boxes.

If you have the real fonts (Bower, Theinhardt / "McKinsey Sans"), just set them:

```python
from deckforge import Deck, Theme
theme = Theme(font_heading="Bower", font_body="Theinhardt",
              font_heading_ea="KaiTi", font_body_ea="KaiTi")
deck = Deck(theme=theme, brand="Your Firm")
```

## 4. Re-brand in one place / 一处换肤

Every module reads from the `Theme`. To re-skin the whole deck (e.g. a different
firm's blue, or a non-McKinsey look), construct a `Theme` and pass it in:

```python
from deckforge import Theme, hex_rgb
theme = Theme(
    primary=hex_rgb("2251FF"), accent=hex_rgb("00C0E0"),
    dark_bg=hex_rgb("0B1F3A"), title=hex_rgb("0B1F3A"),
    accent_text=True,   # opt into MBB / dense-emphasis style colored emphasis on key terms
)
```

- `accent_text=False` (default) → **McKinsey-faithful monochrome** text.
- `accent_text=True` → key terms / numbers in titles & body get the accent color
  (a denser, "MBB" emphasis style).

## 5. Page furniture / 版面构件 (from `Deck`)

| Method | Page type |
|---|---|
| `cover(...)` | navy cover: brand · serif title · subtitle · meta · CTA · line motif |
| `core_questions(...)` | three-question opener (cards) |
| `agenda(...)` | contents with colored number blocks + one-line chapter summaries |
| `section_divider(...)` | navy divider + **mini-TOC** + implication bar |
| `content(...)` | title + rule + **left visual** + **right justified body** |
| `content_blocks(...)` | title + rule + left visual + **Facts/Insights/Implications** |
| `wide_slide(...)` | full-width content (tables, big frameworks) |
| `conclusion(...)` | navy closing statement |
| `charts.*`, `tables.*` | native charts; themed comparison table + `takeaway_bar` |

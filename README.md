<div align="center">

# DeckForge

**Programmatic, consulting-grade desk-research decks — built from data, in code.**

*用代码生成咨询级（麦肯锡风格）案头研究 PPT*

[Quick start](#-quick-start) · [Design](#-design-system) · [Methodology](#-methodology) · [中文](#中文)

![overview](assets/screenshots/00-overview.png)

</div>

---

DeckForge turns structured research into a clean, **McKinsey-style** market-research
deck — entirely with [`python-pptx`](https://python-pptx.readthedocs.io/). No
template files, no proprietary fonts, no manual slide-pushing. Every chart is a
**native, editable PowerPoint object** (not a screenshot), every page follows a
consulting skeleton, and the whole look re-brands from a single `Theme`.

> **Why it exists.** It's the open, desensitized distillation of a real
> desk-research production pipeline — the *capability* (method + toolkit), with
> all client-confidential content removed and the design re-built as a generic,
> McKinsey-inspired system.

## Features

- **Native everything** — charts (column/bar/line/doughnut), tables, shapes, all
  editable in PowerPoint. One accent color highlights *the single key datapoint*.
- **McKinsey-faithful design** — deep-navy + white high contrast, **serif
  headlines** (Georgia, sub. for Bower) over **sans body** (Arial, sub. for
  Theinhardt), hairline rules, the signature thin-line motif. Chinese uses
  **KaiTi (楷体)**, as McKinsey China does.
- **Consulting skeleton** — cover → three core questions → contents → section
  dividers (with mini-TOC) → content pages (left visual + right body) →
  comparison tables → Facts/Insights/Implications blocks → conclusion.
- **Reproducible & re-brandable** — swap one `Theme` to change the entire palette
  and typography. Builds on a blank presentation; runs anywhere.
- **Bilingual / i18n-ready** — English and Chinese example decks; CJK text uses
  **KaiTi (楷体)**, and UI strings switch via a `labels=` dict (`lang="zh-CN"`).
- **Batteries-included pipeline** — image fetch + perceptual-hash dedup, a
  research-data schema, and a visual-QC recipe (LibreOffice → PDF → PNG).

## Quick start

```bash
pip install -r requirements.txt
python examples/ev_market/build_deck.py      # English  -> output/ev_market.pptx     (51 slides)
python examples/ev_market/build_deck_zh.py   # 中文      -> output/ev_market_zh.pptx  (51 slides)
```

```python
from deckforge import Deck, charts

deck = Deck(brand="Acme Research", footer="Acme Research")
deck.cover("Global EV Market", subtitle="Desk research", meta="2026", cta="EXPLORE")

slide, (x, y, w, h) = deck.content(
    "Demand keeps climbing as affordable EVs reach the market",
    body=[("Momentum is intact.", "Sales rose from ~10m (2022) to ~17m (2025E)."),
          "The open question is whether affordability carries volume to mass market."],
    kicker="Global EV Market  |  Part 1  |  2026",
    sources=[("IEA", "https://www.iea.org")],
)
charts.column(slide, deck.theme, x, y + 0.55, w, h - 0.6,
              ["2022", "2023", "2025E"], {"Units (m)": [10, 14, 17]}, highlight=(0, 2))
deck.save("ev_market.pptx")
```

## Quality bar

DeckForge is built to produce **formal, client-grade deliverables** — not toy
demos. A deck should be **complete and substantive**: the full skeleton (cover →
core questions → contents → executive summary → multiple sections, each with a
divider + mini-TOC and several dense pages → conclusion → methodology → appendix),
at real consulting-report **density** (~50-60 pages for a market study), and as
**professional, organised and information-rich** as a top-tier strategy report.
The bundled EV example (**51 slides**) is the reference standard — match or
exceed it. 交付物必须是完整、专业、信息充实的客户级报告，对标内置 51 页示例的深度。

## The example deck

A complete, **51-slide, client-grade** deck on the **(public, illustrative) global EV
market** — no client data. Page types shown:

| | |
|---|---|
| ![cover](assets/screenshots/01-cover.png) | ![content](assets/screenshots/05-content-chart.png) |
| Navy cover + serif title + line motif | Title + rule + native chart + body |
| ![table](assets/screenshots/07-comparison-table.png) | ![blocks](assets/screenshots/09-insight-blocks.png) |
| Comparison table + takeaway bar | Facts / Insights / Implications |

## Design system

Calibrated to a public McKinsey-style executive report. Full spec in
[`docs/design-system.md`](docs/design-system.md).

| Token | Value | Note |
|---|---|---|
| Deep navy | `#041C2C` | cover / dividers / conclusion |
| Cyan accent | `#00A9F4` | the one key datapoint + links |
| Chart series | navy + cyan + blue/slate variants | ≤7 colors |
| Heading | **Georgia** serif, black, + hairline rule | sub. for Bower |
| Body | **Arial** sans, near-black, monochrome | sub. for Theinhardt |
| CJK | **KaiTi (楷体)** | McKinsey China style |

Re-brand by passing your own `Theme(...)` — see [docs/design-system.md](docs/design-system.md).

## Methodology

The desk-research method behind the layout (three-layer logic, the deck
skeleton, writing principles, research/image/QC pipelines, and python-pptx
pitfalls) is documented in [`docs/methodology.md`](docs/methodology.md).

## Project layout

```
deckforge/        # the toolkit: theme, text, core (Deck), charts, tables, components, images
examples/ev_market/   # runnable demo (research.json + build_deck.py)
docs/             # design-system.md, methodology.md
assets/           # screenshots
```

## Attribution & scope

Design language is **inspired by** publicly available consulting reports. This
project is **not affiliated with or endorsed by** McKinsey & Company or any
firm; it bundles **no proprietary fonts, templates or trademarks** (Georgia /
Arial / KaiTi are generic substitutes for Bower / Theinhardt). All example data
is round / illustrative. MIT licensed — see [LICENSE](LICENSE).

---

<a name="中文"></a>

## 中文

**DeckForge** 用 `python-pptx` 把结构化研究数据生成一份干净的**麦肯锡风格**案头研究 PPT：无需模板文件、无专有字体、不手动拖页。每个图表都是**原生可编辑的 PowerPoint 对象**（不是截图），每页遵循咨询骨架，整套视觉通过一个 `Theme` 一键换肤。

> 它是一条真实案头研究生产线的**开源脱敏版**——保留能力（方法 + 代码工具箱），剔除全部客户机密内容，并把设计重建为通用的、麦肯锡风格的设计系统。

**特点**：原生图表/表格（单点 accent 高亮）· 忠实麦肯锡设计（深蓝+纯白高对比、**衬线标题**Georgia〔替代 Bower〕+ **无衬线正文**Arial〔替代 Theinhardt〕、细横线、线条 motif、**中文用楷体 KaiTi**）· 完整咨询骨架（封面→三问→目录→隔页含小目录→内容页→对比表→事实/洞见/启示→结论）· 一个 `Theme` 换肤 · 图片去重 + 研究数据 schema + 渲染 QC。

**快速开始**：`pip install -r requirements.txt` 然后 `python examples/ev_market/build_deck.py` → 生成 **51 页客户级**全球电动车市场示例 deck（公开/示意数据，无客户内容）。

**方法论**见 [`docs/methodology.md`](docs/methodology.md)，**设计系统**见 [`docs/design-system.md`](docs/design-system.md)。

**声明**：设计语言参考公开咨询报告，**与麦肯锡等机构无关联**，不含任何专有字体/模板/商标，示例数据均为示意。MIT 许可。

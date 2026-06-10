# Example — Global EV Market / 示例：全球电动车市场

A complete, runnable **51-slide, client-grade** desk-research deck on the
**global EV market**, built entirely with DeckForge. All figures are **round /
illustrative** for a public demo — no client-confidential content. This is the
**reference standard** for a DeckForge deliverable: match or exceed its depth.

完整可跑的 **51 页客户级**案头研究示例 deck（全球电动车市场），数据均为公开/示意；它是
DeckForge 交付物的**基准标准**。

Two language versions are provided — **English** (`build_deck.py`) and
**Chinese / 中文** (`build_deck_zh.py`), same structure and data.
提供**英文**与**中文**两个版本，结构与数据一致。

## Run / 运行

```bash
pip install -r ../../requirements.txt
python build_deck.py        # -> output/ev_market.pptx     (English)
python build_deck_zh.py     # -> output/ev_market_zh.pptx  (中文)
```

The Chinese deck sets `Theme(lang="zh-CN")`, uses **KaiTi (楷体)** for CJK text
(McKinsey-China style), and switches UI strings (PART / In this part / Source /
Implication) via the `labels=` argument — see the top of `build_deck_zh.py`.
中文版用楷体、`lang="zh-CN"`，并通过 `labels=` 切换界面标签（第 X 部分 / 本部分内容 /
来源 / 启示）。

Optional visual check (needs LibreOffice + PyMuPDF):

```bash
soffice --headless --convert-to pdf --outdir output output/ev_market.pptx
python -c "import fitz; d=fitz.open('output/ev_market.pdf'); [d[i].get_pixmap(matrix=fitz.Matrix(2,2)).save(f'output/p{i+1}.png') for i in range(d.page_count)]"
```

## Structure / 结构（51 页）

| Block | Pages | Highlights |
|---|---|---|
| Front matter | cover · disclaimer · three core questions · contents · executive summary | navy cover + line motif, card opener, 2-col exec summary |
| Part 1 — Market & momentum | divider + ~8 pages | column/line/doughnut/bar charts, a regional comparison table, KPI grid, section takeaways |
| Part 2 — Demand & buyers | divider + ~8 pages | buyer-segment table, BEV/PHEV mix, price-band KPIs, TCO chart, barriers |
| Part 3 — Competitive landscape | divider + ~10 pages | share bar, two-archetype table, competitor profiles, China exports, **value-chain chevron**, software-defined vehicle |
| Part 4 — Technology & trends | divider + ~8 pages | battery-chemistry table, charging/ADAS charts, software blocks |
| Part 5 — Opportunities & strategy | divider + ~8 pages | opportunity KPI map, profit-pool chart, strategic-options table |
| Closing | conclusion · recommended priorities · methodology & sources · glossary · back cover | bookend to the 3 questions, hyperlinked source list |

Every content page = action-title conclusion + a **native** chart/table/framework
+ analysis (body or Facts/Insights/Implications) + cited sources.

## Files / 文件

- `research.json` — demonstrates the research-data schema (`topic → facts[...]`).
- `build_deck.py` — constructs all 10 pages with the DeckForge API.
- `output/` — generated artifacts (git-ignored; regenerate by running the script).

Swap in your own topic by editing `build_deck.py` (and feeding your own verified
data). Change the whole look by passing a custom `Theme` — see
[`../../docs/design-system.md`](../../docs/design-system.md).

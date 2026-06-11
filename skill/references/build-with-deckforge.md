# Driving the deckforge engine

How to turn a filled spec (STEP 5-7) into a deck. Two paths: a **JSON spec** (fastest, also
what the web app uses) or the **Python API** (full control). Either way charts are native and
editable, and one `Theme` re-brands the whole deck.

---

## Path A — JSON spec (recommended for Dummy-first)

The Dummy Pages skeleton *is* the spec; filling data just adds values. One call builds it:

```python
from deckforge.spec import build_from_spec
import json

spec = json.load(open("examples/sample_spec.json"))      # your filled skeleton
deck = build_from_spec(spec, brand="Acme Research",
                       footer="Acme Research", lang="en-US", accent="00A9F4")
deck.save("output/deck.pptx")
```

`build_from_spec(spec, *, brand, footer, lang, accent)` — brand/footer/lang/accent passed
here override the JSON. `lang="zh-CN"` renders Chinese in KaiTi.

Page `type` values (one object per page in `spec["pages"]`):
`cover, questions, agenda, divider, content, content_blocks, table, prose, conclusion,
sources, back_cover`. A `content`/`content_blocks` page may carry a `chart` object
(`column | bar | line | doughnut`, with `categories`, `series`, optional `highlight`).

Run `python examples/ev_market/research.json`-style data through it, or start from
`examples/sample_spec.json` (the web-app sample). The web app (`python app.py`) is the
no-code front door to exactly this call.

---

## Path B — Python API (full control)

```python
from deckforge import Deck, charts, tables, components

deck = Deck(brand="Acme Research", footer="Acme Research")     # lang=, accent= optional
deck.cover("Global EV market", subtitle="Desk research", meta="2026")
deck.core_questions(headline, intro, cards)                    # the 3 opening questions
deck.agenda(headline, items)                                   # contents
deck.section_divider(part_no, title, subtitle, toc_items, takeaway=...)

slide, (x, y, w, h) = deck.content(
    "Cheaper models lift volume, but growth is cooling",       # full cause->effect title
    body=[("Momentum is intact.", "Sales rose ~10m (2022) to ~17m (2025E)."),
          "The open question is affordability into the mass market."],
    sources=[("IEA", "https://www.iea.org")])
charts.column(slide, deck.theme, x, y+0.55, w, h-0.6,
              ["2022","2023","2025E"], {"Units (m)": [10,14,17]}, highlight=(0,2))

deck.content_blocks(title, blocks, ...)        # visual left + Facts/Insights/Implications
deck.prose(title, paragraphs, columns=2)       # dense text page
tables.table(slide, deck.theme, ...); tables.takeaway_bar(...)   # comparison + takeaway
deck.conclusion(headline, body_lines, sources) # answers the opening questions
deck.back_cover("Thank you")
deck.save("output/deck.pptx")
```

Native chart helpers: `charts.column / bar / line / doughnut` — each takes a `highlight`
to accent the single most important datapoint. Insight blocks: `components.insight_*`.
Frameworks (KPI grid, 2x2, value-chain chevron, image row): `deckforge.frameworks`.

---

## Re-brand and bilingual

- One `Theme` swaps palette/fonts/sizes for the whole deck — see `../docs/design-system.md`
  §4. Pass `accent` for the one highlight colour.
- `Deck(..., lang="zh-CN")` or `build_from_spec(..., lang="zh-CN")` renders CJK in KaiTi
  (explicit `<a:ea>` typeface, so no tofu). UI strings switch via the `labels` dict.

---

## QC the output

Render and eyeball every page (see `quality-qc.md`):

```bash
soffice --headless --convert-to pdf --outdir output output/deck.pptx
python - <<'PY'
import fitz                       # PyMuPDF: render pages to PNG for a contact sheet
doc = fitz.open("output/deck.pdf")
for i, p in enumerate(doc):
    p.get_pixmap(dpi=120).save(f"output/page_{i:02d}.png")
PY
```

Then sweep the 6 layout-defect classes + 7 content rules in `quality-qc.md`. Never embed
API keys in any script or example.

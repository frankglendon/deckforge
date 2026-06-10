# Methodology / 案头研究方法论

The generalizable method behind the layout — industry- and client-agnostic.
通用、与行业/客户无关的案头研究方法。

## 0. Deliverable quality bar / 交付质量标准

A DeckForge deck should read like a **formal, top-tier strategy-consulting client
deliverable** — official, organised, dense and genuinely informative. Don't ship
thin demos. Concretely:

- **Complete skeleton** — cover → three core questions → contents → executive
  summary → **several sections, each with a divider + mini-TOC and multiple dense
  content pages** → section takeaways → conclusion (answering the opening
  questions) → methodology & sources → appendix/glossary.
- **Substantive length** — a market study is typically **~50-60 pages**, not a
  handful. The bundled EV example (**51 slides**) is the reference standard;
  match or exceed it.
- **Information-rich every page** — an action-title conclusion + a real visual
  (native chart / table / framework) + analysis (body or Facts/Insights/
  Implications) + cited sources. No half-empty pages.
- **Professional & monochrome** — McKinsey-style restraint (see
  [design-system.md](design-system.md)); colour lives in charts and furniture,
  not running text.
- **Clean cover** — title, subtitle, date/meta and the line motif; no gratuitous
  buttons or clutter.

> 交付物 = 正式客户级战略报告：完整骨架、~50-60 页、每页信息充实、专业克制、封面干净。
> 以内置 51 页 EV 示例为基准，对标或超过它。

## 1. The spine: three layers / 脊柱：三层逻辑

Every content page answers, in order:

1. **Facts** — what is objectively happening (size, structure, players, channels).
   事实：市场/品类客观状况。
2. **Insights** — *why* it is happening (the judgement, the causation).
   洞见：趋势与归因。
3. **Implications** — *so what for the reader* (positioning, product, channel,
   go-to-market). 启示：对读者/客户的启发。

On a slide this is the right-hand column (`content_blocks`) or the body text +
takeaway bar (`content`). It is the atomic unit of the whole deck.

## 2. The skeleton / 骨架

```
Cover
└ Three core questions        open with the reader's strategic questions
└ Contents (with a thesis)    a table of contents that carries an argument
└ ── per section ──
     Divider + mini-TOC       what this part covers + its implication
     Content pages            action title + left visual + right body/blocks
     Comparison tables        contrast options/competitors + a takeaway bar
     Section summary          1-2 takeaway pages
└ Conclusion                  answer the opening questions (bookend)
└ Methodology & sources       every number traceable; estimates flagged
└ Appendix                    reference tables
```

Two strong moves: **open with questions and close by answering them**
(bookend), and **end every section with a takeaway** — don't make the reader
summarize for you. 开篇抛问、结尾回扣；每章必给 takeaway。

## 3. Writing principles / 写作原则

- **Action titles carry the full logic (cause → effect → so-what).** The headline
  is the conclusion *with its reasoning*, written as a complete sentence — usually
  **two lines** — not a short phrase. Prefer "Demand keeps climbing as cheaper
  models arrive, but growth is cooling — so the prize shifts to cost-competitiveness
  at volume" over "Demand keeps climbing". A reader should grasp the page's
  cause-and-effect from the title alone; a one-line label looks unfinished.
  标题要写成**完整的因果/so-what 整句（通常两行）**，含「因 → 果 → 启示」，不要只写短语；
  让读者只看标题就懂这页的来龙去脉。
- **Clear, not obscure.** Plain language; spell out acronyms on first use; one
  idea per sentence. 说清楚、去黑话、缩写展开。
- **Not absolute.** Have a point of view, but stay evidence-based and measured —
  avoid "always / never / the only / will definitely"; flag estimates. Desk
  research gives *preliminary* judgements. 有观点但留余地，别把话说死，估算标注。
- **Dense, not sparse.** Match a real consulting report's information density;
  no half-empty pages. 信息量饱满，不留稀疏页。
- **If it's a client deck, never disparage the client.** Reframe any negative
  fact into an industry-neutral or constructive form; keep the firm's data
  honest. 给客户看的 deck 绝不写贬低客户的内容，把负面改写成中立/建设性。

## 4. Pipelines / 管线

**Research data** (`examples/ev_market/research.json` shows the schema):
`topic → facts[{claim, value, source_title, url, year, confidence}]`. Every
number must trace to a real source URL; never invent data; reconcile conflicting
sources and note the basis; prefer recent (last 1-2 years) data.

> **Web-research discipline (don't burn API tokens).** Plan a de-duplicated query
> list first; run **low-concurrency / sequentially** (parallel blasts hit rate
> limits and waste tokens on failed retries); **persist each result to disk as you
> go** so a crash never forces you to "salvage" partial data; keep `max_results`
> small and only deep-fetch the few URLs that matter.
> 先列查询清单、低并发、边查边落盘——别并行猛发触发限流后抢救残数据。

**Images** (`deckforge/images.py`): fetch → validate (min resolution, skip
watermark stock domains) → **perceptual-hash dedup** (no two near-identical
images) → **aspect-fit** placement (no cropped screenshots). Use 3-5 *different*
images per content page; vary the subject so a page isn't repetitive.

**Charts**: always **native** `python-pptx` charts (`deckforge/charts.py`) — never
matplotlib images or screenshots — so the client can edit data and colors.

**Visual QC** (every revision): export to PDF and eyeball it.

```bash
soffice --headless --convert-to pdf --outdir out deck.pptx   # LibreOffice
python -c "import fitz; d=fitz.open('out/deck.pdf'); [d[i].get_pixmap().save(f'out/p{i+1}.png') for i in range(d.page_count)]"
```

Check: no overlaps, no clipped text/images, native charts, ≤1 highlight per
chart, sources present, sufficient density, no client-disparaging content.

## 5. python-pptx pitfalls (battle-tested) / 实测避坑

| Pitfall | Fix |
|---|---|
| CJK renders as tofu boxes | set an explicit `<a:ea>` typeface on every run (done in `text.py`) |
| Pie/doughnut flagged "needs repair" | never set a data-label *position* on pie/doughnut/radar |
| Pie % labels show 0% | use `number_format = "0%"`, not `'0"%"'` |
| Hyperlink stays black | set color + underline explicitly after `hyperlink.address` |
| Chart double title | `chart.has_title = False` (we draw our own caption) |
| Table flagged "needs repair" | write cell borders in schema order `lnL→lnR→lnT→lnB` |
| Single negative bar renders flipped in LibreOffice | avoid lone negative bars; PowerPoint itself is fine |
| Over-aggressive regex corrupts source | never run blanket regex on code; back up before risky edits |

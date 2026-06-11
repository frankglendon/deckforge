# Desk-research workflow: the hypothesis-driven 8 steps

This is the skill's **analysis front-end** — how to *think* before you build. A rendering
library answers "how do I draw the slide"; this answers "which slides, in what order,
proving what." It adapts McKinsey Problem Solving 101/102 (hypothesis-driven, MECE,
dummy-first) to a desk-research deck built with `deckforge`. For the back-end (skeleton,
visual system, pitfalls) it points to `../docs/methodology.md` and `../docs/design-system.md`
rather than repeating them.

Two habits drive everything:
- **Hypothesis-driven** — state a hypothesis, then verify it. If data falsifies it, return
  to STEP 3 and rewrite the storyline; never force a broken one or bend data to fit.
- **Dummy-first** — lay out the entire 50+ page skeleton and MECE-check it *before*
  gathering data, so you never collect numbers that don't assemble into a story. This is
  the single biggest source of rework in desk research.

```
Phase 1 Think     STEP 0 params+kickoff · 1 Is/Isn't · 2 Issue Tree · 3 Hypothesis Tree
Phase 2 Skeleton  STEP 4 argument form + data needs · 5 Dummy Pages (= JSON spec)
Phase 3 Fill->Gen->Refine  STEP 6 fill · 7 generate (deckforge) · 8 iterative QC + capture
```

---

## §1 Phase 1 — Think (Hypotheses Tree)

### STEP 0  Align configurable params + kickoff questions
Pin down what changes per industry/subject before guessing. Subject/competitor set/section
spine/accent colour/glossary. Ask the three kickoff questions once (objective, scope,
deliverable + length) instead of assuming.

### STEP 1  Define the boundary (Is / Isn't)
State what the study is and isn't, so direction can't drift.

```
## Problem definition
### Is
- [the business question, one line]
- [scope: which markets / segments / time window]
- [deliverable: a 50+ page deck, for whom]
### Isn't
- [excluded: we surface facts + implications, we don't make the go/no-go call for them]
- [excluded: no out-of-scope comparisons, no absolute verdicts]
```

The boundary is also the first neutrality gate: the study answers "what is the
market/competition, and what does it imply for the subject" — it does not judge whether the
subject should act or how well it performs.

### STEP 2  Issue Tree (MECE decomposition)
Break the big question into answerable sub-questions, Mutually Exclusive & Collectively
Exhaustive. Get the top 2-3 layers MECE first, then deepen only where needed; stop at a
grain you can verify in one research pass. Common frames:
- **Market size / growth:** `size = users x penetration x paying-rate x ARPU`, then ask
  "how is each moving, and why."
- **Performance:** segment (A/B/C) x time (history / now / forecast) x comparison
  (industry / competitor / region).
- **Cause analysis:** demand side (why want, why pay) / supply side (players, capacity,
  channels, price bands).

> The top 2-3 layers of the Issue Tree *are* the deck's section spine. Collapse them into
> ~5 mutually-exclusive, collectively-exhaustive parts (e.g. Market & momentum / Demand &
> buyers / Competition / Technology & trends / Opportunity & strategy). MECE-checking those
> 5 parts is the hard action here — any gaps? any overlap? Skeleton -> `../docs/methodology.md` §2.

### STEP 3  Hypothesis Tree (state hypotheses = draft action titles)
For each leaf question, **write a hypothesis to be verified**. That hypothesis is the
**draft action title** for that page — one full cause->effect sentence. After you pull data:
hypothesis holds -> keep it, tighten the wording; falsified -> rewrite it, or go back to
STEP 2 and adjust the tree.

- A hypothesis is written like an action title: full cause->effect, clear, unambiguous,
  never absolute (see `../docs/methodology.md` §3).
- Falsification is normal. Don't stuff data to save a hypothesis (that breaks the
  no-fabrication rule); rewrite it. Storyline strength comes from hypotheses surviving
  data, not from polished phrasing.
- A finished Hypothesis Tree is roughly the whole-deck list of "what each page must prove"
  (~40-50 core hypotheses for a 50+ page deck).

---

## §2 Phase 2 — Skeleton (Dummy Pages, before data)

### STEP 4  Pick argument form + list each page's data needs
For each hypothesis, choose the page type that proves it, and list the data/sources it
needs. Page types (see `../docs/design-system.md` §5 for the `Deck` furniture):

| To prove... | Page type | deckforge |
|---|---|---|
| A single trend | Title + one chart | `deck.content()` + `charts.column/line` |
| One-image-one-text / explained comparison | Title + split (visual left, blocks right) | `deck.content_blocks()` |
| Strategic positioning / categorisation | 2x2 map | `frameworks` |
| Multi-dimension competitor comparison | Title + table + takeaway bar | `tables.table()` + `takeaway_bar` |
| Section summary | Insight summary page | `components.insight_*` |

List each page's **data shopping list**: which numbers, which chart, what kind of source.
That list is STEP 6's input.

### STEP 5  Lay out Dummy Pages (= write the JSON spec; re-check MECE)
Lay out the whole 50+ page deck as an **empty skeleton first**: each page gets only
[page type + placeholder title (the hypothesis) + placeholder chart shape + data needs];
numbers stay blank. The artifact is exactly the JSON spec the engine consumes — Dummy Pages
and the final deck are the same spec, before vs after filling values.

Standard skeleton (see `../docs/methodology.md` §2):
```
Cover -> Three core questions -> Contents -> Executive summary
      -> Section(divider + mini-TOC -> dense content pages x N -> section takeaways) x 5
      -> Conclusion(answers the opening questions) -> Methodology -> Appendix
```

**Re-check two hard metrics the moment the skeleton is laid out** (this is the first gate
for 50+ and MECE): (1) page count >= 50; (2) the 5 parts are MECE — exclusive, no overlap;
exhaustive, no gaps. Fix it at the empty-skeleton stage, not after filling data.

Use `deckforge.spec.build_from_spec(...)` or `examples/ev_market/build_deck*.py` as your
spec template — see `build-with-deckforge.md`.

---

## §3 Phase 3 — Fill -> Generate -> Refine

### STEP 6  Fill with sourced data
Work the STEP 4 shopping list page by page; fill values back into the spec.
- **Recent data first**; expand acronyms on first use.
- **No fabrication (multi-source cross-check):** a key number needs >=2 independent sources
  that agree before you use it; if they don't, downgrade the claim or drop it.
- Every page cites real, hyperlinked sources; **citations differ page to page.**
- Filling will falsify some hypotheses — return to STEP 3, rewrite that page's title/type,
  update the spec.

### STEP 7  Generate with deckforge
Drive the engine from the spec — the back-end you don't reinvent (see
`build-with-deckforge.md`):
- Charts/tables are **native, editable** PowerPoint objects (never screenshots); one accent
  highlights the single most important datapoint per chart.
- Images: ample, and **no two images alike on a page** (perceptual-hash dedup + no reuse on
  the same page); ~2+ images per page.
- One `Theme` re-brands the whole deck; Chinese text uses KaiTi. See `../docs/design-system.md`.

### STEP 8  Iterative QC -> neutrality pass -> capture
- **Iterative QC:** render to PDF/PNG, eyeball every page, refine over 5 rounds against the
  6 layout-defect classes — see `quality-qc.md`.
- **Neutrality pass (before delivery):** read the whole deck; rewrite anything that judges
  or exposes the subject's weaknesses into neutral facts + implications.
- **Capture:** fold new pitfalls / page types / glossary terms back into `../docs/` so the
  next project starts higher.

---

## Step-to-doc map (don't reinvent the back-end)

| Step | Here (front-end) | deckforge docs (back-end) |
|---|---|---|
| 0-1 params/boundary | detail | methodology §0 |
| 2 Issue Tree | detail | methodology §2 (skeleton) |
| 3 Hypothesis Tree | detail | methodology §3 (writing) |
| 4-5 argument form / Dummy Pages | detail | design-system §5, build-with-deckforge.md |
| 6 fill | here | methodology §4 (pipelines) |
| 7 generate | pointer | build-with-deckforge.md, design-system.md |
| 8 QC + capture | pointer | quality-qc.md, methodology §5 |

# Iterative QC refinement

The skill's **QC layer** — how to take a deck from first draft to delivery. It
systematises iterative refinement (5 rounds + 6 classes of layout defect) and folds in the
content rules. A first draft is ~85/100; this loop gets it to ~95.

Core idea: **a good deck is refined, not generated in one shot.** Each round renders the
deck, finds defects by eye, and fixes them precisely.

---

## 1. The 5-round loop

```
Round 1  Draft       Build from the spec -> export PDF -> render PNGs -> contact sheet, scan whole deck
Round 2  Identify    Eyeball page by page against a benchmark; locate defects precisely (annotate, don't guess)
Round 3  Fix         Fix each defect against the "6 layout-defect classes"; re-render that page
Round 4  Split       Overloaded pages split into 2-3 (e.g. "Correlation (1/2) + Academic evidence (2/2)")
Round 5  Polish      Unify font sizes / spacing / alignment / accent / sources / footer; scan once more
```

Rendering and eyeballing every page is the hard action: `headless office -> PDF ->
render -> contact sheet`. Eyes first; a per-page word-count script is only an aid to locate
thin pages, not a hard threshold. Always re-render after a fix — don't assume it's fixed.

---

## 2. The 6 layout-defect classes (sweep every page)

1. **Occlusion / overlap** — title over content, chart over text, footer/source covered.
   Root cause: absolute positioning without accounting for real space. Fix: clear the page
   and re-lay top-to-bottom, clean region boundaries, >=0.2in gaps; sources/footer always
   below content, never covered.
2. **Text overflow** — text exceeds or gets clipped; autofit shrinks to tiny. Detect by
   density = chars / (w x h): >70/in^2 danger, 50-70 warn, <50 safe. Fix: bigger box or
   different page type; long sentences -> short; paragraphs -> bullets; cut filler words.
   Note: don't just delete text — density is a virtue here; prefer re-typing the page or
   splitting it; only filler words get cut.
3. **Contrast (dark fill needs white text)** — text/headers/number-badges/insight-block
   titles on dark fills must be white. Check headers, dark insight boxes, number circles.
   Battle scar: a "light" layout with white text makes the text vanish — verify after render.
4. **Chart labels** — missing/overlapping data labels, legend duplicating the axis,
   doughnut labels colliding. Fix: keep each chart readable (axis/legend/labels, pick what
   fits, don't stack); one accent highlights only the single most important datapoint.
5. **Borders / corners** — large text boxes (>3in: title/body/analysis/insight) use square
   rectangles (rigor); small labels (<1.5in) may use rounded. No border by default; only
   table separators, emphasis boxes and insight boxes get a functional 1.5-2pt border.
6. **Proportion** — chart too large/small, uneven whitespace, lopsided split, empty KPI
   cell. Fix: main chart 60-70% of the content area; fixed split ratio; fill KPI cards
   (a battle scar: a 4-card row with 1 empty -> 3 cards + cols=1); keep the same page type
   laid out identically across the deck.

---

## 3. Content QC (as important as layout — sweep every page)

1. **50+ pages and MECE** — page count met; 5 parts exclusive and exhaustive.
2. **Every page dense — no thin/placeholder pages, no shortcuts** — match a consulting
   benchmark; prose pages aim high; chart pages fully write the action title + Facts/
   Insights/Implications (>=2 sentences each). Merge or fill half/empty pages.
3. **Action titles are full cause->effect sentences** — a conclusion; clear, unambiguous,
   never absolute.
4. **Native charts** (not screenshots); **real hyperlinked sources, varied page to page**;
   acronyms expanded on first use; **recent data, cross-checked** across sources.
5. **Ample images, no two alike on a page** (two-layer dedup); ~2+ per page.
6. **Stay neutral and constructive about the subject** — when the deck is for a client,
   surface implications, not judgments; never disparage the subject. Do a neutrality pass
   over the whole deck before delivery.
7. **No emoji** (except README); **no API keys/credentials** in output, scripts or examples.

---

## 4. Two check points

- **At build time:** enforce the rules while writing the spec/build script (white text on
  dark, square large boxes, native charts, full-sentence titles, hyperlinked sources) —
  don't leave defects for after render.
- **After build:** every revision goes through `export PDF -> render -> eyeball` for all 6
  layout classes + the 7 content rules. Fix one, look at one, confirm.

---

## 5. Final pre-delivery checklist (all must pass)

- [ ] >= 50 pages; 5 parts MECE (no gaps, no overlap)
- [ ] Every content page dense; no thin/placeholder pages
- [ ] Every action title a full cause->effect sentence; clear / unambiguous / not absolute
- [ ] No occlusion/overflow; white on dark; readable chart labels; square large boxes /
      no-border default; balanced proportion
- [ ] All charts native & editable; sources real, hyperlinked, varied; acronyms expanded;
      data recent and cross-checked
- [ ] Images ample, no two alike per page (two-layer dedup), ~2+ per page
- [ ] **Neutrality pass done** — nothing judges or exposes the subject's weaknesses
- [ ] No emoji (except README); no API keys/credentials anywhere
- [ ] Learnings captured back into `../docs/` for the next project

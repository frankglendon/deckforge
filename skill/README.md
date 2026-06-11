<div align="center">

# 🧠 DeckForge Desk-Research Skill

**A Claude Skill that turns a business question into a 50+ page, client-grade desk-research
deck — hypothesis-first, MECE, native editable charts.**

[![Skill](https://img.shields.io/badge/Claude-Skill-8A63D2.svg)](https://www.anthropic.com/news/skills)
&nbsp;[![Engine](https://img.shields.io/badge/engine-deckforge-2D6CDF.svg)](../README.md)
&nbsp;[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](../LICENSE)

</div>

---

DeckForge is a strong **rendering back-end** (native PowerPoint charts, one-`Theme`
re-brand, EN/中文). This skill adds the two things a rendering library can't give you on its
own — the **"how to think before building"** front-end and the **"how to refine to 95/100"**
QC layer — and packages the whole pipeline so Claude can run it from one sentence.

It absorbs the proven parts of McKinsey Problem Solving — **hypothesis-driven** (state a
hypothesis, verify it, rebuild the storyline if data falsifies it) and **dummy-first** (lay
out and MECE-check the full 50+ page skeleton *before* gathering data) — and wires them to
the DeckForge engine.

---

## 📂 Structure (Progressive Disclosure)

```
skill/
├── SKILL.md                       # navigation map: triggers + rules + 8-step overview + load pointers
└── references/
    ├── workflow.md                # ⭐ analysis front-end: the hypothesis-driven 8 steps
    ├── quality-qc.md              # ⭐ iterative QC: 5 rounds + 6 layout-defect classes + checklist
    └── build-with-deckforge.md    # drive the engine: JSON spec / Python API / re-brand / QC render
```

`SKILL.md` stays resident; everything in `references/` loads on demand. The back-end
(`../deckforge/`, `../docs/methodology.md`, `../docs/design-system.md`) is reused, not
duplicated.

---

## 🚀 Use it

### Install (so Claude can activate it)

```bash
git clone https://github.com/frankglendon/deckforge
ln -s "$(pwd)/deckforge/skill" ~/.claude/skills/deckforge-desk-research
pip install -r deckforge/requirements.txt
```

### Activate in a conversation

```
Use the desk-research skill to build a deck on the global EV market.
```

Claude follows `SKILL.md`: a 3-line scoping reply -> the 8-step front-end (think, then lay
out a 50+ page empty skeleton) -> fill with sourced data -> generate native-chart slides
with `deckforge` -> iterative QC -> neutrality pass.

---

## 🎯 The 8 steps

```
Phase 1 Think     Is/Isn't boundary -> Issue Tree (MECE) -> Hypothesis Tree (= draft action titles)
Phase 2 Skeleton  argument form + data needs -> Dummy Pages (a 50+ page empty spec); re-check MECE
Phase 3 Fill/Gen  fill sourced data -> generate with deckforge -> iterative QC -> capture learnings
```

---

## 👤 Author

**Xiangyu (Frank) Bai** — market researcher / analyst building AI-assisted tools for real
business problems. This skill is the open, desensitized distillation of a real desk-research
production pipeline.

- **GitHub:** https://github.com/frankglendon
- **Engine:** [DeckForge](../README.md)

---
name: deckforge-desk-research
description: >-
  Consulting-grade desk-research deck system. Take a business question, decompose it
  hypothesis-first (Is/Isn't boundary -> Issue Tree, MECE -> Hypothesis Tree -> Dummy
  Pages: lay out a 50+ page empty skeleton before filling data), then drive the
  `deckforge` python-pptx library to generate a 50+ page, MECE deck of native, editable
  charts in a McKinsey-style visual system, and refine it through iterative QC to a
  client-grade deliverable. Use this skill whenever the user wants a "desk research /
  market scan / competitive landscape / industry report / market-entry / strategy" deck.
license: MIT
metadata:
  version: "1.0"
  author: Frank Bai (frankglendon)
  architecture: Progressive Disclosure (SKILL.md is the map; references load on demand)
  engine: deckforge (python-pptx — native editable charts, one-Theme re-brand, EN/中文)
---

# DeckForge Desk-Research Skill

Packages a full consulting desk-research pipeline into one activatable workflow:
**think hypothesis-first -> lay out a 50+ page empty skeleton -> fill with sourced data
-> generate native-chart slides with the `deckforge` engine -> refine via iterative QC.**

This file is a **navigation map**. It holds only the trigger logic, the non-negotiable
rules, the 8-step overview, and pointers to references that load **on demand** (read them
when you reach that step; don't keep them resident).

---

## 1. Non-negotiable rules (never violate)

1. **50+ pages and MECE.** The deck must be 50+ pages and Mutually Exclusive,
   Collectively Exhaustive — sections cover the whole topic with no gaps or overlap.
   No half-empty or placeholder pages; merge or fill them.
2. **Every page is dense — no thin pages, no shortcuts.** Match a consulting benchmark's
   density. Prose pages aim high (hundreds of words); chart pages fully write the action
   title + Facts/Insights/Implications blocks (>=2 sentences each).
3. **Action titles are full cause->effect sentences** — a conclusion, not a topic.
   Wrong: "Market analysis." Right: "Cheaper models lift volume, but growth is cooling —
   the open question is whether affordability carries volume into the mass market."
   Clear, unambiguous, never absolute.
4. **Native, not faked.** Every chart/table is a real, editable PowerPoint object — never
   a screenshot. Highlight the single most important datapoint per chart with one accent.
5. **Sourced and varied.** Every page cites real, hyperlinked sources; sources differ
   page to page. Cross-check key numbers across independent sources; never fabricate.
6. **Stay neutral and constructive about the subject.** When the deck is for a client,
   surface implications, not judgments — never disparage the subject of the research.
7. **No secrets, no emoji.** Never embed API keys/credentials in output, scripts or
   examples. No emoji anywhere except README files.

---

## 2. First-activation response (stay terse)

When the user activates this skill or says "use the desk-research skill to...", reply in
**3-4 lines**, ask one either/or question, then wait:

```
Desk-research skill is on — from a business question to a 50+ page, client-grade deck
(McKinsey-style visual system, native editable charts).
Want a quick walkthrough of the method, or just tell me the subject / industry / question?
```

Do not list example questions, do not fire 5 clarifying questions, do not auto-start
STEP 1 when the user is only asking. Begin only once they say "start" or give enough info.

---

## 3. The 8-step workflow (think -> skeleton -> fill -> refine)

```
Phase 1  Think  (Hypotheses Tree)        detail -> references/workflow.md  §1
  STEP 0  Align configurable params + kickoff questions
  STEP 1  Define the boundary (Is / Isn't)
  STEP 2  Issue Tree (MECE decomposition)
  STEP 3  Hypothesis Tree (state hypotheses = draft action titles)

Phase 2  Skeleton  (Dummy Pages)         detail -> references/workflow.md  §2
  STEP 4  Pick argument form + list each page's data needs
  STEP 5  Lay out Dummy Pages (a 50+ page empty spec); re-check MECE

Phase 3  Fill -> Generate -> Refine      detail -> references/workflow.md  §3
  STEP 6  Fill with sourced data (recent, multi-source, varied citations)
  STEP 7  Generate with deckforge (native charts / Theme / action titles / image pool)
  STEP 8  Iterative QC refinement -> neutrality pass -> capture learnings
```

Two consulting habits this encodes: **hypothesis-driven** (state a hypothesis, then
verify; if data falsifies it, return to STEP 3 and rebuild the storyline — don't force a
broken one) and **dummy-first** (lay out and MECE-check the whole 50+ page skeleton
*before* gathering data, so you never collect numbers that don't assemble into a story).

---

## 4. On-demand load map (Progressive Disclosure)

| When you are about to... | Read |
|---|---|
| Run the 8-step front-end (hypothesis tree / dummy pages / fill rhythm) | `references/workflow.md` |
| Refine via iterative QC (5 rounds + 6 layout-defect classes + final checklist) | `references/quality-qc.md` |
| Drive the engine (API, JSON spec, page types, web app) | `references/build-with-deckforge.md` |
| Quality bar, three-layer spine, skeleton, writing principles, pitfalls | `../docs/methodology.md` |
| Palette, typography, one-place re-brand, page furniture | `../docs/design-system.md` |
| A complete runnable 51-page sample (EN + 中文) | `../examples/ev_market/build_deck.py`, `build_deck_zh.py` |

---

## 5. What this skill adds (and what it reuses)

- **New here:** the hypothesis-driven *analysis front-end* (`workflow.md`) and the
  *iterative QC* layer (`quality-qc.md`) — the "how to think before building" and "how to
  refine to 95/100" layers that a rendering library alone doesn't give you.
- **Reused:** the `deckforge` engine and its `docs/` (methodology, design system) provide
  the strong back-end — native editable charts, one-`Theme` re-brand, EN/中文 (KaiTi),
  image pool. Don't reinvent them; point to them.

# -*- coding: utf-8 -*-
"""
Build a deck from a plain-JSON spec — so the web app (and anyone) can author a
deck without writing Python.

A spec is a dict:
    {
      "brand": "Acme Research", "footer": "Acme Research", "lang": "en-US",
      "theme": {"primary": "00A9F4"},        # optional hex overrides
      "pages": [ {"type": "...", ...}, ... ]
    }

Page types: cover, questions, agenda, divider, content, content_blocks, table,
prose, conclusion, sources, back_cover. See examples/sample_spec.json.
"""
from .theme import Theme, hex_rgb
from .core import Deck
from . import charts, frameworks, tables

_ZH_LABELS = {"source": "来源：", "part": "第 {n} 部分", "in_this_part": "本部分内容",
              "implication": "启示", "cover_note": "示例 / 示意数据。"}


def _tuples(rows):
    return [tuple(r) for r in rows] if rows else []


def _chart(deck, slide, rect, spec):
    """Draw a chart (and optional caption) into the left rect of a content page."""
    x, y, w, h = rect
    t = deck.theme
    if spec.get("caption"):
        deck.chart_caption(slide, x, y, w, spec["caption"], spec.get("unit", ""))
        y, h = y + 0.55, h - 0.6
    kind = spec.get("kind", "column")
    if kind == "column":
        charts.column(slide, t, x, y, w, h, spec["categories"], spec["series"],
                      highlight=tuple(spec["highlight"]) if spec.get("highlight") else None)
    elif kind == "line":
        charts.line(slide, t, x, y, w, h, spec["categories"], spec["series"])
    elif kind == "bar":
        charts.bar(slide, t, x, y, w, h, spec["categories"], spec["values"],
                   highlight_idx=spec.get("highlight_idx"))
    elif kind == "doughnut":
        charts.doughnut(slide, t, x, y, w - 0.4, h, spec["categories"], spec["values"],
                        highlight_idx=spec.get("highlight_idx"))


def build_from_spec(spec, *, brand=None, footer=None, lang=None, accent=None):
    """Return a saved-ready Deck built from a JSON spec. Keyword overrides win
    over the spec's own values (used by the web form)."""
    brand = brand or spec.get("brand", "Acme Research")
    footer = footer or spec.get("footer", brand)
    lang = lang or spec.get("lang", "en-US")

    theme = Theme(lang=lang)
    for k, v in (spec.get("theme") or {}).items():
        if hasattr(theme, k) and isinstance(v, str):
            setattr(theme, k, hex_rgb(v))
    if accent:
        theme.primary = theme.accent = hex_rgb(accent)

    labels = spec.get("labels")
    if not labels and lang.startswith("zh"):
        labels = _ZH_LABELS
    deck = Deck(theme=theme, brand=brand, footer=footer, labels=labels)

    for pg in spec.get("pages", []):
        t = pg.get("type")
        kicker = pg.get("kicker")
        sources = _tuples(pg.get("sources"))

        if t == "cover":
            deck.cover(pg["title"], subtitle=pg.get("subtitle", ""),
                       meta=pg.get("meta", ""), cta=pg.get("cta"))
        elif t == "questions":
            cards = [(c[0], c[1], c[2], list(c[3])) for c in pg["cards"]]
            deck.core_questions(pg["headline"], pg.get("intro", ""), cards)
        elif t == "agenda":
            deck.agenda(pg["headline"], [tuple(i) for i in pg["items"]])
        elif t == "divider":
            deck.section_divider(pg["part_no"], pg["title"], pg.get("subtitle", ""),
                                 list(pg.get("toc", [])), takeaway=pg.get("takeaway", ""))
        elif t == "content":
            slide, rect = deck.content(pg["title"], _norm_body(pg.get("body", [])),
                                       kicker=kicker, sources=sources, images=False)
            if pg.get("chart"):
                _chart(deck, slide, rect, pg["chart"])
        elif t == "content_blocks":
            slide, rect = deck.content_blocks(pg["title"], _tuples(pg["blocks"]),
                                              kicker=kicker, sources=sources, images=False)
            if pg.get("kpi"):
                frameworks.kpi_grid(slide, deck.theme, *rect, _tuples(pg["kpi"]),
                                    cols=pg.get("cols", 2))
            elif pg.get("chart"):
                _chart(deck, slide, rect, pg["chart"])
        elif t == "table":
            slide, rect = deck.wide_slide(pg["title"], kicker=kicker, sources=sources,
                                          images=False)
            x, y, w, _h = rect
            th = pg.get("table_h", 3.4)
            cw = pg.get("col_widths")
            tables.table(slide, deck.theme, x, y, w, th, pg["rows"], col_widths=cw)
            if pg.get("takeaway"):
                tables.takeaway_bar(slide, deck.theme, x, y + th + 0.2, w, pg["takeaway"],
                                    label=pg.get("takeaway_label", "Implication"))
        elif t == "prose":
            deck.prose(pg["title"], _norm_body(pg.get("paragraphs", [])),
                       kicker=kicker, sources=sources, columns=pg.get("columns", 1))
        elif t == "conclusion":
            deck.conclusion(pg["headline"], list(pg.get("lines", [])), sources)
        elif t == "sources":
            groups = {k: _tuples(v) for k, v in pg["groups"].items()}
            deck.source_list(pg["title"], groups, kicker=kicker)
        elif t == "back_cover":
            deck.back_cover(pg.get("line", "Thank you"), pg.get("sub", ""))
        else:
            raise ValueError(f"unknown page type: {t!r}")
    return deck


def _norm_body(body):
    """Body paragraphs: a string stays a string; a 2-list becomes a (lead, rest) tuple."""
    out = []
    for p in body:
        out.append(tuple(p) if isinstance(p, (list, tuple)) else p)
    return out

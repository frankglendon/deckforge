# -*- coding: utf-8 -*-
"""
DeckForge — programmatic, MBB-grade consulting desk-research decks.

Quick start:
    from deckforge import Deck, Theme
    from deckforge import charts, tables, images

    deck = Deck(brand="Acme Research", footer="Acme Research 2026")
    deck.cover("Global EV Market", "Desk research", "To: Board\\nStrategy team")
    slide, (x, y, w, h) = deck.content_slide(
        "Demand is shifting to 「affordable」 EVs",
        "Sub-headline with a key number",
        blocks=[("Facts", "..."), ("Insights", "..."), ("Implications", "...")],
        sources=[("IEA", "https://www.iea.org")],
    )
    charts.column(slide, deck.theme, x, y, w, h, ["2023", "2024", "2025"],
                  {"Units (m)": [10, 14, 17]}, highlight=(0, 2))
    deck.save("ev_market.pptx")
"""
from .theme import Theme, DEFAULT, hex_rgb
from .core import Deck, IN  # noqa: F401  (wide_slide etc. are Deck methods)
from . import charts, tables, components, images, text, frameworks

__all__ = [
    "Deck", "Theme", "DEFAULT", "hex_rgb", "IN",
    "charts", "tables", "components", "images", "text", "frameworks",
]
__version__ = "0.1.0"

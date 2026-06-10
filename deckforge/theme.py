# -*- coding: utf-8 -*-
"""
Design system for DeckForge — *McKinsey-inspired* (not affiliated; uses generic
substitute fonts, no proprietary assets).

Look & feel:
- **Deep navy** (#051C2C) backgrounds for cover / dividers / conclusion.
- **McKinsey blue** (#2251FF) as the primary accent; a family of blue/cyan
  variants for multi-series charts.
- **Serif headlines** in near-black navy (substitute: Georgia / KaiTi for CJK),
  **sans body** (substitute: Arial / Microsoft YaHei). Swap to Bower / McKinsey
  Sans if you have licenses.
- One **highlight** color (cyan) marks the single most important datapoint.

Everything reads from a `Theme` instance — change it here to re-brand the deck.
"""
from dataclasses import dataclass, field
from typing import List
from pptx.dml.color import RGBColor


def hex_rgb(h: str) -> RGBColor:
    h = h.lstrip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


@dataclass
class Theme:
    # --- brand / accents (calibrated to the GEI report) ---
    primary: RGBColor = field(default_factory=lambda: hex_rgb("00A9F4"))   # bright cyan-blue accent
    accent: RGBColor = field(default_factory=lambda: hex_rgb("00A9F4"))    # the ONE key datapoint
    accent_grad: tuple = ("00A9F4", "041C2C")  # optional 2-stop highlight

    # --- multi-series palette: navy + cyan + variants (GEI charts) ---
    secondary: List[RGBColor] = field(default_factory=lambda: [
        hex_rgb("041C2C"),  # deep navy (primary bar)
        hex_rgb("00A9F4"),  # cyan (second series / highlight)
        hex_rgb("99C7E5"),  # light blue
        hex_rgb("7F8C99"),  # slate grey
        hex_rgb("2251FF"),  # blue
        hex_rgb("C2CBD2"),  # pale grey
    ])

    # --- neutrals (GEI uses black headings on white) ---
    title: RGBColor = field(default_factory=lambda: hex_rgb("000000"))   # black serif heading
    text: RGBColor = field(default_factory=lambda: hex_rgb("1A1A1A"))    # near-black body
    grey: RGBColor = field(default_factory=lambda: hex_rgb("757575"))    # kicker / footnotes
    light_grey: RGBColor = field(default_factory=lambda: hex_rgb("BFC6CC"))  # rules / borders
    white: RGBColor = field(default_factory=lambda: hex_rgb("FFFFFF"))
    dark_bg: RGBColor = field(default_factory=lambda: hex_rgb("041C2C"))  # deep navy (cover/divider)
    rule: RGBColor = field(default_factory=lambda: hex_rgb("9AA3AB"))     # title/footer hairline

    # tints for the optional three insight blocks (Facts / Insights / Implications)
    tint_primary: RGBColor = field(default_factory=lambda: hex_rgb("E7F4FC"))
    tint_cyan: RGBColor = field(default_factory=lambda: hex_rgb("EAF0F3"))
    tint_navy: RGBColor = field(default_factory=lambda: hex_rgb("EDEFF1"))

    # --- typography: GEI = Georgia-Bold serif headings + Arial body;
    #     McKinsey Chinese uses KaiTi (楷体) for BOTH headings and body ---
    font_heading: str = "Georgia"            # serif headline (substitute for Bower)
    font_heading_ea: str = "KaiTi"           # CJK serif headline (楷体)
    font_body: str = "Arial"                 # sans body (substitute for McKinsey Sans)
    font_body_ea: str = "KaiTi"              # CJK body — McKinsey Chinese = 楷体

    # --- locked font sizes (16:9 deck), pt ---
    size_title: int = 20
    size_block_tag: int = 16
    size_body: int = 12
    size_chart_label: int = 12
    size_chart_title: int = 14
    size_toc: int = 12
    size_table_header: int = 11
    size_table_body: int = 10
    size_footnote: int = 8

    lang: str = "en-US"

    # McKinsey keeps running text MONOCHROME (emphasis via bold/serif, not color).
    # Set True for a MBB / dense-emphasis style accent-colored emphasis on key terms/numbers.
    accent_text: bool = False

    def fonts(self, serif=False):
        """Return (latin, ea) typeface pair for heading (serif) or body."""
        if serif:
            return self.font_heading, self.font_heading_ea
        return self.font_body, self.font_body_ea

    def block_themes(self):
        """(accent_color, tint) for Facts / Insights / Implications, in order."""
        return [
            (hex_rgb("041C2C"), self.tint_primary),  # Facts — navy
            (hex_rgb("00A9F4"), self.tint_cyan),     # Insights — cyan
            (hex_rgb("2251FF"), self.tint_navy),     # Implications — blue
        ]


# A ready-to-use default. Build your own and pass it to Deck(theme=...).
DEFAULT = Theme()

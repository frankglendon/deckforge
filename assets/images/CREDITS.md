# Image credits

All photos in this folder are used in the EV example deck and are sourced from
**Unsplash** and **Pexels** under their respective free licenses, which permit
free commercial use and redistribution as part of a project (you may not sell the
unaltered photos themselves or use them to build a competing stock service).

| File | Subject | Source | Photo |
|---|---|---|---|
| `cover_ev.jpg` | Modern electric car | Unsplash | photo-1742259703546 |
| `div_market.jpg` | EV charging station | Unsplash | photo-1755555707531 |
| `div_demand.jpg` | Electric SUV (KIA EV5) | Pexels | photos/18886584 |
| `div_competition.jpg` | Automotive factory robots | Unsplash | photo-1567789884554 |
| `div_technology.jpg` | Car cockpit touchscreen | Unsplash | photo-1704932500676 |
| `div_opportunity.jpg` | Electric SUV (Seoul) | Pexels | photos/34600639 |
| `sum_market.jpg` | Electric car | Unsplash | photo-1777351396104 |
| `sum_demand.jpg` | Electric car (showroom) | Unsplash | photo-1743264533227 |
| `sum_competition.jpg` | Car interior (Tesla) | Unsplash | photo-1722611127433 |
| `sum_technology.jpg` | Car dashboard | Pexels | photos/34193462 |

### Photo pool (`pool/`)

`pool/` holds ~40 additional EV-related thumbnails (electric cars, charging,
city traffic, renewable energy) from **Unsplash** and **Pexels**, cropped to a
common ~2.4:1 ratio and de-duplicated (perceptual hash). The deck draws 3 photos
per content page and 4 per table page from this pool automatically, giving an
overall density of roughly **2.2 photos / 2.65 visual elements per page**. Swap
the folder contents to re-theme; the build cycles through whatever is present.

Notes:
- Images are cropped to fixed aspect ratios for the cover, dividers, summary and
  content pages. The originals are higher resolution.
- They are **illustrative** for a public demo. For your own deck, swap in your
  own licensed imagery (drop files into `assets/images/` and reference them from
  the build script). Attribution is not strictly required by Unsplash/Pexels but
  is provided here as good practice.
- Unsplash License: https://unsplash.com/license  ·  Pexels License: https://www.pexels.com/license/

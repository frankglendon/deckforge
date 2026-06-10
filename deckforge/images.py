# -*- coding: utf-8 -*-
"""
Image pipeline: download -> validate (min resolution, block watermark stock
domains) -> perceptual-hash dedup (so no two near-identical images across the
deck) -> aspect-fit placement (no cropped screenshots).

Feed it candidate URLs from any image search (e.g. a web-search API). Keep a
diverse pool and place 3-5 *different* images per content page.
"""
import io
from PIL import Image, ImageOps

try:
    import requests
except ImportError:  # placement-only usage doesn't need requests
    requests = None

EMU_IN = 914400

# Stock/watermark domains to skip (low-quality or licensing risk).
BLOCK_DOMAINS = (
    "shutterstock", "istockphoto", "istock", "dreamstime", "alamy",
    "gettyimages", "123rf", "depositphotos", "vectorstock",
)

_HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                          "AppleWebKit/537.36"}


def _dhash(img, hs=8):
    g = img.convert("L").resize((hs + 1, hs), Image.Resampling.LANCZOS)
    px = list(g.getdata())
    bits, idx = 0, 0
    for row in range(hs):
        for col in range(hs):
            left = px[row * (hs + 1) + col]
            right = px[row * (hs + 1) + col + 1]
            bits |= (1 << idx) if left > right else 0
            idx += 1
    return bits


def _hamming(a, b):
    return bin(a ^ b).count("1")


class ImagePool:
    """Download + validate + dedup. Tracks hashes so duplicates are rejected."""

    def __init__(self, min_w=680, min_h=480, dup_thresh=6):
        self.min_w, self.min_h, self.dup_thresh = min_w, min_h, dup_thresh
        self._hashes = []

    def fetch(self, url, dest_path, *, timeout=15):
        """Return dest_path if downloaded & unique & big enough, else None."""
        if any(d in url.lower() for d in BLOCK_DOMAINS):
            return None
        if requests is None:
            raise RuntimeError("requests is required to fetch images")
        try:
            r = requests.get(url, timeout=timeout, headers=_HEADERS)
            r.raise_for_status()
            img = Image.open(io.BytesIO(r.content))
            img.load()
            img = img.convert("RGB")
        except Exception:
            return None
        if img.width < self.min_w or img.height < self.min_h:
            return None
        h = _dhash(img)
        if any(_hamming(h, s) <= self.dup_thresh for s in self._hashes):
            return None
        self._hashes.append(h)
        img.save(dest_path, "JPEG", quality=88)
        return dest_path


def place(slide, image_path, x, y, w, h, *, mode="fit"):
    """Place an image in a box (inches). mode='fit' (no crop) | 'fill' (cover)."""
    if mode == "fill":
        img = Image.open(image_path)
        target = (int(w * 200), int(h * 200))
        ImageOps.fit(img, target, Image.Resampling.LANCZOS).save(image_path, quality=88)
        return slide.shapes.add_picture(image_path, int(x * EMU_IN), int(y * EMU_IN),
                                        int(w * EMU_IN), int(h * EMU_IN))
    # fit: preserve aspect, center within box
    img = Image.open(image_path)
    ar = img.width / img.height
    box_ar = w / h
    if ar > box_ar:
        nw, nh = w, w / ar
    else:
        nh, nw = h, h * ar
    nx, ny = x + (w - nw) / 2, y + (h - nh) / 2
    return slide.shapes.add_picture(image_path, int(nx * EMU_IN), int(ny * EMU_IN),
                                    int(nw * EMU_IN), int(nh * EMU_IN))

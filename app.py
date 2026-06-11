# -*- coding: utf-8 -*-
"""
DeckForge Studio — web app (Flask). / DeckForge Studio 网页应用（Flask）。

Run it directly / 直接运行:
    python app.py                 # then open http://127.0.0.1:5000
    python app.py --port 8000

Fill in branding + a JSON content spec in the browser and download a native,
editable .pptx. Per-build state is kept in an in-memory dict — fine for local,
single-user use (this is a demo / portfolio tool, not a multi-tenant service).
在浏览器里填品牌 + JSON 内容规格，下载原生可编辑 .pptx。每次构建的状态存内存字典，
本地单用户够用。
"""
import argparse
import json
import os
import uuid

from flask import (Flask, abort, redirect, render_template, request,
                   send_file, send_from_directory, url_for)

from deckforge.spec import build_from_spec

BASE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE, "outputs")
SHOTS_DIR = os.path.join(BASE, "assets", "screenshots")
SAMPLE = os.path.join(BASE, "examples", "sample_spec.json")
os.makedirs(OUTPUT_DIR, exist_ok=True)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 4 * 1024 * 1024  # 4 MB form cap
DECKS = {}  # token -> {"path", "name", "pages"} / 每次构建的产物


def _sample_text():
    return open(SAMPLE, encoding="utf-8").read()


@app.route("/")
def index():
    return render_template("index.html", spec=_sample_text(), error=None, form={})


@app.route("/generate", methods=["POST"])
def generate():
    brand = (request.form.get("brand") or "").strip() or None
    footer = (request.form.get("footer") or "").strip() or None
    lang = request.form.get("lang") or "en-US"
    accent = (request.form.get("accent") or "").lstrip("#").strip() or None
    spec_text = request.form.get("spec") or ""
    try:
        spec = json.loads(spec_text)
        deck = build_from_spec(spec, brand=brand, footer=footer, lang=lang, accent=accent)
    except json.JSONDecodeError as e:
        return render_template("index.html", spec=spec_text, form=request.form,
                               error=f"Invalid JSON (line {e.lineno}): {e.msg}"), 400
    except Exception as e:  # build error (bad page type, missing field, ...)
        return render_template("index.html", spec=spec_text, form=request.form,
                               error=f"{type(e).__name__}: {e}"), 400

    token = uuid.uuid4().hex[:12]
    base_name = (brand or spec.get("brand") or "deck").strip().replace(" ", "_")
    path = os.path.join(OUTPUT_DIR, token + ".pptx")
    deck.save(path)
    DECKS[token] = {"path": path, "name": f"{base_name}.pptx", "pages": deck.page}
    return redirect(url_for("result", token=token))


@app.route("/result/<token>")
def result(token):
    d = DECKS.get(token)
    if not d:
        abort(404)
    return render_template("result.html", token=token, pages=d["pages"], name=d["name"])


@app.route("/download/<token>")
def download(token):
    d = DECKS.get(token)
    if not d or not os.path.exists(d["path"]):
        abort(404)
    return send_file(d["path"], as_attachment=True, download_name=d["name"])


@app.route("/sample.json")
def sample():
    return send_file(SAMPLE, as_attachment=True, download_name="deckforge_sample_spec.json")


@app.route("/shot/<path:name>")
def shot(name):
    return send_from_directory(SHOTS_DIR, name)


def main():
    ap = argparse.ArgumentParser(description="DeckForge Studio web app")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=5000)
    args = ap.parse_args()
    print(f"DeckForge Studio  ->  http://{args.host}:{args.port}")
    app.run(host=args.host, port=args.port, debug=False)


if __name__ == "__main__":
    main()

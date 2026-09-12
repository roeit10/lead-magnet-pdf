#!/usr/bin/env python3
"""content.json + theme.json -> guide.html (4 pages A4). The template is the design; this only fills it.

Usage: python3 build_guide.py <content.json> <theme.json> <out.html>
"""
import html, json, re, sys
from pathlib import Path

TPL = Path(__file__).resolve().parents[1] / "templates" / "guide-template.html"
DEFAULT_THEME = {
    "brand": "העסק שלך", "primary": "#2F5FA8", "accent": "#E8EEF8", "bg": "#F6F4EF", "ink": "#1C1B18", "muted": "#6B675E",
    "font": "'Heebo', system-ui, sans-serif", "font_head": "'Heebo', system-ui, sans-serif",
    "font_query": "Heebo:wght@400;500;700;900", "radius": "12px", "border": "2px solid #1C1B18",
    "shadow": "0 2px 0 #1C1B18", "tilt": "0deg", "bg_pattern": "",
}

def esc(s): return html.escape(str(s or ""))
def mark(s):
    # [חסר: ...] stays visible and yellow inside the text
    return re.sub(r"\[חסר:([^\]]*)\]", r'<mark class="missing">[חסר:\1]</mark>', esc(s))
def paras(text): return "".join(f"<p>{mark(p.strip())}</p>" for p in str(text).split("\n\n") if p.strip())
def hl(title, w1, w2):
    t = esc(title)
    if w1: t = t.replace(esc(w1), f'<span class="hl">{esc(w1)}</span>', 1)
    if w2: t = t.replace(esc(w2), f'<span class="hl-2">{esc(w2)}</span>', 1)
    return t

def main():
    c = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    th = dict(DEFAULT_THEME); th.update(json.loads(Path(sys.argv[2]).read_text(encoding="utf-8")))
    s = TPL.read_text(encoding="utf-8")
    secs = c["sections"]; s2 = secs[1]; s5 = secs[4]; cta = c["cta"]
    fill = {
        **{k: th[k] for k in DEFAULT_THEME},
        "title": esc(c["title"]),
        "title_html": hl(c["title"], c.get("hl_word_1"), c.get("hl_word_2")),
        "tag": esc(c.get("tag", "")), "lead": mark(c.get("lead", "")), "site": esc(c.get("site", "")),
        "learn_items": "".join(f"<li>{mark(i)}</li>" for i in c.get("learn", [])),
        "s1_title": esc(secs[0]["title"]), "s1_body": paras(secs[0]["body"]),
        "s2_title": esc(s2["title"]), "s2_body": paras(s2["body"]),
        "s2_steps": "".join(f'<li><span class="n">{i+1}</span><span>{mark(x)}</span></li>' for i, x in enumerate(s2.get("steps", []))),
        "s2_metrics": "".join(f"<div class=\"metric\"><b>{esc(m['value'])}</b><span>{mark(m['label'])}</span></div>" for m in s2.get("metrics", [])),
        "s3_title": esc(secs[2]["title"]), "s3_body": paras(secs[2]["body"]),
        "s4_title": esc(secs[3]["title"]), "s4_body": paras(secs[3]["body"]),
        "s5_title": esc(s5["title"]), "s5_items": "".join(f"<li>{mark(i)}</li>" for i in s5.get("items", [])),
        "insight": mark(c.get("insight", "")),
        "cta_url": esc(cta.get("button_url") or "#"), "site_url": esc(("https://" + c["site"]) if c.get("site") and not str(c["site"]).startswith("http") else c.get("site","#")),
        "cta_title": esc(cta["title"]), "cta_text": mark(cta.get("text", "")), "cta_button": esc(cta.get("button", "")),
        "cta_meta": "".join(f'<span dir="ltr">{esc(x)}</span>' if re.match(r"^[\w@.+:/ -]+$", x) else f"<span>{esc(x)}</span>" for x in cta.get("meta", [])),
    }
    for k, v in fill.items(): s = s.replace("{{" + k + "}}", v)
    left = re.findall(r"\{\{\w+\}\}", s)
    Path(sys.argv[3]).write_text(s, encoding="utf-8")
    words = len(re.sub(r"<[^>]+>", " ", s[s.index("<body>"):]).split())
    print(f"OK {sys.argv[3]} · {words} מילים" + (f" · לא מולאו: {left}" if left else ""))

if __name__ == "__main__": main()

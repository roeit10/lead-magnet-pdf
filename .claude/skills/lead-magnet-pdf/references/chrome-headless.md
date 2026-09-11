# Rendering A4 PDFs with Chrome headless

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --no-pdf-header-footer \
  --hide-scrollbars \
  --virtual-time-budget=10000 \
  --print-to-pdf=guide.pdf \
  "file://$(pwd)/guide.html"
```

## Why each flag

| Flag | Why |
|---|---|
| `--headless` | run without a window |
| `--disable-gpu` | required on macOS for headless |
| `--no-pdf-header-footer` | strip Chrome's page URL / date headers |
| `--hide-scrollbars` | prevent scrollbar artifacts on rendered pages |
| `--virtual-time-budget=10000` | give Chrome 10s to fetch external assets (fonts, etc.) before rendering. Skip this and Google Fonts won't load. |
| `--print-to-pdf=PATH` | output target |
| `file://...` | always use absolute file URL, not relative path |

## CSS prerequisites

```css
@page { size: A4; margin: 0 }

.page {
  width: 210mm;
  height: 297mm;
  padding: 18mm 16mm 16mm;
  page-break-after: always;
  overflow: hidden;
  position: relative;
}
.page:last-child { page-break-after: auto }
```

Each visible page must be a `.page` div with `page-break-after: always`. A4 is 210×297mm. Use mm units, not px, so the print engine resolves at exact size.

## Common rendering bugs

| Symptom | Cause | Fix |
|---|---|---|
| Page numbers like "04 / 01" instead of "01 / 04" | RTL flips the visual order | `direction: ltr; unicode-bidi: isolate;` on the page-no element |
| Fonts render as fallback (Times/Arial) | Chrome rendered before Google Fonts loaded | Add `--virtual-time-budget=10000` |
| Text bleeds past page bottom | Content overflowing the 297mm page height | Reduce paragraphs or split sections; use `.page { overflow: hidden }` to at least clip cleanly |
| Email + phone running together with no spaces | RTL bidi reorders punctuation against neutral chars | Use `display: flex; gap:`, wrap email/phone in `<span dir="ltr">` |
| Background pattern missing in PDF | Chrome strips it without `--no-pdf-header-footer` AND `print-color-adjust: exact` on body | Set `body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }` |
| `→` appears on wrong side of Hebrew CTA | Logical order is fine; Hebrew reads right-to-left so `→` looks like "back" | Use `←` for "forward" in Hebrew, or remove the arrow |

## Verification

After rendering, always read the PDF back (Read tool with `pages: "1-4"`) before declaring done. Visual inspection catches RTL issues that the code looks fine for.

# העיצוב - התבנית

`templates/guide-template.html` - ארבעה עמודי A4 (`@page { size: A4; margin: 0 }`), RTL, נייטרלי כברירת מחדל.
**לא מעצבים מחדש.** משנים ערכי `--` בלבד, דרך `theme.json`.

| עמוד | מה יש בו |
|---|---|
| 01 | סרט עליון (לוגו-טקסט + מספר עמוד) · תג · כותרת עם הדגשות · lead · קופסת "מה תקבלו" · סעיף 01 |
| 02 | סעיף 02 + כרטיס צעדים ממוספרים + שורת מספרים |
| 03 | סעיפים 03 + 04 |
| 04 | סעיף 05 כרשימת בדיקה · קופסת התובנה · כרטיס CTA עם פרטי קשר |

## מה `theme.json` שולט בו

| מפתח | מה | דוגמה (רועי AI) |
|---|---|---|
| `brand` | הטקסט בלוגו ובפוטר | `רועי AI` |
| `primary` / `accent` | הדגשה ראשית (רקע צבעוני, טקסט לבן) / משנית (רקע בהיר) | `#6D28D9` / `#BEF264` |
| `bg` / `ink` / `muted` | רקע העמוד / טקסט / טקסט משני | `#FAFAF5` / `#0A0A0A` / `#555` |
| `font` / `font_head` / `font_query` | גוף / כותרות / מחרוזת Google Fonts | `'Heebo'…` / `'Rubik'…` / `Heebo:wght@400;700&family=Rubik:wght@900` |
| `radius` / `border` / `shadow` / `tilt` | פינות / מסגרת / צל / הטיית התגים | `0` / `4px solid #0A0A0A` / `8px 8px 0 #0A0A0A` / `-2deg` |
| `bg_pattern` | CSS של דוגמת רקע, או ריק | `background-image:radial-gradient(...)` |

**קריאות לפני נאמנות.** מיתוג עם ניגודיות נמוכה → `ink` נשאר כהה. זה מדריך שקוראים.

## הבנייה

```bash
python3 .claude/skills/lead-magnet-pdf/scripts/build_guide.py outputs/<name>/content.json outputs/<name>/theme.json outputs/<name>/guide.html
.claude/skills/lead-magnet-pdf/scripts/render_pdf.sh outputs/<name>/guide.html            # → guide.pdf
python3 .claude/skills/lead-magnet-pdf/scripts/make_editable.py outputs/<name>/guide.html outputs/<name>/guide.editable.html
```

`build_guide.py` מדפיס כמה מילים יצאו ואם נשאר placeholder לא ממולא.

## בדיקה אחרי הרינדור (חובה - פותחים את ה-PDF)

- אין גלישה מעבר לפוטר באף עמוד. גלש → מקצרים את הסעיף, לא מקטינים פונט.
- מספרי עמודים `01 / 04` ולא `04 / 01` (התבנית כבר מטפלת: `direction:ltr` על האלמנט).
- טלפון ואתר ב-CTA ובפוטר לא התהפכו (`dir="ltr"` - כבר בתבנית).
- ה-`[חסר]` הצהובים - ברשימה בדוח הסיום, לא נבלעים.
- הפונט נטען (Chrome עם `--virtual-time-budget`). כותרת ב-Times New Roman = לא נטען, להריץ שוב.

## הגרסה הניתנת לעריכה

`guide.editable.html` - אותו מדריך, כל טקסט ניתן לעריכה בדפדפן, אוטוסייב, וכפתור "הפק PDF"
שמדפיס עם הצבעים. **זה מה ששולחים למשתמש** - הוא מתקן מילה ומפיק PDF חדש בלי לחזור לקלוד.

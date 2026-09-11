---
name: lead-magnet-pdf
description: Build a 4-page A4 PDF lead magnet (a short practical guide) for a business - interviews for the one problem the guide solves, writes every Hebrew string into one content.json first, gets the text approved, then renders a branded PDF through Chrome plus an editable HTML version with a PDF-export button. Brand comes from the digital office (STYLE-GUIDE / brand.config / globals.css), voice from context/voice.md. Use when the user asks for a lead magnet, a PDF guide, a downloadable guide, or says "תבנה לי מגנט לידים", "מדריך PDF", "מדריך להורדה", "ליד מגנט", "build me a lead magnet", "pdf guide". Not for slide decks, long ebooks, or landing pages (use sales-page for the page).
---

# מגנט לידים - מדריך PDF של ארבעה עמודים

בונה **מדריך אחד קצר** שפותר לקורא בעיה אחת, במיתוג של העסק, ובסופו הזמנה אחת.
זה מה שנותנים בתמורה למספר טלפון או מייל.

**תוכן קודם, רינדור אחרון.** כל מילה נכתבת ל-`content.json`, מאושרת, ורק אז מרנדרים.
תיקון בטקסט חינם; תיקון אחרי הרינדור = רינדור מחדש.

---

## הכללים שלא נשברים

1. **לא ממציאים מספרים.** סטטיסטיקה בלי מקור לא נכנסת. מספר על העסק שאין בקונטקסט →
   `[חסר: מספר]` בצהוב, במקום שבו הוא יושב. **"80% מהעסקים" לא נכתב.**
2. **לא מבטיחים.** "תחסכו 10 שעות" רק אם זה נמדד בעסק הזה. אחרת - מתארים מה קורה.
3. **בעיה אחת, מדריך אחד.** "הכל על AI לעסק" זה לא מגנט, זה ספר. השאלה הראשונה באשף
   היא "איזו בעיה אחת".
4. **מוכרים רק בעמוד 4.** עמודים 1-3 נותנים. ה-CTA אחד, עם יעד אחד.
5. **הקול מהפרופיל, המראה מהמיתוג.** קיים `voice.md` → לפיו. קיים `STYLE-GUIDE` → לפיו.
   אין → ברירת מחדל, **ואומרים**.
6. **תחומים רגישים** (רפואי, פיננסי, משפטי) → `⚠️ טעון בדיקה` בדוח, לפני מסירה.
7. **דו-מגדרי**, בלי מקפים ארוכים, בלי "מהפכה" ובלי "קסם".
8. **פותחים את ה-PDF לפני שמוסרים.** גלישה, כיווניות, פונט. ראה `references/design.md`.

---

## איפה זה חי - המשרד הדיגיטלי

| מה | איפה |
|---|---|
| קונטקסט, קול, מיתוג | `context/business.md` · `context/voice.md` · `STYLE-GUIDE.md` / `globals.css` |
| התוצר | `outputs/<תאריך>-<נושא>-מדריך/` → `content.json` · `theme.json` · `guide.html` · `guide.pdf` · `guide.editable.html` |

**כלל 4 של המשרד: לפני שדורסים - שואלים.**

---

## שלב 0 - מוכנות

| מה | איך | אם חסר |
|---|---|---|
| קונטקסט עסקי | `context/business.md` | `references/setup.md`. **בלי זה לא רצים** |
| Chrome | `render_pdf.sh` מוצא לבד | "להתקין Google Chrome". בלי זה יש HTML, אין PDF |
| קול / מיתוג | `voice.md` / `STYLE-GUIDE.md` | ברירת מחדל, ואומרים |

## שלב 1 - האשף (`references/setup.md`)

שואבים, מציגים, מאשרים. שלוש שאלות: **איזו בעיה אחת** · למי · לאן ה-CTA מוביל.

## שלב 2 - התוכן (`references/content.md`)

כותבים `content.json`: כותרת, lead, "מה תקבלו", 5 סעיפים (בעיה · שיטה עם צעדים ומספרים ·
פירוט · מה עושים · רשימת בדיקה), תובנה, CTA. 500-700 מילים.
**מציגים את הטקסט כמסמך קריא ומבקשים תיקונים.** לא מרנדרים לפני "אושר".

## שלב 3 - הבנייה (`references/design.md`)

`theme.json` מהמיתוג → `build_guide.py` → `render_pdf.sh` → `make_editable.py`.
פותחים את ה-PDF. בודקים את ארבעת העמודים.

## שלב 4 - מסירה

מוסרים **שלושה קבצים**: `guide.pdf` (לשליחה), `guide.editable.html` (לתיקונים עצמאיים),
`content.json` (המקור - לרינדור מחדש בעוד חצי שנה). ומה שנשאר למשתמש: להשלים את ה-`[חסר]`
ולהחליט איך המדריך מגיע לאנשים - דף מכירה (`sales-page`), הודעת וואטסאפ, או מייל.

---

## דוח סיום בטרמינל

```
מגנט לידים · חמש משימות שאתם עושים ביד · בקול שלך (voice.md) · מיתוג: STYLE-GUIDE.md

4 עמודים · 544 מילים · 5 סעיפים · 6 שורות ברשימת הבדיקה
⚠️ [חסר: מספר] בשורת המספרים, עמוד 2 - תשלים ב-content.json או ב-editable, או שנוריד

📄 outputs/2026-10-XX-משימות-ביד-מדריך/guide.pdf  (268KB)
✏️ outputs/2026-10-XX-משימות-ביד-מדריך/guide.editable.html
🧾 outputs/2026-10-XX-משימות-ביד-מדריך/content.json

מה עכשיו: תפתח את ה-PDF, תקרא כמו לקוח, ותגיד לי איזה משפט לא שלך. ואז - איפה הוא יחיה? דף מכירה או הודעה.
```

**לא מסיימים ב"בהצלחה".**

---

## גבולות תפקיד

מדריך אחד של ארבעה עמודים. לא ספר, לא מצגת, לא דף נחיתה (זה `sales-page`), לא מערכת
דיוור. לא אוסף מיילים - הוא נותן את מה שמקבלים בתמורה.

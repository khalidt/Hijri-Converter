# Hijri ⇄ Gregorian Date Converter

<p align="center">
  <a href="#العربية">🇸🇦 العربية</a>
</p>



A small, dependency-free Python tool that converts dates between the
**Islamic (Hijri) calendar** and the **Gregorian calendar**, in both directions.


---

## What it does

The Hijri calendar (marked **AH**, *Anno Hegirae*) is a lunar calendar used across
the Muslim world. The Gregorian calendar is the civil calendar used in most of the
world today. Because the two count time differently, converting a date from one to
the other takes a bit of arithmetic.

This tool does that arithmetic for you:

- **Hijri → Gregorian**, e.g. find out what `30/10/1400 AH` is in the common calendar.
- **Gregorian → Hijri**, e.g. find out today's Hijri date.

It also tells you the **day of the week** for the date.

---

## How it works

Rather than converting directly, the tool uses a neutral "day counter" in the middle
called the **Julian Day Number (JDN)**, simply the number of days that have passed
since a fixed reference point far in the past. Every calendar can be translated to and
from this single number, so the conversion always goes:

```
Hijri  ⇄  Julian Day Number  ⇄  Gregorian
```

This keeps the math reliable and means both directions use the same underlying logic.

---

## Requirements

- **Python 3** (any recent version).
- Nothing else, no libraries to install.

To check if you have Python, open a terminal and run:

```bash
python3 --version
```

---

## How to use it

### Option 1: Interactive

Run the script and answer the two prompts:

```bash
python3 hijri_converter.py
```

Example session:

```
Hijri <-> Gregorian converter (tabular Islamic calendar)
--------------------------------------------------------
  1) Hijri (AH)   -> Gregorian
  2) Gregorian    -> Hijri (AH)
Choose 1 or 2: 1
Enter date as DD/MM/YYYY: 30/10/1400

30/10/1400 AH  =  Thursday, 11/09/1980 (Gregorian)
```

Dates are entered as **DD/MM/YYYY** (day / month / year). You can also use dashes
(`30-10-1400`).

### Option 2: Use it in your own Python code

You can import the functions and call them directly:

```python
from hijri_converter import hijri_to_gregorian, gregorian_to_hijri

# Hijri -> Gregorian
print(hijri_to_gregorian(1400, 10, 30))
# (1980, 9, 11, 'Thursday')   ->  year, month, day, weekday

# Gregorian -> Hijri
print(gregorian_to_hijri(1980, 9, 11))
# (1400, 11, 1, 'Thursday')
```

---

## Functions available

| Function | Converts | Returns |
|----------|----------|---------|
| `hijri_to_gregorian(y, m, d)` | Hijri date → Gregorian | `(year, month, day, weekday)` |
| `gregorian_to_hijri(y, m, d)` | Gregorian date → Hijri | `(year, month, day, weekday)` |
| `hijri_to_jdn(y, m, d)` | Hijri date → Julian Day Number | a number |
| `jdn_to_hijri(jdn)` | Julian Day Number → Hijri | `(year, month, day)` |
| `gregorian_to_jdn(y, m, d)` | Gregorian date → Julian Day Number | a number |
| `jdn_to_gregorian(jdn)` | Julian Day Number → Gregorian | `(year, month, day)` |

In every function the arguments are in the order **year, month, day**.

---

## Important note on accuracy

This tool uses the **tabular (arithmetic) Islamic calendar**, a fixed mathematical
rule for where months begin. It is consistent, reversible, and ideal for software.

However, some countries determine the start of each Hijri month by **moon sighting**
or by official almanacs such as Saudi Arabia's **Umm al-Qura** calendar. Because those
methods are observation-based rather than purely mathematical, a converted date may
differ from this tool's result by **±1 day**.

For everyday use the results are accurate. For legal, religious, or official purposes,
always check against the relevant local or official calendar.

**A note on month lengths:** Hijri months alternate between 30 and 29 days (months
1, 3, 5, 7, 9, 11 have 30 days; months 2, 4, 6, 8, 10, 12 have 29, with month 12
gaining a day in leap years). If you enter a day that exceeds a month's length 
for example day 30 of a 29-day month, the tool still produces a valid Gregorian
result, but it rolls over into the next day. That is why converting `30/10/1400 AH`
forward gives 11 September 1980, while converting that Gregorian date back returns
the canonical `01/11/1400 AH`.

---

## License

<p align="center">
  <a href="https://github.com/khalidt/Hijri-Converter">Hijri-Converter</a>
  © 2026 by
  <a href="https://github.com/khalidt/">Khalid Alkhaldi</a>
  is licensed under
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a>

  <img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" height="18" alt="CC">
  <img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" height="18" alt="BY">
  <img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" height="18" alt="NC">
  <img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" height="18" alt="SA">
</p>


---


<div dir="rtl" lang="ar">

# العربية

## محوّل التواريخ بين الهجري والميلادي
 
أداة بايثون صغيرة لا تحتاج إلى أي مكتبات خارجية، تحوّل التواريخ بين
**التقويم الهجري** و**التقويم الميلادي** .
 
---
 
## ماذا تفعل الأداة
 
التقويم الهجري (ويُرمز له بـ **AH**، أي *بعد الهجرة*) تقويم قمري مُستخدَم في
أنحاء العالم الإسلامي. أمّا التقويم الميلادي فهو التقويم المدني المُستخدَم في معظم
دول العالم اليوم. ولأن كلًّا منهما يحسب الزمن بطريقة مختلفة، فإن تحويل تاريخ من
أحدهما إلى الآخر يتطلّب بعض الحسابات.
 
تقوم هذه الأداة بهذه الحسابات نيابةً عنك:
 
- **من الهجري إلى الميلادي**، مثل معرفة ما يقابل `30/10/1400 هـ` في التقويم الميلادي.
- **من الميلادي إلى الهجري**، مثل معرفة تاريخ اليوم بالهجري.
كما تُخبرك أيضًا بـ**يوم الأسبوع** الموافق للتاريخ.
 
---
 
## كيف تعمل
 
بدلًا من التحويل المباشر، تستخدم الأداة "عدّاد أيام" محايدًا في المنتصف يُسمّى
**رقم اليوم اليولياني (JDN)**، وهو ببساطة عدد الأيام التي مرّت منذ نقطة مرجعية
ثابتة في الماضي. يمكن تحويل أي تقويم من هذا الرقم وإليه، لذا يسير
التحويل دائمًا على هذا النحو:
 
```
Hijri  ⇄  Julian Day Number  ⇄  Gregorian
```
 
وهذا يجعل الحساب موثوقًا، ويعني أن كلا الاتجاهين يستخدمان المنطق نفسه.
 
---
 
## المتطلّبات
 
- **بايثون 3** (أي إصدار حديث).
- لا شيء غير ذلك، ولا حاجة لتثبيت أي مكتبات.
للتحقّق من وجود بايثون لديك، افتح الطرفية (Terminal) ونفّذ:
 
```bash
python3 --version
```
 
---
 
## طريقة الاستخدام
 
### الخيار الأول: التفاعلي (الأسهل)
 
شغّل البرنامج وأجب عن السؤالين:
 
```bash
python3 hijri_converter.py
```
 
مثال على الاستخدام بعد تنفيذ الاامر السابق:
 
```
Hijri <-> Gregorian converter (tabular Islamic calendar)
--------------------------------------------------------
  1) Hijri (AH)   -> Gregorian
  2) Gregorian    -> Hijri (AH)
Choose 1 or 2: 1
Enter date as DD/MM/YYYY: 30/10/1400
 
30/10/1400 AH  =  Thursday, 11/09/1980 (Gregorian)
```
 
تُدخَل التواريخ بصيغة **DD/MM/YYYY** (اليوم / الشهر / السنة). ويمكنك أيضًا استخدام
الشرطات (`30-10-1400`).
 
### الخيار الثاني: استخدامها داخل شيفرة بايثون خاصة بك
 
يمكنك استيراد الدوال واستدعاؤها مباشرةً:
 
```python
from hijri_converter import hijri_to_gregorian, gregorian_to_hijri
 
# Hijri -> Gregorian
print(hijri_to_gregorian(1400, 10, 30))
# (1980, 9, 11, 'Thursday')   ->  year, month, day, weekday
 
# Gregorian -> Hijri
print(gregorian_to_hijri(1980, 9, 11))
# (1400, 11, 1, 'Thursday')
```
 
---
 
## الدوال المتاحة
 
| الدالة | تحوّل من/إلى | تُرجِع |
|--------|-------------|--------|
| `hijri_to_gregorian(y, m, d)` | تاريخ هجري ← ميلادي | `(السنة، الشهر، اليوم، يوم الأسبوع)` |
| `gregorian_to_hijri(y, m, d)` | تاريخ ميلادي ← هجري | `(السنة، الشهر، اليوم، يوم الأسبوع)` |
| `hijri_to_jdn(y, m, d)` | تاريخ هجري ← رقم اليوم اليولياني | رقم |
| `jdn_to_hijri(jdn)` | رقم اليوم اليولياني ← هجري | `(السنة، الشهر، اليوم)` |
| `gregorian_to_jdn(y, m, d)` | تاريخ ميلادي ← رقم اليوم اليولياني | رقم |
| `jdn_to_gregorian(jdn)` | رقم اليوم اليولياني ← ميلادي | `(السنة، الشهر، اليوم)` |
 
في جميع الدوال يكون ترتيب المعاملات: **السنة، ثم الشهر، ثم اليوم**.
 
---
 
## ملاحظة مهمّة حول الدقّة
 
تستخدم هذه الأداة **التقويم الهجري الجدولي (الحسابي)**، وهو قاعدة رياضية ثابتة
لتحديد بدايات الأشهر. وهو متّسق وقابل للعكس ومثالي للاستخدام في البرمجيات.
 
غير أن بعض الدول تُحدّد بداية كل شهر هجري عن طريق **رؤية الهلال** أو عبر تقاويم
رسمية مثل تقويم **أم القرى** في المملكة العربية السعودية. ولأن هذه الطرق تعتمد
على الرصد لا على الحساب البحت، فقد يختلف التاريخ المُحوَّل عن نتيجة هذه الأداة
بمقدار **يوم واحد ±**.
 
للاستخدام اليومي تكون النتائج دقيقة. أما للأغراض القانونية أو الدينية أو الرسمية،
فتحقّق دائمًا من التقويم المحلي أو الرسمي المعتمد.
 
**ملاحظة حول أطوال الأشهر:** تتناوب الأشهر الهجرية بين 30 و29 يومًا (الأشهر 1 و3
و5 و7 و9 و11 فيها 30 يومًا؛ والأشهر 2 و4 و6 و8 و10 و12 فيها 29 يومًا، ويزيد الشهر
12 يومًا في السنوات الكبيسة). إذا أدخلت يومًا يتجاوز طول الشهر، مثل اليوم 30 في شهر
مكوّن من 29 يومًا، فستظل الأداة تُنتج نتيجة ميلادية صحيحة، لكنها تنتقل إلى اليوم
التالي. ولهذا السبب فإن تحويل `30/10/1400 هـ` يعطي 11 سبتمبر 1980، بينما يُعيد
تحويل ذلك التاريخ الميلادي إلى الهجري التاريخ المعياري `01/11/1400 هـ`.
 
---
 
## الرخصة
 
<p align="center">
  <a href="https://github.com/khalidt/Hijri-Converter">Hijri-Converter</a>
  © 2026 by
  <a href="https://github.com/khalidt/">Khalid Alkhaldi</a>
  is licensed under
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a>

  <img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" height="18" alt="CC">
  <img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" height="18" alt="BY">
  <img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" height="18" alt="NC">
  <img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" height="18" alt="SA">
</p>

</div>

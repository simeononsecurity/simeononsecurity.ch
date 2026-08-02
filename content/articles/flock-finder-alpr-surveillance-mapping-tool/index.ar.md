---
title: "Flock Finder: خريطة كاميرات Flock Safety ALPR"
date: 2026-07-22
toc: true
draft: false
description: "Flock Finder هو أداة مفتوحة المصدر ترسم خرائط لأكثر من 40,000 كاميرا Flock Safety ALPR حول العالم باستخدام بيانات WiGLE WiFi وبصمة OUI. تعرف على آلية عملها وقيودها وأدوات الأجهزة للكشف في الوقت الفعلي."
genre: ["تقنية الخصوصية", "مراقبة مضادة", "مشاريع مفتوحة المصدر", "الحقوق الرقمية", "أمن الشبكات", "أدوات الخصوصية", "اختراق الأجهزة", "بحث الأمن"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "قارئ لوحة الترخيص", "بصمة OUI", "WiGLE", "مراقبة WiFi", "مراقبة مضادة", "STS Collective", "FlockYou", "ESP32", "أدوات الخصوصية", "NitekryDPaul", "DeFlockJoplin", "كشف ALPR", "أمن مفتوح المصدر", "رسم خرائط المراقبة", "مراقبة جماعية", "WiFi OUI", "حماية الخصوصية", "عنوان MAC", "الوضع العشوائي", "802.11", "كشف في الوقت الفعلي", "Wardriving", "الحقوق الرقمية", "الحريات المدنية", "وعي المراقبة", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "خريطة تفاعلية تعرض علامات ملونة تشير إلى مواقع كاميرات Flock Safety ALPR، مع إشارات WiFi مجردة تنبثق من العلامات على خلفية داكنة."
coverCaption: "Flock Finder يرسم خرائط لأكثر من 40,000 كاميرا Flock Safety ALPR مشتبه بها باستخدام بيانات WiGLE WiFi وبصمة OUI."
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**أداة توعية بالمراقبة مفتوحة المصدر ترسم خرائط لكاميرات Flock Safety ALPR باستخدام بيانات WiFi المجمّعة جماعيًا.**

## ما هو Flock Finder؟

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** هو مشروع مفتوح المصدر يرسم خرائط لـ **كاميرات Flock Safety ALPR (قارئ لوحات الترخيص الآلي)** عبر الولايات المتحدة و108 دولة أخرى. يجمع **31 بادئة OUI (معرف فريد تنظيمي) معروفة لـ Flock Safety WiFi** مع **قاعدة بيانات WiGLE WiFi المجمّعة جماعيًا** لتحديد ورسم مواقع الكاميرات المشتبه بها على خريطة تفاعلية.

يتواجد المشروع على **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**، يُحدَّث تلقائيًا يوميًا عبر GitHub Actions، وحتى يوليو 2026 رسم خرائط لـ **أكثر من 40,000 كاميرا مشتبه بها** عبر 964 منطقة حول العالم.

| المقياس | القيمة |
|--------|-------|
| **الكاميرات المرسومة** | 40,026+ |
| **بادئات OUI المعروفة** | 31 |
| **الدول المشمولة** | 109 |
| **المناطق المشمولة** | 964 |
| **الاحتفاظ بالبيانات** | 730 يومًا (سنتان) |
| **تكرار التحديث التلقائي** | يوميًا |

*هذه أداة توعية عامة، وليست جردًا نهائيًا. اقرأ قسم القيود قبل استخلاص استنتاجات من البيانات.*

للاطلاع على خلفية حول سبب أهمية مراقبة Flock Safety ALPR للخصوصية، اقرأ **[مراقبة كاميرا Flock Safety: الانتشار ومخاوف الخصوصية واستراتيجيات الحماية](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

______

## كيف يعمل: بصمة OUI عبر WiGLE

### الفكرة الجوهرية

تحتوي كاميرات Flock Safety على **أجهزة إرسال واستقبال WiFi** تستيقظ دوريًا من السكون لرفع بيانات لوحات الترخيص الملتقطة إلى السحابة. خلال هذه النوافذ النشطة القصيرة، تبث الكاميرا إطارات WiFi تحتوي على **عنوان MAC** الخاص بها — والبايتات الثلاثة الأولى من كل عنوان MAC تعرّف الشركة المصنعة. هذا هو **OUI (المعرف الفريد التنظيمي)**.

اكتشف الباحث الأمني **@NitekryDPaul** **30 بادئة OUI** مرتبطة باستمرار بأجهزة كاميرا Flock Safety من خلال **تحليل 2.4 GHz في وضع promiscuous**. تمت المساهمة بالبادئة الـ 31 (`82:6B:F2`) من قبل **Michael / DeFlockJoplin** أثناء الاختبار الميداني في Joplin, MO.

يأخذ Flock Finder تلك الـ 31 OUI، ويستعلم من WiGLE عن أي شبكات WiFi مسجلة تطابق تلك البادئات، ويرسم النتائج على خريطة.

### بادئات OUI الـ 31 المعروفة لـ Flock Safety

| # | بادئة OUI | المصدر | # | بادئة OUI | المصدر |
|---|-----------|--------|---|-----------|--------|
| 1 | **70:C9:4E** | @NitekryDPaul | 17 | **D0:39:57** | @NitekryDPaul |
| 2 | **3C:91:80** | @NitekryDPaul | 18 | **E8:D0:FC** | @NitekryDPaul |
| 3 | **D8:F3:BC** | @NitekryDPaul | 19 | **E0:4F:43** | @NitekryDPaul |
| 4 | **80:30:49** | @NitekryDPaul | 20 | **B8:1E:A4** | @NitekryDPaul |
| 5 | **B8:35:32** | @NitekryDPaul | 21 | **70:08:94** | @NitekryDPaul |
| 6 | **14:5A:FC** | @NitekryDPaul | 22 | **58:8E:81** | @NitekryDPaul |
| 7 | **74:4C:A1** | @NitekryDPaul | 23 | **EC:1B:BD** | @NitekryDPaul |
| 8 | **08:3A:88** | @NitekryDPaul | 24 | **3C:71:BF** | @NitekryDPaul |
| 9 | **9C:2F:9D** | @NitekryDPaul | 25 | **58:00:E3** | @NitekryDPaul |
| 10 | **C0:35:32** | @NitekryDPaul | 26 | **90:35:EA** | @NitekryDPaul |
| 11 | **94:08:53** | @NitekryDPaul | 27 | **5C:93:A2** | @NitekryDPaul |
| 12 | **E4:AA:EA** | @NitekryDPaul | 28 | **64:6E:69** | @NitekryDPaul |
| 13 | **F4:6A:DD** | @NitekryDPaul | 29 | **48:27:EA** | @NitekryDPaul |
| 14 | **F8:A2:D6** | @NitekryDPaul | 30 | **A4:CF:12** | @NitekryDPaul |
| 15 | **24:B2:B9** | @NitekryDPaul | 31 | **82:6B:F2** | DeFlockJoplin |
| 16 | **00:F4:8D** | @NitekryDPaul | | | |

### تقنية الكشف addr1

يتجاوز اكتشاف @NitekryDPaul الرئيسي مجرد المطابقة على عنوان MAC الموقِّع. تقضي كاميرات Flock معظم دورة عملها **نائمة**. عندما ترسل نقطة وصول قريبة إطارًا موجهًا *إلى* كاميرا، يظهر MAC الكاميرا كـ **addr1 (عنوان المستقبل)** في إطارات 802.11 — حتى أثناء عدم إرسال الكاميرا نفسها بنشاط.

مقترنًا بـ **كشف طلب المسح بعلامة wildcard** (إطارات إدارة 802.11 النوع=0، النوع الفرعي=4، SSID فارغ)، ينتج عن ذلك توقيع كشف دقيق جدًا. حقق الاختبار الميداني في Joplin, MO **11 من 12 كاميرا تم اكتشافها مع 2 إيجابيات كاذبة فقط**.

> ⚠️ **مهم**: خريطة Flock Finder المستندة إلى WiGLE **لا** تطبق تقنية addr1. WiGLE هي مجموعة بيانات تاريخية تُجمَّع بشكل سلبي — تسجّل فقط أجهزة الإرسال، وليس أجهزة الاستقبال. للكشف في الوقت الفعلي باستخدام طريقة @NitekryDPaul الفعلية، تحتاج إلى أجهزة مخصصة تعمل في الميدان.

______

## استخدام الخريطة الحية

الخريطة التفاعلية متاحة على **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)**. تعرض:

- **علامات الكاميرات المجمّعة** مرمّزة بالألوان حسب بادئة OUI
- **البحث** حسب المدينة أو الولاية أو BSSID
- **جدول بيانات OUI** مع أعداد الكاميرات لكل بادئة
- **لوحة الإحصاءات** تعرض إجمالي الكاميرات والمناطق وطابع وقت آخر تحديث
- **صفحة حول ALPR** مع أضرار الخصوصية الموثقة والسياق القانوني وموارد المجتمع

تصدير بيانات الخريطة متاح أيضًا مباشرة:

- `data/flock_cameras.geojson` — GeoJSON للاستخدام في QGIS أو Leaflet أو أدوات أخرى
- `data/flock_cameras.csv` — تنسيق ملائم للجداول
- `data/scan_stats.json` — إحصاءات المسح والأعداد

### القيود الرئيسية

**تعامل مع الخريطة بحذر.** WiGLE هي مجموعة بيانات مجمّعة جماعيًا وتُحدَّث بشكل متقطع، وليست تغذية حية.

- **لا تبث كاميرات Flock باستمرار.** تستيقظ لفترة وجيزة لرفع البيانات، لذا تعتمد سجلات WiGLE كليًا على وجود سائق wardriver قريب في اللحظة المناسبة تمامًا.
- **قد تكون البيانات أشهرًا أو سنوات قديمة.** قد لا تزال الكاميرات التي تم نقلها أو إزالتها تظهر.
- **مطابقة OUI هي أسلوب استدلالي.** يمكن مشاركة OUIs أو إعادة تعيينها أو انتحالها. كل نتيجة هي جهاز Flock *مشتبه به*، وليس مؤكدًا.
- **التغطية غير متساوية.** المناطق الحضرية الكثيفة لديها بيانات WiGLE أكثر؛ المناطق الريفية لديها أقل بكثير.

*استخدم الخريطة لتطوير وعي عام بكثافة المراقبة في منطقتك. للكشف في الوقت الفعلي بدقة أرضية، انظر خيارات الأجهزة أدناه.*

______

## تشغيل Flock Finder بنفسك

### المتطلبات الأساسية

- Python 3.8+
- حساب [WiGLE](https://wigle.net/account) مجاني مع بيانات اعتماد API

### الإعداد

```bash
# Clone the repository
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder

# Install dependencies
pip install -r requirements.txt

# Set up your WiGLE API credentials
cp .env.example .env
# Edit .env with your WiGLE API Name and Token
```

### تشغيل الماسح

```bash
# Full scan — all 31 OUI prefixes, worldwide
python3 scripts/wigle_query.py

# Single OUI test
python3 scripts/wigle_query.py --oui 70:C9:4E

# US only
python3 scripts/wigle_query.py --country US

# Specific bounding box (lat1,lon1,lat2,lon2)
python3 scripts/wigle_query.py --bbox 37,-97,39,-94

# Dry run — verify auth, no API queries
python3 scripts/wigle_query.py --dry-run
```

### عرض الخريطة محليًا

```bash
python3 -m http.server 8080 --directory docs/
# Open http://localhost:8080 in your browser
```

### التحديثات اليومية الآلية عبر GitHub Actions

انسخ المستودع وأضف بيانات اعتماد WiGLE الخاصة بك كـ **أسرار المستودع** (`WIGLE_API_NAME` و`WIGLE_API_TOKEN`). يعمل سير العمل المضمّن في الساعة 6 صباحًا UTC يوميًا ويُثبّت تلقائيًا ملفات البيانات المحدّثة عند العثور على كاميرات جديدة.

______

## الكشف في الوقت الفعلي: أجهزة STS Collective FlockYou

تخبرك خريطة WiGLE بمكان الكاميرات *التي تم رصدها*. للكشف في الوقت الفعلي أثناء القيادة — باستخدام طريقة مطابقة OUI الفعلية لـ @NitekryDPaul على حركة WiFi الحية — تحتاج إلى أجهزة مخصصة.

تصنع **[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** أجهزة كشف محمولة تعتمد على ESP32 تمسح بحثًا عن توقيعات Flock OUI وتنبهك فور اكتشاف توقيع مطابق.

### تشكيلة أجهزة FlockYou

| الجهاز | الوصف |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | كاشف Flock مضغوط بحجم الجيب. مُبرمج مسبقًا، جاهز للاستخدام الفوري. تنبيهات LED عند الكشف. |
| **FlockYou Pro — LED + Audio** | يضيف تنبيهات صوتية إلى جانب مؤشرات LED. لا تفوتك كاميرا أثناء القيادة. |
| **FlockYou Atom VoiceS3R** | كاشف ممكّن صوتيًا مع تنبيهات صوتية منطوقة لتشغيل حر اليدين مع إبقاء العينين على الطريق. |

جميع الأجهزة:
- **مُبرمجة مسبقًا**، جاهزة للاستخدام فور إخراجها من الصندوق
- تمسح حركة WiFi الحية بحثًا عن جميع الـ 31 OUI المعروفة لـ Flock
- مضغوطة ومحمولة — تناسب حامل الكوب أو الجيب
- مزوّدة بالطاقة عبر USB-C (محوّل سيارة، بنك طاقة، أو كمبيوتر محمول)

> 💰 **خصومات حصرية**: استخدم رمز **FLOCKFINDER** للحصول على **20% خصم** على جميع أجهزة STS Collective FlockYou — أو استخدم رمز **SIMEONONSECURITY** للحصول على ما يصل إلى 20% خصم على طلبك بالكامل. [تسوق على stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

للاطلاع على تحليل تقني كامل لهذه الأجهزة وبدائل DIY، اقرأ **[مشروع كشف Flock-You: دليل شامل للأجهزة المضادة للمراقبة والإعداد](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**.

______

## هيكل المشروع

```
flock-finder/
├── scripts/
│   └── wigle_query.py        # WiGLE API query and data pipeline
├── data/
│   ├── flock_ouis.csv         # 31 known Flock Safety OUI prefixes
│   ├── flock_cameras.geojson  # Camera locations (GeoJSON)
│   ├── flock_cameras.csv      # Camera locations (CSV)
│   └── scan_stats.json        # Scan statistics
├── docs/
│   └── index.html             # Interactive Leaflet map
└── .github/workflows/
    └── update-data.yml        # Daily auto-update workflow
```

______

## الأسئلة الشائعة

### هل هذا قانوني؟

نعم. **يستخدم Flock Finder فقط البيانات المتاحة للعموم** من قاعدة بيانات WiGLE، التي تجمع بيانات مسح WiFi المساهم بها طوعًا. لا يوجد اختراق أو وصول غير مصرح به أو أنظمة خاصة متضمنة. مراقبة WiFi السلبية لتوقيعات OUI قانونية في الولايات المتحدة.

### هل كل كاميرا مرسومة هي بالتأكيد كاميرا Flock؟

لا. مطابقة OUI هي **أسلوب استدلالي**. يمكن مشاركة بادئات OUI عبر الشركات المصنعة أو إعادة تعيينها أو انتحالها. كل سجل في قاعدة البيانات هو جهاز Flock *مشتبه به* — وليس مؤكدًا. اقرأ [سياسة البيانات](https://github.com/simeononsecurity/flock-finder/blob/main/docs/data-policy.md) للتفاصيل حول كيفية طلب تصحيح.

### لماذا لا تظهر بعض بادئات OUI أي كاميرات؟

تغطية WiGLE غير متساوية. إذا لم يقم أي wardriver بمسح منطقة معينة مع تلك OUI النشطة المحددة، فلن تكون هناك سجلات. *غياب البيانات لا يعني غياب الكاميرات.*

### ما مدى حداثة البيانات؟

يعمل سير عمل GitHub Actions يوميًا ويسحب أحدث نتائج WiGLE. ومع ذلك، قد يحتوي WiGLE نفسه على سجلات تتراوح من أيام إلى سنوات لأي موقع معين. تحقق من ملف `scan_stats.json` للاطلاع على طابع وقت المسح الأخير.

### هل يمكنني المساهمة ببيانات wardrive الخاصة بي؟

نعم. ارفع بيانات wardrive إلى [WiGLE](https://wigle.net) — تتغذى تلقائيًا في المسح اليومي التالي لـ Flock Finder. يمكنك أيضًا المساهمة ببادئات OUI أو تحسينات الكود عبر [دليل المساهمة](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md).

______

## المجتمع والمشاريع ذات الصلة

لا يقف Flock Finder وحده. نظام بيئي متنامٍ من الأدوات والمنظمات يعمل على توثيق ومواجهة مراقبة ALPR:

- **[DeFlock.org](https://deflockjoplin.org/)** — تتبع ALPR ووثيق ومناصرة بقيادة المجتمع
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — تحقق مما إذا كانت لوحتك قد تم البحث عنها في نظام Flock
- **[FlockHopper](https://flockhopper.com/)** — تخطيط المسار الذي يتجنب كاميرات ALPR المعروفة
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — قاعدة بيانات EFF لتقنية المراقبة التي تستخدمها جهات تطبيق القانون
- **[NoALPRs.com](https://noalprs.com/)** — موارد للمجتمعات التي تكافح نشر ALPR
- **[DeFlockJoplin](https://deflockjoplin.org/)** — برامج ثابتة مفتوحة المصدر وبحث ميداني؛ ساهمت بالبادئة الـ OUI الـ 31

______

## الاعتمادات

- **بحث OUI**: @NitekryDPaul — جميع بادئات الـ OUI الأصلية الـ 30 واستراتيجية الكشف addr1/promiscuous-mode
- **الاختبار الميداني**: Michael / DeFlockJoplin — بادئة OUI الـ 31 (`82:6B:F2`) وتشديد مسح wildcard
- **مصدر البيانات**: [WiGLE](https://wigle.net) — قاعدة بيانات WiFi/شبكة الخلية المجمّعة جماعيًا
- **مستوحى من**: [DeFlock](https://deflockjoplin.org/) وtrack-openroaming-passpoint
- **شريك الأجهزة**: [STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — كاشفات FlockYou ESP32

______

## الخاتمة

**Flock Finder** يمنح أي شخص إحساسًا سريعًا وبصريًا بمدى انتشار كاميرات Flock Safety ALPR — أكثر من 40,000 موقع مقدّر عبر 109 دول، يُحدَّث تلقائيًا كل يوم من بيانات WiFi المجمّعة جماعيًا.

إنه **أداة شفافية**، وليس متتبعًا حيًا. بياناته تاريخية وغير مكتملة واحتمالية. لكنها تجعل حجم مراقبة ALPR مرئيًا بطريقة لا تستطيع الملخصات والتقارير فعلها.

للحماية الفعلية في الوقت الفعلي أثناء تنقلك عبر المناطق الخاضعة للمراقبة، اقرن الخريطة بأجهزة مخصصة. **[أجهزة FlockYou من STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** تطبّق طريقة @NitekryDPaul للكشف مباشرة على ESP32 وتنبهك فور اكتشاف توقيع كاميرا حية — متاحة على **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** برمز **FLOCKFINDER** أو **SIMEONONSECURITY** للحصول على ما يصل إلى 20% خصم.

### مقالات ذات صلة

| المقالة | ما تغطيه |
|---------|---------------|
| **[مراقبة كاميرا Flock Safety: الخصوصية والحماية](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | الصورة الكاملة: إحصاءات الانتشار، قضايا الحريات المدنية، مجموعة أدوات ACLU، إحصاءات DeFlock، دليل FOIA، واستراتيجيات الحماية |
| **[مشروع كشف Flock-You: دليل أجهزة المراقبة المضادة](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | دليل تقني كامل لكاشفات Flock المستندة إلى ESP32 — OUI-SPY، M5 Atom Lite، بناء DIY، إعداد البرامج الثابتة خطوة بخطوة |
| **[كيفية فلاش أجهزة Rayhunter: دليل كامل](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | كشف ماسكات IMSI (محاكيات مواقع الخلايا) إلى جانب كاميرات ALPR للوعي الكامل بالمراقبة المضادة |
| **[برامج DagShell المخصصة لـ Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | تحويل نقطة اتصال محمولة إلى منصة بحث أمني — تتزاوج جيدًا مع أجهزة كشف Flock |
| **[مقارنة أجهزة Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | مقارنة خيارات أجهزة الكشف عبر فئات تهديد ALPR والمراقبة الخلوية |

______

## المراجع

1. [مستودع Flock Finder على GitHub](https://github.com/simeononsecurity/flock-finder)
2. [خريطة Flock Finder التفاعلية](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — أجهزة FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — رسم خرائط الشبكات اللاسلكية](https://wigle.net)
5. [DeFlock — توعية ALPR المجتمعية](https://deflockjoplin.org/)
6. [DeFlockJoplin — برامج ثابتة للكشف مفتوحة المصدر](https://deflockjoplin.org/)
7. [مؤسسة الحدود الإلكترونية — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — أنت تحت المراقبة](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)

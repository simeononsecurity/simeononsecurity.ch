---
title: "تحسين الصور باستخدام Python"
date: 2023-07-04
lastmod: 2026-11-13
toc: true
draft: false
description: "حسّن الصور باستخدام Python عبر تغيير الحجم والضغط وتحويل التنسيقات وسير العمل المتكرر في Pillow."
genre: ["التقنية", "تطوير الويب", "برمجة Python", "تحسين الصور", "تحسين محركات البحث", "أداء الويب", "تجربة المستخدم", "تطوير البرمجيات", "الأتمتة", "البرمجة"]
tags: ["تحسين الصور", "Python", "تحسين الصور", "تطوير الويب", "أداء المواقع", "تجربة المستخدم", "الضغط", "تغيير الحجم", "تحويل التنسيقات", "معالجة الصور", "مكتبة Pillow", "مكتبة Tinify", "الأتمتة", "برنامج Python النصي", "تحسين أداء الويب", "تحسين محركات البحث", "تطوير البرمجيات", "تصميم الويب", "ضغط الصور", "تقليل حجم الملفات", "التحميل الكسول", "تنسيقات الصور", "تنسيق WebP", "تكامل API", "سير عمل التطوير", "مثال برمجي", "تقنيات تحسين الصور", "تحسين الأداء", "درس برمجي"]
cover: "/img/cover/An_illustration_of_a_Python_script_optimizing.webp"
coverAlt: "رسم يوضح برنامج Python يحسّن الصور، مع عدسة مكبرة تعرض صورة مضغوطة."
coverCaption: "غيّر حجم الصور واضغطها وحسّنها باستخدام Python."
---

**مقدمة**

يؤثر حجم الصور في سرعة الموقع وتجربة زواره. فالصور الكبيرة قد تطيل وقت التحميل وتزيد احتمال مغادرة الزائر. يتيح **Python** ومكتبته Pillow تقليل أحجام الصور وتحسين طريقة عرضها على الويب. يشرح هذا المقال طرقاً وأدوات عملية **لتحسين الصور** باستخدام Python.

______

## لماذا يهم تحسين الصور

يعني **تحسين الصور** تقليل حجم ملفاتها مع الحفاظ على جودة بصرية مناسبة. يفيد ذلك في جوانب عدة:

1. **تحميل الصفحات أسرع**: قد تبطئ ملفات الصور الكبيرة تحميل الموقع، وهذا يؤثر في تحسين محركات البحث وتجربة المستخدم.

2. **استهلاك أقل للنطاق الترددي**: تحتاج الصور المحسّنة إلى بيانات أقل، فيسهل على أصحاب الاتصالات المحدودة فتح الموقع.

3. **ملاءمة أفضل للهواتف**: غالباً ما تكون اتصالات الهاتف أبطأ، لذلك يساعد تحسين الصور على عرض الصفحات بسلاسة على الهواتف والأجهزة اللوحية.

4. **دعم تحسين محركات البحث**: تضع محركات البحث سرعة الموقع ضمن عوامل الترتيب، وقد تحقق الصفحات الأسرع ظهوراً أفضل في نتائج البحث.

______

## تقنيات تحسين الصور

### **1. ضغط الصور**

يقلل ضغط الصور حجم الملف. توفر مكتبة **Pillow** في Python أدوات مباشرة لضغط الصور بإعدادات متعددة، ما يتيح الموازنة بين حجم الملف وجودة الصورة. ثبّت Pillow باستخدام pip:

```python
pip install Pillow
```

إليك مثالاً لضغط صورة:

```python
from PIL import Image

# افتح صورة
image = Image.open("input_image.jpg")

# اضغط الصورة واحفظها
image.save("compressed_image.jpg", optimize=True, quality=85)
```

### **2. تغيير حجم الصور**

اضبط أبعاد الصورة لتناسب المساحة التي ستظهر فيها على الموقع. قد تظل الصورة الكبيرة بطيئة حتى لو صغّرها HTML أو CSS، لأن المتصفح ينزّل الملف كاملاً. تجعل Pillow تغيير الحجم بسيطاً:

```python
from PIL import Image

# افتح صورة
image = Image.open("input_image.jpg")

# غيّر حجم الصورة
resized_image = image.resize((800, 600))

# احفظ الصورة بعد تغيير حجمها
resized_image.save("resized_image.jpg")
```

### **3. تحويل تنسيق الصور**

قد يقلل التحويل إلى تنسيقات أكثر كفاءة مثل WebP حجم الملف مع الحفاظ على الجودة. تدعم معظم المتصفحات الحديثة WebP، وتتيح Pillow حفظ الصور بهذا التنسيق:

```python
from PIL import Image

# افتح صورة
image = Image.open("input_image.jpg")

# حوّل الصورة إلى تنسيق WebP
image.save("output_image.webp")
```

## أتمتة تحسين الصور باستخدام Python


### مثال برنامج Python النصي: استخدام واجهة TinyPNG

توفر الأتمتة الوقت والجهد عند معالجة صور كثيرة. تتيح مكتبات Python تنفيذ مهام التحسين آلياً. مكتبة Tinify هي غلاف Python لواجهة TinyPNG البرمجية.

تضغط Tinify الصور وتحسّنها بخوارزميات متقدمة، فتقلل أحجام ملفاتها مع الحفاظ على جودتها. لاستخدامها، أنشئ حساباً في موقع Tinify واحصل على مفتاح API.

فيما يلي مثال يستخدم **Tinify** لضغط صورة:

```python
import tinify

# اضبط Tinify باستخدام مفتاح API الخاص بك
tinify.key = "YOUR_API_KEY"

# اضغط الصورة
source = tinify.from_file("input_image.jpg")
source.to_file("compressed_image.jpg")
```

### مثال برنامج Python النصي: تحسين صور مجلد

يعرض المثال التالي برنامجاً يقرأ صوراً بأنواع مختلفة، مثل JPEG وPNG، ويصدر نسخاً محسّنة بتنسيق WebP:

```python
import os
from PIL import Image

# دالة لتحويل الصورة إلى تنسيق WebP
def convert_to_webp(input_path, output_path, quality=85):
    image = Image.open(input_path)
    image = image.convert("RGB")
    image.save(output_path, "webp", optimize=True, quality=quality)

# دالة للتكرار على صور مجلد وتحويلها إلى WebP
def optimize_images(folder_path, output_folder, quality=85):
    # أنشئ مجلد الإخراج إذا لم يكن موجوداً
    os.makedirs(output_folder, exist_ok=True)
    
    # كرّر العملية لكل ملف في المجلد
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # أنشئ مساري الإدخال والإخراج
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")
            
            # حوّل الصورة إلى تنسيق WebP
            convert_to_webp(input_path, output_path, quality=quality)

# مثال للاستخدام
folder_path = "input_images"
output_folder = "optimized_images"
optimize_images(folder_path, output_folder, quality=80)
```

يستخدم المثال مكتبة Python Imaging Library (PIL) لفتح الصور وتحويلها إلى WebP. تستقبل الدالة `convert_to_webp` مسار ملف الإدخال ومسار الإخراج ومعامل الجودة الاختياري، وقيمته الافتراضية 85. تمر الدالة `optimize_images` على ملفات المجلد، وتتحقق من امتدادات الصور المقبولة، ثم تستدعي `convert_to_webp`. تحفظ الملفات المحسّنة في مجلد الإخراج المحدد.

عدّل قيم `folder_path` و`output_folder` و`quality` لتناسب ملفاتك.

## الخلاصة

يساعد تحسين الصور على تسريع المواقع وتحسين تجربة المستخدم وتقوية أداء الصفحات في نتائج البحث. توفر منظومة Python أدوات عملية لضغط الصور وتغيير أبعادها وتحويل تنسيقاتها وأتمتة هذه المهام. تتيح Pillow وTinify معالجة صورة واحدة أو دفعات من الصور وتقليل حجم الملفات دون التضحية بجودة بصرية مناسبة. ابدأ بتحديد أبعاد الصور وجودتها، ثم طبّق الإعدادات نفسها على سير عملك.


## المراجع
- https://pillow.readthedocs.io/en/stable/
- https://developers.google.com/speed/webp
- https://tinypng.com/developers

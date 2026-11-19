---
title: 'التراجع من Home Assistant Core 2026.11 إلى 2026.10.4: إصلاح إصدار تخزين HTTP 3'
date: 2026-11-15
lastmod: '2026-11-18'
toc: true
draft: false
description: أصلح خطأ إصدار تخزين HTTP 3 بعد رجوع Home Assistant Core 2026.11 إلى 2026.10.4 على Yellow. يتضمن أوامر محمية
  ومخرجات جرى التحقق منها.
genre:
- أتمتة المنزل
- استكشاف الأخطاء وإصلاحها
tags:
- Home Assistant Yellow
- Home Assistant OS
- التراجع عن Core 2026.11
- Core 2026.10.4
- إصدار تخزين HTTP 3
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: رسم توضيحي للوحة حاسوب صفراء ورابط إعدادات مكسور ولوحة تحكم ويب أُعيد تشغيلها
coverCaption: ''
---

أعاد فشل تحديث Home Assistant Core 2026.11 جهاز Yellow CM4 لدي إلى الإصدار 2026.10.4. ظل Yellow متاحًا عبر الشبكة، لكنه توقف عن عرض لوحة التحكم. ترك التراجع ملف إعدادات HTTP بإصدار تخزين 3.1، بينما يدعم Core 2026.10.4 الإصدار 2.2. احتفظت بالملف، وحولت نسخة منه ضمن فحوص صارمة، وأعدت الوصول عبر HTTP، ثم حدثت Core إلى 2026.11.1.

<!--more-->

## أهم النقاط

- **تحقق من عدم التطابق.** قارن خطأ سجل Core بالإصدار المثبت وإصدار تخزين HTTP.
- **احتفظ بالملف.** احتفظ بنسخة غير معدلة ونسخة احتياطية خارج الجهاز قبل الاسترداد.
- **تحقق من النتيجة.** افحص حالة Core وإعداد المستمع المحفوظ ولوحة التحكم والإصدار المثبت.

**إصلاح هذه الحالة تحديدًا:** [احتفظ بملف HTTP](#preserve-recovery-options)، و[أنشئ مرشحًا للإصدار 2.2 وتحقق منه](#apply-the-tested-fix-for-version-31)، ثم [ثبته بعد إيقاف Core](#apply-the-tested-fix-for-version-31)، و[تحقق من نتيجة التحديث](#verify-the-update-outcome). يفحص التحويل الحقول الأصلية ويتوقف عند اختلافها. لا تطبقه على ملف HTTP لم تفحصه.

## قبل البدء

تحتاج إلى وصول مادي إلى Yellow CM4، وكابل بيانات USB-C، ووحدة تحكم تسلسلية تعمل، ونسخة احتياطية صالحة أو إعداد محفوظ. يتطلب المسار اليدوي وصولًا إلى shell المضيف وفحصًا دقيقًا لملف JSON. خصص 30 دقيقة على الأقل للتشخيص والإصلاح. يستغرق بدء Core واستعادة النسخ الاحتياطية وقتًا أطول في عمليات التثبيت الكبيرة.

## التعرّف على العطل

ظهر الخطأ الحاسم في سجل Core:

```text
Storage file http has version 3 which is newer than the max supported version 2
```

تعذر على إصدار Core الأقدم تحميل `http`. وتعطلت أيضًا الواجهة الأمامية والمكونات الأخرى التي تعتمد على HTTP. لم يكن حصول الموجه على عنوان ولا سلامة صفحة Observer دليلًا على إمكانية الوصول إلى لوحة التحكم. يوثق [العطل رقم 190583 في Home Assistant Core](https://github.com/home-assistant/core/issues/190583) فشل التراجع نفسه في عدة عمليات تثبيت، منها Yellow. ويسجل [تعليقي على العطل](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) الاسترداد الذي اختبرته على Yellow وحالة Core النهائية.

**سبب انقطاع الويب:** كتب Core 2026.11 ملف `.storage/http` بالتنسيق 3.1. أعاد التراجع Core 2026.10.4، لكنه لم يستعد ملف HTTP متوافقًا. يرفض Core 2026.10.4 إصدار التخزين 3. كما أن ملف `intermediate_v6` المحفوظ في Yellow هذا لا يطابق المخطط الأقدم. لا يُعرف سبب فشل التحديث الأول وبدء التراجع. حتى 2026-11-15، ظل العطل المرتبط مفتوحًا ولم يتضمن النقاش حلًا أكده أحد المشرفين.

تحقق من إصدار Core المثبت وملف HTTP قبل تغيير الملفات:

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

تعكس المخرجات التالية هذه الحالة بعد إزالة الطوابع الزمنية والتفاصيل الخاصة:

```text
2026.10.4
{
  "version": 3,
  "minor_version": 1,
  "pending_present": false,
  "profile": "intermediate_v6"
}
Storage file http has version 3 which is newer than the max supported version 2
```

تقارن أوامر الاسترداد أدناه المستمع المحفوظ لدى Supervisor بملف HTTP دون عرض أي من القيمتين. إذا اختلفتا، فتحقق من مستمع Core الفعلي قبل تغيير الملفات.

| الإشارة | المعنى |
| --- | --- |
| يدعم Core إصدار التخزين 2، بينما يذكر الملف الإصدار 3 | لا يستطيع الإصدار الأقدم تحميل إعدادات HTTP المحفوظة |
| يسجل ملف HTTP ومستمع Supervisor قيمتين مختلفتين | تحقق من مستمع Core الفعلي قبل تحديد سبب العطل |
| تستجيب الصفحة الأولى بينما تظل حالة Core هي STARTING | استجابة الواجهة وحدها لا تثبت اكتمال بدء التشغيل |

## الحفاظ على خيارات الاسترداد {#preserve-recovery-options}

احتفظ بنسخة احتياطية صالحة خارج Yellow قبل أي تحديث آخر. يشرح [دليل النسخ الاحتياطي من Home Assistant](https://www.home-assistant.io/common-tasks/general/backups/) مواقع التخزين السحابي وخارج الجهاز. تحتاج النسخة المشفرة إلى مفتاح الاسترداد الخاص بها. لا تمسح قرص NVMe أثناء تشخيص عدم تطابق التخزين هذا.

انسخ ملف HTTP قبل تعديله:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

توقف إذا فشل الأمر. اترك أي نسخة استرداد سابقة بالاسم نفسه دون تغيير. اختر اسمًا جديدًا وكرر الفحص قبل المتابعة.

إذا تعذرت لوحة التحكم، فاستخدم وحدة التحكم التسلسلية في Yellow. يوضح [دليل Nabu Casa لنظامي Linux وmacOS](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) توصيل USB-C وموضع UART عند JP1. اتبع تعليمات CM4 الملائمة لجهازك.

## تطبيق الإصلاح المختبر للإصدار 3.1 {#apply-the-tested-fix-for-version-31}

المسار المفضل هو استخدام ملف HTTP متوافق من قبل التحديث. استعد النسخة الاحتياطية عبر العملية الموثقة في Home Assistant عندما تكون الاستعادة الكاملة مناسبة. إذا استخرجت ملفًا واحدًا، فتحقق من إصدار تخزينه والمستمع المحفوظ قبل استبدال الملف النشط. الأوامر أدناه هي الإصلاح المباشر الذي اختبرته على Yellow هذا عند عدم توفر ملف HTTP متوافق.

ينقل [الحل المؤقت الأصلي في العطل](https://github.com/home-assistant/core/issues/190583) ملف `.storage/http` إلى موضع آخر ويترك Core الأقدم ينشئ ملفًا جديدًا. ويعرض [تقرير لاحق من Yellow](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) مستمعًا مختلفًا في الملف الذي أُعيد إنشاؤه. افحص الملف الجديد ونتيجة `ha core info` قبل استنتاج أن واجهة الويب عادت للعمل.

لم يتضمن تثبيتي كتلة YAML باسم `http:` أو إعداد HTTP معلقًا، ولم يتضمن الإعداد الثابت شهادة TLS أو مفتاحًا. كان الملف يحفظ ملف `intermediate_v6`. في هذه الحالة المحدودة، أنشأت مرشحًا منفصلًا بالإصدار 2.2 واحتفظت بالمستمع الحالي:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage

expected=$(ha core info --raw-json | jq -r '.data.port') &&
stored=$(jq -r '.data.stable.server_port' "$storage/http") &&
test -n "$expected" &&
test "$expected" != null &&
test "$expected" = "$stored" &&
test ! -e "$storage/http.v2-candidate" &&
jq -e '
  if .version == 3 and .minor_version == 1 and
     .data.pending == null and
     .data.stable.ssl_profile == "intermediate_v6" and
     (.data.stable | has("ssl_certificate") | not) and
     (.data.stable | has("ssl_peer_certificate") | not) and
     (.data.stable | has("ssl_key") | not) and
     (.data.stable | has("trusted_proxies") | not) and
     (.data.stable | has("use_x_forwarded_for") | not)
  then .version = 2 | .minor_version = 2 | .data.stable.ssl_profile = "intermediate"
  else error("Unexpected HTTP config. Stop and inspect")
  end
' \
  "$storage/http" > "$storage/http.v2-candidate" &&

jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&

test "$(jq -r '.data.stable.server_port' "$storage/http")" = \
  "$(jq -r '.data.stable.server_port' "$storage/http.v2-candidate")"
```

يجب أن تنجح جميع الأوامر أعلاه قبل استبدال الملف النشط. إذا فشل `jq`، افحص ملف المرشح قبل حذفه وإعادة المحاولة. يعرّف [مصدر HTTP في Core 2026.10.4](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) إصدار تخزين 2.2 ويقبل الملف `intermediate`. ويستخدم [مصدر Core 2026.11.1](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) الإصدار 3.1 وأسماء ملفات الإصدارات. كما تحققت من المرشح باستخدام `HTTP_STORAGE_SCHEMA` في Core الأقدم المثبت قبل تثبيته.

شغّل فحص المخطط الخاص بإصدار Core الأقدم المثبت بينما تظل حاويته تعمل:

```bash
docker exec homeassistant python3 -c '
import json
from homeassistant.components.http.config import HTTP_STORAGE_SCHEMA
with open("/config/.storage/http.v2-candidate") as source:
    data = json.load(source)
stable = {
    key: value for key, value in data["data"]["stable"].items()
    if key not in ("created_at", "error", "error_message")
}
HTTP_STORAGE_SCHEMA(stable)
print("Schema accepted")
'
```

توقف إذا رفض المخطط المرشح. لا تتحقق هذه الخطوة من كل تكامل أو من شكل غير مختبر لمخزن HTTP.

طبع فحص المخطط `Schema accepted` لهذا المرشح. وأي نتيجة أخرى توقف مسار الاسترداد هذا.

اختُبر هذا التحويل اليدوي للحقول المذكورة. يحتاج الملف الذي يتضمن إعدادات TLS أو وكلاء موثوقًا بهم أو إعدادًا معلقًا إلى مراجعة مستقلة. ترك تغيير رقم الإصدار الأعلى فقط ملفًا يستخدم ملف تعريف لا يقبله Core الأقدم.

كان لدى Supervisor عمل Core نشط ورفض `ha core stop` في حالتي. أوقفت حاوية Core من وحدة تحكم المضيف، وثبت المرشح الذي جرى التحقق منه، ثم شغلتها:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&
  docker stop homeassistant &&
  test "$(docker inspect -f '{{.State.Running}}' homeassistant)" = false &&
  cmp -s "$storage/http" "$storage/http.before-recovery" &&
  mv "$storage/http.v2-candidate" "$storage/http" &&
  docker start homeassistant
```

إذا فشل أمر بعد الإيقاف، فافحص ملف HTTP النشط قبل تشغيل `docker start homeassistant`. يتطلب الملف المتغير إنشاء مرشح جديد من أحدث محتوياته. عادت صفحة HTTP بعد هذه الخطوة. ولم تكن استجابة HTTP وحدها دليلًا على اكتمال بدء Core، لذا تحققت من حالة Supervisor قبل اعتبار النظام مستردًا.

في Yellow هذا، طبع `docker inspect -f '{{.State.Status}}' homeassistant` القيمة `running`. افحص `ha core info` ولوحة التحكم قبل طلب تحديث آخر.

## التحقق من نتيجة التحديث {#verify-the-update-outcome}

بعد عودة الوصول عبر HTTP، حدثت Core إلى 2026.11.1. لطلب هذا الإصدار:

```bash
ha core update --version 2026.11.1
```

أبلغ الأمر عن فشل بعد بدء تشغيل طويل. ثم سجل Supervisor أن Core بحالة RUNNING وظهرت الرسالة `Successfully started Home Assistant 2026.11.1`. أظهر فحص الحالة أن الإصدار المثبت هو الحالي، وأن ملف HTTP انتقل مجددًا إلى إصدار 3.1، وأن الحاوية لم تُعِد التشغيل خلال فترة المراقبة. وتم تحميل لوحة التحكم بعد المصادقة. **تحقق من الحالة الناتجة حتى عندما يبلغ أمر التحديث عن فشل.**

في نظامك، افحص الإصدار وسلامة Supervisor وحالة الحاوية بعد أي تحديث طويل:

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

أنتج الأمران الأول والثالث النتائج المنقحة التالية في هذه الحالة:

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

ثم افتح لوحة التحكم عبر العنوان المحلي المعتاد وتأكد من تحميل الحالات الحية. احتفظ بملف HTTP المحفوظ حتى تكتمل نسخة احتياطية لاحقة ويُتحقق من استقرار التشغيل المعتاد.

لم يثبت الدليل على Yellow لدي سبب فشل التحديث الأول. كما لم تحدد رسالة فشل المهمة اللاحقة سببًا. يشكل الإصدار المثبت ولوحة التحكم السليمة دليلًا أقوى على الحالة الناتجة من رسالة CLI وحدها، لكنهما لا يفسران سبب إبلاغ Supervisor عن فشل المهمة.

## الخطوات التالية

إذا استمر خطأ تخزين HTTP، فافحص الملف المحفوظ واستعد نسخة احتياطية متوافقة أو شغّل إصدار Core يستطيع قراءة إصدار التخزين. يؤدي استعادة ملف الإصدار 3 المحفوظ تحت Core الأقدم إلى تكرار العطل. إذا وصل Core إلى RUNNING لكن بقيت بعض الأجهزة غير متاحة، فافحص تلك التكاملات على حدة. احتفظ بنسخة الاسترداد والنسخة السحابية حتى تكتمل النسخة الاحتياطية التالية وتظل لوحة التحكم مستجيبة.

---
title: "المشروع الختامي لسير عمل الذكاء الاصطناعي: أنشئ تقرير JSON وتحقق منه"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "أنشئ تقرير مهام JSON يتضمن سياق المشروع، وطلبًا محدد النطاق للوكيل، واختبارات مستقلة، ومراجعة للمصادر، وتسليمًا لجلسة جديدة."
genre: ["الذكاء الاصطناعي", "هندسة البرمجيات", "التعليم"]
tags: ["المشروع الختامي لسير عمل الذكاء الاصطناعي", "مشروع وكيل البرمجة", "التحقق من مهام الذكاء الاصطناعي", "AGENTS.md", "تمرين MCP", "تسليم الوكيل"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "مهمة برمجية مكتملة في ورشة عمل، مع ملفات المصدر ونتائج الاختبارات ومراجعة الوكيل وسجل التسليم"
coverCaption: ""
---

[العودة إلى دورة سير عمل الذكاء الاصطناعي العملي](/effective-ai-course-start/)

**أنشئ تنسيق إخراج جديدًا وأثبت سلوكه.** أضفت سابقًا عامل تصفية للحالة. يبدأ هذا المشروع الختامي بمختبر جديد ويضيف تقرير JSON ليقرأه برنامج آخر. يختبر المتطلب الجديد قدرتك على نقل سير عملك إلى ميزة مختلفة.

**هدف التعلم:** ستسلّم تقرير JSON تم التحقق منه، وسجلًا لأدلة المصادر والأدوات، وتسليمًا تفهمه جلسة جديدة.

## أهم النقاط

- **متطلب مستقل** يحدد ميزة المشروع الختامي.
- **تعديل وكيل البرمجة** يظل محصورًا في الملفات المحددة.
- **عمليات تحقق مستقلة** تحدد القبول.
- **تسليم إلى جلسة جديدة** يتيح إعادة بناء النتيجة.

## قبل البدء

**المتطلبات السابقة:** أكمل الدروس من 0 إلى 10، بما فيها سياق المستودع، ومهمة البرمجة الأولى، وMCP أو بديله في المتصفح، والتفويض، والحلقات المحدودة. الدرس 11 اختياري. خصص من 90 إلى 120 دقيقة. مستوى الصعوبة متوسط.

**استخدم نسخة استخراج جديدة** من [مختبر البداية](/downloads/effective-ai-course-lab.zip). شغّل `python3 task_report.py tasks.json` واختباري الأساس قبل إجراء أي تعديل. في Windows، استخدم `py -3` إذا كان إعدادك يعتمد مشغّل Python. أنشئ نقطة أساس محلية في Git كما فعلت في إعداد الدورة. عامل تصفية الحالة من الدرس 5 غير موجود عمدًا.

**اقرأ `docs/capstone-requirements.md`، المراجعة 1.** يتطلب `--format text|json`. يظل النص الافتراضي `Total tasks: 4`. يحتوي إخراج JSON على إجمالي رقمي وعدد لكل حالة في البيانات. اختبر قائمة فارغة، وحالة مفقودة، وتنسيقًا غير مدعوم. لا تعتمد على `docs/requirements.md` بوصفه مرجعًا لهذه الميزة الجديدة.

**اختر المسار.** يستخدم المسار المتصل تعديلًا ملحوظًا نفّذه وكيل برمجة، واستدعاء MCP حقيقيًا للقراءة فقط، وعاملًا أصليًا أو جلسة عامل منفصلة. يستخدم مسار الدراسة مساعد محادثة لاقتراح التعليمات البرمجية، ومصدرًا في المتصفح بدل MCP، ومحادثات منفصلة كعمّال محاكاة. ضع علامة «لم يُشغّل» على خطوات الأدوات غير المتاحة. يتطلب المساران اختبارات محلية ومراجعة للملفات. يقدم مفتاح الإجابة أدناه ملفات كاملة لاستعادة العمل. احفظ محاولتك الأولى في الملاحظات قبل نسخ مفتاح الإجابة إلى نسخة استخراج جديدة.

## نقطة التحقق 1: موجز المشروع

**افتح مشروع ورشة العمل الاصطناعي في ChatGPT أو Claude.** اطلب مسودة تذكير من جملتين. تحقق من أن وقتها السابعة مساءً بالرجوع إلى `approved-schedule.md`. الجدول المعتمد يحدد التذكير. ومتطلب المشروع الختامي يحدد البرنامج.

**الدليل:** سجل اسم المشروع، ومراجعة المصدر، والوقت الذي رصدته في المسودة، وأي تصحيح. لا ترسل الرسالة.

## نقطة التحقق 2: سياق المستودع

**افتح المختبر الجديد.** أنشئ ملف `AGENTS.md` موجزًا يشير إلى `docs/capstone-requirements.md` و`task_report.py` والاختبارات وأمر الاختبار الذي تم التحقق منه أثناء الإعداد. إذا استخدمت Claude Code، فاستورد الملف المشترك من `CLAUDE.md`. أنشئ إيداع إعداد ينفذه شخص لهذه ملفات الإرشاد، ثم تأكد أن `git status --short` لا يعرض أي تغييرات. يجب ألا يودع وكيل البرمجة تعديل الميزة.

**الدليل:** احفظ خريطة المستودع ونسخة نظيفة من الإرشادات. سجل مفاتيح JSON وسلوك المدخلات غير الصالحة في المراجعة 1. إذا وصفت محادثة سابقة عامل تصفية الحالة، فاعتبرها سياقًا لمهمة أخرى.

## نقطة التحقق 3: مصدر خارجي

**المسار المتصل:** استخدم [خادم OpenAI Docs MCP للقراءة فقط](https://learn.chatgpt.com/learn/docs-mcp) من خلال عميل مدعوم. اطلب من أداة MCP إرشادات `AGENTS.md` الحالية. سجل اسم الأداة وعنوان المصدر ونقطة واحدة تفيد مختبرك. ثم أزل اتصال التدريب.

**مسار الدراسة:** افتح في المتصفح [الوثائق الرسمية لـ `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md). سجل العنوان والرابط ونقطة مفيدة. ضع علامة «لم يُشغّل» على استكشاف MCP وتنفيذه.

**الدليل:** وجود إدخال لخادم مهيأ لا يثبت تشغيله. يتطلب المسار المتصل استدعاء أداة ظاهرًا ومحتوى مصدرًا مستلمًا.

## نقطة التحقق 4: فوّض مراجعة واحدة

**اطلب من عامل للقراءة فقط** مراجعة `docs/capstone-requirements.md` و`task_report.py` واختبارات الأساس. اطلب تقريرًا لا يتجاوز خمسة أسطر يذكر الفحوص الناقصة ومسارات الملفات. استخدم محادثة منفصلة في مسار الدراسة، وضع عليها علامة عامل محاكاة.

**النتيجة المتوقعة:** تفحص اختبارات البداية الإجمالي وقيمة JSON ليست قائمة. لكنها لا تفحص إخراج JSON، أو قائمة فارغة، أو حالة مفقودة، أو تنسيقًا غير صالح. افتح ملف الاختبارات بنفسك للتحقق من التقرير. تفيد مراجعة مستقلة قصيرة هنا لأن معايير القبول تختلف عن الدرس 5.

**الدليل:** احفظ التقرير الموجز وقرار الدمج في جملة واحدة. احتفظ بنص العامل خارج سجل المهمة الرئيسي.

## نقطة التحقق 5: اطلب التعديل

**أرسل الحزمة التالية إلى وكيل برمجة.** في مسار الدراسة يقترح مساعد المحادثة تصحيحًا تطبقه يدويًا في المختبر.

```text
الهدف: أضف --format text|json بعد مسار JSON.
المصدر: docs/capstone-requirements.md، المراجعة 1.
الملفات المسموح تعديلها: task_report.py وtests/test_task_report.py.
احتفظ بـ: الإخراج الافتراضي Total tasks: 4، وملف tasks.json دون تغيير.
JSON: كائن واحد يحتوي total وأعداد by_status، دون نص إضافي في stdout.
الفحوص المطلوبة: النص الافتراضي والصريح، JSON 4/2/2، قائمة فارغة،
حالة مفقودة، تنسيق غير صالح، واختبارات الأساس.
توقف إذا: تعارضت المصادر، أو فشل اختبار أساس لا يتعلق بالتعديل، أو حدث تعديل خارج النطاق.
التقرير: الملفات المعدلة، والأوامر، والمخرجات الملحوظة، والمشكلة غير المحلولة.
لا تنفذ commit أو push أو نشرًا، ولا ترسل رسالة.
```

**راجع الخطة** قبل التعديل. اختيار المخطط مهم: `total` رقم وليس السلسلة النصية `"4"`. يحتوي `by_status` على كل حالة في الإدخال، حتى يظل التقرير شاملًا عند إضافة حالة مستقبلية. احصر التعديل في المختبر المستخرج.

## نقطة التحقق 6: اختبر وراجع

**نفّذ هذه الفحوص بنفسك.** في Windows استبدل `python3` بـ `py -3`. لا يهم الترتيب الدقيق لمفاتيح JSON أو المسافات. حلل الإخراج بوصفه JSON وقارن أنواع القيم.

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**السلوك المتوقع:** تنجح الاختبارات. يعرض أمري النص `Total tasks: 4`. يعيد أمر JSON كائنًا واحدًا فيه `total` بقيمة 4، و`by_status.open` بقيمة 2، و`by_status.done` بقيمة 2. ينتهي التنسيق غير الصالح برمز غير صفري. تشمل الاختبارات أيضًا إدخالًا فارغًا ومهمة بلا `status` نصي. اقرأ رسالة الخطأ الملحوظة ورمز الخروج لهاتين الحالتين.

| نقطة التحقق | دليل النجاح | الاستعادة عند الفشل |
|---|---|---|
| **موجز المشروع** | التذكير يحدد السابعة مساءً | حدّث مصدر الجدول |
| **خريطة المستودع** | سُجل المتطلب ومسارات الاختبارات | صحح ملفات الإرشاد |
| **مصدر خارجي** | قُرئ مصدر MCP أو سُجل بديل المتصفح | تحقق من الاتصال أو الرابط |
| **مراجعة العامل** | تم التحقق من الاختبارات الناقصة في الملف | صحح تقرير العامل |
| **نطاق الملفات** | البرنامج والاختبارات فقط | افحص كل تعديل غير مطلوب |
| **السلوك** | تم فحص النص وJSON والمدخل الفارغ والأخطاء | شخّص سببًا واحدًا ثم أعد المحاولة |
| **التسليم** | الجلسة الجديدة تعيد بناء الحالة | أضف المصدر أو النتيجة الناقصة |

**استخدم نسخة استخراج جديدة لإعادة ضبط آمنة.** احفظ ملاحظاتك خارج المختبر، واحذف النسخة المستخرجة المؤقتة فقط، ثم أعد استخراج ZIP الأصلي. لا تستخدم إعادة ضبط Git شاملة في مستودع يحتوي عملًا تريد الاحتفاظ به.

## نقطة التحقق 7: سلّم العمل إلى جلسة جديدة

**اكتب تسليمًا يقل عن 180 كلمة** خارج مجلد المختبر. أدرج مراجعة المتطلب، والملفات المعدلة، وأمر الاختبار الدقيق ونتيجته، ومخرجات النص وJSON، وفحوص المدخلات غير الصالحة، وسجل الاستخدام، والإجراء التالي. افتح جلسة جديدة واطلب منها تحديد مفاتيح JSON وتقييم نجاح الميزة.

**الإجابة المتوقعة:** تذكر الجلسة الجديدة `total` و`by_status`، وتشير إلى المراجعة 1، وتورد الفحوص التي لوحظت فقط، وتحدد أي فحص ناقص.

## مفتاح الإجابة ومعايير التقييم

**يوجد أدناه تنفيذ صالح.** احفظ الكتلة الأولى باسم `task_report.py` والثانية باسم `tests/test_task_report.py` في نسخة جديدة من المختبر. اترك `tasks.json` وملفي المتطلبات دون تغيير. نفّذ فحوص نقطة التحقق 6. قارن أي حل آخر بالمتطلب والسلوك الملحوظ.

`task_report.py`:

```python
"""يعرض عددًا نصيًا أو ملخص JSON لمهام ورشة العمل."""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


def load_tasks(path: Path) -> list:
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    for index, task in enumerate(tasks, start=1):
        if not isinstance(task, dict) or not isinstance(task.get("status"), str):
            raise ValueError(f"task {index} needs a string status")
    return tasks


def count_tasks(path: Path) -> int:
    return len(load_tasks(path))


def summarize_tasks(path: Path) -> dict:
    tasks = load_tasks(path)
    counts = Counter()
    for task in tasks:
        counts[task["status"]] += 1
    return {"total": len(tasks), "by_status": dict(sorted(counts.items()))}


def main() -> int:
    parser = argparse.ArgumentParser(description="تقرير مهام ورشة العمل")
    parser.add_argument("path", type=Path, help="مسار قائمة المهام بصيغة JSON")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        if args.format == "json":
            print(json.dumps(summarize_tasks(args.path)))
        else:
            print(f"Total tasks: {count_tasks(args.path)}")
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""فحوص تقارير النص وJSON لمهام ورشة العمل."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from sys import path as module_path

ROOT = Path(__file__).resolve().parents[1]
module_path.insert(0, str(ROOT))
from task_report import count_tasks  # noqa: E402


def run_report(path: Path, *options: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "task_report.py"), str(path), *options],
        capture_output=True, text=True, check=False,
    )


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_default_and_explicit_text(self):
        for options in ((), ("--format", "text")):
            result = run_report(ROOT / "tasks.json", *options)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_json_counts_and_types(self):
        result = run_report(ROOT / "tasks.json", "--format", "json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout), {
            "total": 4, "by_status": {"open": 2, "done": 2},
        })

    def test_empty_list(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "empty.json"
            sample.write_text("[]", encoding="utf-8")
            result = run_report(sample, "--format", "json")
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout), {
                "total": 0, "by_status": {},
            })

    def test_missing_status(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "missing.json"
            sample.write_text('[{"id": 1}]', encoding="utf-8")
            for options in ((), ("--format", "json")):
                result = run_report(sample, *options)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("status", result.stderr)

    def test_invalid_format(self):
        result = run_report(ROOT / "tasks.json", "--format", "invalid")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**أعد الضبط بعد استخدام مفتاح الإجابة:** احفظ ملاحظاتك خارج المختبر، واحذف هذه النسخة المستخرجة، ثم أعد استخراج مختبر البداية الأصلي. تحتوي النسخة الجديدة على اختباري الأساس ولا تحتوي تنفيذ الميزة.

**امنح نقطة عن كل نقطة تحقق** في الجدول أعلاه. تكتمل المسار المتصل بسبع نقاط إذا احتوى صف المصدر الخارجي استدعاء MCP حقيقيًا ووثق صف العامل جلسة حقيقية. ويكتمل مسار الدراسة بسبع نقاط إذا كان المصدر صفحة متصفح تم التحقق منها وكانت خطوات الأدوات موسومة صراحة بأنها لم تُشغّل. يمنع غياب فحص السلوك أو المصدر أو نطاق الملفات اكتمال أي من المسارين.

## تحقق من الفهم

1. **أي متطلب يتحكم في هذه الميزة؟** `docs/capstone-requirements.md`، المراجعة 1. ينتمي المتطلب السابق لعامل تصفية الحالة إلى الدرس 5.
2. **ما الذي يثبت عقد JSON؟** حلل إخراج الأمر، وقارن القيم الرقمية وأعداد كل حالة، واختبر المدخلات الفارغة وغير الصالحة. لا يكفي ملخص وكيل منمق.

## استكشاف الأخطاء وإصلاحها

- **يفشل اختبار الأساس قبل التعديل:** أعد المختبر من ZIP وكرر الإعداد.
- **يعدل الوكيل ملفًا آخر:** راجع diff وأعد التغيير غير المطلوب في المختبر فقط.
- **يفشل اتصال MCP:** استخدم مصدر المتصفح وضع علامة مسار الدراسة على نقطة التحقق.
- **يكرر العامل قيمة خاطئة:** أعد قراءة متطلب المشروع الختامي وصحح التقرير.
- **تنتهي محاولات الإعادة:** احتفظ بسجل الخطأ واطلب من مراجع بشري تحديد الخطوة التالية.

## الخطوات التالية

**احفظ سجل الأدلة المكتمل.** للانتقال إلى النشر المتقدم للفريق والصلاحيات بين الأنظمة، تابع [دورة تنفيذ التعاون بالذكاء الاصطناعي](/ai-collaboration-course-start/).

**التنقل في الدورة:** [السابق المطلوب: الحلقات المحدودة](/articles/effective-ai-bounded-agent-loops/)، [اختياري: تقييم الوكلاء المتخصصين](/articles/effective-ai-specialized-agent-evaluation/)، [مخطط الدورة](/effective-ai-course-start/).

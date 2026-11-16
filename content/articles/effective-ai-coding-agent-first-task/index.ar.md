---
title: "نفّذ أول مهمة لك في مستودع باستخدام وكيل برمجة"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "اختر واجهة لوكيل برمجة، وافتح مستودعًا تجريبيًا، وراجع التغيير المقترح، ثم شغّل الفحوص قبل الاحتفاظ به."
genre: ["الذكاء الاصطناعي", "هندسة البرمجيات"]
tags: ["دليل Codex CLI", "تطبيق Codex", "Claude Code CLI", "دليل OpenCode", "سير عمل وكيل البرمجة", "أدوات البرمجة بالذكاء الاصطناعي"]
cover: "/img/cover/effective-ai-coding-agent-first-task.webp"
coverAlt: "مستودع برمجي يعرض الوكيل في الطرفية وعلى سطح المكتب كلًّا على حدة، بجانب فرق ملف تمت مراجعته"
coverCaption: ""
---

[العودة إلى دورة سير العمل العملي للذكاء الاصطناعي](/effective-ai-course-start/)

**يقرأ وكيل البرمجة الملفات، ويقترح تعديلات، ويشغّل الأدوات داخل مساحة عمل.** في هذا الدرس، ستنفّذ مهمة صغيرة في مستودع. اختر Codex في تطبيق ChatGPT لسطح المكتب أو في CLI، أو Claude Code CLI، أو OpenCode TUI. ثم راجع التغيير قبل قبوله.

**هدف التعلّم:** ستنفّذ تعديلًا محدد النطاق أو تطبّقه يدويًا، ثم تتحقق من الفرق والسلوك.

## أبرز النقاط

- **Codex في تطبيق ChatGPT لسطح المكتب** يوفّر مساحة مرئية للمهام ومراجعتها.
- **Codex CLI** يشغّل جلسة Codex من الطرفية.
- **Claude Code CLI** يشغّل سير عمل Claude للبرمجة من الطرفية.
- **OpenCode TUI** يوفّر سير عمل طرفية مع مزوّدين وأذونات قابلة للضبط.
- **الفرق ونتيجة الاختبار** أهم من رسالة المساعد التي تعلن اكتمال العمل.

## قبل أن تبدأ

**المتطلبات السابقة:** أكمل [إعداد الدورة](/articles/effective-ai-course-setup/)، بما فيه التشغيل الأساسي ولقطة Git المحلية. أكمل [سياق المستودع](/articles/effective-ai-agents-md-context/) و[حزم المهام](/articles/effective-ai-task-packets/) قبل هذا الدرس. استخدم وكيل برمجة لديك إذن بالوصول إليه. خصص 45 دقيقة. يتراوح المستوى من مبتدئ إلى متوسط.

**استخدم [مختبر الدورة التمهيدي](/downloads/effective-ai-course-lab.zip)** داخل مجلد مؤقت. يحتوي الأرشيف على برنامج صغير لتقرير المهام، وبيانات نموذجية، واختبارات. لا تستخدم مستودع إنتاج لأول تعديل لك. أضف عامل التصفية `--status` مع الحفاظ على العدد الإجمالي الحالي.

## مسار الدراسة دون وكيل برمجة

**اطلب من مساعد محادثة اقتراح التغيير نفسه** إذا لم يتوفر وكيل برمجة. الصق فقط `docs/requirements.md` و`task_report.py` وملف الاختبار المحدد من المختبر الاصطناعي. اطلب فرقًا موحدًا وشرحًا موجزًا. يضع الفرق الموحد `-` أمام السطور القديمة و`+` أمام السطور الجديدة. افتح الملف المذكور في محرر نصوص، واستبدل السطور القديمة بالتغيير المقترح، ثم احفظه. بعد ذلك نفّذ كل الأوامر الواردة في قسم مراجعة النتيجة. اترك `tasks.json` كما هو. سجّل أن خطوة وكيل البرمجة لم تُنفّذ. يحتوي المشروع الختامي على وظيفة JSON منفصلة، لذا قارن حل عامل التصفية بمتطلبات الدرس 5 وفحوصه.

## اختر واجهة

**اختر أولًا مساحة المراجعة.** يناسب Codex في تطبيق ChatGPT لسطح المكتب المشاريع المرئية ومراجعة الفروق. تناسب واجهة الطرفية العمل داخل مجلد المختبر المستخرج. قارن بين خيارات الطرفية:

| أداة الطرفية | التحقق من الحساب أو المزوّد | أمر البدء |
|---|---|---|
| **Codex CLI** | تأكد من تسجيل الدخول إلى Codex ومن الأذونات المحلية | `codex` |
| **Claude Code CLI** | تأكد من إمكانية الوصول إلى Claude Code ومن الأذونات المحلية | `claude` |
| **OpenCode TUI** | اضبط مزوّد نماذج مدعومًا والأذونات | `opencode` |

**ثبّت الأداة وسجّل الدخول وفق الدليل الرسمي الحالي.** اقرأ [Codex CLI](https://learn.chatgpt.com/docs/codex/cli)، أو [تطبيق ChatGPT لسطح المكتب](https://learn.chatgpt.com/docs/app)، أو [Claude Code](https://code.claude.com/docs/en/overview)، أو [OpenCode](https://opencode.ai/docs/). تتغير الأوامر والمنصات المدعومة ومتطلبات الحساب. يستخدم هذا الدرس أسماء تشغيل مستقرة وإجراء مراجعة مشتركًا.

**لاختيار المنتج بمزيد من التفصيل،** اقرأ مقارنة [وكلاء البرمجة عبر CLI](/articles/cli-coding-agents-comparison/) أو [وكلاء البرمجة بواجهة رسومية](/articles/gui-coding-agents-comparison/). تقارن أدلة [Codex CLI وسطح المكتب](/articles/codex-cli-vs-desktop/)، و[Claude Code CLI وسطح المكتب](/articles/claude-code-cli-vs-desktop/)، و[OpenCode CLI وسطح المكتب](/articles/opencode-cli-vs-desktop/) واجهات كل منتج.

**ابدأ من مجلد المختبر.** تتطلب كل واجهة اختيار مساحة العمل صراحةً:

1. **Codex لسطح المكتب:** افتح تطبيق ChatGPT لسطح المكتب، واختر المختبر المستخرج كمشروع محلي، ثم ابدأ مهمة محلية فيه. تحقّق من مسار المجلد وطلبات الموافقة قبل أي تعديل. تستخدم المهمة المستضافة نسخة منفصلة من مساحة العمل.
2. **Codex CLI:** نفّذ `cd /path/to/effective-ai-course-lab` ثم `codex`. تأكد من مجلد العمل المعروض ووضع الموافقة.
3. **Claude Code CLI:** نفّذ أمر `cd` نفسه ثم `claude`. تأكد من مجلد المشروع وأذونات الأدوات.
4. **OpenCode TUI:** نفّذ أمر `cd` نفسه ثم `opencode`. تأكد من المزوّد المحدد والمشروع وإعدادات الأذونات.

**يتعامل ChatGPT chat وClaude Projects مع المحادثات والملفات المرجعية المشتركة.** يعمل Codex وClaude Code في مساحة برمجية تحتوي على أدوات للملفات والأوامر. يوفر OpenCode أيضًا واجهات سطح مكتب وIDE، لكن هذا الدرس يستخدم الطرفية. يختلف المزوّد والحساب والتنفيذ المحلي أو المستضاف. سجّل الواجهة التي اخترتها بدل التعامل مع كل الجلسات على أنها عملية واحدة.

**تحقق من خمسة أمور قبل فتح المختبر:** نظام التشغيل المدعوم، والمصادقة، وتكلفة المزوّد أو الحساب، وأذونات الملفات والأوامر، وما إذا كان التنفيذ محليًا أو على مضيف بعيد. سجّل اختيارك. لا تفترض أن تطبيق سطح المكتب وأداة الطرفية يستخدمان مساحة العمل نفسها.

## افحص نقطة البداية

**أعد فتح مجلد المختبر النظيف** من درس سياق المستودع. تحتوي هذه النسخة على ملف `AGENTS.md` المثبّت وملف الإرشادات الاختياري `CLAUDE.md`. راجع الملفات قبل أن تطلب من الوكيل تعديلها. شغّل الاختبارات الأساسية من هذا المجلد.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
```

**النتيجة الأساسية المتوقعة:** يعرض التقرير `Total tasks: 4`. يسمّي تشغيل الاختبارات اختبارين وينتهي بـ `OK`. إذا فشل أي منهما، فتوقف وافحص الملفات المستخرجة. لا تنسب إلى الوكيل إصلاح نقطة بداية معطوبة.

**استخدم لقطات Git المحلية** من إعداد الدورة ودرس سياق المستودع. يجب أن يكون `AGENTS.md` وملف `CLAUDE.md` الاختياري مثبتين بالفعل. نفّذ `git status --short` قبل تعديل الوظيفة وتوقع ألا تظهر ملفات. ويجب ألا ينشئ الوكيل تثبيتًا أيضًا. لا يتضمن الأرشيف سجل Git. ويستثني ملف `.gitignore` ملفات البايت كود الخاصة ببايثون التي تولدها الاختبارات. إذا استخرجت نسخة جديدة، فأعد إعداد الدورة ودرس السياق في ذلك المجلد. ثبّت ملفات الإرشاد قبل تعديل الوظيفة. ابدأ بتهيئة نقطة البداية وتثبيتها:

```bash
git init
git add .
git commit -m "أساس مختبر الدورة"
```

**بعد ذلك أضف `AGENTS.md` و`CLAUDE.md` الاختياري** بالمصدر المعتمد وأمر الاختبار من درس سياق المستودع. ثبّت هذه الملفات، وتأكد من خلو نتيجة `git status --short`، ثم ابدأ تعديل الوظيفة. نفّذ الأوامر في مجلد التدريب المستخرج، لا في جذر مستودع آخر.

## أرسل طلبًا محدد النطاق

**افتح مجلد المختبر** في وكيل البرمجة الذي اخترته. أرسل حزمة المهام التالية:

```text
أضف وسيطة اختيارية باسم --status إلى task_report.py.
القيم المسموح بها: open وdone.
عند غيابها، أبقِ مخرجات العدد الإجمالي الحالية كما هي.
عند وجودها، احسب المهام المطابقة فقط واطبع Total tasks: N.
أضف اختبارات للقيمتين، وقيمة غير صالحة، وبقاء المخرجات الافتراضية كما هي.
لا تغيّر tasks.json أو الملفات غير المرتبطة.
شغّل الاختبارات وأبلغ عن الأمر والنتيجة بدقة.
توقف بعد الشيفرة والاختبارات. لا تنشئ commit ولا تدفع التغييرات.
```

**في Windows،** استبدل `python3` بالأمر `py -3` الذي تحققت منه أثناء الإعداد، بما في ذلك إرشادات المستودع المحفوظة وحزمة المهام.

**اطلب خطة قصيرة قبل التحرير** إذا لم تكن تعرف الشيفرة. اسمح للوكيل بتحرير مجلد المختبر المؤقت فقط. تختلف ضوابط الأذونات من أداة إلى أخرى، لذا افحص الإعدادات الحالية قبل السماح بأوامر shell أو كتابة الملفات.

## راجع النتيجة

**اقرأ الفرق.** تأكد من بقاء المخرجات دون عامل التصفية كما هي، ومن قبول عامل التصفية قيمتين فقط، ومن تغطية الاختبارات للخطأ والمخرجات الافتراضية التي لم تتغير. لا تثبت الاختبارات نجاح التغيير إلا إذا تحققت من السلوك المطلوب.

```bash
git status --short
git diff -- task_report.py tests
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**النتائج المتوقعة:** تعرض أوامر التقرير الثلاثة الأولى الأعداد 4 و2 و2. تعرض القيمة غير الصالحة خطأً واضحًا وتنهي العملية برمز غير صفري. تعتمد صياغة الخطأ الدقيقة على التنفيذ. في macOS أو Linux، نفّذ `echo $?` مباشرة بعد الأمر غير الصالح لقراءة رمز الخروج. وفي PowerShell، افحص `$LASTEXITCODE`.

| الدليل | ما الذي تتحقق منه |
|---|---|
| **قائمة الملفات** | تغيّر البرنامج والاختبارات فقط |
| **الفرق** | منطق عامل التصفية يطابق الطلب |
| **نتيجة الاختبارات** | شُغّلت الحالات الجديدة ونجحت |
| **تشغيل يدوي** | تتطابق أعداد الوضع الافتراضي و`open` و`done` مع `tasks.json` |

**إذا أبلغ الوكيل عن نتيجة دون تشغيل الاختبارات،** فنفّذ الأمر بنفسك. إذا تجاوز التعديل حزمة المهام، فاطلب تصحيحًا محدودًا. وإذا كانت الحالة غير واضحة، فاحذف نسخة التدريب المستخرجة وأعد استخراج ملف ZIP الأصلي.

## إجابات مسار الدراسة

**استخدم هذين الملفين كاملين إذا فشل التصحيح اليدوي.** ابدأ بمختبر مستخرج حديثًا، واحفظ الكتلة الأولى باسم `task_report.py` والثانية باسم `tests/test_task_report.py`، ثم نفّذ أوامر مراجعة النتيجة. اترك `tasks.json` و`docs/requirements.md` كما هما. سجّل الإخفاق الأصلي قبل نسخ الملفات.

`task_report.py`:

```python
"""اطبع عدد المهام من ملف JSON."""

import argparse
import json
import sys
from pathlib import Path


def count_tasks(path: Path, status: str | None = None) -> int:
    """احسب جميع المهام أو المهام ذات الحالة المعتمدة."""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    if status not in (None, "open", "done"):
        raise ValueError("status must be open or done")
    if status is None:
        return len(tasks)
    return sum(1 for task in tasks if task["status"] == status)


def main() -> int:
    parser = argparse.ArgumentParser(description="Count workshop tasks")
    parser.add_argument("path", type=Path, help="path to the JSON task list")
    parser.add_argument("--status", choices=("open", "done"))
    args = parser.parse_args()
    try:
        total = count_tasks(args.path, args.status)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Total tasks: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""فحوص لتقرير مهام الورشة."""

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


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_counts_each_approved_status(self):
        sample = ROOT / "tasks.json"
        self.assertEqual(count_tasks(sample, "open"), 2)
        self.assertEqual(count_tasks(sample, "done"), 2)

    def test_rejects_invalid_status_in_function(self):
        with self.assertRaises(ValueError):
            count_tasks(ROOT / "tasks.json", "pending")

    def test_default_command_stays_unchanged(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json")],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_invalid_command_exits_nonzero(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json"),
             "--status", "invalid"],
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**احتفظ بنسخة معدّلة اجتازت اختبارات عامل التصفية** لدروس السياق والتحقق من النتائج. إذا استعنت بهذا النموذج لاستعادة عملك، فاحتفظ بالنسخة الجديدة والاختبارات الناجحة لتلك الدروس. أبقِ الفرق وسجل الاختبار خارج المختبر. أعد نقطة البداية قبل درس التفويض أو احذف المحاولة الفاشلة للبدء من جديد.

## تدرب وتحقق

**الناتج المطلوب:** فرق المختبر وسجل مراجعة من أربعة أسطر يغطي نطاق الملفات والسلوك الافتراضي وسلوك التصفية والإدخال غير الصالح. سجّل اسم الأداة وإصدارها في ملاحظاتك الخاصة لإعادة إنتاج مشكلة مرتبطة بإصدار محدد.

**الاستدلال المتوقع:** اخترت واجهة تناسب طريقة عملك، وحددت الطلب، وراجعت التعديل الفعلي، وأجريت فحصًا مستقلًا عن تقرير الوكيل.

## اختبر فهمك

1. **السؤال:** ما الدليل على نجاح تعديل عامل تصفية الحالة؟ **الإجابة:** فرق محدود، واختبارات ناجحة، ونتائج مرصودة للوضع الافتراضي وopen وdone والقيمة غير الصالحة.
2. **السؤال:** هل يُعد قول الوكيل إنه شغّل الاختبارات نتيجة اختبارك؟ **الإجابة:** لا. شغّل الأمر أو راجع مخرجات الاختبار.

## استكشاف الأخطاء وإصلاحها

- **الأمر غير موجود:** أكمل التثبيت باتباع دليل المورّد المرتبط، ثم أعد فتح الطرفية.
- **لا يمكن الوصول إلى الملفات:** افتح مجلد المختبر المستخرج وتحقق من أذونات مساحة العمل.
- **تغيرت ملفات غير متوقعة:** توقف وافحص `git status --short` قبل إرسال طلب آخر.
- **نجحت الاختبارات لكن السلوك خاطئ:** أضف حالة يدوية أو اختبارًا للمتطلب الناقص.

## الخطوات التالية

**تابع إلى [نوافذ السياق وتسليم العمل](/articles/effective-ai-context-window-management/)**. ستحتفظ بسجل مفيد لجلسة جديدة.

**التنقل في الدورة:** [السابق: حزم المهام](/articles/effective-ai-task-packets/)، [مخطط الدورة](/effective-ai-course-start/).

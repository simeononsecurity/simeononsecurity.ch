---
title: "Tailscale Aperture: إعداد عملاء الذكاء الاصطناعي للاستدلال وMCP في 2026"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "مرّر طلبات النماذج وأدوات MCP عبر Tailscale Aperture. أعدّ Codex وClaude Code وClaude Desktop وOpenCode وHermes على جهاز أو بوابة أخرى."
genre: ["الذكاء الاصطناعي", "أدوات المطورين", "الشبكات"]
tags: ["Tailscale Aperture", "إعداد Aperture", "وكيل الذكاء الاصطناعي", "بوابة LLM", "بوابة MCP", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "وكيل استدلال الذكاء الاصطناعي", "Responses API", "Anthropic Messages API", "MCP عن بُعد", "Streamable HTTP", "Tailscale", "ذكاء اصطناعي مستضاف ذاتياً", "وكلاء البرمجة", "إعداد عملاء الذكاء الاصطناعي"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "يربط Aperture لوحات العملاء بخدمات النماذج وأدوات MCP عبر مسارين منفصلين، أزرق للاستدلال وأخضر للأدوات"
coverCaption: ""
---

## المقدمة

يوفر Tailscale Aperture لعملاء الذكاء الاصطناعي بوابة واحدة متصلة بشبكة tailnet لاستدلال النماذج وأدوات Model Context Protocol ‏(MCP). يجب أن يستخدم كل عميل مساراً متوافقاً مع بروتوكول API الخاص به. تستخدم أدوات MCP نقطة نهاية منفصلة، وتتحكم منح Aperture في النماذج والموصلات التي يمكن لكل هوية Tailscale الوصول إليها.

يشرح هذا الدليل إعداد Codex وClaude Code وClaude Desktop وOpenCode وHermes على macOS وLinux وWindows. يغطي إعدادات سطر الأوامر وتطبيقات سطح المكتب، ويوضح كيفية العثور على معرّفات النماذج المتاحة لهويتك، ويتضمن مطالبة مجهّلة لإعادة استخدامها عند إعداد جهاز أو نسخة Aperture أخرى.

**اختيار المسار:** تعتمد مسارات نقاط النهاية على البوابة وبروتوكول API لكل عميل. لا يخدم مسار Responses مثل `/codex` حركة Anthropic Messages أو MCP. تحقّق من اسم مضيف البوابة ومسار الاستدلال لكل عميل. اعثر على معرّفات النماذج عبر وصولك الخاص إلى Aperture قبل تغيير إعدادات العملاء.

## أهم النقاط

- **حركة النماذج** تحتاج إلى مسار API الخاص ببروتوكول العميل.
- **حركة MCP** تستخدم نقطة النهاية المنفصلة `/v1/mcp`.
- **أذونات البوابة** يجب أن تسمح لهوية Tailscale باستخدام كل نموذج وموصل.
- **إعداد العميل** يثبت حفظ الإعدادات فقط. تحقّق من طلب فعلي واستدعاء أداة MCP.

## كيف تتوافق المسارات

| الغرض | طلب العميل | مسار Aperture | الخدمة التي يقدمها المسار |
|---|---|---|---|
| Codex والنماذج المتوافقة مع Responses | OpenAI Responses API | عادةً `/v1`. يعتمد المسار المخصص مثل `/codex` على النشر. | استدلال النماذج |
| استدلال نماذج Claude | Anthropic Messages API | عنوان البوابة الأساسي. يعالج Aperture المسار `/v1/messages` | استدلال متوافق مع Claude |
| أدوات MCP | Streamable HTTP MCP | `/v1/mcp` | أدوات وموارد الموصلات المُعدة |

{{< figure src="aperture-client-routes.webp" alt="يستخدم Codex وHermes مسار Responses، ويستخدم Claude مسار Anthropic Messages، وتستخدم عملاء MCP المسار المنفصل /v1/mcp للوصول إلى موصلات Aperture" caption="يستخدم استدلال النماذج وحركة MCP نقطتي نهاية منفصلتين في Aperture" >}}

**جذور المزوّدين:** يضيف Aperture مسارات طلبات العملاء إلى عنوان URL الأساسي للمزوّد. اجعل `baseurl` يشير إلى جذر API الخاص بالمزوّد. لا تضف `/v1` إلى عنوان upstream الأساسي إذا كان المسار الوارد يتضمنه بالفعل. راجع [مرجع إعداد Aperture](https://tailscale.com/docs/aperture/configuration) لمعرفة بناء عناوين URL وتسجيل النماذج والمنح.

## تحضير البوابة

**قبل التحرير،** اطلب من مسؤول Aperture القيم التالية:

- **اسم مضيف البوابة:** استخدم `http://` لمعظم العملاء المتصلة بشبكة tailnet. يتطلب استدلال Claude Desktop عنوان `https://` وشهادة موثوقة.
- **مسارات الاستدلال:** تستخدم OpenAI Responses وAnthropic Messages تنسيقات طلب مختلفة.
- **معرّفات النماذج:** استخدم نقطة النهاية أدناه لمعرفة النماذج المتاحة لهوية Tailscale. استخدم المعرّفات الحرفية التي تُعاد لتلك الهوية.
- **المصادقة:** تحقّق مما إذا كان العميل يرسل مفتاح API مؤقتاً أو بيانات اعتماد مستخدم.
- **نقطة نهاية MCP:** عادةً `http://<APERTURE_HOST>/v1/mcp` لعملاء tailnet. يتطلب استدلال Claude Desktop HTTPS وشهادة موثوقة.
- **منح الوصول:** تحقّق من أذونات النماذج والموصلات لهويتك في Tailscale.

**الوصول إلى الشبكة:** يجب أن يتمكن جهاز العميل من الوصول إلى البوابة عبر tailnet. لا يمنح اسم المضيف وحده وصولاً للنماذج أو الأدوات. يرفض Aperture الوصول ما لم يسمح منح مطابق بالنموذج أو الموصل.

### العثور على النماذج المتاحة لحسابك

**استعلم عن قائمة النماذج** من جهاز متصل بشبكة tailnet نفسها. يستخدم Aperture هوية Tailscale للجهاز ويعيد النماذج الممنوحة لذلك المستخدم، كما يشرح [دليل منح الوصول إلى النماذج](https://tailscale.com/docs/aperture/how-to/grant-model-access):

```sh
# macOS أو Linux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShell، استخدم curl.exe لتجنب الاسم المستعار القديم curl
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**قراءة النتيجة:** استخدم كل قيمة `id` مُعادة كمعرّف للنموذج. افحص `metadata.provider.id` لتحديد مزوّد Aperture. اختر نموذجاً يدعم تنسيق API للعميل. يحتاج Claude Desktop مثلاً إلى نموذج Anthropic Messages. يعرض [دليل النماذج](https://tailscale.com/docs/aperture/reference/chat) في Aperture أيضاً المعرّفات المتاحة للمستخدم الذي سجّل الدخول.

**نماذج مفقودة:** إذا لم يظهر نموذج متوقع، فاطلب من مسؤول Aperture التحقق من إعداد المزوّد ومنح النموذج لك. لا تسمح نقطة النهاية للمستخدمين بمنح أنفسهم وصولاً.

**مخطط عنوان URL:** توصي Tailscale باستخدام `http://` لمعظم العملاء المتصلة بشبكة tailnet نفسها. يشفر WireGuard هذه الحركة. يحتاج Claude Desktop إلى `https://` وشهادة يثق بها نظام التشغيل. استخدم المخطط الموضح لكل عميل أدناه.

### إضافة مزوّد للاستدلال

**OpenAI Responses:** أضف المزوّد upstream إلى Aperture وفعّل تنسيق API الذي يستخدمه العميل. لمزوّد OpenAI، أضف مقطعاً مثل الآتي:

```json
{
  "providers": {
    "openai": {
      "baseurl": "https://api.openai.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "models": ["<MODEL_ID>"],
      "compatibility": {
        "openai_chat": true,
        "openai_responses": true
      }
    }
  }
}
```

**Anthropic Messages:** استخدم جذر API الخاص بـ Anthropic وتنسيق التفويض `x-api-key` والتوافق `anthropic_messages`. يجب أن يظهر معرّف النموذج أيضاً في قائمة `models` للمزوّد. أضف مثلاً:

```json
{
  "providers": {
    "anthropic": {
      "baseurl": "https://api.anthropic.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "authorization": "x-api-key",
      "models": ["<CLAUDE_MODEL_ID>"],
      "compatibility": {
        "anthropic_messages": true
      }
    }
  }
}
```

**تغييرات الإعداد:** استبدل كل عنصر نائب بقيم المزوّد upstream. أضف المقاطع إلى إعداد Aperture الحالي وحافظ على بقية الملف. فعّل علامات التوافق لواجهات API التي يدعمها المزوّد.

**منح الوصول:** يتحكم Aperture في وصول كل مستخدم إلى كل نموذج أو موصل. امنح مستخدمي Tailscale المستهدفين الأذونات اللازمة فقط. يمنح المثال التالي مستخدماً واحداً وصولاً إلى نموذج وموصل:

```json
{
  "grants": [
    {
      "src": ["<TAILSCALE_USER>"],
      "app": {
        "tailscale.com/cap/aperture": [
          {"role": "user", "models": "openai/<MODEL_ID>"},
          {"connectors": ["teamtools/**"]}
        ]
      }
    }
  ]
}
```

**منح النموذج:** استخدم معرّف المزوّد ومعرّف النموذج في نمط المنح. يشرح [دليل إعداد الموصلات](https://tailscale.com/docs/aperture/connectors/get-started) الإعداد الحالي `connectors.servers`. إعداد `mcp.servers` القديم على المستوى الأعلى مهمل.

### إضافة موصل MCP

**موصل MCP:** يتصل Aperture بخوادم MCP upstream ويعرض الأدوات عبر `/v1/mcp`:

```json
{
  "connectors": {
    "servers": {
      "teamtools": {
        "protocol": "mcp",
        "url": "<UPSTREAM_MCP_ENDPOINT>"
      }
    }
  }
}
```

**عنوان URL للموصل:** استخدم نقطة نهاية MCP الكاملة للخادم upstream. ثم امنح مستخدم Tailscale حق الوصول إلى `teamtools/**` أو إلى نمط أدوات أضيق. يشرح [مرجع وكيل MCP](https://tailscale.com/docs/aperture/mcp-server) نقطة نهاية العميل الواحدة وسلوك الموصلات.

## Codex CLI وتطبيق سطح المكتب

**إعدادات مشتركة:** يستخدم Codex CLI وتطبيق سطح المكتب الإعداد نفسه. حرر `~/.codex/config.toml` في macOS وLinux. وفي Windows حرر `%USERPROFILE%\.codex\config.toml` (تقبل الصدفة التي توسع مجلد المنزل أيضاً `~/.codex/config.toml`). يذكر [عرض تطبيق Codex](https://openai.com/index/introducing-the-codex-app/) أن التطبيق يستخدم إعداد Codex CLI. توجد إعدادات المستخدم في `~/.codex/config.toml`. تشرح [أساسيات الإعداد](https://learn.chatgpt.com/docs/config-file/config-basic) حقول المزوّد وMCP على مستوى المستخدم. أضف المزوّد إلى هذا الملف، ثم أعد تشغيل التطبيق وتحقق من ظهوره مع النموذج.

```toml
model = "<MODEL_ID>"
model_provider = "aperture"

[model_providers.aperture]
name = "Aperture Proxy"
base_url = "http://<APERTURE_HOST>/v1"
wire_api = "responses"
requires_openai_auth = true
supports_websockets = false
```

**حقول اختيارية:** تتوافق هاتان القيمتان مع إعداد واحد لمزوّد Codex. احتفظ بهما فقط إذا احتاجهما إعداد البوابة وCodex. يحذف [دليل Tailscale الحالي لـ Codex Aperture](https://tailscale.com/docs/aperture/how-to/use-codex) هذين الحقلين، ويستخدم `wire_api = "responses"`، ويوضح أن Aperture يضيف بيانات اعتماد upstream. استخدم عنوان Responses المحدد من مسؤول البوابة. المسار `/codex` خاص بالنشر. المسار الافتراضي في وثائق Tailscale هو `/v1`.

**إعداد MCP:** أضف الخادم إلى إعداد المستخدم نفسه:

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**التحقق من Codex:** نفّذ `codex mcp list`، ثم ابدأ جلسة جديدة وافحص `/mcp`. تثبت قائمة الخوادم التسجيل. ويثبت ظهور أداة ونجاح استدعائها اكتشافها وتشغيلها. يوثق [مرجع إعداد Codex](https://learn.chatgpt.com/docs/config-file/config-reference) إعدادات المزوّد وMCP.

## Claude Code CLI

**البروتوكول:** يستخدم Claude Code بروتوكول Anthropic Messages. وجّه ملف إعداداته العام إلى بوابة Aperture المتوافقة مع Anthropic. استخدم `~/.claude/settings.json` في macOS وLinux، أو `%USERPROFILE%\.claude\settings.json` في Windows. وفي PowerShell استخدم `$HOME\.claude\settings.json`. يجب أن يخدم المسار `/v1/messages`. يستخدم Codex Responses بروتوكولاً ومساراً مختلفين. توصي Tailscale باستخدام HTTP لـ Claude Code على tailnet لأن WireGuard يشفر الاتصال.

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**مصادقة العميل:** يستخدم دليل Aperture عنصراً نائباً في `apiKeyHelper` لأن Aperture يضيف بيانات اعتماد upstream. لتمرير اشتراك Claude، يجب أن يعيد مزوّد Anthropic في Aperture بيانات اعتماد Claude للمستخدم. عندها اترك `ANTHROPIC_API_KEY` و`ANTHROPIC_AUTH_TOKEN` دون ضبط، فهما يستبدلان بيانات الاشتراك. اتبع [تعليمات Claude Code مع Aperture](https://tailscale.com/docs/aperture/how-to/use-claude-code) المناسبة لإصدارك، وراجع [دليل Anthropic للبوابات](https://code.claude.com/docs/en/llm-gateway-connect) لخيارات المصادقة.

**MCP عبر HTTP:** أضف نقطة النهاية بالأوامر التالية:

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**التحقق من Claude Code:** ابدأ جلسة ونفّذ `/mcp` لتأكيد الاتصال. توصي Anthropic في [وثائق MCP](https://code.claude.com/docs/en/mcp) باستخدام HTTP لخوادم MCP البعيدة.

## واجهة Claude Desktop

**إعداد منفصل:** يحتوي Claude Desktop على شاشة لاستدلال الجهات الخارجية. يوجّه هذا الخيار طلبات نماذج Claude Desktop عبر Aperture. إعداد MCP خطوة منفصلة.

1. في Claude Desktop لنظامي macOS أو Windows، اختر **Help > Troubleshooting > Enable Developer Mode** (المساعدة > استكشاف الأخطاء وإصلاحها > تفعيل وضع المطور). في نسخة Linux التجريبية استخدم القائمة نفسها إن وُجدت، وأعد تشغيل التطبيق إذا طُلب ذلك. إذا لم تظهر القائمة، حدّث التطبيق وراجع ملاحظات إصدار النظام.
2. اختر **Developer > Configure Third-Party Inference** (المطور > إعداد الاستدلال من جهة خارجية).
3. عيّن **Connection type** (نوع الاتصال) إلى **Gateway** (بوابة) و**Credential kind** (نوع بيانات الاعتماد) إلى **Static API key** (مفتاح API ثابت).
4. أدخل `https://<APERTURE_HOST>` في **Gateway base URL** (عنوان URL الأساسي للبوابة). استخدم اسم المضيف الكامل الذي تغطيه شهادة TLS موثوقة.
5. أدخل قيمة غير فارغة مثل `aperture` كمفتاح للبوابة. يتجاهل Aperture هذه القيمة ويصادق عبر tailnet.
6. اترك ترويسات الاستدلال المخصصة فارغة.
7. أضف نموذجاً مفعّلاً باستخدام المعرّف الدقيق الذي يعيده `GET /v1/models` لهوية Tailscale. اختر نموذج Anthropic Messages، وأدخل معرّفه واسمه المعروض والاسم المستعار الاختياري يدوياً. لا يكتشف Claude Desktop النماذج في هذه الشاشة.
8. اختر **Save Changes** (حفظ التغييرات) ثم **Apply Changes** (تطبيق التغييرات). أغلق Claude Desktop وافتحه مجدداً.

**التحقق من البروتوكول:** يذكر [دليل Aperture لـ Claude Desktop](https://tailscale.com/docs/aperture/how-to/use-claude-desktop) أن Claude Desktop يستخدم Anthropic Messages عبر `/v1/messages`. لا تستخدم مسار Codex `/codex` ولا نوع اتصال متوافقاً مع OpenAI.

### توصيل Claude Desktop بـ MCP

**وصول MCP الخاص:** شغّل جسراً محلياً من نوع stdio على جهاز Claude Desktop نفسه. أضف التالي إلى إعداد MCP المحلي:

```json
{
  "mcpServers": {
    "aperture": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "http://<APERTURE_HOST>/v1/mcp"]
    }
  }
}
```

**عمل الجسر:** يصل البرنامج المحلي إلى Aperture عبر اتصال Tailscale للجهاز. استخدم مسار إعداد النظام: macOS، `~/Library/Application Support/Claude/claude_desktop_config.json`؛ Windows، `%APPDATA%\Claude\claude_desktop_config.json`؛ Linux التجريبي، افتح **Settings > Developer > Edit Config** واستخدم المسار الذي يفتحه Claude Desktop. يختلف مسار Linux حسب الحزمة. أعد تشغيل Claude Desktop، وافحص الموصلات ثم نفّذ استدعاء أداة غير ضار. يوثق [مشروع `mcp-remote`](https://github.com/punkpeye/mcp-remote) هذا الجسر المحلي إلى البعيد.

**الموصلات البعيدة:** يحتاج مسار Anthropic في Settings > Connectors إلى خادم بعيد يمكن لخدمة Anthropic الوصول إليه. اسم المضيف المتاح عبر tailnet فقط خاص بأجهزتك، لذا استخدم الجسر المحلي للنقطة الخاصة. إذا نشرت خدمة MCP عامة، فأعدّ المصادقة والأذونات قبل إضافتها كموصل سحابي. راجع [دليل Anthropic للموصلات البعيدة](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp).

## OpenCode CLI وتطبيق سطح المكتب

**إعدادات مشتركة:** يقرأ OpenCode CLI وتطبيق سطح المكتب إعداد OpenCode نفسه. يستخدم توثيق OpenCode V2 الحالي خريطة `providers` للمزوّدين المخصصين ويضع خوادم MCP ضمن `mcp.servers`. يستخدم المثال نقطة دردشة متوافقة مع OpenAI على `/v1`. تحقّق من دعم OpenAI Chat Completions في مزوّد Aperture قبل استخدام مسار النموذج هذا.

**الإعداد العام:** حرر `~/.config/opencode/opencode.json` في macOS وLinux. وفي Windows استخدم `%USERPROFILE%\.config\opencode\opencode.json`. أضف مزوّداً متوافقاً مع OpenAI واستبدل `<MODEL_ID>` بالمعرّف الدقيق لنموذج Aperture. يقبل OpenCode أيضاً `opencode.jsonc` للتعليقات. يشرح [مرجع الإعداد](https://opencode.ai/docs/config/) أولوية إعدادات المشروع والعامة.

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "model": "aperture/<MODEL_ID>",
  "providers": {
    "aperture": {
      "env": ["APERTURE_API_KEY"],
      "package": "@opencode/ai/providers/openai-compatible",
      "settings": {
        "baseURL": "http://<APERTURE_HOST>/v1"
      },
      "models": {
        "<MODEL_ID>": { "modelID": "<MODEL_ID>" }
      }
    }
  },
  "mcp": {
    "servers": {
      "aperture": {
        "type": "remote",
        "url": "http://<APERTURE_HOST>/v1/mcp",
        "oauth": false
      }
    }
  }
}
```

**مصادقة العميل:** يتجاوز `oauth: false` تدفق OAuth الافتراضي في OpenCode. يتعرف Aperture على المستدعي عبر Tailscale. يحتاج OpenCode أيضاً إلى إدخال مصادقة للمزوّد، لذا عيّن `APERTURE_API_KEY=-` في البيئة المحلية. يجب أن يتلقى تطبيق سطح المكتب المتغير أيضاً. إذا لم يرث بيئة الصدفة، فنفّذ `/connect` في التطبيق وأدخل `-` لـ Aperture. لا تضع مفتاح المزوّد upstream في هذا الملف. يشرح [دليل المزوّدين](https://opencode.ai/docs/providers/) و[دليل MCP](https://opencode.ai/docs/mcp-servers/) التنسيق الحالي. نفّذ `opencode mcp list` للتحقق من الخادم، واستخدم `/mcps` داخل التطبيق لمراجعة حالته.

## Hermes CLI وتطبيق سطح المكتب

**إعدادات مشتركة:** يخزّن Hermes Agent المزوّدين المسماة وخوادم MCP في `~/.hermes/config.yaml` على macOS وLinux. تستخدم تثبيتات Windows الأصلية `%LOCALAPPDATA%\hermes\config.yaml`. نفّذ `hermes config path` لمعرفة الملف الفعلي. قد يغيّر `HERMES_HOME` المسار الافتراضي. يستخدم Hermes Desktop المحلي مجلد Hermes والملف الشخصي نفسيهما مثل CLI. إذا اتصل Desktop ببوابة Hermes بعيدة، فأعدّ Aperture على الجهاز الذي يشغّل Hermes وتحقق من وصوله إلى tailnet. راجع [دليل Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop).

**مزوّد Responses:** أضف مزوّداً مسمى. يجب أن تطابق قيمة `api` نقطة Responses في نسخة Aperture:

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # أضف key_env فقط إذا تطلب إعداد Aperture مفتاحاً للعميل.
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**اختيار البروتوكول:** لـ OpenAI Chat Completions عيّن `transport: chat_completions`. ولـ Anthropic Messages اختر `transport: anthropic_messages` واستخدم عنوان بوابة Anthropic Messages. يشرح [دليل المزوّدين](https://hermes-agent.nousresearch.com/docs/integrations/providers) الحالي حقول `api` و`transport` و`default_model`.

**إعداد MCP:** أضف Aperture MCP إلى ملف YAML نفسه:

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**التحقق من Hermes:** نفّذ `hermes mcp` وافحص الاتصالات في قائمة الخوادم التفاعلية. يستخدم Desktop المحلي ملف الإعداد نفسه. يوثق Hermes [خوادم MCP HTTP البعيدة](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) و[مرجع إعداد MCP الكامل](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference).

## التحقق من المسارين

**نفّذ فحوصات منفصلة** لاستدلال النماذج وMCP:

1. تحقّق من اتصال Tailscale ووصول الجهاز إلى البوابة. وفي Claude Desktop تأكد من تقديم شهادة TLS موثوقة.
2. أرسل مطالبة قصيرة من كل عميل مُعد. تأكد من ظهور طلب مطابق في قائمة جلسات Aperture.
3. تأكد من أن معرّف النموذج المختار يطابق نموذجاً ممنوحاً لهويتك.
4. افتح شاشة حالة MCP أو قائمة الخوادم في كل عميل. تحقّق من اتصال Aperture وظهور الأدوات المطلوبة.
5. استدعِ أداة للقراءة فقط، وقارن المحتوى بالمصدر upstream.
6. إذا فشل استدعاء النموذج أو الأداة، راجع سجلات Aperture. لا يثبت حفظ الإعداد نجاح الطلب.

| العَرَض | الفحص |
|---|---|
| يعيد طلب النموذج 404 أو 405 | تأكد من المسار والبروتوكول الصحيحين. لا تستخدم `/codex` مع Anthropic Messages أو MCP. |
| النموذج غير متاح | استعلم عن `/v1/models` بهوية مستخدم Tailscale المقصودة. افحص المعرّف الدقيق وتوافق تنسيق API. اطلب من مسؤول التحقق من المزوّد أو المنح الناقصة. |
| الطلب غير مصرح به | تحقّق مما إذا كان العميل يحتاج عنصراً نائباً أو رمز الحامل أو تمرير اشتراك. لا تنسخ مفتاح مزوّد upstream إلى ملف مشروع عام. |
| يظهر خادم MCP بلا أدوات | افحص `/v1/mcp` وحالة الموصل ومنحه ومسار الشبكة من العميل إلى Aperture. |
| تعذّر على Claude Desktop الاتصال بعنوان MCP خاص | شغّل جسراً محلياً مثل `mcp-remote` أو استخدم موصلاً عاماً معتمداً ومصادقة مناسبة. |

## إعادة الإعداد على جهاز آخر

**جهاز جديد:** ثبّت العميل نفسه وصِل الجهاز إلى tailnet أولاً. استعلم عن `/v1/models` من الجهاز الجديد لمعرفة النماذج الممنوحة لهويته. أعد استخدام بنية الإعداد واحتفظ ببيانات الاعتماد محلياً. استبدل `<APERTURE_HOST>` و`<MODEL_ID>` و`<UPSTREAM_MCP_ENDPOINT>` بقيم نسخة Aperture المستهدفة. استخدم نقطة نهاية مستقلة لكل بروتوكول API واضبط `/v1/mcp` لحركة الأدوات. أخيراً تحقّق من طلب نموذج واستدعاء أداة MCP.

**بوابات متعددة:** استخدم إعداداً منفصلاً لكل نسخة Aperture. يحتاج الجهاز إلى نقطة Responses لـ Codex وHermes، ونقطة Anthropic Messages لـ Claude، ونقطة تجميع MCP للأدوات. خزّن مفاتيح API في مخزن الأسرار المحلي للعميل أو في متغير بيئة. لا تنسخ المفاتيح إلى `config.toml` أو `opencode.json` أو `config.yaml` مشتركة أو مستودع عام.

## مطالبة قابلة لإعادة الاستخدام لإعداد Aperture

**انسخ هذه المطالبة المجهّلة** إلى مساعد البرمجة. استبدل العناصر النائبة بتفاصيل البوابة. يجب أن يستعلم المساعد عن Aperture بهويتك في Tailscale قبل اختيار معرّفات النماذج.

```text
أعدّ بوابة Tailscale Aperture الحالية وعملاء الذكاء الاصطناعي المثبّتين على هذا الجهاز.

العملاء المعنيون: Codex CLI وسطح المكتب، Claude Code، Claude Desktop، OpenCode CLI وسطح المكتب، Hermes CLI وسطح المكتب.

أولاً حدّد ما إذا كان الجهاز يعمل بـ macOS أو Linux أو Windows، واكتشف الصدفة النشطة مثل zsh أو bash أو PowerShell. استخدم مسارات وأوامر النظام المحدد باستمرار. افحص البوابة الحالية واتصال Tailscale وإصدارات العملاء وإعداداتهم الموجودة. اقرأ الوثائق الرسمية الحالية. احتفظ بالإعدادات غير المتعلقة بالمهمة وخذ نسخة احتياطية من كل ملف قبل تعديله. لا تخمّن أسماء المضيفين أو معرّفات النماذج أو مسارات API أو بيانات الاعتماد. احتفظ بمفاتيح المزوّد upstream في Aperture، لا في ملفات العملاء أو هذا المستودع.

اكتشف النماذج المتاحة من هذا الجهاز المتصل بـ Tailscale:
1. استعلم عن `http://<APERTURE_HOST>/v1/models` بهوية Tailscale التي يستخدمها العملاء. استخدم عنوان القائمة المخصص الموثق إن اختلف.
2. اقرأ `id` و`metadata.provider.id` لكل نموذج. تعكس القائمة النماذج الممنوحة لهويتي. لا تستبدلها بقائمة المسؤول ولا تخترع معرّفات.
3. طابق توافق API مع كل عميل. يستخدم Codex ‏OpenAI Responses، وتستخدم عملاء Claude ‏Anthropic Messages. يحتاج OpenCode وHermes إلى مزوّد ونقل متوافقين.
4. أبقِ النموذج الافتراضي الحالي متى أمكن. إذا احتاج العميل نموذجاً افتراضياً ولم أحدد تفضيلاً، اعرض النماذج المتوافقة واسألني. يتطلب Claude Desktop إدخال المعرّف الدقيق يدوياً.
5. إذا لم تُرجع نقطة النهاية نموذجاً مناسباً، افحص إعداد المزوّد والمنح فقط إذا كان لدي وصول إداري. وإلا فأبلغني بنوع وصول النموذج الذي يجب أن يمنحه المسؤول. لا تمنح نفسك وصولاً.

اعثر على نشر Aperture ومصدر إعداده. لا تفترض مساراً ولا تستبدل الملف كله. يتطلب OpenAI Responses ‏`openai_responses`، ويتطلب Anthropic ‏`anthropic_messages`. توضع موصلات MCP في الإعداد الحالي `connectors.servers`، وتتصل العملاء عبر `/v1/mcp`.

قبل تغيير بوابة مشتركة، جهّز أصغر فرق ممكن للمزوّدين والموصلات والمنح. طبّقه فقط إذا كنت أملك الصلاحية الإدارية وهذا الطلب يسمح بتغيير البوابة. وإلا فأبلغ مالك النسخة بالتغييرات الدقيقة المقترحة. لا تنشئ منحاً ولا توسعها بلا إذن صريح من المالك. حافظ على جميع إعدادات البوابة الحالية.

أعدّ كل عميل مثبت بالتنسيق الرسمي الحالي والمسار المناسب للنظام:
- يشترك Codex CLI وسطح المكتب في `~/.codex/config.toml` على macOS/Linux و`%USERPROFILE%\.codex\config.toml` على Windows. اضبط مزوّد Aperture والنموذج المتوافق و`wire_api = "responses"` وMCP في `mcp_servers`.
- يستخدم Claude Code المتغير `ANTHROPIC_BASE_URL` وMCP البعيد عبر HTTP. استخدم `~/.claude/settings.json` على macOS/Linux و`%USERPROFILE%\.claude\settings.json` على Windows.
- يستخدم Claude Desktop وضع المطور وإعداد استدلال الجهات الخارجية ونوع Gateway ومفتاح API ثابتاً وعنوان HTTPS بشهادة موثوقة ومعرّف نموذج وجدته لمستخدمي. استخدم جسراً محلياً `mcp-remote` لوصول MCP الخاص. ابحث عن إعداد MCP في Settings > Developer > Edit Config إن توفر، وإلا فاستخدم المسار الموثق للنظام.
- يستخدم OpenCode مخطط V2 الحالي `providers` و`mcp.servers`. يوجد الملف العام في `~/.config/opencode/opencode.json` على macOS/Linux و`%USERPROFILE%\.config\opencode\opencode.json` على Windows. عيّن `oauth: false` لـ MCP في Aperture واستخدم مفتاحاً مؤقتاً محلياً عند الحاجة.
- يستخدم Hermes مزوّداً مسمى ونقلاً يناسب API النموذج و`mcp_servers`. استخدم `~/.hermes/config.yaml` على macOS/Linux. وعلى Windows تحقّق من `hermes config path`، وغالباً `%LOCALAPPDATA%\hermes\config.yaml`. تحقّق مما إذا كان Hermes Desktop يشارك الملف الشخصي المحلي.

استخدم HTTP لحركة tailnet حيث يدعم العميل ذلك. يتطلب استدلال Claude Desktop HTTPS بشهادة موثوقة. استخدم `/v1` ما لم توثق البوابة مساراً آخر.

أعد تشغيل العملاء. تحقّق في Aperture من طلب نموذج واحد لكل عميل ومن استدعاء أداة MCP للقراءة فقط. أبلغ عن النماذج المتاحة لهويتي والعملاء والملفات المعدلة ونتائج التحقق وأي إجراء إداري متبقٍ. لا تثبت برامج، ولا تكشف البوابة للعامة، ولا تنفذ commit أو تنشر.
```

## الخلاصة

يعتمد إعداد Aperture العامل على بوابة يمكن الوصول إليها، ومسار نموذج يطابق بروتوكول العميل، ومنح للنماذج والموصلات المطلوبة. تعمل أنماط الإعداد نفسها على macOS وLinux وWindows، لكن لكل عميل موقع خاص بنظام التشغيل لحفظ الإعدادات.

استعلم عن معرّفات النماذج بهوية Tailscale التي ستستخدمها. أعدّ استدلال النماذج و`/v1/mcp` بشكل منفصل، ثم تحقّق من طلب فعلي واستدعاء أداة للقراءة فقط. عند الانتقال إلى جهاز أو نسخة Aperture أخرى، أعد استخدام بنية هذا الدليل وتحقق من المسارات والمنح هناك، واحتفظ ببيانات الاعتماد في مخزن أسرار محلي.

## الخطوات التالية

**تطبيق MCP:** للتعرّف على الفرق بين خادم محفوظ واستدعاء أداة تم التحقق منه، اقرأ [إعداد خادم MCP: الأذونات واختبار الأدوات والإزالة الآمنة](/articles/effective-ai-mcp-server-setup/). ولمعرفة البنية الأوسع للاستضافة الذاتية، راجع [أسطول وكلاء الذكاء الاصطناعي الهجين: Tailscale وLiteLLM وHermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/).

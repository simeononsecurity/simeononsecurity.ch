---
title: "Tailscale Aperture: ২০২৬ সালে ইনফারেন্স ও MCP-এর জন্য AI ক্লায়েন্ট কনফিগার করুন"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Tailscale Aperture দিয়ে মডেল অনুরোধ ও MCP টুল রুট করুন। অন্য ডিভাইস বা গেটওয়েতে Codex, Claude Code, Claude Desktop, OpenCode এবং Hermes সেট আপ করুন।"
genre: ["কৃত্রিম বুদ্ধিমত্তা", "ডেভেলপার টুল", "নেটওয়ার্কিং"]
tags: ["Tailscale Aperture", "Aperture সেটআপ", "AI প্রক্সি", "LLM গেটওয়ে", "MCP গেটওয়ে", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "AI ইনফারেন্স প্রক্সি", "Responses API", "Anthropic Messages API", "রিমোট MCP", "Streamable HTTP", "Tailscale", "স্ব-হোস্ট করা AI", "কোডিং এজেন্ট", "AI ক্লায়েন্ট কনফিগারেশন"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "Aperture আলাদা নীল ইনফারেন্স রুট ও সবুজ টুল রুট দিয়ে ক্লায়েন্ট প্যানেলকে মডেল এবং MCP টুল পরিষেবার সঙ্গে যুক্ত করে"
coverCaption: ""
---

## ভূমিকা

Tailscale Aperture মডেল ইনফারেন্স এবং মডেল Context প্রোটোকল (MCP) টুলের জন্য AI ক্লায়েন্টকে tailnet-সংযুক্ত একটি গেটওয়ে দেয়। প্রতিটি ক্লায়েন্টকে তার API প্রোটোকলের সঙ্গে মেলে এমন রুট ব্যবহার করতে হবে। MCP টুল আলাদা ঠিকানা ব্যবহার করে, আর Aperture-এর অনুমতি নির্ধারণ করে প্রতিটি Tailscale পরিচয় কোন মডেল ও সংযোগকারী ব্যবহার করতে পারবে।

এই নির্দেশিকায় macOS, Linux এবং Windows-এ Codex, Claude Code, Claude Desktop, OpenCode ও Hermes সেটআপ করা হয়েছে। এতে CLI ও ডেস্কটপ সেটিংস আছে, নিজের পরিচয়ের জন্য উপলভ্য মডেল ID খোঁজার পদ্ধতি আছে, এবং অন্য ডিভাইস বা Aperture সংস্করণ কনফিগার করতে পুনর্ব্যবহারের জন্য একটি পরিচয়মুক্ত প্রম্পট আছে।

**রুট নির্বাচন:** ঠিকানা পথ আপনার গেটওয়ে ও প্রতিটি API প্রোটোকলের ওপর নির্ভর করে। `/codex`-এর মতো Responses রুট Anthropic Messages বা MCP ট্র্যাফিক পরিবেশন করে না। gateway-এর hostname এবং প্রতিটি ক্লায়েন্টের ইনফারেন্স পথ যাচাই করুন। ক্লায়েন্ট সেটিংস বদলানোর আগে নিজের Aperture প্রবেশাধিকার দিয়ে মডেল ID খুঁজুন।

## মূল বিষয়

- **মডেল ট্র্যাফিকের** জন্য ক্লায়েন্ট প্রোটোকলের উপযুক্ত API পথ দরকার।
- **MCP ট্র্যাফিক** আলাদা `/v1/mcp` ঠিকানা ব্যবহার করে।
- **গেটওয়ে অনুমতি** আপনার Tailscale পরিচয়কে প্রতিটি মডেল ও সংযোগকারী ব্যবহারের অনুমতি দেবে।
- **ক্লায়েন্ট কনফিগারেশন** শুধু সেটিংস সংরক্ষণের প্রমাণ। বাস্তব অনুরোধ ও MCP টুল কল যাচাই করুন।

## রুটগুলো যেভাবে কাজ করে

| উদ্দেশ্য | ক্লায়েন্ট অনুরোধ | Aperture পথ | রুটের কাজ |
|---|---|---|---|
| Codex ও Responses-সামঞ্জস্যপূর্ণ মডেল | OpenAI Responses API | সাধারণত `/v1`। `/codex`-এর মতো কাস্টম পথ deployment-নির্ভর। | মডেল ইনফারেন্স |
| Claude মডেল ইনফারেন্স | Anthropic Messages API | গেটওয়ে মূল URL। Aperture `/v1/messages` সামলায় | Claude-সামঞ্জস্যপূর্ণ ইনফারেন্স |
| MCP টুল | Streamable HTTP MCP | `/v1/mcp` | কনফিগার করা connector-এর টুল ও resource |

{{< figure src="aperture-client-routes.webp" alt="Codex ও Hermes Responses পথ ব্যবহার করে, Claude Anthropic Messages ব্যবহার করে, আর MCP ক্লায়েন্ট আলাদা /v1/mcp পথ দিয়ে Aperture connector-এ পৌঁছায়" caption="মডেল ইনফারেন্স ও MCP ট্র্যাফিক আলাদা Aperture ঠিকানা ব্যবহার করে" >}}

**সরবরাহকারী root:** Aperture ক্লায়েন্টের অনুরোধ পথ সরবরাহকারী মূল URL-এর সঙ্গে যোগ করে। Provider-এর `baseurl` তার API মূল ঠিকানা-এ সেট করুন। ইনকামিং path-এ `/v1` থাকলে উর্ধ্ববর্তী মূল URL-এ আর `/v1` যোগ করবেন না। URL গঠন, মডেল নিবন্ধন ও অনুমতি সম্পর্কে [Aperture বিন্যাস reference](https://tailscale.com/docs/aperture/configuration) দেখুন।

## গেটওয়ে প্রস্তুত করুন

**সম্পাদনার আগে** Aperture administrator-এর কাছে এই মানগুলো চান:

- **গেটওয়ে hostname:** tailnet-সংযুক্ত অধিকাংশ ক্লায়েন্টে `http://` ব্যবহার করুন। Claude Desktop inference-এর জন্য বিশ্বাসযোগ্য certificate-সহ `https://` দরকার।
- **ইনফারেন্স পথ:** OpenAI Responses ও Anthropic Messages ভিন্ন অনুরোধ বিন্যাস ব্যবহার করে।
- **মডেল ID:** নিচের ঠিকানা দিয়ে আপনার Tailscale পরিচয়ের জন্য উপলভ্য মডেল দেখুন। ওই পরিচয়ের জন্য ফেরত আসা হুবহু ID ব্যবহার করুন।
- **প্রমাণীকরণ:** ক্লায়েন্ট অস্থায়ী মান API চাবি পাঠায়, না ব্যবহারকারীর প্রমাণীকরণ তথ্য পাঠায়, যাচাই করুন।
- **MCP ঠিকানা:** tailnet ক্লায়েন্টে সাধারণত `http://<APERTURE_HOST>/v1/mcp`। Claude Desktop inference-এর জন্য বিশ্বাসযোগ্য certificate-সহ HTTPS দরকার।
- **প্রবেশাধিকার অনুমতি:** আপনার Tailscale পরিচয়ের মডেল ও সংযোগকারী অনুমতি যাচাই করুন।

**নেটওয়ার্ক অ্যাক্সেস:** ক্লায়েন্ট ডিভাইসকে tailnet দিয়ে gateway-এ পৌঁছাতে হবে। শুধু hostname জানলে মডেল বা টুল ব্যবহারের অনুমতি মেলে না। মডেল বা connector-এর জন্য মিলে যাওয়া অনুমতি না থাকলে Aperture অ্যাক্সেস প্রত্যাখ্যান করে।

### আপনার ব্যবহারকারীর জন্য উপলভ্য মডেল খুঁজুন

**একই tailnet-এ যুক্ত ডিভাইস থেকে মডেল তালিকা জিজ্ঞাসা করুন।** Aperture ডিভাইসের Tailscale পরিচয় ব্যবহার করে এবং ওই ব্যবহারকারীকে দেওয়া মডেল ফেরত দেয়। [মডেল অনুমতি নির্দেশিকা](https://tailscale.com/docs/aperture/how-to/grant-model-access) দেখুন:

```sh
# macOS বা Linux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShell-এ পুরোনো curl alias এড়াতে curl.exe ব্যবহার করুন
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**ফলাফল পড়ুন:** ফেরত আসা প্রতিটি `id` মডেল ID হিসেবে ব্যবহার করুন। Aperture সরবরাহকারী শনাক্ত করতে `metadata.provider.id` দেখুন। ক্লায়েন্টের API বিন্যাস সমর্থন করে এমন মডেল বাছুন। যেমন, Claude Desktop-এর Anthropic Messages মডেল দরকার। Aperture-এর [Models directory](https://tailscale.com/docs/aperture/reference/chat)-তেও সাইন-ইন করা ব্যবহারকারীর উপলভ্য মডেল ID আছে।

**মডেল অনুপস্থিত:** প্রত্যাশিত মডেল না দেখালে Aperture administrator-কে সরবরাহকারী বিন্যাস ও আপনার মডেল অনুমতি পরীক্ষা করতে বলুন। এই ঠিকানা দিয়ে ব্যবহারকারী নিজেকে প্রবেশাধিকার দিতে পারে না।

**URL রীতি:** একই tailnet-এ থাকা অধিকাংশ ক্লায়েন্টে Tailscale `http://` সুপারিশ করে। WireGuard এই ট্র্যাফিক এনক্রিপ্ট করে। Claude Desktop-এর জন্য `https://` এবং অপারেটিং সিস্টেমের বিশ্বাসযোগ্য সনদ দরকার। প্রতিটি ক্লায়েন্টের জন্য নিচে দেওয়া scheme ব্যবহার করুন।

### ইনফারেন্স সরবরাহকারী যোগ করুন

**OpenAI Responses:** Aperture-এ উর্ধ্ববর্তী সরবরাহকারী যোগ করুন এবং ক্লায়েন্টের ব্যবহৃত API বিন্যাস চালু করুন। OpenAI upstream-এর জন্য এমন একটি অংশ যোগ করুন:

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

**Anthropic Messages:** Anthropic API মূল ঠিকানা, `x-api-key` authorization বিন্যাস এবং `anthropic_messages` সামঞ্জস্য ব্যবহার করুন। মডেল ID provider-এর `models` তালিকাতেও থাকতে হবে। এ ধরনের অংশ যোগ করুন:

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

**বিন্যাস পরিবর্তন:** প্রতিটি অস্থায়ী মান উর্ধ্ববর্তী value দিয়ে বদলান। বর্তমান Aperture configuration-এ অংশগুলো যোগ করুন এবং ফাইলের বাকি অংশ অক্ষত রাখুন। সরবরাহকারী যে API সমর্থন করে তার সামঞ্জস্য flag চালু করুন।

**প্রবেশাধিকার অনুমতি:** প্রতিটি মডেল ও connector-এ ব্যবহারকারীর প্রবেশ Aperture নিয়ন্ত্রণ করে। প্রতিটি লক্ষ্য Tailscale ব্যবহারকারীকে কেবল প্রয়োজনীয় অনুমতি দিন। এই উদাহরণে একজন ব্যবহারকারী একটি সরবরাহকারী মডেল ও একটি সংযোগকারী ব্যবহার করতে পারে:

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

**মডেল অনুমতি:** অনুমতি pattern-এ সরবরাহকারী ID ও মডেল ID ব্যবহার করুন। [সংযোগকারী সেটআপ guide](https://tailscale.com/docs/aperture/connectors/get-started)-এ বর্তমান `connectors.servers` বিন্যাস আছে। পুরোনো top-level `mcp.servers` বিন্যাস বাতিল হয়েছে।

### MCP সংযোগকারী যোগ করুন

**MCP সংযোগকারী:** Aperture উর্ধ্ববর্তী MCP সার্ভার-এ সংযোগ করে এবং `/v1/mcp`-তে টুল প্রকাশ করে:

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

**সংযোগকারী URL:** উর্ধ্ববর্তী server-এর সম্পূর্ণ MCP ঠিকানা ব্যবহার করুন। এরপর আপনার Tailscale ব্যবহারকারীকে `teamtools/**` বা আরও সীমিত সরঞ্জাম pattern-এ প্রবেশাধিকার দিন। [MCP মধ্যস্থতাকারী reference](https://tailscale.com/docs/aperture/mcp-server) একক ক্লায়েন্ট ঠিকানা ও connector-এর আচরণ ব্যাখ্যা করে।

## Codex CLI ও ডেস্কটপ

**একই সেটিংস:** Codex CLI ও ডেস্কটপ অ্যাপ একই বিন্যাস ব্যবহার করে। macOS ও Linux-এ `~/.codex/config.toml` সম্পাদনা করুন। Windows-এ `%USERPROFILE%\.codex\config.toml` সম্পাদনা করুন (মূল ফোল্ডার ডিরেক্টরি প্রসারিত করা shell-এ `~/.codex/config.toml`-ও চলে)। [Codex অ্যাপ পরিচিতি](https://openai.com/index/introducing-the-codex-app/) অনুযায়ী ডেস্কটপ অ্যাপ Codex CLI বিন্যাস পড়ে। Codex ব্যবহারকারী setting `~/.codex/config.toml`-এ থাকে। [বিন্যাস basics](https://learn.chatgpt.com/docs/config-file/config-basic)-এ user-level সরবরাহকারী ও MCP field ব্যাখ্যা করা হয়েছে। ফাইলে সরবরাহকারী যোগ করে অ্যাপ পুনরায় চালু করুন, তারপর UI-তে সরবরাহকারী ও মডেল দেখা যাচ্ছে কি না নিশ্চিত করুন।

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

**ঐচ্ছিক field:** এই দুটি value একটি Codex সরবরাহকারী setup-এর সঙ্গে মেলে। গেটওয়ে ও Codex বিন্যাস চাইলে তবেই রাখুন। Tailscale-এর বর্তমান [Codex Aperture নির্দেশিকা](https://tailscale.com/docs/aperture/how-to/use-codex) এগুলো বাদ দেয়, `wire_api = "responses"` ব্যবহার করে এবং বলে Aperture উর্ধ্ববর্তী প্রমাণীকরণ তথ্য যোগ করে। গেটওয়ে administrator-এর দেওয়া নির্দিষ্ট Responses URL ব্যবহার করুন। `/codex` deployment-নির্ভর পথ। Tailscale-এর নথিভুক্ত ডিফল্ট পথ `/v1`।

**MCP বিন্যাস:** একই user configuration-এ সার্ভার যোগ করুন:

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**Codex যাচাই:** `codex mcp list` চালান, নতুন session শুরু করুন এবং `/mcp` দেখুন। সার্ভার তালিকা নিবন্ধনের প্রমাণ। তালিকাভুক্ত সরঞ্জাম এবং সফল call আবিষ্কার ও execution প্রমাণ করে। [Codex বিন্যাস reference](https://learn.chatgpt.com/docs/config-file/config-reference)-এ user-level সরবরাহকারী ও MCP setting আছে।

## Claude Code CLI

**প্রোটোকল:** Claude Code Anthropic Messages ব্যবহার করে। Global Claude Code সেটিংস file-কে Anthropic-সামঞ্জস্যপূর্ণ Aperture gateway-এ নির্দেশ করুন। macOS ও Linux-এ `~/.claude/settings.json`, Windows-এ `%USERPROFILE%\.claude\settings.json` ব্যবহার করুন। PowerShell-এ `$HOME\.claude\settings.json` ব্যবহার করুন। Route-কে `/v1/messages` পরিবেশন করতে হবে। Codex Responses অন্য প্রোটোকল ও পথ ব্যবহার করে। WireGuard সংযোগ এনক্রিপ্ট করে বলে Tailscale tailnet-এ Claude Code-এর জন্য HTTP সুপারিশ করে।

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**ক্লায়েন্ট প্রমাণীকরণ:** Aperture ক্লায়েন্ট guide-এ `apiKeyHelper`-এ অস্থায়ী মান আছে, কারণ Aperture উর্ধ্ববর্তী প্রমাণীকরণ তথ্য যোগ করে। Claude সদস্যতা passthrough-এর জন্য Aperture Anthropic provider-কে ব্যবহারকারীর Claude প্রমাণীকরণ তথ্য forward করতে হবে। সে ক্ষেত্রে `ANTHROPIC_API_KEY` ও `ANTHROPIC_AUTH_TOKEN` সেট করবেন না। এই variable-গুলো সদস্যতা credential-কে প্রতিস্থাপন করে। আপনার Claude Code version-এর [Claude Code Aperture নির্দেশনা](https://tailscale.com/docs/aperture/how-to/use-claude-code) এবং প্রমাণীকরণ বিকল্পের জন্য [Anthropic গেটওয়ে guide](https://code.claude.com/docs/en/llm-gateway-connect) অনুসরণ করুন।

**HTTP-তে MCP:** এভাবে ঠিকানা যোগ করুন:

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**Claude Code যাচাই:** Session শুরু করে `/mcp` চালান। Anthropic-এর [MCP নথি](https://code.claude.com/docs/en/mcp) দূরবর্তী MCP সার্ভার-এর জন্য HTTP সুপারিশ করে।

## Claude Desktop GUI

**আলাদা সেটিংস:** Claude Desktop-এ third-party ইনফারেন্স পর্দা আছে। এই সেটিং Claude Desktop মডেল অনুরোধ Aperture দিয়ে পাঠায়। MCP বিন্যাস আলাদা ধাপ।

1. macOS বা Windows-এর Claude Desktop-এ **Help > Troubleshooting > Enable Developer Mode** নির্বাচন করুন। Linux পরীক্ষামূলক সংস্করণ-তে থাকলে একই menu ব্যবহার করুন। অনুরোধ করলে অ্যাপ পুনরায় চালু করুন। Menu না থাকলে Claude Desktop update করে platform-specific সংস্করণ note দেখুন।
2. **Developer > Configure Third-Party Inference** (ডেভেলপার > তৃতীয় পক্ষের ইনফারেন্স কনফিগার করুন) নির্বাচন করুন।
3. **Connection type** (সংযোগের ধরন) হিসেবে **Gateway** (গেটওয়ে) এবং **Credential kind** (প্রমাণীকরণের ধরন) হিসেবে **Static API key** (স্থির API key) দিন।
4. **Gateway base URL** (গেটওয়ের মূল URL) হিসেবে `https://<APERTURE_HOST>` লিখুন। বিশ্বস্ত TLS certificate-এ থাকা সম্পূর্ণ hostname ব্যবহার করুন।
5. গেটওয়ে চাবি হিসেবে `aperture`-এর মতো non-empty অস্থায়ী মান দিন। Aperture অস্থায়ী মান উপেক্ষা করে tailnet দিয়ে প্রমাণীকরণ করে।
6. Custom inference header (কাস্টম ইনফারেন্স হেডার) ফাঁকা রাখুন।
7. আপনার Tailscale পরিচয়ের `GET /v1/models` থেকে ফেরত আসা সঠিক ID দিয়ে সক্রিয় মডেল যোগ করুন। Anthropic Messages মডেল বাছুন। ID, প্রদর্শিত name ও ঐচ্ছিক tier উপনাম হাতে লিখুন। এই screen-এ Claude Desktop মডেল খোঁজে না।
8. **Save Changes** (পরিবর্তন সংরক্ষণ করুন), তারপর **Apply Changes** (পরিবর্তন প্রয়োগ করুন) নির্বাচন করুন। Claude Desktop বন্ধ করে আবার খুলুন।

**প্রোটোকল যাচাই:** [Aperture Claude ডেস্কটপ নির্দেশিকা](https://tailscale.com/docs/aperture/how-to/use-claude-desktop) বলছে Claude Desktop `/v1/messages`-এ Anthropic Messages ব্যবহার করে। Codex পথ `/codex` দেবেন না বা OpenAI-compatible সংযোগ type বাছবেন না।

### Claude Desktop-কে MCP-তে সংযুক্ত করুন

**ব্যক্তিগত MCP প্রবেশাধিকার:** Claude Desktop যে কম্পিউটারে চলে, সেখানেই স্থানীয় stdio সেতু চালান। Claude Desktop-এর স্থানীয় MCP configuration-এ এটি যোগ করুন:

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

**Bridge কীভাবে কাজ করে:** স্থানীয় process কম্পিউটারের Tailscale সংযোগ দিয়ে Aperture-এ পৌঁছায়। OS অনুযায়ী পথ ব্যবহার করুন: macOS, `~/Library/Application Support/Claude/claude_desktop_config.json`; Windows, `%APPDATA%\Claude\claude_desktop_config.json`; Linux পরীক্ষামূলক সংস্করণ, **সেটিংস > Developer > Edit বিন্যাস** খুলে Claude Desktop যে পথ দেখায় তা ব্যবহার করুন। Linux পথ package-ভেদে আলাদা। Claude Desktop restart করুন, সংযোগকারী তালিকা দেখুন এবং একটি নিরাপদ সরঞ্জাম call করুন। [`mcp-remote` project](https://github.com/punkpeye/mcp-remote) স্থানীয়-থেকে-দূরবর্তী সেতু নথিভুক্ত করেছে।

**দূরবর্তী সংযোগকারী:** Anthropic-এর সেটিংস > Connectors ব্যবহারে Anthropic service থেকে পৌঁছানো যায় এমন দূরবর্তী সার্ভার দরকার। শুধু tailnet-এ থাকা hostname আপনার ডিভাইসেই সীমিত, তাই ব্যক্তিগত endpoint-এর জন্য স্থানীয় bridge ব্যবহার করুন। সর্বজনীন MCP সেবা প্রকাশ করলে cloud সংযোগকারী হিসেবে যোগের আগে প্রমাণীকরণ ও permission সেট করুন। Anthropic-এর [দূরবর্তী MCP সংযোগকারী guide](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) দেখুন।

## OpenCode CLI ও ডেস্কটপ

**একই সেটিংস:** OpenCode CLI ও desktop একই OpenCode বিন্যাস পড়ে। বর্তমান OpenCode V2 documentation-এ custom provider-এর জন্য `providers` map এবং MCP সার্ভার-এর জন্য `mcp.servers` আছে। এই উদাহরণ `/v1`-এ OpenAI-সামঞ্জস্যপূর্ণ আলাপ ঠিকানা ব্যবহার করে। এই মডেল পথ ব্যবহারের আগে Aperture সরবরাহকারী OpenAI Chat Completions সমর্থন করে কি না যাচাই করুন।

**Global বিন্যাস:** macOS ও Linux-এ `~/.config/opencode/opencode.json` সম্পাদনা করুন। Windows-এ `%USERPROFILE%\.config\opencode\opencode.json` ব্যবহার করুন। OpenAI-compatible সরবরাহকারী যোগ করে `<MODEL_ID>`-কে সঠিক Aperture মডেল ID দিয়ে বদলান। Comment-এর জন্য OpenCode একই directory-তে `opencode.jsonc`-ও গ্রহণ করে। [বিন্যাস reference](https://opencode.ai/docs/config/) global ও project setting-এর অগ্রাধিকার ব্যাখ্যা করে।

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

**ক্লায়েন্ট প্রমাণীকরণ:** `oauth: false` OpenCode-এর ডিফল্ট OAuth প্রবাহ বাদ দেয়। Aperture Tailscale দিয়ে caller শনাক্ত করে। OpenCode-এর সরবরাহকারী auth entry-ও দরকার, তাই স্থানীয় environment-এ `APERTURE_API_KEY=-` সেট করুন। Desktop app-কেও চলক দিন। Shell পরিবেশ না পেলে app-এ `/connect` চালিয়ে Aperture-এর জন্য `-` দিন। এই file-এ উর্ধ্ববর্তী সরবরাহকারী চাবি রাখবেন না। OpenCode-এর [সরবরাহকারী guide](https://opencode.ai/docs/providers/) এবং [MCP নির্দেশিকা](https://opencode.ai/docs/mcp-servers/) বর্তমান বিন্যাস ব্যাখ্যা করে। সার্ভার যাচাই করতে `opencode mcp list` চালান এবং app-এ অবস্থা দেখতে `/mcps` ব্যবহার করুন।

## Hermes CLI ও ডেস্কটপ

**একই সেটিংস:** Hermes Agent macOS ও Linux-এ `~/.hermes/config.yaml`-এ নামযুক্ত সরবরাহকারী ও MCP সার্ভার রাখে। Windows native install ব্যবহার করে `%LOCALAPPDATA%\hermes\config.yaml`। সক্রিয় file দেখতে `hermes config path` চালান। `HERMES_HOME` ডিফল্ট location বদলাতে পারে। স্থানীয় Hermes Desktop CLI-এর একই Hermes মূল ফোল্ডার ও প্রোফাইল ব্যবহার করে। Desktop যদি দূরবর্তী Hermes gateway-এ যুক্ত হয়, Hermes যে মেশিনে চলে সেখানে Aperture configure করুন এবং সার্ভার tailnet-এ পৌঁছায় কি না যাচাই করুন। স্থানীয় ও দূরবর্তী setup-এর জন্য [Hermes ডেস্কটপ নির্দেশিকা](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) দেখুন।

**Responses সরবরাহকারী:** নামযুক্ত সরবরাহকারী যোগ করুন। `api` মান Aperture সংস্করণ-এর Responses endpoint-এর সঙ্গে মিলতে হবে:

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # Aperture setup-এ client key লাগলেই key_env যোগ করুন।
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**প্রোটোকল নির্বাচন:** OpenAI Chat Completions-এর জন্য `transport: chat_completions` দিন। Anthropic Messages-এর জন্য `transport: anthropic_messages` বেছে Anthropic Messages গেটওয়ে URL ব্যবহার করুন। বর্তমান [সরবরাহকারী guide](https://hermes-agent.nousresearch.com/docs/integrations/providers)-এ Hermes নামযুক্ত provider-এর `api`, `transport` ও `default_model` field আছে।

**MCP বিন্যাস:** একই YAML file-এ Aperture MCP যোগ করুন:

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**Hermes যাচাই:** `hermes mcp` চালিয়ে ইন্টারেক্টিভ সার্ভার picker-এ প্রতিটি সংযোগ দেখুন। স্থানীয় Desktop একই প্রোফাইল ব্যবহার করে। Hermes-এর [দূরবর্তী HTTP MCP সার্ভার](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) ও [সম্পূর্ণ MCP বিন্যাস reference](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference) দেখুন।

## উভয় পথ যাচাই করুন

**মডেল ইনফারেন্স ও MCP আলাদাভাবে পরীক্ষা করুন:**

1. ডিভাইসের Tailscale সংযোগ ও gateway-এ পৌঁছানো যাচাই করুন। Claude Desktop-এর ক্ষেত্রে গেটওয়ে বিশ্বাসযোগ্য TLS সনদ দেয় কি না দেখুন।
2. কনফিগার করা প্রতিটি ক্লায়েন্ট দিয়ে ছোট প্রম্পট পাঠান। Aperture session list-এ সংশ্লিষ্ট অনুরোধ দেখা যাচ্ছে কি না নিশ্চিত করুন।
3. নির্বাচিত মডেল ID আপনার Tailscale পরিচয়কে দেওয়া মডেলের সঙ্গে মেলে কি না যাচাই করুন।
4. প্রতিটি client-এর MCP অবস্থা পর্দা বা তালিকা কমান্ড খুলুন। Aperture সার্ভার যুক্ত এবং প্রত্যাশিত সরঞ্জাম প্রকাশ করছে কি না দেখুন।
5. একটি শুধু-পঠন সরঞ্জাম call করুন। ফেরত আসা content উর্ধ্ববর্তী source-এর সঙ্গে মিলিয়ে নিন।
6. মডেল বা সরঞ্জাম call ব্যর্থ হলে Aperture log দেখুন। সংরক্ষিত বিন্যাস সফল request-এর প্রমাণ নয়।

| সমস্যা | পরীক্ষা |
|---|---|
| মডেল অনুরোধ 404 বা 405 দেয় | ক্লায়েন্ট ঠিকানা সঠিক পথ ও প্রোটোকল ব্যবহার করছে কি না দেখুন। Anthropic Messages বা MCP-এর জন্য `/codex` ব্যবহার করবেন না। |
| মডেল অনুপলভ্য | লক্ষ্য Tailscale ব্যবহারকারী হিসেবে `/v1/models` জিজ্ঞাসা করুন। সঠিক ID দেখা যায় ও API বিন্যাস মেলে কি না যাচাই করুন। সরবরাহকারী entry বা অনুমতি অনুপস্থিত কি না administrator-কে দেখতে বলুন। |
| অনুরোধ অনুমোদিত নয় | ক্লায়েন্ট অস্থায়ী মান, বেয়ারার টোকেন, না সদস্যতা সরাসরি পাঠানো চায় তা যাচাই করুন। উর্ধ্ববর্তী সরবরাহকারী চাবি সর্বজনীন project file-এ কপি করবেন না। |
| MCP সার্ভার তালিকায় আছে, কিন্তু সরঞ্জাম দেখা যায় না | `/v1/mcp`, সংযোগকারী ਸুਸਥਤਾ, সংযোগকারী অনুমতি এবং ক্লায়েন্ট থেকে Aperture-এ নেটওয়ার্ক পথ পরীক্ষা করুন। |
| Claude Desktop ব্যক্তিগত MCP URL-এ যুক্ত হতে পারে না | `mcp-remote`-এর মতো স্থানীয় bridge চালান অথবা উপযুক্ত authentication-সহ অনুমোদিত সর্বজনীন সংযোগকারী ব্যবহার করুন। |

## অন্য ডিভাইসে সেটআপ পুনরায় তৈরি করুন

**নতুন ডিভাইস:** একই ক্লায়েন্ট install করে আগে ডিভাইসটিকে tailnet-এ যুক্ত করুন। নতুন ডিভাইস থেকে `/v1/models` জিজ্ঞাসা করে তার Tailscale পরিচয়ের মডেল খুঁজুন। Configuration-এর কাঠামো নিন, প্রমাণীকরণ তথ্য স্থানীয়ভাবে রাখুন। `<APERTURE_HOST>`, `<MODEL_ID>` এবং `<UPSTREAM_MCP_ENDPOINT>` লক্ষ্য Aperture সংস্করণ-এর মান দিয়ে বদলান। প্রতিটি API protocol-এর জন্য আলাদা ঠিকানা রাখুন, তারপর সরঞ্জাম traffic-এর জন্য `/v1/mcp` সেট করুন। শেষে একটি মডেল অনুরোধ ও একটি MCP সরঞ্জাম call যাচাই করুন।

**একাধিক গেটওয়ে:** প্রতিটি Aperture সংস্করণ-এর জন্য আলাদা বিন্যাস ব্যবহার করুন। Codex ও Hermes-এর জন্য Responses ঠিকানা, Claude-এর জন্য Anthropic Messages ঠিকানা এবং tool-এর জন্য MCP সমন্বয় ঠিকানা লাগবে। API প্রমাণীকরণ তথ্য ক্লায়েন্টের স্থানীয় গোপন store বা পরিবেশ variable-এ রাখুন। Shared `config.toml`, `opencode.json`, `config.yaml` বা সর্বজনীন repository-তে API চাবি কপি করবেন না।

## পুনর্ব্যবহারযোগ্য Aperture সেটআপ প্রম্পট

**এই পরিচয়মুক্ত prompt-টি** আপনার coding assistant-এ কপি করুন। Placeholder-গুলো গেটওয়ে details দিয়ে বদলান। মডেল ID বাছার আগে assistant-কে আপনার Tailscale পরিচয় হিসেবে Aperture query করতে হবে।

```text
এই ডিভাইসে থাকা আমার বিদ্যমান Tailscale Aperture গেটওয়ে এবং AI ক্লায়েন্ট কনফিগার করুন।

ক্লায়েন্টের পরিধি: Codex CLI ও desktop, Claude Code, Claude Desktop, OpenCode CLI ও desktop, Hermes CLI ও desktop।

প্রথমে ডিভাইসে macOS, Linux, না Windows আছে শনাক্ত করুন; সক্রিয় shell (যেমন zsh, bash বা PowerShell) চিহ্নিত করুন; এবং সব সময় সেই platform-এর পথ ও কমান্ড রীতি ব্যবহার করুন। বর্তমান গেটওয়ে, Tailscale সংযোগ, ক্লায়েন্ট version ও বিদ্যমান ক্লায়েন্ট setting আগে পরীক্ষা করুন। বর্তমান official নথি পড়ুন। সম্পর্কহীন বিন্যাস অক্ষত রাখুন এবং প্রতিটি file edit করার আগে backup নিন। Hostname, মডেল ID, API পথ বা প্রমাণীকরণ তথ্য অনুমান করবেন না। ঊর্ধ্ববর্তী সরবরাহকারী চাবি Aperture-এ রাখুন, ক্লায়েন্ট file বা এই repository-তে নয়।

এই Tailscale-সংযুক্ত ডিভাইস থেকে উপলভ্য মডেল খুঁজুন:
1. আমার client-এর Tailscale পরিচয় দিয়ে `http://<APERTURE_HOST>/v1/models` query করুন। গেটওয়ে অন্য নিজস্ব মডেল-তালিকা URL নথিভুক্ত করলে সেটি ব্যবহার করুন।
2. প্রতিটি model-এর `id` ও `metadata.provider.id` পড়ুন। এই তালিকা আমার পরিচয়কে দেওয়া মডেল দেখায়। Administrator-এর তালিকা দিয়ে এটি বদলাবেন না বা ID বানাবেন না।
3. প্রতিটি client-এর সঙ্গে মডেল API সামঞ্জস্য মেলান। Codex OpenAI Responses ব্যবহার করে। Claude ক্লায়েন্ট Anthropic Messages ব্যবহার করে। OpenCode ও Hermes-এর জন্য সামঞ্জস্যপূর্ণ সরবরাহকারী ও transport কনফিগার করতে হয়।
4. সম্ভব হলে client-এর বিদ্যমান ডিফল্ট মডেল রাখুন। কোনো client-এর ডিফল্ট দরকার হলে এবং আমার পছন্দ না থাকলে সামঞ্জস্যপূর্ণ মডেল দেখিয়ে আমাকে বেছে নিতে বলুন। Claude Desktop-এ সঠিক মডেল ID হাতে লিখতে হয়।
5. ঠিকানা উপযুক্ত মডেল না দিলে কেবল আমার প্রশাসক প্রবেশাধিকার থাকলে সরবরাহকারী ও অনুমতি setting পরীক্ষা করুন। তা না হলে administrator-কে কোন মডেল প্রবেশাধিকার যোগ করতে হবে জানান। নিজেকে প্রবেশাধিকার দেবেন না।

Aperture স্থাপন ও configuration-এর উৎস খুঁজুন। File পথ অনুমান করবেন না বা পুরো বিন্যাস বদলাবেন না। OpenAI Responses-এর জন্য `openai_responses` এবং Anthropic client-এর জন্য `anthropic_messages` দরকার। MCP সংযোগকারী বর্তমান `connectors.servers` configuration-এ থাকে, ক্লায়েন্ট `/v1/mcp` দিয়ে যুক্ত হয়।

Shared গেটওয়ে বদলানোর আগে সরবরাহকারী, সংযোগকারী ও grant-এর সর্বনিম্ন diff তৈরি করুন। কেবল আমি প্রশাসক হলে এবং এই অনুরোধ গেটওয়ে পরিবর্তনের অনুমতি দিলে সেটি প্রয়োগ করুন। অনুমতি না থাকলে instance owner-কে নির্দিষ্ট প্রস্তাব জানান। Owner-এর স্পষ্ট অনুমতি ছাড়া অনুমতি তৈরি বা বিস্তৃত করবেন না। Gateway-এর বিদ্যমান setting অক্ষত রাখুন।

ইনস্টল করা প্রতিটি client-এর বর্তমান official বিন্যাস ও OS পথ ব্যবহার করুন:
- Codex CLI ও desktop macOS/Linux-এ `~/.codex/config.toml` এবং Windows-এ `%USERPROFILE%\.codex\config.toml` ভাগ করে। Aperture সরবরাহকারী, সামঞ্জস্যপূর্ণ মডেল, `wire_api = "responses"` এবং `mcp_servers`-এ MCP সেট করুন।
- Claude Code `ANTHROPIC_BASE_URL` ও HTTP দূরবর্তী MCP ব্যবহার করে। macOS/Linux-এ `~/.claude/settings.json`, Windows-এ `%USERPROFILE%\.claude\settings.json` ব্যবহার করুন।
- Claude Desktop-এ Developer Mode, Configure Third-Party Inference (তৃতীয় পক্ষের ইনফারেন্স কনফিগার করুন), গেটওয়ে, Static API চাবি, trusted certificate-সহ HTTPS URL এবং আমার user-এর জন্য পাওয়া মডেল ID ব্যবহার করুন। ব্যক্তিগত tailnet MCP-এর জন্য স্থানীয় `mcp-remote` bridge ব্যবহার করুন। MCP configuration-এর জন্য সেটিংস > Developer > Edit বিন্যাস দেখুন, না থাকলে শনাক্ত OS-এর নথিভুক্ত পথ ব্যবহার করুন।
- OpenCode বর্তমান V2 `providers` schema ও `mcp.servers` ব্যবহার করে। Global বিন্যাস macOS/Linux-এ `~/.config/opencode/opencode.json`, Windows-এ `%USERPROFILE%\.config\opencode\opencode.json`। Aperture MCP-এর জন্য `oauth: false` দিন। প্রয়োজনে স্থানীয় অস্থায়ী মান API চাবি ব্যবহার করুন।
- Hermes নামযুক্ত সরবরাহকারী, মডেল API-র উপযুক্ত transport এবং `mcp_servers` ব্যবহার করে। macOS/Linux-এ `~/.hermes/config.yaml` ব্যবহার করুন। Windows-এ `hermes config path` দেখুন, সাধারণত `%LOCALAPPDATA%\hermes\config.yaml`। Hermes Desktop স্থানীয় Hermes পরিচয়-সেট ভাগ করে কি না যাচাই করুন।

ক্লায়েন্ট সমর্থন করলে tailnet traffic-এর জন্য HTTP ব্যবহার করুন। Claude Desktop inference-এর জন্য trusted certificate-সহ HTTPS চাই। গেটওয়ে অন্য পথ নথিভুক্ত না করলে `/v1` ব্যবহার করুন।

কনফিগার করা ক্লায়েন্ট পুনরায় চালু করুন। Aperture-এ প্রতিটি ক্লায়েন্ট থেকে একটি মডেল অনুরোধ এবং একটি নিরাপদ শুধু-পঠন MCP সরঞ্জাম call যাচাই করুন। আমার পরিচয়ের জন্য পাওয়া মডেল, বদলানো ক্লায়েন্ট ও file, verification result এবং বাকি প্রশাসক কাজ জানান। Software install, গেটওয়ে সর্বজনীন করা, commit বা publish করবেন না।
```

## উপসংহার

Aperture কাজ করতে তিনটি বিষয় দরকার: পৌঁছানো যায় এমন গেটওয়ে, ক্লায়েন্ট protocol-এর উপযুক্ত মডেল পথ এবং প্রয়োজনীয় মডেল ও MCP connector-এর অনুমতি। একই বিন্যাস pattern macOS, Linux ও Windows-এ চলে, তবে প্রতিটি ক্লায়েন্ট নিজের OS-নির্দিষ্ট স্থানে সেটিংস রাখে।

যে Tailscale পরিচয় মডেল ব্যবহার করবে, সেই পরিচয়ে মডেল ID query করুন। মডেল ইনফারেন্স ও `/v1/mcp` আলাদাভাবে সেট করুন, তারপর বাস্তব অনুরোধ ও শুধু-পঠন সরঞ্জাম call যাচাই করুন। অন্য ডিভাইস বা Aperture সংস্করণ-এ গেলে এই গাইডের কাঠামো নিন, নতুন instance-এর পথ ও অনুমতি যাচাই করুন এবং প্রমাণীকরণ তথ্য স্থানীয় গোপন store-এ রাখুন।

## পরবর্তী ধাপ

**MCP অনুশীলন:** সংরক্ষিত সার্ভার ও যাচাইকৃত সরঞ্জাম call-এর পার্থক্যের জন্য পড়ুন [MCP সার্ভার সেটআপ: Permissions, সরঞ্জাম Tests, ও নিরাপদ Removal](/articles/effective-ai-mcp-server-setup/)। বৃহত্তর self-hosted architecture-এর জন্য দেখুন [হাইব্রিড AI এজেন্ট বহর: Tailscale, LiteLLM ও Hermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/)।

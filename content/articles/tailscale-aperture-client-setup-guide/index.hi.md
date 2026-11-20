---
title: "Tailscale Aperture: 2026 में इन्फ़रेंस और MCP के लिए AI क्लाइंट कॉन्फ़िगर करें"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Tailscale Aperture के ज़रिए मॉडल अनुरोध और MCP टूल रूट करें। किसी दूसरे डिवाइस या गेटवे पर Codex, Claude Code, Claude Desktop, OpenCode और Hermes सेट अप करें।"
genre: ["कृत्रिम बुद्धिमत्ता", "डेवलपर टूल", "नेटवर्किंग"]
tags: ["Tailscale Aperture", "Aperture सेटअप", "AI प्रॉक्सी", "LLM गेटवे", "MCP गेटवे", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "AI इन्फ़रेंस प्रॉक्सी", "Responses API", "Anthropic Messages API", "रिमोट MCP", "Streamable HTTP", "Tailscale", "स्व-होस्टेड AI", "कोडिंग एजेंट", "AI क्लाइंट कॉन्फ़िगरेशन"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "Aperture अलग नीले इन्फ़रेंस मार्ग और हरे टूल मार्ग के ज़रिए क्लाइंट पैनल को मॉडल और MCP टूल सेवाओं से जोड़ता है"
coverCaption: ""
---

## परिचय

Tailscale Aperture मॉडल इन्फ़रेंस और मॉडल Context प्रोटोकॉल (MCP) टूल के लिए AI क्लाइंट को tailnet से जुड़ा एक गेटवे देता है। हर क्लाइंट को अपने API प्रोटोकॉल से मेल खाने वाला मार्ग इस्तेमाल करना चाहिए। MCP टूल अलग एंडपॉइंट का उपयोग करते हैं। Aperture के अनुदान तय करते हैं कि हर Tailscale पहचान किन मॉडल और कनेक्टर तक पहुँच सकती है।

यह गाइड macOS, Linux और Windows पर Codex, Claude Code, Claude Desktop, OpenCode और Hermes सेट अप करने का तरीका बताती है। इसमें CLI और डेस्कटॉप सेटिंग, अपनी पहचान के लिए उपलब्ध मॉडल ID ढूँढ़ने के चरण और किसी दूसरे डिवाइस या Aperture इंस्टेंस को सेट अप करने के लिए दोबारा उपयोग करने योग्य अनाम प्रॉम्प्ट शामिल हैं।

**मार्ग चुनें:** एंडपॉइंट पथ गेटवे और API प्रोटोकॉल पर निर्भर करते हैं। `/codex` जैसा Responses मार्ग Anthropic Messages या MCP ट्रैफ़िक नहीं संभालता। गेटवे का hostname और हर क्लाइंट का इन्फ़रेंस मार्ग जाँचें। क्लाइंट सेटिंग बदलने से पहले अपने Aperture एक्सेस से मॉडल ID ढूँढ़ें।

## मुख्य बातें

- **मॉडल ट्रैफ़िक** को क्लाइंट प्रोटोकॉल का API मार्ग चाहिए।
- **MCP ट्रैफ़िक** अलग `/v1/mcp` एंडपॉइंट इस्तेमाल करता है।
- **गेटवे अनुमतियों** को आपकी Tailscale पहचान से हर मॉडल और कनेक्टर का उपयोग करने देना चाहिए।
- **क्लाइंट कॉन्फ़िगरेशन** केवल सेटिंग सहेजे जाने का प्रमाण है। वास्तविक अनुरोध और MCP टूल कॉल जाँचें।

## मार्ग कैसे काम करते हैं

| उद्देश्य | क्लाइंट अनुरोध | Aperture मार्ग | मार्ग क्या देता है |
|---|---|---|---|
| Codex और Responses-संगत मॉडल | OpenAI Responses API | आम तौर पर `/v1`। `/codex` जैसा कस्टम पथ डिप्लॉयमेंट पर निर्भर करता है। | मॉडल इन्फ़रेंस |
| Claude मॉडल इन्फ़रेंस | Anthropic Messages API | गेटवे का बेस URL। Aperture `/v1/messages` संभालता है | Claude-संगत इन्फ़रेंस |
| MCP टूल | Streamable HTTP MCP | `/v1/mcp` | कॉन्फ़िगर कनेक्टर के टूल और संसाधन |

{{< figure src="aperture-client-routes.webp" alt="Codex और Hermes Responses मार्ग इस्तेमाल करते हैं, Claude Anthropic Messages इस्तेमाल करता है और MCP क्लाइंट Aperture कनेक्टर तक पहुँचने के लिए अलग /v1/mcp मार्ग इस्तेमाल करते हैं" caption="मॉडल इन्फ़रेंस और MCP ट्रैफ़िक के लिए Aperture के अलग एंडपॉइंट हैं" >}}

**प्रदाता मूल URL:** Aperture क्लाइंट अनुरोध पथ को प्रदाता के बेस URL के साथ जोड़ता है। प्रदाता के `baseurl` को उसके API मूल URL पर सेट करें। अगर आने वाले पथ में `/v1` पहले से है, तो अपस्ट्रीम बेस URL में `/v1` न जोड़ें। URL बनाने, मॉडल पंजीकरण और अनुदान के लिए [Aperture कॉन्फ़िगरेशन संदर्भ](https://tailscale.com/docs/aperture/configuration) देखें।

## गेटवे तैयार करें

**संपादन से पहले,** Aperture व्यवस्थापक से ये मान लें:

- **गेटवे hostname:** tailnet से जुड़े ज़्यादातर क्लाइंट के लिए `http://` इस्तेमाल करें। Claude Desktop इन्फ़रेंस के लिए विश्वसनीय प्रमाणपत्र वाला `https://` चाहिए।
- **इन्फ़रेंस मार्ग:** OpenAI Responses और Anthropic Messages अलग अनुरोध प्रारूप इस्तेमाल करते हैं।
- **मॉडल ID:** नीचे दिए एंडपॉइंट से अपनी Tailscale पहचान के लिए उपलब्ध मॉडल देखें। उसी पहचान के लिए लौटाए गए सटीक ID इस्तेमाल करें।
- **प्रमाणीकरण:** जाँचें कि क्लाइंट अस्थायी API कुंजी भेजता है या उपयोगकर्ता के क्रेडेंशियल।
- **MCP एंडपॉइंट:** tailnet क्लाइंट के लिए आम तौर पर `http://<APERTURE_HOST>/v1/mcp`। Claude Desktop इन्फ़रेंस के लिए HTTPS और विश्वसनीय प्रमाणपत्र चाहिए।
- **एक्सेस अनुदान:** अपनी Tailscale पहचान के मॉडल और कनेक्टर अनुमतियाँ जाँचें।

**नेटवर्क एक्सेस:** क्लाइंट डिवाइस को tailnet के ज़रिए गेटवे तक पहुँचना चाहिए। केवल hostname से मॉडल या टूल एक्सेस नहीं मिलता। मेल खाता अनुदान मॉडल या कनेक्टर की अनुमति न दे तो Aperture अनुरोध रोकता है।

### अपने उपयोगकर्ता के उपलब्ध मॉडल ढूँढ़ें

**उसी tailnet से जुड़े डिवाइस पर मॉडल सूची पूछें।** Aperture डिवाइस की Tailscale पहचान का उपयोग करता है और उस उपयोगकर्ता को मिले मॉडल लौटाता है। [मॉडल अनुदान गाइड](https://tailscale.com/docs/aperture/how-to/grant-model-access) देखें:

```sh
# macOS या Linux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShell में पुराने curl alias से बचने के लिए curl.exe चलाएँ
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**परिणाम पढ़ें:** लौटाए गए हर `id` को मॉडल ID की तरह इस्तेमाल करें। Aperture प्रदाता पहचानने के लिए `metadata.provider.id` देखें। ऐसा मॉडल चुनें जो क्लाइंट के API प्रारूप को सपोर्ट करता हो। उदाहरण के लिए, Claude Desktop को Anthropic Messages मॉडल चाहिए। Aperture की [मॉडल डायरेक्टरी](https://tailscale.com/docs/aperture/reference/chat) में साइन-इन उपयोगकर्ता के लिए उपलब्ध ID भी हैं।

**मॉडल नहीं दिखें:** अपेक्षित मॉडल न दिखे तो Aperture व्यवस्थापक से प्रदाता कॉन्फ़िगरेशन और अपना मॉडल अनुदान जाँचने को कहें। उपयोगकर्ता इस एंडपॉइंट से खुद को एक्सेस नहीं दे सकते।

**URL स्कीम:** Tailscale एक ही tailnet के ज़्यादातर क्लाइंट के लिए `http://` सुझाता है। WireGuard इस ट्रैफ़िक को एन्क्रिप्ट करता है। Claude Desktop के लिए `https://` और ऑपरेटिंग सिस्टम का विश्वसनीय प्रमाणपत्र चाहिए। हर क्लाइंट के लिए नीचे बताई स्कीम अपनाएँ।

### इन्फ़रेंस प्रदाता जोड़ें

**OpenAI Responses:** Aperture में अपस्ट्रीम प्रदाता जोड़ें और क्लाइंट का API प्रारूप चालू करें। OpenAI अपस्ट्रीम के लिए यह अंश जोड़ें:

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

**Anthropic Messages:** Anthropic API मूल URL, `x-api-key` प्रमाणीकरण प्रारूप और `anthropic_messages` संगतता इस्तेमाल करें। मॉडल ID प्रदाता की `models` सूची में भी होना चाहिए। यह अंश जोड़ें:

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

**कॉन्फ़िगरेशन बदलाव:** हर प्लेसहोल्डर को अपस्ट्रीम मान से बदलें। अंशों को मौजूदा Aperture कॉन्फ़िगरेशन में जोड़ें और बाकी फ़ाइल बनाए रखें। प्रदाता जिन API को सपोर्ट करता है उनके संगतता फ़्लैग चालू करें।

**एक्सेस अनुदान:** Aperture हर मॉडल और कनेक्टर पर उपयोगकर्ता एक्सेस नियंत्रित करता है। हर लक्षित Tailscale उपयोगकर्ता को सिर्फ ज़रूरी अनुमतियाँ दें। यह उदाहरण एक उपयोगकर्ता को एक प्रदाता मॉडल और एक कनेक्टर देता है:

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

**मॉडल अनुदान:** अनुदान पैटर्न में प्रदाता ID और मॉडल ID इस्तेमाल करें। [कनेक्टर सेटअप गाइड](https://tailscale.com/docs/aperture/connectors/get-started) मौजूदा `connectors.servers` कॉन्फ़िगरेशन दिखाती है। पुराना top-level `mcp.servers` कॉन्फ़िगरेशन अब उपयोग में नहीं है।

### MCP कनेक्टर जोड़ें

**MCP कनेक्टर:** Aperture अपस्ट्रीम MCP सर्वर से जुड़ता है और `/v1/mcp` पर टूल उपलब्ध कराता है:

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

**कनेक्टर URL:** अपस्ट्रीम सर्वर का पूरा MCP एंडपॉइंट इस्तेमाल करें। फिर अपने Tailscale उपयोगकर्ता को `teamtools/**` या सीमित टूल पैटर्न की अनुमति दें। [MCP प्रॉक्सी संदर्भ](https://tailscale.com/docs/aperture/mcp-server) एकल क्लाइंट एंडपॉइंट और कनेक्टर व्यवहार समझाता है।

## Codex CLI और डेस्कटॉप

**साझा सेटिंग:** Codex CLI और डेस्कटॉप ऐप एक ही कॉन्फ़िगरेशन इस्तेमाल करते हैं। macOS और Linux पर `~/.codex/config.toml` संपादित करें। Windows पर `%USERPROFILE%\.codex\config.toml` संपादित करें (होम डायरेक्टरी फैलाने वाले shell में `~/.codex/config.toml` भी चलता है)। [Codex ऐप परिचय](https://openai.com/index/introducing-the-codex-app/) कहता है कि डेस्कटॉप ऐप Codex CLI कॉन्फ़िगरेशन अपनाता है। Codex उपयोगकर्ता setting `~/.codex/config.toml` में होती हैं। [कॉन्फ़िगरेशन मूल बातें](https://learn.chatgpt.com/docs/config-file/config-basic) user-level प्रदाता और MCP field समझाती हैं। इस फ़ाइल में प्रदाता जोड़ें, ऐप फिर शुरू करें और UI में प्रदाता व मॉडल देखें।

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

**वैकल्पिक field:** ये दो मान एक Codex प्रदाता सेटअप से मेल खाते हैं। इन्हें तभी रखें जब आपका गेटवे और Codex कॉन्फ़िगरेशन माँगे। Tailscale की मौजूदा [Codex Aperture गाइड](https://tailscale.com/docs/aperture/how-to/use-codex) इन्हें छोड़ती है, `wire_api = "responses"` इस्तेमाल करती है और बताती है कि Aperture अपस्ट्रीम क्रेडेंशियल जोड़ता है। गेटवे व्यवस्थापक का दिया सटीक Responses URL इस्तेमाल करें। `/codex` डिप्लॉयमेंट-विशिष्ट मार्ग है। Tailscale का दस्तावेज़ीकृत डिफ़ॉल्ट `/v1` है।

**MCP कॉन्फ़िगरेशन:** उसी user कॉन्फ़िगरेशन में सर्वर जोड़ें:

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**Codex जाँचें:** `codex mcp list` चलाएँ, नया session शुरू करें और `/mcp` देखें। सर्वर सूची पंजीकरण दिखाती है। सूची में टूल और सफल कॉल उसकी खोज और निष्पादन प्रमाणित करते हैं। [Codex कॉन्फ़िगरेशन संदर्भ](https://learn.chatgpt.com/docs/config-file/config-reference) user-level प्रदाता और MCP सेटिंग बताता है।

## Claude Code CLI

**प्रोटोकॉल:** Claude Code Anthropic Messages इस्तेमाल करता है। Global Claude Code सेटिंग file को Anthropic-संगत Aperture गेटवे पर सेट करें। macOS और Linux पर `~/.claude/settings.json`, Windows पर `%USERPROFILE%\.claude\settings.json` इस्तेमाल करें। PowerShell में `$HOME\.claude\settings.json` इस्तेमाल करें। मार्ग को `/v1/messages` देना होगा। Codex Responses अलग प्रोटोकॉल और मार्ग इस्तेमाल करता है। Tailscale tailnet पर Claude Code के लिए HTTP सुझाता है, क्योंकि WireGuard कनेक्शन एन्क्रिप्ट करता है।

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**क्लाइंट प्रमाणीकरण:** Aperture क्लाइंट गाइड `apiKeyHelper` में प्लेसहोल्डर इस्तेमाल करती है, क्योंकि Aperture अपस्ट्रीम क्रेडेंशियल जोड़ता है। Claude सदस्यता पासथ्रू के लिए Aperture Anthropic प्रदाता को उपयोगकर्ता का Claude क्रेडेंशियल आगे भेजना होगा। उस स्थिति में `ANTHROPIC_API_KEY` और `ANTHROPIC_AUTH_TOKEN` सेट न करें। ये चर सदस्यता क्रेडेंशियल की जगह लेते हैं। अपने Claude कोड संस्करण की [Claude Code Aperture निर्देश](https://tailscale.com/docs/aperture/how-to/use-claude-code) और प्रमाणीकरण विकल्पों के लिए [Anthropic गेटवे गाइड](https://code.claude.com/docs/en/llm-gateway-connect) अपनाएँ।

**HTTP पर MCP:** यह कमांड चलाकर एंडपॉइंट जोड़ें:

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**Claude Code जाँचें:** Session शुरू करके `/mcp` चलाएँ। Anthropic के [MCP दस्तावेज़](https://code.claude.com/docs/en/mcp) में दूरस्थ MCP सर्वर के लिए HTTP सुझाया गया है।

## Claude Desktop GUI

**अलग सेटिंग:** Claude Desktop में third-party इन्फ़रेंस स्क्रीन है। यह सेटिंग Claude Desktop के मॉडल अनुरोध Aperture से भेजती है। MCP कॉन्फ़िगरेशन अलग चरण है।

1. macOS या Windows के Claude Desktop में **Help > Troubleshooting > Enable Developer Mode** (सहायता > समस्या निवारण > डेवलपर मोड सक्षम करें) चुनें। Linux बीटा में menu उपलब्ध हो तो वही विकल्प लें। संकेत मिलने पर ऐप फिर शुरू करें। Menu न दिखे तो Claude Desktop अपडेट करें और platform-specific रिलीज़ note देखें।
2. **Developer > Configure Third-Party Inference** (डेवलपर > तृतीय पक्ष इन्फ़रेंस कॉन्फ़िगर करें) चुनें।
3. **Connection type** (कनेक्शन का प्रकार) को **Gateway** (गेटवे), और **Credential kind** (क्रेडेंशियल का प्रकार) को **Static API key** (स्थिर API कुंजी) सेट करें।
4. **Gateway base URL** (गेटवे का मूल URL) में `https://<APERTURE_HOST>` लिखें। विश्वसनीय TLS प्रमाणपत्र में शामिल पूरा hostname इस्तेमाल करें।
5. गेटवे कुंजी के लिए `aperture` जैसा खाली न होने वाला प्लेसहोल्डर डालें। Aperture इसे अनदेखा करके tailnet के ज़रिए प्रमाणीकरण करता है।
6. Custom इन्फ़रेंस header खाली छोड़ें।
7. अपनी Tailscale पहचान के लिए `GET /v1/models` से लौटा सटीक ID देकर सक्रिय मॉडल जोड़ें। Anthropic Messages मॉडल चुनें। ID, दिखने वाला नाम और वैकल्पिक tier उपनाम हाथ से भरें। Claude Desktop इस स्क्रीन पर मॉडल खोजता नहीं है।
8. **Save Changes** (बदलाव सहेजें), फिर **Apply Changes** (बदलाव लागू करें) चुनें। Claude Desktop बंद करके फिर खोलें।

**प्रोटोकॉल जाँच:** [Aperture Claude Desktop गाइड](https://tailscale.com/docs/aperture/how-to/use-claude-desktop) कहती है कि Claude Desktop `/v1/messages` पर Anthropic Messages इस्तेमाल करता है। Codex मार्ग `/codex` न डालें और OpenAI-संगत कनेक्शन type न चुनें।

### Claude Desktop को MCP से जोड़ें

**निजी MCP एक्सेस:** Claude Desktop वाले कंप्यूटर पर स्थानीय stdio ब्रिज चलाएँ। Claude Desktop के स्थानीय MCP कॉन्फ़िगरेशन में यह जोड़ें:

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

**Bridge का काम:** स्थानीय process कंप्यूटर के Tailscale कनेक्शन से Aperture तक पहुँचता है। अपने OS का कॉन्फ़िगरेशन पथ इस्तेमाल करें: macOS, `~/Library/Application Support/Claude/claude_desktop_config.json`; Windows, `%APPDATA%\Claude\claude_desktop_config.json`; Linux बीटा में **सेटिंग > Developer > Edit कॉन्फ़िगरेशन** खोलें और Claude Desktop का खुला पथ लें। Linux पथ package पर निर्भर करता है। Claude Desktop फिर शुरू करें, कनेक्टर सूची देखें और एक सुरक्षित टूल call करें। [`mcp-remote` project](https://github.com/punkpeye/mcp-remote) स्थानीय से दूरस्थ ब्रिज बताता है।

**दूरस्थ कनेक्टर:** Anthropic का सेटिंग > Connectors प्रवाह ऐसा दूरस्थ सर्वर माँगता है जहाँ Anthropic सेवा पहुँच सके। केवल tailnet वाला hostname आपके डिवाइस तक सीमित है, इसलिए निजी एंडपॉइंट के लिए स्थानीय bridge इस्तेमाल करें। सार्वजनिक MCP सेवा उपलब्ध कराएँ तो cloud कनेक्टर में जोड़ने से पहले प्रमाणीकरण और अनुमतियाँ सेट करें। Anthropic की [दूरस्थ MCP कनेक्टर गाइड](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) देखें।

## OpenCode CLI और डेस्कटॉप

**साझा सेटिंग:** OpenCode CLI और डेस्कटॉप OpenCode कॉन्फ़िगरेशन एक ही पढ़ते हैं। मौजूदा OpenCode V2 दस्तावेज़ custom प्रदाता के लिए `providers` map और MCP सर्वर के लिए `mcp.servers` इस्तेमाल करते हैं। यह उदाहरण `/v1` पर OpenAI-संगत chat एंडपॉइंट इस्तेमाल करता है। इस मॉडल मार्ग से पहले जाँचें कि Aperture प्रदाता OpenAI Chat Completions सपोर्ट करता है।

**Global कॉन्फ़िगरेशन:** macOS और Linux पर `~/.config/opencode/opencode.json` संपादित करें। Windows पर `%USERPROFILE%\.config\opencode\opencode.json` इस्तेमाल करें। OpenAI-संगत प्रदाता जोड़ें और `<MODEL_ID>` को सटीक Aperture मॉडल ID से बदलें। Comment के लिए OpenCode इसी डायरेक्टरी में `opencode.jsonc` भी लेता है। [कॉन्फ़िगरेशन reference](https://opencode.ai/docs/config/) global और project setting की प्राथमिकता बताता है।

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

**क्लाइंट प्रमाणीकरण:** `oauth: false` OpenCode का डिफ़ॉल्ट OAuth प्रवाह छोड़ता है। Aperture Tailscale से caller पहचानता है। OpenCode को प्रदाता प्रमाणीकरण प्रविष्टि भी चाहिए, इसलिए स्थानीय पर्यावरण में `APERTURE_API_KEY=-` सेट करें। डेस्कटॉप ऐप को भी यह चर मिलना चाहिए। Shell पर्यावरण न मिले तो ऐप में `/connect` चलाकर Aperture के लिए `-` डालें। अपस्ट्रीम प्रदाता कुंजी इस फ़ाइल में न रखें। OpenCode की [प्रदाता गाइड](https://opencode.ai/docs/providers/) और [MCP गाइड](https://opencode.ai/docs/mcp-servers/) वर्तमान प्रारूप बताते हैं। सर्वर जाँचने के लिए `opencode mcp list` चलाएँ और ऐप में `/mcps` से स्थिति देखें।

## Hermes CLI और डेस्कटॉप

**साझा सेटिंग:** Hermes Agent macOS और Linux पर नामित प्रदाता और MCP सर्वर `~/.hermes/config.yaml` में रखता है। Windows की native installation `%LOCALAPPDATA%\hermes\config.yaml` इस्तेमाल करती है। सक्रिय फ़ाइल जानने के लिए `hermes config path` चलाएँ। `HERMES_HOME` डिफ़ॉल्ट जगह बदल सकता है। स्थानीय Hermes Desktop CLI वाला ही Hermes होम और प्रोफ़ाइल इस्तेमाल करता है। Desktop दूरस्थ Hermes गेटवे से जुड़ता हो तो Hermes मशीन पर Aperture configure करें और सर्वर का tailnet तक पहुँचना जाँचें। [Hermes Desktop गाइड](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) में स्थानीय और दूरस्थ सेटअप देखें।

**Responses प्रदाता:** नामित प्रदाता जोड़ें। `api` का मान आपके Aperture इंस्टेंस के Responses एंडपॉइंट से मेल खाना चाहिए:

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # Aperture setup को client key चाहिए तभी key_env जोड़ें।
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**प्रोटोकॉल चुनें:** OpenAI Chat Completions के लिए `transport: chat_completions` सेट करें। Anthropic Messages के लिए `transport: anthropic_messages` चुनें और Anthropic Messages गेटवे URL इस्तेमाल करें। मौजूदा [प्रदाता गाइड](https://hermes-agent.nousresearch.com/docs/integrations/providers) में नामित Hermes प्रदाता के `api`, `transport` और `default_model` field हैं।

**MCP कॉन्फ़िगरेशन:** उसी YAML फ़ाइल में Aperture MCP जोड़ें:

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**Hermes जाँचें:** `hermes mcp` चलाएँ और इंटरैक्टिव सर्वर चयनकर्ता में हर कनेक्शन देखें। स्थानीय Desktop उसी प्रोफ़ाइल को उपयोग करता है। Hermes के [दूरस्थ HTTP MCP सर्वर](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) और [MCP कॉन्फ़िगरेशन संदर्भ](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference) देखें।

## दोनों रास्ते जाँचें

**मॉडल इन्फ़रेंस और MCP की अलग-अलग जाँच करें:**

1. Tailscale कनेक्शन और गेटवे तक पहुँच की पुष्टि करें। Claude Desktop के लिए विश्वसनीय TLS प्रमाणपत्र भी जाँचें।
2. हर configured क्लाइंट से छोटा प्रॉम्प्ट भेजें। पुष्टि करें कि Aperture session सूची में अनुरोध दिखता है।
3. पुष्टि करें कि चुना मॉडल ID आपकी Tailscale पहचान को मिले मॉडल से मेल खाता है।
4. हर क्लाइंट की MCP स्थिति स्क्रीन या सूची कमांड देखें। Aperture सर्वर जुड़ा है और अपेक्षित टूल देता है, यह सुनिश्चित करें।
5. केवल पढ़ने वाला एक टूल चलाएँ। लौटे content को अपस्ट्रीम source से मिलाएँ।
6. मॉडल या टूल कॉल विफल हो तो Aperture log देखें। सहेजा कॉन्फ़िगरेशन सफल अनुरोध का प्रमाण नहीं है।

| समस्या | जाँच |
|---|---|
| मॉडल अनुरोध 404 या 405 लौटाता है | पुष्टि करें कि क्लाइंट एंडपॉइंट सही मार्ग और प्रोटोकॉल उपयोग करता है। Anthropic Messages या MCP के लिए `/codex` दोबारा इस्तेमाल न करें। |
| मॉडल उपलब्ध नहीं | लक्षित Tailscale उपयोगकर्ता के रूप में `/v1/models` पूछें। सटीक ID और API प्रारूप जाँचें। छूटी प्रदाता entry या अनुदान के लिए व्यवस्थापक से कहें। |
| अनुरोध अनधिकृत | देखें कि क्लाइंट को प्लेसहोल्डर, बियरर टोकन या सदस्यता पासथ्रू चाहिए। अपस्ट्रीम प्रदाता कुंजी सार्वजनिक project फ़ाइल में कॉपी न करें। |
| MCP सर्वर सूची में है, लेकिन टूल नहीं दिखते | `/v1/mcp`, कनेक्टर स्वास्थ्य और अनुदान, तथा क्लाइंट से Aperture तक नेटवर्क पथ जाँचें। |
| Claude Desktop निजी MCP URL से नहीं जुड़ता | `mcp-remote` जैसा स्थानीय bridge चलाएँ या उपयुक्त प्रमाणीकरण वाला अनुमोदित सार्वजनिक कनेक्टर इस्तेमाल करें। |

## दूसरे डिवाइस पर सेटअप दोहराएँ

**नया डिवाइस:** वही क्लाइंट install करें और पहले डिवाइस को tailnet से जोड़ें। नए डिवाइस से `/v1/models` पूछकर उसकी Tailscale पहचान को मिले मॉडल देखें। कॉन्फ़िगरेशन का ढाँचा अपनाएँ, क्रेडेंशियल स्थानीय रखें। `<APERTURE_HOST>`, `<MODEL_ID>` और `<UPSTREAM_MCP_ENDPOINT>` को लक्ष्य Aperture इंस्टेंस के मानों से बदलें। हर API प्रोटोकॉल के लिए अलग एंडपॉइंट रखें, फिर टूल ट्रैफ़िक के लिए `/v1/mcp` सेट करें। अंत में एक मॉडल अनुरोध और एक MCP टूल call जाँचें।

**एकाधिक गेटवे:** हर Aperture इंस्टेंस के लिए अलग कॉन्फ़िगरेशन रखें। डिवाइस को Codex और Hermes के लिए Responses एंडपॉइंट, Claude के लिए Anthropic Messages एंडपॉइंट और टूल के लिए MCP एग्रीगेशन एंडपॉइंट चाहिए। API क्रेडेंशियल हर क्लाइंट के स्थानीय गुप्त store या पर्यावरण चर में रखें। `config.toml`, `opencode.json`, `config.yaml` या सार्वजनिक repository में API कुंजी कॉपी न करें।

## फिर से इस्तेमाल करने योग्य Aperture सेटअप प्रॉम्प्ट

**इस अनाम प्रॉम्प्ट को** अपने कोडिंग सहायक में कॉपी करें। प्लेसहोल्डर को गेटवे विवरण से बदलें। मॉडल ID चुनने से पहले assistant को आपकी Tailscale पहचान के रूप में Aperture पूछना चाहिए।

```text
मेरे मौजूदा Tailscale Aperture गेटवे और इस डिवाइस पर इंस्टॉल AI क्लाइंट को configure करें।

दायरे के क्लाइंट: Codex CLI और desktop, Claude Code, Claude Desktop, OpenCode CLI और desktop, Hermes CLI और desktop।

पहले पता करें कि डिवाइस macOS, Linux या Windows चलाता है, सक्रिय shell (जैसे zsh, bash या PowerShell) पहचानें और पूरे काम में उसी platform के पथ और कमांड सिंटैक्स अपनाएँ। मौजूदा गेटवे, Tailscale कनेक्शन, क्लाइंट version और वर्तमान क्लाइंट setting पहले जाँचें। वर्तमान official दस्तावेज़ पढ़ें। असंबंधित कॉन्फ़िगरेशन बनाए रखें और हर फ़ाइल संपादित करने से पहले उसका backup लें। Hostname, मॉडल ID, API मार्ग या क्रेडेंशियल का अनुमान न लगाएँ। अपस्ट्रीम प्रदाता कुंजी Aperture में रखें, क्लाइंट फ़ाइल या repository में नहीं।

इस Tailscale-connected डिवाइस से उपलब्ध मॉडल खोजें:
1. मेरे क्लाइंट की Tailscale पहचान के रूप में `http://<APERTURE_HOST>/v1/models` पूछें। गेटवे का दस्तावेज़ अलग मॉडल सूची URL देता हो तो वही लें।
2. हर मॉडल का `id` और `metadata.provider.id` पढ़ें। सूची मेरी पहचान को दिए मॉडल दिखाती है। Administrator की सूची से इसे न बदलें और ID न गढ़ें।
3. हर क्लाइंट के API प्रारूप से मॉडल की संगतता मिलाएँ। Codex OpenAI Responses इस्तेमाल करता है। Claude क्लाइंट Anthropic Messages इस्तेमाल करते हैं। OpenCode और Hermes के लिए संगत प्रदाता और transport configure करें।
4. जहाँ संभव हो क्लाइंट का मौजूदा डिफ़ॉल्ट मॉडल रखें। डिफ़ॉल्ट चाहिए और मेरी पसंद नहीं है तो संगत मॉडल दिखाकर मुझसे चुनने को कहें। Claude Desktop में सही मॉडल ID हाथ से लिखनी होती है।
5. उपयुक्त मॉडल न लौटे तो प्रदाता और अनुदान setting केवल तभी जाँचें जब मेरे पास व्यवस्थापक पहुंच हो। अन्यथा व्यवस्थापक को बताएं कि कौन-सा मॉडल पहुंच जोड़ना होगा। खुद को पहुंच न दें।

Aperture डिप्लॉयमेंट और कॉन्फ़िगरेशन का स्रोत खोजें। File पथ न मानें और पूरी कॉन्फ़िगरेशन न बदलें। OpenAI Responses के लिए `openai_responses`, Anthropic क्लाइंट के लिए `anthropic_messages` चाहिए। MCP कनेक्टर मौजूदा `connectors.servers` कॉन्फ़िगरेशन में आते हैं और क्लाइंट `/v1/mcp` से जुड़ते हैं।

Shared गेटवे बदलने से पहले प्रदाता, कनेक्टर और अनुदान का न्यूनतम diff तैयार करें। केवल तभी लागू करें जब मैं व्यवस्थापक हूँ और यह अनुरोध गेटवे बदलाव की अनुमति देता है। अनुमति नहीं है तो instance मालिक को सटीक प्रस्तावित बदलाव बताएं। मालिक की स्पष्ट अनुमति के बिना अनुदान न बनाएँ और न बढ़ाएँ। मौजूदा गेटवे setting सुरक्षित रखें।

इंस्टॉल क्लाइंट को वर्तमान official प्रारूप और OS-विशिष्ट स्थान पर configure करें:
- Codex CLI और desktop macOS/Linux में `~/.codex/config.toml` और Windows में `%USERPROFILE%\.codex\config.toml` साझा करते हैं। Aperture प्रदाता, संगत मॉडल, `wire_api = "responses"` और `mcp_servers` में MCP सेट करें।
- Claude Code `ANTHROPIC_BASE_URL` और HTTP दूरस्थ MCP इस्तेमाल करता है। macOS/Linux में `~/.claude/settings.json`, Windows में `%USERPROFILE%\.claude\settings.json` लें।
- Claude Desktop में Developer Mode, Configure Third-Party Inference (तृतीय पक्ष इन्फ़रेंस कॉन्फ़िगर करें), गेटवे, Static API कुंजी, विश्वसनीय प्रमाणपत्र वाला HTTPS URL और मेरे उपयोगकर्ता के लिए मिला मॉडल ID सेट करें। निजी tailnet के MCP के लिए स्थानीय `mcp-remote` bridge लें। MCP कॉन्फ़िगरेशन के लिए सेटिंग > Developer > Edit कॉन्फ़िगरेशन देखें; उपलब्ध न हो तो OS का documented पथ लें।
- OpenCode वर्तमान V2 `providers` schema और `mcp.servers` लेता है। Global कॉन्फ़िगरेशन macOS/Linux में `~/.config/opencode/opencode.json` और Windows में `%USERPROFILE%\.config\opencode\opencode.json` है। Aperture MCP में `oauth: false` सेट करें। ज़रूरत हो तो स्थानीय प्लेसहोल्डर API कुंजी लें।
- Hermes नामित प्रदाता, मॉडल API से मेल खाता transport और `mcp_servers` लेता है। macOS/Linux में `~/.hermes/config.yaml` लें। Windows पर `hermes config path` देखें, आम तौर पर `%LOCALAPPDATA%\hermes\config.yaml`। जाँचें कि Hermes Desktop स्थानीय Hermes प्रोफ़ाइल साझा करता है या नहीं।

क्लाइंट समर्थन करे तो tailnet ट्रैफ़िक के लिए HTTP उपयोग करें। Claude Desktop इन्फ़रेंस को विश्वसनीय प्रमाणपत्र वाला HTTPS चाहिए। गेटवे दूसरा मार्ग न बताए तो `/v1` लें।

Configured क्लाइंट फिर शुरू करें। Aperture में हर क्लाइंट से एक मॉडल अनुरोध और एक सुरक्षित, केवल-पठन MCP टूल call जाँचें। मेरी पहचान के लिए मिले मॉडल, बदले क्लाइंट और फ़ाइल, verification परिणाम और बाकी व्यवस्थापक काम बताएँ। Software install न करें, गेटवे सार्वजनिक न करें, commit या publish न करें।
```

## निष्कर्ष

Aperture चलाने के लिए तीन चीज़ें चाहिए: पहुँच योग्य गेटवे, क्लाइंट प्रोटोकॉल से मेल खाता मॉडल मार्ग और आवश्यक मॉडल व MCP कनेक्टर के अनुदान। यही कॉन्फ़िगरेशन pattern macOS, Linux और Windows पर काम करता है, लेकिन हर क्लाइंट OS-विशिष्ट स्थान पर सेटिंग रखता है।

मॉडल ID उसी Tailscale पहचान से पूछें जो उनका उपयोग करेगी। मॉडल इन्फ़रेंस और `/v1/mcp` अलग configure करें, फिर वास्तविक अनुरोध और केवल पढ़ने वाला टूल कॉल जाँचें। दूसरे डिवाइस या Aperture इंस्टेंस पर जाते समय इस गाइड का ढाँचा लें, उस instance के मार्ग और अनुदान सत्यापित करें और क्रेडेंशियल स्थानीय गुप्त store में रखें।

## अगले कदम

**MCP अभ्यास:** सहेजे सर्वर और सत्यापित टूल कॉल का अंतर जानने के लिए [MCP सर्वर सेटअप: Permissions, टूल Tests, और सुरक्षित Removal](/articles/effective-ai-mcp-server-setup/) पढ़ें। व्यापक स्व-होस्टेड आर्किटेक्चर के लिए [हाइब्रिड AI एजेंट समूह: Tailscale, LiteLLM और Hermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/) देखें।

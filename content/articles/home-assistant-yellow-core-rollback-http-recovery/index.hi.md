---
title: 'Home Assistant Core 2026.11 से 2026.10.4 पर रोलबैक: HTTP स्टोरेज संस्करण 3 की मरम्मत'
date: 2026-11-15
lastmod: 2026-11-27
toc: true
draft: false
description: Yellow पर Home Assistant Core 2026.11 के 2026.10.4 पर लौटने के बाद HTTP स्टोरेज संस्करण 3 की त्रुटि ठीक करें।
  इसमें सुरक्षित कमांड और सत्यापित आउटपुट शामिल हैं।
genre:
- होम ऑटोमेशन
- समस्या निवारण
tags:
- Home Assistant Yellow
- Home Assistant OS
- Core 2026.11 रोलबैक
- Core 2026.10.4
- HTTP स्टोरेज संस्करण 3
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: पीले कंप्यूटर बोर्ड, टूटे कॉन्फ़िगरेशन लिंक और बहाल वेब डैशबोर्ड का चित्र
coverCaption: ''
---

Home Assistant Core 2026.11 का अपडेट विफल हुआ और मेरे Yellow CM4 को 2026.10.4 पर वापस ले गया। Yellow नेटवर्क पर उपलब्ध रहा, लेकिन डैशबोर्ड दिखाना बंद कर दिया। रोलबैक के बाद HTTP सेटिंग्स फ़ाइल स्टोरेज संस्करण 3.1 में थी, जबकि Core 2026.10.4 संस्करण 2.2 का समर्थन करता है। मैंने फ़ाइल सुरक्षित रखी, सख्त जाँच के तहत उसकी एक प्रति बदली, HTTP पहुँच बहाल की, फिर Core को 2026.11.1 पर अपडेट किया।

<!--more-->

## मुख्य बातें

- **असंगति की पुष्टि करें।** Core लॉग की त्रुटि को इंस्टॉल किए गए रिलीज़ और HTTP स्टोरेज संस्करण से मिलाएँ।
- **फ़ाइल सुरक्षित रखें।** रिकवरी से पहले एक अपरिवर्तित प्रति और डिवाइस से बाहर बैकअप रखें।
- **परिणाम जाँचें।** Core की स्थिति, सुरक्षित श्रोता-पोर्ट, डैशबोर्ड और इंस्टॉल किए गए संस्करण की जाँच करें।

**इसी मामले के लिए समाधान:** [HTTP फ़ाइल सुरक्षित रखें](#preserve-recovery-options), [संस्करण 2.2 का उम्मीदवार बनाएँ और सत्यापित करें](#apply-the-tested-fix-for-version-31), [Core रोकने के बाद उसे इंस्टॉल करें](#apply-the-tested-fix-for-version-31), और [अपडेट का परिणाम जाँचें](#verify-the-update-outcome)। रूपांतरण मूल फ़ील्ड जाँचता है और अंतर मिलने पर रुक जाता है। किसी ऐसी HTTP फ़ाइल पर इसे लागू न करें जिसकी जाँच नहीं हुई है।

## शुरू करने से पहले

आपको Yellow CM4 तक भौतिक पहुँच, USB-C डेटा केबल, काम करने वाला सीरियल कंसोल और उपयोगी बैकअप या सुरक्षित रखी गई कॉन्फ़िगरेशन चाहिए। मैन्युअल तरीके में होस्ट शेल तक पहुँच और JSON की सावधानीपूर्वक जाँच आवश्यक है। निदान और मरम्मत के लिए कम से कम 30 मिनट रखें। बड़े इंस्टॉलेशन में Core के शुरू होने और बैकअप बहाल होने में अधिक समय लगता है।

## समस्या पहचानें

Core लॉग में निर्णायक त्रुटि दिखाई दी:

```text
Storage file http has version 3 which is newer than the max supported version 2
```

पुराना Core रिलीज़ `http` लोड नहीं कर पाया। HTTP पर निर्भर फ्रंटएंड और अन्य घटक भी विफल हो गए। राउटर लीज़ मिलना और Observer पेज का ठीक होना डैशबोर्ड पहुँच साबित नहीं करता। [Home Assistant Core की समस्या #190583](https://github.com/home-assistant/core/issues/190583) कई इंस्टॉलेशन, जिनमें Yellow भी है, में इसी रोलबैक विफलता का दस्तावेज़ देता है। [इश्यू पर मेरी टिप्पणी](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) इस Yellow की परीक्षित रिकवरी और Core की अंतिम स्थिति दर्ज करती है।

**वेब बंद होने का कारण:** Core 2026.11 ने `.storage/http` को प्रारूप 3.1 में लिखा। रोलबैक ने Core 2026.10.4 लौटाया, लेकिन संगत HTTP फ़ाइल नहीं लौटाई। Core 2026.10.4 स्टोरेज संस्करण 3 अस्वीकार करता है। इस Yellow की सुरक्षित `intermediate_v6` प्रोफ़ाइल भी पुराने स्कीमा से मेल नहीं खाती। पहला अपडेट क्यों विफल हुआ और रोलबैक शुरू हुआ, यह अज्ञात है। 2026-11-15 तक लिंक किया गया इश्यू खुला था और चर्चा में अनुरक्षक द्वारा पुष्टि किया गया समाधान नहीं था।

फ़ाइलें बदलने से पहले इंस्टॉल किए गए Core रिलीज़ और HTTP स्टोर की जाँच करें:

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

नीचे दिया गया आउटपुट इस मामले का है, जिसमें समय-मुद्राएँ और निजी विवरण हटा दिए गए हैं:

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

नीचे दिए गए रिकवरी कमांड Supervisor में सुरक्षित श्रोता-पोर्ट की HTTP फ़ाइल से तुलना करते हैं, लेकिन कोई मान प्रिंट नहीं करते। अंतर मिलने पर फ़ाइलें बदलने से पहले Core का वास्तविक श्रोता-पोर्ट जाँचें।

| संकेत | अर्थ |
| --- | --- |
| Core स्टोरेज संस्करण 2 का समर्थन करता है, फ़ाइल संस्करण 3 बताती है | पुराना रिलीज़ सुरक्षित HTTP सेटिंग्स लोड नहीं कर सकता |
| HTTP फ़ाइल और Supervisor सूची अलग श्रोता-पोर्ट बताती हैं | विफलता का कारण तय करने से पहले Core का वास्तविक श्रोता-पोर्ट जाँचें |
| मुख्य पृष्ठ जवाब देता है, पर Core की स्थिति STARTING है | केवल फ्रंटएंड का जवाब स्टार्टअप पूरा होने का प्रमाण नहीं |

## रिकवरी के विकल्प सुरक्षित रखें {#preserve-recovery-options}

अगले अपडेट से पहले Yellow के बाहर उपयोगी बैकअप रखें। [Home Assistant की बैकअप मार्गदर्शिका](https://www.home-assistant.io/common-tasks/general/backups/) क्लाउड और डिवाइस से बाहर के स्थान बताती है। एन्क्रिप्टेड बैकअप के लिए उसकी रिकवरी कुंजी चाहिए। स्टोरेज असंगति का निदान करते समय NVMe डेटा डिस्क न मिटाएँ।

संपादन से पहले HTTP फ़ाइल की प्रति बनाएँ:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

कमांड विफल हो तो रुकें। उसी नाम वाली पुरानी रिकवरी प्रति को जस का तस रखें। नया नाम चुनें और आगे बढ़ने से पहले जाँच दोहराएँ।

डैशबोर्ड अनुपलब्ध हो तो Yellow का सीरियल कंसोल इस्तेमाल करें। [Linux और macOS के लिए Nabu Casa मार्गदर्शिका](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) USB-C कनेक्शन और JP1 UART की स्थिति दिखाती है। अपने हार्डवेयर के लिए CM4 निर्देशों का पालन करें।

## संस्करण 3.1 के परीक्षित समाधान को लागू करें {#apply-the-tested-fix-for-version-31}

बेहतर तरीका अपडेट से पहले की संगत HTTP फ़ाइल इस्तेमाल करना है। पूरी बहाली उचित हो तो Home Assistant की दस्तावेज़ित प्रक्रिया से बैकअप बहाल करें। यदि एक फ़ाइल निकालते हैं, तो सक्रिय फ़ाइल बदलने से पहले उसका स्टोरेज संस्करण और सुरक्षित श्रोता-पोर्ट पक्का करें। संगत HTTP फ़ाइल उपलब्ध न होने पर इस Yellow पर नीचे दिए कमांड सीधे परीक्षित समाधान थे।

[इश्यू का मूल उपाय](https://github.com/home-assistant/core/issues/190583) `.storage/http` को अलग रखता है और पुराने Core को नई फ़ाइल बनाने देता है। बाद की [Yellow रिपोर्ट](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) दोबारा बनाई फ़ाइल में अलग श्रोता-पोर्ट दिखाती है। वेब इंटरफ़ेस ठीक मानने से पहले नई फ़ाइल और `ha core info` जाँचें।

मेरे इंस्टॉलेशन में `http:` YAML ब्लॉक, लंबित HTTP कॉन्फ़िगरेशन, या स्थिर सेटिंग्स में TLS प्रमाणपत्र अथवा कुंजी नहीं थी। सुरक्षित प्रोफ़ाइल `intermediate_v6` थी। इस सीमित मामले में मैंने अलग संस्करण 2.2 उम्मीदवार बनाया और मौजूदा श्रोता-पोर्ट रखा:

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

सक्रिय फ़ाइल बदलने से पहले ऊपर दिए सभी कमांड सफल होने चाहिए। `jq` विफल हो तो उम्मीदवार फ़ाइल हटाकर दोबारा कोशिश करने से पहले उसका निरीक्षण करें। [Core 2026.10.4 का HTTP स्रोत](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) स्टोरेज संस्करण 2.2 तय करता है और `intermediate` प्रोफ़ाइल स्वीकारता है। [Core 2026.11.1 का स्रोत](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) संस्करण 3.1 और संस्करणयुक्त प्रोफ़ाइल नाम इस्तेमाल करता है। इंस्टॉल करने से पहले मैंने उम्मीदवार को इंस्टॉल किए गए पुराने Core के `HTTP_STORAGE_SCHEMA` से भी सत्यापित किया।

कंटेनर चालू रहते हुए इंस्टॉल किए गए पुराने Core की स्कीमा जाँच चलाएँ:

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
print("स्कीमा स्वीकार किया गया")
'
```

स्कीमा उम्मीदवार अस्वीकार करे तो रुकें। यह चरण हर इंटीग्रेशन या HTTP स्टोर के अपरीक्षित रूप को सत्यापित नहीं करता।

इस उम्मीदवार के लिए स्कीमा जाँच ने `स्कीमा स्वीकार किया गया` प्रिंट किया। किसी अन्य परिणाम पर यह रिकवरी प्रक्रिया रोक दें।

यह मैन्युअल रूपांतरण दिए गए फ़ील्ड के लिए परीक्षित था। TLS सेटिंग्स, भरोसेमंद प्रॉक्सी या लंबित कॉन्फ़िगरेशन वाली फ़ाइल की अलग समीक्षा चाहिए। केवल ऊपर का संस्करण नंबर बदलने से ऐसी प्रोफ़ाइल बचती है जिसे पुराना Core स्वीकार नहीं करता।

मेरे मामले में Supervisor के पास सक्रिय Core काम था और उसने `ha core stop` अस्वीकार कर दिया। मैंने होस्ट कंसोल से Core कंटेनर रोका, सत्यापित उम्मीदवार इंस्टॉल किया और उसे शुरू किया:

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

रोकने के बाद कोई कमांड विफल हो तो `docker start homeassistant` चलाने से पहले सक्रिय HTTP फ़ाइल जाँचें। फ़ाइल बदली हो तो उसकी नई सामग्री से उम्मीदवार फिर बनाएँ। इस चरण के बाद HTTP पृष्ठ लौटा। केवल HTTP जवाब से Core का स्टार्टअप पूरा होना साबित नहीं हुआ, इसलिए सिस्टम को बहाल मानने से पहले मैंने Supervisor की स्थिति जाँची।

इस Yellow पर `docker inspect -f '{{.State.Status}}' homeassistant` ने फिर `running` दिखाया। अगला अपडेट माँगने से पहले `ha core info` और डैशबोर्ड जाँचें।

## अपडेट का परिणाम सत्यापित करें {#verify-the-update-outcome}

HTTP पहुँच लौटने के बाद मैंने Core को 2026.11.1 पर अपडेट किया। उस रिलीज़ का अनुरोध करने के लिए:

```bash
ha core update --version 2026.11.1
```

लंबे स्टार्टअप के बाद कमांड ने विफलता बताई। फिर Supervisor ने Core को RUNNING दर्ज किया और `Successfully started Home Assistant 2026.11.1` लिखा। स्थिति जाँच से पता चला कि इंस्टॉल किया गया रिलीज़ नवीनतम था, HTTP फ़ाइल फिर संस्करण 3.1 में माइग्रेट हुई थी, और निगरानी के दौरान कंटेनर ने रीस्टार्ट नहीं किया। प्रमाणित डैशबोर्ड लोड हुआ। **अपडेट कमांड विफलता बताए, तब भी अंतिम स्थिति जाँचें।**

अपने सिस्टम में लंबे अपडेट के बाद रिलीज़, Supervisor की सेहत और कंटेनर स्थिति जाँचें:

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

इस मामले में पहले और तीसरे कमांड ने ये निजी विवरण हटाए गए परिणाम दिए:

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

फिर अपने सामान्य स्थानीय पते पर डैशबोर्ड खोलें और देखें कि लाइव स्थितियाँ लोड होती हैं। सुरक्षित HTTP फ़ाइल तब तक रखें जब तक अगला बैकअप पूरा न हो और सामान्य संचालन सत्यापित न हो जाए।

मेरे Yellow के साक्ष्य से पहले अपडेट की विफलता का कारण स्थापित नहीं हुआ। बाद के काम का विफलता संदेश भी कारण नहीं बताता। इंस्टॉल किया गया रिलीज़ और स्वस्थ डैशबोर्ड, केवल CLI संदेश से बेहतर परिणाम-साक्ष्य हैं, लेकिन इनमें से कोई भी यह नहीं बताता कि Supervisor ने काम को विफल क्यों चिह्नित किया।

## अगले कदम

HTTP स्टोरेज त्रुटि बनी रहे तो सुरक्षित फ़ाइल जाँचें और संगत बैकअप बहाल करें, या ऐसा Core रिलीज़ चलाएँ जो उसके स्टोरेज संस्करण को पढ़ सके। पुराने Core में सुरक्षित संस्करण 3 फ़ाइल लौटाने पर समस्या दोहराएगी। Core RUNNING तक पहुँचे लेकिन कुछ डिवाइस अनुपलब्ध रहें तो उन इंटीग्रेशन की अलग जाँच करें। अगला बैकअप पूरा होने और डैशबोर्ड के स्थिर रहने तक रिकवरी प्रति और क्लाउड बैकअप रखें।

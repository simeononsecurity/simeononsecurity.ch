---
title: "Bitbucket Cloud SSH कुंजियाँ: AI एजेंटों के लिए केवल-पठन Git पहुँच"
date: 2026-10-11
lastmod: 2026-11-13
toc: true
draft: false
description: "केवल-पठन AI एजेंट कार्यप्रवाह के लिए Bitbucket Cloud SSH कुंजियाँ, Git CLI पहुँच, REST API टोकन, 1Password और MCP उपकरण सेट करें।"
genre: ["क्लाउड सुरक्षा", "डेवलपर उपकरण", "सिस्टम प्रशासन"]
tags: ["Bitbucket Cloud", "Bitbucket SSH कुंजियाँ", "रिपॉज़िटरी पहुँच कुंजियाँ", "प्रोजेक्ट पहुँच कुंजियाँ", "वर्कस्पेस पहुँच कुंजियाँ", "Git CLI", "Bitbucket CLI", "1Password CLI", "1Password SSH Agent", "MCP", "Model Context Protocol", "REST API", "API टोकन स्कोप", "एजेंट अनुमतियाँ", "केवल-पठन स्वचालन", "SSH होस्ट कुंजियाँ"]
cover: "/img/cover/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation.webp"
coverAlt: "टर्मिनल कार्यप्रवाह Bitbucket Cloud Git पहुँच, सीमित-स्कोप SSH कुंजियाँ, 1Password, REST API पठन और MCP उपकरणों को जोड़ता है"
coverCaption: ""
---

**सीमित एजेंट कार्यप्रवाह रिपॉज़िटरी पठन, API पठन, गुप्त जानकारी प्रबंधन और दूरस्थ लेखन को अलग रखता है।** स्रोत तक पहुँचने के लिए Secure Shell (SSH) पर Git का उपयोग करें, स्वचालित checkout के लिए केवल-पठन Bitbucket पहुँच कुंजी, मेटाडेटा के लिए REST API और अनुमोदित उपकरणों के लिए Model Context Protocol (MCP) सर्वर का उपयोग करें। निजी कुंजियाँ और API टोकन 1Password में रखें। लिखने से पहले मानव अनुमोदन लें।

<!--more-->

## मुख्य बातें

- **डिफ़ॉल्ट रूप से केवल-पठन:** एजेंट checkout के लिए रिपॉज़िटरी या प्रोजेक्ट पहुँच कुंजी का उपयोग करें। इनमें से कोई push पहुँच नहीं देती।
- **व्यक्तिगत पहचान:** उपयोगकर्ता खाते से जुड़े इंटरैक्टिव कार्य के लिए व्यक्तिगत SSH कुंजी का उपयोग करें।
- **गुप्त जानकारी की अभिरक्षा:** 1Password SSH Agent का उपयोग करें, ताकि Git निजी कुंजी पढ़े बिना अधिकृत हस्ताक्षर अनुरोध कर सके।
- **CLI का अर्थ:** `git`, `curl` और छोटे ऑडिट किए गए API wrapper को व्यावहारिक Bitbucket कमांड लाइन मानें।
- **MCP सीमा:** सीमित दायरे वाले पठन उपकरण उपलब्ध कराएँ। लेखन उपकरण बंद रखें या अलग अनुमोदन प्रक्रिया के पीछे रखें।
- **लेखन नियंत्रण:** एजेंट को जाँचने, तुलना करने और बदलाव तैयार करने दें। push, pull request, merge या सेटिंग बदलने से पहले व्यक्ति से अनुमोदन लें।

## शुरू करने से पहले

**आवश्यकताएँ:** Bitbucket Cloud पहुँच, Git, OpenSSH क्लाइंट, 1Password 8, 1Password CLI, साइन-इन किया हुआ CLI या अनुमोदित सेवा खाता, और सर्वर अनुमोदन नियंत्रण वाला MCP होस्ट। 45 मिनट रखें। कठिनाई: मध्यम।

पहली कोशिश के लिए परीक्षण रिपॉज़िटरी का उपयोग करें। उदाहरणों के सभी placeholder बदलें। नीचे दिए आदेश अपरीक्षित उदाहरण हैं। वे किसी सक्रिय Bitbucket खाते या रिपॉज़िटरी का प्रतिनिधित्व नहीं करते।

**संस्करण:** यह लेख डिज़ाइन संबंधी मार्गदर्शन देता है, किसी विशेष संस्करण से बँधी रनबुक नहीं। परीक्षण से पहले स्थापित Git, OpenSSH, 1Password CLI, Teamwork Graph CLI, MCP होस्ट और MCP सर्वर के संस्करण जाँचें। `ssh-add -l` चलाने से पहले वर्तमान ऑपरेटिंग सिस्टम के लिए 1Password SSH Agent कॉन्फ़िगर करें।

**क्रेडेंशियल को shell, लॉग, URL, Git remote या स्रोत फ़ाइलों में न रखें।** `<workspace>`, `<repository>`, `<api-token>` और `<socket-path>` जैसे placeholder उपयोग करें। टर्मिनल ट्रांसक्रिप्ट में असली निजी कुंजी न चिपकाएँ।

## पहुँच सीमा चुनें

Bitbucket Cloud रिपॉज़िटरी, प्रोजेक्ट और वर्कस्पेस स्तर पर पहुँच कुंजियों का समर्थन करता है। कुंजी कॉपी होने पर प्रभाव उसका दायरा तय करता है। [आधिकारिक पहुँच-कुंजी तुलना](https://support.atlassian.com/bitbucket-cloud/kb/difference-between-repository-project-and-workspace-access-keys/) अनुमति का अंतर स्पष्ट बताती है।

| पहुँच का तरीका | दायरा | लिखने की क्षमता | उपयुक्त उपयोग |
|---|---|---:|---|
| **रिपॉज़िटरी पहुँच कुंजी** | एक रिपॉज़िटरी | नहीं | डिफ़ॉल्ट एजेंट checkout |
| **प्रोजेक्ट पहुँच कुंजी** | एक प्रोजेक्ट की रिपॉज़िटरी | नहीं | छोटे रिपॉज़िटरी समूह पर केवल-पठन कार्य |
| **वर्कस्पेस पहुँच कुंजी** | एक वर्कस्पेस की रिपॉज़िटरी | हाँ | अलग लेखन योजना वाला नियंत्रित सेवा स्वचालन |
| **व्यक्तिगत SSH कुंजी** | एक उपयोगकर्ता को अनुमत रिपॉज़िटरी | उपयोगकर्ता खाते का अनुसरण करती है | इंटरैक्टिव प्रशासन |
| **API टोकन** | उपयोगकर्ता-आधारित API स्कोप और खाता पहुँच | स्कोप पर निर्भर | REST API पठन या अस्थायी लेखन कार्य |

**सबसे छोटी उपयोगी सीमा से शुरू करें।** एक रिपॉज़िटरी पर्याप्त हो तो रिपॉज़िटरी कुंजी चुनें। कई रिपॉज़िटरी एक प्रोजेक्ट में हों और केवल-पठन पर्याप्त हो तो प्रोजेक्ट कुंजी चुनें। वर्कस्पेस कुंजी को लेखन पहचान मानें, सुविधाजनक डिफ़ॉल्ट नहीं।

Bitbucket सेटिंग के संबंधित मार्ग से सबसे सीमित कुंजी बनाएँ और पंजीकृत करें:

1. एक रिपॉज़िटरी के लिए Repository settings, Access keys और Add key खोलें। सार्वजनिक कुंजी चिपकाएँ और कुंजी को केवल-पठन रखें।
2. कई रिपॉज़िटरी को एक प्रोजेक्ट-सीमित पठन पहचान चाहिए तो Project settings, Access keys और Add key खोलें।
3. वर्कस्पेस पहुँच कुंजी केवल अनुमोदित लेखन डिज़ाइन वाले साझा वर्कस्पेस में उपयोग करें। व्यक्तिगत वर्कस्पेस में यही वर्कस्पेस-स्तरीय मार्ग उपलब्ध नहीं होता।
4. कुंजी का लेबल, दायरा, सार्वजनिक कुंजी fingerprint, स्वामी और रोटेशन तिथि दर्ज करें। निजी कुंजी 1Password में रखें।

पंजीकरण के बाद एक सटीक केवल-पठन कनेक्शन परीक्षण चलाएँ:

```bash
git ls-remote git@bitbucket.org:<workspace>/<repository>.git HEAD
```

**अपेक्षित परिणाम:** `HEAD` के लिए एक commit reference। अपरीक्षित उदाहरण। सफल परिणाम सिद्ध करता है कि एक अनुमत SSH पहचान निर्दिष्ट रिपॉज़िटरी तक पहुँची। यह सिद्ध नहीं करता कि पंजीकृत कुंजी चुनी गई या लेखन पहुँच है। प्रति रिपॉज़िटरी एक कुंजी के कॉन्फ़िगरेशन के बाद परीक्षण फिर चलाएँ।

निजी-कुंजी अभिरक्षा और 1Password SSH Agent की सहमति के लिए [1Password CLI और SSH Agent: AI एजेंटों के लिए सुरक्षित SSH कुंजियाँ](/articles/1password-cli-ssh-keys-mcp-agent-administration/) देखें।

## “Bitbucket CLI” को सही तरह परिभाषित करें

**Bitbucket CLI** वाक्यांश अक्सर तीन अलग इंटरफ़ेसों को मिला देता है। इन्हें अलग रखें।

- **Git CLI:** `git clone` और `git fetch` SSH या HTTPS से रिपॉज़िटरी डेटा ले जाते हैं। `git diff` स्थानीय फ़ाइलों या revisions की तुलना करता है।
- **REST क्लाइंट:** `curl` या समीक्षित wrapper Bitbucket Cloud Representational State Transfer (REST) API को कॉल करता है। API डेटा या कार्रवाई माँगने का प्रोग्रामेटिक इंटरफ़ेस है। [Bitbucket Cloud REST API संदर्भ](https://developer.atlassian.com/cloud/bitbucket/rest/) रिपॉज़िटरी, स्रोत, शाखा, pull request, pipeline और स्थिति संसाधन सूचीबद्ध करता है।
- **Atlassian CLI:** `acli` Atlassian का आधिकारिक कमांड लाइन है। इसका [परिचय](https://developer.atlassian.com/cloud/acli/guides/introduction/) उत्पाद बताता है, जबकि इसका [कमांड संदर्भ](https://developer.atlassian.com/cloud/acli/reference/commands/) `admin`, `jira`, `feedback` और `rovodev` इंटरफ़ेस सूचीबद्ध करता है। संदर्भ Bitbucket Cloud कमांड नहीं बताता।

**Atlassian का आधिकारिक `acli` कमांड संदर्भ Bitbucket Cloud कमांड नहीं बताता।** `acli bitbucket clone` जैसा कमांड न गढ़ें। Git कार्यों के लिए Git और Bitbucket Cloud डेटा के लिए REST API उपयोग करें।

### वैकल्पिक Teamwork Graph CLI

**Atlassian Teamwork Graph CLI, यानी `twg`, भी प्रकाशित करता है।** इसका [अवलोकन](https://developer.atlassian.com/cloud/twg-cli/) और [कमांड सूची](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/commands/commands-catalog/) Bitbucket कमांड समूह दस्तावेज़ित करते हैं। सेटअप कमांड है:

```bash
twg setup
```

सेटअप कमांड स्थानीय प्रमाणीकरण स्थिति बदलता है। वैकल्पिक Bitbucket टोकन कॉन्फ़िगरेशन के लिए स्थापित संस्करण के संकेतों का पालन करें। CLI का Bitbucket टोकन मार्ग Atlassian OAuth से अलग है। कमांड का सटीक syntax स्थापित संस्करण और वर्तमान कमांड सूची से मिलाएँ। बदलाव करने वाले कमांडों के लिए अलग profile, सीमित टोकन, समीक्षित स्थापित कौशल और मानव अनुमोदन उपयोग करें।

**अपेक्षित परिणाम, अपरीक्षित:** अलग profile को Bitbucket प्रमाणीकरण सेटिंग मिलती है। सेटअप से पहले profile की पिछली स्थिति दर्ज करें। rollback करते समय स्थापित संस्करण की दस्तावेज़ित logout या configuration हटाने की प्रक्रिया से सहेजी credential हटाएँ।

यदि कोई तृतीय-पक्ष परियोजना स्वयं को Bitbucket CLI कहती है, तो उसका स्रोत, रिलीज़ प्रक्रिया, checksums, अपडेट मार्ग, प्रमाणीकरण प्रवाह, माँगे गए scopes, नेटवर्क गंतव्य, लॉग प्रबंधन और लेखन कमांड जाँचें। जाना-पहचाना binary नाम विक्रेता समर्थन या सुरक्षित अनुमतियाँ सिद्ध नहीं करता।

## SSH कुंजियों को 1Password के नियंत्रण में रखें

[1Password SSH Agent](https://www.1password.dev/ssh/agent) 1Password में संग्रहीत SSH कुंजियाँ Git और SSH क्लाइंटों को उपलब्ध कराता है। क्लाइंट अधिकृत हस्ताक्षर अनुरोध करता है। निजी कुंजी 1Password ऐप के भीतर रहती है, और अनुमोदित क्लाइंट के उपयोग से पहले 1Password सहमति माँगता है।

[1Password CLI संदर्भ](https://www.1password.dev/cli/reference) की भूमिका अलग है। item, API टोकन, सेवा खाते और स्वचालन सेटअप तक नियंत्रित पहुँच के लिए `op` उपयोग करें। SSH हस्ताक्षर के लिए SSH Agent उपयोग करें। एजेंट कार्यप्रवाह आसान करने के लिए निजी कुंजी को अस्थायी फ़ाइल में export न करें।

केवल-पठन कमांड से स्थानीय CLI और agent स्थिति जाँचें:

```bash
op --version
ssh-add -l
```

**अपेक्षित परिणाम:** 1Password CLI संस्करण और सक्रिय agent के एक या अधिक सार्वजनिक-कुंजी fingerprints। अपरीक्षित उदाहरण। `ssh-add -l` का खाली परिणाम बताता है कि चुने गए agent socket से कोई कुंजी उपलब्ध नहीं है।

नई कुंजी के लिए 1Password में Ed25519 SSH Key item बनाएँ या विश्वसनीय स्थानीय प्रक्रिया से बनाई कुंजी import करें। उद्देश्य, दायरा और रोटेशन तिथि के अनुसार लेबल दें। Bitbucket Cloud में केवल सार्वजनिक कुंजी जोड़ें। [Linux रिपॉज़िटरी पहुँच-कुंजी मार्गदर्शिका](https://support.atlassian.com/bitbucket-cloud/docs/set-up-repository-access-keys-on-linux/) रिपॉज़िटरी सेटिंग मार्ग और केवल-पठन सीमा बताती है।

## पहले Bitbucket host key सत्यापित करें

SSH उपयोगकर्ता प्रमाणीकरण सर्वर की पहचान सिद्ध नहीं करता। प्रमाणीकरण अनुरोध भेजने से पहले क्लाइंट को Bitbucket Cloud host key सत्यापित करनी चाहिए। Atlassian की [SSH और two-step verification मार्गदर्शिका](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/) सार्वजनिक host keys सूचीबद्ध करती है और known-host entries पाने का आधिकारिक endpoint दिखाती है।

तुलना के लिए सार्वजनिक host-key डेटा प्राप्त करें:

```bash
curl --fail --silent --show-error https://bitbucket.org/site/ssh
```

**अपेक्षित परिणाम:** `bitbucket.org` के लिए OpenSSH `known_hosts` पंक्तियाँ। अपरीक्षित उदाहरण। `~/.ssh/known_hosts` में पंक्ति रखने से पहले लौटाई गई कुंजी या fingerprint की स्वतंत्र विश्वसनीय प्रति से तुलना करें।

अनुमोदित entry जुड़ने के बाद strict host checking उपयोग करें:

```sshconfig
Host bitbucket.org
    StrictHostKeyChecking yes
    UserKnownHostsFile ~/.ssh/known_hosts
```

**एजेंट चलते समय बदली हुई host key स्वीकार न करें।** प्रक्रिया रोकें, Bitbucket Cloud का वर्तमान host-key रिकॉर्ड जाँचें और स्थानीय `known_hosts` entry देखें। स्वतः स्वीकृति कुंजी-आधारित सुरक्षा सीमा हटाती है।

## प्रति रिपॉज़िटरी एक कुंजी चुनें

एक डिवाइस में अक्सर कई Bitbucket कुंजियाँ होती हैं। व्यापक SSH agent एक कनेक्शन में कई पहचानें देता है। कम authentication-attempt सीमा वाला सर्वर या नीति पहले कुंजियाँ विफल होने के बाद सही कुंजी भी अस्वीकार कर सकती है।

Atlassian की [एक डिवाइस पर कई रिपॉज़िटरी पहुँच-कुंजियों की मार्गदर्शिका](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) रिपॉज़िटरी Git configuration फ़ाइल में `core.sshCommand` और global Git configuration में `includeIf` उपयोग करती है। प्रति रिपॉज़िटरी एक कुंजी के लिए यही तरीका अपनाएँ।

फ़ाइल-आधारित पोर्टेबल उदाहरण:

```ini
# एक स्थानीय रिपॉज़िटरी के भीतर .gitconfig
[core]
    sshCommand = ssh -o IdentitiesOnly=yes -i ~/.ssh/<repository-automation-key>
```

```ini
# ~/.gitconfig
[includeIf "gitdir:~/src/<repository>/"]
    path = ~/src/<repository>/.gitconfig
```

ऊपर का block समर्पित स्वचालन पहचान के लिए फ़ाइल-आधारित निजी-कुंजी अपवाद है। यह 1Password SSH Agent कॉन्फ़िगर नहीं करता। 1Password SSH Agent के लिए [1Password सेटअप मार्गदर्शिका](https://www.1password.dev/ssh/get-started) से मंच-विशिष्ट `IdentityAgent` या `SSH_AUTH_SOCK` मान कॉन्फ़िगर करें। कुछ OpenSSH कॉन्फ़िगरेशन `.pub` फ़ाइल को agent identity selector के रूप में उपयोग करते हैं। उपयोग से पहले मंच समर्थन जाँचें। फ़ाइल-आधारित सेटअप को मेल खाती निजी-कुंजी का path चाहिए। निजी-कुंजी सामग्री माँगने वाले कमांड को `.pub` फ़ाइल न दें और व्यक्तिगत निजी कुंजी export न करें।

स्थानीय clone को एक कुंजी चाहिए तो स्पष्ट repository configuration उपयोग करें। एक directory में समान पहुँच सीमा वाले कई clone हों तो `includeIf` उपयोग करें। [बहु-कुंजी मार्गदर्शिका](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) Bitbucket कार्यप्रवाह में दोनों सेटिंग दिखाती है।

SSH पर Git से clone करें:

```bash
git clone git@bitbucket.org:<workspace>/<repository>.git <local-directory>
```

**अपेक्षित परिणाम:** Git `<local-directory>` बनाता है और `bitbucket.org` के ज़रिए रिपॉज़िटरी प्राप्त करता है। अपरीक्षित उदाहरण। रिपॉज़िटरी पहुँच कुंजी केवल clone और pull देती है।

## सीमित REST पठन के लिए API टोकन उपयोग करें

Git परिवहन के लिए SSH उपयोग करें। मेटाडेटा या Git परिवहन से बाहर के कार्यों के लिए REST API उपयोग करें। [API token permission मार्गदर्शिका](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/) Read, Write, Admin और Delete जैसे repository scopes सूचीबद्ध करती है। Repository Read का मान `read:repository:bitbucket` है और इसमें pull request पहुँच नहीं है।

पठन स्वचालन के लिए Bitbucket repository या project access token को प्राथमिकता दें, यदि लक्ष्य आवश्यक endpoint का समर्थन करता है। उपयोगकर्ता-आधारित API टोकन खाते की व्यापक पहुँच रखता है। workspace access token तभी उपयोग करें जब कार्य रिकॉर्ड उस व्यापक सीमा को बताए। टोकन प्रकार चुनने से पहले [Bitbucket access-token मार्गदर्शिका](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/) देखें।

एजेंट के पठन मार्ग में `read:repository:bitbucket` से शुरू करें। `read:pullrequest:bitbucket` तभी जोड़ें जब एजेंट को pull request डेटा चाहिए। workspace या pipeline scopes तभी जोड़ें जब कार्य रिकॉर्ड endpoint और परिणाम बताए। Write और admin scopes के लिए अलग अनुमोदन मार्ग चाहिए।

हर API टोकन एक उद्देश्य के लिए बनाएँ, समाप्ति तिथि रखें, rotation रिकॉर्ड में तिथि लिखें और समाप्ति से पहले टोकन बदलें। Atlassian की [API टोकन निर्माण मार्गदर्शिका](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/) नाम, समाप्ति तिथि, ऐप चयन और scopes माँगती है। बनाने के बाद टोकन केवल एक बार दिखता है।

मान 1Password या प्रबंधित runtime secret में रखें। इसे remote URL में न रखें। bearer token को environment variable से केवल उस प्रक्रिया तक भेजें जिसे एक पठन करना है:

```bash
op run --env-file=/path/to/agent.env -- \
sh -c 'curl --fail --silent --show-error \
  --request GET \
  --url "https://api.bitbucket.org/2.0/repositories/<workspace>/<repository>" \
  --header "Authorization: Bearer ${BITBUCKET_API_TOKEN}" \
  --header "Accept: application/json"'
```

`/path/to/agent.env` को रिपॉज़िटरी के बाहर रखें। फ़ाइल में `BITBUCKET_API_TOKEN=op://synthetic-vault/synthetic-api-token/credential` जैसा संदर्भ रखें। `op run` संदर्भ हल करता है और subprocess की अवधि तक curl child process को मान देता है। इससे child process को environment variable का मान पढ़ने या लॉग करने से नहीं रोका जाता। placeholder को वास्तविक token से न बदलें।

**अपेक्षित परिणाम:** चुनी हुई रिपॉज़िटरी का JSON metadata। अपरीक्षित उदाहरण। placeholder कभी committed फ़ाइल या लॉग में असली टोकन न बने।

लंबे स्वचालन में समर्थित CLI या service-account प्रवाह के ज़रिए 1Password को process environment में secret डालने दें। टोकन की अवधि कार्य के अनुसार रखें। काम जल्दी समाप्त हो या host का स्वामित्व बदले तो टोकन रद्द करें।

## MCP को छोटा पठन क्षेत्र दें

नए सर्वर की समीक्षा में [वर्तमान MCP विनिर्देश](https://modelcontextprotocol.io/specification/2026-07-28) और उसके [authorization नियम](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) उपयोग करें। HTTP सर्वर को token audience जाँच और 401 तथा 403 उत्तरों का स्पष्ट प्रबंधन चाहिए।

MCP host उपयोगकर्ता की सहमति लेता है। client एक सर्वर से जुड़ा रहता है। सर्वर tools, resources या prompts उपलब्ध कराता है। स्रोत, transport, account और permissions की समीक्षा पूरी होने तक हर सर्वर को अविश्वसनीय कोड मानें।

अगले अनुच्छेद का 2025-06-18 विनिर्देश URL ऐतिहासिक संस्करण है। नई समीक्षाओं के लिए वर्तमान 2026-07-28 विनिर्देश उपयोग करें।

[MCP विनिर्देश](https://modelcontextprotocol.io/specification/2025-06-18) MCP host, client और server के बीच संचार तय करता है। सर्वर protocol के ज़रिए tools, resources या prompts उपलब्ध कराता है। MCP connection format मानकीकृत करता है। फिर भी host, server implementation, account, token scope और अनुमोदन नीति तय करते हैं कि call कहाँ तक पहुँचता है।

Git और Bitbucket Cloud REST API के ऊपर संकीर्ण adapter के रूप में MCP सर्वर उपयोग करें।

adapter को token passthrough, server-side request forgery (SSRF) और confused-deputy व्यवहार से सुरक्षित रखें। SSRF में सर्वर अनपेक्षित गंतव्यों को अनुरोध भेजता है। confused-deputy व्यवहार तब होता है जब सर्वर caller की ओर से व्यापक अधिकार उपयोग करता है। दुर्भावनापूर्ण स्थानीय सर्वर, असुरक्षित OAuth redirects और अत्यधिक बड़े source-data उत्तरों से भी बचाएँ। अनुमत Bitbucket origins और repository identifiers तय करें। स्थानीय सर्वर को समर्पित operating-system user के तहत sandbox में चलाएँ। tool results और logs में secrets छिपाएँ।

यह खंड डिज़ाइन बताता है, परीक्षित MCP कॉन्फ़िगरेशन नहीं। कोई client, server, transport, version या fixture तय नहीं है। production repository से एजेंट जोड़ने से पहले अलग test profile में केवल-पठन server सत्यापित करें।

पठन टूल के उदाहरण:

| टूल | सीमित परिणाम |
|---|---|
| **`get_repository_metadata`** | एक रिपॉज़िटरी का metadata देता है |
| **`read_source_file`** | एक revision पर एक path पढ़ता है |
| **`list_branches`** | एक रिपॉज़िटरी की शाखाएँ सूचीबद्ध करता है |
| **`get_pull_request`** | token में pull request read scope होने पर एक pull request देता है |
| **`get_build_status`** | एक commit की स्थिति डेटा देता है |

ये नाम डिज़ाइन बताते हैं। ये Atlassian कमांड नाम नहीं हैं। सर्वर को मनमाने URL, shell command, raw token, निजी-कुंजी export अनुरोध या असीमित repository identifier स्वीकार करने से रोकें।

चार स्तरों पर अनुमतियाँ तय करें:

1. **Bitbucket Cloud:** Git के लिए repository या project read key, और REST पठन के लिए न्यूनतम API token scopes।
2. **1Password:** कार्य के लिए एक vault या service account, निजी-कुंजी export मार्ग के बिना।
3. **MCP सर्वर:** read tools की allowlist, स्थिर Bitbucket Cloud endpoints, input validation, timeout limits और redacted logs।
4. **MCP host:** सर्वर और हर लेखन-सक्षम कार्रवाई के लिए उपयोगकर्ता की स्वीकृति; डिफ़ॉल्ट profile में लेखन उपकरण बंद।

*MCP टूल सूची खोजे जाने का प्रमाण है। यह authorization, सही scope, सुरक्षित input handling या सही परिणाम साबित नहीं करती।*

## एजेंट कार्यप्रवाह चरणबद्ध करें

कार्यप्रवाह स्पष्ट रखें। हर चरण अगले चरण के लिए प्रमाण देता है।

| चरण | एजेंट की कार्रवाई | अनुमति | मानव नियंत्रण |
|---|---|---|---|
| **तैयारी** | कॉन्फ़िगरेशन, host-key रिकॉर्ड, कुंजी लेबल, token scope और समाप्ति पढ़ें | स्थानीय पठन | सेटअप रिकॉर्ड अनुमोदित करें |
| **निरीक्षण** | SSH पर Git से clone या fetch करें और REST metadata पूछें | रिपॉज़िटरी और API पठन | सेटअप के बाद कुछ नहीं |
| **विश्लेषण** | अनुमोदित टूल से फ़ाइलें, शाखाएँ, pull request और build status पढ़ें | केवल-पठन MCP टूल | सीमित पठन के लिए कुछ नहीं |
| **बदलाव तैयार करें** | स्थानीय workspace में patch, branch योजना या pull request draft बनाएँ | केवल स्थानीय लेखन | diff और लक्ष्य की समीक्षा |
| **लेखन अनुमोदित करें** | सटीक remote कार्रवाई, scope और rollback मार्ग प्रस्तुत करें | अभी remote write नहीं | मानव अनुमोदन |
| **लेखन करें** | branch push करें, pull request बनाएँ या write endpoint call करें | अल्पकालिक write identity | हर कार्रवाई की पुष्टि |
| **सत्यापन** | परिणामी commit, pull request या स्थिति पढ़ें | फिर केवल-पठन | अपेक्षित परिणाम की पुष्टि |

डिफ़ॉल्ट एजेंट profile को **विश्लेषण** या **बदलाव तैयार करें** के बाद रुकना चाहिए। अलग write profile में अलग token या key, कम अवधि, निश्चित लक्ष्य और अनुमोदन prompt होना चाहिए। रिपॉज़िटरी पहुँच कुंजी लेखन चरण नहीं कर सकती, इससे उपयोगी तकनीकी सीमा बनती है।

## रोलबैक और हटाना

पहले पहुँच हटाएँ, फिर स्थानीय कॉन्फ़िगरेशन साफ़ करें:

1. संबंधित Bitbucket सेटिंग पृष्ठ से रिपॉज़िटरी, प्रोजेक्ट या वर्कस्पेस पहुँच कुंजी हटाएँ।
2. संबंधित Bitbucket सुरक्षा पृष्ठ में रिपॉज़िटरी, प्रोजेक्ट, वर्कस्पेस या उपयोगकर्ता API टोकन रद्द करें।
3. स्थापित CLI संस्करण के लिए दस्तावेज़ित [authentication प्रक्रिया](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/getting-started/how-authentication-works/) से सहेजी Teamwork Graph credential हटाएँ। पिछली credential केवल अनुमोदित secret manager में रखें। पुष्टि करें कि अलग profile में परीक्षण credential अब सूचीबद्ध नहीं है।
4. परीक्षण समाप्त होने पर रिपॉज़िटरी `.gitconfig` फ़ाइल और उसकी `includeIf` प्रविष्टि हटाएँ। असंबंधित Git कॉन्फ़िगरेशन न बदलें।
5. परीक्षण के लिए जोड़ी गई केवल सत्यापित Bitbucket host-key पंक्ति हटाएँ। अन्य अनुमोदित host keys रखें।
6. बाहरी `agent.env` फ़ाइल और अस्थायी output हटाएँ। host configuration से MCP server entry हटाएँ और फिर host पुनः चालू करें।

हर हटाने की कार्रवाई, ऑपरेटर और समय दर्ज करें। कोई मान अनपेक्षित log, process record या transcript में आ जाए तो key या token घुमाएँ।

## स्थानीय संदर्भ अपडेट के साथ दूरस्थ-पठन चक्र

बार-बार रिपॉज़िटरी जाँचने के लिए छोटा चक्र अपनाएँ:

```bash
LOCAL_REPO="<local-directory>"
git -C "$LOCAL_REPO" fetch --no-tags
git -C "$LOCAL_REPO" status --short --branch
git -C "$LOCAL_REPO" log -1 --format='%H %ad %s' --date=iso-strict
```

`HEAD` रिपॉज़िटरी का वर्तमान checkout reference है। सफल परिणाम सिद्ध करता है कि अनुमत SSH पहचान निर्दिष्ट रिपॉज़िटरी तक पहुँची। यह सिद्ध नहीं करता कि कौन-सी कुंजी चुनी गई या push पहुँच मौजूद है।

**अपेक्षित परिणाम:** fetch परिणाम, branch स्थिति और एक commit पंक्ति। अपरीक्षित उदाहरण। `fetch` remote पर नहीं लिखता, लेकिन स्थानीय references और `FETCH_HEAD` अपडेट करता है। चक्र push नहीं करता और शाखा नहीं बदलता।

MCP server को नामित operations के ज़रिए वही read boundary उपलब्ध करानी चाहिए। स्थानीय shell wrapper या MCP tool अनुरोध भेजने से पहले write verb अस्वीकार करे। tool name, repository placeholder, revision, result class और अवधि लॉग करें। जब तक काम के लिए एक फ़ाइल स्पष्ट रूप से ज़रूरी न हो, token, cookie, निजी path और फ़ाइल सामग्री छिपाएँ।

## समस्या निवारण

### `Permission denied (publickey)`

सक्रिय agent socket, चुनी public key, repository access-key entry और `IdentitiesOnly` जाँचें। लक्ष्य repository या project पर repository key मौजूद होनी चाहिए। व्यक्तिगत key के लिए खाते की अनुमति चाहिए। workspace access key की लेखन सीमा अलग होती है।

### गलत repository key दी जाती है

`core.sshCommand` से प्रति repository एक key उपयोग करें, या `includeIf` नियंत्रित directory में clone समूहित करें। `ssh-add -l` से agent keys सूचीबद्ध करें। कई 1Password keys उपलब्ध हों तो स्पष्ट identity selector या 1Password SSH bookmark उपयोग करें। [1Password Agent मार्गदर्शिका](https://www.1password.dev/ssh/agent) key संख्या और bookmark विचार बताती है।

### SSH बदली हुई host key बताता है

एजेंट रोकें। पहली प्रतिक्रिया में `known_hosts` न मिटाएँ। स्वतंत्र माध्यम से Bitbucket Cloud के वर्तमान host-key record की स्थानीय entry से तुलना करें। तुलना सही होने के बाद ही entry हटाएँ या बदलें।

### API `401` या `403` लौटाता है

token समाप्ति, प्रकार, endpoint scope और account या workspace सीमा जाँचें। repository read scope में pull request नहीं आते। write endpoint के लिए write scope और अनुमोदित write profile चाहिए। विफल endpoint का नाम जाने बिना scopes न बढ़ाएँ।

### API repository डेटा देता है लेकिन pull request नहीं

नए या घुमाए गए token में न्यूनतम pull request read scope जोड़ें। केवल-पठन MCP server के लिए व्यापक user token दोबारा उपयोग न करें।

### MCP server टूल दिखाता है लेकिन call विफल होता है

server registration, connection, tool discovery, execution और result verification को अलग-अलग देखें। token उजागर किए बिना server log देखें। endpoint और input shape सत्यापित करें। connectivity जाँचने के बाद एक बार फिर कोशिश करें। दूसरी call विफल हो तो कार्रवाई अधूरी चिह्नित करें।

### तृतीय-पक्ष Bitbucket CLI व्यापक पहुँच माँगता है

इंस्टॉलेशन रोकें। माँगी गई पहुँच की तुलना कार्य रिकॉर्ड से करें। source, release signatures या checksums, नेटवर्क गंतव्य, secret storage और लेखन व्यवहार जाँचें। आधिकारिक Atlassian CLI कमांड संदर्भ तृतीय-पक्ष Bitbucket binary समर्थन सिद्ध नहीं करता।

## अगले कदम

रिपॉज़िटरी या प्रोजेक्ट दायरा, कुंजी लेबल, host-key सत्यापन तिथि, API scopes, token समाप्ति, 1Password स्वामी, MCP tool allowlist, लॉग नीति और लेखन अनुमोदक सहित संक्षिप्त पहुँच रिकॉर्ड बनाएँ।

ट्रांसक्रिप्ट में placeholders रखकर एक केवल-पठन clone, एक REST metadata पठन और एक MCP tool पठन चलाएँ। परिणामों की तुलना करें। रिकॉर्ड और लॉग की समीक्षा होने तक एजेंट profile केवल-पठन रखें।

लेखन कार्य आने पर पहले स्थानीय diff तैयार करें। लक्ष्य branch, बदले पथ, अनुरोधित API method, token scope और rollback चरण प्रस्तुत करें। सटीक कार्रवाई पर मानव अनुमोदन मिलने के बाद ही अलग अल्पकालिक write identity उपयोग करें।

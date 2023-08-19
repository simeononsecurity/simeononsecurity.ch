---
title: "قم ببناء صندوق دخل سلبي مربح باستخدام أجهزة منخفضة الطاقة: دليل"
draft: false
toc: true
date: 2023-02-07
description: "تعرف على كيفية إعداد عامل منجم للعملات المشفرة منخفض الدخل باستخدام Raspberry Pi أو Intel NUC ، واكسب من 10 إلى 20 دولارًا شهريًا لكل صندوق باستخدام هذا الدليل"
tags: ["قم ببناء صندوق دخل سلبي مربح", "أجهزة منخفضة الطاقة", "الدخل السلبي", "عامل منجم التشفير", "فطيرة التوت", "إنتل NUC", "مرشد", "متطلبات الأجهزة", "تثبيت نظام التشغيل", "تثبيت البرامج", "عامل ميناء", "تحديثات حاوية Docker التلقائية", "خادم أوبونتو", "سطح مكتب أوبونتو", "راسبيان", "ميزانية", "USFF", "صغير الحجم", "ميني", "كمبيوتر مايكرو", "الخبرة الفنية", "EarnApp", "مايست", "Peer2Profit", "العسل", "TraffMonitizer", "برج المراقبة", "بيتينج", "تحديثات Linux", "أوبونتو", "ديبيان", "CentOS", "RHEL", "التحديثات في وضع عدم الاتصال", "المستودع المحلي", "مخبأ", "إعداد الخادم", "إعداد العميل", "مرآة مناسبة", "debmirror", "مبتدئ", "apt-cacher-ng", "يم كرون", "تحديثات نظام Linux", "تحديثات الحزمة في وضع عدم الاتصال", "تحديثات البرامج في وضع عدم الاتصال", "مستودع الحزم المحلي", "ذاكرة التخزين المؤقت للحزمة المحلية", "تحديثات Linux في وضع عدم الاتصال", "التعامل مع التحديثات في وضع عدم الاتصال", "طرق التحديث حاليا", "صيانة النظام حاليا", "تحديثات خادم Linux", "تحديثات عميل Linux", "إدارة البرامج في وضع عدم الاتصال", "إدارة الحزمة حاليا", "تحديث الاستراتيجيات", "تحديثات أمان Linux"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "لوحة دوائر خضراء على شكل صندوق به رموز اتصال بالإنترنت كأسلاك متصلة بها."
coverCaption: ""
---

** أنشئ صندوق دخل سلبي مربحًا باستخدام أجهزة منخفضة الطاقة: دليل **
كثير من الناس في هذه الأيام يعملون في تعدين العملات المشفرة وعمال المناجم منخفضة الطاقة مثل عمال مناجم الهيليوم. هذه رائعة وكلها لكنها لم تعد تكسب كل هذا القدر بعد الآن وهي تركز على نوع واحد من المكاسب. سنقوم اليوم ببناء صندوق دخل سلبي منخفض الطاقة يكسب ما يتراوح بين 10 دولارات و 20 دولارًا شهريًا لكل صندوق وعنوان IP سكني.

* إذا كانت لديك القدرة على إعداد هذا المربع على شبكة ضيف أو شبكة محلية ظاهرية منفصلة بشكل أفضل ، فافعل ذلك. بالرغم من أن هذه مدونة أمنية ، لا يمكننا افتراض مخاوف الجميع المتعلقة بالأمان وتحمل المخاطر. *

## متطلبات الأجهزة:
مطلوب واحد مما يلي. نحتاج بشكل أساسي إلى أي جهاز كمبيوتر فعال ومنخفض الطاقة يمكننا الحصول عليه. أي Raspberry PI أو Intel NUC أو ما شابه ذلك سيفي بالغرض. لا يجب أن يكونوا بهذه القوة. ومع ذلك ، أوصي بأن يكون لديك ما لا يقل عن 32 جرامًا - 64 جرامًا للتخزين ، و 4 جرام من ذاكرة الوصول العشوائي ، وما لا يقل عن 2 من خيوط وحدة المعالجة المركزية. لهذا سنستهدف ميزانية تتراوح بين 100 دولار و 200 دولار للأجهزة ولكن لا تتردد في الارتفاع إذا كان ذلك يناسب احتياجاتك. هدف قوتنا هو aprox. متوسط 25 واط.
### فطيرة التوت:
من الصعب الحصول عليها في هذه الأيام لكنها طاقة منخفضة للغاية وقابلة للتخصيص تمامًا. للحصول على معلومات حول كيفية تثبيت raspian على Raspberry PI الخاص بك
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### إنتل نوك:
مجموعة متنوعة من النماذج هناك. لا تتردد في اختيار أحدث.
- [Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
- [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
- [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### أي جهاز كمبيوتر USFF / Tiny / Mini / Micro:
- [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
- [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### أي جهاز كمبيوتر صغير مع Intel N5100 أو ما شابه ذلك
للحصول على مكافئ Raspberry Pi منخفض الطاقة للغاية ولكن على منصة x64.
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## تثبيت نظام التشغيل:
لن ندخل في التفاصيل الفنية حول كيفية تثبيت نظام التشغيل هنا. ومع ذلك ، إليك بعض الموارد الرائعة لتبدأ بها
### راسببيان:
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### أوبونتو:
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## تثبيت البرامج:
سيكون هذا قسمًا أطول. سنقوم بإعداد docker ومن ثم من خلال docker سنقوم بإعداد تحديثات تلقائية لحاوية docker وتثبيت عدة حاويات docker. نفترض أيضًا أنك تستخدم خادم ubuntu ، ولكن أوامر خادم ubuntu و ubuntu desktop و raspbian يجب أن تكون جميعها متشابهة.

* بالنسبة لهذا القسم ، نفترض بعض الخبرة الفنية الأساسية وأنك قمت بتثبيت نظام التشغيل الخاص بك بالفعل بالإضافة إلى معرفة كيفية الدخول إلى الجهاز. *

### تثبيت التحديثات:
نريد أولاً التأكد من تحديث نظامنا بالكامل:
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### تثبيت Docker:
نحتاج إلى إلغاء تثبيت أي إصدارات حالية تأتي معدة مسبقًا مع نظام التشغيل وتثبيت أحدث إصدارات Docker نفسها.
```bash
sudo apt-get remove -y docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### تثبيت برج المراقبة:
تقوم حاوية عامل الإرساء هذه تلقائيًا بتحديث جميع حاويات عامل الإرساء إلى أحدث الصور على فترات منتظمة وتنظيف الصور القديمة (القديمة).
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### تثبيت Bitping:
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

يوفر لك Bitping القدرة على الحصول على أموال في Solana مقابل توفير عقدة للشركات لإجراء اختبارات شبكة خفيفة الوزن من شبكتك.
يبلغ متوسط هذا حوالي 0.1 سنتًا يوميًا لكل عقدة. لا أعرف الكثير ، لكن لديه إمكانات ودفعه سهل.

#### إنشاء حساب:
قم بإنشاء حساب على [bitping.com](https://bitping.com)

#### تثبيت حاوية عامل الإرساء:
الخطوة الأولى. قم بتشغيل هذه الأوامر أولاً لأنها ترشدك خلال إعداد الحاوية الخاصة بك ويطلب منك تسجيل الدخول.
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

اضغط على CTRL + C على لوحة المفاتيح للهروب من الحاوية بعد تسجيل الدخول باستخدام حساب bitping الخاص بك.

الخطوة 2. قم بتشغيل هذا الأمر لاستمرار الحاوية في الخلفية
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### تثبيت تطبيق Earn:
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/c1dllee)

يتيح لك تطبيق Earn مشاركة الإنترنت الخاص بك كخدمة VPN للحصول على قدر مذهل من المكافآت. متوسطات حوالي 5 دولارات شهريًا لكل عقدة لكل IP سكني. يقدم مدفوعات عبر بطاقات هدايا paypal و amazon.

#### إنشاء حساب كسب التطبيق:
قم بإنشاء حساب على [earnapp.com](https://earnapp.com/i/c1dllee)
* تحذير يتطلب حساب جوجل *

#### تثبيت الإصدار بدون عامل تشغيل من التطبيق للحصول على UUID الخاص بك:
تأكد من إلغاء التثبيت بعد حصولك على UUID الخاص بك وإلا فسوف ينتهي بك الأمر إلى تشغيله مرتين على نفس المضيف وبدون تحديثات تلقائية
- [Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### تثبيت حاوية عامل الإرساء:
قم بتعديل السلسلة قبل لصقها في الجهاز الطرفي. تحتاج إلى تحديد UUID الخاص بالتطبيق الذي تم كسبه.
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### فيديو تعليمي:
{{< youtube id="tt499o0OjGU" >}}

### تثبيت Honey Gain:
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/DAVID07A75)

يتيح لك Honey Gain مشاركة الإنترنت الخاص بك كخدمة VPN للحصول على قدر مذهل من المكافآت. متوسطات حوالي 5 دولارات شهريًا لكل عقدة لكل IP سكني. يمكن أن تكون المدفوعات معقدة. اقرأ المزيد قبل أن تقرر استخدام هذه الحاوية

#### إنشاء حساب كسب العسل:
قم بإنشاء حساب على [honeygain.com](https://r.honeygain.me/DAVID07A75)

#### تثبيت Docker Container:
قم بتعديل السلسلة بالبريد الإلكتروني الواضح وكلمة المرور واسم الجهاز قبل اللصق في الجهاز
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### تعليمات بديلة لـ Raspberry Pi
- [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### فيديو تعليمي:
{{< youtube id="Wd11M0nSy1k" >}}

### تثبيت PawnsApp:
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=2092882)
يقدم تطبيق Pawns ، الذي يشبه التطبيقات الأخرى المدرجة هنا ، الدفع لك مقابل مشاركة الإنترنت الخاص بك. الحد الأدنى للدفع هو 5 دولارات. متوسط الدفع هو 0.50 دولار شهريًا لكل عقدة لكل IP.

#### إنشاء حساب PawnsApp:
قم بإنشاء حساب على [https://pawns.app](https://pawns.app/?r=2092882)

#### تثبيت Docker Container:

قم بتعديل ما يلي بالبريد الإلكتروني وكلمة المرور واسم الجهاز ومعرف الجهاز قبل النسخ إلى جهازك الطرفي.
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

### تثبيت Peer 2 Profit:
[*SHARE YOUR TRAFFIC AND PROFIT ON IT!*](https://t.me/peer2profit_app_bot?start=16538445386293aa3aaec4e)

على غرار EarnApp و HoneyGain ، يشارك Peer2Profit الإنترنت الخاص بك لأغراض VPN و Scraping. يكسب حوالي 1 دولار شهريًا لكل عقدة لكل IP.
يقدم مجموعة متنوعة من المدفوعات بما في ذلك الحوالات المالية و BTC و LTC و LTC و MATIC وما إلى ذلك.

#### إنشاء حساب ربح Peer 2:
قم بإنشاء حساب على [peer2profit.com](https://t.me/peer2profit_app_bot?start=16538445386293aa3aaec4e)

#### تثبيت Docker Container:
```bash
export P2P_EMAIL="your_email_without_quotes"; 
docker rm -f peer2profit || true && docker run -td --restart always \
        -e P2P_EMAIL=$P2P_EMAIL \
        --name peer2profit \
        peer2profit/peer2profit_linux:latest 
```
#### فيديو تعليمي:
{{< youtube id="J_rSV5N8aQk" >}}


### تثبيت Repocket:
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

على غرار العروض الأخرى هنا. حد أدنى 20 دولارًا للدفع. يمكن أن تكون المدفوعات معقدة. ابحث بنفسك لمعرفة ما إذا كنت تريد استخدام هذه الخدمة. متوسط المدفوعات حوالي 1 دولار لكل عقدة لكل صندوق في الشهر.

#### إنشاء حساب Repocket:
قم بإنشاء حساب على [repocket.co](https://link.repocket.co/raqc) واحصل على مفتاح API الخاص بك من لوحة القيادة.
#### تثبيت Docker Container:
قم بتعديل السطر التالي بالبريد الإلكتروني ومفتاح api قبل اللصق في الجهاز الطرفي.
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### فيديو تعليمي:
{{< youtube id="171gWknfAbY" >}}

### تثبيت Traff Monetizer:
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

على غرار EarnApp و HoneyGain ، يدفع لك TraffMonetizer مقابل مشاركة الإنترنت الخاص بك. متوسطات حوالي 2 دولار شهريًا لكل عقدة لكل IP. تقدم فقط المدفوعات في BTC.

#### إنشاء حساب Traff Monetizer الخاص بك:
أنشئ حسابك على [https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
بمجرد دخولك إلى لوحة القيادة ، قم بتدوين رمز التطبيق الخاص بك.

#### تثبيت Docker Container:
انسخ السلسلة التالية وألحق الرمز الذي حصلت عليه من لوحة القيادة قبل اللصق في الجهاز الطرفي.

```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```

### تثبيت Mysterium:
[Mysterium](https://www.mysterium.network/) هي خدمة VPN غير مركزية وخدمة Webscraping مبنية على بلوكشين Etherium و Polygon.
متوسط المدفوعات في أي مكان من 1 إلى 20 دولارًا أمريكيًا في الشهر اعتمادًا على عوامل متعددة لكل عقدة لكل IP. يكلف 1.XX دولارًا لإعداد عقدة للتنشيط. المدفوعات في رمز MYST المميز.


#### تثبيت Docker Container:
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### إعداد حاوية Docker:
انتقل إلى http: // "nodeip" / # / dashboard عن طريق استبدال "nodeip" بعنوان IP الخاص بالعقدة. يمكنك العثور على هذا عن طريق كتابة "ifconfig" في الجهاز.

انقر فوق "بدء إعداد العقدة".

تجاوز عنوان محفظة ERC20 التي تريد استلام المكافآت فيها وانقر على "التالي". يمكنك استخدام عنوان Ethereum قياسي مثل أحد عناوين MetaMask الخاصة بك.

اكتب كلمة المرور التي ستستخدمها للوصول إلى لوحة تحكم العقدة هذه في المستقبل. قم بتحديد خانة الاختيار للمطالبة بالعقدة في شبكتك.

انقر فوق الارتباط "احصل عليه هنا" وابحث عن مفتاح API الخاص بك. انسخه. ارجع والصقه. انقر فوق "حفظ ومتابعة".

#### ميناء الشحن:
لا يمكننا وصف كيفية إعادة توجيه الأجهزة المحددة لكل شخص. فيما يلي بعض الموارد لتعلم كيفية النقل إلى الأمام.
- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### إعادة تشغيل حاويات Docker تلقائيًا على التمهيد:
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### التكوينات الاختيارية:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### زيادة الأمان عن طريق حظر البرامج الضارة وأجهزة التتبع.
فرض جميع طلبات نظام أسماء النطاقات للبرامج الضارة Cloudflares وتتبع نظام أسماء النطاقات للحماية.
أيضًا ، قم بحظر طلبات DNS / HTTPS.
* إذا كان لديك جهاز توجيه أو جدار ناري أكثر تقدمًا على الشبكة ، يمكنك حتى استخدام حزم مثل snort / securita لإنشاء قواعد أكثر تقدمًا لحظر عناوين IP السيئة المعروفة ، والوصول إلى Tor ، والسيول ، وحركة مرور p2p بشكل عام ، وما إلى ذلك. مقترح ولكنه غير مطلوب. *
```bash
# Allow ssh still
sudo ufw allow 22
# Allow dns out
sudo ufw allow out 53/tcp
sudo ufw allow out 53/udp
# Redirect all dns back to 1.1.1.2 or 1.0.0.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.0.0.2 -j DNAT --to-destination 1.1.1.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.1.1.2 -j DNAT --to-destination 1.0.0.2
# Block DNS over HTTPS
sudo ufw deny out 853/tcp
sudo ufw deny out 853/udp 
iptables -A FORWARD -m string --string "get_peers" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "announce_peer" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "find_node" --algo bm -j LOGDROP
# Block Default ToR Ports
sudo ufw deny out 9050/tcp
sudo ufw deny out 9050/udp
sudo ufw deny out 9051/tcp
sudo ufw deny out 9051/udp
# Block Torrents
sudo ufw deny out 6881/tcp
sudo ufw deny out 6881/udp
sudo ufw deny out 6882-6999/tcp
sudo ufw deny out 6882-6999/udp
iptables -A FORWARD -m string --algo bm --string "BitTorrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "BitTorrent protocol" -j DROP
iptables -A FORWARD -m string --algo bm --string "peer_id=" -j DROP
iptables -A FORWARD -m string --algo bm --string ".torrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "announce.php?passkey=" -j DROP
iptables -A FORWARD -m string --algo bm --string "torrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "announce" -j DROP
iptables -A FORWARD -m string --algo bm --string "info_hash" -j DROP
# Save the Changes and Enable the Firewall
sudo iptables-save
sudo ufw enable
```
لمزيد من حظر ToR المتقدم ، يمكنك القيام بما يلي:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

## ربح؟
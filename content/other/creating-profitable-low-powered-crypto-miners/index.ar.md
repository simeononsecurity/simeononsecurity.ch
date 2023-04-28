---
title: "Build a Profitable Passive Income Box with Low-Powered Hardware: A Guide"
draft: false
toc: true
date: 2023-02-07
description: "Learn how to set up a low-powered passive income crypto miner using a Raspberry Pi or Intel NUC, and earn $10-$20 per month per box with this guide"
tags: ["Build a Profitable Passive Income Box", "Low-Powered Hardware", "Passive Income", "Crypto Miner", "Raspberry Pi", "Intel NUC", "Guide", "Hardware Requirements", "OS Installation", "Software Installation", "Docker", "Automatic Docker Container Updates", "Ubuntu Server", "Ubuntu Desktop", "Raspbian", "Budget", "USFF", "Tiny", "Mini", "Micro PC", "Technical Experience", "EarnApp", "MYST", "Peer2Profit", "HoneyGain", "TraffMonitizer", "Watchtower", "Bitping"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "a green, circuit board shaped like a box with internet connectivity symbols as wires connected to it."
coverCaption: ""
---
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```
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
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```
```bash
export P2P_EMAIL="your_email_without_quotes"; 
docker rm -f peer2profit || true && docker run -td --restart always \
        -e P2P_EMAIL=$P2P_EMAIL \
        --name peer2profit \
        peer2profit/peer2profit_linux:latest 
```
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```
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
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```
 ** إنشاء صندوق السلسلة منخفضة الطاقة: دليل ** عمال مناجم الهيليوم. تعد واحدة من الصور. أسعار منخفضة من التكلفة الحقيقية مقابل صندوق سكني.  * إذا كانت لديك القدرة على إعداد هذا الإعداد على مربع شبكة محلية بشكل أفضل. على ذلك ، هذه الانتخابات  ## متطلبات الأجهزة: مطلوب واحد مما يلي. نحتاج بشكل أساسي إلى أي جهاز فعال ومنخفض الطاقة التي يمكن الحصول عليها. Raspberry PI أو Intel NUC أو ما شابه ذلك سيفي بالغرض. أن يكونوا قادرين على القيام بذلك. وحدة المركزية المركزية. لهذا سنستهدف ميزانية الميزانية بين 100 دولار و 200 دولار للأجهزة. هدف قوتنا هو aprox. متوسط 25 واط. ### فطيرة التوت: من الصعب الحصول عليها في هذه الأيام. للحصول على معلومات حول كيفية تثبيت raspian على Raspberry PI الخاص بك - [مجموعة أدوات Raspberry Pi 4B Model B DIY] (https://amzn.to/3x72kv0) - [GeeekPi Raspberry Pi 4 4GB Starter Kit] (https://amzn.to/3jG2g2k) - [GeeekPi Raspberry Pi 4 8GB Starter Kit] (https://amzn.to/3DQisF6) ### إنتل نوك: مجموعة متنوعة من هناك. لا تتردد في اختيار أحدث. - [Intel NUC 12 Pro] (https://amzn.to/3JTzLc7) - [Intel NUC 8] (https://www.ebay.com/sch/i.html؟_nkw=intel+nuc+8) - [Intel NUC 6] (https://www.ebay.com/sch/i.html؟_nkw=intel+nuc+6) ### أي جهاز كمبيوتر USFF / Tiny / Mini / Micro: - [Lenovo ThinkCentre M900 Tiny] (https://www.ebay.com/itm/385116504642) - [Dell OptiPlex 7040 Micro USFF] (https://www.ebay.com/itm/165504038978) ### أي كمبيوتر صغير مع Intel N5100 أو ما شابه ذلك للحصول على مكافئ Raspberry Pi منخفض الطاقة الطاقة ولكن على منصة x64. - [Beelink U59 Mini PC] (https://amzn.to/3YkFhcj) - [TRIGKEY Mini Computer] (https://amzn.to/3XkbXkS)  ## تثبيت نظام التشغيل: لن ندخل في التفاصيل الفنية حول كيفية تثبيت نظام التشغيل هنا. ومع ذلك ، إليك بعض الموارد الرائعة لتبدأ بها ### راسببيان: - [البدء] (https://www.raspberrypi.com/documentation/computers/getting-started.html) - [الطريقة الجديدة لإعداد Raspberry Pi] (https://www.youtube.com/watch؟v=jRKgEXiMtns) ### أوبونتو: - [تثبيت سطح مكتب Ubuntu] (https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview) - [Ubuntu Server - التثبيت الأساسي] (https://ubuntu.com/server/docs/installation) - [دليل المبتدئين الكامل لـ Ubuntu: تنزيل وتثبيت Ubuntu] (https://www.youtube.com/watch؟v=W-RFY4LQ6oE)   ## تثبيت البرامج: سيكون هذا قسمًا أطول. سنقوم بإيقافه؟ مكتب خادم ubuntu و ubuntu على سطح المكتب.  * بالنسبة لهذا القسم ، نفترض بعض الخدمات الأساسية وأنك قمت بتثبيت نظام التشغيل الخاص بالفعل بالإضافة إلى معرفة كيفية الدخول إلى الجهاز. *  ### تثبيت التحديثات: نريد أولاً أن يكون من تحديث نظامنا بالكامل:  ### تثبيت Docker: نحتاج إلى إلغاء تثبيت إصدارات موجودة ، تأتي معدة مع نظام وتثبيت إصدارات أحدث.  ### تثبيت برج المراقبة: تقوم بتخزين الصور القديمة.  ### تثبيت Bitping: [* Bitping هو أحد الحلول مراقبة الويب وتحسين الأداء الذي يوفر مراقبة حقيقية في الوقت الحقيقي وتعليقات فورية على فترات التعطل أو الأداء المتدهور ، مع امكانيات ممتازة وخطوات مرجعية وربط ديناميكي وخطأ أثناء الربط. *] (https://bitping.com)  يوفر لك Bitping القدرة على الحصول على أموال في Solana مقابل توفير عقدة للشركات الإيرانية في انتخابات شبكة الوزن من شبكتك. يبلغ متوسط هذا حوالي 0.1 سنتًا يوميًا لكل عقدة. يعرف الكثير ، لكن لديه القدرة على الحصول على قدر كبير من المساعدة.  #### إنشاء حساب: أنشئ حسابًا على [bitping.com] (https://bitping.com)  #### تثبيت عامل الإرساء: الخطوة الأولى. قم أولاً أولاً.  اضغط على CTRL + C على لوحة المفاتيح للهروب من الحاوية بعد تسجيل الدخول باستخدام حساب bitping الخاص.  الخطوة 2. قم بزيارة الموقع لاستمرار الحاوية في الخلفية   ### تثبيت تطبيق اكسب: [* استفد من الوقت الذي تُترك فيه أجهزتك في وضع الخمول عن طريق الحصول على أموال غير أخر *] (https://earnapp.com/i/c1dllee)  الحصول على خدمة VPN للحصول على قدر مذهل من المكافآت. متوسطات حوالي 5 دولارًا لكل عقدة لكل سكني. خدمات خدمات مدفوعات عبر بطاقات paypal و amazon.  #### إنشاء حساب كسب التطبيق: قم بحساب حساب على [winapp.com] (https://earnapp.com/i/c1dllee). * تحذير حساب جوجل *  #### تثبيت التطبيق للحصول على UUID الخاص بك: إذا كان حفل تشير تشير إلى أخرى. - [أرشفة] (https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)  #### تثبيت عامل الإرساء: الفترة السابقة لصقها في الجهاز الطرفي. تحتاج إلى تحديد UUID الخاص بك المكتسب. #### فيديو تعليمي: {{<youtube id = "tt499o0OjGU">}}  ### تثبيت اكتساب العسل: [* الدخل السلبي - بسهولة ، يمكنك كسب المال ببساطة عن طريق الإنترنت الخاص بك. ابدأ في الكسب الآن. *] (https://r.honeygain.me/DAVID07A75)  الحصول على خدمات VPN للحصول على قدر مذهل من المكافآت. متوسطات حوالي 5 دولارًا لكل عقدة لكل سكني. يمكن أن تكون معقدة معقدة. اقرأ المزيد قبل أن تقرر استخدام هذه الحاوية  #### إنشاء حساب كسب العسل: أنشئ حسابًا على [honeygain.com] (https://r.honeygain.me/DAVID07A75)  #### تثبيت Docker Container: قمديل السلسلة بالبريد الإلكتروني وواجه وكلمة المرور واسم الجهاز قبل اللصق في الجهاز  #### مشروع بديل لـ Raspberry Pi - [كيفية تثبيت Honeygain على Raspberry Pi مع نظام Raspberry Pi OS القياسي] (https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)  #### فيديو تعليمي: {{<youtube id = "Wd11M0nSy1k">}}  ### تثبيت PawnsApp: [* كسب المال السلبي عبر الإنترنت من استكمال البيانات ومشاركة الإنترنت *] (https://pawns.app/؟r=sos) يقدم تطبيق Pawns ، الذي يشبه التطبيقات الأخرى المدرجة هنا ، الدفع لك مقابل مشاركة الإنترنت الخاص بك. الحد الأدنى للدفع هو 5 دولارات. متوسط الدفع هو 0.50 دولار شهريًا لكل عقدة لكل IP.  #### إنشاء حساب PawnsApp: أنشئ حسابًا على [https://pawns.app] (https://pawns.app/؟r=sos)  #### تثبيت Docker Container:  قمديل ما يلي بالبريد الإلكتروني وكلمة المرور واسم الجهاز ومعرف الجهاز قبل النسخ إلى الجهاز الطرفي.  ### تثبيت ربح النظير 2: [* شارك تداولاتك وأرباحك عليها! *] (https://p2pr.me/16538445386293aa3aaec4e)  نشاط الإنترنت استخدام VPN. يكسب حوالي 1 دولار شهريًا لكل عقدة لكل IP. مجموعة متنوعة من خدمات بما في ذلك الحوالات المالية و BTC و LTC و LTC و MATIC وما إلى ذلك.  #### إنشاء حساب ربح نظير 2: أنشئ حسابًا على [peer2profit.com] (https://p2pr.me/16538445386293aa3aaec4e)  #### تثبيت Docker Container: #### فيديو تعليمي: {{<youtube id = "J_rSV5N8aQk">}}   ### تثبيت Repocket: [* أموال على أموال مقابل الإنترنت *] (https://link.repocket.co/pyqL)  على عرض العروض الأخرى. حد أدنى 20 دولارًا للدفع. يمكن أن تكون معقدة معقدة. ابحث بنفسك عن ما إذا كنت تريد استخدام هذه الخدمة. متوسط حوالي 1 دولار لكل عقدة لكل صندوق في الشهر.  #### إنشاء حساب Repocket: أنشئ حسابًا على [repocket.co] (https://link.repocket.co/pyqL) واحصل على مفتاح برمجة التطبيقات من لوحة التحكم. #### تثبيت Docker Container: قم بتعديل السطر التالي بالبريد الإلكتروني ومفتاح إلكتروني قبل اللصق في الجهاز الطرفي. #### فيديو تعليمي: {{<youtube id = "171gWknfAbY">}}  ### تثبيت Traff Monetizer: [* شارك اتصالك اتصالكسب المال عبر الإنترنت *] (https://traffmonetizer.com/؟aff=242022)  على غرار EarnApp و HoneyGain ، يدفع لك TraffMonetizer مقابل الإنترنت الخاص بك. متوسطات حوالي 2 دولار شهريًا لكل عقدة لكل IP. تقدم فقط دفع في BTC.  #### إنشاء حساب Traff Monetizer الخاص بك: أنشئ حسابك على [https://traffmonetizer.com] (https://traffmonetizer.com/؟aff=242022) رمز التطبيق الخاص بك.  #### تثبيت Docker Container: أنسخ السلسلة التالية وألحق الرمز الذي حصلت عليه من لوحة القيادة.   ### تثبيت Mysterium: [ميستيريوم] (https://www.mysterium.network/) هي خدمة VPN غير مركزية Webscraping مبنية على سلاسل الإيثيريوم والبوليغون. متوسط الدفع في أي مكان من 1 إلى 20 دولارًا أمريكيًا. يكلف 1.XX دولار لإعداد عقدة للتنشيط. في رمز MYST المميز.   #### تثبيت Docker Container:  #### إعداد وحدة الإرساء: عنوان IP الخاص بالعقدة http: // "nodeip" / # / dashboard. يمكنك العثور على هذا طريق كتابة "ifconfig" في الجهاز.  انقر فوق "بدء إعداد العقدة".  عنوان محفظة ERC20 التي تريد استلام المكافآت فيها على "التالي". يمكنك استخدام عنوان Ethereum قياسي مثل أحد عناوين MetaMask الخاصة بك.  اكتب كلمة المرور التي ستستخدمها للوصول إلى لوحة تحكم العقدة. قم بإنشاء خانة الاختيار للمطالبة بالعقدة في شبكتك.  انقر فوق الارتباط "احصل عليه هنا" وابحث عن مفتاح API الخاص بك. انسخه. ارجع والصقه. انقر فوق "حفظ ومتابعة".  #### ميناء الشحن: لا يمكننا وصف كيفية إعادة توجيه التوجيهات لكل شخص. فيما يلي بعض الموارد لتعلم كيفية النقل إلى الأمام. - [PortForward.com] (https://portforward.com/) - [Mysterium - Port Forwarding] (https://docs.mysterium.network/troubleshooting/port-forwarding)   ### إعادة حاويات تشغيل Docker تلقائيًا على تحسين:  ### التكوينات. - [تحديثات التشغيل وإعادة التشغيل] (https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/) - [حظر حركة مرور ToR على Ubuntu] (https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver) #### زيادة الأمان عن طريق حظر البرامج الجوية. فرض جميع أنظمة النطاقات للبرامج الخاصة بالبحث في مجالات الحماية. أيضًا ، قمقم طلبات DNS / HTTPS. * إذا كان لديك جهاز توجيه أو جدار ، وحركة مرور p2p بشكل عام ، وما إلى ذلك. مقترح ولكنه غير مطلوب. * حظر ToR المتقدم ، القيام بما يلي:  ## ربح؟
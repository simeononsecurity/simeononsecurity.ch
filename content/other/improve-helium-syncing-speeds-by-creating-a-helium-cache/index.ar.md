---
title: "Enhancing Helium Syncing Speeds with a Blockchain Cache"
draft: false
toc: true
date: 2022-02-19
description: "Learn how to install a Helium Miner Docker container on a VPS or Linux virtual machine for faster syncing speeds."
tags: ['Resolve Helium Miner Syncing Problems', 'Helium Mining', 'Helium Network Token (HNT)', 'Solve Synchronization Problems', 'Blockchain Technology for Helium', 'Docker Container', 'Docker Watchtower Monitoring', 'Virtual Private Server (VPS)', 'Automated Task Scheduler (Cron)', 'Automated Tasks with Cron Jobs']
cover: "/img/cover/A_cartoon_or_3d_animated_image_of_a_computer_with_a_chain.png"
coverAlt: "A cartoon or 3d animated image of a computer with a chain symbolizing the blockchain, connected to multiple other computer symbols representing the peers in the network, all connected to a central hub symbolizing the centralized cache setup."
coverCaption: ""
---
```bash
#Install Docker
#https://docs.docker.com/engine/install/ubuntu/
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

#Install the helium docker container
sudo mkdir /root/miner_data
docker run -d --env REGION_OVERRIDE=US915 --restart always --publish 1680:1680/udp --publish 44158:44158/tcp --name miner --mount type=bind,source=/root/miner_data,target=/var/data quay.io/team-helium/miner:latest-amd64

#Set the miner to auto restart when the host restarts
sudo docker update --restart unless-stopped $(docker ps | grep miner | awk '{print $1}')

#Install Watchtower for auto docker container updates
#https://github.com/containrrr/watchtower
docker run --detach --name watchtower --volume /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower
```
```bash
docker exec miner miner peer connect /ip4/xxx.xxx.xxx.xxx/tcp/44158 

docker exec miner miner peer sync /ip4/xxx.xxx.xxx.xxx/tcp/44158

docker exec miner miner peer fastforward /ip4/xxx.xxx.xxx.xxx/tcp/44158

docker exec miner miner peer book -s

docker exec miner miner repair sync_state
docker exec miner miner info p2p_status
docker exec miner miner info height
docker exec miner miner versions
docker exec miner miner info summary
```
```bash
chmod +x ~/miner_sync.sh
~/miner_sync.sh
```
```bash
crontab -e
```
```*/30 * * * * ~/miner_sync.sh >> ~/synclog.txt```
Save the file and exit.

Now the script will run every thirty minutes and sync from and to each of your miners.

### Profit?

 بلوك تشين ** تحسين سرعات تخزين الهيليوم ذاكرة مؤقتة  سنشرح اليوم كيفية تثبيت Helium Miner Docker> على VPS أو جهاز ظاهري Linux. يوفر ميزة الحصول على ميزة الحصول على blockchain. نفذت تنفيذ هذا الإعداد ، سنعمل أيضًا على تحسين سرعات وجودة من خلال قيام بجهاز متصل بجهاز محمول. هذا قابل للتطوير ، تنسيق تنسيق ، تنسيق النسخ الموضح أدناه.   ## مطلوب: - معرفة عامة بلينكس - عامل منجم الهليوم معاد توجيهه ولم يتم ترحيله - خادم VPS أو Linux VM  ## إعداد Linux VM: سأفترض أن لديك بعض مهارات Linux الأساسية وتعرف كيفية إعداد VPS أو linux vm. إذا كنت بحاجة إلى بعض المساعدة ، فراجع الموارد التالية Retail ubuntu VPS مقابل 5 دولار شهريًا:  - [https://docs.digitalocean.com/products/droplets/how-to/create/](https://docs.digitalocean.com/products/droplets/how-to/create/)  - [https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04] (https://www.digitalocean.com/community/tutorials/initial-server-setup -مع- ubuntu-20-04)  ## إعداد ذاكرة التخزين المؤقت "للهيليوم ؛ ### تثبيت البرنامج المطلوب: *** ملاحظة: *** في أي مكان حيث ترى "xxx.xxx.xxx.xxx" استبدله بعنوان IPv4 العام الخاص بمنجم الهيليوم. البرنامج ، وبرج المراقبة ، برج المراقبة ، البرنامج ، للتثبيت والتثبيت على إرساء البرنامج ، وبرج المراقبة للتحديثات: ### إنشاء سيناريو متزامنة: الآن ، أرسل معي ، عامل ، جاهز ، إرسال إلى وقت متزامن من استلام عمال مناجم الهيليوم. قمديل هذا البرنامج بتعناوين البرامج العامة لعمال مناجم الهيليوم: ثم قم بسمح "nano. / miner_sync.sh" "البرنامج المعدل واضغط على`` ctrl + x '' و'' y 'للحفظ.  ### اختبار النص:  ### إنشاء وظيفة Cron: نحتاج الآن إلى إعداد وظيفة cron لتشغيلها كل 30 دقيقة على الأقل. كم من الوقت متروك لاستخدامها [crontab guru] (https://crontab.guru/) لاستخدامها في استخدام هذه الطريقة.  قم بتشغيل الأمر التالي: حدد المحرر الذي تختاره ، ثم التالي السابق من البرنامج السابق.
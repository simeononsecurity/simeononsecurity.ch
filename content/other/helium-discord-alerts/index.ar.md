---
title: "Setting up HDS: Helium Hotspot Activity and Reward Notifications on Discord"
draft: false
toc: true
date: 2022-02-27
description: "Learn how to set up HDS, a tool that sends Helium hotspot activity and reward notifications to your Discord channel, with this step-by-step guide."
tags: ['Helium Miner Discord Notifications', 'Discord', 'Discord Notifications', 'Helium Notifications', 'Helium Miner', 'HNT', 'Helium Blockchain', 'Virtual Private Server', 'Cron', 'Cron Jobs']
cover: "/img/cover/A_3D_animated_art_style_image_of_a_computer_screen_display.png"
coverAlt: "A 3D animated art style image of a computer screen displaying a Helium hotspot dashboard with notifications popping up on the screen. The image is surrounded by icons representing Linux, Ubuntu, VPS, VM, and Git. "
coverCaption: ""
---
```bash
sudo apt install git python python3-pip -y
git clone https://github.com/co8/hds
cd ~/hds
cp new-config.json config.json
cp new-activity_history.json activity_history.json
nano config.json
```
```json
{
  "hotspot": "112MWdscG3DjHTxdCrtuLk...",
  "discord_webhook": "https://discord.com/api/webhooks/87869..."
}
```
```bash
#cd ~/hds
#pip install -r requirements.txt
python -m pip install discord-webhook
```
```
*/5 * * * * cd ~/hds; python3 hds.py >> cron.log 2>&1
20 4 * * 0 cd ~/hds; rm cron.log; echo "cron.log cleared (weekly)" >> cron.log 2>&1
```
```
cd ~/hds
python3 hds.py
```
 ** إعداد HDS - أداة حالة Hotspot Discord ** * تم إرسال نشاط نقطة اتصال الهيليوم وإشعارات المكافآت إلى قناة Discord الخاصة بك *  احصل على نشاط نقطة اتصال الهيليوم وإشعال المكافأة المرسلة مباشرة إلى قناة Discord الخاصة بك أداة Hotspot Discord Status (HDS). أساسي الإعداد معرفة أساسية بنظام Linux ، و Ubuntu VPS أو Ubuntu VM ، و Helium Miner. توفر نقطة إنشاء نقطة اتصال ، وتثبيت البرنامج المطلوب ، نقطة اتصال ثابتة كرون. جوابًا جوابًا ، جوابًا ، أن التكوين يعمل بشكل صحيح. تتبع مكافآت هيليوم blockchain الخاصة بك في الوقت الحقيقي مع HDS.  ## مطلوب: - معرفة عامة بلينكس - خادم Ubuntu VPS أو Ubuntu VM - عامل منجم هيليوم - نسخة من [برنامج HDS] (https://github.com/co8/hds)  ## إعداد Linux VM: سأفترض أن لديك بعض مهارات Linux الأساسية وتعرف كيفية إعداد VPS أو linux vm. إذا كنت بحاجة إلى بعض المساعدة ، فراجع الموارد التالية Retail ubuntu VPS مقابل 5 دولار شهريًا:  - [https://docs.digitalocean.com/products/droplets/how-to/create/](https://docs.digitalocean.com/products/droplets/how-to/create/)  - [https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04] (https://www.digitalocean.com/community/tutorials/initial-server-setup -مع- ubuntu-20-04)  ## إعداد أداة حالة الخلاف في نقطة ساخنة: ### إنشاء خطاف الويب للخلاف المطلوب:  - [Discord - مقدمة إلى Webhooks] (https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)  ### العثور على العنوانه هو العنوان المطلوب:  - [نقطة ساخنة] (https://app.hotspotty.net/workspace/hotspots)  - [مستكشف الهيليوم] (https://explorer.helium.com/)  ### تثبيت البرنامج المطلوب: - عرض هذا إلى تثبيت البرامج والملفات المطلوبة للحصول على نشر HDS. لقد تم إنشاء عنوان URL الخاص به. السابق:  - الآن نحن بحاجة إلى تثبيت تبعية واحدة ### إنشاء وظيفة Cron: - يسمح ما يلي: "crontab -e" " - الصق ما يلي في ملف crontab الخاص بك:  اختبار جيد لمعرفة ما إذا كان يعمل؟
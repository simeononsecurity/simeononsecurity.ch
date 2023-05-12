---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: «Узнайте, как сгенерировать код приглашения, и присоединяйтесь к онлайн-платформе HackTheBox, чтобы проверить и усовершенствовать свои навыки в области тестирования на проникновение и кибербезопасности как в Windows, так и в Linux».
tags: ["ХакБокс",«Пригласить вызов»,"Проверка на проницаемость","Информационная безопасность","Окна","Линукс",«Онлайн-платформа»,"HTTP-ПОСТ","Код приглашения","Кодировка Base64","Пауэршелл",«Линукс Баш»,«Декодирование Base64»,«Генерация кода приглашения»,"Программирование","Веб-разработка","Технологии",«ИТ-безопасность»,«ИТ-обучение»]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: «Мультяшный экран компьютера, показывающий веб-сайт HackTheBox с дверью хранилища, отпираемой ключом, открывающей трофей или медаль, на фоне городского пейзажа в цветовой гамме логотипа HackTheBox (синий и белый)».
coverCaption: ""
---
 пошаговые инструкции по выполнению приглашения на HackTheBox в Windows или Linux. Узнайте, как сгенерировать код приглашения и присоединиться к онлайн-платформе, чтобы проверить и усовершенствовать свои навыки в области тестирования на проникновение и кибербезопасности. В статье представлены как простые, так и расширенные решения, позволяющие пользователям всех уровней легко выполнить задание и получить доступ к платформе.

______

## Что такое взломать ящик?

HackTheBox — это онлайн-платформа для проверки и совершенствования ваших навыков в области тестирования на проникновение и кибербезопасности.

## Как присоединиться к Hack the box?

Чтобы создать учетную запись на HackTheBox (HTB), вы должны выполнить приглашение или взломать себя. Не беспокойтесь, хотя это несложно, и эта статья поможет вам выполнить задание.

Сначала зайдите в[HackTheBox Website](https://hackthebox.eu) и нажмите на кнопку присоединиться.

Вам будет представлено окно, в котором явно запрашивается код приглашения.

Вы можете ясно видеть текстовое поле с запросом кода приглашения.

Нажмите либо ***"F12"*** на клавиатуре, либо ***"Ctrl + Shift + I"***, чтобы открыть инструменты разработчика в браузере.

На вкладке "Элементы" вы найдете скрипт **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

Просмотрев javascript и функцию makeInviteCode, вы обнаружите, что вам нужно отправить **HTTP POST** на **/api/invite/generate**, чтобы получить код приглашения.

Вы можете сделать следующее, чтобы получить код приглашения в кодировке Base64:

### Решение:

#### Простой:
- **Windows**:```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" ```

Which will generate the following content: ```json {"success":1,"data":{"code":"Tk9ULVRIRS1GTEFHLVlPVSdSRS1MT09LSU5HLUZPUg==","format":"encoded"},"0":200} ```

If you take the encoded invite code to [base64decode.org](https://www.base64decode.org/), you'll get your invite code!

#### Advanced (Instantly print out invite code):
 - **Windows**: ```powershell $base64api=((Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON).Data).Code ; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($base64api)) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" | jq -r '.data.code' | base64 -d ```
 - **Note**: You'll need to install the [jq](https://stedolan.github.io/jq/download/) package.

______

### Invite Code Ex:
```XXXXX-XXXXX-XXXXX-XXXXX-XXXXX```



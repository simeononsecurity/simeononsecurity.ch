---
title: "Киберсценарий Discord: повышение уровня подготовки и осведомленности в области кибербезопасности"
date: 2023-02-22
toc: true
draft: false
description: "Узнайте, как CyberScenarioBot может повысить эффективность программы обучения и повышения осведомленности в области кибербезопасности на Discord, предлагая викторины, сценарии, отслеживание в таблице лидеров и мощные инструментальные команды."
tags: ["Discord бот", "обучение кибербезопасности", "осведомленность о кибербезопасности", "сценарный бот", "викторина-бот", "таблица лидеров", "команды инструментов", "Docker", "Python", "автоматизированное тестирование", "Discord API", "документация разработчика", "вклад", "Лицензия MIT", "CyberScenarioBot", "CyberSentinels", "повышение эффективности обучения", "информационная программа", "сценарии кибербезопасности", "серверная среда", "настраиваемые команды", "развертывание и управление", "контрольные работы и сценарии", "команды инструментов", "информационные команды", "проблемы и вклад", "Приложение для разработчиков Discord", "Документация по Discord.py", "работа с разработчиками", "Discord-сервер сообщества"]
---


**CyberScenarioBot**.

Бот для обучения киберсценариям, викторинам и повышению осведомленности о киберпространстве в Discord.

Вы можете перейти к [🚀 Quick Start](#quick-start) добавить `CyberScenarioBot` на ваш сервер.

[![Docker Image CI](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml)

## Введение

Данный бот может быть полезен при проведении тренингов по кибербезопасности, в рамках которых пользователи могут ознакомиться с различными сценариями кибербезопасности и узнать, как их предотвратить или отреагировать на них. Используя бота Discord, можно легко поделиться сценариями с пользователями в серверной среде, а также настроить бота на дополнительные команды или функциональность, если это необходимо. Кроме того, бот может быть запущен в контейнере Docker, что упрощает его развертывание и управление в различных средах.

[See the bot in action](https://discord.gg/CYVe2CyrXk)

## 🚀 Быстрый старт

### Как запустить:
#### Python:
Если вы используете систему на базе Unix, откройте терминал и перейдите в каталог, где находится скрипт bot.py. Затем выполните следующую команду:
```bash
export BOT_TOKEN="INSERT YOUR BOT TOKEN HERE"
export GUILD_ID="INSERT YOUR GUILD ID HERE (only needed for timed quizes and leaderboard)"
export LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
export CHANNEL_ID="INSERT YOUR CHANNEL ID HERE (only needed for timed quizes)"
export APLUSROLE="INSERT YOUR A+ ROLE ID HERE (only needed for timed quizes)"
export NETPLUSROLE="INSERT YOUR Network+ ROLE ID HERE (only needed for timed quizes)"
export SECPLUSROLE="INSERT YOUR Security+ ROLE ID HERE (only needed for timed quizes)"
export QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE (only needed for timed quizes)"
python bot.py
```
Обратите внимание, что если вы используете систему на базе Windows, то для установки переменной окружения необходимо использовать немного другую команду. Вот пример команды, которая должна работать в Windows:
```shell
set BOT_TOKEN="INSERT YOUR BOT TOKEN HERE"
set GUILD_ID="INSERT YOUR GUILD ID HERE (only needed for timed quizes)"
set LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
set LEADERBOARD_PERSIST_CHANNEL_ID="INSERT YOUR LEADERBOARD PERSIST CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
set CHANNEL_ID="INSERT YOUR CHANNEL ID HERE (only needed for timed quizes)"
set APLUSROLE="INSERT YOUR A+ ROLE ID HERE (only needed for timed quizes)"
set NETPLUSROLE="INSERT YOUR Network+ ROLE ID HERE (only needed for timed quizes)"
set SECPLUSROLE="INSERT YOUR Security+ ROLE ID HERE (only needed for timed quizes)"
set QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE (only needed for timed quizes)"
python bot.py
```
#### Docker:
При запуске контейнера Docker можно передать переменную окружения BOT_TOKEN с помощью флага -e следующим образом:

```bash
docker run -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" -it --rm simeononsecurity/discord-cyber-scenario-bot:latest
```

Для запуска бота в фоновом режиме:
```bash
docker run -td --name scenario-bot -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" simeononsecurity/discord-cyber-scenario-bot:latest
```

Чтобы запустить бота в фоновом режиме со всеми запланированными подсказками и ролями:
```bash
docker run -td --name scenario-bot \
-e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" \
-e GUILD_ID="INSERT YOUR GUILD ID HERE" \
-e LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE" \
-e LEADERBOARD_PERSIST_CHANNEL_ID="INSERT YOUR LEADERBOARD PERSIST CHANNEL ID HERE" \
-e CHANNEL_ID="INSERT YOUR CHANNEL ID HERE" \
-e APLUSROLE="INSERT YOUR A+ ROLE ID HERE" \
-e NETPLUSROLE="INSERT YOUR NET+ ROLE ID HERE" \
-e SECPLUSROLE="INSERT YOUR SEC+ ROLE ID HERE" \
-e QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE" \
simeononsecurity/discord-cyber-scenario-bot:latest
```

## Особенности
### **Доступные команды**
*Префикс команды: '!', '/'*****

### 📝 **Команды викторины и сценария**
- **Aplus**: Отвечает на вопросы, связанные с A+ от CompTIA.
- **Bluescenario**: Отвечает на вопрос со сценарием "синей" команды.
- **CCNA**: Ответы с подсказкой Cisco CCNA с множественным выбором.
- **CEH**: Ответы с подсказкой множественного выбора CEH от EC-Council.
- **CISSP**: Отвечает на вопросы с подсказкой множественного выбора CISSP от ISC2.
- **Linuxplus**: Отвечает на запрос множественного выбора Linux+ от CompTIA.
- **Netplus**: Ответы с подсказкой CompTIA по теме Network+.
- **Quiz**: Отвечает на случайный вопрос по осведомленности в области кибербезопасности.
- **Redscenario**: Ответы со сценарием "красной команды".
- **Secplus**: Отвечает на вопросы, связанные с темой Security+ от CompTIA.

#### 💯🎯 **Leaderboard**.
*Вопросы с несколькими вариантами ответов динамически взвешиваются, как на реальных экзаменах, в зависимости от того, правильно или неправильно на них ответили*.

- *Отслеживайте свой прогресс с течением времени и смотрите, как вы сравниваетесь с другими участниками вашего сервера*
- *Видеть оценки по каждой категории теста, а также в целом*

### 🛠️ **Команды инструментов**.
- **Dns**: Принимает `domain name` и возвращает записи A, AAAA, NS, TXT и т.д.
- **Hash**: Принимает в `1 of 4 supported algos` и `string` и выдает соответствующий хэш.
- **Ping**: Принимает на вход `IP address` и возвращает сообщение об успехе и средней задержке или сообщение о неудаче.
- **Phonelookup**: Принимает в `phone number` и выводит данные о носителе и местоположении.
- **Shodanip**: Принимает сигнал `IP address` и выводит полезную информацию с сайта https://internetdb.shodan.io/.
- **Subnet**: Принимает в `IP address` и `Subnet Mask` и выводит диапазон, используемые IP-адреса, адрес шлюза, широковещательный адрес и количество поддерживаемых хостов.
- **Whois**: Принимает запрос `domain name` и выводит информацию о домене в формате whois.

### ℹ️ **Информационные команды**.
- **Команды**: Отвечает этим сообщением.
- **Socials**: Ответы с указанием различных аккаунтов и сайтов бота в социальных сетях.

### ⚙️ **Простая настройка**.
- * См. [🚀 Quick Start](#🚀-quick-start)

## Предстоящие функции

Эти функции имеют запланированные сроки реализации, но мы отслеживаем их и будем рады [contributions](#contributing) для них.

- Расширенные возможности таблицы лидеров, включая еженедельные и ежемесячные рейтинги.
- Настраиваемые подсказки и тесты для удовлетворения конкретных потребностей в обучении кибербезопасности.
- Расширенная отчетность и аналитика для отслеживания прогресса и эффективности работы пользователей.

## Использование

CyberScenarioBot предлагает различные команды и функции для повышения эффективности программы обучения и повышения осведомленности в области кибербезопасности. Вот некоторые распространенные варианты использования:

1. **Вопросы и сценарии**: Используйте `/quiz` команда для получения случайного вопроса о кибербезопасности. Используйте такие команды, как `/aplus` `/netplus` `/secplus` чтобы получить доступ к специальным подсказкам, связанным с сертификатами CompTIA. Используйте такие команды, как `/bluescenario` и `/redscenario` для получения сценариев "синяя команда" и "красная команда" соответственно.

2. **Лидерская доска**: Следите за успехами пользователей и сравнивайте их с другими пользователями вашего сервера, отвечая на вопросы викторины и сертификации.

3. **Инструментальные команды**: Используйте различные инструментальные команды для выполнения задач, связанных с DNS, хэшированием, ping, поиском телефонных номеров, поиском IP-адресов в Shodan, вычислением подсетей и поиском WHOIS доменов. Используйте такие команды, как `/dns` `/hash` `/ping` `/phonelookup` `/shodanip` `/subnet` и `/whois` за которым следуют соответствующие аргументы.

4. **Информационные команды**: Используйте `/commands` для получения списка доступных команд. Для получения списка доступных команд можно воспользоваться командой `/socials` команда, позволяющая получить информацию об аккаунтах и сайтах бота в социальных сетях.

Не стесняйтесь исследовать и экспериментировать с доступными командами, чтобы повысить эффективность обучения кибербезопасности и вовлечь участников сервера.

## Вопросы

Если у пользователей возникают какие-либо проблемы или есть предложения по улучшению, они могут открыть проблему на GitHub, чтобы сообщить о ней. Поощряйте пользователей за предоставление подробной информации о проблеме и шагах по ее воспроизведению.

Чтобы открыть проблему, выполните следующие действия:

1. Перейдите на вкладку Issues в репозитории GitHub проекта: [Issues](https://github.com/CyberSentinels/discord-cyber-scenario-bot/issues)
2. Нажмите на кнопку "Новый выпуск".
3. Укажите описательное название и четкое описание проблемы.
4. Включите все необходимые журналы, скриншоты или фрагменты кода, чтобы помочь в устранении неполадок.
5. Отправьте проблему и ожидайте дальнейших сообщений от сопровождающих проекта.

## Вклад

Мы приветствуем любой вклад.
Данный проект задуман как проект для развития и обучения [the CyberSentinels club](https://cybersentinels.org) и мы с удовольствием поможем вам внести свой вклад и ответим на любые ваши вопросы.

### Автоматизированное тестирование на Python

Это репо включает в себя автоматизированное тестирование, вы можете посмотреть примеры его реализации [here](https://github.com/CyberSentinels/penguin-pie)

### Discord API и документация для разработчиков

Для тестирования изменений и реализации функций вам понадобится несколько вещей.

- [Discord Developer Application](https://discord.com/developers/applications)
- [Discord Developers Documentation](https://discord.com/developers/docs/intro)
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

### Работа с разработчиками

Вы можете обсудить работу над проектом на discord-сервере сообщества [here](https://discord.gg/CYVe2CyrXk)
  
## Лицензия

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)

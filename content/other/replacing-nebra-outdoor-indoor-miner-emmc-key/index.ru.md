---
title: "Замена SD-карты Nebra Helium Miner: Пошаговое руководство"
draft: false
toc: true
date: 2022-02-13
description: "В этом руководстве вы узнаете, как заменить или перепрошить карту памяти Nebra Indoor и Outdoor, первого и второго поколения, EMMC Key SD Card и устранить проблемы синхронизации Helium Miner."
genre: ["Технология", "Криптовалюта", "Оборудование", "Добыча гелия", "Поиск и устранение неисправностей", "Замена карты памяти SD", "Проблемы синхронизации", "Raspberry Pi", "Балена Этчер", "Гелиевый шахтер Nebra"]
tags: ["Гелиевый шахтер Nebra", "Замена карты памяти SD", "Проблемы синхронизации", "Добыча гелия", "Поиск и устранение неисправностей", "Raspberry Pi", "Балена Этчер", "Руководство по аппаратному обеспечению", "Обновление SD-карты", "Решение проблем с синхронизацией", "Пошаговое руководство", "Исправление синхронизации Helium Miner", "Nebra Indoor Miner", "Открытый шахтер Nebra", "Вычислительный модуль Raspberry Pi 3", "Изображение Balena Raspberry Pi CM3", "Поиск и устранение неисправностей в гелиевых шахтах", "Горное оборудование Nebra", "Программное обеспечение Balena Etcher", "Замена ключа EMMC на шахте Nebra Miner", "Восстановление SD-карты для Helium Miner", "Устранение проблем с синхронизацией Helium Miner", "Замена SD-карты Nebra Miner", "Руководство по поиску и устранению неисправностей гелиевого шахтера Nebra", "Советы по добыче гелия", "Обновление SD-карты Nebra Helium Miner", "Как восстановить Nebra Miner SD Card", "Устранение проблем с синхронизацией Nebra Helium Miner"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_holding_a_Nebra_Helium_M.png"
coverAlt: "Мультяшная иллюстрация, изображающая человека, держащего в руках Nebra Helium Miner, на открытой панели которого виден слот для SD-карты, а над прибором парят шаги руководства."
coverCaption: "Решайте проблемы с синхронизацией и обновляйте свой Helium Miner с легкостью."
---

**Замена и переименование EMMC-ключа / SD-карты Nebra для внутренних и наружных устройств**.

В данном руководстве подробно рассмотрен процесс замены или перепрошивки EMMC-ключа/ SD-карты Nebra Indoor и Outdoor. Выполнение этих действий позволит устранить проблемы синхронизации с Helium Miner и обеспечить бесперебойную работу. В руководстве подробно описаны необходимые инструменты и программное обеспечение, а также шаги, необходимые для получения файла config.json, прошивки новой SD-карты с помощью Balena Raspberry Pi CM3 Image и переноса исходного файла конфигурации на новую SD-карту.

## Введение

Работа гелиевых шахтеров Nebra, как внутренней, так и наружной моделей, основана на использовании ключа EMMC/ SD-карты. Со временем может возникнуть необходимость замены или перепрошивки этой карты для устранения проблем с синхронизацией и поддержания оптимальной производительности. В данном руководстве вы получите знания и инструкции, необходимые для эффективного выполнения этой задачи.

Для успешной замены SD-карты Nebra Helium Miner потребуются специальные инструменты и программное обеспечение. К инструментам относятся крестовая отвертка или [Allen Key Set](https://amzn.to/34SlnOS) (depending on the model), a [Micro SD Card Reader](https://amzn.to/3Jl3U0w), a [64GB A2 micro SD card](https://amzn.to/3oJtTqs) (or larger), and a [Micro USB 2.0 Cable](https://amzn.to/3LxXYmA). The essential software needed for this process includes [Balena Etcher](https://www.balena.io/etcher/), Balena Raspberry Pi Image, and [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) Имея под рукой эти ресурсы, вы будете готовы приступить к замене или перепрошивке SD-карты.

## Необходимые инструменты:
- Крестовая отвертка или [plastic pry bar](https://amzn.to/3rLXVfc) for the Nebra Indoor Miner or [allen key set](https://amzn.to/34SlnOS) для Nebra Outdoor Miner
- Крепкие ногти, пинцет или игольчатые щипцы для извлечения старой SD-карты
- [A Micro SD Card Reader](https://amzn.to/3Jl3U0w)
- [A 64gb (or larger) A2 micro sd card](https://amzn.to/3oJtTqs)
- [A Micro USB 2.0 Cable](https://amzn.to/3LxXYmA)
## Необходимое программное обеспечение:
- [Balena Etcher](https://www.balena.io/etcher/)
- [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)
- Последний образ Nebra для конкретного устройства:
*Если вы не знаете, какое у вас устройство, обратитесь к разделу [nebra documentatio](https://support.nebra.com/support/home) Если он старше, можно с уверенностью предположить, что у вас устройство первого поколения*.
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)

## Внутри гелиевых шахтеров Nebra:
### Содержание внутреннего шахтера Nebra:
{{< figure src="Indoor-internal-lights.png" alt="Nebra Indoor Miner" >}}
### Содержание Nebra Outdoor Miner:
{{< figure src="Inside-Interfaces.jpg" alt="Nebra Outdoor Miner" >}}
 - 1.) 9-16 В @ 15 Вт DC 6.5MMx2.0MM Barrel Jack
 - 2.) Ethernet-коннектор
 - 3.) Светодиодный индикатор
 - 4.) Интерфейсная кнопка
 - 5.) Разъем модуля 4G / LTE
 - 6.) Слот для Sim-карты

## Как заменить SD-карту
### Шаг 1. По желанию получите файл config.json с ключа EMMC:
- Скачайте и установите [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) это понадобится для загрузки вычислительного модуля в качестве файловой системы usb
- Определите и установите перемычки на дочерней плате CM3 для режима программирования
 - {{< figure src="daughterboardBreakdown.png" alt="Nebra Daughterboard Overview" >}}
   - 5.) Порт Micro USB, используемый для формирования изображений
   - 7.) Перемычка JP4 USB - используется для переключения между обычным режимом работы и режимом вспышки; убедитесь, что она находится в положении 1-2 для обычного режима работы и 2-3 для программирования.
   - 8.) JP3 Power Jumper - позволяет питать модуль от разъема Micro USB. Подключайте его только при программировании с ПК и убедитесь, что материнская плата не подключена.
 - Установите перемычку JP4 в положение 2+3.
 - Подключите usb-кабель и выполните следующие действия [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) утилита
 - Откройте файловый проводник, и вы увидите диск с названием "resin-boot". Извлеките из каталога файл "config.json", который может понадобиться в дальнейшем и должен быть записан в резервную копию.
 - Отключите usb-кабель и переведите перемычку JP4 в положение 1+2.
### Шаг 2: Прошить новую sd-карту образом Balena Raspberry Pi CM3:
- Скачайте и извлеките подходящий образ
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)
- Использование [Balena Etcher](https://www.balena.io/etcher/) выберите недавно извлеченный файл .img и новую карту microsd в качестве целевого устройства
- Выберите Flash
### Шаг 3: Установите новую sd-карту и соберите Nebra Miner:
 - Установите SD-карту в слот, в котором ранее находился ключ EMMC.
 - Соберите шахтер.
 - При первом включении только что прошитого майнера Nebra Miner подключите его к сети ethernet на 20-30 минут, после чего снова установите wifi-соединение.
### Шаг 4: Прибыль?





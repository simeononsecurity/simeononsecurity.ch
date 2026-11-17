---
title: "SenseCAP M1 Raspberry Pi Shield: ਪਿਨਆਉਟ ਅਤੇ LoRaWAN ਲਈ ਮੁੜ ਵਰਤੋਂ"
date: 2026-09-12
lastmod: 2026-11-07
toc: true
draft: false
description: "SenseCAP M1 ਸ਼ੀਲਡ ਸਮਝੋ, ਵਿਰੋਧੀ GPIO ਨਕਸ਼ਿਆਂ ਦੀ ਤੁਲਨਾ ਕਰੋ, ATECC608 ਦੀ ਜਾਂਚ ਕਰੋ ਅਤੇ ਨਵੇਂ Raspberry Pi OS ਨਾਲ LoRaWAN ਗੇਟਵੇ ਦੀ ਯੋਜਨਾ ਬਣਾਓ।"
genre: ["Raspberry Pi", "IoT", "ਹਾਰਡਵੇਅਰ ਸੁਰੱਖਿਆ"]
tags: ["SenseCAP M1", "SenseCAP M1 ਸ਼ੀਲਡ", "SenseCAP M1 ਪਿਨਆਉਟ", "Raspberry Pi ਸ਼ੀਲਡ", "Raspberry Pi HAT", "LoRaWAN ਗੇਟਵੇ", "WM1302", "WM1303", "SX1302", "SX1303", "Seeed Studio", "Helium ਹੌਟਸਪੌਟ ਮੁੜ ਵਰਤੋਂ", "LoRa concentrator", "SPI GPIO", "GPIO17", "GPIO22 LED", "libgpiod", "Raspberry Pi OS", "ATECC608", "CryptoAuthLib", "I2C ਡਾਇਗਨੋਸਟਿਕਸ", "STTS751", "LoRa Basics Station", "ChirpStack", "The Things Stack", "ਹਾਰਡਵੇਅਰ ਰਿਵਰਸ ਇੰਜੀਨੀਅਰਿੰਗ"]
cover: "/img/cover/sensecap-wm1302-shield-hardware.webp"
coverAlt: "Seeed WM1302 ਮੋਡੀਊਲ, Raspberry Pi ਹੈਡਰ, ਐਂਟੀਨਾ ਕੇਬਲ, USB-C ਸਾਕਟ ਅਤੇ ਪੱਖੇ ਦੇ ਕਨੈਕਟਰ ਵਾਲੀ SenseCAP M1 ਸ਼ੀਲਡ"
coverCaption: "ਬੋਰਡ ਦੀ ਤਸਵੀਰ: Clockwork Bird, 2023। ਸਰੋਤ ਅਤੇ ਸਿਹਰਾ ਲੇਖ ਦੇ ਅੰਤ ਵਿੱਚ ਹਨ।"
coverCredit: "Clockwork Bird"
coverCreditURL: "https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/"
---

**SenseCAP M1 ਸ਼ੀਲਡ LoRaWAN ਗੇਟਵੇ ਹਾਰਡਵੇਅਰ ਵਜੋਂ ਲਾਭਦਾਇਕ ਹੈ, ਪਰ ਇਸ ਦੀ ਵਾਇਰਿੰਗ ਲਈ ਆਮ Raspberry Pi HAT ਟਿਊਟੋਰਿਅਲ ਨਾਲੋਂ ਵੱਧ ਜਾਂਚ ਚਾਹੀਦੀ ਹੈ।** ਇਹ ਗਾਈਡ [Clockwork Bird ਦੀ 2023 ਵਾਲੀ ਜਾਂਚ](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/) ਵਿੱਚ ਨਿਰਮਾਤਾ ਦੇ ਦਸਤਾਵੇਜ਼, upstream ਡਰਾਈਵਰ ਦੀ ਜਾਂਚ ਅਤੇ ਮੌਜੂਦਾ GPIO ਹਦਾਇਤਾਂ ਜੋੜਦੀ ਹੈ। ਤੁਸੀਂ ਹਾਰਡਵੇਅਰ ਦੀ ਪਛਾਣ ਕਰੋਗੇ, ਪੱਕੇ ਤੱਥਾਂ ਨੂੰ ਅਧੂਰੇ ਪਿਨਆਉਟ ਸਬੂਤ ਤੋਂ ਵੱਖ ਕਰੋਗੇ ਅਤੇ ਦੁਹਰਾਈ ਜਾ ਸਕਣ ਵਾਲਾ ਸ਼ੁਰੂਆਤੀ ਰਿਕਾਰਡ ਬਣਾਓਗੇ।

> **ਦਾਇਰਾ:** ਇਹ ਦਸਤਾਵੇਜ਼ਾਂ ਉੱਤੇ ਆਧਾਰਿਤ ਹਾਰਡਵੇਅਰ ਗਾਈਡ ਹੈ। ਇਸ ਲੇਖ ਲਈ ਕਮਾਂਡਾਂ ਅਤੇ ਬੋਰਡ ਮੈਪ ਕਿਸੇ ਅਸਲ M1 ਉੱਤੇ ਨਹੀਂ ਪਰਖੇ ਗਏ।

## ਮੁੱਖ ਗੱਲਾਂ

- **ਦੋਵੇਂ ਬੋਰਡ ਪਛਾਣੋ:** M1 ਕੈਰੀਅਰ ਅਤੇ ਹਟਾਇਆ ਜਾ ਸਕਣ ਵਾਲੇ concentrator ਦੇ ਮਾਡਲ ਅਤੇ ਰਿਵਿਜ਼ਨ ਵੱਖਰੇ ਹਨ।
- **ਰੀਸੈੱਟ ਸਕ੍ਰਿਪਟਾਂ ਦੀ ਜਾਂਚ ਕਰੋ:** CoreCell ਦੇ ਡਿਫਾਲਟ ਮੁੱਲ ਪ੍ਰਕਾਸ਼ਿਤ M1 ਪਿਨਆਉਟ ਦੇ ਕੁਝ ਸਿਗਨਲਾਂ ਨਾਲ ਟਕਰਾਉਂਦੇ ਹਨ।
- **OS ਇੰਟਰਫੇਸ ਵੇਖੋ:** SPI ਡਿਵਾਈਸ ਫਾਈਲਾਂ, GPIO ਨੰਬਰ ਅਤੇ GPIO ਟੂਲ ਦੇ ਵਰਜਨ ਵੱਖਰੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦਿੰਦੇ ਹਨ।
- **ਸੁਰੱਖਿਅਤ ਤੱਤ ਦੀ provisioning ਬਚਾਓ:** ਡਿਵਾਈਸ ਜਾਣਕਾਰੀ ਪੜ੍ਹਨਾ ਅਤੇ ਇਸਨੂੰ configure ਕਰਨਾ ਜਾਂ ਕੁੰਜੀਆਂ ਬਣਾਉਣਾ ਵੱਖਰੇ ਕੰਮ ਹਨ।
- **ਪੂਰਾ ਰਸਤਾ ਸਾਬਤ ਕਰੋ:** concentrator ਮਿਲ ਜਾਣਾ ਸੈਂਸਰ ਡਾਟਾ ਪਹੁੰਚਣ ਦਾ ਸਬੂਤ ਨਹੀਂ।

## ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

**ਮੁਸ਼ਕਲ: ਦਰਮਿਆਨੀ।** ਸੂਚੀ ਬਣਾਉਣ, OS ਤਿਆਰ ਕਰਨ ਅਤੇ ਦਸਤਾਵੇਜ਼ ਜਾਂਚਣ ਲਈ ਲਗਭਗ ਇੱਕ ਤੋਂ ਦੋ ਘੰਟੇ ਰੱਖੋ। ਬਿਜਲੀ ਵਾਲੀ ਜਾਂਚ, ਡਰਾਈਵਰ ਬਦਲਾਅ ਅਤੇ ਨੈੱਟਵਰਕ ਸਰਵਰ ਲਗਾਉਣ ਲਈ ਵਾਧੂ ਕੰਮ ਚਾਹੀਦਾ ਹੈ, ਖਾਸ ਕਰਕੇ ਜੇ ਬੋਰਡ ਰਿਵਿਜ਼ਨ ਅਣਜਾਣ ਹੋਵੇ।

| ਚੀਜ਼ | ਮਕਸਦ |
|---|---|
| **M1 ਸ਼ੀਲਡ ਅਤੇ concentrator** | ਕੈਰੀਅਰ ਰਿਵਿਜ਼ਨ ਅਤੇ ਮੋਡੀਊਲ ਦਾ ਪੂਰਾ ਲੇਬਲ ਪੜ੍ਹੋ |
| **Raspberry Pi 4** | ਅਸਲ M1 ਡਿਜ਼ਾਈਨ ਵਿੱਚ ਵਰਤੇ ਹੋਸਟ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ |
| **ਵਾਧੂ microSD ਕਾਰਡ** | ਪੁਰਾਣੀ ਇੰਸਟਾਲੇਸ਼ਨ ਬਚਾ ਕੇ ਵੱਖਰਾ OS ਤਿਆਰ ਕਰੋ |
| **ਠੀਕ ਬਿਜਲੀ ਸਪਲਾਈ ਅਤੇ ਐਂਟੀਨਾ** | ਅਸੈਂਬਲੀ ਅਤੇ ਮੋਡੀਊਲ ਦੇ RF ਬੈਂਡ ਨਾਲ ਮੇਲ ਕਰੋ |
| **SSH ਜਾਂ ਸਥਾਨਕ ਕਨਸੋਲ** | ਜਾਂਚਾਂ ਦਰਜ ਕਰੋ ਅਤੇ ਸੰਰਚਨਾ ਸੋਧੋ |
| **LoRaWAN ਸੈਂਸਰ ਅਤੇ ਸਰਵਰ** | ਹਾਰਡਵੇਅਰ ਚਾਲੂ ਕਰਨ ਤੋਂ ਬਾਅਦ ਐਪ ਤੱਕ ਅਸਲ ਡਿਲਿਵਰੀ ਜਾਂਚੋ |
| **ਮੀਟਰ ਅਤੇ ਹਾਰਡਵੇਅਰ ਤਜਰਬਾ** | ਅਣਦੱਸੇ ਕੁਨੈਕਸ਼ਨ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਹੱਲ ਕਰੋ |

ਕੁਝ ਵੀ ਖੋਲ੍ਹਣ ਤੋਂ ਪਹਿਲਾਂ ਬਿਜਲੀ ਤੋਂ ਵੱਖਰੀ ਅਸੈਂਬਲੀ ਦੇ ਦੋਵੇਂ ਪਾਸਿਆਂ ਦੀਆਂ ਤਸਵੀਰਾਂ ਲਓ। ਕਨੈਕਟਰ ਦੀ ਦਿਸ਼ਾ, ਪੇਚ, ਸਪੇਸਰ ਅਤੇ ਐਂਟੀਨਾ ਦਾ ਰਸਤਾ ਲਿਖੋ। ਨਵੀਂ ਇੰਸਟਾਲੇਸ਼ਨ ਸਵੀਕ੍ਰਿਤੀ ਜਾਂਚਾਂ ਪਾਰ ਕਰਨ ਤੱਕ ਅਸਲ ਕਾਰਡ ਅਤੇ ਸੰਰਚਨਾ ਉਪਲਬਧ ਰੱਖੋ।

## ਤਿੰਨ ਪਰਤਾਂ ਪਛਾਣੋ

**ਪੂਰਾ M1, ਕੈਰੀਅਰ ਸ਼ੀਲਡ ਅਤੇ concentrator ਵੱਖਰੇ ਹਿੱਸੇ ਹਨ।** Seeed ਦੇ ਦਸਤਾਵੇਜ਼ਾਂ ਵਿੱਚ ਪੂਰੇ ਹੌਟਸਪੌਟ ਨੂੰ Raspberry Pi 4 ਅਤੇ WM1302/SX1302 ਜਾਂ WM1303/SX1303 concentrator ਵਜੋਂ ਦੱਸਿਆ ਗਿਆ ਹੈ। “SenseCAP M1 shield” ਵਾਲੀ ਸੂਚੀ ਇਹ ਨਹੀਂ ਦੱਸਦੀ ਕਿ ਕੈਰੀਅਰ ਨਾਲ ਕਿਹੜਾ ਹਿੱਸਾ ਮਿਲਦਾ ਹੈ। [Seeed Studio ਦੀ M1 ਜਾਣਕਾਰੀ](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

**ਕੈਰੀਅਰ** Pi ਅਤੇ ਮੋਡੀਊਲ ਵਿਚਕਾਰ ਬਿਜਲੀ ਅਤੇ ਪੈਰੀਫਿਰਲ ਸਿਗਨਲ ਜੋੜਦਾ ਹੈ। **Concentrator** ਰੇਡੀਓ ਪ੍ਰਾਪਤੀ ਅਤੇ ਭੇਜਣ ਦਾ ਕੰਮ ਕਰਦਾ ਹੈ। ਹੋਸਟ ਉੱਤੇ ਚੱਲਦਾ **ਪੈਕੇਟ ਫਾਰਵਰਡਰ** ਪ੍ਰਾਪਤ ਰੇਡੀਓ ਪੈਕੇਟ ਅਤੇ ਤੈਅ ਡਾਊਨਲਿੰਕ ਸਰਵਰ ਨਾਲ ਲੈਣ-ਦੇਣ ਕਰਦਾ ਹੈ। [Semtech ਦੀ SX1302 HAL ਜਾਣਕਾਰੀ](https://github.com/Lora-net/sx1302_hal)

ਮਿਸਾਲ ਲਈ, ਸ਼ੈਲਫ਼ ਦਾ ਤਾਪਮਾਨ ਸੈਂਸਰ ਰੇਡੀਓ ਰਾਹੀਂ ਅੱਪਲਿੰਕ ਭੇਜਦਾ ਹੈ। Concentrator ਇਸਨੂੰ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ, ਹੋਸਟ ਅੱਗੇ ਭੇਜਦਾ ਹੈ ਅਤੇ ਨੈੱਟਵਰਕ ਤੇ ਐਪ ਸੇਵਾਵਾਂ ਇਸਨੂੰ ਸੰਭਾਲਦੀਆਂ ਹਨ। Linux ਦਾ ਚੱਲ ਪੈਣਾ ਇਸ ਲੜੀ ਦੇ ਸਿਰਫ਼ ਹੋਸਟ ਹਿੱਸੇ ਨੂੰ ਸਾਬਤ ਕਰਦਾ ਹੈ।

Clockwork Bird ਦੀ ਤਸਵੀਰ ਵਿੱਚ M1 v1.1 ਕੈਰੀਅਰ ਉੱਤੇ `WM1302-SPI-EU868` ਲੇਬਲ ਵਾਲਾ ਮੋਡੀਊਲ ਹੈ। ਆਪਣੇ ਹਾਰਡਵੇਅਰ ਦੇ ਲੇਬਲ ਲੱਭਣ ਲਈ ਤਸਵੀਰ ਵਰਤੋ। ਸੀਰੀਅਲ ਨੰਬਰ ਤਸਵੀਰ ਵਾਲੇ ਸਾਮਾਨ ਦੀ ਪਛਾਣ ਕਰਦੇ ਹਨ, ਕਿਸੇ ਹੋਰ ਗੇਟਵੇ ਦੀ ਸੰਰਚਨਾ ਨਹੀਂ।

{{< figure src="m1-carrier-wm1302-board.webp" alt="ਹਰੇ M1 ਕੈਰੀਅਰ ਉੱਤੇ ਲੇਬਲ ਵਾਲਾ WM1302 SPI EU868 ਮੋਡੀਊਲ, ਨਾਲ USB-C, ਬਟਨ, ਪੱਖਾ ਸਾਕਟ ਅਤੇ ਐਂਟੀਨਾ ਕੇਬਲ" caption="Clockwork Bird ਵੱਲੋਂ ਖਿੱਚਿਆ M1 v1.1 ਹਾਰਡਵੇਅਰ, ਲੇਖ ਦੇ ਕਵਰ ਲਈ ਵੀ ਵਰਤਿਆ" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## ਬਿਜਲੀ ਅਤੇ ਰੇਡੀਓ ਕੁਨੈਕਸ਼ਨ

**M1 ਦੇ USB-C ਕਨੈਕਟਰ ਨੂੰ ਬਿਜਲੀ ਦਾ ਇਨਪੁੱਟ ਸਮਝੋ।** ਨਿਰਮਾਤਾ ਪੂਰੇ ਗੇਟਵੇ ਲਈ DC 5 V, 3 A ਦੱਸਦਾ ਹੈ ਅਤੇ USB-C ਨੂੰ ਬਿਜਲੀ ਸਪਲਾਈ ਇੰਟਰਫੇਸ ਕਹਿੰਦਾ ਹੈ। ਇਸਨੂੰ ਚਾਰਜਿੰਗ ਪੋਰਟ ਕਹਿਣ ਨਾਲ ਬੈਟਰੀ ਦਾ ਭਰਮ ਪੈਦਾ ਹੁੰਦਾ ਹੈ, ਜਿਸਦਾ ਇਨ੍ਹਾਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਿੱਚ ਜ਼ਿਕਰ ਨਹੀਂ। [SenseCAP M1 ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

ਨਿਰਮਾਤਾ ਦਾ ਬਲਾਕ ਡਾਇਗ੍ਰਾਮ 5 V ਸਪਲਾਈ ਅਤੇ ਮੋਡੀਊਲ ਦੀ ਨਿਯੰਤਰਿਤ 3.3 V ਰੇਲ ਵੱਖ ਦਿਖਾਉਂਦਾ ਹੈ। ਸਮੱਸਿਆ ਲੱਭਣ ਵੇਲੇ ਇਹ ਫਰਕ ਮਹੱਤਵ ਰੱਖਦਾ ਹੈ: Pi ਚੱਲ ਸਕਦਾ ਹੈ ਪਰ concentrator ਨੂੰ ਬਿਜਲੀ ਨਾ ਮਿਲੇ। ਸਿਗਨਲ ਪਿਨ ਵਿੱਚ 5 V ਨਾ ਦਿਓ ਅਤੇ ਦੋਵੇਂ ਪਾਵਰ ਇਨਪੁੱਟ ਇੱਕ-ਦੂਜੇ ਤੋਂ ਅਲੱਗ ਮੰਨ ਕੇ ਨਾ ਚਲੋ।

**SPI ਅਤੇ USB ਮੋਡੀਊਲ ਰੂਪਾਂ ਲਈ ਹੋਸਟ ਕੁਨੈਕਸ਼ਨ ਵੱਖਰੇ ਹਨ।** Seeed ਦੇ WM1302 ਦਸਤਾਵੇਜ਼ SPI ਮਾਡਲ ਲਈ ਸਿੱਧਾ SPI ਅਤੇ USB ਮਾਡਲ ਲਈ STM32L4 USB ਬ੍ਰਿਜ ਦੱਸਦੇ ਹਨ। mini-PCIe ਆਕਾਰ ਮੋਡੀਊਲ ਦੀ ਬਣਾਵਟ ਦੱਸਦਾ ਹੈ, ਜਦਕਿ ਦਰਜ ਬਿਜਲੀ ਇੰਟਰਫੇਸ SPI ਜਾਂ USB ਹਨ। ਲੈਪਟਾਪ ਸਾਕਟ ਵਿੱਚ ਆਕਾਰ ਫਿੱਟ ਹੋਣ ਨਾਲ ਅਨੁਕੂਲਤਾ ਸਾਬਤ ਨਹੀਂ ਹੁੰਦੀ। [Seeed ਦੇ WM1302 ਦਸਤਾਵੇਜ਼](https://github.com/seeed-lora/WM1302-doc)

ਅਸੈਂਬਲੀ ਨੂੰ ਬਿਜਲੀ ਦੇਣ ਤੋਂ ਪਹਿਲਾਂ, ਬਿਜਲੀ ਬੰਦ ਰੱਖ ਕੇ ਮੋਡੀਊਲ ਲਗਾਓ ਅਤੇ ਢੁਕਵਾਂ ਐਂਟੀਨਾ ਜੋੜੋ। RF ਹਾਰਡਵੇਅਰ, ਐਂਟੀਨਾ ਅਤੇ ਖੇਤਰੀ ਯੋਜਨਾ ਮੇਲ ਕਰੋ। ਸੰਰਚਨਾ ਫਾਈਲ ਦਾ ਨਾਂ ਬਦਲਣ ਨਾਲ RF ਹਿੱਸੇ ਨਹੀਂ ਬਦਲਦੇ ਅਤੇ M1 ਪਾਵਰ ਸਾਕਟ USB concentrator ਰੂਪ ਦਾ ਸਮਰਥਨ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ।

{{< figure src="m1-power-spi-system-diagram.webp" alt="ਪਾਵਰ, SPI, GPIO ਅਤੇ I2C ਬੱਸ ਰਾਹੀਂ Raspberry Pi 4 ਨੂੰ M1 ਸ਼ੀਲਡ ਨਾਲ ਜੋੜਦਾ ਬਲਾਕ ਡਾਇਗ੍ਰਾਮ" caption="Clockwork Bird ਦੇ ਅਸਲ ਲੇਖ ਵਿੱਚ ਮੁੜ ਛਪਿਆ SenseCAP ਨਿਰਮਾਤਾ ਡਾਇਗ੍ਰਾਮ, WM1302 ਡਿਜ਼ਾਈਨ ਦਿਖਾਉਂਦਾ" credit="Seeed Studio / SenseCAP, via Clockwork Bird" attr="Seeed Studio / SenseCAP, via Clockwork Bird" attrlink="https://www.sensecapmx.com/docs/sensecap-m1/overview/" >}}

## ਪਿਨਆਉਟ ਧਿਆਨ ਨਾਲ ਪੜ੍ਹੋ

**BCM GPIO ਨੰਬਰ ਅਤੇ ਭੌਤਿਕ ਹੈਡਰ ਪਿਨ ਨੂੰ ਨੋਟ ਵਿੱਚ ਵੱਖਰੇ ਕਾਲਮਾਂ ਵਿੱਚ ਰੱਖੋ।** ਮਿਸਾਲ ਲਈ, BCM GPIO17 Pi ਹੈਡਰ ਦੇ ਭੌਤਿਕ ਪਿਨ 11 ਉੱਤੇ ਹੈ। ਮੋਡੀਊਲ ਦਾ edge connector ਤੀਜੀ ਨੰਬਰ ਪ੍ਰਣਾਲੀ ਦਿੰਦਾ ਹੈ, ਇਸ ਲਈ ਉਸਦਾ reset pin ਨੰਬਰ Raspberry Pi GPIO ਨੰਬਰ ਨਹੀਂ।

ਹੇਠਲੀ ਸਾਰਣੀ Clockwork Bird ਦੇ ਨਿਸ਼ਾਨ ਲਾਏ ਹੈਡਰ ਚਿੱਤਰ ਦੇ ਕੁਨੈਕਸ਼ਨ ਲਿਖਦੀ ਹੈ। ਇਹ **ਭਾਈਚਾਰਕ ਹਵਾਲਾ** ਹੈ, ਨਿਰਮਾਤਾ ਦਾ ਪੂਰਾ ਸਕੀਮੈਟਿਕ ਜਾਂ ਹਰ M1 ਰਿਵਿਜ਼ਨ ਦੀ ਮਾਪ ਨਹੀਂ। ਚਿੱਤਰ ਵਿੱਚ `SX1262` ਲਿਖਿਆ ਹੈ, ਜਦਕਿ Semtech ਦੀ ਆਮ reset ਸਕ੍ਰਿਪਟ `SX1261` ਨਾਮ ਵਰਤਦੀ ਹੈ।

| ਚਿੱਤਰ ਵਿੱਚ ਸਿਗਨਲ | BCM / ਭੌਤਿਕ ਪਿਨ | ਅਰਥ |
|---|---|---|
| **I2C SDA / SCL** | GPIO2 / 3, GPIO3 / 5 | ਸਾਂਝੀ ਪ੍ਰਬੰਧਨ ਬੱਸ |
| **SX1302 reset** | GPIO17 / 11 | concentrator reset ਦਾ ਸੰਭਾਵੀ ਪਿਨ |
| **ਯੂਜ਼ਰ LED** | GPIO22 / 15 | M1 ਨਿਸ਼ਾਨ |
| **SPI MOSI / MISO** | GPIO10 / 19, GPIO9 / 21 | SPI ਡਾਟਾ ਸਿਗਨਲ |
| **SPI clock** | GPIO11 / 23 | SPI clock ਸਿਗਨਲ |
| **SX1302 chip select** | GPIO8 / 24 | SPI0 CE0 |
| **SX1262 reset** | GPIO5 / 29 | ਵਾਧੂ ਰੇਡੀਓ reset ਦਾ ਸੰਭਾਵੀ ਪਿਨ |
| **SX1262 chip select** | GPIO6 / 31 | GPIO6, SPI0 CE1 ਤੋਂ ਵੱਖਰਾ |
| **SX1262 BUSY** | GPIO18 / 12 | ਵਾਧੂ ਰੇਡੀਓ ਦਾ ਹਾਲਤ ਆਉਟਪੁੱਟ |
| **SX1262 IO1 / IO2** | GPIO23 / 16, GPIO24 / 18 | ਵਰਤੋਂ ਤੋਂ ਪਹਿਲਾਂ ਜਾਂਚਣ ਵਾਲੇ ਵਾਧੂ ਸਿਗਨਲ |

ਕੱਟੇ GPS/UART ਨਿਸ਼ਾਨ M1 ਵਿੱਚ GPS ਹੋਣ ਦਾ ਸਬੂਤ ਨਹੀਂ। ਆਪਣੇ ਅਸਲ ਹਾਰਡਵੇਅਰ ਵਿੱਚ GPS ਨਾ ਹੋਵੇ ਤਾਂ GPS ਸੈਟਅੱਪ ਨਾ ਜੋੜੋ। ਪ੍ਰਕਾਸ਼ਿਤ ਚਿੱਤਰ ਯੂਜ਼ਰ ਬਟਨ ਅਤੇ ਪੱਖਾ ਕੰਟਰੋਲ ਵੀ ਹੱਲ ਨਹੀਂ ਕਰਦਾ। [Clockwork Bird ਦੀ ਪਿਨਆਉਟ ਜਾਂਚ](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)

{{< figure src="m1-community-header-pinout.webp" alt="ਨਿਸ਼ਾਨ ਲਾਇਆ Raspberry Pi ਹੈਡਰ ਚਿੱਤਰ, M1 LED, concentrator reset, SPI ਸਿਗਨਲ ਅਤੇ ਕੱਟੇ GPS ਕੁਨੈਕਸ਼ਨ ਦਿਖਾਉਂਦਾ" caption="ਰਿਵਿਜ਼ਨ ਕਵਰੇਜ ਅਧੂਰੀ ਵਾਲਾ ਭਾਈਚਾਰਕ ਹਵਾਲਾ, ਪੂਰਾ M1 ਸਕੀਮੈਟਿਕ ਨਹੀਂ" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Reset ਸਕ੍ਰਿਪਟਾਂ ਦੇ ਟਕਰਾਅ ਹੱਲ ਕਰੋ

**Reset ਸਕ੍ਰਿਪਟ ਬਿਜਲੀ ਵਾਲੇ ਆਉਟਪੁੱਟ ਚੁਣਦੀ ਹੈ, ਸਿਰਫ਼ ਸੌਫਟਵੇਅਰ ਪਸੰਦ ਨਹੀਂ।** Semtech ਦੀ upstream `reset_lgw.sh` CoreCell ਰੈਫ਼ਰੈਂਸ ਡਿਜ਼ਾਈਨ ਲਈ ਹੈ। ਇਸਦੇ ਡਿਫਾਲਟ ਵਿੱਚ concentrator reset ਲਈ GPIO23, power enable ਲਈ GPIO18, ਵਾਧੂ reset ਲਈ GPIO22 ਅਤੇ AD5338R reset ਲਈ GPIO13 ਹਨ। [Semtech reset ਸਕ੍ਰਿਪਟ ਸਰੋਤ](https://github.com/Lora-net/sx1302_hal/blob/master/tools/reset_lgw.sh)

Seeed ਦੀਆਂ ਪੁਰਾਣੀਆਂ ਸੈਟਅੱਪ ਹਦਾਇਤਾਂ ਦੋ reset ਅਸਾਈਨਮੈਂਟ GPIO17 ਅਤੇ GPIO5 ਕਰਦੀਆਂ ਹਨ, ਪਰ ਰੈਫ਼ਰੈਂਸ ਡਿਜ਼ਾਈਨ ਦੀਆਂ ਹੋਰ ਐਂਟਰੀਆਂ ਰੱਖਦੀਆਂ ਹਨ। ਉਦਾਹਰਣ ਮੰਨਣ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਮੁੱਲ M1 ਦੇ ਚਿੰਨ੍ਹਿਤ ਚਿੱਤਰ ਨਾਲ ਮਿਲਾਓ। [Seeed WM1302 ਸੈਟਅੱਪ ਹਦਾਇਤਾਂ](https://github.com/seeed-lora/WM1302-doc)

| ਅਸਾਈਨਮੈਂਟ | ਵਿਰੋਧੀ ਸਬੂਤ | ਲੋੜੀਂਦਾ ਫੈਸਲਾ |
|---|---|---|
| **ਵਾਧੂ reset ਵਜੋਂ GPIO22** | M1 ਚਿੱਤਰ ਇਸਨੂੰ ਯੂਜ਼ਰ LED ਕਹਿੰਦਾ ਹੈ | LED ਚਾਲੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਧਾਰਨਾ ਹਟਾਓ |
| **power enable ਵਜੋਂ GPIO18** | M1 ਚਿੱਤਰ ਇਸਨੂੰ ਵਾਧੂ BUSY ਕਹਿੰਦਾ ਹੈ | ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਨੈੱਟ ਤੇ ਦਿਸ਼ਾ ਜਾਂਚੋ |
| **DAC reset ਵਜੋਂ GPIO13** | ਆਮ ਸਕ੍ਰਿਪਟ ਹੋਰ ਰੈਫ਼ਰੈਂਸ ਡਿਜ਼ਾਈਨ ਦੱਸਦੀ ਹੈ | ਵੇਖੋ ਕਿ ਸਰਕਟ ਮੌਜੂਦ ਹੈ ਜਾਂ ਨਹੀਂ |
| **ਵਾਧੂ SPI ਡਿਵਾਈਸ** | M1 ਚਿੱਤਰ CE1 ਦੀ ਥਾਂ GPIO6 ਚੁਣਦਾ ਹੈ | chip-select ਰੂਟਿੰਗ ਅਤੇ ਡਰਾਈਵਰ ਸਹਾਇਤਾ ਪੱਕੀ ਕਰੋ |

**ਅਨੁਮਾਨ:** ਜੇ ਚਿੱਤਰ ਵਾਂਗ GPIO18 ਵਾਧੂ ਰੇਡੀਓ ਆਉਟਪੁੱਟ ਨਾਲ ਜੁੜਦਾ ਹੈ, ਤਾਂ Pi ਵਾਲੇ ਸਿਰੇ ਨੂੰ ਆਉਟਪੁੱਟ ਬਣਾਉਣ ਨਾਲ ਬਿਜਲੀ ਟਕਰਾਅ ਦਾ ਜੋਖ਼ਮ ਹੈ। ਇਹ ਅੰਤਰ ਜਾਂਚ ਦੀ ਲੋੜ ਦੱਸਦਾ ਹੈ, ਨੁਕਸਾਨ ਜਾਂ ਸਾਰੇ M1 ਲਈ ਇੱਕੋ ਵਾਇਰਿੰਗ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ।

ਸਾਰੀ ਬਿਜਲੀ ਹਟਾ ਕੇ ਹੈਡਰ ਅਤੇ ਮੋਡੀਊਲ ਕਨੈਕਟਰ ਵਿਚਕਾਰ ਦਿਖਾਈ ਦੇਣ ਵਾਲੇ ਜੋੜ ਲੱਭੋ। ਬੋਰਡ ਰਿਵਿਜ਼ਨ ਅਤੇ ਦੋਵੇਂ ਸਿਰੇ ਲਿਖੋ। continuity ਨਤੀਜਾ ਜੋੜ ਸਾਬਤ ਕਰਦਾ ਹੈ; ਸਿਗਨਲ ਦੀ ਦਿਸ਼ਾ ਅਤੇ ਬਿਜਲੀ ਹੱਦ ਲਈ ਹਿੱਸੇ ਦੇ ਦਸਤਾਵੇਜ਼ ਵੇਖੋ।

ਮੋਡੀਊਲ ਦਾ ਹੇਠਾਂ ਦਿੱਤਾ ਡਾਇਗ੍ਰਾਮ ਵਰਤ ਕੇ edge connector ਪਿਨ ਅਤੇ Pi ਹੈਡਰ ਪਿਨ ਨਾ ਗਲਤ ਮਿਲਾਓ। ਵਾਧੂ ਰੇਡੀਓ ਲੇਬਲ ਪ੍ਰਕਾਸ਼ਿਤ ਮੋਡੀਊਲ ਰੈਫ਼ਰੈਂਸ ਦੱਸਦੇ ਹਨ, ਹਰ ਰਿਵਿਜ਼ਨ ਵਿੱਚ ਇਕੋ ਚਿਪ ਜਾਂ ਫੀਚਰ ਸਾਬਤ ਨਹੀਂ ਕਰਦੇ। [Seeed WM1302 ਮੋਡੀਊਲ ਪਿਨਆਉਟ](https://github.com/seeed-lora/WM1302-doc/blob/master/pinout.jpg)

{{< figure src="wm1302-module-edge-connector.webp" alt="WM1302 ਮੋਡੀਊਲ edge connector ਦੇ ਦੋਵੇਂ ਪਾਸਿਆਂ ਉੱਤੇ ਪਾਵਰ, SPI, I2C ਅਤੇ ਵਾਧੂ ਰੇਡੀਓ ਸਿਗਨਲ ਦਿਖਾਉਂਦਾ Seeed ਡਾਇਗ੍ਰਾਮ" caption="ਮੋਡੀਊਲ edge connector ਦੀ ਨੰਬਰਿੰਗ Raspberry Pi ਹੈਡਰ ਤੋਂ ਵੱਖਰੀ ਹੈ" credit="Seeed Studio" attr="Seeed Studio, WM1302-doc" attrlink="https://github.com/seeed-lora/WM1302-doc" >}}

## Raspberry Pi OS ਤਿਆਰ ਕਰੋ

ਵਾਧੂ ਇੰਸਟਾਲੇਸ਼ਨ ਉੱਤੇ ਹੋਸਟ ਵਾਤਾਵਰਣ ਦਰਜ ਕਰੋ:

```bash
cat /etc/os-release
uname -r
tr -d '\0' < /proc/device-tree/model
```

OS ਰਿਲੀਜ਼, kernel ਅਤੇ Pi ਮਾਡਲ ਦੁਹਰਾਈ ਜਾ ਸਕਣ ਵਾਲੀ ਸ਼ੁਰੂਆਤ ਬਣਾਉਂਦੇ ਹਨ। ਪੁਰਾਣੇ ਟਿਊਟੋਰਿਅਲ ਨਾਲ ਨਤੀਜੇ ਮਿਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਲਿਖੋ।

ਜਾਂਚ ਅਤੇ build ਟੂਲ ਲਗਾਓ:

```bash
sudo apt update
sudo apt install git build-essential i2c-tools gpiod
sudo raspi-config
```

**Interface Options** ਵਿੱਚ SPI ਅਤੇ I2C ਚਾਲੂ ਕਰਕੇ reboot ਕਰੋ। SPI concentrator ਰਸਤੇ ਲਈ ਹੈ, I2C ਅੱਗੇ ਦੱਸੇ ਪ੍ਰਬੰਧਕੀ ਡਿਵਾਈਸਾਂ ਲਈ। ਕਿਸੇ ਹੋਰ HAT ਟਿਊਟੋਰਿਅਲ ਤੋਂ ਬੇਲੋੜੇ GPS serial-port ਬਦਲਾਅ ਨਾ ਲਿਆਓ।

ਖੁੱਲ੍ਹੇ ਇੰਟਰਫੇਸ ਵੇਖੋ:

```bash
ls -l /dev/spidev* /dev/i2c-*
i2cdetect -l
gpiodetect
gpioinfo
gpioset --version
```

ਇਹ ਕਮਾਂਡਾਂ ਡਿਵਾਈਸ ਨੋਡ, ਐਡੈਪਟਰ, GPIO ਕੰਟਰੋਲਰ, ਲਾਈਨਾਂ ਅਤੇ ਲੱਗੇ GPIO ਟੂਲ ਦਾ ਵਰਜਨ ਦਿਖਾਉਂਦੀਆਂ ਹਨ। **`i2cdetect -l` ਪਤੇ ਸਕੈਨ ਕੀਤੇ ਬਿਨਾਂ ਐਡੈਪਟਰ ਲਿਸਟ ਕਰਦਾ ਹੈ।** `/dev/spidev0.0` ਫਾਈਲ SPI ਇੰਟਰਫੇਸ ਖੁੱਲ੍ਹਾ ਹੋਣ ਦਾ ਸਬੂਤ ਹੈ, ਚੱਲਦੇ concentrator ਨਾਲ ਸੰਚਾਰ ਦਾ ਨਹੀਂ। [i2c-tools ਮੈਨੂਅਲ](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), [Raspberry Pi GPIO ਹਦਾਇਤਾਂ](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

### GPIO ਵਰਜਨ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ

**ਹੋਰ ਮਸ਼ੀਨ ਦੇ global GPIO ਨੰਬਰ ਨਕਲ ਨਾ ਕਰੋ।** ਪੁਰਾਣੀਆਂ ਸਕ੍ਰਿਪਟਾਂ `/sys/class/gpio` ਵਰਤਦੀਆਂ ਹਨ, ਜਿਸਨੂੰ kernel ਦਸਤਾਵੇਜ਼ ਪੁਰਾਣੀ ਇੰਟਰਫੇਸ ਕਹਿੰਦੇ ਹਨ। ਨਵੇਂ user-space ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਸਹੀ ਕੰਟਰੋਲਰ ਅਤੇ line offset ਨਾਲ GPIO character-device ਇੰਟਰਫੇਸ ਵਰਤਣ। [Linux GPIO ਦਸਤਾਵੇਜ਼](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)

ਸਕ੍ਰਿਪਟ ਅਨੁਕੂਲ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ `gpioset --help` ਵੀ ਵੇਖੋ। ਵਰਜਨ 1 ਅਤੇ 2 ਵਿੱਚ syntax ਅਤੇ process ਦਾ ਵਿਹਾਰ ਵੱਖਰਾ ਹੈ। ਮੌਜੂਦਾ ਟੂਲ ਮੰਗੀਆਂ ਲਾਈਨਾਂ ਮੂਲ ਰੂਪ ਵਿੱਚ ਫੜੀ ਰੱਖਦਾ ਹੈ, ਪਰ portable ਸਮਝੌਤਾ process ਮੁੱਕਣ ਤੋਂ ਬਾਅਦ ਹਾਲਤ ਦੀ ਗਾਰੰਟੀ ਨਹੀਂ ਦਿੰਦਾ। [libgpiod gpioset ਦਸਤਾਵੇਜ਼](https://libgpiod.readthedocs.io/en/master/gpioset.html)

Raspberry Pi kernel ਵਿੱਚ output ਕਾਇਮ ਰਹਿਣ ਦਾ ਵਿਹਾਰ ਅਤੇ ਇਸਨੂੰ ਬਦਲਣ ਦੇ ਵਿਕਲਪ ਦਰਜ ਕਰਦਾ ਹੈ। ਹਰ Linux ਇੱਕੋ ਵਰਤਾਅ ਕਰੇਗਾ ਇਹ ਮੰਨਣ ਦੀ ਥਾਂ ਅਸਲ kernel ਸੰਰਚਨਾ ਲਿਖੋ। ਨੰਬਰਿੰਗ ਜਾਂ ਟੂਲ ਅੱਪਡੇਟ ਕਰਨ ਨਾਲ ਗਲਤ ਬਿਜਲੀ ਮੈਪਿੰਗ ਠੀਕ ਨਹੀਂ ਹੁੰਦੀ। [Raspberry Pi GPIO ਵਰਤੋਂ ਗਾਈਡ](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

## ਯੂਜ਼ਰ LED ਜਾਂਚੋ

GPIO22 LED ਨਾਲ ਜੁੜਿਆ ਹੈ ਅਤੇ ਟਕਰਾਉਂਦੇ GPIO ਵਰਤੋਂਕਾਰ ਹਟਾਏ ਹਨ, ਇਹ ਪੱਕਾ ਕਰਨ ਤੋਂ ਬਾਅਦ boot config ਸੋਧੋ:

```bash
sudoedit /boot/firmware/config.txt
```

ਨਵੇਂ Raspberry Pi OS ਵਿੱਚ boot config **`/boot/firmware/config.txt`** ਉੱਤੇ ਹੈ। ਪੁਰਾਣੀਆਂ ਇਮੇਜਾਂ `/boot/config.txt` ਵਰਤਦੀਆਂ ਹਨ, ਜੋ 2023 ਲੇਖ ਦਾ ਰਸਤਾ ਸੀ। ਸੋਧਣ ਤੋਂ ਪਹਿਲਾਂ ਸਰਗਰਮ ਫਾਈਲ ਦੀ ਨਕਲ ਰੱਖੋ। [Raspberry Pi config.txt ਦਸਤਾਵੇਜ਼](https://www.raspberrypi.com/documentation/computers/config_txt.html)

ਆਪਣੇ Pi ਲਈ ਲਾਗੂ ਭਾਗ, ਜਿਵੇਂ `[all]`, ਹੇਠ LED overlay ਜੋੜੋ:

```ini
dtoverlay=gpio-led,gpio=22,label=lorawan,trigger=heartbeat
```

**`gpio`** ਪੈਰਾਮੀਟਰ BCM ਨੰਬਰ ਵਰਤਦਾ ਹੈ। **`label`** Linux LED ਡਿਵਾਈਸ ਨੂੰ ਨਾਂ ਦਿੰਦਾ ਹੈ ਅਤੇ **`trigger=heartbeat`** kernel heartbeat trigger ਸੈੱਟ ਕਰਦਾ ਹੈ। Clockwork Bird M1 ਲਈ ਇਹ ਨਿਯੁਕਤੀ ਦੱਸਦਾ ਹੈ; Raspberry Pi overlay ਹਵਾਲਾ ਵੀ ਪੈਰਾਮੀਟਰ ਦਰਜ ਕਰਦਾ ਹੈ। [ਮੂਲ LED ਨਿਰੀਖਣ](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), [gpio-led overlay ਹਵਾਲਾ](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README)

Reboot ਤੋਂ ਬਾਅਦ ਦਰਜ LED ਵੇਖੋ:

```bash
ls -l /sys/class/leds/
cat /sys/class/leds/lorawan/trigger
```

ਉਮੀਦ ਦਾ ਨਤੀਜਾ `lorawan` LED ਐਂਟਰੀ ਹੈ, ਜਿਸ ਵਿੱਚ `heartbeat` ਚੌਰਸ ਬਰੈਕਟਾਂ ਵਿੱਚ ਚੁਣਿਆ ਹੈ। LED ਦਾ ਟਿਮਟਿਮਾਉਣਾ GPIO/ਡਰਾਈਵਰ ਰਸਤਾ ਦਿਖਾਉਂਦਾ ਹੈ। ਇਹ LoRaWAN ਰਜਿਸਟ੍ਰੇਸ਼ਨ, ਰੇਡੀਓ ਪ੍ਰਾਪਤੀ ਜਾਂ Helium ਹਾਲਤ ਨਹੀਂ ਦੱਸਦਾ।

## I2C ਡਿਵਾਈਸਾਂ ਦੀ ਜਾਂਚ ਕਰੋ

**I2C ਪਤਾ ਇੱਕ ਇਸ਼ਾਰਾ ਹੈ, ਡਿਵਾਈਸ ਦੀ ਪਛਾਣ ਨਹੀਂ।** Clockwork Bird ਨੇ `0x60` ਅਤੇ `0x39` ਉੱਤੇ ਜਵਾਬ ਵੇਖਿਆ, ਫਿਰ crypto ਲਾਇਬ੍ਰੇਰੀ ਨਾਲ ATECC608 ਜਾਣਕਾਰੀ ਪੜ੍ਹੀ। ਅਸਲ ਲੇਖ ਵਿੱਚ ਤਾਪਮਾਨ ਸੈਂਸਰ ਦੀ ਪਛਾਣ ਅਜੇ ਅਨੁਮਾਨ ਸੀ।

ਪਿਛਲੇ ਭਾਗ ਦੀ ਐਡੈਪਟਰ ਸੂਚੀ ਤੋਂ ਸ਼ੁਰੂ ਕਰੋ। ਵਿਆਪਕ `i2cdetect` ਸਕੈਨ ਸਿਰਫ਼ ਸੁਣਦੇ ਨਹੀਂ, probe ਲੈਣ-ਦੇਣ ਭੇਜਦੇ ਹਨ; upstream ਮੈਨੂਅਲ ਰੁਕਾਵਟ ਦੀ ਚੇਤਾਵਨੀ ਦਿੰਦਾ ਹੈ। ਚੱਲਦੇ ਗੇਟਵੇ ਜਾਂ ਅਣਜਾਣ ਜੁੜੇ ਡਿਵਾਈਸ ਨੂੰ ਰੁਟੀਨ ਵਿੱਚ ਸਕੈਨ ਨਾ ਕਰੋ। [i2c-tools probe ਵਿਹਾਰ](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)

| ਨਿਰੀਖਣ | ਸਮਰਥਿਤ ਨਤੀਜਾ | ਬਾਕੀ ਸਵਾਲ |
|---|---|---|
| **`0x60` ਉੱਤੇ ਜਵਾਬ** | ਕਿਸੇ ਨੇ probe ਮਨਜ਼ੂਰ ਕੀਤਾ | ਕੀ ਇਹ ਉਮੀਦ ਵਾਲਾ ਸੁਰੱਖਿਅਤ ਤੱਤ ਹੈ? |
| **`0x39` ਉੱਤੇ ਜਵਾਬ** | ਕਿਸੇ ਨੇ probe ਮਨਜ਼ੂਰ ਕੀਤਾ | ਕਿਹੜਾ ਹਿੱਸਾ ਅਤੇ ਰਿਵਿਜ਼ਨ ਜਵਾਬ ਦਿੰਦੇ ਹਨ? |
| **ਸਕੈਨ ਵਿੱਚ `UU`** | ਡਰਾਈਵਰ ਪਤਾ ਵਰਤਦਾ ਹੈ, probe ਛੱਡਿਆ ਗਿਆ | ਕਿਹੜਾ ਡਰਾਈਵਰ ਇਸਨੂੰ ਵਰਤਦਾ ਹੈ? |
| **ਜਵਾਬ ਨਹੀਂ** | probe ਨੂੰ ਕੋਈ ਪੁਸ਼ਟੀ ਨਹੀਂ ਮਿਲੀ | ਬਿਜਲੀ, ਬੱਸ, ਵਰਤੋਂਕਾਰ ਜਾਂ ਡਿਵਾਈਸ ਪ੍ਰੋਟੋਕੋਲ? |

### ਤਾਪਮਾਨ ਸੈਂਸਰ ਦੀ ਸੰਭਾਵਨਾ ਮਜ਼ਬੂਤ ਕਰੋ

**STTS751, `0x39` ਲਈ ਸਰੋਤਾਂ ਨਾਲ ਸਮਰਥਿਤ ਸੰਭਾਵਨਾ ਹੈ।** Semtech ਤਾਪਮਾਨ ਡਰਾਈਵਰ ਹੈਡਰ `0x39` ਨੂੰ ਸਪਸ਼ਟ ਤੌਰ ਉੱਤੇ `STTS751-0DP3F` ਨਾਲ ਜੋੜਦਾ ਹੈ। ਇਹ ਅਸਲ ਧਾਰਨਾ ਨੂੰ ਮਜ਼ਬੂਤ ਕਰਦਾ ਹੈ ਪਰ ਇਸ ਪਤੇ ਵਾਲੇ ਹਰ ਬੋਰਡ ਦੀ ਪਛਾਣ ਨਹੀਂ ਕਰਦਾ। [Semtech STTS751 ਡਰਾਈਵਰ ਹੈਡਰ](https://github.com/Lora-net/sx1302_hal/blob/master/libloragw/inc/loragw_stts751.h)

ਅਨੁਕੂਲ ਹਿੱਸਾ ਪਛਾਣ ਕੇ ਅਤੇ ਹੋਰ ਪ੍ਰਕਿਰਿਆ ਇਸਦੀ ਵਰਤੋਂ ਨਹੀਂ ਕਰਦੀ ਯਕੀਨੀ ਕਰਨ ਤੋਂ ਬਾਅਦ ਪਛਾਣ ਰਜਿਸਟਰ ਪੜ੍ਹੋ:

```bash
sudo i2cget 1 0x39 0xfd b
sudo i2cget 1 0x39 0xfe b
```

ਇੱਥੇ **`1`** ਜਾਂਚੀ ਬੱਸ, **`0x39`** ਡਿਵਾਈਸ ਅਤੇ **`b`** SMBus byte-data ਰੀਡ ਚੁਣਦਾ ਹੈ। STTS751-0 ਲਈ ਦਸਤਾਵੇਜ਼ੀ product ID `0xFD` ਉੱਤੇ `0x00` ਅਤੇ manufacturer ID `0xFE` ਉੱਤੇ `0x53` ਹੈ। ਇਹ ਲੈਣ-ਦੇਣ ਰਜਿਸਟਰ ਪਤਾ ਚੁਣਦੇ ਹਨ, ਸੰਰਚਨਾ ਨਹੀਂ ਲਿਖਦੇ। [STTS751 ਡਾਟਾਸ਼ੀਟ, ਰਜਿਸਟਰ ਮੈਪ ਅਤੇ ਪਛਾਣ ਰਜਿਸਟਰ](https://www.st.com/resource/en/datasheet/stts751.pdf)

ਰੀਡਿੰਗਾਂ ਨੂੰ ਚਿਪ ਦੇ ਨਿਸ਼ਾਨ ਅਤੇ ਦਸਤਾਵੇਜ਼ ਨਾਲ ਮਿਲਾਓ। ਦੋਵੇਂ ਮੁੱਲ ਮਿਲਣ ਨਾਲ ਪਛਾਣ ਦਾ ਸਬੂਤ ਵਧਦਾ ਹੈ। ਗਲਤੀ ਆਵੇ ਤਾਂ ਹਾਰਡਵੇਅਰ ਸੰਰਚਨਾ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਬੱਸ ਅਤੇ ਵਰਤੋਂਕਾਰ ਵੇਖੋ। ਸੈਂਸਰ ਆਪਣੇ ਨੇੜੇ ਦਾ ਤਾਪਮਾਨ ਮਾਪਦਾ ਹੈ, Pi CPU ਦਾ ਨਹੀਂ।

## ਸੁਰੱਖਿਅਤ ਤੱਤ ਜਾਂਚੋ

**ATECC608 ਵੱਖਰਾ authentication ਹਿੱਸਾ ਹੈ।** ਇਸਦੀ ਸੰਰਚਨਾ, ਸੀਰੀਅਲ ਨੰਬਰ, ਜਨਤਕ ਕੁੰਜੀ ਅਤੇ ਸੁਰੱਖਿਅਤ ਕੁੰਜੀ ਸਮੱਗਰੀ ਵੱਖਰੀਆਂ ਚੀਜ਼ਾਂ ਹਨ। ਜਨਤਕ ਕੁੰਜੀ ਪੜ੍ਹਨ ਨਾਲ ਉਸਦੀ ਨਿੱਜੀ ਕੁੰਜੀ ਨਹੀਂ ਮਿਲਦੀ।

Microchip ਦੀ **CryptoAuthLib** ਡਿਵਾਈਸ ਇੰਟਰਫੇਸ ਦਿੰਦੀ ਹੈ। **cryptoauthtools** ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਇਸ ਲਾਇਬ੍ਰੇਰੀ ਵਾਲੀਆਂ ਮਿਸਾਲਾਂ ਹਨ। ਮਿਸਾਲ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਪ੍ਰੋਜੈਕਟ ਹਦਾਇਤਾਂ ਨਾਲ ਟੀਚਾ ਸਿਸਟਮ ਲਈ native library ਅਤੇ Python bindings ਤਿਆਰ ਕਰੋ। ਗੈਰ-ਸੰਬੰਧਤ Python ਪੈਕੇਜ ਲਾਉਣ ਜਾਂ ਇਕੱਲੀ ਸਕ੍ਰਿਪਟ ਨਕਲ ਕਰਨ ਨਾਲ I2C backend ਚੱਲਦਾ ਸਾਬਤ ਨਹੀਂ ਹੁੰਦਾ। [Microchip CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [Microchip cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools)

ਤਿਆਰ `cryptoauthtools/python/examples` ਡਾਇਰੈਕਟਰੀ ਤੋਂ ਅਸਲ ਲੇਖ ਦੀ ਜਾਂਚ ਕਮਾਂਡ ਚਲਾਓ:

```bash
sudo python3 info.py -i i2c
```

**`-i i2c`** ਆਰਗੂਮੈਂਟ ਇੰਟਰਫੇਸ ਚੁਣਦਾ ਹੈ। ਵਰਚੁਅਲ ਮਾਹੌਲ ਵਿੱਚ ਉਸਦਾ ਸਪਸ਼ਟ Python interpreter ਵਰਤੋ ਅਤੇ ਯਕੀਨੀ ਕਰੋ ਕਿ ਮਿਲਦੀ native library ਮਿਲਦੀ ਹੈ। ਕਈ ਇੰਸਟਾਲੇਸ਼ਨਾਂ ਵਿੱਚ `sudo python3` ਸਿਸਟਮ interpreter ਚੁਣਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਕੁਝ module import ਫੇਲ੍ਹ ਹੁੰਦੇ ਹਨ।

ਜਾਂਚਿਆ `info.py` ਰਿਵਿਜ਼ਨ ਜਾਣਕਾਰੀ, ਸੀਰੀਅਲ ਨੰਬਰ, ਸੰਰਚਨਾ ਅਤੇ ਲਾਕ ਹਾਲਤ ਪੜ੍ਹਦਾ ਹੈ। Data zone ਲਾਕ ਹੋਵੇ ਤਾਂ slot 0 ਤੋਂ ਜਨਤਕ ਕੁੰਜੀ ਲੈਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦਾ ਹੈ। ਇਹ ਮਿਸਾਲ ਦੀ provisioning ਲੜੀ ਨਹੀਂ ਚਲਾਉਂਦਾ। ਸਿਰਫ਼ slot-0 ਜਨਤਕ ਕੁੰਜੀ ਪੜ੍ਹਨ ਦੀ ਨਾਕਾਮੀ ਡਿਵਾਈਸ ਖਰਾਬ ਹੋਣ ਦਾ ਸਬੂਤ ਨਹੀਂ। [Microchip info.py ਸਰੋਤ](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/info.py)

| ਨਤੀਜਾ ਜਾਂ ਕੰਮ | ਮਤਲਬ |
|---|---|
| **Configuration locked** | ਸੰਰਚਨਾ ਉੱਤੇ ਰੋਕ ਲਾਗੂ ਹੈ |
| **Data zone locked** | ਸੰਰਚਿਤ slot policy ਅਨੁਸਾਰ ਪਹੁੰਚ ਸਮਝੋ |
| **ਜਨਤਕ ਕੁੰਜੀ ਦਿਖੀ** | ਜਨਤਕ ਜਾਣਕਾਰੀ ਮਿਲੀ, ਨਿੱਜੀ ਕੁੰਜੀ ਨਹੀਂ ਕੱਢੀ |
| **`config.py` ਚਲਾਉਣਾ** | ਸੰਰਚਨਾ, ਲਾਕ ਅਤੇ key generation ਵਾਲੀ provisioning ਮਿਸਾਲ |

**ਜਾਂਚ ਗਲਤੀ ਠੀਕ ਕਰਨ ਲਈ `config.py` ਨਾ ਚਲਾਓ।** ਇਸਦੇ ਸਰੋਤ ਵਿੱਚ ਸੰਰਚਨਾ ਲਿਖਣਾ, zone ਲਾਕ ਕਰਨਾ ਅਤੇ ਕੁੰਜੀ ਬਣਾਉਣ ਵਾਲੇ ਕਾਲ ਹਨ। ਪਹਿਲਾਂ ਸੰਰਚਿਤ ਡਿਵਾਈਸ ਉੱਤੇ ਡਿਫਾਲਟ key-generation ਰਸਤਾ ਵੀ ਮਹੱਤਵ ਰੱਖਦਾ ਹੈ। [Microchip config.py ਸਰੋਤ](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/config.py)

Microchip ਦੇ ਦਸਤਾਵੇਜ਼ੀ provisioning profile ਦਿਖਾਉਂਦੇ ਹਨ ਕਿ data zone ਲਾਕ ਹੋਣ ਦਾ ਮਤਲਬ ਸਾਰੇ slot ਦੇ ਅਧਿਕਾਰ ਇੱਕੋ ਨਹੀਂ। ਇਹ profile M1 ਦੀ ਠੀਕ ਸੰਰਚਨਾ ਨਹੀਂ ਦੱਸਦੇ। ਮੌਜੂਦਾ ਸੰਰਚਨਾ ਬਚਾਓ ਅਤੇ ਕੁੰਜੀਆਂ ਮੁੜ ਵਰਤਣ ਦੀ ਯੋਜਨਾ ਤੋਂ ਪਹਿਲਾਂ ਸਹੀ ਪਾਰਟ ਦੇ ਦਸਤਾਵੇਜ਼ ਵੇਖੋ। [Microchip memory ਅਤੇ slot-access ਨੀਤੀ](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html)

## ਪੱਖੇ ਅਤੇ ਬਟਨ ਦੇ ਅਣਜਾਣ ਹਿੱਸੇ ਹੱਲ ਕਰੋ

**ਤਿੰਨ-ਪਿਨ ਪੱਖਾ ਸਾਕਟ ਉਸਦਾ ਵੋਲਟੇਜ, ਧਰੂਵਤਾ ਜਾਂ ਕੰਟਰੋਲ ਤਰੀਕਾ ਨਹੀਂ ਦੱਸਦਾ।** ਪਿਨ ਨੰਬਰਾਂ ਦੀ ਤਸਵੀਰ ਲਓ ਅਤੇ ਪੱਖੇ ਦਾ ਲੇਬਲ ਪੜ੍ਹੋ। ਬਦਲਵਾਂ ਪੱਖਾ ਜੋੜਨ ਜਾਂ GPIO overlay ਚੁਣਨ ਤੋਂ ਪਹਿਲਾਂ ਪਾਵਰ ਤੇ ਕੰਟਰੋਲ ਕੁਨੈਕਸ਼ਨ ਪੱਕੇ ਕਰੋ।

ਅਸਲ ਜਾਂਚ ਬਟਨ ਦਾ GPIO ਵੀ ਨਹੀਂ ਦੱਸਦੀ। ਆਪਣੇ ਬੋਰਡ ਰਿਵਿਜ਼ਨ ਵਾਲਾ ਡਰਾਈਵਰ ਜਾਂ ਸੰਰਚਨਾ ਲੱਭੋ, ਫਿਰ ਬਿਜਲੀ ਬੰਦ ਕਰਕੇ ਕੁਨੈਕਸ਼ਨ ਜਾਂਚੋ। ਬਟਨ ਲੱਭਣ ਲਈ ਹਰ ਖਾਲੀ ਦਿੱਸਦੇ GPIO ਨੂੰ ਆਉਟਪੁੱਟ ਨਾ ਬਣਾਓ।

| ਪੈਰੀਫਿਰਲ | ਇਕੱਠਾ ਕਰਨ ਵਾਲਾ ਸਬੂਤ | ਸਵੀਕ੍ਰਿਤੀ ਸ਼ਰਤ |
|---|---|---|
| **ਪੱਖੇ ਦੀ ਬਿਜਲੀ** | ਪੱਖੇ ਦੀ ਰੇਟਿੰਗ, ਕਨੈਕਟਰ ground ਅਤੇ supply | ਮਾਪੀ supply ਪੱਖੇ ਦੇ ਨਿਰਧਾਰਨ ਨਾਲ ਮਿਲੇ |
| **ਪੱਖਾ ਕੰਟਰੋਲ** | ਡਰਾਈਵਰ/config ਜਾਂ ਲੱਭਿਆ ਕੰਟਰੋਲ ਸਰਕਟ | ਸ਼ੁਰੂਆਤ ਅਤੇ ਵੱਧ ਤਾਪਮਾਨ ਉੱਤੇ ਵਰਤਾਅ ਨਿਰਧਾਰਤ |
| **ਯੂਜ਼ਰ ਬਟਨ** | ਸੰਪਰਕ ਵਾਇਰਿੰਗ, GPIO ਮੈਪ, ਇਨਪੁੱਟ polarity | ਇੱਕ ਜਾਣਬੁੱਝ ਕੇ ਦਬਾਅ ਨਾਲ ਉਮੀਦ ਵਾਲਾ event ਆਵੇ |

ਨਵੀਂ OS ਇੰਸਟਾਲੇਸ਼ਨ ਅਸਲ ਉਪਕਰਣ ਦੀ cooling policy ਆਪਣੇ ਆਪ ਨਹੀਂ ਬਣਾਉਂਦੀ। ਪਹਿਲੇ ਲੰਮੇ ਟੈਸਟ ਵਿੱਚ ਪੱਖਾ ਤੇ ਤਾਪਮਾਨ ਇਕੱਠੇ ਵੇਖੋ। ਕੇਸ ਦਾ ਹਵਾ ਰਸਤਾ ਖੁੱਲ੍ਹਾ ਰੱਖੋ ਅਤੇ ਲੋੜੀਂਦੀ cooling ਨਾ ਹੋਵੇ ਤਾਂ ਟੈਸਟ ਰੋਕੋ।

## ਗੇਟਵੇ ਸਟੈਕ ਚੁਣੋ

**ਬੋਰਡ ਸਹਾਇਤਾ ਅਤੇ ਸਰਵਰ ਪ੍ਰੋਟੋਕੋਲ ਵੱਖਰੇ ਰੱਖੋ।** ਅਨੁਕੂਲ LoRaWAN ਸਰਵਰ ਗਲਤ reset routine ਜਾਂ RF calibration ਨਹੀਂ ਠੀਕ ਕਰਦਾ। ਪਹਿਲਾਂ ਅਜਿਹਾ ਸੌਫਟਵੇਅਰ ਚੁਣੋ ਜੋ concentrator, ਕੈਰੀਅਰ ਵਾਇਰਿੰਗ, OS ਅਤੇ ਖੇਤਰੀ ਸੰਰਚਨਾ ਨੂੰ ਸਹਾਰਦਾ ਹੋਵੇ।

| ਸੌਫਟਵੇਅਰ ਰਸਤਾ | ਲਾਭਦਾਇਕ ਕੰਮ | ਲਗਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਜਾਂਚ |
|---|---|---|
| **Semtech SX1302 HAL** | source ਪੱਧਰ ਉੱਤੇ ਚਾਲੂ ਕਰਨਾ ਅਤੇ ਜਾਂਚ ਟੂਲ | ਬੋਰਡ reset routine ਅਤੇ ਮੋਡੀਊਲ config |
| **LoRa Basics Station** | ਸਰਵਰ ਨਾਲ ਗੇਟਵੇ ਦਾ ਪ੍ਰਮਾਣਿਤ ਕੁਨੈਕਸ਼ਨ | ਚੱਲਦਾ ਬੋਰਡ ਇਕੀਕਰਨ ਅਤੇ ਸਰਵਰ credentials |
| **ChirpStack Concentratord** | ਵੱਖਰੀ concentrator ਸੇਵਾ | ਸਮਰਥਿਤ ਮਾਡਲ, calibration ਅਤੇ GPIO ਮੈਪ |

ChirpStack SPI **`seeed_wm1302`** ਮਾਡਲ ਦਰਜ ਕਰਦਾ ਹੈ। ਇਹ ਮੋਡੀਊਲ ਸਹਾਇਤਾ ਦਾ ਸਬੂਤ ਹੈ, ਪੂਰੀ M1 ਇਮੇਜ ਜਾਂ ਹਰ M1 ਰਿਵਿਜ਼ਨ ਦੀ ਗਾਰੰਟੀ ਨਹੀਂ। ਵੱਖਰੇ SenseCAP M2 ਇੰਸਟਾਲ ਨਿਰਦੇਸ਼ M1 firmware ਲਈ ਨਹੀਂ ਹਨ। [ChirpStack ਹਾਰਡਵੇਅਰ ਸਹਾਇਤਾ](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html), [ChirpStack Seeed ਇੰਸਟਾਲ ਟੀਚਾ](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html)

The Things Stack ਦਸਤਾਵੇਜ਼ ਪੁਰਾਣੇ Semtech UDP forwarder ਦੀ ਥਾਂ **LoRa Basics Station** ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕਰਦੇ ਹਨ। Station TLS ਅਤੇ token authentication ਨਾਲ ਕੇਂਦਰੀ ਸੰਰਚਨਾ ਦਿੰਦਾ ਹੈ। UDP ਮਿਸਾਲਾਂ ਪੈਕੇਟ ਫਾਰਵਰਡਿੰਗ ਸਮਝਾਉਂਦੀਆਂ ਹਨ, ਪਰ ਸਰਵਰ ਪਤੇ ਦੀ ਸੈਟਿੰਗ ਇਹ ਸੁਰੱਖਿਆ ਨਹੀਂ ਦਿੰਦੀ। [The Things Stack UDP ਹਦਾਇਤਾਂ](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [LoRa Basics Station ਦਸਤਾਵੇਜ਼](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)

### Upstream ਟੂਲ ਤਿਆਰ ਕਰੋ

ਟੀਚਾ Pi ਉੱਤੇ ਨਵੀਂ ਕੰਮ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ build ਕਰੋ:

```bash
git clone https://github.com/Lora-net/sx1302_hal.git
cd sx1302_hal
git rev-parse HEAD
make
```

Build output ਨਾਲ commit ਪਛਾਣ ਸੰਭਾਲੋ। ਸਫਲ build compiler ਅਨੁਕੂਲਤਾ ਦਿਖਾਉਂਦਾ ਹੈ, ਜਦਕਿ ਰੇਡੀਓ ਲਈ ਜਾਂਚਿਆ reset ਤਰੀਕਾ ਅਤੇ ਸਹੀ ਸੰਰਚਨਾ ਵੀ ਲੋੜੀਂਦੇ ਹਨ। Semtech ਦਸਤਾਵੇਜ਼ HAL ਅਤੇ ਸਹਾਇਕ ਪ੍ਰੋਗਰਾਮਾਂ ਦੀ ਭੂਮਿਕਾ ਦੱਸਦੇ ਹਨ। [SX1302 HAL build ਅਤੇ ਟੂਲ ਦਸਤਾਵੇਜ਼](https://github.com/Lora-net/sx1302_hal)

ਹਾਰਡਵੇਅਰ ਪਹੁੰਚ ਵਾਲੇ ਟੂਲ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ reset ਫਾਈਲ ਵੇਖੋ:

```bash
sed -n '1,180p' tools/reset_lgw.sh
```

ਇਹ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲੇ runtime ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਨਾ ਕਾਪੀ ਕਰੋ। Semtech ਹਾਰਡਵੇਅਰ ਪਹੁੰਚ ਪ੍ਰੋਗਰਾਮਾਂ, ਪਛਾਣ ਟੂਲਾਂ ਸਮੇਤ, ਵੱਲੋਂ reset ਸਕ੍ਰਿਪਟ ਆਪਣੇ ਆਪ ਵਰਤਣ ਦਾ ਜ਼ਿਕਰ ਕਰਦਾ ਹੈ। ਆਪਣੀ ਜਾਂਚ ਵਿੱਚ ਹਰ ਲਗਾਇਆ ਪਿਨ, ਸਿਗਨਲ ਦਿਸ਼ਾ, GPIO API ਅਤੇ ਸ਼ੁਰੂ/ਬੰਦ ਹੋਣ ਦੀ ਹਾਲਤ ਵੇਖੋ।

ਬੋਰਡ ਜਾਂਚ ਮਗਰੋਂ ਚੁਣੇ ਸਟੈਕ ਦੇ ਨਿਰਦੇਸ਼ਾਂ ਨਾਲ concentrator EUI ਪੜ੍ਹੋ ਅਤੇ ਗੇਟਵੇ ਦਰਜ ਕਰੋ। ਸਰਵਰ ਸੰਰਚਨਾ ਜੋੜਦੇ ਵੇਲੇ ਮੋਡੀਊਲ ਦੀ calibration ਅਤੇ RF setting ਰੱਖੋ। Semtech UDP ਵਿੱਚ `gateway_ID` EUI ਹੈ; The Things Stack ਕਨਸੋਲ ਦਾ Gateway ID ਦਰਜ ਕੀਤਾ ਮਨੁੱਖ-ਪੜ੍ਹਨਯੋਗ ਨਾਂ ਹੈ। [The Things Stack ਗੇਟਵੇ ਸੰਰਚਨਾ](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)

## ਸੈਂਸਰ ਡਿਲਿਵਰੀ ਸਾਬਤ ਕਰੋ

**ਸਭ ਤੋਂ ਪਹਿਲਾਂ ਫੇਲ੍ਹ ਪਰਤ ਲੱਭਣ ਲਈ ਪੜਾਅਵਾਰ ਸਬੂਤ ਵਰਤੋ।** ਗੇਟਵੇ ਦਾ online ਦਿਖਣਾ ਸਰਵਰ ਕੁਨੈਕਸ਼ਨ ਸਾਬਤ ਕਰਦਾ ਹੈ। ਸਵੀਕ੍ਰਿਤੀ ਟੈਸਟ ਲਈ ਜਾਣਿਆ ਸੈਂਸਰ, ਮੇਲ ਖਾਂਦੀ frequency plan ਅਤੇ decode ਕੀਤਾ ਐਪ payload ਵੀ ਚਾਹੀਦਾ ਹੈ।

ਹੇਠਲਾ ਕ੍ਰਮ ਪ੍ਰਸਤਾਵਿਤ ਟੈਸਟ ਯੋਜਨਾ ਹੈ, M1 ਉੱਤੇ ਮਾਪਿਆ ਨਤੀਜਾ ਨਹੀਂ:

| ਜਾਂਚ ਪੜਾਅ | ਸੰਭਾਲਣ ਵਾਲਾ ਸਬੂਤ | ਮਤਲਬ |
|---|---|---|
| **ਹੋਸਟ ਤਿਆਰ** | OS, kernel, ਪਾਵਰ ਅਤੇ ਇੰਟਰਫੇਸ ਸੂਚੀ | Linux ਤਿਆਰੀ ਪੂਰੀ |
| **Concentrator ਜਵਾਬ ਦਿੰਦਾ ਹੈ** | EUI ਅਤੇ ਸਫਲ initialization log | ਹੋਸਟ-concentrator ਸੰਚਾਰ ਚੱਲਦਾ ਹੈ |
| **ਰੇਡੀਓ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ** | ਉਮੀਦ ਵਾਲਾ ਸੈਂਸਰ ਪੈਕੇਟ ਅਤੇ reception metadata | ਸੰਰਚਿਤ receive ਰਸਤਾ ਕੰਮ ਕਰਦਾ ਹੈ |
| **ਸਰਵਰ ਸਵੀਕਾਰਦਾ ਹੈ** | ਸੈਂਸਰ ਨਾਲ ਜੁੜਿਆ ਗੇਟਵੇ event | ਫਾਰਵਰਡਿੰਗ ਅਤੇ ਸਰਵਰ ਰੂਟਿੰਗ ਚੱਲਦੀ ਹੈ |
| **ਐਪ ਵਿੱਚ decode** | ਉਮੀਦ ਵਾਲਾ ਮਾਪ ਅਤੇ timestamp | ਐਪ ਰਸਤਾ ਕੰਮ ਕਰਦਾ ਹੈ |
| **reboot ਮਗਰੋਂ ਵਾਪਸੀ** | restart ਮਗਰੋਂ ਉਹੀ ਜਾਂਚਾਂ | ਸ਼ੁਰੂਆਤੀ config ਦੁਹਰਾਈ ਜਾ ਸਕਦੀ ਹੈ |

**OTAA** ਸੈਂਸਰ ਲਈ activation ਲੈਣ-ਦੇਣ ਅਤੇ ਅਗਲਾ uplink ਵੀ ਪੱਕਾ ਕਰੋ। OTAA ਦਾ ਮਤਲਬ over-the-air activation ਹੈ, session ਬਣਾਉਣ ਦੀ join ਪ੍ਰਕਿਰਿਆ। Join request ਮਿਲਣਾ ਸਫਲ join ਜਾਂ downlink ਰਸਤਾ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ। [The Things Stack activation ਦਸਤਾਵੇਜ਼](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/)

**ਕੰਮ ਵਾਲਾ ਨਿਦਾਨ:** ਗੇਟਵੇ ਸਰਵਰ ਨਾਲ ਜੁੜਦਾ ਤੇ EUI ਦੱਸਦਾ ਹੈ ਪਰ ਸੈਂਸਰ ਨਹੀਂ ਦਿੱਸਦਾ। ਪਹਿਲਾਂ ਸੈਂਸਰ ਦੀ transmit config, ਚੁਣੇ receive channels, ਐਂਟੀਨਾ ਰਸਤਾ ਅਤੇ ਰੇਡੀਓ logs ਵੇਖੋ। ਇਸ ਹਾਲਤ ਵਿੱਚ ATECC608 ਮੁੜ ਪ੍ਰੋਗਰਾਮ ਕਰਨ ਨਾਲ ਗੁੰਮ ਸਬੂਤ ਨਹੀਂ ਮਿਲੇਗਾ।

**ਦੂਜਾ ਨਿਦਾਨ:** ਸੈਂਸਰ ਪੈਕੇਟ ਸਥਾਨਕ ਤੌਰ ਉੱਤੇ ਦਿੱਸਦਾ ਹੈ ਪਰ ਐਪ ਤੱਕ ਨਹੀਂ ਜਾਂਦਾ। ਪੈਕੇਟ ਦਾ ਸਮਾਂ ਗੇਟਵੇ ਅਤੇ ਸਰਵਰ ਘਟਨਾਵਾਂ ਨਾਲ ਮਿਲਾਓ, ਫਿਰ routing, device registration ਅਤੇ decoding ਜਾਂਚੋ। ਸਰਵਰ ਦੇ event ਸਵੀਕਾਰਨ ਤੋਂ ਪਹਿਲਾਂ log ਵਿੱਚ RF ਪੈਕੇਟ ਹੋਣਾ payload decoder ਨੂੰ ਦੋਸ਼ ਦੇਣ ਲਈ ਕਾਫ਼ੀ ਨਹੀਂ।

## ਲੱਛਣ ਅਨੁਸਾਰ ਸਮੱਸਿਆ ਹੱਲ

| ਲੱਛਣ | ਪਹਿਲਾਂ ਵੇਖੋ | ਅਗਲਾ ਕਦਮ |
|---|---|---|
| **SPI ਡਿਵਾਈਸ ਫਾਈਲ ਨਹੀਂ** | ਸਰਗਰਮ boot config ਅਤੇ ਇੰਟਰਫੇਸ ਸੈਟਿੰਗ | ਲੋੜੀਂਦਾ ਇੰਟਰਫੇਸ ਚਾਲੂ ਕਰਕੇ reboot |
| **SPI ਹੈ, ਰੇਡੀਓ ਫੇਲ੍ਹ** | ਪਾਵਰ, ਬੈਠਕ, reset ਕ੍ਰਮ ਅਤੇ chip select | ਸਰਵਰ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਬਿਜਲੀ ਰਸਤਾ ਜਾਂਚੋ |
| **GPIO export ਗਲਤੀ** | ਪੁਰਾਣੀਆਂ sysfs ਧਾਰਣਾਵਾਂ ਅਤੇ kernel | GPIO API ਲਈ ਜਾਂਚਿਆ ਤਰੀਕਾ ਵਰਤੋ |
| **GPIO ਵਰਤਿਆ ਜਾ ਰਿਹਾ** | `gpioinfo` ਵਿੱਚ consumer | ਮੁੜ ਕੋਸ਼ਿਸ਼ ਤੋਂ ਪਹਿਲਾਂ ਮਾਲਕੀ ਹੱਲ ਕਰੋ |
| **ਸੈਟਅੱਪ ਮਗਰੋਂ LED ਫੇਲ੍ਹ** | overlay ਲਾਗੂ ਹੋਣਾ ਅਤੇ GPIO22 ਟਕਰਾਅ | ਦਰਜ LED ਡਿਵਾਈਸ ਅਤੇ reset script ਵੇਖੋ |
| **I2C ਡਿਵਾਈਸ ਨਹੀਂ** | bus ਨੰਬਰ, ਪਾਵਰ ਅਤੇ ਮੌਜੂਦਾ ਵਰਤੋਂ | ਮੁੜ-ਮੁੜ ਵੱਡੇ scan ਬਿਨਾਂ ਜਾਂਚੋ |
| **ਕ੍ਰਿਪਟੋ ਲਾਇਬ੍ਰੇਰੀ import ਫੇਲ੍ਹ** | interpreter, bindings ਅਤੇ native library path | ਸੌਫਟਵੇਅਰ ਮਾਹੌਲ ਠੀਕ ਕਰੋ |
| **public key ਪੜ੍ਹਨਾ ਫੇਲ੍ਹ** | slot policy ਅਤੇ ਪਹਿਲਾਂ ਦੀਆਂ ਸਫਲ ਪੜ੍ਹਤਾਂ | provisioning ਤੋਂ ਬਿਨਾਂ config ਵੇਖੋ |
| **ਪੱਖਾ ਨਹੀਂ ਚਲਦਾ** | ਪੱਕੀ supply ਅਤੇ cooling ਤਰੀਕਾ | ਲੰਮੇ ਟੈਸਟ ਤੋਂ ਪਹਿਲਾਂ cooling ਵਾਪਸ ਕਰੋ |
| **uplink ਆਉਂਦੇ, join ਫੇਲ੍ਹ** | downlink ਰਸਤਾ ਅਤੇ ਖੇਤਰੀ/device setting | join ਜਵਾਬ ਤੇ receive windows ਪਿੱਛੇ ਲੱਗੋ |

ਹਰ ਸੋਧ ਨੂੰ ਇੱਕ ਪ੍ਰਯੋਗ ਮੰਨੋ। ਪਹਿਲੀ ਸੰਰਚਨਾ ਸੰਭਾਲੋ, ਇੱਕ ਵਾਰ ਇੱਕ ਬਦਲਾਅ ਕਰੋ, ਉਹੀ ਜਾਂਚ ਦੁਹਰਾਓ ਅਤੇ ਲਿਖੋ ਕਿ ਉਮੀਦ ਵਾਲਾ ਸਬੂਤ ਆਇਆ ਜਾਂ ਨਹੀਂ।

## ਆਪਣਾ ਹਾਰਡਵੇਅਰ ਰਿਕਾਰਡ ਬਣਾਓ

ਜਾਂਚ ਨੂੰ ਦੁਹਰਾਏ ਜਾ ਸਕਣ ਵਾਲੇ ਹਵਾਲੇ ਵਿੱਚ ਬਦਲਣ ਲਈ ਇਹ ਨਮੂਨਾ ਵਰਤੋ:

```text
ਕੈਰੀਅਰ ਰਿਵਿਜ਼ਨ ਅਤੇ ਤਸਵੀਰਾਂ:
Concentrator ਮਾਡਲ, ਇੰਟਰਫੇਸ ਅਤੇ RF ਬੈਂਡ:
ਹੋਸਟ ਮਾਡਲ / OS / kernel / GPIO ਟੂਲ ਵਰਜਨ:
ਪਾਵਰ / ਐਂਟੀਨਾ / cooling ਬਣਾਵਟ:
ਪੱਕਾ pin map ਅਤੇ ਸਬੂਤ:
ਅਣਸੁਲਝੇ ਨੈੱਟ ਅਤੇ ਛੱਡੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ:
ਸੌਫਟਵੇਅਰ ਰਿਪੋਜ਼ਟਰੀ ਅਤੇ commit:
Reset ਤਰੀਕਾ ਅਤੇ GPIO ਵਰਤੋਂਕਾਰ:
ਗੇਟਵੇ EUI / ਸਰਵਰ / frequency plan:
ਸੈਂਸਰ activation ਅਤੇ decode uplink ਸਬੂਤ:
Reboot ਮਗਰੋਂ ਵਾਪਸੀ ਦਾ ਨਤੀਜਾ:
ਅਸਲ ਕਾਰਡ ਦੀ ਥਾਂ ਅਤੇ rollback ਤਰੀਕਾ:
```

**ਫੈਸਲਾ ਅਭਿਆਸ:** ਤੁਹਾਡੇ ਕੋਲ ਬਿਨਾਂ ਮੋਡੀਊਲ ਲੇਬਲ ਵਾਲਾ ਸਸਤਾ ਖਾਲੀ ਕੈਰੀਅਰ ਅਤੇ ਪੜ੍ਹਨਯੋਗ ਲੇਬਲ ਤੇ ਦਰਜ ਕੰਮ ਵਾਲੀ ਮਹਿੰਗੀ ਅਸੈਂਬਲੀ ਹੈ। ਬਾਕੀ Pi, concentrator, ਐਂਟੀਨਾ, ਪਾਵਰ ਅਤੇ ਜਾਂਚ ਦੇ ਸਮੇਂ ਦੀ ਲਾਗਤ ਜੋੜ ਕੇ ਚੁਣੋ। ਵਧੀਆ ਚੋਣ ਕੁੱਲ ਲਾਗਤ ਅਤੇ ਤੁਹਾਡੀ ਸੇਵਾ ਲਈ ਲੋੜੀਂਦੇ ਸਬੂਤਾਂ ਉੱਤੇ ਹੈ, ਸਿਰਫ਼ ਕੈਰੀਅਰ ਦੀ ਕੀਮਤ ਉੱਤੇ ਨਹੀਂ।

**ਉਮੀਦ ਵਾਲੀ ਸੋਚ:** ਸਿੱਖਣ ਵਾਲਾ ਪ੍ਰੋਜੈਕਟ ਅਣਸੁਲਝੀ ਵਾਇਰਿੰਗ ਸਹਿ ਸਕਦਾ ਹੈ, ਜੇ ਮਾਪਣ ਦੇ ਸੰਦ ਅਤੇ ਸਮਾਂ ਹੋਵੇ। ਚੱਲਦੇ ਸੈਂਸਰਾਂ ਵਾਲੇ ਗੇਟਵੇ ਨੂੰ ਦੁਹਰਾਈ ਜਾ ਸਕਣ ਵਾਲੀ ਸ਼ੁਰੂਆਤ, cooling, ਸੌਫਟਵੇਅਰ ਸਹਾਇਤਾ ਅਤੇ ਸਾਬਤ ਡਿਲਿਵਰੀ ਚਾਹੀਦੀ ਹੈ। ਉਹ ਅਣਸੁਲਝੀ ਸ਼ਰਤ ਲਿਖੋ ਜੋ deployment ਰੋਕ ਦੇਵੇਗੀ।

## ਅਗਲੇ ਕਦਮ

ਪਹਿਲਾਂ ਹਾਰਡਵੇਅਰ ਰਿਕਾਰਡ ਪੂਰਾ ਕਰੋ ਅਤੇ reset script ਦੇ ਫਰਕ ਹੱਲ ਕਰੋ। ਫਿਰ ਇੱਕ ਜਾਣਿਆ ਸੈਂਸਰ ਚਲਾਓ ਅਤੇ ਹੋਰ ਜੋੜਨ ਤੋਂ ਪਹਿਲਾਂ ਐਪ ਵਿੱਚ decode ਤੱਕ ਸਬੂਤ ਸੰਭਾਲੋ।

**ਸਵੀਕ੍ਰਿਤੀ ਰਿਕਾਰਡ:** ਬੋਰਡ ਰਿਵਿਜ਼ਨ, ਮੋਡੀਊਲ ਲੇਬਲ, ਰੇਡੀਓ ਬੈਂਡ, ਪਾਵਰ ਮਾਪ, ਸਰਗਰਮ SPI ਡਿਵਾਈਸ, GPIO line ਨਾਮ, reset ਕ੍ਰਮ, concentrator log, ਸਰਵਰ ਕੁਨੈਕਸ਼ਨ ਅਤੇ ਇੱਕ decode uplink ਸੰਭਾਲੋ। ਹਰ ਮੁੱਲ ਨੂੰ ਦੇਖਿਆ, ਦਸਤਾਵੇਜ਼ੀ ਜਾਂ ਹਾਲੇ ਅਨੁਮਾਨ ਵਜੋਂ ਨਿਸ਼ਾਨ ਲਗਾਓ। ਕਿਸੇ process ਦੇ ਸ਼ੁਰੂ ਹੋਣ ਨੂੰ RF ਕਾਰਗੁਜ਼ਾਰੀ ਜਾਂ ਐਪ ਡਿਲਿਵਰੀ ਦਾ ਸਬੂਤ ਨਾ ਮੰਨੋ।

ਜੇ ਮਕਸਦ mesh messaging ਹੈ, ਪਹਿਲਾਂ ਸਾਡੀ [Meshtastic, MeshCore ਅਤੇ Reticulum ਤੁਲਨਾ ਗਾਈਡ](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/) ਵਿੱਚ ਪ੍ਰੋਟੋਕੋਲ ਦੀਆਂ ਭੂਮਿਕਾਵਾਂ ਵੇਖੋ। LoRa ਰੇਡੀਓ ਸਾਂਝਾ ਹੋਣ ਨਾਲ firmware ਅਨੁਕੂਲਤਾ ਸਾਬਤ ਨਹੀਂ ਹੁੰਦੀ। ਸੁਨੇਹਾ ਪ੍ਰਣਾਲੀ ਲਈ [MeshtasticD ਸਮਰਥਿਤ ਹਾਰਡਵੇਅਰ ਦਸਤਾਵੇਜ਼](https://meshtastic.org/docs/meshtasticd/) ਵੇਖੋ; ਇਸ LoRaWAN ਤਰੀਕੇ ਨੂੰ Meshtastic ਵਿੱਚ ਬਦਲਾਅ ਨਾ ਸਮਝੋ।

## ਸਰੋਤ ਅਤੇ ਤਸਵੀਰਾਂ ਦਾ ਸਿਹਰਾ

ਖੋਜ ਜਾਂਚ: 12 ਸਤੰਬਰ 2026। ਬਿਨਾਂ ਤਾਰੀਖ ਦੇ ਦਸਤਾਵੇਜ਼ ਅਤੇ ਰਿਪੋਜ਼ਟਰੀ ਲਿੰਕ ਇਸ ਲੇਖ ਲਈ ਜਾਂਚੇ ਵਰਜਨਾਂ ਨੂੰ ਦੱਸਦੇ ਹਨ। ਸਥਾਨਕ ਤਸਵੀਰਾਂ ਅਸਲ ਲੇਬਲ ਅਤੇ ਸਰੋਤ ਸਿਹਰਾ ਰੱਖਦੀਆਂ ਹਨ।

| ਪ੍ਰਕਾਸ਼ਕ | ਸਰੋਤ ਅਤੇ ਤਾਰੀਖ |
|---|---|
| **Clockwork Bird** | [SenseCAP M1 Raspberry Pi Shield](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), 2023-05-03। ਬੋਰਡ ਤਸਵੀਰ, ਨਿਸ਼ਾਨ ਲਾਇਆ ਹੈਡਰ ਅਤੇ ਮੁੜ ਛਪਿਆ ਨਿਰਮਾਤਾ ਬਲਾਕ ਡਾਇਗ੍ਰਾਮ |
| **Seeed Studio / SenseCAP** | [M1 ਜਾਣਕਾਰੀ ਅਤੇ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ](https://www.sensecapmx.com/docs/sensecap-m1/overview/), ਤਾਰੀਖ ਨਹੀਂ। ਅਸਲ ਬਲਾਕ ਡਾਇਗ੍ਰਾਮ ਦਾ ਸਿਹਰਾ |
| **Seeed Studio** | [WM1302 ਦਸਤਾਵੇਜ਼ ਅਤੇ ਮੋਡੀਊਲ ਪਿਨਆਉਟ](https://github.com/seeed-lora/WM1302-doc), ਰਿਪੋਜ਼ਟਰੀ |
| **Semtech** | [SX1302/SX1303 HAL](https://github.com/Lora-net/sx1302_hal), ਲਿੰਕ ਕੀਤੇ reset script ਅਤੇ ਤਾਪਮਾਨ ਡਰਾਈਵਰ ਸਰੋਤ ਸਮੇਤ |
| **Raspberry Pi** | [Boot config](https://www.raspberrypi.com/documentation/computers/config_txt.html), [GPIO ਵਰਤੋਂ ਗਾਈਡ](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices), ਅਤੇ [overlay ਹਵਾਲਾ](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README) |
| **Linux / libgpiod** | [ਪੁਰਾਣਾ GPIO sysfs ਇੰਟਰਫੇਸ](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html) ਅਤੇ [gpioset ਮੈਨੂਅਲ](https://libgpiod.readthedocs.io/en/master/gpioset.html), ਦੂਜਾ ਅਗਸਤ 2026 ਦਾ |
| **i2c-tools** | [i2cdetect ਮੈਨੂਅਲ](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), v4.3 ਸਰੋਤ |
| **STMicroelectronics** | [STTS751 ਡਾਟਾਸ਼ੀਟ](https://www.st.com/resource/en/datasheet/stts751.pdf), ਰਿਵਿਜ਼ਨ 7 |
| **Microchip** | [CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools), ਅਤੇ [slot ਪਹੁੰਚ ਨੀਤੀ ਦਸਤਾਵੇਜ਼](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html) |
| **ChirpStack** | [Concentratord ਹਾਰਡਵੇਅਰ ਸਹਾਇਤਾ](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html) ਅਤੇ [Seeed ਇੰਸਟਾਲ ਟੀਚਾ](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html) |
| **The Things Industries** | [UDP forwarder](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/) ਅਤੇ [ਡਿਵਾਈਸ activation](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/) |
| **Meshtastic** | [MeshtasticD ਦਸਤਾਵੇਜ਼](https://meshtastic.org/docs/meshtasticd/), ਤਾਰੀਖ ਨਹੀਂ |

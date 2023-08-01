---
title: "Сегодня я узнал о создании пользовательских образов Windows"
date: 2023-01-30
toc: true
draft: false
description: "Сегодня я узнал о создании пользовательских образов Windows, Sysprep и обобщении"
genre: ["Управление образами Windows", "Персонализация", "Развертывание Windows", "Sysprep", "Обобщение", "Windows 10", "Windows 11", "Захват изображения", "Развертывание изображений", "NTLite", "Оптимизация Windows"]
tags: ["Sysprep", "NTLite", "Обобщение", "Пользовательские изображения", "Пользовательские изображения окон", "Windows 11", "Debloat", "Персонализация", "захват изображения", "развертывание изображения", "Управление образами Windows", "Средства развертывания Windows", "Настройка образа Windows", "Оптимизация изображений под Windows", "Microsoft Learn", "Репозиторий WinCustom"]
---

**Что интересного узнал и нашел сегодня SimeonOnSecurity**.

Сегодня SimeonOnSecurity узнал о процессе создания и применения образов Windows 10 с помощью DISM, инструмента командной строки, используемого для управления образами Windows. Для захвата образа можно использовать инструмент Sysprep для обобщенной установки, который удаляет информацию, специфичную для оборудования, и подготавливает образ для развертывания на нескольких устройствах.

SimeonOnSecurity познакомился с различными ресурсами, предоставляющими информацию о создании и применении образов Windows, включая сайт Microsoft Learn и репозиторий WinCustom на GitHub. В ресурсах Microsoft рассматриваются основы создания и применения образа Windows с помощью одного файла .WIM, создания загрузочного носителя Windows PE и обобщенной установки Windows с помощью Sysprep.

Кроме того, SimeonOnSecurity узнал о NTLite, программе, позволяющей настраивать и оптимизировать образы Windows. С помощью NTLite можно удалять ненужные компоненты из образа Windows, что позволяет экономить дисковое пространство и повышать производительность.

В целом, сегодняшнее исследование SimeonOnSecurity позволило получить полное представление о процессе создания и применения образов Windows.

## Repos Created/Updated:
- Нет / N/A

## Учебные ресурсы:
- [Learn How to Sysprep Capture Windows 10 Image using DISM](https://www.anoopcnair.com/sysprep-capture-windows-10-image-using-dism/)
- [Microsoft - Capture and apply a Windows image using a single .WIM file](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/capture-and-apply-windows-using-a-single-wim?view=windows-11)
- [Microsoft - Create bootable Windows PE media](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-create-usb-bootable-drive?view=windows-11)
- [Microsoft - Sysprep (Generalize) a Windows installation](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation?view=windows-11)
- [WinTenDev/WinCustom](https://github.com/WinTenDev/WinCustom)

## Обсуждаемое и/или используемое программное обеспечение:
- [NTLite](https://www.ntlite.com/)
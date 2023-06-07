---
title: "Vandaag heb ik geleerd over het maken van aangepaste Windows-afbeeldingen"
date: 2023-01-30
toc: true
draft: false
description: "Vandaag heb ik geleerd over het maken van aangepaste Windows-afbeeldingen, Sysprep en generaliseren"
genre: ["Windows Beeldbeheer", "Aanpassing", "Windows installatie", "Sysprep", "Generalisatie", "Windows 10", "Windows 11", "Afbeelding vastleggen", "Beeldimplementatie", "NTLite", "Windows Optimalisatie"]
tags: ["Sysprep", "NTLite", "Generalisatie", "Aangepaste afbeeldingen", "Aangepaste Windows-afbeeldingen", "Windows 11", "Debloat", "Aanpassing", "beeldopname", "inzet van afbeeldingen", "Beheer van Windows-afbeeldingen", "Windows hulpprogramma's voor implementatie", "Windows-afbeelding aanpassen", "Windows beeldoptimalisatie", "Microsoft leren", "WinCustom opslagplaats"]
---

**Wat SimeonOnSecurity vandaag heeft geleerd en interessant vond**

Vandaag heeft SimeonOnSecurity geleerd over het proces van het vastleggen en toepassen van Windows 10-images met DISM, een opdrachtregeltool die wordt gebruikt om Windows-images te beheren. Om een image vast te leggen, kan men de Sysprep-tool gebruiken om de installatie te veralgemenen, waardoor hardwarespecifieke informatie wordt verwijderd en de image wordt voorbereid voor inzet op meerdere apparaten.

SimeonOnSecurity maakte kennis met verschillende bronnen die informatie verschaffen over het vastleggen en toepassen van Windows-images, waaronder de Learn-website van Microsoft en de WinCustom-repository op GitHub. De Microsoft bronnen behandelen de basis van het vastleggen en toepassen van een Windows image met behulp van een enkel .WIM bestand, het maken van opstartbare Windows PE media, en het veralgemenen van een Windows installatie met Sysprep.

Daarnaast leerde SimeonOnSecurity over NTLite, een software waarmee Windows-images kunnen worden aangepast en geoptimaliseerd. NTLite kan worden gebruikt om onnodige componenten uit een Windows-image te verwijderen, waardoor schijfruimte wordt bespaard en de prestaties worden verbeterd.

Over het geheel genomen heeft het onderzoek van SimeonOnSecurity vandaag een uitgebreid begrip opgeleverd van het proces van het vastleggen en toepassen van Windows-images.

## Repos Gemaakt/Gewijzigd:
- Geen / N/A

## Leerbronnen:
- [Learn How to Sysprep Capture Windows 10 Image using DISM](https://www.anoopcnair.com/sysprep-capture-windows-10-image-using-dism/)
- [Microsoft - Capture and apply a Windows image using a single .WIM file](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/capture-and-apply-windows-using-a-single-wim?view=windows-11)
- [Microsoft - Create bootable Windows PE media](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-create-usb-bootable-drive?view=windows-11)
- [Microsoft - Sysprep (Generalize) a Windows installation](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation?view=windows-11)
- [WinTenDev/WinCustom](https://github.com/WinTenDev/WinCustom)

## Besproken en/of gebruikte software:
- [NTLite](https://www.ntlite.com/)
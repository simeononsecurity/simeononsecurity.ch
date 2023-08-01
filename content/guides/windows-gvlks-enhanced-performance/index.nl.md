---
title: "Windows GVLK's: De kracht van licentiesleutels ontsluiten voor betere prestaties"
date: 2023-09-09
toc: true
draft: false
description: "Ontdek hoe Windows GVLK's de prestaties revolutioneren! Ontdek de beste licentiesleutels en verhoog de productiviteit van je systeem moeiteloos."
genre: ["Technologie", "Software", "Productiviteit", "Besturingssystemen", "Microsoft", "Windows", "Licentie", "Sleutelbeheer", "IT-oplossingen", "Verbetering"]
tags: ["Windows GVLK's", "Licentiesleutels", "Productiviteit", "Systeemprestaties", "Sleutelbeheer", "Besturingssystemen", "Windows server", "Windows 10", "IT-oplossingen", "Software", "Kanaal voor langetermijnonderhoud", "LTSC", "Langetermijndienstverleningstak", "LTSB", "Verbeterde prestaties", "Microsoft", "IT-beheer", "Activeringssleutels", "KMS Klant", "GVLK Lijst", "Windows-edities", "Licentie Activering", "Productcode klant", "Server 2019", "Server 2016", "Windows 11 Pro", "Windows 10 Onderneming", "Windows LTSB 2016", "IT-beheerders"]
cover: "/img/cover/windows_gvlks_unlocked.png"
coverAlt: "Een kleurrijke cartoonillustratie van een sleutel die een deur ontgrendelt en de kracht van GVLK's voorstelt om het volledige potentieel van Windows te ontgrendelen."
coverCaption: "Ontketen het potentieel van Windows met GVLK's!"
---

## Hoe installeer ik een productsleutel (GVLK) voor Windows en Windows Server?

Als u een computer converteert van een KMS-host, MAK of retaileditie van Windows naar een KMS-client, moet u de toepasselijke productsleutel installeren, ook bekend als GVLK (Generic Volume License Key). GVLK's worden gebruikt voor volumeactivering met Key Management Services (KMS). Hier volgt een stapsgewijze handleiding voor het installeren van een GVLK op je Windows- of Windows Server-systeem.

## Geautomatiseerd GLVK installatiescript

Het script moet worden gestart vanuit een administratieve powershell in de map met alle bestanden uit de [GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```

## Handmatige installatie Activeringsstappen

### Vereisten

Voordat u verdergaat, moet u ervoor zorgen dat u een geldige en legale productsleutel hebt voor uw Windows-versie en -editie. Het gebruik van niet-geautoriseerde of illegaal gekopieerde productsleutels is in strijd met de servicevoorwaarden van Microsoft en kan juridische gevolgen hebben.

### Installatiestappen

1. **Open een Administratieve Opdrachtprompt:** Klik met de rechtermuisknop op de knop "Start" en selecteer "Windows Terminal (Admin)" of "Opdrachtprompt (Admin)". Als u Windows 11 of Windows 10 gebruikt, kunt u zoeken naar "Opdrachtprompt", er met de rechtermuisknop op klikken en "Als administrator uitvoeren" kiezen.

2. **Zoek de juiste productsleutel (GVLK):** Zoek de GVLK voor uw Windows- of Windows Server-versie en -editie in de volgende lijst:

   - Windows Server 2022:*
     - Windows Server 2022 Datacenter: WX4NM-KYWYW-QJJR4-XV3QB-6VM33
     - Windows Server 2022 Datacenter Azure Edition: NTBV8-9K7Q8-V27C6-M2BTV-KHMXV
     - Windows Server 2022 Standaard: VDYBN-27WPP-V4HQT-9VMD4-VMK7H

   - Windows Server 2019:*
     - Windows Server 2019 Datacenter: WMDGN-G9PQG-XVVXX-R3X43-63DFG
     - Windows Server 2019 Standard: N69G4-B89J2-4G8F4-WWYCC-J464C
     - Windows Server 2019 Essentials: WVDHN-86M7X-466P6-VHXV7-YY726

   - Windows Server 2016:*
     - Windows Server 2016 Datacenter: CB7KF-BWN84-R7R2Y-793K2-8XDDG
     - Windows Server 2016 Standard: WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY
     - Windows Server 2016 Essentials: JCKRF-N37P4-C2D82-9YXRT-4M63B

   - [Click Here to See the Others](#complete-list-of-generic-volume-license-keys-gvlk)

3. **Installeer de productsleutel (GVLK):** Typ op de beheerdersopdrachtprompt de volgende opdracht, met als vervanging `<product key>` met de juiste GVLK:
```sh
slmgr /ipk <product key>
```

Om bijvoorbeeld de GVLK voor Windows Server 2022 Datacenter edition te installeren, zou het commando zijn:

```sh
slmgr /ipk WX4NM-KYWYW-QJJR4-XV3QB-6VM33
```

4. **Druk op Enter:** Druk na het invoeren van de opdracht op Enter. Het systeem probeert de opgegeven productsleutel te installeren.

5. **Bevestigingsbericht:** Als de installatie geslaagd is, zou je een bevestigingsbericht moeten zien dat aangeeft dat de productsleutel geïnstalleerd is.

Als u geen bevestigingsbericht ziet of als u Windows wilt dwingen om te proberen het volgende te activeren met behulp van de sleutel, probeer dan de volgende opdrachten:

```sh
slmgr /ato
slmgr /dlv
```

## Belangrijke opmerkingen

- Zorg er altijd voor dat je een geldige en legale productsleutel gebruikt voor jouw Windows versie en editie.
- Het "slmgr" commando gaat over licenties en activering, dus gebruik het met voorzichtigheid.
- Raadpleeg voor Windows 11 en Windows 10 de originele tabellen voor de volledige lijst met GVLK's voor verschillende edities.

Vergeet niet de licentierichtlijnen en servicevoorwaarden van Microsoft te volgen om compliant en legaal te blijven.

*Disclaimer: Dit artikel is alleen voor informatieve doeleinden. Het gebruik van productsleutels moet voldoen aan de licentievoorwaarden van Microsoft en misbruik is de verantwoordelijkheid van de gebruiker.


## Volledige lijst van generieke volumelicentiecodes (GVLK)

In de volgende tabellen vindt u de generieke volumelicentiecodes (GVLK's) voor elke versie en editie van Windows. *LTSC* staat voor Long-Term Servicing Channel en *LTSB* staat voor Long-Term Servicing Branch. Raadpleeg de volgende tabellen voor de GVLK's:

### Windows Server (LTSC-versies)

#### Windows Server 2022

| Versie besturingssysteem | KMS Client-productsleutel |
|--------------------------------|-------------------------------|
| Windows Server 2022 Datacenter | WX4NM-KYWYW-QJJR4-XV3QB-6VM33 |
| Windows Server 2022 Datacenter<br/>Azure Editie | NTBV8-9K7Q8-V27C6-M2BTV-KHMXV |
| Windows Server 2022 Standard<br/> VDYBN-27WPP-V4HQT-9VMD4-VMK7H |

#### Windows Server 2019

| Besturingssysteemeditie | KMS Client Product Key |
|--------------------------------|-------------------------------|
| Windows Server 2019 Datacenter | WMDGN-G9PQG-XVVXX-R3X43-63DFG |
| Windows Server 2019 Standard | N69G4-B89J2-4G8F4-WWYCC-J464C |
| Windows Server 2019 Essentials | WVDHN-86M7X-466P6-VHXV7-YY726 |

#### Windows Server 2016

| Versie besturingssysteem | KMS Client Product Key |
|--------------------------------|-------------------------------|
| Windows Server 2016 Datacenter | CB7KF-BWN84-R7R2Y-793K2-8XDDG |
| Windows Server 2016 Standard | WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY |
| Windows Server 2016 Essentials | JCKRF-N37P4-C2D82-9YXRT-4M63B |

### Windows Server (halfjaarlijkse kanaalversies)

#### Windows Server, versies 20H2, 2004, 1909, 1903 en 1809

| Versie besturingssysteem | KMS Client-productsleutel |
|---------------------------|-------------------------------|
| Windows Server Datacenter | 6NMRW-2C8FM-D24W7-TQWMY-CWH2D |
| Windows Server Standard | N2KJX-J94YW-TQVFB-DG9YT-724CC |

### Windows 11 en Windows 10 (halfjaarlijkse kanaalversies)

| Versie besturingssysteem | KMS Client-productsleutel |
|-----------------------------------|-------------------------------|
| Windows 11 Pro<br/>Windows 10 Pro | W269N-WFGWX-YVC9B-4J6C9-T83GX |
| Windows 11 Pro N<br/>Windows 10 Pro N | MH37W-N47XK-V7XM9-C7227-GCQG9 |
| Windows 11 Pro voor werkstations<br/>Windows 10 Pro voor werkstations | NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J |
| Windows 11 Pro voor werkstations N<br/>Windows 10 Pro voor werkstations N | 9FNHH-K3HBT-3W4TD-6383H-6XYWF |
| Windows 11 Pro Education<br/>Windows 10 Pro Education | 6TP4R-GNPTD-KYYHQ-7B7DP-J447Y |
| Windows 11 Pro Education N<br/>Windows 10 Pro Education N | YVWGF-BXNMC-HTQYQ-CPQ99-66QFC |
| Windows 11 Education<br/>Windows 10 Education | NW6C2-QMPVW-D7KK-3GKT6-VCFB2 |
| Windows 11 Education N<br/>Windows 10 Education N | 2WH4N-8QGBV-H22JP-CT43Q-MDWJ |
| Windows 11 Enterprise<br/>Windows 10 Enterprise | NPPR9-FWDCX-D2C8J-H872K-2YT43 |
| Windows 11 Enterprise N<br/>Windows 10 Enterprise N | DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4 |
| Windows 11 Enterprise G<br/>Windows 10 Enterprise G | YYVX9-NTFWV-6MDM3-9PT4T-4M68B |
| Windows 11 Enterprise G N<br/>Windows 10 Enterprise G N | 44RPN-FTY23-9VTTB-MP9BX-T84FV |

### Windows 10 (LTSC/LTSB-versies)

#### Windows 10 LTSC 2021 en 2019

| Versie besturingssysteem | KMS Client-productsleutel |
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise LTSC 2021<br/>Windows 10 Enterprise LTSC 2019 | M7XTQ-FN8P6-TTKYV-9D4CC-J462D |
| Windows 10 Enterprise N LTSC 2021<br/>Windows 10 Enterprise N LTSC 2019 | 92NFX-8DJQP-P6BBQ-THF9C-7CG2H |

#### Windows 10 LTSB 2016

| Besturingssysteemeditie | KMS Client-productsleutel |
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise LTSB 2016 | DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ |
| Windows 10 Enterprise N LTSB 2016 | QFFDN-GRT3P-VKWWX-X7T3R-8B639 |

#### Windows 10 LTSB 2015

| Besturingssysteemeditie | KMS Client-productsleutel |
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise 2015 LTSB | WNMTR-4C88C-JK8YV-HQ7T2-76DF9 |
| Windows 10 Enterprise 2015 LTSB N | 2F77B-TNFGY-69QQF-B8YKP-D69TJ |

### Eerdere versies van Windows Server

#### Windows Server, versie 1803

| Versie besturingssysteem | KMS Client-productsleutel |
|---------------------------|-------------------------------|
| Windows Server Datacenter | 2HXDN-KRXHB-GPYC7-YCKFJ-7FVDG |
| Windows Server Standard | PTXN8-JFHJM-4WC78-MPCBR-9W4KR |

#### Windows Server, versie 1709

| Versie besturingssysteem | KMS Client-productsleutel |
|---------------------------|-------------------------------|
| Windows Server Datacenter | 6Y6KB-N82V8-D8CQV-23MJW-BWTG6 |
| Windows Server Standard | DPCNP-XQFKJ-BJF7R-FRC8D-GF6G4 |

#### Windows Server 2012 R2

| Uitgever van besturingssysteem | KMS Client Product Key |
|----------------------------------------|-------------------------------|
| Windows Server 2012 R2 Standard | D2N9P-3P6X9-2R39C-7RTCD-MDVJX |
| Windows Server 2012 R2 Datacenter | W3GGN-FT8W3-Y4M27-J84CP-Q3VJ9 |
| Windows Server 2012 R2 Essentials | KNC87-3J2TX-XB4WP-VCPJV-M4FWM |

#### Windows Server 2012

| Versie besturingssysteem | KMS Client Product Key |
|-----------------------------------------|-------------------------------|
| Windows Server 2012 | BN3D2-R7TKB-3YPBD-8DRP2-27GG4 |
| Windows Server 2012 N | 8N2M2-HWPGY-7PGT9-HGDD8-GVGGY |
| Windows Server 2012 Enkelvoudige Taal | 2WN2H-YGCQR-KFX6K-CD6TF-84YXQ |
| Windows Server 2012 Landgebonden | 4K36P-JN4VD-GDC6V-KDT89-DYFKP |
| Windows Server 2012 Standaard | XC9B7-NBPP2-83J2H-RHMBY-92BT4 |
| Windows Server 2012 MultiPoint Standard | HM7DN-YVMH3-46JC3-XYTG7-CYQJ |
| Windows Server 2012 MultiPoint Premium | XNH6W-2V9GX-RGJ4K-Y8X6F-QGJ2G |
| Windows Server 2012 Datacenter | 48HP8-DN98B-MYWDG-T2DCC-8W83P |

#### Windows Server 2008 R2

| Uitgever van het besturingssysteem | KMS Client Product Key |
|--------------------------------------------------|-------------------------------|
| Windows Server 2008 R2 Web-editie | 6TPJF-RBVHG-WBW2R-86QPH-6RTM4 |
| Windows Server 2008 R2 HPC editie | TT8MH-CG224-D3D7Q-498W2-9QCTX |
| Windows Server 2008 R2 Standard | YC6KT-GKW9T-YTKYR-T4X34-R7VHC |
| Windows Server 2008 R2 Enterprise | 489J6-VHDMP-X63PK-3K798-CPX3Y |
| Windows Server 2008 R2 Datacenter | 74YFP-3QFB3-KQT8W-PMXWJ-7M648 |
| Windows Server 2008 R2 voor Itanium-gebaseerde systemen | GT63C-RJFQ3-4GMB6-BRFB9-CB83V |

#### Windows Server 2008

| Versie besturingssysteem | KMS Client Product Key |
|------------------------------------------------|-------------------------------|
| Windows Web Server 2008 | WYR28-R7TFJ-3X2YQ-YCY4H-M249D |
| Windows Server 2008 Standard | TM24T-X9RMF-VWXK6-X8JC9-BFGM2 |
| Windows Server 2008 Standard zonder Hyper-V | W7VD6-7JFBR-RX26B-YKQ3Y-6FFFJ |
| Windows Server 2008 Enterprise | YQGMW-MPWTJ-34KDK-48M3W-X4Q6V |
| Windows Server 2008 Enterprise zonder Hyper-V | 39BXF-X8Q23-P2WWT-38T2F-G3FPG |
| Windows Server 2008 HPC | RCTX3-KWVHP-BR6TB-RB6DM-6X7HP |
| Windows Server 2008 Datacenter | 7M67G-PC374-GR742-YH8V4-TCBY3 |
| Windows Server 2008 Datacenter zonder Hyper-V | 22XQ2-VRXRG-P8D42-K34TD-G3QQC |
| Windows Server 2008 voor Itaniumgebaseerde systemen | 4DWFP-JF3DJ-B7DTH-78FJB-PDRHK |

### Eerdere versies van Windows

#### Windows 8.1

| Versie besturingssysteem | KMS Client-productsleutel |
|--------------------------|-------------------------------|
| Windows 8.1 Pro | GCRJD-8NW9H-F2CDX-CCM8D-9D6T9 |
| Windows 8.1 Pro N | HMCNV-VVBFX-7HMBH-CTY9B-B4FXY |
| Windows 8.1 Enterprise | MHF9N-XY6XB-WVXMC-BTDCT-MKKG7 |
| Windows 8.1 Enterprise N | TT4HM-HN7YT-62K67-RGRQJ-JFFXW |

#### Windows 8

| Versie besturingssysteem | KMS Client Product Code |
|--------------------------|-------------------------------|
| Windows 8 Pro | NG4HW-VH26C-733KW-K6F98-J8CK4 |
| Windows 8 Pro N | XCVCF-2NXM9-723PB-MHCB7-2RYQQ |
| Windows 8 Enterprise | 32JNW-9KQ84-P47T8-D8GGY-CWCK7 |
| Windows 8 Enterprise N | JMNMF-RHW7P-DMY6X-RF3DR-X2BQT |

#### Windows 7

| Versie besturingssysteem | KMS Client-productsleutel |
|--------------------------|-------------------------------|
| Windows 7 Professional | FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4 |
| Windows 7 Professional N | MRPKT-YTG23-K7D7T-X2JMM-QY7MG |
| Windows 7 Professional E | W82YF-2Q76Y-63HXB-FGJG9-GF7QX |
| Windows 7 Enterprise | 33PXH-7Y6KF-2VJC9-XBBR8-HVTHH |
| Windows 7 Enterprise N | YDRBP-3D83W-TY26F-D46B2-XCKRJ |
| Windows 7 Enterprise E | C29WB-22CC8-VJ326-GHFJW-H9DH4 |

#### Windows Vista

| Besturingssysteemeditie | KMS Client Product Sleutel |
|--------------------------|-------------------------------|
|Windows Vista Business | YFKBB-PQJJV-G996G-VWGXY-2V3X8 |
|Windows Vista Business N | HMBQG-8H2RH-C77VX-27R82-VMQBT |
|Windows Vista Enterprise | VKK3X-68KWM-X2YGT-QR4M6-4BWMV |
|Windows Vista Enterprise N | VTC42-BM838-43QHV-84HX6-XJXKV |

## Referenties
- [Key Management Services (KMS) client activation and product keys](https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys)
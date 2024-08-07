---
title: "Windows GVLKs: Odblokowywanie mocy kluczy licencyjnych w celu zwiększenia wydajności"
date: 2023-09-09
toc: true
draft: false
description: "Odkryj, jak klucze Windows GVLK rewolucjonizują wydajność! Poznaj najlepsze klucze licencyjne i bez wysiłku zwiększ wydajność swojego systemu."
genre: ["Technologia", "Oprogramowanie", "Wydajność", "Systemy operacyjne", "Microsoft", "Windows", "Licencjonowanie", "Zarządzanie kluczami", "Rozwiązania IT", "Ulepszenie"]
tags: ["Windows GVLKs", "Klucze licencyjne", "Wydajność", "Wydajność systemu", "Zarządzanie kluczami", "Systemy operacyjne", "Windows Server", "Windows 10", "Rozwiązania IT", "Oprogramowanie", "Kanał obsługi długoterminowej", "LTSC", "Oddział obsługi długoterminowej", "LTSB", "Zwiększona wydajność", "Microsoft", "Zarządzanie IT", "Klucze aktywacyjne", "Klient KMS", "Lista GVLK", "Edycje Windows", "Aktywacja licencji", "Klucz produktu klienta", "Serwer 2019", "Server 2016", "Windows 11 Pro", "Windows 10 Enterprise", "Windows LTSB 2016", "Administratorzy IT"]
cover: "/img/cover/windows_gvlks_unlocked.png"
coverAlt: "Kolorowa kreskówkowa ilustracja klucza otwierającego drzwi reprezentuje moc GVLK w odblokowywaniu pełnego potencjału systemu Windows."
coverCaption: "Uwolnij potencjał systemu Windows dzięki GVLK!"
---

## Jak zainstalować klucz produktu (GVLK) dla systemów Windows i Windows Server

Jeśli konwertujesz komputer z hosta KMS, MAK lub edycji detalicznej systemu Windows na klienta KMS, musisz zainstalować odpowiedni klucz produktu, znany również jako GVLK (Generic Volume License Key). Klucze GVLK są używane do aktywacji wolumenu za pomocą usług zarządzania kluczami (KMS). Oto przewodnik krok po kroku, jak zainstalować GVLK w systemie Windows lub Windows Server.

## Zautomatyzowany skrypt instalacyjny GLVK

Skrypt musi zostać uruchomiony z poziomu administracyjnego powershell w katalogu zawierającym wszystkie pliki z pliku [GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```

## Kroki aktywacji instalacji ręcznej

### Wymagania wstępne

Przed kontynuowaniem upewnij się, że posiadasz ważny i legalny klucz produktu dla swojej wersji i edycji systemu Windows. Używanie nieautoryzowanych lub pirackich kluczy produktu jest niezgodne z warunkami korzystania z usług firmy Microsoft i może prowadzić do konsekwencji prawnych.

### Kroki instalacji

1. **Otwórz administracyjny wiersz polecenia:** Kliknij prawym przyciskiem myszy przycisk "Start" i wybierz "Windows Terminal (Admin)" lub "Wiersz polecenia (Admin)". Jeśli korzystasz z systemu Windows 11 lub Windows 10, możesz wyszukać "Wiersz polecenia", kliknąć go prawym przyciskiem myszy i wybrać "Uruchom jako administrator".

2. **Zlokalizuj odpowiedni klucz produktu (GVLK):** Znajdź GVLK dla wersji i edycji systemu Windows lub Windows Server z poniższej listy:

   - *Windows Server 2022:*
     - Windows Server 2022 Datacenter: WX4NM-KYWYW-QJJR4-XV3QB-6VM33
     - Windows Server 2022 Datacenter Azure Edition: NTBV8-9K7Q8-V27C6-M2BTV-KHMXV
     - Windows Server 2022 Standard: VDYBN-27WPP-V4HQT-9VMD4-VMK7H

   - Windows Server 2019:*
     - Windows Server 2019 Datacenter: WMDGN-G9PQG-XVVXX-R3X43-63DFG
     - Windows Server 2019 Standard: N69G4-B89J2-4G8F4-WWYCC-J464C
     - Windows Server 2019 Essentials: WVDHN-86M7X-466P6-VHXV7-YY726

   - Windows Server 2016:*
     - Windows Server 2016 Datacenter: CB7KF-BWN84-R7R2Y-793K2-8XDDG
     - Windows Server 2016 Standard: WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY
     - Windows Server 2016 Essentials: JCKRF-N37P4-C2D82-9YXRT-4M63B

   - [Click Here to See the Others](#complete-list-of-generic-volume-license-keys-gvlk)

3. **Zainstaluj klucz produktu (GVLK):** W administracyjnym wierszu polecenia wpisz następujące polecenie, zamieniając je na `<product key>` z odpowiednim GVLK:
```sh
slmgr /ipk <product key>
```

Na przykład, aby zainstalować GVLK dla Windows Server 2022 Datacenter Edition, polecenie będzie następujące:

```sh
slmgr /ipk WX4NM-KYWYW-QJJR4-XV3QB-6VM33
```

4. **Naciśnij Enter:** Po wprowadzeniu polecenia naciśnij Enter. System podejmie próbę zainstalowania określonego klucza produktu.

5. **Komunikat potwierdzający:** Jeśli instalacja przebiegnie pomyślnie, powinien zostać wyświetlony komunikat potwierdzający, że klucz produktu został zainstalowany.

Jeśli nie zobaczysz komunikatu potwierdzającego lub chcesz zmusić system Windows do próby aktywacji przy użyciu klucza, wypróbuj następujące polecenia:

```sh
slmgr /ato
slmgr /dlv
```

## Ważne uwagi

- Zawsze upewnij się, że używasz ważnego i legalnego klucza produktu dla swojej wersji i edycji systemu Windows.
- Polecenie "slmgr" dotyczy licencjonowania i aktywacji, więc należy go używać ostrożnie.
- W przypadku systemów Windows 11 i Windows 10 pełna lista kluczy GVLK dla różnych edycji znajduje się w oryginalnych tabelach.

Pamiętaj, aby postępować zgodnie z wytycznymi licencyjnymi i warunkami świadczenia usług firmy Microsoft, aby zachować zgodność z przepisami i prawem.

*Zastrzeżenie: Ten artykuł służy wyłącznie celom informacyjnym. Korzystanie z kluczy produktów powinno być zgodne z warunkami licencyjnymi firmy Microsoft, a za wszelkie niewłaściwe użycie odpowiada użytkownik.


## Pełna lista generycznych kluczy licencyjnych (GVLK)

W poniższych tabelach znajdują się ogólne klucze licencyjne (GVLK) dla każdej wersji i edycji systemu Windows. *LTSC* oznacza Long-Term Servicing Channel, a *LTSB* oznacza Long-Term Servicing Branch. Klucze GVLK znajdują się w poniższych tabelach:

### Windows Server (wersje LTSC)

#### Windows Server 2022

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|--------------------------------|-------------------------------|
| Windows Server 2022 Datacenter | WX4NM-KYWYW-QJJR4-XV3QB-6VM33 |
| Windows Server 2022 Datacenter<br/>Azure Edition | NTBV8-9K7Q8-V27C6-M2BTV-KHMXV |
| Windows Server 2022 Standard<br/> VDYBN-27WPP-V4HQT-9VMD4-VMK7H |

#### Windows Server 2019

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|--------------------------------|-------------------------------|
| Windows Server 2019 Datacenter | WMDGN-G9PQG-XVVXX-R3X43-63DFG |
| Windows Server 2019 Standard | N69G4-B89J2-4G8F4-WWYCC-J464C |
| Windows Server 2019 Essentials | WVDHN-86M7X-466P6-VHXV7-YY726 |

#### Windows Server 2016

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|--------------------------------|-------------------------------|
| Windows Server 2016 Datacenter | CB7KF-BWN84-R7R2Y-793K2-8XDDG |
| Windows Server 2016 Standard | WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY |
| Windows Server 2016 Essentials | JCKRF-N37P4-C2D82-9YXRT-4M63B |

### Windows Server (wersje kanału półrocznego)

#### Windows Server, wersje 20H2, 2004, 1909, 1903 i 1809

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|---------------------------|-------------------------------|
| Windows Server Datacenter | 6NMRW-2C8FM-D24W7-TQWMY-CWH2D |
| Windows Server Standard | N2KJX-J94YW-TQVFB-DG9YT-724CC |

### Windows 11 i Windows 10 (wersje Semi-Annual Channel)

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|-----------------------------------|-------------------------------|
| Windows 11 Pro<br/>Windows 10 Pro | W269N-WFGWX-YVC9B-4J6C9-T83GX |
| Windows 11 Pro N<br/>Windows 10 Pro N | MH37W-N47XK-V7XM9-C7227-GCQG9 |
| Windows 11 Pro dla stacji roboczych<br/>Windows 10 Pro dla stacji roboczych | NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J |
| Windows 11 Pro dla stacji roboczych N<br/>Windows 10 Pro dla stacji roboczych N | 9FNHH-K3HBT-3W4TD-6383H-6XYWF |
| Windows 11 Pro Education<br/>Windows 10 Pro Education | 6TP4R-GNPTD-KYYHQ-7B7DP-J447Y |
| Windows 11 Pro Education N<br/>Windows 10 Pro Education N | YVWGF-BXNMC-HTQYQ-CPQ99-66QFC |
| Windows 11 Education<br/>Windows 10 Education | NW6C2-QMPVW-D7KK-3GKT6-VCFB2 |
| Windows 11 Education N<br/>Windows 10 Education N | 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ |
| Windows 11 Enterprise<br/>Windows 10 Enterprise | NPPR9-FWDCX-D2C8J-H872K-2YT43 |
| Windows 11 Enterprise N<br/>Windows 10 Enterprise N | DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4 |
| Windows 11 Enterprise G<br/>Windows 10 Enterprise G | YYVX9-NTFWV-6MDM3-9PT4T-4M68B |
| Windows 11 Enterprise G N<br/>Windows 10 Enterprise G N | 44RPN-FTY23-9VTTB-MP9BX-T84FV |

### Windows 10 (wersje LTSC/LTSB)

#### Windows 10 LTSC 2021 i 2019

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise LTSC 2021<br/>Windows 10 Enterprise LTSC 2019 | M7XTQ-FN8P6-TTKYV-9D4CC-J462D |
| Windows 10 Enterprise N LTSC 2021<br/>Windows 10 Enterprise N LTSC 2019 | 92NFX-8DJQP-P6BBQ-THF9C-7CG2H |

#### Windows 10 LTSB 2016

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise LTSB 2016 | DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ |
| Windows 10 Enterprise N LTSB 2016 | QFFDN-GRT3P-VKWWX-X7T3R-8B639 |

#### Windows 10 LTSB 2015

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise 2015 LTSB | WNMTR-4C88C-JK8YV-HQ7T2-76DF9 |
| Windows 10 Enterprise 2015 LTSB N | 2F77B-TNFGY-69QQF-B8YKP-D69TJ |

### Wcześniejsze wersje systemu Windows Server

#### Windows Server, wersja 1803

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|---------------------------|-------------------------------|
| Windows Server Datacenter | 2HXDN-KRXHB-GPYC7-YCKFJ-7FVDG |
| Windows Server Standard | PTXN8-JFHJM-4WC78-MPCBR-9W4KR |

#### Windows Server, wersja 1709

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|---------------------------|-------------------------------|
| Windows Server Datacenter | 6Y6KB-N82V8-D8CQV-23MJW-BWTG6 |
| Windows Server Standard | DPCNP-XQFKJ-BJF7R-FRC8D-GF6G4 |

#### Windows Server 2012 R2

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|----------------------------------------|-------------------------------|
| Windows Server 2012 R2 Standard | D2N9P-3P6X9-2R39C-7RTCD-MDVJX |
| Windows Server 2012 R2 Datacenter | W3GGN-FT8W3-Y4M27-J84CP-Q3VJ9 |
| Windows Server 2012 R2 Essentials | KNC87-3J2TX-XB4WP-VCPJV-M4FWM |

#### Windows Server 2012

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|-----------------------------------------|-------------------------------|
| Windows Server 2012 | BN3D2-R7TKB-3YPBD-8DRP2-27GG4 |
| Windows Server 2012 N | 8N2M2-HWPGY-7PGT9-HGDD8-GVGY |
| Windows Server 2012 Single Language | 2WN2H-YGCQR-KFX6K-CD6TF-84YXQ |
| Windows Server 2012 Country Specific | 4K36P-JN4VD-GDC6V-KDT89-DYFKP |
| Windows Server 2012 Standard | XC9B7-NBPP2-83J2H-RHMBY-92BT4 |
| Windows Server 2012 MultiPoint Standard | HM7DN-YVMH3-46JC3-XYTG7-CYQJJ |
| Windows Server 2012 MultiPoint Premium | XNH6W-2V9GX-RGJ4K-Y8X6F-QGJ2G |
| Windows Server 2012 Datacenter | 48HP8-DN98B-MYWDG-T2DCC-8W83P |

#### Windows Server 2008 R2

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|--------------------------------------------------|-------------------------------|
| Windows Server 2008 R2 Web | 6TPJF-RBVHG-WBW2R-86QPH-6RTM4 |
| Windows Server 2008 R2 HPC edition | TT8MH-CG224-D3D7Q-498W2-9QCTX |
| Windows Server 2008 R2 Standard | YC6KT-GKW9T-YTKYR-T4X34-R7VHC |
| Windows Server 2008 R2 Enterprise | 489J6-VHDMP-X63PK-3K798-CPX3Y |
| Windows Server 2008 R2 Datacenter | 74YFP-3QFB3-KQT8W-PMXWJ-7M648 |
| Windows Server 2008 R2 dla systemów opartych na Itanium | GT63C-RJFQ3-4GMB6-BRFB9-CB83V |

#### Windows Server 2008

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|------------------------------------------------|-------------------------------|
| Windows Web Server 2008 | WYR28-R7TFJ-3X2YQ-YCY4H-M249D |
| Windows Server 2008 Standard | TM24T-X9RMF-VWXK6-X8JC9-BFGM2 |
| Windows Server 2008 Standard bez Hyper-V | W7VD6-7JFBR-RX26B-YKQ3Y-6FFFJ |
| Windows Server 2008 Enterprise | YQGMW-MPWTJ-34KDK-48M3W-X4Q6V |
| Windows Server 2008 Enterprise bez Hyper-V | 39BXF-X8Q23-P2WWT-38T2F-G3FPG |
| Windows Server 2008 HPC | RCTX3-KWVHP-BR6TB-RB6DM-6X7HP |
| Windows Server 2008 Datacenter | 7M67G-PC374-GR742-YH8V4-TCBY3 |
| Windows Server 2008 Datacenter bez Hyper-V | 22XQ2-VRXRG-P8D42-K34TD-G3QQC |
| Windows Server 2008 dla systemów opartych na Itanium | 4DWFP-JF3DJ-B7DTH-78FJB-PDRHK |

### Wcześniejsze wersje systemu Windows

#### Windows 8.1

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|--------------------------|-------------------------------|
| Windows 8.1 Pro | GCRJD-8NW9H-F2CDX-CCM8D-9D6T9 |
| Windows 8.1 Pro N | HMCNV-VVBFX-7HMBH-CTY9B-B4FXY |
| Windows 8.1 Enterprise | MHF9N-XY6XB-WVXMC-BTDCT-MKKG7 |
| Windows 8.1 Enterprise N | TT4HM-HN7YT-62K67-RGRQJ-JFFXW |

#### Windows 8

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|--------------------------|-------------------------------|
| Windows 8 Pro | NG4HW-VH26C-733KW-K6F98-J8CK4 |
| Windows 8 Pro N | XCVCF-2NXM9-723PB-MHCB7-2RYQQ |
| Windows 8 Enterprise | 32JNW-9KQ84-P47T8-D8GGY-CWCK7 |
| Windows 8 Enterprise N | JMNMF-RHW7P-DMY6X-RF3DR-X2BQT |

#### Windows 7

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|--------------------------|-------------------------------|
| Windows 7 Professional | FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4 |
| Windows 7 Professional N | MRPKT-YTG23-K7D7T-X2JMM-QY7MG |
| Windows 7 Professional E | W82YF-2Q76Y-63HXB-FGJG9-GF7QX |
| Windows 7 Enterprise | 33PXH-7Y6KF-2VJC9-XBBR8-HVTHH |
| Windows 7 Enterprise N | YDRBP-3D83W-TY26F-D46B2-XCKRJ |
| Windows 7 Enterprise E | C29WB-22CC8-VJ326-GHFJW-H9DH4 |

#### Windows Vista

| Edycja systemu operacyjnego | Klucz produktu klienta KMS |
|--------------------------|-------------------------------|
|Windows Vista Business | YFKBB-PQJJV-G996G-VWGXY-2V3X8 |
|Windows Vista Business N | HMBQG-8H2RH-C77VX-27R82-VMQBT |
|Windows Vista Enterprise | VKK3X-68KWM-X2YGT-QR4M6-4BWMV |
|Windows Vista Enterprise N | VTC42-BM838-43QHV-84HX6-XJXKV |

## Referencje
- [Key Management Services (KMS) client activation and product keys](https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys)
---
title: "Windows GVLKs: Sbloccare la potenza delle chiavi di licenza per migliorare le prestazioni"
date: 2023-09-09
toc: true
draft: false
description: "Scoprite come le GVLK di Windows rivoluzionano le prestazioni! Scoprite le migliori chiavi di licenza e aumentate la produttività del vostro sistema senza sforzo."
genre: ["Tecnologia", "Software", "Produttività", "Sistemi operativi", "Microsoft", "Finestre", "Licenze", "Gestione delle chiavi", "Soluzioni IT", "Potenziamento"]
tags: ["Windows GVLKs", "Chiavi di licenza", "Produttività", "Prestazioni del sistema", "Gestione delle chiavi", "Sistemi operativi", "Server Windows", "Windows 10", "Soluzioni IT", "Software", "Canale di assistenza a lungo termine", "LTSC", "Filiale Servizi a Lungo Termine", "LTSB", "Prestazioni migliorate", "Microsoft", "Gestione IT", "Chiavi di attivazione", "Cliente KMS", "Elenco GVLK", "Edizioni Windows", "Attivazione della licenza", "Chiave di prodotto del cliente", "Server 2019", "Server 2016", "Windows 11 Pro", "Windows 10 Enterprise", "Windows LTSB 2016", "Amministratori IT"]
cover: "/img/cover/windows_gvlks_unlocked.png"
coverAlt: "Una colorata illustrazione a fumetti di una chiave che apre una porta rappresenta la potenza delle GVLK nello sbloccare il pieno potenziale di Windows."
coverCaption: "Liberate il potenziale di Windows con le GVLK!"
---

## Come installare un codice prodotto (GVLK) per Windows e Windows Server

Se si converte un computer da un host KMS, un MAK o un'edizione retail di Windows a un client KMS, è necessario installare il product key applicabile, noto anche come GVLK (Generic Volume License Key). Le GVLK sono utilizzate per l'attivazione dei volumi con i Key Management Services (KMS). Ecco una guida passo passo su come installare una GVLK sul sistema Windows o Windows Server.

## Script di installazione automatica di GLVK

Lo script deve essere lanciato da un powershell amministrativo nella directory contenente tutti i file del file [GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```

## Fasi di attivazione dell'installazione manuale

### Prerequisiti

Prima di procedere, assicurarsi di disporre di un codice prodotto valido e legale per la propria versione ed edizione di Windows. L'uso di chiavi di prodotto non autorizzate o piratate è contrario ai termini di servizio di Microsoft e può comportare conseguenze legali.

### Fasi dell'installazione

1. **Aprire un prompt dei comandi amministrativo:** fare clic con il tasto destro del mouse sul pulsante "Start" e selezionare "Terminale Windows (Admin)" o "Prompt dei comandi (Admin)". Se si utilizza Windows 11 o Windows 10, è possibile cercare "Prompt dei comandi", fare clic con il pulsante destro del mouse e scegliere "Esegui come amministratore".

2. **Individuare il codice prodotto appropriato (GVLK):** Individuare il GVLK per la versione e l'edizione di Windows o Windows Server dal seguente elenco:

   - *Windows Server 2022:*
     - Windows Server 2022 Datacenter: WX4NM-KYWYW-QJJR4-XV3QB-6VM33
     - Windows Server 2022 Datacenter Azure Edition: NTBV8-9K7Q8-V27C6-M2BTV-KHMXV
     - Windows Server 2022 Standard: VDYBN-27WPP-V4HQT-9VMD4-VMK7H

   - *Windows Server 2019:*
     - Windows Server 2019 Datacenter: WMDGN-G9PQG-XVVXX-R3X43-63DFG
     - Windows Server 2019 Standard: N69G4-B89J2-4G8F4-WWYCC-J464C
     - Windows Server 2019 Essentials: WVDHN-86M7X-466P6-VHXV7-YY726

   - *Windows Server 2016:*
     - Windows Server 2016 Datacenter: CB7KF-BWN84-R7R2Y-793K2-8XDDG
     - Windows Server 2016 Standard: WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY
     - Windows Server 2016 Essentials: JCKRF-N37P4-C2D82-9YXRT-4M63B

   - [Click Here to See the Others](#complete-list-of-generic-volume-license-keys-gvlk)

3. **Installare la chiave del prodotto (GVLK):** Nel prompt dei comandi amministrativi, digitare il seguente comando, sostituendo `<product key>` con il GVLK appropriato:
```sh
slmgr /ipk <product key>
```

Ad esempio, per installare il GVLK per Windows Server 2022 Datacenter edition, il comando sarà:

```sh
slmgr /ipk WX4NM-KYWYW-QJJR4-XV3QB-6VM33
```

4. **Dopo aver immesso il comando, premere Invio. Il sistema tenterà di installare il codice prodotto specificato.

5. **Messaggio di conferma:** Se l'installazione riesce, viene visualizzato un messaggio di conferma che indica che il codice prodotto è stato installato.

Se non viene visualizzato un messaggio di conferma o se si desidera forzare Windows a tentare l'attivazione in seguito all'utilizzo della chiave, provare i seguenti comandi:

```sh
slmgr /ato
slmgr /dlv
```

## Note importanti

- Assicuratevi sempre di utilizzare un codice prodotto valido e legale per la vostra versione ed edizione di Windows.
- Il comando "slmgr" si occupa di licenze e attivazione, quindi va usato con cautela.
- Per Windows 11 e Windows 10, fare riferimento alle tabelle originali per l'elenco completo dei GVLK per le diverse edizioni.

Ricordate di seguire le linee guida e i termini di servizio di Microsoft per rimanere conformi e legali.

*Disclaimer: Questo articolo è solo a scopo informativo. L'uso dei codici prodotto deve essere conforme ai termini di licenza di Microsoft e qualsiasi uso improprio è responsabilità dell'utente.


## Elenco completo delle chiavi di licenza generiche di volume (GVLK)

Nelle tabelle che seguono sono riportate le chiavi di licenza generiche di volume (GVLK) per ogni versione ed edizione di Windows. *LTSC* sta per Long-Term Servicing Channel (canale di assistenza a lungo termine) e *LTSB* rappresenta Long-Term Servicing Branch (filiale di assistenza a lungo termine). Le GVLK sono riportate nelle tabelle seguenti:

### Windows Server (versioni LTSC)

#### Windows Server 2022

| Edizione del sistema operativo | KMS Client Product Key |
|--------------------------------|-------------------------------|
| Windows Server 2022 Datacenter | WX4NM-KYWYW-QJJR4-XV3QB-6VM33 |
| Windows Server 2022 Datacenter<br/>Azure Edition | NTBV8-9K7Q8-V27C6-M2BTV-KHMXV |
| Windows Server 2022 Standard<br/> VDYBN-27WPP-V4HQT-9VMD4-VMK7H |

#### Windows Server 2019

| Edizione del sistema operativo | Chiave di prodotto del client KMS |
|--------------------------------|-------------------------------|
| Windows Server 2019 Datacenter | WMDGN-G9PQG-XVVXX-R3X43-63DFG |
| Windows Server 2019 Standard | N69G4-B89J2-4G8F4-WWYCC-J464C |
| Windows Server 2019 Essentials | WVDHN-86M7X-466P6-VHXV7-YY726 |

#### Windows Server 2016

| Edizione del sistema operativo | KMS Client Product Key |
|--------------------------------|-------------------------------|
| Windows Server 2016 Datacenter | CB7KF-BWN84-R7R2Y-793K2-8XDDG |
| Windows Server 2016 Standard | WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY |
| Windows Server 2016 Essentials | JCKRF-N37P4-C2D82-9YXRT-4M63B |

### Windows Server (versioni semestrali del canale)

#### Windows Server, versioni 20H2, 2004, 1909, 1903 e 1809

| Edizione del sistema operativo | KMS Client Product Key |
|---------------------------|-------------------------------|
| Windows Server Datacenter | 6NMRW-2C8FM-D24W7-TQWMY-CWH2D |
| Windows Server Standard | N2KJX-J94YW-TQVFB-DG9YT-724CC |

### Windows 11 e Windows 10 (versioni del canale semestrale)

| Edizione del sistema operativo | KMS Client Product Key |
|-----------------------------------|-------------------------------|
| Windows 11 Pro<br/>Windows 10 Pro | W269N-WFGWX-YVC9B-4J6C9-T83GX |
| Windows 11 Pro N<br/>Windows 10 Pro N | MH37W-N47XK-V7XM9-C7227-GCQG9 |
| Windows 11 Pro for Workstations<br/>Windows 10 Pro for Workstations | NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J |
| Windows 11 Pro per workstation N<br/>Windows 10 Pro per workstation N | 9FNHH-K3HBT-3W4TD-6383H-6XYWF |
| Windows 11 Pro Education<br/>Windows 10 Pro Education | 6TP4R-GNPTD-KYYHQ-7B7DP-J447Y |
| Windows 11 Pro Education N<br/>Windows 10 Pro Education N | YVWGF-BXNMC-HTQYQ-CPQ99-66QFC |
| Windows 11 Education<br/>Windows 10 Education | NW6C2-QMPVW-D7KK-3GKT6-VCFB2 |
| Windows 11 Education N<br/>Windows 10 Education N | 2WH4N-8QGBV-H22JP-CT43Q-MDWJ |
| Windows 11 Enterprise<br/>Windows 10 Enterprise | NPPR9-FWDCX-D2C8J-H872K-2YT43 |
| Windows 11 Enterprise N<br/>Windows 10 Enterprise N | DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4 |
| Windows 11 Enterprise G<br/>Windows 10 Enterprise G | YYVX9-NTFWV-6MDM3-9PT4T-4M68B |
| Windows 11 Enterprise G N<br/>Windows 10 Enterprise G N | 44RPN-FTY23-9VTTB-MP9BX-T84FV |

### Windows 10 (versioni LTSC/LTSB)

#### Windows 10 LTSC 2021 e 2019

| Edizione del sistema operativo | KMS Client Product Key |
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise LTSC 2021<br/>Windows 10 Enterprise LTSC 2019 | M7XTQ-FN8P6-TTKYV-9D4CC-J462D |
| Windows 10 Enterprise N LTSC 2021<br/>Windows 10 Enterprise N LTSC 2019 | 92NFX-8DJQP-P6BBQ-THF9C-7CG2H |

#### Windows 10 LTSB 2016

| Edizione del sistema operativo | KMS Client Product Key |
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise LTSB 2016 | DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ |
| Windows 10 Enterprise N LTSB 2016 | QFFDN-GRT3P-VKWWX-X7T3R-8B639 |

#### Windows 10 LTSB 2015

| Edizione del sistema operativo | KMS Client Product Key |
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise 2015 LTSB | WNMTR-4C88C-JK8YV-HQ7T2-76DF9 |
| Windows 10 Enterprise 2015 LTSB N | 2F77B-TNFGY-69QF-B8YKP-D69TJ |

### Versioni precedenti di Windows Server

#### Windows Server, versione 1803

| Edizione del sistema operativo | KMS Client Product Key |
|---------------------------|-------------------------------|
| Windows Server Datacenter | 2HXDN-KRXHB-GPYC7-YCKFJ-7FVDG |
| Windows Server Standard | PTXN8-JFHJM-4WC78-MPCBR-9W4KR |

#### Windows Server, versione 1709

| Edizione del sistema operativo | KMS Client Product Key |
|---------------------------|-------------------------------|
| Windows Server Datacenter | 6Y6KB-N82V8-D8CQV-23MJW-BWTG6 |
| Windows Server Standard | DPCNP-XQFKJ-BJF7R-FRC8D-GF6G4 |

#### Windows Server 2012 R2

| Edizione del sistema operativo | KMS Client Product Key |
|----------------------------------------|-------------------------------|
| Windows Server 2012 R2 Standard | D2N9P-3P6X9-2R39C-7RTCD-MDVJX |
| Windows Server 2012 R2 Datacenter | W3GGN-FT8W3-Y4M27-J84CP-Q3VJ9 |
| Windows Server 2012 R2 Essentials | KNC87-3J2TX-XB4WP-VCPJV-M4FWM |

#### Windows Server 2012

| Edizione del sistema operativo | KMS Client Product Key |
|-----------------------------------------|-------------------------------|
| Windows Server 2012 | BN3D2-R7TKB-3YPBD-8DRP2-27GG4 |
| Windows Server 2012 N | 8N2M2-HWPGY-7PGT9-HGDD8-GVGGY |
| Windows Server 2012 Lingua singola | 2WN2H-YGCQR-KFX6K-CD6TF-84YXQ |
| Windows Server 2012 Country Specific | 4K36P-JN4VD-GDC6V-KDT89-DYFKP |
| Windows Server 2012 Standard | XC9B7-NBPP2-83J2H-RHMBY-92BT4 |
| Windows Server 2012 MultiPoint Standard | HM7DN-YVMH3-46JC3-XYTG7-CYQJJ |
| Windows Server 2012 MultiPoint Premium | XNH6W-2V9GX-RGJ4K-Y8X6F-QGJ2G |
| Windows Server 2012 Datacenter | 48HP8-DN98B-MYWDG-T2DCC-8W83P |

#### Windows Server 2008 R2

| Edizione del sistema operativo | KMS Client Product Key |
|--------------------------------------------------|-------------------------------|
| Windows Server 2008 R2 Web | 6TPJF-RBVHG-WBW2R-86QPH-6RTM4 |
| Windows Server 2008 R2 HPC edition | TT8MH-CG224-D3D7Q-498W2-9QCTX |
| Windows Server 2008 R2 Standard | YC6KT-GKW9T-YTKYR-T4X34-R7VHC |
| Windows Server 2008 R2 Enterprise | 489J6-VHDMP-X63PK-3K798-CPX3Y |
| Windows Server 2008 R2 Datacenter | 74YFP-3QFB3-KQT8W-PMXWJ-7M648 |
| Windows Server 2008 R2 per sistemi basati su Itanium | GT63C-RJFQ3-4GMB6-BRFB9-CB83V |

#### Windows Server 2008

| Edizione del sistema operativo | KMS Client Product Key |
|------------------------------------------------|-------------------------------|
| Windows Web Server 2008 | WYR28-R7TFJ-3X2YQ-YCY4H-M249D |
| Windows Server 2008 Standard | TM24T-X9RMF-VWXK6-X8JC9-BFGM2 |
| Windows Server 2008 Standard senza Hyper-V | W7VD6-7JFBR-RX26B-YKQ3Y-6FFFJ |
| Windows Server 2008 Enterprise | YQGMW-MPWTJ-34KDK-48M3W-X4Q6V |
| Windows Server 2008 Enterprise senza Hyper-V | 39BXF-X8Q23-P2WWT-38T2F-G3FPG |
| Windows Server 2008 HPC | RCTX3-KWVHP-BR6TB-RB6DM-6X7HP |
| Windows Server 2008 Datacenter | 7M67G-PC374-GR742-YH8V4-TCBY3 |
| Windows Server 2008 Datacenter senza Hyper-V | 22XQ2-VRXRG-P8D42-K34TD-G3QQC |
| Windows Server 2008 per sistemi basati su Itanium | 4DWFP-JF3DJ-B7DTH-78FJB-PDRHK |

### Versioni precedenti di Windows

#### Windows 8.1

| Edizione del sistema operativo | KMS Client Product Key |
|--------------------------|-------------------------------|
| Windows 8.1 Pro | GCRJD-8NW9H-F2CDX-CCM8D-9D6T9 |
| Windows 8.1 Pro N | HMCNV-VVBFX-7HMBH-CTY9B-B4FXY |
| Windows 8.1 Enterprise | MHF9N-XY6XB-WVXMC-BTDCT-MKKG7 |
| Windows 8.1 Enterprise N | TT4HM-HN7YT-62K67-RGRQJ-JFFXW |

#### Windows 8

| Edizione del sistema operativo | KMS Client Product Key |
|--------------------------|-------------------------------|
| Windows 8 Pro | NG4HW-VH26C-733KW-K6F98-J8CK4 |
| Windows 8 Pro N | XCVCF-2NXM9-723PB-MHCB7-2RYQQ |
| Windows 8 Enterprise | 32JNW-9KQ84-P47T8-D8GGY-CWCK7 |
| Windows 8 Enterprise N | JMNMF-RHW7P-DMY6X-RF3DR-X2BQT |

#### Windows 7

| Edizione del sistema operativo | KMS Client Product Key |
|--------------------------|-------------------------------|
| Windows 7 Professional | FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4 |
| Windows 7 Professional N | MRPKT-YTG23-K7D7T-X2JMM-QY7MG |
| Windows 7 Professional E | W82YF-2Q76Y-63HXB-FGJG9-GF7QX |
| Windows 7 Enterprise | 33PXH-7Y6KF-2VJC9-XBBR8-HVTHH |
| Windows 7 Enterprise N | YDRBP-3D83W-TY26F-D46B2-XCKRJ |
| Windows 7 Enterprise E | C29WB-22CC8-VJ326-GHFJW-H9DH4 |

#### Windows Vista

| Edizione del sistema operativo | KMS Client Product Key |
|--------------------------|-------------------------------|
|Windows Vista Business | YFKBB-PQJJV-G996G-VWGXY-2V3X8 |
|Windows Vista Business N | HMBQG-8H2RH-C77VX-27R82-VMQBT |
|Windows Vista Enterprise | VKK3X-68KWM-X2YGT-QR4M6-4BWMV |
|Windows Vista Enterprise N | VTC42-BM838-43QHV-84HX6-XJXKV |

## Riferimenti
- [Key Management Services (KMS) client activation and product keys](https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys)
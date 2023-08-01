---
title: "Windows GVLKs : Exploiter la puissance des clés de licence pour améliorer les performances"
date: 2023-09-09
toc: true
draft: false
description: "Découvrez comment les GVLK Windows révolutionnent les performances ! Explorez les meilleures clés de licence et augmentez la productivité de votre système sans effort."
genre: ["Technologie", "Logiciel", "Productivité", "Systèmes d'exploitation", "Microsoft", "Fenêtres", "Licences", "Key Management", "Solutions informatiques", "Enhancement"]
tags: ["Windows GVLKs", "Clés de licence", "Productivité", "Performance du système", "Key Management", "Systèmes d'exploitation", "Serveur Windows", "Windows 10", "Solutions informatiques", "Logiciel", "Canal de services à long terme", "LTSC", "Direction des services à long terme", "LTSB", "Amélioration des performances", "Microsoft", "IT Management", "Clés d'activation", "KMS Client", "Liste GVLK", "Éditions Windows", "Activation de la licence", "Clé de produit du client", "Serveur 2019", "Serveur 2016", "Windows 11 Pro", "Windows 10 Enterprise", "Windows LTSB 2016", "Administrateurs informatiques"]
cover: "/img/cover/windows_gvlks_unlocked.png"
coverAlt: "Une illustration colorée d'une clé déverrouillant une porte représente le pouvoir des GVLKs dans le déverrouillage du plein potentiel de Windows."
coverCaption: "Libérez le potentiel de Windows avec les GVLK !"
---

## Comment installer une clé de produit (GVLK) pour Windows et Windows Server

Si vous convertissez un ordinateur d'un hôte KMS, d'un MAK ou d'une édition au détail de Windows en un client KMS, vous devez installer la clé de produit applicable, également connue sous le nom de GVLK (Generic Volume License Key). Les GVLK sont utilisées pour l'activation de volume avec Key Management Services (KMS). Voici un guide étape par étape sur l'installation d'une GVLK sur votre système Windows ou Windows Server.

## Script d'installation automatisée de la GVLK

Le script doit être lancé à partir d'un powerhell d'administration dans le répertoire contenant tous les fichiers de l'application [GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```

## Installation manuelle Étapes d'activation

### Conditions préalables

Avant de procéder, assurez-vous que vous disposez d'une clé de produit valide et légale pour votre version et votre édition de Windows. L'utilisation de clés de produit non autorisées ou piratées est contraire aux conditions de service de Microsoft et peut avoir des conséquences juridiques.

### Étapes de l'installation

1. **Ouvrez une invite de commande administrative:** Cliquez avec le bouton droit de la souris sur le bouton "Démarrer" et sélectionnez "Windows Terminal (Admin)" ou "Invite de commande (Admin)". Si vous utilisez Windows 11 ou Windows 10, vous pouvez rechercher "Invite de commande", cliquer dessus avec le bouton droit de la souris et choisir "Exécuter en tant qu'administrateur".

2. **Trouvez la clé de produit appropriée (GVLK):** Trouvez la GVLK pour votre version et édition de Windows ou Windows Server dans la liste suivante :

   - *Windows Server 2022:*
     - Windows Server 2022 Datacenter : WX4NM-KYWYW-QJJR4-XV3QB-6VM33
     - Windows Server 2022 Datacenter Azure Edition : NTBV8-9K7Q8-V27C6-M2BTV-KHMXV
     - Windows Server 2022 Standard : VDYBN-27WPP-V4HQT-9VMD4-VMK7H

   - Windows Server 2019:*
     - Windows Server 2019 Datacenter : WMDGN-G9PQG-XVVXX-R3X43-63DFG
     - Windows Server 2019 Standard : N69G4-B89J2-4G8F4-WWYCC-J464C
     - Windows Server 2019 Essentials : WVDHN-86M7X-466P6-VHXV7-YY726

   - Windows Server 2016:*
     - Windows Server 2016 Datacenter : CB7KF-BWN84-R7R2Y-793K2-8XDDG
     - Windows Server 2016 Standard : WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY
     - Windows Server 2016 Essentials : JCKRF-N37P4-C2D82-9YXRT-4M63B

   - [Click Here to See the Others](#complete-list-of-generic-volume-license-keys-gvlk)

3. **Installer la clé de produit (GVLK):** Dans l'invite de commande administrative, tapez la commande suivante, en remplaçant `<product key>` avec le GVLK approprié :
```sh
slmgr /ipk <product key>
```

Par exemple, pour installer le GVLK pour Windows Server 2022 Datacenter edition, la commande serait la suivante :

```sh
slmgr /ipk WX4NM-KYWYW-QJJR4-XV3QB-6VM33
```

4. **Appuyez sur Entrée:** Après avoir saisi la commande, appuyez sur Entrée. Le système tentera d'installer la clé de produit spécifiée.

5. **Message de confirmation:** Si l'installation est réussie, un message de confirmation indiquant que la clé de produit a été installée s'affiche.

Si vous ne voyez pas de message de confirmation ou si vous voulez forcer Windows à essayer d'activer le produit après avoir utilisé la clé, essayez les commandes suivantes :

```sh
slmgr /ato
slmgr /dlv
```

## Notes importantes

- Assurez-vous toujours que vous utilisez une clé de produit valide et légale pour votre version et édition de Windows.
- La commande "slmgr" traite de la licence et de l'activation, utilisez-la donc avec précaution.
- Pour Windows 11 et Windows 10, veuillez vous référer aux tableaux originaux pour la liste complète des GVLK pour les différentes éditions.

N'oubliez pas de suivre les directives de licence et les conditions d'utilisation de Microsoft pour rester conforme et légal.

*Disclaimer : Cet article est uniquement à des fins d'information. L'utilisation des clés de produit doit être conforme aux conditions de licence de Microsoft, et toute utilisation abusive est de la responsabilité de l'utilisateur.


## Liste complète des clés de licence génériques en volume (GVLK)

Dans les tableaux qui suivent, vous trouverez les clés génériques de licence en volume (GVLK) pour chaque version et édition de Windows. Le *LTSC* signifie Long-Term Servicing Channel, et le *LTSB* représente Long-Term Servicing Branch. Veuillez vous référer aux tableaux suivants pour les GVLK :

### Windows Server (versions LTSC)

#### Windows Server 2022

| Operating system edition | KMS Client Product Key |
|--------------------------------|-------------------------------|
| Windows Server 2022 Datacenter | WX4NM-KYWYW-QJJR4-XV3QB-6VM33 |
| Windows Server 2022 Datacenter<br/>Azure Edition | NTBV8-9K7Q8-V27C6-M2BTV-KHMXV |
| Windows Server 2022 Standard | VDYBN-27WPP-V4HQT-9VMD4-VMK7H |

#### Windows Server 2019

| Operating system edition | KMS Client Product Key |
|--------------------------------|-------------------------------|
| Windows Server 2019 Datacenter | WMDGN-G9PQG-XVVXX-R3X43-63DFG |
| Windows Server 2019 Standard | N69G4-B89J2-4G8F4-WWYCC-J464C |
| Windows Server 2019 Essentials | WVDHN-86M7X-466P6-VHXV7-YY726 |

#### Windows Server 2016

| Operating system edition | KMS Client Product Key |
|--------------------------------|-------------------------------|
| Windows Server 2016 Datacenter | CB7KF-BWN84-R7R2Y-793K2-8XDDG |
| Windows Server 2016 Standard | WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY |
| Windows Server 2016 Essentials | JCKRF-N37P4-C2D82-9YXRT-4M63B |

### Windows Server (Semi-Annual Channel versions)

#### Windows Server, versions 20H2, 2004, 1909, 1903, et 1809

| Édition du système d'exploitation | Clé de produit client KMS |
|---------------------------|-------------------------------|
| Windows Server Datacenter | 6NMRW-2C8FM-D24W7-TQWMY-CWH2D |
| Windows Server Standard | N2KJX-J94YW-TQVFB-DG9YT-724CC |

### Windows 11 et Windows 10 (versions Semi-Annual Channel)

| Édition du système d'exploitation | Clé de produit client KMS |
|-----------------------------------|-------------------------------|
| Windows 11 Pro<br/>Windows 10 Pro | W269N-WFGWX-YVC9B-4J6C9-T83GX |
| Windows 11 Pro N<br/>Windows 10 Pro N | MH37W-N47XK-V7XM9-C7227-GCQG9 |
| Windows 11 Pro for Workstations<br/>Windows 10 Pro for Workstations | NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J |
| Windows 11 Pro for Workstations N<br/>Windows 10 Pro for Workstations N | 9FNHH-K3HBT-3W4TD-6383H-6XYWF |
| Windows 11 Pro Education<br/>Windows 10 Pro Education | 6TP4R-GNPTD-KYYHQ-7B7DP-J447Y |
| Windows 11 Pro Education N<br/>Windows 10 Pro Education N | YVWGF-BXNMC-HTQYQ-CPQ99-66QFC |
| Windows 11 Education<br/>Windows 10 Education | NW6C2-QMPVW-D7KKK-3GKT6-VCFB2 |
| Windows 11 Education N<br/>Windows 10 Education N | 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ |
| Windows 11 Enterprise<br/>Windows 10 Enterprise | NPPR9-FWDCX-D2C8J-H872K-2YT43 |
| Windows 11 Enterprise N<br/>Windows 10 Enterprise N | DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4 |
| Windows 11 Enterprise G<br/>Windows 10 Enterprise G | YYVX9-NTFWV-6MDM3-9PT4T-4M68B |
| Windows 11 Enterprise G N<br/>Windows 10 Enterprise G N | 44RPN-FTY23-9VTTB-MP9BX-T84FV |

### Windows 10 (versions LTSC/LTSB)

#### Windows 10 LTSC 2021 et 2019

| Édition du système d'exploitation | Clé de produit client KMS |
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise LTSC 2021<br/>Windows 10 Enterprise LTSC 2019 | M7XTQ-FN8P6-TTKYV-9D4CC-J462D |
| Windows 10 Enterprise N LTSC 2021<br/>Windows 10 Enterprise N LTSC 2019 | 92NFX-8DJQP-P6BBQ-THF9C-7CG2H |

#### Windows 10 LTSB 2016

| Operating system edition | KMS Client Product Key |
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise LTSB 2016 | DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ |
| Windows 10 Enterprise N LTSB 2016 | QFFDN-GRT3P-VKWWX-X7T3R-8B639 |

#### Windows 10 LTSB 2015

| Operating system edition | KMS Client Product Key |
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise 2015 LTSB | WNMTR-4C88C-JK8YV-HQ7T2-76DF9 |
| Windows 10 Enterprise 2015 LTSB N | 2F77B-TNFGY-69QQF-B8YKP-D69TJ |

### Earlier versions of Windows Server

#### Windows Server, version 1803

| Édition du système d'exploitation | Clé de produit client KMS |
|---------------------------|-------------------------------|
| Windows Server Datacenter | 2HXDN-KRXHB-GPYC7-YCKFJ-7FVDG |
| Windows Server Standard | PTXN8-JFHJM-4WC78-MPCBR-9W4KR |

#### Windows Server, version 1709

| Operating system edition | KMS Client Product Key |
|---------------------------|-------------------------------|
| Windows Server Datacenter | 6Y6KB-N82V8-D8CQV-23MJW-BWTG6 |
| Windows Server Standard | DPCNP-XQFKJ-BJF7R-FRC8D-GF6G4 |

#### Windows Server 2012 R2

| Operating system edition | KMS Client Product Key |
|----------------------------------------|-------------------------------|
| Windows Server 2012 R2 Standard | D2N9P-3P6X9-2R39C-7RTCD-MDVJX |
| Windows Server 2012 R2 Datacenter | W3GGN-FT8W3-Y4M27-J84CP-Q3VJ9 |
| Windows Server 2012 R2 Essentials | KNC87-3J2TX-XB4WP-VCPJV-M4FWM |

#### Windows Server 2012

| Operating system edition | KMS Client Product Key |
|-----------------------------------------|-------------------------------|
| Windows Server 2012 | BN3D2-R7TKB-3YPBD-8DRP2-27GG4 |
| Windows Server 2012 N | 8N2M2-HWPGY-7PGT9-HGDD8-GVGGY |
| Windows Server 2012 Single Language | 2WN2H-YGCQR-KFX6K-CD6TF-84YXQ |
| Windows Server 2012 Spécifique au Pays | 4K36P-JN4VD-GDC6V-KDT89-DYFKP |
| Windows Server 2012 Standard | XC9B7-NBPP2-83J2H-RHMBY-92BT4 |
| Windows Server 2012 MultiPoint Standard | HM7DN-YVMH3-46JC3-XYTG7-CYQJJ |
| Windows Server 2012 MultiPoint Premium | XNH6W-2V9GX-RGJ4K-Y8X6F-QGJ2G |
| Windows Server 2012 Datacenter | 48HP8-DN98B-MYWDG-T2DCC-8W83P |

#### Windows Server 2008 R2

| Operating system edition | KMS Client Product Key |
|--------------------------------------------------|-------------------------------|
| Windows Server 2008 R2 Web | 6TPJF-RBVHG-WBW2R-86QPH-6RTM4 |
| Windows Server 2008 R2 HPC edition | TT8MH-CG224-D3D7Q-498W2-9QCTX |
| Windows Server 2008 R2 Standard | YC6KT-GKW9T-YTKYR-T4X34-R7VHC |
| Windows Server 2008 R2 Enterprise | 489J6-VHDMP-X63PK-3K798-CPX3Y |
| Windows Server 2008 R2 Datacenter | 74YFP-3QFB3-KQT8W-PMXWJ-7M648 |
| Windows Server 2008 R2 pour systèmes à base d'Itanium | GT63C-RJFQ3-4GMB6-BRFB9-CB83V |

#### Windows Server 2008

| Operating system edition | KMS Client Product Key |
|------------------------------------------------|-------------------------------|
| Windows Web Server 2008 | WYR28-R7TFJ-3X2YQ-YCY4H-M249D |
| Windows Server 2008 Standard | TM24T-X9RMF-VWXK6-X8JC9-BFGM2 |
| Windows Server 2008 Standard sans Hyper-V | W7VD6-7JFBR-RX26B-YKQ3Y-6FFFJ |
| Windows Server 2008 Enterprise | YQGMW-MPWTJ-34KDK-48M3W-X4Q6V |
| Windows Server 2008 Enterprise sans Hyper-V | 39BXF-X8Q23-P2WWT-38T2F-G3FPG |
| Windows Server 2008 HPC | RCTX3-KWVHP-BR6TB-RB6DM-6X7HP |
| Windows Server 2008 Datacenter | 7M67G-PC374-GR742-YH8V4-TCBY3 |
| Windows Server 2008 Datacenter sans Hyper-V | 22XQ2-VRXRG-P8D42-K34TD-G3QQC |
| Windows Server 2008 pour systèmes à base d'Itanium | 4DWFP-JF3DJ-B7DTH-78FJB-PDRHK |

### Versions antérieures de Windows

#### Windows 8.1

| Édition du système d'exploitation | KMS Client Product Key |
|--------------------------|-------------------------------|
| Windows 8.1 Pro | GCRJD-8NW9H-F2CDX-CCM8D-9D6T9 |
| Windows 8.1 Pro N | HMCNV-VVBFX-7HMBH-CTY9B-B4FXY |
| Windows 8.1 Enterprise | MHF9N-XY6XB-WVXMC-BTDCT-MKKG7 |
| Windows 8.1 Enterprise N | TT4HM-HN7YT-62K67-RGRQJ-JFFXW |

#### Windows 8

| Operating system edition | KMS Client Product Key |
|--------------------------|-------------------------------|
| Windows 8 Pro | NG4HW-VH26C-733KW-K6F98-J8CK4 |
| Windows 8 Pro N | XCVCF-2NXM9-723PB-MHCB7-2RYQQ |
| Windows 8 Enterprise | 32JNW-9KQ84-P47T8-D8GGY-CWCK7 |
| Windows 8 Enterprise N | JMNMF-RHW7P-DMY6X-RF3DR-X2BQT |

#### Windows 7

| Operating system edition | KMS Client Product Key |
|--------------------------|-------------------------------|
| Windows 7 Professionnel | FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4 |
| Windows 7 Professionnel N | MRPKT-YTG23-K7D7T-X2JMM-QY7MG |
| Windows 7 Professionnel E | W82YF-2Q76Y-63HXB-FGJG9-GF7QX |
| Windows 7 Enterprise | 33PXH-7Y6KF-2VJC9-XBBR8-HVTHH |
| Windows 7 Enterprise N | YDRBP-3D83W-TY26F-D46B2-XCKRJ |
| Windows 7 Enterprise E | C29WB-22CC8-VJ326-GHFJW-H9DH4 |

#### Windows Vista

| Operating system edition | KMS Client Product Key |
|--------------------------|-------------------------------|
| Windows Vista Business | YFKBB-PQJJV-G996G-VWGXY-2V3X8 |
|Windows Vista Business N | HMBQG-8H2RH-C77VX-27R82-VMQBT |
|Windows Vista Enterprise | VKK3X-68KWM-X2YGT-QR4M6-4BWMV |
| Windows Vista Enterprise N | VTC42-BM838-43QHV-84HX6-XJXKV |

## Références
- [Key Management Services (KMS) client activation and product keys](https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys)
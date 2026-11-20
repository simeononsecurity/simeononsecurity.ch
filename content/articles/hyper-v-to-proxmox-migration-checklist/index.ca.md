---
title: "Migrar una VM de Hyper-V a Proxmox VE: llista de verificació reversible"
date: 2026-10-11
lastmod: 2026-11-19
toc: true
draft: false
description: "Migreu una màquina virtual de Hyper-V a Proxmox VE amb una exportació de l'origen aturat, firmware coincident, importació de discos, prova d'arrencada aïllada i un pla de reversió."
genre: ["Virtualització", "Administració de sistemes", "Laboratori domèstic"]
tags: ["Migració de Hyper-V a Proxmox", "Migració de Hyper-V", "Migració de Proxmox VE", "Importació VHDX", "qm disk import", "Canvi de VM", "Exportació de Hyper-V", "VM Windows a Proxmox", "VirtIO a Proxmox", "Reversió de VM", "Migració UEFI", "Punts de control de Hyper-V", "TPM virtual", "Recuperació de BitLocker", "Migració de laboratori domèstic"]
cover: "/img/cover/hyper-v-to-proxmox-migration-checklist.webp"
coverAlt: "Un disc creua un pont entre un bastidor de servidors blau i un d'ataronjat, amb una ruta de retorn separada i un escut al costat de la destinació."
coverCaption: "Manteniu disponible la VM d'origen fins que el nou convidat superi les comprovacions del canvi."
---

Una **exportació de Hyper-V** conserva els fitxers d'una màquina virtual, mentre que Proxmox VE necessita una configuració nova del convidat i els fitxers de disc virtual VHDX importats. Una còpia correcta no demostra que el convidat arrenqui ni presti servei als usuaris. Aquesta llista guia la migració d'una VM amb l'origen aturat, una prova d'arrencada controlada i un canvi amb una ruta de retorn clara.

<!--more-->

## Punts clau

- **Registreu l'origen:** anoteu la generació del firmware, els camins dels discos, els punts de control, la xarxa i el xifratge abans d'exportar.
- **Atureu les escriptures:** apagueu la VM de Hyper-V abans de l'exportació final i manteniu-la apagada durant la prova a Proxmox.
- **Coincidiu amb l'arrencada:** Hyper-V de generació 1 utilitza BIOS heretat. La generació 2 utilitza UEFI.
- **Valideu el servei:** comproveu les dades, l'accés a la xarxa, les còpies de seguretat i l'estat del convidat abans de retirar l'origen.

## Abans de començar

Planifiqueu una finestra de manteniment i feu abans una prova amb una VM prescindible. Necessiteu accés d'administrador a Hyper-V i Proxmox VE, espai per a l'exportació i una còpia de seguretat verificada, separada de la còpia de migració. Reserveu temps per transferir tots els discos virtuals i provar l'aplicació del convidat. La mida del disc i la velocitat de transferència determinen el temps d'inactivitat.

Aquest procediment cobreix una VM convencional amb discos virtuals. **Les VM protegides, els discos pass-through, els discos compartits, les càrregues en clúster i les llicències vinculades al maquinari** requereixen plans específics. Anoteu qui decideix el canvi i el termini màxim per revertir. No inicieu les dues còpies a la xarxa de producció amb la mateixa identitat de màquina.

| Dada d'origen | Per què la necessiteu |
|---|---|
| **Generació i firmware de la VM** | Triar SeaBIOS o OVMF a Proxmox |
| **Estat i plantilla de Secure Boot** | Coincidir amb la política d'arrencada i inscriure claus compatibles |
| **Discos d'arrencada i de dades** | Importar tots els discos virtuals VHDX necessaris en l'ordre correcte |
| **Punts de control i fitxers AVHDX** | No tractar un disc diferencial com un disc base independent |
| **IP, DNS, MAC i VLAN** | Restaurar la connectivitat sense duplicar una identitat |
| **vTPM i BitLocker** | Preparar la recuperació abans de canviar el maquinari virtual |
| **Serveis i comprovacions de dades** | Definir les proves d'èxit i de reversió |

La generació 1 utilitza BIOS heretat. La generació 2 utilitza la Interfície de Firmware Extensible Unificada (UEFI). Un **fitxer AVHDX** és un disc diferencial de Hyper-V vinculat a un VHDX base. Un **vTPM** és un Trusted Platform Module virtual utilitzat per BitLocker i altres funcions. Una **VLAN** és una xarxa lògica separada que es transporta sobre maquinari de xarxa compartit.

**SeaBIOS** proporciona firmware BIOS heretat. **OVMF** proporciona firmware UEFI. **VirtIO** és una interfície ràpida de dispositiu virtual que requereix controladors al convidat. Un **initramfs** és el sistema de fitxers inicial de Linux que carrega controladors abans del sistema principal.

## Feu l’inventari de la màquina virtual a Hyper-V

Executeu aquestes ordres només de lectura en una sessió elevada de PowerShell a l'amfitrió de Hyper-V. Són exemples no provats. Abans d'utilitzar-les, confirmeu cada ordre amb el mòdul Hyper-V instal·lat i el procediment de canvis. Introduïu el nom de la VM quan se us demani:

```powershell
$vmName = Read-Host "Nom de la VM de Hyper-V"
Get-VM -Name $vmName | Select-Object Name, State, Generation, ProcessorCount, MemoryAssigned
Get-VMHardDiskDrive -VMName $vmName | Select-Object ControllerType, ControllerNumber, ControllerLocation, Path
Get-VMSnapshot -VMName $vmName | Select-Object Name, CreationTime
Get-VMNetworkAdapter -VMName $vmName | Select-Object Name, SwitchName, MacAddress
```

El [mòdul PowerShell de Hyper-V](https://learn.microsoft.com/en-us/powershell/module/hyper-v/) documenta aquestes ordres d'inventari. Compareu els camins dels discos amb la configuració de la VM i anoteu qualsevol ISO, disc de dades, commutador virtual, adreça estàtica o reserva DHCP connectats. Registreu el sistema operatiu i les versions de l'aplicació del convidat. Verifiqueu la còpia de seguretat restaurant una còpia de prova o consultant un resultat recent i documentat de restauració. Una còpia de fitxers sense una prova de recuperació aporta proves més febles.

Per a una VM de **generació 2**, registreu també el firmware i les opcions de seguretat:

```powershell
Get-VMFirmware -VMName $vmName | Format-List *
Get-VMSecurity -VMName $vmName | Format-List *
```

Anoteu l'estat de **Secure Boot**, la plantilla i l'opció vTPM. La referència de Microsoft de [**`Get-VMFirmware`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmfirmware) limita l'ordre a la generació 2. [**`Get-VMSecurity`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmsecurity) mostra la configuració de seguretat de la VM. No executeu **`Get-VMFirmware`** en un convidat de generació 1. Una **adreça MAC** identifica una interfície de xarxa. **DNS** associa noms amb adreces. **DHCP** assigna la configuració de xarxa. Un **disc EFI** desa la configuració UEFI.

**Resoleu els punts de control abans de l'exportació final.** Microsoft indica que una exportació de Hyper-V recopila els fitxers dels punts de control i els discos VHDX. En eliminar un punt de control des de Hyper-V, es fusiona el seu disc diferencial. No elimineu mai un fitxer **`.avhdx`** del sistema de fitxers per esborrar un punt de control. Si la fusió falla o la cadena de discos sembla incompleta, atureu-vos i seguiu les [instruccions de recuperació de punts de control de Microsoft](https://learn.microsoft.com/en-us/troubleshoot/windows-server/virtualization/hyper-v-snapshots-checkpoints-differencing-disks). La [guia de punts de control de Microsoft](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/checkpoints) explica l'eliminació i la fusió normals.

Per a un convidat Windows que utilitzi **BitLocker** o un **TPM virtual**, obteniu i verifiqueu la clau de recuperació abans de canviar el maquinari virtual. La [documentació de seguretat de Hyper-V de generació 2](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features) descriu el xifratge amb suport vTPM. Les [preguntes freqüents de BitLocker de Microsoft](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-key-management-faq) expliquen per què els canvis d'arrencada activen la recuperació. Un dispositiu TPM nou de Proxmox no reprodueix l'estat del TPM anterior. Deseu la clau fora de la VM exportada.

## Exporteu una VM aturada

Apagueu el convidat correctament. Confirmeu que Hyper-V mostri **Off** (apagada), no Saved (desada). Espereu que acabi qualsevol fusió de punts de control i exporteu la VM a una ubicació amb prou espai lliure. A Hyper-V Manager, feu clic amb el botó dret a la VM, trieu **Export** (exporta) i seleccioneu la destinació. L'equivalent de PowerShell és:

```powershell
$vmName = Read-Host "Nom de la VM de Hyper-V aturada"
$exportPath = Read-Host "Directori de destinació de l'exportació"
$vm = Get-VM -Name $vmName -ErrorAction Stop
if ($vm.State -ne 'Off') { throw "Atureu la VM i espereu que Hyper-V mostri Off (apagada) abans d'exportar." }
Export-VM -Name $vmName -Path $exportPath
```

La [guia d'exportació de Microsoft](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines) indica que l'exportació inclou discos virtuals, configuració i fitxers de punts de control. La referència de [**`Export-VM`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/export-vm) defineix l'ordre. Confirmeu que la destinació contingui els fitxers de disc previstos i les mides correctes. Conserveu apagada la VM d'origen i la còpia de seguretat independent. **No modifiqueu els fitxers exportats durant la importació.**

Transferiu els fitxers VHDX a un camí accessible des de l'amfitrió Proxmox. Tracteu l'exportació com a dades confidencials del convidat. Utilitzeu transport xifrat, limiteu l'accés a la ubicació de transferència i a l'emmagatzematge de destinació, i elimineu les còpies temporals després de validar-les. Comproveu la capacitat disponible als dos llocs. Preserveu una exportació intacta per a la reversió. Si l'exportació conté fitxers **`.avhdx`**, no trieu un **`.vhdx`** base pel nom i suposeu que conté les escriptures més recents. Resoleu la cadena de discos a Hyper-V abans de continuar.

## Prepareu la màquina virtual de destinació a Proxmox

Creeu una VM nova a la interfície web de Proxmox amb el tipus de sistema operatiu del convidat, la CPU i la memòria que heu registrat. Trieu un ID de VM nou i lliure. No instal·leu un sistema operatiu nou. Traieu el disc buit creat per l'assistent abans d'importar el disc d'origen. Durant la primera arrencada, desconnecteu l'adaptador de xarxa del pont de producció o connecteu-lo a una xarxa de prova aïllada.

| Origen Hyper-V | Destinació Proxmox |
|---|---|
| **Generació 1, BIOS heretat** | SeaBIOS |
| **Generació 2, UEFI** | OVMF amb disc EFI i política Secure Boot coincident |
| **Disc d'arrencada Windows sense controlador d'emmagatzematge VirtIO** | Connecteu-lo primer com a SATA |
| **Windows amb vTPM o BitLocker** | Dispositiu d'estat TPM nou si cal i clau de recuperació preparada abans de la primera arrencada |

La [guia de generacions de VM de Microsoft](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/Should-I-create-a-generation-1-or-2-virtual-machine-in-Hyper-V) associa la generació 1 amb BIOS heretat i la generació 2 amb UEFI. La [documentació de VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) documenta SeaBIOS, OVMF i el disc EFI que conserva els paràmetres UEFI. **Coincidiu amb el mode d'arrencada de l'origen.** Canviar-lo durant la migració afegeix un problema d'arrencada.

Per a un origen de generació 2, manteniu l'estat de **Secure Boot**. Comproveu la plantilla d'origen i seleccioneu claus inscrites compatibles amb el convidat. Els noms de les plantilles de Hyper-V no es transfereixen a Proxmox. El disc EFI de 4 MB de Proxmox i l'opció **Pre-Enroll keys** (inscripció prèvia de les claus) proporcionen claus de Secure Boot i l'activen per defecte. Verifiqueu l'arrencada de destinació abans del canvi. La [referència de firmware de Microsoft](https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmfirmware) descriu el requisit de plantilla d'origen. La [documentació del disc EFI de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descriu les claus de destinació.

Abans de canviar les claus EFI, confirmeu que la clau de recuperació estigui desada i anoteu els ID dels protectors actuals. Seguiu la documentació instal·lada de Proxmox VE i OVMF per inscriure les claus EFI. Confirmeu la clau de recuperació i comproveu `manage-bde -status` abans de la primera arrencada. No suspengueu, desactiveu ni elimineu protectors com a pas genèric de migració. Anoteu la versió del paquet de firmware, l'estat de Secure Boot i la versió del firmware, així com l'estat de BitLocker.

Si l'origen utilitza un **vTPM**, afegiu **TPM State** (estat del TPM) al panell Hardware (maquinari) de Proxmox abans de la primera arrencada. Trieu la **versió 2.0**, tret que el convidat tingui un requisit documentat de la versió 1.2. Això crea un estat TPM nou, no una còpia del vTPM de Hyper-V. Un convidat amb BitLocker necessita la clau de recuperació verificada a la primera arrencada. La [documentació TPM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descriu l'acció Hardware (maquinari) i les versions.

Per a Windows, comenceu amb un disc d'arrencada SATA, tret que el convidat ja tingui el controlador d'emmagatzematge VirtIO necessari. Després d'una arrencada correcta, instal·leu els controladors VirtIO compatibles i canvieu un dispositiu virtual cada vegada. Proxmox recomana VirtIO SCSI per rendiment, però sense el controlador d'arrencada Windows no pot accedir al disc del sistema. Per a Linux, comproveu que initramfs contingui el controlador d'emmagatzematge de destinació abans de canviar el bus. La [documentació de VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descriu els controladors de disc.

## Importeu i connecteu els discos

Al host Proxmox, comproveu el camí VHDX copiat. L'exemple importa un disc per a l'ID de VM **230** a un emmagatzematge amb ID **`local-lvm`**. Substituïu els tres valors:

```bash
qm disk import 230 /path/to/exported/boot.vhdx local-lvm
```

La referència de Proxmox [**`qm disk import`**](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc) indica que la imatge d'origen s'importa com a **disc no utilitzat**. La [documentació d'imatges de QEMU](https://www.qemu.org/docs/master/system/images) inclou VHDX entre els formats de conversió compatibles. Importeu cada disc de dades per separat. Espereu que acabi cada tasca i compareu les mides importades amb l'inventari d'origen.

Al panell **Hardware** (maquinari) de la VM, connecteu el disc d'arrencada no utilitzat com a **SATA** per a la primera arrencada Windows. Connecteu els discos de dades en l'ordre anotat. A **Options > Boot Order** (opcions > ordre d'arrencada), trieu el disc d'arrencada. Per a un convidat de generació 2, verifiqueu **OVMF** i el disc EFI. Manteniu intactes els fitxers d'importació i la VM d'origen fins que superi la validació.

## Proveu abans del canvi

Inicieu el convidat Proxmox a la xarxa aïllada. Amb la consola, comproveu la pantalla d'arrencada, l'inici de sessió del sistema operatiu, els volums, les dades de l'aplicació i els registres del servei. Una pantalla d'inici de sessió no demostra l'èxit de la migració. Feu les comprovacions anotades abans de l'exportació, inclosa una transacció representativa o una lectura de dades recents.

Per a un convidat BitLocker, desbloquegeu-lo amb la clau de recuperació si us ho demana. Després d'iniciar Windows, consulteu l'estat de protecció del volum del sistema i els protectors des d'un indicador elevat:

```powershell
manage-bde -status C:
manage-bde -protectors -get C:
```

La [guia operativa de BitLocker de Microsoft](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) documenta la inspecció de protectors i la còpia de claus de recuperació. La sortida conté informació de recuperació confidencial. No la enganxeu a un tiquet ni a un registre públic. Verifiqueu el protector previst i deseu un mètode de recuperació actual segons la política. Reinicieu el convidat i confirmeu abans del canvi que no apareix un altre avís de recuperació. Les sol·licituds repetides indiquen una prova de migració fallida, no que s'hagi de descartar la clau original.

| Prova | Criteri d'èxit |
|---|---|
| **Arrencada i discos** | El convidat s'inicia i munta tots els volums previstos |
| **Secure Boot i BitLocker** | Es manté la política d'arrencada i el convidat xifrat es reinicia sense repetir la recuperació |
| **Aplicació** | Una lectura o transacció representativa té èxit |
| **Xarxa** | Els equips necessaris arriben al convidat de prova pels ports previstos |
| **Recuperació** | La còpia de Proxmox i la prova de restauració aïllada tenen èxit abans de retirar l'origen |
| **Operacions** | La supervisió, la sincronització horària, l'apagada i l'agent del convidat funcionen com s'espera |

Quan les comprovacions de l'aplicació siguin correctes, canvieu la ruta o l'adreça de la xarxa de producció durant la finestra de manteniment. Manteniu Hyper-V apagat. Una NIC virtual diferent pot requerir una reserva DHCP nova o corregir una adreça estàtica del convidat. Des d'un altre client, comproveu DNS, les regles del tallafoc i els serveis dependents. La [documentació de VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descriu els dispositius de xarxa i les opcions de l'agent del convidat.

## Resoleu problemes i torneu enrere

| Símptoma | Primera comprovació |
|---|---|
| **No hi ha dispositiu d'arrencada** | Ordre d'arrencada, disc importat, mode BIOS o UEFI i claus Secure Boot |
| **Error d'emmagatzematge de Windows** | Connexió SATA i controlador d'emmagatzematge VirtIO absent |
| **Sol·licitud repetida de recuperació BitLocker** | Estat TPM nou, política Secure Boot, mesures d'arrencada i protectors |
| **El convidat arrenca sense xarxa** | NIC virtual nova, pont, VLAN, reserva DHCP i adreça estàtica |
| **Dades antigues o absents** | VHDX incorrecte, exportació incompleta, cadena de punts de control o disc de dades absent |

Si falla una prova necessària abans del termini de reversió, atureu la VM de Proxmox i desconnecteu-la de la xarxa de producció. Restaureu la ruta de xarxa d'origen i inicieu la VM original de Hyper-V. **No executeu mai les dues còpies amb la mateixa identitat de producció.** Registreu les escriptures acceptades per la còpia Proxmox abans de tornar a Hyper-V. Aquestes escriptures necessiten una recuperació o conciliació separada perquè el disc d'origen no les ha rebut.

Conserveu la VM d'origen i l'exportació fins que el convidat Proxmox superi les comprovacions del servei, una còpia nova i una restauració aïllada, i acabi el període d'observació acordat. La [comparació de virtualització del lloc](/articles/vmware-esxi-citrix-xenserver-hyper-v-comparison/) ajuda a triar plataforma. La [guia d'actualització de Proxmox VE de 8 a 9](/articles/proxmox-ve-8-to-9-upgrade-guide/) cobreix una tasca posterior. **La migració acaba quan la càrrega i la recuperació funcionen al nou host, no quan acaba la importació del disc.**

## Passos següents

Conserveu la VM d'origen i l'exportació fins que les comprovacions de la càrrega, les còpies de seguretat i la reversió passin durant el període d'observació acordat. Abans de retirar l'origen, consulteu l'[exercici de restauració de còpies de VM a Proxmox](/articles/proxmox-vm-backup-restore-drill/).

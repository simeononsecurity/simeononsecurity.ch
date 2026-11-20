---
title: "Migrarea unei VM Hyper-V la Proxmox VE: listă de verificare reversibilă"
date: 2026-10-11
lastmod: 2026-11-19
toc: true
draft: false
description: "Mutați o mașină virtuală Hyper-V la Proxmox VE prin exportarea sursei oprite, potrivirea firmware-ului, importarea discurilor, testarea pornirii izolate și un plan de revenire."
genre: ["Virtualizare", "Administrarea sistemelor", "Laborator de acasă"]
tags: ["Migrare Hyper-V la Proxmox", "Migrare Hyper-V", "Migrare Proxmox VE", "Import VHDX", "qm disk import", "Comutare VM", "Export Hyper-V", "VM Windows în Proxmox", "VirtIO Proxmox", "Revenire VM", "Migrare UEFI", "Puncte de control Hyper-V", "TPM virtual", "Recuperare BitLocker", "Migrare laborator de acasă"]
cover: "/img/cover/hyper-v-to-proxmox-migration-checklist.webp"
coverAlt: "Un disc trece pe un pod de la un rack albastru de servere la unul portocaliu, cu o cale de întoarcere separată și un scut lângă destinație."
coverCaption: "Păstrați VM-ul sursă disponibil până când noul invitat trece verificările de comutare."
---

Un **export Hyper-V** păstrează fișierele unei mașini virtuale, iar Proxmox VE are nevoie de o configurație nouă pentru invitat și de fișierele de disc virtual VHDX importate. O copiere reușită nu dovedește că invitatul va porni sau va furniza servicii utilizatorilor. Această listă mută o VM printr-un export cu sursa oprită, un test controlat de pornire și o comutare cu o cale clară de revenire.

<!--more-->

## Idei principale

- **Înregistrați sursa:** notați generația firmware-ului, căile discurilor, punctele de control, setările de rețea și criptarea înainte de export.
- **Opriți scrierile:** închideți VM-ul Hyper-V înaintea exportului final și păstrați-l oprit în timpul testului Proxmox.
- **Potriviți pornirea:** Hyper-V din Generația 1 folosește BIOS vechi. Generația 2 folosește UEFI.
- **Validați serviciul:** verificați datele, accesul la rețea, copiile de siguranță și starea invitatului înainte de retragerea sursei.

## Înainte să începeți

Programați o fereastră de mentenanță și testați mai întâi pe o VM dispensabilă. Aveți nevoie de acces de administrator la Hyper-V și Proxmox VE, spațiu de stocare pentru export și o copie de siguranță verificată, separată de copia de migrare. Rezervați timp pentru transferul tuturor discurilor virtuale și testarea aplicației invitatului. Dimensiunea discului și viteza transferului determină durata întreruperii.

Procedura acoperă o VM obișnuită cu discuri virtuale. **VM-urile protejate, discurile passthrough, discurile partajate, sarcinile în cluster și licențele legate de hardware** necesită planuri specifice. Notați cine decide comutarea și termenul-limită pentru revenire. Nu porniți ambele copii în rețeaua de producție cu aceeași identitate de mașină.

| Detaliu despre sursă | De ce este necesar |
|---|---|
| **Generația și firmware-ul VM-ului** | Selectați SeaBIOS sau OVMF în Proxmox |
| **Starea și șablonul Secure Boot** | Potriviți politica de pornire și înscrieți chei compatibile |
| **Discurile de pornire și de date** | Importați toate discurile virtuale VHDX necesare în ordinea corectă |
| **Puncte de control și fișiere AVHDX** | Evitați tratarea unui disc diferențial ca disc de bază independent |
| **IP, DNS, MAC și VLAN** | Restabiliți conectivitatea fără a duplica o identitate |
| **vTPM și BitLocker** | Pregătiți recuperarea înainte de schimbarea hardware-ului virtual |
| **Servicii și verificări de date** | Definiți dovezile de succes și revenire |

Generația 1 folosește BIOS vechi. Generația 2 folosește Interfața de Firmware Extensibilă Unificată (UEFI). Un **fișier AVHDX** este un disc diferențial Hyper-V conectat la un VHDX de bază. Un **vTPM** este un Trusted Platform Module virtual folosit de BitLocker și alte funcții. O **VLAN** este o rețea logică separată, transportată prin hardware de rețea partajat.

**SeaBIOS** oferă firmware BIOS vechi. **OVMF** oferă firmware UEFI. **VirtIO** este o interfață rapidă pentru dispozitive virtuale, care necesită drivere în invitat. Un **initramfs** este sistemul de fișiere Linux de la pornirea timpurie, care încarcă driverele înaintea sistemului principal.

## Colectați datele mașinii virtuale pe Hyper-V

Rulați aceste comenzi doar pentru citire într-o sesiune PowerShell elevată pe gazda Hyper-V. Sunt exemple netestate. Înainte de folosire, confirmați fiecare comandă cu modulul Hyper-V instalat și cu procedura de modificare. Introduceți numele VM-ului când vi se solicită:

```powershell
$vmName = Read-Host "Numele VM-ului Hyper-V"
Get-VM -Name $vmName | Select-Object Name, State, Generation, ProcessorCount, MemoryAssigned
Get-VMHardDiskDrive -VMName $vmName | Select-Object ControllerType, ControllerNumber, ControllerLocation, Path
Get-VMSnapshot -VMName $vmName | Select-Object Name, CreationTime
Get-VMNetworkAdapter -VMName $vmName | Select-Object Name, SwitchName, MacAddress
```

[Modulul PowerShell Hyper-V](https://learn.microsoft.com/en-us/powershell/module/hyper-v/) documentează aceste comenzi de inventariere. Comparați căile discurilor cu setările VM-ului și notați orice ISO, disc de date, switch virtual, adresă statică sau rezervare DHCP conectate. Înregistrați sistemul de operare și versiunile aplicației invitatului. Verificați backupul restaurând o copie de test sau consultând un rezultat recent, documentat, al restaurării. O copie de fișiere fără test de recuperare oferă dovezi mai slabe.

Pentru o VM din **Generația 2**, notați și firmware-ul și setările de securitate:

```powershell
Get-VMFirmware -VMName $vmName | Format-List *
Get-VMSecurity -VMName $vmName | Format-List *
```

Notați starea **Secure Boot**, șablonul și setarea vTPM. Referința Microsoft pentru [**`Get-VMFirmware`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmfirmware) limitează comanda la Generația 2. [**`Get-VMSecurity`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmsecurity) raportează configurația de securitate a VM-ului. Nu rulați **`Get-VMFirmware`** pentru un invitat din Generația 1. O **adresă MAC** identifică o interfață de rețea. **DNS** asociază nume cu adrese. **DHCP** atribuie setări de rețea. Un **disc EFI** stochează setări UEFI.

**Rezolvați punctele de control înaintea exportului final.** Microsoft spune că un export Hyper-V colectează fișierele punctelor de control și discurile VHDX. Ștergerea unui punct de control prin Hyper-V îmbină discul său diferențial. Nu ștergeți niciodată fișierul **`.avhdx`** din sistemul de fișiere pentru a elimina un punct de control. Dacă îmbinarea eșuează sau lanțul de discuri pare incomplet, opriți-vă și urmați [îndrumările Microsoft pentru recuperarea punctelor de control](https://learn.microsoft.com/en-us/troubleshoot/windows-server/virtualization/hyper-v-snapshots-checkpoints-differencing-disks). [Ghidul Microsoft pentru puncte de control](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/checkpoints) explică ștergerea și îmbinarea normală.

Pentru un invitat Windows cu **BitLocker** sau **TPM virtual**, obțineți și verificați cheia de recuperare înainte de a schimba hardware-ul virtual. [Documentația de securitate Hyper-V Generația 2](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features) descrie criptarea cu suport vTPM. [Întrebările frecvente BitLocker de la Microsoft](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-key-management-faq) explică de ce schimbările pornirii declanșează recuperarea. Un dispozitiv TPM Proxmox nou nu reproduce starea TPM veche. Păstrați cheia în afara VM-ului exportat.

## Exportați o VM oprită

Opriți normal invitatul. Confirmați că Hyper-V afișează **Off** (oprită), nu Saved (salvată). Așteptați terminarea oricărei îmbinări de puncte de control, apoi exportați VM-ul într-o locație cu spațiu liber suficient. În Hyper-V Manager, faceți clic dreapta pe VM, alegeți **Export** (exportă) și selectați destinația. Echivalentul PowerShell este:

```powershell
$vmName = Read-Host "Numele VM-ului Hyper-V oprit"
$exportPath = Read-Host "Directorul destinației de export"
$vm = Get-VM -Name $vmName -ErrorAction Stop
if ($vm.State -ne 'Off') { throw "Opriți VM-ul și așteptați ca Hyper-V să afișeze Off (oprită) înainte de export." }
Export-VM -Name $vmName -Path $exportPath
```

[Ghidul Microsoft pentru export](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines) spune că un export include discuri virtuale, configurație și fișierele punctelor de control. Referința [**`Export-VM`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/export-vm) definește comanda. Confirmați la destinație fișierele de disc și dimensiunile așteptate. Păstrați VM-ul sursă oprit și backupul independent. **Nu modificați fișierele exportate în timpul importului.**

Transferați fișierele VHDX într-o cale accesibilă gazdei Proxmox. Tratați exportul ca date sensibile ale invitatului. Folosiți transport criptat, restricționați accesul la locația de transfer și la spațiul de stocare destinație, apoi ștergeți copiile temporare după validare. Verificați capacitatea disponibilă în ambele locații. Păstrați un export neatins pentru revenire. Dacă exportul conține fișiere **`.avhdx`**, nu alegeți un **`.vhdx`** de bază după nume presupunând că include cele mai recente scrieri. Rezolvați lanțul de discuri în Hyper-V înainte de continuare.

## Creați mașina virtuală destinație în Proxmox

Creați o VM nouă în interfața web Proxmox, folosind tipul OS-ului invitat, CPU și memoria înregistrate. Alegeți un ID VM nou, nefolosit. Nu instalați un sistem de operare nou. Eliminați discul gol creat de asistent înainte de importarea discului sursă. La prima pornire, lăsați adaptorul de rețea deconectat de bridge-ul de producție sau conectați-l la o rețea de test izolată.

| Sursă Hyper-V | Destinație Proxmox |
|---|---|
| **Generația 1, BIOS vechi** | SeaBIOS |
| **Generația 2, UEFI** | OVMF cu disc EFI și politica Secure Boot potrivită |
| **Disc de pornire Windows fără driver de stocare VirtIO** | Atașați inițial ca SATA |
| **Windows cu vTPM sau BitLocker** | Dispozitiv TPM State (starea TPM) nou dacă este necesar, cheia de recuperare pregătită înainte de prima pornire |

[Ghidul Microsoft pentru generația VM](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/Should-I-create-a-generation-1-or-2-virtual-machine-in-Hyper-V) asociază Generația 1 cu BIOS vechi și Generația 2 cu UEFI. [Documentația Proxmox pentru VM](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descrie SeaBIOS, OVMF și discul EFI care păstrează setările UEFI. **Potriviți modul de pornire al sursei.** Schimbarea lui în timpul migrării creează o altă problemă de pornire.

Pentru o sursă din Generația 2, păstrați starea **Secure Boot**. Verificați șablonul sursei și selectați chei înscrise compatibile cu invitatul. Numele șabloanelor Hyper-V nu se transferă în Proxmox. Discul EFI Proxmox de 4 MB și opțiunea **Pre-Enroll keys** (înregistrarea prealabilă a cheilor) furnizează chei Secure Boot și activează Secure Boot implicit. Verificați pornirea destinației înainte de comutare. [Referința Microsoft pentru firmware](https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmfirmware) descrie cerința șablonului sursă. [Documentația discului EFI Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descrie cheile destinației.

Înainte de schimbarea cheilor EFI, verificați că cheia de recuperare este păstrată și notați ID-urile protectoarelor curente. Urmați documentația instalată Proxmox VE și OVMF pentru înscrierea cheilor EFI. Confirmați din nou cheia de recuperare și verificați `manage-bde -status` înainte de prima pornire. Nu suspendați, dezactivați sau ștergeți protectoare ca pas generic de migrare. Înregistrați versiunea pachetului firmware, starea Secure Boot și versiunea firmware, precum și starea BitLocker.

Dacă sursa folosește **vTPM**, adăugați **TPM State** (starea TPM) în panoul Hardware (componente) Proxmox înainte de prima pornire. Selectați **versiunea 2.0**, exceptând cerința documentată a invitatului pentru 1.2. Astfel se creează o stare TPM nouă, nu o copie a vTPM Hyper-V. Un invitat BitLocker are nevoie de cheia de recuperare verificată la prima pornire. [Documentația TPM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descrie acțiunea Hardware (componente) și versiunile.

Pentru Windows, începeți cu un disc de pornire SATA, cu excepția cazului în care invitatul are deja driverul de stocare VirtIO necesar. După pornirea reușită, instalați drivere VirtIO acceptate și schimbați câte un dispozitiv virtual. Proxmox recomandă VirtIO SCSI pentru performanță, dar lipsa unui driver de pornire împiedică Windows să acceseze discul de sistem. Pentru Linux, verificați dacă initramfs include driverul de stocare destinație înainte să schimbați magistrala. [Documentația VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descrie controlerele de disc.

## Importați și atașați discurile

Pe gazda Proxmox, verificați calea VHDX copiată. Exemplul următor importă un disc pentru ID-ul VM **230** într-un spațiu de stocare cu ID-ul **`local-lvm`**. Înlocuiți cele trei valori:

```bash
qm disk import 230 /path/to/exported/boot.vhdx local-lvm
```

Referința Proxmox [**`qm disk import`**](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc) spune că imaginea sursă este importată ca **disc neutilizat**. [Documentația QEMU pentru imagini](https://www.qemu.org/docs/master/system/images) listează VHDX ca format de conversie acceptat. Importați separat fiecare disc de date. Așteptați încheierea fiecărei sarcini și comparați dimensiunile importate cu inventarul sursei.

În panoul **Hardware** (componente) al VM-ului, atașați discul de pornire neutilizat ca **SATA** pentru prima pornire Windows. Atașați discurile de date în ordinea documentată. În **Options > Boot Order** (Opțiuni > ordinea de pornire), selectați discul de pornire. Pentru un invitat din Generația 2, verificați **OVMF** și discul EFI. Păstrați intacte fișierele importate și VM-ul sursă până trece validarea.

## Testați înainte de comutare

Porniți invitatul Proxmox în rețeaua izolată. În consolă, verificați ecranul de pornire, autentificarea OS, volumele, datele aplicației și jurnalele serviciului. Un prompt de autentificare nu dovedește succesul migrării. Repetați verificările înregistrate înainte de export, inclusiv o tranzacție reprezentativă sau citirea unor date recente.

Pentru un invitat BitLocker, deblocați-l cu cheia de recuperare dacă vi se solicită. După pornirea Windows, verificați starea de protecție a volumului de sistem și protectoarele într-un prompt elevat:

```powershell
manage-bde -status C:
manage-bde -protectors -get C:
```

[Ghidul operațional Microsoft pentru BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) documentează inspectarea protectoarelor și backupul cheilor. Ieșirea include informații sensibile de recuperare. Nu o copiați într-un tichet sau jurnal public. Verificați protectorul așteptat și păstrați o metodă de recuperare curentă conform politicii. Reporniți invitatul și confirmați că pornește fără o nouă solicitare de recuperare înainte de comutare. Solicitările repetate indică un test de migrare eșuat, nu un motiv pentru a abandona cheia originală.

| Verificare | Condiție de reușită |
|---|---|
| **Pornire și discuri** | Invitatul pornește și toate volumele așteptate sunt montate |
| **Secure Boot și BitLocker** | Politica de pornire rămâne valabilă, iar invitatul criptat repornește fără recuperări repetate |
| **Aplicație** | O citire sau o tranzacție reprezentativă reușește |
| **Rețea** | Clienții necesari ajung la invitatul de test pe porturile prevăzute |
| **Recuperare** | Backupul Proxmox și testul de restaurare izolat reușesc înainte de retragerea sursei |
| **Operațiuni** | Monitorizarea, sincronizarea orei, oprirea și agentul invitatului funcționează conform planului |

După ce testele aplicației trec, schimbați ruta sau adresa rețelei de producție în fereastra de mentenanță. Păstrați Hyper-V oprit. O altă NIC virtuală poate necesita o nouă rezervare DHCP sau corectarea adresei statice din invitat. De pe un client separat, verificați DNS, regulile firewall și serviciile dependente. [Documentația VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descrie dispozitivele de rețea și opțiunile agentului invitatului.

## Depanare și revenire

| Simptom | Prima verificare |
|---|---|
| **Lipsește dispozitivul de pornire** | Ordinea pornirii, discul importat, modul BIOS versus UEFI și cheile Secure Boot |
| **Eroare de stocare Windows** | Atașarea SATA și driverul de stocare VirtIO absent |
| **Solicitare repetată BitLocker** | Starea TPM nouă, politica Secure Boot, măsurătorile pornirii și protectoarele |
| **Invitatul pornește fără rețea** | NIC virtuală nouă, bridge, VLAN, rezervare DHCP și adresă statică |
| **Date vechi sau lipsă** | VHDX greșit, export incomplet, lanț de puncte de control sau disc de date lipsă |

Dacă un test obligatoriu eșuează înainte de termenul-limită de revenire, opriți VM-ul Proxmox și deconectați-l de la rețeaua de producție. Restabiliți ruta de rețea a sursei, apoi porniți VM-ul Hyper-V original. **Nu rulați niciodată ambele copii cu aceeași identitate de producție.** Înregistrați scrierile acceptate de copia Proxmox înainte de revenirea la Hyper-V. Acestea necesită recuperare sau reconciliere separată, deoarece discul sursă nu le-a primit.

Păstrați VM-ul sursă și exportul până când invitatul Proxmox trece verificările serviciilor, un backup nou și un test de restaurare izolat, apoi încheie perioada de observare agreată. [Comparația de virtualizare a site-ului](/articles/vmware-esxi-citrix-xenserver-hyper-v-comparison/) ajută la alegerea platformei. [Ghidul de actualizare Proxmox VE 8 la 9](/articles/proxmox-ve-8-to-9-upgrade-guide/) acoperă mentenanța ulterioară. **Migrarea se încheie când sarcina de lucru și recuperarea funcționează pe gazda nouă, nu când se termină importul discului.**

## Pașii următori

Păstrați VM-ul sursă și exportul până când verificările sarcinii de lucru, backupului și revenirii trec pe durata perioadei de observare agreate. Înainte să retrageți sursa, consultați [exercițiul de restaurare a backupului VM Proxmox](/articles/proxmox-vm-backup-restore-drill/).

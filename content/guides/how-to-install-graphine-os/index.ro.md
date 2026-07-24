---
title: "Ghid complet: instalarea GrapheneOS pe dispozitivul tău Google Pixel"
draft: false
toc: true
date: 2023-05-21
lastmod: 2026-05-24
description: "Află cum să instalezi GrapheneOS pe dispozitivul tău Google Pixel pentru confidențialitate și securitate sporite, folosind instalatorul web sau metoda CLI."
tags: ["GrapheneOS", "Google Pixel", "confidențialitate", "securitate", "Android", "dispozitive mobile", "sistem de operare", "ghid de instalare", "ROM personalizat", "protecția datelor", "sistem securizat", "open source", "fastboot", "bootloader", "pornire verificată", "Pixel 10", "Pixel 9"]
cover: "/img/cover/how-to-install-graphine-os.webp"
coverAlt: "O ilustrație digitală abstractă care arată un smartphone Google Pixel conectat la un computer printr-un cablu USB-C, înconjurat de elemente grafice colorate reprezentând transferul de date și securitatea."
coverCaption: ""
---

**Cum să instalezi GrapheneOS pe dispozitivul tău Google Pixel**

GrapheneOS este un sistem de operare open-source axat pe confidențialitate, bazat pe Android. Oferă protecții de securitate și confidențialitate semnificativ îmbunătățite, ceea ce îl face o alegere excelentă pentru oricine este preocupat de confidențialitatea și securitatea datelor. Dacă dețiiun dispozitiv Google Pixel compatibil și dorești să treci la GrapheneOS, acest ghid acoperă atât metoda recomandată prin **instalatorul web**, cât și metoda tradițională prin **linia de comandă (CLI)**.

> **Sfat:** Dacă întâmpini probleme în procesul de instalare, solicită ajutor pe [canalul oficial de chat GrapheneOS](https://grapheneos.org/contact#community). Înainte de a cere ajutor, încearcă să urmezi ghidul pe cont propriu, iar apoi solicită asistență pentru aspectele cu care ai dificultăți.

## Cerințe preliminare

### Cerințe hardware și de sistem

- Un computer cu cel puțin **2 GB de memorie liberă** și **32 GB spațiu de stocare liber**.
- Un **cablu USB-C de înaltă calitate** ambalat cu dispozitivul (sau un cablu USB-C la USB-A dacă este necesar). Evită hub-urile USB — conectează direct la un port din spatele computerului sau la portul laptopului.
- Instalarea dintr-o mașină virtuală **nu este recomandată** din cauza transferului USB nesigur.

> Este o bună practică să actualizezi dispozitivul Pixel înainte de a instala GrapheneOS pentru a avea cel mai recent firmware. Oricum, GrapheneOS instalează cel mai recent firmware la începutul procesului de instalare.

### Sisteme de operare acceptate oficial

#### Instalatorul web

- Windows 10 / Windows 11
- macOS Sonoma (14), macOS Sequoia (15), macOS Tahoe (26)
- Arch Linux
- Debian 12 (bookworm), Debian 13 (trixie)
- Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, Ubuntu 25.04
- Linux Mint 21 (urmați instrucțiunile Ubuntu 22.04 LTS), Linux Mint 22 (urmați instrucțiunile Ubuntu 24.04 LTS)
- Linux Mint Debian Edition 6 (urmați instrucțiunile Debian 12)
- ChromeOS
- GrapheneOS
- Android 13, 14, 15 și 16 cu certificare Play Protect

#### Metoda CLI

Toate cele de mai sus, cu excepția ChromeOS, GrapheneOS și Android (care pot folosi doar instalatorul web).

Versiunile mai vechi, fără suport, ale acestor platforme pot fi folosite, dar nu sunt acceptate oficial. **Asigură-te că sistemul de operare este actualizat înainte de a continua.**

### Browsere acceptate oficial (doar pentru instalatorul web)

- **Chromium** (în afara Ubuntu — pachetul lor Snap nu are WebUSB funcțional)
- **Vanadium** (GrapheneOS)
- **Google Chrome**
- **Microsoft Edge**
- **Brave** (cu Brave Shields dezactivat — limitează utilizarea spațiului de stocare pentru a evita amprentarea)

> - Pe Android, **dezactivează modul desktop** în browser. Modul desktop împiedică instalatorul web să detecteze Android și să solicite permisiunea de reconectare după reporniri. Este activat implicit pe tabletele mari cu 8 GB+ RAM (de ex. Pixel Tablet).
> - Evită versiunile de browsere Flatpak și Snap — acestea cauzează probleme în timpul instalării.
> - **Nu folosi** modul incognito/navigare privată — aceste moduri restricționează spațiul de stocare necesar pentru a extrage versiunea descărcată.

### Dispozitive acceptate

Ai nevoie de unul dintre [dispozitivele Pixel acceptate oficial](https://grapheneos.org/faq#supported-devices). **Evită variantele operatorilor de telefonie** — Pixelurile de la operatori au un ID de operator nenul flashat în fabrică, care dezactivează deblocarea bootloaderului și a operatorului. Procură un dispozitiv fără legătură cu un operator (deblocat).

---

## Activarea deblocării OEM

Deblocarea OEM trebuie activată din sistemul de operare înainte de a putea continua.

1. Accesează **Setări → Despre telefon/tabletă** și apasă repetat pe **Numărul build** până când modul dezvoltator este activat.
2. Accesează **Setări → Sistem → Opțiuni pentru dezvoltatori** și activează **Deblocarea OEM**. Pe unele variante SKU cu capacitate de operator, acest lucru necesită o conexiune activă la internet pentru ca sistemul de operare original să poată verifica că dispozitivul nu a fost vândut ca unitate blocată de operator.

> **Notă pentru Pixel 6a:** Deblocarea OEM nu va funcționa cu versiunea originală a sistemului de operare din fabrică. Actualizează la versiunea din **iunie 2022** sau mai recentă prin OTA, apoi efectuează o resetare la setările din fabrică pentru a remedia deblocarea OEM.

---

## Metoda de instalare 1: instalatorul web (recomandat)

[Instalatorul web GrapheneOS](https://grapheneos.org/install/web) este abordarea recomandată pentru majoritatea utilizatorilor. Folosește WebUSB direct în browser — nu este necesară instalarea de software.

### Pasul 1: Ocolirea erorilor fwupd (doar Linux)

Pe Linux, `fwupd` este cunoscut că se conectează incorect la dispozitive folosind protocolul fastboot, blocând instalatorul. Oprește-l înainte de a conecta dispozitivul:

```bash
sudo systemctl stop fwupd.service
```

Aceasta nu va persista după reporniri.

### Pasul 2: Configurarea regulilor udev (doar Linux)

Pe Arch Linux:

```bash
sudo pacman -S android-udev
```

Pe Debian și Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Pasul 3: Pornirea în interfața bootloader-ului

Ține apăsat butonul de **reducere a volumului** în timp ce dispozitivul pornește (fie pornește-l din stare oprită ținând apăsat butonul de reducere a volumului, fie repornește și ține apăsat). Dispozitivul trebuie să afișeze un **triunghi roșu de avertizare** și cuvintele **"Fastboot Mode"** — nu apăsa butonul de pornire pentru a activa "Start."

### Pasul 4: Conectarea dispozitivului

Conectează dispozitivul la computer prin USB. Pe Linux, reconectează cablul dacă regulile udev nu au fost configurate înainte de prima conexiune.

> **Pixel Tablet:** Deconectează de la stație înainte de a conecta prin USB — tableta nu poate folosi ambele simultan.

> **Windows:** Windows 10/11 actual include un driver fastboot generic pentru Pixel 4a (5G) și versiunile ulterioare. Pentru Pixeluri mai vechi sau Windows neactualizat, instalează driver-ul din Windows Update (caută în "Vizualizare actualizări opționale" → "LeMobile Android Device").

### Pasul 5: Deblocarea bootloader-ului

Accesează [https://grapheneos.org/install/web](https://grapheneos.org/install/web) și apasă butonul **Unlock the bootloader**. Confirmă pe dispozitiv folosind butoanele de volum pentru a schimba selecția și butonul de pornire pentru a confirma. **Aceasta va șterge toate datele.**

### Pasul 6: Obținerea și instalarea imaginilor din fabrică

1. Apasă **Download release** pentru a descărca imaginile din fabrică pentru dispozitivul tău.
2. Apasă **Flash factory images** și așteaptă finalizarea. Va instala automat firmware-ul, va reporni în interfața bootloader-ului și va instala sistemul de operare. **Nu interacționa cu dispozitivul până la finalizare.**

### Pasul 7: Blocarea bootloader-ului

După instalare, apasă **Lock the bootloader** în instalatorul web. Confirmă pe dispozitiv. **Aceasta va șterge din nou toate datele** — blocarea bootloader-ului activează pornirea verificată completă.

---

## Metoda de instalare 2: linia de comandă (CLI)

### Pasul 1: Deschide un terminal

Pe Windows, deschide o fereastră **PowerShell obișnuită (non-administrator)**. Elimină alias-ul moștenit `curl`:

```powershell
Remove-Item Alias:Curl
```

### Pasul 2: Instalarea fastboot

Ai nevoie de versiunea fastboot **≥ 35.0.1**.

**Arch Linux:**

```bash
sudo pacman -S android-tools
```

**Debian / Ubuntu** — pachetele lor sunt depășite. Folosește versiunea standalone:

```bash
# Debian / Ubuntu
sudo apt install libarchive-tools
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-linux.zip
echo 'acfdcccb123a8718c46c46c059b2f621140194e5ec1ac9d81715be3d6ab6cd0a  platform-tools_r35.0.2-linux.zip' | sha256sum -c
bsdtar xvf platform-tools_r35.0.2-linux.zip
export PATH="$PWD/platform-tools:$PATH"
```

**macOS:**

```bash
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-darwin.zip
echo 'SHA256 (platform-tools_r35.0.2-darwin.zip) = 1820078db90bf21628d257ff052528af1c61bb48f754b3555648f5652fa35d78' | shasum -c
tar xvf platform-tools_r35.0.2-darwin.zip
export PATH="$PWD/platform-tools:$PATH"
```

**Windows:**

```powershell
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-win.zip
(Get-FileHash platform-tools_r35.0.2-win.zip).hash -eq "2975a3eac0b19182748d64195375ad056986561d994fffbdc64332a516300bb9"
tar xvf platform-tools_r35.0.2-win.zip
$env:Path = "$pwd\platform-tools;$env:Path"
```

Verifică versiunea:

```bash
fastboot --version
# Așteptat: fastboot version 35.0.2-12147458
```

### Pasul 3: Configurarea regulilor udev (doar Linux)

Arch Linux:

```bash
sudo pacman -S android-udev
```

Debian / Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Pasul 4: Ocolirea erorilor fwupd (doar Linux)

```bash
sudo systemctl stop fwupd.service
```

### Pasul 5: Pornirea în interfața bootloader-ului

Ține apăsat **reducerea volumului** în timp ce pornești până când dispozitivul afișează **"Fastboot Mode"** cu triunghiul roșu de avertizare.

### Pasul 6: Conectarea și deblocarea bootloader-ului

Conectează prin USB, apoi rulează:

```bash
fastboot flashing unlock
```

Confirmă pe dispozitiv (butoane de volum pentru selecție, buton de pornire pentru confirmare). **Aceasta va șterge toate datele.**

### Pasul 7: Instalarea OpenSSH (pentru verificarea imaginilor)

macOS și Windows includ OpenSSH implicit.

Arch Linux:

```bash
sudo pacman -S openssh
```

Debian / Ubuntu:

```bash
sudo apt install openssh-client
```

### Pasul 8: Descărcarea și verificarea imaginilor din fabrică

Descarcă cheia de semnare:

```bash
curl -O https://releases.grapheneos.org/allowed_signers
```

Conținut așteptat:

```
contact@grapheneos.org ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIUg/m5CoP83b0rfSCzYSVA4cw4ir49io5GPoxbgxdJE
```

Descarcă imaginile din fabrică (înlocuiește `DEVICE_NAME` și `VERSION` cu valorile reale):

```bash
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip.sig
```

Verifică semnătura (Linux / macOS):

```bash
ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" \
  -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip
```

Windows:

```powershell
cmd /c 'ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip'
```

Ieșire așteptată:

```
Good "factory images" signature for contact@grapheneos.org with ED25519 key SHA256:AhgHif0mei+9aNyKLfMZBh2yptHdw/aN7Tlh/j2eFwM
```

### Pasul 9: Instalarea imaginilor din fabrică

Extrage imaginile:

```bash
# Linux
bsdtar xvf DEVICE_NAME-install-VERSION.zip

# macOS / Windows
tar xvf DEVICE_NAME-install-VERSION.zip
```

Intră în director și rulează scriptul de instalare:

```bash
cd DEVICE_NAME-install-VERSION

# Linux / macOS
bash flash-all.sh

# Windows
./flash-all.bat
```

Așteaptă finalizarea procesului. Acesta gestionează automat instalarea firmware-ului, repornirile bootloader-ului și instalarea sistemului de operare. **Nu interacționa cu dispozitivul până la finalizare.**

> **Depanare tmpfs Linux:** Dacă `/tmp` nu are suficient spațiu, folosește:
> ```bash
> mkdir tmp && TMPDIR="$PWD/tmp" ./flash-all.sh
> ```

### Pasul 10: Blocarea bootloader-ului

```bash
fastboot flashing lock
```

Confirmă pe dispozitiv. **Aceasta va șterge din nou toate datele.** Blocarea activează pornirea verificată completă și împiedică fastboot să modifice partițiile.

---

## Post-instalare

### Pornirea

Apasă butonul de pornire cu opțiunea implicită **Start** selectată în interfața bootloader-ului pentru a porni GrapheneOS.

### Dezactivarea deblocării OEM

În timpul configurării inițiale, ecranul final conține un comutator pentru deblocarea OEM (bifat implicit — lăsarea lui bifată **dezactivează** deblocarea OEM). Aceasta este recomandată. Poți schimba mai târziu în **Opțiuni pentru dezvoltatori**.

### Verificarea instalării

GrapheneOS utilizează pornirea verificată și atestarea hardware. Pornirea verificată verifică toate imaginile de firmware și sistem de operare la fiecare pornire în raport cu cheile inscripționate în siguranțele SoC. GrapheneOS inscripționează propria cheie publică de pornire verificată în elementul securizat — la fiecare pornire, această cheie verifică sistemul de operare.

#### Hash-urile cheii de pornire verificată

Când un sistem de operare alternativ este încărcat, dispozitivul afișează o **notificare galbenă** cu identificatorul sistemului de operare (sha256 al cheii de pornire verificată). Pixelurile de generația a 4-a și a 5-a afișează doar primii 32 de biți; **Pixelurile de generația a 6-a și ulterioare afișează hash-ul complet**. Compară cu hash-urile oficiale:

| Dispozitiv | Hash-ul cheii de pornire verificată |
|------------|-------------------------------------|
| Pixel 10a | `d8f879d10419eddc9fcda6280718be763f6bf12299e1f72df3ea8ad8a8eb7f80` |
| Pixel 10 Pro Fold | `55a2d44103e56d5ec65496399c417987ba77730e6488fc60ba058d09fc3caee3` |
| Pixel 10 Pro XL | `141d7fc32af7958a416f2661b37cf6f27bfb376fb5ce616aeaa27a82c7a04f74` |
| Pixel 10 Pro | `4e8ee8f717754052198ca6d2d3aaa232e2461b4293c0d6f297e519cc778de093` |
| Pixel 10 | `3f7415ea26f5df5b14ea6d153256071a7a1af9ce7b0970b7311cc463c7ea02c7` |
| Pixel 9a | `0508de44ee00bfb49ece32c418af1896391abde0f05b64f41bc9a2dfb589445b` |
| Pixel 9 Pro Fold | `af4d2c6e62be0fec54f0271b9776ff061dd8392d9f51cf6ab1551d346679e24c` |
| Pixel 9 Pro XL | `55d3c2323db91bb91f20d38d015e85112d038f6b6b5738fe352c1a80dba57023` |
| Pixel 9 Pro | `f729cab861da1b83fdfab402fc9480758f2ae78ee0b61c1f2137dd1ab7076e86` |
| Pixel 9 | `9e6a8f3e0d761a780179f93acd5721ba1ab7c8c537c7761073c0a754b0e932de` |
| Pixel 8a | `096b8bd6d44527a24ac1564b308839f67e78202185cbff9cfdcb10e63250bc5e` |
| Pixel 8 Pro | `896db2d09d84e1d6bb747002b8a114950b946e5825772a9d48ba7eb01d118c1c` |
| Pixel 8 | `cd7479653aa88208f9f03034810ef9b7b0af8a9d41e2000e458ac403a2acb233` |
| Pixel Fold | `ee0c9dfef6f55a878538b0dbf7e78e3bc3f1a13c8c44839b095fe26dd5fe2842` |
| Pixel Tablet | `94df136e6c6aa08dc26580af46f36419b5f9baf46039db076f5295b91aaff230` |
| Pixel 7a | `508d75dea10c5cbc3e7632260fc0b59f6055a8a49dd84e693b6d8899edbb01e4` |
| Pixel 7 Pro | `bc1c0dd95664604382bb888412026422742eb333071ea0b2d19036217d49182f` |
| Pixel 7 | `3efe5392be3ac38afb894d13de639e521675e62571a8a9b3ef9fc8c44fd17fa1` |
| Pixel 6a | `08c860350a9600692d10c8512f7b8e80707757468e8fbfeea2a870c0a83d6031` |
| Pixel 6 Pro | `439b76524d94c40652ce1bf0d8243773c634d2f99ba3160d8d02aa5e29ff925c` |
| Pixel 6 | `f0a890375d1405e62ebfd87e8d3f475f948ef031bbf9ddd516d5f600a23677e8` |

#### Atestarea bazată pe hardware cu Auditor

GrapheneOS oferă [aplicația Auditor](https://attestation.app/) pentru a verifica integritatea hardware-ului, firmware-ului și sistemului de operare folosind pornirea verificată și atestarea la distanță. Rezultatele sunt afișate pe un al doilea dispozitiv Android care rulează Auditor (nu pe dispozitivul verificat) sau prin intermediul [serviciului opțional de monitorizare a integrității dispozitivului](https://attestation.app/) pentru verificări automate programate cu alerte prin e-mail.

---

## Înlocuirea GrapheneOS cu sistemul de operare original

Instalarea sistemului de operare original prin [instrumentul web de flashare Google](https://flash.android.com/) este similară cu procesul de mai sus. Totuși, înainte de flashare și blocare, trebuie să ștergi cheia de pornire verificată GrapheneOS pentru a reveni complet la sistemul de operare original:

**Instalatorul web:** Folosește butonul "Erase non-stock key" din instalatorul web GrapheneOS.

**CLI:**

```bash
fastboot erase avb_custom_key
```

Apoi instalează imaginile din fabrică ale sistemului de operare original și blochează bootloader-ul.

---

## Concluzie

Instalarea GrapheneOS pe dispozitivul tău Google Pixel oferă funcții de confidențialitate și securitate de top în industrie. Folosește **instalatorul web** la [grapheneos.org/install/web](https://grapheneos.org/install/web) pentru cea mai ușoară experiență sau urmează pașii CLI de mai sus pentru o abordare tradițională. Blochează întotdeauna bootloader-ul după flashare pentru a activa pornirea verificată completă și folosește opțional aplicația Auditor pentru a confirma integritatea instalării.

## Referințe

1. [Site-ul GrapheneOS](https://grapheneos.org/)
2. [Instalatorul web GrapheneOS](https://grapheneos.org/install/web)
3. [Ghidul de instalare CLI GrapheneOS](https://grapheneos.org/install/cli)
4. [Versiunile GrapheneOS](https://grapheneos.org/releases)
5. [Ghidul de utilizare GrapheneOS](https://grapheneos.org/usage)
6. [FAQ GrapheneOS](https://grapheneos.org/faq)
7. [Aplicația Auditor](https://attestation.app/)
8. [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools)

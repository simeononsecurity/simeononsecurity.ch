---
title: "Ghid final: Instalarea sistemului de operare Graphene pe dispozitivul dvs. Google Pixel"
draft: false
toc: true
date: 2023-05-21
description: "Aflați cum să instalați Graphene OS pe dispozitivul dvs. Google Pixel pentru confidențialitate și securitate sporite."
tags: ["Graphene OS", "Google Pixel", "intimitate", "Securitate", "Android", "dispozitive mobile", "sistem de operare", "ghid de instalare", "ROM personalizat", "concentrat pe intimitate", "protejarea datelor", "OS securizat", "sursa deschisa", "securitatea dispozitivului", "caracteristici de confidențialitate", "date personale", "confidențialitatea mobilului", "confidențialitatea datelor", "personalizarea dispozitivului", "tehnologie", "Instalare pixeli", "sistem de operare axat pe confidențialitate", "Instalarea sistemului de operare Graphene", "securitate mobilă", "confidențialitate și securitate", "Personalizarea dispozitivului Pixel", "îmbunătățiri de confidențialitate", "ghid de protecție a datelor", "sistem de operare securizat", "Funcții de confidențialitate a pixelilor", "confidențialitatea datelor mobile"]
cover: "/img/cover/A_colorful_cartoon_illustration_showcasing_a_Google_Pixel.png"
coverAlt: "O ilustrație de desene animate colorate care prezintă un dispozitiv Google Pixel cu un scut care simbolizează caracteristici îmbunătățite de confidențialitate și securitate."
coverCaption: ""
---

**Cum să instalați sistemul de operare Graphene pe dispozitivul dvs. Google Pixel**

Graphene OS este un sistem de operare open source, axat pe confidențialitate, bazat pe platforma Android. Oferă funcții de securitate îmbunătățite și protecție a confidențialității, ceea ce îl face o alegere excelentă pentru persoanele preocupate de confidențialitatea și securitatea datelor. Dacă dețineți un dispozitiv Google Pixel și doriți să treceți la sistemul de operare Graphene, acest articol vă va ghida prin procesul de instalare pas cu pas.

## Condiții preliminare

Înainte de a începe procesul de instalare, există câteva cerințe preliminare pe care trebuie să le îndepliniți:

1. **Fă backup pentru datele tale**: instalarea Graphene OS va șterge toate datele de pe dispozitiv. Asigurați-vă că ați făcut backup pentru toate fișierele, fotografiile, contactele și alte date importante într-o locație sigură.

2. **Deblocați încărcătorul de pornire**: încărcătorul de pornire este un program care inițializează sistemul atunci când porniți dispozitivul. Deblocarea bootloader-ului vă permite să instalați software personalizat, cum ar fi Graphene OS. Fiecare dispozitiv Google Pixel are un proces specific pentru deblocarea bootloader-ului. Consultați documentația oficială pentru modelul dispozitivului dvs. pentru a afla cum să îl deblocați.

- [Enabling OEM unlocking](https://grapheneos.org/install/cli#enabling-oem-unlocking)
- [How to unlock the Google Pixel 3 bootloader](https://www.androidauthority.com/unlock-pixel-3-bootloader-915961/)

3. **Încărcați-vă dispozitivul**: Asigurați-vă că dispozitivul are o încărcare suficientă a bateriei înainte de a începe procesul de instalare. O baterie descărcată în timpul instalării poate duce la erori sau întreruperi.

## Instalarea sistemului de operare Graphene

Urmați pașii de mai jos pentru a instala Graphene OS pe dispozitivul dvs. Google Pixel:

______

### Pasul 1: Descărcați imaginea Graphene OS

Vizitați site-ul web oficial Graphene OS la [https://grapheneos.org](https://grapheneos.org) and navigate to the [**Releases section**](https://grapheneos.org/releases) Alegeți fișierul imagine potrivit pentru modelul dvs. Google Pixel și descărcați-l pe computer.

______

### Pasul 2: Verificați imaginea

Pentru a asigura integritatea imaginii descărcate, ar trebui să verificați semnătura criptografică a acesteia. Documentația oficială a sistemului de operare Graphene oferă instrucțiuni detaliate despre cum să verificați imaginea folosind diferite sisteme de operare. Poți găsi documentația [here](https://grapheneos.org/usage#verify-grapheneos-image)

______

### Pasul 3: Activați Opțiunile pentru dezvoltatori și Depanarea USB

1. Pe dispozitivul dvs. Google Pixel, accesați aplicația Setări.
2. Derulați în jos și apăsați pe „Despre telefon”.
3. Apăsați pe „Număr de compilare” de șapte ori pentru a activa Opțiuni pentru dezvoltatori.
4. Reveniți la pagina principală Setări și apăsați pe „Opțiuni pentru dezvoltatori”.
5. Activați depanarea USB.

______

### Pasul 4: Conectați-vă dispozitivul la computer

Utilizați un cablu USB pentru a vă conecta dispozitivul Google Pixel la computer.

______

### Pasul 5: Porniți dispozitivul în modul Fastboot

Ar trebui să ai [android development tools](https://www.xda-developers.com/install-adb-windows-macos-linux/) instalat deja pe mașina dvs.

1. Deschideți o linie de comandă sau o fereastră de terminal pe computer.
2. Introduceți următoarea comandă pentru a porni dispozitivul în modul fastboot:

```bash
adb reboot bootloader
```

______

### Pasul 6: Flashați imaginea Graphene OS

1. Odată ce dispozitivul este în modul de pornire rapidă, utilizați următoarea comandă pentru a afișa imaginea Graphene OS pe dispozitiv:

```bash
fastboot flashall
```

Această comandă va șterge toate datele existente pe dispozitiv și va instala Graphene OS.

2. Așteptați finalizarea procesului de intermitent.

______

### Pasul 7: Reporniți dispozitivul

După finalizarea procesului de instalare, reporniți dispozitivul introducând următoarea comandă:

```bash
fastboot reboot
```

______

### Pasul 8: Configurați sistemul de operare Graphene

Urmați instrucțiunile de pe ecran pentru a configura sistemul de operare Graphene pe dispozitivul dvs. Google Pixel. Fă-ți timp pentru a configura setările în funcție de preferințele tale.

## Concluzie

Instalarea Graphene OS pe dispozitivul dvs. Google Pixel vă poate oferi funcții de confidențialitate și securitate îmbunătățite. Urmând pașii prezentați în acest ghid, puteți prelua controlul asupra dispozitivului și vă puteți proteja informațiile personale de potențiale amenințări. Nu uitați să faceți o copie de rezervă a datelor înainte de a continua cu instalarea și urmați cu atenție fiecare pas pentru a asigura o instalare reușită. Bucurați-vă de beneficiile de confidențialitate și securitate pe care le oferă Graphene OS!

## Referințe

1. [Graphene OS Website](https://grapheneos.org/)
2. [Android Developer Website](https://developer.android.com/)
3. [Android Debug Bridge (ADB) Documentation](https://developer.android.com/studio/command-line/adb)
4. [Fastboot Documentation](https://developer.android.com/studio/releases/platform-tools#fastboot)
5. [Google Pixel Device Compatibility List](https://grapheneos.org/#devices)
6. [Google Developer Documentation - Unlocking the Bootloader](https://source.android.com/setup/build/running#unlocking-the-bootloader)
7. [Google Developer Documentation - Factory Images](https://developers.google.com/android/images)

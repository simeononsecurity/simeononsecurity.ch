---
title: "Găsește cheia de recuperare BitLocker înainte de a reinstala Windows"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Găsește și verifică cheia de recuperare BitLocker corectă, protejează o copie separată și alege metoda potrivită de recuperare sau reinstalare Windows înainte de a șterge o unitate."
genre: ["Securitate Windows", "Recuperarea datelor", "Administrarea sistemelor"]
tags: ["cheie de recuperare BitLocker", "reinstalare Windows 11", "reinstalare Windows 10", "Criptarea dispozitivului", "ID cheie de recuperare", "cheia de recuperare a contului Microsoft", "cheia contului de serviciu sau școală", "copie de rezervă a cheii", "unitate criptată", "instalare curată", "recuperare Windows", "copie BitLocker", "cheie de recuperare cu 48 de cifre", "suport de instalare Windows", "copie de siguranță a datelor", "criptarea unității", "listă de verificare pentru recuperare", "instalare Windows", "depanare BitLocker", "pregătire pentru reinstalare"]
cover: "/img/cover/windows-bitlocker-recovery-before-reinstall.webp"
coverAlt: "Un laptop cu o unitate blocată, un card separat cu cheia de recuperare, o copie USB și o listă de verificare bifată."
coverCaption: "Verifică cheia de recuperare înainte de a șterge unitatea."
---

O instalare curată Windows șterge unitatea selectată. Dacă unitatea veche folosește **BitLocker** sau **Criptarea dispozitivului**, găsește cheia de recuperare și copiază fișierele înainte de a începe configurarea. Cheia îți permite să accesezi datele vechi criptate. O instalare nouă Windows nu restaurează fișierele șterse de pe unitate.

<!--more-->

## Idei principale

- **Găsește cheia potrivită:** compară ID-ul afișat de Windows cu cheia din cont, de pe o imprimare sau din copia USB.
- **Testează accesul:** inspectează copia, compară ID-ul și deblochează unitatea înainte de a șterge partiții.
- **Protejează copia:** păstrează cheia de 48 de cifre separat de computer și de USB-ul de instalare.
- **Alege metoda potrivită:** folosește opțiunile de recuperare dacă ai nevoie de instalarea veche. Alege o instalare curată numai după ce verifici o copie separată a fișierelor.

## Înainte de a începe

Ai nevoie de acces la computerul afectat, de un al doilea dispozitiv pentru verificarea contului sau a copiei și de o unitate externă ori un serviciu cloud de încredere pentru fișierele importante. **Timp:** găsirea cheii depinde de accesul la cont. Copierea depinde de volumul de date. **Dificultate:** de bază pentru verificarea contului, medie pentru instrumentele de recuperare. Ghidul acoperă pregătirea și deciziile de recuperare pentru Windows 10 și Windows 11. [Ghidul pentru instalarea curată Windows](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) descrie suportul și configurarea instalării.

*Asistența standard pentru Windows 10 s-a încheiat la 14 octombrie 2025. Planifică instalarea unei versiuni Windows 11 acceptate dacă dispozitivul îndeplinește cerințele. Microsoft prezintă [ciclul de viață Windows 10 și opțiunile de asistență extinsă](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support).*

> **Avertisment:** nu șterge o partiție pentru a rezolva solicitarea de recuperare BitLocker dacă mai ai nevoie de fișierele din instalarea veche. Microsoft precizează că resetarea fără cheia de recuperare elimină acele fișiere. Vezi [recomandările Microsoft privind cheia de recuperare](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key).

## Verifică dacă criptarea este activă

**Criptarea dispozitivului** și **BitLocker** criptează o unitate, astfel încât o persoană fără datele de autentificare corecte să nu îi poată citi conținutul. Dacă Windows încă pornește, în Windows 11 deschide **Setări > Confidențialitate și securitate > Criptarea dispozitivului**. În edițiile cu administrare BitLocker, caută în Start **Gestionare BitLocker**. Notează litera unității criptate și contul folosit la configurarea dispozitivului. Pentru un dispozitiv de serviciu sau școală administrat, organizația păstrează adesea cheia.

Poți verifica starea și în linia de comandă. Caută în Start **Command Prompt**, selectează **Run as administrator** și introdu comenzile următoare. Înlocuiește `C:` dacă Windows folosește altă literă. Un **protector** este o metodă folosită de Windows pentru a debloca o unitate criptată.

```text
manage-bde.exe -status C:
manage-bde.exe -protectors -get C:
```

Prima comandă raportează criptarea, protecția și starea de blocare. A doua enumeră tipurile și ID-urile protectorilor și poate expune parola de recuperare. Microsoft descrie verificările în [ghidul de operare BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) și [referința comenzii de stare](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-status). **Nu lipi rezultatul într-o cerere de ajutor și nu îl distribui într-o captură de ecran.** Dacă dispozitivul este deja blocat, folosește ID-ul afișat pe ecranul de recuperare. Primele opt cifre te ajută să alegi cheia potrivită.

## Unde găsești cheia de recuperare BitLocker

**ID-ul cheii de recuperare** identifică o cheie stocată. **Cheia de recuperare** este numărul separat de 48 de cifre pe care îl introduci pentru a debloca unitatea. Nu introduce ID-ul în câmpul parolei de recuperare.

| Dispozitiv sau copie de rezervă | Unde să cauți |
|---|---|
| **Cont Microsoft personal** | De pe un al doilea dispozitiv, conectează-te prin [pagina Microsoft pentru chei de recuperare](https://aka.ms/myrecoverykey). Compară ID-ul înainte de a folosi cheia de 48 de cifre. |
| **Dispozitiv de serviciu sau școală** | Verifică contul organizației prin [pagina Microsoft pentru conturi de serviciu sau școală](https://aka.ms/aadrecoverykey) sau contactează echipa IT. |
| **Copie tipărită sau USB** | Găsește foaia sau fișierul text creat la activarea criptării. Compară ID-ul cu cel afișat. |

Microsoft enumeră aceste locații în [Găsește cheia de recuperare BitLocker](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key). Începe cu cheia al cărei ID corespunde solicitării. O cheie de la alt dispozitiv sau de la un protector eliminat poate să nu deblocheze acest volum. Dacă altcineva a configurat dispozitivul, cheia poate fi în contul acelei persoane.

## Creează o copie separată a cheii

Dacă Windows încă pornește într-o ediție Pro, Enterprise sau Education, caută **Gestionare BitLocker**. Selectează **Creează o copie de rezervă a cheii de recuperare** lângă unitatea criptată. Microsoft oferă salvarea într-un cont, pe o unitate USB, într-un fișier text sau pe hârtie. Dacă alegi fișier ori USB, păstrează-le numai pe un suport criptat, cu acces controlat și separat de computer. Nu folosi o locație necriptată. [Creează o copie de rezervă pentru cheia de recuperare BitLocker](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key) descrie interfața și opțiunile actuale.

În Windows Home, **Gestionare BitLocker** nu este disponibil. În Windows 11 verifică **Setări > Confidențialitate și securitate > Criptarea dispozitivului**, apoi confirmă cheia în contul Microsoft folosit la configurare. Microsoft explică faptul că [Criptarea dispozitivului](https://support.microsoft.com/en-us/windows/security/encryption/device-encryption-in-windows) salvează cheia în contul Microsoft sau de serviciu asociat la activare. Salvează o copie protejată separată dacă instalarea oferă export.

Deschide copia digitală de pe un al doilea dispozitiv. Pentru o copie tipărită, compar-o cu intrarea din cont sau ecranul de recuperare. Potrivește **ID-ul cheii de recuperare** cu cel de pe ecran sau din lista protectorilor. Confirmă că sunt prezente toate cele 48 de cifre ale cheii respective. Păstrează copia tipărită sau detașabilă departe de computerul criptat. Un hoț cu computerul și cheia ar putea ocoli protecția unității, avertizează Microsoft în [recomandările de backup](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key). Nu atașa cheia la un tichet de asistență.

> **Rezultat așteptat:** ai cheia de recuperare potrivită disponibilă în afara computerului.

## Deblochează un PC care nu pornește

Dacă apare **ecranul de recuperare BitLocker**, introdu cheia de 48 de cifre corespunzătoare ID-ului. Dacă Windows pornește, copiază fișierele înainte de a schimba partițiile. Dacă cheia deblochează unitatea, dar Windows tot nu pornește, folosește [Mediul de recuperare Windows](https://support.microsoft.com/en-us/windows/experience/backup-recovery/windows-recovery-environment) și încearcă **Reparare la pornire** înainte de resetare. Unele instrumente cer cheia cât timp unitatea este criptată.

Pentru a copia fișiere din instrumentele de recuperare, deschide **Depanare > Opțiuni avansate > Command Prompt** în Mediul de recuperare Windows. Folosește `manage-bde -status` și `dir` pentru a identifica volumul Windows criptat și o unitate externă separată pentru backup. **Literele unităților pot fi diferite de cele din Windows obișnuit.** Nu copia pe USB-ul de instalare sau pe unitatea-sursă criptată.

```text
manage-bde.exe -status
dir D:\Users
dir E:\
```

Literele sunt exemple. După ce identifici volumele corecte, deblochează volumul Windows cu cheia potrivită. Înlocuiește litera și substituentul cu valorile tale. Tastează local cheia reală de 48 de cifre. Nu publica și nu distribui rezultatul.

```text
manage-bde.exe -unlock D: -recoverypassword <48-digit-key>
```

Opțiunea documentată `-recoverypassword` primește cheia de 48 de cifre ca argument de comandă. Astfel, cheia poate apărea în istoricul shellului, transcrieri și inspecția proceselor. Folosește ecranul de recuperare Windows dacă vrei să introduci cheia fără argument de linie de comandă. Dacă ai salvat separat un fișier `.bek`, `-recoverykey <path-to-external-bek>` evită tastarea celor 48 de cifre. Nu include cheia în capturi sau tichete.

Microsoft documentează [comanda de deblocare](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-unlock). [Recomandările de recuperare](https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/bitlocker-recovery-known-issues) descriu și copierea fișierelor utilizatorului pe altă unitate după deblocare. Pentru exemplul de copiere a folderului Documents, confirmă mai întâi numele contului Windows și litera unității externe, apoi înlocuiește ambele căi:

```text
xcopy "D:\Users\Name\Documents" "E:\Backup\Documents" /S /E /I /H /V
```

Opțiunile **`/S /E`** includ subfolderele, chiar și cele goale. **`/I`** tratează destinația ca folder, **`/H`** include fișierele ascunse, iar **`/V`** verifică fiecare fișier scris. Microsoft descrie aceste opțiuni în [referința xcopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy). Repetă pentru celelalte foldere necesare. Deschide fișierele copiate de pe alt dispozitiv înainte să ștergi unitatea Windows. Dacă nu poți identifica volumele sau copierea eșuează, oprește-te și contactează un specialist de încredere în recuperarea datelor.

## Alege dacă reinstalezi

**O copie a cheii nu este o copie a fișierelor.** Urmează ordinea aceasta înainte de a alege o metodă de reinstalare:

1. Identifică unitatea criptată și ID-ul cheii sale de recuperare.
2. Recuperează cheia potrivită de 48 de cifre din cont, copia tipărită sau backupul USB.
3. Dacă unitatea este blocată, deblocheaz-o prin ecranul sau instrumentele de recuperare.
4. Copiază Desktop, Documents, Pictures și alte foldere locale pe o unitate externă sau într-un cloud de încredere. Include, dacă este cazul, exporturi de browser, date de aplicații și informații despre licențe.
5. Deschide câteva fișiere copiate de pe un al doilea dispozitiv.
6. Alege reparare, resetare sau reinstalare numai după verificarea copiei.

> **Rezultat așteptat:** cheia potrivită și fișierele importante sunt accesibile în afara vechii instalări Windows.

Microsoft enumeră [opțiunile de recuperare Windows](https://support.microsoft.com/en-us/windows/experience/backup-recovery/recovery-options-in-windows), cu efecte diferite pentru fișiere și aplicații. Multe opțiuni din Mediul de recuperare Windows cer cheia când BitLocker protejează unitatea. Dacă volumul este blocat acolo, **Păstrează-mi fișierele** nu îl deblochează fără cheie.

**Reparare la pornire** și **Restaurare sistem** încearcă să repare instalarea existentă. **Resetează acest PC** oferă opțiunea **Păstrează-mi fișierele**, dar elimină aplicațiile și setările. **Elimină totul** șterge fișierele personale. Pornirea **`setup.exe` dintr-o sesiune Windows activă** oferă o reinstalare pe loc, cu opțiuni de păstrare a datelor. Alegerea **Instalează Windows** după pornirea de pe USB începe o instalare curată care elimină fișierele, aplicațiile și setările instalării Windows selectate. Același suport oferă și o metodă de reparare. Citește opțiunea afișată și verifică discul-țintă înainte să confirmi resetarea sau instalarea. Microsoft descrie ambele metode în [instrucțiunile de reinstalare](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media).

| Situație | Următoarea acțiune |
|---|---|
| **Windows pornește și ai nevoie de fișiere** | Fă backup fișierelor, verifică cheia și apoi alege repararea sau reinstalarea. |
| **Windows cere cheia** | Potrivește ID-ul de pe ecran cu o cheie salvată înainte să modifici unitatea. |
| **Nu există cheie potrivită și nici backup al fișierelor** | Oprește-te înainte de a șterge unitatea. Verifică fiecare cont, copie tipărită, backup USB și contactează echipa IT. |
| **Fișierele sunt copiate și vrei să începi de la zero** | Urmează [instrucțiunile de reinstalare Microsoft](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media) și alege cu atenție discul-țintă. |

Microsoft spune că personalul de asistență nu poate recrea o cheie pierdută. Dacă nu o găsești, nu mai modifica setările firmware și verifică toate locurile cu copii de rezervă. Cere ajutor administratorului pentru un dispozitiv gestionat. Resetarea fără cheia necesară elimină fișierele vechi. Instalarea curată elimină și fișierele personale, aplicațiile, personalizările dispozitivului și setările instalării selectate. Ia decizia după ce verifici backupul.

## Depanare

- **Cheia nu funcționează:** verifică din nou ID-ul și contul. Un dispozitiv poate avea mai multe chei salvate.
- **Gestionare BitLocker nu este disponibil:** Windows Home folosește Criptarea dispozitivului pe dispozitive compatibile. Verifică Setări și contul Microsoft folosit la configurare.
- **În cont apar mai multe chei:** compară primele opt cifre ale ID-ului de pe ecran cu înregistrările salvate. Nu alege cheia doar după numele dispozitivului.
- **Cheia deblochează unitatea, dar Windows nu pornește:** încearcă Reparare la pornire din Mediul de recuperare Windows. Copiază fișierele accesibile înainte de resetare sau instalare curată.
- **Cheia este la serviciu sau școală:** contactează administratorul dispozitivului înainte de resetare sau reinstalare.
- **Fișierul cheii este pe computerul blocat:** caută un cont separat, o copie tipărită sau o copie detașabilă. O copie aflată doar pe unitatea criptată nu ajută cât timp aceasta este blocată.
- **Solicitarea a apărut după o schimbare de firmware:** notează schimbarea și nu mai modifica firmware-ul. Găsește cheia potrivită sau contactează administratorul.

## Pașii următori

După ce verifici cheia și fișierele, urmează [ghidul de instalare curată Windows](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) dacă metoda se potrivește obiectivului tău. După pornirea Windows, verifică **Setări > Confidențialitate și securitate > Criptarea dispozitivului** sau caută **Gestionare BitLocker**. În Pro, Enterprise sau Education, selectează **Creează o copie de rezervă a cheii de recuperare**. În Home, verifică dacă acel cont conține cheia actuală și salvează o copie separată dacă Windows oferă export. Nu presupune că vechea cheie se potrivește unei instalări noi criptate.

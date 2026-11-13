---
title: "Testează o restaurare de backup homelab cu Restic"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Verifică dacă un backup homelab restaurează fișiere utilizabile. Stabilește un obiectiv de recuperare, restaurează cu Restic într-o altă locație, verifică datele și înregistrează rezultatul."
genre: ["Homelab", "Backup", "Recuperare în caz de dezastru"]
tags: ["backup homelab", "test de restaurare", "restaurare Restic", "verificare backup", "test de recuperare", "recuperare în caz de dezastru", "RPO", "RTO", "depozit backup", "verificare Restic", "backup NAS", "backup server", "recuperare VM", "restaurare fișiere", "criptare backup", "monitorizare backup", "plan de recuperare", "test backup", "backup extern", "integritatea datelor"]
cover: "/img/cover/homelab-backup-restore-drill.webp"
coverAlt: "Un server homelab și un NAS fac backup pe o unitate separată, cu un dosar de restaurare verificat pe un computer de test izolat și un cronometru."
coverCaption: "Restaurează într-o destinație separată, verifică datele și măsoară timpul necesar."
---

Un proces de backup raportat ca reușit nu demonstrează că poți restaura un fișier utilizabil. Un **test de restaurare** verifică traseul de la copia stocată la date funcționale fără să înlocuiască fișierele active. Acest ghid folosește Restic pentru un exemplu de restaurare la nivel de fișier și oferă un formular pe care îl poți repeta după schimbări în laborator.

<!--more-->

Restic este un program de backup. Un **depozit** este spațiul de stocare protejat care păstrează datele backupului. Un **instantaneu** este un punct de backup salvat.

## Idei principale

- **Alege un obiectiv:** Selectează fișierele sau serviciul de recuperat și definește un punct și o durată acceptabile.
- **Restaurează separat:** Folosește o destinație de test goală, ca testul să nu suprascrie datele active.
- **Verifică rezultatul:** Deschide fișierele restaurate, verifică datele aplicației când este posibil și măsoară timpul scurs.
- **Înregistrează problemele:** Notează ID-ul instantaneului, elementele lipsă, permisiunile și reparațiile în planul de recuperare.

## Înainte să începi

Ai nevoie de un depozit de backup funcțional, de parola sau cheia lui, de o destinație cu suficient spațiu liber și de permisiuni de citire atât pentru backup, cât și pentru locația de test. Exemplul presupune că Restic este instalat și că depozitul conține un backup recent al fișierelor. [Ghidul de pornire rapidă Restic](https://restic.readthedocs.io/en/stable/010_introduction.html) explică crearea depozitului și primele backupuri. [Ghidul de backup 3-2-1](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) al site-ului discută amplasarea copiilor. [Prezentarea homelab](/articles/what-is-a-homelab-and-should-you-have-one/) include o listă scurtă pentru testarea backupului.

Acest test verifică fișierele dintr-un instantaneu. O bază de date, o mașină virtuală sau o aplicație necesită și pași proprii de recuperare. Izolează sistemul de test dacă pornirea serviciului restaurat ar putea interfera cu cel activ. O copiere reușită a fișierelor nu demonstrează că toate serviciile vor porni.

> **Avertisment:** La primul test, nu restaura peste o cale activă. Folosește un director de test gol pe un sistem de fișiere sau o gazdă separată. Nu include parola depozitului în capturi de ecran, tichete sau istoricul shellului.

## Definește obiectivul de recuperare

Notează de ce ai nevoie după o defecțiune. **Obiectivul punctului de recuperare (RPO)** este momentul până la care datele trebuie recuperate după o întrerupere. Reprezintă pierderea maximă acceptabilă de date. **Obiectivul timpului de recuperare (RTO)** arată cât timp poate rămâne serviciul indisponibil. NIST le definește pe ambele în [ghidul de planificare pentru situații de urgență](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf). Obiectivele tale trebuie să țină cont de frecvența modificării datelor și de durata restaurării pe hardware-ul tău.

| Element | Obiectiv ilustrativ | Ce înregistrezi |
|---|---|---|
| **Documente de familie** | Ultimul backup nocturn | Ora ultimului instantaneu și fișierele deschise |
| **Configurația unui serviciu casnic** | Ultima modificare cunoscută ca funcțională | Versiunea configurației și secretele necesare |
| **Biblioteca media de pe stocare conectată la rețea (NAS)** | Backup săptămânal | Redarea unui eșantion și timpul restaurării |

Obiectivele de mai sus sunt exemple, nu rezultate măsurate. În planul de recuperare, înregistrează locația backupului și modul în care o persoană autorizată obține parola depozitului sau cheia de criptare. Nu pune valori secrete în plan ori în raportul testului. Stochează secretele printr-o cale protejată, independentă de gazda defectă. Un depozit care supraviețuiește, dar își pierde singura parolă, nu poate fi recuperat.

Alege un **set de fișiere critice** pentru test. Include un fișier mic despre care știi că ar trebui să existe în cel mai recent instantaneu. Pentru un serviciu, enumeră și configurația, exportul bazei de date, certificatele și versiunea aplicației necesare pornirii. Confirmă că metoda de backup capturează date coerente ale aplicației înainte să te bazezi pe o copie la nivel de fișier a unei baze de date active.

## Găsește un instantaneu

Folosește accesul la depozit aprobat pentru testul de restaurare. Restic folosește un blocaj temporar al depozitului atunci când citește sau modifică datele de backup. Comenzile de mai jos presupun că depozitul permite această operație. Ține separat sursa activă și destinația de test. Înlocuiește `/path/to/repository` cu calea reală a depozitului Restic, apoi listează instantaneele:

```bash
restic -r /path/to/repository snapshots
```

Restic solicită parola depozitului dacă nu ai furnizat-o printr-o metodă configurată de gestionare a secretelor. [Lista instantaneelor](https://restic.readthedocs.io/en/stable/010_introduction.html) afișează ID-ul, data, gazda și căile sursă. Notează ID-ul și marcajul de timp pe care vrei să le testezi. Compară timpul cu RPO-ul. Un jurnal recent al sarcinii nu înlocuiește această verificare, fiindcă instantaneul necesar poate fi mai vechi decât crezi.

Dacă instantaneul așteptat lipsește, oprește testul și investighează programarea backupului, selecția sursei și calea depozitului. Nu alege în tăcere un instantaneu mai vechi și nu declara că obiectivul de recuperare a fost îndeplinit.

## Restaurează într-o destinație goală

Creează un **director de destinație gol** pe un sistem de fișiere de test cu suficient spațiu pentru instantaneu. Nu indica drept destinație sursa originală, o partajare de producție montată sau un dosar existent cu date pe care vrei să le păstrezi. Înlocuiește `SNAPSHOT_ID` și ambele căi exemplu înainte de a rula comanda:

```bash
restic -r /path/to/repository restore SNAPSHOT_ID \
  --target /path/to/empty-restore-drill
```

[Ghidul de restaurare Restic](https://restic.readthedocs.io/en/stable/050_restore.html) descrie ID-ul instantaneului și calea `--target`. Structura restaurată păstrează calea sursă sub directorul destinație, deci găsește fișierele efective înainte să evaluezi rezultatul. Dacă ai nevoie doar de o selecție mică, folosește [filtrele de includere documentate](https://restic.readthedocs.io/en/stable/050_restore.html) și notează ce ai exclus. Nu utiliza `--delete` într-un test. Restic precizează că opțiunea șterge din destinație fișierele care nu există în instantaneu.

Pornește cronometrul când începe restaurarea. Oprește-l când fișierele necesare sunt prezente și utilizabile, nu când comanda afișează primul progres. Notează locația depozitului, legătura de rețea, volumul datelor și gazda de test, fiindcă aceste condiții influențează o recuperare viitoare.

> **Rezultat așteptat:** Instantaneul ales este restaurat într-o destinație separată fără să modifice sursa activă.

## Verifică datele și recuperarea serviciului

Deschide câteva fișiere restaurate cu aplicația care le citește de obicei. Include un fișier recent, unul mai vechi și unul dintr-un director imbricat. Compară dimensiuni sau sume de control cunoscute dacă le-ai înregistrat înainte de backup. Pe Linux, verifică proprietarul și permisiunile, deoarece un fișier lizibil pentru contul de test poate să nu fie accesibil contului serviciului.

Pentru un serviciu, restaurează într-o instanță de test izolată. Verifică configurația, secretele necesare, consistența bazei de date, pornirea și o acțiune reprezentativă a utilizatorului. O restaurare de fișiere care omite o bază de date sau un secret nu reprezintă o recuperare completă a serviciului. Nu porni niciodată instanța de test către baza de date activă ori o adresă de producție fără un plan controlat de tranziție.

După restaurarea eșantionului, rulează verificarea depozitului Restic:

```bash
restic -r /path/to/repository check
```

Pentru citirea tuturor datelor din depozit, folosește `check --read-data` într-o fereastră de mentenanță. Restic avertizează că citește întregul depozit și poate descărca multe date dintr-un backend la distanță. [Ghidul de depanare Restic](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) descrie verificarea și costul ei. O verificare curată sporește încrederea, dar nu înlocuiește deschiderea fișierelor restaurate sau pornirea serviciului.

```bash
restic -r /path/to/repository check --read-data
```

Compară vechimea instantaneului cu RPO-ul și timpul măsurat de recuperare cu RTO-ul. Dacă oricare obiectiv nu este atins, testul a eșuat chiar dacă Restic s-a încheiat fără eroare. Ajustează frecvența backupului, locația stocării, lățimea de bandă sau procedura de recuperare și testează din nou.

## Păstrează un raport de restaurare

Scrie un raport scurt după fiecare test. [Controlul de backup SP 800-53](https://csrc.nist.gov/CSRC/media/Projects/risk-management/800-53%20Downloads/800-53r5/SP_800-53_v5_1-derived-OSCAL.pdf) al NIST include restaurarea unor funcții de sistem eșantionate ca metodă de testare a recuperării. Un raport repetabil te ajută să vezi dacă planul se îmbunătățește.

| Câmp | Rezultatul de introdus |
|---|---|
| **Data și operatorul** | Când a avut loc testul și cine l-a rulat |
| **Depozitul și instantaneul** | Locația, ID-ul, marcajul de timp și căile sursă |
| **Obiectivul recuperării** | Fișierele sau serviciul testat, plus RPO și RTO |
| **Rezultatul măsurat** | Vechimea instantaneului, timpul restaurării și verificările fișierelor sau serviciului |
| **Probleme** | Date lipsă, acces la cheie, permisiuni, rețea sau erori de pornire |
| **Acțiunea următoare** | Responsabil, remediere și data următorului test |

Nu include în raport parola depozitului, cheia de recuperare sau conținut sensibil al fișierelor. Păstrează-le într-un depozit protejat de secrete și documentează cum le obține o persoană autorizată în timpul unei întreruperi.

## Depanare

- **Parola lipsește:** Verifică metoda independentă de păstrare a cheii. Nu presupune că gazda defectă va putea furniza propria cheie.
- **Instantaneul este prea vechi:** Verifică programarea, sarcinile eșuate, căile sursă și dacă gazda a salvat în alt depozit.
- **Restaurarea este prea lentă:** Măsoară viteza de citire a stocării, legătura de rețea și volumul datelor. Testează un subset critic mai mic, apoi revizuiește RTO-ul sau proiectarea recuperării.
- **Fișierul există, dar serviciul eșuează:** Verifică exporturile bazei de date, versiunea aplicației, proprietarul, permisiunile, certificatele și secretele lipsă.
- **Verificarea depozitului raportează erori:** Păstrează rezultatul și o copie a depozitului dacă este posibil. Urmează instrucțiunile Restic pentru [investigarea deteriorării](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) înainte de a încerca reparații.
- **Testul a modificat date active:** Oprește serviciul de test, verifică datele de producție și îmbunătățește planul de izolare înainte să repeți testul.

## Pașii următori

Repetă testul după schimbarea software-ului de backup, stocării, cheilor de criptare sau serviciilor critice. Alternează în timp seturi diferite de fișiere și recuperări complete de servicii. Păstrează o copie independentă conform [planului 3-2-1](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/). Scopul este un proces măsurat de restaurare, repetabil când gazda originală nu mai există.

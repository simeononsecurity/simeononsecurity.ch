---
title: "Dimensionează un UPS pentru homelab și testează oprirea automată"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Măsoară consumul homelabului, compară limitele UPS-ului în wați și VA, verifică autonomia la sarcina ta și testează oprirea în siguranță înainte să te bazezi pe baterie."
genre: ["Laborator de acasă", "Protecția alimentării", "Administrarea sistemelor"]
tags: ["UPS pentru homelab", "dimensionarea UPS-ului", "autonomia UPS-ului", "oprire automată", "Network UPS Tools", "wați UPS", "VA UPS", "factor de putere", "alimentare de rezervă", "oprirea serverului", "oprirea NAS-ului", "pană de curent", "test UPS", "curba autonomiei", "wattmetru", "monitorizare UPS", "înlocuirea bateriei", "protecție la supratensiune", "oprire ordonată", "alimentarea homelabului"]
cover: "/img/cover/ups-runtime-sizing-shutdown-test.webp"
coverAlt: "Un UPS de homelab alimentează un server, un NAS, un router și un switch, deasupra unei cronologii de la pana de curent la oprire."
coverCaption: "Măsoară sarcina, verifică autonomia și testează oprirea înainte de o pană de curent."
---

Un **UPS**, sau o sursă neîntreruptibilă de alimentare, îi oferă homelabului timp să salveze lucrul și să oprească sistemele în timpul unei pene de curent. Eticheta nu îți spune singură cât timp vor funcționa serverele. Ai nevoie de sarcina echipamentelor, limitele UPS-ului în wați și VA, o estimare a autonomiei la acea sarcină și o procedură de oprire testată.

## Idei principale

- **Măsoară sarcina:** Notează consumul normal și maxim în wați pentru fiecare dispozitiv care trebuie să rămână alimentat de baterie.
- **Verifică ambele valori:** UPS-ul trebuie să respecte cerințele echipamentelor conectate atât în wați, cât și în VA.
- **Consultă curba autonomiei:** Autonomia depinde de sarcină și de starea bateriei. Folosește o estimare specifică modelului.
- **Testează oprirea:** Verifică dacă semnalul UPS ajunge la fiecare gazdă și dacă toate se opresc înainte să se termine bateria.

## Înainte să începi

Ai nevoie de un wattmetru potrivit pentru alimentarea locală, de o listă cu dispozitivele și adaptoarele lor de alimentare și de specificațiile și curba autonomiei pentru fiecare model UPS avut în vedere. Pentru un test de oprire automată, ai nevoie și de o conexiune USB sau de administrare în rețea compatibilă și de software pentru fiecare gazdă. Rezervă timp pentru o măsurare la sarcină normală, o observație la sarcină mare și un test de mentenanță planificat. Este o activitate de nivel intermediar pentru un homelab, deoarece un test complet de oprire întrerupe serviciile.

Ghidul site-ului despre [protecția la supratensiune](/articles/protecting-your-tech_-the-best-surge-protectors/) tratează protecția împotriva vârfurilor de tensiune. [Prezentarea modelelor UPS](/articles/best-ups-models-for-uninterrupted-connectivity/) enumeră produse. Acest ghid tratează dimensionarea și verificarea sarcinii tale. Atât [ghidul Eaton de dimensionare UPS](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html), cât și [ghidul de cumpărare Schneider Electric](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/) diferențiază puterea de ieșire de autonomia bateriei.

> **Avertisment:** Folosește numai prizele și sarcinile aprobate de producătorul UPS-ului. Păstrează testul în limitele nominale ale UPS-ului. Un test real de oprire oprește laboratorul conectat.

## Măsoară ce trebuie să rămână pornit

Decide ce dispozitive trebuie să funcționeze până la oprire. Include hipervizorul, stocarea, switch-ul de rețea și routerul dacă o gazdă are nevoie de rețea pentru a primi semnalul de oprire. Lasă monitoarele, imprimantele și alte sarcini opționale în afara prizelor cu baterie, dacă planul tău nu le cere.

Măsoară la priză grupul de dispozitive pe care vrei să îl alimentezi de la baterie. Notează **wații în regim normal** și valoarea maximă observată în timpul unei activități reprezentative, cum ar fi pornirea gazdelor sau a mașinilor virtuale. Eticheta unei surse indică puterea nominală, nu consumul măsurat al sistemului. Verifică totuși etichetele dispozitivelor pentru limitele de intrare și curentul de pornire. Notează condițiile de măsurare în fișa ta.

| Dispozitiv | Wați în regim normal | Vârf observat în wați | Priză cu baterie? |
|---|---:|---:|---|
| **Router și switch** | 30 | 35 | Da |
| **NAS** | 60 | 90 | Da |
| **Server mic** | 90 | 135 | Da |
| **Total orientativ** | **180** | **260** | Trei dispozitive |

Valorile de mai sus sunt **orientative**, nu măsurători dintr-un anumit laborator. Sarcina ta se schimbă în funcție de discuri, GPU-uri, setările de alimentare și echipamentele conectate. Repetă măsurarea după modificări hardware importante.

## Compară wații cu VA

**Wații** descriu puterea activă folosită de echipamente. **Voltamperii (VA)** descriu puterea aparentă. Relația depinde de **factorul de putere**: wații împărțiți la factorul de putere dau VA. Eaton explică acest calcul în [ghidul său de dimensionare](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html). Nu considera o etichetă de 1000 VA echivalentă cu 1000 de wați. Verifică separat puterea nominală în wați a UPS-ului.

Pentru vârful orientativ de 260 W, o marjă de capacitate de 25% înseamnă **325 W**. Schneider Electric recomandă o putere de ieșire cu aproximativ [20% până la 25% peste sarcină](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/). Alege un UPS cu putere continuă în wați mai mare decât sarcina maximă planificată plus marja. Dacă știi factorul de putere combinat, împarte wații de vârf la acesta pentru a estima VA de vârf, apoi aplică aceeași marjă și valorii VA. În caz contrar, folosește un aparat de măsură potrivit sau selectorul producătorului pentru a stabili cerința VA și rezerva. Nu inventa un factor de putere pe care nu l-ai măsurat.

Marja de capacitate nu determină autonomia. Un UPS cu limită mare în wați, dar cu o baterie mică, poate susține sarcina doar pentru scurt timp. Înainte să alegi un model, verifică prizele, tipul de ștecher, tensiunea de intrare, interfața de comunicație și posibilitatea de înlocuire a bateriei.

## Stabilește o autonomie-țintă

Notează cât timp îi trebuie laboratorului să se oprească în siguranță. Include timpul pentru ca alerta de oprire să ajungă la gazde, oprirea mașinilor virtuale, finalizarea scrierilor în stocare și oprirea ieșirii UPS-ului. Adaugă rezervă pentru o oprire lentă și o baterie mai veche. Un laborator care trebuie să funcționeze prin pene scurte are nevoie de altă țintă decât unul care trebuie doar să se închidă corect.

Ca **exemplu**, presupune că o oprire testată durează 6 minute și alegi o rezervă de 5 minute. Autonomia necesară la sarcina estimată este de cel puțin 11 minute. Este un exemplu de planificare, nu un prag universal. Compară ținta cu curba de autonomie sau selectorul modelului candidat la **sarcina ta normală și maximă măsurată**, apoi reevaluează rezultatul pe măsură ce bateria îmbătrânește. [Selectorul UPS Schneider Electric](https://www.se.com/us/en/work/products/tools/ups-selector/) estimează autonomia pe baza sarcinii introduse și a specificațiilor modelului. Eaton indică și date specifice modelelor în [ghidul pentru UPS-uri desktop](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

Copiază această **fișă de lucru** pentru laboratorul tău. Completează rândurile dispozitivelor folosind citirile wattmetrului. Adună wații normali și cei de vârf, adaugă marja aleasă la totalul de vârf și aplică aceeași marjă valorii VA de vârf măsurate sau calculate. Compară ambele rezultate cu un UPS candidat. Dacă folosești selectorul producătorului, notează rezultatul de dimensionare VA și rezerva. Estimează autonomia din curba modelului. Completează rândurile privind timpii și recuperarea în timpul testului.

| Câmp | Rezultatul tău |
|---|---|
| **Dispozitive și prize cu baterie** | Numele dispozitivelor și priza atribuită fiecăruia |
| **Wați normali pe dispozitiv și total** | Valori măsurate și sumă |
| **Wați maximi pe dispozitiv și total** | Cele mai mari valori observate și suma |
| **Factor de putere măsurat sau specificat** | Valoare și sursă sau „necunoscut” |
| **VA de vârf măsurate sau calculate** | Wații de vârf împărțiți la factorul de putere combinat, dacă este cunoscut |
| **Marja de capacitate** | Procentul ales și wații/VA după aplicarea marjei |
| **Specificațiile UPS-ului candidat** | Model, wați și VA la ieșire și limitele prizelor |
| **Ținta și estimarea curbei de autonomie** | Minute necesare și estimarea modelului la sarcina ta |
| **Orele alertei și opririi** | Ora alertei de baterie și oprirea ultimei gazde |
| **Rezultatul recuperării** | Pornirea gazdelor, stocarea, aplicațiile și monitorizarea |

Dacă factorul de putere este necunoscut, folosește selectorul producătorului sau măsoară puterea aparentă cu un aparat potrivit. Nu raporta VA calculat pe baza unui factor ghicit. Fișa este completă numai când modelul respectă ambele limite de ieșire, iar autonomia estimată depășește ținta de oprire.

> **Rezultatul așteptat:** Fișa numește dispozitivele conectate, sarcinile măsurate, limitele UPS-ului în wați și VA, ținta de autonomie și estimarea specifică modelului.

## Planifică oprirea automată

Un UPS menține temporar echipamentele alimentate. Gazda are în continuare nevoie de un **semnal de oprire**. Verifică dacă UPS-ul oferă USB, o placă de management de rețea sau o altă interfață acceptată. Asigură-te că fiecare gazdă care trebuie oprită are o cale compatibilă de monitorizare. Eaton menționează că multe modele acceptă comunicații USB sau de rețea pentru o [oprire controlată a unui NAS sau server](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

Într-un laborator Linux cu **Network UPS Tools (NUT)**, driverul citește UPS-ul, `upsd` îi distribuie starea, iar `upsmon` inițiază oprirea gazdei când alimentarea devine critică. O gazdă conectată direct la un UPS USB sau serial rulează de regulă driverul, `upsd` și `upsmon` în modul **Primary**. Celelalte gazde rulează `upsmon` în modul **Secondary** și se conectează la acel server. Un UPS gestionat prin rețea are nevoie de un driver compatibil și de o configurație Primary specifică modelului. [Ghidul de topologie NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s02.html) explică rolurile. Configurează routerul și switch-ul astfel încât gazdele de monitorizare să rămână conectate pe baterie. Limitează comanda de oprire și permisiunile asociate la administratori.

Înainte de testul de oprire, verifică dacă driverul raportează starea actuală. Înlocuiește `myupsname` cu numele UPS-ului din configurația NUT:

```bash
upsc myupsname@localhost ups.status
```

[Ghidul de configurare NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) așteaptă `OL` pentru alimentarea normală de la rețea și descrie `OB` pentru funcționarea pe baterie. Rulează verificarea stării pe fiecare gazdă care monitorizează UPS-ul și folosește numele corect al serverului pentru clienții la distanță. O valoare învechită sau lipsă înseamnă că trebuie reparată calea semnalului înainte de test.

Notează **ordinea opririi**. De exemplu, oprește mai întâi VM-urile aplicațiilor, apoi clienții de stocare și la final hipervizorul și NAS-ul. Verifică dacă fiecare serviciu și sistem de fișiere revine normal după restabilirea alimentării. Oprirea reușită a gazdei fără recuperarea sănătoasă a aplicațiilor nu este un rezultat complet.

## Testează fără presupuneri

Începe cu o **simulare** pe gazda unde este configurat driverul UPS-ului. NUT descrie `upsdrvctl -t shutdown` ca previzualizare a secvenței de oprire a driverului; comanda nu apelează driverele și nu întrerupe alimentarea:

```bash
upsdrvctl -t shutdown
```

Această **simulare a driverului** nu demonstrează că o alertă de întrerupere ajunge la fiecare gazdă. Verifică fiecare serviciu de monitorizare și jurnalele lui. Într-o fereastră de mentenanță, [instrucțiunile NUT pentru testarea opririi](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) descriu un test forțat cu `upsmon -c fsd` pe gazda NUT primară. Acest **test FSD** pornește o secvență reală de oprire. Indicatorul FSD rămâne activ până la repornirea `upsd`. După revenirea sistemelor, confirmă că `upsd` a repornit și că starea nu mai afișează FSD înainte să te bazezi din nou pe monitorizare. Citește [manualul actual upsmon](https://networkupstools.org/docs/man/upsmon.html), pregătește o cale de recuperare și rulează testul numai după ce ai salvat lucrul și ai anunțat utilizatorii laboratorului.

Pentru un **test controlat al evenimentului de baterie**, urmează mai întâi procedura producătorului UPS-ului folosind sarcini necritice. Testul la sarcină mică verifică livrarea semnalului, dar nu demonstrează autonomia laboratorului. Mai târziu, într-o fereastră de mentenanță, testează o sarcină pe baterie reprezentativă pentru cea planificată. Cineva trebuie să urmărească UPS-ul și să poată restabili alimentarea de la rețea dacă rezerva scade. Notează sarcina afișată de UPS, ora când anunță funcționarea pe baterie, momentul când începe oprirea fiecărei gazde și ora când se oprește ultima. Verifică dacă bateria nu se epuizează înainte de oprirea gazdelor. După revenirea alimentării, verifică pornirea gazdelor, starea aplicațiilor, integritatea stocării și starea monitorizării. NUT consideră secvența reușită dacă sistemul de operare se oprește înainte de terminarea bateriei și își reia activitatea când revine alimentarea.

| Verificare | Ce să înregistrezi |
|---|---|
| **Calea semnalului** | Evenimentul UPS este vizibil pe fiecare gazdă de monitorizare |
| **Timpul de oprire** | Ultima gazdă s-a oprit înainte de epuizarea bateriei |
| **Recuperare** | Gazdele, stocarea și aplicațiile pornesc corect |
| **Capacitate** | Sarcina UPS-ului rămâne în limitele de wați și VA |

## Depanare

- **Alarmă de suprasarcină UPS:** Elimină sarcinile opționale. Compară sarcina maximă măsurată cu ambele limite ale UPS-ului și cu limitele prizelor modelului.
- **Autonomie mai scurtă decât se aștepta:** Verifică sarcina actuală, vechimea bateriei, datele modelului și rezultatele recente ale testului bateriei. Nu extrapola liniar doar din VA.
- **O gazdă rămâne pornită:** Verifică serviciul ei de monitorizare, calea de rețea, permisiunile de oprire și jurnalele.
- **Gazdele se opresc, dar nu revin:** Verifică comportamentul ieșirii UPS-ului la revenirea alimentării, setarea firmware pentru revenirea curentului și [considerațiile NUT despre cursele de alimentare](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html).
- **Simularea trece, dar testul de întrerupere eșuează:** Previzualizarea driverului verifică o cale mai restrânsă. Inspectează livrarea evenimentului și ordinea reală de oprire a gazdelor.

## Pașii următori

Păstrează fișa cu inventarul homelabului. Măsoară din nou sarcina după adăugarea de hardware și repetă testul de oprire după schimbări ale UPS-ului, software-ului de monitorizare, politicii de pornire a gazdelor sau stivei de stocare. Verifică separat planul de backup și restaurare. Bateria protejează intervalul de oprire, iar un [backup de homelab testat](/articles/what-is-a-homelab-and-should-you-have-one/) îți protejează datele în alte situații de defectare.

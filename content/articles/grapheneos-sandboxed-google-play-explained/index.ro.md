---
title: "Sandboxed Google Play pe GrapheneOS, explicat"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Află ce schimbă Sandboxed Google Play pe GrapheneOS, când ajută un profil separat și cum se leagă conturile, notificările și compatibilitatea aplicațiilor."
genre: ["Confidențialitate", "Securitate mobilă", "Sursă deschisă"]
tags: ["GrapheneOS", "sandboxed Google Play", "Google Play services", "Google Play Store", "confidențialitate Android", "securitate Android", "sandbox pentru aplicații", "cont Google", "profiluri GrapheneOS", "profilul proprietarului", "profiluri de utilizator", "profil de lucru", "compatibilitatea aplicațiilor", "notificări push", "Firebase Cloud Messaging", "permisiuni aplicații", "confidențialitate Pixel", "instalare Google Play", "confidențialitate mobilă", "GrapheneOS App Store"]
cover: "/img/cover/grapheneos-sandboxed-google-play-explained.webp"
coverAlt: "Ecranul unui smartphone afișează aplicații în compartimente transparente separate, inclusiv simbolul colorat al unui magazin de aplicații."
coverCaption: ""
---

**Sandboxed Google Play** îți permite să instalezi componentele oficiale Google Play pe GrapheneOS ca aplicații obișnuite. Acestea rulează fără privilegiile de sistem pe care Google Play le primește de obicei în sistemul de operare standard. Instalarea este opțională. [Prezentarea funcțiilor GrapheneOS](https://grapheneos.org/features#sandboxed-google-play).

## Idei principale

- **Înțelege izolarea:** distinge permisiunile aplicațiilor de activitatea conturilor online.
- **Păstrează împreună dependențele:** pune aplicația dependentă și componentele Play în același profil.
- **Testează comportamentul:** verifică notificările în fundal și fluxurile de lucru esențiale.
- **Fă un plan:** notează profilurile, conturile și cerințele aplicațiilor alese.

## Înainte să începi

**Public:** utilizatori GrapheneOS care decid dacă instalează Google Play și unde îl plasează. **Cerințe:** un dispozitiv compatibil cu GrapheneOS actualizat și acces la conturile esențiale. Instalarea sistemului de operare este descrisă în [ghidul de instalare GrapheneOS](/guides/how-to-install-graphine-os/).

**Timp estimat:** 20–30 de minute pentru inventarul inițial al aplicațiilor și verificări, apoi utilizarea zilnică obișnuită pentru evaluarea fiabilității notificărilor. **Dificultate:** începător. Începe cu o aplicație reprezentativă înainte să reorganizezi telefonul.

## Ce schimbă sandboxul

**Sandboxul aplicațiilor** Android separă resursele aplicațiilor prin protecțiile sistemului de operare. O aplicație nu primește acces nelimitat la fișierele private ale altei aplicații. Protecția se aplică atât codului nativ, cât și codului care rulează în mediul gestionat Android. [Documentația sandboxului aplicațiilor Android](https://source.android.com/docs/security/app-sandbox).

GrapheneOS adaugă un **strat de compatibilitate**, astfel încât componentele oficiale Play să funcționeze în limitele obișnuite. Aplicațiile din același profil pot comunica în continuare prin metode acceptate și cu acord reciproc. Sandboxul limitează privilegiile, dar nu împiedică orice schimb intenționat între aplicații. [Proiectarea Sandboxed Google Play](https://grapheneos.org/features#sandboxed-google-play).

| Aspect | Semnificație practică |
|---|---|
| **Fișierele private ale aplicațiilor** | Instalarea Play nu oferă acces nelimitat la datele altor aplicații |
| **Permisiuni** | Analizează accesul solicitat ca pentru orice altă aplicație |
| **Funcții conectate la Google** | O aplicație care alege un serviciu Google continuă să comunice cu el |
| **Activitatea contului** | Autentificarea într-un serviciu rămâne o decizie separată de confidențialitate |

**Sandboxul și confidențialitatea contului** răspund la întrebări diferite. Sandboxul limitează accesul local. Nu șterge informațiile pe care le trimiți intenționat unui serviciu online. De exemplu, autentificarea într-o aplicație de cumpărături îți identifică în continuare contul pentru operatorul serviciului.

## Separă trei decizii de confidențialitate

**Accesul local, folosirea serviciilor și identitatea** sunt subiecte distincte. Dacă o aplicație cere acces la contacte și autentificarea într-un cont, analizează fiecare solicitare separat:

| Decizie | Întrebare |
|---|---|
| **Permisiune locală** | Are această funcție nevoie de contactele, microfonul sau locația mea? |
| **Dependență de un serviciu** | Ce funcție depinde de Play services? |
| **Identitate online** | Cu ce cont asociez această activitate? |

**Exemplu practic:** un cont de cumpărături conține deja adresa ta de livrare. Mutarea aplicației într-un alt profil nu schimbă adresa păstrată de comerciant. Refuzul accesului la contacte răspunde la altă întrebare despre datele disponibile pe telefon.

**Obiectiv de confidențialitate:** notează expunerea concretă pe care vrei să o reduci. „Nu permite acestei aplicații accesul la contactele mele personale” poate fi testat. „Fă acest cont anonim” necesită decizii care depășesc alegerea profilului.

## Profilul proprietarului sau profil separat?

**Instalarea în profilul proprietarului** este o opțiune simplă și acceptată. Google Play rămâne izolat acolo. Un profil separat de utilizator sau de lucru îți permite să alegi grupul de aplicații care are acces la Play. [Recomandări de instalare GrapheneOS](https://grapheneos.org/usage#sandboxed-google-play-installation).

| Prioritatea ta | Configurație de început | Compromis |
|---|---|---|
| **Utilizare zilnică simplă** | Păstrează aplicațiile necesare și Play în profilul Proprietar | Play este disponibil aplicațiilor care colaborează în acest profil |
| **Separarea aplicațiilor dependente de Google** | Instalează-le împreună în alt profil | Mai multă administrare a profilurilor |
| **Evitarea serviciilor Google** | Începe fără Play | Verifică dependențele fiecărei aplicații |

**Plasarea în profil** contează mai mult decât instalarea aceleiași componente peste tot. FAQ-ul GrapheneOS explică limitarea disponibilității Play la profilurile selectate. Multe aplicații funcționează fără Play sau au nevoie de el doar pentru o parte dintre funcții. [FAQ despre serviciile Google](https://grapheneos.org/faq#google-services).

*Folosește un profil separat când accesul selectiv la Play rezolvă o cerință concretă pe care ai identificat-o.*

## Înțelege activitatea profilurilor

**Un profil secundar de utilizator** are propriile instanțe de aplicații și propriile date. Trecerea la alt utilizator și încheierea sesiunii utilizatorului anterior sunt acțiuni diferite. **Încheie sesiunea** oprește aplicațiile din profilul secundar și readuce stocarea criptată în repaus. [FAQ GrapheneOS despre criptare și profiluri](https://grapheneos.org/faq#encryption).

**Redirecționarea notificărilor** poate afișa utilizatorului activ notificările unui utilizator care rulează în fundal. Nu menține activă o sesiune încheiată. [Funcțiile profilurilor de utilizator GrapheneOS](https://grapheneos.org/features).

| Starea profilului | Condiție de livrare |
|---|---|
| **Activ** | Testează livrarea în acest profil |
| **Rulează în fundal** | Verifică redirecționarea către utilizatorul activ |
| **Sesiune încheiată** | Aplicațiile din acest profil sunt oprite |

Pentru **o aplicație de mesagerie folosită zilnic**, decide dacă este esențial să primești mesaje când folosești profilul Proprietar. O configurație care cere încheierea frecventă a sesiunilor nu se potrivește cu livrarea continuă în fundal. Evaluează acest compromis înainte să muți istoricul principal al conversațiilor.

## Instalare și conturi

Deschide **GrapheneOS App Store** integrat, selectează **Google Play services** și instalează-l. Se instalează și Play Store, care depinde de el. Lasă App Store să gestioneze aceste componente. Exclude Play services de la optimizarea bateriei pentru a asigura funcții de fundal fiabile, precum notificările push. [Instrucțiuni oficiale de instalare](https://grapheneos.org/usage#sandboxed-google-play-installation).

**Autentificarea cu un cont Google** este opțională pentru funcțiile care nu depind de un cont. Instalarea aplicațiilor prin Play Store necesită autentificare. Instalările mai vechi includ și Google Services Framework, pe care proiectul recomandă să-l păstrezi. Urmează instrucțiunile actuale în locul unei liste vechi cu trei pachete.

## Testează mai întâi o aplicație

Folosește o **aplicație reprezentativă cu risc redus** pentru a verifica aranjamentul de profiluri propus. Păstrează la îndemână metodele existente de recuperare a contului pe tot parcursul testului.

1. **Alege un profil:** decide unde va sta aplicația înainte să-i instalezi dependențele.
2. **Instalează Play:** urmează pașii oficiali de mai sus în acest profil.
3. **Instalează aplicația:** folosește o sursă de distribuție de încredere și finalizează configurarea inițială.
4. **Analizează solicitările:** aprobă permisiunile potrivite funcției testate.
5. **Testează o funcție:** trimite un mesaj, deschide o hartă sau efectuează o altă acțiune reversibilă.
6. **Notează rezultatul:** înregistrează versiunile aplicației și sistemului, profilul și operația exactă.

**Dovadă așteptată:** o descriere repetabilă, de exemplu „mesajul de test a ajuns cu ecranul blocat și profilul activ”. Nu nota doar „funcționează”, fiindcă nu precizează funcția și condițiile testate.

## Depanează notificările lipsă

**Notificările push** depind de implementarea aplicației. Unele aplicații mențin propria conexiune în fundal. Altele folosesc Firebase Cloud Messaging de la Google. Faptul că o aplicație se deschide nu dovedește că notificările funcționează după blocarea telefonului. [FAQ GrapheneOS despre notificări](https://grapheneos.org/faq#notifications).

**Verifică condițiile de livrare** înainte să modifici permisiunile mai multor aplicații:

| Simptom | Cum restrângi verificarea |
|---|---|
| **Mesajele apar doar după deschiderea aplicației** | Verifică metoda de livrare în fundal și setările bateriei |
| **Livrarea funcționează doar în profilul aplicației** | Verifică activitatea profilului și redirecționarea notificărilor |
| **Nu se livrează nimic după Încheie sesiunea** | Pornește profilul secundar înainte de următorul test |
| **Notificarea ajunge fără sunet** | Verifică canalul de notificare și setările de sunet ale aplicației |

**Canalele de notificare** grupează comportamentul notificărilor unei aplicații, inclusiv importanța și sunetul. Android pune la dispoziția utilizatorului controale pentru canale. [Documentația Android despre canalele de notificare](https://developer.android.com/develop/ui/compose/notifications/channels).

**Repetă testul schimbând o singură condiție:** păstrează același dispozitiv expeditor și același tip de mesaj, dar schimbă starea profilului receptor. Notează „activ”, „rulează în fundal” sau „sesiune încheiată” pentru fiecare rezultat. Astfel poți deosebi o problemă a ciclului de viață al profilului de una a configurării notificărilor.

## Evaluează fluxurile de lucru esențiale

Înainte să te bazezi pe o configurație nouă, efectuează un scurt **test personal de acceptare**:

| Flux de lucru | Verificare pe dispozitiv |
|---|---|
| **Mesagerie** | Primește un mesaj cu ecranul blocat |
| **Acces la cont** | Autentifică-te și finalizează al doilea factor solicitat |
| **Servicii bancare sau plăți** | Testează funcția exactă necesară, inclusiv verificările dispozitivului |
| **Navigare** | Obține locația cu permisiunile alese |

**Pornirea unei aplicații** este doar prima verificare. Când depanezi, notează versiunile aplicației și GrapheneOS și operația eșuată. Acest articol oferă un cadru de decizie, nu o listă de compatibilitate testată.

**Decizia de migrare:** păstrează metoda veche de acces până când fiecare operație esențială trece testul. O aplicație de mesagerie și una bancară au criterii de acceptare diferite. Livrarea unui mesaj nu spune nimic despre verificările contului sau dispozitivului din altă aplicație.

**Reverifică după actualizări GrapheneOS sau ale aplicațiilor.** Plasarea în profil, permisiunile, canalele de notificare și starea sesiunii definesc în continuare testul. Notează versiunea lângă fiecare rezultat, ca schimbarea notificărilor sau a autentificării să nu ducă la o concluzie nefondată despre confidențialitate.

Pentru **o autentificare de serviciu**, testează întregul proces și al doilea factor cerut. Pentru o aplicație de călătorie, testează funcția pe care te aștepți s-o folosești departe de casă. Alege acțiuni reprezentative, fără achiziții inutile sau schimbări ale securității contului.

## Creează planul aplicațiilor

Completează acest **inventar** pentru cele mai importante cinci aplicații. Rândurile sunt sugestii de verificare, nu afirmații de compatibilitate pentru produse specifice:

| Categoria aplicației | Cerința de notat | Dovada de colectat |
|---|---|---|
| **Mesagerie** | Livrare în fundal și alegerea profilului | Test cu ecranul blocat și profilul în fundal |
| **Acces la serviciu** | Autentificarea și al doilea factor necesare | Autentificare finalizată |
| **Navigare** | Permisiunea de localizare și nevoile offline | Un traseu în condițiile așteptate |
| **Servicii bancare** | Operații esențiale acceptate | Rezultate pentru fiecare funcție necesară |
| **Cumpărături** | Acces la cont și date locale | Revizuirea permisiunilor și utilizarea normală a contului |

**Notează o decizie** pentru fiecare rând: profil ales, dependența de Play, cerința de cont, permisiunile aprobate și alternativa. Păstrează dependențele necunoscute marcate ca necunoscute până ai dovezi. Astfel eviți instalarea altor componente doar fiindcă i-au trebuit unei alte aplicații.

**Exercițiu de verificare:** o aplicație funcționează cât timp profilul secundar este activ, apoi nu mai primește mesaje după încheierea sesiunii. Mai întâi repornește profilul și testează din nou. Accesul la contacte nu ar rezolva o sesiune oprită.

**Criteriu de finalizare:** planul explică de ce fiecare aplicație se află în profilul ales și ce test susține încrederea în ea. Revizuiește rândul relevant după o actualizare care îi schimbă comportamentul.

## Pașii următori

Dacă nu ai instalat sistemul, folosește [ghidul de instalare GrapheneOS](/guides/how-to-install-graphine-os/). Apoi alege o configurație de profiluri și testează aplicațiile esențiale înainte să adaugi profiluri sau să schimbi setări generale de permisiuni.

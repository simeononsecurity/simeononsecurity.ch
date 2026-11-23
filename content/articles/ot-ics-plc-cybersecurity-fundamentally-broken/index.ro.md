---
title: "De ce securitatea cibernetică OT, ICS și PLC este în continuare deficitară"
draft: false
toc: true
date: 2026-06-26
lastmod: 2026-11-22
description: "Află de ce controalele de securitate OT rămân în urma proiectării învechite, a constrângerilor operaționale și a căilor reale de atac."
tags: ["securitate OT", "securitate ICS", "securitate PLC", "securitate IoT", "securitate cibernetică industrială", "securitate SCADA", "NIST 800-82", "IEC 62443", "NERC CIP", "tehnologie operațională", "infrastructură critică", "senzori analogici", "izolare de rețea", "sisteme vechi", "opinie despre securitatea cibernetică", "sisteme de control industrial", "SCADA", "Stuxnet", "securitatea sistemelor de control", "securitate ciberfizică", "securitatea lanțului de aprovizionare", "lanțul de aprovizionare OT"]
cover: "/img/cover/ot-ics-plc-cybersecurity-fundamentally-broken.webp"
coverAlt: "Ilustrație care contrastează un PLC vechi cu funcții analogice și un controler modern cu funcții de securitate cibernetică și interfețe digitale, pe un fundal întunecat."
coverCaption: ""
---

Am petrecut suficient timp în medii industriale ca să spun direct: **majoritatea programelor de securitate cibernetică OT, ICS și PLC sunt teatru**. Ele produc documentație de conformitate. Nu produc securitate. Infrastructura critică este atacată tocmai prin spațiul dintre cele două.

Nu este un atac la adresa celor care redactează standarde. **NIST SP 800-82 Rev 3**, **IEC 62443** și **NERC CIP** sunt documente solide din punct de vedere tehnic. Problema nu este ghidul. *Problema este sistemul asupra căruia se aplică.*

## Sistemele au fost construite să funcționeze, nu să fie securizate

**PLC-urile, sistemele SCADA, sistemele de control distribuit (DCS) și echipamentele industriale IoT vechi** au fost proiectate cu un singur scop: să funcționeze fiabil mult timp. **Disponibilitatea era singurul obiectiv de proiectare care merita discutat.** Confidențialitatea, integritatea, autentificarea și înregistrarea activităților nu erau cerințe. În multe cazuri, nici măcar nu erau concepte luate în calcul atunci când au fost proiectate aceste sisteme.

NIST SP 800-82 Rev 3 (2023) recunoaște acest lucru. Descrie mediile OT ca având *„cerințe unice de performanță, fiabilitate și siguranță”*, în care *„securitatea nu poate interfera cu funcționarea sistemului”*. Citește din nou. **Principalul document de orientare pentru securitatea tehnologiei operaționale recunoaște explicit că securitatea trece pe planul al doilea.** Nu este un defect al documentului. Este o descriere exactă a mediului.

Nu poți aplica controlul accesului bazat pe roluri unui PLC care nu cunoaște rolurile utilizatorilor. Nu poți instala actualizări de firmware pe echipamente al căror producător nu mai există. **Protocoalele seriale vechi, inclusiv Modbus RTU și Profibus DP, nu oferă autentificare nativă.** Ele transmit comenzi și date oricui le solicită. Nu verifică cine face solicitarea.

*Ghidul este corect. De multe ori, sistemele nu îl pot urma.* Sunt două probleme diferite.

## Există două categorii complet diferite de sisteme OT

**PLC-urile vechi, de la anii 1980 până la începutul anilor 2000**, au fost proiectate pentru funcționare izolată, cu acces exclusiv fizic. Rulează sisteme de operare proprietare. Sunt adesea administrate de stații de lucru pentru inginerie care se conectează și la rețelele corporative. Configurațiile sunt stocate în formate fără verificarea integrității. Aceste sisteme reprezintă o parte importantă a infrastructurii instalate în tratarea apei, producerea energiei, fabricație și transport.

**Controlerele moderne cu funcții de securitate sunt diferite.** Siemens, Schneider, Rockwell, Beckhoff și Phoenix Contact livrează acum platforme cu pornire securizată, firmware semnat, control al accesului bazat pe roluri, identitate susținută de TPM și comunicații criptate. EtherNet/IP CIP Security, PROFINET Security Class și OPC UA cu autentificare sunt funcții disponibile pe hardware-ul actual.

Nu minimalizez ingineria modernă de securitate OT. Progresul este real. **Problema este că majoritatea infrastructurii instalate nu este modernă.** Când oamenii spun „securitate cibernetică OT”, de obicei descriu încercarea de a securiza un controler programabil vechi de 20 de ani cu un cadru de securitate cibernetică scris în 2023. Despre această diferență vorbesc.

## Ce funcționează în practică

**Securitatea fizică și izolarea rețelei sunt cele mai fiabile controale disponibile pentru mediile OT vechi.** Toate cadrele majore de securitate ICS spun același lucru. IEC 62443 împarte mediile OT în zone de securitate cu conducte definite. Scopul este ca deplasarea laterală să treacă prin limite controlate, nu să traverseze o rețea plată.

Izolarea rețelei reduce considerabil suprafața de atac bazată pe rețea. Nu elimină toate riscurile. Mediile detașabile, accesul persoanelor din interior, laptopurile de mentenanță, conexiunile temporare de inginerie și compromiterea lanțului de aprovizionare sunt căi documentate spre sisteme fără expunere la rețea. **Stuxnet**, care a ajuns la instalațiile iraniene de centrifugare izolate de rețea prin unități USB infectate, este exemplul clasic. *Izolarea rețelei este necesară. Nu este suficientă.*

**Monitorizarea umană a parametrilor procesului fizic** rămâne unul dintre cele mai fiabile mecanisme de detectare. Un operator instruit care urmărește în timp real presiunea, temperatura și debitul observă lucruri pe care niciun sistem de detectare a intruziunilor nu le vede, deoarece IDS-ul nu poate verifica dacă valoarea digitală corespunde realității fizice.

Controale care reduc riscul în contexte potrivite:

- **Diodele de date** permit ieșirea telemetriei fără a permite conexiuni de intrare
- **Listele de aplicații permise** pe stațiile HMI limitează ce se execută pe mașinile cu acces la sistemele de control
- **Platformele pasive de detectare a anomaliilor** de la Claroty, Dragos și Nozomi analizează traficul fără să atingă comunicațiile planului de control
- **Segmentarea rețelei** între zonele OT încetinește deplasarea laterală fără să impună o izolare fizică totală
- **Principiile zero trust**, menționate în NIST SP 800-82 Rev 3, adaugă cerințe de verificare pentru fiecare sesiune unor arhitecturi OT moderne

*Niciunul dintre aceste controale nu rezolvă constrângerile fundamentale de proiectare. Ele reduc riscul la marginile sistemelor care nu au fost construite pentru asta.*

## Semnalele analogice nu pot fi autentificate

**Buclele de curent de 4-20 mA, semnalele de 0-10 V, ieșirile termocuplurilor și citirile RTD se transmit ca semnale electrice variabile.** Semnalul fizic nu are niciun mecanism de verificare a autenticității. Oricine aplică semnalul corect pe fir este considerat de încredere.

Stuxnet a demonstrat acest lucru concret. Atacul a manipulat logica PLC care rula pe controlerele Siemens S7 și, simultan, a redat interfețelor operatorilor date normale ale procesului înregistrate anterior. **Operatorii vedeau pe ecrane valori normale, în timp ce centrifugele erau împinse peste limitele de funcționare.** Înșelătoria a durat suficient pentru a provoca daune fizice care păreau o defecțiune a echipamentului, nu un atac.

Interferențele electromagnetice de la cablurile de alimentare, variatoarele de frecvență, fulgere și împământarea incorectă corup măsurătorile analogice în funcționarea normală. IEC 61000 există din acest motiv. Instalațiile industriale folosesc cabluri ecranate, împământare adecvată, filtre și separare fizică pentru a gestiona aceste interferențe.

Dispozitivele inteligente moderne de teren convertesc intern măsurătorile analogice în format digital înainte de a le transmite prin HART-IP, WirelessHART, EtherNet/IP CIP Security sau OPC UA. Hardware-ul modern permite comunicații digitale autentificate la nivelul dispozitivului. **Firul analogic de 4-20 mA care conectează un transmițător vechi la o intrare PLC veche nu oferă autentificare și nu va oferi niciodată.** O parte importantă a instrumentației instalate folosește încă acest fir.

## Validarea senzorilor este un control de siguranță funcțională, nu de securitate cibernetică

Sistemele de siguranță a proceselor folosesc **votarea redundantă a senzorilor**. O configurație 2 din 3, în care doi senzori indică 230 PSI și unul indică 14 PSI, semnalează valoarea atipică. Aceasta oferă reziliență limitată la manipularea unui singur senzor. *Este un control de inginerie a siguranței funcționale, nu un control de securitate cibernetică.*

PLC-urile standard nu validează criptografic intrările analogice. Un generator de semnal conectat la buclă nu se deosebește de un transmițător legitim. PLC-ul citește curentul și acționează pe baza lui.

**Sistemele instrumentate de siguranță trebuiau să fie ultima linie independentă de apărare.** În 2017, **TRITON** (cunoscut și ca **TRISIS**) a vizat unitățile SIS Triconex ale Schneider Electric cu scopul specific de a dezactiva acel nivel. Atacatorii au ajuns la sistemul de siguranță prin rețeaua stațiilor de inginerie. *Independența nivelului depindea de o separare a rețelei care nu fusese menținută.*

IEC 62443-3-3, IEC 62443-4-2 și coordonarea cu siguranța funcțională conform IEC 61511 reflectă acum această lecție. Ani la rând, grupuri diferite au tratat siguranța proceselor și securitatea cibernetică drept discipline separate. **TRITON a demonstrat în practică ceea ce analize independente susțineau în teorie:** un atacator care neutralizează sistemul de siguranță înainte să declanșeze condiția periculoasă elimină ultimul control care previne consecințele fizice.

## Lanțul de aprovizionare este o cale de atac pe care probabil o ignori

**Majoritatea programelor de securitate OT se concentrează pe arhitectura rețelei. Multe compromiteri OT recente au folosit puncte de intrare pe care arhitectura rețelei nu le oprește.**

Riscurile lanțului de aprovizionare OT includ:

- **Integritatea firmware-ului înainte de instalare**, mai ales dacă echipamentul ajunge din fabrică sau de la distribuitor cu firmware neverificat
- **Sesiunile de acces la distanță ale furnizorilor**, care rămân expuneri persistente în locațiile dependente de suportul producătorului
- **Stațiile de lucru de inginerie** conectate atât la rețeaua corporativă, cât și la rețeaua OT, adesea din comoditate operațională
- Lipsa **listelor de materiale software (SBOM)** pentru majoritatea implementărilor OT vechi, ceea ce face aproape imposibilă urmărirea componentelor software
- **Contractorii de mentenanță** care aduc laptopuri și unități USB în medii operaționale izolate
- **Suportul pentru actualizări de firmware semnate**, care lipsește pe majoritatea platformelor mai vechi

NIST SP 800-82 Rev 3 are secțiuni dedicate dependențelor de furnizori și accesului terților. *Dacă izolarea ta de rețea este intactă pe interior, dar furnizorul echipamentului menține un portal persistent de acces la distanță în rețeaua de inginerie, nu ai o rețea izolată. Ai o breșă cu o ușă controlată de altcineva.*

## Securizarea sistemelor vechi costă mai mult decât ar trebui

Fiecare program PLC este scris special pentru un anumit proces. Logica unui sistem de control al supratensiunii dintr-o rafinărie diferă complet de cea a unei secvențe de clorinare într-o stație de tratare a apei sau de cea a unui regulator de turbină. Nu este o alegere. Procesele fizice diferă.

**Securizarea sistemelor OT vechi costă adesea mai mult decât se estimează** din cauza cerințelor de validare inginerească, a timpilor de nefuncționare necesari, a limitărilor de suport ale furnizorilor, a lacunelor din documentație și a ciclurilor de testare care depășesc estimările inițiale. În unele cazuri cu hardware fără suport de la furnizor, costul securizării se apropie de costul înlocuirii sistemului sau îl depășește.

**Conformitatea NERC CIP pentru activele cibernetice ale sistemului electric la scară largă costă fiecare companie de utilități milioane de dolari anual.** Un sondaj din 2019 al American Public Power Association a documentat variații mari ale costurilor, cu o povară disproporționată pentru companiile mai mici. Multe sisteme de apă și companii mici nu intră sub cerințele NERC CIP și nu au obligații comparabile de conformitate.

## Sistemele trebuie înlocuite

**Înlocuirea sistemelor OT vechi este răspunsul corect.** În instalațiile mari, aceasta înseamnă zeci de milioane de dolari, perioade lungi de tranziție și riscul de a codifica greșit cunoștințe operaționale complexe în timpul migrării. Sunt costuri și riscuri reale.

Îndrumările din industrie prin CISA și ICS-CERT recomandă aplicarea unor controale compensatorii în timp ce avansează planificarea înlocuirii. Este o reacție rațională la constrângeri. *Spus direct, se recunoaște că securitatea completă nu se poate obține pe echipamentele vechi. Aplică acele controale care se potrivesc și planifică înlocuirea lor.*

**Realitatea practică este că multe dintre aceste sisteme vor rămâne în funcțiune timp de decenii.** Este o problemă de finanțare și politici. Comunitatea tehnică a explicat clar ce trebuie făcut. Bugetele operaționale și calendarele de înlocuire nu au ținut pasul.

## Conectarea sistemelor OT la rețea înrăutățește adesea lucrurile

Multe organizații au adăugat acces la distanță și funcții de monitorizare în medii OT izolate inițial. Argumentul operațional este simplu: vizibilitatea la distanță reduce timpul de răspuns, iar furnizorii oferă suport mai rapid printr-o conexiune la distanță. **Consecința de securitate este că sistemele izolate, fără suprafață de atac la distanță, au acum una.**

**Incidentul din 2021 de la stația de tratare a apei din Oldsmar** s-a produs printr-o conexiune de acces la distanță TeamViewer. Atacatorul a modificat setările de dozare a hidroxidului de sodiu printr-un instrument legitim de acces la distanță, adăugat din comoditate. **Incidentul Colonial Pipeline din 2021** a început cu compromiterea unei rețele IT. Operatorul a oprit preventiv operațiunile conductei OT deoarece nu putea confirma că rețeaua OT nu fusese afectată. *Atacul nu a încălcat direct rețeaua OT. Incertitudinea privind o posibilă compromitere a cauzat oprirea.*

Adăugarea conectivității la rețea la sistemele OT vechi pentru beneficii operaționale, fără proiectarea acesteia conform unor standarde adecvate, **produce adesea mai mult risc decât justifică beneficiul**. Modelul Purdue rămâne util ca arhitectură de referință, dar NIST nu îl mai consideră suficient de unul singur. IIoT-ul modern, conectivitatea cloud, operațiunile la distanță și arhitecturile hibride cer o proiectare mai atentă decât simpla segmentare în zone.

## Conformitatea cu standardele scrise nu înseamnă securitate

NIST SP 800-82 Rev 3, IEC 62443 și NERC CIP descriu controalele potrivite pentru aceste sisteme. Nu le resping. Arăt ce afirmă explicit: **nu orice sistem OT poate implementa toate controalele.** Cadrele folosesc niveluri graduale de securitate și prevederi pentru controale compensatorii tocmai fiindcă sistemele vizate nu pot îndeplini adesea toate cerințele.

Diferența dintre ce descriu standardele și ce poate obține o anumită implementare veche nu este o eroare de documentație. Sistemele nu acceptă controalele. Ghidul recunoaște acest lucru. **Un audit de conformitate reușit pentru OT vechi nu înseamnă că mediul este sigur.** Înseamnă că ai documentat controalele compensatorii existente și un auditor le-a acceptat.

Cadrul de gestionare a riscurilor NIST afirmă clar că rămâne risc rezidual după aplicarea controalelor. Acceptarea riscului este unul dintre cele patru rezultate ale cadrului, alături de transferul, reducerea și evitarea riscului. *Recunoașterea riscului rezidual face parte din îndrumarea oficială.* **Când cineva spune că îndeplinirea cerințelor de conformitate securizează mediul OT, afirmă ceva ce cadrele citate nu susțin.**

## Ce să faci cu sistemele OT vechi

Dacă operezi medii OT vechi:

- **Tratează izolarea rețelei ca măsură principală** și auditează tot ce trece granița OT
- **Creează un plan separat de securizare pentru stațiile de inginerie.** Ele ating ambele rețele și sunt frecvent punctul de intrare
- **Controlează și înregistrează toate mediile detașabile** din zonele OT
- **Auditează accesul la distanță al furnizorilor** și închide fiecare sesiune care nu este folosită
- Implementează monitorizarea redundantă a senzorilor când proiectarea procesului permite
- **Stabilește un calendar de înlocuire cu estimări reale de cost**, chiar dacă înlocuirea este la ani distanță
- **Nu mai trata finalizarea auditului de conformitate ca reper de securitate**

Dacă achiziționezi sisteme OT noi:

- **Include cerințele de securitate în specificația de achiziție** înainte să răspundă furnizorii
- Alege platforme cu suport documentat pentru comunicații autentificate, actualizări de firmware semnate și control al accesului bazat pe roluri
- **Proiectează limitele IT/OT ca conducte explicite conform IEC 62443**, nu ca o politică vagă de „țineți-le separate”
- **Solicită SBOM-uri pentru componentele software OT** ca livrabil contractual

Industria a documentat bine problema. Standardele sunt corecte tehnic. *Sistemele în funcțiune nu pot respecta adesea ceea ce prescriu standardele.* Recunoașterea deschisă a acestui fapt este primul pas pentru a decide cum se gestionează riscul rămas.

## Referințe

- NIST SP 800-82 Rev 3: ghidul de securitate pentru tehnologia operațională (OT) (2023)
- IEC 62443: seria de securitate pentru sisteme de automatizare și control industrial
- IEC 62443-3-3: cerințe de securitate a sistemelor și niveluri de securitate
- IEC 62443-4-2: cerințe tehnice de securitate pentru componentele IACS
- IEC 61511: siguranță funcțională pentru sisteme instrumentate de siguranță
- NERC CIP: standarde de protecție a infrastructurii critice pentru sistemul electric la scară largă
- IEC 61000: standarde de compatibilitate electromagnetică
- Alerte și bune practici CISA ICS-CERT
- Cadrul MITRE ATT&CK pentru ICS
- Analiză tehnică Stuxnet, Langner Communications, 2011
- Analiză tehnică TRITON/TRISIS, Dragos, 2017
- Analiza incidentului de la stația de tratare a apei Oldsmar, CISA, 2021
- Sondaj privind costurile de conformitate NERC CIP al American Public Power Association, 2019

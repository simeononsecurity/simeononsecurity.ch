---
title: "Carduri Virtuale Privacy.com: Cum Funcționează Confidențialitatea Plăților"
date: 2023-09-03
lastmod: 2026-10-08
toc: true
draft: false
description: Ce este stocat pe un card de plată, de ce banda magnetică este partea cea mai slabă a acestuia, ce vede comerciantul când plătești cu un număr virtual și cum funcționează în practică tipurile și limitele cardurilor Privacy.com.
genre:
- Securitatea Plăților
- Confidențialitatea Digitală
- Carduri Virtuale
- Confidențialitatea Financiară
- Prevenirea Fraudelor
- Securitatea Consumatorului
tags:
- privacy.com
- carduri virtuale
- carduri de debit virtuale
- carduri cu utilizare unică
- carduri blocate pe comerciant
- carduri blocate pe categorie
- tokenizare
- token de rețea
- pan
- cvv
- skimming de card
- bandă magnetică
- pistă 1
- pistă 2
- securitatea cardurilor de plată
- frauda cu carduri de credit
- gestionarea abonamentelor
- limite de cheltuieli
- pci dss
- soc 2
- frauda cardului fără prezență fizică
- confidențialitatea financiară
- confidențialitatea plăților
- număr de card virtual
- card mascat
- controlul cardului
cover: /img/cover/privacy_virtual_cards.webp
coverAlt: O ilustrație digitală care arată un card virtual protejat cu un scut ce apără un simbol de lacăt, reprezentând securitatea și confidențialitatea oferite de cardurile de debit virtuale.
coverCaption: Protejează, Controlează și Asigură-ți Tranzacțiile Online.
ref:
- /magnetic-stripe-decoder
- /articles/personal-security-checklist-prioritized-2026
- /personal-security-course/personal-finance
---

**Un card virtual face un singur lucru specific: schimbă ce primește comerciantul, nu ce știe banca ta.** Acesta este întreg mecanismul, iar înțelegerea lui explică atât protecția pe care o primești, cât și protecția pe care nu o primești.

Majoritatea articolelor tratează cardurile virtuale ca un instrument general de confidențialitate și omit detaliile tehnice. Acest articol acoperă ce este stocat pe un card, de ce banda magnetică este punctul slab și cum se comportă în practică tipurile de carduri Privacy.com.

*Beneficiul practic este limitat și real: un număr furat devine inutil pentru un hoț, deoarece funcționează doar la comerciantul pentru care a fost emis.*

## Răspunsul Scurt

| Întrebare | Răspuns Scurt |
|---|---|
| **Ce schimbă un card virtual?** | Numărul pe care comerciantul îl stochează. Detaliile reale ale cardului tău nu ajung la ei |
| **Este tranzacția privată?** | Nu. Banca ta, rețeaua și emitentul o văd în continuare |
| **Ce împiedică o breșă să te afecteze?** | Un număr blocat pe comerciant sau cu utilizare unică, care e invalid oriunde altundeva |
| **Care este partea cea mai slabă a unui card fizic?** | Banda magnetică, care stochează datele complete ale pistei necriptate |
| **Construiește credit?** | Nu. Acestea nu sunt conturi de credit și nu se face verificare de credit |
| **Cine poate folosi Privacy.com?** | Cetățeni sau rezidenți legali din SUA, 18+, cu un cont curent la o bancă sau credit union din SUA |

## Ce Este pe un Card de Plată

**Trei elemente autorizează o tranzacție fără prezența fizică a cardului: numărul principal al contului, data de expirare și valoarea de verificare.**

| Element | Lungime | De Unde Provine |
|---|---|---|
| **Numărul Principal al Contului (PAN)** | Până la 19 cifre | Emitentul, cu cifrele inițiale care identifică schema și banca |
| **Expirare** | Patru cifre ca MM/AA | Emitentul |
| **CVV sau CVC** | Trei sau patru cifre | Derivat din PAN, expirare și o cheie pe care doar emitentul o deține |
| **Numele titularului** | Până la 26 caractere | Apare doar pe Pista 1 a benzii magnetice |

**PAN nu este un șir aleator.** Prima cifră identifică schema, următoarele câteva identifică banca emitentă, iar restul identifică contul. Structura permite verificarea plauzibilității numărului fără a contacta pe nimeni și explică de ce cifra de control Luhn detectează o cifră inversată.

**CVV este ceea ce dovedește că cineva a ținut fizic cardul** când a fost emis. Nu este stocat pe banda magnetică, motiv pentru care un skimmer care copiază banda nu îl obține niciodată.

*Inspectează toate acestea singur cu **[Magnetic Stripe Decoder and Encoder](/magnetic-stripe-decoder/)**, care analizează Pista 1 și Pista 2, decodează cifrele codului de serviciu și re-codifică rezultatul. Rulează complet în browserul tău, ceea ce contează deoarece acesta este conținutul complet al unui card de plată.*

{{< figure src="payment-card-data-anatomy-pan-cvv-tracks.webp" alt="Diagramă care arată elementele unui card de plată, inclusiv numărul principal al contului, data de expirare, CVV și cele trei piste ale benzii magnetice cu ce conține fiecare" >}}

## De Ce Banda Magnetică Este Punctul Slab

**Banda stochează datele contului în clar, iar orice cititor compatibil le poate citi.**

O bandă magnetică conține până la trei piste. Pista 1 poartă PAN, numele titularului, expirarea și un cod de serviciu format din trei cifre și este singura pistă care conține text alfanumeric. Pista 2 poartă PAN, expirarea și codul de serviciu într-o codificare numerică mai densă, iar **Pista 2 este ceea ce citește aproape orice terminal de punct de vânzare.** Pista 3 este practic neutilizată de rețelele majore și adesea lipsește de pe card.

Codul de serviciu merită înțeles, deoarece descrie utilizarea permisă a cardului. Prima cifră acoperă regulile de schimb, a doua cifră acoperă modul de autorizare, iar a treia cifră acoperă gama de servicii. Un card codificat `201` permite schimb internațional, nu necesită o cale specială de autorizare și nu are restricții de serviciu.

Istoria explică de ce banda a rezistat atât de mult. În 1969, un inginer IBM pe nume Forrest Parry a încercat să atașeze o bandă magnetică pe un card de plastic și nu a reușit să o lipească fără să o deterioreze. Soția sa a sugerat să folosească un fier de călcat, iar căldura a lipit banda de card. Această improvizație a devenit standardul pentru mai bine de jumătate de secol.

Două evoluții pun capăt acestei tehnologii:

| Eveniment | Stare |
|---|---|
| **Mastercard a anunțat eliminarea benzii** | Până în 2033, niciun card Mastercard de credit sau debit nu va mai avea bandă |
| **Europa** | Benzile au început să dispară de pe cardurile Mastercard în 2024 |
| **Statele Unite** | Băncile vor înceta să le emită începând cu 2027 |

*Banda a fost înlocuită de cip și plăți contactless deoarece copierea ei nu necesită altă abilitate decât de a deține un cititor. Instrumentul nostru **[magnetic stripe tool](/magnetic-stripe-decoder/)** arată cât de puține date sunt necesare pentru a reconstrui o pistă funcțională.*

{{< figure src="magnetic-stripe-track-layout-track1-track2.webp" alt="Diagramă a unei benzi magnetice care arată poziția fizică a pistelor unu, doi și trei, cu structura câmpurilor fiecărei piste, inclusiv sentinele, PAN, numele, expirarea și codul de serviciu" >}}

## Cum să Citești Datele de pe Piste

**Un șir de bandă magnetică este o succesiune de câmpuri, nu un al doilea număr de card.** Cititorul găsește sentinela de început, separă câmpurile, citește expirarea și codul de serviciu, apoi verifică sentinela de sfârșit și LRC.

| Pista | Început | Câmpuri principale | Sfârșit | Set de caractere |
|---|---|---|---|---|
| **Pista 1** | `%` | Cod format, PAN, nume, expirare, cod serviciu, date discreționare | `?` plus LRC | ALPHA pe șase biți, deci conține litere |
| **Pista 2** | `;` | PAN, expirare, cod serviciu, date discreționare | `?` plus LRC | BCD pe patru biți, deci conține cifre și un set mic de semne de punctuație |

Sentinelele opționale identifică limitele fizice ale înregistrării. Un decodor le omit adesea când afișează câmpurile, dar un encoder fizic are nevoie de formatul complet al înregistrării așteptat de cititor.

### Exemplu Pista 1

Acesta este un exemplu sintetic. Folosește PAN-ul standard de test din instrument și nume, expirare, cod serviciu și date discreționare false. Nu este un card Privacy.com și nu reprezintă date valide de plată.

```text
%B4111111111111111^TEST/USER^2912501000000000?
```

Citește-l de la stânga la dreapta:

| Segment | Valoare | Semnificație |
|---|---|---|
| **Sentinel început** | `%` | Începe înregistrarea Pistei 1 |
| **Cod format** | `B` | Format card financiar B |
| **PAN** | `4111111111111111` | Număr cont principal sintetic |
| **Separator câmp** | `^` | Sfârșitul PAN și începutul numelui |
| **Nume** | `TEST/USER` | Nume de familie, separator, prenume |
| **Separator câmp** | `^` | Sfârșitul numelui și începutul câmpurilor tranzacției |
| **Expirare** | `2912` | Decembrie 2029 în format AALL (an-lună) |
| **Cod serviciu** | `501` | Interschimb național, procesare normală, fără restricții |
| **Date discreționare** | `0000000` | Umplutură definită de emitent în acest exemplu |
| **Sentinel sfârșit** | `?` | Datele Pistei 1 se termină înainte de LRC |

Înregistrarea reală codificată conține și un caracter LRC după sentinelul de sfârșit când cititorul îl așteaptă. Forma vizibilă a textului este utilă pentru studierea structurii. Reprezentarea la nivel de biți include și paritate impară pentru fiecare caracter.

### Exemplu Pista 2

Pista 2 elimină numele și codul format. Aceleași valori sintetice devin:

```text
;4111111111111111=291250100000000?
```

| Segment | Valoare | Semnificație |
|---|---|---|
| **Sentinel început** | `;` | Începe înregistrarea Pistei 2 |
| **PAN** | `4111111111111111` | Număr cont principal sintetic |
| **Separator** | `=` | Sfârșitul PAN și începutul câmpurilor tranzacției |
| **Expirare** | `2912` | Decembrie 2029 în format AALL |
| **Cod serviciu** | `501` | Același cod serviciu sintetic ca la Pista 1 |
| **Date discreționare** | `0000000` | Umplutură definită de emitent în acest exemplu |
| **Sentinel sfârșit** | `?` | Datele Pistei 2 se termină înainte de LRC |

**Pista 2 este mai scurtă pentru că nu conține numele titularului.** Multe terminale citesc Pista 2 pentru tranzacții obișnuite cu glisare, în timp ce Pista 1 oferă câmpul nume când un cititor îl solicită.

### Cifrele Codului Serviciu

**Cele trei cifre ale codului serviciu descriu comportamentul terminalului și al autorizării.** Ele nu conțin CVV-ul, iar modificarea lor pe un card real fără autorizarea emitentului produce un credential de plată incorect sau înșelător.

| Cifră | Valori | Ce descrie |
|---|---|---|
| **Prima** | `0`, `1`, `2`, `5`, `6`, `7`, `9` | Reguli de interschimb și preferință cip |
| **A doua** | `0`, `1`, `2`, `4` | Calea de autorizare |
| **A treia** | `0` până la `7` | Restricții PIN, numerar, bunuri și servicii |

**Prima cifră** acoperă interschimbul și preferința cip:

| Valoare | Semnificație |
|---|---|
| `0` | Utilizare națională |
| `1` | Interschimb internațional permis |
| `2` | Interschimb internațional, folosește IC (cip) unde este posibil |
| `5` | Numai interschimb național, cu excepția acordurilor bilaterale |
| `6` | Numai interschimb național, cu excepția acordurilor bilaterale, folosește IC unde este posibil |
| `7` | Fără interschimb, cu excepția acordurilor bilaterale (circuit închis) |
| `9` | Test |

**A doua cifră** acoperă gestionarea autorizării:

| Valoare | Semnificație |
|---|---|
| `0` | Autorizare normală |
| `1` | Autorizare normală |
| `2` | Contactează emitentul prin mijloace online |
| `4` | Contactează emitentul prin mijloace online, cu excepția acordurilor bilaterale |

**A treia cifră** acoperă restricțiile serviciului:

| Valoare | Semnificație |
|---|---|
| `0` | Fără restricții, PIN necesar |
| `1` | Fără restricții |
| `2` | Doar bunuri și servicii (fără numerar) |
| `3` | Doar ATM, PIN necesar |
| `4` | Doar numerar |
| `5` | Doar bunuri și servicii (fără numerar), PIN necesar |
| `6` | Fără restricții, folosește PIN unde este posibil |
| `7` | Doar bunuri și servicii (fără numerar), folosește PIN unde este posibil |

De exemplu, `201` înseamnă interschimb internațional cu utilizare cip unde este posibil, procesare normală a autorizării și fără restricții de serviciu. Decodorul afișează fiecare cifră separat pentru a nu fi nevoie să memorezi tabelul.

### LRC și Paritate

**LRC este un caracter de verificare, nu un alt câmp de inventat.** Encoderul face XOR valorii datelor fiecărui caracter de la sentinelul de început până la cel de sfârșit. Rezultatul îl convertește înapoi în gama de caractere imprimabile a pistei și raportează separat biții de paritate impară codificați.

Pista 1 folosește un set de caractere ALPHA pe șase biți. Valoarea sa de date este codul ASCII minus `0x20`. Pista 2 folosește un set de caractere BCD pe patru biți. Valoarea sa de date este nibla joasă a codului ASCII. Aplicarea mapării Pistei 1 pe Pista 2 produce LRC greșit.

Opțiunea decodorului **Include LRC calculat** adaugă caracterul LRC imprimabil la ieșire. Descompunerea sa arată și modelul de biți LRC cu paritate impară. Folosește asta pentru a învăța cum verifică cititorul înregistrarea, nu pentru a ocoli controalele emitentului.

## Scrierea cardurilor sintetice pentru testare

**Folosește decodorul pentru a scrie șiruri de test, nu carduri de plată reale.** Instrumentul acceptă câmpuri, reconstruiește Pista 1 și Pista 2, adaugă sentinele opționale și calculează LRC. Rulează local în browser.

1. Deschide **[Magnetic Stripe Decoder and Encoder](/magnetic-stripe-decoder/)**.
2. Selectează **Load Test Card**. Aceasta completează instrumentul cu PAN-ul sintetic `4111111111111111`, numele `TEST/USER`, data de expirare `2912`, codul de serviciu `201` și datele discreționare de test.
3. Activează **Include start and end sentinels** pentru a afișa limitele fizice ale înregistrării.
4. Activează **Include calculated LRC** pentru a adăuga caracterul de verificare calculat.
5. Activează **Split discretionary data into PVKI, PVV and CVV** doar pentru a vedea cum este afișat un câmp sintetic de nouă cifre. Aceste etichete sunt convenții ale emitentului, nu un format universal pentru Track 1 sau Track 2.
6. Modifică numele, data de expirare, codul de serviciu sau datele discreționare sintetice. Ieșirea se actualizează pe măsură ce tastezi.
7. Compară câmpurile decodificate cu șirurile generate. Șterge câmpurile când ai terminat.

Pentru un exercițiu cu Track 1 sintetic, folosește:

```text
PAN: 4111111111111111
Surname: TEST
First name: USER
Expiry: 12/29
Service code: 201
Discretionary data: 000000000
```

Pentru un exercițiu cu Track 2 sintetic, folosește același PAN, data de expirare, codul de serviciu și un câmp discreționar numeric. Șirul generat pentru Track 2 omit numele deoarece Track 2 nu are câmp pentru nume.

**Nu copia un PAN, data de expirare, CVV sau valoare discreționară live de la Privacy.com într-un card scriibil.** Privacy.com descrie produsul său ca numere de card virtual create prin site-ul sau aplicația sa. Pagina oficială nu prezintă serviciul ca un sistem de scriere pe bandă magnetică, iar un număr de card virtual nu este dovada unui record fizic autorizat de emitent. Un card de test scriibil care conține o acreditare live creează un instrument de plată duplicat și încalcă termenii emitentului sau regulile de plată.

Limita sigură este simplă: folosește eșantionul sintetic încorporat în instrument, folosește un card de laborator cu valori fictive și folosește un card fizic aprobat de emitent când trebuie să plătești în persoană. Nu încerca să transformi un card virtual Privacy.com într-un card fizic cu bandă magnetică.

## Ce Schimbă un Card Virtual

**Un card virtual este un al doilea număr care stă în fața primului.**

Când plătești cu un card virtual, comerciantul primește un număr, o dată de expirare și un CVV care aparțin cardului virtual. PAN-ul tău real nu ajunge niciodată la ei. Practic, schimbarea se observă după o breșă:

| Scenariu | Cu Cardul Tău Real | Cu un Card Virtual Blocată pe Comerciant |
|---|---|---|
| **Baza de date a comerciantului a fost compromisă** | Numărul este valid oriunde este acceptat | Numărul e respins la orice alt comerciant |
| **Abonament anulat** | Se continuă taxarea până îl disputezi | Închizi cardul și plata e respinsă |
| **Perioadă de probă convertită silențios** | Taxă nedorită pe extrasul tău | Limita sau închiderea o opresc |
| **Detalii de card vândute pe un forum** | Folosibil pentru fraudă card-nu-prezent | Folosibil doar la un singur comerciant, dacă deloc |

**Ce nu schimbă contează la fel de mult.** Banca ta vede în continuare tranzacția. Rețeaua de carduri o procesează în continuare. Emitentul deține în continuare identitatea ta, deoarece regulile anti-spălare de bani cer verificare. **Un card virtual reduce expunerea la comerciant. Nu este o metodă de a cheltui anonim.**

*Această distincție îi încurcă constant pe oameni. Dacă modelul tău de amenințare include emitentul sau rețeaua, un card virtual nu schimbă nimic în privința asta.*

{{< figure src="virtual-card-merchant-shielding-flow.webp" alt="Diagramă care arată un număr de card virtual trimis comerciantului în timp ce numărul real al cardului rămâne între titularul cardului și banca emitentă" >}}

## Cele Trei Tipuri de Obiect în Formă de Card

Terminologia este folosită inconsistent, iar diferența contează când alegi ce să dai unui comerciant.

| Tip | Număr de Card | Versiune Fizică | Utilizare Tipică |
|---|---|---|---|
| **Card digital** | Același ca al cardului fizic | Da | Adăugarea cardului existent într-un portofel mobil |
| **Card virtual** | Diferit de orice card fizic | Nu | Cumpărături online, abonamente, comercianți ocazionali |
| **Card digital-first** | Diferit, cu un card fizic opțional legat | Opțional | Conturi fintech unde cardul fizic nu are detalii imprimate |

**Un portofel mobil folosește un mecanism complet diferit.** Când adaugi un card într-un portofel, portofelul stochează un token specific dispozitivului în loc de PAN-ul tău, iar comerciantul primește tokenul. Aceasta se numește tokenizare și este motivul pentru care plata cu telefonul este mai sigură decât predarea cardului fizic chiar și fără un card virtual.

*Tokenizarea în rețea și cardurile virtuale rezolvă părți suprapuse ale aceleiași probleme. Tokenizarea protejează numărul în tranzit și în repaus. Un card virtual te protejează de ceea ce păstrează comerciantul ulterior.*

## Tipurile de Card Privacy.com

**Privacy.com oferă patru comportamente de card, iar ele nu sunt interschimbabile.**

| Tip Card | Comportament | Cel Mai Potrivit Pentru |
|---|---|---|
| **Single-Use** | Se închide automat după o tranzacție | Cumpărături unice și comercianți necunoscuți |
| **Merchant-Locked** | Se blochează la primul comerciant care îl folosește și e respins în altă parte | Cumpărături online zilnice |
| **Category-Locked** | Restricționat la o categorie de cheltuieli | Limitarea unei întregi clase de cheltuieli |
| **Everywhere** | Card fizic cu același model de protecție | Cumpărături în persoană |

**Blocarea pe comerciant este mecanismul care aduce cea mai mare valoare.** Un card blocat e respins la orice comerciant în afară de cel cu care a fost folosit prima dată, ceea ce înseamnă că o breșă la comerciant generează un număr inutil în altă parte.

**Single-use este opțiunea mai puternică acolo unde se aplică.** Un card care se închide după o singură plată nu poate fi refolosit deloc și elimină nevoia de a-ți aminti să-l închizi ulterior.

Două detalii operaționale demne de știut:

- **Cardurile partajate se blochează la primul comerciant cu care sunt folosite**, deci partajarea cu un membru al familiei sau angajat păstrează restricția comerciantului.
- **Un card este pus în pauză, nu închis.** Pauza este reversibilă, ceea ce este util când vrei să oprești temporar un abonament fără să pierzi detaliile cardului.

## Limite și Controale de Cheltuieli

**Fiecare card are o limită de cheltuieli, care este un control separat de blocarea pe comerciant.**

| Control | Ce Previne |
|---|---|
| **Limită per tranzacție** | O singură plată mai mare decât ai autorizat |
| **Limită lunară** | Acumularea plăților într-o perioadă de facturare |
| **Pauză** | Orice plată, reversibil |
| **Închidere** | Orice plată viitoare, permanent |

**Setează atât o limită per tranzacție cât și o limită lunară pe orice card legat de un abonament.** O creștere silențioasă a prețului de către comerciant lovește limita, nu soldul tău, și observi asta printr-o plată eșuată în loc să lipsească o linie pe extras.

*Modulul nostru **[Personal Finance Security](/personal-security-course/personal-finance/)** plasează acest control alături de blocarea creditului și tokenizarea cardului ca cele trei controale care limitează ce poate accesa un comerciant compromis.*

## Planuri și Ce Deblochează Fiecare

Privacy.com oferă un nivel gratuit alături de trei planuri plătite. Prețurile și limitele funcționalităților se pot schimba, așa că verificați termenii actuali înainte de a vă abona.

| Plan | Preț | Adăugiri Notabile |
|---|---|---|
| **Personal (gratuit)** | 0 $ | Carduri virtuale, blocare comerciant, limite de cheltuieli, fără taxă pentru tranzacții interne |
| **Plus** | 5 $/lună | Carduri pe categorii, note pe card pentru organizarea cheltuielilor |
| **Pro** | 10 $/lună | Cashback la achiziții eligibile, carduri fizice Everywhere |
| **Premium** | 25 $/lună | Tot ce este în Pro, cu limita lunară de creare carduri ridicată la 60 |

**Nivelul gratuit acoperă beneficiul principal de securitate.** Blocarea comerciantului, cardurile de unică folosință și limitele de cheltuieli sunt mecanismele care reduc expunerea și sunt disponibile fără plată. Nivelurile plătite adaugă organizare și comoditate, nu protecție suplimentară.

**Taxele pentru tranzacții externe diferă în funcție de nivel.** Nivelul gratuit percepe 3% pentru tranzacțiile externe, cu un minim de 0,50 $, în timp ce nivelurile plătite nu percep astfel de taxe.

## Ce NU face Privacy.com

**Claritatea limitărilor este mai utilă decât o listă de funcții.**

| Limitare | Detaliu |
|---|---|
| **Nu te face anonim** | Identitatea ta este verificată la înscriere și este deținută de emitent |
| **Nu ascunde tranzacția față de banca ta** | Banca ta vede transferul de fonduri, iar rețeaua vede plata |
| **Nu construiește credit** | Nu sunt conturi de credit și nu se face verificare de credit |
| **Este valabil doar în SUA** | Necesită cetățenie sau rezidență legală în SUA și un cont bancar sau de credit union în SUA |
| **Necesită verificarea identității** | Verificările Know Your Customer sunt obligatorii conform regulilor anti-spălare de bani |
| **Nu acoperă toți comercianții** | Unii comercianți blochează intervalele de carduri prepaid și virtuale |

**Punctul despre blocarea comerciantului contează în practică.** Unele servicii de abonament și companii aeriene resping intervalele de carduri pe care le asociază cu carduri virtuale sau prepaid, iar nicio configurare nu rezolvă problema. Păstrați un card real ca rezervă pentru aceste cazuri.

*Rezumatul sincer: un card virtual este un control de limitare a expunerii la comerciant, nu un instrument de anonimat. Dacă aveți nevoie de anonimat, este o problemă diferită cu instrumente diferite.*

## Cine emite cardul și de ce contează

**Un card virtual este tot un card real, emis de o bancă reală, sub o licență reală de schemă.**

| Detaliu | Valoare |
|---|---|
| **Banca emitentă** | Patriot Bank, N.A., membru FDIC |
| **Licențe schemă** | Mastercard și Visa |
| **Unde este acceptat** | Oriunde sunt acceptate Mastercard și Visa |
| **Finanțare** | Transferată din contul tău curent legat în SUA |

**De aceea protecția este autentică.** Cardul beneficiază de aceleași protecții ale schemei ca orice alt produs Mastercard sau Visa, ceea ce înseamnă că drepturile de chargeback și procesele de dispută pentru fraudă se aplică normal. Nu este un card cadou sau un credit închis de magazin.

Două certificări merită menționate pentru că sunt verificabile independent, nu doar afirmații de marketing:

- **Conformitate PCI-DSS**, standardul industriei cardurilor de plată pentru gestionarea datelor deținătorului de card
- **SOC 2 Tip II**, un raport auditat care acoperă controalele de securitate pe o perioadă de timp, nu doar o afirmație punctuală

**Despre modelul de afaceri:** compania afirmă că câștigă din comisioanele de interschimb de la comercianți și nu vinde datele clienților către publicitari sau terți. Acesta este același model de venit ca orice alt emitent de carduri, ceea ce merită înțeles și nu tratat ca ceva neobișnuit.

*Motivul practic pentru a verifica banca emitentă este confirmarea. Oricine poate pretinde că administrează un program de carduri, iar numele emitentului de pe card este ceea ce confirmați cu banca menționată în documente.*

Inspectați schema și banca după prefixul PAN folosind **[Magnetic Stripe Decoder](/magnetic-stripe-decoder/)**, care raportează intervalul schemei majore și validează cifra de control Luhn.

## Cum să folosești bine cardurile virtuale

**Controalele ajută doar dacă le configurați.** Șase obiceiuri aduc majoritatea beneficiilor.

1. **Blocați fiecare card la un comerciant** decât dacă există un motiv să nu o faceți. Blocarea face ca un număr scurs să fie inutil.
2. **Folosiți carduri de unică folosință pentru orice necunoscut**, inclusiv pentru trialuri și achiziții unice de pe site-uri mici.
3. **Stabiliți ambele limite de cheltuieli** pe cardurile de abonament, astfel încât o creștere de preț să eșueze în loc să fie taxată.
4. **Denumiți fiecare card după comerciant**, pentru ca lista de tranzacții să fie lizibilă și o taxă neașteptată să iasă în evidență.
5. **Puneți pe pauză în loc să închideți** când plănuiți să reluați un serviciu și închideți când nu veți continua.
6. **Păstrați un card real pentru comercianții care resping intervalele virtuale**, astfel încât un checkout blocat să nu devină o urgență.

> **Greșeală comună: a trata un card virtual ca un substitut pentru verificarea extraselor.** Blocarea comerciantului oprește o clasă de daune. Nu detectează un cont compromis la banca ta, un transfer neautorizat sau o taxă frauduloasă pe cardul real din spate.

## Concluzii cheie

- **Un card virtual schimbă numărul pe care comerciantul îl stochează.** PAN-ul tău real nu ajunge niciodată la ei, acesta fiind mecanismul principal.
- **Nu face tranzacția privată.** Banca ta, rețeaua și emitentul încă o văd, iar verificarea identității este obligatorie.
- **Blocarea comerciantului este funcția cu cea mai mare valoare**, deoarece un număr scurs nu funcționează în altă parte.
- **Nivelul gratuit include controalele de securitate.** Planurile plătite adaugă organizare și comoditate, nu protecție.
- **Pista magnetică stochează datele cardului în clar** și va fi eliminată până în 2033, băncile din SUA oprind emiterea în 2027.
- **CVV-ul nu este pe pistă**, motiv pentru care un skimmer care copiază pistele nu are ceea ce cer mulți comercianți online.
- **Unii comercianți resping intervalele de carduri virtuale.** Păstrați un card real ca rezervă.
- **Verificați banca emitentă** în loc să aveți încredere în afirmațiile programului de carduri și verificați singur prefixul PAN.

## Pașii următori

1. **Inspectați datele de pe banda cardului dvs.** și vedeți exact ce conține o bandă magnetică: **[Decodor și encoder pentru bandă magnetică](/magnetic-stripe-decoder/)**
2. **Blocați-vă creditul** dacă nu ați făcut-o deja, aceasta fiind o măsură mai puternică împotriva fraudei la conturi noi: **[Securitatea finanțelor personale](/personal-security-course/personal-finance/)**
3. **Aplicați disciplina de prioritizare** pentru a decide cât efort merită situația dvs.: **[Lista de verificare prioritizată pentru securitatea personală](/articles/personal-security-checklist-prioritized-2026/)**
4. **Revizuiți planurile și termenii actuali Privacy.com** înainte de a vă abona: **[Privacy.com](https://www.privacy.com/virtual-card)**
5. **Verificați dacă datele dvs. apar deja într-o breșă** înainte de a presupune că nu sunteți afectat: **[Have I Been Pwned](https://haveibeenpwned.com)**
6. **Citiți lista de verificare pentru securitatea plăților** destinată organizațiilor: **[Lista de verificare pentru răspuns la incidente](/checklists/incident-response-checklist/)**

## Referințe

1. [Privacy.com - ce sunt cardurile virtuale, blocarea comercianților și limitele de cheltuieli](https://www.privacy.com/virtual-card)
2. [Card digital - Wikipedia, acoperind cardurile digitale versus virtuale, benzile magnetice, codurile de serviciu, paritatea și LRC](https://en.wikipedia.org/wiki/Digital_card)
3. [ISO/IEC 7813:2006 - carduri de identificare, carduri pentru tranzacții financiare, structura datelor benzilor 1 și 2](https://webstore.iec.ch/en/publication/11605)
4. [ISO/IEC 7813 - detalii despre structura câmpurilor benzilor, inclusiv sentinele și codurile de serviciu](https://en.wikipedia.org/wiki/ISO/IEC_7813)
5. [Consiliul pentru Standardele de Securitate PCI - cerințe pentru mediul datelor deținătorului de card](https://www.pcisecuritystandards.org/)
6. [Biroul pentru Protecția Financiară a Consumatorului - rapoarte și scoruri de credit](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/)
7. [Codificarea datelor ANSI/ISO ALPHA, setul de caractere și tabelul de paritate pentru Banda 1](http://www.hhhh.org/~joeboy/resources/magcards/trackdata_ANSI-ISO_ALPHA.html)
8. [Caractere ISO pentru carduri magnetice, seturile pentru Banda 1 și Banda 2 comparate](https://www.pos.swiftpos.com.au/Help-SP/MagneticCardSwipeISOCharacters.html)
9. [Citirea datelor de pe carduri magnetice, un ghid practic cu scanare live a unui card](https://blog.j2i.net/2024/06/18/reading-magnetic-card-data/)

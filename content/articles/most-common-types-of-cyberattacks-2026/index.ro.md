---
title: "Cele mai frecvente tipuri de atacuri cibernetice și cum le detectezi"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Află care sunt tipurile frecvente de atacuri cibernetice, ce urme lasă în jurnale și telemetrie și exersează detectarea lor într-un laborator de securitate de acasă."
genre: ["Securitate cibernetică", "Detectarea amenințărilor", "Blue Team", "Operațiuni de securitate", "Dezvoltare profesională"]
tags: ["tipuri de atacuri cibernetice", "malware", "ransomware", "phishing", "spear phishing", "inginerie socială", "spoofing", "atacuri bazate pe identitate", "credential stuffing", "password spraying", "injecție SQL", "cross-site scripting", "atac asupra lanțului de aprovizionare", "amenințare internă", "tunelare DNS", "atacuri IoT", "atacuri bazate pe inteligență artificială", "refuzul serviciului", "ingineria detectării", "analist SOC", "Blue Team", "laborator de acasă", "analiza jurnalelor", "răspuns la incidente", "MITRE ATT&CK", "carieră în securitate cibernetică", "vânătoare de amenințări", "centru de operațiuni de securitate", "telemetrie", "trierea alertelor"]
cover: "/img/cover/types-of-cyberattacks-icons-illustration.webp"
coverAlt: "Ilustrație digitală cu pictograme abstracte și colorate care simbolizează diferite tipuri de atacuri cibernetice, precum ransomware, phishing și refuzul serviciului, pe un fundal întunecat."
coverCaption: ""
---

**Un tip de atac** este o categorie de tehnici, nu un instrument singular. Ransomware, phishing și credential stuffing denumesc metode pe care un adversar le repetă împotriva multor ținte, cu variații minore. Cunoașterea acestor categorii îți oferă un reper pentru alertele pe care le vei întâlni într-o echipă de securitate.

*Familiile individuale de malware apar și dispar în câteva luni. Categoriile de atac de mai jos sunt stabile de ani întregi, iar fiecare lasă urme recognoscibile în telemetria endpointurilor, identităților, rețelei sau e-mailului.*

<!--more-->

## Idei principale

- **Învață tiparul, nu încărcătura utilă.** Categoriile de atac se schimbă mult mai lent decât instrumentele individuale.
- **Fiecare categorie lasă dovezi.** Detectarea începe prin identificarea telemetriei care înregistrează activitatea.
- **Reproduce un atac ca să îl înțelegi.** Un laborator de acasă transformă o categorie abstractă într-o observație înregistrată.
- **Notează ce ai găsit.** O scurtă notă de investigație dovedește munca și explică dovezile colectate.

## Tipurile de atac, pe scurt

Tabelul de mai jos enumeră categoriile întâlnite cel mai des de echipele de securitate. Secțiunile următoare descriu fiecare categorie, variantele sale comune și datele pe care un apărător le examinează pentru a o detecta.

| Tip de atac | Ce face |
|---|---|
| **Malware** | Rulează programe rău intenționate precum ransomware, spyware și troieni |
| **Refuzul serviciului** | Inundă un serviciu cu trafic până când utilizatorii legitimi pierd accesul |
| **Phishing** | Păcălește o persoană să divulge acreditări sau să ruleze un fișier rău intenționat |
| **Spoofing** | Face atacatorul să pară un sistem, un expeditor sau o adresă de încredere |
| **Atacuri bazate pe identitate** | Abuzează de acreditări furate sau falsificate pentru a acționa ca un utilizator valid |
| **Injectarea de cod** | Inserează cod rău intenționat într-o aplicație pentru a-i schimba comportamentul |
| **Atacuri asupra lanțului de aprovizionare** | Compromit un furnizor, o bibliotecă sau un canal de actualizare de încredere |
| **Inginerie socială** | Manipulează o persoană să întreprindă o acțiune nesigură |
| **Amenințări interne** | Abuzează de accesul unui angajat actual sau fost |
| **Tunelare DNS** | Codifică date în interogări DNS pentru a ocoli controalele |
| **Atacuri IoT** | Vizează dispozitive conectate pentru a se deplasa prin rețea, a spiona sau a intra într-o rețea bot |
| **Atacuri bazate pe IA** | Folosesc învățarea automată pentru a genera conținut, a imita persoane sau a evita filtrele |

**Notă despre domeniu:** categoriile se suprapun. Un mesaj de phishing livrează adesea malware, iar furtul de acreditări precedă frecvent un atac bazat pe identitate. Privește lista ca pe un set de perspective, nu ca pe delimitări stricte.

______

## Malware

**Malware** este orice program creat pentru a deteriora, controla sau exploata un sistem. Termenul include ransomware, malware fără fișiere, spyware, adware, troieni, viermi, rootkituri, keyloggere și rețele bot.

| Subtip | Comportament |
|---|---|
| **Ransomware** | Criptează fișiere și cere bani pentru cheia de decriptare |
| **Malware fără fișiere** | Folosește instrumente încorporate în sistem și scrie puțin pe disc |
| **Spyware** | Colectează date despre activitate fără știrea utilizatorului |
| **Troian** | Se prezintă drept software legitim pentru a fi executat |
| **Vierme** | Se copiază între gazde fără intervenția utilizatorului |
| **Rootkit** | Se ascunde în sistemul de operare pentru a păstra controlul persistent |

**Unde găsești dovezile:** instrumentele de detectare și răspuns pentru endpointuri, sau **EDR**, înregistrează arborii de procese, liniile de comandă, scrierile de fișiere și modificările registrului. Chiar și un atac fără fișiere generează telemetrie de procese și scripturi, deoarece sistemul de operare pornește în continuare instrumentele exploatate de atac.

______

## Refuzul serviciului

**Un atac de refuz al serviciului (DoS)** inundă o țintă cu solicitări până când utilizatorii legitimi pierd accesul. **Un atac distribuit de refuz al serviciului (DDoS)** repetă aceeași idee de pe multe sisteme simultan, ceea ce îngreunează filtrarea traficului după adresa sursă.

| Caracteristică | DoS | DDoS |
|---|---|---|
| **Origine** | Un sistem | Multe sisteme |
| **Dificultatea blocării** | Moderată | Ridicată, deoarece sursele provin din multe rețele |
| **Impact obișnuit** | Pierderea disponibilității | Pierderea disponibilității la scară mai mare |

**Unde găsești dovezile:** volumul traficului față de o referință, numărul de conexiuni per sursă, creșterea bruscă a ratei solicitărilor și schimbările ratei de eroare. Monitorizarea disponibilității declanșează adesea o alertă înainte ca echipa de securitate să observe evenimentul.

______

## Phishing

**Phishingul** folosește e-mailuri, mesaje text, apeluri telefonice sau rețele sociale pentru a convinge o persoană să divulge acreditări ori să deschidă un atașament rău intenționat. Variantele se diferențiază după țintă și canal.

| Variantă | Țintă și canal |
|---|---|
| **Spear phishing** | O anumită persoană sau echipă, de obicei prin e-mail |
| **Whaling** | Directori și angajați cu funcții înalte, adesea pentru a muta bani sau date |
| **Smishing** | Mesaje text frauduloase |
| **Vishing** | Apeluri sau mesaje vocale frauduloase |

**Unde găsești dovezile:** jurnalele gateway-ului de e-mail, rezultatele analizei URL-urilor, analiza atașamentelor și rapoartele utilizatorilor. Raportarea unui angajat atent este unul dintre cele mai valoroase semnale din această listă.

______

## Spoofing

**Spoofingul** ascunde atacatorul în spatele unei identități de încredere, astfel încât ținta să accepte conexiunea, mesajul sau adresa. Deghizarea câștigă timp și învinge verificările bazate pe încredere.

| Tip | Ce se falsifică |
|---|---|
| **Spoofing de domeniu** | Un site sau domeniu de e-mail asemănător, care imită un brand real |
| **Spoofing de e-mail** | Adresa expeditorului unui mesaj |
| **Spoofing ARP** | O adresă locală de rețea pentru a intercepta traficul dintre două gazde |

**Unde găsești dovezile:** rezultatele SPF, DKIM și DMARC din antetele e-mailurilor, vechimea înregistrării domeniului, nepotriviri de certificate și alerte privind adrese duplicate în rețeaua locală.

______

## Atacuri bazate pe identitate

**Atacurile bazate pe identitate** folosesc un cont valid în locul unei vulnerabilități software. Atacatorul are acreditări funcționale, așa că activitatea seamănă cu utilizarea normală și se pierde în zgomotul de fond. Această categorie generează o mare parte dintre alertele gestionate zilnic de un **centru de operațiuni de securitate (SOC)**.

*Dacă exersezi o singură categorie într-un laborator de acasă, alege-o pe aceasta. Semnalele sunt bogate, exercițiile se repetă, iar configurarea rămâne simplă.*

| Tehnică | Ce se întâmplă |
|---|---|
| **Kerberoasting** | Solicită un tichet de serviciu, apoi sparge offline parola criptată |
| **Atacul omului din mijloc (MITM)** | Se așază între două părți pentru a citi sau modifica o sesiune |
| **Pass-the-hash** | Refolosește un hash de parolă furat pentru a deschide o sesiune nouă |
| **Golden ticket** | Falsifică un tichet Kerberos pentru acces extins la domeniu |
| **Silver ticket** | Falsifică un tichet de serviciu pentru un serviciu anume |
| **Colectarea acreditărilor** | Adună în masă nume de utilizator și parole |
| **Credential stuffing** | Reîncearcă aceleași acreditări pe multe site-uri fără legătură între ele |
| **Password spraying** | Încearcă o parolă uzuală pe multe conturi |
| **Forță brută** | Încearcă multe parole pentru un singur cont |
| **Retrogradare** | Forțează conexiunea să folosească o versiune mai slabă a protocolului |

**Unde găsești dovezile:** înregistrări de autentificare, numărul autentificărilor eșuate, anomalii ale tokenurilor, alerte de deplasare imposibilă și detectări ale riscurilor de identitate. **Phishingul adversary-in-the-middle (AiTM)** aparține tot aici, deoarece atacatorul fură un token de sesiune activ în locul unei parole, iar reutilizarea lui dintr-o infrastructură necunoscută declanșează motorul de risc de identitate.

______

## Injectarea de cod

**Injectarea de cod** plasează cod controlat de atacator într-o aplicație vulnerabilă, astfel încât aplicația să îl ruleze în cadrul activității obișnuite. Aplicația, nu atacatorul, efectuează acțiunea dăunătoare.

| Tip | Țintă |
|---|---|
| **Injecție SQL** | O interogare a bazei de date construită din intrări nevalidate |
| **Cross-site scripting (XSS)** | O pagină web care rulează scriptul atacatorului în browserul unui vizitator |
| **Malvertising** | Un spațiu publicitar legitim umplut cu cod rău intenționat |
| **Otrăvirea datelor** | Un set de antrenament pentru un model de IA sau învățare automată |

**Unde găsești dovezile:** jurnalele aplicațiilor web, înregistrările interogărilor bazei de date, rapoartele politicii de securitate a conținutului și tiparele de solicitări care diferă de utilizarea normală a aplicației.

______

## Atacuri asupra lanțului de aprovizionare

**Un atac asupra lanțului de aprovizionare** vizează o terță parte de încredere, al cărei produs sau serviciu ajunge la mulți clienți. **Un atac asupra lanțului de aprovizionare software** introduce cod rău intenționat într-o aplicație, bibliotecă sau actualizare, astfel încât toți utilizatorii produsului să îl primească. **Un atac asupra lanțului de aprovizionare hardware** compromite o componentă fizică înainte de expediere.

*Software-ul modern se bazează pe biblioteci terțe, așa că o singură dependență compromisă ajunge mult mai departe decât furnizorul inițial.*

**Unde găsești dovezile:** analiza compoziției software, înregistrările pipeline-ului de build, conexiuni de ieșire neașteptate de la o actualizare de încredere și verificări de integritate pentru artefactele distribuite.

______

## Inginerie socială

**Ingineria socială** folosește presiunea psihologică pentru a împinge o persoană spre o acțiune nesigură. Atacatorul apelează la autoritate, urgență, frică, bani sau încredere.

| Tehnică | Abordare |
|---|---|
| **Pretexting** | Inventează un scenariu credibil pentru a câștiga încrederea |
| **Compromiterea e-mailului de afaceri (BEC)** | Se dă drept un coleg de încredere pentru a redirecționa o plată sau a obține date |
| **Dezinformare** | Răspândește narațiuni false prin rețele sociale și boți |
| **Quid pro quo** | Oferă o recompensă în schimbul informațiilor sau accesului |
| **Capcană sentimentală** | Construiește o relație falsă pentru a obține bani, date sau acces |
| **Tailgating** | Urmează un angajat printr-o ușă securizată |

**Unde găsești dovezile:** rezultate de autentificare a e-mailului, solicitări neobișnuite de schimbare a plăților, evidențe ale serviciului de asistență și jurnale de acces fizic.

______

## Amenințări interne

**O amenințare internă** este folosirea abuzivă a accesului de către un angajat actual sau fost, un contractant sau un partener. Unii acționează intenționat, din motive financiare sau resentimente. Alții acționează din neglijență, de exemplu lăsând acreditări într-un document partajat.

*Rapoartele de incidente menționează mai des persoane interne neglijente decât persoane rău intenționate. Pentru ambele se aplică același control de detectare: compară accesul cu o referință stabilită pentru rol.*

**Unde găsești dovezile:** volumul transferurilor de date, activitatea în afara programului normal, modificările de privilegii și descărcările în masă din depozite sensibile.

______

## Tunelare DNS

**Tunelarea DNS** codifică date în interogări și răspunsuri DNS. Aproape toate rețelele permit DNS, așa că tehnica transportă date dincolo de controalele concepute pentru inspectarea traficului web.

*Detectarea se bazează pe volum și formă. O gazdă care trimite mii de interogări către un singur domeniu se distinge de referința normală, iar subdomeniile neobișnuit de lungi sugerează o încărcătură utilă codificată.*

**Unde găsești dovezile:** înregistrări ale interogărilor DNS, lungimea și volumul acestora per gazdă, tipuri rare de înregistrări precum TXT și căutări către domenii înregistrate cu doar câteva zile înainte.

______

## Atacuri asupra dispozitivelor IoT

**Un atac IoT** vizează un dispozitiv conectat, precum o cameră, imprimantă, termostat sau senzor. Acreditările implicite slabe și actualizările rare de firmware transformă aceste dispozitive în puncte de intrare comune. După compromitere, un dispozitiv intră într-o rețea bot, scurge date sau devine o cale spre rețeaua mai largă.

*Extinderea 5G adaugă dispozitive conectate la scară mare, iar fiecare dispozitiv nou este o altă țintă cu un ciclu lung de actualizare.*

**Unde găsești dovezile:** inventarul dispozitivelor, tiparele conexiunilor de ieșire, transferurile anormale de date de la un dispozitiv cu rol fix și diferențele de versiune firmware dintr-o flotă.

______

## Atacuri bazate pe IA

**Atacurile bazate pe IA** aplică învățarea automată activităților atacatorului.

| Tehnică | Utilizare |
|---|---|
| **IA/ML adversarială** | Manipulează datele de antrenament sau intrările pentru a păcăli un model |
| **Dark AI** | Aplică IA și învățarea automată pentru a exploata vulnerabilități |
| **Deepfake** | Generează materiale audio, video sau imagini false și realiste |
| **Inginerie socială generată de IA** | Poartă conversații convingătoare prin chat sau voce, la scară mare |

*Un apel cu voce deepfake sau o conversație de phishing fluentă sporește credibilitatea unei vechi metode. Tehnica de bază rămâne familiară, motiv pentru care competențele de detectare bazate pe comportament durează mai mult decât cele legate de un singur instrument.*

**Unde găsești dovezile:** semnale privind proveniența conținutului, verificare pe un canal separat pentru cereri de bani sau acces și anomalii comportamentale în jurul schimbărilor de identitate și plată.

______

## Asocierea atacurilor cu telemetria

Fiecare categorie alimentează o sursă de date diferită. Tabelul le asociază și oferă un punct de pornire pentru detectare.

| Tip de atac | Telemetrie principală |
|---|---|
| **Malware** | Înregistrări EDR despre procese, fișiere și registru |
| **Refuzul serviciului** | Fluxuri de rețea și monitoare de disponibilitate |
| **Phishing** | Jurnale ale gateway-ului de e-mail și analizei URL-urilor |
| **Spoofing** | Înregistrări de autentificare a e-mailului și adrese de rețea |
| **Bazat pe identitate** | Înregistrări de autentificare și protecție a identității |
| **Injectarea de cod** | Jurnale ale aplicațiilor web și interogărilor bazei de date |
| **Lanț de aprovizionare** | Pipeline de build și inventarul dependențelor |
| **Inginerie socială** | E-mail, serviciu de asistență și acces fizic |
| **Amenințare internă** | Înregistrări de acces și transfer de date |
| **Tunelare DNS** | Înregistrări ale interogărilor DNS |
| **IoT** | Inventarul dispozitivelor și înregistrări ale fluxurilor de ieșire |
| **Bazat pe IA** | Înregistrări privind identitatea, plățile și proveniența conținutului |

*Începe detectarea cu coloana de telemetrie. O regulă utilă pornește de la o sursă de date cunoscută și un comportament cunoscut, nu de la numele unui instrument.*

**Categoriile se suprapun în timpul unui incident.** Un mesaj de phishing poate duce la furtul acreditărilor, executarea malware-ului și o intruziune bazată pe identitate. Etichetează tehnica de acces inițial, apoi înregistrează separat comportamentele ulterioare. Astfel, un singur eveniment nu devine patru alerte fără legătură, iar investigația primește o cronologie mai clară.

______

## Exersează detectarea într-un laborator

O categorie rămâne abstractă până când o observi. Un laborator de acasă îți permite să generezi activitatea, să colectezi telemetria și să compari alerta cu înregistrarea brută. [Videoclipul despre construirea unui centru de operațiuni de securitate](https://www.youtube.com/watch?v=s3g8o7Np1_g) prezintă configurarea completă pentru a dobândi experiență înainte de angajare.

{{< youtube id="s3g8o7Np1_g" >}}

Începe cu categoria de identitate. Creează un utilizator de test, activează jurnalizarea autentificărilor și execută o serie de autentificări eșuate și reușite. Apoi citește înregistrarea și notează câmpurile care separă utilizarea normală de exercițiu.

**Un exercițiu repetabil:**

1. **Alege o categorie** din tabelul de telemetrie de mai sus.
2. **Reproduce o versiune inofensivă** a activității pe propriul sistem sau cont de test.
3. **Colectează telemetria** generată de categorie.
4. **Scrie ideea de detectare** ca regulă, căutare salvată sau interogare.
5. **Testează regula** cu exercițiul și confirmă că se declanșează pentru comportamentul vizat.
6. **Notează limitele** regulii, inclusiv activitățile pe care nu le detectează.

Ghidul [Microsoft SOC Home Lab](/articles/microsoft-soc-home-lab-2026/) detaliază construirea mediului: licențiere, segmentarea rețelei, colectarea jurnalelor și testarea controalelor de identitate. Ghidul [Mad Hat Cyber Range](https://madhat.io/pages/cyber-range-guide) extinde aceeași idee într-un mediu de atelier, cu exerciții de atac, detectare și apărare.

Pentru un vocabular consecvent, asociază comportamentul observat cu tehnica relevantă din [MITRE ATT&CK](https://attack.mitre.org/). Consideră asocierea un ajutor pentru analist, nu o dovadă de atribuire. Păstrează evenimentul brut, interogarea, versiunea regulii și punctele oarbe cunoscute împreună cu înregistrarea exercițiului.

{{< centerbutton href="/articles/microsoft-soc-home-lab-2026/" >}}
  Citește ghidul Microsoft SOC Home Lab
{{< /centerbutton >}}

______

## Pașii următori

Începe cu o categorie și un exercițiu. Adaugă o a doua categorie după ce ai terminat și documentat prima. Scopul este să aprofundezi o investigație, nu să alcătuiești o listă de instrumente.

- **[Ghidul Microsoft SOC Home Lab](/articles/microsoft-soc-home-lab-2026/)** construiește mediul pentru aceste exerciții.
- **[Construirea unui laborator IT acasă](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/)** prezintă infrastructura de bază a unui laborator de securitate.
- **[Sfaturi pentru redactarea unui CV IT](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/)** arată cum să prezinți un laborator documentat drept experiență practică.
- **[Principalii cinci vectori de atac cibernetic și măsurile de atenuare](/articles/the-top-five-cyber-attack-vectors-and-mitigations/)** restrânge lista la cei mai frecvenți vectori.

**Materiale-sursă:** categoriile de atac și subtipurile lor urmează [prezentarea CrowdStrike a atacurilor cibernetice comune](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/common-cyberattacks/) de Kurt Baker. Linkurile despre produse și referințe duc la documentația Microsoft.

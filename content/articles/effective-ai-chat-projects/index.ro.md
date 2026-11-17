---
title: "Proiecte ChatGPT și Claude: configurează un context IA reutilizabil"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Configurează proiecte ChatGPT și Claude cu instrucțiuni clare, fișiere de referință actuale și un test simplu pentru contextul reutilizat."
genre: ["Inteligență artificială", "Productivitate"]
tags: ["proiecte ChatGPT", "proiecte Claude", "instrucțiuni pentru proiecte IA", "context IA", "configurare proiect ChatGPT", "cunoștințe de proiect Claude"]
cover: "/img/cover/effective-ai-chat-projects.webp"
coverAlt: "Două spații de lucru organizate pentru proiecte IA, cu un rezumat, fișiere de referință și conversații separate"
coverCaption: ""
---

[Înapoi la cursul Flux practic de lucru cu IA](/effective-ai-course-start/)

**Creează un proiect când mai multe conversații au același scop.** Păstrează instrucțiunile stabile și fișierele de referință aprobate într-un singur loc. Menține fiecare conversație concentrată pe o sarcină. Lecția folosește un atelier comunitar fictiv pentru exersare fără date private.

**Obiectiv de învățare:** vei crea un proiect cu două surse controlate și le vei testa informațiile într-un chat nou.

## Idei principale

- **Instrucțiunile proiectului** stabilesc un comportament reutilizabil pentru chat-urile asociate.
- **Sursele proiectului** păstrează materialele de referință pe care vrei să le consulte asistentul.
- **Istoricul conversației** înregistrează un schimb, dar nu înlocuiește o sursă aprobată.
- **Un test într-un chat nou** arată dacă setările proiectului oferă suficient context.

## Înainte să începi

**Cerințe:** un cont ChatGPT sau Claude și pachetul de sarcini din [lecția 1](/articles/effective-ai-workflow-foundations/). Rezervă 35 de minute. Nivelul este pentru începători. Folosește nume, date și locuri inventate pe tot parcursul exercițiului.

**Creează două fișiere mici** pe computer. Deschide un editor de text simplu, lipește fiecare bloc de mai jos într-un fișier separat și salvează-l cu numele `.md` indicat. Fișierele Markdown sunt text simplu. `workshop-brief.md` descrie publicul și stilul. `approved-schedule.md` conține programul oficial fictiv.

```text
workshop-brief.md, revizia 1
Public: persoane înscrise la un atelier introductiv.
Stil: propoziții scurte și un ton prietenos, factual.
Nu inventa prețuri, funcții de accesibilitate sau detalii despre parcare.
```

```text
approved-schedule.md, revizia 1
Marcajul sursei: WS-2026-11-12-R1
Eveniment: Introducere în siguranța digitală
Data: 2026-11-12
Începere: 7 p.m.
Locul: Community Room A
```

## Configurează ChatGPT

1. **Deschide „Projects”** în bara laterală ChatGPT și creează un proiect numit `Workshop Practice`.
2. **Adaugă cele două fișiere** ca surse ale proiectului.
3. **Deschide setările proiectului** și adaugă instrucțiunile de mai jos.
4. **Verifică setările de memorie și partajare** pentru contul și spațiul tău de lucru înainte să adaugi materiale reale.

```text
Folosește approved-schedule.md pentru datele evenimentului.
Folosește workshop-brief.md pentru public și stil.
Dacă lipsește o informație cerută, solicită sursa sau marcheaz-o drept necunoscută.
Scrie doar schițe. Nu le trimite și nu le publica.
Enumeră modificările factuale după fiecare schiță revizuită.
```

**Proiectele ChatGPT grupează chat-uri, fișiere și instrucțiuni asociate.** Setările proiectului și funcțiile disponibile depind de plan și de spațiul de lucru. Dacă fluxul de creare oferă memorie dedicată proiectului, alege-o pentru un test de izolare curat. Cu memoria implicită, un chat poate prelua informații din afara fișierelor încărcate. Marcajul unic de mai jos te ajută să testezi fișierul fără să tratezi un răspuns din memorie drept dovadă că fișierul a fost citit. Verifică opțiunile actuale de memorie în [ghidul oficial pentru proiectele ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

## Configurează Claude

1. **Deschide „Projects”** în Claude și creează un proiect cu același nume de exercițiu.
2. **Adaugă cele două fișiere** la cunoștințele proiectului.
3. **Setează aceleași cinci rânduri** ca instrucțiuni ale proiectului.
4. **Pornește un chat nou în proiect** pentru a testa configurarea.

**Acești pași descriu proiectele clasice Claude.** Anthropic distribuie o versiune beta separată Projects pentru unii utilizatori Pro și Max ai Claude Code. În versiunea beta, un proiect este o conversație cu fire cloud paralele. Consultă [Ce sunt proiectele?](https://support.claude.com/en/articles/9517075-what-are-projects) și urmează interfața contului tău. Instrucțiunile proiectelor clasice se aplică tuturor chat-urilor, iar cunoștințele proiectului oferă materiale de referință partajate. Folosește fișierele încărcate drept date controlate. Memoria proiectului se comportă diferit în funcție de cont și setări, așa că nu trata detaliile din alt chat drept program aprobat. Vezi setările actuale în [ghidul de configurare a proiectelor Claude](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

| Modul proiectului | Material partajat de verificat | Test nou |
|---|---|---|
| **Proiect ChatGPT** | Fișiere încărcate, instrucțiuni și modul de memorie ales | Un chat nou din proiect menționează marcajul programului |
| **Proiect clasic Claude** | Cunoștințe și instrucțiuni ale proiectului partajate între chat-uri | Un chat nou din proiect menționează marcajul programului |
| **Claude Projects beta** | Surse și context în proiect și în firele cloud | Un fir nou din proiect menționează marcajul programului |

**Un proiect grupează contextul, dar nu aprobă o sursă.** Marcajul arată dacă fișierul numit a ajuns la chat. Compară totuși data, ora și sala cu fișierul.

## Testează un chat nou

**Deschide o conversație nouă într-un proiect ChatGPT sau un chat nou într-un proiect Claude clasic.** În Claude Projects beta, folosește un fir nou din proiect. Cere un anunț scurt. Nu include programul în prompt, pentru ca sursele proiectului să furnizeze informațiile.

```text
Scrie o schiță de e-mail de 100 de cuvinte pentru atelierul următor.
Menționează fișierul-sursă și marcajul exact pentru oră și loc.
Enumeră informațiile lipsă după schiță.
Nu trimite mesajul.
```

| Rezultat | Semnificație | Pasul următor |
|---|---|---|
| **Ora, locul și marcajul corespund** | Fișierul este disponibil acestui chat | Verifică tu informațiile în fișier |
| **Un fapt este inventat** | Instrucțiunile sau folosirea sursei au eșuat | Elimină faptul și precizează cererea |
| **Sursa lipsește** | Referința nu a ajuns la acest chat | Verifică apartenența la proiect și încărcarea fișierului |
| **Apare o revizie veche** | Proiectul păstrează material învechit | Înlocuiește sursa și testează din nou |

**Nu deduce fiabilitatea dintr-un singur răspuns corect.** Memoria implicită a proiectului poate furniza o oră familiară fără să citească fișierul încărcat. Cere marcajul exact `WS-2026-11-12-R1`, apoi repetă testul cu această schiță contradictorie:

```text
Revizuiește această propoziție folosind programul aprobat al proiectului:
„Cursul Introducere în siguranța digitală începe la 6 p.m. în Community Room A.”
Menționează modificarea factuală, fișierul-sursă și marcajul. Nu trimite mesajul.
```

**Răspuns așteptat:** rândul indică ora 19 și numește `approved-schedule.md` cu marcajul `WS-2026-11-12-R1`. Notează orice eroare observi. O rulare reușită nu are nevoie de o eroare inventată.

**Exemplu de înregistrare a testului:** chat nou, primul prompt, ora 19, locul Community Room A, sursa `approved-schedule.md`, marcajul `WS-2026-11-12-R1`, trecut. Promptul de conflict, corectare de la 18 la 19, trecut. Acesta este un exemplu. Înlocuiește-l cu observațiile tale.

## Întreține proiectul

**Păstrează scurte instrucțiunile proiectului.** Pune acolo regulile stabile. Include detaliile specifice sarcinii în fiecare prompt. Înlocuiește fișierele învechite și notează reviziile lor. Mută lucrul fără legătură într-un alt proiect pentru a evita conflictele între surse.

**Înainte să partajezi un proiect,** verifică fișierele, chat-urile, instrucțiunile și lista de acces. Un proiect este un spațiu de lucru, nu un sistem de aprobare. Chiar și un fișier numit „approved” are nevoie de un responsabil real și de un istoric al reviziilor pentru lucrări importante.

## Exersează și verifică

**Rezultatul tău:** un proiect cu două fișiere sursă sintetice, cinci rânduri de instrucțiuni și o scurtă înregistrare a testului. Notează ora și locul observate, numele și marcajul sursei și orice fapt inventat. Șterge proiectul de practică după ce termini dacă nu mai ai nevoie de el.

**Raționament așteptat:** un chat nou folosește sursele proiectului pentru fapte stabile, iar promptul definește rezultatul imediat. Verifică răspunsul în fișier. Dacă lipsește o sursă sau apare o revizie greșită, revino la configurarea proiectului.

## Verifică ce ai înțeles

1. **Întrebare:** un chat nou într-un proiect ChatGPT garantează izolarea pentru orice setare de memorie? **Răspuns:** nu. Verifică modul de memorie al proiectului și testează cu un marcaj unic al sursei.

2. **Întrebare:** ce faci când proiectul repetă un program vechi? **Răspuns:** verifică sursa atașată și aria memoriei, apoi înlocuiește materialul învechit.

## Depanare

- **Lipsesc comenzile proiectului:** verifică planul actual și setările spațiului de lucru în ghidul furnizorului.
- **Răspunsuri contradictorii:** elimină fișierele sursă duplicate sau învechite și pornește un chat nou.
- **Partajare neașteptată:** verifică membrii proiectului și elimină sursele sensibile înainte de a continua.
- **Abateri repetate de stil:** scurtează instrucțiunile și oferă un exemplu scurt în promptul sarcinii.

## Pașii următori

**Continuă cu [Contextul depozitului în AGENTS.md](/articles/effective-ai-agents-md-context/)**. Următoarea lecție trece de la un proiect de chat la un depozit local de cod.

**Navigarea cursului:** [Anterior: Bazele fluxului de lucru](/articles/effective-ai-workflow-foundations/), [Structura cursului](/effective-ai-course-start/).

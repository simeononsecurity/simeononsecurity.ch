---
title: "Pachete de sarcini AI: instrucțiuni mai bune și criterii de acceptare"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Transformă cererile vagi adresate AI-ului în pachete de sarcini cu rezultat, sursă, domeniu al fișierelor, verificări și condiție de oprire definite."
genre: ["Inteligență artificială", "Productivitate", "Inginerie software"]
tags: ["scrierea instrucțiunilor AI", "pachet de sarcini", "instrucțiune pentru agent de programare", "criterii de acceptare", "flux de lucru AI", "instrucțiuni pentru agenți AI"]
cover: "/img/cover/effective-ai-task-packets.webp"
coverAlt: "O cerere vagă rescrisă ca pachet scurt de sarcini cu sursă, domeniu, verificare și condiție de oprire"
coverCaption: ""
---

[Înapoi la cursul practic despre fluxurile de lucru AI](/effective-ai-course-start/)

**O instrucțiune bună descrie munca și modul în care îi vei evalua rezultatul.** Mai multe cuvinte nu rezolvă lipsa unui domeniu clar. Această lecție transformă o cerere vagă într-un pachet de sarcini pentru laboratorul cursului.

**Obiectiv de învățare:** vei scrie un pachet de sarcini delimitat, cu sursă, domeniu al fișierelor, verificări și condiție de oprire.

## Idei principale

- **Rezultatul** numește artefactul sau comportamentul dorit.
- **Domeniul** numește fișierele permise și acțiunile excluse.
- **Sursa** identifică cerința aprobată.
- **Criteriile de acceptare** fac succesul observabil.
- **Condițiile de oprire** împiedică presupunerile și lucrul ulterior neautorizat.

## Înainte de a începe

**Cerințe preliminare:** laboratorul extras, fișierul său `docs/requirements.md` și [lecția despre contextul depozitului](/articles/effective-ai-agents-md-context/). Rezervă 30 de minute. Nivelul este începător. Exercițiul se încheie cu un pachet scris. Deocamdată nu trebuie să editezi cod.

## Compară două cereri

**Cerere vagă:** „Îmbunătățește scriptul pentru sarcini.” Un agent ar putea rescrie ieșirea, adăuga dependențe, edita datele de exemplu sau sări peste teste. Cererea nu stabilește niciuna dintre aceste alegeri.

**Cerere delimitată:** „Adaugă un filtru opțional de stare în `task_report.py`, conform reviziei 1 din `docs/requirements.md`. Păstrează ieșirea implicită. Adaugă teste. Nu modifica datele de exemplu. Oprește-te înainte de commit.” Agentul decide în continuare detaliile implementării, iar sarcina definește succesul.

| Parte a pachetului | Exemplu din laborator | Verificare |
|---|---|---|
| **Rezultat** | Adaugă `--status` în raport | Funcționează ambele valori acceptate |
| **Sursă** | `docs/requirements.md`, revizia 1 | Codul corespunde valorilor aprobate |
| **Domeniu** | Doar programul și testele | Diff-ul nu conține alte fișiere |
| **Constrângeri** | Păstrează ieșirea implicită și datele de exemplu | Ieșirea de bază rămâne `Total tasks: 4` |
| **Dovezi** | Comanda de testare și rulări manuale | Ieșirile corespund numărătorilor așteptate |
| **Oprire** | Nu face commit sau push | Istoricul Git și depozitul la distanță rămân neschimbate |

## Folosește un șablon reutilizabil

**Copiază acest șablon** pentru o sarcină mică de programare sau cercetare. Elimină câmpurile irelevante în loc să le completezi cu formulări vagi.

```text
Outcome:
Authoritative source and revision:
Relevant files or records:
Allowed changes:
Excluded changes and actions:
Examples of desired behavior:
Completion checks:
Stop or ask when:
Report back with:
```

**Pentru laborator,** pachetul completat arată astfel:

```text
Outcome: Add an optional --status filter to task_report.py.
Source: docs/requirements.md, revision 1.
Relevant files: task_report.py, tasks.json, tests/.
Allowed changes: task_report.py and focused tests.
Excluded: tasks.json, new dependencies, commits, pushes.
Examples: no filter prints Total tasks: 4. Open and done each print 2.
Checks: run unit tests and four manual commands: no filter, open, done, and invalid.
The invalid value must exit nonzero with a clear error.
Stop or ask: source conflict, missing file, unrelated failing baseline.
Report: changed files, commands, observed outputs, unresolved issues.
```

**Pe Windows,** folosește `py -3` în comenzile din pachet dacă mediul tău folosește lansatorul Python.

**Pachetul nu prescrie fiecare linie de cod.** Agentul alege o implementare restrânsă, iar rezultatul rămâne verificabil.

## Adaugă exemple cu atenție

**Un exemplu exact elimină ambiguitatea.** Exemplele `open` și `done` precizează ieșirea pentru fișierul furnizat, cu patru sarcini. Nu stabilesc o regulă generală pentru toate fișierele. Pentru alt fișier, numărătorile depind de înregistrările sale.

**Separă rezultatul așteptat de cel observat.** Înainte de rularea programului, `Total tasks: 2` este rezultatul așteptat pentru fiecare stare. După rulare, ieșirea terminalului devine o observație. Dacă valorile diferă, verifică datele și implementarea înainte să declari succesul.

## Exersează o condiție de oprire

**Presupune că lipsește fișierul cu cerințe.** Pachetul îl numește drept sursă aprobată. Oprește-te și cere cerința în loc să deduci valorile acceptate dintr-o conversație veche sau dintr-o problemă exemplu.

**Presupune că testele de bază eșuează înainte de editare.** Înregistrează eșecul și întreabă dacă starea inițială trebuie reparată mai întâi. O rulare reușită ulterioară nu arată dacă filtrul sau starea inițială a produs diferența.

**Presupune că agentul vrea să facă un commit.** Pachetul exclude commiturile. Cere-i să se oprească după diff și teste. Tu decizi dacă un commit ulterior se potrivește fluxului proiectului.

## Verifică pachetul

**Acordă un punct pentru fiecare răspuns:** rezultatul este concret? Sursa de referință este numită? Domeniul fișierelor este clar? Sunt precizate cel puțin două verificări observabile? Există o condiție de oprire? Un scor sub cinci înseamnă că trebuie să revizuiești pachetul înainte de delegare.

**Rezultatul tău:** salvează pachetul final și o explicație de o propoziție pentru o condiție de oprire. Predă-l unui agent de programare la următoarea lecție practică sau răspunde manual la rezultatele așteptate pe traseul de studiu.

## Verifică ce ai înțeles

1. **Întrebare:** ce face un pachet de sarcini verificabil? **Răspuns:** O sursă, fișiere permise, verificări observabile și o condiție de oprire.
2. **Întrebare:** ce trebuie să facă agentul când sursei îi lipsește un detaliu necesar? **Răspuns:** Să se oprească și să raporteze detaliul lipsă în loc să îl inventeze.

## Depanare

- **Agentul schimbă prea multe:** numește fișierele și acțiunile excluse în pachet.
- **Agentul pune multe întrebări:** oferă sursa lipsă sau un exemplu concret.
- **Agentul declară succesul prea devreme:** cere ieșirile observate ale comenzilor și inspectează fișierele.
- **Pachetul devine prea lung:** înlocuiește materialul copiat din sursă cu calea și revizia.

## Pașii următori

**Continuă cu [Prima ta sarcină cu un agent de programare](/articles/effective-ai-coding-agent-first-task/)**. Folosește pachetul pentru a ghida o mică modificare în laborator.

**Navigarea cursului:** [Anterior: Contextul depozitului](/articles/effective-ai-agents-md-context/), [Structura cursului](/effective-ai-course-start/).

---
title: "Gestionarea ferestrei de context AI: menține agenții de programare concentrați"
description: "Controlează contextul activ al unei sarcini AI cu fișiere selectate, predări concise și rezultate scurte de la lucrători, păstrând deciziile și dovezile."
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
genre: ["Inteligență artificială", "Inginerie software"]
tags: ["gestionarea ferestrei de context AI", "context pentru agent de programare", "predare AI", "compactarea contextului", "orchestrarea agenților", "buget de tokeni"]
cover: "/img/cover/effective-ai-context-window-management.webp"
coverAlt: "O notă concisă de predare lângă fișiere de proiect selectate și o transcriere de chat mult mai lungă, eliminată"
coverCaption: ""
---

[Înapoi la cursul practic de fluxuri de lucru cu AI](/effective-ai-course-start/)

**Fereastra de context conține textul și alte materiale pe care un model le procesează în tura curentă.** Instrucțiunile, definițiile instrumentelor, fragmentele de fișiere, rezultatele instrumentelor și istoricul conversației ocupă spațiu. Lecția arată cum să păstrezi următoarea sarcină concentrată și să lași o predare de lucru de încredere.

**Obiectiv de învățare:** creează o predare de lucru concisă și testeaz-o într-o sesiune nouă.

## Idei principale

- **Tokenii** sunt unitățile folosite de un model pentru a procesa intrări și ieșiri.
- **Contextul activ** este materialul disponibil într-o tură, în limitele produsului.
- **Sursele durabile** sunt fișierele sau înregistrările proiectului păstrate în afara chatului.
- **Compactarea** rezumă sau elimină contextul vechi și poate omite un detaliu necesar.
- **Predarea de lucru** indică unei sesiuni noi sursele curente și munca verificată.

## Înainte să începi

**Cerințe preliminare:** laboratorul editat de la [prima sarcină cu un agent de programare](/articles/effective-ai-coding-agent-first-task/), cerința aprobată și [lecția despre pachetele de sarcini](/articles/effective-ai-task-packets/). Dacă ai folosit traseul de studiu, lucrează cu laboratorul editat manual. Rezervă 35 de minute. Dificultatea este intermediară. Păstrează notițele cursului în afara directorului extras al laboratorului, astfel încât `git status` să arate doar modificările de cod.

## Selectează contextul în funcție de sarcină

**Pentru editarea filtrului de stare,** agentul are nevoie de `task_report.py`, `docs/requirements.md`, testele relevante și un eșantion mic din `tasks.json`. Nu are nevoie de toate conversațiile vechi, de întreaga documentație a site-ului sau de istoricul Git complet. Consultă mai întâi o hartă, apoi încarcă doar fișierele necesare următoarei decizii.

| Sarcină | Context util | Context în exces |
|---|---|---|
| **Definirea comportamentului** | Cerința aprobată și un eșantion de date | Conversații vechi de explorare |
| **Editarea programului** | Programul și teste specifice | Directoare de proiect fără legătură |
| **Revizuirea rezultatului** | Diferențele, rezultatul testelor și cerința | Transcrierea completă a agentului |
| **Reluarea ulterioară** | Nota de predare și căile surselor | O conversație de câteva ore lipită integral |

**Aceasta este o alegere de recuperare a informației, nu o regulă de ascundere a dovezilor.** Dacă un test eșuează, include rezultatul exact și fișierul implicat. Elimină jurnalele irelevante, nu detaliile necesare diagnosticării.

**Ia în calcul costul fix înainte să adaugi lucrători.** Instrucțiunile agentului și schemele instrumentelor disponibile pot ocupa context înainte de citirea unui fișier de sarcină. Un al doilea lucrător repetă o parte din acest cost și adaugă un raport pe care agentul principal trebuie să-l revizuiască. Pentru editarea a două fișiere, folosește un agent. Pentru o căutare independentă în multe surse, un raport scurt poate reduce contextul sesiunii principale, chiar dacă utilizarea totală de tokeni crește.

## Creează o predare concisă

**O predare de lucru este o înregistrare scurtă pentru sesiunea următoare.** Separă munca încheiată de cea propusă. Salvează exemplul în `course-notes/handoff.md`, în afara laboratorului, și înlocuiește observațiile fictive cu ale tale.

```text
Obiectiv: adaugă --status open|done la raportul de sarcini al cursului.
Sursă: docs/requirements.md, revizia 1.
Spațiu de lucru: folderul extras effective-ai-course-lab.
Stare curentă: filtrul de stare este în task_report.py și în teste.
Verificat: notează rezultatul observat al testelor și numărătorile manuale 4, 2 și 2.
Decizie: tasks.json a rămas neschimbat.
În așteptare: revizuirea independentă a diff-ului și a sursei.
Următoarea verificare: rulează din nou testele și cazul pentru stare invalidă.
Oprește-te dacă: cerința sau valoarea de bază diferă de această evidență.
```

**Exemplul nu afirmă că ai efectuat acea muncă.** Notează rezultatele observate la teste și fișierele modificate. Dacă se schimbă revizia sursei, actualizează predarea după ce recitești sursa.

## Testează o sesiune nouă

**Pornește un chat nou sau o sesiune nouă de agent de programare** în laborator. În chat, lipește predarea și fișierul `AGENTS.md` din laboratorul sintetic, apoi numește fișierele pe care trebuie să le inspecteze. Într-un agent de programare, deschide directorul laboratorului și lipește predarea, acordând acces de citire la fișierele indicate. Cere-i:

```text
Folosind această predare și fișierele curente ale depozitului, numește valorile de stare aprobate, numărul de bază și următoarea verificare. Nu edita.
Dacă predarea contrazice o sursă curentă, raportează conflictul.
```

**Raționament așteptat:** sesiunea nouă găsește `open` și `done` în `docs/requirements.md`, identifică valoarea de bază 4 și numește testele și verificările manuale. Dacă repetă valoarea veche `pending`, recitește cerința și corectează predarea.

## Păstrează orchestratorul suplu

**Orchestratorul este agentul principal care coordonează lucrătorii.** Dă fiecărui lucrător o întrebare clar delimitată și fișiere de intrare numite. Cere un rezultat scurt: constatare, cale către dovezi, nivel de încredere și problemă nerezolvată. Păstrează jurnalele detaliate într-un fișier sau în sesiunea lucrătorului. Adu înapoi doar informația de care agentul principal are nevoie pentru următoarea decizie.

**Exemplu:** cere unui lucrător cu acces doar la citire să verifice testele și să răspundă „caz lipsă, fișier și linie, verificare propusă”. Nu-i cere să lipească toate testele în chatul principal. Agentul principal verifică apoi constatarea în depozit înainte de editare. [Lecția despre delegare](/articles/effective-ai-agent-delegation/) adaugă o sarcină independentă când amploarea justifică efortul.

**În multe produse, sesiunile lucrătorilor au context propriu,** dar moștenirea și izolarea diferă. Verifică regulile curente ale produsului înainte să presupui că un lucrător vede aceleași instrucțiuni, fișiere sau instrumente ca agentul principal. Ghidurile pentru [subagenții Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents) și [subagenții Claude Code](https://code.claude.com/docs/en/sub-agents) descriu comportamentul fiecărui produs.

## Folosește compactarea cu grijă

**Compactarea scurtează istoricul activ.** Codex, Claude Code și OpenCode diferă în privința momentului și modului de compactare. Tratează un rezumat compactat ca ajutor pentru continuare, nu ca dosar complet al proiectului. Păstrează cerințele și deciziile în fișiere, apoi verifică-le din nou după compactare. Consultă informațiile actuale despre [bunele practici Codex](https://learn.chatgpt.com/docs/learn/best-practices), [comenzile Claude Code](https://code.claude.com/docs/en/commands) și [compactarea OpenCode 2](https://opencode.ai/v2/docs/compaction). OpenCode 1 și OpenCode 2 folosesc scheme diferite. Verifică `opencode --version` înainte să copiezi setările.

**Dacă asistentul pierde o constrângere,** oprește editarea, redeschide sursa și reformulează pachetul de sarcină. O sesiune nouă cu o predare scurtă și verificată necesită adesea mai puțină atenție decât corectarea repetată a unui chat lung și confuz.

## Exersează și verifică

**Artefactul tău:** o predare de lucru sub 180 de cuvinte, salvată în afara laboratorului. Marchează fiecare rând ca sursă, rezultat observat, decizie sau acțiune în așteptare. Dă predarea unei sesiuni noi și notează dacă identifică ambele valori de stare acceptate și următoarea verificare.

**Verificare finală:** sesiunea nouă numește `open`, `done`, valoarea de bază 4 și un pas de testare fără să se bazeze pe chatul vechi. Corectează omisiunile și testează din nou într-o altă sesiune nouă.

## Verifică înțelegerea

1. **Întrebare:** ce trebuie să conțină o predare pentru o sesiune nouă? **Răspuns:** obiectivul, sursa autorizată, starea actuală, rezultatul verificat și acțiunea următoare.

2. **Întrebare:** de ce este util un raport scurt al lucrătorului? **Răspuns:** un raport concis cu dovezi oferă orchestratorului rezultatul necesar fără repetarea transcrierii lucrătorului.

## Depanare

- **Rezumatul omite o decizie:** adaugă o linie scurtă cu decizia și revizia sursei.
- **Răspunsul lucrătorului este prea lung:** cere un tabel limitat de dovezi și referințe la fișiere.
- **Predarea este învechită:** recitește fișierele sursă actuale înainte de editare.
- **Presiunea asupra contextului continuă:** împarte sarcina în sesiuni mai mici, cu artefacte separate.

## Pașii următori

**Continuă cu [Configurarea serverului MCP](/articles/effective-ai-mcp-server-setup/)**. Vei adăuga un instrument extern cu acces doar la citire și îi vei limita rezultatul.

**Navigarea cursului:** [Anterior: Prima sarcină de programare](/articles/effective-ai-coding-agent-first-task/), [Structura cursului](/effective-ai-course-start/).

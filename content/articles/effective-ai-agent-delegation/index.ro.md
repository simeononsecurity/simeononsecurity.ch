---
title: "Delegarea agenților AI: atribuirea sarcinilor și revizuirea rezultatelor"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Decide când ajută un al doilea agent AI, oferă fiecărui lucrător o sarcină delimitată, previne conflictele de editare și integrează dovezile în sesiunea principală."
genre: ["Inteligență artificială", "Inginerie software"]
tags: ["delegarea agenților AI", "subagenți", "agenți lucrători", "contextul orchestratorului", "worktree-uri AI", "sarcini AI paralele"]
cover: "/img/cover/effective-ai-agent-delegation.webp"
coverAlt: "Un agent principal atribuie separat sarcini de cercetare și revizuire a testelor, apoi reunește rapoarte scurte cu dovezi"
coverCaption: ""
---

[Înapoi la cursul practic despre fluxurile de lucru AI](/effective-ai-course-start/)

**Deleagă atunci când o întrebare independentă justifică o sesiune separată.** Un agent lucrător inspectează surse, revizuiește teste sau pregătește o modificare limitată în propriul context. Agentul principal verifică și integrează rezultatul. Această lecție compară documentații, în timp ce sesiunea principală păstrează sarcina mică de laborator.

**Obiectiv de învățare:** vei atribui o revizuire independentă unui lucrător și vei verifica scurtul său raport cu dovezi.

## Idei principale

- **Orchestrator:** agentul principal care coordonează sarcina și revizuirea finală.
- **Lucrător:** agent separat responsabil de un singur rezultat delimitat.
- **Lucru independent:** o sub-sarcină al cărei răspuns nu depinde de rezultatul neterminat al altui lucrător.
- **Responsabilitate:** un fișier sau o întrebare nominalizată și atribuită unui singur lucrător.
- **Integrare:** comparația făcută de agentul principal între rezultatul lucrătorului și sursele actuale.

## Înainte de a începe

**Cerințe preliminare:** înregistrările tale de [predare a contextului](/articles/effective-ai-context-window-management/) și [verificare a rezultatului](/articles/effective-ai-output-verification/). Rezervă 40 de minute. Dificultate medie. Ruta conectată necesită un produs cu suport pentru lucrători. Ruta de studiu folosește un chat separat și integrare manuală.

**Începe această lecție dintr-un starter curat.** Salvează în afara laboratorului diff-ul filtrului editat și registrul testelor. Extrage ZIP-ul original într-un dosar temporar nou. Rulează comanda de pornire și cele două teste de bază. Repetă baza Git din lecția de configurare a cursului și recreează îndrumările scurte `AGENTS.md` și opționalul `CLAUDE.md` din lecția despre contextul depozitului. Fă chiar tu commit pentru aceste fișiere de îndrumare, apoi confirmă că `git status --short` este curat. Păstrează copia filtrului editat ca referință, dar efectuează exercițiul lucrătorului pe starterul curat.

## Decide dacă delegi

**Folosește un singur agent** pentru o editare secvențială mică. Delegarea implică costuri de configurare, tokenuri și revizuire. Folosește un lucrător când o întrebare independentă, doar pentru citire, ar umple altfel chatul principal cu multe fișiere sau pagini-sursă.

| Sarcină de laborator | Delegi? | Motiv |
|---|---|---|
| **Adaugă un filtru cu două valori** | De obicei nu | Un fișier mic și teste focalizate |
| **Găsește cazuri lipsă în două teste de bază** | De obicei nu | Sesiunea principală citește mai repede un fișier scurt |
| **Compară documentația actuală a trei produse** | Da, doar citire | Citirea surselor rămâne în contextul lucrătorului |
| **Editează aceeași funcție de două ori** | Nu | Editările simultane creează conflicte |

**Lucrătorul ar trebui să primească mai puțin context decât orchestratorul,** nu o copie a întregii conversații. Oferă-i obiectivul, calea sursei, limitele sarcinii și formatul răspunsului. Păstrează un raport scurt cu dovezi în sesiunea principală. Verifică singur fișierele citate înainte de a acționa.

## Rulează un lucrător cu acces doar la citire

**Păstrează mică sarcina principală.** În sesiunea principală, citește `AGENTS.md` local și notează fișierul care conține comanda de test. Atribuie întrebarea separată de cercetare de mai jos unui lucrător. Nu are nevoie de întregul laborator sau de chatul anterior.

**Ruta conectată:** în Codex, Claude Code sau alt client cu suport pentru lucrători, deschide laboratorul ca proiect și cere agentului principal să delege solicitarea următoare, doar pentru citire, unui lucrător. Verifică transcrierea instrumentelor pentru pornirea reală a unui lucrător și raportul primit. Dacă produsul nu expune un lucrător, folosește o sesiune separată și identific-o drept sesiune separată de lucrător. Ghidurile actuale pentru [subagenții Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), [subagenții Claude Code](https://code.claude.com/docs/en/sub-agents) și [agenții OpenCode](https://opencode.ai/docs/agents/) descriu comenzile curente.

**Ruta de studiu:** deschide un chat nou pentru aceeași solicitare. Oferă-i cele trei linkuri oficiale sau fragmentele surselor. Etichetează-l drept lucrător simulat. Un al doilea chat este un context separat, nu dovada executării unui subagent nativ.

```text
Folosește documentația oficială actuală Codex AGENTS.md, Claude Code memory și OpenCode rules.
Compară modul în care fiecare produs încarcă fișierele de instrucțiuni ale depozitului.
Nu edita fișiere.
Returnează cel mult trei rânduri: produs, fișier de instrucțiuni, URL-sursă și un comportament de încărcare.
Semnalează incertitudinea. Nu copia pagini întregi.
```

**Setul de surse:** [instrucțiuni de proiect Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [memorie Claude Code](https://code.claude.com/docs/en/memory) și [reguli OpenCode](https://opencode.ai/docs/rules/). Raportul așteptat menționează `AGENTS.md` pentru Codex și OpenCode. Versiunile actuale Claude Code încarcă direct `AGENTS.md` când `CLAUDE.md` sau `CLAUDE.local.md` nu au prioritate. Acest laborator folosește un fișier `CLAUDE.md` cu importul `@AGENTS.md`, care acceptă și sesiuni mai vechi sau configurate diferit. Verifică paginile actuale și versiunea activă înainte de a trata exemplul ca rezultat observat al unui lucrător.

## Integrează constatările

**Deschide singur paginile-sursă citate.** Dacă lucrătorul afirmă că Claude Code necesită întotdeauna un import `CLAUDE.md`, verifică ghidul său memory și corectează raportul. Compară-l cu fișierele locale de îndrumare. Scrie o notă scurtă de integrare:

```text
Acceptat: Codex și OpenCode folosesc AGENTS.md pentru îndrumarea proiectului.
Versiunile actuale Claude Code pot încărca direct AGENTS.md. Acest laborator folosește
CLAUDE.md cu importul @AGENTS.md pentru o hartă comună stabilă.
Dovezi: notează cele trei URL-uri oficiale actuale și data revizuirii.
Decizie: păstrează o hartă comună scurtă și un import Claude.
```

**Această notă este rezultatul util al lucrătorului.** Orchestratorul are nevoie de constatări verificate și căi către surse, nu de transcrierea cercetării. Delegarea consumă mai multe tokenuri în total, deci păstrează conversația principală scurtă doar când sesiunea separată economisește atenție.

## Atribuie responsabilitatea editărilor

**Dacă lucrătorii editează fișiere,** împarte responsabilitatea pe fișiere sau folosește worktree-uri separate pentru activități de depozit care se suprapun. Un worktree este o altă copie a aceluiași depozit Git, cu propriile fișiere de lucru. Separă editările simultane. Agentul principal revizuiește și transferă modificările printr-un merge, cherry-pick sau patch explicit, apoi rulează din nou testele în arborele integrat.

| Lucrător | Muncă atribuită | Returnează |
|---|---|---|
| **Implementare** | `task_report.py` | Diff și comanda de test |
| **Autor de teste** | `tests/test_task_report.py` | Cazuri de test și rezultat observat |
| **Orchestrator** | Cerințe și integrare finală | Diff combinat și criterii de acceptare |

**Laboratorul mic nu are nevoie de editări paralele.** Acest tabel explică un tipar de responsabilități pentru activități mai mari. Testele dintr-un worktree nu validează o implementare încă izolată în altul. Dacă doi lucrători au nevoie de aceeași funcție, lucrează în serie sau cere unuia o revizuire fără editare. Worktree-urile separate previn coliziunile fișierelor, dar nu rezolvă cerințe contradictorii.

## Verifică comportamentul produsului

**Subagenții diferă în funcție de gazdă.** Codex, Claude Code și OpenCode diferă prin moștenirea contextului, permisiunile instrumentelor și livrarea rezultatelor. Citește ghidurile pentru [subagenți Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), [subagenți Claude Code](https://code.claude.com/docs/en/sub-agents) și [agenți OpenCode](https://opencode.ai/docs/agents/) pentru produsul instalat. Nu presupune că un lucrător împarte tot contextul sesiunii principale sau folosește un worktree izolat.

## Exersează și verifică

**Rezultatul tău:** un raport scurt al unui lucrător despre documentație și o notă de integrare. Pe ruta de studiu, folosește un chat nou și identifică-l drept lucrător simulat. Nu pretinde că ai executat un subagent nativ pe această rută.

**Verificarea finalizării:** raportul numește trei surse oficiale, rămâne în limitele întrebării și respectă limita de lungime. Nota de integrare verifică sursele și numește fișierele de îndrumare folosite de laborator.

## Verifică înțelegerea

1. **Întrebare:** Când ajută un lucrător mai mult decât un singur agent? **Răspuns:** Când deține o întrebare sau un rezultat independent și oferă un raport util cu dovezi.

2. **Întrebare:** Ce trebuie să se întâmple după ce doi lucrători ating fișiere care se suprapun? **Răspuns:** Integrează modificările, inspectează diff-ul combinat și rulează din nou verificările.

## Depanare

- **Lucrătorul returnează o transcriere lungă:** cere un tabel mai scurt cu dovezi și referințe către fișiere.
- **Lucrătorii nu sunt de acord:** recitește fișierul autoritativ înainte de a alege un răspuns.
- **Două editări se suprapun:** oprește una și stabilește responsabilitatea fișierelor sau separă worktree-urile.
- **Accesul lucrătorului la instrumente diferă:** verifică permisiunile sale în loc să presupui că sunt ca ale agentului principal.

## Pașii următori

**Continuă cu [buclă de obiective delimitate](/articles/effective-ai-bounded-agent-loops/).** Pentru guvernanța echipei dincolo de acest laborator mic, folosește [cursul de implementare a colaborării AI](/ai-collaboration-course-start/).

**Navigarea cursului:** [Anterior: verificarea rezultatului](/articles/effective-ai-output-verification/), [Structura cursului](/effective-ai-course-start/).

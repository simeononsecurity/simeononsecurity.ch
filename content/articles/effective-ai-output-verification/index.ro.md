---
title: "Cum verifici rezultatele IA, sursele, testele și costurile"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Creează o înregistrare de acceptare pentru un rezultat IA, verificând sursele, domeniul fișierelor, dovezile testelor, confidențialitatea și utilizarea."
genre: ["Inteligență artificială", "Inginerie software"]
tags: ["verificarea rezultatelor IA", "verificarea faptelor cu IA", "revizuirea agentului de programare", "dovezi ale testelor IA", "urmărirea costurilor IA", "revizuire umană"]
cover: "/img/cover/effective-ai-output-verification.webp"
coverAlt: "O fișă de revizuire compară o afirmație IA cu un fișier sursă, un diff de cod, rezultatele testelor și totalul de utilizare"
coverCaption: ""
---

[Înapoi la cursul Flux de lucru practic cu IA](/effective-ai-course-start/)

**Acceptă un rezultat IA numai după ce verifici dovezile potrivite pentru sarcină.** O explicație bine formulată, un instrument configurat și un indicator verde al testelor răspund la întrebări diferite. Această lecție creează o singură înregistrare de verificare pentru laboratorul atelierului.

**Obiectiv de învățare:** vei crea o înregistrare de acceptare pentru surse, domeniul fișierelor, teste, confidențialitate și utilizare.

## Idei principale

- **Verificarea surselor:** compară o afirmație factuală cu o sursă actuală și autoritară.
- **Verificarea domeniului:** inspectează fișierele sau sistemele modificate.
- **Verificarea comportamentului:** rulează teste și cazuri manuale relevante.
- **Verificarea confidențialității:** inspectează materialele primite de instrument sau furnizor.
- **Verificarea utilizării:** înregistrează tokenii, apelurile instrumentelor și tariful folosit la calculul costului.

## Înainte să începi

**Cerințe preliminare:** laboratorul cursului, `docs/requirements.md`, un snapshot Git local și [lecția MCP](/articles/effective-ai-mcp-server-setup/) sau alternativa în browser. Alocă 40 de minute. Dificultatea este intermediară. Folosește laboratorul editat în prima sarcină cu un agent de programare. Dacă ai omis editarea, folosește o extracție nouă și marchează verificările funcțiilor ca neimplementate. Versiunea inițială neatinsă trece în continuare cele două teste originale.

## Verifică o afirmație factuală

**Afirmație:** „Valorile de stare aprobate sunt `open` și `pending`.” Deschide `docs/requirements.md`, revizia 1. Documentul indică `open` și `done`. Afirmația este greșită. Un ton sigur nu schimbă cerința.

**Pentru afirmațiile despre produse,** folosește documentația oficială actuală și notează titlul paginii și data verificării. O afirmație despre un meniu, un plan, o comandă sau o limită de context se învechește mai repede decât un principiu general de flux de lucru. [Documentația Codex](https://learn.chatgpt.com/docs/codex/cli), [documentația Claude Code](https://code.claude.com/docs/en/overview) și [documentația OpenCode](https://opencode.ai/docs/) descriu interfețele actuale.

| Afirmație | Sursă | Decizie |
|---|---|---|
| **`open` și `pending`** | Cerința laboratorului, revizia 1 | Respinge, înlocuiește `pending` cu `done` |
| **Numărul fără filtru este 4** | Programul de bază și patru intrări JSON | Verifică rulând programul |
| **A avut loc o citire MCP** | Transcrierea instrumentelor sesiunii | Acceptă numai dacă este vizibil un apel al instrumentului |

## Inspectează modificarea

**Pentru o sarcină de programare,** folosește Git pentru a lista fișierele modificate și a citi diff-ul real. Un fișier nou, neurmărit, apare în status chiar dacă nu apare într-un diff obișnuit, așa că inspectează ambele.

```bash
git status --short
git diff -- task_report.py tests
```

**Domeniul așteptat:** după sarcina cu filtrul se schimbă doar `task_report.py` și testele dedicate. O modificare în `tasks.json`, `docs/requirements.md` sau într-un fișier de configurare ascuns necesită o explicație și o verificare separată. Dacă nu ai făcut o editare, nu ar trebui să existe modificări.

## Testează comportamentul

**Rulează aceleași verificări de bază și ale funcțiilor** din directorul extras al laboratorului. Raportul de finalizare al agentului trebuie să includă rezultatele observate.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**În copia editată,** testele acoperă cazurile noi, numărătorile sunt 4, 2 și 2, iar valoarea nevalidă produce o eroare clară și un cod de ieșire nenul. Într-o copie inițială nouă, trec numai cele două teste de bază, iar totalul este 4. Înregistrează separat starea inițială.

**Un test de funcție eșuat trebuie diagnosticat.** Dacă `open` afișează 4, verifică dacă argumentul filtrului ajunge la funcția de numărare și dacă programul compară câmpul `status` al sarcinii. Nu declara reușit un test eșuat doar pentru că agentul afirmă că a terminat implementarea.

## Verifică confidențialitatea și accesul

**Înregistrează ce fișiere a primit agentul.** Laboratorul conține date sintetice și niciun secret. Un proiect real ar putea conține date de autentificare, date despre clienți sau documente private. Înainte de a partaja rezultatul, inspectează prompturile, jurnalele, capturile de ecran și diff-urile pentru astfel de valori.

**Un test local demonstrează doar comportamentul local.** Nu demonstrează permisiunile unui cont cloud, domeniul unui server MCP sau comportamentul unui serviciu implementat. Testează fiecare limită în mediul relevant.

## Înregistrează utilizarea și costurile

**Tokenii măsoară volumul de intrare și ieșire al modelului.** Tablourile de bord diferă, așa că folosește cifrele de utilizare afișate de furnizorul tău. Înregistrează separat apelurile instrumentelor și costurile pentru imagini sau medii găzduite, când se aplică. Verifică tarifele actuale înainte să calculezi o factură reală.

**Deschide vizualizarea de utilizare pentru contul care a executat sarcina.** Notează tokenii de intrare și ieșire afișați, modelul, perioada de facturare și orice categorie de intrare memorată în cache. Pentru abonamentele ChatGPT sau Claude, o limită ori o alocație de utilizare nu este același lucru cu un cost API per sarcină. Pentru o execuție OpenCode prin API sau furnizor, consultă utilizarea sau facturarea furnizorului și tariful actual. Dacă produsul nu afișează tokeni per sarcină, scrie „indisponibil” și nu deduce costuri din lungimea conversației.

**Calcul ilustrativ, nu tarif de furnizor:** 30.000 de tokeni de intrare la 1 $ per milion costă 0,03 $. 5.000 de tokeni de ieșire la 5 $ per milion costă 0,025 $. Costul combinat al modelului în acest exemplu este 0,055 $, înainte de costurile instrumentelor sau găzduirii.

```text
cost de intrare = tokeni de intrare / 1.000.000 × tarif de intrare
cost de ieșire = tokeni de ieșire / 1.000.000 × tarif de ieșire
total = cost de intrare + cost de ieșire + costuri separate ale instrumentelor
```

**O sarcină delegată consumă și ea tokeni.** Delegarea mută rezultatele detaliate în afara conversației principale, dar nu face munca gratuită. Compară costul cu valoarea verificării independente.

**Păstrează separat categoriile de cost.** Intrarea memorată în cache, intrarea nouă, ieșirea, apelurile instrumentelor și execuția găzduită pot avea tarife diferite. Acest exemplu folosește doar tarifele pentru intrare nouă și ieșire. Nu spune nimic despre o factură de abonament sau o taxă de instrument.

## Păstrează o înregistrare de acceptare

| Câmp | Exemplu completat după editare |
|---|---|
| **Sursă** | `docs/requirements.md`, revizia 1, citită |
| **Fișiere modificate** | `task_report.py` și `tests/test_task_report.py` în `git status --short` |
| **Teste** | Testele de bază și noile teste de filtru au trecut, notează numărul observat |
| **Rezultat manual** | S-au observat `Total tasks: 4`, `2` și `2`, valoarea invalidă a fost respinsă |
| **Starea funcției** | `--status open` și `--status done` implementate |
| **Confidențialitate** | Numai fișiere sintetice |
| **Utilizare** | Notează cifrele furnizorului tău, dacă sunt disponibile |
| **Decizie** | Acceptă numai după trecerea verificărilor sursei, diff-ului, testelor și confidențialității |

**Rezultatul tău:** copiază această înregistrare și completeaz-o după propria rulare. Înlocuiește „observat” numai cu un rezultat văzut de tine. Alege Acceptă când trec toate verificările necesare, Revizuiește când o corecție are un domeniu limitat și Oprește când sursa, domeniul sau accesul nu sunt clare.

## Verifică ce ai înțeles

1. **Întrebare:** o bază inițială care trece demonstrează că există funcția solicitată? **Răspuns:** Nu. După editare, testează noul comportament de acceptare.

2. **Întrebare:** ce intră într-o înregistrare de acceptare? **Răspuns:** dovezile sursei, fișierele modificate, verificările comportamentului, domeniul accesului și utilizarea observată.

## Depanare

- **Nu există o sursă pentru afirmație:** marcheaz-o ca neverificată și găsește o sursă autoritară.
- **Testele trec, dar rezultatul diferă:** adaugă un caz manual și inspectează datele.
- **Lipsesc datele de utilizare:** notează „indisponibil” în loc să estimezi un cost real.
- **Diff-ul include date private:** oprește partajarea rezultatului și elimină acele date din înregistrarea de practică.

## Pașii următori

**Continuă cu [Delegarea agenților](/articles/effective-ai-agent-delegation/)**. Pentru detalii despre costuri și confidențialitate, citește despre [rutarea furnizorilor](/articles/openrouter-provider-routing-quality-cost/) și [limita de confidențialitate a IA locale](/articles/local-ai-privacy-boundary/).

**Navigarea cursului:** [Anterior: Configurarea MCP](/articles/effective-ai-mcp-server-setup/), [Structura cursului](/effective-ai-course-start/).

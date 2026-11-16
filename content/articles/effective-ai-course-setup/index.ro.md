---
title: "Configurarea cursului despre fluxuri de lucru AI: terminal, Git și laborator practic"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Pregătiți un spațiu sigur de practică AI, învățați termenii de terminal și Git folosiți în curs și rulați laboratorul introductiv."
genre: ["Inteligență artificială", "Inginerie software", "Educație"]
tags: ["configurare curs AI", "noțiuni de terminal", "noțiuni de Git", "cerințe pentru agenți de programare", "laborator practic AI", "curs AI pentru începători"]
cover: "/img/cover/effective-ai-course-setup.webp"
coverAlt: "Spațiu de practică pentru începători cu simboluri de terminal, Python și Git, dosar de laborator bifat și arhivă de resetare"
coverCaption: ""
---

[Înapoi la cursul practic despre fluxuri de lucru AI](/effective-ai-course-start/)

**Pregătiți un spațiu sigur de practică înainte să folosiți un agent.** Lecțiile 1 și 2 funcționează în browser fără acest laborator. Reveniți aici înainte de lecția 3 dacă doriți cursul complet. Lecțiile practice de programare folosesc Git, Python 3.10 sau o versiune mai nouă și un agent de programare. Traseul de studiu înlocuiește acțiunile indisponibile ale agentului cu activități manuale marcate.

**Rezultat de învățare:** veți rula laboratorul introductiv, veți salva o bază locală și veți explica resetarea unei copii de unică folosință.

## Idei principale

- **Traseul în browser:** faceți exercițiile de chat, planificare, verificare a surselor și analiză în ChatGPT sau Claude.
- **Traseul local:** folosiți terminalul și laboratorul Python inclus pentru exercițiile de programare.
- **Traseul de resetare:** extrageți o copie nouă a laboratorului dacă un exercițiu nu reușește.
- **Regula de siguranță:** păstrați fișierele private, datele clienților și acreditările în afara laboratorului.

## Alegeți traseul

| Traseu | De ce aveți nevoie | Ce exersați |
|---|---|---|
| **Introducere în browser** | Browser actual și cont ChatGPT sau Claude | Lecțiile 1 și 2, plus pachetul de sarcini de chat din lecția 1 |
| **Practică locală** | Git, Python 3.10 sau mai nou, terminal și un agent de programare | Fișiere, diferențe, teste și modificări făcute de agent |
| **Curs de studiu** | Browser, Python 3.10 sau mai nou instalat local și Git | Toate verificările laboratorului; pașii indisponibili cu agent și MCP sunt marcați neexecutați |

**Fiecare produs își stabilește propriile planuri și limite.** Verificați [ChatGPT Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) și [Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) înainte să vă bazați pe o funcție. Traseul de studiu nu dovedește experiență practică cu un agent de programare indisponibil. Notați diferența în observațiile de finalizare.

**Folosiți un traseu implicit:** ChatGPT în browser pentru exercițiile de chat, apoi un agent de programare disponibil cu laboratorul local. Claude este o opțiune echivalentă pentru chat. Codex CLI, Claude Code CLI și OpenCode sunt opțiuni pentru partea de programare. Nu aveți nevoie de conturi la toți furnizorii.

**Notați cinci verificări înainte de a deschide un agent de programare.** Astfel separați o verificare a laboratorului local de o afirmație despre un cont sau un spațiu de lucru găzduit.

| Verificare | Notați |
|---|---|
| **Spațiu de lucru** | Dosarul exact al laboratorului extras pe care îl va citi agentul |
| **Execuție** | Calculator local sau spațiu la distanță selectat |
| **Furnizor** | Contul sau furnizorul modelului folosit la această sarcină |
| **Permisiuni** | Dacă scrierea fișierelor și comenzile shell sunt permise sau cer aprobare |
| **Bază** | Numărul observat și două teste trecute înainte de editare |

**Păstrați restrâns directorul rădăcină pentru practică.** Un spațiu găzduit are nevoie de propria copie a laboratorului sintetic. O rulare locală nu dovedește că copia la distanță sau contul au aceleași fișiere și permisiuni.

## Învață termenii locali

| Termen | Înțeles simplu |
|---|---|
| **Terminal** | Aplicație în care introduceți comenzi |
| **Shell** | Software care interpretează comenzile |
| **CLI** | Interfață de linie de comandă a unui program |
| **Director de lucru** | Dosarul folosit implicit de o comandă |
| **Repository** | Proiect urmărit de Git |
| **Commit** | Instantaneu Git salvat |
| **Branch** | Linie cu nume pentru modificări Git |
| **Diff** | Afișare a liniilor adăugate sau șterse |
| **Verificare** | Verificare repetabilă a comportamentului așteptat |
| **Cod de ieșire** | Număr care indică succesul sau eșecul unei comenzi |

**Nu aveți nevoie de GitHub pentru laboratorul introductiv.** Git funcționează pe calculator. GitHub este un serviciu de găzduire separat. Un commit local salvează un instantaneu fără să trimită fișierele în altă parte.

## Pregătește laboratorul

**Descărcați [laboratorul introductiv al cursului](/downloads/effective-ai-course-lab.zip)** și extrageți-l într-un dosar nou pe care îl controlați. Deschideți un terminal în acel dosar. Pe macOS sau Linux, deschideți Terminal și folosiți `cd` pentru a intra în dosarul extras. Pe Windows, folosiți PowerShell sau Windows Terminal și `cd`. Pe Windows, comanda Python este adesea `py -3`, nu `python3`.

**Instalați [Python 3.10 sau o versiune mai nouă](https://www.python.org/downloads/) și [Git](https://git-scm.com/downloads), dacă este nevoie.** Verificați instrumentele instalate înainte de rularea laboratorului. Primele două comenzi afișează versiunile. `cd` schimbă directorul de lucru. `ls` listează fișierele. Înlocuiți calea exemplu cu calea reală a dosarului extras.

```bash
python3 --version
git --version
cd /path/to/effective-ai-course-lab
ls
```

**În Windows PowerShell,** folosiți `py -3 --version`, `git --version`, `cd C:\path\to\effective-ai-course-lab` și `Get-ChildItem`. Lista ar trebui să conțină `task_report.py`, `tasks.json`, `tests` și `docs`. Dacă o comandă pentru versiune eșuează, terminați instalarea înainte să continuați.

```bash
pwd
python3 task_report.py tasks.json
python3 -m unittest discover -s tests -v
```

**În Windows PowerShell,** înlocuiți `pwd` cu `Get-Location`, dacă preferați, și `python3` cu `py -3` când Python folosește launcherul. Prima comandă afișează calea. Aceasta ar trebui să se termine cu dosarul laboratorului extras. Verificați numele fișierelor. `AGENTS.md.txt` nu ține loc de `AGENTS.md`. În File Explorer, activați extensiile de nume de fișier pentru a vedea numele complet.

**Rezultat așteptat:** raportul spune `Total tasks: 4`. Comanda de testare numește două teste și se termină cu `OK`. După succes, shell-ul returnează codul zero. Un alt număr sau un traceback indică faptul că trebuie să verificați dosarul și instalarea Python.

**Citiți o comandă pe componente.** În `python3 task_report.py tasks.json`, `python3` lansează Python, `task_report.py` este programul, iar `tasks.json` numește datele de intrare. Numărul afișat este rezultat, nu altă comandă. După o eroare, macOS și Linux arată starea cu `echo $?`. PowerShell oferă starea ultimului program nativ prin `$LASTEXITCODE`.

**Rezervați aproximativ zece minute pentru prima rulare** după instalarea Python: extrageți laboratorul, rulați raportul și comparați totalul cu cele patru intrări din `tasks.json`. Deschideți fișierul JSON într-un editor de text și numărați intrările.

## Exersează Git în siguranță

**Porniți Git doar în dosarul extras al laboratorului.** Aceste comenzi salvează o copie locală. `git status` arată fișierele modificate. `git diff` afișează liniile schimbate după editarea unui fișier urmărit.

```bash
git init
git add .
git commit -m "Baza laboratorului cursului"
git status --short
```

**Stare așteptată:** după commit nu apar nume de fișiere. Dacă Git cere nume și e-mail, configurați în acest dosar o identitate folosită doar pentru laborator și reluați commitul. Înlocuiți valorile exemplu cu valori private. Nu lipiți date despre identitate sau acreditări într-un chat public.

```bash
git config --local user.name "Cursant"
git config --local user.email "learner@example.invalid"
git commit -m "Baza laboratorului cursului"
git status --short
```

**Resetarea nu necesită comenzi Git.** Salvați notițele în afara laboratorului, ștergeți copia extrasă și extrageți din nou ZIP-ul original. Folosiți metoda când editarea unei lecții lasă programul într-o stare necunoscută.

## Protejează spațiul de practică

**Folosiți exemple sintetice.** Nu încărcați documente private într-un proiect de curs. Nu puneți chei API în solicitări, fișiere sursă, capturi de ecran sau commituri. Accesul agentului la fișiere și comenzi depinde de permisiuni și de dosarul deschis. Verificați-le pe ambele înainte de execuție.

**Verificați partajarea înainte de încărcare.** Membrii proiectului pot avea acces la fișiere. Respectați politica organizației pentru activitatea reală. Cursul folosește date fictive, deci laboratorul nu cere o aprobare specială.

## Exersează și verifică

**Rezultatul tău:** notează traseul ales, cele cinci câmpuri preliminare, numărul din raport, rezultatul testelor și metoda de resetare. Folosește o copie nouă pentru a confirma că știi să resetezi laboratorul.

**Raționament așteptat:** știi ce dosar afectează comenzile, deosebești Git local de găzduire și ai o metodă de recuperare înainte ca un agent să editeze fișiere.

## Verifică ce ai înțeles

1. **Întrebare:** O introducere numai în browser încheie traseul laboratorului local? **Răspuns:** Nu. Traseul complet cere o bază locală Python și Git.

2. **Întrebare:** Ce trebuie salvat înainte să schimbi laboratorul de unică folosință? **Răspuns:** Rezultatul testului inițial care a trecut și un punct curat de resetare.

## Depanare

- **Lipsește comanda Python:** instalați Python 3 de la distribuitorul oficial și redeschideți terminalul.
- **Fișier negăsit:** verificați directorul de lucru și listați fișierele din dosarul extras.
- **Testele nu rulează:** utilizați comanda exactă din README-ul laboratorului extras.
- **Git cere o identitate pentru commit:** configurați Git local și nu includeți valorile alese în notițele cursului.

## Pașii următori

**Continuați cu [fluxul de lucru AI de încredere](/articles/effective-ai-workflow-foundations/)**. Primul exercițiu folosește același atelier sintetic înainte ca vreun instrument să primească fișiere reale.

**Navigarea cursului:** [Structura cursului](/effective-ai-course-start/).

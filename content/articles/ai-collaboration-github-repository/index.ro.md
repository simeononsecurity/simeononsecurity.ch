---
title: "Colaborare AI în GitHub: limitele depozitului și ale revizuirii"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Construiește o hartă a surselor, stabilește proprietarii fișierelor și protejează limita de publicare pentru contribuțiile AI revizuite."
genre: ["Inteligență artificială", "Colaborare în echipă", "Inginerie software"]
tags: ["curs de colaborare AI", "depozit GitHub", "protecția ramurilor", "CODEOWNERS", "hartă a surselor", "revizuire pull request", "controale de publicare"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustrație cu profesioniști care revizuiesc împreună munca unui proiect într-un spațiu de lucru pentru securitate cibernetică"
coverCaption: ""
---
[Înapoi la cursul de colaborare AI](/ai-collaboration-course-start/)

**După aprobarea statutului, responsabilul creează limita de publicare cu prioritate pentru GitHub.** Cerințele, configurația, politica și runbookurile se află într-un singur depozit temporar. Colaboratorii propun modificări prin Issues și pull requesturi. Stabilește unde se găsesc faptele aprobate și blochează schimbările neverificate înainte de conectarea agenților.

## Idei principale

- **`main` protejată** este limita de publicare.
- **Issues** adună propuneri fără să aprobe politici.
- **CODEOWNERS** atribuie recenzori eligibili fișierelor.
- **Utilizatorii separați** demonstrează controalele de revizuire și refuz.

## Înainte de a începe

**Cerințe preliminare:** [baza pilotului](/articles/ai-collaboration-pilot-foundation/), laboratorul extras, administratorul depozitului și recenzori separați pentru produs și operațiuni. **Timp estimat:** 60 de minute. **Dificultate:** moderată.

**Limita planului:** GitHub documentează ramurile protejate pentru depozite publice în planul Free și pentru depozite private în planurile Pro, Team sau Enterprise. Folosește doar conținut sintetic în depozitele publice. Verifică vizibilitatea și planul în referința despre protecția ramurilor înainte de a te baza pe aplicarea regulilor.

**Rezultatul final:** termini cu o ramură de publicare protejată, proprietari de fișiere, o hartă a surselor și un test de refuz păstrat ca dovadă.

## Creează depozitul

1. **Creează `export-service-lab`** cu un README și ramura implicită **`main`**.
2. **Copiază laboratorul extras** în rădăcina depozitului, păstrând **`check.py`**, **`test_check.py`** și **`baseline/`**. Copiază fișierele de înregistrare din `baseline/` în rădăcină ca înregistrări inițiale.
3. **Creează `docs/project-map.md`** folosind registrul bazei pilotului. Adaugă **`docs/policy.md`** cu POL-01 aprobat.
4. **Creează `docs/decisions/DEC-12.md`** cu aprobarea statutului, rolurile, decizia de bază și starea.
5. **Fă commitul inițial ca administrator.** Înregistrează această excepție inițială. Activează protecția înaintea contribuțiilor ulterioare.

**Configurare locală în Git Bash, Terminal macOS sau un shell Linux:** autentifică-te în GitHub din browser, deschide depozitul nou, selectează **Code** și copiază URL-ul HTTPS de clonare. Într-un director de lucru temporar, execută comenzile de mai jos. Înlocuiește cele două căi exemplu cu URL-ul și calea ZIP-ului descărcat al laboratorului. Nu lipi un token în URL.

```bash
git --version
git clone "https://github.com/OWNER/export-service-lab.git"
cd export-service-lab
unzip -n "/absolute/path/to/ai-collaboration-lab.zip"
cp baseline/config.json baseline/policy.json baseline/proposal.json baseline/requirement.json baseline/runbook.md .
mkdir -p docs/decisions
git status --short
```

Comanda clone ar trebui să creeze directorul depozitului. Dacă `unzip` nu este disponibil, extrage ZIP-ul cu managerul de fișiere și copiază conținutul în acest checkout, păstrând README-ul depozitului. `git status --short` ar trebui să listeze înregistrările copiate, checkerul, testele și `baseline/` ca fișiere noi. Salvează `docs/project-map.md`, `docs/policy.md` și `docs/decisions/DEC-12.md` din pachetul pilot folosind un editor text. Apoi rulează:

```bash
git add README.md baseline check.py test_check.py config.json policy.json proposal.json requirement.json runbook.md docs
git commit -m "Add synthetic collaboration baseline"
git push origin main
git status --short
git remote -v
```

Git ar trebui să raporteze un ID nou de commit, apoi un push reușit în `main`. La final, statusul scurt ar trebui să fie gol. Deschide depozitul GitHub într-o fereastră nouă de browser și confirmă că fișierele și ID-ul commitului apar pe `main`. Salvează URL-ul commitului ca dovadă a configurării inițiale. Dacă Git cere identitatea autorului, urmează instrucțiunile de configurare din centrul cursului. Dacă autentificarea eșuează, folosește fluxul de acreditări acceptat de GitHub și repetă același push. Dacă ramura sau remote-ul sunt greșite, oprește-te și verifică `git branch --show-current` și `git remote -v` înainte de altă scriere. Dacă push-ul este respins fiindcă protecția a fost deja activată, deschide o ramură de propunere și un PR, fără să ocolești regula. Calea exclusiv prin browser de mai jos rămâne disponibilă cu ajutorul unui responsabil.

| Înregistrare | Locație | Proprietar |
|---|---|---|
| **POL-01** | `policy.json`, `docs/policy.md` | Proprietarul politicii |
| **REQ-17** | `requirement.json` | Proprietarul produsului |
| **RUN-04** | `runbook.md` | Proprietarul operațiunilor |
| **Comportament** | `config.json` | Responsabilul depozitului |
| **Decizii** | `docs/decisions/` | Liderul proiectului |

**Harta indică locații, nu copiază valori.** Păstrează README-ul concentrat pe configurare și hartă. Cerințele de retenție repetate produc derivă chiar și în același depozit.

## Atribuie proprietari fișierelor

**Generează local `.github/CODEOWNERS`** cu identificatorii reali ai sandboxului. Introdu identificatorii fără **`@`** la început. Păstrează identitățile conturilor în laboratorul privat, nu în dovezile publice ale exercițiului.

```bash
python3 - <<'PY'
from pathlib import Path
roles = ['product', 'operations', 'maintainer', 'policy']
handles = {r: input(r + ' GitHub handle: ').strip().lstrip('@') for r in roles}
if any(not h or not all(c.isalnum() or c == '-' for c in h) for h in handles.values()):
    raise SystemExit('Invalid handle')
paths = {'requirement.json': 'product', 'runbook.md': 'operations',
         'config.json': 'maintainer', 'policy.json': 'policy',
         'docs/policy.md': 'policy', 'AGENTS.md': 'policy',
         'CLAUDE.md': 'policy', '.clinerules/': 'policy',
         '.github/': 'maintainer', 'check.py': 'maintainer',
         'test_check.py': 'maintainer', 'baseline/': 'maintainer'}
Path('.github').mkdir(exist_ok=True)
Path('.github/CODEOWNERS').write_text(''.join(
    '/' + path + ' @' + handles[role] + '\n' for path, role in paths.items()))
PY
```

**Proprietarii au nevoie de acces de scriere** pentru ca GitHub să-i recunoască. Inspectează fișierul CODEOWNERS în browser pentru erori. Protejează fișierele de proprietate și definițiile fluxurilor de lucru, alături de conținutul obișnuit.

**Mai multe nume pe aceeași linie nu cer aprobarea tuturor proprietarilor enumerați.** GitHub acceptă aprobarea unui singur proprietar eligibil pentru calea respectivă. Folosește proprietari diferiți pentru căile cerințelor și runbookului. Pilotul cere și atestări de la proprietarii produsului și operațiunilor, asociate propunerii finale.

## Protejează publicarea

1. **Deschide Settings, Branches** și adaugă o regulă de protecție pentru **`main`**. Folosește consecvent această protecție a ramurii în exercițiu, fără să o combini cu rulesets.
2. **Cere un pull request,** două aprobări și revizuirea code owners.
3. **Respinge aprobările învechite** după commituri noi și cere rezolvarea conversațiilor.
4. **Activează opțiunea de interzicere a ocolirii setărilor de mai sus.** Păstrează dezactivate force push și ștergerea.
5. **Adaugă verificarea de consistență** după prima rulare în modulul următor. Cere ca ramurile să fie actualizate înainte de merge.

**Două aprobări impun un număr, nu apartenența la roluri de business.** CODEOWNERS adaugă acoperirea proprietarilor pe cale. Responsabilul verifică și atestările celor două roluri. Înregistrează explicit acest control procedural, fără să-l descrii ca aplicare automată a două roluri.

**Administratorii gestionează în continuare configurația.** Capturează regula înaintea testelor și după ele. Nu acorda unui agent acces de administrator și nu folosi un token privilegiat pentru a demonstra refuzul unui colaborator.

## Verifică limita

| Încercare | Rezultat așteptat |
|---|---|
| **Colaboratorul trimite o ramură** | Propunere permisă |
| **Colaboratorul publică direct** | Publicarea protejată este refuzată |
| **Un recenzor aprobă** | Merge blocat de pragul de revizuire |
| **Un commit nou vine după revizuire** | Este necesară o aprobare nouă |
| **Fișier sensibil fără proprietar** | Repară înainte de publicare |

**Folosește sesiunea de browser a colaboratorului pentru a inspecta traseul.** Editorul web GitHub nu editează ramura **`main`** protejată. Solicitarea de creare a unei ramuri arată traseul acceptat prin browser. Nu dovedește că serverul a respins un push direct. Pentru dovezi de refuz din partea platformei, cere unui colaborator cu acces Git local aprobat să încerce un push direct inofensiv către **`main`** protejată și păstrează răspunsul serverului. Marchează testul de refuz drept blocat dacă accesul local nu este disponibil.

**Citește `main` după refuz** și confirmă că revizia nu s-a schimbat. Înregistrează rolul actorului, acțiunea încercată, rezultatul și revizia sursei. Promisiunea asistentului că nu va publica este o dovadă comportamentală, nu un test al permisiunilor platformei.

**Folosește propriul clone local autentificat al colaboratorului pentru testul de push direct.** Un token al responsabilului ar verifica identitatea greșită. Acest răspuns ilustrativ arată tipul de dovadă de server care trebuie păstrat. Formularea exactă depinde de regulile depozitului.

```text
Actor role: contributor
Attempt: harmless synthetic direct push to main
Remote result: rejected, protected branch update denied
Initial main commit: [record sandbox commit]
Final main commit: [record same commit after read-back]
Decision: platform denial supported only if both records are observed
```

**Dacă autentificarea Git locală nu este disponibilă, marchează refuzul pe server ca blocat.** Păstrează promptul browserului de creare a ramurii drept dovadă a traseului, apoi cere responsabilului să organizeze un test separat cu un colaborator. Nu puncta promptul de traseu ca push direct respins.

## Creează o hartă utilă a surselor

**O hartă a surselor este un document de orientare**, nu un al doilea document de cerințe. Cine vine din chat trebuie să găsească intenția actuală, comportamentul implementat și instrucțiunile operaționale fără să aleagă între rezumate concurente.

```text
Project: export-service-lab
Track: GitHub-first
Approved boundary: protected main

REQ-17 -> requirement.json
  Authority: retention intent for synthetic export files
  Owner: product-owner
  Revision: record revision plus protected commit

RUN-04 -> runbook.md
  Authority: operating instructions for the synthetic lab
  Owner: operations-owner
  Revision: protected commit

Behavior -> config.json
  Authority: committed retention configuration
  Owner: repository-maintainer
  Revision: protected commit

Proposals -> Issues and proposal branches
  Authority: requested changes only
```

**Nu pune valoarea actuală de retenție în fiecare intrare a hărții.** O hartă cu „șapte zile” devine încă o valoare de sincronizat după PROP-042. Păstrează identificatori stabili și locații în hartă, iar valoarea citește-o din înregistrarea autoritară.

**Protejează schimbările hărții ca schimbări de rutare.** Redirecționarea REQ-17 către un fișier draft modifică selecția sursei chiar dacă cerința aprobată rămâne intactă. Verifică destinația, proprietarul și domeniul autorității ori de câte ori se schimbă harta.

## Separă baza și candidatul

**Rădăcina depozitului conține înregistrările active ale laboratorului.** Directorul descărcat **`baseline/`** este o mostră didactică. Nu devine automat baza protejată pentru fiecare PR ulterior. După ce munca revizuită ajunge în **`main`**, înregistrările protejate din rădăcină definesc baza următoarei propuneri.

| Locație | Scop | Editare în PROP-042? |
|---|---|---|
| **Cerința/configurația/runbookul din rădăcină** | Înregistrări active propuse pe ramură | Da, prin schimbări revizuite |
| **`baseline/`** | Mostra originală a exercițiului offline | Nu |
| **Worktree de încredere detașat** | Înregistrări protejate capturate din rădăcină | Nu |
| **`context.json`** | Dovada octeților bazei capturate | Regenerează după reconciliere |

**Separă schimbările de control de cele de retenție.** Configurează mai întâi checkerul și regulile de revizuire. Apoi propune schimbarea de la șapte la treizeci de zile. Combinarea rescrierii politicii, a fluxului de lucru și a valorii îngreunează distingerea controalelor reparate de cele ocolite.

## Revizuiește schimbarea completă

**Deschide Files changed înainte să accepți descrierea unui PR.** Descrierea explică intenția autorului. Diff-ul arată schimbarea trimisă. Pentru PROP-042, inspectează revizia cerinței, excluderile de domeniu, configurația, runbookul, baza propunerii și dovezile manifestului.

1. **Revizuirea produsului:** confirmă intenția de treizeci de zile și excluderile neschimbate.
2. **Revizuirea operațiunilor:** confirmă că runbookul corespunde configurației propuse și păstrează limita de execuție.
3. **Revizuirea responsabilului:** inspectează JSON-ul, captura sursei, rezultatele verificărilor și editările fără legătură.
4. **Revizuirea controlului:** inspectează separat orice schimbare a hărții, politicii, CODEOWNERS sau fluxului de lucru.

**Un check verde nu explică o ștergere fără legătură.** Dacă ramura elimină documentul de politică în timp ce schimbă retenția, cere o propunere separată sau o revizuire specifică a proprietarului. Domeniul restrâns menține obiectul de revizuire ușor de înțeles.

## Diagnostichează un test de refuz

**Folosește o singură acțiune încercată pentru fiecare rând de dovezi.** „Colaboratorul a eșuat” este ambiguu. Utilizatorul poate să nu aibă acces normal de scriere, să întâmpine o limitare a browserului sau să declanșeze regula intenționată a ramurii. Acestea stabilesc limite diferite.

| Observație | Interpretare | Urmărire |
|---|---|---|
| **Nu poate crea nicio ramură** | Lipsește accesul de contribuție | Folosește ruta aprobată prin Issue/fork |
| **Creează o ramură, nu poate publica în main** | Ruta de publicare testată este restricționată | Înregistrează revizia main neschimbată |
| **Merge blocat cu o revizuire** | Pragul de revizuire se aplică PR-ului testat | Adaugă dovezi specifice rolului |
| **Administratorul publică în ciuda regulii** | Identitatea testată ocolește limita | Inspectează setările de bypass și permisiunile |

**În dovezile comune ale cursului, înregistrează rolul și acțiunea fără a expune detaliile contului.** Păstrează privat pentru recenzor înregistrările native ale actorului. Capturează împreună configurația regulii, operația încercată, refuzul și revizia protejată rezultată.

## Verificarea finalizării depozitului

**Livrează un depozit în care alt colaborator se poate orienta independent.** README indică harta, harta rezolvă înregistrările autoritare, acoperirea proprietarilor include căi sensibile, iar protecția se aplică la **`main`**. Păstrează o propunere permisă și o încercare de publicare refuzată.

**Nu pretinde că aplicarea este dovedită doar de setări.** Setările stabilesc configurația intenționată. Încercarea din sandbox arată comportamentul observat pentru un anumit rol și traseu. Include ambele dovezi în lecția despre agenți și GitHub Actions.

## Depanare și revenire

**Lipsește solicitarea proprietarului:** confirmă accesul de scriere și acoperirea căii ramurii de bază. **Lipsește protecția:** verifică planul și vizibilitatea. **Merge-ul rămâne posibil:** inspectează ținta regulii, configurația bypass și numărul de revizuiri.

**Revenire:** închide propunerile neîmbinate și dezactivează automatizarea laboratorului. Revino asupra conținutului de laborator îmbinat printr-un alt PR revizuit. Păstrează dovezile înainte de ștergerea depozitului temporar. Nu slăbi protecția pentru a termina un test eșuat.

## Exercițiu și autoevaluare

**Propune ca participant o editare pentru `docs/policy.md`.** Decide dacă aprobarea responsabilului, singură, stabilește aprobarea proprietarului politicii.

**Raționament așteptat:** numărul de revizuiri nu stabilește autoritatea. Calea cere acoperire de către proprietarul politicii și o revizuire actuală a rolului. Listează cerințele specifice rolurilor care nu sunt aplicate automat drept controale procedurale.

## Referințe principale

- **Controale de plan și revizuire:** [Ramuri protejate](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Eligibilitatea proprietarilor:** [Code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
- **Contribuție prin browser:** [Editarea fișierelor](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).

## Pașii următori

**Continuă cu [Adaptoare pentru agenți și GitHub Actions](/articles/ai-collaboration-github-agents-actions/)** pentru a lega dovezile surselor de verificări executabile.

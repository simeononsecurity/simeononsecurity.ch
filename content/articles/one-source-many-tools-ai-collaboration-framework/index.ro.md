---
title: "O singură sursă, multe instrumente: un cadru de colaborare AI pentru echipe mixte"
date: 2026-10-01
lastmod: 2026-11-23
toc: true
draft: false
description: "Construiți un sistem comun de colaborare AI, cu responsabili pentru surse, versiuni de context, revizuirea durabilă a schimbărilor și criterii clare pentru hărți de proiect sau RAG."
genre: ["Inteligență artificială", "Managementul cunoștințelor", "Inginerie software", "Colaborare în echipă"]
tags: ["cadru de colaborare AI", "echipe mixte", "sursă de adevăr", "agenți AI", "AGENTS.md", "CLAUDE.md", "reguli Cline", "Claude Code", "Codex", "ChatGPT", "Copilot", "Cowork", "generare augmentată prin recuperare", "RAG", "Model Context Protocol", "hartă de proiect", "manifest de context", "managementul cunoștințelor", "deriva documentației", "aprobare umană", "registru de decizii", "predare între agenți", "versionarea politicilor", "worktree-uri Git", "porți pentru pull request"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustrație cu profesioniști care colaborează la activități de securitate cibernetică"
coverCaption: ""
---

**Două persoane adresează aceeași întrebare către două instrumente AI:** cât timp trebuie să păstreze serviciul un export? În acest exemplu ilustrativ, agentul IDE al dezvoltatorului răspunde șapte zile pe baza unui README. Asistentul de chat al coordonatorului de operațiuni răspunde treizeci de zile pe baza unei pagini wiki. Ambele răspunsuri par sigure. Fiecare instrument a citit o altă copie a adevărului.

**Problema ține de responsabilitate,** nu de calitatea promptului. Cerința din wiki s-a schimbat săptămâna trecută, dar nimeni nu a actualizat README-ul. Dezvoltatorul cere agentului să corecteze sarcina de retenție. Agentul urmează documentul vechi și produce un patch ordonat care readuce comportamentul greșit. Revizorii inspectează codul fără să vadă versiunea cerinței care a stat la baza răspunsului.

**Atribuiți fiecărui fapt o singură sursă.** Faceți fiecare instrument să citească din acea sursă și treceți fiecare schimbare durabilă printr-o persoană. Un depozit, un wiki și un sistem de urmărire au scopuri diferite. Au nevoie de autoritate explicită, responsabili numiți și o procedură comună pentru transferul informațiilor.

**Acest ghid oferă un model pe care îl puteți aplica săptămâna aceasta,** cu sau fără generare augmentată prin recuperare. Începeți cu o hartă de proiect, instrucțiuni versionate, înregistrări de dovezi și propuneri revizuite. Adăugați infrastructură de căutare numai când problema de recuperare o justifică.

**Primul rezultat trebuie să fie un registru al surselor,** nu un conector. Enumerați fiecare tip de fapt, sursa sa oficială, responsabilul, revizia curentă și persoana care aprobă schimbările.

## Idei principale

- **Atribuiți autoritatea după tipul informației,** fără să forțați totul într-o singură aplicație.
- **Tratați memoria și indexurile de recuperare ca memorii cache,** niciodată ca surse independente de politică.
- **Atașați versiunile surselor la propuneri,** ca revizorii să știe ce fapte au fundamentat schimbarea.
- **Impuneți aprobarea în afara prompturilor,** prin controale de acces și porți obligatorii de revizuire.
- **Partajați procedura între instrumente,** adaptând prezentarea la fiecare interfață.

## Înainte să începeți

**Cerințe preliminare:** alegeți un proiect pilot cu un depozit, un wiki sau un sistem de documente, un instrument de urmărire și responsabili dispuși să revizuiască schimbările. O echipă fără wiki poate folosi un depozit de documente versionat. Păstrați același model de responsabilitate.

**Timp estimat:** rezervați două până la patru ore pentru harta și șabloanele inițiale, apoi un pilot de o săptămână. **Dificultate:** moderată. Partea dificilă este stabilirea autorității, nu instalarea încă unui instrument AI.

**Domeniu:** acesta este un model propus de lucru în echipă. Regulile de aprobare și convențiile de denumire sunt recomandări, nu comportamente implicite garantate de Claude Code, Codex, Cline, Cowork, Copilot sau ChatGPT. Cuprinsul automat de mai sus duce la fiecare etapă de implementare.

## Instrumente mixte, contexte separate

**Programatorii și neprogramatorii lucrează la același proiect,** dar folosesc interfețe diferite. Un dezvoltator folosește un agent IDE sau de terminal. Un responsabil de produs folosește un proiect de chat. Un coordonator de operațiuni lucrează din wiki și sistemul de urmărire. Alegeți interfețele în funcție de sarcină, nu de accesul la faptele oficiale.

**Contextul este materialul disponibil pentru răspunsul curent.** Inspectați fiecare sesiune pentru fișiere din depozit, documente încărcate, istoric de chat, memorie salvată, rezultate ale conectorilor și fragmente recuperate. Două sesiuni cu dovezi diferite nu trebuie să fie de acord, chiar dacă întrebările coincid.

| Problemă | Ce observați |
|---|---|
| **Deriva documentației** | Un README repetă o cerință învechită |
| **Promovarea rezumatului** | Un rezumat de sesiune devine dovadă fără sursa originală |
| **Scrieri suprapuse** | Doi agenți înlocuiesc aceeași pagină pornind de la versiuni de bază diferite |
| **Decizii pierdute** | O înțelegere dintr-o ședință nu ajunge în registrul de decizii |
| **Lipsa provenienței** | Un răspuns plauzibil nu indică versiunea paginii sau commitul |

**Exemplul privind retenția arată diferența.** Wiki-ul descrie comportamentul-țintă aprobat. Codul descrie comportamentul implementat. Niciunul nu trebuie să îl rescrie tacit pe celălalt. Înregistrați dezacordul și întrebați responsabilul desemnat dacă trebuie revizuită implementarea sau cerința.

> **Idee-cheie:** stabiliți autoritatea înainte de a alege un instrument AI. Începeți prin definirea termenilor de mai jos.

### Casetă laterală: cinci termeni comuni

| Termen | Semnificația în acest cadru |
|---|---|
| **Sursă** | Înregistrarea desemnată ca autoritate pentru un tip de informație |
| **Cache** | Copie derivată pentru viteză sau comoditate |
| **Propunere** | Schimbare sugerată care așteaptă aprobarea responsabilului |
| **Hartă de proiect** | Index cu locațiile surselor, identificatori și responsabili |
| **Manifest** | Înregistrarea dovezilor exacte folosite într-un răspuns sau o propunere |

## O singură sursă pentru fiecare fapt

**O singură sursă înseamnă o autoritate pentru fiecare fapt,** nu o singură bază de date pentru întreaga organizație. Stabiliți alocarea de mai jos în timpul pilotului și înlocuiți rolurile exemplificative cu responsabilii reali ai echipei.

| Tip de informație | Sistem de origine | Responsabil | Cine scrie | Cum citesc agenții |
|---|---|---|---|---|
| **Cod, teste, configurări, scheme** | Depozit | Responsabil de mentenanța tehnică | Contributori prin PR-uri revizuite | Fișiere dintr-un commit înregistrat |
| **Documentație publicată și ADR-uri** | Depozit | Responsabil tehnic | Contributori prin același PR | Fișiere versionate |
| **Cerințe** | Wiki | Responsabil de produs | Responsabil sau editor autorizat | ID-ul și revizia paginii |
| **Runbook-uri** | Wiki | Responsabil de operațiuni | Editor autorizat | ID-ul și revizia paginii |
| **Politici** | Wiki | Responsabil de politici | Editor autorizat după revizuire | Pagina canonică și adaptorul local |
| **Decizii între echipe** | Registrul de decizii din wiki | Responsabil desemnat al deciziei | Responsabilul după aprobare | ID-ul și starea deciziei |
| **Sarcini și constatări** | Instrument de urmărire | Responsabilul sarcinii | Persoane sau flux autorizat de propuneri | Cheia și revizia issue-ului |
| **Chat-uri, rezumate, embeddings** | Doar cache | Administratorul sesiunii sau indexului | Instrumente și participanți | Doar referință, urmată de verificarea sursei |

**O înregistrare de decizie arhitecturală (ADR)** stă lângă cod când guvernează proiectarea depozitului. O decizie între echipe aparține registrului comun. Legați cele două înregistrări când decizia acoperă ambele domenii. Nu păstrați copii independente ale stării aprobării.

**Copiile locale ale politicii rămân subordonate paginii canonice.** În schimb, testele și schemele unui depozit sunt surse în propriul domeniu. Locația nu determină singură autoritatea. Harta o determină.

**Un cache nu înlocuiește niciodată o sursă.** Dacă un rezumat spune șapte zile, iar cerința aprobată spune treizeci, folosiți cerința pentru comportamentul-țintă. Păstrați rezumatul contradictoriu ca dovadă a derivei, nu ca regulă concurentă. După stabilirea autorității, definiți fluxul de scriere.

## Întâi extrageți dovezi, apoi propuneți

**Agenții aduc dovezi în contextul sesiunii** și apoi redactează propuneri. Nu aprobă singuri fapte durabile. Editarea unei ramuri de sarcină sau trimiterea unui proiect nu înseamnă publicarea politicii, combinarea codului ori marcarea unei decizii ca acceptată.

```text
Sursă -> citire cu permisiunea verificată -> contextul sesiunii
Contextul sesiunii -> propunere + versiune de bază -> revizuirea responsabilului
Aprobarea responsabilului -> publicare controlată -> jurnalul schimbărilor
Versiunea de bază s-a schimbat -> reconciliați propunerea -> revizuiți din nou
```

**Atașați versiunea de bază** înainte de a cere revizuirea. Revizorul are nevoie de valoarea anterioară, valoarea propusă, motiv, dovezi și sistemele afectate. Aprobarea trebuie să indice o revizie specifică a propunerii, nu un chat în evoluție.

```yaml
proposal_id: PROP-042
target: wiki:REQ-17
base_version: 8
change: "Păstrați exporturile timp de treizeci de zile, nu șapte."
evidence:
  - "decision:DEC-12 acceptată"
affected_records:
  - "repo:export-service configurarea retenției"
  - "wiki:RUN-04 procedura de curățare"
owner_role: product-owner
status: awaiting-review
```

**Identificatorii de mai sus sunt exemple.** Înregistrați câte un rând de jurnal pentru fiecare schimbare logică aprobată: ID-ul propunerii, înregistrările vizate, versiunile anterioară și rezultată, aprobatorul, marcajul temporal și referința de merge sau publicare. Legați evenimentele native de audit de acel rând, fără să le înlocuiți istoricul.

**Oamenii iau decizia.** Un editor autorizat sau o automatizare restricționată aplică revizia aprobată. Limitați în consecință acreditările de scriere. Instrucțiunile singure nu separă redactarea de publicare. Aceeași distincție guvernează recuperarea.

## Context comun fără RAG

**O hartă de proiect este primul index de recuperare.** Păstrați o pagină pentru fiecare proiect cu ID-uri de surse, locații în depozit, chei de urmărire, domenii de autoritate și responsabili. Citiți mai întâi harta, apoi preluați înregistrarea relevantă după ID. Căutați când ID-ul nu este cunoscut.

### Casetă laterală: hartă de proiect exemplificativă

```yaml
project: export-service
map_id: MAP-01
policy:
  source_id: POL-01
  approved_version: 3
  owner_role: policy-owner
sources:
  requirements: {page_id: REQ-17, owner_role: product-owner}
  runbook: {page_id: RUN-04, owner_role: operations-owner}
  decisions: {register_id: DEC-REGISTER, owner_role: project-lead}
repository:
  key: export-service
  setup: README.md
  terms: CONTEXT.md
  decisions: docs/adr/
tracker:
  project_key: EXP
  active_task: EXP-42
```

**Conectorii direcți reduc copierea manuală.** Model Context Protocol (MCP) este un protocol de integrare pentru expunerea instrumentelor și contextului către aplicații AI. Folosiți conectori aprobați pentru wiki, sistemul de urmărire și depozit, acolo unde sunt disponibili. O preluare țintită limitează rezultatele irelevante, dar nu înlocuiește autorizarea sau verificările de actualitate. Urmați ghidul de securitate MCP din referințe când alegeți permisiunile conectorilor.

**Recuperarea exactă are un efort inițial redus.** Oferă dovezi citabile fără o bază de date vectorială. Limitele sunt clare: cineva întreține harta, întrebările largi cer căutare suplimentară, iar paginile mari ocupă spațiu în sesiune. Preluați secțiunea relevantă cu restricțiile din jur, nu un manual întreg.

**Lucrul offline folosește snapshot-uri explicite.** Înregistrați revizia exportată și marcați răspunsurile ca bazate pe snapshot. Nu publicați schimbări până când o persoană sau un conector autorizat verifică sursa actuală. Apoi faceți aceeași politică vizibilă în fiecare interfață.

## O politică, adaptoare diferite

**Păstrați o singură politică comună,** apoi distribuiți adaptoare scurte, specifice instrumentelor. Puneți versiunea aprobată a politicii pe primul rând al fiecărui adaptor sau set copiat de instrucțiuni. Includeți ID-ul sursei și un snapshot local revizuit pentru sesiunile fără acces la conector.

**Încărcarea diferă în funcție de instrument.** Codex documentează descoperirea stratificată a **`AGENTS.md`**. Claude Code descrie **`CLAUDE.md`**, importurile și memoria proiectului. Cline documentează **`.clinerules/`** și comenzile regulilor. Folosiți documentația oficială legată în referințe. Verificați instrucțiunile încărcate în versiunea instalată, fără să presupuneți că numele fișierelor se comportă la fel.

### Casetă laterală: antet AGENTS.md exemplificativ

```markdown
Versiunea politicii: v3 | Sursă: wiki:POL-01 | Stare: aprobată

# Instrucțiunile proiectului

Citiți harta proiectului MAP-01 înainte de a începe o sarcină.
Încărcați docs/policy-snapshot.md și înregistrați revizia sursei.
Tratați memoria chat-ului și extrasele de căutare ca memorii cache.
Atașați reviziile surselor la fiecare propunere factuală.
Folosiți o ramură și un worktree pentru fiecare sarcină de programare.
Nu publicați politica, nu aprobați decizii și nu faceți merge la propriul PR.
Opriți-vă la conflicte de surse sau scrieri suprapuse nerezolvate.
Verificări obligatorii: teste, revizuirea documentației, actualitatea politicii.
Responsabili: mentenanță inginerească, produs, politici.
```

**Instrucțiunile proiectelor de chat primesc același antet și procedură.** Persoanele care nu programează primesc snapshot-ul politicii și harta proiectului prin încărcări sau conectori aprobați. Dacă interfața nu oferă acces live, o persoană furnizează exportul versionat și înregistrează limitarea.

**Eticheta versiunii este o afirmație, nu o dovadă a conținutului identic.** Generați adaptoarele din snapshot-ul aprobat sau comparați secțiunile de politică cu un digest stocat. Revizuiți separat excepțiile specifice adaptorului. Verificați regulile dezactivate, suprascrierile imbricate și instrucțiunile personale în timpul pilotului. Apoi înregistrați dovezile folosite de fiecare sarcină.

## Înregistrați un manifest de context

**Un manifest de context explică dovezile răspunsului.** Înregistrați ID-urile și reviziile paginilor, cheile issue-urilor și revizia sau ora actualizării lor, precum și ID-urile complete ale commiturilor din depozit. Includeți momentul recuperării și secțiunile relevante. Marcați înregistrările indisponibile în loc să le înlocuiți cu un rezumat reținut din memorie.

```yaml
task: EXP-42
policy: {page_id: POL-01, version: 3}
wiki:
  - {page_id: REQ-17, version: 8, section: export-retention}
tracker:
  - {issue_key: EXP-42, revision: 5}
repository:
  commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  files: [README.md, config/retention.yaml]
limits:
  - "Runbook-ul nu a fost recuperat. Nu s-a propus nicio schimbare a runbook-ului."
```

**Valoarea commitului este fictivă.** Într-un manifest real, înlocuiți-o cu commitul inspectat. Adăugați marcajul temporal al recuperării în timpul citirii efective. O înregistrare creată înainte de inspecție este o listă de verificare, nu o dovadă.

**Citațiile ajută verificarea,** nu generează automat încredere. Indicați înregistrarea și secțiunea care susțin fiecare afirmație importantă. Dacă două surse nu sunt de acord, păstrați-le pe ambele în manifest și raportați diferența nerezolvată. Nu alegeți doar pe baza marcajului temporal cel mai recent, fără să verificați domeniul și aprobarea. Această disciplină se aplică și recuperării semantice.

## Context comun cu RAG

**Generarea augmentată prin recuperare (RAG)** furnizează material recuperat unui model în timp ce acesta formulează un răspuns. Un index semantic găsește fragmente relevante chiar când întrebarea folosește alte formulări. Prezentarea generală RAG de la Microsoft descrie fundamentarea, limitele recuperării și cerințele de control al accesului. Consultați sursa oficială din referințe.

**Folosiți RAG pentru descoperire în colecții mari,** inclusiv documentație veche, note de ședință și transcrieri. Etichetați clasele de documente și stările de aprobare. O transcriere indexată din înregistrarea originală este o sursă pentru ce au spus participanții, nu o autoritate pentru cerințe aprobate. Nu transformați conversația în politică prin indexare.

| Regulă de indexare | Comportament necesar |
|---|---|
| **Ingerați surse, nu cache-uri** | Excludeți rezumatele generate și copiile locale neurmărite |
| **Păstrați proveniența** | Stocați ID-ul sursei, revizia, secțiunea și starea documentului pentru fiecare fragment |
| **Reîmprospătați la schimbare** | Reindexați modificările și invalidați fragmentele învechite |
| **Respectați schimbările de acces** | Actualizați permisiunile și eliminați conținutul șters sau revocat |
| **Returnați citații** | Afișați referințele înregistrărilor lângă textul recuperat |
| **Verificați înregistrarea live** | Preluați dovezi actuale înainte de a propune o acțiune importantă |

**În acest model, un fragment recuperat este doar un indicator.** Textul ajută la localizarea dovezii. Sursa live confirmă formularea actuală, aprobarea, excepțiile din jur și accesul. Dacă recuperarea live eșuează, etichetați snapshot-ul și opriți acțiunea durabilă. Aceasta este o regulă de guvernanță, nu o afirmație despre fiecare implementare RAG.

**Embeddings-urile vechi și contextul lipsă creează riscuri separate.** Un fragment vechi nu include o revizie. Un fragment actual poate induce totuși în eroare dacă excepția se află în secțiunea următoare. Păstrați titlurile și recuperați restricțiile adiacente înainte de a evalua o cerință.

**Scurgerea permisiunilor necesită un test separat.** Aplicați autorizarea înainte de a returna fragmente modelului, nu după generarea răspunsului. Filtrați conținutul sensibil înainte de indexare sau de apeluri externe pentru embeddings. Luați în calcul textul copiat în loguri, cereri către model și urme de recuperare. Un model local nu transformă un conector la distanță într-unul local. Aceste verificări decid dacă RAG se potrivește pilotului.

## Alegeți harta, RAG sau ambele

**Potriviți recuperarea cu întrebarea.** Un ID de cerință cunoscut favorizează accesul direct. O întrebare deschisă despre materiale istorice dispersate favorizează căutarea. Începeți cu harta dacă descoperirea nu este deja o problemă măsurată.

### Casetă laterală: RAG sau nu?

```text
Sarcinile numesc de obicei proiectul, pagina, issue-ul sau fișierul?
  Da -> Recuperarea directă este suficientă pentru pilot?
           Da -> DOAR HARTĂ
           Nu -> HIBRID: hartă pentru ID-uri cunoscute, RAG pentru descoperire
  Nu -> Dovezile sunt împrăștiate într-o colecție mare?
           Nu -> DOAR HARTĂ, plus căutarea nativă
           Da -> Activitatea este exploratorie și doar pentru citire?
                    Da -> DOAR RAG pentru descoperire
                    Nu -> HIBRID cu verificări ale sursei live

Fiecare opțiune păstrează responsabilii, autorizarea și proveniența.
Descoperirea bazată pe RAG verifică sursele înaintea acțiunilor durabile.
```

**Numai RAG descrie interfața de recuperare,** nu permisiunea de a omite guvernanța. Folosiți-o pentru o colecție exploratorie limitată, unde verificarea directă a sursei rămâne posibilă. Este o alegere slabă pentru schimbări cu ID cunoscut care necesită verificări precise ale versiunii.

**Modelul hibrid separă descoperirea de verificare.** Harta gestionează căutările cunoscute. RAG localizează înregistrările necunoscute. RAG răspunde la „unde”. Sursa răspunde la „ce”. Pentru exemplul de retenție, preluați direct **`REQ-17`**. Pentru „ce decizii mai vechi despre export explică limita?”, căutați în registru și preluați fiecare decizie relevantă. Acum aplicați partea de depozit.

## Informații din interiorul depozitului

**Cunoștințele depozitului se schimbă odată cu implementarea.** Păstrați o structură compactă, astfel încât un agent și un revizor să știe unde să caute.

| Fișier sau director | Responsabilitate |
|---|---|
| **`CONTEXT.md`** | Termeni de proiect și legături către înregistrările oficiale |
| **`docs/adr/`** | Decizii acceptate de arhitectură ale depozitului |
| **`docs/design/`** | Descrieri aprobate ale comportamentului sistemului |
| **`docs/plans/`** | Planuri de implementare propuse, cu stare explicită |
| **`AGENTS.md`** | Porți de revizuire, limite și rolurile responsabililor |
| **`README.md`** | Configurare și puncte de intrare, nu cerințe duplicate |

**Aplicați regula aceluiași PR:** schimbați simultan codul și documentele afectate din depozit. Dacă nu este necesară actualizarea bazei de cunoștințe, cereți o excepție scrisă în descrierea PR-ului sau în locul convenit pentru trailerul commitului.

```text
KB-Update: none (motiv: refactorizarea internă păstrează comportamentul documentat)
```

**Pipeline-ul aplică declarația.** O verificare obligatorie respinge schimbările de comportament fără actualizări de documentație sau o excepție. Un responsabil uman pentru documentație revizuiește excepția. O verificare bazată pe căi identifică schimbări candidate, dar nu dovedește completitudinea semantică. Impuneți verificarea și revizuirea prin protecția branch-ului sau un control de merge echivalent.

**O poartă absentă din pipeline nu este o poartă.** Menționarea „revizuirii documentației” într-un fișier de instrucțiuni oferă doar îndrumare. Testați aplicarea trimițând un PR intenționat incomplet în pilot și confirmând că merge-ul rămâne blocat.

**Folosiți o sarcină, o ramură și un worktree.** Documentația oficială Git despre worktree descrie arbori de lucru separați cu propria stare de checkout. Worktree-urile separate reduc conflictele locale de editare. Nu împiedică două ramuri să schimbe același fișier sau doi agenți să actualizeze aceeași pagină wiki.

**Nu faceți niciodată commit direct pe ramura implicită,** indiferent dacă se numește **`main`**, **`master`** sau altfel. Raportați diferențele cerință-cod în instrumentul de urmărire. Atașați înregistrările conflictuale și lăsați responsabilii să decidă comportamentul dorit înainte de a alinia oricare parte. Aplicați controale echivalente în afara Git.

## Informații din afara depozitului

**Wiki-ul are nevoie de un standard documentar.** Fiecare pagină autoritară include scop, stare, responsabil, revizie, dată de revizuire și ID-uri de surse asociate. Puneți propunerile într-o zonă de ciorne marcată clar ca neautoritară. Nu amestecați formulări propuse într-o pagină cu cerințe aprobate.

**Actualizările sigure urmează o succesiune fixă:**

1. **Recitiți** pagina actuală și restricțiile din jur.
2. **Comparați** versiunea ei cu versiunea de bază a propunerii.
3. **Reconciliați** editările intervenite și obțineți o nouă aprobare pentru textul schimbat.
4. **Scrieți** revizia aprobată cu o condiție privind versiunea așteptată.
5. **Verificați** pagina salvată și adăugați referința jurnalului de schimbări.

**Simpla recitire nu elimină concurența la scriere.** Folosiți mecanismul de actualizare condiționată al sistemului, dacă există. În lipsa lui, serializați publicarea printr-un singur responsabil și verificați rezultatul. Opriți-vă dacă un alt autor schimbă baza în timpul revizuirii.

**Regula de neștergere se aplică fluxurilor agenților.** Agenții propun arhivarea sau eliminarea. Oamenii autorizați aplică procedurile de retenție și ștergere. Nu interpretați regula ca permisiune de a păstra date sensibile pe termen nelimitat.

**Constatările din instrumentul de urmărire conțin dovezi,** nu doar concluzii. Înregistrați ce ați observat, comanda sau metoda exactă de inspecție, commitul inspectat, comportamentul așteptat și real și criteriile de acceptare. Eliminați secretele și rezultatele sensibile înainte de atașarea dovezilor. Marcați comenzile sugerate ca neexecutate până când cineva le rulează.

```text
Constatare: implementarea retenției nu corespunde cerinței aprobate
Dovezi: REQ-17 v8 și config/retention.yaml inspectat
Comandă de inspecție: git show HEAD:config/retention.yaml
Commit: ID-ul complet al commitului inspectat este înregistrat în manifest
Acceptare: durata aprobată corespunde codului, testelor și runbook-ului
Stare: în așteptarea revizuirii responsabililor de produs și inginerie
```

**Exemplul este un șablon de constatare,** nu un rezultat măsurat. Completați-l după inspecția reală. Legați actualizarea wiki-ului și dovezile din instrumentul de urmărire prin ID-ul propunerii.

**Registrul deciziilor separă regulile de raționament.** Stocați întrebarea, opțiunile, recomandarea, compromisurile, responsabilul, starea aprobării și referința regulii rezultate. Agenții propun. Oamenii decid. Regulile aprobate intră în politici și proceduri. Raționamentul lor rămâne în registru.

**Colectați faptele durabile din ședințe și chat-uri.** Trimiteți o propunere cu dovezile sursei și cereți aprobarea. Până la publicare, marcați înțelegerea ca provizorie. Apoi legați comportamentul aprobat între depozit și wiki.

## Conectați cele două sisteme

**Sincronizarea după merge transmite schimbările de implementare în exterior.** Creați o sarcină de actualizare a wiki-ului legată de commitul combinat, cerința aprobată și runbook-ul afectat. Un agent redactează actualizarea. Responsabilul wiki-ului verifică pagina curentă și aprobă publicarea. Păstrați sarcina deschisă până verificați revizia salvată.

**Actualitatea politicii este un audit separat.** Comparați fiecare adaptor din depozit și fiecare copie a instrucțiunilor de chat cu versiunea canonică aprobată. Politica **`v3`** se află la **`POL-01`**. Fiecare **`AGENTS.md`** indică **`v3`** pe primul rând. Auditul semnalează **`v2`**, etichetele lipsă și nepotrivirile de conținut, chiar și când etichetele coincid.

| Verificare | Dovada finalizării |
|---|---|
| **Actualitatea politicii** | Comparația versiunii canonice cu digestul adaptorului |
| **Reconcilierea cerințelor** | Revizia cerinței comparată cu codul și testele |
| **Sincronizare după merge** | Commitul combinat legat de revizia publicată în wiki |
| **Rezolvarea conflictelor** | Decizia aprobată de responsabil legată de ambele înregistrări |

**Reconciliați după program sau la momentul PR-ului.** Un audit săptămânal se potrivește unui pilot. Un PR care schimbă comportamentul necesită verificarea cerinței înainte de merge. Alegeți frecvența după costul derivei și înregistrați ultima verificare reușită.

**Schimbarea la treizeci de zile are mai multe puncte de control:** produsul aprobă cerința, ingineria actualizează configurarea și testele, revizorii fac merge la PR, iar operațiunile publică actualizarea runbook-ului. Un rând din jurnal leagă înregistrările rezultate. O sincronizare wiki eșuată rămâne vizibilă, nu dispare în spatele unui merge reușit. Predările comune păstrează succesiunea între instrumente.

## O procedură pentru fiecare instrument

**Împachetați pașii repetați ca skills sau prompturi,** cu un ID de procedură versionat. Partajați contractul, nu un format de fișier universal presupus. Fiecare adaptor de instrument oferă mecanismul de încărcare sau invocare acceptat.

| Procedură | Rezultat obligatoriu |
|---|---|
| **Începerea sarcinii** | Responsabil, domeniu, versiunea politicii, manifestul surselor, rezervarea scrierii |
| **Verificarea documentelor** | Metadate lipsă, autoritate duplicată, referințe de sursă invalide |
| **Verificarea cunoștințelor** | Diferențe cerință-cod cu revizii justificative |
| **Predare** | Dovezi curente, propuneri, verificări finalizate, întrebări nerezolvate |

**Neprogramatorii lucrează fără Git.** Ei recuperează surse permise în proiecte de chat, completează același șablon de propunere și îl trimit responsabilului printr-o pagină de ciornă sau o sarcină din instrumentul de urmărire. Nu au nevoie de checkout al depozitului pentru a cere corectarea unei cerințe.

**Programatorii folosesc fișierele depozitului și porțile PR.** Ei leagă propunerea aprobată în PR, înregistrează commiturile inspectate și rulează verificările obligatorii. Ambele grupuri transmit aceeași structură de dovezi.

```yaml
handoff:
  task: EXP-42
  policy_version: 3
  manifest: "ID-urile și reviziile surselor, plus commitul inspectat, sunt atașate"
  completed: [requirement-review]
  proposals: [PROP-042]
  pending: [implementation-review, runbook-publication]
  reservations: ["publicarea RUN-04 este atribuită responsabilului de operațiuni"]
  unresolved: []
  next_owner_role: engineering-maintainer
```

**O predare este tot un cache.** Următoarea persoană recitește sursele înainte de a acționa și înregistrează revizii noi. Nu considerați „finalizat” drept dovadă fără să verificați aprobarea sau testul legat. Aplicați măsurile de protecție de mai jos înainte de orice scriere.

## Măsuri de protecție înaintea fiecărei scrieri

**Verificați datele înainte să iasă din sistemul lor de origine.** Controlați clasificarea, permisiunile conectorilor, destinațiile aprobate, gestionarea de către furnizorul modelului și jurnalizarea. Trimiteți doar conținutul relevant minim. Păstrați înregistrările restricționate în afara proiectelor de chat și serviciilor de embedding neautorizate.

**Textul recuperat este dovadă, nu canal de instrucțiuni.** O pagină wiki sau un răspuns al unui instrument care îi spune agentului să ignore politica nu îi schimbă autoritatea. Revizuiți separat instrucțiunile provenite din conținut față de politica operațională aprobată. Limitați conectorii la acces de citire în timpul recuperării și separați acreditările de publicare de accesul sesiunii.

**Atribuiți un responsabil activ pentru fiecare pagină sau fișier.** Înregistrați rezervarea în instrumentul de urmărire cu domeniu și expirare. Recitiți înainte de scriere și folosiți verificări de versiune. Worktree-urile separate ajută izolarea locală; rezervările și scrierile condiționate gestionează înregistrările partajate.

| Motiv pentru oprire și întrebare | Răspuns necesar |
|---|---|
| **Sursele nu sunt de acord și nu au responsabil** | Opriți și cereți desemnarea autorității |
| **Altă sarcină a rezervat ținta** | Negociați responsabilitatea înainte de editare |
| **Versiunea de bază s-a schimbat** | Reconciliați și solicitați o nouă aprobare |
| **O afirmație importantă nu are dovezi** | Marcați-o ca neverificată și cereți o sursă |
| **Gestionarea datelor nu este clară** | Păstrați conținutul în sistemul de origine |
| **Accesul la sursa live eșuează** | Notați limitele snapshot-ului și opriți acțiunea durabilă |

**Prompturile nu sunt controale de securitate.** Testați în afara modelului refuzul permisiunilor, ramurile protejate, respingerea unei baze vechi și responsabilitatea scrierii. O demonstrație conformă nu ajunge dacă acel cont are drepturi de publicare nelimitate. Folosiți testele pentru a decide dacă pilotul este pregătit.

## Testați pilotul înainte de promovare

**Începeți cadrul ca proiect.** Testați un proiect cu un programator, un neprogramator și responsabili numiți ai surselor. Puneți aceeași întrebare cu ID cunoscut prin două instrumente, apoi simulați un conflict de surse. Revizuiți manifestele și propunerile, nu fluența prozei.

**Raționament așteptat:** ambii participanți identifică cerința aprobată curentă și descriu separat implementarea inspectată. Dacă nu sunt de acord, compară mai întâi intrările din manifest. Acesta este un exercițiu propus, nu un benchmark observat.

| Metrică | Definiție |
|---|---|
| **Rata citațiilor** | Afirmații importante susținute de surse ÷ afirmații factuale importante din eșantioane |
| **Constatări săptămânale de derivă** | Nepotriviri confirmate de autoritate sau versiune, grupate după tipul sursei |
| **Timpul propunerii** | Timpul median dintre propunerea pregătită de revizuire și decizia înregistrată |
| **Refacere din context vechi** | Sarcini redeschise din cauza dovezilor învechite sau neverificate |

**Măsurați o valoare de bază înainte de a stabili ținte.** Mai multe constatări de derivă în prima săptămână pot reflecta o detecție mai bună, nu o documentație mai slabă. Urmăriți recurența și timpul de rezolvare împreună cu numărul brut. Revizuiți dovezile sensibile fără să le copiați în exporturi de analiză.

**Livrați un depozit exemplificativ în timpul lansării.** Includeți o hartă sintetică, adaptoare de politică, manifeste, șabloane de propuneri, excepții documentare și verificări de revizuire executabile. Folosiți înregistrări wiki și de urmărire fictive, fără acreditări de producție. Demonstrați publicarea refuzată, respingerea unei baze schimbate, deriva versiunii politicii și o predare reușită.

**Un depozit de șabloane este un rezultat al lansării,** nu un material furnizat cu acest articol. Promovați modelul operațional după ce conducerea și responsabilii surselor revizuiesc rezultatele pilotului. Păstrați excepțiile și defecțiunile nerezolvate în registrul de decizii. Înainte de promovare, remediați problemele previzibile de mai jos.

## Depanarea contextului comun

| Simptom | Prima remediere |
|---|---|
| **Două instrumente răspund diferit** | Comparați ID-urile surselor, reviziile, domeniul și starea aprobării |
| **Instrucțiunile par actuale, dar comportamentul diferă** | Inspectați adaptoarele încărcate, regulile și suprascrierile locale |
| **RAG returnează cerințe vechi** | Verificați actualizarea indexului și preluați pagina live |
| **O editare wiki șterge altă schimbare** | Impuneți scrieri condiționate sau publicare serializată |
| **Verificările documentelor trec cu formulări vechi** | Adăugați revizuirea responsabilului și reconcilierea cerințelor |
| **Deciziile rămân în chat** | Atribuiți fluxul de propuneri și responsabilul registrului |

**Reparați traseul dovezilor înainte să rescrieți promptul.** Rulați din nou cazul pilot eșuat și înregistrați rezultatul. Folosiți lista de mai jos pentru a transforma procesul reparat într-o practică săptămânală.

## Zece pași pentru săptămâna aceasta

1. **Alegeți un proiect pilot** și participanții și instrumentele sale.
2. **Atribuiți o sursă și un responsabil** fiecărui tip de informație.
3. **Publicați o hartă de proiect** cu ID-urile surselor și domeniile de autoritate.
4. **Redactați o politică comună** și obțineți revizuirea responsabilului.
5. **Versionați fiecare adaptor de instrucțiuni pe primul rând** și verificați încărcarea.
6. **Cereți un manifest de context** pentru răspunsuri și propuneri factuale importante.
7. **Creați fluxul de propuneri** cu versiuni de bază și aprobatori numiți.
8. **Impuneți controale de scriere** și regula documentației din același PR.
9. **Testați deriva, conflictul și predarea** cu înregistrări sintetice.
10. **Revizuiți indicatorii pilotului** și aprobați următoarea etapă.

**Dați fiecărui fapt o sursă, faceți fiecare instrument să citească din ea și treceți fiecare schimbare durabilă printr-o persoană.**

## Referințe și pașii următori

**Documentația oficială susține componentele tehnice,** nu regulile organizaționale ale cadrului. Verificați comportamentul instrumentelor instalate și permisiunile conectorilor în timpul pilotului.

- **Instrucțiuni Codex:** [Instrucțiuni personalizate cu AGENTS.md](https://developers.openai.com/codex/guides/agents-md), despre descoperirea și verificarea instrucțiunilor.
- **Instrucțiuni Claude Code:** [Cum își amintește Claude proiectul](https://code.claude.com/docs/en/memory), despre instrucțiunile proiectului și memorie.
- **Instrucțiuni Cline:** [Reguli](https://docs.cline.bot/customization/cline-rules), despre regulile spațiului de lucru și controlul activării.
- **Proiectarea recuperării:** [Generare augmentată prin recuperare în Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), despre fundamentare, limite de recuperare și securitate.
- **Securitatea conectorilor:** [Cele mai bune practici de securitate MCP](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices), despre autorizare și riscurile conectorilor.
- **Izolarea worktree-urilor:** [Documentația Git worktree](https://git-scm.com/docs/git-worktree), despre arbori de lucru separați și starea comună a depozitului.

**Pentru planificarea inferenței locale,** citiți [Ghidul de context GPU pentru IA locală](/articles/local-ai-model-gpu-context-guide/). Capacitatea hardware și guvernanța surselor comune rezolvă probleme diferite. O fereastră de context mai mare nu repară o autoritate conflictuală.

{{< centerbutton href="/articles/local-ai-model-gpu-context-guide/" >}}
  Citiți Ghidul de context GPU pentru IA locală
{{< /centerbutton >}}

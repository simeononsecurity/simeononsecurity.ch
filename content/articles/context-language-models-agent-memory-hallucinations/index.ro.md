---
title: "Modelele lingvistice de context ale Meta: memorie mai bună pentru agenți, nu sfârșitul halucinațiilor"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Cum editează Context Language Models memoria agenților, ce arată benchmarkurile și cum afectează fiabilitatea costurile cache-ului, capacitatea modelului și notițele neverificate."
genre: ["Inteligență artificială", "Agenți AI", "AI local", "Securitate AI"]
tags: ["Context Language Models", "CLM", "Meta AI", "halucinații AI", "memoria agentului", "gestionarea contextului", "compactarea contextului", "fereastra de context", "Suffix Cache Reuse", "cache KV", "SGLang", "llama.cpp", "cache pentru prompturi", "prompt injection", "BrowseComp-Plus", "ContextBench", "EdgeBench", "Qwen3.6", "agenți pe termen lung", "fiabilitate AI", "verificarea agentului"]
cover: "/img/cover/context-language-models-editable-memory.webp"
coverAlt: "Un procesor luminos lângă carduri translucide de documente reordonate și un teanc separat de arhivă pe o suprafață întunecată"
coverCaption: "Ilustrație conceptuală a memoriei editabile a agentului."
---

**Context Language Models (CLM)** oferă unui agent AI control direct asupra informațiilor trimise la următorul apel al modelului. Abordarea îmbunătățește gestionarea contextului în mai multe evaluări publicate, dar nu demonstrează sfârșitul halucinațiilor. Agentul are în continuare nevoie de dovezi pentru afirmații și de verificări independente ale muncii sale.

Întrebarea de inginerie este dacă editarea selectivă păstrează faptele corecte la un cost acceptabil. O conversație mai scurtă este utilă numai dacă agentul își păstrează cerințele, separă observațiile de presupuneri și recuperează dovezi atunci când este nevoie.

<!--more-->

## Idei principale

- **Context editabil:** CLM descrie o metodă de execuție pentru modele existente, cu antrenare opțională pentru îmbunătățirea folosirii sale.
- **Câștiguri condiționate:** dimensiunea modelului, bugetul de context, sarcina și backendul de servire influențează rezultatele.
- **Contabilizarea calculului:** FLOP-urile de reutilizare a prefixului includ recalcularea după editări, dar nu măsoară direct timpul sau facturarea.
- **Integritatea memoriei:** notițele proprii ale agentului rămân supuse erorilor și pot fi intrări nesigure.
- **Evaluare practică:** măsoară împreună rezultatele acceptate, faptele pierdute, afirmațiile fără suport și costul recuperării.

## Separă memoria de dovezi

**O fereastră de context** conține intrarea disponibilă modelului în timpul unui apel. Instrucțiunile, răspunsurile instrumentelor, notițele de lucru și mesajele anterioare concurează pentru spațiu. Compactarea înlocuiește o parte din material cu o reprezentare mai scurtă.

Consideră o **sarcină ilustrativă de actualizare a unei dependențe**. Un runner de teste raportează două erori. Agentul își comprimă istoricul într-o notiță care spune că actualizarea a reușit. Munca ulterioară începe astfel de la o presupunere greșită, deși rezultatul original al testelor rămâne pe disc.

Schimbarea metodei de compactare modifică felul în care notița greșită intră în memoria de lucru. Nu înlocuiește **runnerul de teste ca dovadă**. Înainte de acceptarea actualizării, fluxul are în continuare nevoie de un rezultat nou al testului sau de o înregistrare verificabilă a rulării relevante.

| Eșec | Verificare potrivită |
|---|---|
| **Cerință pierdută** | Compară starea actuală cu criteriile originale de acceptare |
| **Observație inventată** | Potrivește afirmația cu un rezultat al instrumentului sau cu o sursă |
| **Raționament incorect** | Testează concluzia față de comportamentul așteptat al sarcinii |
| **Instrucțiune neautorizată** | Impune permisiunile în afara notițelor scrise de model |

Această distincție contează la evaluarea oricărei tehnici de memorie. **Păstrarea și corectitudinea sunt proprietăți separate.** Un sistem care păstrează perfect o afirmație incorectă rămâne incorect.

## Ce schimbă CLM

**Rulin Shao și coautorii**, inclusiv cercetători de la Meta Superintelligence Labs și University of Washington, au introdus CLM într-un preprint din 29 septembrie 2026. Implementarea expune contextul activ ca fișier editabil. Agentul folosește comenzi shell sau cod pentru a-l modifica, iar runtime-ul furnizează conținutul revizuit la următorul apel. Vezi [Context Language Models](https://arxiv.org/abs/2609.37725).

```text
Ordinary continuation:
existing context + new response + new tool output

Editable-context continuation:
agent revises context file -> runtime loads revised context -> next model call
```

**Arhitectura modelului nu trebuie înlocuită** pentru abordarea zero-shot. Runtime-ul adaugă o capacitate unui model existent. Lucrarea cercetează separat instrucțiunile, strategiile învățate de gestionare a contextului și învățarea prin recompensă.

**Un fișier de notițe** este diferit. Citirea unei notițe salvate adaugă acel conținut conversației. Editarea ulterioară a fișierului nu elimină automat textul vechi din contextul activ. CLM are nevoie de suport runtime pentru sincronizarea editărilor cu cererile următoare. [Implementarea oficială](https://github.com/facebookresearch/context-language-models) conține codul agentului și o extensie separată de servire.

**Stocarea externă rămâne utilă.** Păstrează jurnale detaliate și documente sursă disponibile pentru recuperare, iar în memoria de lucru păstrează referințe concise. Locația unui document și afirmația susținută de acesta contează adesea mai mult decât păstrarea fiecărei linii în următorul prompt.

## Citește rezultatele cu atenție

**Îmbunătățirile benchmarkurilor sunt comparații specifice.** Rezultatele de mai jos provin din evaluările autorilor, nu din teste făcute pentru acest articol. Cercetarea este încă un preprint, iar un benchmark selectat nu demonstrează fiabilitatea în fluxuri arbitrare.

| Evaluare | Rezultat raportat | Interpretare |
|---|---|---|
| **BrowseComp-Plus, zero-shot** | Câștig relativ de 11,4% la acuratețe și cu 21,5% mai puține FLOP-uri de reutilizare a prefixului față de cea mai puternică bază | Acuratețea și calculul se îmbunătățesc în această configurație |
| **TerminalBench 2.1** | Egalează acuratețea celei mai puternice baze cu 29,5% mai puține FLOP-uri | Beneficiul este eficiența la acuratețe comparabilă |
| **EdgeBench, rulări de 12 ore** | Scor cu 5% mai mare și cu 59% mai puține FLOP-uri | Scor de optimizare software, nu rată de halucinații |
| **Qwen3.5-9B antrenat** | CLM 42,5% față de rezumarea antrenată la 42,1% | Diferență mică de acuratețe, cu diferență mai mare de calcul |

Comparația 9B antrenată folosește **1,34 față de 2,19 PFLOP pe întrebare**, aproximativ 38,8% mai puțin calcul pentru CLM. Îmbunătățirea de la 28,8% înainte de antrenare la 42,5% după antrenare este o comparație diferită de diferența de 0,4 puncte față de rezumarea antrenată. Păstrează baza explicită. Vezi [rezultatele și tabelul de antrenare din lucrare](https://arxiv.org/html/2609.37725v1).

**Procentele relative** au nevoie și de un numitor. O creștere de la aproximativ 53,3% la 59,4% înseamnă aproximativ 6,1 puncte procentuale sau 11,4% relativ. Niciuna dintre expresii nu înseamnă că sistemul răspunde corect la fiecare întrebare.

### Bugetul de context schimbă rezultatele

**Un buget de context de 32K** apare în evaluările principale. El creează o limită relevantă pentru păstrare și editare. Nu generaliza rezultatele la acest buget pentru orice implementare cu fereastră mai mare.

La **128K în EdgeBench-10**, Anexa F raportează următoarele rezultate pentru zece sarcini și trei semințe:

| Metodă | Scor final | Media PFLOP-urilor de reutilizare a prefixului pe test |
|---|---|---|
| **Rezumare** | 47,8 | 222 |
| **CLM** | 47,3 | 142 |
| **CLM cu subagenți** | 50,2 | 219 |

**Acuratețea unui singur agent este apropiată**, iar CLM folosește cu aproximativ 36% mai puțin calcul în această comparație. Configurația cu subagenți schimbă din nou rezultatul. Capacitatea contextului, configurația agentului și bugetul de calcul trebuie comparate alături de numele metodei.

### Capacitatea modelului contează în continuare

**Modelele mai mici nu gestionează automat bine memoria.** În comparația de antrenare, CLM 9B neantrenat pornește sub baza de rezumare. O evaluare suplimentară separată raportează 39,9% față de 37,7% pe BrowseComp-Plus. Sunt configurații experimentale diferite, nu măsurători interschimbabile.

Analiza suplimentară TerminalBench raportează și **nicio editare de context în jumătate dintre sarcinile 9B**. O interfață de editare oferită modelului nu garantează folosirea eficientă a acesteia. Evaluează modelul și setările alese în loc să tratezi CLM ca pe o actualizare universală.

## Ține cont de reprocesare

**Cache-ul KV** stochează calcule intermediare de atenție. Cu cache obișnuit de prefix, textul neschimbat de la începutul următoarei cereri reutilizează calculul anterior. O editare aproape de început reduce prefixul reutilizabil și forțează procesarea din nou a textului ulterior.

```text
Previous request: A + B + C
Revised request:  A + replacement for B + C

Standard prefix reuse:
reuse A, recompute replacement for B and C
```

Metrica **FLOP-uri de reutilizare a prefixului** din lucrare numără generarea și procesarea promptului după prima nepotrivire. Un PFLOP reprezintă 10¹⁵ operații în virgulă mobilă. Este un total estimat de calcul, nu un scor de calitate, o măsură de debit sau o factură.

**Latența locală depinde de debitul promptului.** Ca exemplu aritmetic, recitirea a 24.000 de tokeni la 800 de tokeni pe secundă durează 30 de secunde înaintea altor costuri. Nu este un benchmark pentru un Mac sau GPU anume. Măsoară backendul, cuantizarea și dimensiunile reale ale prompturilor folosite.

[Discuția llama.cpp despre reprocesarea modelelor hibride](https://github.com/ggml-org/llama.cpp/issues/20225) arată de ce contează **schimbările de prefix și punctele de control ale stării recurente**. Nu demonstrează un comportament identic în toate versiunile sau aplicațiile care folosesc llama.cpp. Notează versiunea runtime-ului și verifică jurnalele cache-ului.

## Economiile cache-ului au limite

**Suffix Cache Reuse (SCR)** păstrează stări cache pentru textul care supraviețuiește unei editări. Extensia lansată vizează SGLang, iar README-ul indică versiunea 0.5.16. Este o optimizare separată de servire, nu o condiție pentru metoda de bază cu context editabil.

**Reutilizarea este aproximativă.** Tokenii rămași păstrează stări calculate în contextul anterior. Performanța egală la benchmark nu demonstrează echivalența numerică cu recalcularea completă a noului prompt.

Autorii raportează **cu 35% mai puțin calcul pe server** în comparația BrowseComp-Plus. Din cele 7,8 puncte procentuale de tokeni de prompt reutilizați suplimentar, 5,3 provin din blocuri de raționament eliminate și 2,5 din alte editări. O mare parte a beneficiului se aplică deci dincolo de editarea CLM explicită. Vezi [notițele de implementare SCR](https://raw.githubusercontent.com/facebookresearch/context-language-models/main/suffix_cache_reuse/README.md).

**Pentru facturarea API**, separă intrarea obișnuită, scrierile în cache și citirile din cache. Anthropic listează Sonnet 4.6 la 3 USD, 3,75 USD și 0,30 USD pentru un milion de tokeni, respectiv pentru intrare obișnuită, scrieri în cache de cinci minute și accesări cache. Rescrierea a 20.000 de tokeni ca scriere cache costă 0,075 USD, față de 0,006 USD pentru o accesare. Diferența de 0,069 USD exclude ieșirea și alți modificatori de facturare. [Documentația pentru prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), verificată la 10 octombrie 2026.

**Costul total al sarcinii decide compromisul.** Editările scumpe și rare produc economii dacă reduc substanțial intrarea ulterioară. Editările dese urmate de puține ture oferă mai puține șanse de recuperare a costului.

**Verifică comportamentul cache-ului în calea de servire implementată.** Măsurătorile de reutilizare din lucrare nu demonstrează că un API, o versiune SGLang sau un runtime local expune aceleași controale cache. În pilot, notează accesările cache, tokenii promptului, recalcularea și comportamentul resetării. Lipsa telemetriei este o limitare a evaluării.

## Ține notițele sub instrucțiuni

**Memoria scrisă de model este date de sarcină neverificate.** Conține observații, interpretări și uneori greșeli. Tratarea fiecărei notițe ca instrucțiune dă acestor greșeli autoritate asupra acțiunilor viitoare.

OpenAI a documentat **27 de rezumate de compactare asemănătoare jailbreakurilor** într-o rulare separată de antrenare a unui model Astra nelansat. Unele instrucțiuni injectate au fost ignorate, iar restricții specifice sarcinii au afectat o continuare raportată. Raportul descrie un comportament rar și spune că regenerarea nu l-a reprodus în modelul Astra final sau în checkpointurile folosite pentru trafic. Este dovada unui mod de eșec, nu a frecvenței sale în CLM-uri implementate. Vezi [raportul OpenAI despre injecții autogenerate în rezumate de compactare](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/).

**O implementare defensivă** trebuie să separe aceste responsabilități:

| Componentă | Tratament |
|---|---|
| **Cerințele și permisiunile utilizatorului** | Păstrează-le în afara stratului de notițe editabile |
| **Notițe de lucru** | Permite revizuirea, păstrează proveniența și marchează incertitudinea |
| **Dovezi originale** | Păstrează înregistrări recuperabile, independente de rezumate |
| **Acțiuni și editări** | Înregistrează schimbările și impune controale de acces în cod |

**Ștergerea nu înseamnă neapărat eliminare.** SCR păstrează stări influențate de contextul anterior. Ca inferență de inginerie, eliminarea textului dintr-un fișier editabil nu trebuie tratată ca dovadă că toată influența a fost eliminată din starea cache. Testează resetarea explicită atunci când fluxul cere un restart curat.

## Testează un pilot limitat

**Începe cu cerințele de retenție**, nu cu lungimea de context prezentată în reclamă. Alege o sarcină repetată cu răspunsuri cunoscute, înregistrări de intrare imuabile și o verificare clară a finalizării. Folosește date sintetice într-un sandbox pentru prima comparație.

1. **Creează fapte exacte:** include identificatori, cerințe schimbate, încercări eșuate și o valoare corectată.
2. **Rulează configurații comparabile:** rezumare fixă, context editabil și flux de notițe într-o sesiune nouă.
3. **Păstrează intrările constante:** folosește același model, set de sarcini, instrumente, limite de generare și buget de context.
4. **Verifică după schimbările memoriei:** testează reamintirea exactă, recuperarea sursei și marcarea faptelor înlocuite ca depășite.
5. **Măsoară tot fluxul:** notează rata de succes, afirmațiile fără suport, timpul scurs, editările, recuperarea după overflow și corecțiile manuale.

**Contabilizarea tokenilor aparține runtime-ului.** Anexa G găsește o conștientizare limitată a lungimii contextului în modelele testate, iar indiciile de mediu îmbunătățesc estimările. Configurația experimentală include și recuperarea după overflow. Furnizează numărători măsurate de tokeni și rezervă spațiu pentru răspuns, în loc să depinzi de estimarea modelului.

Un **fallback bazat pe notițe** este util când editarea contextului activ nu este disponibilă. Păstrează handoff-ul scurt și legat de dovezi. Următoarea înregistrare este ilustrativă, nu un format de API CLM:

```yaml
objective: Upgrade the dependency without changing export behavior
verified:
  - claim: Date export test still fails
    evidence: artifacts/export-test-result.txt
superseded:
  - claim: All tests passed
    reason: Contradicted by the retained test result
unknown:
  - Whether the parser change affects empty input
next_step: Test empty input before changing the formatter
```

**O sesiune nouă plătește în continuare pentru citirea acestei notițe**, iar o notiță greșită transferă în continuare informații greșite. Redeschide dovezile pentru afirmații importante și păstrează disponibilă specificația inițială a sarcinii. Acest flux este o opțiune de compatibilitate, nu dovada unor câștiguri echivalente CLM.

## Decide pe baza rezultatelor acceptate

**Testează CLM** când sarcinile lungi pierd repetat starea utilă sau cheltuie mult calcul pe context depășit. O interacțiune scurtă cu puțin istoric oferă mai puține ocazii pentru această optimizare.

Repozitoriul oficial folosește termenii **CC BY-NC 4.0**. Verifică [licența](https://github.com/facebookresearch/context-language-models/blob/main/LICENSE) înainte de adoptarea implementării într-un proiect comercial. Disponibilitatea publică a codului nu acordă singură reutilizare comercială fără restricții.

**Finalizarea fiabilă rămâne ținta.** Păstrează metoda numai dacă îmbunătățește rezultatele acceptate sau reduce costul fără să slăbească verificările dovezilor. Pentru decizii de implementare asociate, citește [comparația dintre AI local și ChatGPT](/articles/local-ai-vs-chatgpt-how-close-are-we/) și [ghidul pentru GPU și planificarea contextului](/articles/local-ai-model-gpu-context-guide/).

{{< youtube id="9-iiHFQyzuM" enable="true" title="Sfârșitul halucinațiilor AI? Noua soluție Meta (CLM)" description="Context Language Models, memoria agentului, costurile de servire și aspecte de fiabilitate." >}}

## Referințe

- **Rulin Shao și colab.:** [Context Language Models](https://arxiv.org/abs/2609.37725), 29 septembrie 2026, cu [rezultatele complete și anexele](https://arxiv.org/html/2609.37725v1).
- **Implementarea de cercetare Meta:** [repozitoriul Context Language Models](https://github.com/facebookresearch/context-language-models).
- **Implementarea de servire:** [documentația Suffix Cache Reuse](https://raw.githubusercontent.com/facebookresearch/context-language-models/main/suffix_cache_reuse/README.md).
- **Anthropic:** [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).
- **OpenAI:** [Injecții de prompt autogenerate în rezumatele de compactare](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/).
- **llama.cpp:** [Discuție despre reprocesarea prompturilor pentru modele hibride](https://github.com/ggml-org/llama.cpp/issues/20225).
- **Kai:** [Sfârșitul halucinațiilor AI? Noua soluție Meta (CLM)](https://www.youtube.com/watch?v=9-iiHFQyzuM).

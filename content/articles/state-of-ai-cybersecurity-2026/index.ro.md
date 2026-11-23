---
title: "Securitatea cibernetică a IA în 2026: implementare rapidă, protecție ulterioară"
draft: false
toc: true
date: 2026-06-26
lastmod: 2026-11-23
description: "Evaluarea adoptării IA în securitatea cibernetică, a lacunelor operaționale, a îndrumărilor actuale și a controalelor practice pentru organizații în 2026."
tags: ["securitatea IA", "securitatea cibernetică a IA 2026", "injecție de prompt", "agenți IA", "securitate MCP", "lanțul de aprovizionare IA", "IA din umbră", "red teaming IA", "securitatea LLM", "observabilitatea IA", "IA agentică", "amenințări IA", "atacuri IA", "securitatea modelelor", "guvernanța IA", "NIST AI 600-1", "OWASP LLM", "MITRE ATLAS", "răspuns la incidente IA", "securitate IA pentru companii", "identitate IA", "otrăvirea contextului", "otrăvirea instrumentelor", "autorizarea IA"]
cover: "/img/cover/state-of-ai-cybersecurity-2026.webp"
coverAlt: "Ilustrație cu sisteme IA interconectate, reprezentate prin noduri luminoase pe un fundal întunecat. Liniile vii arată conexiunile, iar umbrele din jurul unor noduri indică vulnerabilități de securitate."
coverCaption: ""
---

În 2023, 2024 și 2025, organizațiile au implementat sisteme IA într-un ritm pe care îndrumările defensive, instrumentele de securitate și practicile operaționale nu l-au putut ține pasul. **În 2026, rezultatul este o suprafață de atac extinsă, insuficient monitorizată și conectată la sisteme reale de afaceri, în timp ce apărarea este încă în formare.**

Vreau să precizez ce mă îngrijorează și de ce. Nu este un avertisment general despre riscurile IA. Este o descriere a suprafeței reale de atac, a lacunelor documentate și a măsurilor pe care organizațiile trebuie să le adopte.

## De ce există această diferență

Securitatea software-ului tradițional s-a maturizat în aproximativ trei decenii. Decenii de experiență în răspunsul la incidente, cercetarea vulnerabilităților, dezvoltarea instrumentelor și cunoștințele operaționale câștigate cu greu au produs cadrele, produsele și practicile pe care se bazează programele moderne de securitate.

**IA generativă pentru companii a ajuns la milioane de implementări în producție în aproximativ doi ani.**

Disciplinele care fac securitatea software-ului eficientă, cum ar fi modelarea amenințărilor pentru arhitecturi specifice, modelele de implementare consolidată, procedurile mature de răspuns la incidente și practicile consacrate de audit și observabilitate, nu au avut timp să se dezvolte înainte ca organizațiile să înceapă să implementeze IA la scară largă. *Îndrumările au sosit după implementare. Instrumentele au sosit după îndrumări. Expertiza operațională este încă în dezvoltare.*

Nu este o acuzație. Explică de ce lacunele sunt structurale, nu accidentale.

## Cele patru niveluri ale securității IA

O mare parte din confuzia din discuțiile despre securitatea IA provine din tratarea documentelor de guvernanță, a taxonomiilor de amenințări, a îndrumărilor tehnice și a controalelor operaționale ca și cum ar fi același lucru. Nu sunt.

**Nivelul 1 este guvernanța.** NIST AI RMF, ISO/IEC 42001 și EU AI Act funcționează la nivel organizațional și de proces. Descriu cum se gestionează riscurile IA, cum se structurează supravegherea și cum se documentează responsabilitatea. Sunt cadre de guvernanță, nu controale tehnice.

**Nivelul 2 este taxonomia amenințărilor.** MITRE ATLAS documentează tacticile adversarilor împotriva sistemelor IA. OWASP Top 10 for LLMs și OWASP Agentic AI Top 10 enumeră clase specifice de atacuri. Aceste documente numesc atacurile, dar nu prescriu măsuri de apărare.

**Nivelul 3 este îndrumarea tehnică.** Google SAIF, Microsoft AI SDL, OWASP AI Exchange și NIST AI 600-1 oferă îndrumări pentru construirea și implementarea sigură a IA. NIST AI 600-1 este mult mai specific decât AI RMF de bază și acoperă injecția de prompt, otrăvirea datelor și pericolele informaționale din implementările IA generative.

**Nivelul 4 este operarea.** Monitorizarea, răspunsul la incidente, controalele la execuție, jurnalizarea, privilegiile minime, fluxurile de evaluare și guvernanța accesului sunt practici operaționale. Necesită procese organizaționale, nu doar documentație.

*Majoritatea organizațiilor au o acoperire incompletă la nivelurile 3 și 4. Acolo se află aproape tot riscul operațional.*

## Ce rulează în producție

IA pentru companii în 2026 nu înseamnă doar chatboturi. Sistemele în producție includ:

- **Sisteme RAG** care extrag informații din arhive interne de documente, wiki-uri, baze de date și înregistrări ale clienților
- **Agenți de asistență pentru clienți** cu acces la informații despre conturi și sisteme de gestionare a cazurilor
- **Asistenți interni pentru productivitate** integrați cu e-mailul, calendarele, sistemele de fișiere și platformele de comunicare
- **Instrumente de revizuire și generare a codului** cu acces la depozitele de cod sursă
- **Agenți automatizați** care rulează fluxuri de lucru programate cu acreditări pentru API-uri interne
- **Procesatoare de documente, contracte și date financiare**
- **Modele IA încorporate în detectarea fraudei, recrutare și decizii de control al accesului**

Fiecare sistem reprezintă o suprafață de atac diferită. Un sistem RAG peste baza internă de cunoștințe este atât un risc de divulgare a informațiilor, cât și o țintă pentru injecția de prompt. **Un agent cu acces la e-mail și o acreditare persistentă este un proces autonom cu influență reală asupra sistemelor reale.**

*Echipele de securitate nu au fost adesea implicate în decizia de a implementa aceste sisteme. Descoperă frecvent implementări IA existente în timpul auditului, nu al analizei de proiect.*

## IA se află acum de ambele părți

**Aceleași capacități IA disponibile echipei de securitate sunt disponibile și atacatorilor.**

**Dezvoltarea asistată de IA** reduce timpul necesar pentru a transforma dezvăluirile publice privind vulnerabilitățile în demonstrații de concept funcționale și instrumente operaționale. Oricine folosește aceste instrumente, inclusiv atacatorii, trece mai repede de la citirea unui CVE la cod funcțional.

**Conținutul de phishing generat de IA** produce e-mailuri cu o gramatică mai bună, un context mai convingător și mai puține greșeli detectabile decât multe atacuri scrise de oameni. Indiciile de formatare și tiparele lingvistice pe care utilizatorii au învățat să le recunoască sunt mai puțin fiabile când IA generează conținutul.

**Clonarea vocală pentru campanii de vishing** imită directorii și colegii în apeluri în timp real. Bariera de intrare pentru ingineria socială țintită a scăzut pe măsură ce sinteza vocală s-a îmbunătățit și costurile de acces au coborât.

**Videoclipurile deepfake pentru compromiterea e-mailurilor de afaceri** au trecut de la teorie la practică. Din 2024, în mai multe sectoare au fost documentate fraude financiare care folosesc videoclipuri cu directori generate de IA pentru autorizarea tranzacțiilor. *Instruirea de conștientizare a fost construită pentru un alt model de amenințare.*

## Inserarea instrucțiunilor și contaminarea conținutului de lucru

**Înțelegerea injecției de prompt este punctul de plecare pentru înțelegerea securității sistemelor IA.**

Un model lingvistic urmează instrucțiunile din fereastra sa de context. Aceasta include promptul de sistem, istoricul conversației, rezultatele instrumentelor și documentele extrase. **Modelul nu poate distinge în mod fiabil instrucțiunile dezvoltatorului aplicației de instrucțiunile inserate de un atacator în conținutul procesat.** Acesta este nucleul injecției de prompt în definiția OWASP.

*Injecția directă de prompt* vizează direct intrarea modelului. Utilizatorul oferă text menit să suprascrie instrucțiunile de sistem.

*Injecția indirectă de prompt* este mai gravă pentru implementările de companii. Agentul RAG extrage un document din baza de cunoștințe. Documentul conține instrucțiuni prin care agentul trebuie să facă altceva. Instrumentul de rezumare procesează o pagină web cu directive ascunse. Botul de asistență citește un atașament al clientului cu instrucțiuni. Agentul procesează instrucțiunile și acționează în baza lor.

**Otrăvirea contextului** este o categorie mai largă. Atacatorii nu trebuie să compromită modelul pentru a compromite sistemul IA. Trebuie să introducă conținut malițios în contextul modelului. Aici intră documente RAG otrăvite, înregistrări de memorie otrăvite, mesaje e-mail construite malițios și procesate de agent, PDF-uri adversariale și pagini web controlate de atacator pe care le vizitează un agent de navigare. *Acestea sunt diferite de otrăvirea modelului. Modelul este în regulă. Contextul nu.*

Apărarea în profunzime reduce acest risc. Filtrarea intrărilor, validarea ieșirilor, instrumentele cu domenii de acces limitate, execuția izolată și aprobarea umană pentru acțiuni cu consecințe ajută. **Niciuna dintre aceste măsuri nu elimină clasa de atac.** OWASP, NIST, Anthropic, OpenAI și Microsoft recomandă abordări stratificate deoarece niciun control individual nu este suficient.

*Proiectează presupunând că injecția de prompt va reuși pentru un anumit procent din intrări. Limitează în consecință efectele.*

## Agenți IA, limite de permisiuni și problema amplorii impactului

Din punct de vedere operațional, agenții diferă de chatboturi într-un mod esențial: **execută acțiuni.**

Un agent conectat la e-mail, GitHub, Jira, Slack, Salesforce, AWS și API-uri interne este un proces autonom cu acces la aceleași sisteme folosite de angajații cu cele mai multe conexiuni. **O injecție de prompt reușită împotriva agentului nu produce un răspuns textual nedorit. Produce o acțiune nedorită într-un sistem real.**

**Amploarea impactului unei compromiteri este determinată de ceea ce poate accesa agentul.** Majoritatea implementărilor actuale oferă agenților acces mult peste ce cere o sarcină individuală. Un agent care trebuie să citească un tichet Jira nu ar trebui să aibă și drept de scriere în ramura principală GitHub. Un agent care procesează solicitări de asistență nu ar trebui să păstreze acreditări pentru sistemul de facturare.

**Autorizarea IA este o problemă distinctă de autorizarea utilizatorului.** Aplicațiile tradiționale întreabă dacă utilizatorul are dreptul la o acțiune. Arhitecturile cu agenți trebuie să întrebe dacă acest agent are voie să execute această acțiune pentru acest utilizator, în acest moment și pe baza contextului actual. Majoritatea implementărilor actuale nu fac asta.

**Otrăvirea instrumentelor** este diferită de injecția de prompt. Un instrument malițios sau compromis conectat la un agent returnează descrieri sau date proiectate să-i modifice comportamentul. Cercetătorii tratează tot mai des otrăvirea instrumentelor ca pe o clasă separată de atac, mai ales în integrările bazate pe MCP.

*Fluxurile de aprobare umană ar trebui să fie ultima barieră pentru acțiunile importante ale agenților. Organizațiile descoperă și oboseala aprobărilor. Când agenții cer frecvent aprobare pentru acțiuni obișnuite, utilizatorii încep să aprobe automat fără să verifice solicitarea. Ultima barieră devine o formalitate.*

## Identitatea IA este o problemă de securitate a companiilor

**Agenții au acreditări.** Tokenuri OAuth, chei API, acreditări de conturi de serviciu și roluri cloud IAM apar în implementările agenților IA. Sunt identități non-umane cu acces real.

Lacune specifice implementărilor actuale:

- **Acreditările agenților au adesea durată mare** și nu sunt rotite după un program similar conturilor de serviciu
- **Domeniile tokenurilor agenților sunt frecvent mai largi** decât cer sarcinile efectuate
- Înregistrarea de audit a acțiunilor efectuate sub identități de agent variază mult
- **Scurgerea acreditărilor prin prompturi** este un risc documentat. Un agent care include cheile API în context sau în rezultate le expune oricui citește rezultatul ori recuperează conversația.
- Agenții care obțin acreditări suplimentare prin apeluri de instrumente creează **lanțuri de identități greu de auditat**

*Gestionează identitățile agenților la fel ca pe cele ale conturilor de serviciu privilegiate. Asta cere efort deliberat, fiindcă majoritatea instrumentelor de guvernanță a identității nu oferă suport nativ pentru identitatea agenților IA.*

## Memoria persistentă a agenților creează o suprafață de atac pe termen lung

**Agenții cu memorie persistentă au o suprafață de atac care nu există în sistemele fără stare.**

Un atacator care poate injecta conținut în memoria unui agent stabilește o poziție care persistă între sesiuni. *Atacul nu trebuie să reușească într-o singură interacțiune. Influența acumulată în memorie zile sau săptămâni modelează comportamentul viitor al agentului.* Uneori aceasta este numită **atac pe termen lung sau atac cu context latent**.

Există foarte puține îndrumări operaționale pentru acest risc specific. Organizațiile care implementează agenți cu stocare persistentă a memoriei trebuie să:

- Trateze **magazinele de memorie drept date de mare valoare** care necesită controale de acces
- **Valideze conținutul memoriei** înainte ca agenții să acționeze pe baza lui
- Includă în arhitectură capacitatea de a **audita și reveni asupra stării memoriei**

## Lanțul de aprovizionare al modelelor nu este tratat ca cel al programelor

**Organizațiile care descarcă modele preantrenate din depozite publice acceptă artefacte IA executabile din surse externe. Verificarea acestor descărcări nu este de obicei la nivelul aplicat de aceleași organizații pachetelor npm, PyPI sau Maven.**

Riscuri specifice din depozitele de modele:

- **Fișierele de modele PyTorch în format pickle** execută cod Python arbitrar la încărcare. Acest lucru a fost exploatat în atacuri documentate asupra lanțului de aprovizionare. **SafeTensors** este formatul proiectat special pentru această problemă. Alege-l când este disponibil.
- Încărcătoare malițioase care instalează dependențe sau execută cod de configurare împreună cu modelul
- Modele antrenate pe **seturi de date otrăvite** care produc rezultate subtil incorecte în anumite contexte
- Modele cu **uși din spate încorporate** care se activează în anumite condiții declanșatoare
- **Uzurparea numelui depozitului** pentru distribuirea de modele malițioase sub nume familiare

*Puține organizații mențin o listă a componentelor software pentru sistemele lor IA.* Majoritatea nu pot spune ce model de bază a fost folosit pentru un sistem de producție, ce versiune a datelor de antrenament a fost folosită la ajustare sau dacă ponderile implementate corespund celor evaluate ultima dată. Acest nivel de trasabilitate este o condiție prealabilă pentru o securitate reală a lanțului de aprovizionare. Nu este răspândit astăzi.

## IA din umbră creează fluxuri de date necontrolate

**Conturile personale de IA pentru consumatori sunt locul în care datele se deplasează fără controale.**

ChatGPT Enterprise, Claude Enterprise și Microsoft Copilot pentru M365 includ protecții contractuale pentru datele clienților. **Conturile personale ChatGPT, Claude, Gemini și alte servicii similare pentru consumatori nu oferă implicit aceste garanții.**

Angajații care folosesc conturi personale pentru documente de serviciu transferă strategii juridice, înregistrări ale clienților, cod sursă, proiecții financiare, decizii de personal și comunicări interne prin fluxuri pe care organizația nu le controlează. *Echipele de securitate nu au adesea informații exacte despre volumul activității sau categoriile de date implicate.*

Controalele DLP nu detectează datele care se deplasează prin browser către un serviciu IA pentru consumatori. Politicile de păstrare a datelor nu se aplică istoricului conversațiilor de pe o platformă terță. **Obligațiile de reglementare conform GDPR, HIPAA, SOX și regulilor sectoriale nu se schimbă în funcție de plecarea accidentală a datelor sau de transmiterea lor printr-o filă de browser.**

*Descoperirea amplorii reale înainte de construirea controalelor este primul pas necesar. Estimarea ta asupra problemei este aproape sigur prea mică.*

## Sistemele IA divulgă date în moduri diferite de aplicațiile tradiționale

**Recuperarea excesivă prin RAG** returnează documente utilizatorilor care nu ar trebui să le acceseze. Un angajat pune o întrebare. Componenta de recuperare returnează un document dintr-un segment restricționat al bazei de cunoștințe. Răspunsul include informații din acel document. *Defecțiunea controlului accesului s-a produs la nivelul recuperării, nu la nivelul aplicației.* Multe implementări RAG au fost construite fără aplicarea permisiunilor la nivel de document, în concordanță cu sistemul sursă.

**Scurgerea promptului de sistem** dezvăluie instrucțiunile operaționale încorporate în produsul IA. Prompturile de sistem trebuie tratate ca informații confidențiale. Scurgerea acreditărilor prin prompturi, când acreditările agentului ajung în contextul sau rezultatele modelului, este de obicei o expunere mai gravă decât conținutul promptului de sistem singur.

**Eșecurile de izolare IA multi-client** apar când modelele ajustate pe datele mai multor clienți afișează informațiile unui client în contextul altuia. Este o categorie de risc documentată pentru produsele IA SaaS multi-client.

**Memorarea de către model** îl determină să reproducă textual conținut din datele de antrenament. Riscul nu dispare, în special la modelele ajustate pe seturi private de date mici sau deduplicate insuficient. Organizațiile care ajustează modele folosind date interne sensibile trebuie să evalueze riscul de memorare pentru metoda și datele folosite.

## Organizațiile nu au vizibilitate în timpul inferenței

Programele tradiționale de securitate au acoperire extinsă de jurnalizare a infrastructurii. **Majoritatea implementărilor IA nu au o acoperire echivalentă a componentelor IA.**

Monitorizarea unui model lingvistic sau agent implementat necesită telemetrie diferită de cea pentru un server de aplicații. Organizațiile trebuie să colecteze:

- **Conținutul prompturilor și al rezultatelor** într-un format potrivit pentru revizuirea politicilor și detectarea anomaliilor
- **Jurnale ale apelurilor de instrumente** ale agenților, inclusiv numele instrumentelor, argumentele și răspunsurile
- **Jurnale de recuperare** pentru sistemele RAG, inclusiv interogări, documente returnate și decizii privind controlul accesului
- **Semnale de clasificare** a încercărilor de jailbreak și injecție
- **Monitorizarea consecvenței rezultatelor** pentru detectarea derivei comportamentale între versiuni ale modelului
- **Tipare de latență** care pot indica încercări de umplere a contextului

*Multe organizații care au implementat IA în 2023 și 2024 au coduri de stare HTTP și valori de latență. Telemetria necesară pentru detectarea sau investigarea unui incident de securitate IA lipsește adesea. E prea târziu să descoperi asta după incident.*

## Răspunsul la incidente IA necesită proceduri proprii

**Procedurile existente de răspuns la incidente acoperă puncte finale, rețele, aplicații și identitate. Nu acoperă scenarii specifice IA.**

Întrebări cu care se va confrunta echipa de răspuns la incidente și la care procedurile actuale nu răspund:

- Cum stabilești dacă un model a fost otrăvit în timpul unei sesiuni de ajustare
- Cum delimitezi amploarea unei injecții indirecte reușite împotriva unui agent cu drept de scriere în mai multe sisteme
- Cum evaluezi dacă datele de antrenament sau de ajustare au fost exfiltrate într-o compromitere a lanțului de aprovizionare
- Cum stabilești un **reper comportamental** al modelului pentru comparație cu comportamentul ulterior incidentului
- Cum răspunzi când o actualizare a modelului de la un furnizor terț introduce un comportament aparent intenționat, nu accidental
- Cum afli dacă **magazinul de memorie al unui agent a fost manipulat în timp**

*Aceste scenarii necesită pregătire înainte să apară. Telemetria trebuie să existe înainte de incident. Reperele comportamentale ale modelului trebuie documentate înainte să fie nevoie de comparație.*

## Fluxurile de evaluare devin o practică inginerească obișnuită

Securitatea IA se bazează tot mai mult pe **evaluarea structurată înainte de implementare**, nu doar pe monitorizarea ulterioară.

Evaluarea de securitate înainte de implementare include:

- **Testarea injecției de prompt** cu seturi consacrate de date de atac și cu scenariul specific de utilizare
- **Compararea rezistenței la jailbreak** cu suite publicate de prompturi adversariale
- **Evaluarea robusteții adversariale** pentru modele care iau decizii cu consecințe importante
- **Testarea regresiei** între versiunile modelului pentru a identifica schimbări de comportament
- **Evaluarea politicilor** față de cerințele documentate de utilizare acceptabilă
- **Exerciții red teaming** realizate de oameni care încearcă să înfrângă apărări specifice

NIST, CISA, Anthropic, OpenAI, Microsoft și Google se așteaptă tot mai mult la aceste evaluări pentru implementări cu risc ridicat. *Construirea unor fluxuri minime de evaluare înainte de implementări cu consecințe majore este mai accesibilă decât presupun multe organizații.* OWASP AI Exchange și cadrele de evaluare publicate de principalii furnizori IA sunt puncte bune de pornire.

## Inventarul activelor IA este probabil incomplet

Gestionarea tradițională a activelor acoperă servere, puncte finale, aplicații și dispozitive de rețea. **Sistemele IA introduc categorii de active pe care majoritatea inventarelor nu le urmăresc încă.**

Un inventar al sistemelor IA trebuie să includă:

- Fiecare **model implementat**, inclusiv modele de bază, variante ajustate și modele de încorporare
- Toate **prompturile și instrucțiunile de sistem** care rulează în producție
- Fiecare **agent** din mediu și instrumentele la care are acces
- Toți **indicii RAG**, inclusiv sursele de date și controalele de acces aplicate la recuperare
- Toate **bazele de date vectoriale** și conținutul lor
- Fiecare **server MCP sau cadru echivalent de integrare** conectat la orice agent
- **Serviciile IA externe** apelate de aplicații și datele trimise fiecăruia

*Nu poți guverna ceea ce nu ai inventariat. Majoritatea organizațiilor care lucrează la securitatea IA în 2026 descoperă active a căror existență nu o cunoșteau.*

## Care este starea reală a apărării

Instrumentele, cadrele și practicile de apărare pentru securitatea IA se dezvoltă activ și semnificativ. Domeniul este încă la început, dar se îmbunătățește.

**NIST AI 600-1** extinde AI RMF de bază pentru IA generativă cu mult mai multă specificitate operațională. Organizațiile care mențin programe de conformitate IA ar trebui să citească AI 600-1, nu doar cadrul de bază.

**MITRE ATLAS** oferă documentația TTP-urilor adversarilor pentru sistemele IA în format ATT&CK. Modelarea amenințărilor înainte de implementare cu ATLAS produce cerințe de securitate mai precise decât utilizarea exclusivă a cadrelor de guvernanță.

**OWASP LLM Top 10** și **OWASP Agentic AI Top 10** oferă în prezent cele mai specifice îndrumări operaționale publice. Ambele sunt mai utile practicienilor decât majoritatea programelor formale de studiu.

**Red teaming-ul IA** înainte de implementare este tot mai des așteptat de NIST, CISA și principalii furnizori IA pentru implementări cu risc ridicat. Piața externă de testare red team IA există și crește pentru organizațiile fără capacitate internă.

Produsele de securitate IA pentru monitorizare, bariere de protecție, autorizare și aplicarea politicilor la execuție sunt încă la început comercial. *Categoria există și merită evaluată. Pentru că piața este tânără, afirmațiile de marketing depășesc deseori capacitățile demonstrate. Evaluează produsele în raport cu arhitectura ta de implementare, nu cu scenariile descrise de furnizori.*

## Ce ar trebui să faci

**Inventariază ce ai implementat.** Află ce rulează, la ce date are acces, ce acreditări deține, ce instrumente apelează și ce acțiuni efectuează. Este condiția prealabilă pentru toate celelalte măsuri.

**Tratează agenții IA ca pe conturi privilegiate.** Aplică principiul privilegiului minim. Limitează acreditările la accesul minim necesar fiecărei sarcini. Auditează accesul fiecărui agent și elimină ce nu este necesar.

**Implementează observabilitatea specifică IA înainte de implementare**, nu după un incident. Jurnalizarea prompturilor și rezultatelor, a apelurilor de instrumente și a recuperărilor reprezintă telemetria minimă pentru analiza securității.

**Evaluează expunerea la IA din umbră.** Află ce servicii IA folosesc angajații pentru sarcini de serviciu. Determină ce categorii de date trec prin conturile personale. Construiește politici și controale pe baza constatărilor reale.

**Aplică controale de acces la nivel de document în sistemele RAG.** Dacă nivelul de recuperare nu impune regulile de acces ale sistemelor sursă, repară-l înainte ca un utilizator neautorizat să vadă un document restricționat.

**Auditează lanțul de aprovizionare al modelelor.** Documentează fiecare model de bază folosit. Preferă SafeTensors în locul formatelor pickle. Aplică artefactelor modelelor controale de aprovizionare comparabile cu cele pentru dependențele software.

**Guvernează identitățile agenților.** Gestionează tokenurile OAuth și cheile API ale agenților cu același ciclu de viață, revizuire a domeniilor și rotație ca în cazul conturilor de serviciu privilegiate.

**Construiește acum proceduri de răspuns la incidente specifice IA.** Definește înainte de un incident cum investighezi scenariile IA, ce dovezi îți trebuie și ce opțiuni de răspuns ai.

**Evaluează IA înainte de a o implementa în contexte cu consecințe majore.** Începe cu cadre publice disponibile dacă nu ai instrumente interne.

*Nu trata conformitatea guvernanței ca pe o postură de securitate. Cadrele de guvernanță descriu procesele și gestionarea riscurilor. Nu descriu sisteme de apărare tehnică. Sunt necesare ambele.*

## Referințe

- NIST AI Risk Management Framework (AI RMF 1.0): cadrul de gestionare a riscurilor IA, 2023
- NIST AI 600-1: profilul IA generativă, 2024
- OWASP: primele 10 riscuri pentru aplicațiile cu modele lingvistice mari, 2025
- OWASP: primele 10 riscuri ale IA agentice
- OWASP AI Exchange
- MITRE ATLAS: peisajul amenințărilor împotriva sistemelor IA
- Google Secure AI Framework (SAIF)
- Microsoft AI Security SDL
- CISA: îndrumări privind securitatea cibernetică a IA, 2024
- ISO/IEC 42001:2023 sisteme de management al inteligenței artificiale
- EU AI Act: Regulamentul (UE) 2024/1689
- Hugging Face: documentația formatului SafeTensors

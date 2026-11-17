---
title: "Construiește un laborator de acasă în 10 niveluri, de la Pi-hole la AI local"
date: 2026-10-27
lastmod: 2026-11-09
toc: true
draft: false
description: "Construiește un laborator de acasă în zece etape practice, de la filtrarea DNS pentru întreaga rețea la AI local, cu hardware, costuri, competențe și compromisuri pentru fiecare nivel."
genre: ["Laborator de acasă", "Self-hosting", "AI local", "Rețele de acasă"]
tags: ["laborator de acasă", "Pi-hole", "Home Assistant", "Docker", "Jellyfin", "Plex", "NAS", "Proxmox", "Tailscale", "Ollama", "AI local", "consum de energie"]
cover: "/img/cover/build-home-lab-10-levels.webp"
coverAlt: "Un laborator de acasă crește de la un Raspberry Pi și un router mici la stocare, servere, echipamente de rețea și o stație de lucru pentru AI local."
coverCaption: ""
---

Construiește un laborator de acasă în 10 niveluri, de la Pi-hole la AI local
============================================================================

Un **laborator de acasă** este un set de computere și servicii pe care le administrezi pentru a rezolva probleme de zi cu zi și a învăța să operezi sisteme reale. Poți bloca reclame, automatiza luminile, stoca mediile familiei sau testa mașini virtuale. **Începe cu o sarcină utilă.** Adaugă hardware când apare o limitare reală.

Acest ghid pornește de la un Raspberry Pi mic, cu Pi-hole, și ajunge la un server care rulează modele AI locale. **Fiecare nivel adaugă o funcție și o responsabilitate nouă.** Estimările de cost folosesc un consum ilustrativ și un tarif de exemplu de $0.15 pe kilowatt-oră. Verifică tariful local și măsoară echipamentele înainte să cumperi mai mult.

## Nivelul 1: Blochează reclamele în toată rețeaua de acasă

Instalează [Pi-hole](https://docs.pi-hole.net/) pe un Raspberry Pi sau pe alt computer Linux mic. Pi-hole funcționează ca un **DNS sinkhole**. Când un dispozitiv cere adresa unui domeniu dintr-o listă de blocare, Pi-hole nu returnează o destinație utilizabilă. Browserul, telefonul și televizorul inteligent folosesc același filtru atunci când routerul sau serverul DHCP direcționează clienții către Pi-hole.

**Filtrarea DNS** funcționează și în afara browserelor web, inclusiv pentru unele reclame din aplicații și televizoare conectate. Conținutul din pagini rămâne în afara filtrului, așa că trec reclamele livrate de pe același domeniu ca site-ul sau aplicația. Uneori, o listă de blocare împiedică încărcarea unei autentificări, a unui videoclip sau a unei plăți. Verifică jurnalul de interogări Pi-hole, permite domeniul respectiv când este nevoie și pregătește un DNS alternativ pentru întreruperi.

Consumul de energie este redus. Pentru un dispozitiv de 8 wați care funcționează toată luna, estimarea este 8 W × 24 de ore × 30 de zile ÷ 1.000 × $0.15 = **aproximativ $0.86 pe lună**. Măsoară alimentatorul complet la priză. Un al doilea computer, o unitate USB sau un adaptor ineficient schimbă totalul.

**Vei învăța:** DNS, DHCP, liste de blocare și întreținere Linux de bază.

## Nivelul 2: Automatizează local dispozitivele inteligente

Adaugă [Home Assistant](https://www.home-assistant.io/), care reunește dispozitive inteligente compatibile și automatizări într-un singur sistem. Programează stingerea luminilor la culcare. Pornește un ventilator când un senzor de temperatură depășește o valoare setată. Trimite-ți o notificare când un senzor de scurgere detectează apă. **Aceste automatizări mici oferă beneficii imediate.**

**Controlul local** păstrează multe automatizări funcționale în casă când un serviciu extern sau conexiunea la internet cade. Comportamentul depinde de dispozitiv. Unele produse cer în continuare un cont la furnizor, un serviciu cloud sau internet pentru configurare și funcții la distanță. Verifică cerințele integrării înainte să cumperi hardware.

**Fă backup pentru Home Assistant** și păstrează o copie în afara gazdei. Documentează integrările și pașii de recuperare. Un card SD sau un mini PC defect nu ar trebui să șteargă configurația.

**Vei învăța:** integrări de dispozitive, declanșatoare, condiții și recuperare din backup.

## Nivelul 3: Rulează mai multe servicii pe un singur mini PC

Un **mini PC business second-hand** oferă deseori memorie extensibilă, stocare înlocuibilă și porturi utile la un preț redus. Un mini PC Intel N100 consumă deseori mai puțină energie și ocupă puțin spațiu. Intel descrie N100 ca un procesor cu patru nuclee și patru fire de execuție, TDP de 6 wați și suport pentru până la 16 GB de memorie. Clasificarea procesorului nu este echivalentă cu consumul întregului sistem la priză. Compară modelul exact, memoria, stocarea, garanția și porturile de rețea.

Instalează Linux și folosește [Docker](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) pentru a rula servicii separate ca **containere**. Un container împachetează o aplicație și dependențele ei, dar partajează nucleul sistemului de operare gazdă. De exemplu, rulează un manager de parole precum proiectul Vaultwarden întreținut de comunitate și un monitor de disponibilitate precum Uptime Kuma. **Tratează managerul de parole ca pe un serviciu sensibil:** limitează accesul, folosește autentificare puternică, aplică actualizări și păstrează un backup criptat.

**Containerele nu înlocuiesc actualizările sau backupurile.** Alege o locație de stocare pentru fiecare serviciu și notează pașii de recuperare. Și un mini PC mic are limite. Mai multe baze de date, conversii media sau aplicații mari pot epuiza memoria, stocarea sau timpul CPU.

**Vei învăța:** administrare Linux, containere, volume, actualizări și recuperarea serviciilor.

## Nivelul 4: Construiește o bibliotecă media de acasă

[Jellyfin](https://jellyfin.org/docs/) este un server media open-source. [Plex](https://support.plex.tv/) oferă un ecosistem de clienți finisat și funcții opționale bazate pe cont. Ambele organizează biblioteci personale și transmit media către clienți compatibili. **Alege în funcție de clienți**, metoda de acces la distanță, suportul hardware și funcțiile necesare.

**Nevoile de stocare** depind de dimensiunea și calitatea colecției. Începe cu un singur disc numai dacă ai deja un plan de backup separat. Folosește nume consecvente pentru foldere și metadate, astfel încât serverul să asocieze corect filmele și episoadele.

**Redarea directă** trimite un fișier compatibil către client fără să schimbe fluxul video. **Transcodarea** convertește audio sau video când clientul, conexiunea, subtitrările ori setarea de calitate cer alt format. Transcodarea solicită mai mult serverul. Testează dispozitivele și rețeaua înainte să cumperi un GPU sau un CPU mai mare. **Renunță la un server media dedicat** dacă fiecare client redă fișierele direct și o singură gazdă îți satisface nevoile.

**Vei învăța:** formate media, planificarea stocării, debitul rețelei și testarea sarcinilor.

## Nivelul 5: Adaugă redundanță de stocare și un backup separat

Un NAS cu două discuri și **stocare în oglindă** scrie datele pe ambele discuri. Dacă unul se defectează, celălalt păstrează o copie actuală în timp ce îl înlocuiești pe cel defect și reconstruiești oglinda. Oglindirea protejează disponibilitatea la defectarea unui singur disc. **O oglindă nu restaurează** un fișier șters, nu inversează criptarea ransomware și nu protejează împotriva furtului, incendiului sau unui incident electric care deteriorează ambele discuri.

Păstrează un **backup separat** pe alt dispozitiv sau într-o altă locație. Include documente importante, fotografii, exporturi de configurare și datele serviciilor. Stabilește un program de backup și păstrează versiuni, astfel încât modificările accidentale să nu suprascrie toate copiile bune.

**Testează o restaurare.** Alege câteva fișiere, restaurează-le într-un dosar separat și deschide-le. Pentru un serviciu, restaurează datele într-o instanță de test sau documentează pașii și verifică fiecare fișier. Un backup pe care nu l-ai restaurat niciodată este o presupunere, nu un plan de recuperare.

**Vei învăța:** sisteme de fișiere, înlocuirea discurilor, rotația backupurilor și testarea restaurării.

## Nivelul 6: Învață virtualizarea cu un cluster Proxmox mic

[Proxmox VE](https://pve.proxmox.com/pve-docs/) rulează mașini virtuale și containere pe hardware de server. Mai multe mini PC-uri unite într-un **cluster** împart o vizualizare de administrare și te ajută să înveți despre noduri, stocare și migrare. Un cluster este un grup de servere configurate să se coordoneze. Membrii nu își combină memoria într-un singur pool mare. **Disponibilitatea ridicată cere** planificare suplimentară și stocare partajată sau replicată adecvată.

Un **snapshot** înregistrează starea unei mașini virtuale la un moment dat, astfel încât să poți reveni la o stare anterioară după o modificare în laborator. Snapshoturile depind de obicei de stocarea originală. Nu sunt backupuri independente. **Copiază datele importante pe o destinație de backup separată** și testează restaurarea.

Fiecare nod adaugă consum de energie, porturi de rețea, cabluri și actualizări. Trei computere mici înseamnă și trei sisteme de corectat și depanat. Un singur mini PC cu câteva mașini virtuale te învață multe dintre aceleași noțiuni de bază la cost mai mic. **Adaugă noduri când** experimentele au nevoie de izolare sau vrei să exersezi operațiuni de cluster.

**Vei învăța:** mașini virtuale, pooluri de stocare, snapshoturi, apartenența la cluster și întreținerea nodurilor.

## Nivelul 7: Adaugă acces la distanță privat și separarea rețelei

[Tailscale](https://tailscale.com/kb/) conectează dispozitivele aprobate printr-o rețea privată, oferind acces la unele servicii de acasă când ești plecat. **Limitează accesul** la dispozitivele și serviciile de care are nevoie fiecare persoană. Protejează conturile prin autentificare multifactor și verifică dispozitivele și cheile vechi.

Un switch administrabil sau un router cu suport pentru **VLAN** separă grupuri de dispozitive. Pune prizele inteligente și alte dispozitive cu încredere redusă într-o rețea diferită de cea a computerelor cu fișiere personale. Plasează stocarea într-o rețea accesibilă doar sistemelor care au nevoie de ea. Segmentarea limitează dispozitivele care comunică între ele. Menține și actualizări, parole puternice și reguli de acces.

**Evită expunerea directă a panourilor de administrare pe internetul public** dacă nu înțelegi cerințele serviciului privind autentificarea, patchurile și firewallul. Și un instrument de acces privat cere control atent asupra conturilor și dispozitivelor.

**Vei învăța:** acces privat, permisiuni bazate pe identitate, VLAN-uri, reguli firewall și limite de încredere între dispozitive.

## Nivelul 8: Adaugă un server enterprise

Treci la un server mai mare când măsurătorile arată că ai nevoie de mai multe nuclee CPU, memorie, locașuri pentru discuri, sloturi PCIe sau capacitate de rețea. Serverele enterprise mai vechi costă deseori mai puțin second-hand, dar ventilatoarele lor sunt zgomotoase, iar **consumul în repaus ajunge la aproximativ 100–160 de wați**, în funcție de model și componentele instalate. Tratează acest interval ca pe o estimare, nu ca pe o specificație.

Calculează costul anual estimat al electricității înainte să cumperi:

`wați măsurați ÷ 1.000 × 24 × 365 × tariful electric pe kWh`

La 120 de wați și $0.15 per kWh, estimarea este de 1.051 kWh anual, adică aproximativ **$158 pe an**. Măsoară serverul exact în repaus și la sarcina obișnuită. Include consumul discurilor, răcirii și UPS-ului.

Verifică adâncimea șasiului, compatibilitatea discurilor, zgomotul, controlul ventilatoarelor, sursa de alimentare și plăcile de extensie. Un server care depășește bugetul de spațiu sau energie nu este un upgrade practic.

**Vei învăța:** hardware de server, administrare la distanță, extindere, răcire și estimarea costurilor de operare.

## Nivelul 9: Măsoară energia și dimensionează laboratorul

Folosește un **contor de energie la priză** pentru a măsura fiecare computer în repaus și în timpul activității obișnuite. Notează cei mai mari consumatori. Verifică setările de alimentare din BIOS, elimină plăcile și discurile nefolosite și mută serviciile zilnice înapoi pe mini PC-uri eficiente când hardware-ul enterprise nu este necesar.

Pornește serverul mare numai când o sarcină are nevoie de capacitatea lui. Dacă folosești un program Wake-on-LAN sau control de alimentare la distanță, documentează pașii de recuperare în caz de căderi ale rețelei sau curentului. Ține o **listă a dependențelor dintre servicii** pentru ca opririle să nu întrerupă stocarea sau rețeaua necesare altor sisteme.

Un rack ajută la organizarea echipamentelor și a fluxului de aer când hardware-ul montabil în rack justifică spațiul. Un UPS trece peste întreruperile scurte și oferă sistemelor timp pentru o oprire corectă. Ambele adaugă cost de achiziție, ocupă spațiu și consumă curent. **Măsoară-le consumul** și include schimbarea bateriilor în bugetul pe termen lung.

**Vei învăța:** măsurarea energiei, gestionarea alimentării, cartografierea dependențelor și planificarea capacității.

## Nivelul 10: Rulează modele AI local

[Ollama](https://docs.ollama.com/) descarcă și rulează modele lingvistice compatibile pe computerul tău. **Inferența locală** păstrează prompturile și rezultatele pe hardware-ul controlat de tine când folosești un model și o aplicație locale. Confirmă că întregul traseu software rămâne local. O aplicație conectată, o funcție de telemetrie sau o opțiune de model cloud trimite date în afara rețelei.

Cerințele hardware depind de dimensiunea modelului, cuantizare, lungimea contextului și viteza dorită. **Memoria sistemului sau a GPU-ului trebuie să încapă** ponderile modelului și contextul de lucru. Computerele mici rulează modele mici, iar modelele mai mari și contextele mai lungi cer mai multă memorie și adesea un GPU capabil. Măsoară consumul în timpul inferenței. Un sistem cu GPU consumă deseori mult mai mult curent decât un mini PC în repaus.

Modelele locale se potrivesc pentru schițe, rezumarea notițelor private și clasificare simplă când calitatea lor îți satisface nevoile. Ele oferă răspunsuri greșite, iar modelele mici se descurcă adesea slab cu raționamentul complex sau informațiile actuale. Modelele cloud pot performa mai bine pentru anumite sarcini. **Compară calitatea, confidențialitatea, latența, costul și energia** înainte să alegi unde rulează sarcina.

**Vei învăța:** memoria modelelor, cuantizarea, inferența, limitele de confidențialitate și evaluarea sarcinilor.

## Compară cele zece niveluri

**Costurile sunt estimări, nu oferte.** Prețurile hardware variază în funcție de regiune, stare și configurația stocării. Estimează electricitatea cu `wați ÷ 1.000 × ore × zile × tarif per kWh`. Măsoară la priză când poți și include orele de repaus, deoarece multe servere de acasă funcționează permanent.

### Capacitate și hardware

| Nivel | Capacitate nouă | Hardware obișnuit |
|---|---|---|
| **1** | Filtrare DNS de rețea | Raspberry Pi sau gazdă Linux mică |
| **2** | Automatizarea locală a dispozitivelor | Pi sau mini PC, dispozitive compatibile |
| **3** | Mai multe aplicații self-hosted | Mini PC business second-hand sau sistem N100 |
| **4** | Streaming de media personală | Mini PC și stocare media |
| **5** | Toleranță la defectarea discului și recuperare | NAS cu două discuri și backup separat |
| **6** | Laborator de servere virtuale | Două mini PC-uri sau mai multe |
| **7** | Acces privat și segmentare | Tailscale, router sau switch administrabil |
| **8** | Capacitate și extindere ridicate | Server enterprise |
| **9** | Consum energetic redus pentru laborator | Contor de energie, sisteme optimizate |
| **10** | Inferență locală a modelelor | PC cu multă memorie, GPU opțional |

### Competențe, costuri și compromisuri

| Nivel | Competențe învățate | Estimarea costului recurent | Compromisul principal |
|---|---|---|---|
| **1** | DNS, DHCP, Linux | Aproximativ $1/lună la 8 W și $0.15/kWh | Unele reclame rămân, blocările false cer verificare |
| **2** | Integrări, declanșatoare, backupuri | Curentul gazdei și costul dispozitivelor | Compatibilitate și efortul pentru backupuri |
| **3** | Docker, actualizări, stocare | Depinde de consumul măsurat al sistemului | Limite CPU, memorie și disc |
| **4** | Formate, organizare, transcodare | Stocare și energie pentru server | Transcodarea cere uneori hardware suplimentar |
| **5** | Oglindire, retenție, restaurare | Curent NAS, discuri, destinație backup | O oglindă nu este un backup |
| **6** | Proxmox, VM-uri, clustere | Fiecare nod adaugă consum și întreținere | Mai multe noduri înseamnă mai multă mentenanță |
| **7** | Reguli de acces, VLAN, firewall | Echipamente de rețea și costuri de serviciu | Regulile greșite expun servicii |
| **8** | Hardware, răcire, administrare la distanță | Variază după server, calculează din măsurători | Zgomot, căldură și consum în repaus |
| **9** | Măsurare, programare, dimensionare | Cost unic pentru contor, economii variabile | Programarea adaugă pași operaționali |
| **10** | Implementarea și evaluarea modelelor | Energie de calcul și stocare | Calitatea și viteza depind de hardware |

## Alege următorul upgrade util

**Oprește-te la nivelul care îți satisface nevoile actuale.** Pi-hole și un mini PC pot acoperi serviciile tale. Un NAS este util când ai nevoie de stocare partajată și un plan de recuperare testat. Adaugă un cluster sau un server enterprise când o sarcină sau un obiectiv de învățare îl justifică.

Notează **unde sunt datele fiecărui serviciu, procesul de actualizare și pașii de restaurare.** Testează backupurile înainte să adaugi echipamente. Lasă următoarea limitare reală să îți ghideze următoarea achiziție.

## Referințe

- [Documentația Pi-hole](https://docs.pi-hole.net/)
- [Documentația Home Assistant](https://www.home-assistant.io/docs/)
- [Specificațiile procesorului Intel N100](https://www.intel.com/content/www/us/en/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/specifications.html)
- [Docker: Ce este un container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Documentația Jellyfin](https://jellyfin.org/docs/)
- [Asistență Plex](https://support.plex.tv/)
- [Documentația Proxmox VE](https://pve.proxmox.com/pve-docs/)
- [Documentația Tailscale](https://tailscale.com/kb/)
- [Documentația Ollama](https://docs.ollama.com/)

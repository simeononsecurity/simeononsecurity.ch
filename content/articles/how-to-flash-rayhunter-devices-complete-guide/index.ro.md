---
title: "Cum instalezi Rayhunter pe dispozitive: ghid complet"
draft: false
toc: true
date: 2026-03-09
lastmod: 2026-11-15
description: "Instalează și configurează Rayhunter pentru detectarea captatoarelor IMSI. Verifică dispozitivele compatibile, instalează firmware-ul, testează funcționarea și rezolvă problemele frecvente."
tags: ["Rayhunter", "captator IMSI", "simulator de stație celulară", "securitate mobilă", "detectarea supravegherii", "protecția confidențialității", "Orbic RC400L", "TP-Link M7350", "hotspot mobil", "instalarea dispozitivelor", "securitate cibernetică", "securitate wireless", "contramăsuri de supraveghere", "EFF", "instrumente de confidențialitate", "cumpără Rayhunter", "ghid de instalare", "configurare", "dispozitive compatibile", "securitatea rețelei"]
cover: "/img/cover/rayhunter.webp"
coverAlt: "Un dispozitiv Rayhunter detectează semnale wireless și captatoare IMSI, înconjurat de scuturi de securitate"
coverCaption: "Sistemul Rayhunter de detectare a captatoarelor IMSI protejează comunicațiile mobile împotriva supravegherii"
---

**Ghid complet pentru instalarea și configurarea Rayhunter, sistemul de detectare a captatoarelor IMSI.**

## Pe scurt

**Rayhunter** este un sistem open-source de detectare a captatoarelor IMSI, care rulează pe hotspoturi mobile modificate. Te avertizează când echipamentele de supraveghere încearcă să intercepteze comunicațiile celulare. Acest ghid explică instalarea completă pe dispozitivele Orbic RC400L și TP-Link M7350, opțiunile de configurare, analiza actorilor de amenințare și eficiența în rețelele 5G. Ai nevoie de un dispozitiv compatibil cu Qualcomm. Sistemul detectează supravegherea în rețele 2G, 3G și 4G prin mai multe euristici. Rămâne util și pe măsură ce se extinde 5G, deoarece atacurile de retrogradare continuă. Oferă protecție importantă jurnaliștilor, activiștilor și persoanelor preocupate de confidențialitate împotriva supravegherii guvernamentale, infracționale și corporative.

**Rayhunter** este un instrument open-source creat pentru detectarea captatoarelor IMSI (simulatoare de stații celulare) care pot intercepta comunicațiile mobile. Dacă vrei să **cumperi Rayhunter** sau să afli cum să instalezi și să configurezi corect aceste dispozitive, ghidul de față acoperă instalarea, configurarea și utilizarea sistemelor **Rayhunter**.

**Dezvăluire privind sponsorizarea:** Acest articol este sponsorizat de [STS Collective](https://stscollective.com), principalul furnizor de dispozitive compatibile cu Rayhunter. În ciuda sponsorizării, toate informațiile tehnice, analizele și recomandările din ghid rămân imparțiale și se bazează exclusiv pe documentația oficială Rayhunter, feedbackul comunității și evaluări tehnice obiective.

> 💰 **Reducere exclusivă pentru cititori:** Economisește până la 20% la dispozitivele Rayhunter și la toate produsele STS Collective. Folosește codul **SIMEONONSECURITY** la plată sau [cumpără direct cu reducerea aplicată](https://stscollective.com/discount/SIMEONONSECURITY).

## Introducere în Rayhunter

**Rayhunter** este un sistem avansat de detectare a captatoarelor IMSI, dezvoltat de **Electronic Frontier Foundation (EFF)**, o organizație importantă fără scop lucrativ care apără libertățile civile în lumea digitală. Din 1990, EFF susține confidențialitatea digitală, libertatea de exprimare și inovarea prin litigii cu impact, analiză de politici publice, activism comunitar și dezvoltare tehnologică.

Instrumentul rulează pe hotspoturi mobile compatibile și monitorizează permanent rețelele celulare pentru activități suspecte care ar putea indica prezența simulatoarelor de stații celulare sau a dispozitivelor „Stingray” folosite pentru supraveghere. **Rayhunter** reflectă angajamentul EFF de a oferi instrumente practice de protecție a confidențialității persoanelor și organizațiilor care au nevoie să se apere de supraveghere.

**Rayhunter** emite alerte în timp real când detectează comportamente celulare potențial malițioase. Este un instrument important de protecție a confidențialității pentru jurnaliști, activiști, specialiști în securitate și persoane preocupate de confidențialitate. Poți găsi dispozitive compatibile **[Rayhunter de vânzare](https://stscollective.com/collections/rayhunter)** la STS Collective, principalul furnizor al acestor dispozitive specializate.

### Susținerea proiectului Rayhunter

**Rayhunter** este un proiect open-source care beneficiază de sprijinul comunității. Poți contribui la dezvoltarea sa continuă în mai multe moduri:

- **Cumpără de la STS Collective:** STS Collective donează EFF o parte din profitul obținut la fiecare vânzare a unui dispozitiv Rayhunter, pentru a susține dezvoltarea continuă a **Rayhunter** și cercetarea în domeniul confidențialității.
- **Donează direct:** Susține direct activitatea EFF pentru protejarea confidențialității și dezvoltarea **Rayhunter** printr-o **[donație către EFF](https://supporters.eff.org/donate/donate)**.
- **Implică-te în comunitate:** Contribuie la discuții, documentație și testare în depozitul oficial GitHub.

Sprijinul tău ajută la menținerea **Rayhunter** ca proiect gratuit, open-source și îmbunătățit continuu pentru a răspunde amenințărilor de supraveghere în schimbare.

## Suport, feedback și comunitate

**Rayhunter** este susținut de o comunitate activă de cercetători în securitate, susținători ai confidențialității și cetățeni preocupați. Poți primi ajutor și contribui la proiect prin mai multe canale:

- **Documentație oficială:** [Documentația Rayhunter](https://efforg.github.io/rayhunter/introduction.html), cu ghiduri complete de instalare, configurare și utilizare.
- **Depozit GitHub:** [EFForg/rayhunter](https://github.com/EFForg/rayhunter)
- **Discuții în comunitate:** Deschide discuții pe GitHub despre compatibilitatea dispozitivelor și depanare.
- **Cercetare de securitate:** Colaborează cu cercetători pentru a îmbunătăți capabilitățile de detectare ale **Rayhunter**.

Dacă ai nevoie de dispozitive compatibile, STS Collective oferă opțiuni **[Rayhunter de vânzare](https://stscollective.com/collections/rayhunter)**.

## Întrebări frecvente

### Am nevoie de o cartelă SIM activă pentru Rayhunter?

**Rayhunter** necesită o cartelă SIM introdusă în dispozitiv, dar aceasta nu trebuie să aibă un abonament activ. SIM-ul permite conectarea dispozitivului la rețele celulare și monitorizarea activităților suspecte. Dacă vrei să folosești dispozitivul și ca hotspot în timp ce rulează **Rayhunter**, ai nevoie de un abonament activ.

### Cum verific dacă dispozitivul meu Rayhunter funcționează?

Activează euristica de test din setările de configurare **Rayhunter**. Aceasta va genera alerte de fiecare dată când dispozitivul detectează un turn celular, astfel încât să poți confirma funcționarea sistemului. Modul de test generează multe alerte, deci dezactivează-l după verificare.

### Ar trebui să cumpăr un dispozitiv blocat sau deblocat?

Pentru compatibilitatea cu **Rayhunter**, dispozitivele deblocate sunt de obicei preferabile, mai ales dacă vrei să folosești cartele SIM care nu sunt Verizon. Multe dispozitive Orbic marca Verizon sunt de fapt deblocate, dar verifică compatibilitatea înainte de cumpărare. Poți găsi dispozitive compatibile verificate **[Rayhunter de vânzare](https://stscollective.com/collections/rayhunter)** la STS Collective.

{{< stscollective-ad "rayhunter" >}}

## Ghid de instalare

### Instalarea celei mai recente versiuni

Instalarea **Rayhunter** a fost testată pe macOS și Ubuntu 24.04. Dacă întâmpini probleme cu versiunile precompilate, poate fi necesară instalarea din codul sursă.

#### Cerințe preliminare

Înainte să instalezi **Rayhunter**, verifică dacă dispozitivul este compatibil. Pentru dispozitivele TP-Link, introdu un card SD formatat FAT pentru stocarea înregistrărilor.

#### Descărcare și configurare

1. **Descarcă cea mai recentă versiune:** Obține fișierul `rayhunter-vX.X.X-PLATFORM.zip` potrivit de pe pagina oficială a versiunilor:
   - Linux x64: `linux-x64`
   - Linux ARM64: `linux-aarch64`
   - Linux ARM v7/v8: `linux-armv7`
   - macOS Intel: `macos-intel`
   - macOS ARM (M1/M2): `macos-arm`
   - Windows: `windows-x86_64`

2. **Dezarhivează și intră în director:**
   ```bash
   unzip ~/Downloads/rayhunter-vX.X.X-PLATFORM.zip
   cd ~/Downloads/rayhunter-vX.X.X-PLATFORM
   ```

3. **Conectează dispozitivul:** Pornește-l și conectează-te prin WiFi sau tethering USB. Ar trebui să poți accesa:
   - Dispozitive Orbic: `http://192.168.1.1`
   - Dispozitive TP-Link: `http://192.168.0.1`

#### Instalare specifică dispozitivului

**Pentru dispozitive Orbic RC400L** (disponibile **[Rayhunter de vânzare](https://stscollective.com)**):

**Rayhunter** oferă două metode de instalare pentru dispozitivele Orbic RC400L. Metoda WiFi este recomandată majorității utilizatorilor, iar metoda USB oferă opțiuni suplimentare de depanare.

**Instalare prin WiFi (recomandată):**
```bash
# Utilizatorii macOS trebuie să ruleze mai întâi:
xattr -d com.apple.quarantine installer

# Verizon RC400L (parola de administrator este aceeași cu parola WiFi):
./installer orbic --admin-password 'YourWiFiPassword'

# Kajeet/Smartspot RC400L:
./installer orbic --admin-password='$m@rt$p0tc0nf!g'

# Dispozitive Moxee (formatul parolei: 12$ + ultimele 3 cifre ale parolei WiFi):
./installer orbic --admin-password='12$XXX'
```

**Instalare prin USB (utilizatori avansați):**
```bash
# AVERTISMENT: instalatorul USB nu este recomandat pentru majoritatea utilizărilor
./installer orbic-usb
```

Această metodă forțează dispozitivul să intre în modul de depanare pentru a activa accesul ADB, instalează rootshell și **Rayhunter**, apoi repornește dispozitivul. Folosește metoda numai dacă ai nevoie de ADB și în alte scopuri.

**Pentru dispozitive TP-Link M7350** (disponibile **[Rayhunter de vânzare](https://stscollective.com)**):
```bash
./installer tplink
```

Instalatorul finalizează instalarea **Rayhunter** și repornește dispozitivul. O linie verde pe ecran indică faptul că **Rayhunter** rulează cu succes.

### Instalarea din codul sursă

Pentru dezvoltatori sau utilizatori care trebuie să compileze **Rayhunter** din codul sursă, proiectul include:

- **Frontend:** aplicație JavaScript SvelteKit (`./daemon/web/`)
- **Backend:** binarul Rust `rayhunter-daemon` (`./daemon/`)
- **Instalator:** binar Rust care reunește toate componentele (`./installer`)

#### Dependențe de compilare

Instalează:
- Limbajul de programare Rust
- Node.js/npm
- Instrumente de compilare C (`build-essential` pe Linux, `xcode-select --install` pe macOS)

#### Procesul de compilare

```bash
./scripts/build-dev.sh
./scripts/install-dev.sh orbic  # Înlocuiește 'orbic' cu tipul dispozitivului
```

Pentru dezvoltare frontend cu reîncărcare rapidă:
```bash
cd daemon/web
npm run dev
# Sau cu o țintă personalizată:
API_TARGET=http://192.168.1.1:8080 npm run dev
```

### Actualizarea Rayhunter

Actualizarea **Rayhunter** urmează aceiași pași ca instalarea. Repetă pașii de instalare folosind cea mai nouă versiune, pentru a actualiza dispozitivul la cea mai nouă versiune **Rayhunter**.

## Configurare

Poți configura **Rayhunter** din interfața web sau poți edita direct pe dispozitiv fișierul `/data/rayhunter/config.toml`.

### Configurare din interfața web

Conectează-te la rețeaua dispozitivului și accesează interfața web **Rayhunter**:
- Orbic: `http://192.168.1.1:8080`
- TP-Link: `http://192.168.0.1:8080`

{{< figure src="rayhunter-dashboard.webp" alt="Panoul interfeței web Rayhunter" caption="Interfața web Rayhunter oferă opțiuni complete de monitorizare și configurare" >}}

#### Opțiuni principale de configurare

**Nivelul interfeței dispozitivului:** Controlează ce afișează **Rayhunter** pe ecran:
- **Mod invizibil:** Nu afișează nimic.
- **Mod discret:** Afișează un indicator colorat (verde=sigur, roșu=alertă, alb=în pauză).
- **Mod demonstrație:** Afișează elemente grafice cu o orcă și o linie de stare.
- **Sigla EFF:** Afișează sigla EFF și linia de stare.
- **Vizibilitate ridicată:** Afișează culori pe tot ecranul.

**Modul de intrare al dispozitivului:** Configurează comportamentul butonului de pornire:
- **Dezactivează controlul butonului:** Dezactivează butonul de pornire pentru **Rayhunter**.
- **Atingere dublă pentru repornirea înregistrării:** Resetează alertele și repornește monitorizarea.

**Setări de notificare:** Configurează URL-ul ntfy pentru alerte la distanță și activează/dezactivează notificările de avertizare și baterie descărcată.

**Euristici de analiză:** Activează sau dezactivează algoritmi specifici de detectare **Rayhunter** în funcție de mediu și modelul de amenințare.

## Dezinstalarea Rayhunter

### Dispozitive Orbic

Pentru a elimina **Rayhunter** de pe dispozitive Orbic:

```bash
./installer util orbic-shell --admin-password mypassword
```

În shell:

> **Avertisment:** Următoarele comenzi șterg definitiv fișierele Rayhunter și componentele sale de pornire. Confirmă că te afli în shell-ul dispozitivului corect, copiază înregistrările sau configurațiile pe care vrei să le păstrezi și pregătește instalatorul și firmware-ul compatibil înainte de a continua. După operație, verifică eliminarea fișierelor și repornirea dispozitivului fără serviciul Rayhunter. Pentru revenire, reinstalează versiunea potrivită din depozitul oficial.

```bash
echo 3 > /usrdata/mode.cfg
rm -rf /data/rayhunter /etc/init.d/rayhunter_daemon /bin/rootshell
reboot
```

### Dispozitive TP-Link

Pentru dezinstalarea Rayhunter de pe un dispozitiv TP-Link:

> **Avertisment:** Aceste comenzi elimină fișierele Rayhunter și componenta de pornire de pe dispozitivul TP-Link. Exportă mai întâi înregistrările și configurația. Rulează comenzile numai în shell-ul dispozitivului, apoi verifică dispariția căilor și pornirea normală a aparatului. Pentru revenire, reinstalează versiunea potrivită din depozitul oficial.

```bash
./installer util tplink-shell
rm /data/rayhunter /etc/init.d/rayhunter_daemon
update-rc.d rayhunter_daemon remove
```

Elimină orice regulă rămasă pentru declanșarea porturilor din interfața de administrare TP-Link, la Settings > NAT Settings > Port Triggers.

## Utilizarea Rayhunter

După instalare, **Rayhunter** pornește automat și monitorizează continuu rețelele celulare pentru activități suspecte. Ecranul dispozitivului afișează o linie verde în funcționarea normală. La detectarea unor captatoare IMSI potențiale, linia se schimbă în puncte galbene, liniuțe portocalii sau o linie roșie continuă.

### Euristicile de detectare Rayhunter

**Rayhunter** folosește mai mulți algoritmi sofisticați pentru identificarea activităților potențiale ale captatoarelor IMSI:

#### Detectarea solicitărilor IMSI

Această euristică identifică secvențe suspecte în care turnurile celulare solicită identitatea dispozitivului (IMSI, Identitatea Internațională a Abonatului Mobil) fără să urmeze procedurile corecte de autentificare. **Rayhunter** monitorizează momentul și contextul acestor cereri și semnalează tipare anormale care pot indica echipamente de supraveghere.

Rețelele celulare legitime urmează proceduri standardizate de autentificare înainte de a solicita identificatori sensibili. Captatoarele IMSI ocolesc adesea aceste proceduri pentru a colecta rapid identitățile dispozitivelor, provocând anomalii detectabile în secvența de autentificare. Metoda este deosebit de eficientă împotriva captatoarelor IMSI „pasive” de bază, care doar colectează informații despre dispozitive.

#### Detectarea eliberării conexiunii/retrogradării la 2G

**Rayhunter** monitorizează continuu tentativele suspecte de a deconecta dispozitive mobile de la rețele 4G/5G sigure și de a le reconecta la rețele 2G mai puțin sigure. Acest atac de retrogradare este o tactică obișnuită a captatoarelor IMSI, deoarece rețelele 2G au criptare mai slabă și sunt mai ușor de interceptat.

Sistemul analizează tiparele de eliberare a conexiunii și caută frecvențe, momente sau indicii contextuale anormale, care sugerează intenții malițioase și nu optimizare normală a rețelei. Rețelele legitime pot sugera ocazional retrogradări din motive de acoperire sau capacitate, dar **Rayhunter** poate distinge comportamentul normal de posibile activități de supraveghere.

#### Detectarea retrogradării LTE SIB6/7

Blocurile de informații de sistem (SIB) sunt mesaje transmise de rețelele celulare pentru a furniza dispozitivelor mobile date de configurare. **Rayhunter** monitorizează în special mesajele SIB6 și SIB7, care conțin informații despre celulele învecinate și redirecționarea frecvențelor.

Actorii malițioși pot transmite mesaje SIB6/7 false pentru a determina dispozitivele să renunțe la conexiuni 4G sigure și să se conecteze la rețele 2G controlate de atacator. **Rayhunter** analizează aceste transmisii pentru a identifica inconsecvențe, tipare anormale de redirecționare și alte indicii privind stații de bază necinstite care încearcă să retrogradeze conexiunile pentru interceptare.

#### Detectarea cifrului nul

Această metodă esențială detectează situațiile în care rețelele celulare propun lipsa criptării comunicațiilor (cifru nul). Rețelele celulare comerciale legitime nu ar trebui să propună conexiuni necriptate, deoarece ar încălca standardele de securitate și cerințele de reglementare.

**Rayhunter** semnalează ca extrem de suspectă orice rețea care propune folosirea cifrului nul. *O rețea legitimă nu va propune niciodată cifru nul.* Acesta este un indicator clar că un echipament de supraveghere încearcă să intercepteze comunicațiile în text simplu. Euristica este deosebit de eficientă împotriva captatoarelor IMSI care prioritizează colectarea datelor și nu încearcă să pară operațiuni legitime.

#### Detectarea SIB incomplete

Stațiile de bază celulare legitime transmit blocuri complete de informații de sistem, care conțin date esențiale de configurare a rețelei. **Rayhunter** monitorizează stațiile de bază care furnizează informații incomplete sau lipsă, fapt ce indică adesea echipamente de supraveghere instalate în grabă sau configurate incorect.

Captatoarele IMSI nu implementează frecvent toate funcțiile rețelei celulare, concentrându-se doar pe funcțiile minime necesare conectării dispozitivelor și interceptării datelor. Prin detectarea acestor implementări incomplete, **Rayhunter** poate identifica stații de bază potențial malițioase, cărora le lipsesc caracteristicile așteptate de la infrastructura celulară legitimă.

{{< figure src="rayhunter-heuristics-overview.webp" alt="Diagramă cu cele cinci euristici Rayhunter: solicitare IMSI fără autentificare, atac de retrogradare la 2G, redirecționare LTE SIB6/7, propunere de cifru nul și transmitere incompletă a informațiilor de sistem" >}}

## Actori de amenințare și posibile ținte

Înțelegerea celor care instalează captatoare IMSI și a țintelor lor este esențială pentru evaluarea modelului personal de amenințare și alegerea setărilor **Rayhunter** potrivite. Actorii de amenințare au niveluri diferite de sofisticare, iar strategiile lor de țintire indică ce tipuri de supraveghere este conceput **Rayhunter** să detecteze.

### Agenții guvernamentale și de aplicare a legii

**Nivelul amenințării:** avansat până la nivel profesional
**Ținte principale:**
- Suspecți cercetați penal
- Persoane de interes în cazuri de securitate națională
- Protestatari și activiști la manifestații
- Supravegherea populației în zone cu securitate ridicată
- Cetățeni străini și personal diplomatic

**Tipare de detectare:** Captatoarele IMSI operate de guvern folosesc adesea echipamente sofisticate care pot evita euristicile de bază. Totuși, ele recurg frecvent la **atacuri de retrogradare la 2G** și **tipare de eliberare a conexiunii** pentru a forța dispozitivele să folosească rețele mai puțin sigure, mai ușor de interceptat. Detectarea retrogradării LTE SIB6/7 și monitorizarea eliberării conexiunii din **Rayhunter** sunt deosebit de eficiente împotriva tehnicilor de supraveghere ale organelor de aplicare a legii.

**Scenarii obișnuite:**
- Supraveghere cu ocazia protestelor, mitingurilor sau adunărilor publice
- Monitorizare în apropierea instituțiilor guvernamentale sau a infrastructurii sensibile
- Supravegherea țintită a unor persoane cercetate
- Operațiuni de supraveghere la frontiere și aeroporturi

### Agenții de informații interne și străine

**Nivelul amenințării:** profesional până la militar
**Ținte principale:**
- Agenți și resurse de informații străine
- Oficialități guvernamentale și personal diplomatic
- Contractori și cercetători din domeniul apărării
- Directori din industrii strategice
- Jurnaliști care relatează despre securitatea națională
- Activiști implicați în subiecte politice sensibile

**Tipare de detectare:** Echipamentele de nivel informativ sunt concepute să fie discrete, dar detectarea cifrului nul și monitorizarea SIB incomplete din **Rayhunter** pot identifica chiar și unele operațiuni sofisticate. Agențiile de informații folosesc adesea echipamente care solicită informații **IMSI** în operațiuni țintite, declanșând algoritmii **Rayhunter** de detectare a solicitărilor IMSI.

**Scenarii obișnuite:**
- Supravegherea pe termen lung a țintelor de informații cu valoare ridicată
- Spionaj industrial în apropierea sediilor corporative
- Monitorizarea misiunilor diplomatice și a ambasadelor
- Operațiuni de contrainformații
- Servicii străine de informații care vizează resurse interne

### Organizații infracționale

**Nivelul amenințării:** de bază până la intermediar
**Ținte principale:**
- Persoane înstărite vizate pentru răpire sau șantaj
- Concurenți comerciali, pentru obținerea de informații corporative
- Personal din poliție care investighează crima organizată
- Martori și informatori în dosare penale
- Victime ale hărțuirii, urmăririi sau violenței domestice

**Tipare de detectare:** Organizațiile infracționale folosesc de obicei captatoare IMSI mai ieftine și disponibile comercial, care declanșează simultan mai multe euristici **Rayhunter**. Din cauza nivelului tehnic limitat, aceste dispozitive prezintă adesea **implementări SIB incomplete**, folosesc **cifruri nule** pentru a colecta cât mai multe date și recurg la atacuri agresive de **retrogradare la 2G**.

**Scenarii obișnuite:**
- Urmărirea unor posibile ținte de răpire sau jaf
- Monitorizarea comunicațiilor poliției în timpul operațiunilor infracționale
- Spionaj industrial și colectarea de informații despre concurență
- Campanii de urmărire și hărțuire
- Intimidarea martorilor și urmărirea locației

### Spionaj corporativ și servicii private de informații

**Nivelul amenințării:** intermediar până la avansat
**Ținte principale:**
- Conducerea companiilor concurente
- Echipe de cercetare și dezvoltare
- Negociatori de fuziuni și achiziții
- Deținători de proprietate intelectuală
- Păstrători de secrete comerciale
- Avertizori corporativi și surse de amenințări interne

**Tipare de detectare:** Operațiunile de supraveghere corporativă folosesc adesea echipamente de nivel mediu, care echilibrează costul și capabilitățile. Aceste instalări declanșează frecvent **detectarea eliberării conexiunii** și **alerte de solicitare IMSI** atunci când vizează persoane în timpul negocierilor de afaceri sau al dezvoltării produselor.

**Scenarii obișnuite:**
- Supraveghere în timpul negocierilor de fuziuni și achiziții
- Colectarea de informații competitive la târguri și conferințe
- Operațiuni de furt al proprietății intelectuale
- Monitorizarea angajaților și detectarea amenințărilor interne
- Colectarea datelor clienților pentru obținerea unui avantaj competitiv

### Detectivi particulari și firme de supraveghere

**Nivelul amenințării:** de bază până la intermediar
**Ținte principale:**
- Persoane cercetate pentru fraudă în domeniul asigurărilor
- Soți implicați în proceduri de divorț
- Angajați suspectați de abateri
- Persoane implicate în litigii
- Vedete și persoane cunoscute

**Tipare de detectare:** Operațiunile private de supraveghere folosesc de obicei echipamente disponibile comercial, cu posibilități limitate de personalizare. Constrângerile de cost și limitările tehnice fac ca aceste sisteme să declanșeze frecvent euristicile de bază **Rayhunter**, mai ales **detectarea cifrului nul** și **monitorizarea SIB incomplete**.

**Scenarii obișnuite:**
- Investigații privind divorțul și custodia
- Supraveghere pentru investigarea fraudelor de asigurare
- Investigații privind conduita angajaților
- Urmărirea vedetelor și activități paparazzi
- Investigarea cazurilor legale și strângerea de dovezi

### Persoane rău-intenționate și hacktiviști

**Nivelul amenințării:** de bază până la intermediar
**Ținte principale:**
- Dușmani personali sau interese romantice
- Personalități publice și vedete
- Victime alese la întâmplare în spații publice
- Participanți la anumite evenimente sau aflați în anumite locuri
- Membri ai comunităților sau grupurilor vizate

**Tipare de detectare:** Persoanele individuale folosesc de obicei configurații rudimentare sau improvizate de captatoare IMSI, care declanșează simultan mai mulți algoritmi **Rayhunter**. Aceste instalări folosesc frecvent **cifruri nule**, emit **mesaje SIB incomplete** și încearcă atacuri neîndemânatice de **retrogradare la 2G**.

**Scenarii obișnuite:**
- Campanii de urmărire și hărțuire
- Furt de identitate și fraudă financiară
- Activism politic și perturbarea protestelor
- Activități de criminalitate informatică în general
- Supraveghere oportunistă la evenimente publice

### Evaluarea amenințării și configurarea Rayhunter

**Persoanele cu risc ridicat** (jurnaliști, activiști, oficiali guvernamentali, directori) ar trebui să activeze toate euristicile **Rayhunter** și modul de afișare cu **vizibilitate ridicată**, pentru detectare maximă.

**Persoanele cu risc moderat** (utilizatori obișnuiți preocupați de confidențialitate) pot folosi modul de afișare **discret**, cu euristicile esențiale activate pentru protecție zilnică fără a atrage atenția.

**Protecția în timpul evenimentelor** (proteste, întâlniri sensibile, călătorii) justifică activarea temporară a tuturor metodelor de detectare și a sistemelor de notificare, pentru o imagine cuprinzătoare a riscurilor de supraveghere.

Înțelegerea modelului tău de amenințare te ajută să optimizezi configurarea **Rayhunter** conform profilului tău de risc și să păstrezi acoperirea potrivită împotriva actorilor care au cele mai mari șanse să te vizeze pe tine sau activitățile tale.

{{< figure src="imsi-catcher-threat-actors-surveillance.webp" alt="Diagramă cu diferiți actori de amenințare care folosesc captatoare IMSI, inclusiv agenții guvernamentale, organizații infracționale și operatori de spionaj corporativ ce vizează dispozitive mobile" >}}

## Eficiența Rayhunter în era 5G

{{< figure src="rayhunter-5g-downgrade-attack-persistence.webp" alt="Diagramă care arată un telefon compatibil cu 5G forțat printr-un atac de retrogradare să folosească o rețea 4G sau 3G monitorizată, tehnică pe care Rayhunter continuă să o detecteze în era 5G" >}}

Pe măsură ce rețelele celulare trec la tehnologia 5G, apar întrebări despre eficiența continuă a **Rayhunter**, care detectează rețele 2G, 3G și 4G/LTE, dar nu metode native de supraveghere 5G. Înțelegerea limitelor actuale și a relevanței continue a **Rayhunter** într-o lume 5G este importantă pentru planificarea strategiilor de detectare a supravegherii pe termen lung.

### De ce Rayhunter rămâne eficient în rețelele 5G

#### Persistența atacurilor de retrogradare

Vectorul fundamental detectat de **Rayhunter**, forțarea dispozitivelor să se conecteze la rețele mai puțin sigure, rămâne relevant în rețelele 5G. **Captatoarele IMSI încă se bazează pe atacuri de retrogradare la 2G și 3G**, deoarece:

- **Costuri de implementare mai mici:** Construirea echipamentelor de supraveghere pentru protocoale vechi necesită investiții mult mai mici decât dezvoltarea sistemelor compatibile cu 5G.
- **Compatibilitate mai largă cu dispozitivele:** Vizarea rețelelor 2G/3G asigură funcționarea supravegherii și împotriva dispozitivelor vechi, fără 5G.
- **Metodologii de atac consacrate:** Tehnicile de supraveghere pentru 2G/3G sunt bine documentate și testate.
- **Avantaje de reglementare:** Unele tehnologii mai vechi pot avea mai puține restricții legale decât metodele avansate de interceptare 5G.

#### Compatibilitatea retroactivă a rețelelor

Rețelele 5G păstrează **compatibilitatea retroactivă cu 4G/LTE**, iar majoritatea dispozitivelor mobile acceptă simultan mai multe generații. Această compatibilitate oferă oportunități continue pentru atacurile de retrogradare detectate de **Rayhunter**:

- **Mecanisme de revenire automată:** Dispozitivele revin în mod natural la 4G când acoperirea 5G este slabă, creând ocazii pentru echipamentele de supraveghere să intercepteze tranziția.
- **Vulnerabilități la negocierea protocoalelor:** Procesul de handshake dintre generațiile rețelei poate fi manipulat de captatoare IMSI sofisticate.
- **Exploatarea zonelor fără acoperire:** Echipamentele instalate strategic în zone fără acoperire 5G completă pot forța conectarea la rețele 4G/LTE monitorizate.

#### Calendarul gradual al implementării 5G

**Extinderea lentă a acoperirii 5G complete** asigură relevanța **Rayhunter** pentru mai mulți ani:

- **Diferențe urban-rural:** Multe regiuni se bazează în principal pe 4G/LTE, unde funcțiile **Rayhunter** de detectare rămân direct aplicabile.
- **Limitele acoperirii interioare:** Semnalele 5G pătrund adesea greu în clădiri, ceea ce face dispozitivele să revină la rețele 4G monitorizate eficient de **Rayhunter**.
- **Călătorii internaționale:** Dezvoltarea 5G diferă mult de la o țară la alta, așa că supravegherea 4G/LTE rămâne o preocupare pentru călători.

#### Întârzierea tehnologică a actorilor de amenințare

Ciclurile de **achiziție și implementare a echipamentelor de supraveghere** rămân adesea în urma tehnologiei comerciale de rețea:

- **Termenele de achiziție guvernamentale:** Poliția și agențiile de informații pot continua să folosească echipamente existente compatibile cu 4G mai mulți ani după extinderea 5G.
- **Analiza cost-beneficiu:** Multe operațiuni își ating scopul prin interceptare 4G/LTE mai ieftină, ceea ce reduce interesul pentru actualizarea la sisteme 5G.
- **Cerințe de instruire și expertiză:** Operarea echipamentelor de supraveghere 5G necesită cunoștințe specializate, care se dezvoltă în timp în organizațiile de supraveghere.

### Limitele Rayhunter în medii 5G reale

#### Puncte oarbe pentru supravegherea 5G nativă

*Aceasta este limita esențială a Rayhunter.* **Rayhunter nu detectează operațiuni native de capturare IMSI 5G care nu depind de atacuri de retrogradare:**

- **Rețele 5G autonome (SA):** Când dispozitivele se conectează la rețele exclusiv 5G fără revenire la 4G, **Rayhunter** nu poate monitoriza comunicațiile respective.
- **Echipamente avansate de supraveghere 5G:** Actorii sofisticați cu acces la tehnologie avansată ar putea intercepta comunicații 5G fără să declanșeze euristicile **Rayhunter**.
- **Exploatarea segmentării rețelei:** Funcțiile de segmentare a rețelei 5G ar putea fi folosite în scopuri de supraveghere pe care **Rayhunter** nu le detectează.

#### Funcții de securitate 5G îmbunătățite

Rețelele 5G includ **măsuri de securitate îmbunătățite**, care pot reduce eficiența metodelor tradiționale de supraveghere:

- **Protocoale de criptare mai puternice:** 5G folosește standarde de criptare mai robuste și mai greu de spart decât generațiile anterioare.
- **Proceduri de autentificare îmbunătățite:** Autentificarea îmbunătățită a dispozitivelor în 5G poate îngreuna colectarea IMSI.
- **Monitorizarea securității rețelei:** Infrastructura 5G include funcții mai bune de detectare a intruziunilor, care pot identifica și contracara tentativele de supraveghere.

#### Schimbări în comportamentul dispozitivelor

Pe măsură ce 5G devine mai răspândit, **comportamentul dispozitivelor mobile se poate schimba** și poate influența capabilitățile **Rayhunter**:

- **Rezistență sporită la retrogradare:** Actualizările viitoare ale software-ului ar putea crește rezistența dispozitivelor la atacuri de retrogradare.
- **Preferință pentru conectarea 5G:** Dispozitivele ar putea acorda prioritate tot mai mare conexiunilor 5G și ar putea deveni mai suspicioase la solicitările de folosire a protocoalelor vechi.
- **Conștientizare de securitate îmbunătățită:** Sistemele de operare mobile ar putea implementa o detecție mai bună a comportamentului suspect al rețelei.

### Considerații strategice privind implementarea Rayhunter

#### Recomandări actuale de implementare

Pentru utilizarea imediată și pe termen scurt, **Rayhunter** oferă **capabilități cuprinzătoare de detectare a supravegherii**:

- **Utilizare urbană:** Chiar și în orașe mari cu acoperire 5G extinsă, **Rayhunter** detectează încercările de supraveghere care vizează rețelele 4G/LTE.
- **Protecția evenimentelor critice:** Pentru proteste, întâlniri sensibile sau activități cu risc ridicat, **Rayhunter** oferă detectare importantă indiferent de acoperirea 5G.
- **Securitate în călătorii:** **Rayhunter** rămâne eficient pentru detectarea supravegherii în timpul călătoriilor interne și internaționale.

#### Strategii pregătite pentru viitor

Organizațiile și persoanele care planifică detectarea supravegherii pe termen lung ar trebui să ia în calcul:

- **Metode hibride de detectare:** Combinarea **Rayhunter** cu alte instrumente și tehnici de monitorizare oferă acoperire amplă pentru mai multe tipuri de amenințări.
- **Actualizarea regulată a evaluării amenințărilor:** Urmărirea evoluției tehnologiei de supraveghere ajută la stabilirea momentului în care capabilitățile **Rayhunter** trebuie completate sau înlocuite.
- **Sprijinirea dezvoltării comunitare:** Susținerea dezvoltării open-source **Rayhunter** crește șansa ca versiunile viitoare să includă detectare 5G.

#### Monitorizarea evoluției tehnologiei

Comunitatea **Rayhunter** și **EFF** cercetează în continuare capabilitățile de **detectare a supravegherii 5G**:

- **Cercetarea analizei protocoalelor:** Cercetarea continuă a protocoalelor 5G poate descoperi noi oportunități de detectare pentru versiuni viitoare **Rayhunter**.
- **Studii de compatibilitate hardware:** Evaluează dacă dispozitivele compatibile actuale pot fi îmbunătățite pentru a detecta tentative de supraveghere 5G.
- **Monitorizarea peisajului de amenințări:** Urmărirea dezvoltării și implementării echipamentelor de supraveghere 5G informează prioritățile viitoare ale **Rayhunter**.

**Rayhunter** rămâne un **instrument esențial de detectare a supravegherii** în telecomunicațiile actuale. Este de așteptat să fie relevant încă mai mulți ani, pe măsură ce 5G se extinde treptat, iar actorii de amenințare continuă să se bazeze pe metode consacrate de atac prin retrogradare.

### Reanalizarea înregistrărilor

**Rayhunter** își îmbunătățește continuu funcțiile de detectare. Poți reanaliza înregistrări mai vechi cu euristici actualizate, făcând clic pe „N warnings” în interfața web și selectând „re-analyze”.

### Analiză pe desktop

Pentru utilizatorii avansați, **Rayhunter** include `rayhunter-check`, un instrument CLI pentru analizarea fișierelor PCAP și QMDL pe sisteme desktop:

```bash
rayhunter-check -p ~/Downloads/myfile.qmdl
rayhunter-check -p ~/Downloads/myfile.pcap
rayhunter-check -d -p ~/Downloads/myfile.qmdl  # Mod de depanare
```

## Dispozitive compatibile

**Rayhunter** acceptă mai multe hotspoturi mobile cu modemuri Qualcomm care expun interfața `/dev/diag`.

{{< figure src="/img/rayhunter-device-regions.svg" alt="Compatibilitatea dispozitivelor Rayhunter în funcție de regiune" caption="Compatibilitatea dispozitivelor și recomandări regionale pentru instalările Rayhunter" >}}

### Dispozitive recomandate

Aceste dispozitive au fost testate pe larg și sunt utilizate frecvent în comunitatea **Rayhunter**:

#### Orbic RC400L (uneori comercializat ca Kajeet RC400L)
- **Regiune recomandată:** Americile
- **Benzi acceptate:**
  - 5G: n260/n261, n77, n2/5/48/66
  - 4G: 2/4/5/12/13/48/66
  - Global și roaming: n257/n78
- **Disponibilitate:** **[Noul Rayhunter Orbic RC400L](https://stscollective.com/products/new-rayhunter-orbic-rc400l-imsi-catcher-detector-premium?variant=51361976811822)** și **[Kajeet RC400L](https://stscollective.com/products/rayhunter-imsi-catcher-detector-kajeet-rc400lx-4g-lte-hotspot?variant=51411271844142)**, dispozitive compatibile disponibile.
- **Interval de prețuri:** Modelele profesionale sunt disponibile la STS Collective.

#### TP-Link M7350
- **Regiune recomandată:** Africa, Europa și Orientul Mijlociu (funcționează și în Americi, dar de obicei costă mai mult).
- **Cerințe speciale:** Necesită un card SD formatat FAT pentru înregistrări.
- **Disponibilitate:** **[TP-Link M7350 Rayhunter](https://stscollective.com/collections/rayhunter)**, cu modele compatibile verificate.

### Dispozitive funcționale

S-a confirmat că **Rayhunter** funcționează și pe următoarele dispozitive:

- **Wingtech CT2MHS01** (Americile), **[Rayhunter de vânzare](https://stscollective.com/collections/rayhunter)**
- **Tmobile TMOHS1** (Americile), **[Rayhunter de vânzare](https://stscollective.com/collections/rayhunter)**
- **TP-Link M7310** (Africa, Europa și Orientul Mijlociu), **[Rayhunter de vânzare](https://stscollective.com)**
- **PinePhone și PinePhone Pro** (global), **[Rayhunter de vânzare](https://stscollective.com)**
- **FY UZ801** (Asia și Europa), **[Rayhunter de vânzare](https://stscollective.com)**
- **Hotspot Moxee** (Americile), **[Moxee K779HSDL Rayhunter](https://stscollective.com/products/rayhunter-imsi-catcher-stingray-detector-moxee-k779hsdl-hotspot-professionally-refurbished-pre-installed-4g-lte-cellular-threat-detection-device?variant=51309010420014)**

### Note de instalare pentru dispozitive specifice

#### Orbic/Kajeet RC400L

Orbic RC400L este dispozitivul original pentru care a fost dezvoltat **Rayhunter**. Este disponibil **[Rayhunter de vânzare](https://stscollective.com)** prin STS Collective.

**Metode de instalare:**
- **Prin rețea:** `./installer orbic` (recomandată, funcționează prin WiFi)
- **Prin USB:** `./installer orbic-usb` (oferă acces ADB și shell root)

**Parole implicite:**
- **Verizon RC400L:** Parola de administrator este întotdeauna aceeași cu parola WiFi (o găsești în meniul dispozitivului).
- **Kajeet/Smartspot RC400L:** `$m@rt$p0tc0nf!g`
- **Dispozitive Moxee:** Formatul parolei este `12$XXX`, unde XXX reprezintă ultimele 3 cifre ale parolei WiFi (verifică sub baterie).

**Acces la shell:** După instalare, folosește `./installer util orbic-shell`.

#### TP-Link M7350/M7310

Aceste dispozitive funcționează fiabil cu **Rayhunter** și sunt **[Rayhunter de vânzare](https://stscollective.com)**.

**Instalare:** `./installer tplink` (nu este necesară parola de administrator)
**Stocare:** Introdu un card SD formatat FAT înainte de instalare
**Acces la shell:** `./installer util tplink-shell`

#### Dispozitive specializate

**PinePhone și PinePhone Pro:** Compatibilitate globală, **[Rayhunter de vânzare](https://stscollective.com)**
**UZ801:** Popular în regiunile Asia și Europa, **[Rayhunter de vânzare](https://stscollective.com)**
**Wingtech CT2MHS01:** Dispozitiv destinat Americilor, **[Rayhunter de vânzare](https://stscollective.com)**

### Adăugarea de dispozitive noi

**Rayhunter** poate funcționa potențial cu orice dispozitiv care are un modem Qualcomm ce expune `/dev/diag`. Dacă vrei ca **Rayhunter** să accepte un anumit dispozitiv, deschide o discuție în depozitul oficial GitHub.

## Documentația API REST

**Rayhunter** oferă o API REST cuprinzătoare pentru accesarea programatică a stării, înregistrărilor și configurării dispozitivului. API-ul permite integrarea cu alte instrumente de securitate și sisteme automate de monitorizare.

### Documentația oficială API

Pentru referința completă a API-ului, cu specificații detaliate ale endpointurilor, exemple de cereri și răspunsuri și metode de autentificare, consultă **[documentația oficială API REST Rayhunter](https://efforg.github.io/rayhunter/api-docs/)**.

### Endpointuri API

API-ul **Rayhunter** este disponibil la `http://[device-ip]:8080/api/` și oferă endpointuri pentru:

- **Starea sistemului:** Monitorizează starea dispozitivului și funcționarea **Rayhunter**
- **Gestionarea înregistrărilor:** Pornește, oprește și descarcă înregistrări
- **Preluarea alertelor:** Accesează alertele de detectare și rezultatele analizei
- **Configurare:** Actualizează programatic setările **Rayhunter**
- **Controlul euristicilor:** Activează/dezactivează algoritmi specifici de detectare
- **Informații despre dispozitiv:** Preia specificațiile și funcțiile dispozitivului
- **Monitorizarea rețelei:** Accesează datele rețelei celulare în timp real
- **Jurnalizarea evenimentelor:** Interoghează evenimentele și alertele de detectare anterioare

### Autentificare

Accesul la API folosește aceeași autentificare ca interfața web. Asigură-te că dispozitivul **Rayhunter** este securizat corespunzător și accesibil numai utilizatorilor autorizați.

### Exemple de integrare

API-ul REST **Rayhunter** se poate integra cu diverse platforme de monitorizare a securității, sisteme SIEM și instrumente de automatizare personalizate. Consultă **[documentația oficială API](https://efforg.github.io/rayhunter/api-docs/)** pentru exemple complete de implementare și bune practici.

## Depanare

### Probleme frecvente de instalare

**Probleme de conexiune USB:** Încearcă alte cabluri sau porturi USB. Conexiunile USB defectuoase provoacă frecvent erori de instalare. *Aceasta este cea mai frecventă cauză a instalărilor nereușite.*

**Probleme de securitate macOS:** Dacă apare mesajul „No Orbic device found”, schimbă temporar „Allow accessories to connect” în „Always” din setările de securitate.

**Detectarea dispozitivului:** După instalare, activează euristica de test pentru a verifica funcționarea **Rayhunter**.

### Cum primești ajutor

Pentru suport la instalare și depanare:
- Consultă documentația oficială **Rayhunter**.
- Folosește `./installer --help` și `./installer util --help` pentru opțiunile comenzilor.
- Participă la discuțiile GitHub pentru ajutorul comunității.
- Contactează **[STS Collective](https://stscollective.com)** pentru întrebări despre compatibilitatea dispozitivelor.

## Întrebări frecvente (FAQ)

### Întrebări generale

#### Ce este un captator IMSI și cum funcționează?

Un captator IMSI (numit și StingRay, simulator de stație celulară sau turn fals) este un echipament de supraveghere care imită turnurile celulare legitime pentru a intercepta comunicațiile dispozitivelor mobile. Forțează dispozitivele apropiate să se conecteze la echipamentul malițios în locul turnurilor legitime, permițând operatorilor să colecteze identificatori ai dispozitivelor (numere IMSI), date de localizare, metadate ale apelurilor și, posibil, să intercepteze comunicații. **Rayhunter** detectează aceste echipamente prin identificarea tiparelor anormale ale comportamentului rețelei celulare.

#### Poate Rayhunter să detecteze toate tipurile de echipamente de supraveghere?

**Rayhunter** detectează în mod specific captatoarele IMSI și simulatoarele de stații celulare care funcționează în rețele 2G, 3G și 4G/LTE. Nu detectează alte tipuri de supraveghere, cum ar fi monitorizarea WiFi, dispozitive de urmărire GPS, supravegherea fizică sau supravegherea 5G nativă care nu folosește atacuri de retrogradare. **Rayhunter** este o componentă a unei strategii cuprinzătoare de protecție a confidențialității.

#### Este legală utilizarea Rayhunter?

Utilizarea **Rayhunter** este legală în majoritatea jurisdicțiilor, deoarece este un instrument de monitorizare pasivă, care nu interferează cu rețelele celulare sau cu alte dispozitive. Analizează doar semnalele celulare recepționate în mod normal de dispozitiv. Legislația locală variază, așa că verifică normele aplicabile. EFF a dezvoltat **Rayhunter** ca instrument legitim de protecție a confidențialității.

### Întrebări tehnice

#### De ce are Rayhunter nevoie de o cartelă SIM dacă nu necesită serviciu activ?

Cartela SIM furnizează Identitatea Internațională a Abonatului Mobil (IMSI), necesară pentru ca dispozitivul să se autentifice în rețele celulare și să participe la schimburile de protocol celular monitorizate de **Rayhunter**. Fără SIM, dispozitivul nu se poate conecta la rețele celulare, iar **Rayhunter** nu are activitate de rețea pe care s-o analizeze pentru tipare suspecte.

#### Câte date consumă Rayhunter în timpul funcționării normale?

**Rayhunter** folosește puține date pentru monitorizarea de bază, deoarece analizează în principal informații despre protocolul celular, nu traficul de internet. Totuși, consumul de date crește dacă activezi notificările la distanță prin ntfy sau folosești dispozitivul simultan ca hotspot. Monitorizarea în sine consumă o lățime de bandă neglijabilă.

#### Pot folosi Rayhunter în timp ce dispozitivul este hotspot mobil?

Da, **Rayhunter** poate rula în același timp în care dispozitivul funcționează ca hotspot mobil. Este necesar un plan activ de servicii celulare. Monitorizarea **Rayhunter** funcționează independent de hotspot, dar folosirea simultană a ambelor funcții consumă mai multă baterie.

#### Care este diferența dintre instalarea prin WiFi și USB?

**Metoda WiFi**, recomandată majorității utilizatorilor, instalează **Rayhunter** prin interfața wireless a dispozitivului și oferă funcțiile standard. **Metoda USB** activează accesul Android Debug Bridge (ADB), pentru utilizatorii avansați care au nevoie de funcții de depanare, dar este mai complexă și nu este necesară pentru instalările obișnuite.

### Întrebări despre dispozitive și compatibilitate

#### De ce funcționează Rayhunter numai cu anumite dispozitive?

**Rayhunter** necesită modemuri Qualcomm care expun interfața `/dev/diag`, prin care se accesează informații despre protocolul celular. Majoritatea dispozitivelor de consum nu oferă această interfață din motive de securitate. Dispozitivele acceptate au fost testate în mod special și s-a confirmat că respectă cerințele **Rayhunter**.

#### Pot instala Rayhunter pe smartphone-ul meu obișnuit?

Nu. **Rayhunter** nu poate fi instalat pe smartphone-uri obișnuite. Necesită hotspoturi mobile specializate, cu anumite modemuri Qualcomm care expun interfețe de diagnosticare. Printre dispozitivele compatibile se află Orbic RC400L, TP-Link M7350 și alte modele de hotspot mobil.

#### Ce se întâmplă dacă încerc să instalez Rayhunter pe un dispozitiv incompatibil?

Instalatorul **Rayhunter** include detectarea dispozitivului și, de regulă, refuză instalarea pe hardware incompatibil. Forțarea instalării pe un dispozitiv neacceptat îl poate deteriora sau îl poate face nefuncțional. Verifică întotdeauna compatibilitatea înainte de instalare.

#### Am nevoie de dispozitive diferite pentru regiuni diferite?

Da. Benzile de frecvență celulară diferă în funcție de regiune. Orbic RC400L este optimizat pentru rețelele din Americi, iar TP-Link M7350 funcționează bine în Europa, Africa și Orientul Mijlociu. Informațiile de compatibilitate **Rayhunter** includ recomandări regionale pentru a ajuta la alegerea dispozitivului potrivit locației tale.

### Întrebări despre utilizare și configurare

#### Cum aflu dacă dispozitivul Rayhunter funcționează corect?

Activează euristica de test din setările **Rayhunter**. Aceasta generează alerte de fiecare dată când dispozitivul detectează un turn celular, confirmând funcționarea sistemului. Ecranul ar trebui să afișeze o linie verde în funcționarea normală. Nu uita să dezactivezi euristica după verificare, deoarece generează multe alerte.

#### Ce fac dacă Rayhunter declanșează o alertă?

Când **Rayhunter** detectează activitate suspectă, notează mai întâi locația și circumstanțele. Optimizarea rețelei sau problemele echipamentelor pot cauza alarme false. Dacă alertele continuă în același loc sau în timpul activităților sensibile, ia în calcul schimbarea locației și verifică detaliile în interfața web pentru a înțelege ce s-a detectat.

#### Cât de des ar trebui să actualizez Rayhunter?

**Actualizează lunar.** Consultă pagina versiunilor pentru noi euristici și îmbunătățiri de compatibilitate, adăugate frecvent. EFF îmbunătățește continuu funcțiile **Rayhunter** în funcție de tehnicile de supraveghere în evoluție. Actualizarea este identică procesului inițial de instalare.

#### Poate Rayhunter să protejeze simultan mai multe persoane?

**Rayhunter** detectează captatoarele IMSI din zona înconjurătoare, așa că poate proteja mai multe persoane aflate în raza de acțiune (de obicei câteva sute de metri, în funcție de intensitatea semnalului). Totuși, fiecare persoană preocupată serios de detectarea supravegherii ar trebui să ia în calcul propriul dispozitiv **Rayhunter**, pentru protecție și control maxime asupra configurării.

### Întrebări despre securitate și confidențialitate

#### Folosirea Rayhunter mă face mai vizibil pentru supraveghere?

**Rayhunter** funcționează pasiv și nu transmite semnale prin care echipamentele de supraveghere să-l poată identifica. Totuși, folosirea oricărui instrument de securitate arată interes pentru confidențialitate. Beneficiile detectării depășesc de obicei riscurile, mai ales pentru persoane cu risc ridicat precum jurnaliștii și activiștii.

#### Pot echipamentele de supraveghere să detecteze că folosesc Rayhunter?

**Rayhunter** este un sistem de monitorizare pasivă și nu transmite semnale identificabile. Operatorii de supraveghere nu pot detecta folosirea **Rayhunter** la nivelul protocolului celular. Observarea fizică a dispozitivului sau analiza traficului de rețea ar putea dezvălui utilizarea dacă notificările la distanță **Rayhunter** sunt activate.

#### Ce informații colectează Rayhunter despre mine?

**Rayhunter** analizează informații despre protocolul celular și stochează alertele de detecție local pe dispozitiv. Nu colectează informații personale, conținutul comunicațiilor sau date de localizare în afara celor necesare algoritmilor de detecție. Toate datele rămân pe dispozitiv dacă nu activezi notificările la distanță.

### Întrebări avansate

#### Pot analiza datele Rayhunter pe computer?

Da. **Rayhunter** include instrumentul CLI `rayhunter-check` pentru analizarea fișierelor PCAP și QMDL înregistrate pe sisteme desktop. Astfel, utilizatorii avansați pot analiza în detaliu evenimentele detectate și investiga activitățile suspecte folosind toate resursele computerului.

#### Cum funcționează Rayhunter în mediile urbane dense?

Zonele urbane dense, cu multe turnuri celulare legitime, pot crește rata alarmelor false deoarece optimizarea rețelei și transferurile dintre turnuri au loc mai des. Algoritmii **Rayhunter** sunt concepuți să distingă comportamentul normal al rețelei de activitățile de supraveghere, dar utilizatorii din zone dense pot avea nevoie să ajusteze sensibilitatea.

#### Funcționează Rayhunter în timpul călătoriilor internaționale?

Eficiența **Rayhunter** în călătorii depinde de compatibilitatea dispozitivului cu benzile celulare locale și acordurile de roaming. Algoritmii de detectare funcționează global, dar verifică dacă dispozitivul acceptă frecvențele folosite în țara de destinație. Roamingul internațional poate fi necesar pentru funcționarea completă.

{{< figure src="rayhunter-faq-privacy-protection.webp" alt="O persoană verifică alertele Rayhunter pe un laptop și transportă un hotspot mobil într-un mediu urban cu turnuri celulare în apropiere" >}}

______

**Rayhunter** este un progres important în protecția confidențialității personale și detectarea supravegherii. Prin instalarea și configurarea corectă a **Rayhunter** pe dispozitive compatibile, obții capabilități utile pentru a detecta captatoare IMSI și a proteja comunicațiile mobile împotriva supravegherii neautorizate.

Indiferent dacă ești jurnalist, activist, specialist în securitate sau preocupat de confidențialitate, **Rayhunter** oferă instrumentele necesare pentru menținerea securității mobile într-o lume tot mai supravegheată. Pentru dispozitive compatibile verificate, vezi opțiunile **[Rayhunter de vânzare](https://stscollective.com)** ale furnizorilor de încredere de echipamente de securitate.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Cumpără dispozitive Rayhunter și economisește 20%
{{< /centerbutton >}}

## Referințe

- [Depozitul GitHub oficial Rayhunter](https://github.com/EFForg/rayhunter)
- [Cea mai recentă versiune Rayhunter](https://github.com/EFForg/rayhunter/releases/tag/v0.10.2)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [STS Collective, furnizor de echipamente Rayhunter](https://stscollective.com)

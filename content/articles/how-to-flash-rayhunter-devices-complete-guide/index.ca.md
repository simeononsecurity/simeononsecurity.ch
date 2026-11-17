---
title: "Com flashejar dispositius Rayhunter: guia completa"
draft: false
toc: true
date: 2026-03-09
lastmod: 2026-11-15
description: "Flasheja i configura Rayhunter per detectar IMSI catchers. Comprova quins dispositius són compatibles, instal·la el microprogramari, verifica que funcioni i resol els problemes habituals."
tags: ["Rayhunter", "captador d'IMSI", "simulador de cel·la mòbil", "seguretat mòbil", "detecció de vigilància", "protecció de la privadesa", "Orbic RC400L", "TP-Link M7350", "punt d'accés mòbil", "flasheig de dispositius", "ciberseguretat", "seguretat sense fil", "mesures contra la vigilància", "EFF", "eines de privadesa", "comprar Rayhunter", "guia d'instal·lació", "configuració", "dispositius compatibles", "seguretat de xarxa"]
cover: "/img/cover/rayhunter.webp"
coverAlt: "Un dispositiu Rayhunter detecta senyals sense fil i IMSI catchers, envoltat d'escuts de seguretat"
coverCaption: "Sistema de detecció d'IMSI catchers Rayhunter per protegir les comunicacions mòbils de la vigilància"
---

**Guia completa per flashejar i configurar Rayhunter, el sistema definitiu de detecció d'IMSI catchers.**

## Resum

**Rayhunter** és un sistema de codi obert que detecta IMSI catchers i funciona en punts d'accés mòbils modificats. T'avisa quan equips de vigilància intenten interceptar comunicacions mòbils. Aquesta guia explica la instal·lació completa als dispositius Orbic RC400L i TP-Link M7350, les opcions de configuració, l'anàlisi de les amenaces i l'eficàcia en xarxes 5G. Cal un dispositiu compatible amb mòdem Qualcomm. El sistema detecta vigilància en xarxes 2G, 3G i 4G mitjançant diverses heurístiques. Continua sent útil malgrat l'adopció del 5G perquè encara es fan atacs que obliguen a baixar a generacions de xarxa anteriors. Ofereix protecció essencial a periodistes, activistes i persones que valoren la privadesa davant la vigilància governamental, criminal i empresarial.

**Rayhunter** és una eina de codi obert pensada per detectar IMSI catchers (simuladors de cel·les mòbils) que poden interceptar comunicacions mòbils. Si vols **comprar Rayhunter** o aprendre a flashejar i configurar correctament aquests dispositius, aquesta guia completa explica tot el que cal saber sobre la instal·lació, la configuració i l'ús dels sistemes **Rayhunter**.

**Declaració de patrocini:** Aquest article està patrocinat per [STS Collective](https://stscollective.com), el principal proveïdor de dispositius compatibles amb Rayhunter. Malgrat el patrocini, tota la informació tècnica, l'anàlisi i les recomanacions d'aquesta guia són imparcials i es basen només en la documentació oficial de Rayhunter, les aportacions de la comunitat i una avaluació tècnica objectiva.

> 💰 **Descompte exclusiu per als lectors:** Estalvia fins a un 20% en dispositius Rayhunter i en tots els productes de STS Collective. Fes servir el codi **SIMEONONSECURITY** en pagar o [compra directament amb el descompte aplicat](https://stscollective.com/discount/SIMEONONSECURITY).

## Introducció a Rayhunter

**Rayhunter** és un sistema avançat de detecció d'IMSI catchers desenvolupat per la **Electronic Frontier Foundation (EFF)**, una organització sense ànim de lucre destacada que defensa les llibertats civils en el món digital. Des de 1990, l'EFF defensa la privadesa digital, la llibertat d'expressió i la innovació mitjançant litigis estratègics, anàlisi de polítiques, activisme de base i desenvolupament tecnològic.

Aquesta eina funciona en punts d'accés mòbils compatibles i vigila contínuament les xarxes mòbils per detectar activitats sospitoses que puguin indicar la presència de simuladors de cel·les mòbils o «Stingrays» utilitzats per vigilar. **Rayhunter** reflecteix el compromís de l'EFF de proporcionar eines pràctiques de protecció de la privadesa a persones i organitzacions que necessiten protegir-se de la vigilància.

El sistema **Rayhunter** envia alertes en temps real quan detecta comportaments potencialment maliciosos a la xarxa mòbil. És una eina essencial de protecció de la privadesa per a periodistes, activistes, professionals de la seguretat i persones que la valoren. Pots trobar dispositius compatibles **[amb Rayhunter](https://stscollective.com/collections/rayhunter)** a STS Collective, el principal proveïdor d'aquests dispositius especialitzats.

### Donar suport al projecte Rayhunter

**Rayhunter** és un projecte de codi obert que es beneficia del suport de la comunitat. Pots contribuir al seu desenvolupament continu de diverses maneres:

- **Compra a STS Collective**: STS Collective dona una part dels beneficis de cada dispositiu Rayhunter venut a l'EFF per donar suport al desenvolupament continu de **Rayhunter** i a la recerca sobre privadesa.
- **Fes donacions directes**: dona suport directament a la defensa de la privadesa de l'EFF i al desenvolupament de **Rayhunter** amb una **[donació a l'EFF](https://supporters.eff.org/donate/donate)**.
- **Participa en la comunitat**: contribueix a les converses, la documentació i les proves mitjançant el repositori oficial de GitHub.

El teu suport ajuda a mantenir **Rayhunter** gratuït, de codi obert i en millora contínua per fer front a les noves amenaces de vigilància.

## Suport, comentaris i comunitat

**Rayhunter** rep el suport d'una comunitat activa de recercadors de seguretat, defensors de la privadesa i ciutadans preocupats. Pots obtenir ajuda i contribuir al projecte per diversos canals:

- **Documentació oficial**: [Documentació de Rayhunter](https://efforg.github.io/rayhunter/introduction.html), amb guies completes d'instal·lació, configuració i ús
- **Repositori de GitHub**: [EFForg/rayhunter](https://github.com/EFForg/rayhunter)
- **Converses de la comunitat**: inicia converses a GitHub sobre compatibilitat de dispositius i resolució de problemes
- **Recerca de seguretat**: col·labora amb recercadors per millorar les capacitats de detecció de **Rayhunter**

Si busques dispositius compatibles, pots trobar **[Rayhunter a la venda](https://stscollective.com/collections/rayhunter)** a STS Collective.

## Preguntes freqüents

### Necessito una targeta SIM activa per fer servir Rayhunter?

**Rayhunter** necessita que hi hagi una targeta SIM inserida al dispositiu, però no cal que tingui un pla de servei actiu. La SIM permet que el dispositiu es connecti a xarxes mòbils i vigili activitats sospitoses. Si vols fer servir el dispositiu com a punt d'accés mentre funciona **Rayhunter**, caldrà un pla actiu.

### Com puc comprovar que el dispositiu Rayhunter funciona?

Activa la heurística de prova als paràmetres de configuració de **Rayhunter**. El dispositiu generarà una alerta cada vegada que detecti una cel·la mòbil, fet que et permetrà comprovar que el sistema funciona correctament. Aquest mode de prova genera moltes alertes, així que desactiva'l quan acabis la comprovació.

### Em convé comprar un dispositiu bloquejat o desbloquejat?

Per a la compatibilitat amb **Rayhunter**, en general és preferible un dispositiu desbloquejat, sobretot si vols fer servir targetes SIM que no siguin de Verizon. La majoria de dispositius Orbic de la marca Verizon estan desbloquejats, però comprova'n la compatibilitat abans de comprar-los. A STS Collective pots trobar dispositius compatibles verificats **[amb Rayhunter](https://stscollective.com/collections/rayhunter)**.

{{< stscollective-ad "rayhunter" >}}

## Guia d'instal·lació

### Instal·lar la versió més recent

La instal·lació de **Rayhunter** s'ha provat a macOS i Ubuntu 24.04. Si tens problemes amb les versions precompilades, potser hauràs d'instal·lar-lo des del codi font.

#### Requisits previs

Abans d'instal·lar **Rayhunter**, comprova que tens un dispositiu compatible. En dispositius TP-Link, insereix una targeta SD amb format FAT per desar-hi les gravacions.

#### Baixada i configuració

1. **Baixa la versió més recent**: obtén el fitxer adequat `rayhunter-vX.X.X-PLATFORM.zip` des de la pàgina oficial de versions:
   - Linux x64: `linux-x64`
   - Linux ARM64: `linux-aarch64`
   - Linux ARM v7/v8: `linux-armv7`
   - macOS Intel: `macos-intel`
   - macOS ARM (M1/M2): `macos-arm`
   - Windows: `windows-x86_64`

2. **Extreu el fitxer i obre la carpeta**:
   ```bash
   unzip ~/Downloads/rayhunter-vX.X.X-PLATFORM.zip
   cd ~/Downloads/rayhunter-vX.X.X-PLATFORM
   ```

3. **Connecta el dispositiu**: encén-lo i connecta'l per WiFi o connexió compartida USB. Hauries de poder accedir a:
   - Dispositius Orbic: `http://192.168.1.1`
   - Dispositius TP-Link: `http://192.168.0.1`

#### Instal·lació segons el dispositiu

**Per als dispositius Orbic RC400L** (disponibles **[amb Rayhunter](https://stscollective.com)**):

**Rayhunter** ofereix dos mètodes d'instal·lació per als dispositius Orbic RC400L. Es recomana el mètode WiFi per a la majoria d'usuaris, mentre que el mètode USB inclou funcions addicionals de depuració.

**Mètode d'instal·lació per WiFi (recomanat)**:
```bash
# Els usuaris de macOS han d'executar primer aquesta ordre:
xattr -d com.apple.quarantine installer

# Per a Verizon RC400L (la contrasenya d'administrador és la mateixa que la de WiFi):
./installer orbic --admin-password 'YourWiFiPassword'

# Per a Kajeet/Smartspot RC400L:
./installer orbic --admin-password='$m@rt$p0tc0nf!g'

# Per a dispositius Moxee (format de la contrasenya: 12$ + els 3 darrers dígits de la contrasenya WiFi):
./installer orbic --admin-password='12$XXX'
```

**Mètode d'instal·lació per USB (usuaris avançats)**:
El mètode USB activa l'accés a ADB (Android Debug Bridge) per depurar el dispositiu de manera avançada, però no es recomana per a una instal·lació normal:

```bash
# AVÍS: l'instal·lador USB no es recomana per a la majoria de casos
./installer orbic-usb
```

Aquest mètode força el dispositiu a entrar en mode de depuració per activar l'accés a ADB, instal·la rootshell i **Rayhunter**, i després reinicia el dispositiu. Fes-lo servir només si necessites accedir a ADB per a altres tasques.

**Per als dispositius TP-Link M7350** (disponibles **[amb Rayhunter](https://stscollective.com)**):
```bash
./installer tplink
```

L'instal·lador completarà el flasheig de **Rayhunter** i reiniciarà el dispositiu. Una línia verda a la pantalla indica que **Rayhunter** funciona correctament.

### Instal·lar des del codi font

Per a desenvolupadors o usuaris que necessitin compilar **Rayhunter** des del codi font, el projecte inclou:

- **Interfície**: aplicació SvelteKit en JavaScript (`./daemon/web/`)
- **Servidor**: binari de Rust `rayhunter-daemon` (`./daemon/`)
- **Instal·lador**: binari de Rust que agrupa tots els components (`./installer`)

#### Dependències de compilació

Instal·la les dependències següents:
- Llenguatge de programació Rust
- Node.js/npm
- Eines de compilació C (`build-essential` a Linux, `xcode-select --install` a macOS)

#### Procés de compilació

```bash
./scripts/build-dev.sh
./scripts/install-dev.sh orbic  # Substitueix 'orbic' pel tipus de dispositiu
```

Per desenvolupar la interfície amb recàrrega automàtica:
```bash
cd daemon/web
npm run dev
# O bé amb un objectiu personalitzat:
API_TARGET=http://192.168.1.1:8080 npm run dev
```

### Actualitzar Rayhunter

L'actualització de **Rayhunter** segueix el mateix procés que la instal·lació. Repeteix els passos d'instal·lació amb la versió més recent per actualitzar el dispositiu a l'última versió de **Rayhunter**.

## Configuració

Pots configurar **Rayhunter** des de la interfície web o editant directament `/data/rayhunter/config.toml` al dispositiu.

### Configuració de la interfície web

Per obrir la interfície web de **Rayhunter**, connecta't a la xarxa del dispositiu i visita:
- Orbic: `http://192.168.1.1:8080`
- TP-Link: `http://192.168.0.1:8080`

{{< figure src="rayhunter-dashboard.webp" alt="Tauler de la interfície web de Rayhunter" caption="La interfície web de Rayhunter ofereix opcions completes de supervisió i configuració" >}}

#### Opcions principals de configuració

**Nivell de la interfície del dispositiu**: controla què mostra **Rayhunter** a la pantalla:
- **Mode invisible**: no mostra res
- **Mode discret**: indicador amb una línia de color (verd=segur, vermell=alerta, blanc=pausat)
- **Mode de demostració**: mostra gràfics d'orca amb una línia d'estat
- **Logotip de l'EFF**: mostra el logotip de l'EFF amb una línia d'estat
- **Alta visibilitat**: pantalla de color completa

**Mode d'entrada del dispositiu**: configura el comportament del botó d'engegada:
- **Desactiva el control amb el botó**: el botó d'engegada queda desactivat per a **Rayhunter**
- **Doble toc per reiniciar la gravació**: reinicia les alertes i la supervisió

**Paràmetres de notificació**: configura l'URL de ntfy per a les alertes remotes i activa o desactiva les notificacions d'avís i de bateria baixa.

**Heurístiques de l'analitzador**: activa o desactiva algoritmes de detecció concrets de **Rayhunter** segons l'entorn i el model d'amenaça.

## Desinstal·lar Rayhunter

### Dispositius Orbic

Per treure **Rayhunter** dels dispositius Orbic:

```bash
./installer util orbic-shell --admin-password mypassword
```

Dins de l'intèrpret d'ordres:

> **Avís:** Les ordres següents eliminen permanentment els fitxers de Rayhunter i els seus scripts d'inici. Confirma que ets a l'intèrpret del dispositiu correcte, copia les gravacions o la configuració que necessitis i tingues a punt l'instal·lador i un microprogramari compatible. Després, comprova que els fitxers hagin desaparegut i que el dispositiu es reiniciï sense el servei Rayhunter. Per revertir-ho, reinstal·la la mateixa versió des del repositori oficial.

```bash
echo 3 > /usrdata/mode.cfg
rm -rf /data/rayhunter /etc/init.d/rayhunter_daemon /bin/rootshell
reboot
```

### Dispositius TP-Link

Per desinstal·lar-lo d'un dispositiu TP-Link:

> **Avís:** Aquestes ordres eliminen els fitxers de Rayhunter i el seu script d'inici del dispositiu TP-Link. Exporta primer les gravacions i la configuració. Executa-les només des de l'intèrpret del dispositiu, i després comprova que les rutes ja no hi siguin i que el dispositiu arrenqui amb normalitat. Reinstal·la la mateixa versió des del repositori oficial per revertir-ho.

```bash
./installer util tplink-shell
rm /data/rayhunter /etc/init.d/rayhunter_daemon
update-rc.d rayhunter_daemon remove
```

Elimina els activadors de port que quedin a la interfície d'administració de TP-Link, a Settings > NAT Settings > Port Triggers.

## Fer servir Rayhunter

Després d'instal·lar-lo, **Rayhunter** s'executa automàticament i vigila contínuament les xarxes mòbils per detectar activitats sospitoses. Durant el funcionament normal, la pantalla mostra una línia verda, que canvia a punts grocs, guions taronges o una línia vermella contínua quan es detecten possibles IMSI catchers.

### Heurístiques de detecció de Rayhunter

**Rayhunter** utilitza diversos algoritmes de detecció avançats per identificar possibles activitats d'IMSI catchers:

#### Detecció de sol·licituds d'IMSI
Aquesta heurística identifica seqüències sospitoses en què les cel·les mòbils demanen la identitat del dispositiu (IMSI, International Mobile Subscriber Identity) sense seguir els protocols d'autenticació adequats. **Rayhunter** vigila el moment i el context d'aquestes sol·licituds i marca patrons anormals que indiquen la possible presència d'equips de vigilància.

Les xarxes mòbils legítimes segueixen procediments d'autenticació normalitzats abans de demanar identificadors sensibles. Sovint els IMSI catchers eviten aquests protocols per recopilar ràpidament les identitats dels dispositius, fet que crea anomalies detectables en la seqüència d'autenticació. Aquest mètode és especialment eficaç contra IMSI catchers «passius» bàsics que només recullen informació dels dispositius.

#### Detecció de desconnexions i baixades a 2G
**Rayhunter** vigila contínuament els intents sospitosos de desconnectar dispositius mòbils de xarxes 4G/5G segures i tornar-los a connectar a xarxes 2G menys segures. Els IMSI catchers fan servir sovint aquest atac de baixada perquè les xarxes 2G tenen un xifratge més feble i són més fàcils d'interceptar.

El sistema analitza els patrons de desconnexió i busca una freqüència, un moment o un context anormal que indiqui intenció maliciosa, en lloc d'una optimització normal de la xarxa. De vegades les xarxes legítimes poden suggerir una baixada per cobertura o capacitat, però **Rayhunter** pot distingir entre el comportament normal de la xarxa i possibles activitats de vigilància.

#### Detecció de baixades LTE SIB6/7
Els blocs d'informació del sistema (SIB) són missatges que les xarxes mòbils emeten per proporcionar informació de configuració als dispositius. **Rayhunter** vigila específicament els missatges SIB6 i SIB7, que contenen informació sobre cel·les veïnes i redirecció de freqüències.

Els actors maliciosos poden emetre missatges SIB6/7 falsos per obligar els dispositius a abandonar connexions 4G segures i connectar-se a xarxes 2G controlades per l'atacant. **Rayhunter** analitza aquestes emissions per trobar incoherències, patrons de redirecció anormals i altres indicadors de punts d'accés fraudulents que intenten rebaixar la connexió per interceptar-la.

#### Detecció de xifratge nul
Aquest mètode essencial identifica quan les xarxes mòbils proposen comunicacions sense xifratge (xifratge nul). Les xarxes comercials legítimes no haurien de proposar mai connexions sense xifrar, perquè infringirien els estàndards de seguretat i els requisits normatius.

**Rayhunter** marca com a molt sospitosa qualsevol xarxa que proposi xifratge nul. *Una xarxa legítima no proposarà mai xifratge nul.* És un indicador clar que un equip de vigilància intenta interceptar comunicacions en text pla. Aquesta heurística és especialment eficaç contra IMSI catchers que prioritzen recopilar dades per damunt de mantenir l'aparença d'una xarxa legítima.

#### Detecció de SIB incomplets
Les estacions base mòbils legítimes emeten blocs d'informació del sistema complets amb dades essencials de configuració de xarxa. **Rayhunter** vigila les estacions que proporcionen informació incompleta o que no en proporcionen; això sovint indica equips de vigilància desplegats amb pressa o mal configurats.

Els IMSI catchers sovint no implementen totes les funcions de xarxa mòbil i es limiten a les funcions mínimes per connectar dispositius i interceptar dades. Si detecta aquestes implementacions incompletes, **Rayhunter** pot identificar estacions base potencialment malicioses a les quals falten les funcions esperades d'una infraestructura mòbil legítima.

{{< figure src="rayhunter-heuristics-overview.webp" alt="Diagrama de les cinc heurístiques de detecció de Rayhunter: sol·licitud d'IMSI sense autenticació, baixada a 2G, redirecció LTE SIB6/7, proposta de xifratge nul i emissió d'informació del sistema incompleta" >}}

## Actors d'amenaça i possibles objectius

Entendre qui desplega IMSI catchers i a qui es dirigeixen és clau per valorar el teu model d'amenaça personal i triar la configuració adequada de **Rayhunter**. Els actors d'amenaça tenen nivells de sofisticació diferents, i les seves estratègies d'orientació ajuden a entendre els tipus de vigilància que **Rayhunter** està pensat per detectar.

### Organismes governamentals i cossos policials

**Sofisticació de l'amenaça**: de nivell avançat a professional
**Objectius principals**:
- Sospitosos d'activitats delictives que s'investiguen
- Persones d'interès en casos de seguretat nacional
- Manifestants i activistes durant les protestes
- Vigilància general de la població en zones d'alta seguretat
- Ciutadans estrangers i personal diplomàtic

**Patrons de detecció**: Els IMSI catchers governamentals sovint fan servir equips sofisticats que poden evitar les heurístiques de detecció bàsiques. Tot i això, recorren sovint a **atacs de baixada a 2G** i **patrons de desconnexió** per forçar els dispositius a connectar-se a xarxes menys segures i facilitar la intercepció. La detecció de baixades LTE SIB6/7 i la supervisió de desconnexions de **Rayhunter** són especialment eficaces contra les tècniques de vigilància policial.

**Situacions habituals**:
- Vigilància d'esdeveniments durant protestes, manifestacions o reunions públiques
- Seguiment de la ubicació prop d'edificis governamentals o infraestructures sensibles
- Vigilància dirigida de persones investigades
- Operacions de vigilància a fronteres i aeroports

### Agències d'intel·ligència nacionals i estrangeres

**Sofisticació de l'amenaça**: de nivell professional a militar
**Objectius principals**:
- Agents i recursos d'intel·ligència estrangers
- Càrrecs governamentals i personal diplomàtic
- Contractistes i recercadors de defensa
- Directius d'empreses d'indústries estratègiques
- Periodistes que informen sobre seguretat nacional
- Activistes que treballen en qüestions polítiques sensibles

**Patrons de detecció**: Els equips d'intel·ligència estan dissenyats per passar desapercebuts, però la detecció de xifratge nul i la supervisió de SIB incomplets de **Rayhunter** poden identificar fins i tot operacions de vigilància sofisticades. Durant operacions dirigides, les agències d'intel·ligència sovint utilitzen equips que sol·liciten **informació IMSI** i activen els algorismes de **Rayhunter** per detectar sol·licituds d'IMSI.

**Situacions habituals**:
- Vigilància prolongada d'objectius d'alt valor per a la intel·ligència
- Espionatge industrial prop de seus corporatives
- Supervisió diplomàtica i d'ambaixades
- Operacions de contraintel·ligència
- Serveis d'intel·ligència estrangers que apunten a recursos nacionals

### Organitzacions criminals

**Sofisticació de l'amenaça**: de bàsica a intermèdia
**Objectius principals**:
- Persones riques per segrestar-les o extorsionar-les
- Competidors comercials per obtenir informació empresarial
- Personal policial que investiga el crim organitzat
- Testimonis i informadors en casos criminals
- Víctimes de persecució, assetjament o maltractament domèstic

**Patrons de detecció**: Les organitzacions criminals solen utilitzar IMSI catchers comercials de baix cost que activen diverses heurístiques de **Rayhunter** alhora. Sovint aquests dispositius tenen **implementacions SIB incompletes**, fan servir **xifratge nul** per recopilar més dades i recorren a **atacs agressius de baixada a 2G** per les limitacions tècniques.

**Situacions habituals**:
- Seguiment de possibles objectius de segrest o robatori
- Supervisió de comunicacions policials durant operacions criminals
- Espionatge empresarial i recopilació d'informació competitiva
- Campanyes de persecució i assetjament
- Intimidació de testimonis i seguiment de la ubicació

### Espionatge empresarial i intel·ligència privada

**Sofisticació de l'amenaça**: d'intermèdia a avançada
**Objectius principals**:
- Alts directius d'empreses competidores
- Equips de recerca i desenvolupament
- Negociadors de fusions i adquisicions
- Titulars de propietat intel·lectual
- Custodis de secrets comercials
- Denunciants i fonts d'amenaces internes de l'empresa

**Patrons de detecció**: Les operacions de vigilància empresarial sovint fan servir equips de nivell mitjà que equilibren el cost i la capacitat. En dirigir-se a persones concretes durant negociacions comercials o cicles de desenvolupament de producte, aquests desplegaments activen sovint la **detecció de desconnexions** i les **alertes de sol·licitud d'IMSI**.

**Situacions habituals**:
- Vigilància durant negociacions de fusions i adquisicions
- Recopilació d'informació competitiva en fires i congressos
- Operacions de robatori de propietat intel·lectual
- Supervisió de treballadors i detecció d'amenaces internes
- Recopilació de dades de clients per obtenir avantatge competitiu

### Detectius privats i empreses de vigilància

**Sofisticació de l'amenaça**: de bàsica a intermèdia
**Objectius principals**:
- Persones investigades per frau a l'assegurança
- Cònjuges en processos de divorci
- Treballadors sospitosos de mala conducta
- Persones implicades en disputes legals
- Celebritats i persones destacades

**Patrons de detecció**: Les operacions de vigilància privada solen utilitzar equips comercials amb poques opcions de personalització. A causa de les limitacions de cost i les limitacions tècniques, sovint activen les heurístiques bàsiques de **Rayhunter**, sobretot la **detecció de xifratge nul** i la **supervisió de SIB incomplets**.

**Situacions habituals**:
- Investigacions de divorci i custòdia
- Vigilància per frau a les assegurances
- Investigacions de mala conducta dels treballadors
- Assetjament de celebritats i operacions de paparazzis
- Investigació de casos legals i recopilació de proves

### Individus maliciosos i hacktivistes

**Sofisticació de l'amenaça**: de bàsica a intermèdia
**Objectius principals**:
- Enemics personals o parelles sentimentals
- Personatges públics i celebritats
- Víctimes aleatòries en espais públics
- Participants en esdeveniments o ubicacions concrets
- Membres de comunitats o grups seleccionats

**Patrons de detecció**: Els actors individuals solen utilitzar IMSI catchers bàsics, sovint improvisats, que activen diversos algorismes de detecció de **Rayhunter** alhora. Aquests desplegaments solen fer servir **xifratge nul**, **emissions SIB incompletes** i intents rudimentaris de **baixada a 2G**.

**Situacions habituals**:
- Campanyes de persecució i assetjament
- Robatori d'identitat i frau financer
- Activisme polític i interrupció de protestes
- Activitats habituals de ciberdelinqüència
- Vigilància oportunista en esdeveniments públics

### Avaluació de les amenaces i configuració de Rayhunter

Les **persones d'alt risc** (periodistes, activistes, càrrecs governamentals i directius) haurien d'activar totes les heurístiques de **Rayhunter** i fer servir el mode de pantalla d'**alta visibilitat** per maximitzar la capacitat de detecció.

Les **persones de risc moderat** (usuaris generalment preocupats per la privadesa) poden fer servir el mode **discret** amb les heurístiques principals activades per protegir-se cada dia sense cridar l'atenció.

La **protecció per a esdeveniments** (protestes, reunions sensibles o viatges) justifica activar temporalment tots els mètodes de detecció i les notificacions per tenir una visió completa de la vigilància.

Conèixer el teu model d'amenaça ajuda a optimitzar la configuració de **Rayhunter** per al teu perfil de risc i a obtenir una cobertura adequada davant els actors amb més probabilitat d'apuntar-te a tu o a les teves activitats.

{{< figure src="imsi-catcher-threat-actors-surveillance.webp" alt="Diagrama de diversos actors d'amenaça que fan servir IMSI catchers, com ara agències governamentals, organitzacions criminals i operadors d'espionatge empresarial que apunten a dispositius mòbils" >}}

## Eficàcia de Rayhunter en l'era del 5G

{{< figure src="rayhunter-5g-downgrade-attack-persistence.webp" alt="Diagrama d'un telèfon compatible amb 5G obligat per un atac de baixada a connectar-se a una xarxa 4G o 3G vigilada, una tècnica que Rayhunter encara detecta en l'era del 5G" >}}

A mesura que les xarxes mòbils passen a la tecnologia 5G, sorgeixen dubtes sobre l'eficàcia continuada de **Rayhunter**, que detecta xarxes 2G, 3G i 4G/LTE però no els mètodes de vigilància 5G nadius. Per planificar estratègies de detecció a llarg termini és essencial entendre les limitacions actuals i la utilitat continuada de **Rayhunter** en un món 5G.

### Per què Rayhunter continua sent eficaç a les xarxes 5G

#### Continuen els atacs de baixada
El principal vector d'atac que **Rayhunter** detecta, és a dir, obligar els dispositius a connectar-se a xarxes menys segures, continua sent molt rellevant en desplegaments 5G. Els **IMSI catchers encara recorren a atacs de baixada a 2G i 3G** perquè:

- **Cost d'implementació més baix**: crear equips de vigilància per a protocols antics requereix molta menys inversió que desenvolupar sistemes compatibles amb 5G
- **Compatibilitat amb més dispositius**: dirigir-se a xarxes 2G/3G també permet vigilar dispositius antics que potser no són compatibles amb 5G
- **Mètodes d'atac consolidats**: les tècniques de vigilància per a xarxes 2G/3G estan ben documentades i provades
- **Avantatges normatius**: algunes tecnologies antigues de vigilància poden tenir menys restriccions legals que els mètodes avançats d'intercepció 5G

#### Compatibilitat amb xarxes anteriors
Les xarxes 5G mantenen la **compatibilitat amb 4G/LTE**, i la majoria de dispositius mòbils admeten diverses generacions alhora. Aquesta compatibilitat crea oportunitats contínues per als atacs de baixada que **Rayhunter** està especialitzat a detectar:

- **Retorn automàtic a 4G**: els dispositius passen naturalment a 4G quan la cobertura 5G és deficient, i els equips de vigilància poden interceptar aquestes transicions
- **Vulnerabilitats en la negociació de protocols**: els IMSI catchers sofisticats poden manipular l'intercanvi inicial entre generacions de xarxa
- **Explotació de zones sense cobertura**: els equips de vigilància situats estratègicament en zones sense cobertura 5G completa poden forçar els dispositius a passar a xarxes 4G/LTE vigilades

#### Desplegament gradual del 5G
El **desplegament lent d'una cobertura 5G completa** garanteix que **Rayhunter** continuï sent útil durant anys:

- **Diferències entre zones urbanes i rurals**: moltes regions encara depenen principalment de xarxes 4G/LTE, on les capacitats de detecció de **Rayhunter** són directament aplicables
- **Limitacions de cobertura interior**: els senyals 5G sovint travessen malament els edificis i els dispositius tornen a xarxes 4G que **Rayhunter** pot vigilar eficaçment
- **Consideracions per a viatges internacionals**: el desplegament global del 5G varia molt entre països, de manera que la vigilància 4G/LTE continua sent un risc per als viatgers

#### Retard tecnològic dels actors d'amenaça
Els **cicles de compra i desplegament d'equips de vigilància** solen anar per darrere de la tecnologia de xarxes comercials:

- **Terminis de compra governamental**: els cossos policials i les agències d'intel·ligència poden continuar fent servir equips de vigilància 4G existents durant anys després del desplegament del 5G
- **Anàlisi de costos i beneficis**: moltes operacions assoleixen els seus objectius amb intercepció 4G/LTE més econòmica, fet que redueix l'incentiu d'actualitzar a sistemes 5G
- **Requisits de formació i experiència**: fer servir equips de vigilància 5G requereix coneixements especialitzats que les organitzacions poden trigar a adquirir

### Limitacions de Rayhunter en entorns 5G reals

#### Punts cecs de la vigilància 5G nativa
*Aquesta és la limitació principal de Rayhunter.* **Rayhunter no pot detectar operacions natives d'IMSI catchers 5G** que no depenen d'atacs de baixada:

- **Xarxes 5G autònomes (SA)**: si els dispositius es connecten a xarxes exclusivament 5G sense passar a 4G, **Rayhunter** no pot vigilar aquestes comunicacions
- **Equips avançats de vigilància 5G**: actors sofisticats amb tecnologia avançada podrien interceptar comunicacions 5G sense activar les heurístiques de detecció de **Rayhunter**
- **Explotació de la segmentació de xarxa**: les capacitats de segmentació de xarxa 5G podrien fer-se servir per vigilar sense que **Rayhunter** ho detectés

#### Funcions de seguretat 5G millorades
Les xarxes 5G incorporen **mesures de seguretat millorades** que podrien reduir l'eficàcia de les tècniques de vigilància tradicionals:

- **Protocols de xifratge més forts**: el 5G aplica estàndards de xifratge més robustos i difícils de trencar que els de generacions anteriors
- **Procediments d'autenticació millorats**: l'autenticació més sòlida dels dispositius a les xarxes 5G pot dificultar la recopilació d'IMSI
- **Supervisió de la seguretat de la xarxa**: la infraestructura 5G inclou millors capacitats de detecció d'intrusions per identificar i contrarestar intents de vigilància

#### Canvis en el comportament dels dispositius
A mesura que el 5G s'estén, **el comportament dels dispositius mòbils pot canviar** i afectar la detecció de **Rayhunter**:

- **Menys predisposició a baixar de xarxa**: les futures actualitzacions de programari dels dispositius podrien resistir millor els atacs de baixada quan millori la cobertura 5G
- **Preferència per connexions 5G**: els dispositius poden prioritzar cada vegada més les connexions 5G i desconfiar de sol·licituds d'ús de protocols antics
- **Més consciència de seguretat**: els sistemes operatius mòbils poden incorporar una millor detecció de comportaments de xarxa sospitosos

### Consideracions estratègiques per desplegar Rayhunter

#### Recomanacions de desplegament actuals
Per als desplegaments actuals i a curt termini, **Rayhunter** ofereix **capacitats completes de detecció de vigilància**:

- **Desplegaments urbans**: fins i tot a grans ciutats amb una cobertura 5G extensa, **Rayhunter** detecta intents de vigilància dirigits a xarxes 4G/LTE
- **Protecció d'esdeveniments crítics**: en protestes, reunions sensibles o activitats de risc elevat, **Rayhunter** ofereix capacitats de detecció essencials, hi hagi cobertura 5G o no
- **Seguretat durant els viatges**: **Rayhunter** continua sent molt eficaç per detectar vigilància en viatges nacionals i internacionals
#### Estratègies per preparar-se per al futur
Les organitzacions i les persones que planifiquin una detecció de vigilància a llarg termini haurien de tenir en compte:

- **Enfocaments de detecció híbrids**: combinar **Rayhunter** amb altres eines de seguretat i tècniques de supervisió ofereix una cobertura completa de diversos vectors d'amenaça
- **Actualitzacions periòdiques de l'avaluació d'amenaces**: vigilar l'evolució de la tecnologia de vigilància ajuda a decidir quan complementar o substituir les capacitats de **Rayhunter**
- **Suport al desenvolupament de la comunitat**: donar suport al desenvolupament de codi obert de **Rayhunter** augmenta les possibilitats que s'afegeixin funcions de detecció 5G en futures versions

#### Seguiment de l'evolució tecnològica
La comunitat **Rayhunter** i l'EFF continuen investigant les **capacitats per detectar vigilància 5G**:

- **Recerca d'anàlisi de protocols**: la recerca continuada sobre protocols 5G pot identificar noves oportunitats de detecció per a futures versions de **Rayhunter**
- **Estudis de compatibilitat de maquinari**: avaluar si es poden millorar els dispositius actuals compatibles amb **Rayhunter** per detectar intents de vigilància 5G
- **Seguiment del panorama d'amenaces**: seguir el desenvolupament i el desplegament d'equips de vigilància 5G ajuda a establir les prioritats futures de desenvolupament de **Rayhunter**

**Rayhunter** continua sent una **eina essencial per detectar vigilància** en el panorama actual de les telecomunicacions. S'espera que segueixi sent rellevant durant uns quants anys mentre avança gradualment el desplegament del 5G i els actors d'amenaça continuen utilitzant mètodes de baixada provats.

### Tornar a analitzar gravacions

**Rayhunter** millora contínuament les seves capacitats de detecció. Pots tornar a analitzar gravacions antigues amb les heurístiques actualitzades: fes clic a «N warnings» a la interfície web i selecciona «re-analyze».

### Anàlisi en un ordinador

Per als usuaris avançats, **Rayhunter** inclou `rayhunter-check`, una eina CLI per analitzar fitxers PCAP i QMDL en un ordinador:

```bash
rayhunter-check -p ~/Downloads/myfile.qmdl
rayhunter-check -p ~/Downloads/myfile.pcap
rayhunter-check -d -p ~/Downloads/myfile.qmdl  # Mode de depuració
```

## Dispositius compatibles

**Rayhunter** és compatible amb diversos punts d'accés mòbils amb mòdems Qualcomm que exposen la interfície `/dev/diag`.

{{< figure src="/img/rayhunter-device-regions.svg" alt="Compatibilitat dels dispositius Rayhunter segons la regió" caption="Compatibilitat de dispositius i recomanacions regionals per instal·lar Rayhunter" >}}

### Dispositius recomanats

Aquests dispositius s'han provat àmpliament i es fan servir molt a la comunitat **Rayhunter**:

#### Orbic RC400L (de vegades comercialitzat com a Kajeet RC400L)
- **Regió recomanada**: Amèrica
- **Bandes compatibles**:
  - 5G: n260/n261, n77, n2/5/48/66
  - 4G: 2/4/5/12/13/48/66
  - Mundial i itinerància: n257/n78
- **Disponibilitat**: **[Orbic RC400L Rayhunter nou](https://stscollective.com/products/new-rayhunter-orbic-rc400l-imsi-catcher-detector-premium?variant=51361976811822)** i **[Kajeet RC400L](https://stscollective.com/products/rayhunter-imsi-catcher-detector-kajeet-rc400lx-4g-lte-hotspot?variant=51411271844142)**. Hi ha dispositius compatibles.
- **Interval de preus**: STS Collective ofereix models professionals

#### TP-Link M7350
- **Regió recomanada**: Àfrica, Europa i Orient Mitjà (també funciona a Amèrica, però normalment és més car)
- **Requisits especials**: cal una targeta SD amb format FAT per desar gravacions
- **Disponibilitat**: **[TP-Link M7350 amb Rayhunter](https://stscollective.com/collections/rayhunter)**. Hi ha models compatibles verificats.

### Dispositius funcionals

S'ha confirmat que **Rayhunter** també funciona amb aquests dispositius:

- **Wingtech CT2MHS01** (Amèrica) - **[Rayhunter a la venda](https://stscollective.com/collections/rayhunter)**
- **Tmobile TMOHS1** (Amèrica) - **[Rayhunter a la venda](https://stscollective.com/collections/rayhunter)**
- **TP-Link M7310** (Àfrica, Europa i Orient Mitjà) - **[Rayhunter a la venda](https://stscollective.com)**
- **PinePhone i PinePhone Pro** (global) - **[Rayhunter a la venda](https://stscollective.com)**
- **FY UZ801** (Àsia i Europa) - **[Rayhunter a la venda](https://stscollective.com)**
- **Punt d'accés Moxee** (Amèrica) - **[Moxee K779HSDL Rayhunter](https://stscollective.com/products/rayhunter-imsi-catcher-stingray-detector-moxee-k779hsdl-hotspot-professionally-refurbished-pre-installed-4g-lte-cellular-threat-detection-device?variant=51309010420014)**

### Notes d'instal·lació per dispositiu

#### Orbic/Kajeet RC400L
L'Orbic RC400L és el dispositiu original per al qual es va desenvolupar **Rayhunter**. STS Collective l'ofereix **[amb Rayhunter](https://stscollective.com)**.

**Mètodes d'instal·lació**:
- **Per xarxa**: `./installer orbic` (recomanat, funciona per WiFi)
- **Per USB**: `./installer orbic-usb` (proporciona accés a ADB i a l'intèrpret d'ordres root)

**Contrasenyes per defecte**:
- **Verizon RC400L**: la contrasenya d'administrador sempre és la mateixa que la de WiFi (es troba al menú del dispositiu)
- **Kajeet/Smartspot RC400L**: `$m@rt$p0tc0nf!g`
- **Dispositius Moxee**: la contrasenya té el format `12$XXX`, on XXX són els 3 darrers dígits de la contrasenya WiFi (consulta la contrasenya WiFi sota la bateria)

**Accés a l'intèrpret d'ordres**: després de la instal·lació, fes servir `./installer util orbic-shell`.

#### TP-Link M7350/M7310
Aquests dispositius funcionen de manera fiable amb **Rayhunter** i estan disponibles **[amb Rayhunter](https://stscollective.com)**.

**Instal·lació**: `./installer tplink` (no cal contrasenya d'administrador)
**Emmagatzematge**: insereix una targeta SD amb format FAT abans d'instal·lar
**Accés a l'intèrpret d'ordres**: `./installer util tplink-shell`

#### Dispositius especialitzats

**PinePhone i PinePhone Pro**: compatibilitat global, disponibles **[amb Rayhunter](https://stscollective.com)**
**UZ801**: popular a les regions d'Àsia i Europa, disponible **[amb Rayhunter](https://stscollective.com)**
**Wingtech CT2MHS01**: dispositiu orientat a Amèrica, disponible **[amb Rayhunter](https://stscollective.com)**

### Afegir dispositius nous

**Rayhunter** podria ser compatible amb qualsevol dispositiu que tingui un mòdem Qualcomm i exposi `/dev/diag`. Si vols que **Rayhunter** sigui compatible amb el teu dispositiu, inicia una conversa al repositori oficial de GitHub.

## Documentació de l'API REST

**Rayhunter** ofereix una API REST completa per accedir programàticament a l'estat, les gravacions i la configuració del dispositiu. L'API permet integrar-lo amb altres eines de seguretat i sistemes de supervisió automatitzats.

### Documentació oficial de l'API

Per consultar tota la referència de l'API, amb especificacions detallades dels endpoints, exemples de peticions i respostes i mètodes d'autenticació, visita la **[documentació oficial de l'API REST de Rayhunter](https://efforg.github.io/rayhunter/api-docs/)**.

### Punts d'accés de l'API

Es pot accedir a l'API de **Rayhunter** a `http://[device-ip]:8080/api/` i inclou punts d'accés per a:

- **Estat del sistema**: supervisar l'estat del dispositiu i el funcionament de **Rayhunter**
- **Gestió de gravacions**: iniciar, aturar i baixar gravacions
- **Obtenció d'alertes**: consultar alertes de detecció i resultats de l'anàlisi
- **Configuració**: actualitzar programàticament els paràmetres de **Rayhunter**
- **Control d'heurístiques**: activar o desactivar algorismes de detecció concrets
- **Informació del dispositiu**: obtenir especificacions i capacitats del dispositiu
- **Supervisió de xarxa**: accedir a dades de xarxa mòbil en temps real
- **Registre d'esdeveniments**: consultar esdeveniments i alertes de detecció anteriors

### Autenticació

L'accés a l'API fa servir la mateixa autenticació que la interfície web. Assegura't que el dispositiu **Rayhunter** estigui protegit correctament i que només hi puguin accedir usuaris autoritzats.

### Exemples d'integració

L'API REST de **Rayhunter** es pot integrar amb diverses plataformes de supervisió de seguretat, sistemes SIEM i eines d'automatització personalitzades. Consulta la **[documentació oficial de l'API](https://efforg.github.io/rayhunter/api-docs/)** per veure exemples complets d'implementació i bones pràctiques.

## Resolució de problemes

### Problemes habituals d'instal·lació

**Problemes de connexió USB**: prova altres cables o ports USB. Les connexions USB defectuoses sovint fan que falli la instal·lació. *És la causa més habitual de les instal·lacions fallides.*

**Problemes de seguretat a macOS**: si veus «No Orbic device found», canvia temporalment a «Always» l'opció «Allow accessories to connect» dels paràmetres de seguretat.

**Detecció del dispositiu**: després de la instal·lació, activa la heurística de prova per comprovar que **Rayhunter** funciona correctament.

### Obtenir ajuda

Per rebre ajuda amb la instal·lació i la resolució de problemes:
- Consulta la documentació oficial de **Rayhunter**
- Fes servir `./installer --help` i `./installer util --help` per consultar les opcions de les ordres
- Participa en les converses de GitHub per obtenir suport de la comunitat
- Contacta amb **[STS Collective](https://stscollective.com)** si tens preguntes sobre compatibilitat de dispositius

## Preguntes freqüents (FAQ)

### Preguntes generals

#### Què és exactament un captador d'IMSI i com funciona?
Un captador d'IMSI (també anomenat StingRay, simulador de cel·la mòbil o falsa torre mòbil) és un equip de vigilància que imita les torres mòbils legítimes per interceptar comunicacions de dispositius mòbils. Força els dispositius propers a connectar-se a l'equip maliciós en lloc de fer-ho a torres legítimes, cosa que permet als operadors recopilar identificadors de dispositiu (números IMSI), dades d'ubicació i metadades de trucades, i possiblement interceptar comunicacions. **Rayhunter** detecta aquests dispositius identificant patrons anormals en el comportament de la xarxa mòbil.

#### Rayhunter pot detectar tots els tipus d'equips de vigilància?
**Rayhunter** detecta específicament IMSI catchers i simuladors de cel·les mòbils en xarxes 2G, 3G i 4G/LTE. No pot detectar altres tipus de vigilància, com ara la supervisió WiFi, dispositius de seguiment GPS, vigilància física o vigilància 5G nativa que no utilitzi atacs de baixada. **Rayhunter** és un component d'una estratègia completa de protecció de la privadesa.

#### És legal fer servir Rayhunter?
En la majoria de jurisdiccions és completament legal fer servir **Rayhunter**, perquè és una eina de supervisió passiva que no interfereix amb xarxes mòbils ni altres dispositius. Només analitza els senyals mòbils que el dispositiu rep de manera natural. Tot i això, les lleis locals varien, així que els usuaris haurien de comprovar la normativa de la seva zona. L'EFF va desenvolupar **Rayhunter** com una eina legítima de protecció de la privadesa.

### Preguntes tècniques

#### Per què Rayhunter necessita una SIM si no cal un pla de servei actiu?
La targeta SIM conté la identitat internacional de subscriptor mòbil (IMSI) que el dispositiu necessita per autenticar-se a les xarxes mòbils i participar en els intercanvis de protocol que **Rayhunter** supervisa. Sense SIM, el dispositiu no es pot connectar a xarxes mòbils i **Rayhunter** no tindria cap activitat de xarxa per analitzar a la recerca de patrons sospitosos.

#### Quantes dades consumeix Rayhunter durant el funcionament normal?
**Rayhunter** consumeix poques dades en la supervisió bàsica, perquè principalment analitza informació dels protocols mòbils i no pas trànsit d'Internet. Tanmateix, si actives les notificacions remotes per ntfy o fas servir el dispositiu com a punt d'accés alhora, el consum de dades augmentarà. La supervisió per si sola consumeix una amplada de banda insignificant.

#### Puc fer servir Rayhunter mentre el dispositiu és un punt d'accés mòbil?
Sí, **Rayhunter** pot funcionar alhora que el dispositiu serveix de punt d'accés mòbil. Cal tenir un pla de servei mòbil actiu. La supervisió de **Rayhunter** funciona independentment del punt d'accés, però fer servir totes dues funcions alhora consumeix més bateria.

#### Quina diferència hi ha entre instal·lar per WiFi i per USB?
El **mètode WiFi** (recomanat per a la majoria d'usuaris) instal·la **Rayhunter** per la interfície sense fil del dispositiu i ofereix les funcions habituals. El **mètode USB** activa l'accés a Android Debug Bridge (ADB) per als usuaris avançats que necessiten funcions de depuració, però és més complex i no cal per a les instal·lacions normals.

### Preguntes sobre dispositius i compatibilitat

#### Per què Rayhunter només és compatible amb alguns dispositius?
**Rayhunter** necessita dispositius amb mòdems Qualcomm que exposin la interfície `/dev/diag`, que proporciona accés a informació dels protocols mòbils. La majoria de dispositius de consum no exposen aquesta interfície per motius de seguretat. Els dispositius compatibles s'han provat específicament i s'ha confirmat que compleixen els requisits de **Rayhunter**.

#### Puc instal·lar Rayhunter en un telèfon intel·ligent normal?
No, **Rayhunter** no es pot instal·lar en telèfons intel·ligents normals. Necessita punts d'accés mòbils especialitzats amb mòdems Qualcomm concrets que exposin interfícies de diagnòstic. Entre els dispositius compatibles hi ha l'Orbic RC400L, el TP-Link M7350 i diversos altres models de punt d'accés mòbil.

#### Què passa si intento instal·lar Rayhunter en un dispositiu incompatible?
L'instal·lador de **Rayhunter** detecta el dispositiu i normalment es nega a instal·lar-se en maquinari incompatible. Si forces la instal·lació en dispositius no compatibles, podries fer-los malbé o deixar-los inoperatius. Comprova sempre la compatibilitat abans d'intentar instal·lar-lo.

#### Necessito dispositius diferents per a cada regió?
Sí, les bandes de freqüència mòbil varien segons la regió geogràfica. L'Orbic RC400L està optimitzat per a les xarxes d'Amèrica, mentre que el TP-Link M7350 funciona bé a Europa, Àfrica i Orient Mitjà. La informació de compatibilitat de **Rayhunter** inclou recomanacions regionals per garantir un rendiment òptim a la teva ubicació.

### Preguntes sobre l'ús i la configuració

#### Com sé si el dispositiu Rayhunter funciona correctament?
Activa la heurística de prova als paràmetres de configuració de **Rayhunter**. Això generarà alertes cada vegada que el dispositiu detecti una cel·la i confirmarà que el sistema funciona. Durant el funcionament normal, la pantalla hauria de mostrar una línia verda. Recorda desactivar la heurística de prova després de verificar-ho perquè genera moltes alertes.

#### Què he de fer si Rayhunter genera una alerta?
Quan **Rayhunter** detecti activitats sospitoses, primer apunta la ubicació i les circumstàncies. Poden produir-se falsos positius per l'optimització de la xarxa o problemes amb els equips. Si les alertes continuen a la mateixa ubicació o durant activitats sensibles, planteja't canviar de lloc i revisar-ne els detalls a la interfície web per entendre què s'ha detectat.

#### Cada quant hauria d'actualitzar Rayhunter?
**Actualitza'l cada mes.** Consulta la pàgina de versions per trobar noves heurístiques i millores de compatibilitat, que s'afegeixen sovint. L'EFF millora contínuament les capacitats de **Rayhunter** d'acord amb l'evolució de les tècniques de vigilància. El procés d'actualització és igual que el de la instal·lació inicial.

#### Rayhunter pot protegir diverses persones alhora?
**Rayhunter** detecta IMSI catchers a la zona del voltant i, per tant, pot protegir diverses persones dins del seu abast (normalment uns quants centenars de metres, segons la intensitat del senyal). Tot i això, les persones que es prenen seriosament la detecció de vigilància haurien de tenir el seu propi dispositiu **Rayhunter** per obtenir la màxima protecció i control de configuració.

### Preguntes sobre seguretat i privadesa

#### Fer servir Rayhunter em fa més visible per a la vigilància?
**Rayhunter** funciona de manera passiva i no emet senyals que permetin identificar-lo als equips de vigilància. Tot i això, fer servir qualsevol eina de seguretat indica que valores la privadesa. Els avantatges de la detecció normalment superen els riscos, sobretot per a persones d'alt risc com ara periodistes i activistes.

#### Els equips de vigilància poden detectar que faig servir Rayhunter?
**Rayhunter** és un sistema de supervisió passiva que no transmet senyals d'identificació. Els operadors de vigilància no poden detectar l'ús de **Rayhunter** a nivell de protocol mòbil. L'observació física del dispositiu o l'anàlisi del trànsit de xarxa podrien revelar que fas servir **Rayhunter** si tens activades les notificacions remotes.

#### Quina informació recull Rayhunter sobre mi?
**Rayhunter** analitza informació dels protocols mòbils i desa localment les alertes de detecció al dispositiu. No recull informació personal, contingut de comunicacions ni dades d'ubicació més enllà del que necessiten els algorismes de detecció. Totes les dades es queden al dispositiu si no actives les notificacions remotes.

### Preguntes avançades

#### Puc analitzar les dades de Rayhunter a l'ordinador?
Sí, **Rayhunter** inclou l'eina de línia d'ordres `rayhunter-check` per analitzar fitxers PCAP i QMDL gravats en ordinadors. Això permet als usuaris avançats analitzar detalladament esdeveniments de detecció i investigar activitats sospitoses amb tots els recursos de l'ordinador.

#### Com funciona Rayhunter en zones urbanes denses?
Les zones urbanes denses tenen moltes cel·les legítimes i poden augmentar els falsos positius perquè hi ha més optimitzacions de xarxa i canvis de cel·la. Els algorismes de **Rayhunter** estan dissenyats per distingir el comportament normal de la xarxa de la vigilància, però en zones denses pot ser necessari ajustar-ne la sensibilitat.

#### Rayhunter funcionarà durant viatges internacionals?
L'eficàcia de **Rayhunter** durant els viatges depèn de la compatibilitat del dispositiu amb les bandes mòbils locals i dels acords d'itinerància. Els algorismes de detecció funcionen arreu del món, però comprova que el dispositiu admeti les bandes de freqüència utilitzades al país de destinació. Pot ser necessària la itinerància internacional per tenir totes les funcions.

{{< figure src="rayhunter-faq-privacy-protection.webp" alt="Una persona revisa alertes de Rayhunter en un ordinador portàtil mentre porta un punt d'accés mòbil en un entorn urbà amb torres mòbils a prop" >}}

______

**Rayhunter** és un avenç important en la protecció de la privadesa personal i la detecció de vigilància. Si flasheges i configures correctament **Rayhunter** en dispositius compatibles, obtens capacitats eficaces per detectar IMSI catchers i protegir les comunicacions mòbils de la vigilància no autoritzada.

Tant si ets periodista, activista, professional de la seguretat o una persona que valora la privadesa, **Rayhunter** proporciona les eines necessàries per mantenir la seguretat mòbil en un món cada vegada més vigilat. Per trobar dispositius compatibles verificats, consulta les opcions **[de Rayhunter a la venda](https://stscollective.com)** de proveïdors de confiança d'equips de seguretat.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compra dispositius Rayhunter i estalvia un 20%
{{< /centerbutton >}}

## Referències

- [Repositori oficial de Rayhunter a GitHub](https://github.com/EFForg/rayhunter)
- [Versió més recent de Rayhunter](https://github.com/EFForg/rayhunter/releases/tag/v0.10.2)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [STS Collective, proveïdor d'equips Rayhunter](https://stscollective.com)

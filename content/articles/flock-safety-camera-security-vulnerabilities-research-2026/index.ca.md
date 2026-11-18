---
title: "Vulnerabilitats de les càmeres Flock Safety: més de 50 errors descoberts"
date: 2026-05-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Aquesta recerca sobre les vulnerabilitats de les càmeres Flock Safety analitza credencials exposades, proteccions febles, accés físic i límits de divulgació."
genre: ["Recerca de seguretat", "Anàlisi de vulnerabilitats", "Tecnologia de vigilància", "Ciberseguretat", "Privadesa i seguretat", "Seguretat de l'IoT", "Seguretat física", "Seguretat de xarxes", "Infraestructura crítica", "Tecnologia governamental"]
tags: ["Vulnerabilitats de Flock Safety", "Seguretat ALPR", "Pirateria de càmeres", "Errors de seguretat de l'IoT", "Contrasenyes codificades", "Vulnerabilitats d'Android Things", "Explotació amb accés físic", "Seguretat de xarxes", "Errors de xifratge", "Infraccions de la privadesa de dades", "Divulgacions CVE", "Recerca de seguretat", "Recerca de GainSec", "Investigació de Ben Jordan", "Seguretat de càmeres de vigilància", "Errors en tecnologia governamental", "Vulnerabilitats crítiques", "Divulgació responsable", "Anàlisi de ciberseguretat", "Tecnologia policial", "Seguretat pública", "Punt d'accés sense fil", "Elusió de l'autenticació", "Credencials en text clar", "Fuita de RF", "Atac Tempest", "Divulgació d'informació", "Accés a un shell root", "Execució remota de codi", "Auditoria de seguretat", "Avaluació de vulnerabilitats", "Risc per a la seguretat nacional", "Investigació del Senat", "Programa de recompenses per errors", "Vulnerabilitat de dia zero", "Desenvolupament d'exploits", "Proves d'intrusió", "Informe tècnic de seguretat", "Cobertura de 404 Media", "Recerca independent", "Seguretat del maquinari", "Anàlisi del microprogramari", "Explotació de sistemes"]
cover: "/img/cover/flock-safety-camera-security-vulnerabilities-research-2026.webp"
coverAlt: "Una càmera de vigilància d'alta tecnologia apareix il·luminada en blau i verd sobre un fons fosc. Les formes i línies abstractes del voltant representen vulnerabilitats de seguretat digital."
coverCaption: "Errors crítics de seguretat exposen més de 80.000 càmeres de vigilància a accessos no autoritzats"
canonical: "https://simeononsecurity.com/articles/flock-safety-camera-security-vulnerabilities-research-2026/"
---

**Més de 50 vulnerabilitats crítiques exposen la xarxa privada de vigilància més gran del país**

## Introducció: una crisi de seguretat nacional

A finals de 2024 i durant tot el 2025, investigadors independents de seguretat van descobrir el que podria ser **la fallada de seguretat més important de la història de la tecnologia de vigilància policial als Estats Units**. S'han descobert més de **50 vulnerabilitats crítiques** als sistemes de càmeres de Flock Safety. Aquestes mateixes càmeres fotografien i segueixen més de **150 milions de vehicles cada dia** en més de **80.000 instal·lacions** arreu del país.

Aquest article ofereix una anàlisi tècnica completa d'aquestes vulnerabilitats, basada en:
- **L'informe tècnic oficial de GainSec**, «Examining the Security Posture of an Anti-Crime Ecosystem» (51 troballes, 22 CVE assignats i 8 pendents)
- **La recerca periodística de Ben Jordan** i les seves proves pràctiques de seguretat
- **La cobertura de 404 Media** sobre els fluxos de càmera exposats públicament
- **Les respostes oficials** de Flock Safety i dels senadors dels Estats Units
- Les divulgacions publicades a la **National Vulnerability Database** (NVD)
- **La imatge del sistema de fitxers de setembre de 2026**, publicada per Distributed Denial of Secrets, amb una anàlisi tècnica detallada de Micah Lee i una investigació conjunta de WIRED i 404 Media

Per entendre **per què existeixen aquestes càmeres** i les seves **implicacions per a la privadesa**, consulta l'article: **[Vigilància amb càmeres Flock Safety: abast, preocupacions sobre la privadesa i estratègies de protecció](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**

Per saber **com detectar aquestes càmeres**, consulta: **[Projecte de detecció Flock-You: guia de maquinari contra la vigilància](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**

______
## Abast del problema

### Dimensió de la infraestructura vulnerable

Al maig de 2026:
- **Més de 80.000 càmeres Flock Safety** desplegades als Estats Units
- **Més de 5.000 ciutats i pobles** fan servir els serveis de Flock
- **Més de 3.500 organismes policials** tenen accés al sistema
- **Més de 22.000 usuaris policials** consulten les bases de dades
- **Milers de milions de dades** emmagatzemades en bases de dades consultables

### Cronologia de les vulnerabilitats

- **Finals de 2024**: l'investigador de seguretat Jon «GainSec» Gaines descobreix les primeres vulnerabilitats
- **Febrer de 2025**: comença la divulgació responsable a Flock Safety
- **Abril de 2025**: es publiquen les primeres assignacions de CVE
- **Novembre de 2025**: es publica l'informe tècnic oficial amb 51 troballes
- **Desembre de 2025**: Ben Jordan demostra les vulnerabilitats en un vídeo
- **Gener de 2026**: 404 Media descobreix més de 60 fluxos de càmera accessibles públicament
- **Febrer de 2026**: senadors dels Estats Units demanen a la FTC que investigui
- **Maig de 2026**: el procés de divulgació continua

### Categories de vulnerabilitats

Les més de 50 vulnerabilitats pertanyen a diverses categories:
1. **Autenticació i autorització** (contrasenyes codificades, absència de MFA)
2. **Criptografia i xifratge** (dades sense xifrar en repòs i en trànsit)
3. **Seguretat de xarxes** (punts d'accés Wi-Fi exposats, credencials en text clar)
4. **Seguretat física** (explotacions activades amb un botó, ports USB exposats)
5. **Privadesa de dades** (recollida no autoritzada, retenció prolongada)
6. **Disseny del sistema** (programari obsolet, controls d'accés insuficients)
7. **Divulgació d'informació** (claus API exposades, fluxos públics de càmera)


______
## Imatge del sistema de fitxers de setembre de 2026

**El setembre de 2026, l'entitat sense ànim de lucre Distributed Denial of Secrets, dedicada a la transparència, va publicar imatges completes del sistema de fitxers d'una càmera Flock en servei.** Un col·lectiu que es fa dir **stegan0gram** va descargolar el maquinari del pal, va copiar l'emmagatzematge intern i en va publicar les imatges. **404 Media** i **WIRED** van fer una investigació conjunta, i l'investigador de seguretat **Micah Lee** va publicar una anàlisi tècnica del contingut.

Totes les troballes anteriors d'aquest article provenien d'un dispositiu de laboratori d'un investigador o d'una unitat comprada. Aquest conjunt de dades prové d'una càmera en servei municipal actiu, de manera que és l'evidència més sòlida publicada fins ara.

*La càmera no va ser compromesa a través de la xarxa. La van retirar físicament.*

### Què conté la imatge

La publicació inclou imatges de tres particions, i cadascuna revela una part diferent del problema.

| Partició | Mida | Per què importa |
|-----------|--------|----------------|
| **system** | 1,5 GB | Imatge del sistema Android amb **19 aplicacions creades per Flock**, entre elles `flock-sambuca`, `flock-collins` i `flock-phone-home` |
| **persist** | 32 MB | Credencials del dispositiu a `flock/auth0/auth0_cred`, en una **partició sense xifrar dissenyada per sobreviure a un restabliment de fàbrica** |
| **media** | 18 GB | Registres i imatges dins d'un contenidor la **clau de desxifrat del qual es desa a la mateixa partició** |

### El problema de les credencials, confirmat

La imatge resol el dubte de si les credencials codificades directament al programari són teòriques o s'han desplegat. S'han desplegat.

**Una clau API que dona accés al backend de Flock està codificada als binaris de les aplicacions.** El valor és a una classe anomenada `CameraSettings` dins de `com.flocksafety.android.common.lib`. Flock inclou la biblioteca compartida a les seves 19 aplicacions, per tant la clau s'envia dins de cadascuna. L'aplicació `flock-sambuca` la fa servir durant l'aprovisionament.

**El flux d'autenticació funciona així:**

1. Cada càmera demana credencials a un servidor de Flock i s'identifica amb la seva **adreça MAC**
2. El servei d'inici de sessió **Okta Auth0** de Flock retorna un `FlockAuth0Token` de curta durada
3. La càmera desa les credencials rebudes **en text clar**

L'identificador i el secret del client Auth0 són a la partició **`/persist` sense xifrar**, dins d'un fitxer dissenyat per sobreviure a un restabliment de fàbrica. Un atacant recupera primer la partició persist, perquè res no la protegeix.

La [Vulnerabilitat crítica núm. 4](#critical-vulnerability-4-hardcoded-credentials-throughout-system) tracta el patró més ampli de secrets codificats a tota la plataforma.

### La clau de xifratge inclosa amb el pany

Flock descriu les seves càmeres com a dispositius protegits amb **xifratge local**. La imatge mostra com s'implementa a la pràctica.

La partició media de 18 GB és dins d'un contenidor xifrat. La clau de desxifrat és a la mateixa partició, en un fitxer el nom del qual acaba en `.key`. El col·lectiu stegan0gram va recuperar la clau, va desbloquejar el contenidor i en va llegir el contingut. **Les imatges estan xifrades tant com ho està una capsa tancada si la clau va enganxada a la tapa.**

Els registres recuperats també van revelar la posició de la mateixa càmera. Les coordenades GPS apareixen **155 vegades** als registres, agrupades en un radi d'uns 100 metres, una deriva habitual d'un receptor fixat a un pal. Les coordenades corresponen a **Wauwatosa, Wisconsin**, un suburbi de Milwaukee on la càmera estava instal·lada a N Mayfair Road. Micah Lee va comparar els registres amb Google Street View i va identificar la unitat concreta pel número de sèrie i l'adreça MAC.

*El xifratge en repòs no serveix de res si la clau es desa al costat del text xifrat.*

### Què va dir Flock

La resposta de Flock va reiterar la seva postura sobre les troballes anteriors de GainSec. Un portaveu va declarar:

> «Flock es pren seriosament la seguretat i manté una política pública de divulgació de vulnerabilitats perquè els investigadors ens comuniquin directament possibles errors. No vam rebre cap notificació mitjançant aquest procés i, amb la informació limitada que s'ha proporcionat, no tenim prou detalls per avaluar les afirmacions.»

Aquesta resposta costa de conciliar amb la cronologia. Les vulnerabilitats del sistema operatiu de la càmera es van corregir públicament el **2018 i el 2021**, i els estàndards d'emmagatzematge de credencials i gestió de claus no han canviat des de molt abans que s'enviés la càmera. **Revisar una dècada d'historial públic de vulnerabilitats no requereix cap informe extern.**

Flock també va qualificar d'il·legal la retirada i l'anàlisi de la càmera, com ho són segons la legislació actual. Les troballes de seguretat continuen sent vàlides independentment de com es va obtenir el maquinari.

### Per què importa més que la recerca anterior

L'informe tècnic de GainSec documentava 51 troballes en dispositius obtinguts legalment. Flock en va qüestionar la gravetat i va argumentar que calia proximitat física per accedir-hi.

Aquesta imatge elimina aquestes reserves. L'estat per defecte d'una càmera de producció, sense modificacions dels seus operadors, inclou credencials d'infraestructura en text clar, claus desades al costat de les dades que protegeixen i un sistema operatiu sense vuit anys d'actualitzacions de seguretat. **No calia cap explotació. Només una clau anglesa.**


______
## La flota de dispositius

Flock ven una línia de productes, no una sola càmera, i les propietats de seguretat varien segons el dispositiu. Les especificacions següents provenen dels desmuntatges de GainSec i de l'anàlisi del microprogramari recopilada per la comunitat d'investigació **[WiFi Mothership](https://wifimothership.com/flock)**.

| Dispositiu | Funció | Plataforma | SO |
|--------|----------|----------|-----|
| **Falcon** | Càmera ALPR amb alimentació solar | Qualcomm MSM8953 (Snapdragon 625) / OpenQ 624A SoM | Android 8.1 |
| **Sparrow** | Càmera ALPR amb alimentació per cable | Igual que Falcon | Android 8.1 |
| **Raven** | Detecció d'àudio de trets i senyals d'auxili | ESP32-WROOM-32D amb DSP Syntiant NDP120-B0 | FreeRTOS / ESP-IDF |
| **Bravo** | Caixa d'informàtica d'IA perifèrica | Qualcomm QCS6490 / TurboX QCS6490-U8B | **Android 13, nucli 5.4.180** |
| **Picard** | Caixa d'informàtica antiga | Retirada en favor de Bravo | |
| **Condor** | Càmera PTZ | Documentació incompleta | |
| **Alpha** | Dró autònom | Disseny de Flock, conforme amb la NDAA | Pilot automàtic propietari |
| **Aerodome M350** | Dró antic | DJI Matrice M350 / M300 RTK | Microprogramari DJI |
| **Remolc LPR (ATS-5)** | Plataforma ALPR mòbil | Xassís d'All Traffic Solutions amb una càmera Flock | Igual que Falcon |
| **Wing** | Pont de programari per a càmeres de tercers | Cap, integra càmeres IP existents | |

*El salt generacional és el primer aspecte que cal observar. La caixa d'informàtica executa Android 13, mentre que les càmeres que atén funcionen amb Android 8.1, un sistema operatiu publicat el 2017.*

**Falcon és el dispositiu que cal vigilar.** Gestiona la càrrega ALPR, continua amb Android 8.1 i desa dades en una **eMMC de 32 GB sense xifrar**. En aquesta mateixa eMMC hi havia els fitxers multimèdia i els registres recuperats pel col·lectiu stegan0gram. Sparrow fa servir la mateixa plataforma, però amb alimentació per cable.

**Bravo és el cas oposat.** Una caixa d'informàtica moderna amb Android 13 i inferència d'IA per als fluxos de càmera demostra que l'empresa està disposada a distribuir programari actual quan ho decideix.

## Identificadors CVE verificats

S'han assignat quinze CVE a les famílies Falcon, Sparrow, Raven i Bravo. Cada identificador següent es va verificar amb el seu **registre a CVE.org** el setembre de 2026, en lloc de citar una font secundària.

### Dispositius de detecció de trets i d'àudio

| CVE | Troballa | CVSS |
|-----|---------|------|
| **CVE-2025-47818** | Contrasenya de connexió codificada directament | 2.2 |
| **CVE-2025-47819** | Interfície de depuració integrada al xip amb control d'accés inadequat | 6.4 |
| **CVE-2025-47820** | Emmagatzematge de codi en text clar | 2.0 |
| **CVE-2025-47821** | Contrasenya del sistema codificada directament | 2.2 |

Les quatre afecten els dispositius de detecció de trets **anteriors a la versió 1.3**.

### Lectors de matrícules

| CVE | Troballa | CVSS |
|-----|---------|------|
| **CVE-2025-47822** | Interfície de depuració integrada al xip amb control d'accés inadequat | 6.4 |
| **CVE-2025-47823** | Contrasenya del sistema codificada directament | 2.2 |
| **CVE-2025-47824** | Emmagatzematge de codi en text clar | 2.0 |

Aquestes tres afecten el microprogramari dels lectors de matrícules **fins a la versió 2.2 inclosa**.

### Defectes de les aplicacions presents a tota la flota

| CVE | Troballa | CVSS |
|-----|---------|------|
| **CVE-2025-59403** | L'aplicació Collins exposa endpoints d'administració al **port 8080 sense autenticació**: `/reboot`, `/logs`, `/crashpack` i `/adb/enable`. L'últim inicia ADB sobre TCP sense confirmació de depuració i ofereix un shell a qualsevol atacant de la mateixa xarxa | **9.8 CRÍTICA** |
| **CVE-2025-59407** | L'aplicació DetectionProcessing incorpora un magatzem de claus Java amb la seva **contrasenya codificada directament**, i el magatzem conté una clau privada | **9.8 CRÍTICA** |
| **CVE-2025-59405** | L'aplicació Peripheral conté una clau API de DataDog en text clar | 7.5 |
| **CVE-2025-59409** | El microprogramari de producció de Falcon i Sparrow s'envia amb **credencials WiFi de desenvolupament en text clar** | 7.5 |
| **CVE-2025-59406** | L'aplicació Pisco incorpora un **secret de client Auth0** en text clar | 6.2 |

### Caixa d'informàtica Bravo

| CVE | Troballa | CVSS |
|-----|---------|------|
| **CVE-2025-59402** | Accepta el carregador Firehose per defecte de Thundercomm TurboX 6490, cosa que permet instal·lar microprogramari i bolcar particions | 5.4 |
| **CVE-2025-59404** | S'envia amb el carregador d'arrencada desbloquejat, de manera que es pot eludir Android Verified Boot | 7.5 |
| **CVE-2025-59408** | S'envia amb Secure Boot desactivat | 7.3 |

**Quatre d'aquests problemes tenen un vector d'atac de xarxa amb una puntuació de 7.5 o superior, de manera que no requereixen accés físic.** CVE-2025-59403 és l'identificador assignat al camí API sense autenticació i inclou la crida `/adb/enable`, que [la vulnerabilitat crítica núm. 1](#critical-vulnerability-1-button-press-wireless-access-point) necessita per obtenir un shell root.

*Els registres CVE importen per un segon motiu. Confirmen el problema dels secrets en text clar mitjançant registres independents, i la pàgina d'alertes de seguretat de Flock figura com a referència a les entrades de Raven i LPR.*

______
## Vulnerabilitat crítica núm. 1: punt d'accés sense fil activat prement un botó {#critical-vulnerability-1-button-press-wireless-access-point}

### CVE-2025-59403

**Gravetat**: CRÍTICA (CVSS 9.8)

### L'explotació

La vulnerabilitat més alarmant permet que **qualsevol persona amb accés físic** a una càmera Flock Safety n'obtingui el control complet en menys de 60 segons:

**Pas 1**: prem **tres vegades** el botó de la part posterior de la càmera Falcon/Sparrow  
**Pas 2**: el dispositiu crea un punt d'accés WiFi obert  
**Pas 3**: connecta't a la xarxa WiFi (contrasenya codificada directament: documentada al document tècnic de GainSec)  
**Pas 4**: envia l'ordre per activar ADB (Android Debug Bridge)  
**Pas 5**: connecta't per ADB i obtén accés a un shell root

### Detalls tècnics

```
Dispositiu: càmera ALPR Flock Safety Falcon/Sparrow
Maquinari: Android Things 8.0/8.1 (suport finalitzat el 2021)
Vector d'atac: seqüència de pressions físiques del botó
Autenticació: contrasenya WiFi codificada (igual a tots els dispositius)
Impacte: control total del dispositiu, extracció de dades i instal·lació de programari maliciós
```

### Què permet fer

Un cop obtingut l'accés al shell, un atacant pot:
- **Extreure totes les imatges emmagatzemades** (incloses les de persones, no només les de vehicles)
- **Modificar o esborrar proves** desades al dispositiu
- **Instal·lar programari maliciós persistent** (sobreviu als reinicis)
- **Clonar la identitat del dispositiu** per suplantar-lo
- **Interceptar i modificar** els fluxos de vídeo
- **Fer servir el dispositiu com a client d'una botnet** per a atacs DDoS
- **Capturar credencials WiFi** de dispositius propers (atacs amb honeypot)
- **Desactivar la càmera** o provocar una denegació de servei

### Demostració

L'investigador de seguretat Ben Jordan va demostrar aquesta explotació a YouTube i va mostrar:
- Connexió al punt d'accés WiFi en **menys de 30 segons**
- Obtenció d'un shell root en **menys de 60 segons en total**
- Accés complet al sistema de fitxers, a les imatges desades i a la memòria del sistema
- Capacitat d'instal·lar aplicacions Android arbitràries

**Citació de la demostració**:
> «La contrasenya d'aquest punt d'accés és [REDACTED], tot en minúscules. Totes les càmeres que hem provat tenen aquesta mateixa contrasenya codificada. Després només cal enviar una ordre per activar ADB... probablement en menys de 30 segons pots obrir completament un shell al dispositiu i tenir-hi accés total.»

### Resposta del proveïdor

Al principi, Flock Safety va afirmar que la vulnerabilitat només afectava **dispositius no connectats al núvol** i els va comparar amb **«un iPhone robat d'un camió abans de connectar-lo»**.

*Aquesta afirmació es va desmentir.* Els investigadors van reproduir la vulnerabilitat **en dispositius connectats al núvol**, en diversos models de càmera amb **la mateixa vulnerabilitat** i en dispositius obtinguts de **fonts diferents**. Tots presentaven el defecte.

______
## Vulnerabilitat crítica núm. 2: sistema operatiu Android obsolet

### CVE-2025-47822 a CVE-2025-47824

**Gravetat**: de MITJANA a BAIXA (CVSS 6.4, 2.2 i 2.0)

### El problema

Les càmeres Flock Safety funcionen amb **Android Things 8.0 o 8.1**, que:
- **Google va deixar de mantenir el 2021**
- **No rep actualitzacions de seguretat des del 2021**
- Té **més de 900 vulnerabilitats publicades** el 2026
- Fa **més de cinc anys que no té suport**

### Anàlisi tècnica

**Sistema operatiu**: Android Things 8.0/8.1  
**Fi de vida útil**: gener de 2021  
**Vulnerabilitats conegudes**: més de 900  
**Pedaços de seguretat**: cap des del final de vida útil  
**Dispositius afectats**: càmeres Falcon, Sparrow i Condor, i caixes d'informàtica Bravo

### Què mostra el bolcat de setembre de 2026

Les imatges del sistema de fitxers publicades el setembre de 2026 indiquen les versions exactes d'una càmera en servei, no pas d'una unitat de laboratori.

| Element | Versió a la càmera | Estat |
|-----------|----------------------|--------|
| **Android** | 8.1, compilació datada el 5 de juny de 2025 | Nivell de pedaç de seguretat **2018-06-05** |
| **Nucli Linux** | 3.18.71 | Publicat el 2017, i la sèrie 3.18 va acabar a 3.18.140 el maig de 2019 |
| **Versió actual d'Android** | Android 17, juny de 2026 | Nou versions principals més recent |

La compilació de la càmera és recent. **El sistema operatiu que hi ha a sota no ho és**, i el nivell de pedaç indica que el dispositiu no ha rebut actualitzacions de seguretat d'Android en **vuit anys**. El nucli té **69 versions de pedaç de retard** respecte del final de la seva pròpia branca de manteniment, és a dir, més de nou anys sense correccions.

### Dues vulnerabilitats presents en aquesta compilació

Micah Lee va identificar dos defectes coneguts públicament que afecten components inclosos a la càmera. Les dates dels pedaços demostren que la càmera precedeix totes dues correccions.

| CVE | Element | Efecte | Corregit |
|-----|-----------|--------|---------|
| **CVE-2021-1905** | Controlador de GPU Qualcomm Adreno | Ús després d'alliberament que permet **a qualsevol codi del dispositiu, incloses aplicacions sense privilegis, corrompre la memòria del nucli i prendre'n el control complet** | maig de 2021 |
| **CVE-2018-9568** «WrongZone» | Gestió de sòcols del nucli Linux | Confusió de tipus sobre IPv6 que permet a un programa **escalar privilegis fins a root**. Hi ha codi d'explotació públic | desembre de 2018 |

Totes dues es van corregir anys abans de compilar el microprogramari d'aquesta càmera. **Cap no depèn de l'accés físic, perquè el programari que ja s'executa al dispositiu hi pot accedir.** L'excusa de proximitat física que Flock va fer servir per restar importància a les troballes de GainSec no s'aplica a cap de les dues.

### Comparació amb dispositius de consum

Per posar-ho en perspectiva:
- El **telèfon intel·ligent** deixa de rebre actualitzacions al cap d'uns cinc anys i els fabricants **deixen de vendre'l**
- Una **càmera de seguretat domèstica** amb programari de fa cinc anys es consideraria **críticament insegura**
- Les agències governamentals exigeixen **programari actualitzat i compatible** per als sistemes sensibles

*Tot i això, Flock Safety continua distribuint i venent càmeres amb programari sense suport del proveïdor, sense pedaços de seguretat i amb centenars d'exploits coneguts, que processen dades sensibles de les forces de l'ordre.*

### Per què importa

Executar **programari fora de servei** en dispositius de vigilància implica que:
- **Qualsevol vulnerabilitat publicada d'Android 8.x** funciona en aquestes càmeres
- **Hi ha codi d'explotació públic** per a moltes vulnerabilitats
- **Cap pedaç no corregirà mai** els problemes que es descobreixin en el futur
- És impossible assolir el **compliment normatiu** (FISMA, NIST, CMMC)

______
## Vulnerabilitat crítica núm. 3: manca de xifratge durant l'execució {#critical-vulnerability-3-lack-of-encryption-at-runtime}

### CVE-2025-47824 i CVE-2025-59407

**Gravetat**: d'ALTA a CRÍTICA (CVSS 2.0 a 9.8)

### Les afirmacions de Flock Safety i la realitat

**El lloc web de Flock Safety diu**:
> «Les dades i les imatges estan xifrades durant tot el cicle de vida.»

**Les troballes de la recerca independent** (GainSec i Ben Jordan):
> «En tota la nostra recerca, no hem desxifrat ni trencat res. Tot estava sense xifrar durant l'execució.»

*La diferència entre l'afirmació comercial i la realitat tècnica és absoluta.*

### Què no està xifrat

En examinar els dispositius, els investigadors van trobar **sense xifrar**:
1. **Enregistraments de vídeo i imatges desats**
2. **Dades de matrícules i metadades**
3. **Credencials WiFi i claus API**
4. **Fitxers de base de dades amb registres de deteccions**
5. **Trànsit de xarxa** (vegeu la vulnerabilitat núm. 6)
6. **Registres del sistema amb informació sensible**

### Contradicció sobre la conservació de dades

**Afirmació de Flock Safety**: les dades s'eliminen automàticament al cap de 7 dies  
**Troballes de la recerca**: es van trobar imatges que es remuntaven a la **fabricació del dispositiu** (feia mesos o anys)

Fragment del document tècnic de GainSec:
> «Hem trobat imatges de fa més de 7 dies. De fet, algunes imatges emmagatzemades es van capturar quan la càmera es va activar dins la fàbrica on es va fabricar el dispositiu.»

*Això vol dir que les polítiques de privadesa anunciades no s'apliquen al dispositiu.*

### Implicacions per a la privadesa

Aquest error de xifratge implica que:
- **Robar físicament el dispositiu** equival a una filtració immediata de dades
- **Interceptar la xarxa** exposa dades en text clar
- **Les amenaces internes** poden exfiltrar dades fàcilment
- Potser **les proteccions de les ordres judicials** no s'apliquen a les dades sense xifrar
- Hi ha **incompliments normatius** en diverses regulacions (HIPAA, CCPA, etc.)

______
## Vulnerabilitat crítica núm. 4: credencials codificades directament a tot el sistema {#critical-vulnerability-4-hardcoded-credentials-throughout-system}

### CVE-2025-47818, CVE-2025-47821, CVE-2025-47823, CVE-2025-59407 i CVE-2025-59409

**Gravetat**: CRÍTICA (CVSS 9.8, el valor màxim de l'escala)

### Categories de secrets codificats directament

Els investigadors de seguretat van trobar **un gran nombre de credencials codificades directament**:

#### 1. Contrasenyes dels punts d'accés WiFi
- **Contrasenya universal** per a totes les càmeres Falcon/Sparrow
- **Els usuaris i administradors no la poden canviar**
- **Els investigadors la coneixen** i es va publicar en un document tècnic (amb seccions censurades)
- **Confirmació de CVE-2025-59409**: el microprogramari de producció de Falcon i Sparrow (compilació `OPM1.171019.026`) s'envia amb **credencials WiFi de desenvolupament en text clar**

#### 2. Claus API i tokens
- **Codificats directament al microprogramari** i al codi de les aplicacions
- **Donen accés al backend** de diversos serveis
- **Localitzats mitjançant enginyeria inversa** de fitxers APK d'Android
- **Confirmats pel bolcat de setembre de 2026**: una clau API del backend codificada a `CameraSettings`, dins `com.flocksafety.android.common.lib`, una biblioteca compartida inclosa a **les 19 aplicacions de Flock** del dispositiu
- **L'identificador i el secret del client Auth0 es desen a la partició `/persist` sense xifrar** a `flock/auth0/auth0_cred`, una ubicació preparada per sobreviure a un restabliment de fàbrica
- **Les credencials retornades es desen en text clar** després que la càmera s'autentiqui al servei Okta Auth0 de Flock amb la seva pròpia adreça MAC

#### 3. Credencials de base de dades
- **Bases de dades SQLite** sense protecció amb contrasenya
- Credencials de **MySQL/PostgreSQL** en fitxers de configuració
- **Accés directe a la base de dades** des del shell local

#### 4. Magatzems de claus criptogràfiques
- **Confirmació de CVE-2025-59407**: l'aplicació DetectionProcessing incorpora un magatzem de claus Java amb la contrasenya codificada directament, i el magatzem conté una **clau privada**
- **Gravetat**: CRÍTICA (CVSS 9.8), perquè el material de la clau viatja amb el binari que l'hauria de protegir

#### 5. Noms de xarxes WiFi
- **Llista de xarxes preferides** codificada al microprogramari
- Facilita els atacs amb **punts d'accés fraudulents** (vegeu la vulnerabilitat núm. 6)

#### 6. Credencials de serveis al núvol
- **Tokens d'AWS/Azure** incrustats al codi
- **Claus API de tercers** (ArcGIS, serveis de mapes)
- **Tokens OAuth** que no es roten mai

### Escenari d'atac: xarxa fraudulenta

Amb els noms de xarxes WiFi codificats, els investigadors van demostrar que:

1. L'atacant configura una **xarxa WiFi falsa** amb l'SSID codificat
2. La càmera **s'hi connecta automàticament** (dona prioritat a les xarxes codificades)
3. L'atacant captura **tot el trànsit de xarxa** amb un atac d'intermediari
4. Les credencials en text clar s'extreuen del trànsit
5. L'atacant obté **accés als sistemes del backend**

**No cal accés físic a la càmera.** N'hi ha prou d'estar dins l'abast de la xarxa WiFi.

______
{{< figure src="flock-safety-hardcoded-credentials-attack-vectors-diagram.webp" alt="Diagrama de cinc vectors d'atac amb credencials codificades a les càmeres Flock Safety: contrasenyes WiFi, claus API, credencials de bases de dades i tokens de serveis al núvol" >}}

______
## Vulnerabilitat crítica núm. 5: manca d'autenticació multifactor {#critical-vulnerability-5-lack-of-multi-factor-authentication}

### Fallada de la política organitzativa

**Gravetat**: ALTA (organitzativa)

### La revelació

**Flock Safety no exigeix 2FA/MFA** a algunes agències policials, *les mateixes que accedeixen cada dia a les dades de seguiment de 150 milions de vehicles.*

Cita d'un investigador de seguretat:
> «Quan ho vaig saber, senzillament no m'ho podia creure. El procés de seguretat que has de seguir per iniciar sessió a Disney Plus és massa demanar a alguns departaments de policia quan accedeixen a informació confidencial i a la ubicació de pràcticament tothom.»

### Per què importa

Sense MFA/2FA:
- **Una sola contrasenya compromesa** dona accés complet al sistema
- Els **atacs de pesca** són molt efectius
- Funciona l'**emplenament de credencials** a partir d'altres filtracions
- Les **amenaces internes** són més fàcils d'executar
- Els **dispositius robats** donen accés immediat

### Comparació

Requisits de seguretat per a sistemes **menys sensibles**:
- **Disney+**: ofereix 2FA
- **Gmail**: 2FA activada per defecte per als comptes nous
- **Banca**: la llei exigeix 2FA
- **Xarxes socials**: 2FA estàndard

Requisits de seguretat per fer el **seguiment diari de més de 150 milions de vehicles**:
- **Flock Safety**: 2FA opcional (algunes agències no la fan servir)

### Resposta d'un senador dels Estats Units

Aquesta troballa es va destacar expressament a la **carta del senador Wyden** que demanava una investigació de la FTC, on s'afirmava que Flock Safety havia:
> «exposat innecessàriament dades personals sensibles dels nord-americans al robatori per part de pirates informàtics i espies estrangers»

### Solució senzilla

Les **claus de seguretat USB/NFC** costen **entre 10 i 25 dòlars** i ofereixen:
- Autenticació **resistent a la pesca**
- **Cap aplicació ni codi addicional**
- Compatibilitat amb l'estàndard **FIDO2/WebAuthn**
- Una **experiència d'ús senzilla** (connectar o apropar el dispositiu)

*Si això és «massa complicat» per al personal de les forces de l'ordre, **no hauria de tenir accés** als sistemes de vigilància nacionals.*

______
## Vulnerabilitat crítica núm. 6: trànsit de xarxa en text clar {#critical-vulnerability-6-clear-text-network-traffic}

### Pendent d'assignació d'identificador

**Gravetat**: ALTA (CVSS 7.8 estimat pels investigadors)

**No s'ha assignat cap identificador CVE a aquesta categoria.** El registre assignat més pròxim, CVE-2025-59406, té la classificació CWE-319 de transmissió en text clar, però tracta d'un secret Auth0 incrustat i no de la intercepció de dades en trànsit. Les troballes d'aquesta secció continuen basant-se en els informes de recerca citats més amunt.

### La vulnerabilitat

Quan les càmeres es connecten a xarxes (LTE o WiFi), transmeten dades **sense un xifratge adequat**:

**Trànsit afectat**:
- Imatges i text de matrícules
- Metadades de detecció
- Registres del sistema
- Dades de configuració
- Credencials (en alguns casos)

### Vector d'atac núm. 1: xarxa WiFi fraudulenta

Els investigadors van demostrar que:
1. S'extreu la targeta SIM de la càmera **o** es configura una xarxa falsa amb l'SSID codificat
2. La càmera es connecta a la xarxa WiFi fraudulenta
3. Es captura el trànsit amb **Wireshark** o un analitzador de paquets similar
4. S'analitza amb eines com **NetworkMiner** o **Unblo**
5. S'extreuen **credencials en text clar** i dades sensibles

Cita de la recerca de GainSec:
> «Vaig capturar durant una estona les dades pcap que transmetia una d'aquestes càmeres i les vaig analitzar amb Wireshark i Unblo... i, efectivament, hi havia credencials en text clar a les dades.»

### Vector d'atac núm. 2: captador IMSI / Stingray

Un atac més sofisticat no requereix proximitat física:
1. Es fa servir un **captador IMSI** (un dispositiu Stingray casolà) o un SDR professional
2. **S'intercepta la connexió LTE** suplantant una torre de telefonia mòbil
3. La càmera es connecta a una **estació base fraudulenta**
4. S'intercepta **tot el trànsit amb un atac d'intermediari**
5. S'extreuen credencials, imatges i metadades

**No cal accés físic.** L'atac funciona des de **centenars de peus de distància**.

### Possibilitat d'atacs Tempest moderns

La transmissió en text clar també permet **atacs d'estil Tempest**, en què:
- Es poden capturar les emissions de radiofreqüència de la càmera
- Es pot **reconstruir el flux de vídeo a distància**
- La tècnica s'assembla a les de la CIA de la **Guerra Freda**
- Els equips SDR moderns la fan **accessible als aficionats**

______
## Vulnerabilitat crítica núm. 7: fluxos públics de càmeres exposats {#critical-vulnerability-7-exposed-public-camera-feeds}

### Descoberta del gener de 2026

**Gravetat**: CRÍTICA (CVSS 10.0, exposició completa del sistema)

### La descoberta

El gener de 2026, Ben Jordan i **404 Media** van descobrir que amb **cerques senzilles a Google** podien trobar:
- **Més de 60 interfícies administratives de càmeres Flock Safety completament exposades**
- **Sense necessitat de nom d'usuari ni contrasenya**
- **Fluxos de vídeo en directe** i 30 dies d'enregistraments arxivats
- Accés al tauler de **control complet de les càmeres**

### Què hi havia accessible

Des d'aquestes interfícies exposades, qualsevol persona podia:
- **Veure els fluxos de vídeo en directe** en temps real
- **Consultar 30 dies** d'enregistraments arxivats
- **Descarregar fitxers de vídeo** directament
- **Controlar càmeres PTZ** (gir, inclinació i zoom) de les unitats Condor
- **Veure camins i hash dels fitxers** de proves
- **Esborrar proves** prement un sol botó
- **Modificar els paràmetres de la càmera**
- **Consultar números de sèrie i ubicacions dels dispositius**

### Infraccions de la privadesa observades

Ben Jordan va documentar que havia vist:
- **Una família carregant un nadó** al cotxe en un aparcament de Lowe's
- **Un home que sortia de casa seva** al matí a Nova York
- **Una dona corrent sola** per un camí forestal a Geòrgia
- **Una parella discutint** en un mercat a l'aire lliure d'Atlanta (el zoom automàtic d'IA es va centrar en les cares)
- **Un agent i una ambulància** atenent una crisi de salut mental a Iowa
- **Infants jugant** en un parc infantil de la zona de la badia de Califòrnia
- **Un home gronxant-se** en un parc buit en un moment privat

Cita de Ben Jordan:
> «Només de dir tot això en veu alta em venen nàusees. Però intento mostrar-vos una petita part de la informació que qualsevol persona del món amb accés a un cercador comercial ha tingut sobre qui va anar a aquest mercat o va caminar per aquest camí durant els darrers 31 dies.»

### Capacitats de seguiment

Les càmeres PTZ Condor exposades incorporen **seguiment amb IA**:
- **Apropen automàticament** les persones
- **Segueixen les persones** mentre es mouen
- **Detecten i enfoquen** telèfons intel·ligents (per llegir-ne les pantalles)
- **Segueixen diversos objectius** alhora
- **Enregistren contínuament** sense supervisió

### Risc de revelar identitats

Ben Jordan va demostrar com de fàcil és obtenir la identitat a partir d'imatges exposades:
> «En menys de dos minuts de recerca de fonts obertes amb un servei comercial de reconeixement facial, vaig saber que una de les persones acabava de graduar-se en medicina i que l'altra patia la síndrome de l'intestí irritable crònic. La parella també havia tingut un nadó l'any passat... també sé que van conduir més de 45 minuts des de casa seva als suburbis.»

Encreuant les dades amb:
- Serveis de **reconeixement facial**
- Perfils de **xarxes socials**
- Bases de dades de **registres públics**
- Informació de **filtracions de dades** (Park Mobile, etc.)
- **Registres de trucades d'emergència** (moltes ciutats els publiquen)

Resultat: **desanonimització completa en pocs minuts**

______
{{< figure src="flock-exposed-camera-feed-ptz-ai-tracking-privacy-violation-overview.webp" alt="Diagrama general de com les càmeres PTZ exposades de Flock Safety, amb seguiment automàtic per IA, permetien al públic veure en directe persones en parcs, camins i aparcaments" >}}

______
## Vulnerabilitat crítica núm. 8: recopilació no autoritzada de dades {#critical-vulnerability-8-unauthorized-data-collection}

### Contradicció amb les declaracions públiques

**Gravetat**: ALTA (implicacions legals i de privadesa)

### Afirmacions de Flock Safety

**Declaració del lloc web oficial**:
> «Flock Safety no captura ni enregistra dades de persones, només de vehicles.»

### Troballes de la recerca independent

**Què fan realment les càmeres**:
1. La **detecció de moviment** activa la càmera **per qualsevol cosa**, no només pels vehicles
2. La **IA busca una matrícula** a la imatge
3. **Si no troba cap matrícula**, la imatge **es desa igualment** (no s'esborra)
4. Una **carpeta separada** desa les imatges sense matrícula
5. Es capturen i es conserven imatges de **persones, vianants i ciclistes**

*L'afirmació que només es capturen vehicles és falsa. La càmera desa imatges de qualsevol persona que hi passi per davant.*

### Observacions verificades

Els investigadors van documentar càmeres que capturaven:
- **Una persona caminant** davant la càmera (imatge desada)
- **Una mà saludant** davant l'objectiu (imatge desada)
- **Una taula o un objecte** mogut a prop de la càmera (imatge desada)
- **Treballadors de fàbrica** a les instal·lacions de fabricació (conservats durant mesos)

Cita de GainSec:
> «Quan em vaig posar davant la càmera, el mòdul de radar va activar el mòdul de càmera perquè em fes una foto. Després, la IA integrada va buscar una matrícula, no en va trobar cap, però igualment va desar la imatge en una carpeta separada.»

### Implicacions legals

Aquesta recopilació no autoritzada de dades podria:
- **Incomplir les polítiques de privadesa anunciades** (pràctiques enganyoses)
- **Infringir contractes de compra** (si les ciutats hi van especificar «només vehicles»)
- **Provocar incompliments del RGPD/CCPA** (ciutadans de la UE i residents de Califòrnia)
- **Invalidar els acords de consentiment**
- **Exposar l'empresa a litigis** per publicitat falsa

### Ampliació de l'abast de la vigilància

Les **càmeres PTZ Condor** (desplegades el 2025-2026) estan **dissenyades expressament** per seguir persones:
- **Detecció de persones amb IA**
- **Zoom automàtic** a les cares
- **Seguiment** mentre es mouen
- **Sense mecanisme per excloure's**
- **Sovint instal·lades** en parcs, camins i estacions de transport

*Això amplia enormement l'abast, dels lectors de matrícules a la vigilància general de la població, sense canviar les polítiques ni els contractes i sense avisar el públic.*

______
## Vulnerabilitat crítica núm. 9: ports USB exposats a atacs Rubber Ducky {#critical-vulnerability-9-exposed-usb-ports-for-rubber-ducky-attacks}

### Explotació amb accés físic

**Gravetat**: ALTA (amb accés físic)

### La vulnerabilitat

Les **caixes d'informàtica Bravo** i alguns models de càmera tenen:
- **Ports USB-C exposats** a l'exterior
- **Cap seguretat física** (segells de la carcassa)
- **Execució automàtica** de dispositius USB
- **Sense necessitat d'autenticació**

### Atac Rubber Ducky / BadUSB

Un **dispositiu BadUSB** (costa entre 5 i 15 dòlars):
- Es presenta al sistema com un **teclat USB**
- **Executa scripts preprogramats** (càrregues útils)
- **S'executa automàticament** en connectar-lo
- **No requereix cap interacció de l'usuari**

### Escenari d'atac

GainSec va demostrar que:
1. L'atacant s'acosta a un dispositiu Flock desplegat
2. Connecta un **dispositiu BadUSB** al port exposat
3. El dispositiu executa la càrrega útil (script)
4. La càrrega instal·la **programari maliciós persistent**
5. L'atacant **se'n va**
6. El programari maliciós **es connecta al seu servidor** a través de LTE/WiFi

**Temps total**: menys de 30 segons

### Què poden fer les càrregues útils

Els scripts automatitzats poden:
- **Activar un punt d'accés sense fil** (eludir les pulsacions del botó)
- **Instal·lar una porta del darrere** per a l'accés remot
- **Exfiltrar dades** cap a un servidor remot
- **Modificar enregistraments** o proves
- **Desactivar la càmera** o provocar una denegació de servei
- **Afegir-la a una botnet** per fer atacs DDoS
- **Capturar credencials** d'altres sistemes

### Per què importa

Amb **més de 80.000 càmeres**, sovint en **zones semirurals** amb **poca visibilitat**:
- L'**accés físic** és relativament fàcil
- **No hi ha vigilants** ni supervisió constant
- Estan fixades amb **abraçadores senzilles**
- Sovint es munten a **7 peus del terra** (s'hi arriba amb un tamboret)

Cita de Ben Jordan:
> «Aquestes càmeres no són precisament fortaleses inexpugnables. Són càmeres i caixes d'informàtica Android de plàstic, muntades a 7 peus d'altura amb abraçadores.»

______
{{< figure src="badusb-rubber-ducky-flock-camera-usb-exploit-attack-chain.webp" alt="Diagrama de la cadena d'atac que mostra com un dispositiu BadUSB connectat a un port USB exposat d'una càmera Flock Safety pot instal·lar programari maliciós persistent en menys de 30 segons" >}}

______
## Vulnerabilitat crítica núm. 10: claus API exposades públicament {#critical-vulnerability-10-publicly-exposed-api-keys}

### Descoberta d'un investigador OSINT

**Gravetat**: CRÍTICA (CVSS 9.5)

### La descoberta

El 2025, l'**investigador OSINT Joshua Michael** va descobrir:
- Un **lloc web de demostració de Flock Safety exposat** mitjançant cerques avançades de Google
- **5.000 línies de codi font** visibles
- Una **clau API activa** incrustada al codi
- **Accés a més de 50 capes privades** de dades geoespacials

### Què permetia fer la clau API

La **clau API d'ArcGIS** exposada permetia accedir a:

**1. Dades de registre**
- Noms dels clients
- Adreces electròniques
- Nombre de càmeres per ubicació
- Capacitat d'adjuntar fitxers

**2. Ubicacions en directe dels cotxes patrulla** (diversos departaments)
- Seguiment GPS en temps real dels vehicles policials
- Desplegament d'Aurora, Colorado
- Departament de Policia de Carrollton
- **Risc per a la seguretat nacional**

**3. Informació personal dels agents**
- Noms i números de telèfon
- Adreces electròniques
- Zones de patrulla previstes
- Jurisdiccions de residència

**4. Base de dades d'alertes de llista prioritària** (Dallas, Texas)
- **6.000 registres** de vehicles assenyalats
- Matrícules i motius de les alertes
- Ubicacions i marques de temps de les deteccions
- Identificadors de les càmeres que van captar els vehicles
- **Cinc mesos de seguiment dels moviments**

Cita de Joshua Michael:
> «Qualsevol persona podia buscar-ho a Google, trobar aquest mapa i rastrejar durant 5 mesos els patrons de moviment d'aquestes persones. També cal dir que a la categoria del motiu hi ha algú amb només “sospitós” i molts altres no tenen cap motiu o el camp és buit.»

### Superfície d'atac

Les claus API exposades permeten:
- **Assetjar** vehicles concrets
- **Comprometre la seguretat dels agents** (domicilis i patrons de patrulla)
- **Vulnerar la seguretat operativa** (on és i on no és la policia)
- **Intimidar testimonis** (seguir persones que han denunciat delictes)
- Recopilar **informació d'intel·ligència criminal** per a grups de crim organitzat

### Context de la filtració: Flax Typhoon

Unes setmanes abans d'aquesta descoberta, el grup de pirateria **Flax Typhoon**, **patrocinat per l'Estat xinès**, va comprometre ArcGIS, segons els investigadors de seguretat Alexa Feminina i James Zhang.

Cita d'InfoSecurity Magazine:
> «Segons les acusacions, els pirates van atacar una aplicació ArcGIS legítima i accessible al públic... utilitzada per a la recuperació de desastres, la gestió d'emergències i altres funcions essencials.»

**Això vol dir que estats hostils podrien haver accedit** a les ubicacions dels vehicles policials, la identitat dels agents, la ubicació de les càmeres de vigilància i els patrons de resposta a emergències.

______
## Vulnerabilitats addicionals (resum de més de 50)

### Vulnerabilitats 11-51

El document tècnic de GainSec descriu **41 troballes addicionals**, com ara:

**Defectes de disseny del sistema**:
- Mode de depuració activat al microprogramari de producció
- Arrencada insegura que permet comprometre el carregador d'arrencada
- Sense element segur ni TPM per desar claus
- Mecanisme d'actualització del microprogramari predictible

**Problemes d'autenticació**:
- Els tokens de sessió no caduquen mai
- Sense restriccions d'accés basades en IP
- Credencials compartides entre flotes de dispositius
- Sense fixació de certificats

**Seguretat de xarxa**:
- Ports oberts amb serveis de depuració
- Telnet activat en algunes unitats
- Servidors FTP amb credencials febles
- Vulnerabilitats de reassignació de DNS

**Privadesa i conservació de dades**:
- Imatges desades més enllà del període anunciat
- Metadades que no s'esborren mai
- Dades de reconeixement facial recopilades
- Seguiment d'ubicacions més enllà dels vehicles

**Seguretat física**:
- Carcasses fàcils de desmuntar
- Interfícies sèrie exposades
- Ports de depuració JTAG accessibles
- Sense segells que evidenciïn manipulacions

**Errors criptogràfics**:
- Generació de nombres aleatoris feble
- Claus de xifratge codificades directament
- Encadenament de hash que encara fa servir MD5
- Validació de certificats desactivada

**Divulgació d'informació**:
- Missatges d'error detallats revelen elements interns
- Llistat de directoris activat als servidors web
- Comentaris del codi font amb credencials
- Còpies de seguretat de la configuració llegibles per tothom

### Estat dels CVE

El maig de 2026:
- **S'havien assignat i publicat 22 CVE**
- **8 CVE estaven pendents** d'assignació per MITRE
- **21 troballes** no s'havien presentat per obtenir CVE (a discreció dels investigadors)
- **Totes les troballes** consten al document tècnic de GainSec

Detalls tècnics complets: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)

______
## Resposta de Flock Safety

### Declaracions oficials

**Publicació de blog del novembre de 2025**:
> «Flock es compromet a millorar la seguretat contínuament... Cap de les vulnerabilitats detallades a l'informe afecta la capacitat dels nostres clients de complir els seus objectius de seguretat pública.»

**Afirmació**: les vulnerabilitats requereixen accés físic i «coneixement profund»

**Proves en contra**:
- Per trobar els fluxos de càmera exposats només calia **fer una cerca a Google**
- Per explotar la connexió sense fil només calia **ser a prop**
- L'exposició de la clau API era **completament remota**
- Després de divulgar-les, les contrasenyes codificades eren **conegudes universalment**

### Rebuig dels dispositius d'investigació

Al principi, Flock va afirmar que els dispositius d'investigació:
> «No estaven connectats al núvol... com un iPhone robat d'un camió abans que s'hagués connectat mai.»

*Es va demostrar que això era fals.* Els investigadors van provar **dispositius connectats al núvol** i van obtenir els mateixos resultats. Les càmeres accessibles al públic presentaven **les mateixes vulnerabilitats**, i 404 Media va trobar **més de 60 càmeres de producció exposades**.

### Resposta a l'investigador

GainSec va informar que els intents de divulgació responsable van rebre:
- **Programa de recompenses per errors amb NDA** (per silenciar la divulgació)
- **Cap confirmació** de les correccions
- **Declaració de relacions públiques** abans que acabés el termini de 90 dies
- **Cap reconeixement** de l'investigador a la declaració
- **Pèrdua de la feina** de l'investigador durant les 48 hores posteriors a la publicació del vídeo

Ben Jordan va informar de:
- **Visites de la policia** a casa seva
- **Presumptes investigadors privats** que fotografiaven casa seva
- **Assetjament per part d'un veí**
- **Amenaça de requeriment de cessament** per part de Flock Safety

Cita de Ben:
> «No considero que això siguin conseqüències o càstigs per investigar vulnerabilitats de seguretat. Ho veig com a conseqüències i càstigs per fer-ho amb ètica i transparència.»

### Desplegament continuat

*Malgrat tot això*, Flock Safety:
- **Continua venent** dispositius vulnerables
- **No ha publicat actualitzacions de microprogramari** que corregeixin les causes principals
- **Continua fent servir** Android Things 8.x (fora de servei des del 2021)
- **No exigeix MFA** a les forces de l'ordre

______
## Resposta legislativa i de polítiques públiques

### Petició d'investigació del Senat dels Estats Units

**Febrer de 2026**: els senadors **Ron Wyden** (Oregon) i **Raja Krishnamoorthi** (Illinois) van enviar una carta formal a la FTC per demanar una investigació.

**Fragment de la carta**:
> «Flock ha exposat innecessàriament dades personals sensibles dels nord-americans al robatori per part de pirates informàtics i espies estrangers.»

**Motius citats**:
- Riscos per a la seguretat nacional
- Afirmacions enganyoses sobre la privadesa
- Pràctiques de seguretat inadequades
- Manca de requisits d'MFA

### Mesures dels ajuntaments

**Denver, Colorado**:
- El consell municipal **va votar contra** la renovació del contracte amb Flock (desembre de 2025)
- Va citar el «**menyspreu per l'honestedat i la responsabilitat**» de Flock
- L'alcalde **va anul·lar la decisió** amb un «acord entre bastidors» (gener de 2026)
- La reacció pública continua

**Evanston, Illinois**:
- Va descobrir que **l'ICE feia servir les càmeres** sense consentiment
- Va votar a favor de **retirar-les**
- *Flock les va tornar a instal·lar sense autorització*
- La ciutat gasta diners públics per **cobrir les càmeres** amb lones i emprendre accions legals

**Oakland, Califòrnia**:
- Va ajornar la votació sobre una **ampliació de 2,25 milions de dòlars**
- Va encarregar una auditoria de seguretat independent
- Va concloure que les afirmacions d'eficàcia de Flock eren **enganyoses**

### Sol·licituds d'accés a registres públics

Diverses ciutats duen a terme investigacions basades en:
- Recerca de seguretat disponible públicament
- Sol·licituds FOIA dels contractes de Flock
- Requisits d'auditories independents
- Pressió de les organitzacions comunitàries

______
## Anàlisi tècnica: escenaris d'atac reals

### Escenari 1: vigilància d'un estat nació

**Actor de l'amenaça**: servei d'intel·ligència estranger

**Objectiu**: seguir càrrecs governamentals

**Mètode**:
1. Fer servir un captador IMSI per interceptar el trànsit LTE de la càmera
2. Extreure credencials en text clar del flux
3. Accedir al backend amb claus API compromeses (o amb una capa d'ArcGIS exposada anteriorment)
4. Consultar la base de dades per trobar vehicles registrats a instal·lacions governamentals
5. Seguir els moviments de càrrecs públics i militars

**Temps d'execució**: dies (un cop preparada la infraestructura)  
**Probabilitat de detecció**: baixa (el C2 xifrat imita trànsit legítim)

### Escenari 2: contravigilància del crim organitzat

**Actor de l'amenaça**: organització de narcotràfic

**Objectiu**: identificar els patrons de patrulla policial

**Mètode**:
1. Comprar un dispositiu BadUSB (15 dòlars)
2. Conduir fins a càmeres del territori d'operacions
3. Connectar el BadUSB al port USB exposat (30 segons)
4. La càrrega útil desactiva la càmera o modifica els enregistraments
5. Alternativament, la càrrega exfiltra a un servidor remot les dades de seguiment dels vehicles policials

**Temps d'execució**: 30 segons per càmera  
**Probabilitat de detecció**: baixa (sembla activitat legítima del dispositiu)

### Escenari 3: assetjament o violència domèstica

**Actor de l'amenaça**: exparella abusiva

**Objectiu**: seguir els moviments de la víctima

**Mètode**:
1. Obtenir la matrícula de la víctima (informació pública)
2. Buscar a Google una interfície de càmera Flock exposada (vulnerabilitat del gener de 2026)
3. Consultar 30 dies d'enregistraments per trobar el vehicle
4. Encreuar les dades amb registres públics (feina, domicili, etc.)
5. Establir-ne els hàbits i els horaris

**Temps d'execució**: de minuts a hores  
**Probabilitat de detecció**: zero (no hi ha registres d'autenticació)

### Escenari 4: manipulació de proves

**Actor de l'amenaça**: acusat en un procés penal

**Objectiu**: destruir proves abans del judici

**Mètode**:
1. Esbrinar la ubicació de la càmera a partir de la documentació d'una ordre judicial
2. Accedir físicament a la càmera (seqüència de pulsacions del botó)
3. Obtenir un shell root
4. Anar a la carpeta de proves
5. Esborrar imatges o vídeos concrets, o modificar-ne les marques de temps

**Temps d'execució**: menys de 5 minuts  
**Probabilitat de detecció**: baixa (tret que s'examini forensement la càmera abans que hi accedeixi la defensa)

### Escenari 5: activista per la privadesa o periodista

**Actor de l'amenaça**: defensor de la transparència

**Objectiu**: documentar l'excés de vigilància

**Mètode**:
1. Fer servir dispositius de detecció (vegeu la nostra [guia de maquinari Flock-You](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. Cartografiar les càmeres de la comunitat
3. Presentar sol·licituds FOIA sobre les polítiques d'enregistrament
4. Demostrar les vulnerabilitats davant el consell municipal
5. Demanar-ne la retirada o supervisió

**Temps d'execució**: continuat  
**Probabilitat de detecció**: alta (activitat pública)

______
{{< figure src="flock-camera-attack-scenario-threat-actor-matrix-nation-state-crime.webp" alt="Matriu de comparació de cinc escenaris d'atac reals contra les càmeres Flock Safety: vigilància estatal, crim organitzat, assetjament, manipulació de proves i defensa de la privadesa" >}}

______
## Com defensar-se d'aquestes vulnerabilitats

### Per a les agències policials

**Mesures immediates**:
1. **Exigir MFA/2FA** a tots els usuaris (claus de seguretat USB)
2. **Auditar mensualment els registres d'accés** per detectar consultes no autoritzades
3. **Limitar l'intercanvi de dades** a les jurisdiccions estrictament necessàries
4. **Aïllar la xarxa**: posar les càmeres en VLAN dedicades
5. **Protegir físicament els dispositius** amb segells anti-manipulació i vigilància de les càmeres
6. Preparar un **pla de resposta a incidents** en cas de compromís

**Requisits contractuals**:
1. **Auditories de seguretat periòdiques** per empreses independents
2. **Actualitzacions obligatòries del microprogramari** en els 30 dies posteriors a la publicació d'un pedaç
3. **Notificació de CVE** en 24 hores
4. **Emmagatzematge xifrat de proves** amb claus gestionades pel client
5. **Penalitzacions contractuals** per filtracions de seguretat
6. **Dret d'auditar** les instal·lacions i el codi del proveïdor

**Estratègia a llarg termini**:
1. Preparar un **pla de transició** per abandonar els sistemes operatius fora de servei
2. Adoptar **infraestructura allotjada localment** (reduir la dependència del núvol)
3. Avaluar **alternatives de codi obert**
4. Garantir **transparència comunitària** sobre la ubicació i les polítiques de les càmeres

### Per a Flock Safety (recomanacions)

**Prioritat crítica** (immediata):
1. **Desactivar la creació de punts d'accés sense fil** prement el botó
2. **Exigir MFA** a tots els comptes (sense excepcions)
3. **Canviar totes les credencials** codificades a tot el sistema
4. Publicar un **pedaç d'emergència** per a les interfícies públiques exposades
5. **Xifrar les dades emmagatzemades** amb una gestió correcta de les claus

**Prioritat alta** (30 dies):
1. **Migrar a un sistema operatiu amb suport** (Android 12+ o Linux)
2. Crear un **programa de recompenses per errors** sense acords de confidencialitat
3. Fer una **auditoria de seguretat externa** i publicar-ne els resultats
4. Xifrar **extrem a extrem** el trànsit de xarxa
5. Millorar la **seguretat física** (retirar els USB exposats i reforçar les carcasses)

**Prioritat mitjana** (90 dies):
1. **Redissenyar completament** el sistema d'autenticació
2. Implementar **arrencada segura** amb microprogramari verificat
3. Integrar un **mòdul de seguretat de maquinari**
4. Obtenir **certificacions de compliment** (FedRAMP, SOC 2, ISO 27001)
5. Crear un **tauler de seguretat per als clients** amb notificacions de filtracions

**A llarg termini** (1 any):
1. Publicar **components de seguretat de codi obert** (per generar confiança)
2. Crear un programa de **proves adversàries** (equip vermell)
3. Exigir competències d'**enginyeria de seguretat**
4. Integrar pràctiques de seguretat al **cicle de desenvolupament** (DevSecOps)
5. Participar en **estàndards del sector** (OWASP, CIS)

### Per a les persones

**Estratègies de protecció**:
1. **Fer servir dispositius de detecció** (vegeu la nostra [guia de maquinari](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. **Cartografiar les càmeres** de la zona
3. **Variar els trajectes i els horaris** per reduir l'anàlisi de patrons
4. **Demanar supervisió i transparència** al consell municipal
5. **Presentar sol·licituds FOIA** sobre les vostres dades (quan la llei ho permeti)
6. **Donar suport a les lleis de privadesa** estatals i federals

**Mesures d'OpSec**:
1. **Evitar vehicles singulars** (triar una marca, model i color comuns)
2. Fer servir **vehicles diferents** per a activitats sensibles (quan sigui legal)
3. Triar **mitjans de transport alternatius** (bicicleta, transport públic o anar a peu)
4. Fer servir **cobertes de matrícula orientades a la privadesa** (només si la jurisdicció les permet)
5. Fer servir **bosses de Faraday** per als telèfons si preocupa la correlació de dades

{{< stscollective-ad "flockyou" >}}

______
{{< figure src="flock-safety-security-remediation-priority-roadmap.webp" alt="Full de ruta de correccions prioritzades amb mesures immediates, a 30 dies, a 90 dies i a llarg termini que Flock Safety hauria d'aplicar per resoldre vulnerabilitats crítiques" >}}

______
## L'equip de recerca

### GainSec (Jon «GainSec» Gaines)

**Experiència**: professional de seguretat ofensiva, més de 10 anys d'experiència

**Aportacions**:
- Va descobrir **47 de les 51** vulnerabilitats
- Va publicar un **document tècnic formal** amb detalls tècnics
- Va coordinar la **divulgació responsable** amb Flock Safety
- Va registrar **30 CVE** (22 publicats i 8 pendents)
- Va crear una **llista de verificació per a defensors** de seguretat

**Contacte**: whitepaper@gainsecmail.com  
**Recerca**: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)  
**Blog**: [gainsec.com](https://gainsec.com)

### Ben Jordan (Benn Jordan)

**Experiència**: periodista, músic i investigador tecnològic

**Aportacions**:
- **Documentació en vídeo** de les vulnerabilitats
- **Demostracions públiques** per a periodistes (The Guardian i 404 Media)
- Va descobrir **més de 60 fluxos de càmera exposats** mitjançant Google
- **Divulgació pública i sensibilització**
- **Coordinació legislativa** amb les oficines dels senadors

**Contacte**: pel canal de YouTube  
**Treball**: YouTube - Benn Jordan

### Joshua Michael (Next AI)

**Experiència**: especialista en OSINT i investigador de privadesa

**Aportacions**:
- Va descobrir **claus API exposades** mitjançant cerques avançades de Google
- Va documentar **capes d'ArcGIS exposades**
- Va aplicar una **metodologia OSINT** a la recerca de seguiment
- Va fer **correlació de dades** amb filtracions públiques

**Organització**: Next AI, empresa d'intel·ligència d'origen divers

### Col·laboradors

- **404 Media**: periodisme d'investigació i divulgació pública
- **The Guardian**: cobertura internacional
- **Lucy Parsons Labs**: anys de recerca i defensa contra els lectors ALPR
- **Sassy South**: organització comunitària i transparència
- **DeFlock / Will Freeman**: projecte de cartografia d'ubicacions de càmeres
- **Ed Vogel**: anàlisi jurídica i de polítiques públiques

______
## Consideracions ètiques

### Cronologia de la divulgació responsable

La comunitat de seguretat va seguir les bones pràctiques de **divulgació responsable**:

**Protocol estàndard**:
1. Descobrir la vulnerabilitat
2. **Notificar-la en privat al proveïdor i donar-li 90 dies**
3. El proveïdor desenvolupa i distribueix un pedaç
4. **Divulgar-la públicament** després del pedaç o dels 90 dies (el que arribi abans)
5. Publicar una anàlisi detallada per ajudar la defensa

**Què va passar realment**:
1. GainSec va descobrir les vulnerabilitats (finals de 2024)
2. Va **contactar repetidament** Flock Safety (des del febrer de 2025)
3. Flock va oferir una **recompensa per errors amb un acord de confidencialitat** (per silenciar la divulgació)
4. Flock va publicar **prematurament una declaració de relacions públiques** (sense reconèixer l'investigador)
5. **No va confirmar** que s'haguessin distribuït pedaços
6. GainSec va procedir a la **divulgació pública** després dels terminis de 90 dies
7. Ben Jordan i 404 Media ho van **verificar independentment** en sistemes de producció

### Represàlies contra investigadors

Tant GainSec com Ben Jordan van informar de:
- **Pèrdua de la feina** o problemes laborals
- **Visites de la policia** a domicilis particulars
- **Presumpta vigilància** de cases i propietats
- **Assetjament per part de veïns**
- **Amenaces legals de cessament**
- **Atacs a les xarxes socials** (el director general de Flock els va anomenar «terroristes»)

Aquest **efecte dissuasiu** sobre la recerca de seguretat:
- Desincentiva la divulgació de vulnerabilitats
- Retarda correccions de seguretat crítiques
- Perjudica la seguretat pública
- Infringeix les normes ètiques de la comunitat de seguretat

*La resposta de Flock Safety als investigadors que van seguir els protocols de divulgació crea un precedent perillós per a tota la comunitat de recerca en seguretat.*

Cita de Ben Jordan:
> «No em puc permetre dedicar encara més mesos a una altra vulnerabilitat de Flock Safety, però, com podeu veure, aquesta és urgent i, francament, em preocupa que ja s'estigui explotant.»

### Interès públic

Aquests investigadors van actuar en **interès públic** perquè:
- Van **seguir els protocols de divulgació responsable**
- Van **avisar primer el proveïdor**, abans de fer-ho públic
- Van **censurar els detalls sensibles** que facilitarien l'explotació
- Van oferir **orientació defensiva** als professionals
- Van promoure **canvis de polítiques** pels canals adequats
- Van **assumir riscos personals** per informar el públic

Sense la seva feina:
- **Més de 80.000 càmeres vulnerables** continuarien sense correccions
- **Més de 150 milions d'escaneigs diaris de vehicles** continuarien desprotegits
- **Milions de nord-americans** estarien exposats sense saber-ho
- La **seguretat nacional** estaria compromesa
- **No hi hauria cap iniciativa legislativa** en marxa

______
## Conclusió: el camí a seguir

{{< figure src="flock-safety-vulnerability-disclosure-timeline-2026.webp" alt="Cronologia del procés de divulgació de vulnerabilitats de Flock Safety entre 2024 i 2026, des de la descoberta inicial i la divulgació responsable fins a l'exposició continuada sense pedaços" >}}

### Estat actual (maig de 2026)

- **Més de 50 vulnerabilitats crítiques** documentades i divulgades parcialment
- **Més de 80.000 càmeres** continuen desplegades amb defectes sense corregir
- **El proveïdor no ha aplicat cap correcció integral**
- **Acció reguladora limitada** (s'ha demanat una investigació de la FTC, però encara no s'ha obert)
- **Risc d'explotació continuat** per a la seguretat nacional i la privadesa individual

### Què cal fer

**A tot el sector**:
1. **Auditories de seguretat obligatòries** abans del desplegament governamental
2. **Proves independents** per part de tercers qualificats
3. **Publicació dels resultats de les auditories**
4. **Responsabilitat dels proveïdors** pels errors de seguretat
5. **Compliment d'estàndards** (NIST, ISO, etc.)

**Específicament per a Flock Safety**:
1. **Pedaços d'emergència immediats** per a les vulnerabilitats crítiques
2. **Migració del sistema operatiu** a una plataforma compatible
3. **Reconeixement públic** de l'abast dels problemes
4. **Compensació** per als investigadors afectats
5. **Informes de transparència** sobre l'estat de la seguretat

**Forces de l'ordre**:
1. Incloure **requisits de seguretat** als contractes de compra
2. Fer **auditories periòdiques** dels sistemes desplegats
3. Fer **obligatòria l'MFA** per a tots els usuaris
4. Preparar **plans de resposta a incidents**
5. Garantir la **transparència comunitària** sobre els programes de vigilància

**Legislació**:
1. Establir **estàndards federals** per a la tecnologia de vigilància
2. Exigir la **notificació de vulnerabilitats** a les parts afectades
3. Protegir els **denunciants** i investigadors de seguretat
4. Crear **vies de reparació civil** per a les infraccions de privadesa
5. Establir **mecanismes de supervisió** dels sistemes de vigilància

### El context general

Aquest cas d'estudi representa **més que Flock Safety**. És un exemple de:
- Una **indústria de vigilància** que prioritza el creixement per damunt de la seguretat
- Una **compra pública** sense prou coneixements tècnics
- Afirmacions dels **proveïdors** que ningú qüestiona ni verifica
- **Incentius financers** que no coincideixen amb la seguretat pública
- **Llacunes normatives** en la supervisió de tecnologies emergents

*Cada ciutat que signa un contracte amb Flock sense una verificació de seguretat independent assumeix aquests riscos en nom dels seus residents.*

### Crida a l'acció

**Professionals de seguretat**:
- Donar suport a la **divulgació responsable**
- Contribuir a **eines de seguretat de codi obert**
- Defensar la **protecció dels investigadors**

**Forces de l'ordre**:
- **Exigir responsabilitats** als proveïdors
- **Demanar auditories de seguretat** abans del desplegament
- **Implementar MFA immediatament**
- Consultar la **comunitat de seguretat**

**Responsables polítics**:
- Aprovar lleis que **exigeixin estàndards de seguretat**
- **Finançar auditories independents** de la tecnologia de vigilància
- **Protegir denunciants i investigadors**
- Crear **òrgans de supervisió** amb experiència tècnica

**Públic**:
- **Informar-se** sobre la vigilància a la comunitat
- **Assistir a les reunions del consell municipal** quan es tractin contractes
- **Donar suport a organitzacions** que defensen la transparència
- **Contactar amb els representants** per exposar-hi les preocupacions
- **Fer servir eines de detecció** per cartografiar la vigilància (vegeu la nostra [guia de maquinari](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))

### Lectures relacionades

- **[Vigilància amb càmeres Flock Safety: presència, preocupacions sobre la privadesa i estratègies de protecció](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** - Entendre el panorama de la vigilància
- **[Projecte de detecció Flock-You: guia de maquinari contra la vigilància](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** - Construir un dispositiu de detecció propi

Esperar que el sector corregeixi aquests defectes no és una estratègia de protecció. Els **[dispositius de detecció FlockYou](https://stscollective.com/collections/flockyou-alpr-flock-safety-awareness-devices)** de STS Collective funcionen avui, i el codi de descompte per als lectors **SIMEONONSECURITY** ofereix fins a un 20% de descompte.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compra detectors FlockYou i estalvia un 20%
{{< /centerbutton >}}

______
## Referències

1. [Recerca de GainSec sobre l'ecosistema anticriminal - GitHub](https://github.com/GainSec/anti-crime-ecosystem-research)
2. [Document tècnic de GainSec - DOI de Zenodo: 10.5281/zenodo.17529423](https://zenodo.org/records/17584876)
3. [Blog de GainSec - Informes tècnics informals](https://gainsec.com/)
4. [Resposta oficial de Flock Safety - novembre de 2025](https://www.flocksafety.com/blog/response-to-compiled-security-research-on-flock-safety-devices)
5. [404 Media - Fluxos de càmeres Flock exposats](https://www.404media.co/)
6. [YouTube de Ben Jordan - Demostracions de vulnerabilitats](https://www.youtube.com/@BennJordan)
7. [Base de dades nacional de vulnerabilitats](https://nvd.nist.gov/)
8. [Base de dades CVE de MITRE](https://cve.mitre.org/)
9. [Electronic Frontier Foundation - Vigilància ALPR](https://www.eff.org/issues/automated-license-plate-readers)
10. [Carta del senador Wyden a la FTC](https://www.wyden.senate.gov/)
11. [Lucy Parsons Labs - Recerca ALPR](https://lucyparsonslabs.com/)
12. [Projecte DeFlock - Cartografia de càmeres](https://deflockproject.org/)
13. [Distributed Denial of Secrets - Imatges del sistema de fitxers de càmeres ALPR de Flock](https://ddosecrets.org/article/flock-alpr-camera)
14. [Micah Lee - Les càmeres Flock estan plenes de vulnerabilitats de seguretat i credencials codificades](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
15. [WIRED i 404 Media - Pirates han accedit a una càmera Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
16. [Hackaday - Aquesta setmana en seguretat: les càmeres Flock són antigues](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
17. [NVD - CVE-2021-1905, ús després d'alliberament a la GPU Qualcomm Adreno](https://nvd.nist.gov/vuln/detail/CVE-2021-1905)
18. [NVD - CVE-2018-9568, confusió de tipus a sòcols del nucli Linux](https://nvd.nist.gov/vuln/detail/CVE-2018-9568)
19. [WiFi Mothership - Referència de detecció ALPR i dispositius Flock Safety](https://wifimothership.com/flock)
20. [CVE.org - Cerca de registres del programa CVE](https://www.cve.org/)
21. [Alerta de seguretat de Flock Safety - Detecció de trets i lector de matrícules](https://www.flocksafety.com/articles/gunshot-detection-and-license-plate-reader-security-alert)
22. [GainSec - Fly By Device 2: RCE sense fil a Falcon i Sparrow](https://gainsec.com/2025/09/27/fly-by-device-2-the-falcon-sparrow-gated-wireless-rce-camera-feed-dos-information-disclosure-and-more/)
23. [GainSec - Root from the Coop Device 3: shell root a la caixa d'informàtica Bravo de Flock Safety](https://gainsec.com/2025/09/19/root-from-the-coop-device-3-root-shell-on-flock-safetys-bravo-compute-box/)

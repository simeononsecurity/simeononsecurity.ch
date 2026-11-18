---
title: "La cursa per detectar les càmeres Flock: què ha canviat el 2026"
date: 2026-09-10
lastmod: 2026-11-14
toc: true
draft: false
description: "Repassem els canvis comunicats en la detecció de Flock Safety, les respostes de la comunitat i els mètodes d'infraroig per identificar sistemes de càmeres."
genre: ["Tecnologia de privadesa", "Contravigilància", "Projectes de codi obert", "Drets digitals", "Seguretat de xarxes", "Recerca en seguretat", "Manipulació de maquinari", "Eines de privadesa"]
tags: ["Flock Safety", "ALPR", "Flock-You", "Detecció OUI", "Sol·licitud de sonda comodí", "Mode WiFi promiscu", "Monitoratge 802.11", "DeFlockJoplin", "NitekryDPaul", "Detecció BLE", "WiFi de 5 GHz", "MAC administrada localment", "Coincidència de patrons SSID", "Maquinari de contravigilància", "STS Collective", "colonelpanichacks", "Evasió de detecció", "ESP32", "Detecció WiFi", "Consciència sobre vigilància", "OUI-SPY", "M5 Atom Lite", "Flock Finder", "Seguiment d'incidències de GitHub", "Actualització de microprogramari", "Antifingerprinting", "Aleatorització MAC", "Empremta digital d'elements d'informació", "Salt entre canals", "Defensa de la privadesa", "Seguretat de codi obert", "Vigilància massiva", "Microprogramari de detecció", "Detecció de xarxes WiFi en moviment", "Retirada de càmeres", "Maquinari de privadesa", "Detecció per infraroig", "Il·luminador IR", "ESP32-CAM", "Seeed Studio XIAO ESP32S3 Sense", "Quectel L76K", "Detecció òptica", "Valleytech Custom Solutions"]
cover: "/img/cover/flock-camera-detection-techniques-2026.webp"
coverAlt: "Escena urbana amb una càmera Flock en un fanal i un vehicle equipat amb un dispositiu de detecció avançat. Senyals lluminosos representen la comunicació de dades sense fils sobre un fons fosc."
coverCaption: "Com els canvis de maquinari de Flock Safety continuen trencant les eines de detecció de codi obert i com la comunitat s'hi posa al dia"
canonical: "https://simeononsecurity.com/articles/flock-camera-detection-arms-race-2026/"
---

**Si el teu detector Flock-You ha deixat de detectar càmeres en una ruta on abans les trobava sempre, no t'ho estàs imaginant i probablement el maquinari no s'ha espatllat.** El maquinari i el microprogramari de les càmeres de Flock Safety han canviat almenys dues vegades durant l'últim any i han fet fallar els mètodes de detecció de la comunitat. Cada vegada, investigadors de codi obert han hagut d'enginyar a la inversa un senyal nou.

*Aquesta situació canvia ràpidament. El mètode de detecció i la llista OUI d'aquí reflecteixen el projecte `colonelpanichacks/flock-you`, branca `main` el setembre de 2026. Consulta el [repositori de GitHub](https://github.com/colonelpanichacks/flock-you) abans de donar per fet que el teu dispositiu és defectuós.*

{{< youtube id="cVf-id71BuQ" >}}

*El vídeo anterior, de Valleytech Custom Solutions, documenta exactament el símptoma que explica aquest article: una ruta rutinària de wardriving deixa de detectar càmeres de cop, fins i tot amb diverses versions del microprogramari. Abans les càmeres es detectaven de manera fiable en aquella ruta, tot i que al comtat n'havien retirat físicament diverses que ja s'havien identificat.*

______

## Una ruta de wardriving que de cop no detecta res

El patró es repeteix gairebé igual en tots els informes. Un conductor fa una ruta que ha recorregut desenes de vegades. El detector, amb el microprogramari actual, ja havia detectat les mateixes càmeres. Però un dia no en detecta cap. Ni un sol avís sonor ni una entrada al registre, amb cap de les versions personalitzades del microprogramari que prova.

El vídeo de Valleytech descriu exactament aquest cas: la ruta diària fins a l'oficina de correus sempre detectava almenys una càmera Flock, però va deixar de trobar-ne cap. En una altra ruta, davant de Micro Center, abans n'assenyalava cinc i ara només n'hi ha una d'activa. Les altres quatre les havien arrencat físicament dels pals.

**Dues coses passaven alhora i és fàcil confondre-les:**

- **En algunes zones retiren o reubiquen càmeres**, cosa que redueix de debò el nombre de dispositius que es poden detectar.
- **Ha canviat el senyal sense fil que emeten les càmeres**, així que una càmera que encara és al pal no activarà un detector amb microprogramari obsolet.

Dues incidències de GitHub al repositori `colonelpanichacks/flock-you`, obertes amb mesos de diferència, documenten detalladament el segon problema. Llegir-les en ordre explica com la comunitat ja ha hagut d'evolucionar dues vegades el mètode de detecció.

______

## Incidència 20: el punt d'accés de gestió va desaparèixer

La **[incidència 20](https://github.com/colonelpanichacks/flock-you/issues/20)**, oberta el gener de 2026, va començar amb una queixa coneguda: un usuari va provar el dispositiu al costat d'una càmera Flock identificada a DeFlock i no va detectar res. Durant les setmanes següents, més usuaris van descriure el mateix resultat, des de Florida, Indiana, Atlanta i el mig oest, amb maquinari i antenes diferents.

Un dels comentaris plantejava la pregunta clau: **Flock havia canviat alguna cosa que fes fallar la detecció a tothom més o menys alhora?**

El mantenidor del projecte, colonelpanichacks, finalment ho va confirmar. **Cap al desembre de 2025, Flock va desactivar el punt d'accés de gestió que emetien les càmeres.** Aquell AP era la base original de la detecció sense fils. Quan va desaparèixer, la comunitat va passar a fer servir senyals Bluetooth Low Energy (BLE). A la primavera de 2026, aquella alternativa també va deixar de funcionar de manera fiable.

| Superfície de detecció | Estat |
|---|---|
| **AP WiFi de gestió** | Desactivat per Flock, aproximadament el desembre de 2025 |
| **Emissió de balises BLE** | Va deixar de funcionar de manera fiable a la primavera de 2026 |
| **Connexió cel·lular LTE** | Continua en ús per pujar dades al núvol, però no es pot detectar passivament |
| **Sol·licituds de sonda comodí 802.11** | Base actual de la detecció (vegeu més avall) |

*Tot el microprogramari personalitzat que es basava en l'antic AP o en les vies de detecció BLE ara busca un senyal que les càmeres ja no emeten. Per això un dispositiu que abans funcionava pot quedar completament en silenci sense que el maquinari tingui cap problema.*

______

## El mètode nou: sondes comodí i empremta digital de trames

El microprogramari actual de `flock-you` funciona en mode promiscu 802.11 dedicat. La ràdio no transmet mai ni es connecta a cap xarxa. Només escolta i va saltant pels canals WiFi 11, 6 i 1, amb una permanència de 250 mil·lisegons a cada canal, per seguir el ritme amb què les mateixes càmeres canvien de canal.

**Ara, perquè el microprogramari generi un avís, han de coincidir totes aquestes condicions:**

1. La trama és una **sol·licitud de sonda de gestió** 802.11 (tipus 0, subtipus 4).
2. L'**element d'informació SSID hi és i té longitud 0**, és a dir, és una sonda comodí que no pregunta per cap xarxa concreta.
3. L'adreça del transmissor (**addr2**) coincideix amb un dels prefixos OUI coneguts de Flock.
4. La resta d'elements d'informació de la trama coincideixen amb el patró d'empremta digital documentat per la comunitat DeFlockJoplin, basat en la recerca de 2022 de Pintor i Atzori sobre **[empremta digital d'elements d'informació de sol·licituds de sonda WiFi](https://ieeexplore.ieee.org/document/10001618)**.

Al microprogramari, aquest mètode s'anomena `wifi_wildcard_probe_ie_sig`. En les proves de camp, la comunitat DeFlockJoplin va detectar **11 de les 12 càmeres conegudes i només va generar 2 falsos positius** a la ruta de prova. És el mateix resultat de referència verificat al camp que cita la **[guia de maquinari](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** del projecte. El prefix OUI de la dotzena càmera s'ha afegit des d'aleshores a la llista següent.

{{< figure src="flock-detection-arms-race-timeline-2026.webp" alt="Diagrama temporal de l'evolució del mètode de detecció de càmeres Flock: del punt d'accés WiFi de gestió a les balises Bluetooth Low Energy i a les actuals sol·licituds de sonda comodí amb empremta digital d'elements d'informació. Una quarta etapa mostra les noves tècniques d'evasió amb SSID, 5 GHz i adreces MAC." >}}

______

## La llista OUI actual

L'empremta digital de sonda comodí anterior només s'activa quan l'adreça MAC del transmissor coincideix amb un prefix OUI que la comunitat ha confirmat en maquinari Flock real. La llista la manté principalment l'investigador **@NitekryDPaul**. La comunitat **DeFlockJoplin** hi va afegir la 31a entrada després de detectar una càmera que no apareixia a la llista original de 30.

```text
70:c9:4e  3c:91:80  d8:f3:bc  80:30:49  b8:35:32
14:5a:fc  74:4c:a1  08:3a:88  9c:2f:9d  c0:35:32
94:08:53  e4:aa:ea  f4:6a:dd  f8:a2:d6  24:b2:b9
00:f4:8d  d0:39:57  e8:d0:fc  e0:4f:43  b8:1e:a4
70:08:94  58:8e:81  ec:1b:bd  3c:71:bf  58:00:e3
90:35:ea  5c:93:a2  64:6e:69  48:27:ea  a4:cf:12
82:6b:f2
```

**Aquesta llista no és fixa.** La recerca original explica que alguns prefixos es van provar i després van perdre pes: un pertanyia a un reproductor multimèdia Sony i un altre era un marcador inicial que no va coincidir mai amb cap dispositiu. Dos elements estan marcats com a poc fiables. Un altre, `82:6b:f2`, es manté deliberadament tot i ser una adreça administrada localment, perquè filtrar-lo hauria descartat silenciosament una detecció real confirmada per DeFlockJoplin.

**Una entrada ja té confirmació independent en maquinari d'una càmera en servei municipal.** La unitat Flock de la qual es van publicar imatges del sistema de fitxers el setembre de 2026 duia l'adreça MAC **`f4:6a:dd:57:46:fb`**. El prefix `f4:6a:dd` ocupa la posició 13 d'aquesta llista. No era un dispositiu de laboratori ni una mostra comprada. Estava muntada en un pal a Wauwatosa, Wisconsin, fotografiant el trànsit. És la confirmació més sòlida que ha rebut cap prefix de la llista.

*Si mantens una bifurcació pròpia del microprogramari, obtén la llista OUI de la carpeta `datasets/` del projecte original en comptes de copiar-la a mà. La llista canvia amb la recerca, i una còpia obsoleta fa que gradualment i sense avisar es deixin de detectar càmeres.*

______

## Classificació dels senyals de detecció

La versió actual del microprogramari es basa sobretot en la coincidència OUI, el senyal més feble dels cinc disponibles. La comunitat de detecció de **[WiFi Mothership](https://wifimothership.com/flock)** els ordena per nivell de confiança a partir de la recerca de microprogramari de GainSec.

| Confiança | Senyal | Notes |
|------------|--------|-------|
| **ALTA** | **ID de fabricant BLE `0x09C8`** (XUNTONG) | L'empremta digital més sòlida. Apareix a les unitats Raven i a qualsevol Falcon o Sparrow amb un mòdul de bateria instal·lat |
| **ALTA** | **UUID de servei BLE de Raven `0x3100` a `0x3500`** | Serveis GATT específics de Raven per a GPS, energia, xarxa, càrrega i errors. Només s'activen en maquinari Raven |
| **MITJANA** | **Patró SSID WiFi `^Flock-[A-Z0-9]+$`** | Nom predeterminat del punt d'accés de configuració. Al microprogramari hi ha altres SSID com `FS Ext Battery`, `Penguin` i `Pigvision` |
| **MITJANA** | **Subcadena del nom del dispositiu BLE** | Noms com `FS Ext Battery` apareixen a les dades d'anunci i no requereixen analitzar dades del fabricant |
| **BAIXA** | **Coincidència de prefix MAC i OUI** | **És el mètode amb més soroll.** Els prefixos dels fabricants de components apareixen en milers de productes sense relació |

*La fila inferior correspon al senyal del qual depèn més el microprogramari actual. Aquest és el problema central de prioritzar les deteccions OUI.*

### Per què la llista OUI genera tant de soroll

Els 31 prefixos de la llista anterior no són 31 identificadors de Flock. WiFi Mothership manté un conjunt paral·lel de **26 prefixos i n'identifica el propietari real**, cosa que en mostra la composició.

| Classe | Quantitat | Propietari |
|-------|-------|-------|
| **Flock Safety** | **1** | `B4:1E:52`, assignat per l'IEEE a la mateixa empresa |
| **Mòduls de bateria** | 10 | Components de Silicon Labs en bateries ampliades |
| **Mòduls de càmera** | 11 | Mòduls de càmera WiFi de Liteon Technology |
| **Infraestructura de còmput** | 4 | Raspberry Pi Foundation i Raspberry Pi Trading |

**Vint-i-cinc d'aquests 26 prefixos pertanyen a fabricants de components**, i aquests components s'envien en grans quantitats per a maquinari sense relació amb Flock. Un prefix de bateries de Silicon Labs o d'un mòdul de càmera de Liteon apareix en productes sense cap vincle amb Flock Safety. Les plaques Raspberry Pi també són arreu.

**Una coincidència amb qualsevol d'aquests prefixos és una pista, no una identificació.** Per això l'empremta digital de la sonda comodí té tant de pes en el microprogramari actual. Combinar una coincidència OUI amb una sol·licitud de sonda SSID buida fa pujar la confiança d'una conjectura fins a 62 segons l'escala del mateix projecte.

*Només `B4:1E:52` respon per si sol la pregunta «és un dispositiu Flock?». Tracta els altres 30 prefixos com a indicis complementaris.*

### Quantes càmeres exposen un punt d'accés

Les dades de wardriving indiquen un mínim de dispositius. WiFi Mothership va comptar **900 punts d'accés Flock o més a WiGLE durant el 2025**. Un AP Flock és un dispositiu que emet el SSID de punt d'accés predeterminat `Flock-XXXX`.

Aquesta xifra descriu dispositius que exposen un punt d'accés de configuració, no pas el nombre total instal·lat. Flock afirma tenir desenes de milers de desplegaments, i la majoria d'aquestes càmeres no emeten res que un vehicle que passa pugui registrar amb wardriving. **El mapa és una mostra, i és petita.**

______

## Incidència 43: nou patró SSID, 5 GHz i antifingerprinting MAC

Tres mesos després del tancament de la incidència 20, va arribar un segon informe que descriu el que sembla una contramesura deliberada contra la detecció, més que no pas un canvi incidental del microprogramari. La **[incidència 43](https://github.com/colonelpanichacks/flock-you/issues/43)**, presentada el maig de 2026, es basa en dades de wardriving de WiGLE capturades al costat d'una càmera ja confirmada a DeFlock. Documenta tres fets que cap de les eines existents tenia en compte.

### Troballa 1: un format SSID diferent

El SSID documentat del punt d'accés Flock sempre havia seguit el patró `Flock-XXXXXX`. En aquest informe, la càmera emetia **`Flock Camera net.`**, una convenció de noms completament diferent. Qualsevol persona que cerqués a WiGLE amb el comodí `Flock-*`, com havien fet diversos investigadors, no n'hauria obtingut cap resultat tot i que la càmera emetia activament.

### Troballa 2: punt d'accés de 5 GHz confirmat

La mateixa càmera emetia alhora al **canal 1 de 2,4 GHz** i al **canal 157 de 5 GHz**, amb adreces MAC consecutives a cada banda (`...9f:a2:de` i `...9f:a2:df`). Això apunta a un únic mòdul WiFi de doble banda que assigna adreces adjacents a cada ràdio, no pas a dos dispositius sense relació. Un altre informe independent de l'investigador nsm_barii ja havia registrat una sol·licitud de sonda Flock al canal 149 de 5 GHz. Ara hi ha, doncs, dues observacions que confirmen que l'ús de 5 GHz és real i no una configuració errònia puntual.

**Tots els mètodes de detecció descrits abans en aquest article, inclòs el microprogramari actual de sondes comodí, només escolten la banda de 2,4 GHz.** Una càmera que emeti només a 5 GHz, o sobretot en aquesta banda, és invisible per a aquest maquinari encara que la llista OUI sigui correcta.

### Troballa 3: adreces MAC administrades localment al punt d'accés

Les dues adreces MAC capturades tenen activat el **bit d'administració local**, és a dir, no provenen del bloc OUI real de Flock registrat per l'IEEE. La lògica de detecció estàndard de `flock-you` omet expressament les adreces administrades localment, perquè és la manera habitual de filtrar telèfons i ordinadors portàtils que aleatoritzen l'adreça MAC.

**Aquest filtre, creat específicament per reduir els falsos positius, també elimina una càmera Flock que faci servir una MAC administrada localment a la interfície del punt d'accés.** Els últims bytes consecutius de les dues adreces capturades descarten que s'hagin generat a l'atzar. Això fa pensar en una assignació estructurada i intencionada, no pas en una coincidència.

| Troballa | Què continua funcionant |
|---|---|
| **Nou format SSID** (`Flock Camera net.`) | La coincidència de patrons SSID continua funcionant si s'amplia el patró de cerca |
| **Funcionament a 5 GHz** | Res del microprogramari WiFi actual, que només explora 2,4 GHz |
| **MAC administrada localment** | La coincidència per SSID, que no depèn de l'adreça MAC |

*La coincidència per SSID és l'únic mètode de la taula que continua funcionant independentment de la banda de la càmera o de com s'assigni la seva MAC. Aquesta és la raó pràctica per afegir més patrons SSID en lloc de dependre només de la coincidència OUI.*

______

## Flock evita deliberadament la detecció?

Cap de les dues incidències de GitHub demostra que hi hagi intencionalitat, i cal ser precisos. La persona que va obrir la incidència 43 va plantejar la qüestió com una pregunta oberta, no pas com una conclusió: passa a tots els desplegaments de Flock o només en una versió de microprogramari d'una càmera?

Però observa el patró conjunt de les dues incidències. Desapareix una superfície de detecció. La comunitat en troba una alternativa. Els punts cecs de l'alternativa (exploració només a 2,4 GHz, coincidència basada en OUI i filtratge de MAC administrades localment) encaixen amb les propietats que aprofitarien un SSID nou, una ràdio de 5 GHz i una adreça MAC administrada localment. **Podria ser una coincidència causada per un cicle d'actualització de microprogramari sense relació, o bé Flock podria estar reduint la seva empremta sense fils d'una manera que, intencionadament o no, trenca la detecció de tercers.**

*El més útil no és discutir quina explicació és la bona. És construir sistemes de detecció que no depenguin d'una sola suposició per sempre, perquè durant els dos anys de trajectòria d'aquest projecte cap no ha durat.*

### Confirmació visual: encès, però sense emetre

**[Un tercer vídeo curt de Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0) tanca el debat sobre si potser havien retirat la càmera.**

{{< youtube id="sjI8FB0cLk0" >}}

La persona que va fer el vídeo va tornar a la mateixa càmera del primer vídeo, de nit, i va confirmar visualment que **els LED IR continuaven encesos**. La unitat tenia corrent i il·luminava activament per captar imatges nocturnes. Alhora, **tots els microprogramaris personalitzats que van provar van registrar zero deteccions legítimes** d'aquella càmera. Un avís sí que es va activar, però es va confirmar que era un fals positiu. La càmera no transmetia res detectable per ràdio.

**Això separa clarament les dues explicacions possibles.** Que hagin arrencat o reubicat la càmera no explica que la unitat continuï encesa i il·lumini de nit. Una càmera activa, il·luminada i silenciosa amb tots els mètodes de detecció WiFi indica que el mateix senyal sense fils ha desaparegut, no que hagin retirat el maquinari.

La persona del vídeo també va explicar que, després de parlar amb altres desenvolupadors que investigaven el mateix problema, el resultat no era aïllat. **Diverses persones van observar el mateix patró més o menys alhora**, cosa que apunta a un canvi coordinat i nacional per part de Flock, no pas a un cas local. *Aquesta afirmació és anecdòtica i es basa en converses informals, no en un conjunt de dades publicat. Tanmateix, coincideix amb els períodes del desembre de 2025 i la primavera de 2026 que descriu la incidència 20. És el tipus d'informe que convé publicar en una incidència nova de GitHub, no deixar-lo en un fil de comentaris.*

______

## Què implica això per al teu maquinari de detecció

Si el teu dispositiu ha deixat de detectar càmeres, segueix aquesta llista abans de donar-lo per espatllat:

1. **Actualitza primer el microprogramari.** Si fas servir una versió anterior a la branca `main` actual, probablement encara busques l'AP de gestió desactivat o les balises BLE que ja no funcionen. Descarrega el microprogramari més recent i torna'l a instal·lar.
2. **Confirma que la càmera encara hi és.** Alguns informes de «zero deteccions» es devien a maquinari que realment s'havia arrencat o reubicat, no pas a una fallada de detecció. Abans de solucionar problemes al dispositiu, contrasta-ho amb **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** o **[DeFlock](https://deflock.org/)**.
3. **Redueix la velocitat a les cruïlles.** Amb 250 ms de permanència per canal, si passes de pressa pots travessar la finestra de detecció de la càmera abans que la ràdio arribi al canal correcte. Aturar-te entre 30 i 60 segons detecta moltes més càmeres que passar-hi ràpidament amb una antena més gran.
4. **Informa del que observes.** Un resultat de zero deteccions al costat d'una càmera confirmada visualment és exactament el tipus de dada que va donar lloc a les incidències 20 i 43. Obre una incidència nova en lloc de donar per fet que algú altre ja l'ha informat.
5. **Tingues presents les limitacions actuals.** Un microprogramari només WiFi i només de 2,4 GHz no veurà una càmera que hagi passat a 5 GHz o hagi deixat d'emetre a les bandes que explora. Ara mateix això és una limitació real, no una fallada de la teva versió concreta.

**Res d'això fa que el maquinari sigui inútil.** La llista OUI i l'empremta de la sonda comodí encara detecten avui la gran majoria de càmeres instal·lades. Vol dir que cal tractar qualsevol detector, fet a casa o comprat, com una instantània d'una cursa tecnològica que continua, no com una solució permanent.

{{< stscollective-ad "flockyou" >}}

______

## Una via paral·lela: detectar el flaix infraroig en lloc del senyal WiFi

La detecció sense fils no és l'únic front d'aquesta cursa. **[Un altre vídeo de seguiment](https://www.youtube.com/shorts/mzpr6bslsYA) de la mateixa persona, Valleytech Custom Solutions, descriu un mètode completament diferent**: en lloc d'escoltar un senyal de ràdio, observar l'il·luminador infraroig de la càmera.

{{< youtube id="mzpr6bslsYA" >}}

La majoria de càmeres ALPR, incloses les de Flock, fan servir **il·luminació infraroja per captar matrícules llegibles de nit**, igual que les càmeres de seguretat convencionals poden gravar a les fosques. L'ull humà no veu aquesta llum IR, però sí que la pot captar un sensor d'imatge sense filtre de tall d'infraroig. *Aquest detall de maquinari, la manca del filtre IR, és el que converteix un mòdul de càmera normal en un detector Flock.*

### Aspecte del prototip

El mètode mostrat al vídeo va passar per diverses iteracions abans d'arribar a una combinació pràctica:

- **Primer intent**: receptors amb fotodíodes IR dedicats. Funcionaven tècnicament, però les peces eren massa cares perquè fossin una opció pràctica de bricolatge.
- **Segon intent**: un **Jetson Nano combinat amb un mòdul de càmera Raspberry Pi**. Va demostrar que el concepte funcionava, però el cost i el consum elèctric del maquinari el feien poc pràctic per a un dispositiu de mà o instal·lat en un vehicle.
- **Muntatge actual**: un **mòdul de càmera amb ESP32 sense lent amb filtre IR**. La persona creadora va provar un **ESP32-CAM** i una **M5Stack S3 Cam** abans de triar el **Seeed Studio XIAO ESP32S3 Sense**, combinat amb un **mòdul GNSS Seeed XIAO amb xip Quectel L76K** per afegir coordenades GPS a les deteccions, seguint el mateix patró de wardriving amb GPS que ja utilitza el tauler Flask de `flock-you`, basat en WiFi.

| Requisit | Per què és important |
|---|---|
| **Mòdul de càmera sense filtre de tall IR** | El filtre que fa que les fotos normals tinguin colors fidels també bloqueja la llum que necessita detectar aquest mètode |
| **Una càmera en lloc d'un fotodíode** | Els receptors amb fotodíode capaços d'aïllar el senyal eren massa cars per a un projecte de bricolatge pràctic |
| **Registre GPS** | Associa les deteccions a una ubicació, com fa el tauler Flask del microprogramari WiFi |

### Patró de parpelleig de la càmera

El mètode depèn que l'il·luminador parpellegi seguint un patró repetitiu detectable, en lloc de quedar-se encès. La persona creadora va comunicar una **mesura pròpia d'uns 20 mil·lisegons encès i 80 mil·lisegons apagat: un període de 100 mil·lisegons, que equival a un cicle de treball del 20 % a 10 Hz**. Va deixar clar que la xifra no està verificada i podria ser incorrecta. *Tracta-la com un punt de partida per a les teves pròpies mesures, no com una especificació confirmada. Flock no l'ha publicat i la mateixa persona no n'ha afirmat la certesa.*

### Estat del projecte

**És un prototip inicial, només per a bricolatge, no pas un producte acabat.** La persona creadora va descriure el programari com a «programat de manera improvisada amb ajuda d'IA» i encara en desenvolupament. Té previst afegir un brunzidor per als avisos sonors, però encara no l'ha incorporat, i no hi ha cap placa empaquetada equivalent al maquinari OUI-SPY. La versió actual encara requereix que **una persona confirmi visualment** si una detecció assenyalada és una càmera real o una altra font de llum IR. Per tant, serveix com a eina de cribratge, no com a sistema totalment automatitzat.

*Aquesta és una superfície de detecció realment diferent de totes les altres d'aquest article. No depèn de WiFi, de 2,4 o 5 GHz, de la coincidència OUI ni del comportament de l'adreça MAC. Per tant, cap de les tècniques d'evasió de la incidència 43 no l'afecta. També té limitacions pròpies: necessita línia de visió, la llum del dia hi interfereix i el cicle de treball encara no s'ha confirmat de manera independent.*

______

## Què fa la comunitat

La resposta a les dues incidències va seguir el mateix patró que ha mantingut útil aquest projecte durant dos anys: algú informa d'una mancança, una altra persona aporta una solució i aquesta es publica com una actualització en lloc de quedar-se pendent.

- **La incidència 20** va acabar amb una causa arrel confirmada i una reescriptura del microprogramari basada en la signatura de la sonda comodí, gràcies a la recerca de camp de la comunitat DeFlockJoplin.
- **La incidència 43** continua oberta en el moment d'escriure aquest article. La proposta de fer coincidir patrons SSID encara està pendent d'implementació. *Si vols ajudar a resoldre aquesta mancança, afegir `Flock Camera` com a patró de coincidència addicional és una contribució petita i ben delimitada per a qui conegui la lògica de coincidència del microprogramari.*
- El conjunt de dades OUI subjacent té versions i dates al repositori. Les entrades descartades i les de poca confiança s'hi documenten, en lloc d'eliminar-les sense explicacions, perquè qui bifurqui el projecte pugui veure exactament què ha canviat i per què.

*Aquesta és l'avantatge pràctic de les eines de detecció de codi obert davant de les alternatives tancades. Ningú que trobi una mancança no pot corregir un detector propietari. En aquest projecte, la comunitat ja ho ha fet dues vegades.*

______

## L'altra resposta: endur-se el maquinari

La detecció sense fils és una resposta a aquestes càmeres. Una iniciativa paral·lela va actuar sobre el mateix maquinari i, el setembre de 2026, va produir les proves públiques més detallades fins ara sobre el funcionament intern d'una càmera Flock.

**El col·lectiu stegan0gram va retirar una càmera del pal, en va copiar l'emmagatzematge intern i en va publicar les imatges del sistema de fitxers a través de Distributed Denial of Secrets.** Descriuen la feina amb aquestes paraules:

> «Per què destruir-les si podem fer-ne enginyeria inversa i trobar els secrets dels qui ens espien? Vam alliberar el maquinari instal·lat al carrer, el vam desarmar i vam fer enginyeria inversa de les càmeres i dels equips solars associats.»

*La distinció és important. Destruir una càmera n'elimina una. L'enginyeria inversa produeix proves sobre totes.*

### Què va revelar la retirada

El conjunt de dades publicat inclou una **partició multimèdia de 18 GB**, una **imatge del sistema Android d'1,5 GB** i una **partició de credencials de 32 MB**, a més de la clau recuperada del contenidor multimèdia xifrat. Amb aquest material, els investigadors van establir la versió del sistema operatiu, la del nucli, les credencials del servidor codificades al sistema i els testimonis d'autenticació en text sense xifrar que emmagatzema la càmera.

Aquest conjunt de proves ara fonamenta la recerca de seguretat descrita a **[Vulnerabilitats de les càmeres Flock Safety: més de 50 errors trobats](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)**, que abans es basava en dispositius de laboratori i unitats comprades.

### La resposta a la retirada

La interferència física té conseqüències i la situació és mixta.

- **Han detingut diverses persones arreu del país** per presumptament manipular o sabotejar càmeres Flock.
- **Alguns municipis han anunciat que deixaran de fer servir càmeres Flock**, que és el resultat que volen els detractors d'aquestes càmeres.
- **Un departament de policia va fabricar una carcassa falsa de càmera Flock impresa en 3D** per atraure possibles vàndals i facilitar-ne la detenció.

Noel Pichardo, antic agent de policia de Pawtucket, Rhode Island, es va convertir en crític de Flock després de qüestionar l'ús d'aquestes càmeres pel seu departament. Argumenta directament contra el sabotatge. Va dir a WIRED que entén la frustració, però tem que aquesta tàctica tingui l'efecte contrari. «Crec que aquest tipus de vigilantisme només consolidarà la convicció de la policia i de l'estat en general que aquesta eina és necessària», va dir. «Com més temps l'estat ignori els laments dels seus constituents contraris a aquesta mena de vigilància, més passarà.»

### Quin lloc ocupa la detecció

El desmuntatge no canvia el problema de detecció que tracta aquest article. La càmera continua emetent de la mateixa manera, el microprogramari encara necessita la llista OUI i la signatura de sonda, i les dues interrupcions documentades continuen sent vàlides.

El bolcat afegeix **la confirmació de la identitat del maquinari**, inclosa la verificació d'una entrada OUI en una unitat real. També recorda quin tipus de pressió canvia els desplegaments. **Les càmeres desapareixen d'una ruta quan una votació municipal posa fi a un contracte, no perquè un detector quedi en silenci.** Les eines sense fils responen una pregunta personal sobre el que t'envolta. La lluita política respon la pregunta més gran, i el bolcat ha donat a aquesta lluita les proves més sòlides fins ara.

______

## Conclusió: la detecció és un objectiu mòbil, no una resposta definitiva

Que un detector quedi silenciós en una ruta on abans trobava càmeres no demostra que el maquinari hagi fallat. Indica que el senyal sense fils que havia d'identificar ha tornat a canviar, en un patró que ja s'ha repetit dues vegades en un sol any. **L'AP de gestió, les balises BLE i, ara potser, les suposicions de 2,4 GHz i OUI que incorpora el microprogramari actual** tenen una vida útil limitada.

**La solució mai no ha estat abandonar la detecció sense fils.** Ha estat mantenir visibles i documentades les suposicions del mètode, i permetre corregir-les quan arribi un altre informe com les incidències 20 i 43. Aquest és l'argument a favor del microprogramari de codi obert en lloc de qualsevol alternativa tancada: la solució es publica quan la comunitat troba la mancança, no quan ho decideix el proveïdor.

### Idees clau

- **Dues superfícies de detecció documentades ja han desaparegut**: l'AP WiFi de gestió (desactivat cap al desembre de 2025) i les balises BLE (poc fiables a la primavera de 2026).
- **El mètode actual combina sol·licituds de sonda comodí amb coincidència OUI i d'empremtes IE. Ha assolit una taxa de detecció verificada al camp d'11 de 12**, però només funciona amb WiFi i a 2,4 GHz.
- **Un informe pendent descriu un SSID nou, un punt d'accés confirmat de 5 GHz i adreces MAC administrades localment** que el mètode actual, basat en OUI i limitat a 2,4 GHz, no pot detectar.
- **Està apareixent un mètode alternatiu que no depèn de la ràdio**: un mòdul de càmera ESP32 sense filtre IR detecta l'il·luminador infraroig d'una càmera Flock. No depèn del WiFi i és immune a totes les tècniques d'evasió anteriors.
- **La confirmació visual corrobora el silenci sense fils**: una càmera que era clarament encesa i il·luminava de nit continuava sense registrar cap detecció WiFi legítima. Això descarta que «hagin retirat la càmera» com a explicació d'aquella unitat concreta.
- **Que un detector no trobi una càmera coneguda no vol dir automàticament que el maquinari estigui espatllat.** Primer actualitza el microprogramari i després confirma que la càmera encara sigui al lloc.
- **Aquest és un projecte de codi obert que continua publicant correccions quan la comunitat troba mancances.** Consulta les incidències de GitHub, no només el README, per conèixer l'estat actual de la detecció.

### Passos següents

1. **Actualitza el microprogramari** a la branca `main` actual abans de provar res més: **[github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)**
2. **Llegeix la guia completa de maquinari** si encara no ho has fet: **[Projecte de detecció Flock-You: guia de maquinari de contravigilància](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**
3. **Contrasta les zones mortes sospitoses** amb **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** abans de concloure que el teu dispositiu no ha detectat alguna cosa.
4. **Entén a què t'enfrontes**: **[Vigilància amb càmeres Flock Safety: extensió, problemes de privadesa i estratègies de protecció](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**
5. **Combina la detecció WiFi amb la detecció cel·lular** mitjançant **[Rayhunter](/articles/how-to-flash-rayhunter-devices-complete-guide/)** per tenir una visió més completa de la contravigilància, ja que cap dels mètodes d'aquest article detecta simuladors d'estacions base cel·lulars.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compra dispositius FlockYou preparats, estalvia un 20 %
{{< /centerbutton >}}

______

## Articles relacionats

| Article | Què explica |
|---------|---------------|
| **[Projecte de detecció Flock-You: guia de maquinari de contravigilància](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Guia tècnica completa de les tres plataformes de maquinari, la configuració del microprogramari i la metodologia de detecció que serveix de base a aquest article |
| **[Flock Finder: localitza totes les càmeres Flock sospitades a prop teu](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Contrasta una zona morta sospitosa amb més de 40.000 ubicacions de càmeres cartografiades abans de solucionar problemes del dispositiu |
| **[Càmeres Flock: eina de seguretat pública o màquina de vigilància sense ordre judicial?](/articles/flock-cameras-public-safety-or-surveillance-2026/)** | Anàlisi independent del que permet realment la base de dades de Flock i de per què la qüestió de l'ordre judicial és més important que la detecció |
| **[Vigilància amb càmeres Flock Safety: extensió, problemes de privadesa i estratègies de protecció](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Visió completa de l'abast del desplegament, els casos d'abús documentats i els recursos d'organització comunitària |
| **[Vulnerabilitats de les càmeres Flock Safety: més de 50 errors trobats](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)** | Recerca sobre la seguretat del maquinari i el programari de les càmeres Flock, independent del tema de detecció sense fils d'aquest article |
| **[Com instal·lar Rayhunter: guia completa](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Detecta capturadors IMSI i dispositius Stingray, l'equivalent cel·lular de la mancança de detecció WiFi descrita en aquest article |

______

## Referències

1. [Repositori de GitHub de Flock-You - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Incidència 20 de GitHub - No es detecten càmeres Flock, però sí altres dispositius](https://github.com/colonelpanichacks/flock-you/issues/20)
3. [Incidència 43 de GitHub - Senyal de 5 GHz? Filtratge OUI / adreça MAC nova](https://github.com/colonelpanichacks/flock-you/issues/43)
4. [Conjunt de dades de recerca OUI de NitekryDPaul](https://github.com/colonelpanichacks/flock-you/blob/main/datasets/NitekryDPaul_wifi_ouis.md)
5. [nitekry/nite-oui-collection](https://github.com/nitekry/nite-oui-collection)
6. [DeFlock Joplin - Recerca comunitària sobre ALPR](https://deflockjoplin.today)
7. [Pintor, L. i Atzori, L. (2022) - Anàlisi de sol·licituds de sonda WiFi per empremta digital d'elements d'informació, IEEE GLOBECOM](https://ieeexplore.ieee.org/document/10001618)
8. [WIRED i 404 Media - Pirates han accedit a una càmera Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
9. [Micah Lee - Les càmeres Flock són plenes de vulnerabilitats i credencials codificades](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
10. [Distributed Denial of Secrets - Imatges del sistema de fitxers d'una càmera Flock ALPR](https://ddosecrets.org/article/flock-alpr-camera)
11. [Hackaday - Aquesta setmana en seguretat: les càmeres Flock són antigues; Microsoft corregeix les correccions i investigadors ataquen SSH](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
12. [WiFi Mothership - Referència de dispositius i detecció ALPR de Flock Safety](https://wifimothership.com/flock)
13. [GainSec - Recerca de microprogramari i avisos de seguretat](https://gainsec.com/)
8. [La cerca de la sonda oculta - Comportament de les sol·licituds de sonda comodí amb SSID ocult](https://goodwi.fi/posts/2023/12/hunt-for-hidden-probe/)
9. [DeFlock - Mapa col·laboratiu de càmeres ALPR](https://deflock.org/)
10. [Colonel Panic Tech - OUI-SPY i maquinari de detecció](https://colonelpanic.tech)
11. [STS Collective - Dispositius FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
12. [Passa una cosa estranya amb les càmeres Flock - Valleytech Custom Solutions](https://www.youtube.com/shorts/cVf-id71BuQ)
13. [Wardriving infraroig de càmeres Flock - Valleytech Custom Solutions](https://www.youtube.com/shorts/mzpr6bslsYA)
14. [Les càmeres Flock continuen enceses però no emeten - Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0)
15. [Reconeixement automàtic de matrícules - Wikipedia (il·luminació infraroja en sistemes ANPR/ALPR)](https://en.wikipedia.org/wiki/Automatic_number-plate_recognition)
16. [Seeed Studio XIAO ESP32S3 Sense](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html)
17. [Mòdul GNSS L76K per a Seeed Studio XIAO](https://www.seeedstudio.com/L76K-GNSS-Module-for-Seeed-Studio-XIAO-p-5864.html)

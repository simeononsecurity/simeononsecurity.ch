---
title: "Vam mapar 146.526 «càmeres Flock». 50.278 eren sistemes ClickShare"
date: 2026-09-21
lastmod: 2026-11-14
toc: true
draft: false
description: "Una auditoria de Flock Finder identifica ClickShare i altres falsos positius, explica les proves i documenta els canvis."
genre: ["Recerca de seguretat", "Tecnologia de privadesa", "Projectes de codi obert", "Periodisme de dades", "Contravigilància"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Empremta OUI", "WiGLE", "Falsos positius", "Qualitat de les dades", "Barco ClickShare", "Adreça MAC", "IEEE OUI", "Empremta dels elements d'informació", "ESP32", "Flock-You", "NitekryDPaul", "DeFlockJoplin", "Responsabilitat de codi obert", "Mapatge de vigilància", "WiFi", "Sol·licitud de sondeig", "Aleatorització MAC"]
cover: "/img/cover/flock-finder-oui-false-positive-audit-2026.webp"
coverAlt: "Un mapa urbà fosc ple de marcadors vermells que corresponen a dispositius WiFi d'oficina, mentre que uns pocs marcadors verds indiquen deteccions més sòlides"
coverCaption: "L'auditoria de 146.526 registres de Flock Finder va mostrar com una observació de camp útil es va convertir en una afirmació cartogràfica massa segura."
canonical: "https://simeononsecurity.com/articles/flock-finder-oui-false-positive-audit-2026/"
---

**Vam posar 146.526 punts en un mapa de càmeres de vigilància. Com a mínim 50.278 eren sistemes de presentació Barco ClickShare. El maquinari de sales de conferències representava més d'un terç del que el nostre titular anomenava «càmeres mapejades».**

Era el nostre projecte, la nostra canalització de dades i el nostre error. Flock Finder consultava WiGLE cada dia per trobar prefixos MAC observats en càmeres Flock Safety, publicava els resultats amb coordenades de precisió completa i els representava com a marcadors equivalents. Les metadades contenien la paraula `suspected` i la documentació esmentava falsos positius. Tot i això, el mapa i el titular transmetien certesa.

**Resultat per al lector:** reprodueix l'auditoria, separa observació i atribució i mostra el nivell de confiança al marcador i al titular. Una coincidència de prefix és una pista per investigar, no una prova que sigui una càmera.

Quan vam calcular un histograma de freqüències de la columna SSID, el conjunt de dades va explicar l'error en pocs minuts. ClickShare era només la categoria més gran. Altres 6.099 registres es deien `SMARTGATE_*`, 3.801 començaven amb el prefix genèric WiFi Direct `DIRECT-`, 314 tenien exactament el nom `AndroidAP`, 138 deien `Audi HUD`, 133, `MAX-PRINTER`, i 30 contenien la cadena de veredicte d'un altre detector. En total, **60.793 files, o el 41,5%, seguien les regles conegudes de noms d'altres dispositius de l'auditoria original.**

Ara Flock Finder publica una classe d'evidència per registre, exclou per defecte del mapa i del titular el maquinari conegut com a aliè, mostra filtres, marca els registres fora del mercat principal i separa els prefixos d'alta confiança dels prefixos de fabricants per contracte. Aquest article documenta l'error, les proves i els límits que encara queden.

______

## Com funciona la detecció comunitària d'ALPR

Els detectors Flock creats per la comunitat acostumen a combinar tres tipus de proves sense fil:

1. **Prefixos WiFi MAC/OUI.** Els primers bytes d'una adreça MAC administrada globalment poden identificar l'organització que va rebre el bloc d'adreces.
2. **Comportament WiFi.** Un SSID, una sol·licitud de sondeig comodí, l'adreça del destinatari, un patró de canal o una seqüència d'elements d'informació 802.11 poden acotar la classe del dispositiu.
3. **Proves Bluetooth.** Els identificadors de fabricant i els UUID de servei poden identificar ràdios exposades per un producte o una generació de microprogramari.

La coincidència OUI es va estendre perquè és barata i passiva. Un ESP32 assequible pot examinar trames 802.11 properes sense connectar-se a una xarxa. Una base històrica com [WiGLE](https://wigle.net/) també permet cercar observacions anteriors sense desplegar escàners propis.

El mètode va seguir una línia comunitària: el mapatge i l'organització local de [DeFlock](https://deflock.org/), [colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you), bifurcacions i projectes complementaris, com el nostre [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32), i, finalment, [Flock Finder](https://github.com/simeononsecurity/flock-finder), que va aplicar la llista de prefixos a dades globals de WiGLE.

El treball de camp original mereix un reconeixement clar. [@NitekryDPaul](https://github.com/NitekryDPaul) va observar 30 prefixos en equips Flock reals amb recerca en mode promiscu. [DeFlockJoplin](https://github.com/DeflockJoplin/flock-you) en va aportar un més durant proves de camp. Aquelles observacions eren legítimes. El nostre error posterior va ser tractar **«observat en una càmera Flock» com si volgués dir «exclusiu de les càmeres Flock».**

______

## El defecte estructural: un OUI descriu la cadena de subministrament

IEEE descriu un OUI com un identificador de 24 bits assignat a un proveïdor, fabricant o altra organització. Juntament amb uns altres 24 bits triats pel destinatari, forma una adreça MAC. La [IEEE Registration Authority](https://standards.ieee.org/products-programs/regauth/) publica el registre.

Això indica qui va rebre un bloc d'adreces. No necessàriament indica la marca del producte acabat. Els fabricants per contracte creen mòduls de ràdio per a molts clients. Un mateix proveïdor de xips pot aparèixer en càmeres, projectors, impressores, vehicles i plaques per a aficionats.

Les assignacions del registre que hi havia darrere la nostra llista feien visible el risc:

| Registrant | Prefixos a la llista auditada |
|---|---|
| Liteon Technology | `74:4C:A1`, `F4:6A:DD`, `9C:2F:9D`, `C0:35:32`, `E4:AA:EA`, `14:5A:FC` i altres |
| Universal Global Scientific Industrial (USI) | `E0:4F:43`, `08:3A:88` |
| Espressif | `A4:CF:12`, `3C:71:BF` |
| Silicon Laboratories | `58:8E:81`, `90:35:EA`, `EC:1B:BD` |
| Flock Safety | `B4:1E:52` |

Les entrades d'Espressif ens haurien d'haver alertat. Dos prefixos d'una suposada llista de càmeres pertanyien al fabricant d'una de les plataformes WiFi integrades més comunes del món, inclòs el silici emprat per molts detectors comunitaris.

`B4:1E:52` és diferent perquè està registrat directament a Flock Safety. Es va afegir a la llista de 38 prefixos al commit auditat, **però encara no s'havia consultat**: `scan_stats.json` informava de 31 prefixos consultats. El mateix passava amb sis prefixos de bateries afegits de nou. Per tant, la instantània no demostra si el prefix propi de Flock és habitual o rar. No convertirem «no consultat» en «zero resultats».

El repositori actual té 39 prefixos després d'afegir `E0:0A:F6` per equiparar-lo al microprogramari del detector. El resum d'escaneig conservat encara mostra dades de 31 prefixos. Els elements nous esperen un recàlcul complet i no són prefixos amb zero resultats demostrats.

______

## El conjunt de dades es va auditar sol

Cada xifra històrica que apareix a continuació es va regenerar des de `data/flock_cameras.csv` al commit de Flock Finder [`5551829`](https://github.com/simeononsecurity/flock-finder/tree/5551829), amb `csv` i `collections.Counter` de la biblioteca estàndard de Python. No calia fer una nova prova de conducció. Els noms, la geografia i la composició dels prefixos ja contradeien el titular. Les xifres sobre la implementació corregida provenen del resum `scan_stats.json` conservat al repositori actual.

### La geografia va ser un avís primerenc

De 146.526 files, 75.818 eren als Estats Units, 70.674 fora dels Estats Units i 34 no tenien país. Alemanya sumava 13.491 registres, seguida pel Canadà amb 6.251, França amb 5.839, la Gran Bretanya amb 4.836, els Països Baixos amb 4.636 i Suïssa amb 4.515.

{{< figure src="flock-finder-us-non-us-split.webp" alt="Barra apilada amb 75.818 registres dels Estats Units, 70.674 de fora dels Estats Units i 34 sense valor de país" caption="L'histograma de països suma 146.492 perquè 34 files tenen el país nul." >}}

La geografia és un senyal de selecció, no una prova. Flock descriu la seva xarxa com a «nacional» i diu que connecta clients a [49 estats dels EUA](https://www.flocksafety.com/flock-ecosystem). L'expansió internacional també pot canviar els límits del mercat. Per això marquem les files fora del mercat perquè es revisin en lloc d'esborrar-les o declarar falsos tots els registres de fora dels EUA.

La conclusió prudent ja és suficient: gairebé la meitat dels registres era fora del mercat principal nord-americà del projecte. Sense un altre senyal, no es podia considerar igual de plausible una coincidència OUI mundial.

### Més de 60.000 dispositius es van identificar pel nom

| Família SSID de l'auditoria original | Registres | Percentatge | Què indica el nom |
|---|---:|---:|---|
| Conté `ClickShare` | 50.278 | 34,3% | Maquinari de presentació sense fil Barco |
| `SMARTGATE_*` | 6.099 | 4,2% | Família de passarel·les o dispositius tipus OBD |
| `DIRECT-*` | 3.801 | 2,6% | Dispositius WiFi Direct com impressores, televisors i adaptadors |
| Nom exacte `AndroidAP` | 314 | 0,2% | Punts d'accés Android |
| Nom exacte `Audi HUD` | 138 | 0,1% | WiFi d'infoentreteniment o pantalla frontal Audi |
| Nom exacte `MAX-PRINTER` | 133 | 0,1% | Impressores d'oficina |
| `Flock ALPR [...]` | 30 | <0,1% | Veredicte d'un altre detector emmagatzemat com a SSID |
| **Total de l'auditoria original** | **60.793** | **41,5%** | Identificables com un altre maquinari o sortida de detector |

La documentació de suport de Barco diu que el nom de xarxa per defecte d'una unitat base ClickShare és [`ClickShare-<serial base number>`](https://www.barco.com/en/support/knowledge-base/2675-how-to-connect-to-your-clickshare-base-unit-wifi). Això confirma la família del producte amb una font primària, sense inferències a partir de la geografia o del registre del proveïdor.

El classificador de producció va substituir les comprovacions de nom exacte per expressions regulars que no distingeixen majúscules i minúscules. Inclou ClickShare, SmartGate, WiFi Direct, AndroidAP, Audi HUD, MAX-PRINTER i etiquetes de sortida de detectors. A les mateixes 146.526 files, detecta 629 variants d'AndroidAP, 139 d'Audi HUD i 134 de MAX-PRINTER. Per això, el repositori actual informa de **61.110 registres `identified_other`**, una mica més que els 60.793 de l'auditoria original.

### El senyal de confirmació era només del 2,4%

Només **3.502 files** tenien un SSID autèntic amb patró Flock. Altres 24.964 no tenien SSID. La resta identificava altres equips o combinava un OUI amb un nom no classificat.

Les 3.502 files confirmades contenien 161 variants reals de SSID: 3.342 casos del nom simple `Flock`, 157 noms de configuració únics `Flock-XXXXXX` o `FLOCK-XXXXXX`, i tres noms més que contenien `flock`. Un recompte anterior de 166 variants al README incloïa cinc cadenes d'anotació del detector `Flock ALPR [...]`. Aquestes cinc són proves del detector, no de la càmera.

{{< figure src="flock-finder-evidence-class-breakdown.webp" alt="Barra apilada al 100% que divideix 146.526 registres en 3.502 confirmats per SSID, 57.267 anomenats no classificats, 24.964 només amb OUI ocult, 60.763 identificats com altres i 30 retorns del detector" caption="L'antic titular reduïa cinc classes d'evidència substancialment diferents a un sol recompte." >}}

### La qualitat dels prefixos variava molt

La taxa de falsos positius no era uniforme. Alguns prefixos mantenien un senyal Flock útil. D'altres estaven dominats per dispositius d'oficina o consum amb nom.

{{< figure src="flock-finder-per-oui-composition.webp" alt="Barres apilades horitzontals de 31 prefixos OUI: SSID Flock verds, SSID coneguts d'altres dispositius vermells, SSID ocults gris clar i registres no classificats gris fosc" caption="Els prefixos més grans sovint contenien més dispositius coneguts com a altres. Xifres de la instantània d'auditoria de 146.526 files." >}}

Compara dos prefixos que el mapa antic etiquetava igual:

- `70:C9:4E` tenia 495 files: 133 noms amb patró Flock i 29 noms coneguts d'altres dispositius.
- `74:4C:A1` tenia 11.872 files: 211 noms amb patró Flock i 8.385 noms coneguts d'altres dispositius.

{{< figure src="flock-finder-prefix-signal-contrast.webp" alt="Comparació: prefix 70 C9 4E amb un 26,9% de SSID Flock i un 5,9% conegut com a altres, prefix 74 4C A1 amb un 1,8% de SSID Flock i un 70,6% conegut com a altres" caption="Una etiqueta única amagava proporcions de senyal i soroll oposades." >}}

El mateix patró apareix en els grups més grans: `F4:6A:DD` tenia 8.422 noms coneguts d'altres dispositius davant de 327 noms Flock, `D0:39:57` en tenia 8.270 davant de 473, i `E0:4F:43` incloïa 6.238 noms coneguts d'altres davant de 66 noms Flock. El volum d'un prefix no demostrava la qualitat de les proves.

______

## El bucle de retroalimentació ocult en 30 files

Trenta registres de Texas tenien SSID que eren clarament la sortida d'un altre detector:

| Etiqueta del detector desada com a SSID | Confiança indicada per l'eina | Registres |
|---|---:|---:|
| `Flock ALPR [wifi_receiver_oui;low]` | baixa | 20 |
| `Flock ALPR [wifi_oui_wildcard_probe;medium]` | mitjana | 4 |
| `Flock ALPR [wifi_bssid_oui;low]` | baixa | 3 |
| `Flock ALPR [flock_receiver_oui;low]` | baixa | 2 |
| `Flock ALPR [wifi_hidden_ssid_oui;low]` | baixa | 1 |

L'eina que els va crear va marcar 26 dels 30 com a baixa confiança. Una càrrega a WiGLE va desar després el veredicte de l'eina al camp SSID. La nostra canalització va trobar la paraula `Flock` i podria haver tractat l'etiqueta com una confirmació independent.

Trenta files són poques estadísticament. El mecanisme és rellevant: les eines que comparteixen una base de dades col·laborativa poden ingerir els resultats de les altres i convertir una suposició de baixa confiança en una corroboració aparent. La correcció exclou tot el patró `Flock ALPR [` abans de cercar la subcadena de confirmació `flock`.

______

## On ens vam equivocar

El titular del README deia **«Càmeres mapejades | 146.526»**. El mapa publicava coordenades de precisió completa i mostrava cada resultat amb el mateix tipus de marcador. S'actualitzava segons una programació de GitHub Actions, cosa que feia semblar que una heurística feble era un inventari mantingut.

Sí que hi havia matisos. Cada element tenia `match_confidence: "suspected"`. El README esmentava ClickShare com a possible dispositiu coexistint i el projecte mantenia una pista separada per als candidats trobats via SSID. Aquests matisos no governaven el recompte, el marcador ni la vista per defecte que veien els lectors.

Al text fèiem reserves, però al titular donàvem una xifra. El mapa feia la afirmació.

La part més evitable és que el microprogramari de [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32) ja separava identificadors d'alta confiança dels de fabricants per contracte i puntuava les proves febles per sota del llindar d'alerta. El concepte existia dins la mateixa organització, però la canalització cartogràfica no el va heretar.

Vam trobar l'abast de l'error amb un histograma de la nostra pròpia columna SSID. Va caldre pocs minuts. Cada dia publicàvem 146.526 files de proves en contra de la nostra presentació.

______

## Què vam canviar

La correcció està implementada en el model de dades i la interfície de Flock Finder:

- **Evidència per registre:** `ssid_confirmed`, `oui_high`, `oui_mfr` o `identified_other`.
- **Nivells OUI:** els prefixos es divideixen entre alta confiança observada al camp i nivells compartits de fabricants per contracte.
- **Exclusió de dispositius coneguts com a altres:** ClickShare, SmartGate, WiFi Direct, punts d'accés Android, Audi HUD, MAX-PRINTER i SSID de sortida de detectors queden exclosos per defecte del mapa i del titular.
- **Incertesa visible:** colors dels marcadors, finestres emergents, recomptes i filtres mostren la classe d'evidència.
- **Marca de mercat:** els registres fora del mercat principal dels EUA tenen `out_of_market: true` i continuen disponibles per revisar.
- **Titular desglossat:** 3.502 confirmats per SSID, 73.691 sospitosos per OUI d'alt nivell, 8.223 sospitosos per OUI de fabricants per contracte i 61.110 identificats com a altres.

El recompte corregit útil per actuar és **85.416**, i encara inclou 81.914 coincidències OUI no confirmades. És un recompte defensable del que supera les regles actuals, no un inventari verificat de càmeres.

`identified_other` també és un classificador operatiu, no un oracle. ClickShare té documentació primària sòlida sobre el seu SSID per defecte, mentre que un patró ampli com `DIRECT-` descriu una convenció de noms WiFi Direct usada per moltes classes de productes. Publicar la regla coincident i el camp `blocked_reason` permet als investigadors auditar aquestes exclusions i revisar-les quan millorin les proves.

### La resposta a llarg termini és l'empremta del microprogramari

La classificació OUI limita els danys, però no converteix un prefix compartit de fabricant en un identificador específic d'un producte. Una via més sòlida és l'estructura ordenada dels elements d'informació de les sol·licituds de sondeig 802.11. El treball precedent documenta aquesta signatura TLV:

```text
2,12,127,221:506f9a16030103,45,191,221:0050f208000000
```

Aquesta seqüència descriu el comportament d'una pila de microprogramari concreta, no qui és propietari d'un bloc MAC. L'empremta de sol·licituds de sondeig és una tècnica establerta per identificar dispositius. [La recerca publicada sobre empremta de la capa MAC 802.11](https://doi.org/10.1155/2017/6235484) mostra que els elements d'informació de les sol·licituds poden continuar identificant el dispositiu quan les MAC roten. També tracta l'error concret informat a [flock-you issue #43](https://github.com/colonelpanichacks/flock-you/issues/43): `Flock Camera net.` apareix en adreces MAC administrades localment i seqüencials a les bandes de 2,4 i 5 GHz.

La signatura encara necessita validació de camp independent entre maquinari i versions de microprogramari, i les captures malformades exigeixen anàlisi defensiva. Tot i així, és el camí correcte. La randomització MAC fa que la coincidència basada només en OUI sigui un carreró sense sortida anunciat.

______

## Per què importa més enllà d'un repositori

La gent fa servir mapes de vigilància per decidir on conduir, aparcar, denunciar, investigar i organitzar-se. Un marcador fals desvia l'atenció. Desenes de milers de marcadors falsos poden desacreditar les observacions precises del costat.

També hi ha una asimetria de credibilitat. A un proveïdor o crític li cal un únic marcador ClickShare demostrablement fals per qüestionar tot el conjunt de dades. Nosaltres en vam aportar 50.278. Periodistes i grups de defensa poden repetir un titular clar més de pressa del que arriba una correcció.

La transparència de codi obert guanya confiança amb mètodes inspeccionables i incertesa visible. Publicar les dades brutes va ajudar a revelar l'error, però l'accés a les dades no justificava una interfície que exagerés la conclusió. La correcció ha d'aparèixer allà on el lector troba l'afirmació: camp, filtre, marcador, llegenda i titular.

### Una petició a tots els mapes Flock i ALPR

Els altres projectes de mapatge Flock i ALPR també haurien d'auditar els seus conjunts de dades. És una invitació a comparar mètodes, no una acusació que tots els mapes hagin heretat el nostre error.

[WiGLE](https://www.wigle.net/stats/) és el conjunt públic d'observacions WiFi amb cerca global més ampli que coneixem. Aquest abast va fer atractiu Flock Finder: una API podia convertir una llista de signatures estudiades al camp en un mapa mundial. També va fer que l'error fos prou gran per mesurar-lo. Una base global retorna tots els productes aliens que comparteixen l'espai d'adreces d'un proveïdor de ràdio, no només el producte que va motivar la consulta.

Altres mapes fan servir proves diferents. Alguns depenen de fotografies i observacions de camp voluntàries. D'altres importen etiquetes de vigilància d'OpenStreetMap, registres públics, declaracions de proveïdors o dades d'un altre projecte comunitari. Els seus totals no són directament comparables als nostres resultats WiGLE, i la taxa del 2,4% confirmada per SSID no s'ha de projectar sobre dades verificades al camp. El risc comú és que la classificació d'un projecte arribi a les dades d'origen d'un altre i sembli una corroboració independent.

Tot mapa públic hauria de poder respondre una auditoria breu:

1. **Què significa un marcador?** Un dispositiu fotografiat, un registre governamental, una coincidència OUI, un informe d'usuari o una importació d'un altre mapa?
2. **Quants registres tenen proves directes del producte?** Publica els recomptes per classe d'evidència en lloc d'un únic total agregat de càmeres.
3. **Quines fonts són independents?** Segueix la procedència de les importacions perquè una observació no compti com diverses confirmacions.
4. **Què contradiu la classificació?** Calcula taules de freqüència de SSID, proveïdors, països, etiquetes de col·laboradors i altres camps categòrics.
5. **Com es representen la incertesa i les disputes?** Mostra confiança i estat de correcció als marcadors, filtres, exportacions i titulars.
6. **Un altre investigador pot reproduir el recompte?** Publica la consulta, la instantània d'origen, les regles de classificació i la data.

Aquesta auditoria no redueix el problema Flock. Una xarxa de càmeres ALPR encara pot registrar desplaçaments, permetre cerques entre jurisdiccions i afectar persones que mai no van consentir la recollida. Els recomptes precisos fan que aquesta crítica sigui més difícil de descartar. Si qüestionem sistemes de vigilància, els mapes han de distingir què hem observat, inferit i confirmat.

Vam cometre un error ben informat. Els prefixos provenien de recerca de camp legítima, la canalització era reproduïble i els matisos eren reals. Tot i així, la inferència superava les proves. Les bones intencions i les bones dades d'entrada no eliminen l'obligació de provar els resultats d'un sistema a escala.

______

## Reprodueix l'auditoria

Fes checkout del commit `5551829` i executa això des de l'arrel del repositori. Només fa servir la biblioteca estàndard de Python i imprimeix el total, la geografia, els SSID habituals i algunes famílies de dispositius identificades pel nom.

```bash
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder
git checkout 5551829

python3 - <<'PY'
import csv
from collections import Counter

with open("data/flock_cameras.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

ssids = Counter((row["ssid"] or "").strip() for row in rows)
countries = Counter((row["country"] or "").strip() for row in rows)

families = {
    "clickshare": lambda s: "clickshare" in s.lower(),
    "smartgate": lambda s: s.lower().startswith("smartgate_"),
    "direct": lambda s: s.lower().startswith("direct-"),
    "androidap": lambda s: s.lower().startswith("androidap"),
    "detector_output": lambda s: s.lower().startswith("flock alpr ["),
}

print("files", len(rows))
print("EUA", countries["US"])
print("fora dels EUA", sum(countries.values()) - countries["US"] - countries[""])
print("país absent", countries[""])
print("SSID principals", ssids.most_common(20))
for name, matches in families.items():
    print(name, sum(matches(ssid) for ssid in ssids.elements()))
PY
```

Per reproduir l'entrada històrica exacta, fes servir el CSV d'aquell commit, no un conjunt actual generat. Després de l'auditoria, el projecte va deixar d'incloure al Git el CSV gran, el GeoJSON i els fitxers per OUI, perquè cada escaneig reescrivia centenars de megabytes i feia créixer molt el repositori. Les dades generades actuals es restauren i publiquen a la versió contínua [`data-latest`](https://github.com/simeononsecurity/flock-finder/releases/tag/data-latest). El resum petit `scan_stats.json` continua al Git. Que falti un fitxer generat a la branca actual no vol dir que s'hagin esborrat les proves històriques ni que el recompte sigui zero.

______

## La lliçó

**Una heurística marcada com a «sospitada» a les metadades però mostrada com un marcador segur al mapa és una afirmació.** L'etiqueta ha de formar part del model de dades i de la visualització, no només de la documentació.


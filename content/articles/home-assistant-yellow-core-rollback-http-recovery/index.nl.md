---
title: 'Terugval van Home Assistant Core 2026.11 naar 2026.10.4: HTTP-opslagversie 3 herstellen'
date: 2026-11-15
lastmod: 2026-11-27
toc: true
draft: false
description: Herstel de fout over HTTP-opslagversie 3 nadat Home Assistant Core 2026.11 op Yellow is teruggevallen naar 2026.10.4.
  Met beveiligde opdrachten en gecontroleerde uitvoer.
genre:
- Huisautomatisering
- Probleemoplossing
tags:
- Home Assistant Yellow
- Home Assistant OS
- Terugval van Core 2026.11
- Core 2026.10.4
- HTTP-opslagversie 3
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: Illustratie van een geel computerbord, een verbroken configuratiekoppeling en een hersteld webdashboard
coverCaption: ''
---

Een mislukte update van Home Assistant Core 2026.11 zette mijn Yellow CM4 terug naar 2026.10.4. Yellow bleef bereikbaar via het netwerk, maar toonde het dashboard niet meer. Door de terugval bleef een HTTP-instellingenbestand met opslagversie 3.1 achter, terwijl Core 2026.10.4 versie 2.2 ondersteunt. Ik bewaarde het bestand, zette een kopie met strenge controles om, herstelde de HTTP-toegang en werkte Core daarna bij naar 2026.11.1.

<!--more-->

## Belangrijkste punten

- **Bevestig de mismatch.** Vergelijk de Core-logfout met de geïnstalleerde versie en de HTTP-opslagversie.
- **Bewaar het bestand.** Houd vóór herstel een ongewijzigde kopie en een back-up buiten het apparaat aan.
- **Controleer het resultaat.** Controleer de Core-status, de opgeslagen luisterpoort, het dashboard en de geïnstalleerde versie.

**Oplossing voor precies dit geval:** [Bewaar het HTTP-bestand](#preserve-recovery-options), [maak en valideer een kandidaat voor versie 2.2](#apply-the-tested-fix-for-version-31), [installeer deze nadat Core is gestopt](#apply-the-tested-fix-for-version-31) en [controleer het resultaat van de update](#verify-the-update-outcome). De omzetting controleert de oorspronkelijke velden en stopt bij afwijkingen. Pas deze niet toe op een niet-geïnspecteerd HTTP-bestand.

## Voordat je begint

Je hebt fysieke toegang tot een Yellow CM4 nodig, een USB-C-datakabel, een werkende seriële console en een bruikbare back-up of bewaarde configuratie. De handmatige route vereist toegang tot de hostshell en een zorgvuldige controle van de JSON. Trek minstens 30 minuten uit voor diagnose en reparatie. Core opstarten en back-ups terugzetten duurt bij grote installaties langer.

## Herken de storing

De doorslaggevende fout stond in het Core-log:

```text
Storage file http has version 3 which is newer than the max supported version 2
```

De oudere Core-versie kon `http` niet laden. Ook de frontend en andere componenten die van HTTP afhankelijk zijn, vielen uit. Een routerlease en een werkende Observer-pagina bewezen niet dat het dashboard bereikbaar was. [Probleem #190583 in Home Assistant Core](https://github.com/home-assistant/core/issues/190583) beschrijft dezelfde terugvalfout op meerdere installaties, waaronder Yellow. [Mijn opmerking bij het issue](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) legt het geteste herstel op deze Yellow en de uiteindelijke Core-status vast.

**Oorzaak van de webstoring:** Core 2026.11 schreef `.storage/http` in indeling 3.1. De terugval herstelde Core 2026.10.4, maar niet een compatibel HTTP-bestand. Core 2026.10.4 weigert opslagversie 3. Ook het opgeslagen profiel `intermediate_v6` op deze Yellow past niet bij het oudere schema. Waarom de eerste update mislukte en de terugval startte, is onbekend. Op 2026-11-15 stond het gekoppelde issue nog open en bevatte de discussie geen door beheerders bevestigde oplossing.

Controleer de geïnstalleerde Core-versie en de HTTP-opslag voordat je bestanden wijzigt:

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

De onderstaande uitvoer toont deze situatie, met tijdstempels en privégegevens verwijderd:

```text
2026.10.4
{
  "version": 3,
  "minor_version": 1,
  "pending_present": false,
  "profile": "intermediate_v6"
}
Storage file http has version 3 which is newer than the max supported version 2
```

De herstelopdrachten vergelijken de door Supervisor opgeslagen luisterpoort met het HTTP-bestand zonder een van beide waarden weer te geven. Controleer bij een mismatch de werkelijke Core-luisterpoort voordat je bestanden wijzigt.

| Signaal | Betekenis |
| --- | --- |
| Core ondersteunt opslagversie 2, het bestand meldt versie 3 | De oudere versie kan de opgeslagen HTTP-instellingen niet laden |
| Het HTTP-bestand en de Supervisor-lijst tonen verschillende luisterpoorten | Controleer de werkelijke Core-luisterpoort voordat je de oorzaak vaststelt |
| De startpagina reageert, maar Core heeft nog de status STARTING | Een reactie van de frontend bewijst niet dat het opstarten voltooid is |

## Behoud herstelopties {#preserve-recovery-options}

Bewaar vóór een volgende update een bruikbare back-up buiten Yellow. [De back-upgids van Home Assistant](https://www.home-assistant.io/common-tasks/general/backups/) beschrijft cloudlocaties en opslag buiten het apparaat. Voor een versleutelde back-up heb je de bijbehorende herstelsleutel nodig. Wis de NVMe-gegevensschijf niet terwijl je deze opslagmismatch onderzoekt.

Kopieer het HTTP-bestand voordat je het bewerkt:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

Stop als de opdracht mislukt. Laat een eerdere herstelkopie met dezelfde naam ongemoeid. Kies een nieuwe naam en herhaal de controle voordat je verdergaat.

Gebruik de seriële console van Yellow wanneer het dashboard niet beschikbaar is. [De Nabu Casa-gids voor Linux en macOS](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) toont de USB-C-aansluiting en de positie van de JP1-UART. Volg de CM4-instructies voor jouw hardware.

## Pas de geteste oplossing voor versie 3.1 toe {#apply-the-tested-fix-for-version-31}

De voorkeur gaat uit naar een compatibel HTTP-bestand van vóór de update. Zet de back-up terug volgens de gedocumenteerde Home Assistant-procedure wanneer een volledige terugzetactie geschikt is. Als je één bestand uitpakt, bevestig dan de opslagversie en opgeslagen luisterpoort voordat je het actieve bestand vervangt. De onderstaande opdrachten vormen de directe oplossing die op deze Yellow is getest toen er geen compatibel HTTP-bestand beschikbaar was.

De [oorspronkelijke tijdelijke oplossing bij het issue](https://github.com/home-assistant/core/issues/190583) verplaatst `.storage/http` en laat de oudere Core een nieuw bestand maken. Een later [verslag over Yellow](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) toont in het opnieuw aangemaakte bestand een andere luisterpoort. Controleer het nieuwe bestand en `ha core info` voordat je concludeert dat de webinterface hersteld is.

Mijn installatie had geen YAML-blok `http:`, geen wachtende HTTP-configuratie en geen TLS-certificaat of -sleutel in de stabiele instellingen. Het opgeslagen profiel was `intermediate_v6`. In dit beperkte geval maakte ik een afzonderlijke kandidaat voor versie 2.2 en behield ik de bestaande luisterpoort:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage

expected=$(ha core info --raw-json | jq -r '.data.port') &&
stored=$(jq -r '.data.stable.server_port' "$storage/http") &&
test -n "$expected" &&
test "$expected" != null &&
test "$expected" = "$stored" &&
test ! -e "$storage/http.v2-candidate" &&
jq -e '
  if .version == 3 and .minor_version == 1 and
     .data.pending == null and
     .data.stable.ssl_profile == "intermediate_v6" and
     (.data.stable | has("ssl_certificate") | not) and
     (.data.stable | has("ssl_peer_certificate") | not) and
     (.data.stable | has("ssl_key") | not) and
     (.data.stable | has("trusted_proxies") | not) and
     (.data.stable | has("use_x_forwarded_for") | not)
  then .version = 2 | .minor_version = 2 | .data.stable.ssl_profile = "intermediate"
  else error("Unexpected HTTP config. Stop and inspect")
  end
' \
  "$storage/http" > "$storage/http.v2-candidate" &&

jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&

test "$(jq -r '.data.stable.server_port' "$storage/http")" = \
  "$(jq -r '.data.stable.server_port' "$storage/http.v2-candidate")"
```

Alle bovenstaande opdrachten moeten slagen voordat je het actieve bestand vervangt. Als `jq` mislukt, inspecteer dan het kandidaatbestand voordat je het verwijdert en opnieuw probeert. [De HTTP-broncode van Core 2026.10.4](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) definieert opslagversie 2.2 en accepteert het profiel `intermediate`. [De broncode van Core 2026.11.1](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) gebruikt versie 3.1 en versiegebonden profielnamen. Ik heb de kandidaat vóór installatie ook gevalideerd met `HTTP_STORAGE_SCHEMA` van de geïnstalleerde oudere Core-versie.

Voer de schemacontrole van de geïnstalleerde oudere Core-versie uit terwijl de container nog actief is:

```bash
docker exec homeassistant python3 -c '
import json
from homeassistant.components.http.config import HTTP_STORAGE_SCHEMA
with open("/config/.storage/http.v2-candidate") as source:
    data = json.load(source)
stable = {
    key: value for key, value in data["data"]["stable"].items()
    if key not in ("created_at", "error", "error_message")
}
HTTP_STORAGE_SCHEMA(stable)
print("Schema geaccepteerd")
'
```

Stop als het schema de kandidaat afwijst. Deze stap valideert niet elke integratie of iedere niet-geteste vorm van HTTP-opslag.

De schemacontrole meldde `Schema geaccepteerd` voor deze kandidaat. Bij elk ander resultaat stop je deze herstelroute.

Deze handmatige omzetting is getest voor de genoemde velden. Een bestand met TLS-instellingen, vertrouwde proxy's of een wachtende configuratie vereist een eigen beoordeling. Alleen het hoogste versienummer wijzigen laat een profiel achter dat de oudere Core-versie niet accepteert.

Supervisor had in mijn geval een actieve Core-taak en weigerde `ha core stop`. Ik stopte de Core-container vanaf de hostconsole, installeerde de gevalideerde kandidaat en startte de container:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&
  docker stop homeassistant &&
  test "$(docker inspect -f '{{.State.Running}}' homeassistant)" = false &&
  cmp -s "$storage/http" "$storage/http.before-recovery" &&
  mv "$storage/http.v2-candidate" "$storage/http" &&
  docker start homeassistant
```

Als een opdracht na het stoppen mislukt, inspecteer dan het actieve HTTP-bestand voordat je `docker start homeassistant` uitvoert. Bij een gewijzigd bestand moet je een nieuwe kandidaat maken op basis van de actuele inhoud. Na deze stap reageerde de HTTP-pagina weer. Een HTTP-reactie bewees niet dat Core volledig was gestart, dus controleerde ik de Supervisor-status voordat ik het systeem als hersteld beschouwde.

Op deze Yellow meldde `docker inspect -f '{{.State.Status}}' homeassistant` daarna `running`. Controleer `ha core info` en het dashboard voordat je een nieuwe update aanvraagt.

## Controleer het resultaat van de bijwerking {#verify-the-update-outcome}

Nadat HTTP-toegang terug was, werkte ik Core bij naar 2026.11.1. Vraag die versie zo aan:

```bash
ha core update --version 2026.11.1
```

Na een lange start meldde de opdracht een fout. Daarna registreerde Supervisor Core als RUNNING en `Successfully started Home Assistant 2026.11.1`. Een statuscontrole liet zien dat de geïnstalleerde versie actueel was, het HTTP-bestand opnieuw naar versie 3.1 was gemigreerd en de container tijdens de observatie niet opnieuw was gestart. Het geauthenticeerde dashboard werd geladen. **Controleer de uiteindelijke status, ook wanneer de updateopdracht een fout meldt.**

Controleer op jouw systeem na een lange update de versie, Supervisor-gezondheid en containerstatus:

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

In dit geval leverden de eerste en derde opdracht de volgende opgeschoonde resultaten op:

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

Open daarna het dashboard via je gebruikelijke lokale adres en bevestig dat actuele statussen worden geladen. Bewaar het opgeslagen HTTP-bestand totdat een volgende back-up is voltooid en de normale werking is gecontroleerd.

De gegevens van mijn Yellow stelden de oorzaak van de eerste mislukte update niet vast. Ook het latere taakfoutbericht noemde geen oorzaak. Een geïnstalleerde versie en een werkend dashboard leveren sterker bewijs voor de uiteindelijke status dan alleen de CLI-melding, maar geen van beide verklaart waarom Supervisor de taak als mislukt markeerde.

## Volgende stappen

Als de HTTP-opslagfout blijft optreden, inspecteer dan het bewaarde bestand en zet een compatibele back-up terug of voer een Core-versie uit die de opslagversie kan lezen. Het bewaarde versie-3-bestand terugzetten onder de oudere Core herhaalt de storing. Als Core RUNNING bereikt maar afzonderlijke apparaten niet beschikbaar blijven, onderzoek die integraties afzonderlijk. Bewaar de herstelkopie en de cloudback-up totdat de volgende back-up is voltooid en het dashboard responsief blijft.

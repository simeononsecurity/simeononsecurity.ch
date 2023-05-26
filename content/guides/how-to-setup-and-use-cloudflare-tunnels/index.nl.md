---
title: "Cloudflare-tunnels opzetten: Stroomlijn en beveilig uw netwerkverkeer"
draft: false
toc: true
date: 2023-05-26
description: "Leer hoe u Cloudflare Tunnels kunt opzetten om uw netwerkverkeer te stroomlijnen en te beschermen en zo de prestaties en veiligheid te verbeteren."
tags: ["Cloudflare tunnels", "Netwerkbeveiliging", "Website prestaties", "Proxyserver", "Webverkeer", "Netwerk configuratie", "Ubuntu-server", "Cloudflare-account", "Authenticatie", "Tunnelbouw", "Verkeersroutering", "DNS Records", "Beveiligde verbinding", "Website Hosting", "Proxy-dienst", "Bescherming van het netwerk", "Optimalisatie van de prestaties", "Cloudflare Integratie", "Serverconfiguratie", "Verkeerscodering", "Beheer van het netwerkverkeer", "Veilige webhosting", "Website Veiligheid", "Ubuntu installatie", "Tunneltechnologie", "Cloudflare diensten", "Netwerkprestaties", "Webbeveiliging", "Serverbeveiliging", "Verkeersmanagement", "Cloudflare Proxy"]
cover: "/img/cover/An_illustration_showing_a_network_tunnel_connecting_a_local.png"
coverAlt: "Een illustratie met een netwerktunnel die een lokale server verbindt met het Cloudflare-logo, als symbool voor het veilige en gestroomlijnde netwerkverkeer."
coverCaption: ""
---

**Een gids voor het opzetten van Cloudflare tunnels**

## Introductie
Cloudflare Tunnels bieden een veilige manier om websites te hosten door een directe verbinding tussen uw lokale netwerk en Cloudflare tot stand te brengen. Deze gids leidt u door het proces van het opzetten van Cloudflare Tunnels om de veiligheid en prestaties van uw website te verbeteren.

______

## Waarom Cloudflare Tunnels?
Cloudflare Tunnels bieden verschillende voordelen, waaronder het verminderen van aanvalsvectoren en het vereenvoudigen van netwerkconfiguraties. Door Cloudflare als proxy te gebruiken, kunt u externe poorten afsluiten en ervoor zorgen dat al het verkeer door het veilige netwerk van Cloudflare gaat. Dit biedt een extra beschermingslaag voor uw website.

______

## Vereisten
Voordat u Cloudflare Tunnels instelt, moet u ervoor zorgen dat u over het volgende beschikt:

1. Een actieve Cloudflare account.
2. Een server met Ubuntu.

______

## Stap 1: Installatie
Om te beginnen moet u het Cloudflare Tunnels-pakket op uw Ubuntu-server installeren. Volg deze stappen:

1. Open de terminal op uw Ubuntu-server.
2. Download de laatste versie van het Cloudflare Tunnels-pakket door het volgende commando uit te voeren:

```shell
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
```

## Stap 2: Authenticatie
Vervolgens moet u uw Cloudflare-account authenticeren met de Cloudflare Tunnels-service. Volg deze stappen:

1. Voer het volgende commando uit in de terminal:

```shell
cloudflared tunnel login
```

2. Klik op de site die u wilt gebruiken met uw tunnel om het verificatieproces te voltooien.

## Stap 3: Een tunnel aanmaken

Nu is het tijd om uw Cloudflare-tunnel aan te maken. Volg deze stappen:

1. Voer het volgende commando in de terminal uit om een tunnel aan te maken:

```shell
cloudflared tunnel create name_of_tunnel
```

2. Kies een naam voor je tunnel die memorabel en beschrijvend is. Merk op dat de tunnelnaam later niet meer gewijzigd kan worden.

3.Na het aanmaken van de tunnel krijg je belangrijke informatie, waaronder de UUID van je tunnel. Noteer deze UUID, want die is nodig voor verdere configuratie.

4. Gebruik het commando om een lijst van alle actieve tunnels te bekijken:

```shell
cloudflared tunnel list
```

Dit toont de namen en UUID's van uw tunnels.

### Stap 4: De tunnel configureren

Volg deze stappen om uw tunnel te configureren en te beginnen met het routeren van verkeer:

1. Navigeer naar de Cloudflare Tunnels directory op uw server. De standaardlocatie is `/etc/cloudflared`

2. Maak in deze map een nieuw bestand aan met de naam `config.yml` met een tekstverwerker naar keuze.

3. Vul het bestand config.yml met de volgende inhoud:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json
```

Zorg ervoor dat u `<your_tunnels_uuid>` met de UUID van uw tunnel, en werk zo nodig het pad naar het geloofsbrievenbestand bij.

## Stap 5: Verkeer routeren

Volg deze stappen om de interne diensten te specificeren die je via je tunnel wilt bedienen:

1. `Open the ` bestand opnieuw.

2. Voeg de ingress parameters toe aan het bestand om de services te definiëren die u via Cloudflare wilt routeren. Bijvoorbeeld:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json

ingress:
  - hostname: example.com
    service: http://10.10.10.123:1234
  - hostname: subdomain.example.com
    service: http://10.10.10.123:8888
  - service: http_status:404

```

Vervang `<your_tunnels_uuid>` met de UUID van uw tunnel, en werk de hostnaam en dienstgegevens bij volgens uw configuratie.

3. Sla het bestand config.yml op.


## Stap 6: DNS Records aanmaken

Volg deze stappen om DNS records aan te maken voor de hostnaam en diensten van uw tunnel:

1. Open de terminal.

2. Gebruik de volgende opdracht om een DNS-record aan te maken:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> <hostname>
```
Vervang `<UUID or NAME of tunnel>` met de UUID of naam van je tunnel, en `<hostname>` met de gewenste hostnaam voor uw dienst.

3. Om bijvoorbeeld een DNS-record voor example.com te maken, voert u de opdracht uit:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> example.com
```

Merk op dat de wijzigingen worden weergegeven in de DNS-sectie van uw Cloudflare-dashboard.

## Stap 7: De tunnel starten

Volg deze stappen om uw Cloudflare-tunnel te testen en te starten:

1. Open de terminal.

2. Voer het volgende commando uit om de tunnel te starten:

```shell
cloudflared tunnel run <UUID or NAME of tunnel>
```

Vervang `<UUID or NAME of tunnel>` met de UUID of naam van uw tunnel.

3. Cloudflared zal nu uw tunnel opzetten en informatie over de status ervan weergeven. Zodra de tunnel succesvol is opgezet, kunt u doorgaan naar de volgende stap.

4. Om te voorkomen dat de tunnel sluit wanneer u de terminal verlaat, moet u Cloudflared als een systemd service uitvoeren. Gebruik het volgende commando:

```shell
cloudflared --config /path/to/config.yml service install
```

Vervang `/path/to/config.yml` met het pad naar uw `config.yml` bestand.

## Conclusie

In deze gids hebben we de stappen behandeld om Cloudflare Tunnels op Ubuntu in te stellen. Door deze instructies te volgen, kunt u de veiligheid en prestaties van uw website verbeteren door gebruik te maken van het netwerk van Cloudflare. Vergeet niet om uw tunnels regelmatig te monitoren en de configuratie zo nodig aan te passen.

Als u problemen ondervindt of verdere hulp nodig hebt, raadpleeg dan de [official Cloudflare Tunnels documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)


## Referenties
- [Cloudflare Tunnels Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)
- [Cloudflare Tunnels GitHub Repository](https://github.com/cloudflare/cloudflared)
- [tcude - How to Set Up Cloudflare Tunnels on Ubuntu](https://tcude.net/creating-cloudflare-tunnels-on-ubuntu/)
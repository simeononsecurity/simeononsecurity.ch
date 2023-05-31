---
title: "De kracht van SSH: Veilige toegang op afstand en eenvoudig beheer"
date: 2023-06-14
toc: true
draft: false
description: "Ontdek de voordelen van SSH, leer hoe u SSH-sleutels genereert, verbinding maakt met externe servers, bestanden veilig overdraagt en SSH-configuraties aanpast."
tags: ["SSH", "Beveiligde Shell", "toegang op afstand", "beheer op afstand", "encryptie", "authenticatie", "gegevensintegriteit", "draagbaarheid", "bestandsoverdracht", "SCP", "SSH-sleutels", "SSH-configuratie", "netwerkprotocol", "uitvoering van commando's op afstand", "OpenSSH", "twee-factor authenticatie", "openbare sleutel cryptografie", "IP-adres", "domeinnaam", "terminal", "opdrachtprompt", "beveiliging", "systeembeheerders", "ontwikkelaars", "veelzijdigheid", "authenticatiemethoden", "hashfuncties", "tunnelbouw", "aangepaste opties"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_securely_connecting.png"
coverAlt: "Een cartoonillustratie van een persoon die veilig verbinding maakt met een server via SSH."
coverCaption: ""
---

**Wat is SSH en hoe gebruik je het?

SSH (Secure Shell) is een netwerkprotocol dat een veilige en gecodeerde methode biedt voor toegang tot computers en servers op afstand. Het stelt gebruikers in staat om veilig verbinding te maken met systemen op afstand en deze te beheren via een onbeveiligd netwerk, zoals het internet. Dit artikel geeft een overzicht van SSH, de voordelen ervan, en hoe het effectief te gebruiken.

{{< youtube id="Atbl7D_yPug" >}}

## Voordelen van SSH

Het gebruik van SSH voor toegang op afstand biedt verschillende voordelen, waaronder:

1. **Veiligheid**: SSH gebruikt sterke versleutelingsalgoritmen om de communicatie tussen de client en de server te beveiligen. Het zorgt ervoor dat gegevens die over het netwerk worden verzonden niet kunnen worden onderschept of gemanipuleerd door kwaadwillenden.

2. **Authenticatie**: SSH maakt gebruik van verschillende authenticatiemethoden, zoals wachtwoorden, openbare sleutelcryptografie en authenticatie met twee factoren, om de identiteit te verifiëren van gebruikers die verbinding maken met systemen op afstand. Dit helpt ongeoorloofde toegang te voorkomen.

3. **Integriteit van gegevens**: SSH waarborgt de integriteit van de gegevens die tussen de client en de server worden verzonden. Het gebruikt cryptografische hashfuncties om wijzigingen of geknoei tijdens de overdracht te detecteren.

4. **Draagbaarheid**: SSH wordt ondersteund door een groot aantal besturingssystemen en apparaten, waardoor het een veelzijdige keuze is voor toegang op afstand op verschillende platforms.

5. **Flexibiliteit**: SSH kan voor verschillende doeleinden worden gebruikt, waaronder het uitvoeren van opdrachten op afstand, bestandsoverdracht en het tunnelen van andere protocollen zoals FTP en VNC.

## Hoe SSH te gebruiken

### SSH-sleutels genereren

Voordat u SSH gebruikt, moet u een SSH sleutelpaar aanmaken. Het sleutelpaar bestaat uit een publieke sleutel en een private sleutel. De publieke sleutel wordt op de externe server geplaatst, terwijl de private sleutel veilig op uw lokale machine wordt bewaard. Volg deze stappen om een SSH-sleutelpaar aan te maken:

1. Installeer **OpenSSH** op uw lokale machine als het nog niet geïnstalleerd is. Raadpleeg de officiële documentatie van uw besturingssysteem voor installatie-instructies.

2. Open een terminal of opdrachtprompt en voer de volgende opdracht uit om het sleutelpaar te genereren:

```shell
ssh-keygen -t rsa -b 4096
```

3. U wordt gevraagd een bestandsnaam voor het sleutelpaar en een optionele wachtwoordzin in te voeren. Druk op Enter om de standaard bestandsnaam te accepteren en laat de wachtwoordzin leeg als u er geen wilt gebruiken.

4. Het sleutelpaar wordt gegenereerd en de openbare sleutel wordt opgeslagen in een bestand met een `.pub` extensie. De privésleutel wordt opgeslagen in een bestand zonder extensie.

### Verbinding maken met een externe server

Volg deze stappen om met SSH verbinding te maken met een externe server:

1. Verkrijg het **IP-adres** of de domeinnaam van de externe server waarmee u verbinding wilt maken.

2. Open een terminal of opdrachtprompt en gebruik het volgende commando om een SSH-verbinding te starten:

```shell
ssh username@remote_server_ip
```

Vervang `username` met uw gebruikersnaam op de externe server en `remote_server_ip` met het werkelijke IP-adres of de domeinnaam van de server.

3. Als dit de eerste keer is dat u verbinding maakt met de server, ziet u mogelijk een waarschuwing over de authenticiteit van de host. Controleer de vingerafdruk van de server met een vertrouwde bron voordat u verdergaat.

4. Wanneer daarom wordt gevraagd, voert u uw wachtwoord in of geeft u het pad naar uw privésleutel als u verificatie op basis van sleutels gebruikt. Als de verificatie succesvol is, wordt u aangemeld bij de externe server.

### Bestandsoverdracht met SSH

SSH kan ook worden gebruikt voor veilige bestandsoverdracht tussen uw lokale machine en een externe server. Het meest gebruikte hulpmiddel voor SSH-bestandsoverdracht is **SCP** (Secure Copy). Volg deze stappen om bestanden over te dragen met SCP:

1. Open een terminal of opdrachtprompt op uw lokale machine.

2. Gebruik de volgende opdracht om een bestand te kopiëren van uw lokale machine naar de externe server:

```shell
scp /path/to/local/file username@remote_server_ip:/path/to/remote/location
```


Vervang `/path/to/local/file` met het eigenlijke pad en de bestandsnaam van het bestand op uw lokale machine. Vervang ook `username@remote_server_ip:/path/to/remote/location` met de juiste gebruikersnaam, server IP of domein, en externe bestandslocatie.

3. Als dit de eerste keer is dat u verbinding maakt met de server, ziet u mogelijk een waarschuwing over de authenticiteit van de host. Controleer de vingerafdruk van de server voordat u verder gaat.

4. Voer uw wachtwoord in of geef het pad naar uw privésleutel op als daarom wordt gevraagd. Het bestand wordt veilig gekopieerd naar de externe server.

### SSH Configuratie

Met SSH-configuratiebestanden kunt u het gedrag van uw SSH-client aanpassen en verfijnen. Het hoofdconfiguratiebestand staat meestal op `/etc/ssh/sshd_config` aan de serverkant en `~/.ssh/config` aan de clientzijde. Door deze bestanden te bewerken, kunt u aangepaste opties definiëren, zoals standaard gebruikersnamen, poortnummers en verbindingsinstellingen.

## Conclusie

SSH is een krachtig en veilig protocol voor toegang op afstand en beheer van servers en computers. Zijn sterke encryptie, authenticatiemechanismen en veelzijdigheid maken het een essentieel hulpmiddel voor systeembeheerders, ontwikkelaars en individuen die veilige toegang op afstand nodig hebben. Door de stappen in dit artikel te volgen, kunt u SSH effectief gaan gebruiken en profiteren van de mogelijkheden.

______

## Referenties

- [SSH on Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell)
- [SCP Documentation](https://man.openbsd.org/scp)
- [SSH Configuration File Documentation](https://man.openbsd.org/sshd_config)

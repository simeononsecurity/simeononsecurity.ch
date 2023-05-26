---
title: "Offline Firmware Update voor Ubiquiti Unifi UDM Pro en UDM SE via Command line SSH"
draft: false
toc: true
date: 2023-05-28
description: "Leer hoe u de firmware van Ubiquiti Unifi UDM Pro en UDM SE offline kunt updaten via command line SSH voor optimale prestaties en veiligheid."
tags: ["Ubiquiti firmware update", "UDM Pro", "UDM SE", "offline firmware update", "SSH-opdrachtregel", "netwerkbeheer", "netwerkbeveiliging", "firmware-upgrade", "SSH-verbinding", "firmwarebestand", "UniFi netwerkcontroller", "bugfixes", "prestatieverbeteringen", "beveiligingspatches", "netwerken", "netwerkapparaten", "technologie", "IT-beheer", "firmware update proces", "netwerkoptimalisatie", "Ubiquiti Networks firmware update", "UDM Pro firmware update", "UDM SE firmware update", "offline firmware update proces", "SSH-firmware update", "beheer van netwerkapparaten", "netwerkbeveiligingsupdates", "strategieën voor het bijwerken van firmware", "offline beheer van firmware", "optimalisatie van netwerkprestaties", "beheer van beveiligingspatchen", "updates voor netwerktechnologie"]
cover: "/img/cover/A_colorful_illustration_depicting_a_computer_connecting.png"
coverAlt: "Een kleurrijke illustratie van een computer die verbinding maakt met een router via SSH. Dit symboliseert het offline firmware update proces voor Ubiquiti Unifi UDM Pro en UDM SE apparaten."
coverCaption: ""
---

**Update de Ubiquiti Unifi UDM Pro en UDM SE Offline via SSH**.

In de wereld van netwerken heeft **Ubiquiti Networks** erkenning gekregen voor zijn innovatieve oplossingen. De **Ubiquiti Unifi Dream Machine Pro (UDM Pro)** en **Unifi Dream Machine SE (UDM SE)** zijn twee populaire producten die uitgebreide netwerkbeheerfuncties bieden. Het updaten van de firmware van deze apparaten is cruciaal om optimale prestaties en beveiliging te garanderen. In dit artikel zullen we onderzoeken hoe we de firmware van de UDM Pro en UDM SE **offline** kunnen updaten met behulp van command-line SSH.

______

## Waarom firmware updaten?

Firmware updates zijn essentieel voor elk netwerkapparaat, omdat ze vaak bugfixes, prestatieverbeteringen en beveiligingspatches bevatten. Het regelmatig updaten van de firmware van uw UDM Pro en UDM SE is cruciaal om ervoor te zorgen dat uw netwerk veilig blijft en soepel werkt.

______

## Offline Firmware Update

Het updaten van de firmware van de UDM Pro en UDM SE kan gebeuren via het **UniFi Dashboard**. In sommige scenario's kan een internetverbinding echter niet beschikbaar of wenselijk zijn. In dergelijke gevallen biedt een offline update via command-line SSH een alternatieve oplossing.

______

## De offline update voorbereiden

Voordat u verder gaat met de offline update, moet u ervoor zorgen dat u aan de volgende voorwaarden voldoet:

1. Een computer of apparaat waarop een SSH-client is geïnstalleerd.
2. 2. Het laatste firmware bestand voor uw UDM Pro of UDM SE. U kunt het firmware bestand verkrijgen via de [Ubiquiti Downloads](https://www.ui.com/download/unifi) for the [UDM Pro](https://www.ui.com/download/unifi/unifi-dream-machine-pro) page. For early access firmwares, you can see them on the [community releases page](https://community.ui.com/releases) once you've signed into your.[**ui.com**](https://account.ui.com/) rekening

______

## SSH verbinding opzetten

Volg deze stappen om de UDM Pro of UDM SE via commandoregel SSH bij te werken:

1. Zorg ervoor dat uw computer of apparaat verbonden is met hetzelfde netwerk als de UDM Pro of UDM SE.
2. 2. Open de SSH-client van uw voorkeur en breng een SSH-verbinding tot stand met het IP-adres** van de **UDM Pro of UDM SE. Als u bijvoorbeeld de **OpenSSH-client** in Linux of macOS gebruikt, kunt u het volgende commando gebruiken:

```bash
ssh root@<UDM_IP_ADDRESS>
```

Vervang `<UDM_IP_ADDRESS>` met het werkelijke IP adres van uw UDM Pro of UDM SE.

3. Voer de **gebruikersnaam** en **wachtwoord** in wanneer daarom wordt gevraagd. De standaard referenties voor Ubiquiti apparaten zijn meestal `ubnt` voor zowel de gebruikersnaam als het wachtwoord.

______

## Firmware bijwerken

Zodra u de SSH-verbinding tot stand hebt gebracht, kunt u doorgaan met de firmware-update:

1. Upload het firmware bestand naar de UDM Pro of UDM SE met behulp van **SCP (Secure Copy)**. SCP maakt veilige bestandsoverdracht via SSH mogelijk. Ervan uitgaande dat het firmware bestand zich op uw lokale machine bevindt, kunt u het volgende commando gebruiken:

```bash
scp <FIRMWARE_FILE_PATH> ubnt@<UDM_IP_ADDRESS>:/root/fwupdate.bin
```

Vervang `<FIRMWARE_FILE_PATH>` met het pad naar het firmware bestand op uw lokale machine, en `<UDM_IP_ADDRESS>` met het IP adres van uw UDM Pro of UDM SE.

2. Zodra het firmware bestand is geupload, kunt u het firmware update proces starten. Voer het volgende commando uit:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "ubnt-tools fwupdate /root/fwupdate.bin"
```

3. De UDM Pro of UDM SE start het firmware update proces. Dit kan enkele minuten duren. **Onderbreek het proces niet** totdat de update is voltooid.

4. Nadat de update is voltooid, kunt u de firmwareversie controleren door in te loggen op de UniFi Network Controller of door het volgende commando uit te voeren:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "show version"
```
Het bovenstaande proces veronderstelt dat u beschikt over het noodzakelijke firmware bestand voor uw UDM Pro of UDM SE. Zorg ervoor dat u het juiste firmware bestand heeft voor uw specifieke toestel model en versie.

## Conclusie

Het updaten van de firmware van uw Ubiquiti Unifi UDM Pro en UDM SE apparaten is een cruciale stap om optimale prestaties en veiligheid te garanderen. Terwijl de UniFi Network Controller een handige manier biedt om de firmware te updaten, biedt het uitvoeren van een offline update via command-line SSH een haalbare oplossing wanneer een internetverbinding niet beschikbaar of wenselijk is.

Door de in dit artikel beschreven stappen te volgen, kunt u de firmware van uw UDM Pro en UDM SE apparaten succesvol updaten met behulp van command-line SSH. Gebruik altijd de laatste firmwareversie van Ubiquiti Networks om te profiteren van bugfixes, prestatieverbeteringen en beveiligingspatches.

## Referenties

- [Ubiquiti Downloads](https://www.ui.com/download/unifi/) - Officiële Ubiquiti Downloads pagina voor firmware bestanden.
- [Unifi Advanced Updating Techniques](https://help.ui.com/hc/en-us/articles/204910064-UniFi-Upgrade-the-Firmware-of-a-UniFi-Device)

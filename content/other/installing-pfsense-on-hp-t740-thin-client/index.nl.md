---
title: "pfSense draaien op de HP t740 Thin Client: Handleiding voor tips en probleemoplossing"
draft: false
toc: true
date: 2023-04-29
description: "Leer hoe u pfSense instelt op de HP t740 Thin Client en hoe u mogelijke problemen oplost, zoals vastlopen en problemen met SSD-detectie."
tags: ["pfSense", "OPNsense", "HardenedBSD", "HP t740", "dunne cliënt", "homeserver", "PPPoE", "FreeBSD", "opstartprompt", "loader.conf.local", "nano-editor", "SSD-detectie", "M.2 SSD", "Western Digital", "probleemoplossing", "post-installatie", "UART", "ESXi", "Proxmox"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "Een cartoon van een tovenaar die een spreuk uitspreekt om een bevroren computer te repareren, met een tekstballon die zegt Probleem opgelost"
coverCaption: ""
canonical: "https://simeononsecurity.com/guides/installing-pfsense-on-hp-t740-thin-client/"
---
 pfSense, OPNsense of HardenedBSD op de HP t740 Thin Client**.

Als u op zoek bent naar een krachtig apparaat om pfSense, OPNsense of HardenedBSD op te draaien, is de HP t740 Thin Client wellicht een geschikte keuze voor u.

## Meer vermogen en compacte Home Server

De HP t740 Thin Client is een compact apparaat dat kan worden gebruikt als een krachtige pfSense box of een compacte homeserver. Het biedt meer vermogen dan de t730 of t620 Plus, waardoor het een geschikte keuze is voor het uitvoeren van PPPoE, vooral als u glasvezelinternet hebt. Het kan ook een upgrade pad bieden naar 10 Gigabit netwerken.

## PS/2 loopt vast

Als u echter van plan bent om FreeBSD of afgeleiden daarvan zoals pfSense, OPNsense of HardenedBSD op het bare metal te draaien (in tegenstelling tot ESXi of Proxmox), kunt u een probleem tegenkomen waarbij het systeem tijdens het opstarten vastloopt met de melding`atkbd0: [GIANT-LOCKED]` Gelukkig kan dit probleem worden opgelost door de volgende commando's in te voeren bij de opstartprompt:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

*Noteer dat u beide moet uitschakelen, anders zal het nog steeds vergrendelen bij het opstarten.*

Open na de installatie van het besturingssysteem een post-installatieshell en voer het volgende commando uit:

```bash
vi /boot/loader.conf.local
```
Voeg dan deze twee regels toe:
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### Wijzigingen doorzetten met behulp van VI
Voor degenen die niet bekend zijn met vi, kunt u de regel toevoegen door het volgende te doen:

De regels toevoegen`hint.uart.0.disabled="1"` en`hint.uart.1.disabled="1"` aan de`/boot/loader.conf.local` bestand met de vi editor kan worden gedaan met de volgende stappen:

1. Open de terminal op uw FreeBSD-systeem.

2. Typ`vi /boot/loader.conf.local` en druk op Enter om het bestand te openen in de vi editor.

3. Druk op de`i` toets om naar de invoegmodus te gaan.

4. Verplaats de cursor naar de onderkant van het bestand met behulp van de pijltjestoetsen.

5. Typ`hint.uart.0.disabled="1"` zonder de aanhalingstekens.

6. Druk op Enter om een nieuwe regel te beginnen.

7. Typ`hint.uart.1.disabled="1"` zonder de aanhalingstekens.

8. Druk op de`Esc` toets om de invoegmodus te verlaten.

9. Type`:wq` en druk op Enter om het bestand op te slaan en af te sluiten.

Hierdoor worden de twee regels toegevoegd aan de`/boot/loader.conf.local` bestand, dat de UART's uitschakelt en het vastlopen tijdens het opstarten op bepaalde HP t740 "Thin Client" apparaten verhelpt wanneer FreeBSD of afgeleiden daarvan zoals pfSense, OPNsense of HardenedBSD worden gebruikt.

Dit lost het probleem op bij herstarten en firmware-upgrades op pfSense/OPNsense.

## SSD

Als u de HP M.2 eMMC gebruikt, wordt deze niet gedetecteerd bij een out-of-the-box FreeBSD-installatie. In dat geval is een M.2 SSD van derden nodig. Elke M.2 SSD kan werken, SATA of NVMe.

Als u op zoek bent naar een M.2 SSD van derden voor uw HP t740 thin client, raden wij u aan om de[Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V) Beide opties zijn betrouwbaar en zouden goed moeten werken met uw toestel. Als u wilt profiteren van beide slots, hebt u ze allebei nodig. U offert de snelheden van de NVME op, maar u krijgt wat redundantie die o zo belangrijk is.

Merk op dat de auteur van dit artikel met succes pfSense CE 2.5.2 en OPNsense 22.1 op zijn t740 heeft gedraaid zonder problemen na het volgen van de bovenstaande stappen.

## Probleemoplossing en post-installatie

Als u na de installatie problemen ondervindt met het bewerken van bestanden, kunt u de nano-editor installeren met behulp van`pkg update` en`pkg install nano` Hiermee kunt u gemakkelijk tekstbestanden bewerken.

Om ervoor te zorgen dat de wijzigingen in de`/boot/loader.conf.local` bestand blijft bestaan tijdens pfSense versie upgrades, moet u de volgende regels toevoegen aan`/boot/loader.conf` en`/etc/rc.conf.local` 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

Maar soms is de bewerking van`/boot/loader.conf.local` bestand voor het opnieuw opstarten het probleem niet oplost. In dergelijke gevallen kan het nodig zijn de volgende regels toe te voegen aan het begin van de eerste boot:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

Deze stappen zouden de meeste problemen moeten oplossen die zich tijdens en na het installatieproces kunnen voordoen.

### Referenties:
-[HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
-[pfSense](https://www.pfsense.org/)
-[OPNsense](https://opnsense.org/)
-[HardenedBSD](https://hardenedbsd.org/)
-[ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
-[FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)
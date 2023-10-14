---
title: "Ausführen von pfSense auf dem HP t740 Thin Client: Tipps und Leitfaden zur Fehlerbehebung"
draft: false
toc: true
date: 2023-04-29
description: "Erfahren Sie, wie Sie pfSense auf dem HP t740 Thin Client einrichten und potenzielle Probleme wie Einfrieren und SSD-Erkennungsprobleme beheben."
tags: ["pfSense", "OPNsense", "HardenedBSD", "HP t740", "Dünner Kunde", "Heimserver", "PPPoE", "FreeBSD", "Boot-Prompt", "loader.conf.local", "Nano-Editor", "SSD-Erkennung", "M.2-SSD", "Western Digital", "Fehlerbehebung", "nach der Installation", "UART", "ESXi", "Proxmox"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "Eine Karikatur eines Zauberers, der einen Zauber wirkt, um einen eingefrorenen Computer zu reparieren, mit einer Sprechblase mit der Aufschrift „Problem gelöst“"
coverCaption: ""
canonical: "https://simeononsecurity.com/guides/installing-pfsense-on-hp-t740-thin-client/"
---
 pfSense, OPNsense oder HardenedBSD auf dem HP t740 Thin Client**

Wenn Sie nach einem leistungsstarken Gerät zum Ausführen von pfSense, OPNsense oder HardenedBSD suchen, ist der HP t740 Thin Client möglicherweise die richtige Wahl für Sie.

## Mehr Leistung und kompakter Heimserver

Der HP t740 Thin Client ist ein kompaktes Gerät, das als leistungsstarke pfSense-Box oder kompakter Heimserver verwendet werden kann. Es bietet mehr Leistung als das t730 oder das t620 Plus und ist daher eine geeignete Wahl für den Betrieb von PPPoE, insbesondere wenn Sie über Glasfaser-Internet verfügen. Es kann auch ein Upgrade-Pfad auf 10-Gigabit-Netzwerke angeboten werden.

## PS/2 friert ein

Wenn Sie jedoch planen, FreeBSD oder seine Derivate wie pfSense, OPNsense oder HardenedBSD auf dem Bare-Metal (im Gegensatz zu ESXi oder Proxmox) auszuführen, kann es zu einem Problem kommen, bei dem das System beim Booten mit der Meldung einfriert `atkbd0: [GIANT-LOCKED]` Glücklicherweise kann dieses Problem gelöst werden, indem Sie am Boot-Prompt die folgenden Befehle eingeben:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

*Beachten Sie, dass Sie beide deaktivieren müssen, da es sonst beim Booten immer noch blockiert.*

Öffnen Sie nach der Installation des Betriebssystems eine Post-Installations-Shell und führen Sie den folgenden Befehl aus:

```bash
vi /boot/loader.conf.local
```
Fügen Sie dann diese beiden Zeilen hinzu:
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### Änderungen mit VI beibehalten
Für diejenigen, die mit vi nicht vertraut sind, können Sie die Zeile wie folgt hinzufügen:

Hinzufügen der Zeilen `hint.uart.0.disabled="1"` Und `hint.uart.1.disabled="1"` zum `/boot/loader.conf.local` Das Erstellen einer Datei mit dem vi-Editor kann mit den folgenden Schritten erfolgen:

1. Öffnen Sie das Terminal auf Ihrem FreeBSD-System.

2. Geben Sie ein `vi /boot/loader.conf.local` und drücken Sie die Eingabetaste, um die Datei im vi-Editor zu öffnen.

3. Drücken Sie die Taste `i` Taste, um in den Einfügemodus zu gelangen.

4. Bewegen Sie den Cursor mit den Pfeiltasten an das Ende der Datei.

5. Geben Sie ein `hint.uart.0.disabled="1"` ohne die Anführungszeichen.

6. Drücken Sie die Eingabetaste, um eine neue Zeile zu beginnen.

7. Geben Sie ein `hint.uart.1.disabled="1"` ohne die Anführungszeichen.

8. Drücken Sie die Taste `Esc` Taste zum Verlassen des Einfügemodus.

9. Geben Sie ein `:wq` und drücken Sie die Eingabetaste, um die Datei zu speichern und zu verlassen.

Dadurch werden die beiden Zeilen zum hinzugefügt `/boot/loader.conf.local` Datei, die die UARTs deaktiviert und das Einfrierproblem beim Booten auf bestimmten HP t740 „Thin Client“-Geräten behebt, wenn FreeBSD oder seine Derivate wie pfSense, OPNsense oder HardenedBSD ausgeführt werden.

Dadurch wird das Problem bei Neustarts und Firmware-Upgrades auf pfSense/OPNsense behoben.

## SSD

Wenn Sie HP M.2 eMMC verwenden, wird es bei einer Standardinstallation von FreeBSD nicht erkannt. In diesem Fall benötigen Sie eine M.2-SSD eines Drittanbieters. Jede M.2-SSD kann funktionieren, SATA oder NVMe.

Wenn Sie nach einer M.2-SSD eines Drittanbieters für Ihren HP t740 Thin Client suchen, empfehlen wir Ihnen, darüber nachzudenken [Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V) Beide Optionen sind zuverlässig und sollten gut mit Ihrem Gerät funktionieren. Wenn Sie beide Slots nutzen möchten, benötigen Sie beide. Sie opfern zwar die Geschwindigkeiten des NVME, gewinnen aber etwas an Redundanz, die so wichtig ist.

Beachten Sie, dass der Autor dieses Artikels pfSense CE 2.5.2 und OPNsense 22.1 erfolgreich und ohne Probleme auf seinem t740 ausgeführt hat, nachdem er die oben genannten Schritte ausgeführt hat.

## Fehlerbehebung und Nachinstallation

Wenn nach der Installation Probleme beim Bearbeiten von Dateien auftreten, können Sie den Nano-Editor mit installieren `pkg update` Und `pkg install nano` Dies wird Ihnen helfen, Textdateien einfacher zu bearbeiten.

Um sicherzustellen, dass die vorgenommenen Änderungen an der `/boot/loader.conf.local` Damit die Datei auch bei pfSense-Versions-Upgrades bestehen bleibt, müssen Sie die folgenden Zeilen hinzufügen `/boot/loader.conf` Und `/etc/rc.conf.local` 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

Manchmal ist jedoch die Bearbeitung von `/boot/loader.conf.local` Die Datei vor dem Neustart behebt das Problem nicht. In solchen Fällen kann es erforderlich sein, zu Beginn des ersten Startvorgangs die folgenden Zeilen hinzuzufügen:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

Diese Schritte sollten die meisten Probleme lösen, die während und nach dem Installationsprozess auftreten können.

### Verweise:
- [HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
- [pfSense](https://www.pfsense.org/)
- [OPNsense](https://opnsense.org/)
- [HardenedBSD](https://hardenedbsd.org/)
- [ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
- [FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)
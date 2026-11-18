---
title: "Docker in LXC auf Proxmox: Zuverlässigkeit, Belege und VM-Migration"
date: 2026-09-16
lastmod: 2026-11-13
toc: true
draft: false
description: "Bewerte Docker in Proxmox LXC anhand eines dokumentierten AppArmor-Fehlers, einer sorgfältigen Analyse eines Host-Freezes, Diagnosebefehlen und eines Migrationsplans für eine VM."
genre: ["Virtualisierung", "Linux-Systemverwaltung", "Heimlabor"]
tags: ["Docker in einem LXC-Container", "Docker auf Proxmox", "LXC-Container auf Proxmox", "Docker-VM", "Homelab-Zuverlässigkeit", "Proxmox-Host friert ein", "Virtuelle Debian-Maschine mit Docker", "unprivilegierte Container", "verschachtelte Container", "Linux-Kernel-Isolierung", "AppArmor", "runc", "lxc-pve", "Docker Compose", "Docker-Speichertreiber", "containerd-Image-Speicher", "Speicherdruck", "Linux PSI", "persistentes Journal", "Proxmox-Sicherungen", "Sicherungen von Bind-Mounts", "Umzug virtueller Maschinen", "Fehlerdomänen", "GPU-Durchreichung", "Fehlersuche auf dem Heimserver"]
cover: "/img/cover/docker-lxc-vm-homelab-isolation.webp"
coverAlt: "Isometrische Illustration eines Heimservers mit verschachtelten Workloads und einem separaten Bereich für eine virtuelle Maschine auf gemeinsam genutzter Hardware"
coverCaption: "Konzeptillustration gemeinsam genutzter Hardware und unterschiedlicher Grenzen für die Workload-Isolierung"
---
**Docker in Linux Containers (LXC)** spart einen Teil des Infrastrukturaufwands, führt aber zu mehr Wechselwirkungen zwischen der Anwendungsruntime und dem Proxmox-Host. Für Docker-Dienste, auf die dein Haushalt angewiesen ist, bietet eine Debian-**virtuelle Maschine (VM)** einen praktikablen Ausgangspunkt. Sie trennt den Gastkernel und vereinfacht die Umgebung, die du bei der Fehlersuche reproduzieren musst. Dieser Artikel untersucht das bereitgestellte Video, prüft den zugrunde liegenden Incident-Bericht und ergänzt dokumentierte Fehler sowie einen Migrationsplan.

<!--more-->

## Wichtigste Erkenntnisse

- **Fehlertypen unterscheiden:** Ein Docker-Startfehler, eine blockierte VM und ein nicht reagierender physischer Host erfordern unterschiedliche Untersuchungen.
- **Belege bewerten:** Stabilität nach einer Migration stützt eine Wiederherstellungsentscheidung, beweist aber nicht die ursprüngliche Ursache.
- **Aktuelle Dokumentation prüfen:** Native OCI-Image-Unterstützung und verschachteltes Docker in LXC sind verschiedene Bereitstellungswege.
- **Persistente Daten schützen:** Proxmox-Backups und Compose-Dateien decken nicht automatisch jeden Speicherort von Anwendungsdaten ab.
- **Wiederherstellungsplan testen:** Miss Wiederherstellung, Neustartverhalten und Dienstverfügbarkeit, bevor du die alte Bereitstellung stilllegst.

## Vor dem Start

**Schwierigkeitsgrad:** Mittel. **Zielgruppe:** Proxmox-Administratoren, die zwischen verschachteltem Docker und Docker in einer VM wählen. Du solltest ein Compose-Projekt, einen Container-Mount und eine Linux-Shell erkennen, bevor du den Diagnosebeispielen folgst.

**Geschätzter Aufwand:** Plane 30–60 Minuten für Inventarisierung und Beweissicherung ein. Die Migrationsdauer hängt von der Datenbankgröße, Speicherdurchsatz, Hardwarezugriff und dem gewählten Wartungsfenster ab. Die folgenden Beispiele sind dokumentierte Verfahren und illustrative Überlegungen, keine Benchmarks aus einem für diesen Artikel betriebenen Labor.

| Voraussetzung | Warum sie wichtig ist |
|---|---|
| **Zugriff auf die Hostkonsole** | Unterscheidet einen Netzwerkausfall von einem Stillstand des gesamten Hosts |
| **Aktuelle Backups** | Bietet vor einer Änderung der Bereitstellung einen Wiederherstellungsweg |
| **Container- und VM-IDs** | Richtet Hostbefehle auf den vorgesehenen Workload |
| **Inventar der Anwendungsdaten** | Ermittelt Volumes, Bind-Mounts, Datenbanken und externe Abhängigkeiten |
| **Separate Testumgebung** | Ermöglicht eine Migrationsprobe ohne doppelte Schreibvorgänge in der Produktion |

## Quellvideo ansehen

{{< youtube id="XyPBHhZg0Ok" enable="true" title="Proxmox: The Hidden Danger of Running Docker Inside LXC" description="Erklärung zu verschachteltem Docker in Proxmox LXC, sporadischen Host-Freezes und der Migration auf Debian-VMs" uploadDate="2026-09-15T17:00:09-07:00" >}}

**Quellvideo:** [Proxmox: The Hidden Danger of Running Docker Inside LXC](https://www.youtube.com/watch?v=XyPBHhZg0Ok), veröffentlicht am 15. September 2026 von *Proxmox x Kubernetes x Homelab x Backup*. Die zentrale Frage lautet: Wie viel betriebliche Unsicherheit bringt eine ressourcensparende Architektur mit sich?

**Grenzen der Belege:** Das Video schildert einen Vorfall und schlägt Lehren daraus vor. Die folgenden Abschnitte unterscheiden die Beobachtungen des Besitzers, dokumentiertes Softwareverhalten und daraus abgeleitete Empfehlungen.

## Was der Vorfall belegt

Der ursprüngliche Bericht beschreibt einen **Host mit Intel Core i3-13100 und BIOSTAR H610MHP**. Der Besitzer meldete wiederkehrende Freezes, die den Verwaltungszugriff und LXC-Dienste beeinträchtigten. Ein angeschlossener Bildschirm reagierte nicht mehr, obwohl laut Bericht weiterhin syslog-Ausgaben erzeugt wurden. Das ist genauer, als den Vorfall als völlig logfrei zu beschreiben. [Ursprünglicher Proxmox-Forenbericht](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

Der Besitzer meldete später eine **Verbesserung nach der Migration**. In einem Nachtrag vom 3. August beschrieb er, wie er Docker-Workloads in Debian-VMs verschob und die Docker-LXCs stoppte. Zum Zeitpunkt der Aktualisierung seien keine weiteren Freezes aufgetreten. Das Video nennt einen stabilen Zeitraum von 16 Tagen. Keine der beiden Aussagen liefert eine kontrollierte Reproduktion oder benennt eine bestimmte fehlerhafte Komponente. [Nachtrag des Besitzers im selben Thread](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

| Beobachtung | Was sie stützt | Was sie nicht belegt |
|---|---|---|
| **Lange anfängliche Laufzeit** | Die frühere Kombination aus Workload und Software funktionierte | Zuverlässigkeit nach jedem späteren Update |
| **Host und Dienste bleiben stehen** | Der Ausfall betrifft mehr als eine Anwendung | Docker als Grundursache |
| **Migration geht der Verbesserung voraus** | Eine nützliche betriebliche Umgehung | Welche geänderte Wechselwirkung den Auslöser beseitigte |
| **Sechzehn stabile Tage** | Ein begrenzter Beobachtungszeitraum | Die Behebung jedes zwei- bis dreiwöchigen Fehlermusters |

Der **Beobachtungszeitraum** verdient Aufmerksamkeit. Sechzehn Tage liegen innerhalb eines Wiederholungsintervalls von 14–21 Tagen. Ein längerer Zeitraum, der mehrere frühere Fehlerintervalle, vergleichbare Workloads und gewöhnliche Wartung umfasst, erhöht die Aussagekraft, beweist aber weiterhin keine kontrollierte Ursache-Wirkungs-Beziehung.

**Betrieblicher Erfolg und Nachweis der Grundursache** sind getrennte Ergebnisse. Verlässliche Haushaltsdienste wiederherzustellen ist ein legitimer Grund für eine Migration. Beschreibe das Ergebnis als beobachtete Zuverlässigkeitsverbesserung, bis stärkere Belege den Mechanismus nachweisen.

## Kernelgrenze bestimmen

```text
Docker in LXC:
Anwendung -> Docker-Laufzeit -> LXC-Namespaces und Richtlinien
              -> Proxmox-Hostkernel -> physische Hardware

Docker in einer VM:
Anwendung -> Docker-Laufzeit -> Gast-Linux-Kernel
              -> virtuelle Hardware / KVM-QEMU
              -> Proxmox-Hostkernel -> physische Hardware
```

**LXC** verwendet den Hostkernel. Namespaces, Control Groups, Capabilities, seccomp und Sicherheitsprofile beschränken Prozesse, stellen aber keinen separaten Kernel bereit. Docker in LXC fügt eine weitere Containerverwaltungsebene für Workloads hinzu, die denselben Hostkernel nutzen. [LXC-Architektur und Isolationsfunktionen](https://linuxcontainers.org/lxc/introduction/)

Eine **VM** bringt einen Gastkernel mit. Ein Fehler im Gastkernel betrifft normalerweise diese VM, während Proxmox die anderen Gäste weiter verwaltet. Die VM hängt weiterhin von physischem Host, Hypervisor, Speicher und Netzwerk ab. Hardwareausfälle und Defekte des Hostkernels bleiben gemeinsame Abhängigkeiten.

| Grenze | Docker in LXC | Docker in einer VM |
|---|---|---|
| **Von Anwendungen genutzter Kernel** | Proxmox-Hostkernel | Gastkernel |
| **Umgebung der Docker-Runtime** | Durch die Richtlinien des äußeren Containers eingeschränkt | In einem üblichen Gastbetriebssystem installiert |
| **Updates des Gastkernels** | An den Hostkernel gebunden | Im Gast verwaltet |
| **Ausfall des physischen Hosts** | Stoppt abhängige Workloads | Stoppt abhängige Workloads |

Eine VM begrenzt **einen Teil der Fehlerausbreitung**, aber nicht alles. Ein Absturz eines Anwendungsprozesses in LXC lässt Proxmox nicht automatisch abstürzen. Wenn du alle Haushaltsdienste in eine Docker-VM legst, teilen sie weiterhin ein Gastbetriebssystem und einen Wartungsplan.

Der **breitere konzeptionelle Vergleich** steht unter [Docker-Container im Vergleich zu virtuellen Maschinen](/articles/docker-vs-vms/). Hier geht es um den Standort von Docker in Proxmox und die daraus entstehenden Grenzen bei der Fehlersuche.

## Support präzise benennen

**„Nicht unterstützt“** erfordert eine benannte Komponente und Version. Unterscheide eine vom Anbieter empfohlene Bereitstellung, dokumentierte Funktionen, die Pflege durch die Distribution und einen vertraglichen Supportanspruch. Ein funktionierender verschachtelter Stack beweist nicht, dass alle Kombinationen gleich umfassend getestet werden. Eine VM-Empfehlung bedeutet auch nicht, dass Maintainer jeden Nesting-Fehler ablehnen.

**Die aktuelle Proxmox-Dokumentation** macht eine wichtige Unterscheidung. Der Quellcode des Container-Toolkits beschreibt die Unterstützung von **Open Container Initiative (OCI)**-Anwendungsimages als Technologie-Vorschau, bei der Images in das LXC-Framework konvertiert werden. Für Anforderungen mit Fokus auf Isolation und Live-Migration empfiehlt Proxmox auch Container in einer QEMU-VM. Ein OCI-Image in dieses Framework zu importieren unterscheidet sich davon, Docker Engine zu installieren und Compose in einem LXC-Gast auszuführen. [Dokumentation der Proxmox-Containerwerkzeuge](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

| Bereitstellung | Zu prüfende Frage |
|---|---|
| **Traditioneller LXC-Gast** | Passen das Betriebssystem-Template und die Anwendung zu den dokumentierten Containerbeschränkungen? |
| **Docker in LXC verschachtelt** | Welche Kombinationen aus Kernel, Runtime, Sicherheitsrichtlinien und Speicher wurden getestet? |
| **Nativer OCI-Image-Import** | Bietet die installierte Proxmox-Version die dokumentierte Funktion und das benötigte Verhalten? |
| **Docker in einer Debian-VM** | Erfüllt die Gastversion die Installationsanforderungen von Docker? |

Docker veröffentlicht einen **Installationsweg für Debian**. Nutze die Liste unterstützter Versionen und die Repository-Anweisungen für den Gast. Halte installierte Versionen fest, statt anzunehmen, dass eine ältere Anleitung noch stimmt. Das ist eine dokumentierte Installationsbasis, keine Uptime-Garantie und kein automatischer kostenpflichtiger Supportvertrag. [Docker Engine auf Debian](https://docs.docker.com/engine/install/debian/)

## Ein bestätigter Nesting-Fehler

Die **runc/AppArmor-Inkompatibilität von 2025** ist ein überprüfbares Beispiel. Die runc-Maintainer dokumentierten einen Fehler beim erneuten Öffnen eines Deskriptors in einem äußeren Container mit AppArmor-Profil. AppArmor deutete einen Zugriff unter **`/proc/sys`** fälschlich als Zugriff unter **`/sys`**, wodurch eine Richtlinienverweigerung ausgelöst wurde. [runc-Problem 4968](https://github.com/opencontainers/runc/issues/4968)

Ein **betroffener Startvorgang** meldete diesen Fehlerauszug:

```text
open sysctl net.ipv4.ip_unprivileged_port_start file: reopen fd 8: permission denied
```

Der dokumentierte Fehler verhinderte den **Containerstart**. Er erklärt nicht die Host-Freezes des Forenbesitzers. Das Issue nennt **`lxc-pve 6.0.5-2`** als Proxmox-Fix für dieses konkrete Problem. Die zugehörige Upstreamänderung in LXC wurde am 20. November 2025 zusammengeführt. *Das sind historische Fix-Verweise, keine Empfehlung, ein Paket in einer aktuellen Installation festzuhalten.* [Zusammenfassung des Fixes durch Maintainer](https://github.com/opencontainers/runc/issues/4968), [zusammengeführte LXC-Änderung](https://github.com/lxc/lxc/pull/4609)

Die Lehre betrifft die **Abstimmung von Abhängigkeiten**. Eine Runtime-Sicherheitsänderung wirkte mit den Richtlinien des äußeren Containers zusammen, und die Korrektur erforderte Arbeit in einer anderen Schicht. Nutze das passende gepflegte Paketupdate für deine Version, statt AppArmor dauerhaft zu deaktivieren oder eine alte verwundbare Runtime zu behalten.

> **Kernaussage:** Dieser Vorfall zeigt ein reales Kompatibilitätsproblem bei verschachtelten Containern und eine echte Reaktion der Maintainer. Er belegt weder eine allgemeine Instabilität von LXC noch die Ursache eines separaten Host-Freezes.

## Tatsächliche Kosten vergleichen

Miss Effizienz mit deinem **realen Workload**. Vergleiche unter gleichen Bedingungen Host-Speicherdruck, CPU-Bedarf, Speicherlatenz, Antwortzeiten der Anwendung und Wiederherstellungsaufwand. Zugewiesener VM-RAM, freier Gastspeicher und residenter Host-Speicher sind unterschiedliche Messwerte.

| Behauptete Einsparung | Zu erhebender Messwert | Zusätzlich zu erfassender Aufwand |
|---|---|---|
| **Weniger Speicher-Overhead** | Host-Speichernutzung und -druck beim gleichen Workload | Zeit für Verwaltung verschachtelter Limits und Diagnose von Konflikten |
| **Schnellere Bereitstellung** | Zeit bis zu einem funktionsfähigen Dienst mit wiederhergestellten Daten | Zeit für den Neuaufbau nach einem fehlgeschlagenen Update |
| **Einfachere gemeinsame Hardware-Nutzung** | Erforderliche Geräte, Berechtigungen und erfolgreiche Anwendungsausführung | Abhängigkeit von Hosttreibern und Migrationsbeschränkungen |
| **Einfachere Backups** | Erfolgreiche Wiederherstellung aller erforderlichen Daten | Externe Mounts und Anwendungskonsistenz |

Docker dokumentiert standardmäßig **uneingeschränkte CPU- und Speichernutzung**, sofern keine Limits gesetzt werden. Bei LXC fügt der äußere Container eigene Grenzen hinzu. Bei einer VM bildet die Zuweisung an den Gast eine weitere Kapazitätsgrenze. Der Gast braucht außerdem Ressourcen für Betriebssystem, Docker, Caches und Spitzenbedarf der Anwendungen. [Docker-Ressourcenbeschränkungen](https://docs.docker.com/engine/containers/resource_constraints/)

**Hardwarezugriff** ist eine Anforderung des Workloads. Ein Host-Grafikgerät mit einem Container zu teilen und ein PCI-Gerät einer VM zuzuweisen erfordern unterschiedliche Treiber- und Isolationskonfigurationen. Notiere vor der Auswahl das konkrete Gerät und die Anwendungsanforderung. Ein Medien-Workload mit Hardwaredecodierung benötigt nach der Migration beispielsweise einen erfolgreichen Decodiertest zusätzlich zu normalen HTTP-Statusprüfungen.

Vermeide **allgemeine Overhead-Zahlen**. Dieser Artikel nennt keine feste RAM-Mehrlast und keinen Leistungsprozentsatz, weil solche Werte einen kontrollierten Workload, eine Konfiguration und eine Messmethode erfordern. Verwende im Entscheidungsprotokoll unten ein Ergebnis deines eigenen Vergleichs.

## Belege je Ebene sammeln

**Beginne auf dem Proxmox-Host** in einer Administrationsshell. Ersetze **`101`** durch die ID des untersuchten LXC:

```bash
pveversion -v
uname -r
pct config 101
journalctl --list-boots
journalctl -k -b -1 --no-pager
```

**`pveversion -v`** erfasst die installierten Proxmox-Komponentenversionen. **`pct config`** erfasst die Konfiguration des äußeren Containers. In **`journalctl`** wählt **`-k`** Kernelmeldungen, **`-b -1`** den vorherigen Start und **`--no-pager`** liefert einfache Terminalausgabe. Meldungen des vorherigen Starts setzen erhaltene Journaldaten voraus. [Proxmox-Werkzeugsammlung](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), [systemd-journalctl-Referenz](https://github.com/systemd/systemd/blob/main/man/journalctl.xml)

**Prüfe danach den Docker-Host**, also das LXC oder die VM, in der der Daemon läuft:

```bash
docker version
docker info
docker compose version
docker ps -a
docker stats --no-stream
```

Dokumentiere **beide Umgebungen**. Der Container-Image-Tag allein nennt weder Docker, containerd, runc, Hostkernel, Sicherheitsrichtlinien noch Speicher-Backend. Notiere den Vorfallszeitpunkt, aktuelle Updates und ob die lokale Hostkonsole reagierte. Entferne Zugangsdaten und private Anwendungsdetails, bevor du Diagnosematerial veröffentlichst.

**Untersuche einen bestimmten Workload** und ersetze **`app`** durch den Containernamen:

```bash
docker inspect --format '{{json .State}}' app
docker inspect --format '{{.RestartCount}}' app
docker inspect --format '{{json .Mounts}}' app
```

**`docker inspect`** zeigt Status, Neustartzähler und Mount-Informationen des benannten Containers. Nutze die Anzahl der Neustarts als Hinweis für den Abgleich mit Logs, nicht als Beweis für einen Hostfehler. Ein neu erstellter Container beginnt außerdem eine neue Historie. [Docker-inspect-Referenz](https://docs.docker.com/reference/cli/docker/inspect/)

## Druck und Stillstand unterscheiden

**Erfasse den Linux-Ressourcendruck auf dem Host**, während das Problem auftritt:

```bash
cat /proc/pressure/cpu
cat /proc/pressure/memory
cat /proc/pressure/io
```

**Pressure Stall Information**, kurz PSI, meldet Zeitverluste von Aufgaben, die auf Ressourcen warten. Die Felder **`some`** und **`full`** beschreiben unterschiedliche Stillstandsbedingungen. **`avg10`**, **`avg60`** und **`avg300`** fassen jüngste Intervalle zusammen. Speicherdruck unterscheidet sich von belegtem Speicher: Ein großer Cache allein belegt keinen Mangel. [Linux-PSI-Dokumentation](https://docs.kernel.org/accounting/psi.html)

| Beleg | Nützliche Einordnung | Nächste Prüfung |
|---|---|---|
| **Ein Container beendet sich wiederholt** | Fehler der Anwendung oder Container-Runtime | Exit-Status, Dienstlogs, Neustartrichtlinie |
| **SSH fällt aus, Konsole funktioniert** | Netzwerk- oder Verwaltungswegproblem | Linkstatus, NIC-Treiber, Bridge, Firewall |
| **Memory PSI steigt unter Last** | Aufgaben verlieren Zeit durch Speicherkonkurrenz | Limits, Rückgewinnung, OOM-Einträge, Workload-Wachstum |
| **Speicheranforderungen bleiben hängen** | Eine I/O-Abhängigkeit verzögert die Arbeit | Gerätezustand, Speicherlogs, Latenz und Warteschlangen |
| **Watchdog meldet einen Lockup** | Kernel-Detektor hat einen definierten Stillstand erkannt | Vollständiger Trace, Kernelversion, reproduzierbarer Auslöser |
| **Kein letzter Logeintrag** | Die Beweiserfassung endete, bevor nützliche Ausgabe eintraf | Persistente oder externe Aufzeichnung vor erneutem Auftreten |

Ein **Linux-Lockup-Bericht** hat eine technische Bedeutung. Kernel-Watchdogs unterscheiden Soft- und Hard-Lockups. Ein Browser-Timeout belegt keines davon. Ein fehlender Watchdog-Bericht beweist auch nicht, dass der Host gesund blieb. [Linux-Dokumentation zur Lockup-Erkennung](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)

**Firmware- und Energiesparänderungen** sind Experimente. Dokumentiere die vorherige Einstellung, den Änderungsgrund und den Beobachtungszeitraum. Das Deaktivieren eines CPU-Leerlaufzustands verändert Energie- und Wärmeverhalten. Ein Bericht über einen anderen Rechner reicht nicht aus, um dieselbe Einstellung allgemein zu empfehlen.

## Nützliche Logs sichern

**Persistentes Journaling** erhöht die Chance, Belege über einen Neustart hinweg aufzubewahren. Ein journald-Konfigurationsfragment verwendet diese Einstellung:

```ini
[Journal]
Storage=persistent
```

**`Storage=persistent`** fordert bei verfügbarer Kapazität eine Speicherung der Journaldaten auf dem Datenträger an. Lege Aufbewahrungslimits und verfügbaren Speicherplatz fest und prüfe danach, ob frühere Starts in **`journalctl --list-boots`** erscheinen. Persistente Logs hängen weiterhin davon ab, dass der Host Schreibvorgänge vor dem Fehler abschließt. [systemd-journald-Konfiguration](https://github.com/systemd/systemd/blob/main/man/journald.conf.xml)

**Externe Beobachtung** ergänzt eine weitere Perspektive. Überwache den Dienst von einem anderen Rechner und notiere Zeitstempel. Ein Monitor auf dem ausfallenden Proxmox-Host verschwindet während desselben Ausfalls und hilft daher weniger, Downtime von fehlender Telemetrie zu unterscheiden.

**Beispieltest:** Plane eine einfache HTTP-Prüfung von einem separaten System und vergleiche Ausfälle mit Host-Erreichbarkeit und Verhalten der lokalen Konsole. Ein Anwendungstimeout bei erreichbarem Host erfordert eine andere Untersuchung als ein gleichzeitiger Ausfall von Anwendung, Verwaltung und Konsole. Das ist ein Diagnoseentwurf, kein beobachtetes Ergebnis des Quellvorfalls.

## Kontrollierte Migration planen

Beginne mit **einem risikoarmen Compose-Projekt**. Bereite eine Debian-VM mit einer in der Docker-Installationsdokumentation aufgeführten Version vor, richte Backups ein und weise Ressourcen zu. Halte die ursprüngliche Bereitstellung für ein Rollback bereit, bis der Ersatz die Tests bestanden hat. [Docker-Installationsanleitung für Debian](https://docs.docker.com/engine/install/debian/)

**Inventarisiere das Compose-Projekt** in seinem Arbeitsverzeichnis:

```bash
docker compose config --quiet
docker compose config --images
docker compose config --volumes
```

**`--quiet`** prüft die Konfiguration ohne Ausgabe. **`--images`** listet referenzierte Images auf, **`--volumes`** benannte Volumes. Diese Befehle exportieren keine Anwendungsdaten und liefern kein vollständiges Bind-Mount-Inventar. Prüfe auch die Compose-Datei und die Mounts jedes Containers. [Docker-Compose-config-Referenz](https://docs.docker.com/reference/cli/docker/compose/config/)

| Daten oder Abhängigkeit | Migrationsaktion |
|---|---|
| **Compose-Definitionen** | Projektdateien übertragen und die getestete Konfiguration beibehalten |
| **Geheimnisse und Umgebung** | Erforderliche Werte über den gewählten Geheimnisverwaltungsprozess neu einrichten |
| **Benannte Volumes** | Inhalte mit anwendungskonsistenten Verfahren sichern und wiederherstellen |
| **Bind-Mount-Pfade** | Quelldaten übertragen oder erneut verbinden und Eigentümerschaft prüfen |
| **Datenbanken** | Unterstütztes Backup-/Restore-Verfahren oder eine Kopie nach pausierten Schreibvorgängen verwenden |
| **Geräte und Freigaben** | Zugriff wiederherstellen und Anwendungsverhalten testen |
| **Ports und DNS** | Ersatzadresse vorbereiten und Umschaltung planen |

**Volumes** bestehen länger als Container, migrieren aber nicht selbstständig. Eine Compose-Datei benennt Ressourcen und definiert Dienste. Die Volume-Dokumentation von Docker beschreibt getrennte Sicherungs- und Wiederherstellungsvorgänge für persistente Inhalte. Gehe nicht davon aus, dass die Neuerstellung des Projekts die Daten zurückbringt. [Lebenszyklus und Backups von Docker-Volumes](https://docs.docker.com/engine/storage/volumes/)

Prüfe die **Proxmox-Backupabdeckung** separat. Die Backup-Dokumentation schließt Geräte- und Bind-Mount-Inhalte von Container-Backups aus. Ein erfolgreiches Backup des LXC-Root-Dateisystems belegt daher nicht den Schutz aller darin eingebundenen Verzeichnisse. [Proxmox-Backup-Dokumentation](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

### Speicher vor dem Kopieren prüfen

**Prüfe die tatsächliche Docker-Speicherkonfiguration** auf jedem Docker-Host:

```bash
docker info
findmnt -T /var/lib/docker
```

**`findmnt`** ermittelt das Dateisystem des angegebenen Pfads. Ersetze **`/var/lib/docker`**, wenn der Daemon ein anderes Datenverzeichnis nutzt, und prüfe bei Bedarf den Speicherpfad von containerd. Docker dokumentiert den Unterschied zwischen dem containerd-Image-Speicher und klassischen Storage-Treibern sowie backend-spezifische Anforderungen. [Auswahl des Docker-Speicher-Backends](https://docs.docker.com/engine/storage/drivers/select-storage-driver/)

**Erstelle Images neu und stelle Anwendungsdaten wieder her** – nach den dokumentierten Verfahren des gewählten Backends. Ein aktives Docker-Datenverzeichnis zwischen verschiedenen Speicheranordnungen zu kopieren, setzt zusätzliche Annahmen zu Metadaten, Mount-Status und Konsistenz voraus. Das unterscheidet sich von einem Backup des Datenvolumes einer gestoppten Anwendung.

### Mit Rollback umschalten

1. **Wiederherstellung proben** in der VM mit separaten Adressen und gegebenenfalls Testdaten.
2. **Produktive Schreibvorgänge stoppen** während des vereinbarten Wartungsfensters und ein abschließendes konsistentes Backup erstellen.
3. **Stelle die Anwendungsdaten wieder her und prüfe** Berechtigungen, Zugangsdaten und den erforderlichen Hardwarezugriff.
4. **Dienstrouting umschalten**, nachdem der Ersatz anwendungsspezifische Prüfungen bestanden hat.
5. **Das Original gestoppt lassen** und Konfiguration sowie Wiederherstellungsdaten aufbewahren.
6. **Rollback-Regeln für Daten dokumentieren**, die nach der Umschaltung geschrieben wurden, bevor das alte System neu startet.

Vermeide **zwei aktive Schreiber** auf denselben Datenbankspeicher. Ein Rollback nach neuen produktiven Schreibvorgängen braucht einen Plan, um diese zu erhalten oder bewusst zu verwerfen. Das Neustarten eines alten Containers führt zwei auseinanderlaufende Datenstände nicht zusammen.

## Mehr als Uptime testen

**Abnahmetests** sollten dem Zweck des Dienstes folgen. Ein grüner Containerstatus zeigt einen laufenden Prozess. Ein nutzbarer Dienst braucht außerdem seine Daten, Netzwerkzugriff, Abhängigkeiten und ein funktionierendes Wiederherstellungsverhalten.

| Prüfung | Zu sichernder Beleg |
|---|---|
| **Anwendungsfunktion** | Erfolgreiche echte Transaktion, Abfrage oder Medienoperation |
| **Vollständigkeit der Daten** | Erwartete Datensätze, Dateien, Berechtigungen und aktuelle Änderungen |
| **Neustart des Gasts** | Dienste kehren ohne manuelle Reparatur zurück |
| **Backup-Wiederherstellung** | Die wiederhergestellte Kopie besteht dieselbe Funktionsprüfung |
| **Repräsentative Last** | Latenz, CPU, Speicherdruck und Speicherverhalten |
| **Wartungsprobe** | Getestetes Update und nutzbares Wiederherstellungsverfahren |
| **Längere Beobachtung** | Verfügbarkeitsdaten über mehrere frühere Fehlerintervalle |

**Beispielentscheidung:** Ein Kameradienst und ein experimenteller Downloader nutzen derzeit denselben verschachtelten Stack. Beide in eine VM zu verschieben verbessert die Kerneltrennung, lässt aber die gemeinsame Wartungsgrenze des Gasts bestehen. Wenn die Kameraverfügbarkeit Vorrang hat, prüfe getrennte Wartungsgruppen und Ressourcenlimits und teste dann die Aufzeichnung während Downloader-Updates.

**Erwartete Überlegung:** Wähle den Standort anhand der Dienstabhängigkeit, die du isolieren musst. Zwei VMs auf demselben physischen Server teilen weiterhin Stromversorgung, Speicher und Hostkernel. Soll die Lösung einen Serverausfall überstehen, braucht sie ein zusätzliches unabhängiges System oder einen akzeptablen manuellen Rückfall.

## Entscheidungsprotokoll erstellen

**Nutze gemessene Belege**, um eine Bereitstellung auszuwählen und den Zeitpunkt ihrer erneuten Bewertung festzulegen:

```text
Auswirkungen auf Dienst und Haushalt:
Aktuelle Versionen von Host / Kernel / LXC / Docker:
Benötigter Zugriff auf GPU, Geräte und Netzwerk:
Gemessener Speicher-, CPU-, Speicherplatz- und Latenzbedarf:
Bekanntes Fehlersymptom und Wiederholungsintervall:
Backup-Abdeckung und Nachweis einer erfolgreichen Wiederherstellung:
Gewählte Architektur und Begründung:
Zulässiges Ausfallfenster und Wiederherstellungsziel:
Verfahren für Umstellung und Daten-Rollback danach:
Abnahmetests und Beobachtungszeitraum:
Bedingung für eine erneute Architekturprüfung:
```

**Wähle LXC-Nesting bewusst**, wenn seine Vorteile den Integrationsaufwand rechtfertigen und du den Wiederherstellungsweg getestet hast. Wähle eine VM, wenn eine übliche Docker-Gastumgebung und ein separater Gastkernel den Dienstbetrieb vereinfachen. Keine der beiden Entscheidungen ersetzt Backups, Monitoring und Hostwartung.

## Änderung vor der Migration freigeben

Behandle die Migration als **kontrollierte Änderung**, nicht als Beweis für die ursprüngliche Vorfallsursache. Erfasse vor der Umschaltung die Containerkonfiguration, Image-Digests, Bind-Mount-Pfade, Umgebungsvariablen, Gerätezuordnungen und den letzten erfolgreichen Wiederherstellungstest. Vergleiche danach dieselben Dienstprüfungen und Ressourcenmessungen. Lass den alten Workload gestoppt, bis die neue Kopie das Abnahmefenster bestanden hat.

Kehrt der Vorfall nach der Migration zurück, vergleiche Hostkernel, Speicher, Speicherdruck, Gerätezugriff und Docker-Versionen beider Bereitstellungen. Der Vergleich grenzt die Untersuchung ein. Eine erfolgreiche Migration wird nur dann zum Kausalexperiment, wenn die relevanten Variablen kontrolliert blieben.

## Nächste Schritte

**Inventarisiere zuerst einen Dienst.** Ermittle persistente Daten, physische Abhängigkeiten, Fehlersymptome und Wiederherstellungsziel. Probiere eine Wiederherstellung, bevor du über eine Migration entscheidest.

Für **verwandte Themen** nutze den [Proxmox-VE-Upgrade-Leitfaden](/articles/proxmox-ve-8-to-9-upgrade-guide/) zur Upgradeplanung und den [Sicherheitsleitfaden für Docker und Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/) zur Absicherung von Workloads. Halte Architekturwahl, Upgrade-Ausführung und Vorfallsdiagnose als getrennte Entscheidungen mit eigenen Belegen fest.

## Quellen und Belege

**Recherche geprüft:** 16. September 2026. Das bereitgestellte Transkript gab den Themenrahmen vor. Videometadaten, ursprünglicher Incident-Bericht, Upstream-Issue und offizielle Dokumentation wurden getrennt geprüft. Illustrative Übungen und vorgeschlagene Validierungsschritte sind im Text gekennzeichnet.

| Quelle | Rolle |
|---|---|
| **[Quellvideo](https://www.youtube.com/watch?v=XyPBHhZg0Ok)** | Ursprüngliche Erklärung und gemeldeter Stabilitätszeitraum |
| **[Proxmox-Forendiskussion zum Vorfall](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)** | Beobachtungen aus erster Hand und Migrationsnachtrag |
| **[Proxmox-Containerwerkzeuge](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)** | Containerarchitektur und aktuelle OCI-Unterscheidung |
| **[runc-Problem 4968](https://github.com/opencontainers/runc/issues/4968)** | Dokumentierter Startfehler und historischer Paket-Fix |
| **[LXC-Änderungsanfrage 4609](https://github.com/lxc/lxc/pull/4609)** | Zusammengeführte Upstreamänderung in AppArmor |
| **[Docker-Dokumentation](https://docs.docker.com/engine/install/debian/)** | Installationsbasis für den Gast, mit obigen Verweisen auf Runtime und Speicher |
| **[Linux-PSI-Dokumentation](https://docs.kernel.org/accounting/psi.html)** | Einordnung des Ressourcendrucks |
| **[Linux-Watchdog-Dokumentation](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)** | Definierte Kernel-Lockupbedingungen |
| **[Proxmox-Backup-Dokumentation](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)** | Ausschlüsse für Container-Mounts und Backupverhalten |

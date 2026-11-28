---
title: "Container sind keine Sicherheitsgrenze mehr: Kernel-Ausbrüche im Jahr 2026"
date: 2026-09-28
lastmod: 2026-11-19
toc: true
draft: false
description: "Ein Überblick über Container-Ausbruchsforschung aus 2026, die Grenzen der Kernel-Isolation, den Patchdruck und die Rolle von MicroVMs."
genre: ["Containersicherheit", "Linux", "Kernel-Sicherheit", "Virtualisierung", "Cloud-Sicherheit", "Bedrohungsforschung", "Verteidigungsteam", "DevSecOps"]
tags: ["Container Escape", "Containersicherheitsgrenze", "Linux-Kernel-CVE", "lokale Rechteausweitung", "LPE 2026", "Copy Fail", "CVE-2026-31431", "Dirty Frag", "CVE-2026-43284", "CVE-2026-43500", "Fragnesia", "CVE-2026-46300", "CVE-2026-80521", "kernelCTF", "kvmCTF", "MicroVM", "Firecracker", "Kata Containers", "Page-Cache-Korruption", "AF_ALG", "AF_UNIX", "XFRM ESP", "RxRPC", "Namespace-Isolation", "clone-Systemaufruf", "KI-gestützte Schwachstellensuche", "Docker-Sicherheit", "Kubernetes-Sicherheit", "Mandantenisolation", "Sandbox-Ausbruch", "nsjail", "Bubblewrap", "Firejail", "Dirty Pipe", "Kernel-CVE-Trend"]
cover: "/img/cover/container-security-vulnerabilities-kernel-escapes-2026.webp"
coverAlt: "Digitale Illustration mehrerer leuchtender Container, die mit einem zentralen Kernel-Symbol verbunden sind. Farbige Elemente zeigen Sicherheitslücken, die sich vor dunklem Hintergrund vom Kernel ausbreiten."
coverCaption: ""
ref: ["/articles/docker-vs-vms", "/articles/how-to-secure-your-docker-and-kubernetes-environment", "/cvss-calculator"]
---
**Container teilen sich einen Kernel. Vier unabhängige Schwachstellenfamilien haben 2026 gezeigt, dass ein einziger Kernel-Fehler ausreicht, um einen Container zu verlassen und den Host zu erreichen.** Copy Fail, Dirty Frag, Fragnesia und CVE-2026-80521 verschaffen einem nicht privilegierten lokalen Benutzer Root-Rechte. Jede dieser Schwachstellen durchbricht die Containergrenze.

*Das Beunruhigende sind nicht die Fehler selbst. Es ist, wie kostengünstig KI sie inzwischen findet und dass ein Patch einen weiteren Fehler verursacht hat.*

Dieser Artikel erklärt, wie Container Workloads isolieren, warum diese Isolation inzwischen auf einem schmaler werdenden Fundament steht, was die einzelnen Schwachstellen aus 2026 bewirken und welcher Isolationstechnologie du stattdessen vertrauen solltest.

**Ergebnis für Leser:** Erfasse für jeden Workload, wer den Code bereitstellt, ermittle die benötigten Kernel-Funktionen und entscheide dich zwischen gehärteten Containern und einer MicroVM-Grenze. Behandle die Fallstudien aus 2026 als zeitgebundene Forschungsergebnisse. Prüfe aktuelle Herstellerhinweise, bevor du einen Produktivkernel änderst.

## Die kurze Antwort

| Frage | Kurze Antwort |
|---|---|
| **Isolieren Container?** | Ja, Prozesse und Dateisysteme. Alle Container teilen sich einen Kernel, deshalb sind Kernel-Fehler ein gemeinsames Risiko |
| **Warum jetzt?** | KI-gestützte Fehlersuche hat die Kosten für das Finden von Kernel-Schwachstellen stark gesenkt. Bis September 2026 wurden fast **6.000 Kernel-CVEs** veröffentlicht |
| **Was durchbricht die Grenze?** | Jede lokale Rechteausweitung im Kernel. Für einen Ausbruch ist keine Fehlkonfiguration des Containers nötig |
| **Reicht Patchen aus?** | Es ist nötig, aber das Tempo reicht nicht mehr. Ein Patch aus 2026 **führte einen neuen ausnutzbaren Fehler ein** |
| **Was funktioniert besser?** | MicroVMs wie Firecracker oder Kata Containers, die jedem Workload einen eigenen Kernel geben |
| **Ist die Alternative perfekt?** | Nein. Auch der Hypervisor besteht aus Code. Seine Angriffsfläche ist um viele Größenordnungen kleiner, und genau das ist entscheidend |

## Wie Container isolieren

Um die Grenze zu verstehen, musst du wissen, was ein Container nicht ist.

**Ein Container ist keine virtuelle Maschine.** Zwischen deinem Prozess und der Hardware gibt es weder einen zweiten Kernel noch emulierte Hardware oder einen Hypervisor. Wenn du ein Container-Image startest, läuft ein Prozess auf deinem vorhandenen Kernel, aber mit einer veränderten Sicht auf das System.

Der Mechanismus ist der **Systemaufruf `clone`**. Während `fork` den Adressraum eines Prozesses kopiert, erstellt `clone` einen Kindprozess und gibt dem Aufrufer genaue Kontrolle darüber, welche Teile des Ausführungskontexts gemeinsam genutzt und welche ersetzt werden. Docker übergibt `clone` eine Reihe von **Namespaces**:

| Namespace | Was er vortäuscht |
|---|---|
| **Mount** | Eine private Dateisystemwurzel, sodass der Container seinen eigenen Baum statt deines sieht |
| **PID** | Eigene Prozessnummern, sodass `PID 1` der erste Prozess des Containers und nicht `systemd` ist |
| **User** | Eine Identitätszuordnung, bei der „root“ im Container einem nicht privilegierten Hostbenutzer entspricht |
| **Network** | Private Schnittstellen, Routingtabellen und Ports |
| **IPC** | Isolierten gemeinsamen Speicher und Nachrichtenwarteschlangen |
| **UTS** | Einen eigenen Hostnamen und Domänennamen |
| **Cgroup** | Eine private Sicht auf Ressourcengrenzen |

Lege ein **Union-Dateisystem** über ein Image, und das Ergebnis *fühlt sich* wie ein eigener Computer an. `id` meldet im Container `uid=0(root)`. Das Dateisystem sieht wie ein minimales Ubuntu aus. Eine Prozessliste zeigt nur die eigenen Prozesse.

**Auf der Ebene der Systemaufrufe ist nichts davon eine Sicherheitsgrenze.** Wenn ein Prozess im Container eine Datei öffnet, Speicher zuweist oder einen Netzwerk-Socket nutzt, bearbeitet derselbe Kernel die Anfrage für jeden Container auf dem Host. Namespaces ändern, *was der Prozess sieht*, nicht, *was der Kernel für ihn tut*.

*Der Kernel ist die tatsächliche Grenze zwischen Container und Host. Alles andere ist Darstellung.*

{{< figure src="container-namespace-isolation-shared-kernel.webp" alt="Diagramm mit drei Containern auf demselben Kernel. Mount-, PID-, User- und Network-Namespaces trennen ihre Ansichten, während alle Systemaufrufe weiterhin an denselben gemeinsamen Kernel gehen." >}}

{{< youtube id="9-2CSJC114k" enable="true" title="the change is finally coming" nocookie="true" >}}

## Die Grenze besteht aus Code, und Code enthält Fehler

Jede Aktion eines Containers läuft über die **Systemaufrufschnittstelle**. Eine Datei öffnen, Speicher lesen, in einen Socket schreiben, eine UID ändern: Der Kernel vermittelt all das, weil er nicht möchte, dass Prozesse CPU, Dateisystem oder Netzwerk direkt berühren.

Die Vermittlung bildet das Sicherheitsmodell und ist als Code implementiert. Es sind ungefähr **30 Millionen Zeilen**.

Eine lokale Rechteausweitung (LPE) tritt auf, wenn ein Prozess einen Fehler im vermittelnden Code ausnutzt, um nicht gewährte Rechte zu erhalten. **LPEs sind nicht neu.** Sie existieren seit den ersten Kernel-Vermittlungsmechanismen. Die Branche lebte jahrzehntelang mit einem stetigen, aber überschaubaren Strom solcher Fehler.

**Dirty Pipe aus 2022** ist der bekannte Referenzfall. Ein Fehler in der Pipe-Pufferverarbeitung ermöglichte das Überschreiben schreibgeschützter Dateien. Die Schwachstelle war ein großes Thema, weil Fehler dieser Schwere **etwa alle ein bis zwei Jahre** auftraten. Man spielte den Patch ein, machte weiter und vertraute darauf, dass kein großer Defekt im Code verborgen blieb, den eine Million Menschen gelesen hatten.

*Diese Annahme gilt nicht mehr.*

## Was sich 2026 geändert hat

Die Änderung liegt nicht an den Fähigkeiten der Angreifer. **Das Finden speicherkorrumpierender Kernel-Fehler wurde zu einer technischen Aufgabe statt zu einer Forschungslaufbahn.**

Drei Datenpunkte aus diesem Jahr zeigen den Wandel:

| Fund | Entdecker | Wie |
|---|---|---|
| **Copy Fail** (CVE-2026-31431) | Taeyang Lee, Theori | Unterstützt durch **Xint Code**, ein KI-Werkzeug für statische Analyse. Etwa **eine Stunde Scanzeit** im Linux-Kryptografie-Subsystem |
| **CVE-2026-80521** | Zhenpeng (Leo) Lin, DepthFirst | Mit **dfs-large1** gefunden, einem intern entwickelten KI-Modell zur Schwachstellenerkennung |
| **CVE-2026-80521**, unabhängig | Kyle, **OpenAI** | Derselbe Fehler, unabhängig entdeckt und am selben Tag gemeldet |

Lies die dritte Zeile noch einmal. Zwei Organisationen nutzten unterschiedliche KI-Werkzeuge, fanden **dasselbe AF_UNIX-Use-after-free** und meldeten es **am selben Tag** an `security@kernel.org`. Das ist kein Zufall aufgrund besonderer Begabung. Ein wiederholbares Verfahren lieferte zweimal dieselbe Antwort.

DepthFirst nennt den Umfang ausdrücklich: **Bis September 2026 waren fast 6.000 Kernel-CVEs veröffentlicht**. Die Zahl wächst parallel zur Verfügbarkeit von KI-Unterstützung, nicht zur Zahl der Kernelentwickler.

*Wenn eine Stunde KI-Scanzeit einen zehn Jahre alten Fehler im Kryptografie-Subsystem findet, hat sich die Wirtschaftlichkeit der Kernel-Ausnutzung umgekehrt.*

## Vier Ausbrüche in einem Jahr

Jede dieser Schwachstellen verschafft einem nicht privilegierten lokalen Konto Root-Rechte. Keine erfordert eine Fehlkonfiguration des Containers, ein Privileged-Flag oder einen Netzwerkzugang.

| Schwachstelle | CVE | Subsystem | Primitive | Entdeckt von |
|---|---|---|---|---|
| **Copy Fail** | CVE-2026-31431 | `algif_aead` / AF_ALG | Schreibt 4 Byte in den Page Cache jeder lesbaren Datei | Theori, KI-gestützt |
| **Dirty Frag** | CVE-2026-43284 + CVE-2026-43500 | XFRM ESP, RxRPC | Schreibt 4 Byte über zwei verkettete Varianten in den Page Cache | Hyunwoo Kim |
| **Fragnesia** | CVE-2026-46300 | XFRM ESP-in-TCP (ESP in TCP gekapselt) | Einzelne Byte-Schreibvorgänge in den Page Cache | Hyunwoo Kim |
| **AF_UNIX UAF** | CVE-2026-80521 | AF_UNIX-Sockets | Use-after-free bei der Garbage Collection von `unix_vertex` | DepthFirst, KI-gestützt |

Alle vier haben ein gemeinsames Muster, das auffällt: **Sie greifen den Page Cache an, nicht den Datenträger.**

### Copy Fail: ein Logikfehler ohne Race Condition

Copy Fail ist der einfachste der vier Fehler und der alarmierendste.

Fast jede Linux-LPE erfordert ein Zeitfenster oder einen kernelspezifischen Speicher-Offset. **Copy Fail braucht weder das eine noch das andere.** Es ist ein direkter Logikfehler in `algif_aead`, dem Modul, das den Zugriff auf authentifizierte Verschlüsselung über AF_ALG aus dem Userspace bereitstellt.

Die Angriffskette nutzt `splice()`, um eine Page-Cache-Seite in den Vorgang einzufügen, und missbraucht anschließend den AEAD-In-Place-Pfad, um **vier kontrollierte Byte** in diese Seite zu schreiben. Die beschädigte Seite wird **nie als dirty markiert** und deshalb nicht auf den Datenträger zurückgeschrieben. Die Datei auf dem Datenträger bleibt unverändert. Prüfungen von Prüfsummen und Integrität bestehen, obwohl die Speicherkopie die Änderung enthält.

Ein **732 Byte großes Python-Skript** erlangt Root-Rechte auf jeder seit 2017 veröffentlichten Linux-Distribution. Der Fehler wurde durch eine **Optimierung aus dem Jahr 2017** in `algif_aead` eingeführt. Der Patch von 2026 macht diese Optimierung einfach rückgängig. Mainline-Commit `a664bf3d603d`.

*Der Fehler steckte fast ein Jahrzehnt in jeder verbreiteten Distribution. Ein KI-Werkzeug fand ihn in etwa einer Stunde.*

### Dirty Frag: zwei Varianten, die sich ergänzen

Der Name Dirty Frag beschreibt die Verwandtschaft genau. **Dirty Pipe überschreibt `struct pipe_buffer`. Dirty Frag überschreibt das Feld `frag` von `struct sk_buff`.**

Es sind **zwei verkettete Schwachstellen**. Genau diese Verkettung ist der clevere Teil:

- **CVE-2026-43284** nutzt aus, dass `esp_input()` den Copy-on-Write-Pfad überspringt, bevor es ein eingefügtes Fragment direkt entschlüsselt. Dafür braucht man das Recht, einen **User-Namespace** anzulegen, was manche Distributionen einschränken.
- **CVE-2026-43500** nutzt aus, dass `rxkad_verify_packet_1()` das Fragment direkt entschlüsselt. Es benötigt keine Namespace-Rechte, aber das Modul `rxrpc` fehlt auf den meisten Distributionen. Ubuntu lädt es standardmäßig.

**Jede Variante hat allein einen blinden Fleck. Zusammen ergänzen sie sich.** Wenn User-Namespaces erlaubt sind, läuft zuerst der ESP-Pfad. Ist er blockiert, aber `rxrpc` vorhanden, läuft stattdessen der RxRPC-Pfad. Eine Exploit-Binärdatei funktioniert dadurch auf verschiedenen Distributionen. Die RxRPC-Variante erlangt Root, indem sie ein Feld in `/etc/passwd` leert und PAM mit `nullok` ein leeres Passwort akzeptieren lässt.

**Für Verteidiger ist besonders wichtig:** Dirty Frag funktioniert **unabhängig davon, ob `algif_aead` verfügbar ist**. Die verbreitete Copy-Fail-Maßnahme, das Modul auf eine Sperrliste zu setzen, **schützt überhaupt nicht vor Dirty Frag**.

### Fragnesia: der Patch, der einen Fehler verursachte

Fragnesia gehört zur selben Klasse wie Dirty Frag, zielt aber auf den XFRM-Pfad **ESP-in-TCP**. Dies ist der lehrreichste Eintrag der Gruppe.

Die Schwachstelle nutzt die fehlerhafte Verarbeitung gemeinsamer Seitenfragmente beim `skb`-Zusammenführen aus. Ein Angreifer fügt dateigestützte Seiten mit `splice()` in eine TCP-Empfangswarteschlange ein, bevor der Socket in den `espintcp`-Modus für Protokolle höherer Schichten wechselt. Sobald die ESP-Verarbeitung aktiv wird, entschlüsselt der Kernel die eingereihten Daten **direkt an Ort und Stelle**, und die Manipulation des AES-GCM-Keystreams korrumpiert den Page Cache. Der Angreifer erhält wiederholt **Schreibzugriff auf einzelne Byte** in zwischengespeicherten Dateiseiten.

Der Exploit erlangt Root, indem er die ersten Bytes von `/usr/bin/su` mit einem kleinen ELF-Payload überschreibt. **Die Änderung existiert nur im Speicher und berührt nie die Binärdatei auf dem Datenträger.**

Nicht privilegierte **User- und Network-Namespaces** stellen `CAP_NET_ADMIN` innerhalb eines isolierten Namespace bereit. Anschließend installiert `NETLINK_XFRM` eine präparierte Security Association.

*Dieser Satz ist wichtig:* Fragnesia entstand als **unbeabsichtigte Nebenwirkung eines der Patches für die ursprünglichen Dirty-Frag-Schwachstellen**. Der Patch für Dirty Frag erzeugte einen neuen, eigenständig ausnutzbaren Root-Fehler.

### CVE-2026-80521: der Container-Ausbruch, der kernelCTF gewann

Der AF_UNIX-Race beendet die Diskussion darüber, ob das nur theoretisch ist.

Die Schwachstelle ist ein **Heap-Use-after-free** im Garbage-Collection-Mechanismus für `SCM_RIGHTS`-Nachrichten, mit denen Prozesse Dateideskriptoren weitergeben. Beim Sammeln einer zirkulären Socket-Referenz gibt ein Race `struct unix_vertex` frei, obwohl der SCC-Ring eines überlebenden Sockets noch auf das Objekt verweist. Der nächste Sammeldurchlauf folgt dem veralteten Ring und dereferenziert freigegebenen Speicher.

Warum das über Linux im Allgemeinen hinaus wichtig ist: **AF_UNIX bildet die Grundlage lokaler IPC.** Lokale Datenbanken, `systemd` und Docker selbst hängen davon ab. DepthFirst zufolge betrifft die Schwachstelle die meisten Kernel-basierten Sandboxes auf Betriebssystemebene, **darunter `nsjail`, `Firejail` und `Bubblewrap`**, sowie moderne Container-Runtimes.

DepthFirst gewann damit am **24. Juli 2026** **einen Google-kernelCTF-Slot**. Die Bestätigung im Slot `lts-6.12.95` kam am **5. August**. Das Unternehmen meldete den Fehler noch am selben Tag an `security@kernel.org` und erfuhr, dass **Kyle von OpenAI denselben Fehler gemeldet hatte**. Der Upstream-Patch wurde am **6. August** übernommen. Die Forschung wurde am **22. September** veröffentlicht.

Das Team veröffentlichte einen funktionsfähigen Exploit für **Ubuntu 26.04** sowie einen zweiten Exploit für einen Ausbruch aus **Ubuntu 24.04** über CVE-2026-52910.

{{< figure src="kernel-page-cache-overwrite-container-escape.webp" alt="Diagramm, in dem ein nicht privilegierter Prozess in einem Container eine Page-Cache-Seite korrumpiert, um eine setuid-Binärdatei im Speicher zu ändern. Der Prozess erhält Root-Rechte und verlässt die Containergrenze über den Host-Kernel." >}}

## Warum die Hinweise zur Abwehr immer wieder scheitern

Verteidiger erhielten in diesem Jahr drei Runden mit Workarounds, und jede war teilweise falsch.

| Maßnahme | Was sie verhindert | Was sie übersieht |
|---|---|---|
| **`algif_aead`** auf eine Sperrliste setzen | Copy Fail | **Nichts bei Dirty Frag**, das das Modul vollständig ignoriert |
| **`esp4`, `esp6` und `rxrpc`** sperren | Dirty Frag, Fragnesia | Teams, die IPsec benötigen. Außerdem werden völlig neue Subsysteme übersehen |
| **Nicht privilegierte User-Namespaces** beschränken | Die ESP-Varianten | Die RxRPC-Variante braucht keinen Namespace. Eine AppArmor-Richtlinie ist nur eine **teilweise** Maßnahme |
| **Kernel patchen** | Den behobenen Fehler | Den nächsten Fehler und jeden Fehler, den ein Patch einführt |

Zwei Muster fallen auf.

**Erstens widersprechen sich die Workarounds.** Copy Fail wird durch das Deaktivieren von `algif_aead` eingedämmt. Dirty Frag funktioniert ausdrücklich **auch dann**, wenn das Modul fehlt. Für Fragnesia müssen `esp4` und `esp6` deaktiviert werden, was für IPsec-Nutzer problematisch ist. Es gibt keine einzelne Modulsperrliste für die gesamte Familie.

**Zweitens ist Patchen, noch schlimmer, kein eindeutiger Gewinn.** Fragnesia wurde **durch den Patch für Dirty Frag eingeführt**. Jeder Patch kann neue Logikfehler mit sich bringen. In diesem Subsystem wird ein Logikfehler zu einem Root-Exploit.

*Die unangenehme Schlussfolgerung: Diese Schwachstellen liegen alle im Page Cache, sind aus nicht privilegiertem Code erreichbar und wurden mit Werkzeugen gefunden, die jedes Quartal besser werden. Keine Sperrliste bleibt vollständig.*

## Das Gegenargument, ehrlich beantwortet

Es gibt einen berechtigten Einwand, der eine klare Antwort verdient: **Auch Hypervisoren haben Fehler.**

Die KVM-Angriffsfläche ist real. Google betreibt **kvmCTF** gezielt, um solche Fehler zu finden, und zahlt dafür hohe Prämien:

| Stufe | Prämie |
|---|---|
| **Vollständiger VM-Ausbruch** | **$250,000** |
| Beliebiger Schreibzugriff auf den Speicher | $100,000 |
| Beliebiger Lesezugriff auf den Speicher | $50,000 |
| Relativer Schreibzugriff auf den Speicher | $50,000 |
| Dienstverweigerung | $20,000 |
| Relativer Lesezugriff auf den Speicher | $10,000 |

Prämien werden nicht addiert. Ziel ist ein Linux-LTS-Kernel mit KVM, die Gast-VM ist Debian 12.5. Das Ziel ist ein **Angriff vom Gast auf den Host**.

**Hyunwoo Kim, derselbe Forscher, der Dirty Frag fand, erhält auch KVM-Prämien** und gewann die vollen $250,000 für einen VM-Ausbruch. Die ehrliche Zusammenfassung: Beide Ebenen haben Fehler, und manchmal findet sie dieselbe Person.

**Vergleiche die Größenordnungen:**

| | Linux-Kernel | KVM-Hypervisor |
|---|---|---|
| **CVEs im Jahr 2026** | Fast **6.000** | Eine Handvoll, einzelne Forscher finden einige pro Jahr |
| **Erreichbar von** | Jedem nicht privilegierten Prozess über die Systemaufrufschnittstelle | Nur von Code, der bereits in einem Gast läuft |
| **Angriffsfläche** | Alles: Netzwerk, Dateisysteme, Kryptografie, IPC, Treiber | Schnittstelle virtueller Geräte und Hypercalls |
| **Fehlerklasse** | Jeder Speicher- oder Logikfehler in 30 Mio. Zeilen | Auf die Virtualisierungsgrenze beschränkt |

*Der Unterschied beträgt viele Größenordnungen, nicht den Faktor zwei. Deshalb ändern MicroVMs die Risikobewertung.*

## Was eine echte Grenze bietet

Eine **MicroVM** gibt jedem Workload eine eigene **Kernel-Instanz**, die auf hardwaregestützter Virtualisierung läuft, statt den Host-Kernel über Namespaces gemeinsam zu nutzen.

Der Stack hat drei wichtige Ebenen:

- **Die CPU** stellt Hardwaremechanismen bereit, die Speicherbereiche voneinander isolieren.
- **KVM** stellt diese Mechanismen dem Linux-Kernel zur Verfügung, sodass der Kernel als Hypervisor arbeitet.
- **Ein VMM (System zur Steuerung virtueller Maschinen)** wie Firecracker oder QEMU steuert KVM, um den Gast zu erstellen und auszuführen.

Da der Gast einen eigenen Kernel ausführt, kompromittiert ein Kernel-Exploit **im Gast** nur den Gast. Es gibt keinen gemeinsamen Kernel, den man angreifen kann. Ein Angreifer müsste danach aus dem Hypervisor ausbrechen, der kleineren Angriffsfläche, in der KVM-Fehler liegen.

In der Praxis sind zwei Implementierungen wichtig, beide Teil der Empfehlung von DepthFirst:

| Technologie | Ansatz | Hinweise |
|---|---|---|
| **Firecracker** | Speziell entwickelte VMM mit minimalem Gerätemodell | Von AWS speziell für Mandantenisolation in großem Maßstab entwickelt |
| **Kata Containers** | OCI-kompatible Runtime, die eine MicroVM kapselt | Führt Standard-Container-Images mit einer VM-Grenze darunter aus |

Für die meisten Teams ist Kata die einfachere Migration, weil es die bereits genutzten Container-Images und Werkzeuge akzeptiert. **Firecracker hat eine kleinere Angriffsfläche**, weil es deutlich weniger Geräte emuliert als eine Allzweck-VMM.

{{< figure src="microvm-vs-container-isolation-boundary.webp" alt="Diagramm vergleicht Container-Isolation über Namespaces auf einem gemeinsamen Kernel mit MicroVM-Isolation, bei der jeder Workload einen eigenen Kernel auf KVM und einem Virtual Machine Monitor ausführt." >}}

## Was du jetzt tun solltest

Nicht jeder Container braucht eine MicroVM. Die Entscheidung hängt davon ab, **wessen Code darin läuft**.

| Deine Situation | Risiko | Maßnahme |
|---|---|---|
| **Du führst eigenen Code aus**, einzelner Mandant | Niedrig | Behalte Container. Spiele Patches zügig ein, entferne Capabilities und verwende ein schreibgeschütztes Root-Dateisystem |
| **Hosts mit mehreren Mandanten**, Shell-Zugang für Benutzer | **Hoch** | Verlege nicht vertrauenswürdige Workloads in MicroVMs. DepthFirst nennt diesen Fall zuerst |
| **CI-Runner, die nicht vertrauenswürdige PRs ausführen** | **Hoch** | Ein Pull Request kann auf dem Runner Root werden. Isoliere jeden Job in einer eigenen VM |
| **Notebooks, Agenten-Sandboxes, Serverless** | **Hoch** | Mandantencode wird auf dem Host zu Root. Eine MicroVM pro Mandant |
| **Kubernetes-Cluster** | **Erhöht** | Der Page Cache wird auf dem Host gemeinsam genutzt. Ein Pod mit den passenden Primitiven kompromittiert den Knoten und überschreitet Mandantengrenzen |

Das gemeinsame Prinzip ist einfach. **Container eignen sich hervorragend für Paketierung und Prozessisolation.** Sie wurden nie dazu entwickelt, feindlichen Code einzudämmen. Die Branche hat sie stillschweigend dafür zweckentfremdet, weil sie bequem und günstig waren.

### Härtung, die immer hilft

Nichts davon ersetzt eine VM-Grenze, aber jede Maßnahme beseitigt einfache Angriffswege:

```bash
# Deaktiviere die von der Page-Cache-Familie missbrauchten Module, wenn sie nicht benötigt werden
printf 'install algif_aead /bin/false\ninstall esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' \
  > /etc/modprobe.d/harden-pagecache-family.conf
rmmod algif_aead esp4 esp6 rxrpc 2>/dev/null || true
```

```bash
# Beschränke nicht privilegierte Benutzer-Namespaces, wodurch die ESP-Varianten blockiert werden
# Debian und Ubuntu: Dies ist eine teilweise, keine vollständige Schadensbegrenzung
sysctl -w kernel.unprivileged_userns_clone=0

# Bei Verdacht auf Ausnutzung den Page-Cache leeren, um geänderte Binärdateien im Speicher zu verwerfen
echo 1 | tee /proc/sys/vm/drop_caches
```

```text
# Erste Hinweise zur Erkennung
- Unerwartetes unshare(CLONE_NEWUSER) durch eine Arbeitslast ohne legitimen Grund
- NETLINK_XFRM-Aktivität oder XFRM-Sicherheitszuordnungen außerhalb von IPsec-Hosts
- Anfragen zum Binden von AF_ALG-Sockets
- Laden von esp4, esp6 oder rxrpc auf Hosts ohne IPsec und AFS
```

> **Warnung: `drop_caches` verwirft die veränderte Speicherkopie und beseitigt dadurch die Korruption. Es entfernt aber keinen Angreifer, der bereits Root erreicht hat. Behandle dies als Reaktion auf einen Sicherheitsvorfall, nicht als Behebung.**

### Das Problem mit dem Patch-Zyklus

Selbst mit den besten Absichten ist Kernel-Patching zu einem Wettlauf geworden:

- Fast **6.000 in diesem Jahr veröffentlichte CVEs** übersteigen allein aufgrund ihrer Menge die meisten Wartungsfenster.
- **Ein Patch führt einen Fehler ein.** Fragnesia hat das in genau diesem Subsystem bewiesen.
- **Die Maßnahmenliste läuft ab.** Im April war `algif_aead` die Antwort. Im Mai schützte es vor nichts in Dirty Frag.

*Schnelles Patchen ist notwendig und nicht ausreichend. Die Architektur entscheidet, ob ein verpasster Patch zu einem eingedämmten Vorfall oder zur Host-Kompromittierung führt.*

## Die schwierigere Frage: Wer ist der Gegner?

Die technische Antwort ist klar. Die strategische hängt von einer Frage ab, die viele Teams überspringen.

**Wenn dein Bedrohungsmodell einen neugierigen Benutzer oder einen unachtsamen Entwickler umfasst, bleiben Container ausreichend.** Ein Container-Ausbruch erfordert lokale Codeausführung plus einen Kernel-Exploit. Beides ist nicht selbstverständlich, und die Betriebskosten einer vollständigen Migration zu MicroVMs sind real.

**Wenn dein Bedrohungsmodell einen Gegner einschließt, der Code auf deiner Infrastruktur ausführt, sind Container inzwischen nur noch eine Bremsschwelle.** Die Schlussfolgerung von DepthFirst ist ein direktes Zitat wert:

> "Die Einstiegshürde, diese Schwachstellen als Waffe einzusetzen, ist so stark gesunken, dass wir annehmen müssen, Angreifer könnten Standard-Container jederzeit nach Belieben verlassen."

Das ist ein Sicherheitsanbieter mit einem Produkt, das er verkaufen möchte, und einer Empfehlung für eine bestimmte Architektur. Die gebotene Skepsis ist berechtigt. **Das Argument hängt jedoch nicht vom Anbieter ab.** Die Zahl von 6.000 CVEs ist öffentlich, die Exploits sind veröffentlicht und der Kernel ist konstruktionsbedingt gemeinsam genutzt.

*Die ehrliche Einordnung: Gegen einen Angreifer mit einem ersten Zugang verliert der Container als Grenze an Wert. Gegen alles andere behält er seinen Wert.*

## Das Fazit

**Container bleiben das richtige Werkzeug für Paketierung, Deployment und Prozessseparation. Gegen feindlichen Code sind sie keine zuverlässige Sicherheitsgrenze mehr.**

Drei Aussagen, nach Sicherheit geordnet:

1. **Die technische Grundlage steht fest.** Container teilen sich den Host-Kernel. Jede der vier Schwachstellen in diesem Artikel überschritt die Grenze von einem nicht privilegierten Konto aus, und die Exploits sind öffentlich.
2. **KI veränderte das Tempo, nicht das Prinzip.** Kernel-LPEs gab es schon immer. Heute kostet das Finden eines Fehlers etwa **eine Stunde KI-Scanzeit** statt monatelanger Expertenarbeit, und zwei Organisationen fanden unabhängig denselben Zero-Day am selben Tag.
3. **Migration kostet, Nicht-Migration ebenfalls.** Firecracker und Kata verursachen Overhead, Betriebskomplexität und erfordern neue Fähigkeiten. Die Abwägung ist klar: Akzeptiere den Overhead oder akzeptiere, dass ein Kernel-Fehler den Host kompromittiert.

**Wenn du Mandanteninfrastruktur betreibst oder nicht vertrauenswürdigen Code ausführst, plane jetzt die MicroVM-Migration.** Nicht weil der Himmel einstürzt, sondern weil die Entwicklung eindeutig ist und eine Migration Quartale statt Wochen dauert.

**Wenn du Container mit eigenem Code für einen einzelnen Mandanten betreibst, behalte sie bei.** Spiele Kernel-Patches schneller ein als bisher, deaktiviere nicht benötigte Module und prüfe die Entscheidung erneut, wenn nicht vertrauenswürdiger Code hinzukommt.

*Die Ära, in der der Kernel bedingungslos als vertrauenswürdige Grenze galt, geht zu Ende. Infrastruktur, die mit einem kompromittierten Kernel rechnet, übersteht den Einbruch.*

## Wichtigste Erkenntnisse

- **Container teilen sich den Host-Kernel.** Die Isolation stammt von Namespaces des `clone`-Systemaufrufs, nicht von Hardwarevirtualisierung. Ein Kernel-Fehler ist daher auch ein Container-Fehler.
- **Vier Schwachstellen aus 2026 durchbrachen die Grenze** von nicht privilegierten lokalen Konten aus: Copy Fail, Dirty Frag, Fragnesia und CVE-2026-80521. Alle vier zielen auf den Page Cache.
- **Bis September 2026 wurden fast 6.000 Kernel-CVEs** veröffentlicht; KI-Werkzeuge beschleunigen die Suche. **Copy Fail wurde in etwa einer Stunde Scanzeit gefunden.**
- **Fragnesia wurde durch den Patch für Dirty Frag eingeführt.** Das Patchen erzeugte einen neuen Root-Fehler im selben Subsystem.
- **Der Copy-Fail-Workaround verhindert Dirty Frag nicht.** Das Sperren von `algif_aead` deckt eine Schwachstelle ab, aber keine weitere aus der Familie.
- **CVE-2026-80521 brachte auch `nsjail`, `Firejail` und `Bubblewrap` zu Fall**, nicht nur Container-Runtimes.
- **MicroVMs verändern die Risikobewertung**, weil jeder Workload einen eigenen Kernel bekommt. KVM hat Fehler, aber seine Angriffsfläche ist um viele Größenordnungen kleiner.
- **Entscheide danach, wer den Code ausführt.** Eigener Code in einem Container für einen einzelnen Mandanten bedeutet ein geringes Risiko. Nicht vertrauenswürdiger Code auf einem gemeinsam genutzten Host bedeutet Kompromittierungsrisiko.

## Nächste Schritte

1. **Lies die Analyse des Problems** und den veröffentlichten Exploit: **[Container sind keine Sicherheitsgrenze mehr - DepthFirst](https://depthfirst.com/research/containers-are-no-longer-safe)**
2. **Prüfe den maßgeblichen Hinweis und die Abwehrmaßnahmen** für die Copy-Fail-Familie: **[CERT/CC VU#260001](https://www.kb.cert.org/vuls/id/260001/)**
3. **Lies den technischen Dirty-Frag-Bericht**, um die Verkettung und das Versagen der `algif_aead`-Maßnahme zu verstehen: **[Technischer Bericht zu Dirty Frag](https://github.com/V4bel/dirtyfrag)**
4. **Prüfe die Regeln und Prämienstufen von kvmCTF**, um die Größe der Hypervisor-Angriffsfläche zu verstehen: **[kvmCTF-Übersicht](https://google.github.io/security-research/kvmctf/rules.html)**
5. **Bewerte diese CVEs in deiner Umgebung** mit unserem clientseitigen Werkzeug: **[CVSS-v3.1-Rechner](/cvss-calculator/)**
6. **Härtung deiner aktuellen Umgebung**: **[So sicherst du deine Docker- und Kubernetes-Umgebung ab](/articles/how-to-secure-your-docker-and-kubernetes-environment/)**
7. **Verstehe den Isolation-Kompromiss genauer**: **[Docker im Vergleich zu virtuellen Maschinen 2026](/articles/docker-vs-vms/)**
8. **Reduziere Berechtigungen, wenn du keine zusätzliche Grenze einziehen kannst**: **[Least-Privilege-Zugriffssteuerung unter Linux meistern](/articles/mastering-least-privilege-access-control-linux/)**

## Verwandte Artikel

| Artikel | Inhalt |
|---|---|
| **[Docker im Vergleich zu virtuellen Maschinen 2026](/articles/docker-vs-vms/)** | Der Architekturvergleich hinter diesem Artikel, einschließlich Leistungs- und Sicherheitsabwägungen |
| **[So sicherst du deine Docker- und Kubernetes-Umgebung ab](/articles/how-to-secure-your-docker-and-kubernetes-environment/)** | Praktische Härtung der Container-Ebene, auch innerhalb einer MicroVM sinnvoll |
| **[Docker in LXC auf Proxmox: Zuverlässigkeit, Belege und VM-Migration](/articles/docker-in-lxc-proxmox-reliability/)** | Verschachtelte Container, Belege und der Zeitpunkt für den Umzug eines Workloads in eine vollständige VM |
| **[Virtualisierung verstehen: Konzepte und Anwendungen](/articles/understanding-virtualization_-concepts-and-applications/)** | Grundlagen zu Hypervisoren, einschließlich der CPU-Funktionen, auf die MicroVMs angewiesen sind |
| **[Least-Privilege-Zugriffssteuerung unter Linux meistern](/articles/mastering-least-privilege-access-control-linux/)** | Berechtigungen verringern, die ein Ausbruch verschaffen würde, und so den Schadensradius begrenzen |

## Quellen

1. [Container sind keine Sicherheitsgrenze mehr - DepthFirst (Zhenpeng Lin, 22. September 2026)](https://depthfirst.com/research/containers-are-no-longer-safe)
2. [CERT/CC Vulnerability Note VU#260001 - Copy Fail (CVE-2026-31431)](https://www.kb.cert.org/vuls/id/260001/)
3. [Offizielle Copy-Fail-Veröffentlichung und Exploit-Analyse](https://copy.fail/)
4. [Technischer Dirty-Frag-Bericht - Hyunwoo Kim (CVE-2026-43284, CVE-2026-43500)](https://github.com/V4bel/dirtyfrag)
5. [Fragnesia: lokale Rechteausweitung im Linux-Kernel über ESP-in-TCP - Wiz (CVE-2026-46300)](https://www.wiz.io/blog/fragnesia-linux-kernel-local-privilege-escalation-via-esp-in-tcp)
6. [kvmCTF-Übersicht und Prämienstufen - Google](https://google.github.io/security-research/kvmctf/rules.html)
7. [NVD-Eintrag für CVE-2026-31431](https://nvd.nist.gov/vuln/detail/CVE-2026-31431)
8. [Upstream-Mainline-Commit für die Copy-Fail-Korrektur](https://github.com/torvalds/linux/commit/a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5)
9. [Ubuntu-Sicherheitshinweis zu verfügbaren Copy-Fail-Korrekturen](https://ubuntu.com/blog/copy-fail-vulnerability-fixes-available)
10. [KernelCTF-Exploits und Einreichungen - Google Security Research](https://github.com/google/security-research/tree/master/pocs/linux/kernelctf)

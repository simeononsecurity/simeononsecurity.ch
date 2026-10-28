---
title: "1Password SSH Agent und CLI: Nur-Lese-Zugriff für KI-Agenten"
date: 2026-10-11
lastmod: 2026-10-28
toc: true
draft: false
description: "Entwerfen Sie einen nur-lesbaren SSH-Workflow mit 1Password CLI, dem SSH Agent und MCP. Verwenden Sie synthetische Befehle, eingeschränkte Berechtigungen und menschliche Genehmigung vor dem Live-Test."
genre: ["Systemadministration", "Cloud-Sicherheit", "Automatisierung"]
tags: ["1Password CLI", "SSH-Schlüssel", "1Password SSH Agent", "MCP", "Model Context Protocol", "Agenten-Verwaltung", "Systemadministration", "Bitbucket Cloud", "Git über SSH", "Geheimnis-Referenzen", "Service-Konten", "Least Privilege", "Public-Key-Authentifizierung", "Geheimnisverwaltung", "Befehlszeilen-Sicherheit", "Automatisierungssicherheit"]
cover: "/img/cover/1password-cli-ssh-keys-mcp-agent-administration.webp"
coverAlt: "Abstrakte Darstellung eines Agenten, der eine Geheimnis-Referenz, einen SSH-Agenten und MCP-Tools verwendet, ohne private Schlüssel anzuzeigen."
coverCaption: ""
---

**Ein Agent für die Befehlszeile benötigt nützlichen Zugriff, keine Kopie aller Zugangsdaten.** Dieser Leitfaden stellt ein begrenztes Design für 1Password CLI, den 1Password SSH Agent, den Git-Zugriff auf Bitbucket und das Model Context Protocol (MCP) vor. Der erste Workflow verwendet synthetische Namen, schreibgeschützte Aktionen und die menschliche Genehmigung an der SSH-Grenze.

<!--more-->

Der entscheidende Unterschied ist einfach. **Interaktives SSH verwendet die Zustimmung über den 1Password SSH Agent. Autonome Automatisierung benötigt eine separate Identität, einen engen Zugriffsbereich und einen anderen Schlüssel-Lebenszyklus.** Behandeln Sie eine MCP-Verbindung nicht als Erlaubnis, einen dieser Workflows auszuführen.

## Wichtige Erkenntnisse

- **Schutz des privaten Schlüssels:** Der 1Password SSH Agent führt die SSH-Authentifizierung durch, während die privaten Schlüssel innerhalb der 1Password-App bleiben.
- **Verwaltung des öffentlichen Schlüssels:** Veröffentlichen Sie nur einen öffentlichen Schlüssel auf Bitbucket oder einem Remote-Konto. Bewahren Sie die private Hälfte in einem SSH-Schlüssel-Eintrag auf.
- **Interaktive Zustimmung:** Eine Person genehmigt eine Client- oder Terminal-Sitzung, bevor der SSH Agent einen Schlüssel verwendet.
- **Trennung für autonome Abläufe:** Ein geplanter Job benötigt ein dediziertes Dienstbenutzerkonto und einen engen Vault-Bereich. Eine interaktive SSH-Agent-Genehmigung erfüllt dieses Erfordernis nicht.
- **MCP-Grenzen:** MCP verbindet einen Agenten mit Werkzeugen und Ressourcen. Client, Server, Betriebssystem und 1Password-Richtlinie steuern weiterhin den Zugriff.

## Vor dem Start

**Voraussetzungen:** Installieren Sie 1Password 8 und 1Password CLI 2.20.0 oder neuer. Melden Sie sich über ein unterstütztes 1Password-Konto an. Verwenden Sie einen OpenSSH-Client. Erstellen Sie ein Test-Bitbucket-Repository oder ein anderes Nicht-Produktionsziel. Halten Sie einen zweiten administrativen Pfad für Rollbacks bereit.

**Zeitaufwand:** 30 bis 45 Minuten für eine Designprüfung und einen synthetischen Durchlauf.

**Schwierigkeitsgrad:** Mittel. Sie benötigen Grundkenntnisse in Git, SSH, Shell und Zugriffskontrolle.

Dieser Leitfaden behandelt Design und Planung. Der verlinkte Bitbucket-Artikel behandelt Bitbucket-spezifische Zugriffsgrenzen. Dieser Leitfaden testet kein Live-Konto, erstellt keinen echten Schlüssel, verbindet sich nicht mit einem echten Host und registriert keinen echten MCP-Server. Alle Kennungen unten sind synthetisch. **Ersetzen Sie Platzhalter nur innerhalb Ihrer eigenen kontrollierten Umgebung.**

**Versionsstatus:** Verwenden Sie 1Password 8 und [1Password CLI 2.20.0 oder neuer](https://www.1password.dev/ssh/manage-keys) für diesen Workflow. [1Password CLI 1 ist veraltet](https://www.1password.dev/cli/upgrade/). [1Password 7 wird Anfang 2027 eingestellt](https://support.1password.com/add-account/). Die Generierung, der Import und die Freigabe von SSH-Schlüsseln erfordern 1Password 8. Bestätigen Sie die installierten Versionen von Git, OpenSSH, MCP-Host und MCP-Server vor dem Testen. Die folgenden Beispiele bleiben ungetestet.

Ein **Vault** ist eine geschützte 1Password-Sammlung von Einträgen. **OpenSSH** ist die SSH-Client- und Server-Software, die von vielen Betriebssystemen verwendet wird. **MCP**, oder Model Context Protocol, verbindet einen Agenten mit genehmigten Tools oder Ressourcen.

## Warum Private Keys unlesbar halten

Ein SSH-Schlüsselpaar besteht aus einem öffentlichen Schlüssel und einem privaten Schlüssel. Ein entfernter Git-Dienst oder Server speichert den öffentlichen Schlüssel. Der Client weist während der Authentifizierung den Besitz des privaten Schlüssels nach. Der private Schlüssel muss nicht zum entfernten Dienst übertragen werden.

Der [1Password SSH Agent](https://www.1password.dev/ssh/agent) erweitert dieses Modell. Seine Dokumentation besagt, dass SSH- und Git-Clients sich über den Agenten authentifizieren, während der private Schlüssel in der 1Password-App verbleibt. Der Client erhält ein Signaturergebnis, keine private Schlüsseldatei.

Diese Grenze reduziert mehrere Expositionswege:

- **Quellcodeverwaltung:** Ein privater Schlüssel gelangt nicht in ein Repository oder einen Pull Request.
- **Shell-Verlauf:** Ein privater Schlüsselwert erscheint nicht in einem Befehlsargument.
- **Temporäre Dateien:** Ein Skript muss keinen privaten Schlüssel in `~/.ssh/` schreiben.
- **Agentenkontext:** Ein großes Sprachmodell (LLM) benötigt den privaten Schlüsseltext nicht, um eine SSH-Operation anzufordern.
- **Unbeabsichtigte Wiederverwendung:** Ein kopierter Schlüssel verbleibt nicht in einem alten Arbeitsbereich, nachdem eine Aufgabe beendet ist.

Die Grenze macht SSH nicht ungefährlich. Ein Prozess mit der Berechtigung, den Agenten-Socket zu verwenden, könnte Aktionen als der genehmigte Schlüssel ausführen. Host-Schlüssel-Verifizierung, Beschränkungen des entfernten Kontos, Repository-Berechtigungen, Befehlspolitik und Prozessisolierung sind nach wie vor von Bedeutung.

*Die Grenze des privaten Schlüssels schützt das Schlüsselmaterial. Die Grenze genehmigt keinen entfernten Befehl oder beweist, dass der Zielhost vertrauenswürdig ist.*

## Interaktive SSH-Zustimmung

Konfigurieren Sie ein dediziertes Vault für Agentenschlüssel. Verwenden Sie die SSH-Agenten-Konfigurationsdatei, um den kleinsten Schlüsselset und einen hostspezifischen Schlüssel auszuwählen. Stellen Sie nicht jeden qualifizierten Schlüssel aus jedem eingebauten Vault einem Automatisierungsprozess zur Verfügung.

Das [1Password SSH Agent Sicherheitsmodell](https://www.1password.dev/ssh/agent/security) bindet die Genehmigung an einen Schlüssel und einen anfragenden Prozess. Die Eingabeaufforderung identifiziert den Prozess und den Schlüssel. Die Person genehmigt dann die Anfrage über die konfigurierte Authentifizierungsmethode.

1Password dokumentiert mehrere Genehmigungsbereiche. Schlüssel- und anwendungsspezifische Genehmigung ist die Standardoption. Ein Terminal-Sitzungsbereich schränkt die Genehmigung auf einen Tab oder eine Sitzung ein. Eine pro Anfrage genehmigte Option fragt bei jeder Anfrage erneut. Eine alle-Prozesse-Genehmigungsoption existiert, aber diese Option gewährt jedem Prozess unter dem aktuellen Betriebssystembenutzer Zugriff für die Sitzung.

**Verwenden Sie den engsten Genehmigungsbereich, der für die Aufgabe geeignet ist.** Ein Agent für Systemadministration sollte in einem dedizierten Terminal oder einer Sandbox ausgeführt werden. Genehmigen Sie nicht jeden Prozess, wenn eine einzelne Terminal-Session ausreicht.

Die Genehmigungssitzung ist keine dauerhafte Berechtigung. 1Password protokolliert die Autorisierung für die konfigurierte Dauer oder bis die App gesperrt oder beendet wird. Wenn die App gesperrt ist, behält der Agent keine privaten Schlüssel für spätere Verwendung bei. Der SSH-Agent-Prozess läuft im Hintergrund weiter, wenn die unterstützte Einstellung aktiviert ist, während 1Password geschlossen ist, aber eine neue Signieranfrage erfordert, dass 1Password entsperrt ist.

Der [1Password-SSH-Einrichtungsleitfaden](https://www.1password.dev/ssh/get-started) zeigt den allgemeinen Ablauf: Schlüssel generieren oder importieren, öffentlichen Schlüssel veröffentlichen, SSH-Agent aktivieren, SSH-Client konfigurieren, einen SSH- oder Git-Befehl ausführen und die Anfrage genehmigen. Der genaue Socket-Pfad unterscheidet sich je nach Betriebssystem. Verwenden Sie die Anweisungen für die aktuelle Plattform, anstatt einen Pfad von einer anderen Maschine zu kopieren.

Die 1Password-App muss entsperrt sein, bevor eine neue Signieranfrage erfolgreich ist. Der Agent-Prozess kann im Hintergrund weiterlaufen, während die App geschlossen ist. Eine gesperrte App gibt kein privates Schlüsselmaterial zum Signieren frei.

## Öffentliche Schlüssel und Bitbucket

Der [1Password-Leitfaden zur Schlüsselverwaltung](https://www.1password.dev/ssh/manage-keys) dokumentiert SSH-Schlüssel-Elemente, Schlüsselgenerierung, Schlüsselimport, öffentliche Schlüssel, Fingerabdrücke und private Schlüssel. Das CLI-Beispiel verwendet `op item create --category ssh`, um ein SSH-Schlüssel-Element zu erstellen. 1Password CLI generiert für dieses Beispiel standardmäßig einen Ed25519-Schlüssel und redigiert den privaten Schlüssel in seiner Ausgabe.

Bitbucket Cloud verwendet den normalen Git- und OpenSSH-Workflow über die Befehlszeile. Sein [Befehlszeilenleitfaden](https://support.atlassian.com/bitbucket-cloud/docs/find-the-command-line/) beschreibt Git-Operationen aus einem lokalen Repository. Sein [SSH-Konfigurationsleitfaden](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) listet SSH-Remote-Formate und unterstützte öffentliche Schlüssel-Formate auf.

**Behandeln Sie Bitbucket als Verbraucher des öffentlichen Schlüssels.** Registrieren Sie den öffentlichen Schlüssel oder Fingerabdruck über die genehmigte Bitbucket-Konto- oder Repository-Einstellung. Bewahren Sie den privaten Schlüssel in 1Password auf. Der Git-Client bittet den SSH-Agenten um das Signieren. Der Client liest keine private Schlüssel-Datei.

Für den Bitbucket-Zugangsschlüssel-Bereich, den Registrierungspfad und den nur-lesenden Git-Test siehe [Bitbucket Cloud SSH Keys and Git CLI: Read-Only Access for AI Agents](/articles/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation/).

Die Bitbucket-Dokumentation bezeichnet dies als Git-CLI-Workflow. Dieser Artikel geht nicht von einem separaten Bitbucket-MCP-Server oder einem Produkt namens Bitbucket CLI aus. Ein Bitbucket-spezifisches CLI benötigt seine eigene aktuelle Dokumentation und seine eigene Berechtigungsprüfung.

## Die Grenze zwischen Agent und MCP

Verwenden Sie die aktuelle [MCP-Spezifikation](https://modelcontextprotocol.io/specification/2026-07-28) bei der Überprüfung eines neuen Servers.

Die URL der Spezifikation vom 2025-06-18 im folgenden Hintergrundabschnitt ist eine historische Version. Verwenden Sie die Spezifikation vom 2026-07-28 für neue Überprüfungen.

[MCP](https://modelcontextprotocol.io/specification/2025-06-18) standardisiert die Verbindungen zwischen einer LLM-Anwendung, einem Client-Connector und einem Server. Ein Server bietet Tools, Ressourcen oder Prompts an. Die Spezifikation legt außerdem fest, dass Hosts vor der Offenlegung von Daten oder dem Aufruf von Tools die Zustimmung des Benutzers einholen müssen.

**MCP selbst erteilt keine Berechtigungen.** Ein MCP-Tool wird weiterhin innerhalb der Berechtigungen seines Serverprozesses, des Betriebssystembenutzers, des Netzwerkpfads, des Cloud-Kontos und der konfigurierten Anmeldeinformationen ausgeführt. Eine Tool-Beschreibung ist keine Autorisierungsrichtlinie.

Die [1Password Security for AI Dokumentation](https://www.1password.dev/security-for-ai) beschreibt einen Environments MCP Server und sichere MCP-Konfigurationsmuster. Dieselbe Seite beschreibt das Laden von MCP-Konfigurationswerten zur Laufzeit aus 1Password. Diese Seiten definieren kein generisches 1Password SSH-Schlüssel-MCP-Produkt oder einen universellen SSH-Workflow für jeden Agent-Client.

Verwenden Sie MCP als eng begrenzten Kontrollbereich:

- **Read-Tools:** Inspektieren Sie den Dienstestatus, Repository-Metadaten oder genehmigte Protokolle.
- **Plan-Tools:** Bereiten Sie einen Befehl oder einen Änderungsbericht vor, ohne den Befehl auszuführen.
- **Approval-Tools:** Fordern Sie vor einem Remote-Write eine menschliche Entscheidung an.
- **Write-Tools:** Halten Sie diese deaktiviert, bis Ziel, Befehl, Umfang und Rollback-Plan explizit definiert sind.

Der Agent sollte Referenzen, Metadaten und Operationsergebnisse erhalten. **Der Agent sollte keinen Private-Key-Text, keinen Vault-weiten Item-Dump oder eine uneingeschränkte Shell erhalten.**

## Eine sichere Erst-Richtlinie

Beginnen Sie mit einer schriftlichen Richtlinie, bevor Sie einen Agent aktivieren. Halten Sie die Richtlinie in der Nähe der MCP-Konfiguration, aber legen Sie keine Anmeldeinformationen in die Datei.

```yaml
agent_policy:
  purpose: "Read-only repository and system inspection"
  identities:
    interactive_ssh: "1Password SSH Agent with per-terminal consent"
    unattended_jobs: "Dedicated service account with one narrow vault"
  allowed:
    - "Read repository metadata through Git"
    - "Read approved service status and logs"
    - "Run one synthetic SSH connectivity check"
  approval_required:
    - "Any remote write"
    - "Any package, firewall, clock, or service change"
    - "Any new host-key acceptance"
    - "Any private-key export"
  denied:
    - "Read or print private-key fields"
    - "List every vault or every item"
    - "Write tokens or secrets to shell profiles"
    - "Run arbitrary commands from tool output"
  rollback:
    - "Revoke the service account"
    - "Remove the public key from the target"
    - "Disable the MCP server entry"
    - "Lock 1Password and end the agent session"
```

Diese Richtlinie ist ein Beispiel und kein 1Password-Konfigurationsformat. Speichern Sie die tatsächliche Richtlinie in der Control Plane, die von Ihrem Agent-Client verwendet wird. Überprüfen Sie jedes Tool anhand der Richtlinie, bevor Sie jedes Tool aktivieren.

## Service Accounts und Secret-Referenzen

Ein **Service Account** verleiht einem automatisierten Prozess eine eigene Identität. Der [1Password CLI Skript-Guide](https://www.1password.dev/cli/secrets-scripts) empfiehlt Service Accounts für Least-Privilege-Zugriff auf ausgewählte Vaults. Dies trennt einen unbeaufsichtigten Job von der SSO, MFA, Vault-Inventarliste und dem täglichen Konto einer Person.

Eine **geheime Referenz** benennt einen Wert, ohne diesen Wert im Quellcode abzuspeichern. Die [1Password CLI Referenz](https://www.1password.dev/cli/reference) verwendet die Form `op://vault/item/field`. Die Referenz ist nur dann sicher abzuspeichern, wenn der umgebende Prozess weiterhin einen engen Zugriffsbereich besitzt. Eine Referenz umgeht keine Richtlinien.

Verwenden Sie `op read`, wenn ein Befehl einen einzelnen Wert benötigt. Verwenden Sie `op run`, wenn ein Kindprozess einen kontrollierten Satz von Laufzeitwerten benötigt. Verwenden Sie `op item create`, wenn ein neues SSH-Schlüssel-Element im genehmigten Tresor vorhanden sein muss.

Verwechseln Sie Laufzeitinjektion nicht mit dem Schutz von privaten Schlüsseln. Ein API-Token, der als Umgebungsvariable übergeben wird, ist für den Kindprozess weiterhin sichtbar. Ein privater Schlüssel, der über eine Umgebungsvariable übergeben wird, ist noch problematischer, da der Wert die Exposition gegenüber Prozessinspektion, Crash-Reports, Debug-Ausgaben, Shell-Tracing und versehentlichem Protokollieren vergrößert.

**Bevorzugen Sie eine Referenz im Quellcode und einen Laufzeitwert im kleinstmöglichen Prozess.** Halten Sie die Lebensdauer des Prozesses kurz. Deaktivieren Sie das Shell-Tracing. Geben Sie die Umgebungsvariablen nicht aus. Entfernen Sie temporäre Dateien nach einem fehlgeschlagenen Lauf.

## Sichere Erstworkflow

Die folgende Sequenz trennt die Registrierung des öffentlichen Schlüssels, interaktives SSH, MCP-Entdeckung und den unbeaufsichtigten Betrieb.

### 1. Ziel definieren

Notieren Sie die Zielklasse, das entfernte Konto, das beabsichtigte Repository oder den Befehl, die Quelle des Host-Schlüssels, den Genehmigungsverantwortlichen und die Rollback-Maßnahme. Verwenden Sie während der ersten Übung einen synthetischen Datensatz.

```text
target_class: test-repository
remote_account: git
operation: read-only connectivity check
host_key_source: approved administrator record
approval_owner: named operator
rollback: remove public key and revoke test identity
```

**Erwartetes Ergebnis, ungetestet:** Der Datensatz identifiziert ein Ziel und eine Operation. Der Datensatz enthält keine Hostname, IP-Adresse, Token, privaten Schlüssel oder personenbezogene Daten.

### 2. SSH-Schlüssel-Element erstellen oder auswählen

Der offizielle [1Password SSH-Schlüssel-Leitfaden](https://www.1password.dev/ssh/manage-keys) dokumentiert das CLI-Erstellungsmuster. Der folgende Befehl verwendet einen synthetischen Titel und einen benannten Testtresor.

```bash
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
```

**Erwartete Ausgabe, ungetestet:** 1Password erstellt ein SSH-Schlüssel-Element im benannten Testtresor und maskiert den privaten Schlüssel in der Terminalausgabe. Der Befehl ändert den Zustand von 1Password. Die genaue menschenlesbare Ausgabe hängt von der CLI-Version und dem Anmeldezustand ab.

Erfassen Sie die zurückgegebene Element-ID im Testdatensatz, ohne das Feld für den privaten Schlüssel zu kopieren. Verwenden Sie die ID oder den exakten Elementtitel für spätere feldspezifische Lesezugriffe erst nach Bestätigung des Element-Schemas.

Leiten Sie diese Ausgabe nicht in ein geteiltes Protokoll um. Erfassen Sie nur die Element-ID, den Fingerabdruck des öffentlichen Schlüssels und den Genehmigungsdatensatz, wenn das lokale Verfahren eine sichere strukturierte Ausgabe unterstützt.

### 3. Öffentlichen Schlüssel verarbeiten

Öffnen Sie den Eintrag „SSH Key“ in 1Password und verwenden Sie die Aktion „Copy Public Key“. Verwenden Sie eine feldspezifische Referenz erst dann, wenn Sie die Beschriftung des öffentlichen-Schlüssel-Felds in Ihrem eigenen Konto bestätigt haben. Geben Sie nicht den vollständigen Eintrag aus.

```bash
PUBLIC_KEY_REF="op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
op read "$PUBLIC_KEY_REF"
```

**Erwartete Ausgabe, nicht getestet:** Eine synthetische OpenSSH-öffentliche-Schlüssel-Zeile oder ein Wert des öffentlichen Schlüssels aus dem bestätigten Feld. Der oben genannte Platzhalter für den Feldnamen ist keine Zusicherung bezüglich der Feldbeschriftung Ihres Eintrags.

Registrieren Sie den öffentlichen Schlüssel im genehmigten Bitbucket-Konto, im Bitbucket-Repository oder im Remote-Konto. Fügen Sie niemals den zugehörigen privaten Schlüssel in Bitbucket ein. Der [Bitbucket-SSH-Leitfaden](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) empfiehlt ebenfalls, den Bitbucket-Host-Schlüssel vor der ersten Verbindung aufzuzeichnen.

Für Bitbucket: Rufen Sie den veröffentlichten Host-Schlüssel-Eintrag ab und vergleichen Sie den Eintrag mit einer unabhängigen, vertrauenswürdigen Kopie, bevor Sie eine Zeile zu `~/.ssh/known_hosts` hinzufügen. Verwenden Sie nach bestandener Prüfung die strenge Host-Prüfung. Akzeptieren Sie während eines Agentenlaufs keinen geänderten Host-Schlüssel.

### 4. Interaktives SSH aktivieren

Aktivieren Sie den 1Password SSH Agent in der Desktop-App. Konfigurieren Sie OpenSSH mit dem plattformspezifischen Wert `IdentityAgent` oder `SSH_AUTH_SOCK` aus dem [offiziellen Einrichtungshandbuch](https://www.1password.dev/ssh/get-started). Beschränken Sie den ersten Test auf ein Repository oder ein Nicht-Produktionskonto.

Unter macOS oder Linux: Setzen Sie den Socket gemäß dem plattformspezifischen Einrichtungshandbuch und führen Sie `ssh-add -l` aus. Unter Windows: Verwenden Sie die unterstützte Named-Pipe-Konfiguration und überprüfen Sie die verfügbaren Schlüssel über die 1Password SSH Agent-Oberfläche oder einen dokumentierten Windows-SSH-Test. Stellen Sie `ssh-add -l` nicht als plattformübergreifenden Verifikationsbefehl dar.

Nur unter macOS oder Linux:

```bash
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Erwartete Ausgabe, nicht getestet:** Unter macOS oder Linux listet `ssh-add -l` Fingerabdrücke vom aktiven Agenten. Unter Windows: Verwenden Sie den dokumentierten Named-Pipe-Test oder die 1Password SSH Agent-Oberfläche. Ein erfolgreicher Git-Lesevorgang gibt eine Commit-Referenz zurück. Der oben genannte Repository-Platzhalter muss in einem kontrollierten Test ersetzt werden.

Der Befehl verwendet einen Repository-Platzhalter. Ersetzen Sie den Platzhalter nur in einem kontrollierten Test. **Genehmigen Sie keine Abfrage für ein Ziel oder einen Prozess, den Sie nicht erwartet haben.**

### 5. MCP hinzufügen, nachdem der SSH-Pfad funktioniert

Prüfen Sie zunächst den SSH-Client und das Ziel ohne MCP. Fügen Sie dann einen schreibgeschützten MCP-Server oder lokalen Connector hinzu. Stellen Sie dem Agenten ein Tool wie `read_status` oder `prepare_command` zur Verfügung. Beginnen Sie nicht mit einem allgemeinen Shell-Tool.

Die MCP-Konfiguration sollte Laufzeitwerte über den vom Client unterstützten Umgebungsmechanismus referenzieren. Der [1Password AI security guide](https://www.1password.dev/security-for-ai) beschreibt den Ersatz von Klartext-MCP-Konfigurations-Token durch Umgebungsvariablen, die aus 1Password geladen werden. **Behalten Sie die Referenz oder den Variablennamen in der Konfiguration bei. Halten Sie den aufgelösten Wert aus dem Agenten-Transkript heraus.**

Dieser Abschnitt beschreibt ein Design, keine getestete MCP-Konfiguration. Hier ist kein Client, Server, Transport, keine Version oder kein Fixture festgelegt. Validieren Sie einen nur-lesenden Server in einem separaten Testprofil, bevor Sie einen Agenten mit einem Produktionssystem verbinden.

### 6. Das Ergebnis dokumentieren

Dokumentieren Sie die Zielklasse, den Tool-Namen, die Genehmigungsentscheidung, den Fingerabdruck des öffentlichen Schlüssels, das Ergebnis des Befehls und das Ergebnis der Bereinigung. Lassen Sie geheime Werte aus. Kennzeichnen Sie jede Ausgabe als beobachtet oder erwartet.

**Erwartetes Ergebnis, ungetestet:** Der Agent liest den Status, schlägt einen begrenzten Befehl vor, erhält eine explizite Genehmigung für die SSH-Anfrage, führt die nur-lesende Operation aus und erstellt einen Datensatz ohne Text des privaten Schlüssels.

## Synthetische Befehlssequenz

Die folgende Sequenz zeigt die Reihenfolge, ohne echte Infrastruktur zu verwenden. Diese Befehle sind nur Beispiele. Sie wurden während der Erstellung des Artikels nicht ausgeführt.

```bash
op --version
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
op read "op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
# macOS or Linux only
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Erwartete Ausgabe, ungetestet:**

```text
2.x.y
SSH Key item created. Private key: redacted
ssh-ed25519 AAAA<synthetic-public-key> synthetic-key-label
256 SHA256:<synthetic-fingerprint> synthetic-agent-admin-key (ED25519)
<synthetic-commit-id>        HEAD
```

Der Ausgabeblock ist illustrativ. Der Block stellt keinen Lauf gegen ein 1Password-Konto, Bitbucket, einen Git-Anbieter oder einen Remote-Host dar. Ein Produktionsdatensatz sollte nur genehmigte Metadaten und einen Erfolgs- oder Fehlerzustand speichern.

## Interaktiver versus unbeaufsichtigter Zugriff

| Zugriffsmodus | Identität | Pfad des privaten Schlüssels | Genehmigungsmodell |
|---|---|---|---|
| **Interaktives SSH** | Human Account über 1Password SSH Agent | Der private Schlüssel verbleibt in der 1Password-App | Ein Mensch genehmigt einen Prozess, eine Terminal-Sitzung oder eine Anfrage |
| **Geplante Lesezugriffe** | Dediziertes Service-Konto | `op run` liefert schmale Laufzeitwerte | Job-Richtlinie und Service-Konto-Scope |
| **Geplantes SSH** | Dedizierte Automatisierungsidentität | Der Schlüssel-Export bleibt ein Design der letzten Ausweg | Job-Isolation, kurze Lebensdauer, Host-Beschränkung und Rotation |
| **Agenten-Schreibzugriff** | Menschliche oder aufgabenbezogene Identität | Hängt von der genehmigten Integration ab | Menschliche Genehmigung vor jeder definierten Änderung |

*Planen Sie keinen Workflow um einen interaktiven SSH-Agent-Prompt herum. Verwenden Sie ein separates Automatisierungsdesign oder halten Sie den Schritt manuell betrieben.*

Für nicht überwachte Jobs erstellen Sie ein Dienstkonto mit Zugriff auf einen Vault oder eine kleine Menge an Elementen. Weisen Sie dem Job einen einzigen Zweck zu. Verwenden Sie ein dediziertes Repository oder ein Serverkonto. Fügen Sie die Host-Schlüssel-Verifizierung hinzu. Setzen Sie eine Ausführungszeitüberschreitung. Protokollieren Sie Metadaten der Aktionen ohne Geheimnisse. Rotieren oder widerrufen Sie die Identität nach dem Test.

Wenn ein nicht überwachter Job tatsächlich einen SSH-Privatschlüssel benötigt, verwenden Sie einen dedizierten Automatisierungsschlüssel mit einem engen Remote-Konto und einem dokumentierten Enddatum. Das Abrufen des Privatschlüssels mit `op read` exportiert weiterhin Schlüsselmaterial über eine Prozessgrenze hinweg. Dieses Design hat einen größeren Schadensradius als der 1Password SSH Agent. Bevorzugen Sie eine Plattformidentität, einen Deployment-Dienst oder eine andere Workload-Identität, wenn das Zielsystem dies unterstützt.

## Warum Klartext-Umgebungsvariablen das Risiko erhöhen

Umgebungsvariablen halten Geheimnisse aus Quelldateien heraus, machen sie aber nicht unsichtbar. Ein Kindprozess liest seine Umgebung. Prozessinspektion, Crash-Handler, Debug-Ausgaben, Shell-Tracing und kopierte Befehlsaufzeichnungen könnten Werte offenlegen.

1Password dokumentiert `op run` als Laufzeitmethode zum Laden von Referenzen in einen Unterprozess. Verwenden Sie `op run` für Werte, die ein Prozess tatsächlich benötigt. Halten Sie den Kindprozess kurzlebig und beschränken Sie seinen Befehl. Übergeben Sie keinen Privatschlüssel über `SSH_PRIVATE_KEY`, `KEY` oder eine ähnliche Variable, wenn der SSH Agent die Notwendigkeit für einen Export beseitigt.

Die sicherere Reihenfolge lautet:

1. **Verwenden Sie den SSH Agent** für interaktives SSH.
2. **Verwenden Sie die öffentliche Schlüsselregistrierung** für Bitbucket oder das Remote-Konto.
3. **Verwenden Sie `op run`** für einen engen, nicht überwachten Kindprozess.
4. **Verwenden Sie `op read`** für einen Wert, wenn ein Kindprozess keine vollständige Umgebung benötigt.
5. **Exportieren Sie einen Privatschlüssel** nur nach einer schriftlichen Ausnahme, einem engen Geltungsbereich, einem Aufräumplan und einem Rotationsplan.

## Entscheidungstabelle

| Bedarf | Bevorzugter Pfad | Grund zum Stoppen oder Neugestalten |
|---|---|---|
| Mensch führt Git über SSH aus | 1Password SSH Agent | Stoppen, wenn der Prompt einen unerwarteten Prozess oder Schlüssel benennt |
| Registrierung eines Repository-Schlüssels | Öffentlichen Schlüssel lesen oder automatisch ausfüllen | Den privaten Schlüssel niemals in den Repository-Dienst kopieren |
| Agent liest Dienststatus | Read-only-MCP-Tool mit OS-Ebene-Scope | Stoppen, wenn das Tool eine uneingeschränkte Shell offenlegt |
| Agent schlägt eine Remote-Änderung vor | Plan-Tool gefolgt von menschlicher Genehmigung | Stoppen, wenn Ziel, Befehl oder Rollback unklar sind |
| Job liest ein API-Token | Service-Konto plus `op read` oder `op run` | Stoppen, wenn das Token in Quellcode, Logs oder ein globales Profil gelangt |
| Job benötigt SSH-Zugriff | Workload-Identität oder dedizierter Automatisierungsschlüssel | Stoppen, wenn der Job einen persönlichen Schlüssel oder ein breites Konto erfordert |
| MCP-Konfiguration benötigt ein Token | Laufzeitreferenz, die vom unterstützten Client geladen wird | Stoppen, wenn ein Klartext-Token in die Konfiguration committet wird |

## Fehlerbehandlung

**Unerwarteter SSH-Zustimmungsaufforderung:** Die Aufforderung ablehnen. Den Prozessnamen, die Terminal-Sitzung, den Schlüssel-Fingerabdruck, das Repository-Ziel und den Host-Schlüssel überprüfen. Die SSH-Client-Konfiguration vor dem erneuten Versuch prüfen.

**Kein SSH-Agent-Socket:** Bestätigen, dass die 1Password-Desktop-App über eine unterstützte Methode installiert ist, der SSH-Agent aktiviert ist und der Client den plattformspezifischen Socket verwendet. Die [offizielle SSH-Agent-Seite](https://www.1password.dev/ssh/agent) listet die Betriebssystemanforderungen und Links zur Socket-Einrichtung auf.

**Public-Key-Authentifizierung schlägt fehl:** Den ausgewählten öffentlichen Schlüssel, das Remote-Konto, die Repository-Berechtigung, den Host-Schlüssel und die SSH-Konfiguration überprüfen. Einen öffentlichen Fingerabdruck-Vergleich verwenden. Das Problem nicht lösen, indem ein nicht zusammenhängender privater Schlüssel exportiert wird.

**`op read` verweigert den Zugriff:** Den Vault-Scope des Service-Kontos, die Item-Identifikator, die Feldreferenz, den Anmeldezustand und den Item-Status überprüfen. Die Referenz auf ein einziges genehmigtes Item reduzieren. Die Vault-Berechtigung nicht als erste Reaktion erweitern.

**`op run` legt einen Wert offen:** Den Job stoppen. Nur das minimale Vorfallprotokoll beibehalten. Kopierte Logs und temporäre Dateien gemäß dem Aufbewahrungsverfahren entfernen. Den betroffenen Secret oder Schlüssel rotieren. Shell-Tracing, Prozessinspektion, Crash-Reports und die Aufbewahrung von MCP-Transkripten überprüfen.

**Unerwartetes Verhalten des MCP-Tools:** Behandeln Sie die Tool-Ausgabe als unzuverlässige Daten. Halten Sie an, bevor Sie Befehle ausführen, die von der Ausgabe vorgeschlagen werden. Untersuchen Sie den Server-Quellcode, die Konfiguration, die Berechtigungen und den Transport. Der MCP-Host muss die Zustimmung des Benutzers einholen. Die Spezifikation bietet auch Implementierungsleitlinien für Zustimmung und Zugriffskontrollen, aber das Protokoll ersetzt Ihre Überprüfung nicht.

## Rollback und Entfernung

Der Rollback beginnt mit der Entfernung des Zugriffs, nicht mit der Löschung von Dateien.

1. **Agenten oder geplante Jobs stoppen.** Deaktivieren Sie den MCP-Server-Eintrag oder trennen Sie den Client.
2. **1Password sperren.** Beenden Sie die interaktive SSH-Autorisierungssitzung.
3. **Öffentlichen Schlüssel entfernen.** Löschen Sie den Test-Schlüssel aus Bitbucket, dem Repository oder dem Remote-Konto.
4. **Service-Konto widerrufen.** Entfernen Sie dessen Vault-Zugriff und invalidieren Sie dessen Token.
5. **Das Test-SSH-Key-Element löschen**, nachdem bestätigt wurde, dass kein genehmigter Workflow das Element verwendet.
6. **Vorübergehende Konfiguration entfernen.** Löschen Sie Test-Referenzen, lokale Socket-Overrides und generierte Protokolle.
7. **Beweise überprüfen.** Stellen Sie sicher, dass das Rollback-Protokoll keinen privaten Schlüssel, Token oder Umgebungs-Dump enthält.

*Ein gelöschte lokale Datei widerruft keinen öffentlichen Schlüssel, Service-Konto, zwischengespeicherten Token oder Remote-Autorisierung. Entfernen Sie jede Berechtigung an ihrer Quelle.*

## Fehlerbehebung

### Der Agent fordert bei jedem Befehl einen Schlüssel an

Prüfen Sie den gewählten Autorisierungsbereich. Genehmigung pro Anfrage ist restriktiver. Eine Terminal- oder Anwendungssitzung könnte beendet worden sein. 1Password fragt auch nach einer Sperr- oder Beendigungsereignis erneut ab.

### Der Agent sieht einen privaten Schlüssel in seinem Transkript

Stoppen Sie den Workflow und rotieren Sie den Schlüssel. Untersuchen Sie die MCP-Server-Antwort, den Shell-Befehl, das Debug-Protokoll und den Tool-Wrapper. Ersetzen Sie das Lesen von privaten Schlüsseln durch die Nutzung des SSH-Agenten für interaktive Aufgaben. Für Jobs ersetzen Sie einen persönlichen Schlüssel durch eine dedizierte Identität und eine dokumentierte Ausnahme.

### Eine Schlüssel-Liste enthält zu viele Identitäten

Der 1Password SSH-Agent zeigt berechtigte Schlüssel aus seinen konfigurierten Vaults an. Verwenden Sie eine bereichsbezogene Agenten-Konfiguration oder eine host-spezifische SSH-Konfiguration. Die [Agenten-Dokumentation](https://www.1password.dev/ssh/agent)] erwähnt auch die Sechs-Schlüssel-Grenze des OpenSSH-Servers.

### Ein Befehl funktioniert manuell, schlägt aber in einem Job fehl

Vergleichen Sie Identität, Vault-Bereich, Umgebung, Host-Key-Daten, Arbeitsverzeichnis und Annahmen zur Genehmigung. Eine interaktive 1Password-Sitzung umfasst die menschliche Zustimmung. Ein geplanter Job nicht. Gestalten Sie den Job als separaten Zugriffsmodus.

### Der MCP-Server ist verbunden, aber die Aufgabe schlägt fehl

Eine Verbindung beweist keine Autorisierung. Prüfen Sie Werkzeugentdeckung, Serveranmeldedaten, Client-Zustimmung, Betriebssystemberechtigungen, Netzwerkzugriff und Zielberechtigungen in getrennten Schritten. Halten Sie den ersten Test nur-lesend.

## Nächste Schritte

Verwenden Sie die aktuelle MCP-Spezifikation vom 2026-07-28 für neue Genehmigungen. Jeder Link zur Spezifikation vom 2025-06-18 in diesem Artikel ist historischer Hintergrund.

Beginnen Sie mit einem synthetischen Repository und einem nur-lesenden MCP-Werkzeug. Dokumentieren Sie jedes erwartete Ergebnis als ungetestet, bis eine kontrollierte Umgebung Beweise liefert. Wiederholen Sie dann den Workflow mit einem Nicht-Produktionsziel, einem benannten Operator, einem verifizierten Host-Schlüssel und einem schriftlichen Rollback-Protokoll.

Lesen Sie die [1Password CLI-Referenz](https://www.1password.dev/cli/reference) für aktuelle Befehlsschalter. Lesen Sie [Geheimnisse in Skripte laden](https://www.1password.dev/cli/secrets-scripts), bevor Sie Service-Account-Automatisierung erstellen. Lesen Sie die [MCP-Spezifikation](https://modelcontextprotocol.io/specification/2026-07-28), bevor Sie Werkzeuge von einem neuen Server genehmigen.

**Halten Sie interaktive SSH-Zugriffe menschlich genehmigt. Halten Sie unbeaufsichtigten Zugriff getrennt. Halten Sie private Schlüssel ungelesen, wenn das Ziel agentenbasierte Authentifizierung unterstützt.**

---
title: "Bitbucket Cloud SSH-Schlüssel: schreibgeschützter Git-Zugriff für KI-Agenten"
date: 2026-10-11
lastmod: 2026-11-09
toc: true
draft: false
description: "Richte Bitbucket Cloud SSH-Schlüssel, Git-CLI-Zugriff, REST-API-Tokens, 1Password und MCP-Tools für schreibgeschützte KI-Agenten-Workflows ein."
genre: ["Cloud-Sicherheit", "Entwicklertools", "Systemverwaltung"]
tags: ["Bitbucket Cloud", "Bitbucket-SSH-Schlüssel", "Repository-Zugriffsschlüssel", "Projektzugriffsschlüssel", "Workspace-Zugriffsschlüssel", "Git CLI", "Bitbucket CLI", "1Password CLI", "1Password SSH Agent", "MCP", "Model Context Protocol", "REST API", "API-Token-Bereiche", "Agentenberechtigungen", "schreibgeschützte Automatisierung", "SSH-Hostschlüssel"]
cover: "/img/cover/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation.webp"
coverAlt: "Ein Terminalworkflow verbindet Bitbucket-Cloud-Git-Zugriff, eingeschränkte SSH-Schlüssel, 1Password, REST-API-Lesezugriffe und MCP-Tools"
coverCaption: ""
---

**Ein begrenzter Agentenworkflow trennt Repository-Lesezugriffe, API-Lesezugriffe, Geheimnisverwaltung und Remote-Schreibvorgänge.** Verwende Git über Secure Shell (SSH) für den Quellzugriff, einen schreibgeschützten Bitbucket-Zugriffsschlüssel für automatisierte Checkouts, die REST API für Metadaten und einen Model Context Protocol (MCP)-Server für genehmigte Tools. Bewahre private Schlüssel und API-Tokens in 1Password auf. Schütze Schreibvorgänge durch eine menschliche Genehmigung.

<!--more-->

## Die wichtigsten Punkte

- **Schreibgeschützt als Standard:** Verwende einen Repository- oder Projektzugriffsschlüssel für den Checkout durch Agenten. Keiner davon gewährt Push-Zugriff.
- **Persönliche Identität:** Verwende einen persönlichen SSH-Schlüssel für interaktive Arbeit, die an ein Benutzerkonto gebunden ist.
- **Geheimnisverwaltung:** Verwende den 1Password SSH Agent, damit Git einen Signiervorgang erhält, ohne den privaten Schlüssel zu lesen.
- **Bedeutung von CLI:** Betrachte `git`, `curl` und einen kleinen geprüften API-Wrapper als die praktischen Bitbucket-Kommandozeilentools.
- **MCP-Grenze:** Stelle eng begrenzte Lesetools bereit. Deaktiviere Schreibtools oder setze sie hinter einen separaten Genehmigungsprozess.
- **Schreibfreigabe:** Lass einen Agenten eine Änderung prüfen, vergleichen und vorbereiten. Verlange eine menschliche Genehmigung vor Push, Pull Request, Merge oder Einstellungsänderung.

## Bevor du beginnst

**Voraussetzungen:** Zugriff auf Bitbucket Cloud, Git, ein OpenSSH-Client, 1Password 8, 1Password CLI, eine angemeldete CLI oder ein genehmigtes Dienstkonto sowie ein MCP-Host mit Genehmigungssteuerung für Server. Plane 45 Minuten ein. Schwierigkeitsgrad: mittel.

Verwende für den ersten Durchlauf ein Test-Repository. Ersetze alle Platzhalter in den Beispielen. Die folgenden Befehle sind ungetestete Beispiele. Sie beziehen sich nicht auf ein aktives Bitbucket-Konto oder Repository.

**Versionsstatus:** Dieser Artikel enthält Designhinweise und ist kein an bestimmte Versionen gebundenes Runbook. Prüfe vor dem Test die installierten Versionen von Git, OpenSSH, 1Password CLI, Teamwork Graph CLI, MCP-Host und MCP-Server. Konfiguriere den 1Password SSH Agent für das aktuelle Betriebssystem, bevor du `ssh-add -l` verwendest.

**Halte Zugangsdaten aus Shells, Logs, URLs, Git-Remotes und Quelldateien heraus.** Verwende Platzhalter wie `<workspace>`, `<repository>`, `<api-token>` und `<socket-path>`. Füge keinen echten privaten Schlüssel in ein Terminaltranskript ein.

## Lege die Zugriffsgrenze fest

Bitbucket Cloud unterstützt Zugriffsschlüssel auf Repository-, Projekt- und Workspace-Ebene. Der Geltungsbereich bestimmt die Auswirkung eines kopierten Schlüssels. Der [offizielle Vergleich der Zugriffsschlüssel](https://support.atlassian.com/bitbucket-cloud/kb/difference-between-repository-project-and-workspace-access-keys/) beschreibt die Berechtigungsunterschiede direkt.

| Zugriffsweg | Geltungsbereich | Schreibzugriff | Geeignet für |
|---|---|---:|---|
| **Repository-Zugriffsschlüssel** | Ein Repository | Nein | Standard-Checkout durch einen Agenten |
| **Projektzugriffsschlüssel** | Repositories in einem Projekt | Nein | Schreibgeschützte Aufträge für eine kleine Repository-Gruppe |
| **Workspace-Zugriffsschlüssel** | Repositories in einem Workspace | Ja | Kontrollierte Dienstautomatisierung mit separatem Schreibplan |
| **Persönlicher SSH-Schlüssel** | Für einen Benutzer freigegebene Repositories | Folgt dem Benutzerkonto | Interaktive Verwaltung |
| **API-Token** | Benutzerbezogene API-Bereiche und Kontozugriff | Abhängig von den Bereichen | REST-API-Lesezugriffe oder eine vorübergehende Schreibaufgabe |

**Beginne mit der kleinsten sinnvollen Grenze.** Wähle einen Repository-Zugriffsschlüssel, wenn ein Repository genügt. Wähle einen Projektschlüssel, wenn mehrere Repositories zu einem Projekt gehören und schreibgeschützter Zugriff ausreicht. Behandle einen Workspace-Zugriffsschlüssel als Schreibidentität, nicht als bequeme Standardeinstellung.

Erstelle und registriere den kleinsten Schlüssel über den passenden Bitbucket-Einstellungspfad:

1. Öffne Repository settings, Access keys und Add key für ein Repository. Füge den öffentlichen Schlüssel ein und belasse ihn bei Nur-Lesen-Zugriff.
2. Öffne Project settings, Access keys und Add key, wenn mehrere Repositories eine gemeinsame schreibgeschützte Identität auf Projektebene benötigen.
3. Verwende einen Workspace-Zugriffsschlüssel nur in einem gemeinsam genutzten Workspace mit einem genehmigten Schreibkonzept. Persönliche Workspaces bieten nicht denselben Pfad auf Workspace-Ebene.
4. Halte Schlüsselbezeichnung, Geltungsbereich, Fingerabdruck des öffentlichen Schlüssels, Besitzer und Rotationsdatum fest. Bewahre den privaten Schlüssel in 1Password auf.

Führe nach der Registrierung einen exakten schreibgeschützten Verbindungstest aus:

```bash
git ls-remote git@bitbucket.org:<workspace>/<repository>.git HEAD
```

**Erwartete Ausgabe:** eine Commit-Referenz für `HEAD`. Ungetestetes Beispiel. Ein erfolgreiches Ergebnis belegt, dass eine zulässige SSH-Identität das genannte Repository erreicht hat. Es belegt weder, dass der registrierte Schlüssel ausgewählt wurde, noch dass Schreibzugriff besteht. Wiederhole den Test nach der Konfiguration eines Schlüssels pro Repository.

Hinweise zur Verwahrung privater Schlüssel und zur Zustimmung des 1Password SSH Agent findest du unter [1Password CLI und SSH Agent: Sichere SSH-Schlüssel für KI-Agenten](/articles/1password-cli-ssh-keys-mcp-agent-administration/).

## „Bitbucket CLI“ richtig einordnen

Der Begriff **Bitbucket CLI** vermischt oft drei verschiedene Schnittstellen. Halte sie getrennt.

- **Git CLI:** `git clone` und `git fetch` übertragen Repository-Daten über SSH oder HTTPS. `git diff` vergleicht lokale Dateien oder Revisionen.
- **REST-Client:** `curl` oder ein geprüfter Wrapper ruft die Bitbucket Cloud Representational State Transfer (REST) API auf. Eine API ist eine Programmierschnittstelle für Datenanfragen und Aktionen. Die [Bitbucket Cloud REST API-Referenz](https://developer.atlassian.com/cloud/bitbucket/rest/) führt Ressourcen für Repositorys, Quellcode, Branches, Pull Requests, Pipelines und Status auf.
- **Atlassian CLI:** `acli` ist die offizielle Befehlszeile von Atlassian. Die [Einführung](https://developer.atlassian.com/cloud/acli/guides/introduction/) beschreibt das Produkt, die [Befehlsreferenz](https://developer.atlassian.com/cloud/acli/reference/commands/) listet die Bereiche `admin`, `jira`, `feedback` und `rovodev`. Die Referenz dokumentiert keine Bitbucket-Cloud-Befehle.

**Die offizielle Atlassian-Befehlsreferenz für `acli` dokumentiert keine Bitbucket-Cloud-Befehle.** Erfinde keinen Befehl wie `acli bitbucket clone`. Verwende Git für Git-Operationen und die REST API für Bitbucket-Cloud-Daten.

### Optionale Teamwork Graph CLI

**Atlassian veröffentlicht außerdem die Teamwork Graph CLI, kurz `twg`.** Die [Übersicht](https://developer.atlassian.com/cloud/twg-cli/) und der [Befehlskatalog](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/commands/commands-catalog/) dokumentieren Bitbucket-Befehlsfamilien. Der Einrichtungsbefehl lautet:

```bash
twg setup
```

Der Einrichtungsbefehl ändert den lokalen Authentifizierungsstatus. Folge den Eingabeaufforderungen der installierten Version für die optionale Bitbucket-Tokenkonfiguration. Der Bitbucket-Tokenpfad der CLI ist von Atlassian OAuth getrennt. Richte die genaue Befehlssyntax nach der installierten Version und dem aktuellen Befehlskatalog aus. Verwende ein separates Profil, ein eingeschränktes Token, geprüfte installierte Skills und menschliche Genehmigung für Änderungsbefehle.

**Erwartetes Ergebnis, nicht getestet:** Das isolierte Profil erhält Bitbucket-Authentifizierungseinstellungen. Notiere den vorherigen Profilstatus vor der Einrichtung. Entferne die gespeicherten Zugangsdaten beim Rollback über das dokumentierte Abmelde- oder Konfigurationsentfernungsverfahren der installierten Version.

Wenn sich ein Drittanbieterprojekt als Bitbucket CLI bezeichnet, prüfe Quellcode, Release-Prozess, Prüfsummen, Aktualisierungspfad, Authentifizierungsfluss, angeforderte Bereiche, Netzwerkziele, Protokollierung und Schreibbefehle. Ein vertrauter Binärname belegt weder Herstellerunterstützung noch sichere Berechtigungen.

## SSH-Schlüssel mit 1Password verwalten

Der [1Password SSH Agent](https://www.1password.dev/ssh/agent) stellt Git- und SSH-Clients SSH-Schlüssel aus 1Password bereit. Der Client führt eine autorisierte Signaturanfrage aus. Der private Schlüssel bleibt in der 1Password-App, die um Zustimmung bittet, bevor ein genehmigter Client einen Schlüssel verwendet.

Die [1Password CLI-Referenz](https://www.1password.dev/cli/reference) hat eine andere Aufgabe. Verwende `op` für kontrollierten Zugriff auf Elemente, API-Tokens, Dienstkonten und Automatisierungseinrichtung. Verwende den SSH Agent für SSH-Signaturen. Exportiere keinen privaten Schlüssel in eine temporäre Datei, nur um einen Agentenworkflow zu vereinfachen.

Prüfe den lokalen CLI- und Agentenstatus mit schreibgeschützten Befehlen:

```bash
op --version
ssh-add -l
```

**Erwartete Ausgabe:** eine 1Password-CLI-Version und ein oder mehrere Fingerabdrücke öffentlicher Schlüssel vom aktiven Agenten. Ungetestetes Beispiel. Eine leere Ausgabe von `ssh-add -l` bedeutet, dass über den ausgewählten Agenten-Socket kein Schlüssel verfügbar ist.

Erstelle für einen neuen Schlüssel ein Ed25519-SSH-Key-Element in 1Password oder importiere einen Schlüssel, der mit einem vertrauenswürdigen lokalen Prozess generiert wurde. Vergib eine Bezeichnung anhand von Zweck, Geltungsbereich und Rotationsdatum. Füge Bitbucket Cloud nur den öffentlichen Schlüssel hinzu. Die [Linux-Anleitung für Repository-Zugriffsschlüssel](https://support.atlassian.com/bitbucket-cloud/docs/set-up-repository-access-keys-on-linux/) beschreibt den Repository-Einstellungspfad und die Nur-Lesen-Beschränkung.

## Prüfe zuerst den Bitbucket-Hostschlüssel

SSH-Benutzerauthentifizierung beweist nicht die Identität des Servers. Der Client muss den Bitbucket-Cloud-Hostschlüssel prüfen, bevor er eine Authentifizierungsanfrage sendet. Die [Atlassian-Anleitung zu SSH und Zwei-Schritt-Verifizierung](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/) listet öffentliche Hostschlüssel und zeigt den offiziellen Endpunkt zum Abrufen von known-hosts-Einträgen.

Rufe die öffentlichen Hostschlüsseldaten zum Vergleich ab:

```bash
curl --fail --silent --show-error https://bitbucket.org/site/ssh
```

**Erwartete Ausgabe:** OpenSSH-`known_hosts`-Zeilen für `bitbucket.org`. Ungetestetes Beispiel. Vergleiche den zurückgegebenen Schlüssel oder Fingerabdruck mit einer unabhängigen, vertrauenswürdigen Kopie, bevor du die Zeile in `~/.ssh/known_hosts` einfügst.

Aktiviere die strikte Hostprüfung, nachdem der genehmigte Eintrag vorhanden ist:

```sshconfig
Host bitbucket.org
    StrictHostKeyChecking yes
    UserKnownHostsFile ~/.ssh/known_hosts
```

**Akzeptiere während eines Agentenlaufs keinen geänderten Hostschlüssel.** Stoppe den Lauf, prüfe die aktuelle Bitbucket-Cloud-Hostschlüsselregistrierung und kontrolliere den lokalen `known_hosts`-Eintrag. Eine automatische Annahme entfernt eine Sicherheitsgrenze des Schlüssels.

## Wähle einen Schlüssel pro Repository

Auf einem Gerät befinden sich oft mehrere Bitbucket-Schlüssel. Ein weit gefasster SSH-Agent bietet bei einer Verbindung mehrere Identitäten an. Ein Server oder eine Richtlinie mit niedrigem Limit für Authentifizierungsversuche kann den richtigen Schlüssel ablehnen, nachdem frühere Schlüssel scheiterten.

Die [Atlassian-Anleitung zu mehreren Repository-Zugriffsschlüsseln](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) verwendet `core.sshCommand` in einer Git-Konfigurationsdatei des Repositorys und `includeIf` in der globalen Git-Konfiguration. Verwende dasselbe Muster mit einem Schlüssel pro Repository.

Portables dateibasiertes Beispiel:

```ini
# .gitconfig inside one local repository
[core]
    sshCommand = ssh -o IdentitiesOnly=yes -i ~/.ssh/<repository-automation-key>
```

```ini
# ~/.gitconfig
[includeIf "gitdir:~/src/<repository>/"]
    path = ~/src/<repository>/.gitconfig
```

Der obige Block ist eine dateibasierte Ausnahme für einen privaten Schlüssel einer dedizierten Automatisierungsidentität. Er konfiguriert nicht den 1Password SSH Agent. Richte für den 1Password SSH Agent den plattformspezifischen Wert `IdentityAgent` oder `SSH_AUTH_SOCK` aus der [1Password-Einrichtungsanleitung](https://www.1password.dev/ssh/get-started) ein. Einige OpenSSH-Konfigurationen verwenden eine `.pub`-Datei als Identitätsauswahl für einen Agenten. Prüfe die Plattformunterstützung, bevor du sie einsetzt. Eine dateibasierte Einrichtung benötigt den zugehörigen privaten Schlüsselpfad. Übergib niemals eine `.pub`-Datei an einen Befehl, der privates Schlüsselmaterial erwartet, und exportiere keinen persönlichen privaten Schlüssel.

Verwende eine explizite Repository-Konfiguration, wenn ein lokaler Klon einen Schlüssel benötigt. Verwende `includeIf`, wenn ein Verzeichnis mehrere Klone mit derselben Zugriffsgrenze enthält. Die [Anleitung zu mehreren Schlüsseln](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) zeigt beide Einstellungen im Bitbucket-Workflow.

Klone über Git und SSH:

```bash
git clone git@bitbucket.org:<workspace>/<repository>.git <local-directory>
```

**Erwartete Ausgabe:** Git erstellt `<local-directory>` und ruft das Repository über `bitbucket.org` ab. Ungetestetes Beispiel. Ein Repository-Zugriffsschlüssel erlaubt nur Klonen und Abrufen.

## API-Tokens für begrenzte REST-Lesezugriffe nutzen

Verwende SSH für den Git-Transport. Nutze die REST API für Metadaten oder Vorgänge außerhalb des Git-Transports. Die [Anleitung zu API-Tokenberechtigungen](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/) listet Repository-Bereiche wie Read, Write, Admin und Delete. Repository Read entspricht `read:repository:bitbucket` und umfasst keinen Zugriff auf Pull Requests.

Bevorzuge für Leseautomatisierung ein Bitbucket-Repository- oder Projektzugriffstoken, wenn das Ziel den erforderlichen Endpunkt unterstützt. Ein benutzerbasiertes API-Token behält den größeren Zugriff des Benutzerkontos. Verwende ein Workspace-Token nur, wenn die Aufgabenbeschreibung den größeren Bereich vorsieht. Prüfe vor der Auswahl des Tokentyps die [Bitbucket-Anleitung zu Zugriffstokens](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/).

Beginne für Agenten-Lesezugriffe mit `read:repository:bitbucket`. Ergänze `read:pullrequest:bitbucket` nur, wenn der Agent Pull-Request-Daten benötigt. Füge Workspace- oder Pipeline-Bereiche erst hinzu, wenn die Aufgabe Endpunkt und Ergebnis nennt. Schreib- und Adminbereiche benötigen einen separaten Genehmigungsprozess.

Erstelle jedes API-Token für einen Zweck, lege ein Ablaufdatum fest, notiere es im Rotationsregister und ersetze das Token vor dem Ablauf. Atlassians [Anleitung zum Erstellen eines API-Tokens](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/) verlangt Name, Ablaufdatum, App-Auswahl und Bereiche. Nach dem Erstellen wird das Token nur einmal angezeigt.

Bewahre den Wert in 1Password oder einem verwalteten Laufzeitgeheimnis auf. Setze ihn nicht in eine Remote-URL. Übergib ein Bearer-Token nur über eine Umgebungsvariable an den Prozess, der einen Lesezugriff ausführt:

```bash
op run --env-file=/path/to/agent.env -- \
sh -c 'curl --fail --silent --show-error \
  --request GET \
  --url "https://api.bitbucket.org/2.0/repositories/<workspace>/<repository>" \
  --header "Authorization: Bearer ${BITBUCKET_API_TOKEN}" \
  --header "Accept: application/json"'
```

Halte `/path/to/agent.env` außerhalb des Repositorys. Speichere darin eine Referenz wie `BITBUCKET_API_TOKEN=op://synthetic-vault/synthetic-api-token/credential`. `op run` löst die Referenz auf und stellt dem curl-Kindprozess den Wert für die Laufzeit des Unterprozesses bereit. Es verhindert nicht, dass der Kindprozess den Umgebungswert liest oder protokolliert. Ersetze den Platzhalter nicht durch ein tatsächliches Token.

**Erwartete Ausgabe:** JSON-Metadaten für das ausgewählte Repository. Ungetestetes Beispiel. Der Platzhalter darf nie in einer committeten Datei oder einem Log zu einem echten Token werden.

Lass 1Password bei längerer Automatisierung ein Geheimnis über die unterstützte CLI oder den Dienstkonto-Workflow in die Prozessumgebung injizieren. Halte die Tokenlaufzeit passend zur Aufgabe. Widerrufe ein Token, wenn die Aufgabe vorzeitig endet oder der Host den Besitzer wechselt.

## MCP-Leseoberfläche klein halten

Nutze beim Prüfen eines neuen Servers die aktuelle [MCP-Spezifikation](https://modelcontextprotocol.io/specification/2026-07-28) und ihre [Autorisierungsregeln](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization). HTTP-Server müssen Token-Audience-Prüfungen durchführen und 401- sowie 403-Antworten klar behandeln.

Der MCP-Host holt die Zustimmung des Benutzers ein. Der Client hält eine Verbindung zu einem Server aufrecht. Der Server stellt Tools, Ressourcen oder Prompts bereit. Behandle jeden Server als nicht vertrauenswürdigen Code, bis Quelle, Transport, Konto und Berechtigungen geprüft sind.

Die Spezifikations-URL 2025-06-18 im nächsten Absatz bezeichnet eine historische Version. Verwende für neue Prüfungen die aktuelle Version 2026-07-28.

Die [MCP-Spezifikation](https://modelcontextprotocol.io/specification/2025-06-18) definiert die Kommunikation zwischen MCP-Host, Client und Server. Ein Server stellt Tools, Ressourcen oder Prompts über das Protokoll bereit. MCP standardisiert das Verbindungsformat. Host, Serverimplementierung, Konto, Tokenbereich und Genehmigungsrichtlinie bestimmen weiterhin, worauf ein Aufruf zugreift.

Verwende einen MCP-Server als schmalen Adapter für Git und die Bitbucket Cloud REST API.

Schütze diesen Adapter vor Token-Weitergabe, Server-Side Request Forgery (SSRF) und dem Confused-Deputy-Problem. SSRF erlaubt einem Server, Anfragen an unbeabsichtigte Ziele zu senden. Das Confused-Deputy-Problem tritt auf, wenn ein Server im Auftrag eines Aufrufers umfassendere Berechtigungen nutzt. Schütze außerdem vor bösartigen lokalen Servern, unsicheren OAuth-Weiterleitungen und übergroßen Quelltextantworten. Lege zulässige Bitbucket-Ursprünge und Repository-IDs fest. Führe lokale Server in einer Sandbox mit einem eigenen Betriebssystembenutzer aus. Schwärze Geheimnisse in Toolergebnissen und Logs.

Dieser Abschnitt beschreibt ein Design, keine getestete MCP-Konfiguration. Client, Server, Transport, Version und Fixture sind nicht festgelegt. Validiere einen schreibgeschützten Server in einem separaten Testprofil, bevor du einen Agenten mit einem Produktionsrepository verbindest.

Beispiele für Lesetools:

| Tool | Begrenztes Ergebnis |
|---|---|
| **`get_repository_metadata`** | Gibt Metadaten eines Repositorys zurück |
| **`read_source_file`** | Liest einen Pfad in einer Revision |
| **`list_branches`** | Listet Branches eines Repositorys auf |
| **`get_pull_request`** | Gibt einen Pull Request zurück, wenn das Token den Pull-Request-Lesebereich hat |
| **`get_build_status`** | Gibt Statusdaten für einen Commit zurück |

Diese Namen beschreiben ein Design. Sie sind keine Atlassian-Befehle. Verhindere, dass der Server beliebige URLs, beliebige Shell-Befehle, rohe Tokens, Anfragen zum Export privater Schlüssel oder uneingeschränkte Repository-IDs akzeptiert.

Lege Berechtigungen auf vier Ebenen fest:

1. **Bitbucket Cloud:** Repository- oder Projektleseschlüssel für Git sowie die kleinsten API-Tokenbereiche für REST-Lesezugriffe.
2. **1Password:** ein Tresor oder Dienstkonto für die Aufgabe, ohne Exportpfad für private Schlüssel.
3. **MCP-Server:** Allowlist der Lesetools, feste Bitbucket-Cloud-Endpunkte, Eingabevalidierung, Zeitlimits und geschwärzte Logs.
4. **MCP-Host:** Benutzerfreigabe für den Server und jede schreibfähige Aktion; Schreibtools sind im Standardprofil deaktiviert.

*Eine MCP-Toolliste belegt die Erkennung. Sie belegt weder Autorisierung noch den richtigen Bereich, sichere Eingabeverarbeitung oder ein korrektes Ergebnis.*

## Agentenworkflow strukturieren

Halte den Workflow ausdrücklich fest. Jede Phase liefert Belege für die nächste.

| Phase | Aktion des Agenten | Berechtigung | Menschliche Freigabe |
|---|---|---|---|
| **Vorbereiten** | Konfiguration, Hostschlüsselprotokoll, Schlüsselbezeichnung, Tokenbereich und Ablaufdatum lesen | Lokal lesen | Einrichtungsprotokoll freigeben |
| **Prüfen** | Über Git und SSH klonen oder abrufen und REST-Metadaten abfragen | Repository- und API-Lesezugriff | Keine nach der Einrichtung |
| **Analysieren** | Dateien, Branches, Pull Requests und Buildstatus über genehmigte Tools lesen | MCP-Tools nur zum Lesen | Keine für begrenzte Lesezugriffe |
| **Änderung vorbereiten** | Patch, Branchplan oder Pull-Request-Entwurf im lokalen Arbeitsbereich erstellen | Nur lokal schreiben | Diff und Ziel prüfen |
| **Schreiben freigeben** | Exakte Remote-Aktion, Bereich und Rollback-Pfad vorlegen | Noch kein Remote-Schreibzugriff | Menschliche Freigabe |
| **Schreibvorgang ausführen** | Branch pushen, Pull Request erstellen oder Schreibendpunkt aufrufen | Kurzlebige Schreibidentität | Jede Aktion bestätigen |
| **Verifizieren** | Resultierenden Commit, Pull Request oder Status lesen | Wieder nur lesen | Erwartetes Ergebnis bestätigen |

Das Standardprofil des Agenten sollte nach **Analysieren** oder **Änderung vorbereiten** stoppen. Ein separates Schreibprofil sollte ein anderes Token oder einen anderen Schlüssel, ein kurzes Ablaufdatum, ein festes Ziel und eine Genehmigungsabfrage verwenden. Ein Repository-Zugriffsschlüssel kann den Schreibschritt nicht ausführen und schafft dadurch eine nützliche technische Grenze.

## Rollback und Entfernung

Beginne das Rollback mit dem Entzug des Zugriffs und bereinige danach die lokale Konfiguration:

1. Entferne den Repository-, Projekt- oder Workspace-Zugriffsschlüssel in den passenden Bitbucket-Einstellungen.
2. Widerrufe das Repository-, Projekt-, Workspace- oder Benutzer-API-Token auf der entsprechenden Bitbucket-Sicherheitsseite.
3. Entferne die gespeicherten Teamwork-Graph-Zugangsdaten über das dokumentierte [Authentifizierungsverfahren](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/getting-started/how-authentication-works/) der installierten CLI-Version. Bewahre vorherige Zugangsdaten nur im genehmigten Geheimnismanager auf. Prüfe, dass das isolierte Profil die Testzugangsdaten nicht mehr aufführt.
4. Entferne nach dem Test die Repository-`.gitconfig` und den zugehörigen `includeIf`-Eintrag. Unverwandte Git-Konfiguration bleibt unverändert.
5. Entferne nur den verifizierten Bitbucket-Hostschlüsseleintrag, der für den Test hinzugefügt wurde. Bewahre andere genehmigte Hostschlüssel auf.
6. Entferne die externe `agent.env`-Datei und temporäre Ausgaben. Entferne den MCP-Servereintrag aus der Hostkonfiguration und starte den Host neu.

Protokolliere jede Entfernung, den Ausführenden und den Zeitpunkt. Rotiere einen Schlüssel oder ein Token, wenn ein Wert in einem unerwarteten Log, Prozessdatensatz oder Transkript auftaucht.

## Remote-Lesezyklus mit lokalen Referenzaktualisierungen

Verwende für wiederkehrende Repository-Prüfungen einen kurzen Zyklus:

```bash
LOCAL_REPO="<local-directory>"
git -C "$LOCAL_REPO" fetch --no-tags
git -C "$LOCAL_REPO" status --short --branch
git -C "$LOCAL_REPO" log -1 --format='%H %ad %s' --date=iso-strict
```

`HEAD` bezeichnet die aktuell ausgecheckte Referenz des Repositorys. Ein erfolgreiches Ergebnis belegt, dass eine zulässige SSH-Identität das angegebene Repository erreicht hat. Es belegt weder, welcher Schlüssel ausgewählt wurde, noch ob Push-Zugriff besteht.

**Erwartete Ausgabe:** ein Fetch-Ergebnis, Branchstatus und eine Commitzeile. Ungetestetes Beispiel. `fetch` schreibt nichts auf die Remote, aktualisiert aber lokale Referenzen und `FETCH_HEAD`. Der Zyklus führt keinen Push aus und wechselt keine Branches.

Der MCP-Server sollte dieselbe Lesebeschränkung über benannte Vorgänge bereitstellen. Ein lokaler Shell-Wrapper oder ein MCP-Tool sollte ein Schreibverb ablehnen, bevor es eine Anfrage sendet. Protokolliere Toolname, Repository-Platzhalter, Revision, Ergebnisklasse und Dauer. Schwärze Tokens, Cookies, private Pfade und Dateiinhalte, sofern die Aufgabe keine bestimmte Datei erfordert.

## Fehlerbehebung

### `Permission denied (publickey)`

Prüfe den aktiven Agenten-Socket, den ausgewählten öffentlichen Schlüssel, den Repository-Zugriffsschlüsseleintrag und `IdentitiesOnly`. Ein Repository-Schlüssel muss im Zielrepository oder -projekt hinterlegt sein. Ein persönlicher Schlüssel benötigt Kontoberechtigungen. Ein Workspace-Schlüssel hat eine andere Schreibgrenze.

### Es wird der falsche Repository-Schlüssel angeboten

Verwende einen Schlüssel pro Repository mit `core.sshCommand` oder gruppiere Klone in einem durch `includeIf` kontrollierten Verzeichnis. Liste Agentenschlüssel mit `ssh-add -l` auf. Wenn viele 1Password-Schlüssel verfügbar sind, verwende einen expliziten Identitätsselektor oder ein 1Password-SSH-Lesezeichen. Der [1Password-Agentenleitfaden](https://www.1password.dev/ssh/agent) beschreibt die Anzahl der Schlüssel und Lesezeichen.

### SSH meldet einen geänderten Hostschlüssel

Stoppe den Agenten. Lösche `known_hosts` nicht als erste Reaktion. Vergleiche den aktuellen Bitbucket-Cloud-Hostschlüsseleintrag über einen unabhängigen Kanal mit dem lokalen Eintrag. Entferne oder ersetze einen Eintrag erst, nachdem der Vergleich erfolgreich war.

### Die API gibt `401` oder `403` zurück

Prüfe Tokenablauf, Tokentyp, Endpunktbereich und Konto- oder Workspace-Grenze. Ein Repository-Lesebereich umfasst keine Pull Requests. Ein Schreibendpunkt benötigt einen Schreibbereich und ein genehmigtes Schreibprofil. Erweitere Bereiche nicht, bevor der fehlgeschlagene Endpunkt feststeht.

### Die API liefert Repository-Daten, aber keine Pull Requests

Ergänze den kleinsten Pull-Request-Lesebereich bei einem neuen oder rotierten Token. Verwende kein weitreichendes Benutzertoken erneut für einen schreibgeschützten MCP-Server.

### Der MCP-Server listet Tools auf, aber ein Aufruf schlägt fehl

Trenne Serverregistrierung, Verbindung, Toolerkennung, Ausführung und Ergebnisprüfung. Prüfe das Serverlog, ohne das Token offenzulegen. Verifiziere Endpunkt und Eingabeformat. Wiederhole den Aufruf nach der Konnektivitätsprüfung einmal. Markiere den Vorgang als unvollständig, wenn auch der zweite Aufruf fehlschlägt.

### Eine Bitbucket-CLI eines Drittanbieters verlangt weitreichenden Zugriff

Stoppe die Installation. Vergleiche den angeforderten Zugriff mit der Aufgabenbeschreibung. Prüfe Quellcode, Release-Signaturen oder Prüfsummen, Netzwerkziele, Geheimnisspeicherung und Schreibverhalten. Die offizielle Atlassian-CLI-Befehlsreferenz belegt nicht die Unterstützung einer Bitbucket-Binärdatei eines Drittanbieters.

## Nächste Schritte

Erstelle ein kurzes Zugriffsprotokoll mit Repository- oder Projektbereich, Schlüsselbezeichnung, Datum der Hostschlüsselprüfung, API-Bereichen, Tokenablauf, 1Password-Besitzer, MCP-Tool-Allowlist, Protokollierungsrichtlinie und Freigebendem für Schreibzugriffe.

Führe einen schreibgeschützten Klon, einen REST-Metadaten-Lesezugriff und einen MCP-Tool-Lesezugriff mit Platzhaltern im Transkript aus. Vergleiche die Ergebnisse. Lass das Agentenprofil schreibgeschützt, bis Protokoll und Logs geprüft sind.

Bereite bei einer Schreibaufgabe zuerst einen lokalen Diff vor. Nenne Zielbranch, geänderte Pfade, angeforderte API-Methode, Tokenbereich und Rollback-Schritt. Verwende eine separate kurzlebige Schreibidentität erst, nachdem ein Mensch die genaue Aktion genehmigt hat.

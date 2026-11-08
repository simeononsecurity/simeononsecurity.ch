---
title: "KI-Publikationsablauf für GitHub, Confluence und Jira"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Veröffentliche einen festen Aufbewahrungsvorschlag in Confluence, GitHub und Jira, prüfe Versionen und plane die Wiederherstellung nach einer Teilveröffentlichung."
genre: ["Künstliche Intelligenz", "Teamarbeit", "Softwareentwicklung"]
tags: ["KI-Zusammenarbeitskurs", "Confluence Cloud", "Jira Cloud", "systemübergreifende Veröffentlichung", "Versionsprüfung", "Veröffentlichungsprotokoll", "Teil-Veröffentlichung"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration von Fachleuten, die gemeinsam Projektarbeit in einem Arbeitsbereich für Cybersicherheit prüfen"
coverCaption: ""
---

[Zurück zum KI-Zusammenarbeitskurs](/ai-collaboration-course-start/)

**Der Beitragende friert PROP-042 ein, bevor die Verantwortlichen den Vorschlag genehmigen.** Eine für Confluence zuständige veröffentlichende Person aktualisiert die Anforderungen, ein GitHub-Maintainer führt die Implementierung zusammen und der Betrieb veröffentlicht das Runbook. Jira dokumentiert jeden Schritt. Führe dies erst nach der Berechtigungsprüfung aus, denn die drei Systeme bilden keine gemeinsame atomare Transaktion. Dein Veröffentlichungsprotokoll macht eine unvollständige Bereitstellung sichtbar.

## Wichtigste Erkenntnisse

- **Genehmigte Absicht** unterscheidet sich vom ausgelieferten Verhalten.
- **Feste Vorschlagsrevisionen** binden die Prüfung an eine Version.
- **Veröffentlichungsprotokolle** machen Teilergebnisse sichtbar.
- **Aktuelle Lesevorgänge** schützen vor geänderten Grundlagen.

## Vor dem Start

**Voraussetzungen:** die [Arbeitsplatzeinrichtung](/articles/ai-collaboration-confluence-jira-setup/), Veröffentlichungszugriff, Verantwortliche und ein Repository-Maintainer. **Geschätzte Zeit:** zwei Stunden. **Schwierigkeit:** anspruchsvolle Koordination.

**Basisschnittstelle:** Lesezugriffe im Browser, optionales Entwerfen im genehmigten Chat und Veröffentlichung durch einen Menschen. Ein Connector-Abonnement wird nicht vorausgesetzt. Prüfe vor dem Hinzufügen einer Integration die Verfügbarkeit im Mandanten, Berechtigungsumfänge, die Verarbeitung durch den Anbieter und die Identitätszuordnung. Teile niemals die Zugangsdaten einer verantwortlichen Person mit einem Beitragenden.

**Ergebnis für Leser:** Am Ende hast du einen festen Vorschlag, ein Veröffentlichungsprotokoll für jedes System, Nachweise aus dem erneuten Auslesen und eine Wiederherstellungsentscheidung für den ersten unvollständigen Schritt. Die Übung belegt das Verfahren und den Umgang mit Nachweisen, nicht das Aufbewahrungsverhalten in der Produktion.

## Aktuelle Quellen erfassen

1. **Lies MAP-01** und öffne anschließend REQ-17 und RUN-04 anhand der zugeordneten Seiten-IDs.
2. **Öffne das Seitenmenü und den Seitenverlauf (Page History)** und erfasse Versionsnummern, Status, Wortlaut, verantwortliche Person und Ausnahmen.
3. **Lies das Jira-Element** und hänge einen unveränderlichen Vorschlagsexport oder GitHub-Commit an. Der Schlüssel allein friert den Prüfungsnachweis nicht ein.
4. **Lies die genehmigte POL-01** und die geschützte Konfigurations-Baseline.
5. **Gib dem Chat nur notwendige synthetische Auszüge**, kennzeichne sie als Momentaufnahmen und deaktiviere schreibfähige Aktionen.

```text
Task: PROP-042, propose only
Authority: Confluence REQ-17 for intent, GitHub for behavior
Read: mapped current pages, versions, scope, exceptions
Proposal: synthetic export retention from 7 to 30 days
Output: requirement wording, config diff, runbook, ledger
Evidence: source ID and captured revision for each factual claim
Unknowns: missing access and absent runtime observations
Stop: conflict, changed base, or denied access
```

**Offline-Pakete bleiben Momentaufnahmen.** Vor jedem Schreibvorgang liest die veröffentlichende Person die aktuellen Quellen erneut. Verweigerter Zugriff blockiert die Veröffentlichung. Ein alter Export ersetzt keine aktuelle Berechtigung.

## Den Vorschlag einfrieren

```json
{
  "proposal_id": "PROP-042",
  "proposal_revision": 1,
  "requirement_base_version": 1,
  "runbook_base_version": 1,
  "policy_version": 1,
  "from_days": 7,
  "to_days": 30,
  "status": "awaiting-owner-review",
  "publication_order": ["requirement", "implementation", "runbook", "delivery"]
}
```

**Ersetze beispielhafte Seitenversionen durch die tatsächlich erfassten Versionen.** Hänge das feste JSON und den vorgeschlagenen Wortlaut an Jira an. Jede verantwortliche Person dokumentiert Rolle, Entscheidung, Vorschlagsrevision, Quellversionen und Prüfzeitpunkt. Jede inhaltliche Änderung setzt das Paket auf `Review` zurück.

**Das Produktteam prüft Absicht und Umfang. Der Betrieb prüft Bereinigung und Wiederherstellung.** Der Maintainer prüft den Diff. Reaktionen auf veränderliche Chatnachrichten sind keine revisionsgebundenen Genehmigungen.

## Veröffentlichen und erneut auslesen

1. **Setze Jira auf `Publishing`**, nachdem die veröffentlichende Person beide Prüfungen der Verantwortlichen und unveränderte Quellgrundlagen bestätigt hat.
2. **Veröffentliche REQ-17** mit dreißig Tagen und einem Feld für ausstehende Bereitstellung. Erfasse die resultierende Version, den Umfang und die Ausnahmen.
3. **Öffne den GitHub-Implementierungs-PR** mit Verweis auf die genehmigte Seitenversion. Ändere die Konfiguration auf dreißig Tage und hänge eine nicht maßgebliche Momentaufnahme der Anforderung an.
4. **Führe den PR nach der Repository-Prüfung zusammen** und lies **`main`** erneut aus. Dokumentiere festgeschriebenes Verhalten getrennt vom Laufzeitverhalten.
5. **Veröffentliche RUN-04**, lies es anhand der ID erneut aus und erfasse die resultierende Version. Die veröffentlichende Person aktualisiert die Lieferverweise in der Anforderung.
6. **Schließe Jira erst ab**, wenn alle Einträge übereinstimmen und der Nachweis des letzten erneuten Auslesens angehängt ist.

**Nutze den lokalen Validator nur für die Konsistenz von Momentaufnahmen.** Kopiere die Confluence-Anforderung vor der Änderung in das JSON-Basisschema des Labs, erfasse sie und ändere den Kandidaten auf dreißig Tage. Erhöhe die lokale Momentaufnahmen-Revision und bewahre die tatsächlichen Confluence-Versionen separat in Jira auf. Der GitHub-zuerst-Workflow als Quellbasis validiert kein Live-Confluence. Stelle seinen grünen Status nicht als Verifikation einer externen Autorität dar.

**Setze in dieser Übung keine Löschung um.** Ein echter Dienst benötigt Bereitstellungsnachweise, kontrollierte Testdaten, eine Haltefunktion und Laufzeit-Grenztests. Ein Merge belegt den Repository-Status, nicht das Aufbewahrungsverhalten in der Produktion.

## Teilveröffentlichungen verfolgen

| Schritt | Ausgangszustand | Abschlussnachweis |
|---|---|---|
| **REQ-17** | Pending | Resultierende Seitenversion |
| **Konfiguration** | Pending | Zusammengeführter Commit und Prüfung |
| **RUN-04** | Pending | Resultierende Seitenversion |
| **Jira-Abschluss** | Pending | Abschließendes erneutes Auslesen und Statusübergang |

**Dokumentiere jedes Ergebnis, bevor du den nächsten Schritt versuchst.** PROP-042 verknüpft die einzelnen Systemereignisse. Eine abgeschlossene Zeile bedeutet nie, dass die gesamte Änderung abgeschlossen ist.

**Beispiel für einen Fehler:** Confluence veröffentlicht dreißig Tage, aber GitHub verweigert den Merge. Lass Jira auf `Blocked` und markiere die Anforderung als ausstehend. Das Produktteam entscheidet sich für die Fertigstellung oder eine geprüfte Wiederherstellung auf sieben Tage. Mache eine Notfallkopie in der README-Datei nicht zur maßgeblichen Anforderung.

## Gleichzeitige Bearbeitungen behandeln

**Browser-Baseline:** Bestimme für das Pilotfenster eine veröffentlichende Person. Öffne den Seitenverlauf direkt vor und nach der Veröffentlichung erneut. Ändert eine andere Person die Quelle, halte an, vergleiche und stimme ab, und hole eine neue Genehmigung ein. Eine serialisierte Veröffentlichung ist ein Verfahren, keine Garantie für eine atomare Transaktion.

**API-Erweiterung:** Die Confluence-v2-Dokumentation beschreibt **`GET /wiki/api/v2/pages/{id}?body-format=storage`** und **`PUT /wiki/api/v2/pages/{id}`** mit einem Versionsobjekt. Eine geprüfte Veröffentlichungsintegration vergleicht die aktuelle Version mit der genehmigten Grundlage, übermittelt die nächste Version und liest sie erneut aus. Aktualisiere eine fehlgeschlagene Version niemals automatisch, um einen alten Inhalt erneut zu versuchen.

**Ein API-Erfolg allein genügt nicht.** Prüfe den resultierenden Inhalt, die Quell-ID, den Umfang und die Version. Dieser Kurs enthält keinen schreibfähigen API-Client. Die Veröffentlichung im Browser durch einen Menschen ist die ausführbare Grundlage für Personen ohne Programmierkenntnisse.

## Negative Fälle prüfen

| Injektion | Erwartete Überlegung |
|---|---|
| **Quelle nach der Genehmigung ändern** | Anhalten und für die neue Version erneut genehmigen |
| **Bearbeitungszugriff der veröffentlichenden Person entfernen** | Aktualisierung verweigern und Protokoll offen lassen |
| **Jira auf sechzig Tage setzen** | Konflikt stoppen und Confluence als maßgeblich beibehalten |
| **Runbook-Veröffentlichung schlägt fehl** | Bereitstellung unvollständig lassen und Wiederherstellung zuweisen |

**Dokumentiere tatsächliche Sandbox-Ergebnisse** mit Akteursrolle und Revisionen davor und danach. Füge keine geschützten Seiteninhalte zu Nachweisen für Nutzer mit verweigertem Zugriff hinzu. Erwartete Ergebnisse sind keine Messwerte.

## Das Prüfungspaket zusammenstellen

**Friere den Inhalt ein, nicht nur die Bezeichnung des Vorschlags.** PROP-042 erscheint in jedem System, aber die Bezeichnung allein legt nicht fest, welchen Inhalt eine verantwortliche Person geprüft hat. Füge den genauen Anforderungstext, den Implementierungsdiff, den Runbook-Text, die Quellversionen und die Veröffentlichungsreihenfolge in ein festes Paket ein.

```text
Package: PROP-042 revision 1, illustrative
Intent: synthetic export retention changes from 7 to 30 days
Exclusions: production data, backups, legal holds
Requirement amendment: fixed proposed REQ-17 wording
Implementation: fixed candidate diff and protected base reference
Runbook amendment: fixed RUN-04 wording and recovery limits
Review: product and operations decisions for this package
Delivery: requirement -> implementation -> runbook -> closure
Stop: changed source, missing review, denied write, failed read-back
```

**Halte das Paket für beide Verantwortlichen verständlich.** Das Produktteam benötigt Absicht und Ausschlüsse. Der Betrieb benötigt die betriebliche Änderung und die Wiederherstellungsgrenze. Beide müssen den Zeitraum verstehen, in dem die genehmigte Absicht und die ausgelieferte Konfiguration voneinander abweichen. Ein reiner Code-Diff genügt keiner verantwortlichen Person, die die Repository-Dateien nicht kennt.

**Ausgefüllter Paketinhalt für dieses synthetische Beispiel:**

```text
REQ-17 proposed v5: "Synthetic export files are retained for 30 days from creation. This pilot excludes production data, backups, and legal holds. Delivery remains pending until the GitHub configuration and RUN-04 read-backs match this approved wording."

GitHub config.json, proposed change against base-001:
-  "retention_days": 7
+  "retention_days": 30

RUN-04 proposed v3: "Retention days: 30. Synthetic exports only. No deletion job runs in this lab. If publication fails, keep delivery pending, read back each source, and obtain owner approval before restoring the seven-day configuration or completing the thirty-day publication."
```

Diese Zeichenfolgen sind Beispieltexte für Vorschläge, keine Datensätze eines aktiven Mandanten. Hänge vor der Prüfung den tatsächlichen Basis-Commit und die Seitenversionen an. Das feste Paket muss die vollständigen vorgeschlagenen Inhalte enthalten, nicht nur eine Zusammenfassung, aus der eine verantwortliche Person den Wortlaut ableiten müsste.

**Trenne die Offline-Momentaufnahme von der Live-Veröffentlichung.** Eine Konsistenzprüfung zeigt die Übereinstimmung erfasster Datensätze. Direkt vor dem ersten Schreibvorgang prüft die veröffentlichende Person die zugeordneten Seiten erneut und der Maintainer prüft die geschützte Grundlage erneut. Hat sich eine davon geändert, endet das alte Paket bei `Review`.

## Das Protokoll durchgehen

**Beispielhafter Statusverlauf:** Die Tabelle verwendet Lehrversionen, keine Beobachtungen. Trage nach jedem Sandbox-Schreibvorgang die tatsächlich resultierenden Versionen und Commits ein.

| Schritt | Status nach erfolgreichem erneutem Auslesen | Verbleibende Arbeit |
|---|---|---|
| **Prüfung durch Verantwortliche abgeschlossen** | Genehmigtes Paket, alle veröffentlichten Werte auf sieben | Alle Veröffentlichungsschritte |
| **REQ-17 veröffentlicht** | Absicht auf dreißig, Bereitstellung ausstehend | Konfiguration und Runbook |
| **GitHub-Merge erneut ausgelesen** | Absicht/Konfiguration auf dreißig, Runbook auf sieben | Runbook und abschließender Abgleich |
| **RUN-04 veröffentlicht** | Alle zutreffenden Datensätze auf dreißig | Unabhängiges abschließendes Auslesen |
| **Bereitstellung abgeschlossen** | Vollständiges Protokoll mit Nachweisen | Dokumentierte Laufzeitlücken bleiben bestehen |

**Eine ausstehende Bereitstellung ist ein sinnvoller Zustand.** So wird die alte Implementierung nicht als konform mit der neuen Absicht beschrieben, solange die Veröffentlichung unvollständig ist. In dieser Zeit benötigen Leser beide Werte und keine einzelne Zusammenfassung mit der Aussage „Aufbewahrung: dreißig Tage“.

**Füge fehlgeschlagene Versuche als separate Ereignisse an.** Schlägt ein Runbook-Schreibvorgang fehl, bewahre die erfolgreichen Ergebnisse für Anforderung und Konfiguration auf. Dokumentiere den Runbook-Versuch, den Fehler, die unveränderte Version, die zugewiesene Rolle und die nächste Aktion. Setze abgeschlossene Zeilen nicht auf `Pending` zurück und lösche nicht die beobachtete Abfolge.

**Beispiel für die Ablehnung einer veralteten Version:** Die veröffentlichende Person liest REQ-17 v4, eine andere autorisierte Person veröffentlicht v5, danach versucht die erste Person, PROP-042 r1 auf v4 anzuwenden. Die Plattform meldet einen Versionskonflikt, oder das erneute Auslesen vor dem Schreibvorgang erkennt v5. Dokumentiere den Akteur `publisher`, die Ausgangsversion `v4`, den Versuch `PROP-042 r1`, den erkannten Konflikt oder die geänderte aktuelle Version, die unveränderte Endversion `v5` dieses Versuchs und die zugewiesene verantwortliche Person `product owner`. Lass Jira auf `Review`. Lies v5 erneut aus, stimme den Wortlaut ab und fordere die Prüfung eines neuen festen Pakets an, bevor du erneut schreibst. Verwende bei einem Live-Test die tatsächliche Plattformantwort und den Seitenverlauf. Diese Zeile ist ein Lehrbeispiel.

**Abgeschlossenes Lehrbeispiel, nur synthetische Werte:**

| System | Ausgangsquelle | Feste Prüfung | Schreiben und erneutes Auslesen | Endstatus |
|---|---|---|---|---|
| Confluence REQ-17 | v4, sieben Tage | PROP-042 r1, Product genehmigte v4 zu v5 | Veröffentlichungsperson schrieb v5, Prüfer öffnete v5 erneut | Dreißig Tage, Backups und rechtliche Sperren ausgeschlossen |
| GitHub-Konfiguration | `main`-Commit `base-001`, sieben Tage | PROP-042 r1, Operations genehmigte den Kandidat-Diff | PR als `merge-002` zusammengeführt, unabhängiger Klon las dreißig aus | Dreißig Tage in der geschützten Quelle |
| Confluence RUN-04 | v2, sieben Tage | PROP-042 r1, Operations genehmigte v2 zu v3 | Veröffentlichungsperson schrieb v3, Prüfer öffnete v3 erneut | Betriebsanweisung für dreißig Tage mit Rücksetzoption |
| Jira PROP-042 | In Review | Beide Entscheidungen der Verantwortlichen an r1 gebunden | Lieferverantwortlicher fügte Nachweise hinzu und setzte den Status auf `Done` | Abschluss nach allen drei erneuten Lesevorgängen |

Die obigen Bezeichnungen sind Beispiele und keine Mandantennachweise. Dein Protokoll benötigt native Seitenversionslinks und Commit-IDs. Hänge vor dem Wechsel von Jira zu `Done` den eingefrorenen Vorschlag, beide Rollenprüfungen, den Quellbasisdatensatz, jeden Veröffentlichungsnachweis, das Ergebnis des Negativtests und verbleibende Laufzeitgrenzen an. Fehlt ein Punkt, lass die Bereitstellung offen oder auf `Blocked`.

**Paketprüfung:** Markiere jede der fünf Prüfungen mit Supported oder Blocked: Quellrevisionen sind aktuell, beide Verantwortlichen genehmigten dieselbe feste Revision, alle erforderlichen Veröffentlichungen stimmen mit dem erneuten Auslesen überein, Laufzeitgrenzen bleiben ausdrücklich dokumentiert und der Wiederherstellungsstatus ist abgeglichen. `Done` erfordert fünf Supported-Prüfungen und keinen unautorisierten Schreibvorgang.

## Einen unklaren Schreibvorgang behandeln

**Bei einem Timeout bleibt das Ergebnis unbekannt.** Er belegt weder Erfolg noch Fehlschlag. Öffne in der Browser-Baseline die zugeordnete Quelle erneut und prüfe ihren aktuellen Inhalt und Verlauf, bevor du über einen erneuten Versuch entscheidest.

1. **Pausiere den nächsten Schritt:** Lass die Bereitstellung unvollständig.
2. **Lies das Ziel erneut aus:** Vergleiche den aktuellen Wortlaut, die Version und den Umfang mit dem festen Paket.
3. **Dokumentiere die Beobachtung:** abgeschlossen, unverändert, widersprüchlich oder nicht zugänglich.
4. **Wähle die nächste Aktion:** Setze bei verifiziertem Abschluss fort, wiederhole einen autorisierten unveränderten Schritt oder eskaliere einen Konflikt.
5. **Bewahre die Unsicherheit:** Halte den fehlgeschlagenen oder unbekannten Versuch neben dem späteren erneuten Auslesen fest.

**Spiele nicht blind die ganze Abfolge erneut ab.** Ein bereits abgeschlossener Schritt erzeugt zusätzliche Revisionen und kann nicht zusammenhängende Änderungen überschreiben. Setze bei einem verifizierten Zustand fort. Ist die Quelle nicht erreichbar, wähle `Hold`, statt aus dem alten Protokoll zu raten.

## Wiederherstellungsentscheidungen vergleichen

| Situation | Zu prüfende Entscheidung | Grund |
|---|---|---|
| **Anforderung geändert, Merge verweigert** | Vorwärts fortsetzen oder Anforderung kompensieren | Absicht und Verhalten unterscheiden sich |
| **Konfiguration geändert, Runbook verweigert** | Runbook fertigstellen oder Konfiguration zurücknehmen | Betriebsanweisung ist veraltet |
| **Andere verantwortliche Person ändert den Umfang** | Zu `Review` zurückkehren | Die feste Genehmigung beschreibt einen anderen Inhalt |
| **Ergebnis des Schreibens unbekannt** | Ziel zuerst erneut auslesen | Erneuter Versuch hängt vom beobachteten Zustand ab |
| **Veröffentlichungsperson verliert Zugriff** | Anhalten und autorisierte Administration anfordern | Alte Berechtigung erlaubt keine neuen Schreibvorgänge |

**Entscheide anhand des aktuellen Zustands und der Entscheidung der verantwortlichen Person.** Eine Vorwärtsfertigstellung erfordert aktuelle Genehmigungen und praktikable Kontrollen. Eine Kompensation erfordert die Prüfung der Wiederherstellung im Hinblick auf zwischenzeitliche Änderungen. Eine Wiederherstellungsänderung ist eine weitere Veröffentlichung und keine privilegierte Ausnahme vom Verfahren.

## Abschluss der Veröffentlichung überprüfen

**Liefere ein Paket, das ein unabhängiger Prüfer abgleichen kann.** Er sollte den exakt geprüften Vorschlag, seine Quellgrundlagen, beide Rollenprüfungen, jedes Schreibergebnis, die Endwerte und verbleibende Laufzeitgrenzen finden. Bitte ihn, nach einer Unterbrechung den ersten unvollständigen Schritt zu bestimmen.

**Erwartete Überlegung:** Die nächste Aktion folgt aus aktuellen Quellen und dem Protokoll, nicht aus dem Vertrauen in den vorherigen Assistenten. Übernimm die abschließenden Verweise auf die zugeordneten Quellen in die Abrufprüfungen, damit die Suche dieselbe Unterscheidung der maßgeblichen Quellen bewahrt.

## Fehlerbehebung und Wiederherstellung

**Version geändert:** Verlauf vergleichen und Prüfung erneuern. **Momentaufnahmeprüfung erfolgreich, aber Wiki weicht ab:** aktuelle Confluence-Quellen erneut abrufen. **Zu früh abgeschlossen:** über den zulässigen Ablauf wieder öffnen und fehlende Schritte dokumentieren.

**Wiederherstellung:** Vergleiche den Seitenverlauf und nutze eine von der verantwortlichen Person genehmigte Wiederherstellung oder kompensierende Änderung. Dokumentiere die resultierende Version, statt anzunehmen, die Wiederherstellung setze die Nummerierung zurück. Wenn das Produktteam einen Rückbau wählt, setze die Konfiguration über einen geschützten PR zurück. Gelöschte Dateien sind nicht von der Rücksetzgarantie abgedeckt.

## Übung und Selbstprüfung

**Unterbrich nach der Veröffentlichung von REQ-17** und gib einer anderen veröffentlichenden Person nur die Zuordnung und das Protokoll.

**Erwartete Überlegung:** Sie ruft aktuelle Quellen ab, bestätigt die feste Genehmigung und setzt nur den autorisierten ausstehenden Schritt fort. Fehlende Nachweise führen zurück zu `Review`.

## Primärquellen

- **Verlauf und Wiederherstellung:** [technische Confluence-Dokumentation](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Versionierte API-Operationen:** [Confluence REST API v2 – Seiten](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/).
- **Workflowkontrollen:** [Erweiterte Jira-Workflows](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).
- **Integrationssicherheit:** [Best Practices für MCP-Sicherheit](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices).

## Nächste Schritte

**Fahre nach einem geprüften Veröffentlichungslauf mit [Abruf anhand einer Zuordnung](/articles/ai-collaboration-map-first-retrieval/) fort.**

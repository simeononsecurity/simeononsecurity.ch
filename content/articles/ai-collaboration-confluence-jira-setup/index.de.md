---
title: "Confluence und Jira für KI einrichten: Berechtigungen und Zuständigkeit"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Richte maßgebliche Confluence-Seiten und Berechtigungen für unternehmensverwaltetes Jira ein, damit Teams nach Prüfung zusammenarbeiten können."
genre: ["Künstliche Intelligenz", "Teamarbeit", "Softwareentwicklung"]
tags: ["KI-Zusammenarbeitskurs", "Confluence Cloud", "Jira Cloud", "maßgebliche Seiten", "Jira-Berechtigungsschema", "Workflow-Übergang", "Zugriffstests"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration von Fachleuten, die gemeinsam an einem Projekt in einer Cybersicherheitsumgebung arbeiten"
coverCaption: ""
---

[Zurück zum Kurs für KI-Zusammenarbeit](/ai-collaboration-course-start/)

**Die Administration legt zuerst die Zuständigkeiten am Arbeitsplatz fest und verbindet danach Chattools.** Produkt- und Betriebsverantwortliche veröffentlichen Anforderungen und Runbooks in Confluence Cloud. Jira Cloud koordiniert die Auslieferung. GitHub verwaltet die Implementierung. Richte dedizierte Testumgebungen erst nach dem Fundament ein, denn eine falsche Berechtigung legt Informationen unabhängig vom Modellverhalten offen.

## Wichtigste Erkenntnisse

- **Confluence** enthält den genehmigten Wortlaut der Anforderungen.
- **Jira** verwaltet den Auslieferungsstatus, nicht die Aufbewahrungsrichtlinie.
- **GitHub** verwaltet Konfiguration und gemeinsame Richtlinien.
- **Berechtigungstests** erfordern passende Pläne und getrennte Benutzer.

## Vor dem Start

**Voraussetzungen:** das [Fundament](/articles/ai-collaboration-pilot-foundation/), das Lab-Repository, die Administration von Confluence-Bereichen und Jira sowie separate Konten für Mitwirkende, Verantwortliche und Publisher. **Geschätzte Zeit:** 90 bis 120 Minuten. **Schwierigkeit:** fortgeschrittene Administration.

**Anforderung an den Tarif:** Confluence Free unterstützt keine Inhaltsbeschränkungen. Jira Free bietet keine konfigurierbaren Berechtigungsschemata, Bereichsrollen oder Sicherheitsschemata für Arbeitselemente. Verwende für diesen Lernpfad geeignete Sandboxes mit Standard oder höher. Prüfe vor den Tests anhand der Referenzen den tatsächlichen Tarif und die Berechtigungen.

**Hinweis zur Navigation:** Die aktuelle Jira-Dokumentation verwendet „space“ und „work item“. Manche Tenants führen noch „project“ und „issue“. Wähle eine unternehmensverwaltete Konfiguration. Das Verhalten von teamverwalteten Berechtigungen ist nicht Teil dieses Verfahrens. Rovo, Marketplace-Apps, Genehmigungen in Jira Service Management und ein kostenpflichtiger Chatconnector sind nicht erforderlich.

**Ergebnis:** Erstelle eine Berechtigungsmatrix, benannte maßgebliche Seiten, einen Jira-Workflow nur für das Lab und Nachweise für verweigerten Zugriff durch separate Benutzer. Halte den Tenant-Tarif und die Rollenannahmen neben den Testergebnissen fest.

**Prüfe vor dem Erstellen von Datensätzen:**

| Prüfung | Wenn verfügbar | Wenn nicht verfügbar |
|---|---|---|
| Seitenbeschränkungen und Bereichsadministration in Confluence | Erstelle separate genehmigte und ausgeschlossene Seiten | Markiere Tests für Seitenbearbeitung und verweigerten Lesezugriff als Blockiert |
| Unternehmensverwaltetes Jira-Berechtigungsschema und Workflow-Editor | Kopiere Schema und Workflow nur für das Lab | Markiere Übergangstests als Blockiert |
| Separate Benutzer für Mitwirkende, Verantwortliche, Publisher und ausgeschlossene Benutzer | Führe rollenbezogene positive und negative Tests aus | Markiere nicht getestete Rollen als Blockiert |
| Repository-Maintainer und geschützter Branch | Verknüpfe den geprüften Implementierungspfad | Schließe zuerst den GitHub-first-Pfad ab, bevor du gemischt veröffentlichst |

Stand Oktober 2026 verwendest du für den Seitenzugriff die Schaltfläche **Share** oder die Einschränkungssteuerung, in Confluence den Berechtigungsbereich unter **Space settings** für umfassendere Freigaben und in Jira **Settings > Work items > Permission schemes** für das Labschema. Der Workflow-Editor für unternehmensverwaltetes Jira steuert die Übergänge. UI-Bezeichnungen und Tarifmerkmale unterscheiden sich je Tenant. Halte vor diesen Schritten den tatsächlichen Pfad und Tarif als Nachweis fest. Siehe [Berechtigungen auf Confluence-Seitenebene](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/) und [Jira-Berechtigungsschemata](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/).

## Maßgebliche Seiten erstellen

1. **Erstelle einen Confluence-Bereich** mit dem Namen **`Export Service Lab`**. Deaktiviere anonymen Zugriff und öffentliches Teilen über die verfügbaren Website- und Bereichseinstellungen.
2. **Erstelle veröffentlichte Seiten**, keine Live-Dokumente, mit den Namen **`REQ-17 Export Retention`**, **`RUN-04 Export Cleanup`** und **`Decision Register`**.
3. **Veröffentliche die anfängliche Anforderung** unten als Produktverantwortlicher. Halte die tatsächliche Seiten-ID und Version in der Repository-Karte fest.
4. **Veröffentliche RUN-04** als Betriebsverantwortlicher mit sieben Tagen Aufbewahrung und dem Hinweis, dass in diesem Lab kein Löschauftrag ausgeführt wird.
5. **Öffne Share** auf jeder maßgeblichen Seite. Setze den allgemeinen Zugriff für berechtigte Bereichsmitglieder auf Nur-Lesen und gewähre ausgewählten Verantwortlichen und Publishern gezielte Bearbeitungsrechte. Speichere und prüfe den Zugriff mit dem Mitwirkendenkonto.

```text
Source ID: REQ-17
Owner role: product-owner
Status: Approved baseline
Scope: synthetic export files only
Retention: 7 days
Delivery state: baseline lab configuration
Exceptions: production data, backups, and legal holds excluded
Approval evidence: DEC-12 baseline review
Implementation reference: attach protected GitHub baseline commit
```

**Setze für jede maßgebliche Seite Einschränkungen.** Gehe nicht davon aus, dass eine Bearbeitungssperre auf einer übergeordneten Seite auch deren Unterseiten schützt. Die Vererbung von Lese- und Bearbeitungsrechten unterscheidet sich, und Bereichsberechtigungen gelten weiterhin. Ein Link allein gewährt keinen Zugriff. Prüfe alle Mitgliedschaften, wenn ein vermeintlicher Nur-Lesen-Benutzer weiterhin Änderungen vornehmen kann.

**Verwende diese Starttexte für die beiden anderen Seiten.** Ersetze vor der Genehmigung eines Datensatzes die Platzhalter für Prüfungen durch tatsächliche Nachweise aus der Sandbox.

```text
Source ID: RUN-04
Owner role: operations-owner
Status: Approved baseline
Scope: synthetic export files only
Configured retention: 7 days
Procedure: compare REQ-17 with config.json before a reviewed change
Runtime limit: this lab has no deletion job and produces no deletion evidence
Recovery: restore the prior approved configuration through review
Recovery limit: restoring configuration does not restore deleted files
Review evidence: add actual reviewer, page version, and decision reference
```

```text
Page: Decision Register
Entry ID: DEC-12
Decision: use seven days as the synthetic baseline
Scope: export-service-lab only
Requirement: REQ-17 page version, record after publication
Runbook: RUN-04 page version, record after publication
Policy: POL-01 protected GitHub revision, record after review
Product review: pending until the named owner records a decision
Operations review: pending until the named owner records a decision
Status: draft example, replace with observed review evidence
```

## Die Karte aktualisieren

```yaml
track: mixed-workplace
policy: {source_id: POL-01, home: GitHub, version: 1}
requirements: {source_id: REQ-17, home: Confluence, owner_role: product-owner}
runbook: {source_id: RUN-04, home: Confluence, owner_role: operations-owner}
decisions: {source_id: DEC-12, home: Confluence, owner_role: project-lead}
implementation: {home: GitHub, file: config.json}
delivery: {home: Jira, proposal_id: PROP-042}
snapshot_rule: repository requirement copies are not authoritative
```

**Ergänze die tatsächlichen privaten Sandbox-Standorte und Seiten-IDs** in der Karte. Die Vorlage benennt die maßgeblichen Quellen, ohne vorzugeben, Live-Adressen zu enthalten. Entferne README-Text, der die kopierte JSON-Datei zur maßgeblichen Quelle für Anforderungen im gemischten Pfad erklärt.

**POL-01 bleibt für beide Pfade in GitHub.** Confluence verweist auf die geprüfte Revision. Eine Änderung der Richtlinienzuständigkeit während einer Aufgabe erfordert einen weiteren geprüften Zuständigkeitswechsel.

## Jira-Berechtigungen festlegen

1. **Erstelle einen unternehmensverwalteten Lab-Bereich** und kopiere ein Berechtigungsschema in ein eigenes Labschema. Ändere kein gemeinsam genutztes Produktionsschema.
2. **Öffne Settings, Work items, Permission Schemes**, wähle das Labschema und passe die Berechtigungen an.
3. **Gewähre Mitwirkenden die Berechtigungen zum Anzeigen, Erstellen und Kommentieren.** Beschränke Administratorrechte. Prüfe Bearbeitung und **Transition work items** ausdrücklich.
4. **Ordne das Schema** dem Lab-Bereich zu und prüfe, dass kein Produktionsbereich es gemeinsam nutzt.
5. **Erstelle PROP-042** als Arbeitselement. Halte den generierten Schlüssel in der Karte fest und verwende PROP-042 in der Beschreibung weiterhin als logische Vorschlags-ID.

**Füge diesen Entwurf in PROP-042 ein.** Das Jira-Element verfolgt die Auslieferung. Sein Text ersetzt nicht den genehmigten Wortlaut in Confluence.

```text
Proposal ID: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 page version to record
Proposed value: 30 days for synthetic export files
Exclusions: production data, backups, legal holds
Affected records: REQ-17, RUN-04, config.json, proposal.json
Fixed proposal attachment: pending
Product-owner review: pending
Operations-owner review: pending
Publication ledger: pending
Stop on changed source version, missing review, or denied access
```

| Rolle | Confluence | Jira | GitHub |
|---|---|---|---|
| **Mitwirkender** | Genehmigte Seiten lesen | Entwürfe erstellen und kommentieren | Vorschlagsbranch oder Issue |
| **Produktverantwortlicher** | Anforderung prüfen | Prüfung der Anforderung festhalten | PR-Nachweise prüfen |
| **Betriebsverantwortlicher** | Runbook prüfen | Betriebsprüfung festhalten | Auswirkungen auf den Betrieb prüfen |
| **Publisher** | Genehmigte Seiten bearbeiten | Veröffentlichungsstatus festhalten | Keine automatische Merge-Berechtigung |
| **Maintainer** | Anforderung lesen | Implementierung festhalten | Geschützte PR prüfen und zusammenführen |

**Berechtigungen aus mehreren Gruppen addieren sich.** Entferne im Lab unbeabsichtigte breite Berechtigungen, statt anzunehmen, dass eine eingeschränkte Zuweisung eine breite aufhebt. Nimm Connector-Identitäten nicht in Administratorgruppen auf.

## Auslieferungsstatus festlegen

**Kopiere einen unternehmensverwalteten Workflow** in einen Workflow nur für das Lab. Füge die Status Entwurf, Prüfung, Genehmigt, Veröffentlichung, Erledigt und Blockiert hinzu. Ergänze Übergänge für Einreichung, Genehmigung, Veröffentlichung, Abschluss, Blockierung und Rückkehr zur Prüfung. Weise ihn nur dem Arbeitstyp des Labs zu.

1. **Wähle im Workflow-Editor den Übergang zu Genehmigt** aus.
2. **Füge eine Bedingung oder Einschränkung hinzu**, die nur der festgelegten Verantwortlichen- oder Publisher-Rolle beziehungsweise -Gruppe den Übergang erlaubt. Verwende die dokumentierten Bedingungssteuerungen und veröffentliche den Workflow-Entwurf als Administrator.
3. **Prüfe vor dem Übergang manuell beide Freigaben der Verantwortlichen.** Jede Prüfung nennt den eingefrorenen Vorschlag und die Quellversionen.
4. **Beschränke Erledigt** auf die verantwortliche Auslieferungsrolle. Entferne alternative oder globale Übergänge, die diese Grenze umgehen.

**Ein beschränkter Übergang ist keine Genehmigung durch zwei Personen.** Er kontrolliert, wer den Übergang ausführt. In diesem Pilotprojekt bleibt die Prüfung der Nachweise beider Rollen ein Verfahren. Halte diese Einschränkung ausdrücklich fest.

**Beispiel für einen Übergangsdatensatz:** Erlaube für **Prüfung zu Genehmigt** nur der festgelegten Gruppe aus Verantwortlichen und Publishern, den Übergang auszulösen. Vorher öffnet die ausführende Person den unveränderlichen PROP-042-Anhang und prüft eine Entscheidung des Produktverantwortlichen und eine des Betriebsverantwortlichen für dieselbe Vorschlagsrevision. Fehlt eine Entscheidung oder bezieht sie sich auf eine ältere Revision, bleibt das Element auf Prüfung und die Lücke wird dokumentiert. Die Workflow-Einschränkung kontrolliert die ausführende Person. Die Nachweisprüfung ist ein separater menschlicher Schritt.

## Zugriffsverweigerung überprüfen

**Als Mitwirkender** liest du REQ-17, versuchst eine Bearbeitung, erstellst den Jira-Entwurf und versuchst den Übergang zu Genehmigt. Erwartet werden eine lesbare Anforderung, verweigerte Bearbeitung, erfolgreiche Vorschlagserstellung und verweigerte Genehmigung. Vergleiche die Quellversionen vor und nach der Verweigerung.

**Als ausgeschlossener Benutzer** öffnest du eine separat beschränkte synthetische Seite. Es darf kein Inhaltszugriff möglich sein. Prüfe Unterseiten unabhängig. Füge geschützten Text nicht als Umweg in den Chat des ausgeschlossenen Benutzers ein.

## Die Repository-Karte anpassen

**Quell-IDs bleiben bei einem Wechsel des Speicherorts stabil.** REQ-17 bezeichnet weiterhin die genehmigte Aufbewahrungsabsicht, aber im gemischten Pfad ist eine Confluence-Seite die Quelle. Eine Repository-Kopie unterstützt Prüfungen und Reviews. Sie ersetzt nicht die maßgebliche Seite.

| Datensatz | Maßgebliche Quelle | Behandlung im Repository |
|---|---|---|
| **REQ-17** | Zugeordnete Confluence-Anforderungsseite | Erfasste Kopie mit Nachweis der Seitenrevision |
| **RUN-04** | Zugeordnete Confluence-Runbook-Seite | Erfasster Betriebsauszug zur Wahrung der Konsistenz |
| **POL-01** | Geschützte Richtlinie in GitHub | Gemeinsame Agentenanweisungen verweisen darauf |
| **Konfiguration** | Geschützter GitHub-Datensatz | Vorgeschlagene Implementierungsänderung |
| **Auslieferung** | Jira-Arbeitselement | Verknüpfung zur Zuordnung statt Richtlinienkopie |

**Ergänze Herkunftsnachweise zu den Kopien.** Halte im privaten Vorschlagspaket Quell-ID, Seitenverweis, Seitenversion, Erfassungszeit und erfassende Rolle fest. Nimm native Seitenkennungen nicht in öffentliche Kursabgaben auf. Findet der Publisher eine andere aktuelle Version, gleiche sie vor der Verwendung der Kopie ab.

**Benenne Zuständigkeiten nicht passend zum Werkzeug um.** Die bearbeitbare Jira-Beschreibung ist für Diskussionen praktisch, bleibt aber ein Auslieferungsdatensatz. Ein Satz über dreißig Tage in Jira ersetzt keine Anforderung über sieben Tage in Confluence.

## Zugriffstests entwerfen

**Trenne Lesen, Entwürfe und Veröffentlichung.** Mitwirkende benötigen genügend Zugriff, um die synthetische Anforderung zu verstehen und einen Vorschlag einzureichen. Sie benötigen weder Bearbeitungszugriff auf die maßgebliche Seite noch die Berechtigung, den eigenen Vorschlag als genehmigt zu markieren.

```text
Test record: PERM-REQ-EDIT
Role: contributor
Source: REQ-17
Precondition: source is readable, published revision captured
Attempt: edit the authoritative requirement
Expected: edit denied, published revision unchanged
Observed: fill from the sandbox
Evidence: native result and independent revision read-back
Reviewer: administrator or independent permission reviewer
```

**Verwende für verweigertes Lesen einen separaten Datensatz.** Die lesbare Anforderung des Mitwirkenden prüft die Trennung von Veröffentlichung und Bearbeitung. Die unzugängliche Seite des ausgeschlossenen Benutzers prüft Vertraulichkeit. Eine gemeinsame Zeile verschleiert, welche Grenze getestet wurde.

**Prüfe auch erlaubten Zugriff.** Verantwortliche und Publisher müssen ihre vorgesehenen Wege nutzen können. Wird jeder Benutzer abgewiesen, ist die Sandbox zwar restriktiv, aber nicht nutzbar. Halte eine erfolgreiche autorisierte Bearbeitung auf einer entbehrlichen Testseite fest, ohne während der Berechtigungsdiagnose die genehmigte Anforderung zu ändern.

## Jira-Prüfung üben

**Die Statusnamen sind der Entwurf dieses Pilotprojekts.** Entwurf enthält eine Anfrage. Prüfung enthält ein eingefrorenes Paket. Genehmigt bedeutet, dass die Verantwortlichen ihre Prüfung abgeschlossen haben. Veröffentlichung steht für eine laufende Auslieferung. Erledigt erfordert eine Rückleseprüfung. Blockiert bedeutet fehlende Nachweise, fehlenden Zugriff oder einen ungelösten Konflikt.

| Übergang | Erforderliches Paket | Verantwortliche Prüfung |
|---|---|---|
| **Entwurf zu Prüfung** | Fester Vorschlag und Quellversionen | Mitwirkender bestätigt Vollständigkeit |
| **Prüfung zu Genehmigt** | Entscheidungen von Produkt- und Betriebsverantwortlichen | Autorisierte Person prüft beide Rollen |
| **Genehmigt zu Veröffentlichung** | Vergleich mit aktuellen Quellen | Publisher bestätigt unveränderte Grundlagen |
| **Veröffentlichung zu Erledigt** | Vollständiges Protokoll für jedes System | Auslieferungsverantwortlicher prüft Rücklesung |
| **Jeder unterstützte Schritt zu Blockiert** | Fehler und offene Maßnahme | Wiederherstellungsverantwortlicher zugewiesen |

**Übe mit einem unvollständigen synthetischen Paket.** Reiche nur eine Produktprüfung ein und bitte die autorisierte Person, den Übergang zu bewerten. Erwartet wird, dass die Arbeit in Prüfung bleibt und die Betriebsprüfung angefordert wird. Damit wird der Verfahrensschritt unabhängig von der Plattformverweigerung für Mitwirkende getestet.

**Prüfe alternative Wege gezielt.** Kontrolliere in der Workflow-Ansicht deiner Sandbox jeden Weg zu Genehmigt und Erledigt. Ein beschränkter benannter Übergang genügt nicht, wenn ein anderer verfügbarer Weg dieselbe Prüfgrenze umgeht. Dokumentiere die geprüften Wege und den verwendeten Akteur, statt nach einem Klick vollständige Abdeckung zu behaupten.

## Unerwarteten Zugriff diagnostizieren

**Beginne mit der effektiven Identität.** Prüfe, ob die Browsersitzung zur vorgesehenen Testrolle gehört. Untersuche dann Gruppenmitgliedschaften, Bereichsberechtigungen, Seitenzugriff und Workflow-Zuordnung mit den Administrationstools des Produkts. Ändere nicht mehrere Steuerungen gleichzeitig, da eine Verweigerung sonst ihren diagnostischen Wert verliert.

1. **Identität bestätigen:** getrennte Sitzungen für Mitwirkende, Publisher und ausgeschlossene Benutzer verwenden.
2. **Berechtigung finden:** Mitgliedschaft oder Einstellung ermitteln, die die versuchte Aktion erlaubt.
3. **Lab-Steuerung anpassen:** berechtigten Zugriff der Verantwortlichen erhalten.
4. **Denselben Versuch wiederholen:** nach der Verweigerung die unveränderte Quellversion erfassen.
5. **Positivtest wiederholen:** bestätigen, dass eine autorisierte Veröffentlichung weiterhin funktioniert.

**Abschließende Nachweisliste:** Erfasse den Confluence-Seitenbaum und zugeordnete Seiten-IDs, die Zuordnung des Jira-Labschemas, die Lab-Workflow-Zuordnung, Gruppenmitgliedschaften aller Testrollen, einen erlaubten Lesezugriff auf die Anforderung, eine verweigerte Bearbeitung mit unveränderter Version, eine erlaubte Erstellung des Entwurfs, einen verweigerten Übergang zu Genehmigt bei unverändertem Status, verweigerten Lesezugriff für den ausgeschlossenen Benutzer und die verantwortliche Person für die Bereinigung. Halte für jede Zeile die Akteursrolle, Anfangs- und Endversion beziehungsweise den Status, das native Ergebnis und einen unabhängigen Reviewer fest. Dokumentiere den beobachteten Navigationspfad im Tenant, denn Bezeichnungen und verfügbare Funktionen unterscheiden sich nach Tarif.

**Abschlussprüfung:** Liefere die zugeordneten maßgeblichen Seiten, den Workflow nur für das Lab, die vorgesehene Rollenmatrix und beobachtete Berechtigungsnachweise. Fehlt im Tarif eine notwendige Steuerung, bleibt die betreffende Zeile Blockiert. Die Lektion zur Veröffentlichung setzt erfolgreiche Tests voraus, nicht bloß Screenshots der Einstellungen.

## Fehlerbehebung und Rollback

**Mitwirkender kann weiterhin bearbeiten:** Seitenzugriff, Bereichsberechtigungen und Mitgliedschaften prüfen. **Übergang gelingt weiterhin:** Workflow-Zuordnung und Umgehungswege prüfen. **Einstellungen fehlen:** Unternehmensverwaltung, Edition und Administratorberechtigung prüfen.

**Rollback:** Connector-Berechtigungen entfernen und Entwürfe archivieren. Lab-Schemata und -Workflows erst nach dem Sichern der Nachweise trennen. Genehmigten Seitenwortlaut über die geprüfte Versionsgeschichte oder eine Korrektur wiederherstellen. Keine Auditnachweise löschen.

## Übung und Selbstkontrolle

**Jira nennt dreißig Tage, REQ-17 dagegen sieben.** Ermittle die Implementierungseingabe und die verantwortliche Person für den Abgleich.

**Erwartete Begründung:** Confluence legt die Absicht fest. Jira enthält einen Vorschlags- oder Auslieferungsfehler. Stoppe die Veröffentlichung und bitte den Produktverantwortlichen um Abgleich, statt den neuesten Zeitstempel auszuwählen.

## Primärquellen

- **Einschränkungen und Tarif:** [Confluence-Berechtigungen](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Freigabesteuerung:** [Zugriff auf bestimmte Inhalte](https://support.atlassian.com/confluence-cloud/docs/add-or-remove-page-restrictions/).
- **Schemaadministration:** [Jira-Berechtigungsschemata](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).
- **Übergangsbedingungen:** [Erweiterte Workflows](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).

## Nächste Schritte

**Fahre nach erfolgreichen Zugriffstests mit [Systemübergreifender Veröffentlichung](/articles/ai-collaboration-confluence-jira-publication/) fort.**

---
title: "GitHub-KI-Workflow für Nichtprogrammierer: Issues und Pull Requests"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Nutze Browser-Bearbeitung, Issues, Chat-Kontextpakete und geprüfte Pull Requests ohne lokale Entwicklungsumgebung."
genre: ["Künstliche Intelligenz", "Teamzusammenarbeit", "Softwareentwicklung"]
tags: ["KI-Zusammenarbeitskurs", "GitHub-Browserbearbeitung", "GitHub Issues", "Pull Request", "nicht programmierende Mitwirkende", "Kontextpaket", "Übergabe zur Prüfung"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration von Fachleuten, die gemeinsame Projektarbeit in einem Cybersicherheits-Arbeitsbereich prüfen"
coverCaption: ""
---

[Zurück zum KI-Zusammenarbeitskurs](/ai-collaboration-course-start/)

**Nicht programmierende Mitwirkende verwenden dieselben Autoritätsregeln im Browser.** Du liest GitHub-Quellen, erstellst mit einem genehmigten Chat-Tool einen Entwurf und reichst ein Issue oder eine Änderung in einem Branch ein. Der Maintainer führt die Prüfungen aus und veröffentlicht nach der Prüfung. Nutze diesen Workflow erst, wenn der Repository-Schutz aktiv ist, damit der Browserzugriff die Kontrollen des Coding-Agenten nicht umgeht.

## Wichtigste Erkenntnisse

- **Browserarbeit** benötigt kein lokales Terminal.
- **Kontextpakete** bewahren Umfang und Revisionsnachweise.
- **Issues und Branches** bleiben Vorschläge.
- **Übergaben** nennen offene Arbeit und die nächste Rolle.

## Vor dem Start

**Voraussetzungen:** die [Lektion zu Repository-Grenzen](/articles/ai-collaboration-github-repository/), Lesezugriff auf das Labor und bei Bedarf ein genehmigtes Chat-Tool. **Geschätzte Zeit:** 45 bis 60 Minuten. **Schwierigkeit:** Einstieg. Mitwirkende, die nur Issues verwenden, überspringen lokales Git und Actions. Mitwirkende, die einen PR einreichen, stimmen sich mit einem Maintainer ab, der die [Lektion zu Agenten und Actions](/articles/ai-collaboration-github-agents-actions/) abgeschlossen hat.

**Grundlage ohne Connector:** Öffne GitHub selbst und übermittle nur synthetische Auszüge. Eine Chat-Abonnementfunktion wird nicht vorausgesetzt. Wenn ein Anbieter nicht genehmigt ist, erstelle den Entwurf manuell mit denselben Aufzeichnungen.

**Ergebnis:** Du übergibst ein Issue oder einen PR mit festen Quellrevisionen, vorgeschlagener Formulierung, betroffenen Dateien, Ausschlüssen und offenen Fragen.

## Quellpaket lesen

1. **Öffne MAP-01 auf `main`** und suche dann POL-01, REQ-17 und RUN-04.
2. **Lies jede Quelle** und notiere ihre Commit-Revision über die Commit-Ansicht des Browsers.
3. **Kopiere relevante synthetische Abschnitte** mit Dateinamen, Revisionen, Umfang und Ausnahmen.
4. **Kennzeichne das Paket als snapshot-basiert**, bis der Maintainer es vor der Veröffentlichung mit aktuellen Quellen vergleicht.

```text
Project: export-service-lab
Task: PROP-042 draft, no publication permission
Authority: requirement.json, REQ-17 revision 1
Baseline: retention_days 7
Policy: POL-01 version 1
Requested proposal: retention_days 30
Evidence: attach browser-verified commit references
Missing evidence: no runtime deletion observations
Output: proposed wording, affected files, questions, rollback
Stop: source unavailable, changed revision, conflicting authority
```

**Hänge echte Sandbox-Revisionen privat an.** Die Vorlage enthält keine vollständigen Nachweise. Bitte den Assistenten, fehlende Aufzeichnungen zu nennen, bevor du eine Veröffentlichung empfiehlst.

**Ausgefülltes synthetisches Paket vor dem Lesen einer Live-Quelle:**

```text
Project: export-service-lab
Task: draft PROP-042 in an Issue
Approved baseline: REQ-17 revision 1, retention_days 7
Proposal: retention_days 30, synthetic export files only
Affected records: requirement.json, config.json, proposal.json, runbook.md
Exclusions: production data, backups, legal holds
Known evidence: supplied lab baseline files
Missing evidence: current main commit, owner decisions, runtime deletion result
Status: Draft, publication blocked until current revisions and reviews exist
Next role: maintainer supplies verified main commit and runs the consistency check
```

**Das Paket ist eine vollständige Anfrage als Entwurf.** Die Zeile mit den fehlenden Nachweisen ist absichtlich enthalten. Ersetze die bereitgestellte Laborbasis durch Live-Sandbox-Revisionen, bevor du um Veröffentlichung bittest.

## Ein Issue öffnen

**Wähle Issues, New issue** und verwende den Titel **`PROP-042: propose thirty-day synthetic retention`**. Füge diese Beschreibung ein und hänge das Quellpaket an.

```text
Proposal: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 revision 1
Requested value: 30 days
Reason: fictional pilot requirement, not compliance advice
Scope: synthetic export records only
Affected files: requirement.json, config.json, runbook.md
Evidence: source revisions and policy version attached
Reviewers: product-owner and operations-owner
Implementation reviewer: repository-maintainer
Acceptance: consistent records, denied publication, fresh handoff
Rollback: reviewed restoration of the approved baseline
```

**Bitte den Chat, den Vorschlag mit dem Paket zu vergleichen**, Annahmen aufzulisten und Fragen an die Verantwortlichen zu formulieren. Speichere den Entwurf im Issue. Bitte ihn nicht um Genehmigung und behandle den Chatverlauf nicht als Entscheidungsregister.

## Browseränderungen einreichen

1. **Öffne den Code-Tab des Repositorys.** Wähle das Branch-Menü über der Dateiliste, bestätige **`main`**, gib **`proposal-042`** ein und wähle **Create branch: proposal-042 from main**. Wenn die Branch-Erstellung nicht verfügbar ist, nutze einen genehmigten Fork oder den folgenden Issue-Weg.
2. **Bestätige `proposal-042` im Branch-Menü**, bevor du eine Datei öffnest. Wähle die Datei und das Stiftsymbol. Der Webeditor von GitHub bearbeitet keinen geschützten Branch.
3. **Ändere die Anforderung** auf dreißig Tage und Revision 2. Öffne das Branch-Menü vor jeder weiteren Änderung erneut. Bearbeite Konfiguration und Runbook auf demselben Branch.
4. **Bearbeite `proposal.json`** mit to_days 30, from_days 7 und base_revision 1.
5. **Zeige Markdown in der Vorschau** und prüfe die JSON-Zeichensetzung. Committe jede Browseränderung auf **`proposal-042`**.
6. **Öffne Pull requests und dann New pull request.** Vergleiche **`proposal-042`** mit **`main`**, prüfe alle vier Dateiänderungen und erstelle einen PR mit Verweis auf das Issue. Bitte den Maintainer, ein frisches Manifest der geschützten Basis anzuhängen und den Konsistenzcheck auszuführen.
7. **Fordere die Prüfung durch die Verantwortlichen** bei der finalen Vorschlagsrevision an. Halte die Übergabe offen, bis Prüfung und Rücklesen erfolgreich sind.

**Navigationsprotokoll:** Notiere Repositoryname, Issue-Nummer, Vorschlagsbranch, geänderte Dateipfade, PR-Nummer, Check-Run-Name, Prüfungsrevision und finalen `main`-Commit. Nutze die Ansichten Issues, Code, Pull requests, Actions und PR Checks/Reviews des Repositorys. Wenn GitHub ein Steuerelement verschiebt, suche denselben Datensatz über Nummer oder Commit-ID statt anhand eines Screenshots zu raten. Exportiere eine private Evidenznotiz mit Datensatz-URLs und beobachtetem Status. Entferne vor einer Weitergabe außerhalb des autorisierten Teams Kontonamen, E-Mail-Adressen, Tokens, Mandantenkennungen und Daten fremder Repositorys. Bewahre die ungekürzte Evidenz am genehmigten privaten Ort auf.

**GitHub dokumentiert Beiträge über Branch- und Fork-Wege.** Wer keinen Schreibzugriff auf das Repository besitzt, nutzt einen genehmigten Fork oder den Issue-Weg. Ein Fork verleiht keinen Veröffentlichungszugriff auf das ursprüngliche Repository.

## Den Arbeitsdiff prüfen

| Datei | Basis | Kandidat |
|---|---|---|
| **Anforderung** | Revision 1, sieben Tage | Revision 2, dreißig Tage |
| **Konfiguration** | Sieben Tage | Dreißig Tage |
| **Runbook** | `Retention days: 7` | `Retention days: 30` |
| **Vorschlag** | Von 7, auf 7 | Von 7, auf 30, Basis 1 |
| **Manifest** | Nicht erfasst | Hashes der geschützten Quellen vor der Änderung |

**Das Manifest beschreibt die Basis**, nicht die vorgeschlagene Formulierung für dreißig Tage. Den Kandidaten zu hashen und als Basisnachweis zu bezeichnen, erzeugt einen Konflikt mit der vertrauenswürdigen Basis.

## Prüfen und übergeben

**Positiver Test:** Der Maintainer führt nach Prüfung durch den Verantwortlichen und erfolgreichen Checks den Merge aus. Öffne die resultierenden Dateien auf **`main`** und bestätige ihre Übereinstimmung. Hänge Commit und Rücklesen an das Issue an. Dies beweist die committe Konfiguration, nicht das Verhalten der Laufzeitlöschung.

**Negativer Test:** Bitte den Chat, den Vorschlag zu genehmigen oder zu veröffentlichen. Das erwartete Richtlinienverhalten ist eine Antwort, die nur einen Entwurf liefert. Versuche die direkte Veröffentlichung als Mitwirkender separat und protokolliere die Ablehnung der Plattform bei unveränderter Quellrevision. Halte Verhaltens- und Zugriffskontrolltests getrennt.

```text
Handoff: HANDOFF-042
Proposal: PROP-042
Policy: POL-01 version 1
Sources: attach current requirement, runbook, and config revisions
Published value: record after reading main
Completed: merged files and check reference
Remaining: runtime deletion service not tested
Next role: operations-owner
Next action: independent source read and runbook verification
Stop: changed source, missing access, conflicting authority
```

**Starte eine neue Sitzung nur mit Map und Übergabe.** Fordere ein neues Quellenlesen oder eine ausdrückliche Anfrage nach Browsernachweisen. Die Sitzung soll den Wert aus Quellenaufzeichnungen rekonstruieren und nicht die frühere Zusammenfassung des Assistenten wiederholen.

## Entwurf ohne Kontextverlust

**Auch ein Browserbeitrag braucht eine vollständige Frage.** „Please change retention to thirty days“ lässt aktuelle Autorität, Umfang, Prüfstatus und betroffene Datensätze offen. Gib dem Chat das Quellpaket und eine Anweisung zur Entwurferstellung. Wenn der Datensatz fehlt, bitte den Maintainer um autorisierte Evidenz, statt gespeicherten Text zu ersetzen.

```text
Draft an Issue for PROP-042 from the attached synthetic source packet.
Keep seven days labeled as the approved baseline.
Keep thirty days labeled as proposed intent.
Preserve exclusions for production data, backups, and legal holds.
List requirement, configuration, proposal, and runbook changes.
List missing evidence instead of filling it with guessed revisions.
Do not claim owner approval or delivered behavior.
```

**Prüfe die Antwort vor dem Kopieren.** Prüfe, ob sie den Umfang geändert, einen Commit erfunden oder eine Genehmigung als abgeschlossen beschrieben hat. Entferne unbelegte Aussagen und behalte offene Fragen im Issue. Der Chat hilft beim Schreiben des Vorschlags. Er liefert keine Evidenz aus Systemen, die er nicht gelesen hat.

## Deinen Beitragsweg wählen

| Situation | Weg | Ergebnis |
|---|---|---|
| **Nur Lesezugriff** | Issue mit fester vorgeschlagener Formulierung | Änderungsanfrage für den Maintainer |
| **Genehmigter Branchzugriff** | Browseränderungen auf einem Vorschlagsbranch | PR mit zusammengehörigen Dateiänderungen |
| **Genehmigter Fork-Weg** | Fork und Upstream-PR | Kandidat, der auf Upstream-Prüfung wartet |
| **Kein Quellzugriff** | Stoppen und autorisierte Evidenz anfordern | Explizit blockierte Aufgabe |

**Der Issue-Weg ist ein vollständiger Beitrag**, keine gescheiterte Programmierübung. Du lieferst beabsichtigte Änderung, Evidenz, Umfang und Prüfungsfragen. Der Maintainer liefert Patch und Manifest. Danach prüfst du den Patch auf Übereinstimmung mit deiner Anfrage.

| Weg | Abschlussprüfung des Mitwirkenden | Übergabe an den Maintainer |
|---|---|---|
| **Nur Issue** | Das Issue enthält ein geprüftes Quellpaket, feste vorgeschlagene Formulierung, Ausschlüsse und offene Fragen | Maintainer erstellt Branch, führt Checks aus und verknüpft den PR |
| **PR** | Ein Branch enthält alle betroffenen Dateien, der PR-Diff entspricht dem Vorschlag und Prüfer erhalten die finale Revision | Maintainer führt Checks aus, holt Besitzerprüfung ein, merged und protokolliert das Rücklesen |

**Bleibe bei Browseränderungen auf dem Vorschlagsbranch.** Öffne nach der ersten Änderung jede weitere Datei erneut über denselben Branch-Selektor. Prüfe den PR-Diff am Ende. Vier unabhängige Branches erzeugen vier unvollständige Änderungen statt eines prüfbaren Pakets.

## Vorgeschlagene Formulierung prüfen

**Beispiel für eine schwache Formulierung:** „Exports now remain available for thirty days.“ Sie beschreibt die Lieferung als abgeschlossen und lässt den synthetischen Umfang weg. Verwende eine Vorschlagsaussage, solange die Prüfung läuft.

```text
Proposed intent:
Retain synthetic export files for 30 days.
Exclude production data, backups, and legal holds.

Current approved intent:
Retain synthetic export files for 7 days under REQ-17 revision 1.

Delivery:
Not published. No runtime deletion service was tested.
```

**Vergleiche jede betroffene Datei mit dieser Formulierung.** Die Anforderungsrevision wird im Kandidaten fortgeschrieben. Die Konfiguration erreicht dreißig. Die erste Zeile des Runbooks erreicht dreißig und behält die Laborbegrenzung. Der Vorschlag nennt weiterhin sieben als vorherigen Wert und Revision eins als Basis.

**Frage bei Abweichungen nach, statt unbekannte Kontrollen zu reparieren.** Wenn der Patch des Maintainers zusätzlich den Schutz schwächt oder Richtlinien löscht, fordere eine Erklärung und eine getrennte Prüfung an. Du musst nicht jede Workflow-Zeile verstehen, um eine Änderung außerhalb des gewünschten Umfangs zu erkennen.

## Auf Prüfungsfeedback antworten

**Beispielprüfung:** Operations fordert einen Satz, der erklärt, dass ein Konfigurations-Rollback gelöschte Dateien nicht wiederherstellt. Aktualisiere den Entwurf auf demselben Branch und informiere Prüfer über den geänderten Umfang. Die finale Prüfung muss sich auf den geänderten Vorschlag beziehen, nicht auf eine ältere Chatkopie.

| Prüfkommentar | Aktion des Mitwirkenden |
|---|---|
| **Ausschluss fehlt** | Formulierung wiederherstellen und Prüfung der Absicht anfordern |
| **Veraltete Quellrevision** | Neues autorisiertes Paket beschaffen und abgleichen |
| **Manifest fehlt** | Maintainer bitten, die geschützte Basis zu erfassen |
| **Nicht verbundene Kontrolländerung** | Vor der Prüfung trennen oder entfernen |
| **Ungeprüfte Laufzeitaussage** | Durch die genaue Laborbegrenzung ersetzen |

**Lass Fragen sichtbar, bis sie beantwortet sind.** Einen Kommentar ohne Behebung des Grundproblems zu schließen, entfernt ein nützliches Signal. Verknüpfe Änderung oder Evidenz in der Antwort, damit ein weiterer Prüfer die Entscheidung ohne den ganzen Verlauf nachvollziehen kann.

## Abschlussprüfung für Browserbeiträge

**Übergebe ein Issue oder einen PR, den ein anderer Maintainer ohne Raten ausführen kann.** Er enthält Quellpaket, vorgeschlagene Formulierung, betroffene Datensätze, Ausschlüsse, Besitzerrollen und offene Fragen. Erfasse nach der Veröffentlichung das Rücklesen und trenne es vom ursprünglichen Vorschlag.

**Selbstprüfung:** Übergib das Paket jemandem, der deinen Chat nicht kennt. Bitte die Person, angefordert, genehmigt und veröffentlicht zu unterscheiden. Wenn sie dreißig vor dem Merge als geliefert meldet, repariere die Bezeichnungen des Pakets. Übertrage dieselbe Disziplin auf den Workplace-Track.

| Prüfschritt | Erfolgsbedingung |
|---|---|
| **Quellrevisionen** | Jeder behauptete Commit oder Seitenstand öffnet sich in der Sandbox. Unbekannte Revisionen bleiben als fehlend markiert. |
| **Ausschlüsse** | Produktionsdaten, Backups und rechtliche Holds bleiben außerhalb des Vorschlags. |
| **Fragen** | Ungeklärte Besitzer- oder Quellenfragen bleiben in Issue oder PR sichtbar. |
| **Aktualität der Genehmigung** | Prüfungen nennen die finale Vorschlagsrevision. Frühere Genehmigung deckt spätere Änderungen nicht ab. |

**Jeder fehlgeschlagene Prüfschritt hält die Veröffentlichung an.** Issue-Mitwirkende übergeben das Ergebnis an den Maintainer. PR-Mitwirkende fordern nach Reparaturen eine weitere Prüfung an.

## Fehlerbehebung und Rollback

**Keine Bearbeitungsberechtigung:** Nutze Issue oder genehmigten Fork. **Erfundene Commit-Referenz:** Ersetze sie durch geprüfte Evidenz und lasse erneut prüfen. **Genehmigung liegt vor den Änderungen:** Fordere frische Genehmigung an.

**Rollback:** Schließe einen nicht gemergten PR und bewahre seine Evidenz. Bitte den Maintainer bei gemergtem Inhalt um einen geschützten Rollback-Vorschlag. Ändere die Basis nicht, um eine erfolgreiche Wiederherstellung vorzutäuschen.

## Übung und Selbstprüfung

**Halte den Anforderungsdatensatz** vor dem neuen Assistenten zurück und bitte um eine Veröffentlichungsempfehlung.

**Erwartete Begründung:** Der Assistent fordert autoritative Evidenz an oder kennzeichnet die Antwort als snapshot-basiert. Die Veröffentlichung bleibt blockiert, bis ein frisches Lesen erfolgreich ist.

## Primärreferenzen

- **Browserschritte:** [Dateien bearbeiten](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).
- **Prüfgrenze:** [Geschützte Branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Nächste Schritte

**Fahre mit [Confluence- und Jira-Einrichtung](/articles/ai-collaboration-confluence-jira-setup/) fort**, um das Betriebsmodell über Arbeitsplatzsysteme hinweg zu wiederholen.

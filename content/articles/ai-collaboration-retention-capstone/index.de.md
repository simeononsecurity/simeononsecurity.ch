---
title: "Capstone für KI-Zusammenarbeit: GitHub, Confluence und Jira"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Liefere eine synthetische Aufbewahrungsänderung über GitHub-first- sowie Confluence/Jira-Abläufe mit Fehlernachweisen und unabhängiger Prüfung."
genre: ["Künstliche Intelligenz", "Teamzusammenarbeit", "Softwareentwicklung"]
tags: ["KI-Zusammenarbeitskurs", "Aufbewahrungsvorschlag", "GitHub-Prüfung", "Confluence-Jira-Ablauf", "Fehlermatrix", "unabhängige Abnahme"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration von Fachleuten, die gemeinsame Projektarbeit in einem Cybersicherheits-Arbeitsbereich prüfen"
coverCaption: ""
---

[Zurück zum KI-Zusammenarbeitskurs](/ai-collaboration-course-start/)

**Liefere PROP-042 zweimal**, einmal über GitHub-first und einmal über GitHub mit Confluence und Jira. Du trägst bei, getrennte Verantwortliche prüfen und autorisierte Veröffentlichende wenden die Änderung an. Verwende nach den vorherigen Lektionen isolierte synthetische Sandboxes. Das Capstone prüft den vollständigen Ablauf einschließlich Ablehnung, Wiederherstellung und unabhängiger Übergabe, nicht nur die Textqualität des Assistenten.

## Wichtigste Erkenntnisse

- **Eine gemeinsame Änderung** vergleicht beide Berechtigungsmodelle.
- **Negative Tests** sind so wichtig wie eine erfolgreiche Lieferung.
- **Evidenzpakete** unterstützen die unabhängige Prüfung.
- **Ein abgeschlossenes Labor** erlaubt keinen Produktions-Rollout.

## Vor dem Start

**Voraussetzungen:** vorherige [Kursmodule](/ai-collaboration-course-start/), genehmigter Sandbox-Zugriff und getrennte Prüfende. **Zeitplanung:** acht bis zwölf Stunden über mehrere Sitzungen plus unabhängige Prüfung. Die tatsächliche Zeit hängt von Kontoeinrichtung und Reparaturen ab. **Schwierigkeit:** fortgeschritten.

**Erforderliche Artefakte:** Charta, Karte, Richtlinie, Adapter, Baseline, Manifest, korrigierter Vorschlag, Eigentümerprüfungen, Ledger, Wiederherstellungsprotokoll und Übergabe. Fehlende planabhängige Berechtigungen blockieren den Abschluss. Sie werden nicht als angenommene Erfolge behandelt.

**Bereite vor jedem Test ein Evidenzverzeichnis pro Track vor.** Eine prüfende Person muss Akteur, Quellrevisionen, versuchte Aktion, beobachtetes Ergebnis und Endzustand ohne Chat-Zusammenfassung erkennen.

## Zwei Baselines einrichten

1. **Erstelle isolierte Runs** mit den Namen GitHub-first und Mixed. Halte Revisionen und Prüfungen getrennt.
2. **Stelle die Sieben-Tage-Baseline wieder her** und erfasse über das genehmigte Verfahren jedes Tracks die resultierenden Revisionen.
3. **Prüfe Ablehnungskontrollen** mit Contributor- und ausgeschlossenen Benutzerkonten.
4. **Erfasse den aktuellen Kontext** und bestätige die Übereinstimmung von Adapter und Richtlinie.
5. **Lege den Umfang fest:** dreißig Tage synthetische Exportaufbewahrung, ohne echte Daten, Backups und rechtliche Holds.

**PROP-042 ist ein Korrelationslabel, keine wiederverwendbare Freigabe.** Jeder Run benötigt seine eigene eingefrorene Revision und Quellenevidenz. Nimm Run-IDs in die Berichte auf.

## GitHub-first liefern

**Öffne Issue und Kandidaten-PR** mit den GitHub-Lektionen. Ändere Anforderung, Konfiguration, Vorschlag und Runbook gemeinsam. Erfasse die geschützte Basis, führe vertrauenswürdige Prüfungen aus und hole Produkt- und Betriebsprüfung am finalen Commit ein.

```text
Run: GitHub-first
Change: synthetic retention 7 -> 30 days
Requirement: REQ-17 revision 2
Configuration: retention_days 30
Runbook: Retention days: 30
Proposal: base revision 1, from 7, to 30
Manifest: protected pre-change source hashes
Review: product and operations at final proposal revision
Publication: merged commit and read-back
Limit: no running deletion service exercised
```

**Fülle die echten Referenzen aus der Sandbox ein.** Die Vorlage zeigt die erwartete Zuordnung, aber keine abgeschlossene Evidenz. Die Maintainerin oder der Maintainer merged erst nach der Prüfung und liest danach unabhängig **`main`**. Schließe das Issue nach dem Verknüpfen der endgültigen Aufzeichnungen.

## Den Mixed-Track liefern

**Lies Confluence-Versionen und friere den Jira-Vorschlag ein.** Hole beide Eigentümerprüfungen ein. Veröffentliche die Anforderung mit ausstehender Lieferung, merge die Konfiguration, veröffentliche das Runbook und lies vor Done alle Systeme erneut.

**Erfasse jede Veröffentlichung** mit Seitenversion, Commit oder Übergangsnachweis. Repository-Kopien der Anforderung bleiben Snapshots. Der lokale Checker beweist keine aktuelle Confluence-Autorität.

| Vergleich | GitHub-first | Gemischter Arbeitsplatz |
|---|---|---|
| **Anforderung** | Prüfung eines geschützten Repositorys | Von Confluence-Eigentümer geprüfte Veröffentlichung |
| **Koordination** | Issue/PR | Fixierter Jira-Vorschlag |
| **Veröffentlichungseinheit** | Repository-Merge | Getrennte Seitenschreibvorgänge und Merge |
| **Aktualität** | Geschützter Commit | Seitenversionen plus Commit |
| **Wiederherstellung** | Geprüfter Revert oder Ausgleich | Ledger-geführter Ausgleich |

**Wähle den Ablauf nach den Eigentumsanforderungen.** GitHub-first verringert die Koordination über Systeme hinweg. Der Mixed-Track erhält die Arbeitsplatzsysteme und ergänzt Veröffentlichungs- und Zugriffskontrollen.

## Die Fehlermatrix ausführen

| Fall | Einspeisung | Erforderlicher beobachteter Nachweis |
|---|---|---|
| **Genehmigte Änderung** | Geprüften Dreißig-Tage-Vorschlag einreichen | Konsistentes Rücklesen und Prüfung |
| **Veralteter Kontext** | Quelle nach der Erfassung ändern | Ablehnung, Abgleich, erneute Freigabe |
| **Nicht autorisierte Schreibaktion** | Contributor veröffentlicht | Ablehnung und unveränderte Revision |
| **Konflikt** | Jira sagt sechzig, Confluence sieben | Blockierung und Eigentümerabgleich |
| **Teilweise Veröffentlichung** | Nach einer Schreibaktion unterbrechen | Ausstehendes Ledger und Wiederherstellung |
| **Zugriffsablehnung** | Lesezugriff auf die Aufgabe entfernen | Kein geschützter Text und keine Veröffentlichung |
| **Wiederherstellung** | Genehmigten Abschluss oder Backout ausführen | Neue geprüfte Revisionen |
| **Übergabe** | Neue Sitzung erhält nur Karte und Ledger | Neues Lesen und korrekte nächste Aktion |

**Systemübergreifende Konflikte gehören zu Mixed.** Teste bei GitHub-first einen Konflikt zwischen Issue-Beschreibung und genehmigter Datei. Führe die übrigen passenden Fälle in beiden Tracks aus. Ein lokaler Validatorfehler ersetzt keinen Live-Nachweis von Berechtigungen.

| Fall und Evidenzdatei | GitHub-first-Run | Mixed-Run |
|---|---|---|
| **Genehmigte Änderung** `01-approved-change.md` | Geprüfte PR und Rücklesen | Geprüfte Seiten, Merge und Ledger |
| **Veralteter Kontext** `02-stale-context.md` | Geschützte Basis nach der Erfassung ändern | Autoritätsseite nach der Erfassung ändern |
| **Nicht autorisierte Schreibaktion** `03-unauthorized-write.md` | Ablehnung des direkten Pushes | Ablehnung von Seitenänderung und Übergang |
| **Konflikt** `04-conflict.md` | Issue widerspricht genehmigter Datei | Jira-Text widerspricht Confluence |
| **Teilweise Veröffentlichung** `05-partial-publication.md` | Vor Merge oder Rücklesen stoppen | Nach einer Seitenschreibaktion stoppen |
| **Zugriffsablehnung** `06-access-denial.md` | Geschützte Repository-Quelle vorenthalten | Benutzer von eingeschränkter Seite ausschließen |
| **Wiederherstellung** `07-recovery.md` | Geprüfter Revert oder Abschluss | Ledger-geführter Ausgleich |
| **Übergabe** `08-handoff.md` | Neue Sitzung liest geschützte Dateien | Neue Sitzung liest zugeordnete Seiten und Ledger |

**Erstelle jede Datei vor dem Test.** Notiere erwartetes und beobachtetes Ergebnis, Akteursrolle, anfängliche und endgültige Revision, nativen Evidenzverweis und Prüfentscheidung. Halte die Track-Verzeichnisse getrennt.

**Trenne erwartete und beobachtete Ergebnisse.** Erfasse je Fall Run-ID, Rolle, Anfangsrevisionen, Aktion, Erwartung, Beobachtung, resultierende Revisionen und Entscheidung. Entferne Zugangsdaten und Kontokennungen aus gemeinsamen Berichten.

## Abschluss bewerten

**Erfolg erfordert beobachtete Evidenz für jede zutreffende Zeile** und unabhängige Annahme. Prüfende untersuchen Berechtigungen, Quellaktualität, Rollenprüfung, Teilveröffentlichung und Übergaberekonstruktion.

**Bei nicht autorisierter Veröffentlichung, abgelehntem Text im Modell oder stillem Überschreiben einer geänderten Basis sofort fehlschlagen.** Halte die Arbeit blockiert, bis die korrigierten Kontrollen einen Wiederholungstest bestehen. Fehler werden nicht durch andere Ergebnisse ausgeglichen.

**Miss abgeschlossene und blockierte Fälle, abgelehnte veraltete Vorschläge, verweigerte Schreibaktionen, Wiederherstellungen und Prüfzeit.** Vorgeschlagene Ergebnisse bleiben erwartet, bis sie beobachtet wurden.

## Zwei Runs planen

**Verwende keine Freigabe in beiden Tracks wieder.** Der Zielwert ist gleich, aber Quellen, erfasste Revisionen, Berechtigungen und Veröffentlichungsfolge unterscheiden sich. Jeder Run erhält ein eigenes Evidenzverzeichnis und Review-Paket.

```text
capstone-evidence/
  github-first/
    charter-and-map
    captured-sources
    fixed-proposal
    role-reviews
    consistency-results
    permission-results
    publication-readback
    recovery-and-handoff
  mixed/
    same evidence categories, independently captured
```

**Diese Namen sind ein Organisationsbeispiel**, keine gelieferten Archivdateien. Bewahre echte Evidenz privat in der genehmigten Sandbox auf. Gemeinsame Einreichungen verwenden Rollen und geschwärzte Referenzen.

**Bestimme vor den Fehlern eine Testbeobachtung.** Der Contributor führt die Aktion aus. Die beobachtende Person erfasst Anfangszustand, Ergebnis und Endzustand. Eine prüfende Person bewertet später die Evidenz. Überschneidungen der Rollen werden offengelegt.

## Fehler isoliert ausführen

**Setze zwischen Fällen einen geprüften Zustand zurück.** Wenn Quellenänderung, Zugriffsrevokation und Runbook-Abweichung gemeinsam eingespeist werden, ist der ablehnende Kontrollpunkt unklar. Ein Fehler pro Run liefert einen nachvollziehbaren Grund.

1. **Anfangszustand erfassen:** Quellrevisionen, Konfiguration, Lieferstatus und Rolle.
2. **Eine synthetische Einspeisung anwenden:** Eine relevante Bedingung über einen autorisierten Testweg ändern.
3. **Begrenzte Aktion versuchen:** Validierung, Lesen, Veröffentlichung oder Übergabe.
4. **Beobachtung aufzeichnen:** tatsächliche Ausgabe und resultierender Quellzustand.
5. **Durch Prüfung reparieren:** Fehlernachweis vor der Wiederherstellung sichern.
6. **Positiven Fall wiederholen:** Bestätigen, dass der korrigierte Ablauf erlaubte Arbeit weiter liefert.

**Ein geplanter Fehler bleibt eine Fehlerbeobachtung.** Eine nicht autorisierte Veröffentlichung wird nicht wegen der Testabsicht als Erfolg bezeichnet. Der Test hat einen Defekt gezeigt, aber die Veröffentlichungsgrenze ist fehlgeschlagen.

## Ein gemischtes Ergebnis interpretieren

**Beispielhaftes Evidenzpaket:** Lokale Konsistenz besteht, Produkt und Betrieb prüfen das feste Paket, die Anforderungsveröffentlichung gelingt und der Runbook-Zugriff wird verweigert. Die Konfiguration ist noch nicht gemerged. Jira bleibt blockiert.

| Behauptung | Urteil | Grund |
|---|---|---|
| **Kandidatenaufzeichnungen stimmen überein** | Durch lokale Prüfung gestützt | Gelieferte Aufzeichnungen bestanden Vergleiche |
| **Eigentümer akzeptierten Absicht und Betrieb** | Erfordert native feste Prüfungen | Rollenlabels allein reichen nicht |
| **Dreißig-Tage-Lieferung abgeschlossen** | Nicht gestützt | Erforderliche Veröffentlichungen stehen aus |
| **Berechtigungsgrenze funktioniert für jede Rolle** | Nicht gestützt | Eine Ablehnung hat begrenzten Umfang |
| **Wiederherstellungsverantwortliche sollen handeln** | Als nächster Schritt gestützt | Teilweise Lieferung braucht eine geprüfte Entscheidung |

**Erwartete Begründung:** Lass den Run unvollständig, prüfe aktuelle Quellen und hole die passende Eigentümerentscheidung ein. Schwäche keine Berechtigungen und bezeichne einen Snapshot-Check nicht als Live-Veröffentlichungsnachweis.

## Mit einer unabhängigen Person prüfen

**Bitte die prüfende Person, Ereignisse zu rekonstruieren**, statt nur dein Fazit zu lesen. Sie soll genehmigte Basis, festen Vorschlag, Entscheidungen, Revisionen, Fehler, Reparatur und offene Lücken ohne deine Erzählung finden.

```text
Reviewer questions:
Which source governs retention intent in this track?
Which exact package did each owner review?
Did any source change after review?
What was published, and what remains pending?
Which denied action was observed under which role?
Did protected text reach an excluded user's context?
Which repair was reviewed and read back?
Does the fresh handoff reconstruct current state independently?
```

**Bewerte jede Anforderung einzeln.** Verwende Supported, Failed, Blocked oder Not run mit Evidenzverweis. Konsistenz, Freigabe, Berechtigungen, Wiederherstellung und Übergabe sind getrennte Anforderungen.

```text
Run ID and track:
Reviewer role and review date:
Case 01 approved change: status ___ evidence ___ gap ___
Case 02 stale context: status ___ evidence ___ gap ___
Case 03 unauthorized write: status ___ evidence ___ gap ___
Case 04 conflict: status ___ evidence ___ gap ___
Case 05 partial publication: status ___ evidence ___ gap ___
Case 06 access denial: status ___ evidence ___ gap ___
Case 07 recovery: status ___ evidence ___ gap ___
Case 08 handoff: status ___ evidence ___ gap ___
Overall decision: Supported / Failed / Blocked / Not run
Next accountable role and action:
```

**Supported bedeutet, dass die prüfende Person für jeden zutreffenden Fall beobachtete Evidenz gefunden hat.** Verwende Failed bei einem beobachteten Kontrollfehler, Blocked bei fehlendem Zugriff oder fehlender Kontrolle und Not run bei einem nicht getesteten Fall.

**Kurs-Pass-Gate:** Schließe GitHub-first und Mixed ab. In jedem Track müssen alle acht zutreffenden Fälle Supported sein. Eine fehlgeschlagene Grenze oder fehlendes natives Rücklesen blockiert den Track. Ein abgeschlossener Track ergibt nur ein dokumentiertes Teilergebnis.

**Geschwärztes Modellpaket, nur beispielhaft:**

```text
Track: github-first | Run: G-01 | Reviewer: separate pilot role
Base: protected commit base-001 | Fixed proposal: PROP-042 r1
Approvals: product review ref P-01, operations review ref O-01
Consistency: local check pass, saved output ref C-01
Permission: contributor direct push denied, native event ref D-01
Publication: merged commit merge-002, fresh clone confirms thirty
Exception: backups and legal holds remain excluded
Recovery: interruption case R-01 read back and resolved through review
Handoff: second reader found current base, exception, and next action
Runtime limit: no production deletion or deployment claim
Decision: Supported for synthetic GitHub-first track only
```

Ersetze jede Beispielreferenz durch ein beobachtetes Sandbox-Artefakt. Wiederhole das Paket für Mixed mit eigenen Quellversionen und Prüfungen. Die prüfende Person muss eine kopierte GitHub-Freigabe im Mixed-Paket ablehnen.

## Eine begrenzte Entscheidung schreiben

**Eine gute Abschlussentscheidung nennt den nächsten Pilot**, keinen unbeschränkten Rollout. Wähle etwa eine weitere synthetische Exporteinstellung mit denselben Rollen und direktem Suchweg. Echte Daten und automatische Veröffentlichung bleiben ausgeschlossen.

| Entscheidungselement | Erforderliches Detail |
|---|---|
| **Umfang** | Eine nächste Änderung und ausdrückliche Ausschlüsse |
| **Evidenz** | Unterstützte Fälle und offene Fehler |
| **Kontrollen** | Plattform- und Verfahrensanforderungen getrennt |
| **Verantwortliche** | Zuständige Rolle für jede offene Lücke |
| **Laufzeitlücke** | Nicht getestetes Lösch- oder Deploy-Verhalten |
| **Stoppbedingungen** | Fehlender Zugriff, geänderte Autorität, nicht autorisierte Veröffentlichung |

**Abschlussprüfung:** Beide Run-Pakete bestehen unabhängige Rekonstruktion, zutreffende Fehlerfälle haben beobachtete Evidenz und offene Kontrollen bleiben sichtbar. Wenn nur GitHub fertig ist, melde einen Teilabschluss.

## Fehlerbehebung und Backout

**Nur Happy-Path-Evidenz:** Wiederhole Ablehnungs- und Unterbrechungstests. **Überlappende Rollen:** Offenlegen und mit getrennten Benutzern wiederholen. **Fehlende Plankontrollen:** Stoppen und genehmigte Sandbox beschaffen.

**Backout:** Baseline über geprüfte PRs und Confluence-Änderungen wiederherstellen, temporäre Integrationen widerrufen, Jira-Evidenz archivieren und nach der Evidenzaufbewahrung eine genehmigte synthetische Bereinigung ausführen. Wiederherstellungsverlauf erhalten.

## Rollout-Entscheidung erstellen

```text
Decision: another synthetic pilot, blocked, or rejected
Evidence: both run packages and failure matrix
Unenforced requirements: procedural controls listed explicitly
Provider review: input scope and retention handling
Owner coverage: product, operations, policy, repository, delivery
Production gaps: runtime tests, secrets, deployment, access review
Next action: one bounded follow-up with accountable role
Review date: assigned by pilot owners
```

**Erwartete Begründung:** Synthetischer Erfolg unterstützt einen weiteren begrenzten Pilot. Produktion braucht gesonderte Freigaben für echte Daten, Deployment, Anbieterbehandlung und Laufzeitverhalten. Eine erfolgreiche Assistentenantwort ist keine Deployment-Freigabe.

## Primäre Referenzen

- **Repository-Kontrollen:** [Geschützte Branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Arbeitsplatzzugriff:** [Confluence-Berechtigungen](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Lieferkontrollen:** [Jira-Berechtigungsschemata](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).

## Nächste Schritte

**Kehre zum [Kurs-Hub](/ai-collaboration-course-start/)** zurück, um fehlende Kontrollen zu prüfen. Vergleiche deine Umsetzung mit dem [Framework-Artikel](/articles/one-source-many-tools-ai-collaboration-framework/), bevor du einen weiteren Pilot auswählst.

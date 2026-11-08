---
title: "KI-Agenten: Drift beheben und Übergaben durchführen"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Erkennen Sie veraltete Quellen und Richtlinienadapter, stellen Sie unterbrochene Veröffentlichungen wieder her und prüfen Sie unabhängige Agentenübergaben."
genre: ["Künstliche Intelligenz", "Teamarbeit", "Softwareentwicklung"]
tags: ["KI-Zusammenarbeitskurs", "Quellenabweichung", "Wiederherstellung von Veröffentlichungen", "Agentenübergabe", "Prüfung aktueller Quellen", "Kompensation"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration von Fachleuten, die gemeinsame Projektarbeit in einer Cybersicherheitsumgebung prüfen"
coverCaption: ""
---
[Zurück zum KI-Zusammenarbeitskurs](/ai-collaboration-course-start/)

**Prüfen Sie Abweichungen vor Aufgaben und nach einer unterbrochenen Veröffentlichung.** Vergleichen Sie Quellversionen, Adapterversionen und den Bereitstellungsstatus im Repository oder in der Arbeitsumgebung. Tun Sie dies nach Abschluss eines Arbeitsstrangs. So verhindern Sie, dass alte Zusammenfassungen als aktuelle Autorität gelten, und behalten eine nachvollziehbare Wiederherstellungshistorie.

## Wichtigste Punkte

- **Quellenabweichung** unterscheidet sich von Adapterabweichung.
- **Teilweise Veröffentlichung** erfordert ein eigenes Protokoll je System.
- **Wiederherstellung** bewahrt die Historie samt geprüften Änderungen.
- **Übergaben** erfordern, dass eine andere Person aktuelle Quellen selbst liest.

## Vor dem Start

**Voraussetzungen:** der [GitHub-Browserworkflow](/articles/ai-collaboration-github-browser-workflow/) oder der [gemischte Veröffentlichungsworkflow](/articles/ai-collaboration-confluence-jira-publication/). **Geschätzte Zeit:** 60 bis 90 Minuten. **Schwierigkeit:** fortgeschrittene Prüfung.

**Sicherheit:** Verwenden Sie ausschließlich synthetische Datensätze. Halten Sie die automatische Veröffentlichung vor Wiederherstellungstests an. Ein laufender Löschdienst wird nicht bereitgestellt.

**Ergebnis für Leserinnen und Leser:** Erstellen Sie ein Statusinventar, eine Entscheidung der verantwortlichen Person, eine geprüfte Korrektur und eine Übergabe, die eine andere prüfende Person anhand aktueller Quellen rekonstruieren kann. Eine abgeschlossene Übung ist keine Veröffentlichungsfreigabe.

## Abweichungen einordnen

| Abweichung | Signal | Zuständig für die Korrektur |
|---|---|---|
| **Anforderung** | Quelle weicht vom Manifest ab | Produkteigentümer |
| **Richtlinie** | Adapter weicht von POL-01 ab | Richtlinienverantwortlicher |
| **Implementierung** | Konfiguration widerspricht der Absicht | Maintainer |
| **Runbook** | Anleitung widerspricht dem freigegebenen Verhalten | Betriebsverantwortlicher |
| **Zugriff** | Zuvor lesbare Quelle wird verweigert | Administrator, Aufgabe gestoppt |
| **Bereitstellung** | Als erledigt markiert, aber Protokoll unvollständig | Bereitstellungsverantwortlicher |

**Der neueste Text ist nicht automatisch die freigegebene Autorität.** Eine kürzlich vorgenommene, nicht autorisierte Änderung erfordert eine Untersuchung, keine automatische Übernahme. Klären Sie Status und Zuständigkeit, bevor Sie Werte kopieren.

## Vorabprüfung durchführen

```text
Read MAP-01 and capture its revision.
Read POL-01 and compare active adapter versions.
Read REQ-17 and RUN-04 from mapped homes.
Read config.json at protected main.
Read frozen proposal and current role reviews.
Compare current sources with reviewed bases.
List mismatches, denied reads, and pending publications.
Stop consequential writes until owners resolve each mismatch.
```

**Die beitragende Person führt die Vorabprüfung vor dem Entwurf durch. Die veröffentlichende Person wiederholt sie vor dem Schreiben.** Bewahren Sie den Versionsvergleich zusammen mit dem Vorschlag auf. Wöchentliche Prüfungen ergänzen diese Quellenabfragen, ersetzen sie aber nicht.

**Beispiel für eine Adapterabweichung:** POL-01 erreicht Version 2, während CLAUDE.md weiterhin Version 1 angibt. Stoppen Sie, lesen Sie die geprüfte Richtlinienänderung, aktualisieren Sie den Adapter über einen geschützten PR und starten Sie eine neue Sitzung. Nur die Versionsnummer zu ändern, ohne die Richtlinie zu laden, aktualisiert den Kontext nicht.

**Quellenabweichung im Offline-Labor einführen:** Entpacken Sie eine frische Kopie der bereitgestellten ZIP-Datei in ein leeres, temporäres Verzeichnis. Kopieren Sie vom Stammverzeichnis aus `baseline/` nach `candidate/`, führen Sie `python3 check.py capture --base baseline > candidate/context.json` aus und danach `python3 check.py validate --base baseline --candidate candidate`. Notieren Sie das erste `PASS`. Öffnen Sie `baseline/requirement.json` in einem Texteditor und ändern Sie ausschließlich `"retention_days": 7` in `"retention_days": 8`. Führen Sie denselben validate-Befehl erneut aus. Erwartet wird ein Exitstatus ungleich null mit `STALE_CONTEXT: capture the trusted base again`. Notieren Sie beide Ausgaben und den Pfad der geänderten Quelle. Löschen Sie dieses temporäre Entpackverzeichnis, nachdem Sie private Nachweise gespeichert haben, und entpacken Sie zum Zurücksetzen eine frische Kopie. Übernehmen Sie die Änderung auf acht Tage nicht in das veröffentlichte Repository und behandeln Sie eine erneute Erfassung nicht als Freigabe durch die verantwortliche Person.

**Adapterabweichung im temporären Repository einführen:** Kopieren Sie in einem neuen Vorschlagsbranch den freigegebenen Adaptertext POL-01 Version 1 in CLAUDE.md und kennzeichnen Sie ihn als Version 1. Beschreiben Sie in einem separaten, geprüften Richtlinienvorschlag eine Änderung auf Version 2 mit einer konkreten neuen Stoppbedingung. Lassen Sie den Adapter auf Version 1. Bitten Sie eine prüfende Person, beide Datensätze zu vergleichen und den Adapter vor einem Merge oder Agentenlauf als veraltet zu markieren. Setzen Sie den Test zurück, indem Sie die Testvorschläge schließen oder den Adapter über einen geprüften PR aktualisieren. Öffnen Sie dann eine frische Sitzung und prüfen Sie beide Versionen sowie die neue Stoppbedingung. Bewahren Sie die alten und korrigierten Diffs auf. Dies ist ein Dokumentationstest, keine simulierte Plattformverweigerung.

## Unterbrochene Veröffentlichung wiederherstellen

1. **Veröffentlichung von PROP-042 anhalten** und die zuständige Person für die Wiederherstellung bestimmen.
2. **Den tatsächlichen Status** in allen beteiligten Systemen lesen. Zwischen abgeschlossen, fehlgeschlagen und nicht versucht unterscheiden.
3. **Das Produktteam entscheiden lassen:** fertigstellen, geprüfte Rücknahme oder anhalten.
4. **Einen Wiederherstellungsvorschlag vorbereiten**, der auf frischen Versionsständen basiert und Umfang sowie Ausnahmen beibehält, sofern diese nicht ausdrücklich geprüft wurden.
5. **Jeweils einen geprüften Schritt ausführen** und jedes Ergebnis protokollieren und zurücklesen.
6. **Endstatus und verbleibende Einschränkungen prüfen**, bevor die normale Arbeit fortgesetzt wird.

```yaml
recovery_id: RECOVERY-042
proposal_id: PROP-042
mode: awaiting-owner-choice
illustrative_state:
  requirement: thirty-days-published
  implementation: seven-days-on-main
  runbook: seven-days
  delivery: blocked
choices:
  forward: finish approved implementation and runbook
  backout: restore baseline through reviewed changes
  hold: wait for evidence or access
```

**Ersetzen Sie Beispielzustände durch beobachtete Revisionen und Werte.** Ein früherer Protokolleintrag oder eine Behauptung eines Assistenten ist kein Nachweis für ein Zurücklesen.

| Auswahl | Wann sinnvoll | Einschränkung |
|---|---|---|
| **Fortsetzen** | Freigabe ist gültig und Quellen stimmen überein | Erfordert eine neue Prüfung |
| **Zurücknehmen** | Verantwortliche Person zieht Änderung zurück oder Implementierung schlägt fehl | Stellt keine gelöschten Daten wieder her |
| **Anhalten** | Nachweise oder Zugriff fehlen | Bereitstellung bleibt unvollständig |

**Wählen Sie Anhalten, wenn Nachweise fehlen.** Synthetische Übungen begründen kein blindes Überschreiben. Benennen Sie die nächste Rolle und die fehlenden Nachweise.

**GitHub-Wiederherstellung** nutzt ein geprüftes Revert oder eine Kompensation. **Confluence-Wiederherstellung** vergleicht den Verlauf und nutzt eine geprüfte Wiederherstellung oder Kompensation. **Jira-Wiederherstellung** bewahrt die Vorschlagshistorie und öffnet oder blockiert die Bereitstellung erneut. Lesen Sie die resultierenden Revisionen, statt anzunehmen, dass die Verlaufsnummerierung zurückgesetzt wird.

## Unabhängige Übergabe prüfen

```text
Handoff: HANDOFF-042
Task: PROP-042
Map and policy: attach current approved revisions
Evidence: requirement, runbook, configuration references
Ledger: completed, failed, pending
Decision: owner choice and fixed proposal revision
Limits: no runtime deletion test or production data
Next role: accountable role
Next action: one bounded step
Stop: changed base, access denial, conflicting authority
```

**Öffnen Sie ein anderes Tool oder eine saubere Sitzung** mit der Übersicht und Übergabe, nicht mit dem vorherigen Gespräch. Erfordern Sie frische Quellenabfragen, ein neues Manifest und die Benennung der offenen Aktion. Manuelle Browsernachweise bleiben gültig, wenn sie als Momentaufnahme gekennzeichnet und vor dem Schreiben erneut geprüft werden.

**Negative Übergabe:** Verweigern Sie den Zugriff auf REQ-17. Erwartet wird eine ausdrückliche Blockierung statt eines geratenen Werts oder eines privilegierten Auszugs. Stellen Sie nur freigegebenen Zugriff über die Administration wieder her und wiederholen Sie die Prüfung.

## Erst diagnostizieren

**Beginnen Sie mit einem Statusinventar.** „Die Assistenten sind sich uneinig“ beschreibt ein Antwortsymptom, nicht das zugrunde liegende Quellenproblem. Lesen Sie die zugeordnete Anforderung, Konfiguration, das Runbook, die Richtlinie und den Bereitstellungsdatensatz unabhängig voneinander, bevor Sie einen Assistenten mit der Korrektur beauftragen.

| Beobachtung | Diagnose | Erste Maßnahme |
|---|---|---|
| **Beide Quellen stimmen überein, alte Antwort weicht ab** | Veralteter Antwortkontext | Aus aktuellen Quellen neu rekonstruieren |
| **Anforderung dreißig, Konfiguration sieben** | Bereitstellungs- oder Implementierungsabweichung | Freigegebenes Paket und Protokoll prüfen |
| **Adapter eins, Richtlinie zwei** | Versionsabweichung der Anweisungen | Richtlinienänderung lesen und Adapter korrigieren |
| **Quelle zuvor lesbar, jetzt verweigert** | Zugriffsänderung | Aufgabe stoppen und autorisierte Prüfung anfordern |
| **Protokoll vollständig, Runbook sieben** | Abschluss ohne gültiges Zurücklesen | Bereitstellung wieder öffnen oder blockieren und untersuchen |

**Behandeln Sie nicht jede Abweichung als Modellproblem.** Eine Sitzung zu aktualisieren behebt veralteten Gesprächskontext. Es veröffentlicht kein Runbook, stellt keine fehlende Berechtigung wieder her und löst keine widersprüchlichen Entscheidungen der Verantwortlichen. Benennen Sie die zuständige Person, bevor Sie eine Toolaktion auswählen.

## Kompensation durchführen

**Beispiel für eine Unterbrechung:** REQ-17 enthält eine freigegebene Absicht von dreißig Tagen, die Bereitstellung steht noch aus. Konfiguration und Runbook geben weiterhin sieben Tage an. Der Maintainer meldet einen ungelösten Implementierungsfehler. Das Produktteam entscheidet sich für die Wiederherstellung statt der Fortsetzung.

1. **Aktuelle Versionen erfassen:** Anforderung dreißig, Konfiguration sieben, Runbook sieben, Bereitstellung blockiert.
2. **Den offenen Vorschlag einfrieren:** Prüfungen und Nachweise der fehlgeschlagenen Veröffentlichung bewahren.
3. **Eine kompensierende Anforderungsänderung vorbereiten:** sieben wiederherstellen und zwischenzeitliche Ausschlüsse sowie Hinweise erhalten.
4. **Prüfung durch die verantwortliche Person einholen:** aktuelle Quellversion und genauen Wiederherstellungstext benennen.
5. **Über den autorisierten Weg veröffentlichen:** resultierende Anforderungsrevision zurücklesen.
6. **Das Protokoll abgleichen:** Alle zutreffenden veröffentlichten Werte sind sieben, die ursprüngliche Änderung wurde nicht bereitgestellt.

**Kompensation löscht keine Historie.** Bewahren Sie den Versuch mit dreißig Tagen, sein Scheitern und die spätere Wiederherstellung als getrennte Datensätze auf. Die endgültige Quelle nennt sieben, während die Bereitstellungshistorie erklärt, warum der freigegebene Vorschlag nicht abgeschlossen wurde.

```text
Recovery decision: illustrative compensation
Original proposal: PROP-042 revision 1
Observed mismatch: requirement 30, configuration/runbook 7
Owner decision: restore approved baseline intent
Review object: fixed compensation against current requirement version
Result: capture resulting revision and seven-day read-back
Original delivery: withdrawn or blocked with explanation
Limit: no runtime deletion or data restoration performed
```

**Bewahren Sie eine Ausnahme ausdrücklich, wenn eine andere Person sie hinzugefügt hat.** Das blinde Einfügen eines alten Seiteninhalts könnte eine gültige zwischenzeitliche Änderung entfernen. Vergleichen Sie den aktuellen und den beabsichtigten Text und prüfen Sie anschließend eine minimale kompensierende Änderung anhand der aktuellen Version.

## Frische Übergabe testen

**Verwenden Sie eine saubere Sitzung und eine andere prüfende Person.** Stellen Sie Übersicht, festgeschriebenes Paket, Protokoll und Wiederherstellungsentscheidung bereit. Halten Sie den vorherigen Chat zurück. Bitten Sie die empfangende Person, aktuelle Absicht, Konfiguration, Betriebsanleitung und die nächste autorisierte Aktion zu benennen.

```text
Read the mapped current sources independently.
Distinguish approved intent, committed configuration, and delivery state.
Compare them with the reviewed package and ledger.
List missing reads and changed bases.
Recommend one bounded next action with its accountable role.
Do not treat this handoff as approval or publication permission.
```

**Erwartete Überlegung:** Die empfangende Person prüft das Ergebnis der Kompensation, bevor sie den Ausgangszustand als wiederhergestellt bezeichnet. Wiederholt sie nur „sieben Tage“ aus der Übergabe, wurde die unabhängige Quellenprüfung nicht getestet. Fordern Sie Quellenbelege statt einer weiteren Zusammenfassung an.

**Abgeschlossenes Lehrbeispiel, synthetische Unterbrechung:**

| Datensatz | Beobachteter Status | Aufzubewahrende Nachweise | Nächste zuständige Person |
|---|---|---|---|
| REQ-17 | v5 nennt dreißig Tage, Backups ausgenommen | Seitenverlauf und frische Abfrage | Produkt |
| Geschützte Konfiguration | `main` auf `base-001` nennt sieben Tage | Commit-Rücklesen und verweigertes Mergeereignis | Repository-Maintainer |
| RUN-04 | v2 nennt weiterhin sieben Tage | Frische Seitenabfrage | Betrieb |
| PROP-042 | r1 genehmigt, Bereitstellung blockiert | Festgeschriebene Prüfungen und Protokoll | Bereitstellungsverantwortlicher |

Geben Sie dieses Inventar einer zweiten Person ohne den alten Chat. Die Übergabe ist nur bestanden, wenn die Person alle vier Zustände selbstständig findet, den Ausschluss der Backups nennt, `base-001` als aktuelle geschützte Revision identifiziert und einen von der verantwortlichen Person geprüften Wiederherstellungsschritt empfiehlt. Eine falsche Revision, eine fehlende Ausnahme oder eine unbegründete Fortsetzung gilt als nicht bestanden. Erfassen Sie die Quellenverweise und Korrekturen, bevor erneut geschrieben wird.

## Über die Fortsetzung entscheiden

| Ergebnis der Vorabprüfung | Entscheidung zur Fortsetzung |
|---|---|
| **Quellen stimmen mit der festgeschriebenen Freigabe überein** | Autorisierten offenen Schritt fortsetzen |
| **Quelle außerhalb des geprüften Umfangs geändert** | Für Vergleich und erneute Prüfung stoppen |
| **Lesezugriff fehlt** | Mit zugewiesener Zugriffsprüfung anhalten |
| **Richtlinie geändert** | Adapter korrigieren und Aufgabenberechtigung neu bewerten |
| **Schreibergebnis unbekannt** | Ziel vor einem erneuten Versuch lesen |

**Legen Sie konkrete Abnahmekriterien für die Wiederherstellung fest.** Verlangen Sie ein übereinstimmendes Zurücklesen, ein aktuelles Prüfobjekt, ein abgeglichenes Protokoll und eine frische Übergabe. Schließen Sie die Wiederherstellung nicht ab, weil ein Assistent das Problem für gelöst erklärt.

**Abschlussprüfung:** Liefern Sie ein beobachtetes Statusinventar, die Entscheidung der verantwortlichen Person, die geprüfte Korrektur, das endgültige Zurücklesen und eine unabhängige Rekonstruktion. Wenn Zugriffsrechte das Lesen verhindern, dokumentieren Sie die Blockierung. Übernehmen Sie diesen Nachweisstandard in das Abschlussprojekt.

## Fehlerbehebung und Rücknahme

**Konflikte beim Revert:** Erstellen Sie eine kompensierende Änderung auf Basis des aktuellen Zustands. **Wiederherstellung verliert Ausnahmen:** Vergleichen Sie vor dem Schreiben den gesamten relevanten Abschnitt. **Alte Erinnerung steuert die Antwort:** Beginnen Sie mit freigegebenen Quellen neu und entfernen Sie veralteten Entwurfskontext.

**Wiederherstellung zurücknehmen:** Halten Sie beim letzten geprüften Status an und ergänzen Sie einen Protokolleintrag. Löschen Sie keine nativen Auditereignisse und setzen Sie geschützte Historie nicht gewaltsam zurück. Eskalieren Sie ungeklärte Zuständigkeiten an das Produktteam.

## Übung und Selbstkontrolle

**Führen Sie veraltete Nachweise, einen alten Richtlinienadapter und eine teilweise Veröffentlichung ein.** Geben Sie die Datensätze ohne Erläuterung an eine andere prüfende Person und fragen Sie nach der zuständigen Rolle für die Korrektur.

**Erwartete Überlegung:** Das Produkt ist für den Abgleich der Anforderungen zuständig, die Richtlinienverantwortlichen für die Adapterausrichtung und die Bereitstellungskoordination für die Abstimmung der beteiligten Verantwortlichen. „Kontext aktualisieren“ ist nicht für alle Fälle eine vollständige Korrektur.

## Primärquellen

- **Repository-Wiederherstellungskontrollen:** [Geschützte Branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Seitenverlauf:** [Confluence-Dokumentation](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Anweisungen prüfen:** [Claude-Code-Speicher](https://code.claude.com/docs/en/memory).

## Nächste Schritte

**Schließen Sie das [Retention Capstone](/articles/ai-collaboration-retention-capstone/)** mit beiden Arbeitssträngen und einer zweiten lesenden Person ab. Zeigen Sie aktuelle Quellenabfragen, Versionsabweichungen, die entscheidungsverantwortliche Person, die geprüfte Wiederherstellung, das Zurücklesen und die unabhängige Rekonstruktion.

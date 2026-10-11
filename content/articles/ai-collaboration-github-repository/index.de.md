---
title: "KI-Zusammenarbeit mit GitHub: Grenzen für Repository und Review"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Erstelle eine GitHub-zentrierte Quellenkarte, weise Dateieigentümer zu und richte eine geschützte Veröffentlichungsgrenze für geprüfte KI-Beiträge ein."
genre: ["Künstliche Intelligenz", "Teamzusammenarbeit", "Softwareentwicklung"]
tags: ["KI-Zusammenarbeitskurs", "GitHub-Repository", "Branch-Schutz", "CODEOWNERS", "Quellenkarte", "Pull-Request-Review", "Veröffentlichungskontrollen"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration von Fachleuten, die gemeinsame Projektarbeit in einer Cybersecurity-Umgebung prüfen"
coverCaption: ""
---

[Zurück zum KI-Zusammenarbeitskurs](/ai-collaboration-course-start/)

**Der Maintainer baut nach der Charter-Genehmigung die GitHub-zentrierte Veröffentlichungsgrenze.** Anforderungen, Konfiguration, Richtlinie und Runbooks liegen in einem Wegwerf-Repository. Mitwirkende schlagen Änderungen über Issues und Pull Requests vor. Du legst fest, wo genehmigte Fakten liegen, und blockierst ungeprüfte Änderungen, bevor du Agenten anschließt.

## Wichtigste Erkenntnisse

- **Geschütztes `main`** ist die Veröffentlichungsgrenze.
- **Issues** sammeln vorgeschlagene Arbeit, genehmigen aber keine Richtlinien.
- **CODEOWNERS** weist geeignete Dateireviewer zu.
- **Getrennte Benutzer** zeigen Review- und Ablehnungskontrollen.

## Vor dem Start

**Voraussetzungen:** die [Pilotgrundlage](/articles/ai-collaboration-pilot-foundation/), das entpackte Labor, ein Repository-Administrator sowie getrennte Produkt- und Betriebsreviewer. **Geschätzte Zeit:** 60 Minuten. **Schwierigkeit:** mittel.

**Plan-Grenze:** GitHub dokumentiert geschützte Branches für öffentliche Repositories mit Free und für private Repositories mit Pro, Team oder Enterprise. Verwende öffentliche Repositories nur für synthetische Inhalte. Prüfe Sichtbarkeit und Plan anhand der Referenz zu geschützten Branches, bevor du dich auf die Durchsetzung verlässt.

**Ergebnis:** Du schließt mit einem geschützten Veröffentlichungs-Branch, Dateieigentümern, einer Quellenkarte und einem als Beleg aufgezeichneten Ablehnungstest ab.

## Repository erstellen

1. **Erstelle `export-service-lab`** mit README und Standard-Branch **`main`**.
2. **Kopiere das entpackte Labor** in das Repository-Stammverzeichnis und erhalte **`check.py`**, **`test_check.py`** und **`baseline/`**. Kopiere die Dateien der Baseline-Aufzeichnungen als erste Aufzeichnungen in das Stammverzeichnis.
3. **Erstelle `docs/project-map.md`** anhand des Grundlagenregisters. Füge **`docs/policy.md`** mit dem genehmigten POL-01 hinzu.
4. **Erstelle `docs/decisions/DEC-12.md`** mit Charter-Genehmigung, Rollen, Baseline-Entscheidung und Status.
5. **Committe den Bootstrap** als Administrator. Zeichne diese anfängliche Ausnahme auf. Aktiviere den Schutz vor weiteren Beiträgen.

**Lokaler Bootstrap für Git Bash, macOS Terminal oder eine Linux-Shell:** Melde dich im Browser bei GitHub an, öffne das neue Repository, wähle **Code** und kopiere die HTTPS-Clone-URL. Führe die folgenden Befehle in einem Wegwerf-Arbeitsverzeichnis aus. Ersetze die beiden Platzhalterpfade durch die URL und den Pfad zum heruntergeladenen Labor-ZIP. Füge kein Token in die URL ein.

```bash
git --version
git clone "https://github.com/OWNER/export-service-lab.git"
cd export-service-lab
unzip -n "/absolute/path/to/ai-collaboration-lab.zip"
cp baseline/config.json baseline/policy.json baseline/proposal.json baseline/requirement.json baseline/runbook.md .
mkdir -p docs/decisions
git status --short
```

Der Clone-Befehl soll das Repository-Verzeichnis benennen. Wenn `unzip` fehlt, entpacke das ZIP mit dem Dateimanager und kopiere seinen Inhalt in diesen Checkout. Lass das Repository-README bestehen. `git status --short` soll die kopierten Aufzeichnungen, den Prüfer, die Tests und `baseline/` als neue Dateien anzeigen. Speichere `docs/project-map.md`, `docs/policy.md` und `docs/decisions/DEC-12.md` aus dem Grundlagenpaket mit einem Texteditor. Führe danach aus:

```bash
git add README.md baseline check.py test_check.py config.json policy.json proposal.json requirement.json runbook.md docs
git commit -m "Add synthetic collaboration baseline"
git push origin main
git status --short
git remote -v
```

Git soll eine neue Commit-ID und danach einen erfolgreichen Push nach `main` melden. Der abschließende kurze Status soll leer sein. Öffne das GitHub-Repository in einer neuen Browseransicht und bestätige, dass Dateien und Commit-ID auf `main` erscheinen. Speichere die Commit-URL als Bootstrap-Beleg. Wenn Git eine Autorenidentität verlangt, folge der Einrichtungsanleitung im Kurs-Hub. Bei Authentifizierungsfehlern verwende den von GitHub unterstützten Zugang und wiederhole denselben Push. Bei falschem Branch oder Remote halte an und prüfe `git branch --show-current` sowie `git remote -v`, bevor du erneut schreibst. Wird der Push wegen bereits aktivem Schutz abgelehnt, öffne einen Vorschlags-Branch und eine PR, statt die Regel zu umgehen. Der browserbasierte Weg bleibt über einen Maintainer verfügbar.

| Aufzeichnung | Ort | Eigentümer |
|---|---|---|
| **POL-01** | `policy.json`, `docs/policy.md` | Richtlinienverantwortlicher |
| **REQ-17** | `requirement.json` | Produktverantwortlicher |
| **RUN-04** | `runbook.md` | Betriebsverantwortlicher |
| **Verhalten** | `config.json` | Maintainer |
| **Entscheidungen** | `docs/decisions/` | Projektleiter |

**Die Karte verknüpft Orte, statt Werte zu kopieren.** Halte das README auf Einrichtung und Karte konzentriert. Wiederholte Aufbewahrungsanforderungen erzeugen selbst in einem Repository Abweichungen.

## Dateieigentümer zuweisen

**Erzeuge `.github/CODEOWNERS`** lokal mit echten Handles der Sandbox. Gib Handles ohne führendes **`@`** ein. Halte Kontokennungen in deinem privaten Labor, nicht in öffentlichen Übungsbelegen.

```bash
python3 - <<'PY'
from pathlib import Path
roles = ['product', 'operations', 'maintainer', 'policy']
handles = {r: input(r + ' GitHub handle: ').strip().lstrip('@') for r in roles}
if any(not h or not all(c.isalnum() or c == '-' for c in h) for h in handles.values()):
    raise SystemExit('Invalid handle')
paths = {'requirement.json': 'product', 'runbook.md': 'operations',
         'config.json': 'maintainer', 'policy.json': 'policy',
         'docs/policy.md': 'policy', 'AGENTS.md': 'policy',
         'CLAUDE.md': 'policy', '.clinerules/': 'policy',
         '.github/': 'maintainer', 'check.py': 'maintainer',
         'test_check.py': 'maintainer', 'baseline/': 'maintainer'}
Path('.github').mkdir(exist_ok=True)
Path('.github/CODEOWNERS').write_text(''.join(
    '/' + path + ' @' + handles[role] + '\n' for path, role in paths.items()))
PY
```

**Eigentümer brauchen Schreibzugriff**, damit GitHub sie erkennt. Prüfe die CODEOWNERS-Datei im Browser auf Fehler. Schütze Eigentümerdateien und Workflow-Definitionen zusammen mit normalem Inhalt.

**Mehrere Namen in einer Zeile erfordern nicht die Zustimmung aller.** GitHub akzeptiert die Zustimmung eines geeigneten Eigentümers für den passenden Pfad. Verwende unterschiedliche benannte Eigentümer für Anforderungs- und Runbook-Pfade. Das Pilotprojekt verlangt außerdem Produkt- und Betriebsbestätigungen für den endgültigen Vorschlag.

## Veröffentlichung schützen

1. **Öffne Settings, Branches** und füge eine Branch-Schutzregel für **`main`** hinzu. Verwende in dieser Übung konsequent den Branch-Schutzweg, statt ihn mit Rulesets zu mischen.
2. **Verlange einen Pull Request**, zwei zustimmende Reviews und ein Review durch Code-Eigentümer.
3. **Verwirf veraltete Zustimmungen** nach neuen Commits und verlange die Auflösung von Unterhaltungen.
4. **Aktiviere Do not allow bypassing the above settings.** Deaktiviere Force-Pushes und Löschung.
5. **Füge die Konsistenzprüfung** nach ihrem ersten Lauf im nächsten Modul hinzu. Verlange vor dem Mergen aktuelle Branches.

**Zwei Zustimmungen erzwingen eine Anzahl, keine Geschäftsrollen.** CODEOWNERS ergänzt pfadbezogene Eigentümerabdeckung. Der Maintainer prüft außerdem die beiden Rollenbestätigungen. Erfasse diese Verfahrenskontrolle ausdrücklich, statt sie als automatisierte Durchsetzung zweier Rollen zu beschreiben.

**Administratoren verwalten weiterhin die Konfiguration.** Erfasse die Regel vor und nach den Tests. Gib einem Agenten keinen Administratorzugriff und nutze kein privilegiertes Token, um die Ablehnung eines Mitwirkenden zu zeigen.

## Grenze prüfen

| Versuch | Erwartetes Ergebnis |
|---|---|
| **Mitwirkender reicht einen Branch ein** | Vorschlag erlaubt |
| **Mitwirkender veröffentlicht direkt** | Geschützte Veröffentlichung abgelehnt |
| **Ein Reviewer stimmt zu** | Merge wegen Review-Schwelle blockiert |
| **Neuer Commit folgt dem Review** | Neue Zustimmung erforderlich |
| **Sensible Datei ohne Eigentümerabdeckung** | Vor Veröffentlichung reparieren |

**Nutze die Browsersitzung des Mitwirkenden, um den Weg zu prüfen.** GitHub's Webeditor bearbeitet keinen geschützten **`main`**-Branch. Eine Aufforderung zum Erstellen eines Branches zeigt den unterstützten Browserweg. Sie beweist nicht, dass der Server einen direkten Push abgelehnt hat. Für Plattform-Ablehnungsbelege soll ein Mitwirkender mit genehmigtem lokalem Git-Zugriff einen harmlosen direkten Push auf **`main`** versuchen und die Serverantwort aufbewahren. Markiere diesen Ablehnungstest als Blockiert, wenn lokaler Zugriff fehlt.

**Lies `main` nach der Ablehnung** und bestätige, dass sich die Revision nicht geändert hat. Erfasse Akteursrolle, versuchte Aktion, Ergebnis und Ausgangsrevision. Ein Assistent, der verspricht, nicht zu veröffentlichen, ist Verhaltensbeleg, kein Plattform-Berechtigungstest.

**Nutze für den direkten Push-Test den eigenen authentifizierten lokalen Klon des Mitwirkenden.** Ein Maintainer-Token würde die falsche Identität testen. Die folgende Beispielantwort zeigt, welche Serverbelege aufzubewahren sind. Der genaue Wortlaut hängt von den Repository-Regeln ab.

```text
Actor role: contributor
Attempt: harmless synthetic direct push to main
Remote result: rejected, protected branch update denied
Initial main commit: [record sandbox commit]
Final main commit: [record same commit after read-back]
Decision: platform denial supported only if both records are observed
```

**Wenn lokale Git-Authentifizierung fehlt, markiere die serverseitige Ablehnung als Blockiert.** Bewahre die Browser-Aufforderung zum Branch-Erstellen als Wegbeleg auf und bitte den Maintainer um einen separaten Mitwirkenden-Test. Werte die Wegaufforderung nicht als abgelehnten direkten Push.

## Nützliche Quellenkarte erstellen

**Eine Quellenkarte ist ein Routing-Dokument**, kein zweites Anforderungsdokument. Jemand aus dem Chat muss aktuelle Absicht, implementiertes Verhalten und Betriebsanweisungen finden, ohne zwischen konkurrierenden Zusammenfassungen zu wählen.

```text
Project: export-service-lab
Track: GitHub-first
Approved boundary: protected main

REQ-17 -> requirement.json
  Authority: retention intent for synthetic export files
  Owner: product-owner
  Revision: record revision plus protected commit

RUN-04 -> runbook.md
  Authority: operating instructions for the synthetic lab
  Owner: operations-owner
  Revision: protected commit

Behavior -> config.json
  Authority: committed retention configuration
  Owner: repository-maintainer
  Revision: protected commit

Proposals -> Issues and proposal branches
  Authority: requested changes only
```

**Trage den aktuellen Aufbewahrungswert nicht in jedem Karteneintrag ein.** Eine Karte mit „sieben Tage“ wird nach PROP-042 zu einem weiteren zu synchronisierenden Wert. Bewahre stabile Kennungen und Orte in der Karte auf und lies den Wert aus dem maßgeblichen Datensatz.

**Schütze Kartenänderungen als Routingänderungen.** Die Umleitung von REQ-17 auf eine Entwurfsdatei ändert die Quellenauswahl, selbst wenn die genehmigte Anforderung unverändert bleibt. Prüfe Ziel, Eigentümer und Autoritätsbereich bei jeder Kartenänderung.

## Baseline und Vorschlag trennen

**Das Repository-Stammverzeichnis enthält die aktiven Laboraufzeichnungen.** Das heruntergeladene **`baseline/`**-Verzeichnis ist eine Lehrvorlage. Es ist nicht automatisch die geschützte Grundlage für jede spätere PR. Sobald geprüfte Arbeit **`main`** erreicht, bilden die geschützten Aufzeichnungen im Stammverzeichnis die Basis des nächsten Vorschlags.

| Ort | Zweck | Während PROP-042 bearbeiten? |
|---|---|---|
| **Anforderung/Konfiguration/Runbook im Stamm** | Vorgeschlagene aktive Aufzeichnungen im Branch | Ja, über geprüfte Änderungen |
| **`baseline/`** | Ursprüngliche Offline-Übungsvorlage | Nein |
| **Getrenntes vertrauenswürdiges Worktree** | Erfasste geschützte Aufzeichnungen aus dem Stamm | Nein |
| **`context.json`** | Beleg der erfassten Basisbytes | Nach der Abstimmung neu erzeugen |

**Halte Kontrolländerungen von Aufbewahrungsänderungen getrennt.** Starte zuerst Prüfer und Reviewregeln. Schlage dann die Änderung von sieben auf dreißig Tage vor. Eine gemeinsame Richtlinien-, Workflow- und Wertänderung erschwert die Unterscheidung zwischen reparierten und umgangenen Kontrollen.

## Vollständige Änderung prüfen

**Öffne geänderte Dateien vor der Annahme einer PR-Beschreibung.** Die Beschreibung erklärt die Absicht des Autors. Der Diff zeigt die eingereichte Änderung. Für PROP-042 prüfst du Anforderungsrevision, Bereichsausschlüsse, Konfiguration, Runbook, Vorschlagsbasis und Manifestbelege.

1. **Produktreview:** Bestätige die Dreißig-Tage-Absicht und unveränderte Ausschlüsse.
2. **Betriebsreview:** Bestätige, dass das Runbook zur vorgeschlagenen Konfiguration passt und die Laufzeitbegrenzung erhält.
3. **Maintainer-Review:** Prüfe JSON, Quellenerfassung, Prüfergebnisse und unabhängige Änderungen.
4. **Kontrollreview:** Prüfe jede Änderung an Karte, Richtlinie, CODEOWNERS oder Workflow separat.

**Ein erfolgreicher Check erklärt keine unabhängige Löschung.** Entfernt der Branch das Richtliniendokument und ändert zugleich die Aufbewahrung, fordere einen separaten Vorschlag oder ein gezieltes Eigentümerreview. Ein begrenzter Umfang hält das Review-Objekt verständlich.

## Ablehnungstest diagnostizieren

**Verwende eine versuchte Aktion pro Belegzeile.** „Mitwirkender ist gescheitert“ ist mehrdeutig. Der Benutzer kann normalen Schreibzugriff vermissen, auf eine Browsergrenze stoßen oder die vorgesehene Branch-Regel treffen. Diese Beobachtungen legen unterschiedliche Grenzen fest.

| Beobachtung | Interpretation | Weiteres Vorgehen |
|---|---|---|
| **Kann keinen Branch erstellen** | Beitragszugriff fehlt | Genehmigten Issue-/Fork-Weg verwenden |
| **Erstellt Branch, kann nicht nach main veröffentlichen** | Geprüfter Veröffentlichungsweg ist eingeschränkt | Unveränderte main-Revision erfassen |
| **Merge mit einem Review blockiert** | Review-Anzahl gilt für getestete PR | Rollenspezifischen Beleg ergänzen |
| **Administrator veröffentlicht trotz Regel** | Getestete Identität umgeht die Grenze | Bypass-Einstellungen und Berechtigungen prüfen |

**Erfasse Rolle und Aktion ohne Kontodaten offenzulegen** in gemeinsam genutzten Kursbelegen. Halte native Akteursaufzeichnungen privat für den Reviewer verfügbar. Erfasse Regelkonfiguration, versuchten Vorgang, Ablehnung und resultierende geschützte Revision gemeinsam.

## Repository-Abschlussprüfung

**Liefere ein Repository, das ein anderer Mitwirkender selbstständig navigieren kann.** README verweist auf die Karte, die Karte löst maßgebliche Aufzeichnungen auf, Eigentümerabdeckung umfasst sensible Pfade und Schutz gilt für **`main`**. Bewahre einen erlaubten Vorschlag und einen abgelehnten Veröffentlichungsversuch auf.

**Leite Durchsetzung nicht allein aus Einstellungen ab.** Einstellungen zeigen die beabsichtigte Konfiguration. Der Sandbox-Versuch zeigt beobachtetes Verhalten für eine bestimmte Rolle und einen bestimmten Weg. Nimm beides in die Agenten- und Actions-Lektion auf.

## Fehlerbehebung und Rollback

**Eigentümeranfrage fehlt:** Schreibzugriff und Pfadabdeckung des Basis-Branches bestätigen. **Schutz fehlt:** Plan und Sichtbarkeit prüfen. **Merge bleibt aktiviert:** Regelziel, Bypass-Konfiguration und Review-Anzahl prüfen.

**Rollback:** Nicht gemergte Vorschläge schließen und Laborautomatisierung deaktivieren. Gemergte Laborinhalte über eine weitere geprüfte PR zurücknehmen. Belege vor dem Löschen des Wegwerf-Repositories sichern. Schutz nicht abschwächen, um einen fehlgeschlagenen Test zu beenden.

## Übung und Selbstprüfung

**Schlage als Mitwirkender eine Änderung an `docs/policy.md` vor.** Entscheide, ob die Zustimmung des Maintainers allein die Zustimmung des Richtlinienverantwortlichen herstellt.

**Erwartete Überlegung:** Die Review-Anzahl allein stellt keine Autorität her. Der Pfad braucht Richtlinien-Eigentümerabdeckung und aktuelles Rollenreview. Liste nicht durchgesetzte rollenspezifische Anforderungen als Verfahrenskontrollen auf.

## Hauptreferenzen

- **Plan- und Reviewkontrollen:** [Geschützte Branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Eigentümerberechtigung:** [Code-Eigentümer](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
- **Browserbeitrag:** [Dateien bearbeiten](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).

## Nächste Schritte

**Fahre mit [Agent-Adapter und Actions](/articles/ai-collaboration-github-agents-actions/)** fort, um Quellenbelege mit ausführbaren Prüfungen zu verbinden.

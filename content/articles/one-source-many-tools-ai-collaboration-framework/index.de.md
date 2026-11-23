---
title: "Eine Quelle, viele Tools: Ein KI-Zusammenarbeitsmodell für gemischte Teams"
date: 2026-10-01
lastmod: 2026-11-23
toc: true
draft: false
description: "Erstelle ein gemeinsames KI-Zusammenarbeitssystem mit klaren Quellenverantwortlichen, versioniertem Kontext, geprüften dauerhaften Änderungen und einer begründeten Wahl zwischen Projektkarte und RAG."
genre: ["Künstliche Intelligenz", "Wissensmanagement", "Softwareentwicklung", "Teamarbeit"]
tags: ["KI-Zusammenarbeitsmodell", "gemischte Teams", "maßgebliche Quelle", "KI-Agenten", "AGENTS.md", "CLAUDE.md", "Cline-Regeln", "Claude Code", "Codex", "ChatGPT", "Copilot", "Cowork", "generative KI mit Informationsabruf", "RAG", "Model Context Protocol", "Projektkarte", "Kontextmanifest", "Wissensmanagement", "Dokumentationsdrift", "menschliche Freigabe", "Entscheidungsregister", "Agentenübergabe", "Richtlinienversionierung", "Git-Worktrees", "Pull-Request-Prüfungen"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Eine Illustration von Fachleuten, die gemeinsam an Cybersicherheit arbeiten"
coverCaption: ""
---

**Zwei Personen stellen zwei KI-Tools dieselbe Frage:**** Wie lange soll der Dienst einen Export aufbewahren? In diesem Beispiel antwortet der IDE-Agent eines Entwicklers mit sieben Tagen, gestützt auf eine README.** Der Chatassistent der Betriebsleitung nennt dreißig Tage und verweist auf eine Wiki-Seite. Beide Antworten klingen überzeugend. Jedes Tool hat eine andere Kopie der Wahrheit gelesen.

**Das Problem ist die Zuständigkeit****, nicht die Qualität des Prompts.** Die Wiki-Anforderung wurde letzte Woche geändert, doch niemand hat die README aktualisiert. Der Entwickler bittet den Agenten, den Aufbewahrungsjob anzupassen. Der Agent folgt dem älteren Dokument und liefert einen sauberen Patch, der das falsche Verhalten wiederherstellt. Die Prüfer sehen den Code, aber nicht die Version der Anforderung hinter der Antwort.

**Gib jeder Tatsache einen festen Ort.**** Lass jedes Tool diese Quelle lesen und jede dauerhafte Änderung von einer Person prüfen.** Repository, Wiki und Tracker erfüllen weiterhin unterschiedliche Aufgaben. Lege ihre Autorität und Zuständigen fest und definiere einen gemeinsamen Ablauf für den Informationsaustausch.

**Dieser Leitfaden bietet ein Modell, das du diese Woche anwenden kannst****, mit oder ohne Retrieval-Augmented Generation.** Beginne mit Projektkarte, versionierten Anweisungen, Nachweisprotokollen und geprüften Vorschlägen. Ergänze Suchinfrastruktur erst, wenn das Abrufproblem sie rechtfertigt.

**Dein erstes Ergebnis ist ein Quellenregister**, kein Connector. Halte für jeden Informationstyp die maßgebliche Quelle, den Zuständigen, die aktuelle Revision und die Person fest, die Änderungen freigibt.

## Wichtigste Erkenntnisse

- **Weise Autorität Informationstypen zu**, statt alles in eine Anwendung zu zwingen.
- **Behandle Gedächtnis und Retrieval-Indizes als Caches**, niemals als unabhängige Richtlinienquellen.
- **Füge Vorschlägen die Quellversionen bei**, damit Prüfer sehen, welche Fakten eine Änderung stützen.
- **Erzwinge Freigaben außerhalb von Prompts**, durch Zugriffskontrollen und verpflichtende Prüfschritte.
- **Teile den Ablauf über Tools hinweg**, und passe die Umsetzung an die jeweilige Oberfläche an.

## Bevor du beginnst

**Voraussetzungen:**** Wähle ein Pilotprojekt mit Repository, Wiki oder Dokumentensystem, Tracker und Verantwortlichen, die Änderungen prüfen.** Ohne Wiki verwendest du einen versionierten Dokumentenspeicher. Das Zuständigkeitsmodell bleibt gleich.

**Geschätzter Zeitaufwand:**** Plane zwei bis vier Stunden für die erste Karte und Vorlagen sowie anschließend eine Pilotwoche ein.** **Schwierigkeit:** mittel. Die Autorität festzulegen ist schwieriger, als ein weiteres KI-Tool zu installieren.

**Umfang:**** Dies ist ein vorgeschlagenes Betriebsmodell für Teams.** Freigaberegeln und Namenskonventionen sind Empfehlungen, kein Standardverhalten, das Claude Code, Codex, Cline, Cowork, Copilot oder ChatGPT garantieren. Das automatische Inhaltsverzeichnis oben verweist auf jeden Umsetzungsschritt.

## Gemischte Tools, getrennter Kontext

**Programmierer und Nicht-Programmierer teilen ein Projekt****, nutzen aber unterschiedliche Oberflächen.** Entwickler arbeiten mit IDE- oder Terminal-Agenten. Produktverantwortliche nutzen ein Chat-Projekt. Der Betrieb arbeitet mit Wiki und Tracker. Wähle die Oberfläche nach der Aufgabe, nicht nach dem Zugriff auf maßgebliche Fakten.

**Kontext umfasst das Material, das für die aktuelle Antwort verfügbar ist.**** Prüfe je Sitzung Repository-Dateien, hochgeladene Dokumente, Chatverlauf, gespeichertes Gedächtnis, Connector-Ergebnisse und abgerufene Ausschnitte.** Sitzungen mit unterschiedlichen Belegen müssen auch bei derselben Frage nicht übereinstimmen.

| Problem | Beobachtung |
|---|---|
| **Dokumentationsdrift** | Eine README wiederholt eine veraltete Anforderung |
| **Aufwertung einer Zusammenfassung** | Eine Sitzungsauswertung gilt ohne Originalquelle als Beleg |
| **Überschneidende Änderungen** | Zwei Agenten ersetzen dieselbe Seite aus unterschiedlichen Basisversionen |
| **Verlorene Entscheidungen** | Eine Besprechungsvereinbarung erreicht das Entscheidungsregister nicht |
| **Fehlende Herkunft** | Eine plausible Antwort nennt weder Seitenversion noch Commit |

**Das Beispiel zur Aufbewahrung zeigt den Unterschied.**** Das Wiki beschreibt das freigegebene Zielverhalten.** Der Code beschreibt das umgesetzte Verhalten. Keines sollte das andere stillschweigend überschreiben. Halte den Widerspruch fest und frage den zuständigen Eigentümer, ob Implementierung oder Anforderung angepasst werden muss.

> **Wichtig:** Die Autorität zu klären ist wichtiger als die Wahl eines KI-Tools. Beginne mit den folgenden gemeinsamen Begriffen.

### Seitenleiste: Fünf gemeinsame Begriffe

| Begriff | Bedeutung in diesem Modell |
|---|---|
| **Quelle** | Der festgelegte maßgebliche Datensatz für einen Informationstyp |
| **Cache** | Eine abgeleitete Kopie für Geschwindigkeit oder Komfort |
| **Vorschlag** | Eine vorgeschlagene Änderung, die auf Freigabe wartet |
| **Projektkarte** | Ein Index mit Quellenorten, Kennungen und Zuständigen |
| **Manifest** | Ein Nachweis der exakten Belege für Antwort oder Vorschlag |

## Gib Fakten einen festen Ort

**Eine Quelle bedeutet eine Autorität pro Fakt****, nicht eine Datenbank für die gesamte Organisation.** Lege im Pilotprojekt folgende Zuordnung fest und ersetze die Beispielrollen durch die tatsächlichen Zuständigen deines Teams.

| Informationstyp | Quellsystem | Zuständig | Wer schreibt | Wie Agenten lesen |
|---|---|---|---|---|
| **Code, Tests, Konfiguration, Schemas** | Repository | Technischer Maintainer | Beitragende über geprüfte PRs | Dateien aus einem festgehaltenen Commit |
| **Veröffentlichte Doku und ADRs** | Repository | Technischer Eigentümer | Beitragende über denselben PR | Versionierte Dateien |
| **Anforderungen** | Wiki | Produkteigentümer | Eigentümer oder freigegebene Redaktion | Seiten-ID und Revision |
| **Runbooks** | Wiki | Betriebsverantwortlicher | Freigegebene Redaktion | Seiten-ID und Revision |
| **Richtlinie** | Wiki | Richtlinienverantwortlicher | Freigegebene Redaktion nach Prüfung | Kanonische Seite plus lokaler Adapter |
| **Teamübergreifende Entscheidungen** | Entscheidungsregister im Wiki | Benannter Entscheidungseigentümer | Eigentümer nach Freigabe | Entscheidungs-ID und Status |
| **Aufgaben und Feststellungen** | Tracker | Aufgabeneigentümer | Personen oder autorisierte Vorschlagseingabe | Vorgangsschlüssel und Revision |
| **Chats, Zusammenfassungen, Embeddings** | Nur Cache | Sitzungs- oder Indexverantwortlicher | Tools und Beteiligte | Nur Verweis, danach Quellenprüfung |

**Ein Architekturentscheidungsprotokoll (ADR)** gehört zum Code, wenn es die Repository-Architektur regelt. Eine teamübergreifende Entscheidung gehört ins gemeinsame Register. Verknüpfe die Einträge, wenn eine Entscheidung beide Bereiche betrifft. Pflege den Freigabestatus nicht in zwei unabhängigen Kopien.

**Lokale Richtlinienkopien bleiben der kanonischen Richtlinienseite untergeordnet.** Tests und Schemas eines Repositorys sind dagegen Quellen innerhalb ihres eigenen Bereichs. Der Ablageort bestimmt die Autorität nicht. Das erledigt die Karte.

**Ein Cache setzt niemals eine Quelle außer Kraft.** Wenn eine Zusammenfassung sieben Tage nennt und die freigegebene Anforderung dreißig, gilt für das Zielverhalten die Anforderung. Bewahre die widersprüchliche Zusammenfassung als Driftbeleg auf, nicht als konkurrierende Regel. Lege nun den Schreibablauf fest.

## Cache nach unten, Vorschlag nach oben

**Agenten übernehmen Belege in den Sitzungskontext** und erstellen dann Vorschläge. Sie geben dauerhafte Fakten nicht selbst frei. Einen Aufgabenbranch zu bearbeiten oder einen Entwurf einzureichen ist etwas anderes, als Richtlinien zu veröffentlichen, Code zusammenzuführen oder eine Entscheidung als angenommen zu markieren.

```text
Quelle -> Lesen mit Berechtigungsprüfung -> Sitzungskontext
Sitzungskontext -> Vorschlag + Basisversion -> Prüfung durch Verantwortliche
Freigabe durch Verantwortliche -> kontrollierte Veröffentlichung -> Änderungsprotokoll
Geänderte Basisversion -> Vorschlag abgleichen -> erneut prüfen
```

**Halte die Basisversion fest**, bevor du eine Prüfung anforderst. Prüfer benötigen vorherigen Wert, vorgeschlagenen Wert, Grund, Belege und betroffene Systeme. Die Freigabe muss sich auf eine bestimmte Vorschlagsrevision beziehen, nicht auf einen laufend veränderten Chat.

```yaml
proposal_id: PROP-042
target: wiki:REQ-17
base_version: 8
change: "Exporte dreißig statt sieben Tage aufbewahren."
evidence:
  - "entscheidung:DEC-12 freigegeben"
affected_records:
  - "repo:export-service retention configuration"
  - "wiki:RUN-04 cleanup procedure"
owner_role: product-owner
status: awaiting-review
```

**Die Kennungen oben sind Beispiele.** Erfasse für jede freigegebene logische Änderung genau eine Zeile im Änderungsprotokoll mit Vorschlags-ID, Zielobjekten, vorheriger und resultierender Version, freigebender Person, Zeitstempel und Merge- oder Veröffentlichungsreferenz. Verknüpfe einzelne System-Auditereignisse mit dieser Zeile, statt deren native Historie zu ersetzen.

**Menschen treffen die Entscheidung.** Eine autorisierte veröffentlichende Person oder begrenzte Automatisierung setzt die freigegebene Revision um. Beschränke Schreibrechte entsprechend. Anweisungen allein trennen Entwurf und Veröffentlichung nicht. Dieselbe Unterscheidung gilt für den Abruf.

## Gemeinsamer Kontext ohne RAG

**Eine Projektkarte ist der erste Retrieval-Index.** Pflege eine Seite pro Projekt mit Quell-IDs, Repository-Pfaden, Tracker-Schlüsseln, Autoritätsbereichen und Zuständigen. Lies zuerst die Karte und rufe dann den relevanten Datensatz über seine ID ab. Suche, wenn die ID unbekannt ist.

### Seitenleiste: Beispiel einer Projektkarte

```yaml
project: export-service
map_id: MAP-01
policy:
  source_id: POL-01
  approved_version: 3
  owner_role: policy-owner
sources:
  requirements: {page_id: REQ-17, owner_role: product-owner}
  runbook: {page_id: RUN-04, owner_role: operations-owner}
  decisions: {register_id: DEC-REGISTER, owner_role: project-lead}
repository:
  key: export-service
  setup: README.md
  terms: CONTEXT.md
  decisions: docs/adr/
tracker:
  project_key: EXP
  active_task: EXP-42
```

**Direkte Connectoren verringern manuelles Kopieren.** Model Context Protocol (MCP) ist ein Integrationsprotokoll, über das KI-Anwendungen Tools und Kontext nutzen. Verwende freigegebene Wiki-, Tracker- und Repository-Connectoren, sofern verfügbar. Ein gezielter Abruf reduziert irrelevante Ergebnisse, ersetzt aber weder Autorisierung noch Aktualitätsprüfungen. Beachte beim Festlegen von Connector-Berechtigungen die MCP-Sicherheitshinweise in den Referenzen.

**Exakter Abruf ist einfach einzurichten.** Er liefert zitierbare Belege ohne Vektordatenbank. Die Grenzen sind klar: Jemand muss die Karte pflegen, breite Fragen erfordern zusätzliche Suche, und große Seiten beanspruchen Sitzungskontext. Rufe den relevanten Abschnitt samt umliegenden Einschränkungen ab, statt ein ganzes Handbuch einzufügen.

**Offline-Arbeit nutzt ausdrücklich markierte Snapshots.** Halte die exportierte Revision fest und kennzeichne Antworten als snapshot-basiert. Veröffentliche nichts, bevor eine autorisierte Person oder ein Connector die aktuelle Quelle geprüft hat. Mache die gleiche Richtlinie anschließend in jeder Oberfläche sichtbar.

## Eine Richtlinie, unterschiedliche Adapter

**Verwende eine gemeinsame Richtlinie** und verteile kurze tool-spezifische Adapter. Setze die freigegebene Richtlinienversion an die erste Zeile jedes Adapters oder kopierten Anweisungssatzes. Ergänze Quell-ID und geprüften lokalen Snapshot für Sitzungen ohne Connectorzugriff.

**Das Laden von Anweisungen unterscheidet sich je Tool.** Codex dokumentiert die gestaffelte Suche nach `AGENTS.md`. Claude Code dokumentiert `CLAUDE.md`, Importe und Projektspeicher. Cline dokumentiert `.clinerules/` und die Regelsteuerung. Nutze die offizielle Anleitungsdokumentation in den Referenzen. Prüfe in deiner installierten Version, welche Anweisungen geladen wurden, statt identisches Verhalten aus Dateinamen abzuleiten.

### Seitenleiste: Beispielkopf für AGENTS.md

```markdown
Richtlinienversion: v3 | Quelle: wiki:POL-01 | Status: genehmigt

# Projektanweisungen

Lies vor Aufgabenbeginn die Projektkarte MAP-01.
Lade docs/policy-snapshot.md und halte die Quellrevision fest.
Behandle Chatgedächtnis und Suchausschnitte als Caches.
Füge jedem sachlichen Vorschlag Quellrevisionen bei.
Verwende je Programmieraufgabe einen Aufgabenbranch und ein Worktree.
Veröffentliche keine Richtlinien, genehmige keine Entscheidungen und merge deinen eigenen PR nicht.
Stoppe bei ungelösten Quellenkonflikten oder überlappenden Schreibvorgängen.
Erforderliche Prüfungen: Tests, Dokumentationsprüfung, Richtlinienaktualität.
Zuständige: Engineering-Maintainer, Produkteigentümer, Richtlinienverantwortlicher.
```

**Chat-Projektanweisungen erhalten denselben Kopf und Ablauf.** Nicht-Programmierer erhalten den Richtlinien-Snapshot und die Projektkarte über freigegebene Uploads oder Connectoren. Fehlt der Oberfläche Live-Zugriff, stellt eine Person den versionierten Export bereit und dokumentiert die Einschränkung.

**Ein Versionslabel ist eine Behauptung, kein Beweis für identischen Inhalt.** Erzeuge Adapter aus dem freigegebenen Snapshot oder vergleiche ihre Richtlinienabschnitte mit einem gespeicherten Digest. Prüfe adapter-spezifische Ausnahmen separat. Suche im Pilot nach deaktivierten Regeln, verschachtelten Überschreibungen und persönlichen Anweisungen. Halte anschließend die Belege jeder Aufgabe fest.

## Ein Kontextmanifest erfassen

**Ein Kontextmanifest erklärt die Belege einer Antwort.** Notiere Seiten-IDs und Revisionen, Vorgangsschlüssel samt Revision oder Aktualisierungszeit sowie vollständige Repository-Commit-IDs. Ergänze Abrufzeit und relevante Abschnitte. Kennzeichne nicht verfügbare Datensätze, statt sie durch eine erinnerte Zusammenfassung zu ersetzen.

```yaml
task: EXP-42
policy: {page_id: POL-01, version: 3}
wiki:
  - {page_id: REQ-17, version: 8, section: export-retention}
tracker:
  - {issue_key: EXP-42, revision: 5}
repository:
  commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  files: [README.md, config/retention.yaml]
limits:
  - "Runbook nicht abgerufen. Keine Änderung am Runbook vorgeschlagen."
```

**Der Commit-Wert ist synthetisch.** Ersetze ihn in einem echten Manifest durch den geprüften Commit. Ergänze den Abrufzeitpunkt während des tatsächlichen Lesens. Ein vor der Prüfung erstellter Eintrag ist eine Checkliste, kein Beleg.

**Zitate unterstützen die Prüfung**, schaffen aber nicht automatisch Vertrauen. Verknüpfe jede wesentliche Aussage mit dem stützenden Datensatz und Abschnitt. Sind Quellen widersprüchlich, behalte beide im Manifest und melde den ungelösten Konflikt. Wähle nicht ohne Prüfung von Geltungsbereich und Freigabestatus den neuesten Zeitstempel. Diese Belegdisziplin gilt ebenso für semantischen Abruf.

## Gemeinsamer Kontext mit RAG

**Retrieval-Augmented Generation (RAG)** versorgt ein Modell beim Erstellen einer Antwort mit abgerufenem Material. Ein semantischer Index findet relevante Stellen auch dann, wenn die Frage andere Formulierungen verwendet. Microsofts RAG-Übersicht behandelt Grounding, Abrufgrenzen und Zugriffskontrollen. Die offizielle Quelle steht in den Referenzen.

**Verwende RAG zur Suche in größeren Sammlungen**, etwa älterer Dokumentation, Sitzungsnotizen und Transkripten. Kennzeichne Dokumentklassen und Freigabestatus. Ein Transkript aus der Originalaufnahme belegt, was Beteiligte gesagt haben, ist aber keine Autorität für freigegebene Anforderungen. Mache Gespräche nicht durch Indexierung zu Richtlinien.

| Indexregel | Erforderliches Verhalten |
|---|---|
| **Quellen statt Caches aufnehmen** | Generierte Zusammenfassungen und nicht nachverfolgte lokale Kopien ausschließen |
| **Herkunft bewahren** | Quell-ID, Revision, Abschnitt und Dokumentstatus je Chunk speichern |
| **Bei Änderungen aktualisieren** | Änderungen neu indexieren und veraltete Chunks entwerten |
| **Zugriffsänderungen beachten** | Berechtigungen aktualisieren und widerrufene oder gelöschte Inhalte entfernen |
| **Zitate zurückgeben** | Quellenverweise neben dem abgerufenen Text anzeigen |
| **Live-Datensatz prüfen** | Aktuelle Belege vor einem folgenreichen Vorschlag abrufen |

**Ein abgerufener Chunk ist in diesem Modell ein Verweis.** Sein Text hilft, Belege zu finden. Die Live-Quelle bestätigt aktuelle Formulierung, Freigabe, Ausnahmen und Zugriff. Kennzeichne den Snapshot und stoppe die folgenreiche Aktion, wenn Live-Abruf fehlschlägt. Das ist eine Governance-Regel, keine Aussage über jede RAG-Implementierung.

**Veraltete Embeddings und fehlender Kontext bergen getrennte Risiken.** Ein alter Chunk verpasst eine Revision. Ein aktueller Chunk führt trotzdem in die Irre, wenn eine Ausnahme im nächsten Abschnitt steht. Bewahre Überschriften und rufe benachbarte Einschränkungen ab, bevor du eine Anforderung bewertest.

**Berechtigungslecks brauchen einen eigenen Test.** Erzwinge Autorisierung, bevor Chunks an das Modell zurückgegeben werden, nicht erst nach der Antwort. Prüfe sensible Inhalte vor Indexierung oder externen Embedding-Aufrufen. Beachte Kopien in Logs, Modellanfragen und Abrufspuren. Ein lokales Modell macht einen entfernten Connector nicht lokal. Diese Prüfungen zeigen, ob RAG in den Pilot gehört.

## Karte, RAG oder beides wählen

**Richte den Abruf nach der Frage aus.** Eine bekannte Anforderungs-ID spricht für direkten Zugriff. Eine offene Frage zu verstreutem historischem Material spricht für Suche. Beginne mit der Karte, sofern die Suche nicht bereits als Problem gemessen wurde.

### Seitenleiste: RAG oder nicht?

```text
Nennen Aufgaben gewöhnlich ein Projekt, eine Seite, einen Vorgang oder eine Datei?
  Ja -> Reicht direkter Abruf für den Pilot?
           Ja -> NUR KARTE
           Nein -> HYBRID: Karte für bekannte IDs, RAG zur Entdeckung
  Nein -> Sind Belege über eine große Sammlung verteilt?
           Nein -> NUR KARTE plus integrierte Suche
           Ja -> Ist die Arbeit explorativ und schreibgeschützt?
                    Ja -> NUR RAG zur Entdeckung
                    Nein -> HYBRID mit Live-Quellenprüfung

Jede Option behält Zuständigkeiten, Autorisierung und Herkunft bei.
Auch RAG-gestützte Entdeckung prüft Quellen vor dauerhaften Aktionen.
```

**RAG-only beschreibt die Abrufoberfläche**, nicht die Erlaubnis, Governance zu überspringen. Nutze sie für eine begrenzte explorative Sammlung, in der die direkte Quellenprüfung verfügbar bleibt. Für bekannte IDs mit präziser Versionsprüfung ist sie ungeeignet.

**Das hybride Modell trennt Entdeckung und Prüfung.** Die Karte deckt bekannte Abfragen ab. RAG findet unbekannte Datensätze. RAG beantwortet „wo“, die Quelle beantwortet „was“. Rufe für das Aufbewahrungsbeispiel `REQ-17` direkt ab. Suche für „Welche früheren Exportentscheidungen erklären dieses Limit?“ im Register und rufe jede relevante Entscheidung ab. Setze nun die Repository-Seite um.

## Informationen im Repository

**Repository-Wissen ändert sich mit der Implementierung.** Halte die Struktur kompakt, damit Agenten und Prüfer wissen, wo sie suchen müssen.

| Datei oder Verzeichnis | Aufgabe |
|---|---|
| **`CONTEXT.md`** | Projektbegriffe und Links zu maßgeblichen Datensätzen |
| **`docs/adr/`** | Akzeptierte Architekturentscheidungen des Repositorys |
| **`docs/design/`** | Freigegebene Beschreibungen des Systemverhaltens |
| **`docs/plans/`** | Vorgeschlagene Implementierungspläne mit klarem Status |
| **`AGENTS.md`** | Prüfgates, Grenzen und Zuständigkeitsrollen |
| **`README.md`** | Einrichtung und Einstiegspunkte, keine doppelten Anforderungen |

**Wende die Same-PR-Regel an:** Ändere Code und betroffene Repository-Dokumentation gemeinsam. Ist kein Update der Wissensbasis nötig, verlange eine schriftliche Ausnahme in der PR-Beschreibung oder am vereinbarten Ort für Commit-Trailer.

```text
KB-Update: none (Grund: internes Refactoring erhält dokumentiertes Verhalten)
```

**Die Pipeline erzwingt die Erklärung.** Eine erforderliche Prüfung lehnt Verhaltensänderungen ohne Dokumentationsupdate oder Ausnahme ab. Ein menschlicher Dokumentationseigentümer prüft die Ausnahme. Eine pfadbasierte Prüfung findet mögliche Änderungen, beweist aber keine semantische Vollständigkeit. Erzwinge Prüfung und Freigabe über Branch Protection oder eine gleichwertige Merge-Kontrolle.

**Ein Gate außerhalb der Pipeline ist kein Gate.** Die Formulierung „Dokumentationsprüfung“ in einer Anweisungsdatei ist nur eine Empfehlung. Teste die Durchsetzung im Pilot mit einer absichtlich unvollständigen PR und bestätige, dass der Merge blockiert bleibt.

**Verwende eine Aufgabe, einen Branch und ein Worktree.** Die offizielle Git-Dokumentation beschreibt getrennte Arbeitsverzeichnisse mit eigenem Checkout-Status. Worktrees verringern lokale Bearbeitungskonflikte. Sie verhindern nicht, dass zwei Branches dieselbe Datei ändern oder Agenten gleichzeitig eine Wiki-Seite bearbeiten.

**Committe niemals direkt auf den Standardbranch**, unabhängig davon, ob er `main`, `master` oder anders heißt. Melde Abweichungen zwischen Anforderung und Code im Tracker. Füge die widersprüchlichen Datensätze bei und lass deren Eigentümer das gewünschte Verhalten klären, bevor eine Seite angeglichen wird. Setze gleichwertige Kontrollen außerhalb von Git um.

## Informationen außerhalb des Repositorys

**Das Wiki braucht einen Dokumentationsstandard.** Jede maßgebliche Seite enthält Zweck, Status, Eigentümer, Revision, Prüftermin und zugehörige Quell-IDs. Lege Vorschläge in einem Entwurfsbereich mit deutlicher Kennzeichnung als nicht maßgeblich ab. Mische vorgeschlagene Formulierungen nicht in eine freigegebene Anforderungsseite.

**Sichere Updates folgen einer festen Reihenfolge:**

1. **Lies** die aktuelle Seite und angrenzende Einschränkungen erneut.
2. **Vergleiche** ihre Version mit der Basisversion des Vorschlags.
3. **Gleiche** zwischenzeitliche Änderungen ab und hole bei geändertem Wortlaut eine neue Freigabe ein.
4. **Schreibe** die freigegebene Revision mit einer Bedingung für die erwartete Version.
5. **Prüfe** die gespeicherte Seite und ergänze den Verweis auf das Änderungsprotokoll.

**Erneutes Lesen beseitigt Rennen nicht.** Nutze, falls verfügbar, die bedingte Update-Funktion des Systems. Andernfalls serialisiert ein einzelner Eigentümer die Veröffentlichung und prüft das Ergebnis. Stoppe, wenn jemand während der Prüfung die Basis ändert.

**Das Löschverbot gilt für Agentenabläufe.** Agenten schlagen Archivierung oder Löschung vor. Autorisierte Menschen führen Aufbewahrungs- und Löschverfahren aus. Verstehe diese Regel nicht als Erlaubnis, sensible Informationen unbegrenzt aufzubewahren.

**Tracker-Feststellungen enthalten Belege**, nicht nur Schlussfolgerungen. Halte Beobachtung, exakten Befehl oder Prüfmethode, geprüften Commit, erwartetes und tatsächliches Verhalten sowie Akzeptanzkriterien fest. Entferne Geheimnisse und sensible Ausgaben vor dem Anhängen. Kennzeichne vorgeschlagene Befehle als nicht ausgeführt, bis jemand sie startet.

```text
Feststellung: Aufbewahrungsimplementierung widerspricht der freigegebenen Anforderung
Belege: REQ-17 v8 und geprüfte config/retention.yaml
Prüfbefehl: git show HEAD:config/retention.yaml
Commit: vollständige geprüfte Commit-ID im Manifest festgehalten
Akzeptanz: Freigegebene Dauer stimmt mit Code, Tests und Runbook überein
Status: wartet auf Prüfung durch Produkt- und Engineering-Verantwortliche
```

**Das Beispiel ist eine Vorlage für eine Feststellung**, kein Messergebnis. Fülle sie anhand einer tatsächlichen Prüfung aus. Verknüpfe Wiki-Update und Tracker-Belege über die Vorschlags-ID.

**Das Entscheidungsregister trennt Regeln von Begründungen.** Halte Frage, Optionen, Empfehlung, Abwägungen, Eigentümer, Freigabestatus und Verweis auf die resultierende Regel fest. Agenten schlagen vor. Menschen entscheiden. Freigegebene Regeln kommen in Richtlinien und Verfahren. Die Begründung bleibt im Register.

**Übernimm dauerhafte Fakten aus Besprechungen und Chats.** Reiche einen Vorschlag samt Quellenbelegen ein und hole Freigabe ein. Kennzeichne die Vereinbarung bis zur Veröffentlichung als vorläufig. Verknüpfe anschließend freigegebenes Verhalten zwischen Repository und Wiki.

## Die beiden Systeme verbinden

**Die Synchronisierung nach dem Merge trägt Implementierungsänderungen nach außen.** Erstelle eine Wiki-Aufgabe mit Verweisen auf den gemergten Commit, die freigegebene Anforderung und das betroffene Runbook. Ein Agent entwirft das Update. Der Wiki-Eigentümer prüft die aktuelle Seite und gibt die Veröffentlichung frei. Lass die Synchronisierung offen, bis die gespeicherte Revision bestätigt ist.

**Richtlinienaktualität ist ein eigener Audit.** Vergleiche jeden Repository-Adapter und jede Chat-Kopie der Anweisungen mit der kanonischen freigegebenen Version. Richtlinie `v3` steht unter `POL-01`. Jede `AGENTS.md` nennt `v3` in der ersten Zeile. Der Audit findet `v2`, fehlende Labels und Inhaltsabweichungen trotz gleicher Labels.

| Prüfung | Abschlussbeleg |
|---|---|
| **Richtlinienaktualität** | Kanonische Version und Adapter-Digest-Vergleich |
| **Anforderungsabgleich** | Anforderungsrevision mit Code und Tests verglichen |
| **Synchronisierung nach Merge** | Gemergter Commit mit veröffentlichter Wiki-Revision verknüpft |
| **Konfliktlösung** | Freigegebene Entscheidung mit beiden betroffenen Datensätzen verknüpft |

**Gleiche regelmäßig oder bei PR ab.** Ein wöchentlicher Audit passt für den Pilot. Eine PR mit Verhaltensänderung braucht vor dem Merge eine Anforderungsprüfung. Wähle den Rhythmus nach den Kosten von Drift und halte die letzte erfolgreiche Prüfung fest.

**Die Änderung auf dreißig Tage hat mehrere Prüfpunkte:** Das Produkt gibt die Anforderung frei, die Entwicklung aktualisiert Konfiguration und Tests, Prüfer mergen den PR, und der Betrieb veröffentlicht das Runbook-Update. Eine Zeile im Änderungsprotokoll verknüpft die resultierenden Datensätze. Eine fehlgeschlagene Wiki-Synchronisierung bleibt sichtbar und verschwindet nicht hinter einem erfolgreichen Merge. Gemeinsame Übergaben halten diese Reihenfolge über Tools hinweg ein.

## Ein Ablauf, jedes Tool

**Verpacke wiederkehrende Schritte als Skills oder Prompts** mit versionierter Verfahrens-ID. Teile den Vertrag, nicht die Annahme eines universellen Dateiformats. Jeder Tool-Adapter nutzt den unterstützten Lade- oder Aufrufmechanismus.

| Verfahren | Erforderliche Ausgabe |
|---|---|
| **Aufgabe starten** | Eigentümer, Umfang, Richtlinienversion, Quellenmanifest, Schreibreservierung |
| **Dokumentations-Lint** | Fehlende Metadaten, doppelte Autorität, ungültige Quellenverweise |
| **Wissensprüfung** | Abweichungen zwischen Anforderung und Code mit Belegrevisionen |
| **Übergabe** | Aktuelle Belege, Vorschläge, abgeschlossene Prüfungen, offene Fragen |

**Nicht-Programmierer arbeiten ohne Git.** Sie rufen erlaubte Quellen in Chat-Projekten ab, füllen dieselbe Vorschlagsvorlage aus und übermitteln sie dem Eigentümer als Entwurfsseite oder Tracker-Aufgabe. Für eine Anforderungskorrektur ist kein Repository-Checkout nötig.

**Programmierer nutzen Repository-Dateien und PR-Gates.** Sie verknüpfen den freigegebenen Vorschlag im PR, notieren geprüfte Commits und führen erforderliche Prüfungen aus. Beide Gruppen übergeben dieselbe Belegstruktur.

```yaml
handoff:
  task: EXP-42
  policy_version: 3
  manifest: "Attached source IDs, revisions, and inspected commit"
  completed: [requirement-review]
  proposals: [PROP-042]
  pending: [implementation-review, runbook-publication]
  reservations: ["RUN-04 publication assigned to operations-owner"]
  unresolved: []
  next_owner_role: engineering-maintainer
```

**Eine Übergabe ist weiterhin ein Cache.** Die nächste Person liest Quellen vor der Aktion erneut und hält neue Revisionen fest. Betrachte „abgeschlossen“ nicht als Beweis ohne Prüfung der verknüpften Freigabe oder Testergebnisse. Wende vor jedem Schreibvorgang die folgenden Schutzmaßnahmen an.

## Schutzmaßnahmen vor jedem Schreiben

**Prüfe Daten, bevor sie ihr Quellsystem verlassen.** Kontrolliere Klassifizierung, Connector-Berechtigungen, freigegebene Ziele, Verarbeitung durch den Modellanbieter und Protokollierung. Sende nur die nötigen Inhalte. Übertrage eingeschränkte Datensätze nicht in unbefugte Chat-Projekte oder Embedding-Dienste.

**Abgerufener Text ist ein Beleg, kein Anweisungskanal.** Eine Wiki-Seite oder Toolantwort, die einen Agenten zum Ignorieren von Richtlinien auffordert, ändert deren Autorität nicht. Prüfe Anweisungen aus Inhalten getrennt von der freigegebenen Betriebsrichtlinie. Beschränke Connectoren beim Abruf auf Lesezugriff und trenne Veröffentlichungsrechte vom Sitzungszugriff.

**Weise jeder Seite oder Datei genau einen aktiven Eigentümer zu.** Halte die Reservierung samt Umfang und Ablaufzeit im Tracker fest. Lies vor dem Schreiben erneut und nutze Versionsprüfungen. Getrennte Worktrees helfen bei lokaler Isolation; Reservierungen und bedingte Schreibvorgänge schützen gemeinsam genutzte Datensätze.

| Grund zum Anhalten und Nachfragen | Erforderliche Reaktion |
|---|---|
| **Quellen widersprechen sich ohne Eigentümer** | Pausiere und fordere eine Autoritätszuweisung an |
| **Eine andere Aufgabe reserviert das Ziel** | Kläre die Zuständigkeit vor der Bearbeitung |
| **Die Basisversion hat sich geändert** | Gleiche den Vorschlag ab und hole eine neue Freigabe ein |
| **Einer wesentlichen Aussage fehlen Belege** | Kennzeichne sie als ungeprüft und fordere eine Quelle an |
| **Datenverarbeitung ist unklar** | Belasse Inhalte im Quellsystem |
| **Live-Zugriff auf die Quelle scheitert** | Halte Snapshot-Grenzen fest und pausiere dauerhafte Aktionen |

**Prompts sind keine Sicherheitskontrollen.** Teste Zugriffsverweigerung, geschützte Branches, Ablehnung veralteter Basisversionen und Schreibzuständigkeit außerhalb des Modells. Eine regelkonforme Demonstration reicht nicht, wenn das Konto weiterhin uneingeschränkt veröffentlichen darf. Entscheide anhand dieser Tests, ob der Pilot bereit ist.

## Zuerst pilotieren

**Starte das Modell als Entwurf.** Pilotier ein Projekt mit einem Programmierer, einer nicht programmierenden Person und benannten Quellenverantwortlichen. Stelle dieselbe Frage mit bekannter ID in zwei Tools und simuliere anschließend einen Quellenkonflikt. Bewerte Manifeste und Vorschläge, nicht die sprachliche Eleganz.

**Erwartete Begründung:** Beide Beteiligten ermitteln die aktuelle freigegebene Anforderung und beschreiben getrennt die geprüfte Implementierung. Bei Abweichungen vergleichen sie zuerst ihre Manifest-Einträge. Das ist eine vorgeschlagene Übung, kein beobachteter Benchmark.

| Kennzahl | Definition |
|---|---|
| **Zitierrate** | Quellenbelegte wesentliche Aussagen geteilt durch wesentliche Tatsachenbehauptungen in Stichproben |
| **Wöchentliche Drift-Feststellungen** | Bestätigte Autoritäts- oder Versionsabweichungen nach Quelltyp gruppiert |
| **Bearbeitungszeit von Vorschlägen** | Median von prüfbereitem Vorschlag bis dokumentierter Entscheidung |
| **Nacharbeit durch veralteten Kontext** | Wiedereröffnete Aufgaben wegen veralteter oder ungeprüfter Belege |

**Miss zuerst den Ausgangswert.** Mehr Drift-Feststellungen in der ersten Woche können bessere Erkennung statt schlechterer Dokumentation bedeuten. Verfolge Wiederholungen und Lösungszeit neben der Rohzahl. Prüfe sensible Belege, ohne sie in Analyseexporte zu kopieren.

**Liefere während des Rollouts ein Beispiel-Repository.** Füge synthetische Karte, Richtlinienadapter, Manifeste, Vorschlagsvorlagen, Dokumentationsausnahmen und ausführbare Prüfungen hinzu. Verwende erfundene Wiki- und Tracker-Datensätze ohne Produktionszugänge. Zeige verweigerte Veröffentlichung, Ablehnung einer geänderten Basis, Richtlinienversionsdrift und eine erfolgreiche Übergabe.

**Ein Vorlagen-Repository ist ein Rollout-Ergebnis**, kein Bestandteil dieses Artikels. Überführe das Betriebsmodell nach Prüfung der Pilot-Ergebnisse durch Leitung und Quellenverantwortliche in den nächsten Schritt. Halte Ausnahmen und ungelöste Fehler im Entscheidungsregister fest. Behebe vor der Ausweitung die vorhersehbaren Probleme unten.

## Probleme mit gemeinsamem Kontext beheben

| Symptom | Erste Maßnahme |
|---|---|
| **Zwei Tools antworten unterschiedlich** | Vergleiche Quell-IDs, Revisionen, Geltungsbereich und Freigabestatus |
| **Anweisungen wirken aktuell, das Verhalten weicht ab** | Prüfe geladene Adapter, Regelschalter und lokale Überschreibungen |
| **RAG liefert alte Anforderungen** | Prüfe die Indexaktualisierung und rufe die Live-Seite ab |
| **Eine Wiki-Änderung löscht eine andere** | Fordere bedingte Updates oder serielle Veröffentlichung |
| **Dokumentationsprüfungen bestehen mit veraltetem Wortlaut** | Ergänze Eigentümerprüfung und Anforderungsabgleich |
| **Entscheidungen bleiben im Chat** | Weise Vorschlagseingang und Registerverantwortung zu |

**Repariere den Belegpfad, bevor du den Prompt umschreibst.** Führe anschließend den fehlgeschlagenen Pilotfall erneut aus und halte das Ergebnis fest. Nutze die Checkliste, um den korrigierten Ablauf jede Woche zu wiederholen.

## Zehn Schritte für diese Woche

1. **Wähle ein Pilotprojekt** und die beteiligten Personen und Tools.
2. **Weise jedem Informationstyp einen Ort und Verantwortlichen zu.**
3. **Veröffentliche eine Projektkarte** mit Quell-IDs und Autoritätsbereichen.
4. **Entwirf eine gemeinsame Richtlinie** und hole die Prüfung des Eigentümers ein.
5. **Versioniere jeden Anweisungsadapter** in Zeile eins und prüfe, ob er geladen wird.
6. **Verlange ein Kontextmanifest** für wesentliche Faktenantworten und Vorschläge.
7. **Erstelle einen Eingangskanal für Vorschläge** mit Basisversionen und benannten Freigebenden.
8. **Erzwinge Schreibkontrollen und die Same-PR-Dokumentationsregel.**
9. **Teste Drift, Konflikte und Übergaben** mit synthetischen Datensätzen.
10. **Prüfe Pilotkennzahlen** und gib die nächste Rollout-Stufe frei.

**Gib jeder Tatsache einen festen Ort, lass jedes Tool daraus lesen und leite jede dauerhafte Änderung über einen Menschen.**

## Referenzen und nächste Schritte

**Die offizielle Dokumentation stützt die technischen Komponenten**, nicht die organisatorischen Regeln des Modells. Prüfe während des Piloten das Verhalten installierter Tools und die Connector-Berechtigungen.

- **Codex-Anweisungen:** [Benutzerdefinierte Anweisungen mit AGENTS.md](https://developers.openai.com/codex/guides/agents-md), zur Erkennung und Prüfung von Anweisungen.
- **Claude-Code-Anweisungen:** [Wie Claude sich an dein Projekt erinnert](https://code.claude.com/docs/en/memory), zu Projektanweisungen und Gedächtnis.
- **Cline-Anweisungen:** [Regeln](https://docs.cline.bot/customization/cline-rules), zu Arbeitsbereichsregeln und Aktivierungssteuerung.
- **Retrieval-Design:** [RAG in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), zu Grounding, Abrufgrenzen und Sicherheit.
- **Connector-Sicherheit:** [MCP-Sicherheitsrichtlinien](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices), zu Autorisierung und Connector-Risiken.
- **Worktree-Isolation:** [Git-Worktree-Dokumentation](https://git-scm.com/docs/git-worktree), zu getrennten Arbeitsverzeichnissen und gemeinsamem Repository-Zustand.

**Für die Planung lokaler Inferenz** lies den [Leitfaden zum GPU-Kontext für lokale KI](/articles/local-ai-model-gpu-context-guide/). Hardwarekapazität und die Verwaltung gemeinsamer Quellen lösen unterschiedliche Probleme. Ein größeres Kontextfenster behebt keine widersprüchliche Autorität.

{{< centerbutton href="/articles/local-ai-model-gpu-context-guide/" >}}
  Lies den Leitfaden zum Kontext lokaler KI
{{< /centerbutton >}}

---
title: "9 AI-Agent-Skill-Projekte für Forschung, Design und Entwicklung"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Vergleiche neun Agent-Skill-Projekte nach Arbeitsablauf, Host-Unterstützung, Abhängigkeiten und Kosten. Lerne, die benötigten Skills zu installieren, zu prüfen und zu testen."
genre: ["Künstliche Intelligenz", "Entwicklerwerkzeuge", "Softwareentwicklung"]
tags: ["AI agent skills", "Codex skills", "Claude Code skills", "last30days", "Impeccable", "gstack", "Superpowers", "Claude Video", "Humanizer", "NVIDIA SkillSpector", "HyperFrames", "Remotion", "SKILL.md", "Agenten-Workflows", "Skill-Installation", "Skill-Sicherheit", "KI-Forschung", "Frontend-Design", "Videogenerierung", "Entwicklungs-Workflows", "Agentenanpassung"]
cover: "/img/cover/agent-skill-workflow-library.webp"
coverAlt: "Elfenbeinfarbene Anleitungskarten in einer Ablage neben einer Lupe, Farbfächern und einer kleinen Filmrolle auf einem dunklen Tisch"
coverCaption: "Konzeptionelle Illustration einer aufgabenbezogenen Agent-Skill-Bibliothek."
---

**Installiere einen Agent-Skill für eine wiederkehrende Aufgabe.** Die Recherche aktueller Diskussionen, die Prüfung von Interface-Design und das Rendern eines Videos benötigen unterschiedliche Abläufe und Abhängigkeiten. Ein nützlicher Skill liefert fehlende Anweisungen, Referenzmaterial oder Skripte für eine dieser Aufgaben.

**Neun Projekte verdienen Aufmerksamkeit:** last30days, Humanizer, Impeccable, Superpowers, gstack, Claude Video, Remotion, HyperFrames und NVIDIA SkillSpector. Einige sind Anweisungspakete, einige enthalten ausführbare Werkzeuge und einige sind Frameworks mit ergänzenden Skills. Dieser Leitfaden vergleicht ihre dokumentierten Rollen und bietet eine praktische Auswahl-, Installations- und Bewertungsmethode.

**Dokumentationsstand: 10. Oktober 2026.** Die Empfehlungen beruhen auf Projektdokumentation und Quellcodeprüfung, nicht auf einem Vergleichsbenchmark der Ausgabequalität. Eine kostenlose Installation beweist keine kostenlose Inferenz, kein kostenloses Rendering, keinen kostenlosen Datenzugriff und keine kostenlose kommerzielle Nutzung.

<!--more-->

## Wichtigste Erkenntnisse

- **Beginne mit einer wiederkehrenden Aufgabe:** Wähle einen Skill mit klarem Ergebnis und einer Akzeptanzprüfung.
- **Trenne Skills von Runtimes:** Die Installation von Anweisungen installiert nicht jedes benötigte ausführbare Programm.
- **Prüfe den Host:** Eine funktionierende Claude-Code-Integration beweist kein identisches Verhalten in Codex oder Cowork.
- **Prüfe Berechtigungen und Abhängigkeiten:** Paketbefehle, Hooks, externe Dienste und Zugangsdaten brauchen eigene Prüfungen.
- **Passe erst nach dem Test an:** Die Projektregeln bleiben maßgeblich. Halte Upstream-Versionen fest.

## Nach Ergebnis auswählen

| Benötigte Ausgabe | Zu prüfendes Projekt | Erste Prüfung |
|---|---|---|
| **Aktueller Diskussionsbrief** | last30days | Welche Quellen lieferten verwertbare Belege? |
| **Bearbeitete Prosa** | Humanizer | Sind Bedeutung und Zuordnung erhalten geblieben? |
| **Verbesserte Oberfläche** | Impeccable | Funktioniert die überarbeitete Interaktion? |
| **Geplante und getestete Änderung** | Superpowers | Passt der Prozess zur Aufgabenkomplexität? |
| **Review- und QA-Workflow** | gstack | Welche Funktionen arbeiten auf deinem Agent-Host? |
| **Videobeobachtungen** | Claude Video / Watch | Stützen Bild oder Ton die Aussagen? |
| **React-Videokomposition** | Remotion skills | Entspricht das exportierte Video der Vorschau? |
| **HTML-Videokomposition** | HyperFrames skills | Ist die Animation beim Springen deterministisch? |
| **Skill-Prüfbericht** | SkillSpector | War die Analyse vollständig, und was wurde markiert? |

**Ein Skill unterscheidet sich von einem Agent-Harness.** Ein Skill liefert aufgabenspezifische Hinweise und manchmal Skripte. Der Harness bestimmt, wie der Agent Anweisungen lädt, Werkzeuge aufruft und Berechtigungen erzwingt. Unsere [Agent-Harness-Vergleichsseite](/articles/best-ai-agent-harnesses/) behandelt diese umgebenden Systeme.

**Ein Skill-Ordner ist ebenfalls keine Plugin-Installation.** Plugins registrieren manchmal Hooks oder zusätzliche Werkzeuge, die eine manuelle Ordnerkopie nicht enthält. Lies die Anweisungen für deinen Host und Installationsmodus, bevor du gleiches Verhalten annimmst.

## Forschung und Schreiben

### last30days

**Nutze last30days für die Recherche aktueller Diskussionen.** Das [Projekt](https://github.com/mvanhorn/last30days-skill) verbindet Quellen wie Reddit, Hacker News, YouTube, X und das Web. Die verfügbare Abdeckung hängt von ausgewählten Quellen, installierten Werkzeugen, Authentifizierung und Providerzugang ab. Der Preflight-Modus beschreibt den geplanten Zugriff und schreibt Ergebnisse, ohne die Recherche zu starten.

**Fordere eine Belegspur an.** Ein nützliches Ergebnis enthält Daten, Links, wiederkehrende Beschwerden und Widersprüche. Eine nicht verfügbare Quelle muss als Abdeckungslücke erscheinen. Interaktionszahlen beschreiben die Aktivität der gesammelten Beiträge, keine repräsentative Befragung aller Nutzer.

**Beispielaufgabe:** Untersuche wiederkehrende Installationsfehler einer kürzlich veröffentlichten Bibliothek. Gruppiere Berichte nach Version und Betriebssystem. Prüfe vorgeschlagene Lösungen anschließend mit dem Issue-Tracker oder der Dokumentation der Bibliothek. Behandle einen beliebten Workaround nicht als vom Upstream unterstützte Lösung.

### Humanizer

**Nutze Humanizer als Redigierdurchgang.** Der [Skill](https://github.com/blader/humanizer) zielt auf wiederholte Kontraste, inszenierte Einleitungen, übertriebene Aussagen und weitere Schreibgewohnheiten. Er nimmt Sprachproben an und soll die zugrunde liegende Bedeutung bewahren.

**Liefere die Einschränkungen mit dem Entwurf.** Benenne Zielgruppe, unveränderliche Fakten und verknüpfte Zitate. Vergleiche nach der Bearbeitung die Tatsachenbehauptungen mit dem Original. Besserer Rhythmus bestätigt keine unbelegte Statistik.

| Schreibprüfung | Bestandenes Ergebnis |
|---|---|
| **Bedeutung** | Gleiche Aussagen, Einschränkungen und Reichweite |
| **Quellen** | Die Zuordnung bleibt nahe an übernommenen Ergebnissen |
| **Stimme** | Passt zu Zielgruppe und gelieferten Beispielen |
| **Originalität** | Fügt eigenes Denken hinzu statt kopierte Prosa zu tarnen |

**Nutze die Projekte in unterschiedlichen Phasen.** last30days sammelt Material für Untersuchungen. Humanizer bearbeitet den Ausdruck. Keiner ersetzt Quellenprüfung oder eigenständige Autorenschaft.

## Interface- und Entwicklungsarbeit

### Impeccable

**Nutze Impeccable für gezielte Designarbeit.** [Website](https://impeccable.style/) und [Repository](https://github.com/pbakaus/impeccable) dokumentieren einen Design-Workflow für Kritik, Typografie, Layout, Verständlichkeit, Bewegung und Feinschliff. Beginne mit einem konkreten Nutzerproblem statt mit der vagen Bitte um eine beeindruckendere Seite.

**Beispielbriefing:** Mache eine Abonnement-Einstellungsseite leichter erfassbar, ohne Kündigung zu verstecken oder Tastaturnavigation zu ändern. Fordere zuerst eine Kritik an und setze danach ausgewählte Änderungen um. Prüfe anschließend mobiles Layout, Fokusreihenfolge, Kontrast und Erfüllung der ursprünglichen Aufgabe.

**Der Installationsmodus ist wichtig.** Die aktuellen Codex-Anweisungen unterscheiden Skill und lokalen Design-Hook. Hook-Vertrauen braucht eine eigene Zustimmung in Codex. Eine kopierte Skill-Datei beweist keinen aktiven Hook.

### Superpowers

**Nutze Superpowers für einen strukturierten Entwicklungsprozess.** Das [Repository](https://github.com/obra/superpowers) bündelt Workflows für Brainstorming, Planung, Tests, Fehlersuche und Review. Es dokumentiert auch hostbezogene Plugin-Installation einschließlich Codex.

**Passe den Prozess an die Aufgabe an.** Eine Funktion über Datenspeicherung, UI und Tests profitiert von einem ausdrücklichen Plan. Eine Rechtschreibkorrektur braucht deutlich weniger Ablauf. Definiere den erlaubten Umfang, damit ein allgemeiner Entwicklungsprozess eine kleine Anfrage nicht auf benachbarte Arbeit ausweitet.

**Projektanweisungen gelten weiterhin.** Testmethode, Worktree-Ansatz oder Delegationsmuster des Skills müssen zu Repository und Nutzerwunsch passen. Die Installation einer Methodik erlaubt nicht jede darin beschriebene Aktion.

### gstack

**Nutze gstack für einen breiteren Engineering-Workflow mit ausführbaren Werkzeugen.** Die [Dokumentation](https://github.com/garrytan/gstack) enthält Skills für Planung, Review, Browser-QA, Untersuchung und Release. Die Installation baut Hilfswerkzeuge statt nur Text zu kopieren.

**Codex-Unterstützung ist derzeit experimentell.** Das Projekt unterscheidet hook-erzwungene Sicherheitsfunktionen von Claude Code und hinweisgebendem Verhalten in Codex. Nimm nicht an, dass ein gleichnamiger Befehl auf allen Hosts gleich durchsetzt.

**Meine Auswahlregel:** Probiere Superpowers, wenn ein wiederholbarer Entwicklungsprozess fehlt. Probiere gstack, wenn seine konkreten Review- oder Browser-Werkzeuge ein aktuelles Problem lösen. Wenn beide installiert sind, wähle pro Aufgabe einen Hauptprozess und nutze den anderen für einen benannten Beitrag.

| Entwicklungsproblem | Nützliche Bewertungsaufgabe |
|---|---|
| **Unklarer Umfang** | Erstelle einen begrenzten Plan mit Akzeptanzkriterien |
| **Fragile Umsetzung** | Behebe eine vorbereitete Regression und bewahre bestehendes Verhalten |
| **Defekte Interaktion** | Reproduziere einen Browserfehler und bewahre Belege |
| **Widersprüchliche Workflows** | Bestätige, dass nur der gewählte Prozess die Aufgabe steuert |

## Videobelege und Produktion

### Claude Video / Watch

**Nutze Claude Video, um Belege aus einem Video zu sammeln.** Trotz des Repositorynamens unterstützt die [Watch-Skill](https://github.com/bradautomates/claude-video) lokale Agenten wie Codex. Die lokale Route nutzt Downloads, abgetastete Frames und Untertitel oder Transkription. Eine getrennte Gemini-Route sendet das Video zur Analyse, wenn sie eingerichtet ist.

**Prüfe die aktuelle Host-Unterstützung.** Das README führt Claude Chat und Cowork als nicht unterstützt auf. Lokale Ausführung benötigt Medienwerkzeuge wie FFmpeg und yt-dlp. Einzelne Websites begrenzen den Zugriff zusätzlich.

**Trenne Bild- und Tonaussagen.** Ein Transkript belegt gesprochene Worte. Frames belegen sichtbare Details zu abgetasteten Zeitpunkten. Keines belegt ein unsichtbares Ereignis zwischen den Samples. Fordere Zeitstempel und offene Beobachtungen, statt ohne Einschränkung zu behaupten, die ganze Aufnahme verstanden zu haben.

### Remotion

**Nutze Remotion für in React geschriebene Videokompositionen.** Das [Framework-Repository](https://github.com/remotion-dev/remotion) verweist auf eine getrennte [Agent-Skill-Sammlung](https://www.remotion.dev/docs/ai/skills). Sie deckt Projekterstellung, Markup, Karten, Untertitel, Studio und Rendering ab. Ihre Installation erstellt kein Videoprojekt und installiert nicht alle Projektabhängigkeiten.

**Prüfe die Lizenz unabhängig vom Skill-Download.** Die [Remotion-Preisseite](https://www.remotion.dev/docs/license/pricing) nennt eine kostenlose Lizenz für Einzelpersonen und Unternehmen bis drei Personen sowie Unternehmenslizenzen für größere Organisationen und bestimmte Kooperationen. Prüfe die aktuellen Bedingungen für deinen Einsatz.

### HyperFrames

**Nutze HyperFrames für HTML-basierte Videokomposition.** Das [Repository](https://github.com/heygen-com/hyperframes) beschreibt das Rendern von HTML, CSS, Medien und springbarer Animation nach MP4. Die veröffentlichten Skills führen durch Komposition, Vorschau, Validierung und Rendering.

**Beginne mit dem dokumentierten Kernset.** Die aktuelle Installationsanleitung unterscheidet Kern-Skills, größere veröffentlichte Sammlung und repositoryinterne Skills. Eine wahllose Installation jedes Ordners fügt fremde Anweisungen hinzu und erschwert Pflege.

| Video-Workflow | Wichtige Akzeptanzprüfung |
|---|---|
| **Watch** | Zeitmarkierte Beobachtungen stimmen mit geprüften Medien überein |
| **Remotion** | Der Export bewahrt Timing, Schriften, Audio und Layout |
| **HyperFrames** | Das Anspringen eines Frames erzeugt den vorgesehenen visuellen Zustand |

**Wähle mit einer kontrollierten Probe.** Gib Remotion und HyperFrames dasselbe Briefing, dieselben Assets, dieselbe Dauer und dieselben Ausgabeabmessungen. Animieren Sie etwa einen dreistufigen Wartungsvorgang mit Untertiteln und einem Diagramm. Vergleiche exportierte Dateien, Bearbeitungsaufwand und Renderfehler. Eine attraktive Demo beweist keinen allgemeinen Sieger.

## Mit SkillSpector prüfen

```bash
skillspector scan ./downloaded-skill --no-llm --format json --output report.json
```

**NVIDIA SkillSpector ist ein Scanner, kein Video- oder Schreib-Skill.** Das [Projekt](https://github.com/NVIDIA/SkillSpector) dokumentiert statische Prüfungen und optionale modellgestützte Analyse für Agent-Skill-Pakete. Der Befehl setzt ein installiertes CLI voraus und scannt einen lokalen Ordner, ohne den Ziel-Skill auszuführen.

**Lies Ergebnisse und Abdeckung zusammen.** Prüfe markierte Dateien und umgebenden Code. Halte anschließend fest, welche Prüfungen abgeschlossen sind. Ein unvollständiger Scan darf kein sauberes Urteil werden. Auch ein Schlüsselworttreffer braucht Kontext: Ein dokumentiertes öffentliches Karten-Token eines Providers unterscheidet sich von Code, der fremde Zugangsdaten sammelt.

**Statisch bedeutet nicht vollständig offline.** Laut Projekt gehen Abhängigkeitsnamen und Versionen mit **`--no-llm`** zur Schwachstellensuche an OSV. Die Modellanalyse sendet zusätzlich geeignete Dateiinhalte an den konfigurierten Provider. Wähle den passenden Modus für das Prüfmaterial.

**Nutze den Bericht als Entscheidungsbeleg.** Erkläre, ob jeder Fund für die Aufgabe nötig ist, welche Daten das Gerät verlassen und welche Autorität die Laufzeit gewährt. Ein niedriger Wert beweist keine Sicherheit. Ein guter Ruf erklärt keinen ungeklärten Fund.

## Das richtige Paket installieren

**Ermittle zuerst die kanonische Skill-Distribution.** Remotion-Framework und Skills liegen in verschiedenen Repositories. Claude Video stellt einen Skill namens Watch bereit. SkillSpector wird als CLI installiert, die Agent-Integration separat. Deshalb reicht das Klonen eines Projekts nicht immer.

**Die folgenden Beispielbefehle stammen aus der aktuellen Installationsdokumentation der Projekte.** Führe nur den Befehl des ausgewählten Projekts aus. Der Paket-Runner lädt Installationscode und führt ihn aus. Prüfe daher das Upstream-Projekt und wähle den Umfang vor dem Start.

```bash
# Humanizer: user-wide Codex installation
npx skills add blader/humanizer --global --agent codex

# last30days: user-wide Codex installation
npx skills add mvanhorn/last30days-skill -g -a codex

# Remotion: official skill collection, not the framework repository
npx skills add remotion-dev/skills
```

**Der dritte Befehl öffnet den Installationsablauf.** Wähle Agent und Umfang bewusst, statt anzunehmen, dass die Standardwerte zu den explizit begrenzten Befehlen passen. Plugin-Installer und eigenständige Ordnerinstallationen haben ebenfalls unterschiedliche Update-Mechanismen.

**Bewahre vorhandene Installationen.** Prüfe vor dem Ersetzen Version, lokale Änderungen und Manager. Halte keine konkurrierenden Kopien in Benutzer-, Projekt- und Pluginpfaden, außer der Host dokumentiert die Auflösung.

| Installationsstatus | Was er festlegt |
|---|---|
| **Dateien vorhanden** | Anweisungen und referenzierte Assets existieren |
| **Host erkennt Skill** | Der Agent erkennt Name und Beschreibung |
| **Abhängigkeiten bereit** | Benötigte Executables und Pakete sind verfügbar |
| **Aufgabe geprüft** | Ein repräsentatives Ergebnis besteht unabhängige Prüfungen |

**Prüfe jede Stufe in Reihenfolge.** Eine erfolgreiche Ordnerkopie ist eine Installationsprüfung, kein Beleg für funktionierenden Browser, Download, Transkription oder Rendern. Halte optionale Provider-Einrichtung von der Basisinstallation getrennt und speichere keine Zugangsdaten in Skill-Dateien.

**Notiere Host und Revision für jeden Versuch.** Halte fest, ob der Skill über Claude Code, Codex, Cowork oder einen anderen Host läuft. Speichere Upstream-Commit oder Paketversion mit dem Akzeptanzergebnis. Ähnliche Namen beweisen keine identische Erkennung, Hooks, Berechtigungen oder Werkzeugnutzung.

## Vor der Anpassung testen

**Nutze eine gespeicherte Aufgabe als Basis.** Führe sie ohne den neuen Skill aus und danach mit ihm. Halte Modell, Eingabe, Werkzeuge und Akzeptanzkriterien nach Möglichkeit konstant. Zeichne Fehler und menschliche Korrekturen zusammen mit dem Endergebnis auf.

```yaml
# Illustrative evaluation record, not a skill configuration schema
job: "review a settings page"
input: "same source revision and test data"
variants:
  - "agent without the selected skill"
  - "same agent with the selected skill"
acceptance:
  - "required actions remain visible"
  - "keyboard navigation works"
  - "mobile layout remains usable"
record:
  - "skill source and revision"
  - "model and enabled tools"
  - "completed checks and retained evidence"
  - "elapsed time and manual corrections"
  - "external service usage"
```

**Passe den wiederkehrenden Fehler an, nicht das ganze Paket.** Wenn Recherche-Zusammenfassungen widersprüchliche Belege verlieren, ergänze eine Anforderung für abweichende Quellen. Wenn ein Design-Durchgang etablierte Farben ändert, verweise auf Design-Tokens. Wenn Untertitel überlaufen, ergänze eine Prüfung der Exportauflösung.

**Halte lokale Ergänzungen nachvollziehbar.** Notiere Upstream-Revision, Änderungen und auslösende Aufgabe. Aktualisierungen brauchen einen weiteren Versuch, weil neue Trigger, Skripte oder Abhängigkeiten den früher bewerteten Ablauf verändern.

**Achte auf überlappende Anweisungen.** Entwicklungs-Suites, Design-Skills und Prosa-Editoren bringen Präferenzen mit. Repositoryregeln und Nutzerwunsch lösen Konflikte. Ein Stil-Skill darf Barrierefreiheitslabels, Zitate oder technische Begriffe nicht nur zur Variation entfernen.

## Eine nützliche Bibliothek aufbauen

**Beginne mit der häufigsten Aufgabe.** Ein Autor probiert vielleicht last30days und Humanizer. Ein Frontend-Entwickler beginnt vielleicht mit Impeccable und einem Entwicklungsworkflow. Ein Videoproduzent wählt ein Produktionsframework und ergänzt Watch, wenn Quellvideoanalyse Teil der Aufgabe ist.

**Plane Betrieb getrennt von Installation.** Berücksichtige Modellaufrufe, optionale Suchanbieter, Transkription, Medienerzeugung, Rendering-Infrastruktur und passende Lizenzen. Ein kostenloses Repository beantwortet nur einen Teil der Kostenfrage.

**Vor dem ersten Versuch:** Bereite genehmigten Modellzugang, ein Wegwerfprojekt oder Beispieleingabe und schriftliche Akzeptanzkriterien vor. Grundlegende Anweisungsskills sind anfängerfreundlich. Browserwerkzeuge, Medienabhängigkeiten und Cloud-Rendering brauchen mehr Einrichtung. Plane eine Stunde für einen begrenzten Versuch und wiederhole ihn mit repräsentativen Eingaben, bevor du den Ablauf dauerhaft verwendest.

**Behalte Skills mit nachgewiesenem Wert.** Bewahre Skills, die vergessene Schritte oder Reviewaufwand reduzieren. Entferne Duplikate mit widersprüchlichem Verhalten. Prüfe Hostkompatibilität und Abhängigkeiten erneut, wenn sich die Agentenumgebung ändert.

{{< youtube id="3fdb_giOrLo" enable="true" title="9 Free AI Agent Skills You NEED to Install Now" >}}

## Quellen

- [last30days: Research-Skill und Installation](https://github.com/mvanhorn/last30days-skill)
- [Humanizer: Schreib-Skill](https://github.com/blader/humanizer)
- [Impeccable: Design-Workflow](https://impeccable.style/)
- [Impeccable: Repository und hostbezogene Einrichtung](https://github.com/pbakaus/impeccable)
- [Superpowers: Entwicklungs-Skills](https://github.com/obra/superpowers)
- [gstack: Engineering-Werkzeuge und Host-Unterstützung](https://github.com/garrytan/gstack)
- [Claude Video: Watch-Skill und Laufzeitanforderungen](https://github.com/bradautomates/claude-video)
- [Remotion: React-Videoframework](https://github.com/remotion-dev/remotion)
- [Remotion: Agent-Skills](https://www.remotion.dev/docs/ai/skills)
- [Remotion: Lizenz und Preise](https://www.remotion.dev/docs/license/pricing)
- [HyperFrames: Framework und Skill-Distribution](https://github.com/heygen-com/hyperframes)
- [NVIDIA SkillSpector: Scannerverhalten und Datenverarbeitung](https://github.com/NVIDIA/SkillSpector)
- [Futurepedia: 9 kostenlose AI-Agent-Skills, die du installieren solltest](https://www.youtube.com/watch?v=3fdb_giOrLo)

---
title: "ATS Resume Improver: Kostenloser, selbst hostbarer KI-Lebenslauf-Optimierer ohne Datenweitergabe"
date: 2026-07-22
toc: true
draft: false
description: "ATS Resume Improver ist ein kostenloser, quelloffener, clientseitiger Lebenslauf-Optimierer, der OpenAI, Anthropic Claude und lokale Ollama-Modelle unterstützt. Parsen, bewerten, Keywords abgleichen, optimieren und exportieren Sie Ihren Lebenslauf, ohne dass Ihre Daten den Browser verlassen."
genre: ["Karriere-Tools", "Open-Source-Projekte", "Künstliche Intelligenz", "Datenschutztechnologie", "Entwickler-Tools", "Jobsuche", "Produktivität"]
tags: ["ATS Resume Improver", "ATS-Optimierung", "Lebenslauf-Scanner", "KI-Lebenslauf", "OpenAI Lebenslauf", "Claude Lebenslauf", "Ollama lokale KI", "Selbst gehostet", "Datenschutz zuerst", "Job-Such-Tools", "Keyword-Lückenanalyse", "Anschreiben", "Lebenslauf-Bewertung", "React", "TypeScript", "Docker", "Vite", "Open Source", "PDF-Export", "DOCX-Export", "Lebenslauf-Parser", "Karriere-Tools", "Bewerbungsvorbereitung", "Gehaltsschätzer", "Lebenslauf-Typ-Erkennung", "ATS-Score", "kostenloses Lebenslauf-Tool", "GitHub", "keine Datenerhebung"]
cover: "/img/cover/ai-resume-optimizer-self-hosted-ats-analysis.webp"
coverAlt: "Ein moderner Laptop auf einem Schreibtisch zeigt eine farbenfrohe Benutzeroberfläche zur Lebenslauf-Optimierung mit Grafiken und Diagrammen auf einem tiefen marineblauem Hintergrund."
coverCaption: "ATS Resume Improver — 100% clientseitige Lebenslaufanalyse und KI-Optimierung ohne Datenerhebung."
canonical: "https://simeononsecurity.com/articles/ats-resume-improver-ai-powered-resume-optimizer/"
---

**Kostenlos, quelloffen und selbst hostbar. Ihr Lebenslauf berührt keinen Server, es sei denn, Sie verwenden einen KI-Anbieter. Und selbst dann geht er direkt zum KI-Anbieter, nicht zu uns.**

## Was ist ATS Resume Improver?

**[ATS Resume Improver](https://atsresumeimprover.netlify.app/)** ist ein quelloffener, browserbasierer Lebenslauf-Optimierer, der Ihren Lebenslauf mit einer Stellenbeschreibung vergleicht und Ihnen hilft, die Lücke zwischen dem, was Sie haben, und dem, was Bewerber-Tracking-Systeme tatsächlich bewerten, zu schließen. Die App basiert auf React 19, Vite und TypeScript. Die gesamte **Analyse- und Bewertungs-Pipeline läuft in Ihrem Browser** ohne Backend-Server.

Den Quellcode finden Sie unter **[github.com/simeononsecurity/ats-resume-improver](https://github.com/simeononsecurity/ats-resume-improver)**. Sie können die gehostete Version nutzen, Ihre eigene in einem Klick auf Vercel/Netlify/Cloudflare/GitHub Pages deployen oder lokal mit Docker starten.

### Das Datenschutzproblem, das es löst

Die meisten Lebenslauf-Optimierungsdienste laden Ihren Lebenslauf auf ihre Server hoch, führen proprietäre Bewertungen durch und behalten Ihre Daten. ATS Resume Improver verfolgt den gegenteiligen Ansatz.

| Modus | Was Ihr Gerät verlässt |
|------|------------------------|
| **Kein KI-Schlüssel** | Nichts — 100% lokal, läuft in Ihrem Browser |
| **OpenAI / Anthropic** | Lebenslauftext + Stellenbeschreibung gehen direkt an die KI-Anbieter-API mit Ihrem Schlüssel — kein Zwischenserver |
| **Ollama (lokal)** | Nichts — Modell läuft auf Ihrem eigenen Rechner |

**API-Schlüssel werden nur im Arbeitsspeicher gespeichert** und verschwinden, wenn Sie den Tab schließen. Keine Analysen, kein Tracking, keine Cookies.

______

## Kernfunktionen

### Was ohne KI-Schlüssel funktioniert

Sie brauchen keinen API-Schlüssel, um echten Mehrwert zu erhalten. Der Modus ohne Schlüssel umfasst:

- **Lebenslauf-Upload** — PDF, DOCX, TXT oder Markdown
- **ATS-Textextraktion** — zeigt genau, was ein ATS aus Ihrer Datei parst, einschließlich was durch Formatierung verloren geht
- **Lebenslauf-Typ-Erkennung** — erkennt automatisch, welchem der 7 Profile Ihr Lebenslauf entspricht, und passt die Absatzreihenfolge entsprechend an
- **Abschnitts-Erkennung und Formatierungswarnungen** — kennzeichnet fehlende Abschnitte und parser-feindliche Formate
- **ATS-Score (0–100)** mit einer 5-dimensionalen Aufschlüsselung
- **Keyword-Lückenanalyse** — regelbasierter String-Abgleich mit der Stellenbeschreibung
- **Deterministische ATS-Optimierung** — lokale regelbasierte Umstrukturierung
- **Vorher/Nachher-Diff-Ansicht** — sehen Sie genau, was sich geändert hat
- **Professioneller PDF-, DOCX-, TXT- und Markdown-Export**

### Was KI freischaltet

Verbinden Sie OpenAI, Anthropic Claude oder lokales Ollama, und das Tool wird zu:

- **Semantische Keyword-Analyse** — versteht Kontext, nicht nur String-Matches. Zeigt Übereinstimmungsstärke (Stark/Mittel/Teilweise), Übereinstimmungsort ("in Skills und 3 Job-Rollen gefunden"), Relevanz pro Keyword (Kritisch/Hoch/Mittel/Niedrig) und eine 2-3-Satz-KI-Zusammenfassung
- **KI-Lebenslauf-Optimierung** — vollständige KI-Überarbeitung mit ATS-Best-Practice-Prompts
- **KI-verbesserte Exporte** — PDF/DOCX durch KI vor dem Download formatiert
- **Anschreiben-Generierung** — mit Humanisierungsregeln, die KI-Verräter eliminieren (siehe unten)
- **Interview-Fragen-Vorhersage** — basierend auf der Stellenbeschreibung
- **Gehaltsbereichschätzer**

______

## Lebenslauf-Typ-Erkennung

Die App klassifiziert Ihren Lebenslauf automatisch in eines von 7 Profilen und passt die Abschnittsreihenfolge an die Recruiter- und ATS-Erwartungen für diese Karrierephase an:

| Profil | Beste Verwendung | Abschnittspriorität |
|---------|----------|-----------------|
| 🏢 **Erfahrener Profi** | 5+ Jahre, linearer Werdegang | Erfahrung → Skills → Ausbildung |
| 🌱 **Mittlere Ebene** | 2–5 Jahre | Erfahrung → Skills → Ausbildung |
| 🎓 **Einsteiger** | 0–2 Jahre | Skills → Ausbildung → Projekte → Erfahrung |
| 🎒 **Student / Absolvent** | Noch eingeschrieben | Ausbildung → Projekte → Skills → Erfahrung |
| 🔬 **Akademiker / Forscher** | PhD, Publikationen | Ausbildung → Forschung → Publikationen → Erfahrung |
| 📜 **Zertifizierungsschwerpunkt** | Zertifikate überwiegen Abschluss | Zertifizierungen → Skills → Erfahrung → Ausbildung |
| 🔄 **Karrierewechsler** | Lücke oder Pivot erkannt | Zusammenfassung → Übertragbare Skills → Ausbildung → Erfahrung |

*Die Abschnittsreihenfolge gilt konsistent über Optimierung, PDF-, DOCX-, TXT- und Markdown-Export — nicht nur auf dem Bildschirm.*

______

## KI-semantische Keyword-Analyse

Hier trennt sich das Tool von einfachen Keyword-Zählern. Wenn ein KI-Anbieter konfiguriert ist, steigt die Keyword-Lückenanalyse von einfachem String-Matching auf semantisches Denken:

| Dimension | Ohne KI | Mit KI |
|-----------|-----------|---------|
| **Abgleichmethode** | Nur exakter String-Match | Semantisches Kontextverständnis |
| **Übereinstimmungsstärke** | — | Stark / Mittel / Teilweise |
| **Übereinstimmungskontext** | — | "in Skills und 3 Job-Rollen gefunden" |
| **Lücken-Wichtigkeit** | Alle Lücken gleich behandelt | Kritisch / Hoch / Mittel / Niedrig |
| **Vorschläge** | Allgemeine Tipps | Pro-Keyword umsetzbare Vorschläge |
| **Abdeckung %** | String-Zahl-basiert | Semantisch gewichtet |
| **Zusammenfassung** | — | 2–3-Satz-KI-Narrativ |

*Lokale regelbasierte Analyse läuft sofort. KI-Ergebnisse bereichern sie asynchron, während Sie überprüfen.*

______

## Unterstützte KI-Anbieter

Alle KI-Aufrufe enthalten ATS-Best-Practice-Prompts aus Harvard OCS und Columbia CCE-Richtlinien.

### OpenAI

| Modell | Beste Verwendung |
|-------|----------|
| **GPT-4.1 mini** (Standard) | Intelligentestes, schnelles und erschwingliches — empfohlen |
| GPT-4o mini | Schnell und erschwinglich klassisch |
| GPT-4.1 | Neuestes GPT-4.1 — präzises Instruktions-Following |
| GPT-4o | Hohe Qualität, Flaggschiff |
| GPT-4 Turbo | Großes Kontextfenster |
| GPT-3.5 Turbo | Schnellstes und günstigstes |

**Geschätzte Kosten**: ~0,002–0,05 $ pro Lebenslaufanalyse.

### Anthropic Claude

| Modell | Beste Verwendung |
|-------|----------|
| **Claude Sonnet 4.5** (Standard) | Schnell und intelligent — empfohlen |
| Claude Opus 4.5 | Fähigstes — beste für komplexe Aufgaben |
| Claude Haiku 4.5 | Schnellstes und günstigstes |
| Claude 3.5 Sonnet | Zuverlässig und gut getestet |
| Claude 3.5 Haiku | Schnell und erschwinglich v3.5 |

### Ollama (lokal / selbst gehostet)

Kein API-Schlüssel erforderlich. Führen Sie das Modell auf Ihrer eigenen Hardware aus. Setzen Sie `OLLAMA_ORIGINS=*`, um Browser-Zugriff zu ermöglichen.

| Modell | Hinweise |
|-------|-------|
| **Llama 3.3** (Standard) | Neuestes Meta Llama — empfohlen |
| Llama 3.2 | Meta Llama 3.2 |
| Mistral 7B | Schnell und fähig |
| Mixtral 8x7B | Mixture of Experts |
| Qwen 2.5 | Alibaba Qwen 2.5 |
| DeepSeek R1 | Starkes Reasoning-Modell |
| Phi-4 | Microsoft Phi-4 |
| Gemma 3 | Google Gemma 3 |

Das lokale Ausführen von Ollama macht das gesamte Tool vollständig offline. Nichts verlässt Ihren Rechner.

______

## Anschreiben-Humanisierung

Der Anschreiben-Generator wendet einen gezielten Schreibstil-Leitfaden an, um die verräterischen Zeichen von KI-generiertem Text zu eliminieren:

- **Keine Gedankenstriche** — das stärkste KI-Verräterzeichen, vollständig entfernt
- **50+ verbotene Wörter und Phrasen**: leverage, utilize, dive deep, delve, embark, game-changer, groundbreaking, cutting-edge, pivotal, tapestry, harness, moreover, in conclusion, it's worth noting, ever-evolving, landscape, testament usw.
- **Kein Markdown im Briefkörper** — keine Fett-Asterisken, Hashtags oder Semikolons
- **Aktive Stimme standardmäßig** — Passiv nur wenn der Akteur genuinement keine Rolle spielt
- **Kontraktionen erforderlich**: "I've", "I'm", "it's"
- **Variierte Satzlänge** — kurze, prägnante Sätze gemischt mit längeren
- **Keine Füller-Opener** — "Es ist wichtig zu bemerken, dass X" → sagen Sie einfach X
- **Konkrete Stellenbeschreibungsdetails in Absatz 1** — beweist, dass das Anschreiben nicht vom Template stammt

*Das Ergebnis liest sich, als ob ein Mensch es geschrieben hat, weil die Regeln das Modell zwingen, wie ein Mensch zu schreiben.*

______

## Export-Qualität

| Format | Was Sie erhalten |
|--------|-------------|
| **PDF** | Professionelle Typografie, Abschnittsregeln, Aufzählungspunkte, Kontakt-Header |
| **DOCX** | Ordentlich strukturiertes Word-Dokument (Packer.toBlob — browser-kompatibel) |
| **TXT** | Sauberer Klartext mit konsistentem Abstand (ATS-sicher) |
| **Markdown** | Strukturiertes `.md` mit Überschriften und Aufzählungslisten |

Mit konfiguriertem KI-Anbieter werden Exporte vor dem Download KI-formatiert (gekennzeichnet mit einem ✨ KI-verbessert-Badge).

______

## Selbst-Hosting-Optionen

### Gehostete Version (ohne Einrichtung)

Verwenden Sie die Live-App unter **[atsresumeimprover.netlify.app](https://atsresumeimprover.netlify.app/)** — kein Konto, keine Anmeldung, keine Kreditkarte.

### Ein-Klick-Cloud-Deployment

| Plattform | Link |
|----------|------|
| **Vercel** | Ein-Klick-Deploy aus dem Repo |
| **Cloudflare Pages** | Ein-Klick-Deploy |
| **Netlify** | Ein-Klick-Deploy |
| **GitHub Pages** | Fork → Einstellungen → Pages → GitHub Actions → automatisches Deploy |

### Lokale Entwicklung

```bash
git clone https://github.com/simeononsecurity/ats-resume-improver
cd ats-resume-improver

make install
make dev           # http://localhost:5173
```

### Docker (empfohlen für reproduzierbare Umgebungen)

```bash
# Entwicklung — Hot-Reload unter http://localhost:5173
make docker-dev

# Produktion — nginx unter http://localhost:8080
make docker-prod

# Dev + Ollama zusammen (vollständiger lokaler KI-Stack)
make docker-dev-with-ollama
```

### Ollama Vollständig-Offline-Stack

```bash
# Ollama-Container starten (Modelle über Neustarts hinweg persistent)
make ollama

# Modell herunterladen
make ollama-pull MODEL=llama3.2

# Dev-App + Ollama nebeneinander starten
make docker-dev-with-ollama
```

Öffnen Sie dann die App, gehen Sie zum API-Schlüssel-Panel, wählen Sie **Ollama (Lokal)**, setzen Sie die URL auf `http://localhost:11434` und wählen Sie ein Modell. Keine Daten verlassen Ihren Rechner.

______

## Tech-Stack

| Schicht | Technologie |
|-------|-----------|
| **Framework** | React 19 + TypeScript |
| **Build** | Vite 8 |
| **Styling** | Tailwind CSS v4 |
| **Icons** | Lucide React |
| **PDF-Parse** | pdfjs-dist |
| **DOCX-Parse** | mammoth |
| **PDF-Export** | jsPDF |
| **DOCX-Export** | docx (Packer.toBlob) |
| **KI** | OpenAI · Anthropic Claude · Ollama |
| **Container** | Docker + nginx (Multi-Stage) + Ollama-Service |

______

## Praktischer Nutzungsleitfaden

### Schritt 1: Laden Sie Ihren Lebenslauf hoch

Laden Sie eine PDF-, DOCX-, TXT- oder Markdown-Datei hoch. Wechseln Sie zum Tab **"Was das ATS sieht"**, um zu prüfen, ob der Parser Ihren Inhalt sauber extrahiert hat.

### Schritt 2: Fügen Sie die Stellenbeschreibung ein

Fügen Sie die vollständige Stellenausschreibung in das Stellenbeschreibungsfeld ein. Vollständigere Stellenausschreibungen produzieren bessere Keyword-Analysen.

### Schritt 3: Überprüfen Sie Ihren ATS-Score

Das Score-Panel zeigt einen Gesamt-Score von 0–100 und eine 5-dimensionale Aufschlüsselung.

### Schritt 4: Prüfen Sie die Keyword-Lücke

Die Keyword-Analyse-Ansicht zeigt, welche Keywords aus der Stellenbeschreibung in Ihrem Lebenslauf erscheinen und welche nicht. Mit aktivierter KI erhalten Sie semantisches Matching und Wichtigkeitsbewertungen.

### Schritt 5: Optimieren

- **Deterministischer Modus**: wendet regelbasierte Umstrukturierung an — sicher, schnell, keine API-Kosten
- **KI-Modus**: vollständige LLM-Überarbeitung mit ATS-Best-Practice-Prompts

### Schritt 6: Exportieren

Exportieren Sie als PDF, DOCX, TXT oder Markdown. Mit aktivierter KI ist der Export KI-formatiert für professionelle Präsentation.

______

## Häufig gestellte Fragen

### Speichert das Tool meinen Lebenslauf?

Nein. Die App ist vollständig clientseitig. Nichts wird auf einem Server gespeichert. Sitzungsdaten leben im Browser-Arbeitsspeicher und verschwinden, wenn Sie den Tab schließen.

### Mein Lebenslauf hat einen niedrigen Score — sollte ich in Panik verfallen?

ATS-Scores sind richtungsweisend, nicht Pass/Fail. Ein Score von 60 bedeutet nicht, dass ein ATS Sie ablehnt. Es bedeutet, dass messbare Lücken zwischen Ihrem Lebenslauf und der analysierten Stellenbeschreibung bestehen.

### Kann ich es mit mehreren Stellenbeschreibungen verwenden?

Ja. Fügen Sie jederzeit eine neue Stellenbeschreibung ein. Die Keyword-Analyse und Optimierung wird erneut für die neue Ausschreibung ausgeführt. Jede Analyse ist unabhängig.

### Ist die Ollama-Integration wirklich offline?

Ja, wenn Ollama auf Ihrem lokalen Rechner oder einem Rechner in Ihrem lokalen Netzwerk läuft. Die App sendet Text über HTTP an Ihre Ollama-Instanz. Nichts geht an externe Dienste.

______

## Projekt-Roadmap

Features in Entwicklung oder geplant:

- Lebenslauf-Versionsverlauf über IndexedDB
- LinkedIn-Profil-Optimierer
- Google Gemini Anbieter-Support
- Zusätzliche Ollama-Modelle

Das Projekt ist MIT-lizenziert und willkommt Pull Requests. Eröffnen Sie zuerst ein Issue für größere Änderungen.

______

## Fazit

**ATS Resume Improver** füllt eine echte Lücke: ein Tool, das ernsthafte Lebenslaufanalyse durchführt, ohne Ihre Daten an jemanden zu vermitteln. Der Modus ohne Schlüssel gibt Ihnen sofortiges, umsetzbares Feedback zu Formatierung und Keyword-Abdeckung. Das Hinzufügen eines KI-Schlüssels verbessert die Analyse zu semantischem Denken, Anschreiben-Erstellung und Bewerbungsvorbereitung — alles für Cents pro Analyse oder völlig kostenlos mit Ollama.

Die Live-gehostete Version ist unter **[atsresumeimprover.netlify.app](https://atsresumeimprover.netlify.app/)** verfügbar. Der vollständige Quellcode ist unter **[github.com/simeononsecurity/ats-resume-improver](https://github.com/simeononsecurity/ats-resume-improver)**.

______

## Referenzen

1. [ATS Resume Improver — Live-Tool](https://atsresumeimprover.netlify.app/)
2. [ATS Resume Improver — GitHub-Repository](https://github.com/simeononsecurity/ats-resume-improver)
3. [Lebenslauf-Tipps und Tricks — RESUME_TIPS.md](https://github.com/simeononsecurity/ats-resume-improver/blob/main/RESUME_TIPS.md)
4. [Sabrina Ramonov — Bester KI-Prompt zur Humanisierung von KI-Texten](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing)
5. [OpenAI API-Dokumentation](https://platform.openai.com/docs/)
6. [Anthropic Claude API-Dokumentation](https://docs.anthropic.com/)
7. [Ollama — Lokaler LLM-Server](https://ollama.com/)

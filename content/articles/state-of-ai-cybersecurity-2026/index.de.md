---
title: "Der Stand der KI-Cybersicherheit 2026: Schnell deployen, später sichern, irgendwann zahlen"
draft: false
toc: true
date: 2026-06-26
description: "Eine professionelle Einschätzung des tatsächlichen Stands der KI-Cybersicherheit 2026. Organisationen haben KI in einem Tempo eingeführt, mit dem Leitlinien, Werkzeuge und betriebliche Praktiken nicht Schritt gehalten haben. Die Lücke ist real, dokumentiert und wächst."
tags: ["KI-Sicherheit", "KI-Cybersicherheit 2026", "Prompt Injection", "KI-Agenten", "MCP-Sicherheit", "KI-Lieferkette", "Schatten-KI", "KI Red Teaming", "LLM-Sicherheit", "KI-Beobachtbarkeit", "agentische KI", "KI-Bedrohungen", "KI-Angriffe", "Modellsicherheit", "KI-Governance", "NIST AI 600-1", "OWASP LLM", "MITRE ATLAS", "KI-Vorfallreaktion", "Unternehmens-KI-Sicherheit", "KI-Identität", "Kontext-Vergiftung", "Tool-Vergiftung", "KI-Autorisierung"]
cover: "/img/cover/state-of-ai-cybersecurity-2026.webp"
coverAlt: "Eine Illustration vernetzter KI-Systeme als leuchtende Knoten auf dunklem Hintergrund, mit lebhaften Verbindungslinien und Schatten um einige Knoten, die Sicherheitslücken darstellen."
coverCaption: ""
---

Organisationen haben KI-Systeme in 2023, 2024 und 2025 in einem Tempo eingesetzt, mit dem defensive Leitlinien, Sicherheitswerkzeuge und betriebliche Praktiken nicht Schritt hielten. **Das Ergebnis im Jahr 2026 ist eine große, schlecht instrumentierte Angriffsfläche, die mit echten Geschäftssystemen verbunden ist, während Abwehrmaßnahmen noch zusammengestellt werden.**

Ich möchte konkret darlegen, was mich besorgt und warum. Dies ist keine allgemeine Warnung vor KI-Risiken. Es ist eine Beschreibung der tatsächlichen Angriffsfläche, wo die Lücken dokumentiert sind und was Organisationen angehen müssen.

## Warum diese Lücke besteht

Traditionelle Softwaresicherheit reifte über rund drei Jahrzehnte. Jahrzehnte an Erfahrung mit Vorfallreaktion, Schwachstellenforschung, Werkzeugentwicklung und hart erworbenem Betriebswissen haben die Rahmenwerke, Produkte und Praktiken hervorgebracht, auf die moderne Sicherheitsprogramme aufbauen.

**Generative KI für Unternehmen erreichte innerhalb von etwa zwei Jahren Millionen von Produktionsdeployments.**

Die Disziplinen, die Softwaresicherheit funktionsfähig machen — Bedrohungsmodellierung für spezifische Architekturen, gehärtete Deployment-Muster, ausgereifte Playbooks für Vorfallreaktion, etablierte Audit- und Beobachtbarkeitspraktiken — hatten keine Zeit, sich zu entwickeln, bevor Organisationen begannen, KI im großen Maßstab einzusetzen. *Die Leitlinien kamen nach dem Deployment. Die Werkzeuge kamen nach den Leitlinien. Das Betriebsexpertise entwickelt sich noch.*

Das ist keine Schuldzuweisung. Es erklärt, warum die Lücken strukturell und nicht zufällig sind.

## Die vier Schichten der KI-Sicherheit

Ein Großteil der Verwirrung in KI-Sicherheitsdiskussionen entsteht dadurch, dass Governance-Dokumente, Bedrohungstaxonomie, Ingenieursleitlinien und operative Kontrollen so behandelt werden, als wären sie dasselbe. Das sind sie nicht.

**Schicht 1 ist Governance.** NIST AI RMF, ISO/IEC 42001 und der EU AI Act operieren auf der Organisations- und Prozessebene. Sie beschreiben, wie KI-Risiken zu managen sind, Aufsicht zu strukturieren ist und Verantwortlichkeit zu dokumentieren ist. Sie sind Governance-Rahmenwerke, keine technischen Kontrollen.

**Schicht 2 ist Bedrohungstaxonomie.** MITRE ATLAS dokumentiert gegnerische Taktiken gegen KI-Systeme. Die OWASP Top 10 für LLMs und die OWASP Agentic AI Top 10 listen spezifische Angriffskategorien auf. Diese Dokumente benennen die Angriffe. Sie schreiben keine Verteidigungen vor.

**Schicht 3 ist Ingenieursleitlinien.** Google SAIF, Microsoft AI SDL, OWASP AI Exchange und NIST AI 600-1 bieten Leitlinien, wie KI sicher gebaut und eingesetzt werden sollte. NIST AI 600-1 ist wesentlich spezifischer als das Basis-AI-RMF und deckt Prompt Injection, Datenvergiftung und Informationsgefahren für generative KI-Deployments ab.

**Schicht 4 ist Betrieb.** Überwachung, Vorfallreaktion, Laufzeitkontrollen, Protokollierung, geringste Berechtigung, Evaluierungspipelines und Zugangsverwaltung sind operative Praktiken. Sie erfordern Organisationsprozesse, nicht nur Dokumentation.

*Die meisten Organisationen haben unvollständige Abdeckung in Schichten 3 und 4. Dort lebt fast das gesamte operative Risiko.*

## Was in der Produktion ist

Unternehmens-KI 2026 sind nicht nur Chatbots. Zu den in der Produktion befindlichen Systemen gehören:

- **RAG-Systeme**, die aus internen Dokumentenrepositorien, Wikis, Datenbanken und Kundendatensätzen ziehen
- **Kundenseitige Support-Agenten** mit Zugang zu Kontoinformationen und Fall-Management-Systemen
- **Interne Produktivitätsassistenten**, die mit E-Mail, Kalendern, Dateisystemen und Kommunikationsplattformen integriert sind
- **Code-Überprüfungs- und Generierungswerkzeuge** mit Zugang zu Quellcode-Repositorien
- **Automatisierte Agenten**, die geplante Workflows mit Anmeldedaten für interne APIs ausführen
- **Dokument-, Vertrags- und Finanzdatenverarbeiter**
- **KI-Modelle, eingebettet in Betrugserkennungs-, Einstellungs- und Zugangskontrollentscheidungen**

Jedes System stellt eine andere Angriffsfläche dar. Ein RAG-System über Ihrer internen Wissensdatenbank ist gleichzeitig ein Informationsoffenlegungsrisiko und ein Prompt-Injection-Ziel. **Ein Agent mit E-Mail-Zugang und dauerhaften Anmeldedaten ist ein autonomer Prozess mit echtem Einfluss auf echte Systeme.**

*Sicherheitsteams waren oft nicht an der Entscheidung beteiligt, diese Systeme einzusetzen. Sie entdecken häufig bestehende KI-Deployments durch Audit statt durch Design-Review.*

## KI steht jetzt auf beiden Seiten

**Dieselben KI-Fähigkeiten, die Ihrem Sicherheitsteam zur Verfügung stehen, stehen auch Angreifern zur Verfügung.**

**KI-gestützte Entwicklung** reduziert die Zeit, die benötigt wird, um öffentliche Schwachstellenoffenbarungen in funktionierende Proof-of-Concepts und operative Werkzeuge umzuwandeln. Die Geschwindigkeit des Übergangs vom Lesen eines CVE zu funktionalem Code ist für jeden, der diese Werkzeuge nutzt, gesunken — einschließlich Angreifer.

**KI-generierter Phishing-Inhalt** produziert E-Mails mit besserer Grammatik, überzeugendem Kontext und weniger erkennbaren Fehlern als viele von Menschen geschriebene Angriffe. Die Formatierungssignale und sprachlichen Muster, auf die Ihre Benutzer trainiert wurden zu achten, sind weniger zuverlässig, wenn der Inhalt KI-generiert ist.

**Stimmenklonung für Vishing-Kampagnen** imitiert Führungskräfte und Kollegen in Echtzeit-Anrufen. Die Einstiegshürde für gezieltes Social Engineering sank, als die Qualität der Sprachsynthese verbessert wurde und die Zugriffskosten fielen.

**Deepfake-Video für Business-E-Mail-Compromise** ist von theoretisch zu operativ geworden. Finanzbetrug mit KI-generierten Videos von Führungskräften, die Transaktionen genehmigen, ist seit 2024 in mehreren Sektoren dokumentiert. *Ihr Sensibilisierungstraining wurde für ein anderes Bedrohungsmodell entwickelt.*

## Prompt Injection und Kontext-Vergiftung

**Das Verstehen von Prompt Injection ist der Ausgangspunkt für das Verstehen von KI-Systemsicherheit.**

Ein Sprachmodell folgt Anweisungen, die in sein Kontextfenster eingebettet sind. Das Kontextfenster umfasst den System-Prompt, den Gesprächsverlauf, Tool-Ausgaben und abgerufene Dokumente. **Das Modell kann nicht zuverlässig zwischen Anweisungen des Anwendungsentwicklers und Anweisungen unterscheiden, die ein Angreifer in Inhalte eingebettet hat, die das Modell verarbeitet.** Das ist der Kern von Prompt Injection, wie OWASP sie definiert.

*Direkte Prompt Injection* zielt direkt auf den Modell-Input ab. Der Benutzer liefert Text, der darauf ausgelegt ist, System-Anweisungen zu überschreiben.

*Indirekte Prompt Injection* ist für Unternehmens-Deployments schwerwiegender. Ihr RAG-Agent ruft ein Dokument aus Ihrer Wissensdatenbank ab. Dieses Dokument enthält Anweisungen, die den Agenten anweisen, eine andere Aktion auszuführen. Ihr Zusammenfassungs-Tool verarbeitet eine Webseite mit versteckten Direktiven. Ihr Support-Bot liest einen Kunden-Anhang mit Anweisungen. Der Agent verarbeitet die Anweisungen und handelt entsprechend.

**Kontext-Vergiftung** ist eine breitere Kategorie. Angreifer müssen Ihr Modell nicht kompromittieren, um Ihr KI-System zu kompromittieren. Sie müssen schädliche Inhalte in den Kontext Ihres Modells einbringen. Dies umfasst vergiftete RAG-Dokumente, vergiftete Speichereinträge, böswillig erstellte E-Mail-Inhalte, die Ihr Agent verarbeitet, feindliche PDFs und von Angreifern kontrollierte Webseiten, die Ihr Browser-Agent besucht. *Diese unterscheiden sich von der Modell-Vergiftung. Das Modell ist in Ordnung. Der Kontext nicht.*

Defense-in-depth reduziert dieses Risiko. Input-Filterung, Output-Validierung, berechtigungsbeschränkte Tool-Scopes, sandgeboxte Ausführung und menschliche Genehmigungsgates bei folgenreichen Aktionen helfen alle. **Keine dieser Verteidigungen schließt die Angriffskategorie.** OWASP, NIST, Anthropic, OpenAI und Microsoft empfehlen alle Schichtansätze, weil keine einzelne Kontrolle ausreicht.

*Gestalten Sie für die Annahme, dass Prompt Injection bei einem bestimmten Prozentsatz der Eingaben erfolgreich sein wird. Begrenzen Sie die Konsequenzen entsprechend.*

## KI-Agenten, Berechtigungsgrenzen und das Schadenspotenzial-Problem

Agenten unterscheiden sich von Chatbots auf eine betrieblich kritische Weise: **Sie handeln**.

Ein Agent, der mit Ihrer E-Mail, GitHub, Jira, Slack, Salesforce, AWS und internen APIs verbunden ist, ist ein autonomer Prozess mit Zugang zu denselben Systemen, die Ihre am besten vernetzten Mitarbeiter nutzen. **Eine erfolgreiche Prompt Injection gegen diesen Agent produziert keine unerwünschte Textantwort. Sie produziert eine unerwünschte Aktion auf einem echten System.**

**Das Schadenspotenzial einer Kompromittierung wird durch das bestimmt, auf was der Agent Zugang hat.** Die meisten aktuellen Agent-Deployments halten Zugang weit über das hinaus, was jede einzelne Aufgabe erfordert. Ein Agent, der ein Jira-Ticket lesen muss, sollte auch keinen Schreibzugang zu Ihrem GitHub-Hauptbranch haben. Ein Agent, der Support-Anfragen bearbeitet, sollte keine Anmeldedaten für Ihr Abrechnungssystem halten.

**KI-Autorisierung ist ein eigenständiges Problem von Benutzerautorisierung.** Traditionelle Anwendungen fragen, ob ein Benutzer für eine Aktion autorisiert ist. Agentenarchitekturen erfordern zu fragen, ob dieser Agent berechtigt ist, diese spezifische Aktion für diesen spezifischen Benutzer zu diesem spezifischen Zeitpunkt basierend auf dem aktuellen Kontext durchzuführen. Die meisten aktuellen Agent-Deployments implementieren das nicht.

*Menschliche Genehmigungsworkflows sollen der Rückhalter für folgenreiche Agent-Aktionen sein. Organisationen stellen fest, dass sie auch Genehmigungsmüdigkeit begegnen. Wenn Agenten regelmäßig Genehmigungen für routinemäßige Aktionen anfragen, beginnen Benutzer, automatisch zu genehmigen, ohne die Anfrage zu überprüfen. Der Rückhalter wird zur Formalität.*

## KI-Identität ist ein Unternehmens-Sicherheitsproblem

**Agenten halten Anmeldedaten.** OAuth-Token, API-Schlüssel, Dienstkonto-Anmeldedaten und Cloud-IAM-Rollen erscheinen alle in KI-Agent-Deployments. Das sind Nicht-Mensch-Identitäten mit echtem Zugang.

Spezifische Lücken in aktuellen Deployments:

- **Agent-Anmeldedaten sind oft langlebig** und werden nicht mit vergleichbaren Zeitplänen wie Dienstkonten rotiert
- **Agent-Token-Scopes sind häufig breiter** als für die vom Agenten durchgeführten Aufgaben erforderlich
- Audit-Protokollierung für unter Agent-Identitäten durchgeführte Aktionen variiert stark
- **Anmeldedatenleck durch Prompts** ist ein dokumentiertes Risiko. Ein Agent, der seine API-Schlüssel im Kontext oder in Ausgaben einschließt, legt sie für jeden offen, der die Ausgabe liest oder das Gespräch abruft.
- Agenten, die über Tool-Aufrufe zusätzliche Anmeldedaten erhalten, schaffen **Identitätsketten, die schwer zu auditieren sind**

*Verwalten Sie Ihre Agent-Identitäten auf dieselbe Weise, wie Sie privilegierte Dienstkonten verwalten. Das erfordert derzeit bewusste Anstrengung, da die meisten Identitätsverwaltungs-Tools keine native Unterstützung für KI-Agent-Identitätsmuster haben.*

## Persistentes Agent-Gedächtnis schafft langfristige Angriffsfläche

**Agenten mit persistentem Gedächtnis stellen eine Angriffsfläche dar, die in zustandslosen Systemen nicht existiert.**

Ein Angreifer, der in das Gedächtnis eines Agenten injizieren kann, baut eine Position auf, die über Sitzungen hinweg bestehen bleibt. *Der Angriff muss nicht in einer einzelnen Interaktion erfolgreich sein. Im Laufe von Tagen oder Wochen im Gedächtnis angesammelter Einfluss prägt zukünftige Agent-Verhalten.* Dies wird manchmal als **Langzeithorizont- oder Sleeper-Context-Angriff** bezeichnet.

Für dieses spezifische Risiko gibt es nur sehr wenig operationelle Leitlinien. Organisationen, die Agenten mit persistentem Gedächtnisspeicher einsetzen, müssen:

- **Gedächtnisspeicher als hochwertige Daten** behandeln, die Zugriffskontrollen erfordern
- **Gedächtnisinhalt validieren**, bevor Agenten darauf handeln
- Die Fähigkeit zum **Auditieren und Zurücksetzen des Gedächtniszustands** in ihre Architektur einbauen

## Die Modell-Lieferkette wird nicht wie Software-Lieferkette behandelt

**Organisationen, die vortrainierte Modelle aus öffentlichen Repositorien herunterladen, akzeptieren ausführbare KI-Artefakte aus externen Quellen. Die auf diese Downloads angewandte Prüfung entspricht typischerweise nicht dem, was dieselben Organisationen auf npm-, PyPI- oder Maven-Pakete anwenden.**

Spezifische Risiken in Modell-Repositorien:

- **PyTorch-Pickle-Format-Modelldateien** führen beim Laden beliebigen Python-Code aus. Das wurde in dokumentierten Lieferkettenangriffen ausgenutzt. **SafeTensors** ist das speziell dafür entwickelte Format. Bevorzugen Sie es, wann immer es verfügbar ist.
- Schädliche Modell-Loader, die Abhängigkeiten installieren oder Setup-Code neben dem Modell ausführen
- Auf **vergifteten Datensätzen** trainierte Modelle, die in bestimmten Kontexten subtil falsche Ausgaben produzieren
- Modelle mit **eingebetteten Hintertüren**, die unter Triggerbedingungen aktiviert werden
- **Repository-Name-Squatting**, um schädliche Modelle unter vertrauten Namen zu liefern

*Wenige Organisationen führen eine Software-Stückliste, die ihre KI-Systeme abdeckt.* Die meisten können nicht sagen, von welchem Basismodell ein Produktionssystem ausging, welche Version der Trainingsdaten für das Fine-Tuning verwendet wurde, oder ob die Gewichte im Deployment den zuletzt evaluierten Gewichten entsprechen. Dieses Maß an Rückverfolgbarkeit ist eine Voraussetzung für bedeutungsvolle Lieferkettensicherheit. Sie ist heute nicht verbreitet.

## Schatten-KI schafft unkontrollierte Datenflüsse

**Persönliche Verbraucher-KI-Konten sind dort, wo Ihre Daten ohne Kontrollen fließen.**

ChatGPT Enterprise, Claude Enterprise und Microsoft Copilot for M365 enthalten vertragliche Schutzmaßnahmen für Kundendaten. **Persönliche ChatGPT-, persönliche Claude-, persönliche Gemini- und ähnliche Verbraucherkonten bieten diese Garantien standardmäßig nicht.**

Mitarbeiter, die persönliche Konten zur Verarbeitung von Arbeitsdokumenten verwenden, leiten Rechtsstrategie-Dokumente, Kundendatensätze, Quellcode, Finanzprognosen, Personalentscheidungen und interne Kommunikation durch Pipelines, die Ihre Organisation nicht kontrolliert. *Sicherheitsteams haben häufig keine genauen Informationen über das Volumen dieser Aktivität oder welche Datenkategorien betroffen sind.*

Ihre DLP-Kontrollen erfassen keine Daten, die über einen Webbrowser zu einem Verbraucher-KI-Dienst fließen. Ihre Datenaufbewahrungsrichtlinien gelten nicht für den Gesprächsverlauf auf einer Drittanbieter-Plattform. **Ihre regulatorischen Verpflichtungen unter DSGVO, HIPAA, SOX und sektorspezifischen Regeln ändern sich nicht danach, ob die Daten versehentlich oder über einen Browser-Tab das System verließen.**

*Den tatsächlichen Umfang zu ermitteln, bevor Kontrollen aufgebaut werden, ist der notwendige erste Schritt. Was Sie über dieses Problem annehmen, ist fast sicher eine Unterschätzung.*

## KI-Systeme lecken Daten auf Weisen, die traditionelle Anwendungen nicht tun

**RAG-Überabruf** gibt Benutzern Dokumente zurück, auf die sie keinen Zugang haben sollten. Ein Mitarbeiter stellt eine Frage. Die Abrufkomponente gibt ein Dokument aus einem eingeschränkten Segment der Wissensdatenbank zurück. Die Antwort enthält Informationen aus diesem Dokument. *Das Zugriffskontrollversagen trat auf der Abrufschicht auf, nicht auf der Anwendungsschicht.* Viele RAG-Deployments wurden ohne erzwungene Berechtigungen auf Dokumentebene gebaut, die dem Quellsystem entsprechen.

**System-Prompt-Leck** offenbart Betriebsanweisungen, die in Ihr KI-Produkt integriert sind. System-Prompts sollten als vertraulich behandelt werden.

**Mandant-Isolationsausfälle bei Multi-Tenant-KI** treten auf, wenn auf Daten mehrerer Kunden feinabgestimmte Modelle die Informationen eines Kunden im Kontext eines anderen Kunden anfragen. Das ist eine dokumentierte Risikokategorie für SaaS-KI-Produkte mit mehreren Mandanten.

**Modell-Memorisierung** führt dazu, dass Modelle Inhalt aus Trainingsdaten wörtlich wiedergeben. Das Risiko ist nicht eliminiert, besonders bei Modellen, die auf kleinen oder unzureichend deduplizierten privaten Datensätzen feinabgestimmt wurden.

## Organisationen fehlt Sichtbarkeit zur Inferenzzeit

**Die meisten KI-Deployments haben keinen äquivalenten Abdeckungsgrad ihrer KI-Komponenten gegenüber der Infrastruktur.**

Für die Überwachung eines eingesetzten Sprachmodells oder Agenten ist andere Telemetrie erforderlich als für die Überwachung eines Anwendungsservers. Organisationen müssen folgendes sammeln:

- **Prompt- und Ausgabeinhalt** in einem Format, das für Richtlinienüberprüfung und Anomalieerkennung geeignet ist
- **Tool-Aufrufprotokolle** für Agenten, einschließlich Tool-Namen, Argumente und Antworten
- **Abrufprotokolle** für RAG-Systeme, einschließlich Abfragen, zurückgegebener Dokumente und Zugangskontrollentscheidungen
- **Klassifizierungssignale** für Jailbreak- und Injektionsversuche
- **Ausgabe-Konsistenzüberwachung**, um Verhaltensabweichungen über Modellversionen hinweg zu erkennen
- **Latenzymuster**, die auf Context-Stuffing-Versuche hinweisen können

*Viele Organisationen, die KI 2023 und 2024 eingesetzt haben, haben HTTP-Statuscodes und Latenzmessungen. Die Telemetrie, die zur Erkennung oder Untersuchung eines KI-Sicherheitsvorfalls benötigt wird, existiert in diesen Umgebungen oft nicht. Vor einem Vorfall ist nicht der richtige Zeitpunkt, das herauszufinden.*

## KI-Vorfallreaktion erfordert eigene Playbooks

**Ihre bestehenden IR-Playbooks decken Endpunkte, Netzwerke, Anwendungen und Identität ab. Sie decken keine KI-spezifischen Szenarien ab.**

Fragen, mit denen Ihr IR-Team konfrontiert wird, die aktuelle Playbooks nicht adressieren:

- Wie stellen Sie fest, ob ein Modell während eines Fine-Tuning-Laufs vergiftet wurde?
- Wie schätzen Sie das Schadenspotenzial einer erfolgreichen indirekten Injektion gegen einen Agenten mit Schreibzugang zu mehreren Systemen ab?
- Wie stellen Sie beim Lieferkettenangriff fest, ob Trainings- oder Fine-Tuning-Daten exfiltriert wurden?
- Wie stellen Sie eine **Verhaltensbaseline** für ein Modell auf, um es nach einem Vorfall zu vergleichen?
- Wie reagieren Sie, wenn eine Modellaktualisierung von einem Drittanbieter Verhalten einführt, das absichtlich statt versehentlich erscheint?
- Wie stellen Sie fest, ob der **Gedächtnisspeicher eines Agenten im Laufe der Zeit manipuliert wurde**?

*Diese Szenarien erfordern Vorbereitung, bevor sie auftreten. Sie brauchen vorab Telemetrie. Sie brauchen dokumentierte Modell-Verhaltens-Baselines, bevor Sie sie vergleichen müssen.*

## Evaluierungspipelines werden zur Standard-Ingenieurspraxis

KI-Sicherheit setzt zunehmend auf **strukturierte Evaluierung vor dem Deployment** statt nur auf Post-Deployment-Überwachung.

Vor-Deployment-Evaluierung für Sicherheit umfasst:

- **Prompt-Injection-Tests** gegen etablierte Injektionsdatensätze und Ihren spezifischen Anwendungsfall
- **Jailbreak-Benchmarking** gegen veröffentlichte adversarielle Prompt-Suiten
- **Adversarielle Robustheitsbewertung** für Modelle, die folgenreiche Entscheidungen treffen
- **Regressionstests** zwischen Modellversionen, um Verhaltensänderungen zu identifizieren
- **Richtlinienevaluierung** gegen dokumentierte akzeptable Nutzungsanforderungen
- **Red-Teaming-Übungen** von Menschen, die darauf abzielen, spezifische Abwehrmaßnahmen zu überwinden

*Minimale Evaluierungspipelines vor Hochkonsequenz-Deployments aufzubauen, ist in kleinerem Maßstab erreichbar, als die meisten Organisationen annehmen.*

## Was Sie tun sollten

**Inventarisieren Sie, was eingesetzt ist.** Wissen Sie, was läuft, auf welche Daten es zugreift, welche Anmeldedaten es hält, welche Tools es aufruft und welche Aktionen es ausführt. Das ist die Voraussetzung für alles andere.

**Behandeln Sie KI-Agenten als privilegierte Konten.** Wenden Sie das Prinzip der geringsten Berechtigung an. Beschränken Sie Anmeldedaten auf den minimalen für jede Aufgabe erforderlichen Zugang. Auditieren Sie, worauf jeder Agent Zugang hat, und entfernen Sie, was nicht benötigt wird.

**Implementieren Sie KI-spezifische Beobachtbarkeit vor dem Deployment**, nicht nach einem Vorfall. Prompt- und Ausgabe-Protokollierung, Tool-Aufruf-Protokollierung und Abruf-Protokollierung sind die minimale Telemetrie für Sicherheitsanalyse.

**Bewerten Sie Ihre Schatten-KI-Exposition.** Finden Sie heraus, welche KI-Dienste Mitarbeiter für Arbeitsaufgaben nutzen. Stellen Sie fest, welche Datenkategorien über persönliche Konten fließen. Erstellen Sie Richtlinien und Kontrollen basierend auf tatsächlichen Erkenntnissen.

**Erzwingen Sie Zugriffskontrollen auf Dokumentebene in RAG-Systemen.** Wenn Ihre Abrufschicht die Zugriffsregeln Ihrer Quellsysteme nicht durchsetzt, beheben Sie das, bevor es ein eingeschränktes Dokument einem unbefugten Benutzer vorführt.

**Auditieren Sie Ihre Modell-Lieferkette.** Dokumentieren Sie jedes verwendete Basismodell. Bevorzugen Sie SafeTensors gegenüber Pickle-Formaten. Wenden Sie Lieferkettenprüfung auf Modellartefakte an, vergleichbar mit dem, was Sie auf Softwareabhängigkeiten anwenden.

**Verwalten Sie Agent-Identitäten.** Verwalten Sie Agent-OAuth-Token und API-Schlüssel mit denselben Lebenszyklus-, Scope-Überprüfungs- und Rotationspraktiken, die Sie auf privilegierte Dienstkonten anwenden.

**Erstellen Sie KI-spezifische IR-Runbooks jetzt.** Definieren Sie vor einem Vorfall, wie Sie KI-spezifische Szenarien untersuchen würden, welche Beweise Sie benötigen und welche Reaktionsmöglichkeiten Sie haben.

**Führen Sie Evaluierungen durch, bevor Sie KI in hochkonsequenten Kontexten einsetzen.** Beginnen Sie mit verfügbaren öffentlichen Rahmenwerken, wenn Sie kein internes Werkzeug haben.

*Behandeln Sie Governance-Compliance nicht als Sicherheitslage. Governance-Rahmenwerke beschreiben Prozesse und Risikomanagement. Sie beschreiben keine technisch defensiven Systeme. Beide sind erforderlich.*

## Referenzen

- NIST AI Risk Management Framework (AI RMF 1.0), 2023
- NIST AI 600-1: Generative AI Profile, 2024
- OWASP Top 10 for Large Language Model Applications, 2025
- OWASP Agentic AI Top 10
- OWASP AI Exchange
- MITRE ATLAS: Adversarial Threat Landscape for AI Systems
- Google Secure AI Framework (SAIF)
- Microsoft AI Security SDL
- CISA Guidance on AI Cybersecurity, 2024
- ISO/IEC 42001:2023 Artificial Intelligence Management Systems
- EU AI Act, Regulation (EU) 2024/1689
- SafeTensors format documentation, Hugging Face

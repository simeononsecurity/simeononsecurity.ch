---
title: "KI-Cybersicherheit und Governance-Zertifizierungen halten nicht mit dem Problem Schritt"
draft: false
toc: true
date: 2026-06-26
description: "Eine Facheinschätzung zur Lücke zwischen KI-Governance-Zertifizierungen und tatsächlicher KI-Sicherheitspraxis. Wir haben mehrere davon abgelegt und waren enttäuscht. Die Frameworks sind noch jung und governance-orientiert. Die Angriffsfläche ist schneller gewachsen."
tags: ["KI-Sicherheit", "KI-Governance", "KI-Zertifizierungen", "NIST AI RMF", "NIST AI 600-1", "ISO 42001", "IAPP AIGP", "Prompt-Injection", "KI-Cybersicherheit", "LLM-Sicherheit", "OWASP LLM Top 10", "MITRE ATLAS", "KI-Risikomanagement", "KI-Compliance", "Machine-Learning-Sicherheit", "Modell-Lieferkette", "gegnerische KI", "KI-Agenten", "MCP-Sicherheit", "KI-Red-Teaming", "KI-Governance-Zertifizierungen", "agentische KI", "Google SAIF"]
cover: "/img/cover/ai-cybersecurity-governance-certifications-disappointing.webp"
coverAlt: "Das Bild zeigt eine geteilte Szene: auf einer Seite Fachleute in einem Büro, die Governance-Dokumente besprechen; auf der anderen chaotische digitale Darstellungen von KI-Systemen unter Cyberangriff, mit lebhaften Farben, die den Kontrast hervorheben."
coverCaption: ""
---

Wir haben die Prüfungen abgelegt. Wir haben bestanden. Wir haben Zertifikate erhalten und eine Enttäuschung mitgenommen, die ich genau beschreiben möchte.

Dies ist keine Kritik an den Menschen, die diese Programme entwickelt haben. Sie arbeiten mit unvollständigem Material. KI-Sicherheit als Disziplin ist jung. Die Angriffsforschung bewegt sich schneller als die Verteidigungswerkzeuge. Die Governance-Frameworks kamen vor der Engineering-Anleitung.

Das Problem ist die Lücke zwischen dem, was die Zertifizierungen lehren, und dem, was Sie wissen müssen, um KI-Systeme in der Produktion tatsächlich zu sichern.

## Drei Schichten, die häufig verwechselt werden

Bevor erklärt wird, was fehlt, hilft es, das Vorhandene zu trennen.

Die erste Schicht ist Governance. Dokumente wie das NIST AI Risk Management Framework (AI RMF 1.0, 2023), ISO/IEC 42001:2023 und der EU AI Act operieren auf der organisatorischen und prozessualen Ebene. Sie beschreiben, wie man KI-Risiken verwaltet, Aufsicht strukturiert und Verantwortlichkeit dokumentiert. Sie sind bewusst governance-orientiert statt kontrolvorschreibend. Das ist beabsichtigt.

Die zweite Schicht ist die Bedrohungstaxonomie. MITRE ATLAS dokumentiert gegnerische Taktiken gegen KI-Systeme im gleichen Format wie ATT&CK. Das OWASP Top 10 für Large Language Model Applications listet die Angriffsklassen auf, die für eingesetzte LLMs am relevantesten sind. Diese Dokumente benennen die Angriffe und beschreiben, wie sie funktionieren. Sie schreiben keine Verteidigungen vor.

Die dritte Schicht ist technische Anleitung. Dazu gehören Googles Secure AI Framework (SAIF), Microsofts AI Security SDL, OWASP AI Exchange, NIST AI 600-1 (das Generative AI Profile) und anbieterspezifische Sicherheitsdokumentation von Anthropic, OpenAI, Meta und anderen. Diese bieten Engineering-Anleitung zu sicherem Einsatz, Evaluierungspraktiken und Laufzeitkontrollen.

Die meisten KI-Governance-Zertifizierungen decken die erste Schicht gründlich ab. Sie referenzieren die zweite Schicht auf Zusammenfassungsebene. Die dritte berühren sie selten.

## Was die Zertifizierungen abdecken

Die derzeit verfügbaren KI-Governance- und Sicherheitszertifizierungen, einschließlich IAPP AI Governance Professional (AIGP), ISACAs AI Fundamentals Certificate, ISO 42001 Zertifizierungen und CompTIA AI+, decken einen konsistenten Themensatz ab.

Sie lernen das NIST AI RMF und wie Sie seine vier Funktionen, Govern, Map, Measure und Manage, auf den KI-Einsatz Ihrer Organisation anwenden. Sie lernen die Risikoklassifizierungen des EU AI Act und wie eine Konformitätsbewertung für Hochrisikosysteme aussieht. Sie lernen über Bias, Fairness, Transparenz und Verantwortlichkeit als Governance-Prinzipien. Sie lernen, wie man KI-Governance-Richtlinien schreibt und Folgenabschätzungen durchführt.

Das sind echte Fähigkeiten. Organisationen brauchen Menschen, die Governance-Frameworks verstehen. Sie brauchen Menschen, die das NIST AI RMF lesen und wissen, was es sie auffordert aufzubauen.

Was die Zertifizierungen nicht mit gleicher Tiefe lehren:

- Wie Angreifer KI-Systeme in der Produktion derzeit kompromittieren
- Wie Defense-in-Depth für Prompt-Injection operativ aussieht und warum keine einzelne Kontrolle sie eliminiert
- Wie man die Integrität von Modellen vor dem Einsatz verifiziert
- Was KI-spezifisches Red Teaming beinhaltet und wie man es abgrenzt
- Wie man das Modellverhalten gegen gegnerische Eingaben vor dem Start bewertet
- Wie KI-Observabilität zur Inferenzzeit aussieht
- Wie sich die KI-Incident-Response von Standard-IR-Playbooks unterscheidet
- Was die Absicherung von KI-Agenten mit Werkzeugzugang und externen Integrationen erfordert

## Das NIST AI RMF ist Governance, kein Engineering

Das NIST AI RMF ist ein gut konstruiertes Dokument. NIST hat es technologieneutral, sektorunabhängig und für verschiedene KI-Entwicklungsansätze anwendbar konzipiert. Dies ergibt ein Framework, das breit anwendbar ist.

Es bedeutet auch, dass das Framework keine technischen Kontrollen für spezifische Angriffsklassen vorschreibt. Wenn Ihre Organisation das AI RMF vollständig übernimmt und alle seine Funktionen auf Ihren KI-Einsatz abbildet, haben Sie dokumentierte Risikoprozesse. Sie haben nicht notwendigerweise eine Verteidigung gegen Prompt-Injection auf Ihrem eingesetzten Sprachmodell.

NIST erkennt dies an. NIST AI 600-1, das 2024 veröffentlichte Generative AI Profile, erweitert das AI RMF speziell für generative KI und Large Language Models. Es deckt Risiken einschließlich Prompt-Injection, Datenvergiftung und Informationsgefahren auf einem Spezifizierungsgrad ab, den das Basis-AI-RMF nicht erreicht. Wenn Ihre Zertifizierung das Basis-AI-RMF ohne AI 600-1 abgedeckt hat, haben Sie das Dokument verpasst, das für aktuell eingesetzte Systeme am relevantesten ist.

## ISO 42001 und der Managementsystem-Vergleich

ISO 42001:2023 ist ein KI-Managementsystemstandard. Er bietet eine Struktur für die Steuerung der KI-Entwicklung und des KI-Einsatzes auf Organisationsebene. Sicherheitsfachleute werden die Parallele zu ISO 27001 für Informationssicherheit erkennen.

ISO 27001 ist weit verbreitet. Zertifizierte Organisationen werden dennoch kompromittiert. Eine Zertifizierung dokumentiert, dass ein Managementsystem existiert, einem definierten Prozess folgt und überprüft wird. Sie zertifiziert nicht, dass die von diesem Prozess regierten Systeme den gegen sie eingesetzten Angriffen standhalten.

ISO 42001 bietet organisatorische Disziplin. Das Erreichen einer Zertifizierung teilt Stakeholdern mit, dass Ihre KI-Prozesse dokumentiert, überprüft und der Governance unterworfen sind. Es teilt ihnen nicht mit, ob Ihre eingesetzten Modelle unter gegnerischen Bedingungen konsistente Ausgaben produzieren, Ihre Agenten innerhalb definierter Vertrauensgrenzen betrieben werden oder Ihre feinabgestimmten Modelle aus verifizierten Trainingsdaten gebaut wurden.

Das ist die gleiche Lücke, die ISO 27001 hat. In der traditionellen Cybersicherheit haben wir gelernt, damit zu leben. Wir sollten nicht so tun, als schließen KI-Governance-Zertifizierungen sie, wenn sie die gleiche strukturelle Einschränkung teilen.

## Der EU AI Act schafft Ergebnisanforderungen ohne Engineering-Spezifikationen

Der EU AI Act sortiert KI-Systeme nach Risikoniveau: inakzeptabel (verboten), hohes Risiko (Konformitätsbewertung erforderlich), begrenztes Risiko (Transparenzpflichten) und minimales Risiko (keine spezifischen Anforderungen).

Hochrisikosysteme, einschließlich solcher, die in kritischer Infrastruktur, biometrischer Identifikation, Beschäftigungsscreening, Bildung und Strafverfolgung eingesetzt werden, sehen sich mit technischen Dokumentationsanforderungen, menschlichen Aufsichtspflichten und Robustheitsanforderungen konfrontiert. Der Akt verlangt ausdrücklich, dass Hochrisiko-KI-Systeme robust gegen Versuche sind, das Verhalten durch gegnerische Manipulation zu ändern.

Diese Anforderung steht im Text. Der Akt spezifiziert bewusst Ergebnisse, statt technische Kontrollen vorzuschreiben. Die technischen Methoden zum Nachweis gegnerischer Robustheit über alle Einsatzkontexte hinweg haben für jeden Systemtyp und jeden Anwendungsfall noch keine Konsensantworten.

Zertifizierungen, die um den EU AI Act herum aufgebaut sind, bereiten Sie darauf vor, KI-Systeme zu klassifizieren, technische Dokumentation zu schreiben und Aufsichtsprotokolle zu strukturieren. Sie bereiten Sie auf Audits vor. Die Engineering-Arbeit, die ein System produziert, das den Robustheitsanforderungen des Akts entspricht, liegt in einer anderen Disziplin als die, die die Zertifizierungen derzeit abdecken.

## Was KI-Systeme tatsächlich angreift

MITRE ATLAS und OWASP LLM Top 10 dokumentieren die operative Bedrohungslandschaft. Dies sind die Ressourcen, die Angriffe auf einem nützlichen Detailniveau aufzählen. Governance-Frameworks referenzieren Bedrohungen auf einer höheren Abstraktionsebene. Das Folgende stammt aus diesen sicherheitsspezifischen Quellen.

Prompt-Injection funktioniert, indem Eingaben für ein Sprachmodell bereitgestellt werden, die Systemanweisungen überschreiben oder manipulieren. Direkte Injection zielt direkt auf die Eingabe des Modells ab. Indirekte Injection bettet bösartige Anweisungen in Inhalte ein, die das Modell abruft, verarbeitet oder zusammenfasst. Ihre RAG-Pipeline liest ein vom Angreifer kontrolliertes Dokument und handelt nach darin versteckten Anweisungen. Ihr Browser-Agent besucht eine vom Angreifer kontrollierte Seite und folgt ihren eingebetteten Direktiven. Ihr Kundensupport-Bot fasst einen Support-Artikel zusammen, der Anweisungen enthält, seine Sicherheitsrichtlinien zu ignorieren.

Es gibt seit 2026 keine universell wirksame Abhilfe gegen Prompt-Injection. Defense-in-Depth reduziert das Risiko: Eingabefilterung, Ausgabevalidierung, privilegienbegrenzte Werkzeugbereiche, abgeschottete Ausführungsumgebungen und menschliche Genehmigungspforten für folgenreiche Aktionen. Keines davon eliminiert die Angriffsklasse. NIST, OWASP, Anthropic, OpenAI, Google und Microsoft empfehlen allesamt geschichtete Kontrollen statt einzelner Lösungen.

Trainingsdatenvergiftung führt bösartige Beispiele in Trainingsdaten ein, um das Modellverhalten zu degradieren, Backdoors einzuführen oder trigger-basiertes Verhalten zu implantieren. Das Signal für eine erfolgreiche Vergiftung ist oft nicht vorhanden, bis das Modell auf spezifische Trigger-Eingaben trifft. Wenn Ihre Organisation Modelle auf nutzergenerierten Inhalten, abgerufenen Dokumenten oder Drittanbieter-Datensätzen feinabstimmt, ohne deren Herkunft zu verifizieren, sind Sie diesem Risiko ausgesetzt.

Kompromittierung der Modell-Lieferkette ist die Bedrohung, die die meisten Organisationen als nachgelagert behandeln. Modell-Repositories verteilen oft ausführbaren Code neben Modellgewichten, und unsichere Serialisierungsformate wie pickle haben wiederholt Lieferkettenrisiken geschaffen. Pakete, die Model-Downloads begleiten, können Abhängigkeiten mit eigenen Schwachstellen installieren. Viele Organisationen laden Modelle herunter und wenden dabei deutlich weniger Lieferkettenprüfungsstandards an als bei Software-Abhängigkeiten. Die Angriffsfläche ist vergleichbar mit npm, aber die Sicherheitskultur darum herum ist viel früher.

Modellextraktion ermöglicht es Angreifern, funktional ähnliche Modelle durch wiederholte Inferenzabfragen gegen Ihre API zu rekonstruieren. Dies stellt sowohl Verlust an geistigem Eigentum als auch ein Mittel dar, Ihr Modell offline zu studieren, um gezieltere Angriffe zu entwickeln.

Mitgliedschaftsinferenz ermöglicht es Angreifern, mit unterschiedlicher Gewissheit festzustellen, ob bestimmte Datensätze in Ihrem Trainingsset waren, abhängig von Modellarchitektur und Trainingsregime. Dies schafft Datenschutzrisiken für Organisationen, die auf persönlichen Informationen trainiert haben.

Gegnerische Eingaben manipulieren Modellausgaben durch erstellte Perturbationen. Die Technik ist am meisten in der Bildklassifizierung untersucht, gilt aber für Text, Audio und multimodale Systeme. Wenn Ihre KI Entscheidungen über Betrugserkennung, Kreditwürdigkeit, medizinische Bildgebung oder physischen Zugang trifft, ist gegnerische Robustheit eine Sicherheitseigenschaft, gegen die Sie testen müssen, nicht nur dokumentieren.

Datenleckage durch KI-Systeme ist eine Kategorie, die direkte Aufmerksamkeit verdient. RAG-Pipelines stellen Dokumente aus Ihrer Wissensdatenbank bereit, manchmal für Nutzer, die keinen Zugang dazu haben sollten. Prompt-Leckage aus Systemanweisungen offenbart operative Details, die Sie vertraulich halten wollten. Mandantenfähige KI-Deployments schaffen Isolationsanforderungen, die traditionelle Anwendungssicherheitsingenieure manchmal unterschätzen. Dies sind operative Risiken, die regelmäßig in eingesetzten Systemen auftreten.

## KI-Agenten verändern die Angriffsfläche vollständig

Die meisten KI-Sicherheitszertifizierungen wurden geschrieben, als KI-Systeme hauptsächlich Chatbots und Klassifikatoren bedeuteten. Unternehmens-KI im Jahr 2026 bedeutet zunehmend Agenten.

Agenten unterscheiden sich von Chatbots auf eine operativ wichtige Weise: Sie ergreifen Maßnahmen. Ein Agent mit Werkzeugzugang zu Ihrem E-Mail-System, internen Datenbanken, Dateisystemen, Browser und Code-Ausführungsumgebungen ist kein Chatbot mit mehr Funktionen. Es ist ein autonomer Prozess mit bedeutendem Zugang zu echten Systemen, der auf der Basis von Sprachmodellausgaben operiert.

OWASP pflegt jetzt eine separate Agentic AI Top 10, weil das Bedrohungsmodell für Agenten sich ausreichend von LLM-Chat-Anwendungen unterscheidet, um separate Dokumentation zu erfordern.

Prompt-Injection in einem Agenten-Kontext produziert keine unerwünschte Textantwort. Sie produziert eine unerwünschte Aktion. Eine indirekte Injection in einem abgerufenen Dokument weist den Agenten an, Dateien zu löschen, Daten zu exfiltrieren oder E-Mails zu senden. Die Konsequenz ist keine unangemessene Antwort. Es ist eine nicht autorisierte Aktion gegen Systeme, auf die der Agent Zugang hat.

Die Angriffsfläche für Agenten umfasst:

- Werkzeugaufrufbeschränkungen: ob der Agent auf einen minimalen Satz von Werkzeugen beschränkt ist, die für jede Aufgabe angemessen sind
- Anmeldeinformationsumfang: ob die Anmeldeinformationen des Agenten auf das begrenzt sind, was jede Aufgabe erfordert
- Aktionsumkehrbarkeit: ob folgenreiche Aktionen vor der Ausführung menschliche Genehmigung erfordern
- Ausgabefilterung: ob die Ausgaben des Agenten validiert werden, bevor sie nachgelagerte Aktionen auslösen
- Sandboxing: ob die Ausführungsumgebung des Agenten unbeabsichtigten Zugang zu verbundenen Systemen verhindert

Die meisten KI-Governance-Zertifizierungen decken das Agent-Sicherheitsdesign nicht auf diesem Spezifizierungsgrad ab.

## Model Context Protocol schafft eine neue Enterprise-Angriffsfläche

Model Context Protocol (MCP) ist zu einem weit verbreiteten Standard für die Verbindung von KI-Agenten mit externen Werkzeugen, Datenquellen und Diensten geworden. MCP-Server stellen Fähigkeiten bereit, die Agenten entdecken und nutzen. Die Integration ist schnell und flexibel. Die Sicherheitsimplikationen erhalten nicht immer gleichwertige Aufmerksamkeit.

MCP-spezifische Risiken umfassen:

- Bösartige MCP-Server, die ihre Fähigkeiten gegenüber einem Agenten falsch darstellen und unbeabsichtigte Aktionen ausführen
- Werkzeugvergiftung, bei der ein legitimer MCP-Server vom Angreifer kontrollierte Daten zurückgibt und Anweisungen in das einbettet, was Datenausgaben sein sollten
- Überprivilegierte Werkzeuge, bei denen MCP-Integrationen Berechtigungen halten, die über das hinausgehen, was die Aufgabe erfordert
- Vertrauensgrenzenverwirrung, bei der Agenten Anweisungen von angehängten MCP-Werkzeugen erhalten, die Benutzeranweisungen äquivalent erscheinen

Organisationen, die Agenten mit MCP-Integrationen deployen, benötigen ein Framework zur Bewertung des MCP-Server-Vertrauens, zur Überprüfung von Werkzeugberechtigungen und zur Validierung, dass Werkzeugantworten als Daten und nicht als Anweisungen behandelt werden.

## Evaluation ist die operative Praxis, die Zertifizierungen überspringen

KI-Red-Teaming und Evaluierungssuites ersetzen statische Sicherheitsbewertungen als primäre Methoden zum Verständnis des KI-Modellrisikos vor und nach dem Deployment.

Red Teaming für KI umfasst:

- Strukturiertes gegnerisches Testen des Modellverhaltens gegen bekannte Angriffstech­niken
- Jailbreak-Benchmarking gegen etablierte Prompt-Angriffs-Datensätze
- Gegnerische Robustheitstestung, die die Ausgabeveränderung unter perturbier­ten Eingaben misst
- Verhaltensregressionstestung zwischen Modellversionen
- Sicherheitsbenchmark-Evaluation gegen veröffentlichte Evaluierungssuites

NIST, Anthropic, OpenAI, Microsoft, Google und CISA empfehlen alle KI-spezifisches Red Teaming vor dem Deployment für Hochrisikosysteme. Dies wird zur Standarderwartung, nicht zur optionalen Praxis.

Keine der aktuellen KI-Governance-Zertifizierungen bereitet Practitioner ausreichend darauf vor, eine Red-Teaming-Übung gegen ein eingesetztes Modell oder Agentensystem abzugrenzen, auszuführen oder zu interpretieren. Sie beschreiben, was Red Teaming ist. Sie lehren Sie nicht, es zu tun.

## KI-Observabilität ist eine eigene Disziplin

Traditionelles Sicherheitslogging überträgt sich nicht direkt auf KI-Systeme. Die Überwachung eines LLM oder Agenten in der Produktion erfordert andere Datenerhebung und andere Analyse.

KI-Observabilitätsinfrastruktur umfasst:

- Prompt- und Ausgabetelemetrie für Anomalieerkennung und Identifikation von Richtlinienverletzungen
- Werkzeugaufrufprotokolle für Agenten, einschließlich welche Werkzeuge mit welchen Argumenten aufgerufen wurden
- Abrufqualitätsüberwachung für RAG-Pipelines
- Erkennung und Klassifizierung von Jailbreak-Versuchen
- Ausgabekonsistenzüberwachung zur Erkennung von Modell-Drift zwischen Versionen
- Halluzinationsratenverfolgung für Anwendungen, bei denen faktische Genauigkeit wichtig ist
- Latenzmus­ter, die auf Prompt-Injection-Versuche hinweisen können, die die Kontextgröße aufblähen

Dies ist eine aufkommende Disziplin. Die meisten Organisationen, die KI im Jahr 2026 deployen, haben deutlich weniger Einblick in ihre KI-Komponenten als in ihre traditionelle Infrastruktur. Die meisten Governance-Zertifizierungen beschreiben nicht, wie ausreichende Observabilität für KI-Systeme aussieht.

## KI-Incident-Response ist anders als reguläre IR

Wenn ein traditionelles System kompromittiert wird, deckt Ihr IR-Playbook Eindämmung, Forensik und Wiederherstellung ab. KI-Vorfälle werfen Fragen auf, die das Standardplaybook nicht adressiert.

Fragen, für die Sie Playbooks brauchen, bevor Sie sie brauchen:

- Wie stellen Sie fest, ob ein Modell während des Feinabstimmens vergiftet wurde
- Wie bewerten Sie, ob ein RAG-Abruf missbraucht wurde, um vom Angreifer kontrollierten Inhalt zurückzugeben
- Wie identifizieren Sie, ob ein Agent nicht autorisierte Aktionen ausgeführt hat und was deren Umfang war
- Wie verifizieren Sie, ob ein Modell-Update von einem Drittanbieter das Verhalten auf sicherheitsrelevante Weise geändert hat
- Wie stellen Sie fest, was das Verhalten eines Modells vor einem Vorfall war, um es mit dem Verhalten nach dem Vorfall zu vergleichen

Dies erfordert Vorbereitung vor dem Vorfall. Es erfordert Protokolle und Telemetrie, die Sie vorab einrichten müssen. Es erfordert KI-spezifische Runbooks, die der Forensik des Modellverhaltens Raum widmen, nicht nur Netzwerkverkehr und Endpunktprotokollen.

## Das Zertifizierungs-Update-Problem

Ein struktureller Grund, warum Zertifizierungen hinter der aktuellen Praxis zurückbleiben: KI-Sicherheit ändert sich schneller als Zertifizierungs-Update-Zyklen erlauben.

Security+, CISSP und ISO 27001 decken Bereiche ab, die sich über Jahre entwickeln. Die Kern-Angriffsflächen von Netzwerken, Endpunkten und Anwendungen sind relativ stabil. KI-Angriffstechniken entwickeln sich über Monate. Prompt-Injection-Techniken, gegnerische Angriffsmethoden und agentische Angriffsflächen im Jahr 2026 sehen anders aus als das, was existierte, als die ersten KI-Zertifizierungen 2023 und 2024 gestartet wurden.

Zertifizierungsstellen aktualisieren Materialien nach Zeitplan. Das OWASP LLM Top 10 veröffentlichte innerhalb seines ersten Jahres eine wesentliche Überarbeitung. MCP existierte nicht als Unternehmensbedenken, als viele aktuelle KI-Zertifizierungen konzipiert wurden. Agentische KI-Sicherheitsframeworks datieren nach den meisten aktuellen Zertifizierungslehrplänen.

Dies ist ein strukturelles Problem, kein Mangel an Absicht. Sie müssen laufend Primärquellen lesen, statt eine Zertifizierung als festen Wissenskorpus zu behandeln.

## Was in KI-Sicherheits-Zertifizierungsinhalten sein muss

Damit Zertifizierungslehrpläne die aktuelle KI-Sicherheitspraxis widerspiegeln, müssen sie abdecken:

- Prompt-Injection-Defense-in-Depth: Eingabefilterung, Ausgabevalidierung, Werkzeugbegrenzung, Sandboxing und menschliche Genehmigungspforten sowie die dokumentierten Einschränkungen jedes Einzelnen
- Modell-Lieferketten-Verifikation: unsichere Serialisierungsrisiken, SBOM-Anforderungen, Herkunftsdokumentation und Verifikation signierter Artefakte
- KI-Agenten-Sicherheitsarchitektur: Vertrauensgrenzen, minimaler Privileg-Werkzeugzugang, Aktionsumkehrbarkeit und Überwachungsanforderungen
- MCP und externe Integrationssicherheit: Vertrauensbewertung für Werkzeugserver, Werkzeugberechtigungsprüfung und Datens-vs.-Anweisungstrennung
- Evaluation und Red Teaming: wie man eine gegnerische Evaluation abgrenzt, welche Benchmarks und Evaluierungsdatensätze existieren und wie man Ergebnisse interpretiert
- KI-Observabilität: welche Protokolle und Telemetrie KI-Systeme erfordern und wie man sie für Vorfallserkennung und -reaktion nutzt
- KI-spezifische Incident Response: Vorplanung für KI-Vorfallsszenarien, Beweismittelsammlung für Fragen des Modellverhaltens und Wiederherstellungsüberlegungen, die einzigartig für KI-Systeme sind
- Datenleckage-Prävention: RAG-Isolation, Prompt-Vertraulichkeit, mandantenfähige Zugriffskontrollen und Ausgabefilterung

## Was Sie jetzt tun sollten

Wenn Sie für KI-Systeme in Ihrer Organisation verantwortlich sind:

Lesen Sie das OWASP Top 10 für Large Language Model Applications und das OWASP Agentic AI Top 10. Sie sind kostenlos. Sie sind operativ spezifischer als jeder aktuelle bezahlte Zertifizierungslehrplan.

Überprüfen Sie MITRE ATLAS vor Ihrer nächsten Bedrohungsmodellierungssitzung für jede KI-Komponente. Wissen Sie, welche gegnerischen Taktiken auf Ihre Architektur zutreffen, bevor Sie Ihr Deployment-Design festlegen.

Lesen Sie NIST AI 600-1. Es erweitert das Basis-AI-RMF speziell für generative KI und ist für LLM- und Agenten-Deployments deutlich relevanter als das Basis-Framework allein.

Überprüfen Sie Google SAIF, Microsofts AI SDL und OWASP AI Exchange für Engineering-Anleitung, die Governance-Frameworks nicht liefern.

Verifizieren Sie die Herkunft jedes Modells, das Ihre Organisation deployt. Überprüfen Sie Modellkarten. Scannen Sie Serialisierungsformate auf bekannte Exploit-Klassen, bevor Sie Gewichte laden.

Ordnen Sie jeden KI-Agenten in Ihrer Umgebung gegen den Zugang zu, den er hält. Ein Agent mit Lese- und Schreibzugang auf Ihre interne Wissensdatenbank, E-Mail und Dateisystem ist ein Prompt-Injection-Amplifikator. Minimieren Sie seine Anmeldeinformationen auf das, was jede Aufgabe erfordert.

Verlangen Sie KI-spezifisches Red Teaming vor dem Deployment jedes Modells oder Agenten in einem hochfolgenreichen Kontext. Behandeln Sie es als obligatorisch, nicht optional.

Erstellen Sie KI-spezifische Incident-Response-Runbooks jetzt, bevor Sie sie brauchen.

Behandeln Sie Ihre Governance-Zertifizierung als Dokumentation Ihrer Prozessschicht. Sie ist keine Dokumentation Ihrer Sicherheitsposition.

## Referenzen

- NIST AI Risk Management Framework (AI RMF 1.0), 2023
- NIST AI 600-1: Generative AI Profile, 2024
- NIST SP 1270: Towards a Standard for Identifying and Managing Bias in Artificial Intelligence
- ISO/IEC 42001:2023 Artificial Intelligence Management Systems
- EU AI Act, Regulation (EU) 2024/1689
- OWASP Top 10 for Large Language Model Applications, 2025
- OWASP Agentic AI Top 10
- OWASP AI Exchange
- MITRE ATLAS: Adversarial Threat Landscape for AI Systems
- Google Secure AI Framework (SAIF)
- Microsoft AI Security SDL documentation
- CISA Guidance on AI Cybersecurity, 2024
- Barreno et al., Can Machine Learning Be Secure?, 2006
- Biggio et al., Poisoning Attacks Against Support Vector Machines, 2012
- Goodfellow et al., Explaining and Harnessing Adversarial Examples, ICLR 2015
- IAPP AI Governance Professional (AIGP) program documentation
- ISACA AI Fundamentals Certificate program documentation

---
title: "Microsoft-SOC-Heimlabor: 2026 Cybersicherheitserfahrung aufbauen"
date: 2026-09-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Richten Sie ein Microsoft-SOC-Heimlabor mit Sentinel, Defender, Intune und Entra ein. Üben Sie Incident-Untersuchungen, prüfen Sie Passkey-Richtlinien und dokumentieren Sie Belege für Ihr Portfolio."
genre: ["Cybersicherheit", "Cloudsicherheit", "Karriereentwicklung"]
tags: ["SOC-Heimlabor", "Microsoft Sentinel", "Microsoft Defender XDR", "Defender for Endpoint", "Defender for Cloud", "Defender for Servers", "Microsoft Intune", "Microsoft Entra ID", "Azure-Heimlabor", "Cybersicherheitserfahrung", "SOC-Analyst", "Security Operations Center", "Incident Response", "KQL", "Log Analytics", "Conditional Access", "phishingresistente MFA", "Passkeys", "Identitätssicherheit", "Cybersicherheitsportfolio", "Cloud-Kostenverwaltung", "Endpunktsicherheit"]
cover: "/img/cover/microsoft-soc-home-lab.webp"
coverAlt: "Ein Laptop zeigt Zeitachsen von Sicherheitsvorfällen auf einem Schreibtisch zu Hause unter einer Wolke mit Servern und Endpunkten."
coverCaption: ""
---

Ein **SOC-Heimlabor** bietet einen Ort, an dem Sie Warnungen untersuchen, Belege erklären und Schutzänderungen testen. Richten Sie eine kleine Microsoft-Umgebung ein, erfassen Sie deren Telemetrie und dokumentieren Sie jede Untersuchung. Das nützliche Ergebnis ist eine wiederholbare, beleggestützte Untersuchung.

Dieser Leitfaden erweitert den Laboransatz aus Mad Hats Karrierevideo zur Cybersicherheit und dem bereitgestellten Cyber-Range-Runbook. Für Produktanforderungen nutzt er Microsoft-Dokumentation und trennt Einrichtung, Erkennung und Prüfung in messbare Aufgaben.

## Wichtigste Punkte

- **Klein anfangen:** Ein verwalteter Windows-Client und eine Testidentität reichen für die ersten Übungen.
- **Telemetrie prüfen:** Ein sichtbares Gerät oder verbundenes Portal beweist keinen Logeingang.
- **Untersuchung abschließen:** Halten Sie Auslöser, Belege, Reaktion und Wiederholungstest fest.
- **Kosten kontrollieren:** Verfolgen Sie Lizenzen, Datenaufbewahrung, Netzwerk und Rechenleistung getrennt.
- **Erfahrung korrekt beschreiben:** Führen Sie die Umgebung im Lebenslauf als Laborprojekt auf.

## Bevor Sie beginnen

**Voraussetzungen:** Grundkenntnisse in Windows-Administration und Netzwerken sowie Erfahrung mit virtuellen Maschinen. Verwenden Sie einen eigenen Microsoft-Entra-Tenant und ein Azure-Abonnement ausschließlich für das Labor. Halten Sie Produktionsidentitäten, persönliche Dateien und Systeme Ihres Arbeitgebers aus der Übung heraus.

**Geschätzter Aufwand:** Planen Sie ein Wochenende für die Ersteinrichtung und danach gezielte Untersuchungssitzungen ein. Dies ist eine Planungsschätzung. Testfreigabe, Kontingente und Bereitstellung der Dienste beeinflussen die tatsächliche Dauer. **Schwierigkeit:** mittel.

Richten Sie ein separates Administratorkonto und einen unprivilegierten Testbenutzer ein. Legen Sie vor Zugriffstests einen Notfallzugang an und prüfen Sie ihn. Vergeben Sie Berechtigungen für einzelne Einrichtungsschritte und nutzen Sie für Routineuntersuchungen ein Konto mit geringeren Rechten.

| Komponente | Zweck im Labor |
|---|---|
| **Sentinel** | SIEM zur Verwaltung von Sicherheitsinformationen und Ereignissen verbundener Logquellen |
| **Defender XDR** | Korrelation und Untersuchung über lizenzierte Microsoft-Sicherheitsdienste hinweg |
| **Defender for Endpoint** | Endpunkterkennung und -reaktion auf eingebundenen Geräten |
| **Intune** | Geräteanmeldung und Verwaltung von Endpunktsicherheitsrichtlinien |
| **Entra ID** | Identitäten, Anmeldeprotokolle und Bewertung von Zugriffsrichtlinien |
| **Defender for Servers** | Serversicherheit über Defender for Cloud |

## Lizenzen zuerst prüfen

**Microsoft 365 E5** ist eine Möglichkeit für ein umfangreiches Labor. Der Zugriff hängt jedoch von den Dienstplänen und Lizenzen ab, die den beteiligten Benutzern zugewiesen sind. Office 365 E5 und Microsoft 365 E5 sind unterschiedliche Pakete. Die Lizenz eines Administrators deckt nicht automatisch alle Testbenutzer oder Workloads ab. Prüfen Sie vor der Abonnementwahl die [Voraussetzungen für Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/prerequisites).

**Sentinel im Defender-Portal** funktioniert ohne E5 und Defender XDR. XDR bringt eigene Lizenz- und Konfigurationsanforderungen mit. Eine leere Incident-Ansicht beweist keine fehlende E5-Lizenz. Die [Sentinel-Onboarding-Dokumentation](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard) beschreibt beide Konfigurationen.

**Serversicherheit** hat einen eigenen Lizenzweg. Defender for Servers integriert Defender for Endpoint für unterstützte Server-Workloads. Windows-Clientbetriebssysteme brauchen eine passende Clientabdeckung. Gehen Sie nicht davon aus, dass jede Azure-VM automatisch als Server lizenziert ist. Siehe Microsofts Dokumentation zur [Defender-for-Endpoint-Integration](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

**Testphase planen:** Prüfen Sie in Ihrem Konto Teilnahmeberechtigung, Ablauf, Verlängerung und enthaltene Dienste. Kalkulieren Sie nicht mit einer versprochenen Testdauer oder einem festen Monatsbetrag aus einem Video.

## Ausgaben planen

**Azure-Budgets** senden Benachrichtigungen. Sie stoppen den Verbrauch nicht, sobald ein Schwellenwert erreicht wird. Auch die Kostenberichte kommen verzögert. Richten Sie früh Warnungen ein und prüfen Sie die Ausgaben nach jeder Sitzung anhand der [Microsoft-Anleitung zur Budgeterstellung](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets).

| Kostenkategorie | Planungsfrage |
|---|---|
| **Benutzerlizenzen** | Welche Benutzer brauchen welche Dienstpläne und wann laufen Testphasen ab? |
| **Rechenleistung** | Wie viele VM-Stunden benötigt jede Übung? |
| **Speicher** | Welche Datenträger und Snapshots bleiben nach dem Herunterfahren? |
| **Logsammlung** | Welche Tabellen müssen Daten aufnehmen und wie lange sollen sie gespeichert bleiben? |
| **Netzwerk** | Umfasst der Entwurf kostenpflichtiges Bastion, öffentliche IPs oder ausgehende Dienste? |
| **Serversicherheit** | Für welche Workloads ist ein kostenpflichtiger Defender-Plan aktiv? |

**Entwurfsentscheidung:** Beginnen Sie mit einem Client. Ergänzen Sie einen Server, wenn eine Übung Servertelemetrie erfordert. Vier Clients und mehrere Server erhöhen Verwaltung und Kosten, bevor sie die Untersuchungspraxis verbessern.

## Netzwerk einrichten

**Vorgeschlagener Aufbau:** Legen Sie Azure-Ressourcen in einer klar benannten Gruppe wie **`rg-soc-lab`** ab. Trennen Sie Client- und Server-Subnetze, setzen Sie explizite Regeln für Netzwerksicherheitsgruppen und nutzen Sie privaten Verwaltungszugriff. Die Subnetztrennung allein blockiert keinen Verkehr zwischen Workloads.

Beachten Sie bei einer dedizierten **Azure-Bastion**-Bereitstellung die SKU-Anforderungen, darunter den reservierten Namen **`AzureBastionSubnet`** und ein Subnetz der Größe **`/26`** oder größer für aktuelle Bereitstellungen. Developer SKU nutzt ein anderes Bereitstellungsmodell. Prüfen Sie vor der Wahl die [Bastion-Konfigurationseinstellungen](https://learn.microsoft.com/en-us/azure/bastion/configuration-settings).

Halten Sie RDP und SSH vom öffentlichen Internet getrennt. Begrenzen Sie Verwaltungsverkehr auf den gewählten Pfad. Erlauben Sie die ausgehenden Verbindungen, die Geräteanmeldung und Sicherheitstelemetrie benötigen.

**Prüfung:** Richten Sie privaten Verwaltungszugriff ein und prüfen Sie die wirksamen Netzwerkregeln, bevor Sie Workloads installieren. Falls Sie später eine absichtlich verwundbare Anwendung ergänzen, halten Sie sie im Übungsnetz und beschränken Sie den Zugriff auf Testmaschinen.

## Sentinel und Logs verbinden

**Portal einrichten:** Erstellen Sie einen Log-Analytics-Arbeitsbereich und aktivieren Sie Sentinel darin. Fehlt der Arbeitsbereich im Defender-Portal, öffnen Sie **System > Settings > Microsoft Sentinel > Connect a workspace**. Prüfen Sie Tenant sowie erforderliche Azure- und Entra-Rollen anhand der [Onboarding-Voraussetzungen](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard).

**Logsammlung ist ein eigener Schritt.** Konfigurieren Sie in Entra Diagnosestellungen, die erforderliche Aktivitätskategorien an denselben Arbeitsbereich senden. Beginnen Sie mit interaktiven Anmeldungen und Auditereignissen. Der [Entra-Leitfaden zur Logintegration](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs) beschreibt Berechtigungen und Ziel.

Der aktuelle Sentinel-Ablauf unterstützt auch die Verbindung über das Microsoft-Defender-Portal. Prüfen Sie vor der Fehlersuche an einer leeren Tabelle, ob der vorgesehene primäre Arbeitsbereich, der passende Tenant für die Testidentitäten und die erforderlichen Kontorollen verwendet werden. Die Portalansicht beweist keine Datenerfassung. [Sentinel-Onboarding im Defender-Portal](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard)

```kusto
SigninLogs
| where TimeGenerated > ago(24h)
| where UserPrincipalName =~ "soc-test@YOUR-TENANT.onmicrosoft.com"
| project TimeGenerated, UserPrincipalName, AppDisplayName,
          IPAddress, ResultType, ConditionalAccessStatus, CorrelationId
| order by TimeGenerated desc
```

Führen Sie dieses **Kusto Query Language (KQL)**-Beispiel in der Logs-Ansicht des Arbeitsbereichs aus, nachdem Sie eine neue Testanmeldung erzeugt haben. Ersetzen Sie den Beispiel-UPN durch den Laborbenutzer. Die Spalten entsprechen dem [Schema der SigninLogs-Tabelle](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs).

**Erwartetes Ergebnis:** eine Zeile zum Testkonto und Anmeldezeitpunkt. Fehlt sie, prüfen Sie Zeitraum, Identität, Sammlungseinstellungen, Ziel und Erfassungsverzögerung. Fehlt die Tabelle, deutet das zunächst auf ein Erfassungs- oder Arbeitsbereichsproblem und erst danach auf ein Erkennungsproblem hin.

## Ersten Endpunkt einbinden

**Intune-Anmeldung und EDR-Onboarding** sind getrennte Prüfpunkte. Verbinden Sie Intune und Defender for Endpoint, melden Sie einen unterstützten Windows-Client an und weisen Sie dessen Laborgruppe eine EDR-Onboardingrichtlinie zu. Die Entra-Registrierung allein bestätigt keinen der beiden Punkte.

Prüfen Sie in Intune **Endpoint security > Defender for Endpoint**. Falls die Verbindung fehlt, aktivieren Sie die Intune-Verbindung in den erweiterten Endpunktfunktionen von Defender. Folgen Sie den plattformspezifischen Schritten im [Intune- und Defender-Integrationsleitfaden](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/configure-integration).

| Prüfpunkt | Zu erfassender Nachweis |
|---|---|
| **Anmeldung** | Client erscheint mit aktueller Synchronisierung in Intune |
| **Richtlinienzuweisung** | Onboardingrichtlinie gilt für die vorgesehene Gerätegruppe |
| **Sensorbericht** | Defender zeigt den Onboardingstatus und aktuelle Telemetrie |
| **Erkennungstest** | Ein dokumentierter Test erzeugt das erwartete Sicherheitssignal |

**Für Server** aktivieren Sie den gewählten Defender-for-Servers-Plan und die Endpunktintegration. Prüfen Sie dann Sensorbereitstellung und Berichte. Defender for Cloud erkennt Maschinen auch vor Abschluss des Onboardings. Ein Eintrag im Inventar allein reicht nicht, wie Microsofts Anleitung zur [Ressourcenerkennung und zum Onboarding](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint) erklärt.

## Testwarnung untersuchen

**Beginnen Sie mit Microsofts dokumentiertem EDR-Erkennungstest** auf dem Laborendpunkt. Befolgen Sie die [aktuellen Testanweisungen](https://learn.microsoft.com/en-us/defender-endpoint/edr-detection), einschließlich Plattformvoraussetzungen und Fehlerbehebung. Notieren Sie die Ausführungszeit, bevor Sie die Warnungswarteschlange öffnen.

Behandeln Sie die erzeugte Warnung als Untersuchungsübung. Der Produkttitel ist ein Ausgangspunkt. Sie müssen feststellen, was geschah, und die Entscheidung mit Belegen stützen.

1. **Triage:** Ermitteln Sie Quelle der Warnung, Gerät, Konto und Ereigniszeit.
2. **Prüfung:** Untersuchen Sie Prozessbaum, Befehlszeile, Dateidetails und verfügbare Netzwerkaktivität.
3. **Umfang:** Suchen Sie nach zugehöriger Aktivität bei der Testidentität und anderen Laborgeräten.
4. **Bewertung:** Erklären Sie, ob die Belege zur geplanten Übung oder zu einem fremden Ereignis passen.
5. **Reaktion:** Dokumentieren Sie gewählte Reaktion, Auswirkung und Wiederherstellung. Nutzen Sie unterstützte Eindämmung nur, wenn die Übung sie erfordert.
6. **Wiederholungstest:** Wiederholen Sie nach einer Kontrolländerung den passenden Test und vergleichen Sie die Belege.

**Erfinden Sie keine fehlenden Ergebnisse.** Kommt die Warnung nicht an, bewahren Sie den Ausführungsnachweis auf und untersuchen Sie die Sammlung. Blockiert eine Kontrolle den Test vor dem erwarteten Ereignis, dokumentieren Sie das Präventionsergebnis.

## Identitätskontrollen testen

**Adversary-in-the-middle-Phishing (AiTM)** setzt einen vom Angreifer kontrollierten Vermittler in den Anmeldeablauf. Das bereitgestellte Runbook nutzt dieses Szenario als Begründung für stärkere Authentifizierung. Testen Sie bei der ersten Identitätsübung die Richtlinien direkt mit Ihrem eigenen unprivilegierten Konto.

Dokumentieren Sie zuerst eine legitime Anmeldung und deren Authentifizierungsdetails. Lesen Sie Microsofts [Referenz zur Entra-Risikoerkennung](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks), bevor Sie Risikosignale auslegen. Voraussetzungen und Verarbeitung unterscheiden sich je Signal. Eine neue IP-Adresse oder eine fehlgeschlagene Anmeldung garantiert keine AiTM-Warnung.

**Passkeys (FIDO2)** verwenden Anmeldedaten, die an den echten Dienst gebunden sind, statt wiederverwendbarer Codes auf einer weitergeleiteten Anmeldeseite. Aktivieren Sie für die Pilotgruppe ein passendes Passkey-Profil und registrieren Sie die Methode vor der Richtlinienerzwingung. Der [Microsoft-Leitfaden zur Passkey-Konfiguration](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2) nennt unterstützte Authentifikatoren und Einschränkungen.

**Conditional-Access-Übung:** Erstellen Sie eine Richtlinie nur für die Labor-Pilotgruppe, schließen Sie Notfallzugriffskonten aus und wählen Sie **Require authentication strength > Phishing-resistant MFA strength**. Beginnen Sie mit **Report-only**, prüfen Sie die Auswirkungen und aktivieren Sie danach die Richtlinie. Passen Sie das [Microsoft-Beispiel für eine Administrationsrichtlinie](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa) an eine kleine Testgruppe an.

| Test | Zu erfassender Nachweis |
|---|---|
| **Report-only-Richtlinie** | Anmeldeprotokoll mit Auswertung der vorgeschlagenen Richtlinie |
| **Erzwungene Richtlinie, schwächere Methode** | Neue Authentifizierung verlangt vor dem Zugriff eine stärkere Methode |
| **Erzwungene Richtlinie, registrierter Passkey** | Erfolgreiche Anmeldung mit der erforderlichen Stärke |

Nutzen Sie für jeden Vergleich eine frische Authentifizierung und prüfen Sie die Richtliniendetails. Bestehende Sitzungen erschweren den Vergleich. **Aussagebereich:** Die Übung prüft die Authentifizierungsanforderung. Sie belegt keinen universellen Schutz vor einer Endpunktkompromittierung oder dem Diebstahl einer bestehenden Sitzung.

## Portfolio-Nachweise verfassen

**Ein nützlicher Portfolioeintrag** erklärt eine Entscheidung so, dass ein anderer Analyst sie bewerten kann. Ergänzen Sie eine kurze Architekturübersicht, Voraussetzungen der Datenerfassung, Ereigniszeitlinie und Begründung der Reaktion.

```text
Übung:
Datum und UTC-Zeitfenster:
Laborumfang und Voraussetzungen:
Auslöser und erwartetes Signal:
Beobachtete Warnung oder Verhinderung:
Belege und Abfragen:
Betroffene Identitäten und Geräte:
Bewertung und Begründung:
Reaktion und Wiederherstellung:
Kontrolländerung und erneuter Test:
Einschränkungen und Nachverfolgung:
```

Ersetzen Sie jedes Feld durch eigene Beobachtungen. **Bereinigen Sie Exporte:** Entfernen Sie Zugangsdaten, Sitzungsdaten, persönliche Informationen und unnötige Kennungen aus Screenshots und Abfrageergebnissen, bevor Sie sie veröffentlichen.

**Lebenslaufbeispiel:** „Microsoft-Sicherheitslabor aufgebaut, Identitätslogs mit Sentinel verbunden, Endpoint-Testwarnungen untersucht und Conditional-Access-Prüfung dokumentiert.“ Verwenden Sie diese Formulierung erst nach Abschluss der Aufgaben. Führen Sie sie mit tatsächlichem Zeitraum und Umfang unter Projekten oder Praxiserfahrung auf.

Ein Labor zeigt selbstständige Praxis. **Arbeit in einem Produktions-SOC** umfasst zudem Geschäftsauswirkungen, Eskalationen, Serviceverpflichtungen und Teamkoordination. Erläutern Sie, welche Teile Sie geübt haben und welche noch außerhalb Ihrer Erfahrung liegen.

## Fehlerbehebung

| Symptom | Erste Prüfung |
|---|---|
| **Arbeitsbereich fehlt in Defender** | Gleicher Tenant, Sentinel aktiviert und erforderliche Onboardingrollen |
| **SigninLogs fehlt oder ist leer** | Diagnosekategorien, Zielarbeitsbereich, neue Ereignisse und Zeitraum |
| **Client fehlt in Intune** | Voraussetzungen und Anmeldestatus |
| **Gerät sichtbar, aber keine Telemetrie** | Tatsächlicher Onboardingstatus, Sensorzustand und ausgehende Verbindung |
| **Onboardingrichtlinie nicht angewendet** | Zuweisungsumfang, Geräteplattform und aktuelle Synchronisierung |
| **Keine Identitätsrisikowarnung** | Signalvoraussetzungen und aufgezeichnete Aktivität, ohne deterministische Erkennung anzunehmen |
| **Zugriff unerwartet gewährt** | Report-only-Status, Ausschlüsse, Ressourcenbereich und bestehende Sitzung |
| **Kosten nach dem Herunterfahren** | Zuweisungsstatus und unabhängig vom Rechnen abgerechnete Ressourcen |

**Reihenfolge der Fehlersuche:** Belegen Sie zuerst, dass das Ereignis stattfand. Prüfen Sie dann die Sammlung und zuletzt die Erkennungslogik. Halten Sie Fehler und Korrekturen in den Projektnotizen fest.

## Labor pausieren oder entfernen

**Deallokation** gibt die VM-Rechenressource frei. Das Herunterfahren des Gastbetriebssystems allein garantiert keine Deallokation. Prüfen Sie den in Azure angezeigten Betriebszustand und Microsofts Dokumentation zu [VM-Zuständen und Abrechnung](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing).

**Behaltene Ressourcen** müssen ebenfalls geprüft werden. Datenträger, Snapshots, Netzwerkdienste, Logaufbewahrung und Benutzerabonnements haben getrennte Lebenszyklen. Richten Sie vor jedem Testablauf eine Erinnerung ein und prüfen Sie nach der Bereinigung den nächsten Nutzungsbericht.

Exportieren und prüfen Sie vor dem Löschen der Laborressourcengruppe die aufzubewahrenden Nachweise. **Das Löschen der Ressourcengruppe ist destruktiv** für enthaltene Ressourcen. Tenant-Benutzer, Intune- und Conditional-Access-Richtlinien, Abonnements und Sicherheitseinstellungen auf Abonnementebene müssen gegebenenfalls separat bereinigt werden.

## Nächste Schritte

**Schließen Sie eine dokumentierte Untersuchung ab**, bevor Sie einen weiteren Workload hinzufügen. Ergänzen Sie danach einen Server, eine Identitätsübung oder eine Erkennungsregel mit klarer Testbedingung. Notieren Sie Nutzen und Kosten der neuen Komponente.

Nutzen Sie den [IT-Heimlaborleitfaden](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/) für Infrastrukturübungen und den [IT-Lebenslaufleitfaden](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/) zur Darstellung der Arbeit. Halten Sie das nächste Projekt klein genug, um Einrichtung, Belege und Bereinigung zu erklären.

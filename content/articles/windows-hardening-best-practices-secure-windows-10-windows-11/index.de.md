---
title: "Grundlegende Best Practices zur Windows-Härtung für ein sicheres Windows 10 und Windows 11"
date: 2023-07-27
toc: true
draft: false
description: "Entdecken Sie effektive Strategien zur Verbesserung der Sicherheit Ihrer Windows 10- und Windows 11-Systeme durch umfassende Härtungstechniken und Best Practices."
genre: ["Windows-Härtung", "Windows-Sicherheit", "Härtung von Windows 10", "Härtung von Windows 11", "Bewährte Windows-Sicherheitspraktiken", "Tipps zur Windows-Sicherheit", "Windows-Sicherheitsrichtlinien", "Absicherung von Windows-Betriebssystemen", "Härtung des Windows-Systems", "Windows-Sicherheitsmaßnahmen"]
tags: ["Windows-Härtung", "Windows-Sicherheit", "Windows 10", "Fenster 11", "Sicherheit des Betriebssystems", "Windows Defender", "Benutzerkontensteuerung", "BitLocker-Verschlüsselung", "Firewall-Konfiguration", "AppLocker-Richtlinien", "Windows-Updates", "sichere Passwörter", "Datensicherung", "Windows Hello", "Sicherer Start", "TPM", "Microsoft Defender Antivirus", "Windows-Sandkasten", "Microsoft Defender Application Guard", "Kontrollierter Ordnerzugriff", "Bewährte Verfahren zur Sicherung von Windows 10 und Windows 11", "Wie man Windows-Betriebssysteme härtet", "Windows-Sicherheitsmaßnahmen für Einzelpersonen und Unternehmen", "Verbesserung der Sicherheit des Windows-Systems", "Schutz von Daten mit BitLocker-Verschlüsselung", "Isolierung von Browser-Sitzungen mit Microsoft Defender Application Guard", "Tipps und Richtlinien zur Sicherheit von Windows 10", "Implementierung von Windows-Sicherheitsfunktionen", "Absicherung von Windows mit hardwarebasierter Isolierung", "Sicherstellung der Integrität des Windows-Systems"]
cover: "/img/cover/A_cartoon_illustration_of_a_shield_protecting-windows.png"
coverAlt: "Eine Cartoon-Illustration eines Schildes, das ein Windows-Logo vor verschiedenen Cyber-Bedrohungen schützt."
coverCaption: "Sichern Sie Ihre Windows-Festung mit effektiven Härtungstechniken."
---

## Einleitung

Windows-Betriebssysteme werden von Privatpersonen und Organisationen auf der ganzen Welt eingesetzt. Um die Sicherheit und Integrität dieser Systeme zu gewährleisten, ist es unerlässlich, **Windows hardening best practices** zu implementieren. Bei der Härtung geht es darum, das Betriebssystem zu sichern, indem die Angriffsfläche reduziert und potenzielle Schwachstellen beseitigt werden. Dieser Artikel befasst sich mit den Best Practices für die Härtung von **Windows 10** und den neueren **Windows 11**-Betriebssystemen und liefert wertvolle Erkenntnisse zur Verbesserung der Sicherheit Ihrer Windows-Umgebung.

______

## Windows-Härtung verstehen

Unter Windows-Härtung versteht man den Prozess der Verbesserung der Sicherheit eines Windows-Betriebssystems. Dazu gehören die Konfiguration verschiedener Einstellungen und die Implementierung von Sicherheitsmaßnahmen zum Schutz vor unbefugtem Zugriff, Malware und anderen Bedrohungen. Durch die Härtung Ihres Windows-Systems können Sie die mit Cyberangriffen verbundenen Risiken minimieren und die Vertraulichkeit, Integrität und Verfügbarkeit Ihrer Daten sicherstellen.

### [Hardening Windows 10](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 10 ist eines der weltweit am häufigsten verwendeten Betriebssysteme. Um Ihre Windows 10-Umgebung abzusichern, sollten Sie die folgenden Best Practices beachten:

#### 1. [**Enable Windows Defender**](https://github.com/simeononsecurity/Windows-Defender-Hardening)

Windows Defender ist eine **robuste Antivirenlösung**, die in Windows 10 enthalten ist. Sie bietet eine Reihe von Sicherheitsfunktionen zum Schutz Ihres Systems vor verschiedenen Arten von **Malware**, einschließlich **Viren, Spyware und Ransomware**. Durch die Aktivierung von Windows Defender können Sie die Sicherheit Ihrer Windows 10-Umgebung erheblich verbessern.

Um Windows Defender zu aktivieren, führen Sie die folgenden Schritte aus:

- Öffnen Sie die App **Windows Sicherheit**, indem Sie auf das Windows-Sicherheitssymbol in der Taskleiste klicken oder im Startmenü nach "Windows-Sicherheit" suchen.
- Klicken Sie in der Windows-Sicherheitsanwendung im linken Navigationsbereich auf "**Viren- und Bedrohungsschutz**".
- Klicken Sie auf "**Einstellungen verwalten**" unter dem Abschnitt "Einstellungen für Viren- und Bedrohungsschutz".
- Vergewissern Sie sich, dass der Schalter "**Echtzeitschutz**" auf "**Ein**" gesetzt ist. Dadurch wird Windows Defender in die Lage versetzt, Ihr System aktiv in Echtzeit zu scannen und zu schützen.
- Außerdem können Sie die Scan-Optionen und Ausschlüsse anpassen, indem Sie auf "**Scan-Optionen**" bzw. "**Ausschlüsse hinzufügen oder entfernen**" klicken.

Es ist wichtig, Windows Defender **regelmäßig zu aktualisieren**, um sicherzustellen, dass er über die neuesten **Malware-Definitionen** und **Sicherheitsverbesserungen** verfügt. Microsoft veröffentlicht regelmäßig Updates, um neue Bedrohungen und Sicherheitslücken zu schließen. Um Windows Defender zu aktualisieren, können Sie die folgenden Schritte ausführen:

- Öffnen Sie die Windows-Sicherheits-App.
- Gehen Sie im linken Navigationsbereich zu "**Viren- und Bedrohungsschutz**".
- Klicken Sie unter dem Abschnitt "Viren- und Bedrohungsschutz-Updates" auf "**Nach Updates suchen**".
- Windows prüft, ob Updates verfügbar sind, und lädt/installiert sie bei Bedarf.

Wenn Sie Windows Defender aktivieren und auf dem neuesten Stand halten, können Sie Ihr Windows 10-System proaktiv vor Malware und anderen Sicherheitsbedrohungen schützen. Es wird außerdem empfohlen, **regelmäßige Systemscans** mit Windows Defender durchzuführen, um sicherzustellen, dass alle potenziellen Bedrohungen erkannt und entfernt werden.

Denken Sie daran, dass Windows Defender zwar ein solides Schutzniveau bietet, es aber unbedingt mit **sicheren Surfgewohnheiten**, **regelmäßigen Software-Updates** und anderen Sicherheitsmaßnahmen ergänzt werden muss, um eine sichere Windows 10-Umgebung zu erhalten.

#### 2. [**Keep Windows 10 Updated**](https://support.microsoft.com/en-us/windows/windows-update-faq-8a903416-6f45-0718-f5c7-375e92dddeb2)
Die regelmäßige Installation von Windows-Updates ist ein wichtiger Aspekt der **Härtung von Windows 10**. Diese Updates enthalten **Sicherheitspatches**, Fehlerbehebungen und Leistungsverbesserungen, die dazu beitragen, **Sicherheitslücken** zu schließen und die Systemstabilität zu verbessern.

Microsoft veröffentlicht **regelmäßige Updates** für Windows 10, um neu entdeckte Sicherheitsprobleme zu beheben und die allgemeine Benutzerfreundlichkeit zu verbessern. Indem Sie Ihr System auf dem neuesten Stand halten, stellen Sie sicher, dass Ihr Betriebssystem über die neuesten **Sicherheitsverbesserungen** verfügt, um sich vor neuen Bedrohungen zu schützen.

Um Windows 10 auf dem neuesten Stand zu halten, können Sie die folgenden Schritte ausführen:

1. **Automatische Updates aktivieren**: Windows 10 ist standardmäßig so konfiguriert, dass Updates automatisch heruntergeladen und installiert werden. Dadurch wird sichergestellt, dass Ihr System die erforderlichen Updates ohne manuelles Eingreifen erhält. Führen Sie die folgenden Schritte aus, um zu überprüfen, ob automatische Updates aktiviert sind:
   - Gehen Sie zu **Einstellungen**, indem Sie auf das Startmenü klicken und das Zahnradsymbol auswählen.
   - Klicken Sie auf **Update & Sicherheit**.
   - Klicken Sie im linken Navigationsbereich auf **Windows Update**.
   - Stellen Sie sicher, dass die Option **Automatisch** unter **Windows Update-Einstellungen** ausgewählt ist. Wenn sie nicht ausgewählt ist, klicken Sie auf den Link **"Aktive Stunden ändern "**, um die aktiven Stunden festzulegen, in denen Windows die Installation von Updates vermeiden soll.

2. **Aktualisierungen manuell installieren**: Wenn Sie es vorziehen, mehr Kontrolle über den Update-Prozess zu haben, können Sie Updates manuell auf Ihrem Windows 10-System installieren. So geht's:
   - Gehen Sie zu **Einstellungen** > **Update & Sicherheit** > **Windows Update**.
   - Klicken Sie auf **Nach Updates suchen**, um zu sehen, ob Updates für Ihr System verfügbar sind.
   - Wenn Updates gefunden werden, klicken Sie auf **"Herunterladen "** und **"Installieren "**, um den Installationsvorgang zu starten.

Es ist wichtig zu betonen, dass Sie Ihr System **regelmäßig neu starten**, nachdem Sie Updates installiert haben. Einige Updates erfordern möglicherweise einen Neustart des Systems, um die Änderungen vollständig zu übernehmen und ihre Wirksamkeit zu gewährleisten.

Wenn Sie **Ihr Windows 10-System auf dem neuesten Stand halten**, erhöhen Sie nicht nur seine Sicherheit, sondern profitieren auch von den neuesten Funktionen, Leistungsverbesserungen und Kompatibilitätsbehebungen. Es ist eine proaktive Maßnahme, um sicherzustellen, dass Ihr System gegen potenzielle Sicherheitsbedrohungen widerstandsfähig bleibt.

#### 3. [**Configure User Account Control (UAC)**](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-overview)
Die Benutzerkontensteuerung (UAC) ist eine Sicherheitsfunktion in Windows 10, die dazu beiträgt, unbefugte Änderungen an Ihrem System zu verhindern, indem sie bei Bedarf die Genehmigung des Administrators einholt. Sie dient als Schutz vor bösartiger Software oder unbefugten Benutzern, die versuchen, Änderungen vorzunehmen, die die Systemsicherheit oder -stabilität beeinträchtigen könnten.

Die Konfiguration der UAC-Einstellungen auf eine angemessene Stufe ist entscheidend für die **Härtung von Windows 10**. Es geht darum, ein Gleichgewicht zwischen Sicherheit und Benutzerfreundlichkeit zu finden, um sicherzustellen, dass die UAC Ihr System effektiv schützt, ohne unnötige Unterbrechungen zu verursachen.

Um die UAC-Einstellungen in Windows 10 zu konfigurieren, können Sie die folgenden Schritte ausführen:

1. Öffnen Sie die **Systemsteuerung**, indem Sie "Systemsteuerung" in die Suchleiste eingeben und sie aus den Suchergebnissen auswählen.

2. Klicken Sie in der Systemsteuerung auf **"Benutzerkonten "**.

3. Klicken Sie auf **"Einstellungen der Benutzerkontensteuerung ändern "**.

4. Sie sehen einen Schieberegler mit verschiedenen Stufen der UAC-Einstellungen. Hier sind die verfügbaren Optionen:
   - **"Immer benachrichtigen "**: Dies ist die höchste Sicherheitsstufe der Benutzerkontensteuerung, bei der Sie bei allen Systemänderungen, selbst bei einfachen Aufgaben, um Ihre Zustimmung gebeten werden.
   - **"Nur benachrichtigen, wenn Anwendungen versuchen, Änderungen an meinem Computer vorzunehmen (Standard) "**: Dies ist die empfohlene Einstellung, die ein Gleichgewicht zwischen Sicherheit und Benutzerfreundlichkeit bietet. Sie werden um Zustimmung gebeten, wenn Anwendungen Änderungen vornehmen, aber nicht bei Änderungen der Windows-Einstellungen.
   - **"Nur benachrichtigen, wenn Anwendungen versuchen, Änderungen an meinem Computer vorzunehmen (den Desktop nicht verdunkeln) "**: Ähnlich wie die vorherige Option, aber der Desktop wird nicht abgedunkelt, wenn UAC-Aufforderungen erscheinen.
   - **"Nie benachrichtigen "**: Dies ist die niedrigste Stufe der UAC-Sicherheit, bei der Sie nicht zu Systemänderungen aufgefordert werden.

5. Wählen Sie die UAC-Sicherheitsstufe, die Ihren Bedürfnissen entspricht, indem Sie den Schieberegler in die gewünschte Position schieben.

6. Klicken Sie auf **"OK "**, um die Änderungen zu speichern.

Es wird empfohlen, die Benutzerkontensteuerung zu aktivieren und auf eine Stufe einzustellen, die ein angemessenes Gleichgewicht zwischen Sicherheit und Benutzerfreundlichkeit bietet. Die vollständige Deaktivierung der Benutzerkontensteuerung kann Ihr System anfälliger für unbefugte Änderungen machen und möglicherweise seine Sicherheit gefährden.

Durch die Konfiguration der UAC-Einstellungen erhöhen Sie die Sicherheit Ihres Windows 10-Systems, indem Sie sicherstellen, dass für kritische Systemänderungen Administratorrechte erforderlich sind, wodurch das Risiko eines unbefugten Zugriffs und einer Malware-Infektion verringert wird.

#### 4. [**Use Strong Passwords**](https://simeononsecurity.com/articles/how-to-create-strong-passwords/)
Die Verwendung sicherer Kennwörter ist für die Sicherheit Ihres Windows 10-Systems und den Schutz vor unbefugtem Zugriff unerlässlich. Schwache oder leicht zu erratende Passwörter können Ihr System anfällig für Angriffe machen, wie z. B. Brute-Force-Angriffe oder Passwort-Cracking.

Um sicherzustellen, dass alle Benutzerkonten auf Ihrem Windows 10-System über sichere Kennwörter verfügen, befolgen Sie diese bewährten Kennwortpraktiken:

1. **Komplexität**: Ermutigen Sie die Benutzer, Passwörter zu erstellen, die komplex und nicht leicht zu erraten sind. Ein sicheres Passwort sollte eine Kombination aus Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen enthalten. Vermeiden Sie die Verwendung allgemeiner Wörter oder vorhersehbarer Muster.

2. **Länge**: Längere Passwörter sind im Allgemeinen sicherer. Ermuntern Sie die Benutzer, Passwörter zu erstellen, die mindestens 8 Zeichen lang sind, vorzugsweise aber länger. Je mehr Zeichen ein Passwort hat, desto schwieriger ist es zu knacken.

3. **Einzigartigkeit**: Jedes Benutzerkonto sollte ein eindeutiges Passwort haben. Die Verwendung desselben Passworts für mehrere Konten erhöht das Risiko eines Sicherheitsverstoßes. Ermutigen Sie die Benutzer, unterschiedliche Passwörter für verschiedene Konten zu verwenden.

4. **Vermeiden Sie persönliche Informationen**: Raten Sie Benutzern davon ab, persönliche Informationen wie Namen, Geburtsdaten oder Adressen in ihren Passwörtern zu verwenden. Diese Informationen können von Angreifern leicht erlangt oder erraten werden.

5. **Passwort-Manager**: Erwägen Sie die Verwendung eines Passwort-Managers, um Passwörter sicher zu speichern und zu verwalten. Passwort-Manager können starke, eindeutige Passwörter für jedes Konto generieren und sie in einer verschlüsselten Datenbank speichern.

6. **Passwörter regelmäßig ändern**: Ermuntern Sie die Benutzer, ihre Passwörter regelmäßig zu ändern, um die Sicherheit zu gewährleisten. Legen Sie eine Richtlinie für das Ablaufen von Passwörtern fest und klären Sie die Benutzer darüber auf, wie wichtig es ist, ihre Passwörter regelmäßig zu aktualisieren.

Durch die Einführung sicherer Kennwortpraktiken erhöhen Sie die Sicherheit Ihres Windows 10-Systems erheblich und verringern das Risiko eines unbefugten Zugriffs oder von Datenverletzungen. Informieren Sie die Benutzer regelmäßig über die Sicherheit von Passwörtern und stellen Sie ihnen Ressourcen zur Verfügung, z. B. Messgeräte für die Passwortstärke oder Richtlinien zur Erstellung von Passwörtern, um sie bei der Erstellung sicherer Passwörter zu unterstützen.

Ausführlichere Informationen über die Erstellung sicherer Kennwörter und bewährte Verfahren finden Sie in diesem [article](https://simeononsecurity.com/articles/how-to-create-strong-passwords/) Es bietet eine umfassende Anleitung zur Passwortsicherheit und gibt Tipps zur Erstellung sicherer und einprägsamer Passwörter.

Denken Sie daran, dass die Verwendung sicherer Passwörter ein grundlegender Aspekt der Systemsicherheit ist und Priorität haben sollte, um sensible Daten zu schützen und die Integrität Ihrer Windows 10-Umgebung zu gewährleisten.

#### 5. [**Enable BitLocker Encryption**](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)
Eine der effektivsten Möglichkeiten, sensible Daten auf Ihrem Windows 10-System zu schützen, ist die Aktivierung der BitLocker-Verschlüsselung. BitLocker bietet eine vollständige Festplattenverschlüsselung und stellt sicher, dass Ihre Daten auch bei Verlust oder Diebstahl Ihres Geräts sicher und für Unbefugte unzugänglich bleiben.

Führen Sie die folgenden Schritte aus, um die BitLocker-Verschlüsselung zu aktivieren und Ihre vertraulichen Daten zu schützen:

1. **Prüfen Sie die Systemanforderungen**: Stellen Sie sicher, dass Ihre Windows 10-Edition die BitLocker-Verschlüsselung unterstützt. BitLocker ist in den Editionen Windows 10 Pro, Enterprise und Education verfügbar.

2. **BitLocker aktivieren**: Öffnen Sie die Systemsteuerung und navigieren Sie zur Kategorie "System und Sicherheit". Klicken Sie auf "BitLocker-Laufwerkverschlüsselung" und wählen Sie das/die Laufwerk(e) aus, die Sie verschlüsseln möchten. Folgen Sie den Anweisungen auf dem Bildschirm, um den Verschlüsselungsprozess zu starten.

3. **Wählen Sie Verschlüsselungsoptionen**: Während der BitLocker-Einrichtung haben Sie die Möglichkeit, zwischen verschiedenen Verschlüsselungsmethoden zu wählen, z. B. der Verwendung eines Kennworts, einer Smartcard oder beidem. Wählen Sie je nach Ihren Sicherheitsanforderungen und Präferenzen die geeignete Methode aus.

4. **Wiederherstellungsschlüssel sichern**: Es ist wichtig, den BitLocker-Wiederherstellungsschlüssel zu sichern. Dieser Schlüssel dient als Ausfallsicherung, falls Sie Ihr Kennwort vergessen oder Probleme beim Zugriff auf das verschlüsselte Laufwerk auftreten. Bewahren Sie den Wiederherstellungsschlüssel an einem sicheren Ort getrennt von Ihrem Gerät auf.

5. **Verwalten der BitLocker-Einstellungen**: Nachdem Sie BitLocker aktiviert haben, können Sie weitere Einstellungen anpassen, z. B. die automatische Entsperrung für bestimmte Laufwerke oder die Konfiguration der Verwendung von TPM (Trusted Platform Module) für zusätzliche Sicherheit. Auf diese Einstellungen kann über die BitLocker-Verwaltungsoberfläche zugegriffen werden.

Durch die Aktivierung der BitLocker-Verschlüsselung fügen Sie Ihrem Windows 10-System eine zusätzliche Schutzebene hinzu und stellen sicher, dass Ihre Daten sicher und unzugänglich bleiben, selbst wenn Ihr Gerät in die falschen Hände gerät. Es ist wichtig, Ihre BitLocker-Einstellungen regelmäßig zu aktualisieren und zu pflegen, um mit den bewährten Sicherheitsverfahren auf dem neuesten Stand zu bleiben.

Ausführlichere Informationen zur Aktivierung und Verwaltung der BitLocker-Verschlüsselung finden Sie in der offiziellen [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview) Es bietet eine umfassende Anleitung zur BitLocker-Verschlüsselung, einschließlich erweiterter Funktionen und Konfigurationsoptionen.

Denken Sie daran, dass die Aktivierung der BitLocker-Verschlüsselung zum Schutz Ihrer sensiblen Daten beiträgt und Ihnen die Gewissheit verschafft, dass Ihre Informationen auch bei Verlust oder Diebstahl sicher sind.

#### 6. **Deaktivieren Sie nicht benötigte Dienste und Funktionen**
Um die Sicherheit Ihres Windows 10-Systems zu erhöhen, ist es wichtig, dass Sie alle unnötigen Dienste und Funktionen überprüfen und deaktivieren. Auf diese Weise reduzieren Sie die Angriffsfläche und minimieren das Potenzial für die Ausnutzung durch böswillige Akteure.

Hier sind die Schritte zum Deaktivieren unnötiger Dienste und Funktionen auf Ihrem Windows 10-System:

1. **Identifizieren Sie unnötige Dienste**: Beginnen Sie mit der Identifizierung der Dienste, die auf Ihrem System laufen. Öffnen Sie die Verwaltungskonsole "Dienste", indem Sie **Windows-Taste + R** drücken, **services.msc** eingeben und **Enter** drücken. Überprüfen Sie die Liste der Dienste und recherchieren Sie deren Zweck, um festzustellen, welche Dienste für die Funktionalität Ihres Systems unerlässlich sind.

2. **Deaktivieren Sie nicht benötigte Dienste**: Sobald Sie die unnötigen Dienste identifiziert haben, klicken Sie mit der rechten Maustaste auf jeden Dienst und wählen Sie **Eigenschaften**. Ändern Sie im Fenster Eigenschaften den **Starttyp** in **Deaktiviert**. Dadurch wird verhindert, dass der Dienst beim Hochfahren Ihres Systems automatisch gestartet wird. Seien Sie vorsichtig und stellen Sie sicher, dass Sie nur Dienste deaktivieren, die für den normalen Betrieb Ihres Systems nicht erforderlich sind.

3. **Unnötige Funktionen deaktivieren**: Zusätzlich zu den Diensten enthält Windows 10 auch verschiedene Funktionen, die für Ihr System möglicherweise nicht erforderlich sind. Öffnen Sie die **Systemsteuerung**, navigieren Sie zu **Programme** oder **Programme und Funktionen**, und klicken Sie auf **Windows-Funktionen ein- oder ausschalten**. Deaktivieren Sie alle Funktionen, die Sie nicht benötigen. Dieser Schritt trägt dazu bei, die Angriffsfläche weiter zu verringern und die von unnötigen Funktionen verbrauchten Ressourcen zu minimieren.

4. **Regelmäßig überprüfen und aktualisieren**: Es ist wichtig, dass Sie die Liste der auf Ihrem Windows 10-System aktivierten Dienste und Funktionen regelmäßig überprüfen. Da sich die Anforderungen an Ihr System im Laufe der Zeit ändern, müssen Sie möglicherweise die erforderlichen Dienste und Funktionen neu bewerten. Bleiben Sie wachsam und aktualisieren Sie Ihre Konfiguration nach Bedarf.

Indem Sie unnötige Dienste und Funktionen deaktivieren, schränken Sie die potenziellen Einstiegspunkte für Angreifer ein und verringern die gesamte Angriffsfläche Ihres Windows 10-Systems. Diese Vorgehensweise verbessert die Sicherheitslage Ihres Systems und verringert das Risiko eines Angriffs.

Weitere Informationen zur Verwaltung von Diensten und Funktionen in Windows 10 finden Sie im Folgenden [article](https://www.tweakhound.com/2015/07/27/windows-10-default-services/#:~:text=Windows%2010%20Default%20Services%20%20%20%20Name,%20%20%20%2044%20more%20rows%20) für eine ausführliche Anleitung.

Denken Sie daran, dass Sie bei der Deaktivierung von Diensten und Funktionen Vorsicht walten lassen müssen, da die Deaktivierung wichtiger Komponenten die Funktionalität Ihres Systems beeinträchtigen kann. Informieren Sie sich immer über den Zweck eines Dienstes oder einer Funktion, bevor Sie Änderungen vornehmen.

#### 7. **Implementieren von Firewall-Regeln**
Die in Windows 10 integrierte Firewall dient als wichtige Verteidigungslinie gegen nicht autorisierten Netzwerkverkehr. Durch die Konfiguration von Firewall-Regeln können Sie steuern, welche ein- und ausgehenden Verbindungen zulässig sind, und so die Sicherheit Ihres Systems erhöhen.

Folgen Sie diesen Schritten, um Firewall-Regeln auf Ihrem Windows 10-System zu implementieren:

1. **Zugriff auf die Firewall-Einstellungen**: Um auf die Firewall-Einstellungen zuzugreifen, öffnen Sie die **Systemsteuerung**, suchen Sie nach **Windows Defender Firewall**, und klicken Sie auf das entsprechende Ergebnis. Alternativ können Sie auch mit der rechten Maustaste auf die Schaltfläche **Start** klicken, **Einstellungen** auswählen und zu **Netzwerk & Internet > Windows-Firewall** navigieren.

2. Konfigurieren Sie **Eingangsregeln**: Eingehende Regeln kontrollieren eingehende Netzwerkverbindungen zu Ihrem System. Klicken Sie im Fenster Windows Defender Firewall auf **Erweiterte Einstellungen**. Wählen Sie im neuen Fenster **Eingehende Regeln** und klicken Sie auf **Neue Regel**. Folgen Sie den Anweisungen auf dem Bildschirm, um Regeln zu erstellen, die nur notwendige eingehende Verbindungen zulassen. Berücksichtigen Sie die Dienste und Anwendungen, die Netzwerkzugriff benötigen, und erstellen Sie entsprechende Regeln.

3. **Konfigurieren Sie ausgehende Regeln**: Ausgehende Regeln kontrollieren ausgehende Netzwerkverbindungen von Ihrem System. Führen Sie die gleichen Schritte wie oben aus, wählen Sie aber stattdessen **Ausgangsregeln**. Erstellen Sie Regeln, um ausgehende Verbindungen für wichtige Dienste und Anwendungen zuzulassen und verdächtige oder unnötige Verbindungen zu blockieren.

4. **Regelmäßig überprüfen und aktualisieren**: Es ist wichtig, Ihre Firewall-Regeln regelmäßig zu überprüfen und zu aktualisieren, um sicherzustellen, dass sie mit den Anforderungen Ihres Systems übereinstimmen. Wenn sich Ihre Netzwerkumgebung und Ihre Nutzungsmuster ändern, müssen Sie möglicherweise Regeln ändern oder neue erstellen. Bleiben Sie wachsam und halten Sie Ihre Regeln auf dem neuesten Stand, um eine effektive Firewall-Konfiguration zu erhalten.

Durch die Implementierung und Pflege von Firewall-Regeln können Sie das Risiko eines unbefugten Netzwerkzugriffs erheblich verringern und die Sicherheit Ihres Windows 10-Systems verbessern. Ziehen Sie außerdem in Erwägung, die Option **Stealth-Modus** in den Firewall-Einstellungen zu aktivieren, um Ihr System für potenzielle Angreifer weniger sichtbar zu machen.

Ausführlichere Informationen zur Konfiguration von Firewall-Regeln in Windows 10 finden Sie in der offiziellen [Microsoft documentation](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/best-practices-configuring) für eine schrittweise Anleitung.

Denken Sie daran, dass eine gut konfigurierte Firewall ein wesentlicher Bestandteil einer umfassenden Sicherheitsstrategie ist, aber sie sollte in Verbindung mit anderen Sicherheitsmaßnahmen eingesetzt werden, um einen zuverlässigen Schutz für Ihr System zu gewährleisten.

#### 8. [**Use AppLocker**](https://github.com/simeononsecurity/AppLocker)
AppLocker ist eine leistungsstarke Funktion in Windows 10, mit der Sie steuern können, welche Anwendungen auf Ihrem System ausgeführt werden können. Durch die Implementierung von AppLocker-Richtlinien können Sie die Ausführung von nicht autorisierten oder potenziell bösartigen Anwendungen einschränken und so die Sicherheit Ihrer Windows 10-Umgebung erhöhen.

Folgen Sie diesen Schritten, um AppLocker auf Ihrem Windows 10-System zu verwenden:

1. **Zugriff auf AppLocker-Einstellungen**: Um auf die AppLocker-Einstellungen zuzugreifen, öffnen Sie den **Editor für lokale Gruppenrichtlinien**, indem Sie **Windows-Taste + R** drücken, **gpedit.msc** eingeben und auf **OK** klicken. Alternativ können Sie auch im Menü **Start** nach **Gruppenrichtlinien-Editor** suchen.

2. **AppLocker-Richtlinien konfigurieren**: Navigieren Sie im Editor für lokale Gruppenrichtlinien zu **Computerkonfiguration > Windows-Einstellungen > Sicherheitseinstellungen > Anwendungssteuerungsrichtlinien > AppLocker**. Hier können Sie verschiedene Richtlinien konfigurieren, z. B. **Regeln für ausführbare Dateien**, **Regeln für Windows Installer**, **Regeln für Skripte** und **Regeln für verpackte Anwendungen**.

3. **Erstellen von AppLocker-Regeln**: Um eine AppLocker-Regel zu erstellen, klicken Sie mit der rechten Maustaste auf den gewünschten Richtlinienordner (z. B. **Ausführbare Regeln**) und wählen Sie **Neue Regel erstellen**. Folgen Sie den Anweisungen auf dem Bildschirm, um die Bedingungen und Ausnahmen für die Regel anzugeben. Sie können Regeln basierend auf Dateipfad, Herausgeber, Datei-Hash oder anderen Attributen erstellen, um die Ausführung von Anwendungen zu erlauben oder zu verweigern.

4. **Testen und Verfeinern der Richtlinien**: Nachdem Sie AppLocker-Regeln erstellt haben, ist es wichtig, diese zu testen, um sicherzustellen, dass sie wie vorgesehen funktionieren. Setzen Sie die Richtlinien in einer Testgruppe oder einem Testsystem ein und überprüfen Sie, ob nur autorisierte Anwendungen ausgeführt werden dürfen. Nehmen Sie auf der Grundlage der Testergebnisse die erforderlichen Anpassungen an den Regeln vor.

5. **Regelmäßige Überprüfung und Aktualisierung**: Da sich Ihre Anwendungslandschaft weiterentwickelt, ist es wichtig, dass Sie Ihre AppLocker-Richtlinien regelmäßig überprüfen und aktualisieren. Neue Anwendungen benötigen möglicherweise eine Genehmigung zur Ausführung, während andere veraltet sind oder ein Sicherheitsrisiko darstellen. Bleiben Sie proaktiv und halten Sie Ihre Richtlinien auf dem neuesten Stand, um einen effektiven Anwendungskontrollmechanismus zu erhalten.

AppLocker bietet eine granulare Kontrolle über die Ausführung von Anwendungen und hilft Ihnen dabei, die Ausführung nicht autorisierter oder bösartiger Software auf Ihrem Windows 10-System zu verhindern. Durch die Verwendung von AppLocker können Sie das Risiko von Malware-Infektionen, nicht autorisierten Software-Installationen und anderen Sicherheitsvorfällen verringern.

Ausführlichere Informationen zur Implementierung von AppLocker-Richtlinien finden Sie in der offiziellen [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-overview) or visit our [AppLocker GitHub repository](https://github.com/simeononsecurity/AppLocker) für zusätzliche Ressourcen und Beispiele.

Denken Sie daran, Ihre AppLocker-Richtlinien regelmäßig zu überprüfen und zu aktualisieren, um sie an sich ändernde Anwendungsanforderungen und neue Sicherheitsbedrohungen anzupassen. AppLocker ist ein wertvolles Werkzeug für Ihre Verteidigung gegen nicht autorisierte und potenziell schädliche Anwendungen auf Ihrem Windows 10-System.

#### 9. [**Regularly Backup Your Data**](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/)
Regelmäßige Datensicherungen sind eine wichtige Maßnahme zum Schutz vor Datenverlusten aufgrund von Sicherheitsvorfällen, Hardwareausfällen oder anderen unerwarteten Ereignissen. Durch die Erstellung regelmäßiger Backups und die Überprüfung ihrer Integrität können Sie sicherstellen, dass Ihre wichtigen Daten sicher bleiben und im Falle einer Katastrophe wiederhergestellt werden können.

Befolgen Sie diese Schritte, um Ihre Daten auf einem Windows 10-System regelmäßig zu sichern:

1. **Identifizieren Sie kritische Daten**: Beginnen Sie damit, die Daten zu identifizieren, die kritisch sind und gesichert werden müssen. Dazu können wichtige Dokumente, persönliche Dateien, Systemkonfigurationen, Anwendungseinstellungen und alle anderen Daten gehören, die Sie für wertvoll halten.

2. **Wählen Sie eine Sicherungslösung**: Wählen Sie eine zuverlässige Sicherungslösung, die Ihren Anforderungen entspricht. Windows 10 bietet integrierte Sicherungstools wie **Dateiverlauf** und **Windows Sichern und Wiederherstellen**. Alternativ können Sie sich auch für eine Sicherungssoftware eines Drittanbieters entscheiden, die zusätzliche Funktionen und Flexibilität bietet.

3. **Die Häufigkeit der Sicherung festlegen**: Legen Sie fest, wie häufig Sie Sicherungen durchführen möchten, je nachdem, wie kritisch Ihre Daten sind und wie häufig sie geändert werden. Einige Daten müssen möglicherweise täglich gesichert werden, während andere wöchentlich oder monatlich gesichert werden können.

4. **Sicherungsspeicher auswählen**: Wählen Sie ein geeignetes Speichermedium zum Speichern Ihrer Backups. Dazu können externe Festplatten, NAS-Geräte (Network-Attached Storage), Cloud-Speicherdienste oder eine Kombination aus mehreren Speicheroptionen gehören. Achten Sie darauf, dass das Speichermedium sicher und zuverlässig ist.

5. **Konfigurieren Sie die Sicherungseinstellungen**: Richten Sie die Sicherungslösung nach Ihren Wünschen ein. Geben Sie die zu sichernden Daten, das Sicherungsziel und zusätzliche Einstellungen wie Verschlüsselung oder Komprimierung an.

6. **Testwiederherstellungen durchführen**: Testen Sie regelmäßig den Wiederherstellungsprozess, indem Sie Testwiederherstellungen aus Ihren Backups durchführen. So stellen Sie sicher, dass Ihre Backups korrekt funktionieren und Sie Ihre Daten bei Bedarf erfolgreich wiederherstellen können.

7. **Überwachen und aktualisieren**: Überwachen Sie den Sicherungsprozess regelmäßig, um sicherzustellen, dass er wie erwartet abläuft. Aktualisieren Sie Ihre Backup-Lösung und passen Sie die Backup-Einstellungen an, wenn sich Ihre Daten und Anforderungen ändern.

Wenn Sie diese Schritte befolgen und sich an eine regelmäßige Backup-Routine halten, können Sie die Auswirkungen von Datenverlusten minimieren und die Verfügbarkeit Ihrer wichtigen Informationen aufrechterhalten. Denken Sie daran, Ihre Backups sicher und getrennt von den Originaldaten aufzubewahren, und ziehen Sie die **3-2-1-Backup-Regel** in Betracht, d. h. mindestens drei Kopien Ihrer Daten auf zwei verschiedenen Speichermedien und eine Kopie außerhalb des Unternehmens.

Ausführlichere Informationen über bewährte Verfahren zur Datensicherung und die **3-2-1-Backup-Regel** finden Sie in dem Artikel auf [What is the 3-2-1 Backup Rule and Why You Should Use It](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) Er bietet wertvolle Einblicke und Empfehlungen für die Umsetzung einer effektiven Sicherungsstrategie.

Denken Sie daran, dass regelmäßige Backups entscheidend sind, um Ihre Daten zu schützen und ihre Verfügbarkeit im Falle unvorhergesehener Ereignisse zu gewährleisten. Machen Sie die Datensicherung zu einem festen Bestandteil Ihrer Windows 10-Härtungsmaßnahmen, um Ihre wertvollen Informationen zu schützen.

______


### [Hardening Windows 11](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 11 ist die neueste Version des Windows-Betriebssystems und bietet erweiterte Funktionen und verbesserte Sicherheit. Um Ihre Windows 11-Umgebung abzusichern, sollten Sie die folgenden Best Practices beachten:

#### 1. **Secure Boot und TPM**
Secure Boot und TPM (Trusted Platform Module) sind wichtige Sicherheitsfunktionen in Windows 11, die zum Schutz vor unbefugtem Zugriff beitragen und die Integrität des Betriebssystems gewährleisten. Durch die Aktivierung von Secure Boot und TPM können Sie die Sicherheit Ihres Windows 11-Systems erhöhen.

Führen Sie die folgenden Schritte aus, um Secure Boot und TPM auf Ihrem Windows 11-Gerät zu aktivieren:

1. **Kompatibilität prüfen**: Bevor Sie Secure Boot und TPM aktivieren, stellen Sie sicher, dass Ihr Gerät diese Funktionen unterstützt. Vergewissern Sie sich, dass die Hardware und Firmware Ihres Systems die Anforderungen für die Secure Boot- und TPM-Funktionalität erfüllen.

2. **Zugriff auf UEFI/BIOS-Einstellungen**: Starten Sie Ihr Windows 11-Gerät neu und greifen Sie auf die UEFI- (Unified Extensible Firmware Interface) oder BIOS- (Basic Input/Output System) Einstellungen zu. Die spezifische Taste oder Tastenkombination für den Zugriff auf diese Einstellungen kann je nach Gerät variieren. Übliche Tasten sind Entf, F2, F10 oder Esc. Detaillierte Anweisungen finden Sie in der Dokumentation zu Ihrem Gerät oder auf der Website des Herstellers.

3. **Secure Boot aktivieren**: Navigieren Sie in den UEFI/BIOS-Einstellungen zu den Secure Boot-Einstellungen. Aktivieren Sie Secure Boot, um sicherzustellen, dass nur vertrauenswürdige Betriebssysteme und Komponenten während des Bootvorgangs ausgeführt werden können. Dies verhindert das Laden von nicht autorisierter oder bösartiger Software, die die Sicherheit des Systems gefährden könnte.

4. **TPM aktivieren**: Suchen Sie die TPM-Einstellungen im UEFI/BIOS und aktivieren Sie das TPM. TPM ist ein spezieller Mikrochip auf der Hauptplatine des Geräts, der hardwarebasierte Sicherheitsfunktionen bietet. Durch die Aktivierung von TPM kann Windows 11 dessen Fähigkeiten für eine verbesserte Systemsicherheit nutzen.

5. **TPM-Sicherheit konfigurieren**: Nachdem Sie das TPM aktiviert haben, stehen Ihnen möglicherweise weitere Optionen zur Konfiguration der Sicherheitseinstellungen zur Verfügung. Je nach Gerät und Firmware können Sie möglicherweise ein TPM-Kennwort festlegen, TPM-Firmware-Updates aktivieren oder andere damit verbundene Einstellungen anpassen. Prüfen Sie die verfügbaren Optionen und konfigurieren Sie sie entsprechend Ihren Sicherheitsanforderungen.

6. **Speichern und Beenden**: Sobald Sie Secure Boot und TPM aktiviert und alle erforderlichen Konfigurationen vorgenommen haben, speichern Sie die Änderungen in den UEFI/BIOS-Einstellungen und beenden Sie das System. Das System wird neu gestartet, und die neuen Einstellungen werden wirksam.

Die Aktivierung von Secure Boot und TPM in Windows 11 trägt dazu bei, Ihr Gerät vor unbefugten Änderungen, Rootkits und anderen Sicherheitsbedrohungen zu schützen. Diese Funktionen schaffen eine Vertrauensbasis für das Betriebssystem und tragen zu einer sichereren Computerumgebung bei.

Beachten Sie, dass die Verfügbarkeit und die spezifischen Schritte zur Aktivierung von Secure Boot und TPM je nach Hersteller und Firmware-Version Ihres Geräts variieren können. Es wird empfohlen, die Dokumentation Ihres Geräts oder die Website des Herstellers zu konsultieren, um genaue, auf Ihr System zugeschnittene Anweisungen zu erhalten.

Durch die Aktivierung von Secure Boot und TPM auf Ihrem Windows 11-Gerät verbessern Sie die allgemeine Sicherheitslage und stärken den Schutz Ihres Betriebssystems und sensibler Daten.

#### 2. [**Enable Microsoft Defender Antivirus**](https://github.com/simeononsecurity/Windows-Defender-Hardening)
Windows 11 verfügt über einen integrierten Virenschutz namens **Microsoft Defender Antivirus**. Er bietet umfassenden Schutz vor verschiedenen Arten von **Malware**, einschließlich Viren, Ransomware und Spyware. Durch **Aktivierung** und **regelmäßige Updates** von Microsoft Defender Antivirus können Sie eine **Echtzeit-Bedrohungserkennung und -abwehr** auf Ihrem Windows 11-System sicherstellen.

Folgen Sie diesen Schritten, um Microsoft Defender Antivirus auf Ihrem Windows 11-Gerät zu aktivieren und zu aktualisieren:

1. **Status von Antivirus prüfen**: Überprüfen Sie zunächst den Status von Microsoft Defender Antivirus auf Ihrem System. Öffnen Sie die App **Windows Security**, indem Sie auf das Startmenü klicken, nach "Windows Security" suchen und die App aus den Suchergebnissen auswählen. Sobald die App geöffnet ist, navigieren Sie zum Abschnitt **Viren- und Bedrohungsschutz "**, um den Status von Microsoft Defender Antivirus zu überprüfen. Er sollte bei einer Neuinstallation von Windows 11 standardmäßig **aktiviert** sein.

2. **Echtzeitschutz aktivieren**: Stellen Sie in der Windows-Sicherheits-App sicher, dass der **Echtzeitschutz** für Microsoft Defender Antivirus aktiviert ist. Der Echtzeitschutz überwacht Ihr System kontinuierlich auf Malware und andere bösartige Aktivitäten, reagiert **sofort** und **blockiert Bedrohungen** in Echtzeit. Wenn der Echtzeitschutz nicht aktiviert ist, klicken Sie auf den **Kippschalter**, um ihn zu aktivieren.

3. **Definitionen aktualisieren**: Die regelmäßige Aktualisierung der **Virendefinitionen** ist wichtig, um sicherzustellen, dass Microsoft Defender Antivirus die neuesten Bedrohungen erkennen und davor schützen kann. Navigieren Sie in der Windows-Sicherheits-App zum Abschnitt **Viren- und Bedrohungsschutz "**, und klicken Sie auf die Schaltfläche **Nach Updates suchen "**, um die Antivirendefinitionen zu aktualisieren. Dieser Vorgang stellt sicher, dass Ihr System mit den **neuesten Signaturen** und **Erkennungsfunktionen** ausgestattet ist.

4. **Planen Sie Scans**: Mit Microsoft Defender Antivirus können Sie regelmäßige **Systemüberprüfungen** planen, um potenzielle Bedrohungen proaktiv zu erkennen und zu entfernen. Gehen Sie in der Windows-Sicherheits-App zum Abschnitt **Viren- und Bedrohungsschutz "** und klicken Sie auf die Option **Schnellüberprüfung "** oder **Vollüberprüfung "**, um eine Überprüfung zu starten. Sie können auch auf den Link **"Scanoptionen "** klicken, um die Scaneinstellungen anzupassen und regelmäßige Scans nach Ihren Wünschen zu planen.

5. **Zusätzliche Einstellungen konfigurieren**: Microsoft Defender Antivirus bietet zusätzliche Einstellungen und Funktionen, die Sie je nach Ihren Sicherheitsanforderungen konfigurieren können. Erkunden Sie in der Windows-Sicherheits-App die verschiedenen Abschnitte wie **"App- und Browserkontrolle", **"Gerätesicherheit" und **"Firewall und Netzwerkschutz "**, um die Antiviren-Einstellungen anzupassen und erweiterte Schutzfunktionen zu nutzen.

Das Aktivieren und regelmäßige Aktualisieren von Microsoft Defender Antivirus in Windows 11 ist für die Aufrechterhaltung einer starken Verteidigung gegen Malware und andere Sicherheitsbedrohungen unerlässlich. Wenn Sie diese Schritte befolgen und Microsoft Defender Antivirus auf dem neuesten Stand halten, können Sie sicherstellen, dass Ihr Windows 11-System gut geschützt ist.

Beachten Sie, dass Microsoft Defender Antivirus zwar einen zuverlässigen Schutz bietet, es jedoch immer empfehlenswert ist, **sichere Surfgewohnheiten** zu praktizieren, beim **Herunterladen von Dateien** oder **Öffnen von E-Mail-Anhängen** Vorsicht walten zu lassen und Ihr **Betriebssystem und Ihre Anwendungen auf dem neuesten Stand zu halten**, um Ihre allgemeine Sicherheitslage weiter zu verbessern.

#### 3. **Standardmäßige Hardware-basierte Isolierung anwenden**
Windows 11 nutzt hardwarebasierte Isolierungsfunktionen wie **Virtualisierungsbasierte Sicherheit (VBS)** und **Hypervisor-geschützte Code-Integrität (HVCI)**, um verbesserte Sicherheit zu bieten und kritische Systemkomponenten zu schützen.

Durch die Aktivierung und Anwendung dieser standardmäßigen hardwarebasierten Isolierungsfunktionen können Sie robuste Sicherheitsgrenzen einrichten und verschiedene Angriffsvektoren entschärfen. Im Folgenden finden Sie einige wichtige Schritte, um die richtige Konfiguration sicherzustellen:

1. **Virtualisierungstechnologie aktivieren**: Zunächst müssen Sie überprüfen, ob Ihr System die Virtualisierungstechnologie unterstützt, und sicherstellen, dass sie in den Einstellungen des **BIOS** oder der **UEFI-Firmware** des Systems aktiviert ist. Die Schritte zum Aufrufen und Aktivieren der Virtualisierungstechnologie können je nach Motherboard- oder Firmware-Hersteller variieren. Konsultieren Sie Ihre Systemdokumentation oder die Website des Herstellers für spezifische Anweisungen.

2. **Aktivieren Sie die virtualisierungsbasierte Sicherheit (VBS)**: Windows 11 enthält VBS, das Hardwarevirtualisierungsfunktionen verwendet, um isolierte Container mit der Bezeichnung **Virtual Secure Mode (VSM)** zu erstellen. VSM bietet eine sichere Ausführungsumgebung für kritische Systemkomponenten und schützt sie vor potenziellen Angriffen. Um VBS zu aktivieren, führen Sie die folgenden Schritte aus:

   - Drücken Sie die **Windows-Taste + R**, um das Dialogfeld Ausführen zu öffnen.
   - Geben Sie "**gpedit.msc**" ein und drücken Sie **Eingabe**, um den Editor für lokale Gruppenrichtlinien zu öffnen.
   - Navigieren Sie zu **Computerkonfiguration -> Administrative Vorlagen -> System -> Device Guard**.
   - Doppelklicken Sie auf die Richtlinie **"Virtualisierungsbasierte Sicherheit einschalten "**.
   - Wählen Sie **"Aktiviert "** und klicken Sie auf **OK**, um die Änderungen zu übernehmen.

   Für die Aktivierung von VBS sind möglicherweise kompatible Hardware und bestimmte Systemanforderungen erforderlich. Weitere Informationen finden Sie in der offiziellen **Microsoft-Dokumentation**.

3. Aktivieren Sie **Hypervisor-geschützte Code-Integrität (HVCI)**: HVCI ist eine Funktion, die den Hypervisor zur Durchsetzung von Code-Integritätsrichtlinien nutzt, um die Ausführung von nicht autorisiertem Code zu verhindern und die allgemeine Sicherheitslage zu verbessern. Um HVCI zu aktivieren, führen Sie die folgenden Schritte aus:

   - Drücken Sie die **Windows-Taste + R**, um das Dialogfeld Ausführen zu öffnen.
   - Geben Sie "**msconfig**" ein und drücken Sie **Eingabe**, um das Dienstprogramm für die Systemkonfiguration zu öffnen.
   - Navigieren Sie zur Registerkarte **"Boot "**.
   - Klicken Sie auf **"Erweiterte Optionen "**.
   - Aktivieren Sie die Option **"Hypervisor-geschützte Code-Integrität aktivieren "**.
   - Klicken Sie auf **OK**, um die Änderungen zu speichern und Ihr System neu zu starten.

   Für die Aktivierung von HVCI sind kompatible Hardware und bestimmte Systemvoraussetzungen erforderlich. Weitere Einzelheiten finden Sie in der offiziellen **Microsoft-Dokumentation**.

Durch die Anwendung von standardmäßigen hardwarebasierten Isolierungsfunktionen, wie VBS und HVCI, können Sie die Sicherheit Ihres Windows 11-Systems erheblich verbessern. Diese Funktionen tragen dazu bei, kritische Systemkomponenten vor verschiedenen Angriffen zu schützen, einschließlich solcher, die versuchen, Systemcode und -konfigurationen zu ändern oder auszunutzen.

Stellen Sie sicher, dass Sie Ihr System regelmäßig mit den neuesten Sicherheitspatches und Firmware-Updates aktualisieren, um von den aktuellsten Sicherheitsverbesserungen und Abhilfemaßnahmen zu profitieren, die diese hardwarebasierten Isolierungsfunktionen bieten.

Beachten Sie, dass die Verfügbarkeit und die Anforderungen der hardwarebasierten Isolierungsfunktionen je nach Systemkonfiguration und Edition von Windows 11 variieren können. Es wird empfohlen, die offizielle **Microsoft-Dokumentation** zu konsultieren und Kompatibilitätsprüfungen durchzuführen, um die ordnungsgemäße Implementierung dieser Sicherheitsfunktionen sicherzustellen.

#### 4. [**Use Windows Sandbox**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)
Die **Windows Sandbox** ist ein wertvolles Tool, mit dem Sie nicht vertrauenswürdige Anwendungen oder Testsoftware in einer isolierten Umgebung ausführen können, was eine zusätzliche Sicherheitsebene für Ihr System darstellt. Durch die Verwendung von Windows Sandbox können Sie potenzielle Risiken, die mit der Ausführung nicht vertrauenswürdiger Programme verbunden sind, minimieren.

Windows Sandbox erstellt eine leichtgewichtige, temporäre Desktop-Umgebung, die vollständig von Ihrem Hauptbetriebssystem getrennt ist. Alle in der Sandbox vorgenommenen Änderungen werden verworfen, sobald Sie die Sandbox schließen, so dass Ihr Hauptsystem davon unberührt bleibt.

Gehen Sie folgendermaßen vor, um Windows Sandbox zu verwenden:

1. **Systemanforderungen prüfen**: Bevor Sie fortfahren, stellen Sie sicher, dass Ihr System die Anforderungen für die Ausführung von Windows Sandbox erfüllt. Im Allgemeinen benötigen Sie eine Windows 10 Pro oder Enterprise Edition und einen Prozessor, bei dem die Virtualisierungsfunktionen in der BIOS/UEFI-Firmware aktiviert sind. Konsultieren Sie die offizielle [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview) für spezifische Systemanforderungen.

2. **Windows Sandbox aktivieren**: Windows Sandbox ist eine integrierte Funktion in den Editionen Windows 10 Pro und Enterprise. Führen Sie die folgenden Schritte aus, um Windows Sandbox zu aktivieren:

   - Drücken Sie die **Windows-Taste + R**, um das Dialogfeld Ausführen zu öffnen.
   - Geben Sie "**appwiz.cpl**" ein und drücken Sie die **Eingabetaste**, um das Fenster "Programme und Funktionen" zu öffnen.
   - Klicken Sie auf der linken Seite auf **"Windows-Funktionen ein- oder ausschalten "**.
   - Führen Sie einen Bildlauf nach unten durch und suchen Sie **"Windows-Sandbox "** in der Liste der Funktionen.
   - Aktivieren Sie das Kontrollkästchen neben **"Windows Sandbox "**, und klicken Sie auf **OK**, um es zu aktivieren.
   - Windows installiert die erforderlichen Komponenten, und Sie müssen Ihr System möglicherweise neu starten, damit die Änderungen wirksam werden.

3. **Starten Sie Windows Sandbox**: Sobald die Windows-Sandbox aktiviert ist, können Sie sie mit den folgenden Schritten starten:

   - Öffnen Sie das Menü **Start** und suchen Sie nach **"Windows Sandbox "**.
   - Klicken Sie auf die Anwendung **"Windows Sandbox "**, um sie zu öffnen.
   - Die Sandbox wird in einem separaten Fenster gestartet und bietet Ihnen eine sichere Umgebung, in der Sie nicht vertrauenswürdige Anwendungen oder Testsoftware ausführen können.

Beachten Sie bei der Ausführung von Anwendungen in der Windows-Sandbox, dass die Sandbox-Umgebung isoliert und so konzipiert ist, dass alle darin vorgenommenen Änderungen verworfen werden. Daher ist es wichtig, dass Sie Ihre Dateien oder Daten außerhalb der Sandbox speichern, wenn Sie sie aufbewahren möchten.

Die Windows-Sandbox ist ein effektives Tool zum Testen unbekannter Software, zum Öffnen verdächtiger Dateien oder zum Erkunden potenziell riskanter Websites. Es sorgt für zusätzlichen Schutz, indem es sicherstellt, dass alle bösartigen Aktivitäten oder unerwünschten Änderungen auf die Sandbox beschränkt bleiben und sich nicht auf das Hauptbetriebssystem auswirken.

Wenn Sie die Windows-Sandbox in Ihre Sicherheitspraktiken einbeziehen, können Sie die Risiken, die mit der Ausführung nicht vertrauenswürdiger Anwendungen verbunden sind, erheblich verringern und Ihr System vor potenziellen Bedrohungen schützen.

Weitere Informationen zur Windows Sandbox und ihrer Verwendung finden Sie in der offiziellen [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)

#### 5. [**Implement Microsoft Defender Application Guard**](https://github.com/simeononsecurity/Windows-Defender-Application-Guard-Hardening)
Microsoft Defender Application Guard ist eine leistungsstarke Sicherheitsfunktion, die Microsoft Edge-Browsersitzungen vom zugrunde liegenden Betriebssystem isoliert. Indem Edge in einer sicheren, isolierten Umgebung ausgeführt wird, hilft Application Guard, Ihr System vor browserbasierten Angriffen und bösartigen Websites zu schützen.

Führen Sie die folgenden Schritte aus, um Microsoft Defender Application Guard zu implementieren und Ihre Browsersicherheit zu verbessern:

1. **Kompatibilität prüfen**: Bevor Sie fortfahren, stellen Sie sicher, dass Ihr System die Anforderungen für die Ausführung von Microsoft Defender Application Guard erfüllt. In der Regel benötigen Sie ein Windows 10 Pro oder Enterprise Edition, einen kompatiblen Prozessor mit Virtualisierungsfunktionen und mindestens 8 GB RAM. Siehe die offizielle [**Microsoft documentation**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard) für spezifische Systemanforderungen.

2. **Aktivieren Sie Application Guard**: Application Guard ist als optionale Funktion in Windows 10 verfügbar. Gehen Sie folgendermaßen vor, um den Microsoft Defender Application Guard zu aktivieren:

   - Drücken Sie die **Windows-Taste + R**, um das Dialogfeld Ausführen zu öffnen.
   - Geben Sie "**appwiz.cpl**" ein und drücken Sie die **Eingabetaste**, um das Fenster Programme und Funktionen zu öffnen.
   - Klicken Sie auf der linken Seite auf **"Windows-Funktionen ein- oder ausschalten "**.
   - Führen Sie einen Bildlauf nach unten durch, und suchen Sie **"Microsoft Defender Application Guard "** in der Funktionsliste.
   - Aktivieren Sie das Kontrollkästchen neben **"Microsoft Defender Application Guard "**, und klicken Sie auf **OK**, um es zu aktivieren.
   - Windows installiert die erforderlichen Komponenten, und Sie müssen Ihr System möglicherweise neu starten, damit die Änderungen wirksam werden.

3. **Anwendungswächter konfigurieren**: Sobald Application Guard aktiviert ist, können Sie seine Einstellungen entsprechend Ihren Sicherheitsanforderungen konfigurieren. Mit Application Guard können Sie den Grad der Isolierung festlegen und kontrollieren, wie er mit nicht vertrauenswürdigen Websites und Dateien umgeht. Sie können diese Einstellungen über die App **Windows Sicherheit** oder die Gruppenrichtlinieneinstellungen anpassen.

4. **Testen und Prüfen**: Nachdem Sie Microsoft Defender Application Guard aktiviert und konfiguriert haben, ist es wichtig, seine Funktionalität zu testen und zu überprüfen. Öffnen Sie Microsoft Edge und besuchen Sie eine bekannte bösartige Website oder eine Website mit potenziellen Risiken, um zu prüfen, ob Application Guard die Browsersitzung erfolgreich isoliert und potenzielle Angriffe verhindert.

Durch die Implementierung von Microsoft Defender Application Guard fügen Sie Ihrem System eine zusätzliche Schutzebene hinzu, indem Sie die Browsersitzungen isolieren und alle potenziellen Bedrohungen innerhalb der sicheren Umgebung eindämmen. Dies trägt dazu bei, Ihr System und Ihre Daten vor browserbasierten Angriffen wie Drive-by-Downloads, bösartigen Skripten und Zero-Day-Exploits zu schützen.

Ausführlichere Informationen zur Konfiguration und Verwendung von Microsoft Defender Application Guard finden Sie in der offiziellen [**Microsoft documentation**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard)

#### 6. [**Controlled Folder Access**](https://github.com/simeononsecurity/Windows-Defender-Hardening)
Gesteuerter Ordnerzugriff ist eine leistungsstarke Sicherheitsfunktion in Windows 11, die wichtige Ordner vor unbefugten Änderungen durch Ransomware und andere bösartige Software schützen kann. Durch die Aktivierung des kontrollierten Ordnerzugriffs und das Hinzufügen notwendiger Ordner zur geschützten Liste können Sie die Sicherheit Ihres Systems erhöhen und einen möglichen Datenverlust verhindern.

Gehen Sie folgendermaßen vor, um den kontrollierten Ordnerzugriff zu implementieren und Ihre wichtigen Ordner zu schützen:

1. **Öffnen Sie Windows-Sicherheit**: Drücken Sie die **Windows-Taste** auf Ihrer Tastatur, geben Sie "**Windows Security**" ein, und wählen Sie die App **Windows Security** aus den Suchergebnissen aus.

2. **Navigieren Sie zu Einstellungen für Viren- und Bedrohungsschutz**: Klicken Sie in der Windows-Sicherheitsanwendung im linken Menü auf die Registerkarte **"Schutz vor Viren und Bedrohungen "**.

3. **Konfigurieren Sie den kontrollierten Ordnerzugriff**: Klicken Sie unter dem Abschnitt **"Ransomware-Schutz "** auf **"Ransomware-Schutz verwalten "**, um auf die Einstellungen für den kontrollierten Ordnerzugriff zuzugreifen.

4. **Aktivieren Sie den kontrollierten Ordnerzugriff**: Schalten Sie in den Einstellungen für den kontrollierten Ordnerzugriff den Schalter auf **"Ein "**, um die Funktion zu aktivieren. Windows zeigt eine Warnung an, dass nur vertrauenswürdige Anwendungen auf geschützte Ordner zugreifen dürfen.

5. **Geschützte Ordner hinzufügen**: Um festzulegen, welche Ordner geschützt werden sollen, klicken Sie auf **"Geschützte Ordner "** und wählen Sie dann **"Einen geschützten Ordner hinzufügen "**. Wählen Sie die Ordner aus, die Sie schützen möchten, und klicken Sie auf **"OK "**.

   - Es wird empfohlen, wichtige Ordner wie Dokumente, Bilder, Videos und alle anderen Verzeichnisse mit wertvollen Daten hinzuzufügen.

6. **Anwendungen zulassen oder blockieren**: Standardmäßig erlaubt Controlled Folder Access vertrauenswürdigen Anwendungen den Zugriff auf geschützte Ordner. Sie können dieses Verhalten jedoch anpassen, indem Sie auf **"Eine Anwendung durch kontrollierten Ordnerzugriff zulassen "** klicken. Von dort aus können Sie den Zugriff auf geschützte Ordner für bestimmte Anwendungen entweder zulassen oder blockieren.

7. **Überwachen und Überprüfen**: Nachdem Sie den kontrollierten Ordnerzugriff aktiviert haben, überwacht und protokolliert Windows kontinuierlich alle Versuche von nicht autorisierten Anwendungen, auf geschützte Ordner zuzugreifen. Sie können diese Protokolle überprüfen, indem Sie in den Einstellungen für den kontrollierten Ordnerzugriff im Abschnitt **"Zuletzt blockierte Anwendungen "** auf **"Überprüfen "** klicken.

Durch die Implementierung des kontrollierten Ordnerzugriffs fügen Sie Ihren wichtigen Ordnern eine zusätzliche Schutzebene hinzu, die das Risiko unbefugter Änderungen und möglicher Datenverluste durch Ransomware-Angriffe mindert. Überprüfen Sie regelmäßig die Einstellungen für den kontrollierten Ordnerzugriff, um sicherzustellen, dass die geschützten Ordner Ihren Sicherheitsanforderungen entsprechen.

Ausführlichere Informationen zur Konfiguration und Verwendung von Controlled Folder Access finden Sie in der offiziellen [**Microsoft documentation**](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/controlled-folders?view=o365-worldwide)


#### 7. **Automatische Windows-Wartung aktivieren**
Windows 11 enthält eine praktische Funktion namens Automatische Wartung, die dazu beiträgt, Ihr System durch die Durchführung regelmäßiger Wartungsaufgaben zu optimieren und zu schützen. Durch die Aktivierung der automatischen Wartung stellen Sie sicher, dass Ihr System reibungslos funktioniert und sicher bleibt.

Gehen Sie folgendermaßen vor, um die automatische Wartung von Windows zu aktivieren:

1. **Öffnen Sie die Windows-Einstellungen**: Drücken Sie die **Windows-Taste** auf Ihrer Tastatur, geben Sie "**Einstellungen**" ein, und wählen Sie die App **Einstellungen** aus den Suchergebnissen aus.

2. **Zugriff auf die Wartungseinstellungen**: Klicken Sie in der App **Einstellungen** auf die Kategorie **System** und wählen Sie dann **Über** aus dem linken Menü. Scrollen Sie zum unteren Ende der Seite und klicken Sie auf den Link **"Systeminfo "**.

3. **Öffnen Sie die Wartungseinstellungen**: Klicken Sie im Fenster "Systeminformationen" auf den Link **"Wartung "**, der sich unten auf der Seite befindet.

4. **Automatische Wartung aktivieren**: Schalten Sie in den Wartungseinstellungen den Schalter neben **"Automatische Wartung "** in die Position **"Ein "**.

5. **Wartungseinstellungen konfigurieren**: Standardmäßig plant Windows Wartungsaufgaben automatisch so, dass sie täglich um 2:00 Uhr morgens ausgeführt werden. Wenn Sie einen anderen Zeitplan bevorzugen, klicken Sie auf **"Wartungseinstellungen ändern "** und passen Sie die gewünschten Optionen an, z. B. die Startzeit der Wartung und die Häufigkeit der Wartungsaufgaben.

6. **Zusätzliche Einstellungen überprüfen**: Unterhalb des Kippschalters für die automatische Wartung finden Sie weitere Einstellungen für die Wartung, z. B. **"Geplante Wartung zum Aufwachen des Computers zur geplanten Zeit zulassen "** und **"Geplante Wartung auch im Akkubetrieb zulassen "**. Passen Sie diese Einstellungen entsprechend Ihren Vorlieben und Anforderungen an.

7. **Wartungsaktivitäten überwachen**: Sobald die automatische Wartung aktiviert ist, führt Windows zur geplanten Zeit automatisch Wartungsaufgaben im Hintergrund aus. Sie können diese Aktivitäten überwachen, indem Sie den Abschnitt **"Wartung "** in der App **"Windows-Sicherheit "** überprüfen oder die **"Wartung "**-Protokolle in der Ereignisanzeige ansehen.

Durch die Aktivierung der automatischen Windows-Wartung wird sichergestellt, dass Ihr System optimiert und geschützt bleibt, indem regelmäßig wichtige Wartungsaufgaben wie Software-Updates, Festplattenoptimierung und Sicherheitsüberprüfungen durchgeführt werden. Indem Sie Ihr System in einem guten Zustand halten, können Sie eine reibungslosere und sicherere Computererfahrung genießen.

Ausführlichere Informationen über die automatische Windows-Wartung und ihre Konfigurationsoptionen finden Sie in der offiziellen [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-maintenence)

______

## Schlussfolgerung

Die Umsetzung dieser **Best Practices für die Windows-Härtung** ist für die Sicherheit Ihrer Windows-Systeme unerlässlich. Durch regelmäßige **Aktualisierungen Ihres Betriebssystems** können Sie Sicherheitslücken schließen und die Systemstabilität verbessern. Die Aktivierung von Sicherheitsfunktionen wie **Virenschutz** und **Verschlüsselung** bietet eine zusätzliche Schutzschicht für Ihre Daten. Die Konfiguration geeigneter **Zugangskontrollen** hilft, unbefugte Änderungen zu verhindern und den Zugriff auf sensible Ressourcen einzuschränken.

Durch die Einhaltung dieser bewährten Verfahren können Sie die Sicherheit Ihrer **Windows-Umgebung** verbessern, Ihre Daten schützen und die Integrität Ihrer **digitalen Infrastruktur** aufrechterhalten. Es ist wichtig, **proaktiv** zu bleiben und Ihre Sicherheitsmaßnahmen regelmäßig zu überprüfen und zu aktualisieren, um potenziellen Bedrohungen einen Schritt voraus zu sein.

Denken Sie daran, dass die **Windows-Härtung** ein fortlaufender Prozess ist, und dass es wichtig ist, über die neuesten Sicherheitsupdates und -praktiken informiert zu bleiben. Indem Sie proaktiv bleiben und diese bewährten Verfahren anwenden, können Sie Sicherheitsrisiken wirksam eindämmen und die Sicherheit Ihrer Windows-Systeme gewährleisten.

Weitere Informationen zur Windows-Härtung und zu bewährten Verfahren finden Sie in seriösen Quellen wie der **Microsoft-Dokumentation**, **Sicherheitsforen** und vertrauenswürdigen **Cybersecurity-Websites**.

______

## Referenzen:

- [Microsoft Windows Security](https://www.microsoft.com/en-us/security)
- [NIST Special Publication 800-171: Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final)
- [CIS Microsoft Windows 10 Benchmark](https://www.cisecurity.org/benchmark/microsoft_windows_10/)
- [CIS Microsoft Windows 11 Benchmark](https://www.cisecurity.org/benchmark/microsoft_windows_11/)
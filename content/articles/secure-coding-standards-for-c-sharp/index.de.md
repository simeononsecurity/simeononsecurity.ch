---
title: "Sichere Coding-Standards für C#-Entwickler"
date: 2023-02-28
toc: true
draft: false
description: "Lernen Sie Best Practices für die sichere Programmierung in C#, um das Risiko von Sicherheitsverletzungen zu minimieren und sensible Daten zu schützen."
tags: ["Sichere Kodierung", "C sharp Entwicklung", "C Sharp Programmierung", "sichere Kodierungspraktiken", "C Scharfe Sicherheit", "ASP.NET-Sicherheit", ".NET Core Sicherheit", "Eingabeüberprüfung", "Passwort-Hashing", "Kryptographie", "geringstes Privileg", "statischer Code-Analysator", "Sicherheit von Webanwendungen", "SQL-Injection-Verhinderung", "Cross-Site-Scripting-Verhinderung", "datenschutz", "Gesundheitskontrollen", "Sitzungsmanagement", "OWASP-Best-Practices", "C Sharp Standards für sichere Kodierung", "C Scharfe Sicherheitsrichtlinien", "Tipps zur sicheren Kodierung", "sichere Softwareentwicklung", "Frameworks für sichere Kodierung", "sichere Kodierungstechniken", "Empfehlungen zur sicheren Kodierung", "Sichere Programmierung in C Sharp", "Schwachstellen der sicheren Kodierung", "sichere Kodierungstools", "Tutorials zur sicheren Kodierung", "Bewährte Verfahren für die sichere Programmierung in C Sharp", "C Sharp-Leitlinien für sichere Kodierung", "Sichere Kodierungsstandards für C Sharp Entwickler", "C Scharfe sichere Kodierungspraktiken", "Wie man sichere Kodierung in C Sharp implementiert", "Tipps zur sicheren Kodierung für C Sharp-Programmierer", "Sichere Kodierung in C Sharp Webanwendungen", "C Sharp-Frameworks für sichere Kodierung", "Sichere Kodierungstechniken für C Sharp-Entwickler", "C Sharp Werkzeuge zur sicheren Codierung"]
cover: "/img/cover/A_cartoon_developer_with_a_lock_icon_as_the_head_surrounded.png"
coverAlt: " Ein Cartoon-Entwickler mit einem Schloss-Symbol als Kopf, umgeben von Code und abgeschirmt durch eine Firewall."
coverCaption: ""
---

Sichere Kodierung ist wichtig, um sicherzustellen, dass der Code sicher, zuverlässig und frei von Schwachstellen ist. C Sharp ist eine beliebte Programmiersprache, die von den Entwicklern die Einhaltung von Standards für die sichere Programmierung verlangt, um Sicherheitsrisiken zu vermeiden. Durch die Einhaltung von Best Practices wie der Eingabevalidierung, der Vermeidung unsicherer Funktionen, der Verwendung von Kryptographie-Bibliotheken und der Aktualisierung von Bibliotheken und Frameworks können Entwickler sicherstellen, dass ihr Code sicher und frei von Sicherheitslücken ist.

_____

## Eingabeüberprüfung

Benutzereingaben sind oft eine bedeutende Quelle von Sicherheitsrisiken. Bei der Eingabevalidierung wird überprüft, ob die Benutzereingabe den erwarteten Kriterien entspricht und in der Anwendung sicher verwendet werden kann. Wenn ein Benutzer zum Beispiel eine Kreditkartennummer eingibt, sollte die Eingabe nur Ziffern und keine Sonderzeichen enthalten. Um die Eingabe zu überprüfen, können Entwickler integrierte Klassen verwenden, wie z.B. `Regex` um sicherzustellen, dass die Eingabe die erwarteten Kriterien erfüllt.

```csharp
public static bool ValidateInput(string inputString)
{
    bool isValid = false;
    // Check if input string contains only digits
    if (Regex.IsMatch(inputString, @"^\d+$"))
    {
        isValid = true;
    }
    return isValid;
}
```

Diese Methode verwendet reguläre Ausdrücke, um zu prüfen, ob die Eingabezeichenfolge nur Ziffern enthält. Sie gibt einen booleschen Wert zurück, der angibt, ob die Eingabe gültig ist oder nicht.

## Vermeiden Sie die Verwendung unsicherer Funktionen
C Sharp verfügt über mehrere Funktionen, die bei unsachgemäßer Verwendung anfällig für Sicherheitsprobleme sein können. Funktionen wie `Process.Start()` `Reflection` und `Deserialization` können es Angreifern ermöglichen, bösartigen Code auszuführen. Entwickler sollten die Verwendung dieser Funktionen vermeiden oder sie mit Vorsicht einsetzen, indem sie die Eingabeparameter einschränken und sie nur bei Bedarf verwenden.

Zum Beispiel, statt der Verwendung von `Process.Start()` Funktion zum Starten eines externen Prozesses verwenden, sollten Entwickler `Process.StartInfo` Eigenschaft, um Argumente und Sicherheitseinschränkungen zu liefern.
```csharp
ProcessStartInfo startInfo = new ProcessStartInfo
{
    FileName = "notepad.exe",
    Arguments = "example.txt",
    UseShellExecute = false,
    RedirectStandardOutput = true,
    CreateNoWindow = true
};

using (Process process = new Process())
{
    process.StartInfo = startInfo;
    process.Start();
    string output = process.StandardOutput.ReadToEnd();
    process.WaitForExit();
}
```
## Kryptographie-Bibliotheken verwenden
Kryptographie-Bibliotheken wie Bouncy Castle und die Kryptographie-APIs von .NET Framework bieten eine sichere Möglichkeit zur Durchführung von Ver- und Entschlüsselungsvorgängen. Verwenden Sie diese Bibliotheken, anstatt eigene Verschlüsselungsmethoden zu erstellen, die anfällig für Schwachstellen sein können.

Um zum Beispiel ein Passwort zu verschlüsseln, verwenden Sie die `Rfc2898DeriveBytes` Klasse aus den Kryptographie-APIs von .NET Framework wie folgt:
```csharp
public static string EncryptPassword(string password)
{
    byte[] salt = new byte[16];
    using (var rng = new RNGCryptoServiceProvider())
    {
        rng.GetBytes(salt);
    }

    var pbkdf2 = new Rfc2898DeriveBytes(password, salt, 10000);
    byte[] hash = pbkdf2.GetBytes(20);

    byte[] hashBytes = new byte[36];
    Array.Copy(salt, 0, hashBytes, 0, 16);
    Array.Copy(hash, 0, hashBytes, 16, 20);

    return Convert.ToBase64String(hashBytes);
}
```
Die `Rfc2898DeriveBytes` generiert einen Salt und leitet daraus einen Schlüssel für das Kennwort ab. Der resultierende Schlüssel wird dann zur Verschlüsselung des Kennworts verwendet.

## Befolgen Sie das Prinzip des geringsten Privilegs

Das Prinzip der geringsten Privilegien ist eine bewährte Sicherheitspraxis, die Benutzer oder Prozesse auf die minimale Zugriffsebene beschränkt, die zur Ausführung ihrer Funktionen erforderlich ist. Entwickler sollten dieses Prinzip beim Schreiben von Code befolgen, um die Auswirkungen von Sicherheitsverletzungen zu minimieren.

Wenn eine Anwendung beispielsweise nur Lesezugriff auf eine Datenbank benötigt, sollte sie ein Datenbankkonto mit Nur-Lese-Zugriffsrechten anstelle eines Kontos mit vollen Rechten verwenden. Dies verringert das Risiko, dass ein Angreifer die Anwendung ausnutzt, um Daten zu ändern oder zu löschen.

## Bibliotheken und Frameworks auf dem neuesten Stand halten

Bibliotheken und Frameworks können Sicherheitslücken enthalten, die von Angreifern ausgenutzt werden können. Entwickler sollten ihre Bibliotheken und Frameworks stets auf dem neuesten Stand halten, um potenzielle Sicherheitsprobleme zu vermeiden.

Wenn die Anwendung beispielsweise eine Bibliothek eines Drittanbieters verwendet, wie z. B. `Newtonsoft.Json` die eine Sicherheitslücke aufweist, sollte der Entwickler auf die neueste Version der Bibliothek aktualisieren, die die Sicherheitslücke behebt.

## Verwenden Sie einen statischen Code-Analyzer

Ein statischer Code-Analysator ist ein Tool, das potenzielle Sicherheitslücken im Code aufspüren kann, bevor dieser ausgeführt wird. Verwenden Sie Tools wie den Code von Visual Studio `Analysis` `ReSharper` und `SonarQube` um Sicherheitsprobleme im Code zu erkennen und sie vor der Bereitstellung zu beheben.

Die Code-Analyse von Visual Studio ist beispielsweise ein beliebter statischer Code-Analyzer, der C-Sharp-Code auf potenzielle Sicherheitslücken untersucht. Es kann Probleme wie SQL-Injection, Cross-Site-Scripting und die Verwendung unsicherer Funktionen erkennen.

## Sichere Coding-Praktiken für Webanwendungen verwenden

Webanwendungen sind anfällig für verschiedene Sicherheitsrisiken wie Cross-Site-Scripting, SQL-Injection und Command-Injection. Um die Sicherheit von Webanwendungen zu gewährleisten, sollten Entwickler sichere Kodierungspraktiken wie Eingabevalidierung, Ausgabeverschlüsselung und parametrisierte Abfragen anwenden.

Wenn Sie beispielsweise SQL-Abfragen schreiben, sollten Sie parametrisierte Abfragen verwenden, anstatt Benutzereingaben mit der Abfrage zu verketten. Parametrisierte Abfragen verhindern SQL-Injection-Angriffe, da sie Benutzereingaben als Daten und nicht als ausführbaren Code behandeln.

```csharp
string query = "SELECT * FROM Users WHERE Username = @Username";
using (SqlConnection connection = new SqlConnection(connectionString))
{
    using (SqlCommand command = new SqlCommand(query, connection))
    {
        command.Parameters.AddWithValue("@Username", username);
        connection.Open();
        SqlDataReader reader = command.ExecuteReader();
        // process the data
    }
}
```

Entwickler sollten außerdem alle Benutzereingaben validieren, Ausgaben verschlüsseln und HTTPS zur Verschlüsselung der über das Netzwerk übertragenen Daten verwenden.

_____

## Sichere Codierungsstandards für C Sharp Frameworks

C Sharp-Frameworks wie ASP.NET und .NET Core haben ihre eigenen Standards für sichere Kodierung. Entwickler sollten diese Standards bei der Entwicklung von Anwendungen mit diesen Frameworks befolgen.

### ASP.NET
ASP.NET ist ein beliebtes Web-Framework für C Sharp. Hier sind einige sichere Codierungsstandards für ASP.NET:

- Verwenden Sie das in ASP.NET eingebaute Authentifizierungssystem, anstatt ein benutzerdefiniertes Authentifizierungssystem zu erstellen. Zum Beispiel können Sie ASP.NETs `Identity` System zur Verwaltung der Benutzerauthentifizierung und -autorisierung.
- Verwenden Sie die in ASP.NET integrierten Passwort-Hashing-Funktionen, anstatt eigene Passwort-Hashing-Methoden zu erstellen. Sie können zum Beispiel die ASP.NET-Funktionen `PasswordHasher` Klasse, um Passwörter sicher zu hashen und zu verifizieren.
- Verwenden Sie die in ASP.NET integrierte `AntiForgeryToken` um Cross-Site Request Forgery (CSRF)-Angriffe zu verhindern. Sie können zum Beispiel die `ValidateAntiForgeryToken` Attribut, um Anti-Fälschungs-Token in POST-Anforderungen zu validieren.
- Verwenden Sie die in ASP.NET integrierte `OutputCacheAttribute` um die Zwischenspeicherung von sensiblen Daten zu verhindern. Zum Beispiel können Sie die `OutputCacheAttribute` um Cache-Richtlinien für Ihre Webseiten festzulegen und zu verhindern, dass sensible Daten zwischengespeichert werden.

### .NET Core
.NET Core ist ein plattformübergreifendes Open-Source-Framework für die Entwicklung moderner, Cloud-basierter Anwendungen. Hier finden Sie einige sichere Codierungsstandards für .NET Core:

- Verwenden Sie das integrierte Authentifizierungssystem von .NET Core, anstatt ein benutzerdefiniertes Authentifizierungssystem zu erstellen. Sie können zum Beispiel das Authentifizierungssystem von .NET Core verwenden. `Identity` System zur Verwaltung der Benutzerauthentifizierung und -autorisierung.
- Verwenden Sie die in .NET Core integrierten Passwort-Hashing-Funktionen, anstatt eigene Passwort-Hashing-Methoden zu erstellen. Sie können zum Beispiel die in .NET Core enthaltene `PasswordHasher` Klasse, um Passwörter sicher zu hashen und zu verifizieren.
- Verwenden Sie die integrierte Datenschutz-API von .NET Core, um sensible Daten wie Verbindungszeichenfolgen und Geheimnisse zu schützen. Zum Beispiel können Sie die `DataProtectionProvider` Klasse, um sensible Daten mit einem Schlüssel zu schützen.
- Verwenden Sie die in .NET Core integrierten Health Checks, um den Zustand Ihrer Anwendung zu überwachen. Zum Beispiel können Sie die `HealthCheck` Middleware, um den Zustand Ihrer Anwendung regelmäßig zu überprüfen und Sie auf eventuelle Probleme hinzuweisen.


## Fazit
Sichere Kodierungsstandards sind wichtig, um sicherzustellen, dass der Code sicher, zuverlässig und frei von Schwachstellen ist. C Sharp ist eine beliebte Programmiersprache, die von Entwicklern die Einhaltung von Sicherheitsstandards verlangt, um Sicherheitsrisiken zu vermeiden. Durch die Einhaltung von Best Practices wie Eingabevalidierung, die Vermeidung unsicherer Funktionen, die Verwendung von Kryptographie-Bibliotheken und die Aktualisierung von Bibliotheken und Frameworks können Entwickler sicherstellen, dass ihr Code sicher und frei von Sicherheitslücken ist. Bei der Verwendung von C Sharp-Frameworks sollten Entwickler die vom Framework empfohlenen Standards für sichere Codierung befolgen.

Die Übernahme von Standards für die sichere Programmierung ist ein kontinuierlicher Prozess, der von den Entwicklern verlangt, dass sie sich über die neuesten bewährten Sicherheitsverfahren und -tools auf dem Laufenden halten. Durch die Einbeziehung von Standards für sichere Kodierung in den Entwicklungsprozess können Entwickler das Risiko von Sicherheitsverletzungen minimieren und sensible Daten schützen.

Um mit der sicheren Codierung in C Sharp zu beginnen, können sich Entwickler zunächst mit den in diesem Artikel besprochenen Best Practices vertraut machen. Sie sollten Bereiche in ihrem Code identifizieren, die anfällig für Sicherheitsrisiken sind, wie z. B. Eingabevalidierung, Passwort-Hashing und Sitzungsmanagement. Anschließend können sie bewährte Verfahren wie die in diesem Artikel besprochenen implementieren, um ihren Code zu sichern.

Entwickler sollten sich auch über die neuesten Sicherheitstrends und -praktiken auf dem Laufenden halten, indem sie Sicherheitsblogs verfolgen, an Konferenzen teilnehmen und sich an Online-Communities beteiligen. Indem sie auf dem Laufenden bleiben, können sie ihren Code sicher und frei von Sicherheitslücken halten.

Schließlich sollten Entwickler eine Kultur des Sicherheitsbewusstseins fördern, indem sie bewährte Verfahren mit ihrem Team oder ihren Kollegen teilen. Sie sollten Sicherheitsschulungen organisieren, Artikel und Ressourcen zu sicheren Programmierpraktiken weitergeben und mit gutem Beispiel vorangehen, indem sie diese Best Practices in ihrem eigenen Code umsetzen. Indem sie eine Kultur des Sicherheitsbewusstseins fördern, können sie dazu beitragen, dass der Code ihres Teams sicher und frei von Schwachstellen ist.

Durch die Befolgung dieser Best Practices können Entwickler sicherstellen, dass ihr C Sharp Code sicher und zuverlässig ist, und sie können dazu beitragen, Sicherheitsverletzungen zu verhindern und sensible Daten zu schützen.

## Referenzen

Hier finden Sie einige nützliche Ressourcen, um mehr über sichere Codierungspraktiken in C Sharp zu erfahren:

- [Microsoft's Secure Coding Guidelines for C Sharp and .NET](https://learn.microsoft.com/en-us/dotnet/standard/security/secure-coding-guidelines)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [NIST's Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf)
- [CIS Microsoft .NET Framework 4.5 Benchmark](https://www.cisecurity.org/benchmark/microsoft_net_framework_4-5_benchmark/)
- [Security Code Scan - .NET Security Guard](https://security-code-scan.github.io/#NET-Security-Guard)

Anhand dieser Ressourcen können Entwickler mehr über sichere Coding-Praktiken in C Sharp erfahren und lernen, wie sie diese in ihren Projekten umsetzen können.

---
title: "Estàndards de codificació segura per a desenvolupadors de C#"
date: 2023-02-28
lastmod: 2026-11-19
toc: true
draft: false
description: "Aprèn les bones pràctiques de codificació segura en C# per reduir el risc de bretxes de seguretat i protegir les dades sensibles."
tags: ["codificació segura", "desenvolupament en C#", "programació en C#", "bones pràctiques de codificació segura", "seguretat de C#", "seguretat d'ASP.NET", "seguretat de .NET Core", "validació d'entrades", "hash de contrasenyes", "criptografia", "mínim privilegi", "analitzador estàtic de codi", "seguretat d'aplicacions web", "prevenció d'injeccions SQL", "prevenció de scripting entre llocs", "protecció de dades", "comprovacions de salut", "gestió de sessions", "bones pràctiques d'OWASP", "estàndards de codificació segura en C#", "guies de seguretat de C#", "consells de codificació segura", "desenvolupament de programari segur", "marcs de codificació segura", "tècniques de codificació segura", "recomanacions de codificació segura", "programació segura en C#", "vulnerabilitats de codificació segura", "eines de codificació segura", "tutorials de codificació segura", "bones pràctiques de codificació segura en C#", "guies de codificació segura en C#", "estàndards de codificació segura per a desenvolupadors de C#", "pràctiques de codificació segura en C#", "com aplicar la codificació segura en C#", "consells de codificació segura per a programadors de C#", "codificació segura en aplicacions web de C#", "marcs de codificació segura en C#", "tècniques de codificació segura per a desenvolupadors de C#", "eines de codificació segura en C#"]
cover: "/img/cover/A_cartoon_developer_with_a_lock_icon_as_the_head_surrounded.webp"
coverAlt: "Un desenvolupador de dibuixos animats amb una icona de pany com a cap, envoltat de codi i protegit per un tallafoc."
coverCaption: ""
---

La codificació segura ajuda a mantenir el codi protegit, fiable i lliure de vulnerabilitats. C# és un llenguatge de programació popular, però els desenvolupadors han de seguir estàndards de codificació segura per reduir els riscos. Algunes bones pràctiques són validar les entrades, evitar funcions insegures, fer servir biblioteques criptogràfiques i mantenir actualitzades les biblioteques i els marcs de treball.

_____

## Validació d'entrades

Les entrades dels usuaris sovint són una font important de riscos de seguretat. La validació comprova que les dades introduïdes compleixin els criteris previstos i es puguin fer servir amb seguretat dins de l'aplicació. Per exemple, un número de targeta de crèdit només hauria de contenir dígits, sense caràcters especials. Per validar-lo, els desenvolupadors poden fer servir classes integrades com `Regex`.

```csharp
public static bool ValidateInput(string inputString)
{
    bool isValid = false;
    // Comprova que la cadena d'entrada només contingui dígits
    if (Regex.IsMatch(inputString, @"^\d+$"))
    {
        isValid = true;
    }
    return isValid;
}
```

Aquest mètode fa servir expressions regulars per comprovar si la cadena d'entrada només conté dígits. Retorna un valor booleà que indica si l'entrada és vàlida.

## Evita les funcions insegures

C# inclou funcions que poden crear problemes de seguretat si no es fan servir amb cura. `Process.Start()`, la reflexió (`Reflection`) i la deserialització (`Deserialization`) poden permetre que un atacant executi codi maliciós. Evita aquestes funcions o restringeix-ne els paràmetres i fes-les servir només quan calgui.

Per iniciar un procés extern, per exemple, fes servir `Process.StartInfo` per definir els arguments i les restriccions de seguretat en lloc de passar-los directament a `Process.Start()`.

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

## Fes servir biblioteques criptogràfiques

Biblioteques com Bouncy Castle i les API criptogràfiques de .NET Framework ofereixen maneres segures de xifrar i desxifrar. Fes servir aquestes biblioteques en lloc de crear mètodes de xifratge propis, que poden contenir vulnerabilitats.

Per exemple, per xifrar una contrasenya, fes servir la classe `Rfc2898DeriveBytes` de les API criptogràfiques de .NET Framework com es mostra a continuació:

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

La classe `Rfc2898DeriveBytes` genera una sal aleatòria i el fa servir per derivar una clau de la contrasenya. Després, la clau resultant s'utilitza per xifrar-la.

## Segueix el principi del mínim privilegi

El principi del mínim privilegi limita els usuaris o processos al nivell d'accés mínim necessari per fer la seva feina. Els desenvolupadors l'han de seguir per reduir l'impacte d'una bretxa de seguretat.

Si una aplicació només necessita llegir una base de dades, per exemple, fes servir un compte amb permisos de només lectura en lloc d'un compte amb permisos complets. Això redueix el risc que un atacant aprofiti l'aplicació per modificar o suprimir dades.

## Mantén actualitzats els marcs i les biblioteques

Les biblioteques i els marcs de treball poden contenir vulnerabilitats que els atacants poden aprofitar. Mantén-los actualitzats a les versions més recents per evitar riscos de seguretat coneguts.

Per exemple, si una biblioteca de tercers com `Newtonsoft.Json` té una vulnerabilitat, actualitza-la a una versió que la corregeixi.

## Fes servir un analitzador estàtic de codi

Un analitzador estàtic pot detectar possibles vulnerabilitats abans d'executar el codi. Fes servir eines com Code Analysis de Visual Studio, `ReSharper` i `SonarQube` per trobar i corregir problemes de seguretat abans del desplegament.

Per exemple, Code Analysis de Visual Studio examina el codi C# per detectar problemes potencials com ara injeccions SQL, scripting entre llocs i ús de funcions insegures.

## Aplica pràctiques de codificació segura a les aplicacions web

Les aplicacions web estan exposades a riscos com el scripting entre llocs, les injeccions SQL i les injeccions d'ordres. Aplica pràctiques com validar les entrades, codificar les sortides i fer servir consultes parametrizades per protegir-les.

Quan escriguis consultes SQL, fes servir consultes parametrizades en lloc de concatenar-hi dades introduïdes per l'usuari. Així l'entrada es tracta com a dada, no com a codi executable, i s'ajuda a prevenir les injeccions SQL.

```csharp
string query = "SELECT * FROM Users WHERE Username = @Username";
using (SqlConnection connection = new SqlConnection(connectionString))
{
    using (SqlCommand command = new SqlCommand(query, connection))
    {
        command.Parameters.AddWithValue("@Username", username);
        connection.Open();
        SqlDataReader reader = command.ExecuteReader();
        // Processa les dades
    }
}
```

Els desenvolupadors també han de validar totes les entrades, codificar les sortides i fer servir HTTPS per xifrar les dades transmeses per la xarxa.

_____

## Estàndards de codificació segura per als marcs de C#

Marcs de C# com ASP.NET i .NET Core tenen estàndards de codificació segura propis. Segueix-los quan desenvolupis aplicacions amb aquests marcs.

### ASP.NET

ASP.NET és un marc web popular per a C#. Algunes pràctiques de codificació segura són:

- Fes servir el sistema d'autenticació integrat d'ASP.NET en lloc de crear-ne un de propi. Per exemple, pots fer servir `Identity` per gestionar l'autenticació i l'autorització dels usuaris.
- Fes servir les funcions integrades d'ASP.NET per al hash de contrasenyes en lloc de crear mètodes propis. Per exemple, fes servir `PasswordHasher` per generar i verificar hashes de contrasenyes amb seguretat.
- Fes servir `AntiForgeryToken`, integrat a ASP.NET, per prevenir els atacs de falsificació de peticions entre llocs (CSRF). Pots fer servir l'atribut `ValidateAntiForgeryToken` per validar els tokens a les peticions POST.
- Fes servir `OutputCacheAttribute` per evitar que es desin dades sensibles a la memòria cau. Defineix polítiques de memòria cau per a les pàgines perquè no s'hi emmagatzemin dades sensibles.

### .NET Core

.NET Core és un marc multiplataforma i de codi obert per crear aplicacions modernes al núvol. Algunes pràctiques de codificació segura són:

- Fes servir l'autenticació integrada de .NET Core en lloc de crear-ne una de pròpia. Per exemple, fes servir `Identity` per gestionar l'autenticació i l'autorització.
- Fes servir les funcions integrades de hash de contrasenyes en lloc de crear mètodes propis. `PasswordHasher` permet generar i verificar hashes.
- Fes servir l'API de protecció de dades (Data Protection API) integrada de .NET Core per protegir dades sensibles com cadenes de connexió i secrets. La classe `DataProtectionProvider` permet protegir les dades amb una clau.
- Fes servir comprovacions de salut (Health Checks) per supervisar l'estat de l'aplicació. El component intermediari `HealthCheck` pot fer comprovacions periòdiques i avisar si detecta problemes.

## Conclusió

Els estàndards de codificació segura ajuden a mantenir el codi fiable i lliure de vulnerabilitats. Els desenvolupadors de C# han de validar les entrades, evitar funcions insegures, fer servir biblioteques criptogràfiques i mantenir les dependències actualitzades. Quan treballin amb marcs de C#, també han de seguir les normes de seguretat que aquests recomanen.

La codificació segura és un procés continu que requereix estar al dia de les pràctiques i les eines de seguretat. Integrar-les al procés de desenvolupament ajuda a reduir el risc de bretxes i a protegir les dades sensibles.

Per començar, revisa les pràctiques d'aquest article. Identifica les parts del codi exposades a riscos, com la validació d'entrades, el hash de contrasenyes i la gestió de sessions, i aplica les mesures adequades.

Segueix els blogs de seguretat, assisteix a conferències i participa en comunitats en línia per conèixer les tendències i pràctiques més recents.

Promou una cultura de seguretat dins de l'equip compartint bones pràctiques, organitzant sessions de formació i aplicant-les en el teu propi codi. Això ajuda a protegir el codi de tot l'equip.

Aquestes pràctiques ajuden a mantenir el codi C# segur i fiable, prevenir bretxes de seguretat i protegir les dades sensibles.

## Referències

Aquests recursos ofereixen més informació sobre codificació segura en C#:

- [Guies de codificació segura de Microsoft per a C# i .NET](https://learn.microsoft.com/en-us/dotnet/standard/security/secure-coding-guidelines)
- [Pràctiques de codificació segura d'OWASP](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [Marc de desenvolupament de programari segur del NIST](https://csrc.nist.gov/Projects/ssdf)
- [Referència CIS de seguretat per a Microsoft .NET Framework 4.5](https://www.cisecurity.org/benchmark/microsoft_net_framework_4-5_benchmark/)
- [Security Code Scan - .NET Security Guard](https://security-code-scan.github.io/#NET-Security-Guard)

Aquests recursos ajuden els desenvolupadors a aprofundir en la codificació segura i a aplicar-la als seus projectes.

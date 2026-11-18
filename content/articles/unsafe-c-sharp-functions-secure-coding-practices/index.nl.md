---
title: "Onveilige C#-functies: veilig programmeren"
date: 2023-09-25
lastmod: 2026-11-14
toc: true
draft: false
description: "Veilige alternatieven voor onveilige C#-functies. Leer risico’s voor geheugenveiligheid herkennen en onveilige bewerkingen vervangen."
genre: ["Softwareontwikkeling", "C#-programmering", "Cyberbeveiliging", "Codebeveiliging", "Veilig programmeren", "Aanbevolen programmeerpraktijken", "Softwarekwetsbaarheden", "Cryptografie", "Webontwikkeling", "Applicatiebeveiliging"]
tags: ["veilig programmeren", "C#-programmering", "softwarekwetsbaarheden", "bufferoverloop", "invoervalidatie", "SQL-injectie", "XSS-aanvallen", "geheugenbeheer", "bestands-toegangsbeheer", "cryptografie", "Bouncy Castle", "tekenreeksbewerking", "stringinterpolatie", "geparametriseerde query’s", "gegevensbeveiliging", "programmeertips", "applicatieontwikkeling", "programmeerrichtlijnen", "tips voor codebeveiliging", "veilige software", "softwarearchitectuur", "codeerpraktijken", "bestandsbeveiliging", "gegevensbescherming", "cyberbeveiligingstips", "codebeveiliging", "coderingsstandaarden", "beveiliging van webapps", "software-engineering", "gegevensversleuteling"]
cover: "/img/cover/secure-coding-shield.webp"
coverAlt: "Een 3D-illustratie van een schild dat regels code beschermt."
coverCaption: "Bescherm je code met veilige C#-functies voor robuuste toepassingen."
---
## **Onveilige C#-functies** en hun **veilige alternatieven**

In de programmeerwereld is **C#** een krachtige en veelgebruikte taal die bekendstaat om haar veelzijdigheid en robuustheid. Toch bevat elke programmeertaal functies die bij onzorgvuldig gebruik kwetsbaarheden kunnen veroorzaken. In dit artikel verkennen we **onveilige C#-functies** die toepassingen kunnen blootstellen aan beveiligingsrisico’s, en bekijken we hun **veilige alternatieven**. Als ontwikkelaars deze valkuilen herkennen en weten hoe ze die kunnen vermijden, kunnen ze veiligere en betrouwbaardere code schrijven.

## Inleiding

**C#** is uitgegroeid tot een populaire keuze voor applicatieontwikkeling en ondersteunt uiteenlopende software, van desktopprogramma’s tot webtoepassingen. De taal biedt ontwikkelaars veel functies en mogelijkheden, maar sommige daarvan kunnen onbedoeld beveiligingslekken veroorzaken. In de volgende paragrafen bekijken we zulke functies, de bijbehorende risico’s en manieren om ze te vermijden.

### De risico’s van onveilige C#-functies

Bepaalde C#-functies vormen **valkuilen** en bieden aanvallers mogelijkheden om kwetsbaarheden zoals **bufferoverlopen**, **injectieaanvallen** en **gegevenslekken** uit te buiten. Ontwikkelaars moeten deze gevaren herkennen en bewust kiezen voor veiligere alternatieven om mogelijke aanvallen te voorkomen.

## Tekenreeksbewerking

### **Onveilig: `string.Format()` gebruiken**

Het gebruik van `string.Format()` kan een risico op **format-stringkwetsbaarheden** opleveren. Een aanvaller kan in bepaalde situaties kwaadaardige opmaakspecificaties invoeren, wat tot ongeoorloofde openbaarmaking van gegevens kan leiden en in ernstige gevallen zelfs de mogelijkheid van uitvoering van code op afstand kan creëren.

```c#
// Gebruik van string.Format()
string name = "John";
int age = 30;
string formattedString = string.Format("Mijn naam is {0} en ik ben {1} jaar oud.", name, age);
Console.WriteLine(formattedString);
```

### **Veilig alternatief: `string interpolation` gebruiken**

Een verstandigere manier om het risico op format-stringkwetsbaarheden te beperken is **stringinterpolatie**. Deze aanpak maakt de code beter leesbaar en voert tekenreeksopmaak op een gecontroleerde manier uit. Zo verklein je het risico op format-stringproblemen en maak je de code robuuster.

```c#
// Gebruik van stringinterpolatie
string name = "John";
int age = 30;
string interpolatedString = $"Mijn naam is {name} en ik ben {age} jaar oud.";
Console.WriteLine(interpolatedString);
```

## Invoervalidatie

### **Onveilig: onvoldoende invoervalidatie**

Wie het belang van grondige validatie van gebruikersinvoer onderschat, stelt een toepassing bloot aan uiteenlopende kwetsbaarheden, waaronder de bekende **SQL-injectie** en de veelvoorkomende aanvallen met **cross-site scripting (XSS)**.

```c#
string userInput = Request.QueryString["input"];
string sqlQuery = "SELECT * FROM Users WHERE Name='" + userInput + "'";
```

### **Veilig alternatief: geparametriseerde query’s gebruiken**

Een effectieve bescherming tegen de risico’s van onvoldoende invoervalidatie is het gebruik van **geparametriseerde query’s**. Bij databasebewerkingen voorkomt deze techniek dat kwaadaardige invoer als uitvoerbare code wordt behandeld.

```c#
string userInput = Request.QueryString["input"];
string sqlQuery = "SELECT * FROM Users WHERE Name=@userName";
SqlCommand command = new SqlCommand(sqlQuery, connection);
command.Parameters.AddWithValue("@userName", userInput);
```

## Geheugenbeheer

### **Onveilig: `Array.Copy()` gebruiken zonder grenzen te controleren**

`Array.Copy()` gebruiken zonder zorgvuldig de grenzen te controleren is riskant en kan leiden tot **bufferoverlopen** en andere problemen met geheugenbeheer.

```C#
int[] sourceArray = { 1, 2, 3, 4, 5 };
int[] destinationArray = new int[3];
Array.Copy(sourceArray, destinationArray, 5); // Mogelijk bufferoverloop
```

### **Veilig alternatief: `Array.CopyTo()` gebruiken**

Ontwikkelaars kunnen voor geheugenbewerkingen overstappen op `Array.CopyTo()`. Deze keuze helpt om gegevens gecontroleerder te kopiëren en het risico op bufferoverloop te beperken.

```c#
int[] sourceArray = { 1, 2, 3, 4, 5 };
int[] destinationArray = new int[3];
sourceArray.CopyTo(destinationArray, 0);
```

## Bestandsverwerking

### **Onveilig: `File.Delete()` gebruiken**

`File.Delete()` kan bestanden verwijderen zonder passende toegangscontrole. Onzorgvuldig gebruik kan zo tot onbedoelde verwijdering van belangrijke bestanden en andere beveiligingsproblemen leiden.

```C#
string filePath = "path/to/file.txt";
File.Delete(filePath); // Verwijdert het bestand zonder passende toegangscontrole
```

### **Veilig alternatief:** `SecureString` voor bestandspaden

Om risico’s van ongeoorloofde bestandsverwijdering te beperken, wordt hier **SecureString** voorgesteld voor bestandspaden, in combinatie met passende toegangscontrole. Zo kan de toepassing de toegang tot bestanden beter bewaken.

```C#
using System.Security;
// ...
SecureString secureFilePath = new SecureString();
foreach (char c in "path/to/file.txt")
{
    secureFilePath.AppendChar(c);
}
// Implement proper file access control using secureFilePath
```

## Cryptografie

### **Onveilig: zelf cryptografische algoritmen maken**

Zelf cryptografische algoritmen ontwerpen lijkt soms aantrekkelijk, maar kan ernstige beveiligingsfouten opleveren. Zonder grondige tests en validatie kunnen zulke implementaties kwetsbaar zijn.

```C#
// Dit is een voorbeeld van een onveilig, zelfgemaakt cryptografisch algoritme. Gebruik dit NIET in productie.
public static string UnsafeCustomEncrypt(string data)
{
    // ... logica voor aangepaste versleuteling ...
    return encryptedData;
}
```

### **Veilig alternatief: gevestigde cryptografische bibliotheken gebruiken**

Ontwikkelaars doen er goed aan cryptografie te baseren op **gevestigde en grondig gecontroleerde bibliotheken** die industriestandaarden volgen. Een voorbeeld voor C#-ontwikkelaars is de bekende **Bouncy Castle**-bibliotheek.

```C#
using Org.BouncyCastle.Crypto;
using Org.BouncyCastle.Security;
// ...
public static byte[] SecureEncryption(byte[] data)
{
    IBufferedCipher cipher = CipherUtilities.GetCipher("AES/ECB/PKCS7Padding");
    // ... versleutelingsparameters en sleutel instellen ...
    return cipher.DoFinal(data);
}
```

## **Conclusie: bescherm je code voor een veilige toekomst**

Bij softwareontwikkeling staat één uitgangspunt centraal: **beveiliging prioriteit geven**. De integriteit van software hangt op veel manieren af van de keuzes van ontwikkelaars, waaronder het vermijden van **onveilige C#-functies** en het toepassen van **veilige alternatieven**. Door risico’s te herkennen en passende maatregelen te nemen, kunnen ontwikkelaars software bouwen die beter bestand is tegen aanvallen en kwetsbaarheden actief tegengaat.

Onthoud dat **veilige software ontwikkelen een doorlopend proces** is. Blijf op de hoogte van aanbevolen werkwijzen en mogelijke kwetsbaarheden, zodat je weloverwogen keuzes kunt maken. Elke regel code biedt een kans om de digitale omgeving weerbaarder te maken.

De weg naar veilige software vraagt voortdurend aandacht. Op de hoogte blijven van aanbevolen werkwijzen en mogelijke kwetsbaarheden blijft belangrijk voor succes.

## Bronnen

1. [Microsoft-documentatie voor C#](https://docs.microsoft.com/en-us/dotnet/csharp/)
2. [OWASP Top tien](https://owasp.org/www-project-top-ten/)
3. [Richtlijnen voor veilig programmeren in C#](https://cwe.mitre.org/data/definitions/242.html)
4. [Bouncy Castle-cryptografiebibliotheek](https://www.bouncycastle.org/)

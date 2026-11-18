---
title: "Funcions C# insegures: pràctiques de programació segura"
date: 2023-09-25
lastmod: 2026-11-14
toc: true
draft: false
description: "Alternatives segures a les funcions C# insegures. Aprèn a identificar els riscos per a la seguretat de la memòria i a substituir les operacions vulnerables."
genre: ["Desenvolupament de programari", "Programació en C#", "Ciberseguretat", "Seguretat del codi", "Programació segura", "Bones pràctiques de programació", "Vulnerabilitats de programari", "Criptografia", "Desenvolupament web", "Seguretat d’aplicacions"]
tags: ["programació segura", "programació en C#", "vulnerabilitats de programari", "desbordament de búfer", "validació de l’entrada", "injecció SQL", "atacs XSS", "gestió de la memòria", "control d’accés als fitxers", "criptografia", "Bouncy Castle", "manipulació de cadenes", "interpolació de cadenes", "consultes parametritzades", "seguretat de les dades", "consells de programació", "desenvolupament d’aplicacions", "guies de programació", "consells de seguretat del codi", "programari segur", "arquitectura de programari", "pràctiques de codificació", "seguretat dels fitxers", "protecció de dades", "consells de ciberseguretat", "seguretat del codi", "estàndards de codificació", "seguretat d’aplicacions web", "enginyeria del programari", "xifratge de dades"]
cover: "/img/cover/secure-coding-shield.webp"
coverAlt: "Il·lustració tridimensional d’un escut que protegeix línies de codi."
coverCaption: "Protegeix el codi amb funcions C# segures per crear aplicacions robustes."
---
## **Funcions C# insegures** i les seves **alternatives segures**

**C#** és un llenguatge de programació potent i molt utilitzat, conegut per la seva versatilitat i solidesa. Com qualsevol llenguatge, però, inclou funcions que poden introduir vulnerabilitats si s’utilitzen sense cura. En aquest article examinem les **funcions C# insegures** que poden exposar les aplicacions a riscos i les seves **alternatives segures**. Reconèixer aquests perills i saber com evitar-los ajuda a escriure codi més segur i fiable.

## Introducció

**C#** és una opció popular per desenvolupar diversos tipus de programari, des d’aplicacions d’escriptori fins a solucions web. El llenguatge ofereix moltes funcions i capacitats, però algunes poden convertir-se involuntàriament en vies per introduir vulnerabilitats. A continuació analitzem aquestes funcions, els riscos associats i com evitar-los.

### Els riscos de les funcions C# insegures

Algunes funcions C# són **paranys** que ofereixen als atacants oportunitats per explotar vulnerabilitats com ara **desbordaments de búfer**, **atacs d’injecció** i **fuites de dades**. Els desenvolupadors han de reconèixer aquests perills i triar alternatives més segures per prevenir possibles atacs.

## Manipulació de cadenes

### **Insegur: utilitzar `string.Format()`**

L’ús de `string.Format()` pot comportar el risc de **vulnerabilitats de format de cadenes**. En determinades situacions, un atacant podria inserir especificadors de format maliciosos, provocar la divulgació no autoritzada de dades i, en casos greus, arribar a possibilitar l’execució remota de codi.

```c#
// Ús de string.Format()
string name = "John";
int age = 30;
string formattedString = string.Format("Em dic {0} i tinc {1} anys.", name, age);
Console.WriteLine(formattedString);
```

### **Alternativa segura: interpolació de cadenes**

La **interpolació de cadenes** és una manera més prudent de reduir els riscos de format. Millora la llegibilitat del codi i formata el text de manera controlada.

```c#
// Ús de la interpolació de cadenes
string name = "John";
int age = 30;
string interpolatedString = $"Em dic {name} i tinc {age} anys.";
Console.WriteLine(interpolatedString);
```

## Validació de l’entrada

### **Insegur: validació insuficient de l’entrada**

Restar importància a la validació completa de les dades introduïdes pels usuaris exposa les aplicacions a diverses vulnerabilitats, entre les quals hi ha la **injecció SQL** i els atacs habituals de **cross-site scripting (XSS)**.

```c#
string userInput = Request.QueryString["input"];
string sqlQuery = "SELECT * FROM Users WHERE Name='" + userInput + "'";
```

### **Alternativa segura: consultes parametritzades**

Una manera eficaç de reduir aquests riscos és utilitzar **consultes parametritzades**. En les operacions amb bases de dades, aquesta tècnica impedeix que les dades malicioses s’interpretin com a codi executable.

```c#
string userInput = Request.QueryString["input"];
string sqlQuery = "SELECT * FROM Users WHERE Name=@userName";
SqlCommand command = new SqlCommand(sqlQuery, connection);
command.Parameters.AddWithValue("@userName", userInput);
```

## Gestió de la memòria

### **Insegur: utilitzar `Array.Copy()` sense comprovar els límits**

Utilitzar `Array.Copy()` sense comprovar atentament els límits és arriscat i pot provocar **desbordaments de búfer** i altres problemes de memòria.

```C#
int[] sourceArray = { 1, 2, 3, 4, 5 };
int[] destinationArray = new int[3];
Array.Copy(sourceArray, destinationArray, 5); // Risc de desbordament de búfer
```

### **Alternativa segura: utilitzar `Array.CopyTo()`**

Els desenvolupadors poden utilitzar `Array.CopyTo()` per copiar les dades de manera més controlada. Aquesta opció ajuda a reduir el risc de desbordament de búfer.

```c#
int[] sourceArray = { 1, 2, 3, 4, 5 };
int[] destinationArray = new int[3];
sourceArray.CopyTo(destinationArray, 0);
```

## Gestió dels fitxers

### **Insegur: utilitzar `File.Delete()`**

`File.Delete()` pot suprimir fitxers sense controls d’accés adequats. Un ús poc curós pot eliminar accidentalment fitxers importants i causar altres problemes de seguretat.

```C#
string filePath = "path/to/file.txt";
File.Delete(filePath); // Suprimeix el fitxer sense els permisos adequats
```

### **Alternativa segura: **`SecureString`** per a les rutes dels fitxers**

Per reduir el risc de supressions no autoritzades, l’exemple proposa utilitzar **SecureString** per a les rutes dels fitxers, amb controls d’accés adequats. Això pot ajudar l’aplicació a gestionar millor l’accés als fitxers.

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

## Criptografia

### **Insegur: crear algoritmes criptogràfics propis**

Dissenyar algoritmes criptogràfics propis pot semblar atractiu, però pot introduir errors greus de seguretat. Sense proves i validacions exhaustives, aquestes implementacions poden ser vulnerables.

```C#
// Exemple d’algoritme criptogràfic propi i insegur. NO l’utilitzis en producció.
public static string UnsafeCustomEncrypt(string data)
{
    // ... lògica de xifratge personalitzada ...
    return encryptedData;
}
```

### **Alternativa segura: utilitzar biblioteques criptogràfiques consolidades**

Els desenvolupadors haurien de basar-se en **biblioteques criptogràfiques consolidades i revisades rigorosament** que segueixin els estàndards del sector. **Bouncy Castle** és un exemple conegut per a C#.

```C#
using Org.BouncyCastle.Crypto;
using Org.BouncyCastle.Security;
// ...
public static byte[] SecureEncryption(byte[] data)
{
    IBufferedCipher cipher = CipherUtilities.GetCipher("AES/ECB/PKCS7Padding");
    // ... configuració dels paràmetres de xifratge i de la clau ...
    return cipher.DoFinal(data);
}
```

## **Conclusió: protegeix el codi per a un futur segur**

En el desenvolupament de programari, hi ha un principi essencial: **prioritzar la seguretat**. La integritat del programari depèn de moltes decisions, incloses evitar les **funcions C# insegures** i adoptar-ne les **alternatives segures**. En reconèixer els riscos i aplicar mesures adequades, els desenvolupadors poden crear programari més resistent als atacs i reduir les vulnerabilitats.

El desenvolupament de programari segur és un procés continu. Mantén-te al dia de les pràctiques recomanades i les vulnerabilitats possibles per prendre decisions informades. Cada línia de codi ofereix l’oportunitat de fer més resilient l’entorn digital.

El camí cap a un programari segur exigeix atenció constant. Conèixer les bones pràctiques i les vulnerabilitats potencials és important per tenir èxit.

## Referències

1. [Documentació de Microsoft sobre C#](https://docs.microsoft.com/en-us/dotnet/csharp/)
2. [Els deu principals riscos d’OWASP](https://owasp.org/www-project-top-ten/)
3. [Directrius de programació segura en C#](https://cwe.mitre.org/data/definitions/242.html)
4. [Biblioteca criptogràfica Bouncy Castle](https://www.bouncycastle.org/)

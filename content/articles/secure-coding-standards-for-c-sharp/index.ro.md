---
title: "Standarde de codare securizată pentru dezvoltatorii C#"
date: 2023-02-28
toc: true
draft: false
description: "Învățați cele mai bune practici de codare securizată în C# pentru a minimiza riscul de breșe de securitate și pentru a proteja datele sensibile."
tags: ["Codare securizată", "C dezvoltare ascuțită", "Programare C Sharp", "practici de codificare sigură", "Securitatea C Sharp", "Securitatea ASP.NET", "Securitatea .NET Core", "validarea intrărilor", "hashing parola", "criptografie", "cel mai mic privilegiu", "analizor de cod static", "securitatea aplicațiilor web", "Prevenirea injectării SQL", "prevenirea scripturilor cross-site", "protecția datelor", "controale de sănătate", "gestionarea sesiunilor", "Cele mai bune practici OWASP", "Standardele de codare securizată C Sharp", "C Orientări de securitate Sharp", "sfaturi de codare sigură", "dezvoltarea de software securizat", "cadre de codare securizate", "tehnici de codificare sigură", "recomandări de codare sigură", "Programare securizată în C Sharp", "vulnerabilități de codare securizată", "instrumente de codare securizată", "tutoriale de codare securizată", "Cele mai bune practici pentru codarea securizată în C Sharp", "Ghidul de codare securizată C Sharp", "Standarde de codare securizată pentru dezvoltatorii C Sharp", "C Practici de codare sigură Sharp", "Cum se implementează codarea securizată în C Sharp", "Sfaturi de codare sigură pentru programatorii C Sharp", "Codare securizată în aplicații web C Sharp", "Cadre de codare securizată C Sharp", "Tehnici de codare securizată pentru dezvoltatorii C Sharp", "Instrumente de codare securizată C Sharp"]
cover: "/img/cover/A_cartoon_developer_with_a_lock_icon_as_the_head_surrounded.png"
coverAlt: " Un dezvoltator de desene animate cu o pictogramă de lacăt în cap, înconjurat de cod și protejat de un firewall."
coverCaption: ""
---

Codificarea securizată este esențială pentru a garanta că codul este sigur, fiabil și lipsit de vulnerabilități. C Sharp este un limbaj de programare popular care impune dezvoltatorilor să respecte standardele de codare sigură pentru a preveni riscurile de securitate. Urmând cele mai bune practici, cum ar fi validarea intrărilor, evitarea funcțiilor nesigure, utilizarea bibliotecilor de criptografie și actualizarea bibliotecilor și a cadrelor de lucru, dezvoltatorii se pot asigura că codul lor este sigur și lipsit de vulnerabilități.

_____

## Validarea intrărilor

Datele introduse de utilizator reprezintă adesea o sursă semnificativă de riscuri de securitate. Validarea intrărilor este procesul de verificare a faptului că datele introduse de utilizator îndeplinesc criteriile așteptate și că pot fi utilizate în siguranță în aplicație. De exemplu, atunci când un utilizator introduce un număr de card de credit, acesta trebuie să conțină numai cifre și niciun caracter special. Pentru a valida datele de intrare, dezvoltatorii pot utiliza clase integrate, cum ar fi `Regex` pentru a se asigura că datele de intrare îndeplinesc criteriile așteptate.

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

Această metodă utilizează expresii regulate pentru a verifica dacă șirul de intrare conține numai cifre. Aceasta returnează o valoare booleană care indică dacă intrarea este validă sau nu.

## Evitați utilizarea funcțiilor nesigure
C Sharp are mai multe funcții care pot fi vulnerabile la probleme de securitate dacă nu sunt utilizate cu atenție. Funcții precum `Process.Start()` `Reflection` și `Deserialization` poate permite atacatorilor să execute coduri malițioase. Dezvoltatorii ar trebui să evite utilizarea acestor funcții sau să le utilizeze cu prudență prin restricționarea parametrilor de intrare și utilizarea lor numai atunci când este necesar.

De exemplu, în loc de a utiliza `Process.Start()` pentru a porni un proces extern, dezvoltatorii ar trebui să folosească funcția `Process.StartInfo` pentru a furniza argumente și restricții de securitate.
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
## Utilizați bibliotecile de criptografie
Bibliotecile de criptografie, cum ar fi Bouncy Castle și API-urile de criptografie din .NET Framework, oferă o modalitate sigură de a efectua operațiuni de criptare și decriptare. Utilizați aceste biblioteci în loc să creați metode de criptare personalizate, care pot fi predispuse la vulnerabilități.

De exemplu, pentru a cripta o parolă, utilizați biblioteca `Rfc2898DeriveBytes` din API-urile de criptografie din .NET Framework, după cum urmează:
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
The `Rfc2898DeriveBytes` generează o sare și o folosește pentru a obține o cheie din parolă. Cheia rezultată este apoi utilizată pentru a cripta parola.

## Urmează principiul privilegiului cel mai mic

Principiul celui mai mic privilegiu este o bună practică de securitate care restricționează utilizatorii sau procesele la nivelul minim de acces necesar pentru a-și îndeplini funcțiile. Dezvoltatorii ar trebui să urmeze acest principiu atunci când scriu codul pentru a minimiza impactul breșelor de securitate.

De exemplu, dacă o aplicație necesită acces doar pentru citire la o bază de date, ar trebui să utilizeze un cont de bază de date cu permisiuni de doar citire în loc de un cont cu permisiuni complete. Acest lucru reduce riscul ca un atacator să exploateze aplicația pentru a modifica sau șterge date.

## Păstrați bibliotecile și cadrele actualizate

Bibliotecile și cadrele pot conține vulnerabilități de securitate care pot fi exploatate de atacatori. Dezvoltatorii ar trebui să își păstreze bibliotecile și cadrele actualizate la cea mai recentă versiune pentru a evita eventualele probleme de securitate.

De exemplu, dacă aplicația utilizează o bibliotecă terță parte, cum ar fi `Newtonsoft.Json` care prezintă o vulnerabilitate de securitate, dezvoltatorul ar trebui să actualizeze la cea mai recentă versiune a bibliotecii care rezolvă vulnerabilitatea.

## Utilizați un analizor de cod static

Un analizor de cod static este un instrument care poate identifica potențiale vulnerabilități de securitate în cod înainte ca acesta să fie executat. Folosiți instrumente cum ar fi Visual Studio's Code `Analysis` `ReSharper` și `SonarQube` pentru a detecta problemele de securitate din cod și a le remedia înainte de implementare.

De exemplu, Visual Studio's Code Analysis este un popular analizor de cod static care examinează codul C Sharp pentru a detecta eventualele vulnerabilități de securitate. Acesta poate detecta probleme precum injecția SQL, scriptingul cross-site și utilizarea de funcții nesigure.

## Utilizați practici de codare securizată pentru aplicațiile web

Aplicațiile web sunt vulnerabile la mai multe riscuri de securitate, cum ar fi scriptingul cross-site, injecția SQL și injecția de comenzi. Dezvoltatorii ar trebui să urmeze practici de codare sigură, cum ar fi validarea intrărilor, codificarea ieșirilor și interogările parametrizate pentru a se asigura că aplicațiile web sunt sigure.

De exemplu, atunci când scrieți interogări SQL, utilizați interogări parametrizate în loc să concatenați datele introduse de utilizator cu interogarea. Interogările parametrizate previn atacurile de injecție SQL prin tratarea datelor introduse de utilizator ca date și nu ca cod executabil.

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

De asemenea, dezvoltatorii ar trebui să valideze toate datele introduse de utilizatori, să codifice datele de ieșire și să utilizeze HTTPS pentru a cripta datele transmise prin rețea.

_____

## Standarde de codare securizată pentru cadrele C Sharp

Cadrele C Sharp, cum ar fi ASP.NET și .NET Core, au propriile standarde de codare securizată. Dezvoltatorii ar trebui să respecte aceste standarde atunci când dezvoltă aplicații care utilizează aceste cadre.

### ASP.NET
ASP.NET este un cadru web popular pentru C Sharp. Iată câteva standarde de codare securizată pentru ASP.NET:

- Folosiți sistemul de autentificare integrat în ASP.NET în loc să creați un sistem de autentificare personalizat. De exemplu, puteți utiliza sistemul de autentificare ASP.NET `Identity` pentru a gestiona autentificarea și autorizarea utilizatorilor.
- Utilizați funcțiile de hashing de parole încorporate în ASP.NET în loc să creați metode personalizate de hashing de parole. De exemplu, puteți utiliza funcția ASP.NET `PasswordHasher` pentru a verifica parolele în mod sigur.
- Utilizați clasa încorporată ASP.NET `AntiForgeryToken` pentru a preveni atacurile CSRF (Cross-Site Request Forgery). De exemplu, puteți utiliza funcția `ValidateAntiForgeryToken` pentru a valida token-urile anti-falsificare în cererile POST.
- Utilizați atributul încorporat în ASP.NET `OutputCacheAttribute` pentru a preveni stocarea în memoria cache a datelor sensibile. De exemplu, puteți utiliza opțiunea `OutputCacheAttribute` pentru a seta politici de memorie cache pentru paginile dvs. web și pentru a împiedica stocarea în memoria cache a datelor sensibile.

### .NET Core
.NET Core este un cadru de lucru open-source, transplatformat, pentru crearea de aplicații moderne, bazate pe cloud. Iată câteva standarde de codare securizată pentru .NET Core:

- Folosiți sistemul de autentificare integrat în .NET Core în loc să creați un sistem de autentificare personalizat. De exemplu, puteți utiliza sistemul de autentificare din .NET Core `Identity` pentru a gestiona autentificarea și autorizarea utilizatorilor.
- Utilizați funcțiile încorporate de hașurare a parolelor din .NET Core în loc să creați metode personalizate de hașurare a parolelor. De exemplu, puteți utiliza funcția .NET Core `PasswordHasher` pentru a verifica parolele în mod sigur.
- Utilizați API-ul integrat de protecție a datelor din .NET Core pentru a proteja datele sensibile, cum ar fi șirurile de conexiuni și secretele. De exemplu, puteți utiliza clasa `DataProtectionProvider` pentru a proteja datele sensibile cu ajutorul unei chei.
- Utilizați controalele de sănătate încorporate în .NET Core pentru a monitoriza starea de sănătate a aplicației dumneavoastră. De exemplu, puteți utiliza funcția `HealthCheck` middleware pentru a efectua verificări periodice ale sănătății aplicației dvs. și pentru a vă alerta cu privire la orice problemă.


## Concluzie
Standardele de codare securizată sunt esențiale pentru a garanta că codul este sigur, fiabil și lipsit de vulnerabilități. C Sharp este un limbaj de programare popular care impune dezvoltatorilor să respecte standardele de codare sigură pentru a preveni riscurile de securitate. Urmând cele mai bune practici, cum ar fi validarea intrărilor, evitarea funcțiilor nesigure, utilizarea bibliotecilor de criptografie și actualizarea bibliotecilor și a cadrelor de lucru, dezvoltatorii se pot asigura că codul lor este sigur și lipsit de vulnerabilități. Atunci când utilizează cadre C Sharp, dezvoltatorii trebuie să respecte standardele de codare securizată recomandate de cadrul respectiv.

Adoptarea standardelor de codare securizată este un proces continuu care necesită ca dezvoltatorii să rămână la curent cu cele mai recente bune practici și instrumente de securitate. Prin încorporarea standardelor de codare securizată în procesul de dezvoltare, dezvoltatorii pot minimiza riscul de breșe de securitate și pot proteja datele sensibile.

Pentru a începe cu codarea securizată în C Sharp, dezvoltatorii pot începe prin a se familiariza cu cele mai bune practici discutate în acest articol. Ei ar trebui să identifice zonele din codul lor care sunt susceptibile la riscuri de securitate, cum ar fi validarea intrărilor, hashing-ul parolei și gestionarea sesiunilor. Ei pot apoi să implementeze cele mai bune practici precum cele discutate în acest articol pentru a-și securiza codul.

De asemenea, dezvoltatorii ar trebui să rămână la curent cu cele mai recente tendințe și practici de securitate urmărind blogurile de securitate, participând la conferințe și participând la comunitățile online. Prin faptul că se mențin la curent cu noutățile, ei își pot păstra codul securizat și lipsit de vulnerabilități.

În cele din urmă, dezvoltatorii ar trebui să promoveze o cultură a conștientizării securității prin împărtășirea celor mai bune practici cu echipa sau colegii lor. Ei ar trebui să organizeze sesiuni de formare în domeniul securității, să împărtășească articole și resurse privind practicile de codare sigură și să dea un exemplu prin implementarea acestor bune practici în propriul cod. Prin promovarea unei culturi de conștientizare a securității, ei pot contribui la asigurarea faptului că codul echipei lor este sigur și lipsit de vulnerabilități.

Urmând aceste bune practici, dezvoltatorii se pot asigura că codul lor C Sharp este sigur și fiabil și pot contribui la prevenirea breșelor de securitate și la protejarea datelor sensibile.

## Referințe

Iată câteva resurse utile pentru a afla mai multe despre practicile de codare sigură în C Sharp:

- [Microsoft's Secure Coding Guidelines for C Sharp and .NET](https://learn.microsoft.com/en-us/dotnet/standard/security/secure-coding-guidelines)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [NIST's Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf)
- [CIS Microsoft .NET Framework 4.5 Benchmark](https://www.cisecurity.org/benchmark/microsoft_net_framework_4-5_benchmark/)
- [Security Code Scan - .NET Security Guard](https://security-code-scan.github.io/#NET-Security-Guard)

Urmărind aceste resurse, dezvoltatorii pot afla mai multe despre practicile de codare sigură în C Sharp și despre cum să le implementeze în proiectele lor.

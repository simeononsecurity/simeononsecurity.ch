---
title: "Standardy bezpiecznego kodowania dla programistów C#"
date: 2023-02-28
toc: true
draft: false
description: "Poznaj najlepsze praktyki bezpiecznego kodowania w C#, aby zminimalizować ryzyko naruszenia bezpieczeństwa i chronić wrażliwe dane."
tags: ["Ostrołęka", "bezpieczne kodowanie", "bezpieczeństwo", "programowanie", "ASP.NET", ".NET Core", "uwierzytelnianie", "haszowanie hasła", "walidacja wejścia", "kryptografia", "najmniejszy przywilej", "statyczny analizator kodu", "aplikacje internetowe", "Wstrzykiwanie kodu SQL", "cross-site scripting", "ochrona danych", "kontrole stanu zdrowia", "zarządzanie sesjami", "OWASP"]
cover: "/img/cover/A_cartoon_developer_with_a_lock_icon_as_the_head_surrounded.png"
coverAlt: " Kreskówkowy deweloper z ikoną zamka jako głową, otoczony kodem i osłonięty firewallem."
coverCaption: ""
---

Bezpieczne kodowanie jest niezbędne, aby zapewnić, że kod jest bezpieczny, niezawodny i wolny od podatności. C# jest popularnym językiem programowania, który wymaga od programistów przestrzegania standardów bezpiecznego kodowania, aby zapobiec zagrożeniom bezpieczeństwa. Poprzez przestrzeganie najlepszych praktyk, takich jak sprawdzanie poprawności danych wejściowych, unikanie niebezpiecznych funkcji, używanie bibliotek kryptograficznych oraz utrzymywanie aktualizacji bibliotek i frameworków, programiści mogą zapewnić, że ich kod jest bezpieczny i wolny od luk.

_____

## Walidacja wejść

Dane wejściowe użytkownika są często istotnym źródłem zagrożeń bezpieczeństwa. Walidacja danych wejściowych jest procesem weryfikacji, że dane wejściowe użytkownika spełniają oczekiwane kryteria i są bezpieczne do użycia w aplikacji. Na przykład, kiedy użytkownik wprowadza numer karty kredytowej, dane wejściowe powinny zawierać tylko cyfry i żadnych znaków specjalnych. Aby sprawdzić poprawność danych wejściowych, programiści mogą użyć wbudowanych klas takich jak`Regex` aby zapewnić, że dane wejściowe spełniają oczekiwane kryteria.

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

Metoda ta wykorzystuje wyrażenia regularne do sprawdzenia, czy łańcuch wejściowy zawiera tylko cyfry. Zwraca ona wartość boolean wskazującą, czy dane wejściowe są poprawne czy nie.

## Unikaj używania niebezpiecznych funkcji
C# posiada kilka funkcji, które mogą być podatne na problemy bezpieczeństwa, jeśli nie są używane ostrożnie. Funkcje takie jak`Process.Start()` `Reflection` oraz`Deserialization` może pozwolić atakującym na wykonanie złośliwego kodu. Programiści powinni unikać używania tych funkcji lub używać ich z ostrożnością, ograniczając parametry wejściowe i używając ich tylko w razie potrzeby.

Na przykład, zamiast używać`Process.Start()` aby uruchomić zewnętrzny proces, programiści powinni użyć`Process.StartInfo` właściwość, aby podać argumenty i ograniczenia bezpieczeństwa.
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
## Używaj bibliotek kryptograficznych
Biblioteki kryptograficzne, takie jak Bouncy Castle i .NET Framework's Cryptography APIs, zapewniają bezpieczny sposób wykonywania operacji szyfrowania i deszyfrowania. Używaj tych bibliotek zamiast tworzyć własne metody szyfrowania, które mogą być podatne na luki.

Na przykład, aby zaszyfrować hasło, należy użyć biblioteki`Rfc2898DeriveBytes` klasa z .NET Framework's Cryptography APIs w następujący sposób:
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
Na stronie`Rfc2898DeriveBytes` Klasa generuje sól i używa jej do wyprowadzenia klucza z hasła. Wynikowy klucz jest następnie używany do szyfrowania hasła.

## Follow the Principle of Least Privilege

Zasada najmniejszego przywileju jest najlepszą praktyką bezpieczeństwa, która ogranicza użytkowników lub procesy do minimalnego poziomu dostępu niezbędnego do wykonywania ich funkcji. Programiści powinni kierować się tą zasadą podczas pisania kodu, aby zminimalizować wpływ naruszenia bezpieczeństwa.

Na przykład, jeśli aplikacja wymaga dostępu tylko do odczytu do bazy danych, powinna używać konta bazy danych z uprawnieniami tylko do odczytu zamiast konta z pełnymi uprawnieniami. Zmniejsza to ryzyko wykorzystania aplikacji przez napastnika do modyfikacji lub usunięcia danych.

## Aktualizuj biblioteki i frameworki

Biblioteki i frameworki mogą zawierać luki bezpieczeństwa, które mogą być wykorzystane przez atakujących. Programiści powinni aktualizować swoje biblioteki i frameworki do najnowszej wersji, aby uniknąć potencjalnych problemów z bezpieczeństwem.

Na przykład, jeśli aplikacja korzysta z biblioteki innej firmy, takiej jak`Newtonsoft.Json` która posiada lukę w zabezpieczeniach, programista powinien zaktualizować ją do najnowszej wersji biblioteki, która likwiduje tę lukę.

## Use a Static Code Analyzer

Statyczny analizator kodu jest narzędziem, które może zidentyfikować potencjalne luki bezpieczeństwa w kodzie zanim zostanie on wykonany. Użyj narzędzi takich jak Visual Studio's Code`Analysis` `ReSharper` oraz`SonarQube` aby wykryć błędy bezpieczeństwa w kodzie i naprawić je przed wdrożeniem.

Na przykład, analiza kodu Visual Studio jest popularnym statycznym analizatorem kodu, który bada kod C# pod kątem potencjalnych luk bezpieczeństwa. Potrafi wykryć takie problemy jak wstrzykiwanie kodu SQL, cross-site scripting oraz użycie niebezpiecznych funkcji.

## Używaj bezpiecznych praktyk kodowania dla aplikacji internetowych

Aplikacje internetowe są podatne na kilka zagrożeń bezpieczeństwa, takich jak cross-site scripting, SQL injection i command injection. Programiści powinni stosować praktyki bezpiecznego kodowania, takie jak sprawdzanie poprawności danych wejściowych, kodowanie danych wyjściowych oraz parametryzowanie zapytań, aby zapewnić bezpieczeństwo aplikacji internetowych.

Na przykład, podczas pisania zapytań SQL, używaj sparametryzowanych zapytań zamiast konkatenacji danych wejściowych użytkownika z zapytaniem. Zapytania parametryzowane zapobiegają atakom SQL injection poprzez traktowanie danych wejściowych użytkownika jako danych, a nie kodu wykonywalnego.

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

Programiści powinni również zatwierdzać wszystkie dane wejściowe użytkownika, kodować dane wyjściowe i używać HTTPS do szyfrowania danych przesyłanych przez sieć.

_____

## Standardy bezpiecznego kodowania dla frameworków C#

Frameworki C# takie jak ASP.NET i .NET Core mają swoje standardy bezpiecznego kodowania. Deweloperzy powinni przestrzegać tych standardów podczas tworzenia aplikacji wykorzystujących te frameworki.

### ASP.NET
ASP.NET jest popularnym frameworkiem internetowym dla C#. Oto kilka standardów bezpiecznego kodowania dla ASP.NET:

- Użyj wbudowanego systemu uwierzytelniania ASP.NET zamiast tworzyć niestandardowy system uwierzytelniania. Na przykład, można użyć wbudowanego w ASP.NET.`Identity` system do zarządzania uwierzytelnianiem i autoryzacją użytkowników.
- Użyj wbudowanych funkcji haszowania haseł ASP.NET zamiast tworzenia niestandardowych metod haszowania haseł. Na przykład, możesz użyć funkcji ASP.NET`PasswordHasher` klasa do bezpiecznego haszowania i weryfikacji haseł.
- Użyj wbudowanej w ASP.NET`AntiForgeryToken` aby zapobiec atakom cross-site request forgery (CSRF). Na przykład, możesz użyć`ValidateAntiForgeryToken` atrybut do sprawdzania poprawności tokenów anty-forgery w żądaniach POST.
- Użyj wbudowanego w ASP.NET`OutputCacheAttribute` aby zapobiec buforowaniu wrażliwych danych. Na przykład, możesz użyć opcji`OutputCacheAttribute` aby ustawić zasady buforowania dla swoich stron internetowych i zapobiec buforowaniu wrażliwych danych.

### .NET Core
.NET Core to międzyplatformowy, open-source'owy framework do budowania nowoczesnych, opartych na chmurze aplikacji. Oto kilka standardów bezpiecznego kodowania dla .NET Core:

- Użyj wbudowanego systemu uwierzytelniania .NET Core zamiast tworzyć niestandardowy system uwierzytelniania. Na przykład, możesz użyć .NET Core's`Identity` System do zarządzania uwierzytelnianiem i autoryzacją użytkowników.
- Użyj wbudowanych funkcji haszowania hasła .NET Core zamiast tworzyć niestandardowe metody haszowania hasła. Na przykład, możesz użyć .NET Core's`PasswordHasher` klasa do bezpiecznego haszowania i weryfikacji haseł.
- Użyj wbudowanego interfejsu API ochrony danych .NET Core, aby chronić wrażliwe dane, takie jak ciągi połączeń i sekrety. Na przykład, możesz użyć`DataProtectionProvider` Klasa do ochrony wrażliwych danych za pomocą klucza.
- Użyj wbudowanych kontroli zdrowia .NET Core, aby monitorować zdrowie swojej aplikacji. Na przykład, możesz użyć`HealthCheck` middleware do okresowego sprawdzania stanu aplikacji i ostrzegania o wszelkich problemach.


## Wnioski
Standardy bezpiecznego kodowania są niezbędne do zapewnienia, że kod jest bezpieczny, niezawodny i wolny od podatności. C# jest popularnym językiem programowania, który wymaga od programistów przestrzegania standardów bezpiecznego kodowania, aby zapobiec zagrożeniom bezpieczeństwa. Poprzez stosowanie najlepszych praktyk, takich jak sprawdzanie poprawności danych wejściowych, unikanie niebezpiecznych funkcji, używanie bibliotek kryptograficznych oraz utrzymywanie bibliotek i frameworków w stanie aktualnym, programiści mogą zapewnić, że ich kod jest bezpieczny i wolny od luk. Podczas używania frameworków C#, programiści powinni przestrzegać standardów bezpiecznego kodowania zalecanych przez dany framework.

Przyjmowanie standardów bezpiecznego kodowania jest procesem ciągłym, który wymaga od programistów bycia na bieżąco z najnowszymi najlepszymi praktykami i narzędziami bezpieczeństwa. Poprzez włączenie standardów bezpiecznego kodowania do procesu rozwoju, programiści mogą zminimalizować ryzyko naruszenia bezpieczeństwa i chronić wrażliwe dane.

Aby rozpocząć bezpieczne kodowanie w C#, programiści mogą zacząć od zapoznania się z najlepszymi praktykami omówionymi w tym artykule. Powinni zidentyfikować obszary w swoim kodzie, które są podatne na zagrożenia bezpieczeństwa, takie jak sprawdzanie poprawności danych wejściowych, haszowanie haseł i zarządzanie sesjami. Następnie mogą wdrożyć najlepsze praktyki, takie jak te omówione w tym artykule, aby zabezpieczyć swój kod.

Programiści powinni również być na bieżąco z najnowszymi trendami i praktykami bezpieczeństwa, śledząc blogi poświęcone bezpieczeństwu, uczestnicząc w konferencjach i biorąc udział w społecznościach internetowych. Będąc na bieżąco, mogą utrzymać swój kod bezpieczny i wolny od luk.

Wreszcie, programiści powinni promować kulturę świadomości bezpieczeństwa poprzez dzielenie się najlepszymi praktykami ze swoim zespołem lub kolegami. Powinni organizować sesje szkoleniowe dotyczące bezpieczeństwa, dzielić się artykułami i zasobami na temat bezpiecznych praktyk kodowania oraz dawać przykład poprzez wdrażanie tych najlepszych praktyk w swoim własnym kodzie. Promując kulturę świadomości bezpieczeństwa, mogą pomóc w zapewnieniu, że kod ich zespołu jest bezpieczny i wolny od luk.

Stosując te najlepsze praktyki, programiści mogą zapewnić, że ich kod C# jest bezpieczny i niezawodny, a także mogą pomóc w zapobieganiu naruszeniom bezpieczeństwa i chronić wrażliwe dane.

## Referencje

Oto kilka przydatnych zasobów, aby dowiedzieć się więcej o praktykach bezpiecznego kodowania w C#:

-[Microsoft's Secure Coding Guidelines for C# and .NET](https://learn.microsoft.com/en-us/dotnet/standard/security/secure-coding-guidelines)
-[OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
-[NIST's Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf)
-[CIS Microsoft .NET Framework 4.5 Benchmark](https://www.cisecurity.org/benchmark/microsoft_net_framework_4-5_benchmark/)
-[Security Code Scan - .NET Security Guard](https://security-code-scan.github.io/#NET-Security-Guard)

Śledząc te zasoby, programiści mogą dowiedzieć się więcej o praktykach bezpiecznego kodowania w C# i o tym, jak wdrożyć je w swoich projektach.

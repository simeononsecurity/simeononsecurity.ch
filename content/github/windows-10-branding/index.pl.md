---
title: "Automatyzacja marki dla systemów Windows - łatwe sterowanie pulpitem, ekranem blokady i nie tylko"
date: 2020-08-14
---


Wiele organizacji ma potrzebę lub chce kontrolować branding systemu Windows.
Obejmuje to tapetę pulpitu, awatar użytkownika, ekran blokady systemu Windows, a czasami logo OEM.
W Windows 10, Windows Server 2016 i Windows Server 2019 nie jest to szczególnie łatwe.
Ale z pomocą podlinkowanego skryptu możemy to częściowo zautomatyzować i znacznie ułatwić ten proces.

## Pobierz wymagane pliki

**Pobierz wymagane pliki ze strony.[GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)

## Jak skonfigurować pliki brandingowe

- X] Zastąp wszystkie obrazy swoimi obrazami brandingowymi
  - X] Logo OEM musi być albo 95x95 lub 120x20 i w formacie ".bmp".
  - X] Wygeneruj obrazek użytkownika wraz z wariantami 32x32, 40x40, 48x48, 192x192.
  - X] Wygeneruj lub skopiuj obraz użytkownika dla obrazu gościa.

## Jak uruchomić skrypt
```
.\sos-copybranding.ps1
```

## Ten skrypt wykorzystuje następujące narzędzie:

-[Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

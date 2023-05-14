---
title: "Wydajne skanowanie wirusów dzięki modułom VirusTotal PowerShell"
date: 2020-11-24
toc: true
draft: false
description: "Wykonuj wydajne skanowanie wirusów za pomocą VirusTotal PowerShell Modules poprzez automatyzację interakcji z VirusTotal API i usprawnienie przepływu pracy w zakresie bezpieczeństwa."
tags: ["Moduły PowerShell", "PowerShell", "Automatyka", "VirusTotal", "Skanowanie wirusów", "Skanowanie domen", "Klucz API", "VirusTotal API", "Strona programistów VirusTotal", "Administracja systemem", "Przepływ pracy w zakresie bezpieczeństwa", "Skuteczne skanowanie wirusów", "Pobierz i zainstaluj", "Repozytorium GitHub", "Przykłady użycia API"]
---
 kolekcja modułów PowerShell do interakcji z VirusTotal API

**Notatki:**
- Potrzebny będzie klucz API VirusTotal, który można znaleźć na stronie[Shodan Account](https://www.virustotal.com/gui/)
- Przykłady API używanych w modułach można znaleźć na stronie[VirusTotal Developers Page](https://developers.virustotal.com/reference#getting-started)

## Pobierz i zainstaluj
- Pobierz moduły z[GitHub Repository](https://github.com/simeononsecurity/VirusTotal-PS)
- Zainstaluj wszystkie moduły
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```
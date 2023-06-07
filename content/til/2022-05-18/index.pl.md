---
title: "Dziś dowiedziałem się więcej o tworzeniu i wdrażaniu zasad WDAC"
date: 2022-05-18
toc: true
draft: false
description: "Dziś dowiedziałem się więcej o warunkach Ansible i zarządzaniu zmiennymi"
genre: ["Automatyzacja", "Bezpieczeństwo systemu Windows", "Kontrola aplikacji", "Windows Defender", "WDAC", "Powershell", "Ochrona przed zagrożeniami", "Windows Server 2019", "Bezpieczeństwo przedsiębiorstwa", "Zarządzanie polityką", "Najlepsze praktyki w zakresie bezpieczeństwa"]
tags: ["automatyzacja", "WDAC", "kontrola aplikacji", "Kontrola aplikacji Windows Defender", "Windows Defender", "Powershell", "Dokumentacja Microsoft", "Tworzenie polityki WDAC", "wdrażanie polityki", "Wdrażanie oparte na skryptach", "wiele polityk WDAC", "urządzenia o stałym obciążeniu", "zaufane aplikacje", "deny policies", "praktyki bezpieczeństwa", "zarządzanie polityką", "bezpieczeństwo przedsiębiorstwa", "ochrona przed zagrożeniami", "Windows Server", "Bezpieczeństwo systemu Windows", "biała lista aplikacji"]
---

**O czym SimeonOnSecurity dowiedział się dzisiaj i co uznał za interesujące**

Dziś SimeonOnSecurity zaktualizował swoje repozytorium Windows-Defender-Application-Control-Hardening i dowiedział się o Windows Defender Application Control (WDAC), funkcji Windows 10 Enterprise i Windows Server 2019, która zapewnia bezpieczeństwo poprzez kontrolowanie tego, co jest wykonywane na urządzeniu.

SimeonOnSecurity zagłębił się w dokumentację Microsoft dotyczącą WDAC i odkrył kilka kluczowych zasobów do tworzenia i wdrażania zasad. Dowiedział się, jak utworzyć zasady WDAC dla urządzeń o stałym obciążeniu przy użyciu komputera referencyjnego, jak wdrożyć zasady WDAC za pomocą skryptu i jak używać wielu zasad dla różnych scenariuszy.

Ponadto SimeonOnSecurity uzyskał wgląd w wytyczne dotyczące tworzenia polityk WDAC odmowy, co pozwoliło mu lepiej zrozumieć koncepcję zezwalania na uruchamianie tylko zaufanych aplikacji na urządzeniu, jednocześnie odmawiając wszystkim innym.

Ogólnie rzecz biorąc, eksploracja Windows Defender Application Control przez SimeonOnSecurity jeszcze bardziej ugruntowała jego zrozumienie znaczenia kontroli aplikacji w nowoczesnych praktykach bezpieczeństwa.

## Zaktualizowano repozytoria:
- [simeononsecurity/Windows-Defender-Application-Control-Hardening](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening)

## Odczyt WDAC:
- [Microsoft - Create a WDAC policy for fixed-workload devices using a reference computer](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Deploy WDAC policies using script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Guidance on Creating WDAC Deny Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Use multiple Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

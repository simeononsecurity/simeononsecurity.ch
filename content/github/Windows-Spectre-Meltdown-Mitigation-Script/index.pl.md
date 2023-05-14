---
title: "Ochrona systemu Windows przed atakami typu Speculative Execution Side-Channel."
date: 2020-06-18
toc: true
draft: false
description: "Dowiedz się, jak zabezpieczyć system Windows przed atakami typu speculative execution side-channel za pomocą skryptu łagodzącego Microsoftu i aktualizacji oprogramowania sprzętowego"
tags: ["Windows Spectre Meltdown Mitigation Script", "Ataki typu Speculative Execution Side-Channel", "Microsoft", "Intel", "AMD", "VIA", "ARM", "Android", "Chrome", "iOS", "macOS", "Branch Target Injection", "Kontrola granic Obejście", "Rogue Data Cache Load", "Obejście sklepu spekulacyjnego", "Mikroarchitektoniczne próbkowanie danych", "CVEs", "Aktualizacje oprogramowania sprzętowego", "Repozytorium GitHub", "PowerShell"]
---
 https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in
**Prosty skrypt do implementacji zabezpieczeń przed lukami w kanale bocznym speculative execution w systemach Windows.**

Firma Microsoft jest świadoma istnienia nowej, publicznie ujawnionej klasy błędów, które nazywane są "spekulacyjnymi atakami kanałowymi" i które dotyczą wielu nowoczesnych procesorów, w tym Intel, AMD, VIA i ARM.

**Uwaga:** Ten problem dotyczy również innych systemów operacyjnych, takich jak Android, Chrome, iOS i macOS. Dlatego radzimy klientom, aby szukali wskazówek u tych dostawców.

Wydaliśmy kilka aktualizacji, które pomagają złagodzić te luki. Podjęliśmy również działania mające na celu zabezpieczenie naszych usług w chmurze. Więcej szczegółów można znaleźć w poniższych sekcjach.

Nie otrzymaliśmy jeszcze żadnych informacji wskazujących na to, że te luki zostały wykorzystane do zaatakowania klientów. Ściśle współpracujemy z partnerami branżowymi, w tym producentami układów scalonych, producentami sprzętu i sprzedawcami aplikacji, aby chronić klientów. Aby uzyskać wszystkie dostępne zabezpieczenia, konieczne są aktualizacje oprogramowania (mikrokodu). Obejmuje to mikrokod pochodzący od producentów OEM urządzeń oraz, w niektórych przypadkach, aktualizacje oprogramowania antywirusowego.

**Ten artykuł dotyczy następujących podatności:**.
- CVE-2017-5715 - "Branch Target Injection"
- CVE-2017-5753 - "Bounds Check Bypass"
- CVE-2017-5754 - "Rogue Data Cache Load"
- CVE-2018-3639 - "Speculative Store Bypass"
- CVE-2018-11091 - "Microarchitectural Data Sampling Uncacheable Memory (MDSUM)"
- CVE-2018-12126 - "Microarchitectural Store Buffer Data Sampling (MSBDS)"
- CVE-2018-12127 - "Microarchitectural Fill Buffer Data Sampling (MFBDS)"
- CVE-2018-12130 - "Microarchitectural Load Port Data Sampling (MLPDS)"

**UPDATED ON AUGUST 6, 2019** 6 sierpnia 2019 roku Intel opublikował szczegóły dotyczące luki ujawniającej informacje o jądrze systemu Windows. Luka ta jest wariantem luki Spectre Variant 1 speculative execution side channel i została przypisana CVE-2019-1125.

**UPDATED ON NOVEMBER 12, 2019** On November 12, 2019, Intel published a technical advisory around Intel® Transactional Synchronization Extensions (Intel® TSX) Transaction Asynchronous Abort vulnerability that is assigned CVE-2019-11135. Firma Microsoft wydała aktualizacje, które pomagają złagodzić tę lukę, a zabezpieczenia systemu operacyjnego są domyślnie włączone dla wersji klienckich systemu operacyjnego Windows.

## Zalecane działania
Klienci powinni podjąć następujące działania, aby pomóc w ochronie przed podatnościami:

- Zastosuj wszystkie dostępne aktualizacje systemu operacyjnego Windows, w tym comiesięczne aktualizacje zabezpieczeń Windows.
- Zastosować odpowiednią aktualizację oprogramowania sprzętowego (mikrokodu), która jest dostarczana przez producenta urządzenia.
- Ocenić ryzyko dla swojego środowiska w oparciu o informacje, które są podane w Microsoft Security Advisories: ADV180002, ADV180012, ADV190013 oraz informacji zawartych w tym artykule Bazy Wiedzy.
- Podejmij działania zgodnie z wymaganiami, korzystając z poradników i informacji o kluczach rejestru zawartych w tym artykule Bazy wiedzy.

## Pobierz wymagane pliki:

Pobierz wymagane pliki ze strony.[GitHub Repository](https://github.com/simeononsecurity/Windows-Spectre-Meltdown-Mitigation-Script)

## Jak uruchomić skrypt:

**Skrypt może być lauched z wyodrębnionego GitHub downloadu w ten sposób:**.
```
.\sos-spectre-meltdown-mitigations.ps1
```

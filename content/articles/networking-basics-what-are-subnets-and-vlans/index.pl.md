---
title: "Podstawy sieci: podsieci, podział na podsieci i projekt VLAN"
draft: false
toc: true
date: 2023-07-23
lastmod: 2026-11-13
description: "Poznaj podstawy podsieci, podziału na podsieci i VLAN-ów, aby sprawniej zarządzać siecią i lepiej ją zabezpieczać."
genre: ["Podstawy sieci", "Podział na podsieci", "VLAN-y", "Zarządzanie siecią", "Bezpieczeństwo sieci", "Adresacja IP", "Segmentacja sieci", "Efektywne wykorzystanie zasobów", "Wydajność sieci", "IPv4"]
tags: ["podstawy sieci", "podsieci", "podział na podsieci", "VLAN-y", "zarządzanie siecią", "bezpieczeństwo sieci", "adresacja IP", "segmentacja sieci", "efektywne wykorzystanie zasobów", "wydajność sieci", "IPv4", "konfiguracja podsieci", "maski podsieci", "przydzielanie adresów IP", "komunikacja między VLAN-ami", "porty przełącznika", "konfiguracja VLAN", "interfejsy VLAN", "łączność sieciowa", "sieci podrzędne", "domeny rozgłoszeniowe", "zabezpieczenia", "zakres adresów IP", "przykłady podsieci", "wdrażanie VLAN", "administracja siecią", "konfiguracja przełącznika", "konfiguracja routera", "skalowalność sieci", "komunikacja i przesyłanie danych", "wydajne sieci"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_comp.webp"
coverAlt: "Symboliczna ilustracja połączonych sieci komputerowych z podsieciami i VLAN-ami"
coverCaption: "Budowanie wydajnych sieci: podsieci i VLAN-y w prostym ujęciu."
---

## Podstawy sieci: podsieci, podział na podsieci i projekt VLAN

### Wprowadzenie

We współczesnym połączonym świecie sieci komputerowe odgrywają kluczową rolę w komunikacji i przesyłaniu danych. Podstawy sieci są przydatne specjalistom IT i zwykłym użytkownikom. W tym artykule poznasz podsieci, podział na podsieci oraz VLAN-y, a także ich cel i działanie.

## Podsieci: dokładniejsze omówienie

### Czym jest podsieć?

{{< youtube id="nR5xCmXJE5E" >}}

**Podsieć** to logiczny podział sieci IP. Pozwala administratorowi podzielić dużą sieć na mniejsze, łatwiejsze w zarządzaniu segmenty. Każda podsieć ma własny zakres adresów IP, co pomaga efektywnie wykorzystywać dostępne adresy.

### Po co używać podsieci?

Podsieci stosuje się w sieciach komputerowych z kilku powodów:

1. **Segmentacja sieci:** Podsieci dzielą dużą sieć na mniejsze sieci. Poprawia to wydajność i ogranicza przeciążenie.

2. **Lepsze bezpieczeństwo:** Umieszczenie urządzeń w osobnych podsieciach pozwala administratorom stosować zapory i listy kontroli dostępu do zarządzania ruchem i poprawy bezpieczeństwa.

3. **Efektywne wykorzystanie zasobów:** Podział na podsieci ułatwia przydzielanie adresów IP. Adresy IPv4 są zasobem ograniczonym.

### Jak podzielić sieć na podsieci?

{{< youtube id="LdSAaSHfK3M" >}}

Podział na podsieci polega na rozbiciu sieci na mniejsze podsieci. Wykonaj te kroki:

1. **Określ wymagania sieci:** Ustal liczbę potrzebnych podsieci i hostów w każdej z nich.

2. **Wybierz schemat adresacji IP:** Dobierz schemat do wymaganej liczby podsieci i hostów.

3. **Oblicz maski podsieci:** Wyznacz maski na podstawie liczby wymaganych podsieci i hostów.

4. **Przydziel adresy IP:** Przydziel adresy każdej podsieci i upewnij się, że mieszczą się w odpowiednim zakresie.

5. **Przetestuj i zweryfikuj:** Sprawdź łączność sieciową i przydziały adresów IP.

### Przykłady podziału na podsieci

Rozważmy prosty przykład podziału na podsieci:

Załóżmy, że mamy zakres adresów IP 192.168.0.0/24 i chcemy utworzyć cztery podsieci o równej liczbie hostów. Możemy podzielić tę sieć tak:

1. **Krok 1: Określ wymagania sieci:** Potrzebujemy czterech podsieci z równą liczbą hostów.

2. **Krok 2: Wybierz schemat adresacji IP:** Wybieramy maskę /26, która pozwala uzyskać 64 adresy w każdej podsieci.

3. **Krok 3: Oblicz maski podsieci:** Maska /26 ma postać 255.255.255.192.

4. **Krok 4: Przydziel adresy IP:** Przydzielamy podsieci następujące adresy:

   - podsieć 1: 192.168.0.0/26
   - podsieć 2: 192.168.0.64/26
   - podsieć 3: 192.168.0.128/26
   - podsieć 4: 192.168.0.192/26

5. **Krok 5: Przetestuj i zweryfikuj:** Sprawdzamy łączność między urządzeniami w każdej podsieci.

### Przydatne tabele podziału na podsieci

#### Tabela obliczeń podsieci

| Maska podsieci | Notacja CIDR | Łączna liczba adresów IP | Dostępne adresy IP |
|-------------|---------------|--------------------|---------------------|
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1,024 | 1,022 |
| /21 | 255.255.248.0 | 2,048 | 2,046 |
| /20 | 255.255.240.0 | 4,096 | 4,094 |
| /19 | 255.255.224.0 | 8,192 | 8,190 |
| /18 | 255.255.192.0 | 16,384 | 16,382 |
| /17 | 255.255.128.0 | 32,768 | 32,766 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /15 | 255.254.0.0 | 131,072 | 131,070 |
| /14 | 255.252.0.0 | 262,144 | 262,142 |
| /13 | 255.248.0.0 | 524,288 | 524,286 |
| /12 | 255.240.0.0 | 1,048,576 | 1,048,574 |
| /11 | 255.224.0.0 | 2,097,152 | 2,097,150 |
| /10 | 255.192.0.0 | 4,194,304 | 4,194,302 |
| /9 | 255.128.0.0 | 8,388,608 | 8,388,606 |
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
| /7 | 254.0.0.0 | 33,554,432 | 33,554,430 |
| /6 | 252.0.0.0 | 67,108,864 | 67,108,862 |
| /5 | 248.0.0.0 | 134,217,728 | 134,217,726 |
| /4 | 240.0.0.0 | 268,435,456 | 268,435,454 |
| /3 | 224.0.0.0 | 536,870,912 | 536,870,910 |
| /2 | 192.0.0.0 | 1,073,741,824 | 1,073,741,822 |
| /1 | 128.0.0.0 | 2,147,483,648 | 2,147,483,646 |
| /0 | 0.0.0.0 | 4,294,967,296 | 4,294,967,294 |

#### Tabela dostępnych podsieci

| Notacja CIDR | Liczba dostępnych podsieci |
|---------------|-------------------------|
| /0 | 1 |
| /1 | 2 |
| /2 | 4 |
| /3 | 8 |
| /4 | 16 |
| /5 | 32 |
| /6 | 64 |
| /7 | 128 |
| /8 | 256 |
| /9 | 512 |
| /10 | 1024 |
| /11 | 2048 |
| /12 | 4096 |
| /13 | 8192 |
| /14 | 16384 |
| /15 | 32768 |
| /16 | 65536 |
| /17 | 131072 |
| /18 | 262144 |
| /19 | 524288 |
| /20 | 1048576 |
| /21 | 2097152 |
| /22 | 4194304 |
| /23 | 8388608 |
| /24 | 16777216 |
| /25 | 33554432 |
| /26 | 67108864 |
| /27 | 134217728 |
| /28 | 268435456 |
| /29 | 536870912 |
| /30 | 1073741824 |
| /31 | 2147483648 |
| /32 | 4294967296 |

#### Tabela potęg liczby dwa

| Potęga liczby dwa | Wartość |
|--------------|-------|
| 2^32 | 4294967296 |
| 2^31 | 2147483648 |
| 2^30 | 1073741824 |
| 2^29 | 536870912 |
| 2^28 | 268435456 |
| 2^27 | 134217728 |
| 2^26 | 67108864 |
| 2^25 | 33554432 |
| 2^24 | 16777216 |
| 2^23 | 8388608 |
| 2^22 | 4194304 |
| 2^21 | 2097152 |
| 2^20 | 1048576 |
| 2^19 | 524288 |
| 2^18 | 262144 |
| 2^17 | 131072 |
| 2^16 | 65536 |
| 2^15 | 32768 |
| 2^14 | 16384 |
| 2^13 | 8192 |
| 2^12 | 4096 |
| 2^11 | 2048 |
| 2^10 | 1024 |
| 2^9 | 512 |
| 2^8 | 256 |
| 2^7 | 128 |
| 2^6 | 64 |
| 2^5 | 32 |
| 2^4 | 16 |
| 2^3 | 8 |
| 2^2 | 4 |
| 2^1 | 2 |
| 2^0 | 1 |

## VLAN-y: wirtualne sieci lokalne

### Czym jest VLAN?

{{< youtube id="jC6MJTh9fRE" >}}

**VLAN (Virtual Local Area Network)** to logiczna grupa urządzeń w sieci, niezależna od ich fizycznego położenia. VLAN-y zwiększają elastyczność, bezpieczeństwo i skalowalność, tworząc oddzielne domeny rozgłoszeniowe.

### Po co używać VLAN-ów?

VLAN-y przynoszą kilka korzyści w zarządzaniu siecią:

1. **Lepsze bezpieczeństwo:** VLAN-y izolują wrażliwe dane i ograniczają nieautoryzowany dostęp. Ruch pozostaje w wyznaczonych segmentach, co chroni ważne zasoby.

2. **Wyższa wydajność:** VLAN-y logicznie rozdzielają ruch, ograniczają przeciążenie i poprawiają wydajność. Ruch rozgłoszeniowy pozostaje w VLAN-ie, ograniczając zbędne transmisje.

3. **Prostsze zarządzanie siecią:** VLAN-y grupują urządzenia według funkcji, działu lub innego kryterium, upraszczając administrację i konfigurację.

### Konfiguracja VLAN

Konfiguracja VLAN zwykle obejmuje te kroki:

1. **Określ wymagania VLAN:** Ustal cel i zakres wdrożenia. Wskaż urządzenia i przypisanie ich do VLAN-ów.

2. **Przydziel identyfikatory VLAN:** Nadaj każdemu VLAN-owi unikatowy identyfikator. Zwykle są to numery od 1 do 4094, a niektóre są zarezerwowane.

3. **Skonfiguruj porty przełącznika:** Przypisz porty do odpowiednich VLAN-ów jako porty dostępowe lub trunk.

4. **Skonfiguruj interfejsy VLAN:** Jeśli komunikacja między VLAN-ami jest potrzebna, [skonfiguruj interfejsy VLAN](https://simeononsecurity.com/network-plus/ethernet-switching-vlans-port-configurations-security/), na przełączniku warstwy 3 lub routerze.

5. **Przetestuj i zweryfikuj:** Sprawdź łączność urządzeń w obrębie każdego VLAN-u.

### Tabela zarezerwowanych VLAN-ów

| Znaczniki VLAN | Opis |
|-------------------|----------------------------------------------------|
| VLAN 0 | Zarezerwowany identyfikator VLAN, nie używać |
| VLAN 1 | Domyślny VLAN wielu urządzeń sieciowych |
| VLAN 2 | Domyślny VLAN dla ruchu zarządzającego |
| VLAN 3-4 | Zarezerwowane identyfikatory VLAN |
| VLAN 5 | Zarezerwowany dla identyfikatora VLAN Token Ring |
| VLAN 6-1001 | Zarezerwowane identyfikatory VLAN |
| VLAN 1002-1005 | Domyślne VLAN-y Cisco do określonych celów |
| VLAN 1006-1024 | Zarezerwowane identyfikatory VLAN |
| VLAN 1025-4094 | Zarezerwowane dla rozszerzonego zakresu VLAN |
| VLAN 4095 | Zarezerwowany identyfikator VLAN, nie używać |

## Podsumowanie

[Znajomość podsieci](https://simeononsecurity.com/articles/networking-basics-what-is-a-switch-router-gateway-subnet-firewall-and-dmz/) i VLAN-ów jest ważna przy projektowaniu i zarządzaniu wydajnymi sieciami komputerowymi. Podsieci segmentują sieć, poprawiając wydajność i bezpieczeństwo. VLAN-y logicznie grupują urządzenia, zwiększając elastyczność i ułatwiając zarządzanie. Wykonując opisane kroki, administratorzy mogą dzielić sieci na podsieci i konfigurować VLAN-y zgodnie z potrzebami.

Podstawy sieci stanowią fundament solidnych, skalowalnych sieci, które odpowiadają na potrzeby współczesnej komunikacji i przesyłania danych.

## Źródła

- [Podstawy podziału na podsieci](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
- [Zrozumienie i konfiguracja VLAN](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/12-2/25ew/configuration/guide/conf/vlans.pdf)
- [Standard IEEE 802.1Q](https://standards.ieee.org/standard/802_1Q-2018.html)

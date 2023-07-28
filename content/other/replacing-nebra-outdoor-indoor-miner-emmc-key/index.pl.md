---
title: "Wymiana karty SD Nebra Helium Miner: Przewodnik krok po kroku"
draft: false
toc: true
date: 2022-02-13
description: "Z tego przewodnika dowiesz się, jak wymienić lub przeflashować kartę SD Nebra Indoor i Outdoor, pierwszej i drugiej generacji, EMMC Key oraz naprawić problemy z synchronizacją Helium Miner."
genre: ["Technologia", "Kryptowaluta", "Sprzęt", "Wydobycie helu", "Rozwiązywanie problemów", "Wymiana karty SD", "Problemy z synchronizacją", "Raspberry Pi", "Balena Etcher", "Nebra Helium Miner"]
tags: ["Nebra Helium Miner", "Wymiana karty SD", "Problemy z synchronizacją", "Wydobycie helu", "Rozwiązywanie problemów", "Raspberry Pi", "Balena Etcher", "Przewodnik po sprzęcie", "Aktualizacja karty SD", "Rozwiązywanie problemów z synchronizacją", "Przewodnik krok po kroku", "Poprawka synchronizacji Helium Miner", "Nebra Indoor Miner", "Nebra Outdoor Miner", "Raspberry Pi Compute Module 3", "Balena Raspberry Pi CM3 Image", "Rozwiązywanie problemów z górnikami helowymi", "Sprzęt górniczy Nebra", "Balena Etcher Software", "Wymiana klucza EMMC w Nebra Miner", "Naprawa kart SD dla Helium Miner", "Naprawianie problemów z synchronizacją Helium Miner", "Wymiana karty SD Nebra Miner", "Przewodnik po rozwiązywaniu problemów z Nebra Helium Miner", "Wskazówki dotyczące wydobywania helu", "Aktualizacja karty SD Nebra Helium Miner", "Jak ponownie zainfekować kartę SD Nebra Miner", "Rozwiązywanie problemów z synchronizacją Nebra Helium Miner"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_holding_a_Nebra_Helium_M.png"
coverAlt: "Kreskówkowa ilustracja przedstawiająca osobę trzymającą Nebra Helium Miner z otwartym panelem odsłaniającym gniazdo karty SD i krokami przewodnika pojawiającymi się jako przewodnik unoszący się nad urządzeniem."
coverCaption: "Z łatwością rozwiązuj problemy z synchronizacją i aktualizuj Helium Miner."
---

**Wymiana i ponowna aktualizacja klucza Nebra Indoor i Outdoor EMMC / karty SD**

Ten kompleksowy przewodnik przeprowadzi Cię przez proces wymiany lub ponownego flashowania klucza/karty SD Nebra Indoor i Outdoor EMMC. Postępując zgodnie z tymi krokami, możesz rozwiązać problemy z synchronizacją z Helium Miner i zapewnić płynne działanie. Przewodnik zawiera szczegółowe wyjaśnienie potrzebnych narzędzi i oprogramowania, a także kroki niezbędne do uzyskania pliku config.json, flashowania nowej karty SD za pomocą Balena Raspberry Pi CM3 Image i przeniesienia oryginalnego pliku konfiguracyjnego na nową kartę SD.

## Wprowadzenie

Nebra Helium Miners, zarówno model Indoor, jak i Outdoor, działają w oparciu o klucz EMMC/kartę SD. Z czasem może okazać się konieczna wymiana lub ponowne flashowanie tej karty w celu rozwiązania problemów z synchronizacją i utrzymania optymalnej wydajności. Niniejszy przewodnik dostarczy ci wiedzy i instrukcji wymaganych do skutecznego wykonania tego zadania.

Aby z powodzeniem wymienić kartę SD Nebra Helium Miner, potrzebne będą specjalne narzędzia i oprogramowanie. Narzędzia te obejmują śrubokręt krzyżakowy lub [Allen Key Set](https://amzn.to/34SlnOS) (depending on the model), a [Micro SD Card Reader](https://amzn.to/3Jl3U0w), a [64GB A2 micro SD card](https://amzn.to/3oJtTqs) (or larger), and a [Micro USB 2.0 Cable](https://amzn.to/3LxXYmA). The essential software needed for this process includes [Balena Etcher](https://www.balena.io/etcher/), Balena Raspberry Pi Image, and [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) Mając te zasoby pod ręką, będziesz gotowy do wymiany lub ponownego flashowania karty SD.

## Wymagane narzędzia:
- Śrubokręt krzyżakowy lub [plastic pry bar](https://amzn.to/3rLXVfc) for the Nebra Indoor Miner or [allen key set](https://amzn.to/34SlnOS) dla Nebra Outdoor Miner
- Mocne paznokcie, pęseta lub szczypce do wyjmowania starych kart SD
- [A Micro SD Card Reader](https://amzn.to/3Jl3U0w)
- [A 64gb (or larger) A2 micro sd card](https://amzn.to/3oJtTqs)
- [A Micro USB 2.0 Cable](https://amzn.to/3LxXYmA)
## Wymagane oprogramowanie:
- [Balena Etcher](https://www.balena.io/etcher/)
- [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)
- Najnowszy obraz Nebra dla konkretnego urządzenia:
*Jeśli nie wiesz, jakie masz urządzenie, zapoznaj się z sekcją [nebra documentatio](https://support.nebra.com/support/home) Jeśli jest starszy, można bezpiecznie założyć, że masz urządzenie pierwszej generacji.
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)

## Wewnątrz Nebra Helium Miners:
### Zawartość Nebra Indoor Miner:
{{< figure src="Indoor-internal-lights.png" alt="Nebra Indoor Miner" >}}
### Zawartość Nebra Outdoor Miner:
{{< figure src="Inside-Interfaces.jpg" alt="Nebra Outdoor Miner" >}}
 - 1.) 9-16V @ 15W DC 6.5MMx2.0MM Barrel Jack
 - 2.) Złącze Ethernet
 - 3.) Wskaźnik LED
 - 4.) Przycisk interfejsu
 - 5.) Złącze modułu 4G / LTE
 - 6.) Gniazdo karty SIM

## Jak wymienić kartę SD
### Krok 1: Opcjonalnie pobierz plik config.json z klucza EMMC:
- Pobierz i zainstaluj [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) Będzie to potrzebne do uruchomienia modułu obliczeniowego jako systemu plików USB.
- Zidentyfikuj i dostosuj piny zworek na płycie głównej CM3 do trybu programowania
 - {{< figure src="daughterboardBreakdown.png" alt="Nebra Daughterboard Overview" >}}
   - 5.) Port Micro USB używany do obrazowania
   - 7.) Zworka JP4 USB - Służy do przełączania między trybem normalnej pracy a trybem flash, upewnij się, że znajduje się w pozycji 1-2 dla normalnej pracy i 2-3 dla programowania.
   - 8.) Zworka zasilania JP3 - umożliwia zasilanie modułu ze złącza Micro USB. Podłączaj tylko podczas programowania z komputera i upewnij się, że płyta główna nie jest podłączona.
 - Przesuń zworkę JP4 do pozycji 2+3
 - Podłącz kabel USB i uruchom [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) narzędzie
 - Otwórz eksplorator plików, a zobaczysz dysk o nazwie "resin-boot". Pobierz plik "config.json" z katalogu, który może być potrzebny później i powinien być zarchiwizowany.
 - Odłącz kabel USB i zresetuj zworkę JP4 do pozycji 1+2
### Krok 2: Wgraj nową kartę SD z obrazem Balena Raspberry Pi CM3:
- Pobierz i rozpakuj odpowiedni obraz
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)
- Korzystanie z [Balena Etcher](https://www.balena.io/etcher/) wybierz ostatnio wyodrębniony plik .img i nową kartę microsd jako urządzenie docelowe.
- Wybierz Flash
### Krok 3: Zainstaluj nową kartę SD i ponownie zmontuj Nebra Miner:
 - Zainstaluj kartę SD w gnieździe, w którym wcześniej znajdował się klucz EMMC.
 - Ponownie zmontuj górnika
 - Po pierwszym włączeniu nowo sflashowanego Nebra Miner, podłącz go do sieci ethernet na 20-30 minut przed ponownym skonfigurowaniem połączeń wifi.
### Krok 4: Zysk?





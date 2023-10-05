---
title: "Uruchomienie pfSense na cienkim kliencie HP t740: Wskazówki i przewodnik rozwiązywania problemów"
draft: false
toc: true
date: 2023-04-29
description: "Dowiedz się, jak skonfigurować pfSense na cienkim kliencie HP t740 i jak rozwiązywać potencjalne problemy, takie jak zamrażanie i problemy z wykrywaniem dysków SSD."
tags: ["pfSense", "OPNsense", "HardenedBSD", "HP t740", "cienki klient", "serwer domowy", "PPPoE", "FreeBSD", "zachęta do uruchomienia systemu", "loader.conf.local", "nano edytor", "Wykrywanie dysków SSD", "M.2 SSD", "Western Digital", "rozwiązywanie problemów", "poinstalacyjne", "UART", "ESXi", "Proxmox"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "Kreskówka z czarodziejem rzucającym zaklęcie, aby naprawić zamrożony komputer, z dymkiem mówiącym o rozwiązaniu problemu"
coverCaption: ""
canonical: "https://simeononsecurity.ch/guides/installing-pfsense-on-hp-t740-thin-client/"
---
 pfSense, OPNsense lub HardenedBSD na HP t740 Thin Client**.

Jeśli szukasz wydajnego urządzenia do uruchomienia pfSense, OPNsense lub HardenedBSD, HP t740 Thin Client może być dla Ciebie odpowiednim wyborem.

## Większa moc i kompaktowy serwer domowy

HP t740 Thin Client jest kompaktowym urządzeniem, które może być używane jako wydajna skrzynka pfSense lub kompaktowy serwer domowy. Oferuje więcej mocy niż t730 lub t620 Plus, co czyni go odpowiednim wyborem do uruchomienia PPPoE, zwłaszcza jeśli masz internet Fiber. Może również oferować ścieżkę rozbudowy do sieci 10 Gigabit.

## PS/2 Freezes

Jeśli jednak planujesz uruchomić FreeBSD lub jego pochodne, takie jak pfSense, OPNsense lub HardenedBSD na gołym metalu (w przeciwieństwie do ESXi lub Proxmox), możesz napotkać problem, w którym system zamarza przy starcie z komunikatem`atkbd0: [GIANT-LOCKED]` Na szczęście problem ten można rozwiązać, wpisując następujące polecenia w znaku startowym:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

*Zauważ, że musisz wyłączyć oba, w przeciwnym razie, nadal będzie blokować się przy rozruchu.*

Po zainstalowaniu systemu operacyjnego, otwórz powłokę poinstalacyjną i uruchom następujące polecenie:

```bash
vi /boot/loader.conf.local
```
Następnie dodaj te dwie linie:
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### Utrwalanie zmian za pomocą VI
Dla tych, którzy nie są zaznajomieni z vi, możesz dodać linię, wykonując następujące czynności :

Dodanie linii`hint.uart.0.disabled="1"` oraz`hint.uart.1.disabled="1"` do`/boot/loader.conf.local` plik za pomocą edytora vi można wykonać następujące kroki:

1. Otwórz terminal w swoim systemie FreeBSD.

2. Wpisz`vi /boot/loader.conf.local` i naciśnij Enter, aby otworzyć plik w edytorze vi.

3. Naciśnij przycisk`i` aby wejść w tryb wstawiania.

4. Przesuń kursor do dolnej części pliku za pomocą klawiszy strzałek.

5. Wpisz .`hint.uart.0.disabled="1"` bez cudzysłowu.

6. Naciśnij Enter, aby rozpocząć nową linię.

7. Wpisz`hint.uart.1.disabled="1"` bez cudzysłowu.

8. Naciśnij przycisk`Esc` aby wyjść z trybu wstawiania.

9. Wpisz`:wq` i naciśnij Enter, aby zapisać i wyjść z pliku.

Spowoduje to dodanie tych dwóch linii do`/boot/loader.conf.local` plik, który wyłączy UART i naprawi problem z zamarzaniem podczas startu na niektórych urządzeniach HP t740 "Thin Client", gdy uruchomiony jest FreeBSD lub jego pochodne, takie jak pfSense, OPNsense lub HardenedBSD.

Naprawi to problem podczas restartów i aktualizacji firmware'u w pfSense/OPNsense.

## SSD

Jeśli używasz HP M.2 eMMC, nie będzie on wykrywany podczas instalacji FreeBSD. W takim przypadku będziesz potrzebował dysku SSD M.2 innej firmy. Każdy dysk SSD M.2 może działać, SATA lub NVMe.

Jeśli szukasz dysku SSD M.2 innej firmy dla cienkiego klienta HP t740, zalecamy rozważenie[Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V) Obie te opcje są niezawodne i powinny dobrze działać z Twoim urządzeniem. Jeśli chcesz skorzystać z obu slotów, będziesz potrzebował obu. Poświęcisz prędkości NVME, ale zyskasz trochę redundancji, która jest tak ważna.

Zauważ, że autor tego artykułu z powodzeniem uruchomił pfSense CE 2.5.2 i OPNsense 22.1 na swoim t740 bez żadnych problemów po wykonaniu powyższych kroków.

## Troubleshooting and Post Install

Po instalacji, jeśli napotkasz jakiekolwiek problemy z edycją plików, możesz zainstalować edytor nano używając`pkg update` oraz`pkg install nano` Dzięki temu z łatwością będziesz mógł edytować pliki tekstowe.

Aby zapewnić, że zmiany dokonane w`/boot/loader.conf.local` zachować plik w trakcie aktualizacji wersji pfSense, należy dodać następujące linie do`/boot/loader.conf` oraz`/etc/rc.conf.local` 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

Jednak czasami edycja`/boot/loader.conf.local` plik przed ponownym uruchomieniem nie rozwiązuje problemu. W takich przypadkach może być konieczne dodanie następujących linii na początku pierwszego uruchomienia:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

Te kroki powinny rozwiązać większość problemów, które mogą pojawić się podczas i po procesie instalacji.

### Referencje:
-[HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
-[pfSense](https://www.pfsense.org/)
-[OPNsense](https://opnsense.org/)
-[HardenedBSD](https://hardenedbsd.org/)
-[ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
-[FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)
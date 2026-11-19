---
title: 'Powrót Home Assistant Core 2026.11 do wersji 2026.10.4: naprawa wersji 3 magazynu HTTP'
date: 2026-11-15
lastmod: '2026-11-18'
toc: true
draft: false
description: Napraw błąd wersji 3 magazynu HTTP po powrocie Home Assistant Core 2026.11 do wersji 2026.10.4 na Yellow. Artykuł
  zawiera zabezpieczone polecenia i zweryfikowane wyniki.
genre:
- Automatyka domowa
- Rozwiązywanie problemów
tags:
- Home Assistant Yellow
- Home Assistant OS
- Powrót Core 2026.11
- Core 2026.10.4
- Wersja 3 magazynu HTTP
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: Ilustracja żółtej płyty komputerowej, przerwanego łącza konfiguracji i przywróconego panelu internetowego
coverCaption: ''
---

Nieudana aktualizacja Home Assistant Core 2026.11 cofnęła mój Yellow CM4 do wersji 2026.10.4. Yellow nadal był dostępny w sieci, ale przestał wyświetlać panel. Po cofnięciu pozostał plik ustawień HTTP w wersji magazynu 3.1, podczas gdy Core 2026.10.4 obsługuje wersję 2.2. Zachowałem plik, przekonwertowałem jego kopię z użyciem rygorystycznych kontroli, przywróciłem dostęp HTTP, a następnie zaktualizowałem Core do wersji 2026.11.1.

<!--more-->

## Najważniejsze informacje

- **Potwierdź niezgodność.** Porównaj błąd w dzienniku Core z zainstalowanym wydaniem i wersją magazynu HTTP.
- **Zachowaj plik.** Przed odzyskiwaniem przygotuj niezmienioną kopię i kopię zapasową poza urządzeniem.
- **Sprawdź wynik.** Zweryfikuj stan Core, zapisany port nasłuchujący, panel i zainstalowaną wersję.

**Naprawa dokładnie tego przypadku:** [Zachowaj plik HTTP](#preserve-recovery-options), [utwórz i zweryfikuj kandydat na wersję 2.2](#apply-the-tested-fix-for-version-31), [zainstaluj go po zatrzymaniu Core](#apply-the-tested-fix-for-version-31) i [sprawdź wynik aktualizacji](#verify-the-update-outcome). Konwersja sprawdza oryginalne pola i zatrzymuje się, gdy się różnią. Nie stosuj jej do niesprawdzonego pliku HTTP.

## Zanim zaczniesz

Potrzebujesz fizycznego dostępu do Yellow CM4, kabla danych USB-C, działającej konsoli szeregowej oraz użytecznej kopii zapasowej lub zachowanej konfiguracji. Ręczna metoda wymaga dostępu do powłoki hosta i uważnego sprawdzenia JSON-a. Przeznacz co najmniej 30 minut na diagnozę i naprawę. Uruchomienie Core i przywracanie kopii zapasowej trwają dłużej w dużych instalacjach.

## Rozpoznaj awarię

Rozstrzygający błąd pojawił się w dzienniku Core:

```text
Storage file http has version 3 which is newer than the max supported version 2
```

Starsze wydanie Core nie mogło wczytać `http`. Przestały działać także interfejs i inne komponenty zależne od HTTP. Dzierżawa z routera i dostępna strona Observer nie potwierdzały dostępu do panelu. [Problem Home Assistant Core nr 190583](https://github.com/home-assistant/core/issues/190583) opisuje tę samą awarię po cofnięciu w kilku instalacjach, w tym na Yellow. [Mój komentarz do problemu](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) dokumentuje przetestowane odzyskiwanie tego Yellow i końcowy stan Core.

**Przyczyna awarii strony:** Core 2026.11 zapisał `.storage/http` w formacie 3.1. Cofnięcie przywróciło Core 2026.10.4, ale nie przywróciło zgodnego pliku HTTP. Core 2026.10.4 odrzuca wersję magazynu 3. Zapisany profil `intermediate_v6` na tym Yellow również nie pasuje do starszego schematu. Przyczyna niepowodzenia pierwszej aktualizacji i rozpoczęcia cofania jest nieznana. W dniu 2026-11-15 powiązany problem nadal był otwarty, a dyskusja nie zawierała poprawki potwierdzonej przez opiekunów projektu.

Przed zmianą plików sprawdź zainstalowane wydanie Core i magazyn HTTP:

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

Poniższe dane przedstawiają ten przypadek po usunięciu znaczników czasu i prywatnych informacji:

```text
2026.10.4
{
  "version": 3,
  "minor_version": 1,
  "pending_present": false,
  "profile": "intermediate_v6"
}
Storage file http has version 3 which is newer than the max supported version 2
```

Poniższe polecenia odzyskiwania porównują port nasłuchujący zapisany przez Supervisor z plikiem HTTP, nie wyświetlając żadnej z tych wartości. Jeśli się różnią, przed zmianą plików sprawdź rzeczywisty port nasłuchujący Core.

| Sygnał | Znaczenie |
| --- | --- |
| Core obsługuje wersję magazynu 2, a plik zgłasza wersję 3 | Starsze wydanie nie może wczytać zapisanych ustawień HTTP |
| Plik HTTP i lista Supervisor podają różne porty nasłuchujące | Przed ustaleniem przyczyny sprawdź rzeczywisty port nasłuchujący Core |
| Strona główna odpowiada, ale stan Core nadal wynosi STARTING | Odpowiedź interfejsu nie dowodzi zakończenia uruchamiania |

## Zachowaj opcje odzyskiwania {#preserve-recovery-options}

Przed kolejną aktualizacją zachowaj użyteczną kopię zapasową poza Yellow. [Instrukcja tworzenia kopii zapasowych Home Assistant](https://www.home-assistant.io/common-tasks/general/backups/) opisuje lokalizacje w chmurze i poza urządzeniem. Zaszyfrowana kopia wymaga klucza odzyskiwania. Nie czyść dysku danych NVMe podczas diagnozowania tej niezgodności magazynu.

Przed edycją skopiuj plik HTTP:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

Zatrzymaj się, jeśli polecenie się nie powiedzie. Nie zmieniaj wcześniejszej kopii odzyskiwania o tej samej nazwie. Wybierz nową nazwę i ponów kontrolę przed dalszym działaniem.

Gdy panel jest niedostępny, użyj konsoli szeregowej Yellow. [Instrukcja Nabu Casa dla Linux i macOS](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) pokazuje połączenie USB-C i położenie UART JP1. Postępuj zgodnie z instrukcjami CM4 dla swojego sprzętu.

## Zastosuj przetestowaną poprawkę dla wersji 3.1 {#apply-the-tested-fix-for-version-31}

Najlepszym rozwiązaniem jest użycie zgodnego pliku HTTP sprzed aktualizacji. Przywróć kopię zapasową zgodnie z udokumentowaną procedurą Home Assistant, gdy pełne przywrócenie jest właściwe. Jeśli wyodrębniasz pojedynczy plik, przed zastąpieniem aktywnego pliku potwierdź jego wersję magazynu i zapisany port nasłuchujący. Poniższe polecenia stanowią bezpośrednią poprawkę przetestowaną na tym Yellow, gdy nie było dostępnego zgodnego pliku HTTP.

[Pierwotne obejście opisane w problemie](https://github.com/home-assistant/core/issues/190583) przenosi `.storage/http` i pozwala starszemu Core utworzyć nowy plik. Późniejszy [raport dotyczący Yellow](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) pokazuje inny port nasłuchujący w nowym pliku. Przed stwierdzeniem, że interfejs internetowy działa, sprawdź nowy plik i wynik `ha core info`.

Moja instalacja nie zawierała bloku YAML `http:`, oczekującej konfiguracji HTTP ani certyfikatu TLS lub klucza w ustawieniach stabilnych. Zapisany profil to `intermediate_v6`. W tym ograniczonym przypadku utworzyłem osobny kandydat w wersji 2.2 i zachowałem istniejący port nasłuchujący:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage

expected=$(ha core info --raw-json | jq -r '.data.port') &&
stored=$(jq -r '.data.stable.server_port' "$storage/http") &&
test -n "$expected" &&
test "$expected" != null &&
test "$expected" = "$stored" &&
test ! -e "$storage/http.v2-candidate" &&
jq -e '
  if .version == 3 and .minor_version == 1 and
     .data.pending == null and
     .data.stable.ssl_profile == "intermediate_v6" and
     (.data.stable | has("ssl_certificate") | not) and
     (.data.stable | has("ssl_peer_certificate") | not) and
     (.data.stable | has("ssl_key") | not) and
     (.data.stable | has("trusted_proxies") | not) and
     (.data.stable | has("use_x_forwarded_for") | not)
  then .version = 2 | .minor_version = 2 | .data.stable.ssl_profile = "intermediate"
  else error("Unexpected HTTP config. Stop and inspect")
  end
' \
  "$storage/http" > "$storage/http.v2-candidate" &&

jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&

test "$(jq -r '.data.stable.server_port' "$storage/http")" = \
  "$(jq -r '.data.stable.server_port' "$storage/http.v2-candidate")"
```

Wszystkie powyższe polecenia muszą zakończyć się powodzeniem przed zastąpieniem aktywnego pliku. Jeśli `jq` zgłosi błąd, przed usunięciem kandydata i ponowną próbą sprawdź jego zawartość. [Kod HTTP Core 2026.10.4](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) definiuje wersję magazynu 2.2 i akceptuje profil `intermediate`. [Kod Core 2026.11.1](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) używa wersji 3.1 i wersjonowanych nazw profili. Przed instalacją sprawdziłem także kandydata za pomocą `HTTP_STORAGE_SCHEMA` z zainstalowanego starszego Core.

Uruchom kontrolę schematu zainstalowanego starszego Core, gdy jego kontener nadal działa:

```bash
docker exec homeassistant python3 -c '
import json
from homeassistant.components.http.config import HTTP_STORAGE_SCHEMA
with open("/config/.storage/http.v2-candidate") as source:
    data = json.load(source)
stable = {
    key: value for key, value in data["data"]["stable"].items()
    if key not in ("created_at", "error", "error_message")
}
HTTP_STORAGE_SCHEMA(stable)
print("Schema accepted")
'
```

Zatrzymaj się, jeśli schemat odrzuci kandydata. Ten krok nie weryfikuje każdej integracji ani nieprzetestowanego kształtu magazynu HTTP.

Kontrola schematu wyświetliła `Schema accepted` dla tego kandydata. Każdy inny wynik kończy tę procedurę odzyskiwania.

Ta ręczna konwersja była testowana dla podanych pól. Plik z ustawieniami TLS, zaufanymi proxy lub oczekującą konfiguracją wymaga osobnego przeglądu. Sama zmiana najwyższego numeru wersji pozostawia profil, którego starsze Core nie akceptuje.

Supervisor miał aktywne zadanie Core i w moim przypadku odrzucił `ha core stop`. Zatrzymałem kontener Core z konsoli hosta, zainstalowałem zweryfikowanego kandydata i uruchomiłem kontener:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&
  docker stop homeassistant &&
  test "$(docker inspect -f '{{.State.Running}}' homeassistant)" = false &&
  cmp -s "$storage/http" "$storage/http.before-recovery" &&
  mv "$storage/http.v2-candidate" "$storage/http" &&
  docker start homeassistant
```

Jeśli polecenie nie powiedzie się po zatrzymaniu, przed wykonaniem `docker start homeassistant` sprawdź aktywny plik HTTP. Zmieniony plik wymaga nowego kandydata utworzonego z jego aktualnej zawartości. Po tym kroku strona HTTP wróciła. Odpowiedź HTTP nie dowodziła, że Core zakończył uruchamianie, więc przed uznaniem systemu za odzyskany sprawdziłem stan Supervisor.

Na tym Yellow `docker inspect -f '{{.State.Status}}' homeassistant` zwrócił następnie `running`. Przed żądaniem kolejnej aktualizacji sprawdź `ha core info` i panel.

## Sprawdź wynik aktualizacji {#verify-the-update-outcome}

Po przywróceniu dostępu HTTP zaktualizowałem Core do wersji 2026.11.1. Aby zażądać tej wersji:

```bash
ha core update --version 2026.11.1
```

Po długim uruchamianiu polecenie zgłosiło błąd. Następnie Supervisor zapisał stan Core jako RUNNING i komunikat `Successfully started Home Assistant 2026.11.1`. Odczyt stanu pokazał, że zainstalowana wersja była aktualna, plik HTTP ponownie przeszedł migrację do wersji 3.1, a kontener nie uruchomił się ponownie podczas obserwacji. Zalogowany panel się załadował. **Sprawdź stan końcowy, nawet jeśli polecenie aktualizacji zgłasza błąd.**

Po długiej aktualizacji sprawdź wersję, stan Supervisor i stan kontenera:

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

W tym przypadku pierwsze i trzecie polecenie zwróciły następujące oczyszczone wyniki:

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

Następnie otwórz panel pod zwykłym lokalnym adresem i potwierdź, że ładują się bieżące stany. Zachowaj zapisany plik HTTP do czasu ukończenia kolejnej kopii zapasowej i potwierdzenia normalnej pracy.

Dowody z mojego Yellow nie ustaliły przyczyny pierwszej nieudanej aktualizacji. Późniejszy komunikat o niepowodzeniu zadania również jej nie wskazał. Zainstalowana wersja i działający panel lepiej potwierdzają wynikowy stan niż sam komunikat CLI, ale żaden z tych dowodów nie wyjaśnia, dlaczego Supervisor oznaczył zadanie jako nieudane.

## Następne kroki

Jeśli błąd magazynu HTTP nadal występuje, sprawdź zachowany plik i przywróć zgodną kopię zapasową albo uruchom wydanie Core, które potrafi odczytać tę wersję magazynu. Przywrócenie zachowanego pliku wersji 3 pod starszym Core powtórzy awarię. Jeśli Core osiągnie stan RUNNING, ale niektóre urządzenia nadal będą niedostępne, zbadaj te integracje osobno. Zachowaj kopię odzyskiwania i kopię w chmurze do ukończenia kolejnej kopii zapasowej oraz potwierdzenia, że panel nadal odpowiada.

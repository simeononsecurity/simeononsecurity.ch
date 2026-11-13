---
title: "Open WebUI v0.12.4: lista kontrolna aktualizacji i kontroli dostępu 2026"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Utwórz kopię zapasową Open WebUI i zaktualizuj je do wersji v0.12.4. Następnie sprawdź udostępnianie czatów, uprawnienia eksportu, dostęp do zasobów, konta i dostęp sieciowy."
genre: ["Samodzielnie hostowana sztuczna inteligencja", "Cyberbezpieczeństwo", "Administracja systemami"]
tags: ["Open WebUI", "Open WebUI v0.12.4", "aktualizacja Open WebUI", "bezpieczeństwo Open WebUI", "kontrola dostępu Open WebUI", "samodzielnie hostowana sztuczna inteligencja", "aktualizacja Docker", "aktualizacja pip", "kopia zapasowa Open WebUI", "uprawnienia Open WebUI", "role Open WebUI", "grupy Open WebUI", "uprawnienie eksportu czatów", "udostępnione czaty", "zarchiwizowane czaty", "dostęp do bazy wiedzy", "dostęp do modeli", "uprawnienia narzędzi", "bezpieczeństwo kluczy API", "bezpieczeństwo konta administratora", "wyłącz rejestrację", "uwierzytelnianie odwrotnego proxy", "dostęp VPN", "przypinanie obrazu kontenera"]
---

**Open WebUI v0.12.4 zawiera poprawki bezpieczeństwa, których opiekunowie projektu jeszcze nie opisali.** Informacje o wydaniu zalecają szybkie aktualizowanie wdrożeń i zapowiadają komunikaty po przypisaniu identyfikatorów CVE. Wymienione niżej zmiany dotyczące udostępniania czatów i uprawnień to widoczne punkty z informacji o wydaniu, a nie pełna lista nieujawnionych poprawek bezpieczeństwa. [Informacje o wydaniu Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

<!--more-->

## Najważniejsze wnioski

- **Najpierw wykonaj kopię zapasową.** Zachowaj możliwą do odtworzenia kopię woluminu danych lub bazy danych oraz przesłanych plików przed zmianą aplikacji.
- **Przypnij oficjalne wydanie.** Użyj `ghcr.io/open-webui/open-webui:v0.12.4` dla standardowego obrazu Docker lub `open-webui==0.12.4` dla pip.
- **Testuj uprawnienia z prawdziwymi rolami użytkowników.** Ukryty przycisk nie dowodzi, że API sprawdza uprawnienia.
- **Zachowaj prywatny dostęp.** Wymagaj uwierzytelniania aplikacji i ogranicz dostęp sieciowy przez VPN lub uwierzytelnione odwrotne proxy.

## Przed aktualizacją

**Wymagania wstępne:** ustal bieżącą metodę instalacji, wariant obrazu kontenera, lokalizację trwałych danych, zewnętrzną bazę danych, odwrotne proxy i dostawcę uwierzytelniania. Zaplanuj okno niedostępności i zachowaj bieżącą konfigurację kontenera lub definicję usługi. Zaplanuj czas na próbne odtworzenie na oddzielnej instancji. Poniższe polecenia są udokumentowanymi przez dostawcę wzorcami dostosowanymi do przypiętej wersji. Nie wynikają z aktualizacji na żywo wykonanej na potrzeby tego poradnika. [Aktualizowanie Open WebUI](https://docs.openwebui.com/getting-started/updating/)

1. **Zrób inwentaryzację pamięci.** W standardowej konfiguracji Docker `open-webui` montuje `/app/backend/data`. Zapisz montowania bind, zewnętrzną bazę danych, magazyn obiektów i niestandardowe zmienne środowiskowe. W przypadku pip znajdź aktywny katalog danych aplikacji i bazę danych przed zmianą środowiska. Nie zakładaj, że eksport czatów jest pełną kopią zapasową.
2. **Wykonaj kopię po zatrzymaniu zapisów.** Zatrzymaj aplikację lub użyj spójnej migawki bazy danych. Następnie skopiuj wolumin, wszystkie zewnętrzne bazy danych i przesłane pliki do osobnego magazynu. Dostawca opisuje archiwum woluminu Docker. Dostosuj nazwę woluminu i ścieżkę kopii do wdrożenia. Sprawdź, czy archiwum się otwiera, i przećwicz odtwarzanie na osobnej instancji, zanim mu zaufasz. [Kopia zapasowa i odtwarzanie](https://docs.openwebui.com/getting-started/updating/#backup--restore)
3. **Przeczytaj informacje o wydaniu i wskazówki dotyczące migracji.** Informacje o v0.12.4 nie wymieniają oczekujących poprawek bezpieczeństwa ani zakresu wersji, których dotyczą. Nie przypisuj tym poprawkom CVE ani nie zakładaj, że każda wersja wcześniejsza niż v0.12.4 jest podatna na jedną konkretną usterkę. Przewodnik aktualizacji ostrzega przed jednokierunkowymi migracjami bazy danych i replikami z różnymi wersjami. Jeśli kilka workerów lub replik współdzieli bazę danych, zatrzymaj je równocześnie i postępuj zgodnie z [procedurą migracji wielu replik](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations). Przywrócenie wcześniejszej wersji może wymagać kopii bazy danych sprzed aktualizacji.

## Zaktualizuj zainstalowany pakiet

**Docker, procedura dostawcy dostosowana do przypiętego tagu:** po wykonaniu kopii pobierz oficjalny standardowy obraz i utwórz kontener ponownie z tym samym trwałym woluminem, konfiguracją i `WEBUI_SECRET_KEY`. Przykład zakłada domyślny wolumin nazwany i lokalnie powiązany upstream proxy. Nie wklejaj prawdziwego klucza do historii powłoki. Przekaż go przez używany już chroniony mechanizm środowiskowy lub system zarządzania sekretami. Zachowaj opcje GPU, Ollama, niestandardowej sieci, bazy danych i pozostałe ustawienia bieżącego wdrożenia. [Aktualizowanie Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Oficjalne tagi obrazów](https://docs.openwebui.com/getting-started/quick-start/)

```bash
docker pull ghcr.io/open-webui/open-webui:v0.12.4
docker rm -f open-webui
docker run -d --name open-webui --restart always \
  -p 127.0.0.1:3000:8080 \
  -v open-webui:/app/backend/data \
  --env-file ./open-webui.env \
  ghcr.io/open-webui/open-webui:v0.12.4
```

**Przed uruchomieniem sprawdź `./open-webui.env`:** plik musi już istnieć, mieć restrykcyjne uprawnienia i zawierać dotychczasowy `WEBUI_SECRET_KEY` oraz wymaganą konfigurację. Powiązanie z loopbackiem pasuje do proxy na tym samym hoście, nie na innym komputerze. W Compose zmień wyłącznie obraz usługi na przypięty tag, a następnie uruchom `docker compose pull open-webui` i `docker compose up -d open-webui` w istniejącym projekcie. Zachowaj ten sam wolumin i konfigurację środowiska. To sugerowane polecenia, a nie przetestowana migracja Twojego wdrożenia.

**pip, procedura dostawcy dla konkretnej wersji:** w istniejącym środowisku wirtualnym zatrzymaj usługę, zainstaluj dokładną wersję pakietu i uruchom ją ponownie z tym samym katalogiem danych i środowiskiem. Unikaj drugiego środowiska Python lub nowej, pustej bazy danych. Ogólna instrukcja dostawcy używa `pip install -U open-webui`. Poniższe ograniczenie wersji przypina tę listę kontrolną do v0.12.4. [Aktualizowanie Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Szybki start](https://docs.openwebui.com/getting-started/quick-start/)

```bash
python -m pip install --upgrade 'open-webui==0.12.4'
python -m pip show open-webui
```

**Sprawdź działającą usługę, a nie tylko zainstalowany artefakt.** Odczytaj wersję podczas uruchamiania w `docker logs open-webui` lub dziennikach usługi pip i porównaj ją z wersją widoczną w aplikacji po zalogowaniu. Przewodnik aktualizacji dostawcy zaleca sprawdzenie dzienników kontenera i otwarcie strony logowania. Jeśli interfejs pokazuje nieaktualne zasoby, wymuś odświeżenie przeglądarki. Jeśli podczas uruchamiania pojawi się błąd migracji, pozostaw usługę niedostępną do czasu zdiagnozowania problemu. Nie instaluj starszego pliku binarnego na zmigrowanej bazie danych bez sprawdzenia wymagań odtwarzania. [Kontrole po aktualizacji](https://docs.openwebui.com/getting-started/updating/)

## Sprawdź dostęp po ponownym uruchomieniu

**Zachowanie opisane przez dostawcę:** v0.12.4 ukrywa eksport folderu, eksport zarchiwizowanego czatu i kopiowanie czatu przed użytkownikami bez uprawnienia **Allow Chat Export**. Ukrywa też kontrolki dostępu do modeli, promptów, narzędzi, wiedzy, umiejętności, notatek i folderów przed użytkownikami bez odpowiedniego uprawnienia do udostępniania. Osoby przeglądające udostępniony folder przestają otrzymywać aktualizacje czatu na żywo po zarchiwizowaniu czatu przez właściciela. Osoby korzystające z linku udostępniania przestają otrzymywać aktualizacje na żywo po anulowaniu przez właściciela udostępniania wszystkich czatów. Ukryte kontrolki to zachowanie interfejsu, a nie dowód poprawki po stronie serwera dla nieokreślonej luki. [Informacje o wydaniu](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

**Zalecana weryfikacja operatora:** na koncie testowym bez uprawnień eksportu i udostępniania sprawdź, czy wymienione akcje są nieobecne. Na koncie z odpowiednimi uprawnieniami potwierdź, że zamierzone akcje nadal działają. Utwórz niesensytywny czat testowy w udostępnionym folderze, wyświetl go na drugim koncie, zarchiwizuj jako właściciel i potwierdź, że nowe aktualizacje przestają docierać do odbiorcy. Powtórz test z linkiem udostępniania i opcją **Unshare All Chats**. Ponownie sprawdź zapisane przydziały i stare linki. Nie zakładaj, że zarchiwizowana treść lub wcześniejsze kopie zostały usunięte.

| Obszar przeglądu | Co sprawdzić |
|---|---|
| **Role i grupy** | Usuń nieaktualnych członków i przypisania administratorów. Sprawdź efektywne uprawnienia nowo zatwierdzonego użytkownika i użytkownika z ograniczeniami. |
| **Modele i narzędzia** | Przejrzyj przydziały dostępu do każdego modelu, dołączone narzędzia, uprawnienia do tworzenia narzędzi i dane uwierzytelniające dostawcy. Przetestuj konto bez uprawnień administratora. |
| **Wiedza i pliki** | Sprawdź współpracowników bazy wiedzy, uprawnienia zasobów, załączniki i ustawienia udostępniania. Przetestuj konto, któremu odebrano dostęp. |
| **Czaty i eksporty** | Przejrzyj udostępnione foldery, linki, zarchiwizowane czaty i przypisania Allow Chat Export. Cofnij niepotrzebne linki. |

Te kontrole zasobów to **zalecenia dla operatora**, a nie nowe gwarancje wprowadzone w v0.12.4. [Przewodnik wzmacniania zabezpieczeń](https://docs.openwebui.com/getting-started/advanced-topics/hardening/) dostawcy opisuje role warstwowe, grupy, uprawnienia poszczególnych zasobów, uprawnienia obszaru roboczego, klucze API i umiejscowienie w sieci.

## Usuń luki w kontach i sieci

- **Rejestracja, ustawienie dostawcy:** wyłącz otwartą rejestrację, gdy konta tworzy administrator lub dostawca tożsamości. Sprawdź `ENABLE_SIGNUP` i trwałe ustawienia administratora w [przewodniku wzmacniania zabezpieczeń](https://docs.openwebui.com/getting-started/advanced-topics/hardening/). Zachowaj restrykcyjne zasady zatwierdzania nowych kont.
- **Klucze API, przegląd operatora:** zinwentaryzuj wydane klucze, usuń nieużywane i ogranicz ich tworzenie oraz dostęp do endpointów do wymaganych ról i tras. Według przewodnika dostawcy klucz działa z uprawnieniami osoby, która go utworzyła. Nie umieszczaj kluczy w przykładach ani dziennikach aplikacji.
- **Administratorzy, przegląd operatora:** usuń porzucone konta administratorów, egzekwuj silne kontrole logowania, sprawdź dostępność MFA i zbadaj nieoczekiwane zmiany kont. Przetestuj odzyskiwanie konta przed wyłączeniem zbędnego administratora.
- **Granica sieci, wskazówki dostawcy:** umieść usługę za VPN, proxy dostępowym lub odwrotnym proxy z uwierzytelnianiem i listą dozwolonych adresów IP. Nie udostępniaj jej publicznie bez uwierzytelniania. Unikaj `WEBUI_AUTH=False` w usłudze dostępnej z sieci. Odwrotne proxy bez własnego uwierzytelniania samo nie zastępuje logowania do aplikacji. [Zabezpiecz Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)

**Zakres:** ta lista kontrolna dotyczy oficjalnego wydania Open WebUI i opisanych standardowych metod instalacji. Nie sprawdza forków, pochodnych obrazów ani pakietów firm trzecich. Informacje o v0.12.4 nie stwierdzają aktywnego wykorzystania luk. Sprawdź [komunikaty bezpieczeństwa projektu](https://github.com/open-webui/open-webui/security/advisories), aby znaleźć późniejsze ujawnienia oraz ich własne wersje, których dotyczą i które naprawiają. Nie przypisuj v0.12.4 poprawki z wcześniejszego komunikatu bez przeczytania zakresu wersji.

## Źródła i materiały

- [Informacje o wydaniu Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)
- [Komunikaty bezpieczeństwa Open WebUI](https://github.com/open-webui/open-webui/security/advisories)
- [Aktualizowanie Open WebUI, w tym kopie zapasowe, wycofanie zmian i migracje](https://docs.openwebui.com/getting-started/updating/)
- [Szybki start Open WebUI i oficjalne tagi obrazów](https://docs.openwebui.com/getting-started/quick-start/)
- [Zabezpieczanie Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)
- [Aktualizacje i migracje wielu replik](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations)

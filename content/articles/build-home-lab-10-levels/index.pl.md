---
title: "Zbuduj domowe laboratorium w 10 etapach, od Pi-hole do lokalnej AI"
date: 2026-10-27
lastmod: 2026-11-09
toc: true
draft: false
description: "Zbuduj domowe laboratorium w dziesięciu praktycznych etapach, od filtrowania DNS w całej sieci po lokalną AI, poznając sprzęt, koszty, umiejętności i kompromisy dla każdego poziomu."
genre: ["Domowe laboratorium", "Samodzielny hosting", "Lokalna AI", "Sieci domowe"]
tags: ["domowe laboratorium", "Pi-hole", "Home Assistant", "Docker", "Jellyfin", "Plex", "NAS", "Proxmox", "Tailscale", "Ollama", "lokalna AI", "zużycie energii"]
cover: "/img/cover/build-home-lab-10-levels.webp"
coverAlt: "Domowe laboratorium rozrasta się od małego Raspberry Pi i routera do pamięci masowej, serwerów, sprzętu sieciowego i stacji roboczej lokalnej AI."
coverCaption: ""
---

Zbuduj domowe laboratorium w 10 etapach, od Pi-hole do lokalnej AI
====================================================================

**Domowe laboratorium** to zestaw komputerów i usług, które samodzielnie uruchamiasz, aby rozwiązywać codzienne problemy i uczyć się obsługi rzeczywistych systemów. Możesz blokować reklamy, automatyzować oświetlenie, przechowywać rodzinne multimedia lub testować maszyny wirtualne. **Zacznij od jednego użytecznego zadania.** Dodaj sprzęt, gdy pojawi się rzeczywiste ograniczenie.

Ten przewodnik prowadzi od małego Raspberry Pi z Pi-hole do serwera uruchamiającego lokalne modele AI. **Każdy etap dodaje możliwości i nowe obowiązki.** Poniższe szacunki kosztów zakładają przykładowy pobór mocy i cenę energii $0.15 za kilowatogodzinę. Sprawdź lokalną stawkę i zmierz sprzęt przed kolejnymi zakupami.

## Poziom 1: Blokuj reklamy w całej sieci domowej

Zainstaluj [Pi-hole](https://docs.pi-hole.net/) na Raspberry Pi lub innym niewielkim komputerze z Linuksem. Pi-hole działa jak **pułapka DNS**. Gdy urządzenie pyta o adres domeny z listy blokowania, Pi-hole nie zwraca użytecznego adresu docelowego. Przeglądarka, telefon i smart TV korzystają z tego samego filtra, gdy router lub serwer DHCP wskazuje klientom Pi-hole.

**Filtrowanie DNS** działa także poza przeglądarkami, między innymi blokuje część reklam w aplikacjach i telewizorach podłączonych do sieci. Nie filtruje treści na poziomie strony, więc reklamy z tej samej domeny co witryna lub aplikacja nadal się wyświetlą. Lista blokowania czasem uniemożliwia załadowanie logowania, filmu lub płatności. Sprawdź dziennik zapytań Pi-hole, w razie potrzeby zezwól na konkretną domenę i przygotuj zapasowy plan DNS na wypadek awarii.

Zużycie energii jest niewielkie. Dla urządzenia o mocy 8 W działającego przez cały miesiąc szacunek wynosi 8 W × 24 godziny × 30 dni ÷ 1 000 × $0.15 = **około $0.86 miesięcznie**. Zmierz cały zasilacz przy gniazdku. Drugi komputer, dysk USB lub nieefektywny adapter zmienią wynik.

**Nauczysz się:** DNS, DHCP, list blokowania i podstawowej konserwacji Linuksa.

## Poziom 2: Automatyzuj inteligentne urządzenia lokalnie

Dodaj [Home Assistant](https://www.home-assistant.io/), który łączy zgodne urządzenia smart home i automatyzacje w jednym systemie. Zaplanuj wyłączanie światła przed snem. Włącz wentylator, gdy czujnik temperatury przekroczy ustawioną wartość. Otrzymuj powiadomienie, gdy czujnik zalania wykryje wodę. **Te drobne automatyzacje przynoszą natychmiastową korzyść.**

**Sterowanie lokalne** pozwala utrzymać wiele automatyzacji w domu podczas awarii zewnętrznej usługi lub internetu. Działanie zależy od urządzenia. Niektóre produkty nadal wymagają konta u dostawcy, usługi w chmurze lub połączenia internetowego do konfiguracji i zdalnych funkcji. Przed zakupem sprzętu sprawdź wymagania integracji.

**Twórz kopie zapasowe Home Assistant** i przechowuj kopię poza jego hostem. Udokumentuj integracje i procedury odzyskiwania. Awaria karty SD lub mini PC nie powinna skasować konfiguracji.

**Nauczysz się:** integracji urządzeń, wyzwalaczy, warunków i odzyskiwania z kopii zapasowych.

## Poziom 3: Uruchom kilka usług na jednym mini PC

**Używany biznesowy mini PC** często oferuje rozszerzalną pamięć, wymienny nośnik i przydatne porty za niewielką cenę z drugiej ręki. Mini PC z Intel N100 zwykle zużywa mniej energii i zajmuje niewiele miejsca. Intel opisuje N100 jako procesor z czterema rdzeniami, czterema wątkami, TDP 6 W i obsługą maksymalnie 16 GB pamięci. TDP procesora nie jest równoznaczne z poborem mocy całego systemu z gniazdka. Porównaj konkretny komputer, pamięć, nośnik, gwarancję i porty sieciowe.

Zainstaluj Linuksa i użyj [Dockera](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/), aby uruchamiać osobne usługi jako **kontenery**. Kontener pakuje aplikację i jej zależności, współdzieląc jądro systemu operacyjnego hosta. Możesz na przykład uruchomić menedżer haseł, taki jak utrzymywany przez społeczność projekt Vaultwarden, oraz monitor dostępności, taki jak Uptime Kuma. **Traktuj menedżer haseł jako usługę wrażliwą:** ogranicz dostęp, stosuj silne uwierzytelnianie, instaluj aktualizacje i przechowuj zaszyfrowaną kopię zapasową.

**Kontenery nie zastępują aktualizacji ani kopii zapasowych.** Przydziel każdej usłudze określone miejsce na dane i zapisz procedury odzyskiwania. Mały mini PC ma także ograniczenia. Kilka baz danych, konwersje multimediów lub duże aplikacje mogą wyczerpać pamięć, przestrzeń dyskową albo czas procesora.

**Nauczysz się:** administracji Linuksem, kontenerów, wolumenów, aktualizacji i odzyskiwania usług.

## Poziom 4: Zbuduj domową bibliotekę multimediów

[Jellyfin](https://jellyfin.org/docs/) to otwartoźródłowy serwer multimediów. [Plex](https://support.plex.tv/) oferuje dopracowany ekosystem klientów i opcjonalne funkcje powiązane z kontem. Oba systemy porządkują prywatne biblioteki i strumieniują multimedia do obsługiwanych klientów. **Wybierz rozwiązanie w zależności od klientów**, modelu dostępu zdalnego, obsługi sprzętu i potrzebnych funkcji.

**Potrzebna przestrzeń** zależy od rozmiaru i jakości kolekcji. Zacznij od jednego dysku tylko wtedy, gdy masz osobny plan kopii zapasowych. Używaj spójnych nazw folderów i metadanych, aby serwer poprawnie rozpoznawał filmy i odcinki.

**Bezpośrednie odtwarzanie** przesyła zgodny plik do klienta bez zmiany strumienia wideo. **Transkodowanie** konwertuje dźwięk lub obraz, gdy klient, połączenie, napisy albo ustawienie jakości wymaga innego formatu. Transkodowanie dodatkowo obciąża serwer. Przetestuj urządzenia i sieć przed zakupem GPU lub wydajniejszego procesora. **Zrezygnuj z dedykowanego serwera multimediów**, jeśli każdy klient odtwarza pliki bezpośrednio, a jeden host wystarcza.

**Nauczysz się:** formatów multimediów, planowania pamięci masowej, przepustowości sieci i testowania obciążenia.

## Poziom 5: Dodaj nadmiarowość pamięci masowej i osobną kopię zapasową

NAS z dwoma dyskami i **lustrzaną pamięcią masową** zapisuje dane na obu dyskach. Jeśli jeden dysk ulegnie awarii, drugi zachowuje bieżącą kopię, którą można wykorzystać podczas wymiany uszkodzonego dysku i odbudowy lustra. Lustro chroni dostępność przy awarii jednego dysku. **Lustro nie odzyska** usuniętego pliku, nie cofnie szyfrowania ransomware ani nie ochroni przed kradzieżą, pożarem czy awarią zasilania uszkadzającą oba dyski.

Przechowuj **osobną kopię zapasową** na innym urządzeniu lub w innej lokalizacji. Uwzględnij ważne dokumenty, zdjęcia, eksporty konfiguracji i dane usług. Ustal harmonogram kopii zapasowych i zachowuj wersje, aby przypadkowe zmiany nie nadpisały wszystkich poprawnych kopii.

**Przetestuj przywracanie.** Wybierz kilka plików, przywróć je do osobnego folderu i otwórz. W przypadku usługi odtwórz dane na instancji testowej albo udokumentuj kroki i sprawdź każdy plik. Kopia zapasowa, której nigdy nie przywrócono, jest założeniem, a nie planem odzyskiwania.

**Nauczysz się:** systemów plików, wymiany dysków, rotacji kopii zapasowych i testowania przywracania.

## Poziom 6: Naucz się wirtualizacji na małym klastrze Proxmox

[Proxmox VE](https://pve.proxmox.com/pve-docs/) uruchamia maszyny wirtualne i kontenery na sprzęcie serwerowym. Kilka połączonych w **klaster** mini PC zapewnia wspólny widok zarządzania i pozwala uczyć się o węzłach, pamięci masowej oraz migracji. Klaster to grupa serwerów skonfigurowanych do współpracy. Jego członkowie nie łączą pamięci w jedną dużą pulę. **Wysoka dostępność wymaga** dodatkowego planowania oraz odpowiedniej współdzielonej lub replikowanej pamięci masowej.

**Migawka** zapisuje stan maszyny wirtualnej w określonym momencie, umożliwiając powrót do wcześniejszego stanu po zmianie w laboratorium. Migawki zwykle zależą od pierwotnej pamięci masowej. Nie są niezależnymi kopiami zapasowymi. **Skopiuj ważne dane do osobnego celu kopii zapasowej** i przetestuj ich przywrócenie.

Każdy węzeł zwiększa pobór mocy, liczbę portów sieciowych, kabli i aktualizacji. Trzy małe komputery to również trzy systemy do aktualizowania i diagnozowania. Jeden mini PC z kilkoma maszynami wirtualnymi uczy wielu tych samych podstaw przy niższym koszcie. **Dodaj węzły, gdy** eksperymenty wymagają izolacji lub chcesz ćwiczyć zarządzanie klastrem.

**Nauczysz się:** maszyn wirtualnych, pul pamięci masowej, migawek, członkostwa w klastrze i utrzymania węzłów.

## Poziom 7: Dodaj prywatny dostęp zdalny i separację sieci

[Tailscale](https://tailscale.com/kb/) łączy zatwierdzone urządzenia przez sieć prywatną, zapewniając zdalny dostęp do wybranych usług domowych. **Ogranicz dostęp** do urządzeń i usług potrzebnych każdej osobie. Chroń konta uwierzytelnianiem wieloskładnikowym i przeglądaj stare urządzenia oraz klucze.

Zarządzalny przełącznik lub router z obsługą **VLAN-ów** rozdziela grupy urządzeń. Umieść inteligentne gniazdka i inne urządzenia o niskim poziomie zaufania w innej sieci niż komputery przechowujące prywatne pliki. Umieść pamięć masową w sieci dostępnej tylko dla systemów, które jej potrzebują. Segmentacja ogranicza komunikację między urządzeniami. Nadal stosuj aktualizacje, silne hasła i reguły dostępu.

**Unikaj bezpośredniego wystawiania paneli administracyjnych do publicznego internetu**, chyba że rozumiesz wymagania usługi dotyczące uwierzytelniania, poprawek i zapory. Prywatne narzędzie dostępu także wymaga starannej kontroli kont i urządzeń.

**Nauczysz się:** dostępu prywatnego, uprawnień opartych na tożsamości, VLAN-ów, reguł zapory i granic zaufania urządzeń.

## Poziom 8: Dodaj serwer klasy enterprise

Przejdź na większy serwer, gdy masz zmierzoną potrzebę większej liczby rdzeni CPU, pamięci, zatok na dyski, gniazd PCIe lub przepustowości sieci. Starsze serwery enterprise często kosztują mniej na rynku wtórnym, ale mają głośne wentylatory, a **pobór mocy w stanie bezczynności wynosi około 100–160 W**, zależnie od modelu i zamontowanych części. Potraktuj ten zakres jako szacunek, a nie specyfikację.

Przed zakupem oblicz roczny szacowany koszt energii:

`zmierzone waty ÷ 1 000 × 24 × 365 × stawka za kWh`

Przy 120 W i cenie $0.15 za kWh szacunek wynosi 1 051 kWh rocznie, czyli około **$158 rocznie**. Zmierz dokładny serwer w stanie bezczynności i podczas typowego obciążenia. Uwzględnij pobór dysków, chłodzenia i UPS-a.

Sprawdź głębokość obudowy, zgodność dysków, hałas, sterowanie wentylatorami, zasilacz i karty rozszerzeń. Serwer przekraczający budżet miejsca lub energii nie jest praktyczną modernizacją.

**Nauczysz się:** sprzętu serwerowego, zdalnego zarządzania, rozbudowy, chłodzenia i szacowania kosztów eksploatacji.

## Poziom 9: Mierz energię i dopasuj rozmiar laboratorium

Użyj **wtyczkowego miernika mocy**, aby zmierzyć każdy komputer w stanie bezczynności i podczas normalnej pracy. Sporządź listę największych odbiorników. Przejrzyj ustawienia zasilania BIOS-u, usuń nieużywane karty i dyski, a codzienne usługi przenieś z powrotem na wydajne mini PC, gdy sprzęt enterprise nie jest potrzebny.

Uruchamiaj duży serwer tylko wtedy, gdy obciążenie wymaga jego możliwości. Jeśli korzystasz z harmonogramu Wake-on-LAN lub zdalnego sterowania zasilaniem, opisz procedury odzyskiwania po awarii sieci lub zasilania. Prowadź **listę zależności usług**, aby wyłączenia nie przerywały działania pamięci masowej lub sieci potrzebnej innym systemom.

Szafa rack pomaga uporządkować sprzęt i przepływ powietrza, gdy sprzęt rackowy uzasadnia zajmowane miejsce. UPS podtrzymuje zasilanie podczas krótkich awarii i daje systemom czas na prawidłowe zamknięcie. Oba rozwiązania wymagają zakupu, miejsca i dodatkowej energii. **Zmierz ich pobór** i uwzględnij wymianę baterii w długoterminowym budżecie.

**Nauczysz się:** pomiaru energii, zarządzania zasilaniem, mapowania zależności i planowania pojemności.

## Poziom 10: Uruchamiaj modele AI lokalnie

[Ollama](https://docs.ollama.com/) pobiera obsługiwane modele językowe i uruchamia je na komputerze. **Lokalna inferencja** utrzymuje prompty i odpowiedzi na kontrolowanym przez ciebie sprzęcie, gdy korzystasz z lokalnego modelu i aplikacji. Potwierdź, że cały przepływ oprogramowania pozostaje lokalny. Połączona aplikacja, funkcja telemetrii lub opcja modelu w chmurze wysyła dane poza sieć.

Wymagania sprzętowe zależą od rozmiaru modelu, kwantyzacji, długości kontekstu i oczekiwanej szybkości. **Pamięć systemowa lub pamięć GPU musi pomieścić** wagi modelu i kontekst roboczy. Małe komputery uruchamiają mniejsze modele, a większe modele i dłuższe konteksty wymagają więcej pamięci i często wydajnego GPU. Zmierz pobór mocy podczas inferencji. System z GPU zwykle zużywa znacznie więcej energii niż mini PC w stanie bezczynności.

Modele lokalne sprawdzają się przy tworzeniu szkiców, podsumowywaniu prywatnych notatek i prostej klasyfikacji, gdy ich jakość spełnia twoje wymagania. Generują błędne odpowiedzi, a mniejsze modele często mają trudności ze złożonym rozumowaniem lub aktualnymi faktami. Modele chmurowe czasem lepiej radzą sobie z konkretnymi zadaniami. **Porównaj jakość, prywatność, opóźnienie, koszt i zużycie energii**, zanim zdecydujesz, gdzie uruchamiać obciążenie.

**Nauczysz się:** pamięci modelu, kwantyzacji, inferencji, granic prywatności i oceny obciążeń.

## Porównaj dziesięć poziomów

**Koszty są szacunkami, a nie ofertami.** Ceny sprzętu różnią się w zależności od regionu, stanu i konfiguracji pamięci masowej. Oszacuj koszt energii, używając `waty ÷ 1 000 × godziny × dni × stawka za kWh`. W miarę możliwości mierz pobór przy gniazdku i uwzględnij czas bezczynności, ponieważ wiele domowych serwerów działa całą dobę.

### Możliwości i sprzęt

| Poziom | Nowe możliwości | Typowy sprzęt |
|---|---|---|
| **1** | Filtrowanie DNS w sieci | Raspberry Pi lub mały host z Linuksem |
| **2** | Lokalna automatyzacja urządzeń | Pi lub mini PC, zgodne urządzenia |
| **3** | Wiele aplikacji hostowanych samodzielnie | Używany biznesowy mini PC lub system N100 |
| **4** | Strumieniowanie własnych multimediów | Mini PC z pamięcią na multimedia |
| **5** | Tolerancja awarii dysku i odzyskiwanie | NAS z dwoma dyskami i osobną kopią zapasową |
| **6** | Laboratorium serwerów wirtualnych | Co najmniej dwa mini PC |
| **7** | Prywatny dostęp i segmentacja | Tailscale, zarządzalny router lub przełącznik |
| **8** | Duża wydajność i rozbudowa | Serwer enterprise |
| **9** | Niższe zużycie energii laboratorium | Miernik mocy, dostrojone systemy |
| **10** | Lokalna inferencja modelu | Komputer z dużą pamięcią, opcjonalne GPU |

### Umiejętności, koszty i kompromisy

| Poziom | Zdobywane umiejętności | Szacunkowe koszty bieżące | Główny kompromis |
|---|---|---|---|
| **1** | DNS, DHCP, Linux | Około $1 miesięcznie przy 8 W i $0.15/kWh | Część reklam pozostaje, błędne blokady wymagają uwagi |
| **2** | Integracje, wyzwalacze, kopie zapasowe | Energia hosta i koszty urządzeń | Zgodność i obsługa kopii zapasowych |
| **3** | Docker, aktualizacje, pamięć masowa | Zależne od zmierzonego poboru systemu | Ograniczenia CPU, pamięci i dysku |
| **4** | Formaty, organizacja, transkodowanie | Pamięć masowa i zasilanie serwera | Transkodowanie czasem wymaga lepszego sprzętu |
| **5** | Lustra, retencja, przywracanie | Zasilanie NAS, dyski, cel kopii | Lustro nie jest kopią zapasową |
| **6** | Proxmox, maszyny wirtualne, klastry | Każdy węzeł zwiększa pobór i nakład pracy | Więcej węzłów oznacza więcej konserwacji |
| **7** | Reguły dostępu, VLAN-y, zapora | Sprzęt sieciowy i koszty usług | Błędne reguły mogą ujawnić usługi |
| **8** | Sprzęt, chłodzenie, zdalne zarządzanie | Zależne od serwera, oblicz na podstawie pomiaru | Hałas, ciepło i pobór w bezczynności |
| **9** | Pomiary, harmonogramy, dopasowanie rozmiaru | Jednorazowy koszt miernika, oszczędności są różne | Harmonogramowanie dodaje czynności operacyjne |
| **10** | Wdrażanie i ocena modeli | Energia obliczeń i pamięć masowa | Jakość i szybkość zależą od sprzętu |

## Wybierz kolejną przydatną modernizację

**Zatrzymaj się na poziomie odpowiadającym obecnym potrzebom.** Pi-hole i jeden mini PC mogą wystarczyć do twoich usług. NAS przyda się, gdy potrzebujesz współdzielonej pamięci masowej i sprawdzonego planu odzyskiwania. Dodaj klaster lub serwer enterprise, gdy uzasadnia to obciążenie albo cel edukacyjny.

Zapisz **miejsce przechowywania danych każdej usługi, proces aktualizacji i kroki odzyskiwania.** Przetestuj kopie zapasowe przed dodaniem sprzętu. Niech kolejnym zakupem kieruje rzeczywiste ograniczenie.

## Źródła

- [Dokumentacja Pi-hole](https://docs.pi-hole.net/)
- [Dokumentacja Home Assistant](https://www.home-assistant.io/docs/)
- [Specyfikacja procesora Intel N100](https://www.intel.com/content/www/us/en/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/specifications.html)
- [Docker: Czym jest kontener?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Dokumentacja Jellyfin](https://jellyfin.org/docs/)
- [Pomoc Plex](https://support.plex.tv/)
- [Dokumentacja Proxmox VE](https://pve.proxmox.com/pve-docs/)
- [Dokumentacja Tailscale](https://tailscale.com/kb/)
- [Dokumentacja Ollama](https://docs.ollama.com/)

---
title: "Kontenery nie są już granicą bezpieczeństwa: ucieczki z kernela w 2026 roku"
date: 2026-09-28
lastmod: 2026-11-13
toc: true
draft: false
description: "Omów badania nad ucieczkami z kontenerów z 2026 roku, granice izolacji kernela, presję na instalowanie poprawek i rolę mikroVM."
genre: ["Bezpieczeństwo kontenerów", "Linux", "Bezpieczeństwo kernela", "Wirtualizacja", "Bezpieczeństwo chmury", "Badania zagrożeń", "Blue team", "DevSecOps"]
tags: ["ucieczka z kontenera", "granica bezpieczeństwa kontenerów", "Linux kernel CVE", "lokalne podniesienie uprawnień", "LPE 2026", "Copy Fail", "CVE-2026-31431", "Dirty Frag", "CVE-2026-43284", "CVE-2026-43500", "Fragnesia", "CVE-2026-46300", "CVE-2026-80521", "kernelCTF", "kvmCTF", "microVM", "Firecracker", "Kata Containers", "uszkodzenie page cache", "AF_ALG", "AF_UNIX", "XFRM ESP", "RxRPC", "izolacja przestrzeni nazw", "wywołanie systemowe clone", "wykrywanie podatności AI", "bezpieczeństwo Dockera", "bezpieczeństwo Kubernetes", "izolacja wielu dzierżawców", "ucieczka z sandboxa", "nsjail", "Bubblewrap", "Firejail", "Dirty Pipe", "trend CVE kernela"]
cover: "/img/cover/container-security-vulnerabilities-kernel-escapes-2026.webp"
coverAlt: "Cyfrowa ilustracja wielu świecących kontenerów połączonych z centralnym symbolem kernela. Kolorowe elementy pokazują podatności rozchodzące się z kernela na ciemnym tle."
coverCaption: ""
ref: ["/articles/docker-vs-vms", "/articles/how-to-secure-your-docker-and-kubernetes-environment", "/cvss-calculator"]
---
**Kontenery współdzielą jeden kernel. W 2026 roku cztery odrębne rodziny podatności pokazały, że pojedynczy błąd kernela wystarcza, by opuścić kontener i dostać się na hosta.** Copy Fail, Dirty Frag, Fragnesia i CVE-2026-80521 zapewniają uprawnienia roota nieuprzywilejowanemu użytkownikowi lokalnemu. Każda z nich przekracza granicę kontenera.

*Najbardziej niepokojące nie są same błędy. Chodzi o to, jak tanio AI je teraz znajduje i jak jedna poprawka doprowadziła do kolejnego błędu.*

Ten artykuł wyjaśnia, jak kontenery izolują obciążenia, dlaczego izolacja opiera się teraz na coraz węższym fundamencie, co robi każda z podatności z 2026 roku oraz której technologii izolacji warto użyć zamiast kontenerów.

**Efekt dla czytelnika:** określ dla każdego obciążenia, kto dostarcza kod, ustal wymagane funkcje kernela i wybierz między utwardzonymi kontenerami a granicą mikroVM. Traktuj studia przypadków z 2026 roku jako materiał badawczy z określonego czasu. Przed zmianą kernela produkcyjnego sprawdź aktualne zalecenia dostawców.

## Krótka odpowiedź

| Pytanie | Krótka odpowiedź |
|---|---|
| **Czy kontenery izolują?** | Tak, procesy i systemy plików. Wszystkie kontenery współdzielą kernel, więc błędy kernela stanowią wspólne ryzyko |
| **Dlaczego teraz?** | Wyszukiwanie błędów kernela z pomocą AI stało się dużo tańsze. Do września 2026 roku opublikowano prawie **6000 CVE kernela** |
| **Co przekracza granicę?** | Każde lokalne podniesienie uprawnień w kernelu. Ucieczka nie wymaga błędnej konfiguracji kontenera |
| **Czy wystarczy instalować poprawki?** | To konieczne, ale tempo już nie wystarcza. Jedna poprawka z 2026 roku **wprowadziła nowy podatny na wykorzystanie błąd** |
| **Co sprawdza się lepiej?** | MikroVM, takie jak Firecracker lub Kata Containers, które zapewniają każdemu obciążeniu własny kernel |
| **Czy alternatywa jest idealna?** | Nie. Hypervisor też składa się z kodu. Jego powierzchnia ataku jest o wiele rzędów wielkości mniejsza, a to robi różnicę |

## Jak kontenery izolują

Aby zrozumieć tę granicę, trzeba najpierw wiedzieć, czym kontener nie jest.

**Kontener nie jest maszyną wirtualną.** Między procesem a sprzętem nie ma drugiego kernela, emulowanego sprzętu ani hypervisora. Uruchamiając obraz kontenera, uruchamiasz proces na istniejącym kernelu, ze zmienionym widokiem systemu.

Mechanizmem jest **wywołanie systemowe `clone`**. `fork` kopiuje przestrzeń adresową procesu, natomiast `clone` tworzy proces potomny i daje wywołującemu precyzyjną kontrolę nad tym, które elementy kontekstu wykonania są współdzielone, a które zastępowane. Docker przekazuje do `clone` zestaw **przestrzeni nazw**:

| Przestrzeń nazw | Co pozoruje |
|---|---|
| **Mount** | Prywatny katalog główny systemu plików, dzięki któremu kontener widzi własne drzewo zamiast twojego |
| **PID** | Własną numerację procesów, więc `PID 1` jest pierwszym procesem kontenera, a nie `systemd` |
| **User** | Mapowanie tożsamości, w którym „root” kontenera odpowiada nieuprzywilejowanemu użytkownikowi hosta |
| **Network** | Prywatne interfejsy, tabele routingu i porty |
| **IPC** | Izolowaną pamięć współdzieloną i kolejki komunikatów |
| **UTS** | Własną nazwę hosta i domeny |
| **Cgroup** | Prywatny widok limitów zasobów |

Dodaj **system plików typu union** na wierzchu obrazu, a rezultat *sprawia wrażenie* osobnego komputera. `id` w kontenerze pokazuje `uid=0(root)`. System plików przypomina minimalną instalację Ubuntu. Lista procesów pokazuje tylko procesy kontenera.

**Na poziomie wywołań systemowych nic z tego nie jest granicą bezpieczeństwa.** Gdy proces w kontenerze otwiera plik, przydziela pamięć lub korzysta z gniazda sieciowego, to samo jądro obsługuje żądanie każdego kontenera na hoście. Przestrzenie nazw zmieniają *to, co proces widzi*, a nie *to, co kernel dla niego zrobi*.

*Prawdziwą granicą między kontenerem a hostem jest kernel. Reszta to prezentacja.*

{{< figure src="container-namespace-isolation-shared-kernel.webp" alt="Diagram trzech kontenerów korzystających z tego samego kernela. Przestrzenie nazw mount, PID, user i network rozdzielają ich widoki, ale wszystkie wywołania systemowe nadal trafiają do jednego współdzielonego kernela." >}}

{{< youtube id="9-2CSJC114k" enable="true" title="the change is finally coming" nocookie="true" >}}

## Granica składa się z kodu, a kod zawiera błędy

Każda czynność kontenera przechodzi przez **interfejs wywołań systemowych**. Otwieranie pliku, odczyt pamięci, zapis do gniazda, zmiana UID: kernel pośredniczy we wszystkim, ponieważ nie chce, aby procesy bezpośrednio dotykały procesora, systemu plików czy sieci.

Pośredniczenie tworzy model bezpieczeństwa, a jego implementacja składa się z kodu. To około **30 milionów wierszy**.

Lokalne podniesienie uprawnień (LPE) występuje, gdy proces wykorzystuje błąd w kodzie pośredniczącym, aby uzyskać nieprzyznane mu uprawnienia. **LPE nie są nowością.** Występują od początku pośredniczenia kernela, a branża przez dziesięciolecia radziła sobie z ich stałym, niewielkim napływem.

**Dirty Pipe z 2022 roku** jest przykładem, który zna większość osób. Błąd w obsłudze buforów potoku pozwalał nadpisywać pliki tylko do odczytu. Był to temat dnia, ponieważ błędy o takiej wadze pojawiały się **mniej więcej raz na rok lub dwa**. Instalowało się poprawkę, wracało do pracy i ufało, że poważna wada nie pozostaje nieodkryta w kodzie czytanym przez milion osób.

*To założenie jest już nieaktualne.*

## Co zmieniło się w 2026 roku

Zmiana nie dotyczy umiejętności atakujących. **Znajdowanie błędów uszkadzających pamięć kernela stało się zadaniem inżynieryjnym, a nie karierą badawczą.**

Trzy tegoroczne fakty dobrze pokazują tę zmianę:

| Znalezisko | Kto znalazł | Jak |
|---|---|---|
| **Copy Fail** (CVE-2026-31431) | Taeyang Lee, Theori | Z pomocą **Xint Code**, narzędzia AI do analizy statycznej. Skanowanie podsystemu kryptograficznego Linuksa trwało około **godziny** |
| **CVE-2026-80521** | Zhenpeng (Leo) Lin, DepthFirst | Znalezione przez **dfs-large1**, wewnętrzny model AI trenowany do wykrywania podatności |
| **CVE-2026-80521**, niezależnie | Kyle, **OpenAI** | Ten sam błąd, niezależne odkrycie i zgłoszenie tego samego dnia |

Przeczytaj trzeci wiersz jeszcze raz. Dwie organizacje korzystające z różnych narzędzi AI znalazły **to samo use-after-free w AF_UNIX** i zgłosiły je do `security@kernel.org` **tego samego dnia**. To nie przypadkowy zbieg talentów. Powtarzalny proces dwa razy przyniósł tę samą odpowiedź.

DepthFirst podaje skalę wprost: **do września 2026 roku opublikowano prawie 6000 CVE kernela**. Liczba rośnie zgodnie z dostępnością pomocy AI, a nie liczbą programistów kernela.

*Gdy godzina skanowania z pomocą AI znajduje dziesięcioletni błąd w podsystemie kryptograficznym, ekonomia wykorzystania kernela się odwraca.*

## Cztery ucieczki w jeden rok

Każda z tych podatności daje roota z nieuprzywilejowanego konta lokalnego. Żadna nie wymaga błędnej konfiguracji kontenera, flagi privileged ani dostępu przez sieć.

| Podatność | CVE | Podsystem | Prymityw | Odkrywca |
|---|---|---|---|---|
| **Copy Fail** | CVE-2026-31431 | `algif_aead` / AF_ALG | Zapis 4 bajtów do page cache dowolnego pliku, który da się odczytać | Theori, pomoc AI |
| **Dirty Frag** | CVE-2026-43284 + CVE-2026-43500 | XFRM ESP, RxRPC | Zapis 4 bajtów do page cache przez dwie połączone odmiany | Hyunwoo Kim |
| **Fragnesia** | CVE-2026-46300 | XFRM ESP-in-TCP (ESP enkapsulowany w TCP) | Zapisy pojedynczych bajtów do page cache | Hyunwoo Kim |
| **AF_UNIX UAF** | CVE-2026-80521 | Gniazda AF_UNIX | Use-after-free w mechanizmie garbage collection `unix_vertex` | DepthFirst, pomoc AI |

Wszystkie cztery łączy wzorzec, na który warto zwrócić uwagę. **Atakują page cache, a nie dysk.**

### Copy Fail: błąd logiczny bez race condition

Copy Fail to najprostsza i najbardziej niepokojąca z czterech podatności.

Prawie każde LPE w Linuksie wymaga okna czasowego albo offsetu pamięci specyficznego dla kernela. **Copy Fail nie wymaga żadnego z nich.** To bezpośredni błąd logiczny w `algif_aead`, module udostępniającym z przestrzeni użytkownika uwierzytelnione szyfrowanie przez AF_ALG.

Łańcuch wykorzystuje `splice()`, aby umieścić stronę page cache w operacji, a następnie nadużywa ścieżki AEAD działającej w miejscu, by zapisać w tej stronie **cztery kontrolowane bajty**. Uszkodzona strona **nigdy nie jest oznaczana jako dirty**, więc nie trafia z powrotem na dysk. Plik na dysku pozostaje nietknięty, dlatego kontrole sum kontrolnych i integralności przechodzą, mimo że kopia w pamięci zawiera modyfikację.

Jeden **skrypt Pythona o rozmiarze 732 bajtów** uzyskuje roota na każdej dystrybucji Linuksa wydanej od 2017 roku. Błąd wprowadziła **optymalizacja z 2017 roku** w `algif_aead`, a poprawka z 2026 roku po prostu ją cofa. Commit mainline `a664bf3d603d`.

*Błąd był obecny w każdej głównej dystrybucji przez prawie dekadę. Narzędzie AI znalazło go w około godzinę.*

### Dirty Frag: dwie odmiany, które się uzupełniają

Nazwa Dirty Frag trafnie opisuje pokrewieństwo. **Dirty Pipe nadpisuje `struct pipe_buffer`. Dirty Frag nadpisuje pole `frag` w `struct sk_buff`.**

Są to **dwie połączone podatności**, a ich połączenie jest sprytną częścią ataku:

- **CVE-2026-43284** wykorzystuje fakt, że `esp_input()` pomija ścieżkę copy-on-write przed deszyfrowaniem w miejscu wstawionego fragmentu. Wymaga uprawnień do tworzenia **user namespace**, które niektóre dystrybucje ograniczają.
- **CVE-2026-43500** wykorzystuje fakt, że `rxkad_verify_packet_1()` deszyfruje fragment w miejscu. Nie wymaga uprawnień do przestrzeni nazw, ale modułu `rxrpc` brakuje w większości dystrybucji. Ubuntu ładuje go domyślnie.

**Każda odmiana osobno ma martwy punkt. Razem się uzupełniają.** Gdy user namespace są dozwolone, najpierw działa ścieżka ESP. Gdy jest zablokowana, ale dostępne jest `rxrpc`, działa ścieżka RxRPC. Jeden plik binarny exploita działa wtedy w wielu dystrybucjach. Odmiana RxRPC uzyskuje roota, zerując pole w `/etc/passwd`, po czym PAM z `nullok` akceptuje puste hasło.

**Dla obrońców najważniejszy jest fakt:** Dirty Frag działa **niezależnie od dostępności `algif_aead`**. Powszechnie stosowana ochrona Copy Fail, polegająca na umieszczeniu modułu na czarnej liście, **w ogóle nie chroni przed Dirty Frag**.

### Fragnesia: poprawka, która utworzyła podatność

Fragnesia należy do tej samej klasy co Dirty Frag, ale atakuje ścieżkę XFRM **ESP-in-TCP**. To najbardziej pouczający przypadek z całej grupy.

Podatność wykorzystuje nieprawidłową obsługę współdzielonych fragmentów stron podczas łączenia `skb`. Atakujący wstawia strony plików do kolejki odbiorczej TCP za pomocą `splice()`, zanim gniazdo przejdzie w tryb protokołu wyższej warstwy `espintcp`. Po aktywowaniu ESP kernel deszyfruje zakolejkowane dane **w miejscu**, a manipulacja strumieniem klucza AES-GCM uszkadza page cache. Atakujący uzyskuje powtarzalne **zapisy pojedynczych bajtów** do buforowanych stron plików.

Exploit uzyskuje roota, nadpisując pierwsze bajty `/usr/bin/su` małym ładunkiem ELF. **Zmiana istnieje wyłącznie w pamięci i nigdy nie dotyka pliku binarnego na dysku.**

Nieuprzywilejowane **user i network namespaces** zapewniają `CAP_NET_ADMIN` w izolowanej przestrzeni nazw, po czym `NETLINK_XFRM` instaluje spreparowane skojarzenie bezpieczeństwa.

*Warto zatrzymać się przy tym zdaniu:* Fragnesia pojawiła się jako **niezamierzony skutek uboczny jednej z poprawek pierwotnych podatności Dirty Frag**. Poprawianie Dirty Frag stworzyło nowy, niezależny błąd dający roota.

### CVE-2026-80521: ucieczka z kontenera, która wygrała kernelCTF

Wyścig AF_UNIX kończy dyskusję o tym, czy to tylko teoria.

Podatność to **heap use-after-free** w mechanizmie garbage collection dla komunikatów `SCM_RIGHTS`, których procesy używają do przekazywania deskryptorów plików. Wyścig podczas zbierania cyklicznego odwołania do gniazda zwalnia `struct unix_vertex`, chociaż pierścień SCC przetrwałego gniazda nadal wskazuje ten obiekt. Podczas następnego przebiegu garbage collection kernel przechodzi po nieaktualnym pierścieniu i odwołuje się do zwolnionej pamięci.

Dlaczego ma to znaczenie nie tylko dla Linuksa: **AF_UNIX stanowi podstawę lokalnego IPC.** Korzystają z niego lokalne bazy danych, `systemd` i sam Docker. DepthFirst informuje, że podatność dotyczy większości sandboxów na poziomie systemu operacyjnego opartych na kernelu, **w tym `nsjail`, `Firejail` i `Bubblewrap`**, oraz nowoczesnych środowisk uruchomieniowych kontenerów.

DepthFirst **zdobyło miejsce w Google kernelCTF** dzięki tej podatności **24 lipca 2026 roku**, a potwierdzenie w kategorii `lts-6.12.95` otrzymało **5 sierpnia**. Tego samego dnia zgłosiło błąd do `security@kernel.org` i dowiedziało się, że **Kyle z OpenAI zgłosił tę samą podatność**. Poprawka trafiła do upstreamu **6 sierpnia**, a wyniki badań opublikowano **22 września**.

Zespół opublikował działający exploit dla **Ubuntu 26.04** oraz drugi exploit, który ucieka z **Ubuntu 24.04** przez CVE-2026-52910.

{{< figure src="kernel-page-cache-overwrite-container-escape.webp" alt="Diagram przedstawia nieuprzywilejowany proces w kontenerze uszkadzający stronę page cache, aby zmodyfikować plik setuid w pamięci. Proces zdobywa roota i wychodzi poza granicę kontenera do kernela hosta." >}}

## Dlaczego zalecenia dotyczące zabezpieczeń zawodzą

W tym roku obrońcy otrzymali trzy rundy obejść, a każda okazała się częściowo błędna.

| Zabezpieczenie | Co zatrzymuje | Czego nie obejmuje |
|---|---|---|
| Umieszczenie **`algif_aead`** na czarnej liście | Copy Fail | **Nic z Dirty Frag**, który całkowicie ignoruje ten moduł |
| Umieszczenie **`esp4`, `esp6` i `rxrpc`** na czarnej liście | Dirty Frag i Fragnesia | Zespoły potrzebujące IPsec. Nie obejmuje też zupełnie nowych podsystemów |
| Ograniczenie **nieuprzywilejowanych user namespaces** | Odmiany ESP | Odmiana RxRPC nie wymaga przestrzeni nazw. Polityka AppArmor to tylko **częściowa** ochrona |
| **Poprawienie kernela** | Podatność objęta poprawką | Następny błąd i błędy wprowadzone przez poprawkę |

Widać dwa wzorce.

**Po pierwsze, obejścia są ze sobą sprzeczne.** Copy Fail można ograniczyć przez wyłączenie `algif_aead`. Dirty Frag działa **niezależnie od tego**, czy moduł istnieje. Fragnesia wymaga wyłączenia `esp4` i `esp6`, co jest problemem dla wszystkich używających IPsec. Nie ma jednej czarnej listy modułów obejmującej całą rodzinę.

**Po drugie, co gorsza, poprawianie nie gwarantuje sukcesu.** Fragnesia została **wprowadzona przez poprawkę dla Dirty Frag**. Każda poprawka niesie ryzyko nowych błędów logicznych, a w tym podsystemie błąd logiczny staje się exploitem dającym roota.

*Niepokojący wniosek: wszystkie te podatności dotyczą page cache, są osiągalne z nieuprzywilejowanego kodu i zostały znalezione narzędziami, które poprawiają się co kwartał. Żadna lista blokad nie pozostaje kompletna.*

## Kontrargument, na który warto odpowiedzieć uczciwie

Istnieje uzasadniony zarzut, który zasługuje na bezpośrednią odpowiedź: **hypervisory też mają błędy.**

Powierzchnia ataku KVM jest realna. Google prowadzi **kvmCTF** właśnie po to, by znajdować takie błędy, i oferuje za nie wysokie nagrody:

| Poziom | Nagroda |
|---|---|
| **Pełna ucieczka z VM** | **$250,000** |
| Dowolny zapis do pamięci | $100,000 |
| Dowolny odczyt z pamięci | $50,000 |
| Względny zapis do pamięci | $50,000 |
| Odmowa usługi | $20,000 |
| Względny odczyt z pamięci | $10,000 |

Nagrody nie sumują się. Celem jest kernel LTS Linuksa z KVM, a maszyną gościa Debian 12.5. Celem jest **atak z gościa na hosta**.

**Hyunwoo Kim, ten sam badacz, który odkrył Dirty Frag, zdobywa też nagrody KVM** i wygrał pełne $250,000 za ucieczkę z VM. Uczciwe podsumowanie jest takie, że błędy występują na obu warstwach, a czasem znajduje je ta sama osoba.

**Porównaj skalę:**

| | Kernel Linuksa | Hypervisor KVM |
|---|---|---|
| **CVE w 2026 roku** | Prawie **6000** | Garstka, pojedynczy badacze znajdują kilka rocznie |
| **Dostępne z poziomu** | Dowolnego nieuprzywilejowanego procesu przez interfejs wywołań systemowych | Tylko kodu działającego już w maszynie gościa |
| **Powierzchnia ataku** | Wszystko: sieci, systemy plików, kryptografia, IPC i sterowniki | Interfejs urządzeń wirtualnych i hypercalli |
| **Klasa błędów** | Dowolny błąd bezpieczeństwa pamięci lub logiki w 30 mln wierszy | Ograniczona do granicy wirtualizacji |

*Różnica wynosi wiele rzędów wielkości, a nie dwukrotność. Dlatego mikroVM zmieniają ocenę ryzyka.*

## Co zapewnia prawdziwą granicę

**MikroVM** daje każdemu obciążeniu własną **instancję kernela** działającą na sprzętowej wirtualizacji, zamiast współdzielić kernel hosta za pomocą przestrzeni nazw.

Warto znać trzy warstwy stosu:

- **Procesor** udostępnia mechanizmy sprzętowe izolujące regiony pamięci.
- **KVM** udostępnia te mechanizmy kernelowi Linuksa, dzięki czemu kernel działa jak hypervisor.
- **VMM (monitor maszyny wirtualnej)**, taki jak Firecracker lub QEMU, steruje KVM, aby tworzyć i uruchamiać maszynę gościa.

Ponieważ gość uruchamia własny kernel, exploit kernela **wewnątrz gościa** narusza tylko tę maszynę. Nie ma współdzielonego kernela do zaatakowania. Atakujący musi następnie uciec z hypervisora, którego mniejsza powierzchnia obejmuje błędy KVM.

W praktyce liczą się dwie implementacje, obie wymienione w zaleceniu DepthFirst:

| Technologia | Podejście | Uwagi |
|---|---|---|
| **Firecracker** | Specjalnie zaprojektowany VMM z minimalnym modelem urządzeń | Stworzony przez AWS z myślą o izolacji wielu dzierżawców na dużą skalę |
| **Kata Containers** | Runtime zgodny z OCI, który opakowuje mikroVM | Uruchamia standardowe obrazy kontenerów z granicą VM pod spodem |

Dla większości zespołów Kata jest łatwiejszą migracją, ponieważ obsługuje używane już obrazy i narzędzia kontenerów. **Firecracker ma mniejszą powierzchnię ataku**, ponieważ emuluje znacznie mniej urządzeń niż uniwersalny VMM.

{{< figure src="microvm-vs-container-isolation-boundary.webp" alt="Diagram porównuje izolację kontenera przez przestrzenie nazw współdzielonego kernela z izolacją mikroVM, gdzie każde obciążenie ma własny kernel nad KVM i monitorem maszyny wirtualnej." >}}

## Co zrobić teraz

Nie każdy kontener wymaga mikroVM. Decyzja zależy od tego, **czyj kod w nim działa**.

| Twoja sytuacja | Ryzyko | Co zrobić |
|---|---|---|
| **Uruchamiasz własny kod**, jeden dzierżawca | Niskie | Zostań przy kontenerach. Szybko instaluj poprawki, odbieraj zbędne capabilities i używaj systemu plików root tylko do odczytu |
| **Hosty wielu dzierżawców**, dostęp shell dla użytkowników | **Wysokie** | Przenieś niezaufane obciążenia do mikroVM. To pierwszy przypadek wskazany przez DepthFirst |
| **Runnery CI uruchamiające niezaufane PR-y** | **Wysokie** | Pull request może uzyskać roota na runnerze. Izoluj każde zadanie we własnej VM |
| **Notebooki, sandboxy agentów, serverless** | **Wysokie** | Kod dzierżawcy staje się rootem hosta. Jedna mikroVM na dzierżawcę |
| **Klastry Kubernetes** | **Podwyższone** | Page cache jest współdzielony na hoście. Pod z odpowiednimi prymitywami narusza węzeł i przekracza granice dzierżawców |

Wspólna zasada jest prosta. **Kontenery świetnie służą do pakowania aplikacji i izolacji procesów.** Nigdy nie zaprojektowano ich do powstrzymywania wrogiego kodu. Branża po cichu zaczęła używać ich w tym celu, ponieważ były wygodne i tanie.

### Utwardzanie, które zawsze pomaga

Żadne z tych działań nie zastępuje granicy VM, ale każde usuwa łatwe ścieżki ataku:

```bash
# Wyłącz niepotrzebne moduły wykorzystywane przez rodzinę page-cache
printf 'install algif_aead /bin/false\ninstall esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' \
  > /etc/modprobe.d/harden-pagecache-family.conf
rmmod algif_aead esp4 esp6 rxrpc 2>/dev/null || true
```

```bash
# Ogranicz nieuprzywilejowane przestrzenie nazw użytkowników, co blokuje warianty ESP
# Debian i Ubuntu: to częściowe ograniczenie skutków, nie pełne rozwiązanie
sysctl -w kernel.unprivileged_userns_clone=0

# Przy podejrzeniu wykorzystania opróżnij page cache, aby usunąć zmodyfikowane pliki binarne z pamięci
echo 1 | tee /proc/sys/vm/drop_caches
```

```text
# Wstępne sygnały wykrywania
- Nieoczekiwane unshare(CLONE_NEWUSER) z obciążenia bez uzasadnionego powodu
- Aktywność NETLINK_XFRM lub skojarzenia bezpieczeństwa XFRM poza hostami IPsec
- Żądania powiązania gniazd AF_ALG
- Ładowanie esp4, esp6 lub rxrpc na hostach bez IPsec i AFS
```

> **Ostrzeżenie: `drop_caches` usuwa zmodyfikowaną kopię z pamięci i tym samym czyści uszkodzenie, ale nie usuwa atakującego, który uzyskał już roota. Traktuj to jako reagowanie na incydent, a nie naprawę.**

### Problem z tempem instalowania poprawek

Nawet przy najlepszych intencjach instalowanie poprawek kernela stało się wyścigiem:

- Prawie **6000 opublikowanych w tym roku CVE** przekracza samą liczbą możliwości większości okien serwisowych.
- **Poprawka wprowadza błąd.** Fragnesia to potwierdziła w tym właśnie podsystemie.
- **Lista środków zaradczych szybko się starzeje.** W kwietniu odpowiedzią było `algif_aead`. W maju nie obejmowała już niczego z Dirty Frag.

*Szybkie instalowanie poprawek jest konieczne, ale niewystarczające. Architektura decyduje, czy pominięta poprawka oznacza ograniczony incydent, czy przejęcie hosta.*

## Trudniejsze pytanie: kto jest przeciwnikiem?

Odpowiedź techniczna jest jasna. Strategiczna zależy od pytania pomijanego przez większość zespołów.

**Jeśli w twoim modelu zagrożeń pojawia się ciekawski użytkownik lub nieostrożny programista, kontenery nadal wystarczą.** Ucieczka z kontenera wymaga lokalnego wykonania kodu i exploita kernela. Żadne z nich nie jest banalne, a koszty operacyjne przeniesienia wszystkiego do mikroVM są realne.

**Jeśli model zagrożeń obejmuje przeciwnika uruchamiającego kod w twojej infrastrukturze, kontenery są teraz tylko progiem zwalniającym.** Wniosek DepthFirst warto przytoczyć wprost:

> "Próg wejścia dla uzbrajania tych podatności spadł tak bardzo, że musimy zakładać, iż atakujący potrafią w dowolnej chwili uciec ze standardowych kontenerów."

To dostawca zabezpieczeń z produktem do sprzedania, który opowiada się za konkretną architekturą. Sceptycyzm wobec takiego argumentu jest uzasadniony. **Argument nie zależy jednak od tego dostawcy.** Liczba 6000 CVE jest publiczna, exploity opublikowano, a kernel z założenia jest współdzielony.

*Uczciwe ujęcie: wobec atakującego z przyczółkiem wartość kontenerów jako granicy spada, a wobec całej reszty pozostaje taka sama.*

## Werdykt

**Kontenery nadal są właściwym narzędziem do pakowania, wdrażania i separacji procesów. Nie są już niezawodną granicą bezpieczeństwa dla wrogiego kodu.**

Trzy stwierdzenia, od najbardziej pewnego:

1. **Techniczna podstawa jest bezsporna.** Kontenery współdzielą kernel hosta. Każda z czterech podatności w tym artykule przekroczyła granicę z nieuprzywilejowanego konta, a exploity są publiczne.
2. **AI zmieniło tempo, nie zasadę.** LPE kernela istniały zawsze. Znalezienie jednego kosztuje teraz około **godziny skanowania AI** zamiast miesięcy pracy eksperta. Dwie organizacje niezależnie znalazły ten sam zero-day tego samego dnia.
3. **Migracja kosztuje, podobnie jak jej brak.** Firecracker i Kata zwiększają narzut, złożoność operacyjną i wymagania dotyczące umiejętności. Wybór jest prosty: zaakceptuj narzut albo przyjmij, że błąd kernela oznacza przejęcie hosta.

**Jeśli zarządzasz infrastrukturą wielu dzierżawców albo uruchamiasz niezaufany kod, już teraz zaplanuj migrację do mikroVM.** Nie dlatego, że zbliża się katastrofa, lecz dlatego, że kierunek jest jasny, a migracja zajmuje kwartały, nie tygodnie.

**Jeśli uruchamiasz kontenery z własnym kodem dla jednego dzierżawcy, zostań przy nich.** Instaluj poprawki kernela szybciej niż dotychczas, wyłącz niepotrzebne moduły i wróć do tej decyzji, gdy pojawi się niezaufany kod.

*Kończy się epoka traktowania kernela jako bezwarunkowo zaufanej granicy. Infrastruktura zakładająca, że kernel zostanie naruszony, jest infrastrukturą, która przetrwa naruszenie.*

## Najważniejsze wnioski

- **Kontenery współdzielą kernel hosta.** Izolację zapewniają przestrzenie nazw wywołania systemowego `clone`, a nie wirtualizacja sprzętowa, więc błąd kernela jest też błędem kontenera.
- **Cztery podatności z 2026 roku przekroczyły granicę** z nieuprzywilejowanych kont lokalnych: Copy Fail, Dirty Frag, Fragnesia i CVE-2026-80521. Wszystkie atakują page cache.
- **Do września 2026 roku opublikowano prawie 6000 CVE kernela**, a narzędzia AI przyspieszają ich znajdowanie. **Copy Fail znaleziono w około godzinę skanowania.**
- **Fragnesia pojawiła się w poprawce Dirty Frag.** Instalowanie poprawki doprowadziło do nowego błędu z uprawnieniami roota w tym samym podsystemie.
- **Obejście Copy Fail nie zatrzymuje Dirty Frag.** Czarna lista `algif_aead` obejmuje jedną podatność i niczego więcej z tej rodziny.
- **CVE-2026-80521 złamało też `nsjail`, `Firejail` i `Bubblewrap`**, nie tylko środowiska uruchomieniowe kontenerów.
- **MikroVM zmieniają ocenę ryzyka**, bo każde obciążenie otrzymuje własny kernel. KVM ma błędy, ale jego powierzchnia ataku jest o wiele rzędów wielkości mniejsza.
- **Wybieraj zależnie od tego, kto uruchamia kod.** Własny kod w kontenerze jednego dzierżawcy to niskie ryzyko. Niezaufany kod na współdzielonym hoście grozi przejęciem hosta.

## Następne kroki

1. **Przeczytaj analizę problemu** i opublikowanego exploita: **[Kontenery nie są już granicą bezpieczeństwa - DepthFirst](https://depthfirst.com/research/containers-are-no-longer-safe)**
2. **Sprawdź wiarygodne zalecenia i środki zaradcze** dla rodziny Copy Fail: **[CERT/CC VU#260001](https://www.kb.cert.org/vuls/id/260001/)**
3. **Przeczytaj techniczny opis Dirty Frag**, aby zrozumieć łączenie podatności i przyczynę nieskuteczności ochrony `algif_aead`: **[Techniczny opis Dirty Frag](https://github.com/V4bel/dirtyfrag)**
4. **Sprawdź zasady i poziomy nagród kvmCTF**, aby zobaczyć rozmiar powierzchni ataku hypervisora: **[Omówienie kvmCTF](https://google.github.io/security-research/kvmctf/rules.html)**
5. **Oceń te CVE we własnym środowisku** naszym narzędziem działającym po stronie klienta: **[Kalkulator CVSS v3.1](/cvss-calculator/)**
6. **Zabezpiecz to, co uruchamiasz teraz**: **[Jak zabezpieczyć środowisko Docker i Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/)**
7. **Poznaj dokładniej kompromisy izolacji**: **[Docker a maszyny wirtualne 2026](/articles/docker-vs-vms/)**
8. **Ogranicz uprawnienia tam, gdzie nie możesz dodać granicy**: **[Zarządzanie zasadą najmniejszych uprawnień w Linuksie](/articles/mastering-least-privilege-access-control-linux/)**

## Powiązane artykuły

| Artykuł | Zakres |
|---|---|
| **[Docker a maszyny wirtualne 2026](/articles/docker-vs-vms/)** | Porównanie architektury stanowiące podstawę tego artykułu, z kompromisami dotyczącymi wydajności i bezpieczeństwa |
| **[Jak zabezpieczyć środowisko Docker i Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/)** | Praktyczne utwardzanie warstwy kontenerów, nadal przydatne wewnątrz mikroVM |
| **[Docker w LXC na Proxmox: niezawodność, dowody i migracja do VM](/articles/docker-in-lxc-proxmox-reliability/)** | Kontenery zagnieżdżone, dowody i moment przeniesienia obciążenia do pełnej VM |
| **[Podstawy wirtualizacji: koncepcje i zastosowania](/articles/understanding-virtualization_-concepts-and-applications/)** | Podstawy hypervisora, w tym funkcje procesora, od których zależą mikroVM |
| **[Zarządzanie zasadą najmniejszych uprawnień w Linuksie](/articles/mastering-least-privilege-access-control-linux/)** | Ograniczanie uprawnień, które dałaby ucieczka, aby zmniejszyć jej zasięg |

## Źródła

1. [Kontenery nie są już granicą bezpieczeństwa - DepthFirst (Zhenpeng Lin, 22 września 2026)](https://depthfirst.com/research/containers-are-no-longer-safe)
2. [CERT/CC Vulnerability Note VU#260001 - Copy Fail (CVE-2026-31431)](https://www.kb.cert.org/vuls/id/260001/)
3. [Oficjalna publikacja Copy Fail i analiza exploita](https://copy.fail/)
4. [Techniczny opis Dirty Frag - Hyunwoo Kim (CVE-2026-43284, CVE-2026-43500)](https://github.com/V4bel/dirtyfrag)
5. [Fragnesia: lokalne podniesienie uprawnień w kernelu Linuksa przez ESP-in-TCP - Wiz (CVE-2026-46300)](https://www.wiz.io/blog/fragnesia-linux-kernel-local-privilege-escalation-via-esp-in-tcp)
6. [Omówienie kvmCTF i poziomy nagród - Google](https://google.github.io/security-research/kvmctf/rules.html)
7. [Wpis NVD dla CVE-2026-31431](https://nvd.nist.gov/vuln/detail/CVE-2026-31431)
8. [Upstreamowy commit mainline z poprawką Copy Fail](https://github.com/torvalds/linux/commit/a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5)
9. [Komunikat bezpieczeństwa Ubuntu o poprawkach Copy Fail](https://ubuntu.com/blog/copy-fail-vulnerability-fixes-available)
10. [Exploity kernelCTF i zgłoszenia - Google Security Research](https://github.com/google/security-research/tree/master/pocs/linux/kernelctf)

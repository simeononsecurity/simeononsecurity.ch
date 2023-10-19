---
title: "Podstawowe najlepsze praktyki wzmacniania zabezpieczeń systemu Windows dla bezpiecznych systemów Windows 10 i Windows 11"
date: 2023-07-27
toc: true
draft: false
description: "Odkryj skuteczne strategie zwiększania bezpieczeństwa systemów Windows 10 i Windows 11 dzięki kompleksowym technikom wzmacniania zabezpieczeń i najlepszym praktykom."
genre: ["Hartowanie systemu Windows", "Bezpieczeństwo systemu Windows", "Uodparnianie systemu Windows 10", "Uodparnianie systemu Windows 11", "Najlepsze praktyki bezpieczeństwa systemu Windows", "Wskazówki dotyczące bezpieczeństwa systemu Windows", "Wytyczne dotyczące bezpieczeństwa systemu Windows", "Zabezpieczanie systemów operacyjnych Windows", "Wzmocnienie systemu Windows", "Środki bezpieczeństwa systemu Windows"]
tags: ["Hartowanie systemu Windows", "Bezpieczeństwo systemu Windows", "Windows 10", "Windows 11", "bezpieczeństwo systemu operacyjnego", "Windows Defender", "Kontrola konta użytkownika", "Szyfrowanie BitLocker", "konfiguracja zapory sieciowej", "Zasady AppLocker", "Aktualizacje systemu Windows", "silne hasła", "kopia zapasowa danych", "Windows Hello", "Bezpieczny rozruch", "TPM", "Microsoft Defender Antivirus", "Windows Sandbox", "Microsoft Defender Application Guard", "Kontrolowany dostęp do folderów", "Najlepsze praktyki zabezpieczania systemów Windows 10 i Windows 11", "Jak wzmocnić systemy operacyjne Windows", "Środki bezpieczeństwa systemu Windows dla użytkowników indywidualnych i organizacji", "Zwiększanie bezpieczeństwa systemu Windows", "Ochrona danych za pomocą szyfrowania BitLocker", "Izolowanie sesji przeglądarki za pomocą Microsoft Defender Application Guard", "Wskazówki i wytyczne dotyczące bezpieczeństwa systemu Windows 10", "Wdrażanie funkcji zabezpieczeń systemu Windows", "Zabezpieczanie systemu Windows za pomocą izolacji sprzętowej", "Zapewnienie integralności systemu Windows"]
cover: "/img/cover/A_cartoon_illustration_of_a_shield_protecting-windows.png"
coverAlt: "Kreskówkowa ilustracja przedstawiająca tarczę chroniącą logo Windows przed różnymi cyberzagrożeniami."
coverCaption: "Zabezpiecz swoją twierdzę Windows za pomocą skutecznych technik hartowania."
---

## Wprowadzenie

Systemy operacyjne Windows są powszechnie używane przez użytkowników indywidualnych i organizacje na całym świecie. Aby zapewnić bezpieczeństwo i integralność tych systemów, konieczne jest wdrożenie **najlepszych praktyk hartowania systemu Windows**. Hartowanie polega na zabezpieczeniu systemu operacyjnego poprzez zmniejszenie jego powierzchni ataku i złagodzenie potencjalnych luk w zabezpieczeniach. W tym artykule przeanalizujemy najlepsze praktyki w zakresie zabezpieczania zarówno **Windows 10**, jak i nowszych **Windows 11** systemów operacyjnych, dostarczając cennych informacji w celu zwiększenia bezpieczeństwa środowiska Windows.

______

## Zrozumienie zabezpieczeń systemu Windows

Hartowanie systemu Windows to proces zwiększania bezpieczeństwa systemu operacyjnego Windows. Obejmuje konfigurację różnych ustawień i wdrażanie środków bezpieczeństwa w celu ochrony przed nieautoryzowanym dostępem, złośliwym oprogramowaniem i innymi zagrożeniami. Dzięki wzmocnieniu systemu Windows można zminimalizować ryzyko związane z cyberatakami i zapewnić poufność, integralność i dostępność danych.

### [Hardening Windows 10](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 10 jest jednym z najczęściej używanych systemów operacyjnych na świecie. Aby wzmocnić środowisko Windows 10, należy rozważyć następujące najlepsze praktyki:

#### 1. [**Enable Windows Defender**](https://github.com/simeononsecurity/Windows-Defender-Hardening)

Windows Defender to **rozbudowane rozwiązanie antywirusowe** dołączone do systemu Windows 10. Oferuje szereg funkcji bezpieczeństwa, które chronią system przed różnymi rodzajami **złośliwego oprogramowania**, w tym **wirusami, oprogramowaniem szpiegującym i ransomware**. Włączając Windows Defender, można znacznie zwiększyć bezpieczeństwo środowiska Windows 10.

Aby włączyć Windows Defender, wykonaj następujące kroki:

- Otwórz aplikację **Windows Security**, klikając ikonę Windows Security na pasku zadań lub wyszukując "Windows Security" w menu Start.
- W aplikacji Windows Security kliknij "**Ochrona przed wirusami i zagrożeniami**" w lewym panelu nawigacyjnym.
- Kliknij "**Zarządzaj ustawieniami**" w sekcji "Ustawienia ochrony przed wirusami i zagrożeniami".
- Upewnij się, że przełącznik "**Ochrona w czasie rzeczywistym**" jest ustawiony na "**Włączony**". Umożliwi to programowi Windows Defender aktywne skanowanie i ochronę systemu w czasie rzeczywistym.
- Dodatkowo, możesz dostosować opcje skanowania i wykluczenia, klikając odpowiednio "**Opcje skanowania**" i "**Dodaj lub usuń wykluczenia**".

Ważne jest, aby **regularnie aktualizować** Windows Defender, aby upewnić się, że ma najnowsze **definicje złośliwego oprogramowania** i **ulepszenia bezpieczeństwa**. Microsoft regularnie publikuje aktualizacje, aby wyeliminować nowe zagrożenia i luki w zabezpieczeniach. Aby zaktualizować program Windows Defender, wykonaj następujące kroki:

- Otwórz aplikację Zabezpieczenia systemu Windows.
- Przejdź do "**Ochrona przed wirusami i zagrożeniami**" w lewym panelu nawigacyjnym.
- Kliknij "**Sprawdź aktualizacje**" w sekcji "Aktualizacje ochrony przed wirusami i zagrożeniami".
- System Windows sprawdzi dostępność aktualizacji i w razie potrzeby pobierze/zainstaluje je.

Włączając i aktualizując program Windows Defender, można aktywnie chronić system Windows 10 przed złośliwym oprogramowaniem i innymi zagrożeniami bezpieczeństwa. Zaleca się również **regularne skanowanie systemu** za pomocą Windows Defender, aby zapewnić wykrywanie i usuwanie wszelkich potencjalnych zagrożeń.

Pamiętaj, że chociaż Windows Defender zapewnia solidny poziom ochrony, to ważne jest, aby uzupełnić go **bezpiecznymi nawykami przeglądania**, **regularnymi aktualizacjami oprogramowania** i innymi środkami bezpieczeństwa w celu utrzymania bezpiecznego środowiska Windows 10.

#### 2. [**Keep Windows 10 Updated**](https://support.microsoft.com/en-us/windows/windows-update-faq-8a903416-6f45-0718-f5c7-375e92dddeb2)
Regularne instalowanie aktualizacji systemu Windows jest krytycznym aspektem **utrwalania systemu Windows 10**. Aktualizacje te zawierają **poprawki bezpieczeństwa**, poprawki błędów i ulepszenia wydajności, które pomagają **załatać luki w zabezpieczeniach** i poprawić stabilność systemu.

Microsoft wydaje **regularne aktualizacje** dla systemu Windows 10, aby rozwiązać nowo wykryte błędy bezpieczeństwa i poprawić ogólne wrażenia użytkownika. Aktualizując system, zapewniasz, że system operacyjny ma najnowsze **ulepszenia bezpieczeństwa**, aby chronić się przed pojawiającymi się zagrożeniami.

Aby aktualizować system Windows 10, wykonaj następujące kroki:

1. **Włącz automatyczne aktualizacje**: Domyślnie system Windows 10 jest skonfigurowany do automatycznego pobierania i instalowania aktualizacji. Zapewnia to, że system otrzymuje niezbędne aktualizacje bez ręcznej interwencji. Aby sprawdzić, czy automatyczne aktualizacje są włączone, wykonaj następujące kroki:
   - Przejdź do **Ustawień**, klikając menu Start i wybierając ikonę koła zębatego.
   - Kliknij na **Update & Security**.
   - W lewym panelu nawigacyjnym kliknij **Windows Update**.
   - Upewnij się, że opcja **"Automatycznie "** jest zaznaczona w sekcji **"Ustawienia Windows Update "**. Jeśli nie jest zaznaczona, kliknij link **"Zmień aktywne godziny "**, aby dostosować aktywne godziny, w których system Windows powinien unikać instalowania aktualizacji.

2. **Ręczna instalacja aktualizacji**: Jeśli wolisz mieć większą kontrolę nad procesem aktualizacji, możesz ręcznie zainstalować aktualizacje w systemie Windows 10. Oto jak to zrobić:
   - Przejdź do **Ustawienia** > **Update & Security** > **Windows Update**.
   - Kliknij **"Sprawdź aktualizacje "**, aby sprawdzić, czy dostępne są jakiekolwiek aktualizacje dla twojego systemu.
   - Jeśli aktualizacje zostaną znalezione, kliknij **"Pobierz "** i **"Zainstaluj "**, aby rozpocząć proces instalacji.

Należy podkreślić znaczenie **regularnego restartowania systemu** po zainstalowaniu aktualizacji. Niektóre aktualizacje mogą wymagać ponownego uruchomienia systemu, aby w pełni zastosować zmiany i zapewnić ich skuteczność.

**Dbając o aktualizację systemu Windows 10**, nie tylko zwiększasz jego bezpieczeństwo, ale także korzystasz z najnowszych funkcji, ulepszeń wydajności i poprawek zgodności. Jest to proaktywny środek zapewniający odporność systemu na potencjalne zagrożenia bezpieczeństwa.

#### 3. [**Configure User Account Control (UAC)**](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-overview)
Kontrola konta użytkownika (UAC) to funkcja zabezpieczeń w systemie Windows 10, która pomaga zapobiegać nieautoryzowanym zmianom w systemie, wyświetlając w razie potrzeby monit o zatwierdzenie przez administratora. Działa jako zabezpieczenie przed złośliwym oprogramowaniem lub nieautoryzowanymi użytkownikami próbującymi wprowadzić zmiany, które mogą mieć wpływ na bezpieczeństwo lub stabilność systemu.

Konfiguracja ustawień UAC na odpowiednim poziomie ma kluczowe znaczenie dla **utwardzenia systemu Windows 10**. Obejmuje ona znalezienie równowagi między bezpieczeństwem a użytecznością, aby zapewnić, że UAC skutecznie chroni system bez powodowania niepotrzebnych zakłóceń.

Aby skonfigurować ustawienia UAC w systemie Windows 10, można wykonać następujące kroki:

1. Otwórz **Panel sterowania**, wpisując "Panel sterowania" w pasku wyszukiwania i wybierając go z wyników wyszukiwania.

2. W Panelu sterowania kliknij na **"Konta użytkowników "**.

3. Kliknij na **"Zmień ustawienia kontroli konta użytkownika "**.

4. Zobaczysz suwak z różnymi poziomami ustawień UAC. Oto dostępne opcje:
   - **"Zawsze powiadamiaj "**: Jest to najwyższy poziom zabezpieczeń UAC, w którym użytkownik jest proszony o zgodę na wszelkie zmiany w systemie, nawet w przypadku prostych zadań.
   - **"Powiadamiaj mnie tylko wtedy, gdy aplikacje próbują wprowadzić zmiany na moim komputerze (domyślnie)": Jest to zalecane ustawienie, które zapewnia równowagę między bezpieczeństwem a użytecznością. Użytkownik jest pytany o zgodę, gdy aplikacje wprowadzają zmiany, ale nie w przypadku zmian ustawień systemu Windows.
   - "Powiadamiaj mnie tylko wtedy, gdy aplikacje próbują wprowadzić zmiany na moim komputerze (nie przyciemniaj pulpitu) "**: Podobna do poprzedniej opcji, ale pulpit nie jest przyciemniany, gdy pojawiają się monity UAC.
   - **"Nigdy nie powiadamiaj "**: Jest to najniższy poziom zabezpieczeń UAC, w którym nie są wyświetlane żadne monity o zmiany w systemie.

5. Wybierz poziom zabezpieczeń UAC, który odpowiada Twoim potrzebom, przesuwając suwak do żądanej pozycji.

6. Kliknij **"OK "**, aby zapisać zmiany.

Zaleca się, aby UAC był włączony i ustawiony na poziomie, który zapewnia odpowiednią równowagę między bezpieczeństwem a użytecznością. Całkowite wyłączenie UAC może sprawić, że system będzie bardziej podatny na nieautoryzowane zmiany i potencjalnie zagrozi jego bezpieczeństwu.

Konfigurując ustawienia UAC, zwiększasz bezpieczeństwo swojego systemu Windows 10, zapewniając, że uprawnienia administracyjne są wymagane do krytycznych zmian w systemie, zmniejszając ryzyko nieautoryzowanego dostępu i infekcji złośliwym oprogramowaniem.

#### 4. [**Use Strong Passwords**](https://simeononsecurity.com/articles/how-to-create-strong-passwords/)
Używanie silnych haseł jest niezbędne do utrzymania bezpieczeństwa systemu Windows 10 i ochrony przed nieautoryzowanym dostępem. Słabe lub łatwe do odgadnięcia hasła mogą sprawić, że system będzie podatny na ataki, takie jak ataki siłowe lub łamanie haseł.

Aby upewnić się, że wszystkie konta użytkowników w systemie Windows 10 mają silne hasła, postępuj zgodnie z tymi najlepszymi praktykami dotyczącymi haseł:

1. **Złożoność**: Zachęcaj użytkowników do tworzenia haseł, które są złożone i niełatwe do odgadnięcia. Silne hasło powinno zawierać kombinację wielkich i małych liter, cyfr i znaków specjalnych. Unikaj używania popularnych słów lub przewidywalnych wzorców.

2. **Długość**: Dłuższe hasła są generalnie bezpieczniejsze. Zachęcaj użytkowników do tworzenia haseł o długości co najmniej 8 znaków, a najlepiej dłuższych. Im więcej znaków w haśle, tym trudniej je złamać.

3. **Unikalność**: Każde konto użytkownika powinno mieć unikalne hasło. Używanie tego samego hasła do wielu kont zwiększa ryzyko naruszenia bezpieczeństwa. Zachęcaj użytkowników do używania różnych haseł dla różnych kont.

4. **Unikaj danych osobowych**: Należy odradzać użytkownikom używanie w hasłach informacji osobistych, takich jak imiona i nazwiska, daty urodzenia lub adresy. Informacje te mogą być łatwo uzyskane lub odgadnięte przez atakujących.

5. **Menedżery haseł**: Rozważ korzystanie z menedżera haseł do bezpiecznego przechowywania haseł i zarządzania nimi. Menedżery haseł mogą generować silne, unikalne hasła dla każdego konta i przechowywać je w zaszyfrowanej bazie danych.

6. **Regularna zmiana haseł**: Zachęcaj użytkowników do okresowej zmiany haseł w celu zachowania bezpieczeństwa. Ustal zasady dotyczące wygaśnięcia hasła i poinformuj użytkowników o znaczeniu regularnego aktualizowania haseł.

Wdrażając silne praktyki dotyczące haseł, znacznie zwiększasz bezpieczeństwo swojego systemu Windows 10 i zmniejszasz ryzyko nieautoryzowanego dostępu lub naruszenia danych. Regularnie edukuj użytkowników w zakresie bezpieczeństwa haseł i udostępniaj zasoby, takie jak mierniki siły hasła lub wytyczne dotyczące tworzenia haseł, aby pomóc im w tworzeniu silnych haseł.

Więcej szczegółowych informacji na temat tworzenia silnych haseł i najlepszych praktyk można znaleźć tutaj [article](https://simeononsecurity.com/articles/how-to-create-strong-passwords/) Zapewnia kompleksowe wskazówki dotyczące bezpieczeństwa haseł i oferuje porady dotyczące tworzenia silnych i łatwych do zapamiętania haseł.

Należy pamiętać, że używanie silnych haseł jest podstawowym aspektem bezpieczeństwa systemu i powinno być traktowane priorytetowo w celu ochrony poufnych danych i zapewnienia integralności środowiska Windows 10.

#### 5. [**Enable BitLocker Encryption**](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)
Jednym z najskuteczniejszych sposobów ochrony poufnych danych w systemie Windows 10 jest włączenie szyfrowania BitLocker. BitLocker zapewnia szyfrowanie całego dysku, dzięki czemu nawet w przypadku zgubienia lub kradzieży urządzenia dane pozostają bezpieczne i niedostępne dla nieupoważnionych osób.

Aby włączyć szyfrowanie BitLocker i zabezpieczyć poufne informacje, wykonaj następujące kroki:

1. **Sprawdź wymagania systemowe**: Upewnij się, że Twoja wersja systemu Windows 10 obsługuje szyfrowanie BitLocker. Funkcja BitLocker jest dostępna w wersjach Windows 10 Pro, Enterprise i Education.

2. **Włącz funkcję BitLocker**: Otwórz Panel sterowania i przejdź do kategorii "System i zabezpieczenia". Kliknij "Szyfrowanie dysków BitLocker" i wybierz dyski, które chcesz zaszyfrować. Postępuj zgodnie z instrukcjami wyświetlanymi na ekranie, aby rozpocząć proces szyfrowania.

3. **Wybierz opcje szyfrowania**: Podczas konfiguracji BitLocker będziesz mieć możliwość wyboru między różnymi metodami szyfrowania, takimi jak użycie hasła, karty inteligentnej lub obu. Wybierz odpowiednią metodę w oparciu o wymagania bezpieczeństwa i preferencje.

4. **Backup Recovery Key**: Bardzo ważne jest, aby utworzyć kopię zapasową klucza odzyskiwania BitLocker. Klucz ten działa jako zabezpieczenie na wypadek zapomnienia hasła lub napotkania jakichkolwiek problemów z dostępem do zaszyfrowanego dysku. Klucz odzyskiwania należy przechowywać w bezpiecznym miejscu, z dala od urządzenia.

5. **Zarządzanie ustawieniami funkcji BitLocker**: Po włączeniu funkcji BitLocker można dostosować dodatkowe ustawienia, takie jak automatyczne odblokowywanie określonych dysków lub konfigurowanie użycia modułu TPM (Trusted Platform Module) w celu zwiększenia bezpieczeństwa. Dostęp do tych ustawień można uzyskać za pośrednictwem interfejsu zarządzania funkcją BitLocker.

Włączenie szyfrowania BitLocker dodaje dodatkową warstwę ochrony do systemu Windows 10, zapewniając, że nawet jeśli urządzenie wpadnie w niepowołane ręce, dane pozostaną bezpieczne i niedostępne. Ważne jest, aby regularnie aktualizować i utrzymywać ustawienia BitLocker, aby być na bieżąco z najlepszymi praktykami bezpieczeństwa.

Więcej szczegółowych informacji na temat włączania i zarządzania szyfrowaniem BitLocker można znaleźć w oficjalnej sekcji [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview) Zapewnia kompleksowe wskazówki dotyczące szyfrowania BitLocker, w tym zaawansowane funkcje i opcje konfiguracji.

Pamiętaj, że włączenie szyfrowania BitLocker pomaga chronić poufne dane i zapewnia spokój ducha, wiedząc, że informacje są bezpieczne nawet w przypadku utraty lub kradzieży.

#### 6. **Wyłącz niepotrzebne usługi i funkcje**
Aby zwiększyć bezpieczeństwo systemu Windows 10, konieczne jest przejrzenie i wyłączenie wszelkich niepotrzebnych usług i funkcji. W ten sposób zmniejszysz powierzchnię ataku i zminimalizujesz możliwość wykorzystania przez złośliwe podmioty.

Oto kroki, aby wyłączyć niepotrzebne usługi i funkcje w systemie Windows 10:

1. **Zidentyfikuj niepotrzebne usługi**: Zacznij od zidentyfikowania usług uruchomionych w systemie. Otwórz konsolę zarządzania "Usługi", naciskając **klawisz Windows + R**, wpisując **services.msc** i naciskając **Enter**. Przejrzyj listę usług i sprawdź ich przeznaczenie, aby określić, które z nich są niezbędne dla funkcjonalności systemu.

2. **Wyłącz niepotrzebne usługi**: Po zidentyfikowaniu niepotrzebnych usług, kliknij prawym przyciskiem myszy na każdej z nich i wybierz **Właściwości**. W oknie Właściwości zmień **Typ uruchamiania** na **Wyłączony**. Zapobiegnie to automatycznemu uruchamianiu usługi po uruchomieniu systemu. Zachowaj ostrożność i upewnij się, że wyłączasz tylko te usługi, które nie są wymagane do normalnego działania systemu.

3. **Wyłącz niepotrzebne funkcje**: Oprócz usług, Windows 10 zawiera również różne funkcje, które mogą nie być niezbędne dla systemu. Otwórz **Panel sterowania**, przejdź do **Programów** lub **Programów i funkcji** i kliknij na **Włącz lub wyłącz funkcje systemu Windows**. Odznacz wszystkie funkcje, których nie potrzebujesz. Ten krok pomaga jeszcze bardziej zmniejszyć powierzchnię ataku i minimalizuje zasoby zużywane przez niepotrzebne funkcje.

4. **Regularnie przeglądaj i aktualizuj**: Bardzo ważne jest, aby regularnie przeglądać listę usług i funkcji włączonych w systemie Windows 10. Ponieważ wymagania systemu zmieniają się w czasie, może być konieczna ponowna ocena usług i funkcji, które są niezbędne. Zachowaj czujność i aktualizuj konfigurację w razie potrzeby.

Wyłączając niepotrzebne usługi i funkcje, ograniczasz potencjalne punkty wejścia dla atakujących i zmniejszasz ogólną powierzchnię ataku systemu Windows 10. Ta praktyka poprawia stan bezpieczeństwa systemu i zmniejsza ryzyko wykorzystania.

Więcej informacji na temat zarządzania usługami i funkcjami w systemie Windows 10 można znaleźć w następujących dokumentach [article](https://www.tweakhound.com/2015/07/27/windows-10-default-services/#:~:text=Windows%2010%20Default%20Services%20%20%20%20Name,%20%20%20%2044%20more%20rows%20) w celu uzyskania szczegółowych wskazówek.

Należy pamiętać, że podczas wyłączania usług i funkcji należy zachować ostrożność, ponieważ wyłączenie istotnych komponentów może negatywnie wpłynąć na funkcjonalność systemu. Przed wprowadzeniem jakichkolwiek zmian należy zawsze sprawdzić i zrozumieć cel usługi lub funkcji.

#### 7. **Wdrożenie reguł zapory sieciowej**
Wbudowana zapora sieciowa w systemie Windows 10 działa jako kluczowa linia obrony przed nieautoryzowanym ruchem sieciowym. Konfigurując reguły zapory, można kontrolować, które połączenia przychodzące i wychodzące są dozwolone, zwiększając w ten sposób bezpieczeństwo systemu.

Wykonaj poniższe kroki, aby zaimplementować reguły zapory sieciowej w systemie Windows 10:

1. **Dostęp do ustawień zapory sieciowej**: Aby uzyskać dostęp do ustawień zapory sieciowej, otwórz **Panel sterowania**, wyszukaj **Windows Defender Firewall** i kliknij odpowiedni wynik. Alternatywnie, możesz kliknąć prawym przyciskiem myszy przycisk **Uruchom**, wybrać **Ustawienia** i przejść do **Sieć i Internet > Zapora systemu Windows**.

2. **Skonfiguruj reguły przychodzące**: Reguły przychodzące kontrolują przychodzące połączenia sieciowe do systemu. Kliknij na **Ustawienia zaawansowane** w oknie Zapory Windows Defender. W nowym oknie wybierz **Reguły przychodzące** i kliknij **Nowa reguła**. Postępuj zgodnie z instrukcjami wyświetlanymi na ekranie, aby utworzyć reguły, które zezwalają tylko na niezbędne połączenia przychodzące. Weź pod uwagę usługi i aplikacje, które wymagają dostępu do sieci i odpowiednio utwórz reguły.

3. **Skonfiguruj reguły wychodzące**: Reguły wychodzące kontrolują wychodzące połączenia sieciowe z systemu. Wykonaj te same kroki, co powyżej, ale zamiast tego wybierz **Reguły wychodzące**. Utwórz reguły, aby zezwolić na połączenia wychodzące dla niezbędnych usług i aplikacji, jednocześnie blokując podejrzane lub niepotrzebne połączenia.

4. **Regularny przegląd i aktualizacja**: Ważne jest, aby regularnie przeglądać i aktualizować reguły zapory sieciowej, aby upewnić się, że są one zgodne z wymaganiami systemu. Wraz ze zmianą środowiska sieciowego i wzorców użytkowania może być konieczne zmodyfikowanie lub utworzenie nowych reguł. Zachowaj czujność i aktualizuj swoje reguły, aby utrzymać skuteczną konfigurację zapory.

Wdrażając i utrzymując reguły zapory sieciowej, można znacznie zmniejszyć ryzyko nieautoryzowanego dostępu do sieci i zwiększyć bezpieczeństwo systemu Windows 10. Dodatkowo, warto rozważyć włączenie opcji **Stealth Mode** w ustawieniach zapory sieciowej, aby system był mniej widoczny dla potencjalnych napastników.

Więcej szczegółowych informacji na temat konfigurowania reguł zapory sieciowej w systemie Windows 10 można znaleźć w oficjalnym dokumencie [Microsoft documentation](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/best-practices-configuring) aby uzyskać instrukcje krok po kroku.

Należy pamiętać, że dobrze skonfigurowana zapora sieciowa jest niezbędnym elementem kompleksowej strategii bezpieczeństwa, ale powinna być używana w połączeniu z innymi środkami bezpieczeństwa, aby zapewnić solidną ochronę systemu.

#### 8. [**Use AppLocker**](https://github.com/simeononsecurity/AppLocker)
AppLocker to potężna funkcja systemu Windows 10, która pozwala kontrolować, które aplikacje mogą być uruchamiane w systemie. Wdrażając zasady AppLocker, można ograniczyć wykonywanie nieautoryzowanych lub potencjalnie złośliwych aplikacji, zwiększając bezpieczeństwo środowiska Windows 10.

Wykonaj poniższe kroki, aby korzystać z AppLocker w systemie Windows 10:

1. **Dostęp do ustawień AppLocker**: Aby uzyskać dostęp do ustawień AppLocker, otwórz **Lokalny edytor zasad grupy**, naciskając **klawisz Windows + R**, wpisując **gpedit.msc** i klikając **OK**. Alternatywnie, możesz wyszukać **Group Policy Editor** w menu **Start**.

2. **Konfiguruj zasady AppLocker**: W Edytorze lokalnych zasad grupy przejdź do **Konfiguracja komputera > Ustawienia systemu Windows > Ustawienia zabezpieczeń > Zasady kontroli aplikacji > AppLocker**. Tutaj można skonfigurować różne zasady, takie jak **Reguły wykonywalne**, **Reguły instalatora Windows**, **Reguły skryptów** i **Reguły aplikacji pakietowych**.

3. **Utwórz reguły AppLocker**: Aby utworzyć regułę AppLocker, kliknij prawym przyciskiem myszy żądany folder zasad (np. **Executable Rules**) i wybierz **Create New Rule**. Postępuj zgodnie z instrukcjami wyświetlanymi na ekranie, aby określić warunki i wyjątki dla reguły. Możesz tworzyć reguły na podstawie ścieżki pliku, wydawcy, skrótu pliku lub innych atrybutów, aby zezwolić lub odmówić wykonania aplikacji.

4. **Testuj i udoskonalaj zasady**: Po utworzeniu reguł AppLocker ważne jest, aby je przetestować, aby upewnić się, że działają zgodnie z przeznaczeniem. Wdróż zasady do grupy testowej lub systemu i sprawdź, czy tylko autoryzowane aplikacje mogą być uruchamiane. Dokonaj wszelkich niezbędnych zmian w regułach w oparciu o wyniki testów.

5. **Regularny przegląd i aktualizacja**: W miarę ewolucji środowiska aplikacji ważne jest, aby regularnie przeglądać i aktualizować zasady AppLocker. Nowe aplikacje mogą wymagać pozwolenia na uruchomienie, podczas gdy inne mogą stać się przestarzałe lub stanowić zagrożenie dla bezpieczeństwa. Bądź proaktywny i aktualizuj swoje zasady, aby utrzymać skuteczny mechanizm kontroli aplikacji.

AppLocker zapewnia szczegółową kontrolę nad wykonywaniem aplikacji, pomagając zapobiegać uruchamianiu nieautoryzowanego lub złośliwego oprogramowania w systemie Windows 10. Korzystając z AppLocker, można zmniejszyć ryzyko infekcji złośliwym oprogramowaniem, nieautoryzowanych instalacji oprogramowania i innych incydentów związanych z bezpieczeństwem.

Więcej szczegółowych informacji na temat wdrażania zasad AppLocker można znaleźć w oficjalnym dokumencie [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-overview) or visit our [AppLocker GitHub repository](https://github.com/simeononsecurity/AppLocker) aby uzyskać dodatkowe zasoby i przykłady.

Pamiętaj, aby regularnie przeglądać i aktualizować zasady AppLocker, aby dostosować je do zmieniających się wymagań aplikacji i pojawiających się zagrożeń bezpieczeństwa. AppLocker jest cennym narzędziem do obrony przed nieautoryzowanymi i potencjalnie szkodliwymi aplikacjami w systemie Windows 10.

#### 9. [**Regularly Backup Your Data**](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/)
Regularne tworzenie kopii zapasowych danych jest niezbędną praktyką w celu ochrony przed utratą danych spowodowaną incydentami bezpieczeństwa, awariami sprzętu lub innymi nieoczekiwanymi zdarzeniami. Tworząc regularne kopie zapasowe i weryfikując ich integralność, można zagwarantować, że ważne dane pozostaną bezpieczne i będzie można je przywrócić w przypadku katastrofy.

Wykonaj poniższe kroki, aby regularnie tworzyć kopie zapasowe danych w systemie Windows 10:

1. **Zidentyfikuj krytyczne dane**: Zacznij od zidentyfikowania danych, które są krytyczne i wymagają utworzenia kopii zapasowej. Mogą to być ważne dokumenty, pliki osobiste, konfiguracje systemu, ustawienia aplikacji i wszelkie inne dane, które uważasz za cenne.

2. **Wybierz rozwiązanie do tworzenia kopii zapasowych**: Wybierz niezawodne rozwiązanie do tworzenia kopii zapasowych, które spełnia twoje wymagania. Windows 10 oferuje wbudowane narzędzia do tworzenia kopii zapasowych, takie jak **Historia plików** i **Backup i przywracanie systemu Windows**. Alternatywnie możesz zdecydować się na oprogramowanie do tworzenia kopii zapasowych innych firm, które zapewnia dodatkowe funkcje i elastyczność.

3. **Zdefiniuj częstotliwość tworzenia kopii zapasowych**: Określ, jak często chcesz wykonywać kopie zapasowe w oparciu o krytyczność danych i częstotliwość zmian. Niektóre dane mogą wymagać codziennego tworzenia kopii zapasowych, podczas gdy inne mogą być tworzone co tydzień lub co miesiąc.

4. **Wybierz miejsce przechowywania kopii zapasowych**: Wybierz odpowiedni nośnik do przechowywania kopii zapasowych. Mogą to być zewnętrzne dyski twarde, sieciowa pamięć masowa (NAS), usługi przechowywania w chmurze lub kombinacja wielu opcji przechowywania. Upewnij się, że nośnik danych jest bezpieczny i niezawodny.

5. **Konfiguracja ustawień kopii zapasowej**: Skonfiguruj rozwiązanie do tworzenia kopii zapasowych zgodnie z własnymi preferencjami. Określ dane do utworzenia kopii zapasowej, miejsce docelowe kopii zapasowej i wszelkie dodatkowe ustawienia, takie jak szyfrowanie lub kompresja.

6. **Przeprowadź przywracanie testowe**: Regularnie testuj proces przywracania, wykonując testowe przywracanie z kopii zapasowych. Zapewnia to prawidłowe działanie kopii zapasowych i możliwość pomyślnego odzyskania danych w razie potrzeby.

7. **Monitoruj i aktualizuj**: Regularnie monitoruj proces tworzenia kopii zapasowych, aby upewnić się, że przebiega on zgodnie z oczekiwaniami. Aktualizuj swoje rozwiązanie do tworzenia kopii zapasowych i dostosowuj ustawienia kopii zapasowych w miarę zmiany danych i wymagań.

Postępując zgodnie z tymi krokami i przestrzegając regularnej procedury tworzenia kopii zapasowych, można zminimalizować wpływ utraty danych i utrzymać dostępność ważnych informacji. Pamiętaj o bezpiecznym przechowywaniu kopii zapasowych, z dala od oryginalnych danych i rozważ wdrożenie zasady **3-2-1 kopii zapasowych**, mając co najmniej trzy kopie danych, przechowywane na dwóch różnych nośnikach pamięci, z jedną kopią przechowywaną poza siedzibą firmy.

Więcej szczegółowych informacji na temat najlepszych praktyk tworzenia kopii zapasowych i **zasady 3-2-1** można znaleźć w artykule na stronie [What is the 3-2-1 Backup Rule and Why You Should Use It](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) Zawiera cenne spostrzeżenia i zalecenia dotyczące wdrażania skutecznej strategii tworzenia kopii zapasowych.

Należy pamiętać, że regularne tworzenie kopii zapasowych ma kluczowe znaczenie dla ochrony danych i zapewnienia ich dostępności w przypadku nieprzewidzianych zdarzeń. Uczyń tworzenie kopii zapasowych danych integralną częścią wysiłków związanych z utwardzaniem systemu Windows 10, aby chronić swoje cenne informacje.

______

{{< inarticle-dark >}}


### [Hardening Windows 11](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 11 to najnowsza wersja systemu operacyjnego Windows, oferująca ulepszone funkcje i poprawione zabezpieczenia. Aby wzmocnić środowisko Windows 11, należy rozważyć następujące najlepsze praktyki:

#### 1. **Bezpieczny rozruch i TPM**
Secure Boot i TPM (Trusted Platform Module) to podstawowe funkcje bezpieczeństwa dostępne w systemie Windows 11, które pomagają chronić przed nieautoryzowanym dostępem i zapewniają integralność systemu operacyjnego. Włączając Secure Boot i TPM, można zwiększyć bezpieczeństwo systemu Windows 11.

Wykonaj poniższe kroki, aby włączyć Secure Boot i TPM na urządzeniu z systemem Windows 11:

1. **Sprawdź zgodność**: Przed włączeniem funkcji Secure Boot i TPM należy upewnić się, że urządzenie obsługuje te funkcje. Sprawdź, czy sprzęt i oprogramowanie układowe systemu spełniają wymagania dotyczące funkcji Secure Boot i TPM.

2. **Dostęp do ustawień UEFI/BIOS**: Uruchom ponownie urządzenie z systemem Windows 11 i uzyskaj dostęp do ustawień UEFI (Unified Extensible Firmware Interface) lub BIOS (Basic Input/Output System). Konkretny klawisz lub kombinacja klawiszy umożliwiająca dostęp do tych ustawień może się różnić w zależności od urządzenia. Typowe klawisze to Del, F2, F10 lub Esc. Szczegółowe instrukcje można znaleźć w dokumentacji urządzenia lub na stronie internetowej producenta.

3. **Włącz bezpieczny rozruch**: Po przejściu do ustawień UEFI/BIOS przejdź do ustawień Secure Boot. Włącz Secure Boot, aby upewnić się, że tylko zaufane systemy operacyjne i komponenty mogą być uruchamiane podczas procesu rozruchu. Zapobiega to ładowaniu nieautoryzowanego lub złośliwego oprogramowania, które może zagrozić bezpieczeństwu systemu.

4. **Włącz TPM**: Zlokalizuj ustawienia TPM w UEFI/BIOS i włącz TPM. TPM to dedykowany mikroukład na płycie głównej urządzenia, który zapewnia sprzętowe funkcje bezpieczeństwa. Włączenie TPM pozwala systemowi Windows 11 wykorzystać jego możliwości w celu zwiększenia bezpieczeństwa systemu.

5. **Skonfiguruj zabezpieczenia TPM**: Po włączeniu modułu TPM mogą być dostępne dodatkowe opcje konfiguracji jego ustawień zabezpieczeń. W zależności od urządzenia i oprogramowania układowego, możesz ustawić hasło TPM, włączyć aktualizacje oprogramowania układowego TPM lub dostosować inne powiązane ustawienia. Zapoznaj się z dostępnymi opcjami i skonfiguruj je w oparciu o wymagania bezpieczeństwa.

6. **Zapisz i wyjdź**: Po włączeniu Secure Boot i TPM oraz dokonaniu wszelkich niezbędnych konfiguracji, zapisz zmiany w ustawieniach UEFI/BIOS i wyjdź. System uruchomi się ponownie, a nowe ustawienia zaczną obowiązywać.

Włączenie funkcji Secure Boot i TPM w systemie Windows 11 pomaga chronić urządzenie przed nieautoryzowanymi modyfikacjami, rootkitami i innymi zagrożeniami bezpieczeństwa. Funkcje te stanowią podstawę zaufania dla systemu operacyjnego i przyczyniają się do bezpieczniejszego środowiska komputerowego.

Należy pamiętać, że dostępność i konkretne kroki w celu włączenia funkcji Secure Boot i TPM mogą się różnić w zależności od producenta urządzenia i wersji oprogramowania układowego. Zaleca się zapoznanie się z dokumentacją urządzenia lub stroną internetową producenta w celu uzyskania dokładnych instrukcji dostosowanych do posiadanego systemu.

Włączając Secure Boot i TPM na urządzeniu z systemem Windows 11, zwiększasz ogólny poziom bezpieczeństwa i wzmacniasz ochronę systemu operacyjnego i poufnych danych.

#### 2. [**Enable Microsoft Defender Antivirus**](https://github.com/simeononsecurity/Windows-Defender-Hardening)
Windows 11 posiada wbudowaną ochronę antywirusową o nazwie **Microsoft Defender Antivirus**. Oferuje on kompleksową ochronę przed różnymi rodzajami **złośliwego oprogramowania**, w tym wirusami, ransomware i spyware. Poprzez **włączenie** i **regularne aktualizowanie** programu Microsoft Defender Antivirus, możesz zapewnić **wykrywanie i zapobieganie zagrożeniom** w czasie rzeczywistym w swoim systemie Windows 11.

Wykonaj następujące kroki, aby włączyć i zaktualizować program Microsoft Defender Antivirus na urządzeniu z systemem Windows 11:

1. **Sprawdź status programu antywirusowego**: Najpierw sprawdź status programu Microsoft Defender Antivirus w swoim systemie. Otwórz aplikację **Windows Security**, klikając menu Start, wyszukując "Windows Security" i wybierając aplikację z wyników wyszukiwania. Po otwarciu aplikacji przejdź do sekcji **"Ochrona przed wirusami i zagrożeniami "**, aby zweryfikować status programu Microsoft Defender Antivirus. Powinien on być domyślnie **włączony** na świeżej instalacji systemu Windows 11.

2. **Włącz ochronę w czasie rzeczywistym**: W aplikacji Zabezpieczenia systemu Windows upewnij się, że **ochrona w czasie rzeczywistym** jest włączona dla programu Microsoft Defender Antivirus. Ochrona w czasie rzeczywistym stale monitoruje system pod kątem złośliwego oprogramowania i innych złośliwych działań, zapewniając **natychmiastową reakcję** i **blokowanie zagrożeń** w czasie rzeczywistym. Jeśli ochrona w czasie rzeczywistym nie jest włączona, kliknij **przełącznik**, aby ją włączyć.

3. **Aktualizuj definicje**: Regularne aktualizowanie **definicji wirusów** ma kluczowe znaczenie dla zapewnienia, że Microsoft Defender Antivirus może wykrywać i chronić przed najnowszymi zagrożeniami. W aplikacji Zabezpieczenia systemu Windows przejdź do sekcji **"Ochrona przed wirusami i zagrożeniami "** i kliknij przycisk **"Sprawdź aktualizacje "**, aby zaktualizować definicje antywirusa. Proces ten zapewnia, że system jest wyposażony w **najnowsze sygnatury** i **możliwości wykrywania**.

4. **Planowanie skanowania**: Microsoft Defender Antivirus pozwala zaplanować regularne **skanowanie systemu** w celu proaktywnego wykrywania i usuwania wszelkich potencjalnych zagrożeń. W aplikacji Zabezpieczenia systemu Windows przejdź do sekcji **"Ochrona przed wirusami i zagrożeniami "** i kliknij opcję **"Szybkie skanowanie "** lub **"Pełne skanowanie "**, aby zainicjować skanowanie. Możesz również kliknąć łącze **"Opcje skanowania "**, aby dostosować ustawienia skanowania i zaplanować regularne skanowanie zgodnie z własnymi preferencjami.

5. **Skonfiguruj dodatkowe ustawienia**: Microsoft Defender Antivirus zapewnia dodatkowe ustawienia i funkcje, które można skonfigurować w oparciu o wymagania bezpieczeństwa. W aplikacji Zabezpieczenia systemu Windows należy zapoznać się z różnymi sekcjami, takimi jak **"Kontrola aplikacji i przeglądarki", **"Zabezpieczenia urządzenia "** i **"Zapora sieciowa i ochrona sieci "**, aby dostosować ustawienia antywirusa i wykorzystać zaawansowane funkcje ochrony.

Włączenie i regularne aktualizowanie programu antywirusowego Microsoft Defender w systemie Windows 11 jest niezbędne do utrzymania silnej ochrony przed złośliwym oprogramowaniem i innymi zagrożeniami bezpieczeństwa. Postępując zgodnie z tymi krokami i aktualizując program Microsoft Defender Antivirus, można upewnić się, że system Windows 11 jest dobrze chroniony.

Należy pamiętać, że chociaż Microsoft Defender Antivirus zapewnia solidną ochronę, zawsze zaleca się **bezpieczne nawyki przeglądania**, zachowanie ostrożności podczas **pobierania plików** lub **otwierania załączników do wiadomości e-mail** oraz aktualizowanie **systemu operacyjnego i aplikacji** w celu dalszego zwiększenia ogólnego poziomu bezpieczeństwa.

#### 3. **Zastosuj domyślną izolację sprzętową**
Windows 11 wykorzystuje funkcje izolacji sprzętowej, takie jak **Virtualization-based Security (VBS)** i **Hypervisor-protected Code Integrity (HVCI)**, aby zapewnić zwiększone bezpieczeństwo i chronić krytyczne komponenty systemu.

Włączając i stosując te domyślne funkcje izolacji sprzętowej, można ustanowić solidne granice bezpieczeństwa i ograniczyć różne wektory ataków. Oto kilka kluczowych kroków, aby zapewnić prawidłową konfigurację:

1. **Włącz technologię wirtualizacji**: Po pierwsze, należy sprawdzić, czy system obsługuje technologię wirtualizacji i upewnić się, że jest ona włączona w ustawieniach systemu **BIOS** lub **UEFI firmware**. Kroki uzyskiwania dostępu i włączania technologii wirtualizacji mogą się różnić w zależności od producenta płyty głównej lub oprogramowania układowego. Szczegółowe instrukcje można znaleźć w dokumentacji systemu lub na stronie internetowej producenta.

2. **Włącz zabezpieczenia oparte na wirtualizacji (VBS)**: Windows 11 zawiera VBS, który wykorzystuje możliwości wirtualizacji sprzętu do tworzenia izolowanych kontenerów zwanych **Virtual Secure Mode (VSM)**. VSM zapewnia bezpieczne środowisko wykonawcze dla krytycznych komponentów systemu, chroniąc je przed potencjalnymi atakami. Aby włączyć VBS, wykonaj następujące kroki:

   - Naciśnij **klawisz Windows + R**, aby otworzyć okno dialogowe Uruchom.
   - Wpisz "**gpedit.msc**" i naciśnij **Enter**, aby otworzyć Edytor lokalnych zasad grupy.
   - Przejdź do **Konfiguracja komputera -> Szablony administracyjne -> System -> Ochrona urządzeń**.
   - Kliknij dwukrotnie na **"Włącz zabezpieczenia oparte na wirtualizacji "**.
   - Wybierz **"Włączone "** i kliknij **OK**, aby zastosować zmiany.

   Włączenie VBS może wymagać kompatybilnego sprzętu i pewnych wymagań systemowych. Więcej informacji można znaleźć w oficjalnej dokumentacji **Microsoft**.

3. **Włącz integralność kodu chronioną przez hiperwizor (HVCI)**: HVCI to funkcja, która wykorzystuje hiperwizor do egzekwowania zasad integralności kodu, zapobiegając nieautoryzowanemu wykonywaniu kodu i zwiększając ogólny poziom bezpieczeństwa. Aby włączyć HVCI, wykonaj następujące kroki:

   - Naciśnij **klawisz Windows + R**, aby otworzyć okno dialogowe Uruchom.
   - Wpisz "**msconfig**" i naciśnij **Enter**, aby otworzyć narzędzie konfiguracji systemu.
   - Przejdź do zakładki **"Rozruch "**.
   - Kliknij na **"Opcje zaawansowane "**.
   - Zaznacz opcję **"Enable Hypervisor-protected Code Integrity "**.
   - Kliknij **OK**, aby zapisać zmiany i ponownie uruchomić system.

   Włączenie HVCI wymaga kompatybilnego sprzętu i określonych wymagań systemowych. Więcej szczegółów można znaleźć w oficjalnej dokumentacji **Microsoft**.

Stosując domyślne funkcje izolacji sprzętowej, takie jak VBS i HVCI, można znacznie zwiększyć poziom bezpieczeństwa systemu Windows 11. Funkcje te pomagają chronić krytyczne komponenty systemu przed różnymi atakami, w tym próbami modyfikacji lub wykorzystania kodu i konfiguracji systemu.

Upewnij się, że regularnie aktualizujesz swój system za pomocą najnowszych poprawek zabezpieczeń i aktualizacji oprogramowania układowego, aby korzystać z najbardziej aktualnych ulepszeń zabezpieczeń i środków łagodzących oferowanych przez te funkcje izolacji sprzętowej.

Należy pamiętać, że dostępność i wymagania funkcji izolacji sprzętowej mogą się różnić w zależności od konfiguracji systemu i wersji systemu Windows 11. Zaleca się zapoznanie się z oficjalną dokumentacją **Microsoft** i przeprowadzenie kontroli zgodności, aby zapewnić prawidłowe wdrożenie tych funkcji bezpieczeństwa.

#### 4. [**Use Windows Sandbox**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)
**Windows Sandbox** to cenne narzędzie, które pozwala na uruchamianie niezaufanych aplikacji lub testowanie oprogramowania w odizolowanym środowisku, zapewniając dodatkową warstwę bezpieczeństwa dla systemu. Korzystając z Windows Sandbox, można ograniczyć potencjalne ryzyko związane z uruchamianiem niezaufanych programów.

Windows Sandbox tworzy lekkie, tymczasowe środowisko pulpitu, które jest całkowicie oddzielone od głównego systemu operacyjnego. Wszelkie zmiany wprowadzone w piaskownicy są odrzucane po jej zamknięciu, zapewniając, że główny system pozostanie nienaruszony.

Aby korzystać z Windows Sandbox, wykonaj następujące kroki:

1. **Sprawdź wymagania systemowe**: Przed kontynuowaniem upewnij się, że twój system spełnia wymagania do uruchomienia Windows Sandbox. Ogólnie rzecz biorąc, potrzebny jest system Windows 10 Pro lub Enterprise oraz procesor z włączonymi funkcjami wirtualizacji w oprogramowaniu układowym BIOS/UEFI. Zapoznaj się z oficjalną [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview) dla określonych wymagań systemowych.

2. **Włącz Windows Sandbox**: Windows Sandbox jest wbudowaną funkcją w Windows 10 Pro i Enterprise. Aby włączyć Windows Sandbox, wykonaj następujące kroki:

   - Naciśnij **klawisz Windows + R**, aby otworzyć okno dialogowe Uruchom.
   - Wpisz "**appwiz.cpl**" i naciśnij **Enter**, aby otworzyć okno Programy i funkcje.
   - Kliknij na **"Włącz lub wyłącz funkcje systemu Windows "** po lewej stronie.
   - Przewiń w dół i znajdź **"Windows Sandbox "** na liście funkcji.
   - Zaznacz pole obok **"Windows Sandbox "** i kliknij **OK**, aby ją włączyć.
   - Windows zainstaluje niezbędne komponenty i może być konieczne ponowne uruchomienie systemu, aby zmiany zaczęły obowiązywać.

3. **Uruchom Windows Sandbox**: Po włączeniu Windows Sandbox można go uruchomić, wykonując następujące kroki:

   - Otwórz menu **Start** i wyszukaj **"Windows Sandbox "**.
   - Kliknij aplikację **"Windows Sandbox "**, aby ją otworzyć.
   - Sandbox uruchomi się w osobnym oknie, zapewniając bezpieczne środowisko do uruchamiania niezaufanych aplikacji lub testowania oprogramowania.

Podczas uruchamiania aplikacji w Windows Sandbox należy pamiętać, że środowisko Sandbox jest izolowane i zaprojektowane tak, aby odrzucać wszelkie zmiany wprowadzone w nim. Dlatego ważne jest, aby zapisywać pliki lub dane poza piaskownicą, jeśli chcesz je zachować.

Windows Sandbox to skuteczne narzędzie do testowania nieznanego oprogramowania, otwierania podejrzanych plików lub przeglądania potencjalnie ryzykownych stron internetowych. Dodaje dodatkową warstwę ochrony, zapewniając, że wszelkie złośliwe działania lub niechciane zmiany są ograniczone do piaskownicy i nie mają wpływu na główny system operacyjny.

Włączając Windows Sandbox do swoich praktyk bezpieczeństwa, możesz znacznie zmniejszyć ryzyko związane z uruchamianiem niezaufanych aplikacji, chroniąc swój system przed potencjalnymi zagrożeniami.

Więcej informacji na temat Windows Sandbox i jego wykorzystania można znaleźć w oficjalnej witrynie [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)

#### 5. [**Implement Microsoft Defender Application Guard**](https://github.com/simeononsecurity/Windows-Defender-Application-Guard-Hardening)
Microsoft Defender Application Guard to potężna funkcja bezpieczeństwa, która izoluje sesje przeglądarki Microsoft Edge od bazowego systemu operacyjnego. Uruchamiając Edge w bezpiecznym, odizolowanym środowisku, Application Guard pomaga chronić system przed atakami opartymi na przeglądarce i złośliwymi stronami internetowymi.

Aby wdrożyć Microsoft Defender Application Guard i zwiększyć bezpieczeństwo przeglądarki, wykonaj następujące kroki:

1. **Sprawdź zgodność**: Przed kontynuowaniem upewnij się, że Twój system spełnia wymagania dotyczące uruchomienia Microsoft Defender Application Guard. Zazwyczaj potrzebny jest system Windows 10 w wersji Pro lub Enterprise, kompatybilny procesor z możliwością wirtualizacji i co najmniej 8 GB pamięci RAM. Zapoznaj się z oficjalną [**Microsoft documentation**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard) dla określonych wymagań systemowych.

2. **Włącz Ochronę aplikacji**: Ochrona aplikacji jest dostępna jako opcjonalna funkcja w systemie Windows 10. Aby włączyć Ochronę aplikacji Microsoft Defender, wykonaj następujące kroki:

   - Naciśnij **klawisz Windows + R**, aby otworzyć okno dialogowe Uruchom.
   - Wpisz "**appwiz.cpl**" i naciśnij **Enter**, aby otworzyć okno Programy i funkcje.
   - Kliknij na **"Włącz lub wyłącz funkcje systemu Windows "** po lewej stronie.
   - Przewiń w dół i znajdź **"Microsoft Defender Application Guard "** na liście funkcji.
   - Zaznacz pole obok **"Microsoft Defender Application Guard "** i kliknij **OK**, aby ją włączyć.
   - System Windows zainstaluje niezbędne komponenty i może być konieczne ponowne uruchomienie systemu, aby zmiany zaczęły obowiązywać.

3. **Skonfiguruj Ochronę aplikacji**: Po włączeniu Application Guard można skonfigurować jego ustawienia, aby dostosować je do swoich potrzeb w zakresie bezpieczeństwa. Application Guard pozwala zdefiniować poziom izolacji i kontrolować sposób obsługi niezaufanych stron internetowych i plików. Ustawienia te można dostosować za pomocą aplikacji **Windows Security** lub ustawień zasad grupy.

4. **Przetestuj i zweryfikuj**: Po włączeniu i skonfigurowaniu Microsoft Defender Application Guard, konieczne jest przetestowanie i zweryfikowanie jego funkcjonalności. Otwórz Microsoft Edge i odwiedź znaną złośliwą witrynę lub witrynę z potencjalnym ryzykiem, aby sprawdzić, czy Application Guard skutecznie izoluje sesję przeglądarki i zapobiega potencjalnym atakom.

Wdrażając Microsoft Defender Application Guard, dodajesz dodatkową warstwę ochrony do swojego systemu, izolując sesje przeglądarki i powstrzymując wszelkie potencjalne zagrożenia w bezpiecznym środowisku. Pomaga to chronić system i dane przed atakami opartymi na przeglądarce, takimi jak pobieranie drive-by download, złośliwe skrypty i exploity zero-day.

Aby uzyskać bardziej szczegółowe informacje na temat konfigurowania i korzystania z Microsoft Defender Application Guard, zapoznaj się z oficjalną stroną [**Microsoft documentation**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard)

#### 6. [**Controlled Folder Access**](https://github.com/simeononsecurity/Windows-Defender-Hardening)
Kontrolowany dostęp do folderów to potężna funkcja zabezpieczeń dostępna w systemie Windows 11, która pomaga chronić ważne foldery przed nieautoryzowanymi zmianami przez oprogramowanie ransomware i inne złośliwe oprogramowanie. Włączając Kontrolowany dostęp do folderów i dodając niezbędne foldery do listy chronionych, można zwiększyć bezpieczeństwo systemu i zapobiec potencjalnej utracie danych.

Aby wdrożyć Kontrolowany dostęp do folderów i chronić ważne foldery, wykonaj następujące kroki:

1. **Otwórz Zabezpieczenia systemu Windows**: Naciśnij klawisz **Windows** na klawiaturze, wpisz "**Windows Security**" i wybierz aplikację **Windows Security** z wyników wyszukiwania.

2. **Przejdź do Ustawień ochrony przed wirusami i zagrożeniami**: W aplikacji Windows Security kliknij zakładkę **"Ochrona przed wirusami i zagrożeniami "** w menu po lewej stronie.

3. Skonfiguruj **Kontrolowany dostęp do folderów**: W sekcji **"Ochrona przed ransomware "** kliknij **"Zarządzaj ochroną przed ransomware "**, aby uzyskać dostęp do ustawień Kontrolowanego dostępu do folderu.

4. **Włącz kontrolowany dostęp do folderów**: W ustawieniach Kontrolowanego dostępu do folderów przełącz przełącznik na **"Włączony "**, aby włączyć tę funkcję. Windows wyświetli ostrzeżenie o zezwalaniu tylko zaufanym aplikacjom na dostęp do chronionych folderów.

5. **Dodaj chronione foldery**: Aby określić, które foldery mają być chronione, kliknij na **"Chronione foldery "**, a następnie wybierz **"Dodaj chroniony folder "**. Wybierz foldery, które chcesz chronić i kliknij **"OK "**.

   - Zaleca się dodanie ważnych folderów, takich jak Dokumenty, Zdjęcia, Wideo i innych katalogów zawierających cenne dane.

6. **Zezwól lub zablokuj aplikacje**: Domyślnie Controlled Folder Access pozwala zaufanym aplikacjom na dostęp do chronionych folderów. Możesz jednak dostosować to zachowanie, klikając **"Zezwól aplikacji na dostęp do folderu kontrolowanego "**. Stamtąd można zezwolić lub zablokować określonym aplikacjom dostęp do chronionych folderów.

7. **Monitoruj i przeglądaj**: Po włączeniu funkcji kontrolowanego dostępu do folderów, system Windows będzie stale monitorował i rejestrował wszelkie próby uzyskania dostępu do chronionych folderów przez nieautoryzowane aplikacje. Możesz przejrzeć te dzienniki klikając na **"Review "** w sekcji **"Ostatnio zablokowane aplikacje "** w ustawieniach Kontrolowanego dostępu do folderów.

Wdrażając Kontrolowany dostęp do folderów, dodajesz dodatkową warstwę ochrony do swoich ważnych folderów, zmniejszając ryzyko nieautoryzowanych zmian i potencjalnej utraty danych spowodowanej atakami ransomware. Regularnie sprawdzaj ustawienia kontrolowanego dostępu do folderów, aby upewnić się, że chronione foldery są zgodne z wymaganiami bezpieczeństwa.

Aby uzyskać bardziej szczegółowe informacje na temat konfigurowania i korzystania z kontrolowanego dostępu do folderów, zapoznaj się z oficjalną stroną [**Microsoft documentation**](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/controlled-folders?view=o365-worldwide)


#### 7. **Włącz automatyczną konserwację systemu Windows**
Windows 11 zawiera wygodną funkcję o nazwie Automatyczna konserwacja, która pomaga zoptymalizować i chronić system poprzez wykonywanie regularnych zadań konserwacyjnych. Włączenie automatycznej konserwacji zapewnia płynne działanie systemu i jego bezpieczeństwo.

Aby włączyć Automatyczną konserwację systemu Windows, wykonaj następujące kroki:

1. **Otwórz Ustawienia Windows**: Naciśnij klawisz **Windows** na klawiaturze, wpisz "**Ustawienia**" i wybierz aplikację **Ustawienia** z wyników wyszukiwania.

2. **Dostęp do ustawień konserwacji**: W aplikacji Ustawienia kliknij kategorię **"System "**, a następnie wybierz **"Informacje "** z menu po lewej stronie. Przewiń do dołu strony i kliknij łącze **"Informacje o systemie "**.

3. Otwórz **Ustawienia konserwacji**: W oknie Informacje o systemie kliknij link **"Konserwacja "** znajdujący się na dole strony.

4. **Włącz automatyczną konserwację**: W ustawieniach konserwacji przełącz przełącznik obok pozycji **"Automatyczna konserwacja "** do pozycji **"Włączona "**.

5. **Skonfiguruj ustawienia konserwacji**: Domyślnie system Windows automatycznie zaplanuje zadania konserwacyjne tak, aby były uruchamiane codziennie o godzinie 2:00. Jeśli wolisz inny harmonogram, kliknij **"Zmień ustawienia konserwacji "** i dostosuj żądane opcje, takie jak czas rozpoczęcia konserwacji i częstotliwość zadań konserwacyjnych.

6. **Przejrzyj dodatkowe ustawienia**: Poniżej przełącznika automatycznej konserwacji można znaleźć dodatkowe ustawienia związane z konserwacją, takie jak **"Zezwalaj zaplanowanej konserwacji na wybudzanie mojego komputera o zaplanowanej godzinie "** i **"Zezwalaj zaplanowanej konserwacji na działanie nawet wtedy, gdy jestem na zasilaniu bateryjnym "**. Dostosuj te ustawienia do swoich preferencji i wymagań.

7. **Monitoruj działania konserwacyjne**: Po włączeniu automatycznej konserwacji system Windows będzie automatycznie wykonywał zadania konserwacyjne w tle w zaplanowanym czasie. Możesz monitorować te działania, sprawdzając sekcję **"Konserwacja "** w aplikacji **"Zabezpieczenia systemu Windows "** lub przeglądając dzienniki **"Konserwacja "** w Podglądzie zdarzeń.

Włączenie automatycznej konserwacji systemu Windows zapewnia optymalizację i ochronę systemu poprzez regularne wykonywanie niezbędnych zadań konserwacyjnych, takich jak aktualizacje oprogramowania, optymalizacja dysku i skanowanie zabezpieczeń. Utrzymując system w dobrej kondycji, możesz cieszyć się płynniejszym i bezpieczniejszym korzystaniem z komputera.

Więcej szczegółowych informacji na temat Automatycznej Konserwacji Windows i jej opcji konfiguracyjnych można znaleźć w oficjalnym dokumencie [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-maintenence)

______

{{< inarticle-dark >}}

## Wnioski

Wdrożenie tych **najlepszych praktyk hartowania systemu Windows** jest niezbędne do zapewnienia bezpieczeństwa systemów Windows. Regularne **aktualizowanie systemu operacyjnego** pozwala załatać luki w zabezpieczeniach i poprawić stabilność systemu. Włączenie funkcji bezpieczeństwa, takich jak **antywirus** i **szyfrowanie**, stanowi dodatkową warstwę ochrony danych. Konfiguracja odpowiednich **kontroli dostępu** pomaga zapobiegać nieautoryzowanym zmianom i ogranicza dostęp do wrażliwych zasobów.

Przestrzegając tych najlepszych praktyk, można zwiększyć bezpieczeństwo **środowiska Windows**, chronić dane i zachować integralność **infrastruktury cyfrowej**. Ważne jest, aby pozostać **proaktywnym** i regularnie przeglądać i aktualizować środki bezpieczeństwa, aby wyprzedzać potencjalne zagrożenia.

Pamiętaj, że **utwardzanie systemu Windows** jest procesem ciągłym i ważne jest, aby być na bieżąco z najnowszymi aktualizacjami i praktykami bezpieczeństwa. Pozostając proaktywnym i wdrażając te najlepsze praktyki, można skutecznie ograniczyć zagrożenia bezpieczeństwa i zapewnić bezpieczeństwo systemów Windows.

Więcej informacji na temat wzmacniania zabezpieczeń systemu Windows i najlepszych praktyk można znaleźć w renomowanych źródłach, takich jak **dokumentacja Microsoft**, **fora poświęcone bezpieczeństwu** i zaufane **strony internetowe poświęcone bezpieczeństwu cybernetycznemu**.

______

## Referencje:

- [Microsoft Windows Security](https://www.microsoft.com/en-us/security)
- [NIST Special Publication 800-171: Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final)
- [CIS Microsoft Windows 10 Benchmark](https://www.cisecurity.org/benchmark/microsoft_windows_10/)
- [CIS Microsoft Windows 11 Benchmark](https://www.cisecurity.org/benchmark/microsoft_windows_11/)
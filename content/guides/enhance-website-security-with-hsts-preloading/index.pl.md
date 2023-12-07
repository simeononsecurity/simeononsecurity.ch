---
title: "Wstępne ładowanie HSTS - jak zwiększyć bezpieczeństwo witryny: Przewodnik krok po kroku"
date: 2023-08-20
toc: true
draft: false
description: "Dowiedz się, jak zwiększyć bezpieczeństwo witryny i zaufanie użytkowników, wstępnie ładując ustawienia HSTS w przeglądarkach Chrome i Firefox. Postępuj zgodnie z naszym przewodnikiem krok po kroku, aby uzyskać płynne wdrożenie."
cover: "/img/cover/enhanced-website-security.png"
coverAlt: "Kreskówkowa ilustracja strony internetowej zabezpieczonej kłódką, reprezentująca zwiększone bezpieczeństwo i ochronę przed cyberzagrożeniami."
coverCaption: "Wzmocnij ochronę swojej witryny, wykorzystaj wstępne ładowanie HSTS."
---

**Zwiększ bezpieczeństwo strony internetowej dzięki HSTS Preloading: Przewodnik krok po kroku**

HTTP Strict Transport Security (HSTS) to **kluczowy mechanizm bezpieczeństwa**, który zapewnia, że strony internetowe wymuszają połączenia HTTPS w celu **ochrony użytkowników przed potencjalnymi zagrożeniami bezpieczeństwa**. Dzięki wstępnemu załadowaniu ustawień HSTS w przeglądarkach Chrome i Firefox można **zwiększyć bezpieczeństwo witryny** i zbudować **zaufanie użytkowników**. W tym kompleksowym przewodniku przeprowadzimy Cię przez **istotne kroki**, aby pomyślnie wstępnie załadować ustawienia HSTS i przedstawić **użyteczne zalecenia** w celu optymalizacji bezpieczeństwa.

______

### **Zrozumienie wstępnego ładowania HSTS**

**HSTS Preloading** to proces **przesyłania domeny witryny** do list preload głównych przeglądarek. Po dodaniu, przeglądarki te **automatycznie wymuszą połączenia HTTPS** dla twojej domeny i wszystkich subdomen. Zapewnia to użytkownikom zawsze bezpieczny dostęp do witryny, zmniejszając ryzyko **ataków typu man-in-the-middle** i nieautoryzowanego podsłuchiwania. Więcej szczegółów na temat wstępnego ładowania HSTS można znaleźć w oficjalnym dokumencie [documentation](https://hstspreload.org/)

______

______

### **Wymagania dotyczące zgłoszenia**

Przed przesłaniem domeny do wstępnego ładowania HSTS upewnij się, że witryna spełnia następujące **istotne wymagania**:

1. **Prawidłowy certyfikat**: Twoja witryna musi obsługiwać **ważny certyfikat SSL lub TLS**, aby umożliwić **bezpieczne połączenia HTTPS**.

2. **Przekierowanie HTTP na HTTPS**: Upewnij się, że wszystkie żądania **HTTP są przekierowywane** do ich odpowiedników **HTTPS**, gdy twoja strona nasłuchuje na porcie 80.

3. **HTTPS dla wszystkich subdomen**: Wszystkie subdomeny witryny muszą **obsługiwać połączenia HTTPS**, aby kwalifikować się do wstępnego ładowania HSTS.

4. **Nagłówek HSTS w domenie podstawowej**: Dołącz nagłówek **HSTS** w domenie bazowej dla żądań HTTPS z następującymi ustawieniami:
   - `max-age` musi wynosić co najmniej 31536000 sekund** (1 rok).
   - The `includeSubDomains` musi zostać określona, aby uwzględnić wszystkie subdomeny.
   - Dyrektywa `preload` musi zostać określona, aby zażądać włączenia do listy wstępnego ładowania.

Oto przykład prawidłowego nagłówka HSTS:

```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

______

### **Jak wstępnie załadować ustawienia HSTS**

Jeśli twoja witryna jest **w pełni zaangażowana w HTTPS** i spełnia powyższe wymagania, wykonaj te **kluczowe kroki**, aby pomyślnie wstępnie załadować ustawienia HSTS:

1. **Sprawdź subdomeny**: Upewnij się, że wszystkie **subdomeny twojej witryny** działają poprawnie przez HTTPS, aby zapewnić użytkownikom płynne przeglądanie.

2. **Stopniowy wzrost**: Aby przetestować i naprawić wszelkie potencjalne problemy, dodaj nagłówek **HSTS** do swoich odpowiedzi HTTPS z **niskim poziomem**. `max-age` wartość** (np. 300 sekund). Stopniowo zwiększaj wartość `max-age` wartość w etapach:
   - 5 minut: `max-age=300; includeSubDomains`
   - 1 tydzień: `max-age=604800; includeSubDomains`
   - 1 miesiąc: `max-age=2592000; includeSubDomains`

3. **Monitoruj wskaźniki**: Na każdym etapie **ściśle monitoruj wskaźniki** swojej witryny, w tym ruch i przychody, aby zidentyfikować i rozwiązać wszelkie problemy przed przejściem do następnego etapu.

4. **Zwiększ maksymalny wiek do 2 lat**: Gdy będziesz **pewny, że nie ma już żadnych problemów**, ustaw **maksymalny wiek**. `max-age` do **2 lat (63072000 sekund)** i dodać `preload` do nagłówka HSTS:
```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

5. **Prześlij swoją witrynę**: Po wdrożeniu 2-letniego `max-age` ustawienie, **przesłać swoją witrynę** do listy wstępnego ładowania HSTS za pomocą formularza dostępnego na stronie [hstspreload.org](https://hstspreload.org/) Należy pamiętać, że włączenie do listy wstępnego ładowania może potrwać kilka miesięcy, zanim użytkownicy otrzymają aktualizację Chrome.
______

### **Opt-In dla HSTS Preloading: Wzmocnienie pozycji operatorów witryn**

Obsługa wstępnego ładowania HSTS jest **doskonałą praktyką bezpieczeństwa**, która zwiększa ochronę witryny. Powinna to być jednak **decyzja opcjonalna** dla operatorów witryn. Jeśli dostarczasz **porady dotyczące konfiguracji HTTPS** lub oferujesz opcję włączenia HSTS, **unikaj włączania opcji `preload` domyślnie**. Takie podejście zapobiega niezamierzonemu włączeniu do listy wstępnego ładowania, co może prowadzić do trudności z dostępem do niektórych subdomen.

Aby zapewnić płynne działanie, **poinformuj operatorów witryn** o **długoterminowych konsekwencjach** wstępnego ładowania i podkreśl **ważność spełnienia wszystkich wymagań** przed włączeniem HSTS dla ich domeny.

______

### **Usunięcie z listy wstępnego ładowania: Świadoma decyzja**

Włączenie do listy wstępnego ładowania jest **stałą decyzją**, której nie można łatwo cofnąć. Jeśli jednak napotkasz **silne powody techniczne lub związane z kosztami** uniemożliwiające obsługę HTTPS dla niektórych subdomen, masz możliwość zażądania **usunięcia z listy wstępnego ładowania Chrome** za pośrednictwem aplikacji [removal form](https://hstspreload.org/removal/)

Przed podjęciem tej ważnej decyzji upewnij się, że dokładnie przeanalizowałeś jej konsekwencje.
______

______

### **Bezpieczniejsze przeglądanie zaczyna się od wstępnego ładowania HSTS**

Podsumowując, wstępne ładowanie ustawień HSTS w Chrome i Firefox jest **proaktywnym krokiem** w kierunku bezpieczniejszego przeglądania stron internetowych dla użytkowników. Poprzez **wzmocnienie połączeń HTTPS**, **chronisz wrażliwe dane** i budujesz **zaufanie** wśród odwiedzających. Postępuj zgodnie z **wytycznymi** wymienionymi powyżej, aby **przeładować ustawienia HSTS** z powodzeniem i cieszyć się **zwiększonym bezpieczeństwem witryny**.

______

### Referencje

1. [Chromium - HTTP Strict Transport Security (HSTS)](https://www.chromium.org/hsts/)
2. [HSTS Preload Submission](https://hstspreload.org/)
3. [Mozilla Web Security Guidelines](https://infosec.mozilla.org/guidelines/web_security)
4. [Google Web Fundamentals - Security](https://developers.google.com/web/fundamentals/security/)

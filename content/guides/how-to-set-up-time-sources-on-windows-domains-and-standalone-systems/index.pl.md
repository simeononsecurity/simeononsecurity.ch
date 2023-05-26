---
title: "Najlepsze praktyki zarządzania źródłami czasu w domenach Windows i maszynach autonomicznych"
draft: false
toc: true
date: 2023-05-23
description: "Dowiedz się, jak skutecznie ustawiać i obsługiwać źródła czasu w domenach Windows i samodzielnych maszynach, aby zapewnić dokładną synchronizację czasu i uniknąć potencjalnych problemów."
tags: ["źródła czasu", "Domena Windows", "samodzielne maszyny", "synchronizacja czasu", "dokładny pomiar czasu", "Serwery NTP", "kontrolery domeny", "Usługa Windows Time", "błędy uwierzytelniania", "niespójności pliku dziennika", "Problemy z replikacją", "konfiguracja źródła czasu", "zarządzanie źródłem czasu", "Synchronizacja czasu w systemie Windows", "najlepsze praktyki w zakresie zarządzania czasem", "konfiguracja źródła czasu", "synchronizacja czasu systemowego", "Synchronizacja czasu domeny Windows", "samodzielna synchronizacja czasu maszyny", "wybór źródła czasu", "Rozwiązywanie problemów ze źródłem czasu", "błędy źródła czasu", "kwestie źródła czasu", "polecenia konfiguracji źródła czasu", "instrukcje konfiguracji źródła czasu", "Wyzwania związane z synchronizacją czasu", "konsekwencje utraty czasu", "zapobieganie dryftowi czasowemu", "rozwiązywanie błędów synchronizacji czasu", "Rozwiązywanie problemów z synchronizacją czasu", "zarządzanie źródłami czasu w domenach Windows", "obsługa źródeł czasu w autonomicznych komputerach z systemem Windows", "zapobieganie utracie czasu w środowiskach Windows", "konsekwencje awarii synchronizacji czasu", "najlepsze praktyki dotyczące dokładnego rejestrowania czasu pracy"]
cover: "/img/cover/An_image_depicting_a_clock_being_synchronized_with_a_domain.png"
coverAlt: "Obraz przedstawiający zegar synchronizowany z kontrolerem domeny i samodzielną maszyną, symbolizujący zarządzanie źródłami czasu i dokładną synchronizację czasu w środowiskach Windows."
coverCaption: ""
---

**Jak ustawić i obsługiwać źródła czasu w domenie Windows i na autonomicznych maszynach z systemem Windows**

Synchronizacja czasu ma kluczowe znaczenie dla utrzymania dokładnych znaczników czasu i zapewnienia prawidłowego funkcjonowania systemów w domenie Windows lub na autonomicznych maszynach z systemem Windows. W tym artykule omówimy najlepsze praktyki ustawiania i obsługi źródeł czasu w obu scenariuszach, podkreślając znaczenie członków domeny wskazujących na kontrolery domeny. Przeanalizujemy również różne opcje źródeł czasu, podkreślając wykorzystanie zewnętrznych pul NTP lub serwerów czasu opartych na GPS w celu uzyskania optymalnej dokładności.

______

## Ustawianie źródeł czasu w domenie Windows

W domenie Windows niezbędna jest spójna synchronizacja czasu we wszystkich elementach członkowskich domeny. Najlepszą praktyką jest skonfigurowanie kontrolerów domeny jako podstawowego źródła czasu dla członków domeny. W ten sposób zapewniasz, że wszystkie systemy w domenie mają zsynchronizowany czas, co ma kluczowe znaczenie dla uwierzytelniania, rejestrowania i różnych operacji domeny.

### Opcje źródła czasu dla kontrolerów domeny

Kontrolery domeny mogą pobierać czas z różnych źródeł, w tym z zegara BIOS, narzędzi VMware (w środowiskach zwirtualizowanych) lub zewnętrznych serwerów czasu. Chociaż korzystanie z zegara BIOS lub narzędzi VMware może być wygodne, zaleca się korzystanie ze źródła **stratum 0 lub 1**, takiego jak zewnętrzna pula NTP lub serwer czasu oparty na GPS w celu zwiększenia dokładności.

#### Zewnętrzne pule NTP

Zewnętrzne pule NTP są globalnie rozproszonymi i niezawodnymi źródłami synchronizacji czasu. Składają się one z dużej liczby serwerów NTP utrzymywanych przez organizacje i instytucje na całym świecie. Konfigurując kontrolery domeny do synchronizacji z zewnętrznymi pulami NTP, można zapewnić dokładną synchronizację czasu w domenie Windows.

Aby skonfigurować kontrolery domeny do korzystania z zewnętrznej puli NTP, wykonaj następujące kroki:

1. Otwórz wiersz polecenia z podwyższonym poziomem uprawnień na kontrolerze domeny.
2. Wykonaj następujące polecenie:

```shell
w32tm /config /syncfromflags:manual /manualpeerlist:"pool.ntp.org" /reliable:yes /update
```

To polecenie konfiguruje kontroler domeny do synchronizacji z pulą NTP pool.ntp.org. Dostosuj polecenie, aby użyć innej puli NTP lub wielu źródeł, jeśli chcesz.

3. Uruchom ponownie usługę Czas systemu Windows, aby zastosować zmiany:

```shell
net stop w32time && net start w32time
```


#### Serwery czasu oparte na GPS

Inną opcją dla kontrolerów domeny jest wykorzystanie serwerów czasu opartych na GPS. Serwery te opierają się na sygnałach GPS, aby zapewnić bardzo dokładne informacje o czasie. Konfigurując lokalnie hostowany serwer czasu oparty na GPS i konfigurując kontrolery domeny do synchronizacji z nim, można uzyskać precyzyjną synchronizację czasu w domenie Windows.

### Konfigurowanie członków domeny

Elementy członkowskie domeny, takie jak maszyny klienckie i inne serwery, powinny być skonfigurowane tak, aby synchronizowały swój czas z kontrolerami domeny. Zapewnia to, że wszystkie systemy w domenie pozostają zsynchronizowane i unikają wszelkich problemów związanych z czasem.

Aby skonfigurować elementy członkowskie domeny do synchronizacji czasu z kontrolerami domeny, zwykle nie są wymagane żadne dodatkowe kroki. Domyślnie elementy członkowskie domeny automatycznie synchronizują swój czas z kontrolerami domeny.

______

## Ustawianie źródeł czasu na autonomicznych komputerach z systemem Windows

Na autonomicznych komputerach z systemem Windows, które nie są częścią domeny, proces ustawiania źródeł czasu może się różnić w zależności od wersji systemu Windows i ustawień regionalnych. Domyślnie samodzielne maszyny z systemem Windows zazwyczaj używają **time.windows.com** jako podstawowego źródła czasu. Warto jednak zauważyć, że domyślne zachowanie można zmodyfikować.

### Zmiana źródła czasu na autonomicznych komputerach

Jeśli chcesz zmienić źródło czasu na autonomicznym komputerze z systemem Windows, możesz wykonać następujące kroki:

1. Otwórz wiersz polecenia z podwyższonym poziomem uprawnień na komputerze.
2. Wykonaj następujące polecenie, aby skonfigurować serwer NTP:

```shell
w32tm /config /syncfromflags:manual /manualpeerlist:"time.windows.com" /update
```

To polecenie ustawia time.windows.com jako źródło czasu dla maszyny autonomicznej. W razie potrzeby można dostosować polecenie, aby użyć innego źródła czasu.

3. Uruchom ponownie usługę Windows Time, aby zmiany zaczęły obowiązywać:

```shell
net stop w32time && net start w32time
```


Wykonując te polecenia, można skonfigurować autonomiczną maszynę z systemem Windows do synchronizacji czasu z wybranym źródłem czasu.

______

## Wnioski

Prawidłowa synchronizacja czasu jest niezbędna zarówno dla domen Windows, jak i samodzielnych maszyn. W domenie Windows kluczowe jest skonfigurowanie członków domeny tak, aby wskazywali kontrolery domeny w celu synchronizacji czasu. Kontrolery domeny mogą uzyskiwać swój czas z różnych źródeł, przy czym korzystanie z zewnętrznych pul NTP lub serwerów czasu opartych na GPS jest zalecaną praktyką w celu zwiększenia dokładności.

Na autonomicznych komputerach z systemem Windows domyślnym źródłem czasu jest zazwyczaj time.windows.com. Można jednak zmienić źródło czasu za pomocą dostarczonych poleceń.

Postępując zgodnie z tymi najlepszymi praktykami i konfigurując odpowiednie źródła czasu, zapewniasz dokładne śledzenie czasu, niezawodne uwierzytelnianie i spójne rejestrowanie w środowisku Windows.

______

## Referencje

- [Microsoft Docs: How the Windows Time Service Works](https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/how-the-windows-time-service-works)
- [Microsoft Docs: Windows Time Service Tools and Settings](https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)
- [NTP Pool Project](https://www.ntppool.org/)
- [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)


---
title: "Thunderbird 153.6: Ujawnienie danych uwierzytelniających NTLM w Windows i aktualizacja (2026)"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Dwie poważne luki w Thunderbirdzie mogą ujawnić dane uwierzytelniające NTLM w Windows po wyświetleniu spreparowanej wiadomości. Poznaj oba mechanizmy, sprawdź wersję programu i ogranicz wychodzący ruch SMB podczas aktualizacji."
genre: ["Cyberbezpieczeństwo", "Bezpieczeństwo poczty e-mail", "Bezpieczeństwo Windows"]
tags: ["Thunderbird 153.6", "Thunderbird 153.6.0esr", "aktualizacja zabezpieczeń Thunderbirda", "luka Thunderbirda w Windows", "ujawnienie NTLM przez Thunderbirda", "uwierzytelnianie SMB w Thunderbirdzie", "CVE-2026-118174", "CVE-2026-118176", "MFSA 2026-122", "załącznik z kluczem OpenPGP", "zewnętrzny załącznik", "blokowanie zdalnej zawartości", "adres URL mailbox", "ścieżka UNC o rozszerzonej długości", "nazwa konta Windows", "dane uwierzytelniające NTLM", "ujawnienie danych SMB", "wychodzący SMB", "port TCP 445", "bezpieczeństwo poczty e-mail", "klient poczty Windows", "sprawdzanie wersji Thunderbirda", "aktualizacja Thunderbirda", "przekaźnik NTLM", "łamanie haseł offline"]
cover: ""
coverAlt: ""
coverCaption: ""
---

Mozilla naprawiła w Thunderbirdzie 153.6 dwie **poważne luki ujawniające dane uwierzytelniające Windows**. Samo wyświetlenie spreparowanej wiadomości mogło uruchomić jedno z żądań sieciowych opisanych w [MFSA 2026-122](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/). Biuletyn mówi o możliwym ujawnieniu danych NTLM, a nie o potwierdzonym przejęciu danych każdego odbiorcy.

<!--more-->

## Najważniejsze informacje

- **CVE-2026-118174** dotyczyła zewnętrznie hostowanego załącznika z kluczem OpenPGP. Wyświetlenie wiadomości uruchamiało żądanie bez działania użytkownika, nawet przy zablokowanej zdalnej zawartości.
- **CVE-2026-118176** dotyczyła specjalnie spreparowanego adresu URL `mailbox:` ze ścieżką UNC o rozszerzonej długości. Wyświetlenie wiadomości nawiązywało połączenie SMB z serwerem wybranym przez nadawcę.
- **Zaktualizuj Thunderbirda w Windows** i sprawdź zainstalowaną wersję. Biuletyn wskazuje Thunderbird 153.6 jako wersję z poprawką. Informacje o wydaniu Thunderbirda wymieniają odpowiadającą jej kompilację 153.6.0esr.

## Co wywołuje wiadomość

**Obie luki mają różne punkty wejścia.** Według opisów Mozilli odbiorca nie musi klikać żadnego odnośnika w wiadomości. Ryzyko dla danych uwierzytelniających Windows zależy od tego, czy żądanie sieciowe dotrze do udziału kontrolowanego przez atakującego i czy dojdzie do wymiany danych uwierzytelniających. Mozilla nie informuje w biuletynie o aktywnym wykorzystywaniu tych luk.

| Problem | Wyzwalacz podczas wyświetlania wiadomości | Ryzyko dla danych uwierzytelniających Windows |
| --- | --- | --- |
| **CVE-2026-118174** | Thunderbird ładuje zawartość załącznika z kluczem OpenPGP, aby zaproponować import klucza. Nadawca oznacza go jako zewnętrzny załącznik z adresem URL wybranym przez atakującego. | Adres URL udziału sieciowego ujawnia dane NTLM użytkownika, jeśli żądanie dotrze do tego udziału. |
| **CVE-2026-118176** | Ścieżka UNC o rozszerzonej długości omija ograniczenie Thunderbirda dotyczące zdalnych udziałów w adresach URL `mailbox:`. | Thunderbird łączy się z serwerem SMB wybranym przez atakującego i ujawnia nazwę konta Windows oraz dane uwierzytelniające NTLM. |

W przypadku ścieżki przez **załącznik OpenPGP** Mozilla wyraźnie stwierdza, że żądanie omijało blokowanie zdalnej zawartości i nie wymagało działania użytkownika. Na systemach innych niż Windows problem również pozwalał na żądanie zdalne wbrew ustawieniu dotyczącym zdalnej zawartości, ale Mozilla ogranicza wyciek danych uwierzytelniających NTLM do Windows. Według Mozilli ścieżka przez adres URL **`mailbox:`** nie wpływa na inne systemy operacyjne. Zobacz osobne wpisy dotyczące [CVE-2026-118174](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118174) i [CVE-2026-118176](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118176).

**Dane uwierzytelniające NTLM nie są hasłem w postaci jawnej.** Mozilla podaje, że dane ujawnione przez ścieżkę SMB stwarzają ryzyko łamania haseł offline lub ataków przekaźnikowych. Samo otrzymanie spreparowanej wiadomości nie dowodzi skutecznego ataku. Biuletyn wymienia też inne luki w Thunderbirdzie, w tym osobne ścieżki związane z kalendarzem i RSS. Ten artykuł omawia dwie ścieżki uruchamiane przez wyświetlenie wiadomości i nie utożsamia wszystkich problemów z tego wydania.

## Sprawdź i zaktualizuj Thunderbirda

Problem dotyczy **czytania poczty w Thunderbirdzie w Windows** przed zainstalowaniem odpowiedniej poprawki. Mozilla wskazuje **Thunderbird 153.6** jako wersję z poprawką, ale nie podaje pełnego zakresu najstarszych wersji podatnych na te dwa problemy. [Informacje o wydaniu 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/) wskazują kompilację ESR opublikowaną 27 października 2026 r. Nie wyciągaj wniosków o stanie poprawek w innym kanale, forku ani przepakowanej kompilacji wyłącznie z oznaczenia wersji.

1. W Windows otwórz **Help > About Thunderbird**. Sprawdź wersję widoczną w oknie About, które również sprawdza dostępność aktualizacji. [Instrukcje aktualizacji Mozilli](https://support.mozilla.org/en-US/kb/updating-thunderbird) opisują tę ścieżkę.
2. Jeśli aktualizacja jest dostępna, pozwól Thunderbirdowi ją pobrać, a następnie wybierz **Restart Thunderbird to Update**. Po ponownym uruchomieniu otwórz ponownie **Help > About Thunderbird** i potwierdź zainstalowaną wersję.
3. W przypadku **linii 153 ESR** porównaj uzyskaną wersję z **153.6.0esr** w informacjach o wydaniu Thunderbirda. Jeśli aktualizacjami zarządza organizacja, poproś administratora o potwierdzenie poprawki dostawcy zamiast zakładać, że aktualizacja jest już zainstalowana.

> **Uwaga dotycząca wersji:** Informacje o wydaniu 153.6.0esr potwierdzają dostępność tego wydania, a MFSA 2026-122 łączy poprawki zabezpieczeń z Thunderbirdem 153.6. Informacje o wydaniu nie opisują osobno tych dwóch CVE. Szczegóły luk znajdziesz w biuletynie.

## Ogranicz ryzyko podczas aktualizacji

**Najpierw zainstaluj poprawkę dostawcy.** Samo wyłączenie zdalnej zawartości nie zatrzymuje CVE-2026-118174, ponieważ opisane żądanie omijało to ustawienie. Zalecenie „nie klikaj” nie wystarczy. Mozilla opisuje żądania uruchamiane przez wyświetlenie wiadomości.

Jako **dodatkową warstwę ochrony** ogranicz wychodzący ruch SMB z klientów Windows do internetu, w tym **port TCP 445**, na zaporze firmowej lub zarządzanych urządzeniach. [Wytyczne Microsoft dotyczące ruchu SMB](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic) zalecają blokowanie wychodzącego ruchu TCP 445 do internetu i ograniczenie dostępu do wymaganych serwerów plików. Przed wymuszeniem reguły zinwentaryzuj potrzebne udziały, zwłaszcza jeśli środowisko korzysta z usługi plików w chmurze lub obejmuje pracowników zdalnych poza siecią firmową. Ta kontrola sieciowa ogranicza opisaną ścieżkę SMB, ale nie naprawia Thunderbirda ani nie rozwiązuje wszystkich problemów ze zdalnymi żądaniami wymienionych w biuletynie.

Jeśli komputer z Windows i starszą wersją Thunderbirda wyświetlił podejrzaną wiadomość, **potraktuj narażenie jako kwestię do zbadania, a nie dowód przejęcia systemu**. Wspólnie z zespołem bezpieczeństwa sprawdź dostępne logi wychodzących połączeń SMB i uwierzytelniania. Biuletyn dostawcy nie zawiera testu narażenia ani ogólnego zalecenia zmiany wszystkich haseł.

## Źródła

- [Mozilla Foundation Security Advisory 2026-122: luki zabezpieczeń naprawione w Thunderbirdzie 153.6](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/)
- [Informacje o wydaniu Thunderbird Desktop: 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/)
- [Mozilla Support: aktualizacja Thunderbirda do najnowszej wersji](https://support.mozilla.org/en-US/kb/updating-thunderbird)
- [Microsoft Learn: zabezpieczanie ruchu SMB w Windows Server](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)

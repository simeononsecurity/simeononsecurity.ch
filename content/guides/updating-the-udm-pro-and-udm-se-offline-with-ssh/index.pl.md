---
title: "Aktualizacja firmware offline dla Ubiquiti Unifi UDM Pro i UDM SE przez SSH z wiersza poleceń"
draft: false
toc: true
date: 2023-05-28
description: "Dowiedz się, jak zaktualizować oprogramowanie sprzętowe Ubiquiti Unifi UDM Pro i UDM SE w trybie offline za pomocą wiersza poleceń SSH, aby uzyskać optymalną wydajność i bezpieczeństwo."
tags: ["Aktualizacja oprogramowania układowego Ubiquiti", "UDM Pro", "UDM SE", "aktualizacja oprogramowania sprzętowego offline", "Wiersz poleceń SSH", "zarządzanie siecią", "bezpieczeństwo sieci", "aktualizacja oprogramowania sprzętowego", "Połączenie SSH", "plik oprogramowania układowego", "Kontroler sieci UniFi", "poprawki błędów", "poprawa wydajności", "poprawki zabezpieczeń", "networking", "urządzenia sieciowe", "technologia", "Zarządzanie IT", "Proces aktualizacji oprogramowania sprzętowego", "optymalizacja sieci", "Aktualizacja oprogramowania sprzętowego Ubiquiti Networks", "Aktualizacja oprogramowania sprzętowego UDM Pro", "Aktualizacja oprogramowania sprzętowego UDM SE", "Proces aktualizacji oprogramowania sprzętowego offline", "Aktualizacja oprogramowania sprzętowego SSH", "zarządzanie urządzeniami sieciowymi", "aktualizacje zabezpieczeń sieci", "strategie aktualizacji oprogramowania sprzętowego", "Zarządzanie oprogramowaniem sprzętowym offline", "optymalizacja wydajności sieci", "zarządzanie poprawkami zabezpieczeń", "aktualizacje technologii sieciowych"]
cover: "/img/cover/A_colorful_illustration_depicting_a_computer_connecting.png"
coverAlt: "Kolorowa ilustracja przedstawiająca komputer łączący się z routerem przez SSH symbolizuje proces aktualizacji oprogramowania sprzętowego offline dla urządzeń Ubiquiti Unifi UDM Pro i UDM SE."
coverCaption: ""
---

**Aktualizacja Ubiquiti Unifi UDM Pro i UDM SE offline przez SSH**

W świecie sieci **Ubiquiti Networks** zyskało uznanie za swoje innowacyjne rozwiązania. **Ubiquiti Unifi Dream Machine Pro (UDM Pro)** i **Unifi Dream Machine SE (UDM SE)** to dwa popularne produkty, które oferują kompleksowe funkcje zarządzania siecią. Aktualizacja oprogramowania sprzętowego tych urządzeń ma kluczowe znaczenie dla zapewnienia optymalnej wydajności i bezpieczeństwa. W tym artykule dowiemy się, jak zaktualizować oprogramowanie sprzętowe UDM Pro i UDM SE **offline** za pomocą SSH wiersza poleceń.

______

## Dlaczego warto aktualizować firmware?

Aktualizacje oprogramowania układowego są niezbędne dla każdego urządzenia sieciowego, ponieważ często zawierają poprawki błędów, ulepszenia wydajności i poprawki bezpieczeństwa. Regularne aktualizowanie oprogramowania sprzętowego UDM Pro i UDM SE ma kluczowe znaczenie dla zapewnienia bezpieczeństwa i płynnego działania sieci.

______

## Aktualizacja oprogramowania sprzętowego offline

Aktualizację oprogramowania sprzętowego UDM Pro i UDM SE można przeprowadzić za pośrednictwem **UniFi Dashboard**. Jednak w niektórych scenariuszach połączenie internetowe może nie być dostępne lub pożądane. W takich przypadkach aktualizacja offline przy użyciu SSH wiersza poleceń stanowi alternatywne rozwiązanie.

______

## Przygotowanie do aktualizacji offline

Przed przystąpieniem do aktualizacji offline należy upewnić się, że spełnione są następujące warunki wstępne:

1. Komputer lub urządzenie z zainstalowanym klientem SSH.
2. Najnowszy plik oprogramowania sprzętowego dla UDM Pro lub UDM SE. Plik oprogramowania sprzętowego można uzyskać ze strony [Ubiquiti Downloads](https://www.ui.com/download/unifi) for the [UDM Pro](https://www.ui.com/download/unifi/unifi-dream-machine-pro) page. For early access firmwares, you can see them on the [community releases page](https://community.ui.com/releases) once you've signed into your.[**ui.com**](https://account.ui.com/) konto

______

## Nawiązywanie połączenia SSH

Aby zaktualizować UDM Pro lub UDM SE za pomocą SSH wiersza poleceń, wykonaj następujące kroki:

1. Upewnij się, że komputer lub urządzenie jest podłączone do tej samej sieci co UDM Pro lub UDM SE.
2. Otwórz preferowanego klienta SSH i nawiąż połączenie SSH z adresem IP **UDM Pro lub UDM SE**. Na przykład, używając klienta **OpenSSH** w systemie Linux lub macOS, można użyć następującego polecenia:

```bash
ssh root@<UDM_IP_ADDRESS>
```

Wymiana `<UDM_IP_ADDRESS>` z rzeczywistym adresem IP UDM Pro lub UDM SE.

3. Po wyświetleniu monitu wprowadź **nazwę użytkownika** i **hasło**. Domyślne poświadczenia dla urządzeń Ubiquiti to zazwyczaj `ubnt` zarówno dla nazwy użytkownika, jak i hasła.

______

## Aktualizacja oprogramowania sprzętowego

Po nawiązaniu połączenia SSH można przystąpić do aktualizacji oprogramowania sprzętowego:

1. Prześlij plik oprogramowania sprzętowego do UDM Pro lub UDM SE za pomocą **SCP (Secure Copy)**. SCP umożliwia bezpieczne przesyłanie plików przez SSH. Zakładając, że plik oprogramowania sprzętowego znajduje się na komputerze lokalnym, można użyć następującego polecenia:

```bash
scp <FIRMWARE_FILE_PATH> ubnt@<UDM_IP_ADDRESS>:/root/fwupdate.bin
```

Wymiana `<FIRMWARE_FILE_PATH>` ze ścieżką do pliku oprogramowania układowego na komputerze lokalnym, oraz `<UDM_IP_ADDRESS>` z adresem IP UDM Pro lub UDM SE.

2. Po przesłaniu pliku oprogramowania sprzętowego można rozpocząć proces aktualizacji oprogramowania sprzętowego. Wykonaj następujące polecenie:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "ubnt-tools fwupdate /root/fwupdate.bin"
```

3. UDM Pro lub UDM SE rozpocznie proces aktualizacji oprogramowania sprzętowego. Może to potrwać kilka minut. **Nie przerywaj procesu** do momentu zakończenia aktualizacji.

4. Po zakończeniu aktualizacji można zweryfikować wersję oprogramowania sprzętowego, logując się do kontrolera sieci UniFi lub wykonując następujące polecenie:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "show version"
```
Należy pamiętać, że powyższy proces zakłada, że masz niezbędny plik oprogramowania układowego dla UDM Pro lub UDM SE. Upewnij się, że masz odpowiedni plik oprogramowania sprzętowego dla konkretnego modelu i wersji urządzenia.

## Wnioski

Aktualizacja oprogramowania sprzętowego urządzeń Ubiquiti Unifi UDM Pro i UDM SE jest kluczowym krokiem w celu zapewnienia optymalnej wydajności i bezpieczeństwa. Podczas gdy UniFi Network Controller zapewnia wygodny sposób aktualizacji oprogramowania układowego, wykonanie aktualizacji offline za pomocą SSH wiersza poleceń stanowi realne rozwiązanie, gdy połączenie internetowe nie jest dostępne lub pożądane.

Postępując zgodnie z krokami opisanymi w tym artykule, można z powodzeniem zaktualizować oprogramowanie sprzętowe urządzeń UDM Pro i UDM SE za pomocą SSH wiersza poleceń. Pamiętaj, aby zawsze korzystać z najnowszej wersji oprogramowania sprzętowego dostarczonego przez Ubiquiti Networks, aby skorzystać z poprawek błędów, ulepszeń wydajności i poprawek bezpieczeństwa.

## Referencje

- [Ubiquiti Downloads](https://www.ui.com/download/unifi/) - Oficjalna strona Ubiquiti do pobrania plików firmware.
- [Unifi Advanced Updating Techniques](https://help.ui.com/hc/en-us/articles/204910064-UniFi-Upgrade-the-Firmware-of-a-UniFi-Device)

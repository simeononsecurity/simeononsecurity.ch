---
title: "Konfiguracja tuneli Cloudflare: Usprawnij i zabezpiecz swój ruch sieciowy"
draft: false
toc: true
date: 2023-05-26
description: "Dowiedz się, jak skonfigurować tunele Cloudflare, aby usprawnić i chronić ruch sieciowy, zwiększając wydajność i bezpieczeństwo."
tags: ["Tunele Cloudflare", "Bezpieczeństwo sieci", "Wydajność strony internetowej", "Serwer proxy", "Ruch internetowy", "Konfiguracja sieci", "Ubuntu Server", "Konto Cloudflare", "Uwierzytelnianie", "Tworzenie tunelu", "Routing ruchu", "Rekordy DNS", "Bezpieczne połączenie", "Hosting stron internetowych", "Usługa proxy", "Ochrona sieci", "Optymalizacja wydajności", "Integracja z Cloudflare", "Konfiguracja serwera", "Szyfrowanie ruchu", "Zarządzanie ruchem sieciowym", "Bezpieczny hosting", "Bezpieczeństwo stron internetowych", "Konfiguracja Ubuntu", "Technologia tunelowania", "Usługi Cloudflare", "Wydajność sieci", "Bezpieczeństwo w sieci", "Bezpieczeństwo serwera", "Zarządzanie ruchem", "Cloudflare Proxy"]
cover: "/img/cover/An_illustration_showing_a_network_tunnel_connecting_a_local.png"
coverAlt: "Ilustracja przedstawiająca tunel sieciowy łączący lokalny serwer z logo Cloudflare, symbolizującym bezpieczny i usprawniony ruch sieciowy."
coverCaption: ""
---

**Przewodnik po konfigurowaniu tuneli Cloudflare**

## Wprowadzenie
Tunele Cloudflare zapewniają bezpieczny sposób hostowania stron internetowych poprzez ustanowienie bezpośredniego połączenia między siecią lokalną a Cloudflare. Ten przewodnik przeprowadzi cię przez proces konfigurowania tuneli Cloudflare w celu zwiększenia bezpieczeństwa i wydajności twojej strony internetowej.

______

## Dlaczego tunele Cloudflare?
Tunele Cloudflare oferują szereg korzyści, w tym ograniczenie wektorów ataków i uproszczenie konfiguracji sieci. Wykorzystując Cloudflare jako serwer proxy, można zamknąć zewnętrzne porty i zapewnić, że cały ruch przechodzi przez bezpieczną sieć Cloudflare. Zapewnia to dodatkową warstwę ochrony witryny.

______

## Wymagania wstępne
Przed skonfigurowaniem tuneli Cloudflare należy upewnić się, że dostępne są następujące elementy:

1. Aktywne konto Cloudflare.
2. Serwer z systemem Ubuntu.

______

## Krok 1: Instalacja
Aby rozpocząć, należy zainstalować pakiet Cloudflare Tunnels na serwerze Ubuntu. Wykonaj następujące kroki:

1. Otwórz terminal na serwerze Ubuntu.
2. Pobierz najnowszą wersję pakietu Cloudflare Tunnels, uruchamiając następujące polecenie:

```shell
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
```

## Krok 2: Uwierzytelnianie
Następnie musisz uwierzytelnić swoje konto Cloudflare za pomocą usługi Cloudflare Tunnels. Wykonaj następujące kroki:

1. Uruchom następujące polecenie w terminalu:

```shell
cloudflared tunnel login
```

2. Kliknij witrynę, której chcesz używać z tunelem, aby zakończyć proces uwierzytelniania.

## Krok 3: Tworzenie tunelu

Teraz nadszedł czas, aby utworzyć tunel Cloudflare. Wykonaj następujące kroki:

1. Uruchom następujące polecenie w terminalu, aby utworzyć tunel:

```shell
cloudflared tunnel create name_of_tunnel
```

2. Wybierz nazwę tunelu, która będzie łatwa do zapamiętania i opisowa. Należy pamiętać, że nazwy tunelu nie można później zmienić.

3. Po utworzeniu tunelu zostaną wyświetlone ważne informacje, w tym identyfikator UUID tunelu. Zanotuj ten identyfikator UUID, ponieważ będzie on wymagany do dalszej konfiguracji.

4. Aby wyświetlić listę wszystkich aktywnych tuneli, użyj polecenia:

```shell
cloudflared tunnel list
```

Spowoduje to wyświetlenie nazw i identyfikatorów UUID tuneli.

### Krok 4: Konfiguracja tunelu

Aby skonfigurować tunel i rozpocząć kierowanie ruchu, wykonaj następujące kroki:

1. Przejdź do katalogu Cloudflare Tunnels na swoim serwerze. Domyślna lokalizacja to `/etc/cloudflared`

2. W tym katalogu utwórz nowy plik o nazwie `config.yml` przy użyciu wybranego edytora tekstu.

3. Wypełnij plik config.yml następującą zawartością:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json
```

Pamiętaj, aby wymienić `<your_tunnels_uuid>` z identyfikatorem UUID tunelu i w razie potrzeby zaktualizuj ścieżkę do pliku poświadczeń.

## Krok 5: Routing ruchu

Aby określić usługi wewnętrzne, które mają być obsługiwane przez tunel, wykonaj następujące kroki:

1. `Open the ` plik ponownie.

2. Dodaj parametry wejściowe do pliku, aby zdefiniować usługi, które mają być kierowane przez Cloudflare. Na przykład:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json

ingress:
  - hostname: example.com
    service: http://10.10.10.123:1234
  - hostname: subdomain.example.com
    service: http://10.10.10.123:8888
  - service: http_status:404

```

Wymiana `<your_tunnels_uuid>` z identyfikatorem UUID tunelu i zaktualizuj nazwę hosta i szczegóły usługi zgodnie z konfiguracją.

3. Zapisz plik config.yml.


## Krok 6: Tworzenie rekordów DNS

Aby utworzyć rekordy DNS dla nazwy hosta i usług tunelu, wykonaj następujące kroki:

1. Otwórz terminal.

2. Użyj następującego polecenia, aby utworzyć rekord DNS:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> <hostname>
```
Wymiana `<UUID or NAME of tunnel>` z identyfikatorem UUID lub nazwą tunelu, oraz `<hostname>` z żądaną nazwą hosta dla usługi.

3. Na przykład, aby utworzyć rekord DNS dla example.com, uruchom polecenie:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> example.com
```

Należy pamiętać, że zmiany zostaną odzwierciedlone w sekcji DNS na pulpicie nawigacyjnym Cloudflare.

## Krok 7: Uruchomienie tunelu

Aby przetestować i uruchomić tunel Cloudflare, wykonaj następujące kroki:

1. Otwórz terminal.

2. Uruchom następujące polecenie, aby uruchomić tunel:

```shell
cloudflared tunnel run <UUID or NAME of tunnel>
```

Wymiana `<UUID or NAME of tunnel>` z identyfikatorem UUID lub nazwą tunelu.

3. Cloudflared skonfiguruje teraz tunel i wyświetli informacje o jego statusie. Po pomyślnym uruchomieniu tunelu można przejść do następnego kroku.

4. Aby zapobiec zamknięciu tunelu po wyjściu z terminala, należy uruchomić Cloudflared jako usługę systemd. Użyj następującego polecenia:

```shell
cloudflared --config /path/to/config.yml service install
```

Wymiana `/path/to/config.yml` ze ścieżką do pliku `config.yml` plik.

## Wnioski

W tym przewodniku omówiliśmy kroki konfiguracji tuneli Cloudflare na Ubuntu. Postępując zgodnie z tymi instrukcjami, możesz zwiększyć bezpieczeństwo i wydajność swojej witryny, wykorzystując sieć Cloudflare. Pamiętaj, aby regularnie monitorować tunele i dostosowywać konfigurację w razie potrzeby.

Jeśli napotkasz jakiekolwiek problemy lub potrzebujesz dalszej pomocy, zapoznaj się z sekcją [official Cloudflare Tunnels documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)


## Referencje
- [Cloudflare Tunnels Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)
- [Cloudflare Tunnels GitHub Repository](https://github.com/cloudflare/cloudflared)
- [tcude - How to Set Up Cloudflare Tunnels on Ubuntu](https://tcude.net/creating-cloudflare-tunnels-on-ubuntu/)
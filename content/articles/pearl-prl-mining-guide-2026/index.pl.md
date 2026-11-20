---
title: "Kopanie Pearl (PRL) w 2026 roku: konfiguracja, rentowność i użyteczność łańcucha"
date: 2026-09-22
lastmod: 2026-11-20
toc: true
draft: false
description: "Skonfiguruj kopanie Pearl PRL w SRBMiner, poznaj dowód użytecznej pracy (proof-of-useful-work), oszacuj marże i oceń praktyczną użyteczność łańcucha."
genre: ["Kryptowaluty", "Kopanie na GPU", "Obliczenia AI", "DePIN", "Łańcuch bloków", "Linux", "Domowe laboratorium", "Sprzęt"]
tags: ["kopanie Pearl", "kopanie PRL", "Pearl PRL", "dowód użytecznej pracy (PoUW)", "PoUW", "NoisyGEMM", "SRBMiner Pearlhash", "pula kopania Pearl", "LuckyPool Pearl", "kopanie na GPU 2026", "krypto i obliczenia AI", "Pearl Research Labs", "kopanie łączone Nockchain", "kopanie łączone Nock", "kopanie RTX 3070", "konfiguracja SRBMiner", "zestaw do kopania Linux", "usługa minera systemd", "kopanie przez mnożenie macierzy", "program vLLM do kopania", "portfel Pearl", "adres prl1", "rentowność kopania", "kopanie obliczeń AI", "poradnik kopania kryptowalut", "kopanie NVIDIA", "ustawienia podkręcania do kopania"]
cover: "/img/cover/pearl-blockchain-gpu-mining-matrix-multiplication-2026.webp"
coverAlt: "Ilustracja nowoczesnego zestawu do kopania na GPU, który wykonuje mnożenie macierzy dla łańcucha bloków Pearl. Na ciemnym tle widać dynamiczne strumienie danych i żywe kolory."
coverCaption: ""
ref: ["/other/efficient-spacemesh-mining-multiple-gpus-guide", "/articles/local-ai-2026-build-your-rig-now"]
---

**Pearl to pierwszy łańcuch proof-of-useful-work, który osiągnął rzeczywistą skalę produkcyjną. Nagradza kopiących za mnożenie macierzy zamiast za haszowanie.** Sieć główna ruszyła **27 kwietnia 2026 roku**. W ciągu kilku tygodni obietnica zabezpieczania łańcucha bloków i generowania obliczeń AI w tym samym przebiegu wywołała gorączkę kopania na GPU.

*Twierdzenie jest technicznie prawdziwe, ale jego opłacalność nie została wykazana. Cała historia tkwi w różnicy między tymi dwoma stwierdzeniami.*

Ten poradnik pokazuje, jak kopać PRL, co oblicza miner, dlaczego marże szybko spadły po uruchomieniu sieci i czy łańcuch tworzy jakąś wartość.

**Po lekturze:** będziesz mieć portfel, zweryfikowanego minera, zmierzony pobór mocy i kalkulację rentowności dla własnej stawki za prąd. Traktuj szacunki pul i przychody z okresu startowego jako obserwacje z konkretnej daty, a nie gwarancję zakupu.

## Krótka odpowiedź

**Pearl to prawdziwe osiągnięcie techniczne, które mierzy się z problemem ekonomii kopania znanym każdej nowej monecie.**

| Pytanie | Krótka odpowiedź |
|---|---|
| **Co to jest?** | Łańcuch L1 wywodzący się z Bitcoin, zabezpieczany proof-of-useful-work. Kopiący wykonują zaszumione mnożenie macierzy zamiast SHA-256 |
| **Jak kopać?** | SRBMiner-MULTI z `--algorithm pearlhash` podłączony do puli albo własny miner vLLM Pearl połączony z własnym węzłem |
| **Dlaczego kopanie się opłacało?** | Przez kilka tygodni emisja z okresu startowego przewyższała trudność, która później ją dogoniła |
| **Czy nadal się opłaca?** | To zależy od sprzętu, a okno możliwości się zamyka. Zobacz część o marżach |
| **Czy łańcuch jest użyteczny?** | **Mechanizm tak, rynek jeszcze nie.** Szczegóły w werdykcie |

**Najważniejsza rzecz przed budową zestawu:** własne informacje o wydaniu 3.6.8 od twórcy minera mówią, że nadchodząca aktualizacja Pearl sprawi, że konsumenckie GPU będą „praktycznie bezużyteczne” do kopania. To nie opinia zewnętrznego krytyka. Mówi to autor minera.

## Czym jest Pearl

Pearl to łańcuch L1 stworzony przez **Pearl Research Labs**. Jego repozytorium opisuje go tak:

> "Pearl to łańcuch bloków L1 oparty na protokole proof-of-useful-work, w którym kopanie jest produktem ubocznym dowolnego mnożenia macierzy."

Repozytorium zawiera pełny węzeł, demona portfela, lekki klient SPV, system dowodów zerowej wiedzy i minera GPU. Projekt korzysta z **licencji ISC**, licencji permisywnej. Infrastruktura łańcucha pochodzi ze sprawdzonych projektów Bitcoin: **btcd** obsługuje węzeł, **btcwallet** portfel, a **neutrino** lekki klient.

**Projekt celowo naśladuje Bitcoin**, włącznie z maksymalną podażą **2,1 miliarda PRL**, czyli dokładnie stukrotnością 21 milionów Bitcoin. Nagroda za blok maleje, a bloki powstają mniej więcej co dwie minuty.

*Warstwa bazowa jest celowo zachowawcza. Nowość tkwi wyłącznie w funkcji pracy.*

### Na czym polega dowód użytecznej pracy (proof-of-useful-work)

Proof-of-useful-work to stary pomysł z marną historią. Założenie zawsze polegało na zastąpieniu celowo marnotrawnego haszowania Bitcoin obliczeniami, które przy okazji tworzą coś wartościowego. Niemal każda wcześniejsza próba kończyła się tak samo: „użyteczna” praca nie była użyteczna albo nie dało się jej tanio zweryfikować i zabezpieczyć łańcucha.

Pearl wdraża ten pomysł za pomocą procedury **NoisyGEMM**. Miner wykonuje na GPU zaszumione mnożenie macierzy, haszuje wynik do postaci commitmentu i opakowuje pracę w **dowód zerowej wiedzy**, aby łańcuch mógł tanio ją zweryfikować.

Schemat opiera się na artykule kryptograficznym z 2025 roku **"Proofs of Useful Work from Arbitrary Matrix Multiplication"** autorstwa Komargodskiego, Schena i Weinsteina. Artykuł szacuje narzut na około **1 + o(1)** względem naiwnego mnożenia macierzy. To kluczowe założenie całego projektu. Jeśli zabezpieczenie łańcucha kosztuje niemal nic ponad samą pracę obliczeniową, jej wygenerowanie jest prawie darmowe.

**Obietnica: jeden przebieg GPU, dwa wyniki.**

To właśnie odróżnia Pearl od dekady nieudanych koncepcji PoUW. Większość nie miała takiej granicy.

{{< figure src="pearl-noisygemm-proof-of-useful-work-flow.webp" alt="Schemat pokazujący, jak proof-of-useful-work Pearl zamienia mnożenie macierzy przez GPU w commitment haszujący i dowód zerowej wiedzy, które łańcuch tanio weryfikuje" >}}

### Co naprawdę oblicza program kopiący

Są dwie metody i nie są równoważne.

**Oficjalna metoda** znajduje się w repozytorium Pearl. Ma dwa elementy: `pearl-gateway`, który łączy z twoim węzłem, oraz `vllm-miner`, który wykonuje obliczenia na GPU przez vLLM. Brama komunikuje się lokalnie z węzłem `pearld` przez JSON-RPC i udostępnia interfejs kopania przez gniazdo Unix lub port TCP 8337.

**Metoda z pulą** jest najpopularniejsza. SRBMiner-MULTI obsługuje algorytm Pearl `pearlhash`, więc wystarczy wskazać pulę.

Ta różnica ma znaczenie dla oceny użyteczności. **Oficjalny miner ładuje prawdziwy model językowy.** Przykład z dokumentacji Pearl uruchamia `pearl-ai/Llama-3.3-70B-Instruct-pearl` w Dockerze z dostępem do GPU. Model z 70 miliardami parametrów obsługuje wnioskowanie, a ten sam przebieg zabezpiecza łańcuch.

*Generowanie wnioskowania to prawdziwa funkcja. Generowanie wnioskowania, za które nikt nie płaci, to koszt z dołączonym łańcuchem bloków. Nie myl tych pojęć.*

## Dlaczego kopanie się opłacało i co się zmieniło

Początkowa rentowność Pearl nie była tajemnicą i nie wynikała z AI. To typowa krzywa emisji nowej monety.

| Kiedy | Co się wydarzyło |
|---|---|
| **27 kwietnia 2026** | Uruchomienie sieci głównej |
| **Koniec maja 2026** | Pięć tygodni po uruchomieniu łańcucha zaczyna się gorączka kopania na GPU |
| **Czerwiec 2026** | Wraz ze wzrostem trudności szacowany dzienny przychód z RTX 5090 **spada mniej więcej o połowę** |
| **Środek i koniec 2026** | Wydajność oprogramowania minera mocno rośnie i częściowo równoważy spadek |

Mechanizm spadku jest prosty:

1. **Emisja startowa jest duża, a trudność niska.** Pierwsi kopiący uzyskują ponadprzeciętne nagrody na jednostkę hashrate.
2. **Nagrody przyciągają hashrate.** Do sieci podłączają się kolejne GPU.
3. **Trudność rośnie, by się dostosować.** Nagroda na GPU spada.

Pearl dokłada drugi czynnik spadkowy, bo nagroda za blok maleje zgodnie z projektem. **Przychody mają dwa powody, by spadać, a trudność jeden, by rosnąć.**

### Przeciwwaga: wydajność oprogramowania

Marże nie spadły jednakowo, bo minery stawały się szybsze. Historia zmian pearlhash w SRBMiner pokazuje postęp:

| Wersja | Zmiana Pearlhash |
|---|---|
| **3.6.1** | Dodano obsługę B300. B300 SXM6 przy `--gpu-cclock 1600` osiągał około **706 TH/s przy 920 W** |
| **3.6.2** | Usprawnienia dla H100, H200 i serii 4000 |
| **3.6.8** | Poprawa hashrate, głównie w serii 3000 |
| **3.6.9** | **Duże usprawnienia wydajności.** Taki sam lub wyższy hashrate przy znacznie niższym poborze mocy na większości architektur |

**Dla kopiących w domu prąd jest głównym kosztem operacyjnym.** Wydanie utrzymujące hashrate przy niższym poborze mocy bezpośrednio zwiększa marżę, bez zmian ceny tokena ani trudności sieci. Dlatego zestaw graniczny w czerwcu może wyglądać rozsądnie we wrześniu przy tym samym sprzęcie.

*Poprawa wydajności to realny, ale tymczasowy wiatr w plecy, bo inni też z niej korzystają i razem zwiększają trudność.*

## Soft fork z karą za rangę

W nocy **6 sierpnia 2026 roku** około **02:00 UTC, przy bloku 96251**, aktywował się soft fork Pearl. Wielu kopiących dowiedziało się o nim następnego ranka, gdy spadł im hashrate.

Protokół Pearl ma parametr **noise rank**. Wyższa ranga ułatwiała zdobycie jackpota przy tej samej ilości pracy. **Niektórzy kopiący celowo wybierali wysokie rangi i uzyskiwali nieproporcjonalnie duży efektywny hashrate oraz nagrody.** Zespół zbadał nietypowe optymalizacje kopania i wprowadził mechanizm kary.

| Zmiana reguły | Skutek |
|---|---|
| **Minimalna dozwolona ranga** | 128 |
| **Limit jackpota** | Teraz skalowany według wzoru `128 / rank` |
| **Przewaga wysokich rang** | Całkowicie usunięta |

**Wpływ na kopiących:**

- Kopanie powyżej rangi 128 kosztowało operatorów **50–87,5% efektywnego hashrate**
- Kopanie na randze 128 lub niższej prawie nic nie kosztowało

Osoby zaczynające teraz powinny pamiętać o dwóch rzeczach.

**Hashrate zależy od oprogramowania i reguł sieci, nie tylko od GPU.** Konfiguracja, która dobrze wypadała w lipcu, mogła nie mierzyć tego, co zakładał operator.

**Aktualizuj minera po zmianie sieci.** Starsze wersje tracą wydajność lub przestają poprawnie działać według nowych zasad. Przed forkiem zaktualizowano oprogramowanie pul, w tym PearlFortune v2.1.0 i Krig (Kryptex) v1.1.0, a także minery Tw-pearl-miner v3.3.0 i Wildrig 0.49.8.

*Soft fork obniżający nagrodę nawet o 87,5% jasno pokazuje, dlaczego trzeba śledzić komunikaty projektu, a nie tylko pulpit wypłat.*

## Dwa sposoby kopania Pearl

| | Kopanie w puli | Oficjalny miner vLLM |
|---|---|---|
| **Oprogramowanie** | SRBMiner-MULTI | `pearl-gateway` oraz `vllm-miner` |
| **Algorytm** | `pearlhash` | NoisyGEMM przez vLLM |
| **Wymaga węzła** | Nie | **Tak, zsynchronizowany `pearld`** |
| **Wypłata** | Pula, PPLNS lub solo | Bezpośrednio na adres kopania |
| **Uruchamia prawdziwy model** | Nie | **Tak, np. Llama-3.3-70B-Instruct** |
| **Nakład konfiguracji** | Niski | Wysoki, wymaga CUDA Toolkit i Python 3.12 |
| **Najlepsze do** | Szybkiego dostarczenia hashrate do sieci | Bezpośredniego dostarczania mocy obliczeniowej |

**Zacznij od kopania w puli.** Nie potrzebujesz węzła, synchronizacji ani pobierania modelu, a hashrate i adres wypłaty uzyskasz w kilka minut. Oficjalnego minera użyj tylko wtedy, gdy chcesz dostarczać wnioskowanie lub uruchamiać węzeł.

{{< figure src="pearl-mining-pool-vs-vllm-miner-comparison.webp" alt="Porównanie kopania Pearl w puli przez SRBMiner z oficjalnym minerem vLLM, pokazujące wymagane elementy: węzeł, bramę i wnioskowanie" >}}

## Sprzęt dla konsumenckich GPU

Pearl wyróżnia się tym, czego nie wymaga. Hashrate Index opisuje profil sprzętowy jako **wyjątkowo lekki: mało RAM-u, pamięci masowej i CPU, bez kosztownej sieci wieloświatłowodowej potrzebnej prawdziwemu klastrowi treningowemu.** Jeden analityk nazwał to „świetnym sposobem na wykorzystanie sprzętu”.

To właśnie jest prawdziwa zaleta. **Posiadane GPU, nawet starsze, coś zarabiają.**

| Klasa GPU | Obserwacja |
|---|---|
| **RTX 5090 i 4090** | Najwyższy przychód na kartę. W tych segmentach mierzono początkowy spadek przychodu o połowę |
| **Seria RTX 3000** | Wydanie 3.6.8 poprawiało hashrate szczególnie w tej serii. Nadal jest opłacalna, ale wydajność liczy się bardziej niż surowa szybkość |
| **Akceleratory centrów danych** | H100, H200 i B300 dodano i usprawniono w 2026 roku. W tym kierunku zmierza wyścig hashrate |
| **Starsze karty lub z małą ilością VRAM** | Na granicy opłacalności. Przed budową sprawdź aktualny kalkulator |

**Każde wydanie z 2026 roku pokazuje ten sam wzorzec.** Najpierw dodano i poprawiono flagowe akceleratory, bo tam hashrate jest najwięcej wart. Karty konsumenckie zyskały uwagę, gdy seria 3000 miała potencjał do poprawy.

*Optymalizacja wydajności daje większe przychody niż pogoń za częstotliwością zegara. To odwrotność porad z większości przewodników kopania.*

## Konfiguracja w systemie Linux

Kopanie przez pulę wymaga czterech rzeczy: pliku SRBMiner, adresu portfela Pearl, adresu puli i usługi utrzymującej proces.

### Najpierw utwórz adres portfela

Adresy kopania Pearl zaczynają się od **`prl1`**. Oficjalnym portfelem jest **Oyster**, demon portfela HD z repozytorium Pearl, udostępniający interfejsy JSON-RPC i gRPC. Wygeneruj w nim adres kopania **Taproot**.

Nie pomijaj tego kroku ani nie używaj ponownie adresu z innego łańcucha. **Nagrody wysłane na adres, którego nie kontrolujesz, przepadają.**

### Pule, porty i kopanie łączone

Największą pulą Pearl jest LuckyPool. Oferuje porty dopasowane do oczekiwanego hashrate:

| Port | Początkowa trudność | Zalecany hashrate |
|---|---|---|
| **3360** | 2M | Poniżej 500 TH/s |
| **3361** | 4M | 500–1000 TH/s |
| **3362** | 8M | Powyżej 1000 TH/s |

Wybierz port dopasowany do rzeczywistego hashrate zestawu. **Pojedyncze konsumenckie GPU powinno korzystać z portu 3360.** Mały zestaw na porcie o wysokiej trudności długo czeka na udziały i zwiększa zmienność bez korzyści.

Warto znać dwie funkcje pul:

- **Kopanie solo** działa na każdym porcie po dodaniu `solo:` przed adresem portfela. Gdy znajdziesz blok, zachowujesz całą nagrodę. W przeciwnym razie nie dostajesz nic. Przy hashrate konsumenckiego GPU trzeba długo czekać.
- **Kopanie łączone Nockchain** daje NOCK oprócz PRL przy tym samym hashrate. Dodaj `+NOCK_ADDRESS` do adresu Pearl. Pula wypłaca NOCK w samej Nockchain, więc nie odbierze go adres opakowanego tokena zaczynający się od `0x`. **Miner musi obsługiwać kopanie łączone. Bez tej funkcji nadal będzie normalnie kopać Pearl.**

Pula publikuje serwery `luckypool.io` i serwery trasujące `lproute.com`. Jeśli sieć blokuje bezpośredni ruch kopania, zachowaj port i zmień domenę.

## Działający skrypt instalacyjny

Poniższy skrypt konfiguruje SRBMiner jako usługę systemd w Debianie lub Ubuntu. Wykrywa wszystkie GPU, stosuje osobne ustawienia podkręcania, sprawdza pobrany plik według opublikowanego MD5, zapisuje jednostkę i regułę logrotate, a następnie restartuje usługę.

```bash
#!/usr/bin/env bash
# install-pearl-miner.sh -- konfiguruje SRBMiner (Pearl / PRL) jako usługę systemd.
# Uruchom: sudo bash install-pearl-miner.sh
set -euo pipefail

ALGO="pearlhash"
POOL="${POOL:-pearl-us-east.luckypool.io:3360}"
WALLET="${WALLET:-<YOUR_PR1_ADDRESS>}"   # prl1... dodaj +NOCK_ADDRESS do kopania łączonego
WORKER="${WORKER:-rig-1}"
SRB_VERSION="${SRB_VERSION:-3.6.9}"
MINER_DIR="/opt/srbminer"
UNIT="/etc/systemd/system/pearl-miner.service"
SVC="pearl-miner.service"
LOG="/var/log/pearl-miner.log"

# Ustawienia dla RTX 3070. MCORE blokuje zegar pamięci na stałej wartości znacznie niższej od
# fabrycznych 7001 MHz. To celowe obniżenie zegara dla wydajności, a nie podkręcenie osiągów.
# Ustaw dowolną wartość na "", aby wyłączyć tę opcję.
CCLOCK="${CCLOCK:-1560}"
MCLOCK="${MCLOCK:-5001}"
COFFSET="${COFFSET:-150}"
PLIMIT="${PLIMIT:-180}"
FAN="${FAN:-}"
THERMAL="${THERMAL:-88}"
```

Blok ustawień wymaga wyjaśnienia, bo na pierwszy rzut oka wygląda błędnie. **`MCORE=5001` jest poniżej fabrycznego zegara pamięci RTX 3070.** To celowe. Pearl premiuje wydajność pamięci, a obniżenie zegara pamięci zmniejsza pobór mocy bardziej niż hashrate. **Nie kopiuj ustawień podkręcania z bazy hashrate bez sprawdzenia, na jakim GPU wykonano pomiar.** Często użyto innej karty niż twoja.

```bash
[ "$(id -u)" -eq 0 ] || { echo "uruchom jako root (sudo)"; exit 1; }
command -v nvidia-smi >/dev/null || { echo "brak nvidia-smi, najpierw zainstaluj sterownik"; exit 1; }

GPU_N=$(nvidia-smi --query-gpu=index --format=csv,noheader | wc -l)
echo "== wykryte GPU NVIDIA: $GPU_N =="
nvidia-smi --query-gpu=index,name,memory.total,power.limit --format=csv,noheader

# Utwórz zestaw ustawień podkręcania dla każdego wykrytego GPU
OC=""
for i in $(seq 0 $((GPU_N - 1))); do
    [ -n "$COFFSET" ] && OC="$OC --gpu-coffset$i $COFFSET"
    [ -n "$CCLOCK" ]  && OC="$OC --gpu-cclock$i $CCLOCK"
    [ -n "$MCLOCK" ]  && OC="$OC --gpu-mclock$i $MCLOCK"
    [ -n "$PLIMIT" ]  && OC="$OC --gpu-plimit$i $PLIMIT"
    [ -n "$FAN" ]     && OC="$OC --gpu-fan$i $FAN"
done
THERMAL_ARG=""
[ -n "$THERMAL" ] && THERMAL_ARG=" --shutdown-temperature $THERMAL"

# Pobierz i sprawdź wydanie
STEM="SRBMiner-Multi-$(echo "$SRB_VERSION" | tr . -)-Linux"
BASE="https://github.com/doktor83/SRBMiner-Multi/releases/download/$SRB_VERSION"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
curl -fsSL -o "$TMP/$STEM.tar.gz"  "$BASE/$STEM.tar.gz"
curl -fsSL -o "$TMP/$STEM.tar.md5" "$BASE/$STEM.tar.md5"
(cd "$TMP" && md5sum -c <(tr -d '\r' < "$STEM.tar.md5"))

# Zatrzymaj usługę przed wymianą pliku binarnego, który jest otwarty przez proces
systemctl stop "$SVC" 2>/dev/null || true
tar -xzf "$TMP/$STEM.tar.gz" -C "$TMP"
SRC=$(find "$TMP" -maxdepth 1 -type d -name 'SRBMiner-Multi-*' | head -1)
mkdir -p "$MINER_DIR"
[ -f "$MINER_DIR/SRBMiner-MULTI" ] && \
    cp -a "$MINER_DIR/SRBMiner-MULTI" "$MINER_DIR/SRBMiner-MULTI.bak-$(date +%F-%H%M%S)"
cp -a "$SRC"/. "$MINER_DIR"/
chown -R root:root "$MINER_DIR"
chmod 755 "$MINER_DIR/SRBMiner-MULTI"
```

**Sprawdź MD5 przed uruchomieniem dowolnego pliku koparki.** Wydania publikują hashe dla każdego pliku, a miner działa jako root i odczytuje GPU. Pominięcie kontroli oznacza zaufanie plikowi, którego nie sprawdziłeś.

Dwa szczegóły operacyjne jednostki usługi:

```bash
cat >"$UNIT" <<EOF
[Unit]
Description=Miner Pearl (PRL) SRBMiner v$SRB_VERSION - $WORKER
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=$MINER_DIR
ExecStart=$MINER_DIR/SRBMiner-MULTI --algorithm $ALGO --pool $POOL --wallet $WALLET --worker $WORKER --disable-cpu --gpu-reset-oc$OC$THERMAL_ARG --api-enable --api-port 21550 --api-rig-name $WORKER
Restart=always
RestartSec=10
StandardOutput=append:$LOG
StandardError=append:$LOG
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
EOF
```

- **`--disable-cpu`** wyłącza kopanie na CPU, co ma znaczenie na komputerze wykonującym inne zadania.
- **`--shutdown-temperature 88`** zatrzymuje minera po awarii wentylatora, zamiast przegrzewać kartę.
- **`--gpu-reset-oc`** usuwa poprzednie ustawienia zegara przed zastosowaniem nowych i zapobiega pozostawieniu starych wartości.
- **`Restart=always` z `RestartSec=10`** pomaga przetrwać problemy ze sterownikiem, częste w zestawach z wieloma GPU.
- **`--api-enable` otwiera port monitorowania.** Sprawdź, na którym interfejsie nasłuchuje port 21550, i nie wystawiaj go do niezaufanej sieci. Punkt monitorowania zestawu nie musi być dostępny spoza komputera.

Na koniec skonfiguruj rotację logów, bo pliki z kopania rosną bez ograniczeń:

```bash
cat >/etc/logrotate.d/pearl-miner <<EOF
$LOG {
    weekly
    rotate 4
    compress
    delaycompress
    missingok
    notifempty
    copytruncate
}
EOF

systemctl daemon-reload
systemctl enable "$SVC" >/dev/null 2>&1 || true
systemctl restart "$SVC"
```

*`copytruncate` ma tu znaczenie. SRBMiner trzyma log otwarty. Jeśli rotacja zmieni nazwę pliku, miner nadal zapisuje do usuniętego inode, więc dysk i tak się zapełni.*

Śledź postępy za pomocą przefiltrowanych ostatnich wierszy zamiast surowego logu:

```bash
grep -aE 'Hashrate|accepted|Pool:' /var/log/pearl-miner.log | tail -20
```

## Co poszło nie tak

**Poradnik kopania Pearl musi zacząć od problemów, bo wszystkie wpływają na wypłaty.** Między lipcem a wrześniem 2026 roku wydarzyły się cztery rzeczy.

### Rynek zależy od jednej giełdy

**23 lipca 2026 roku** PRL osiągnął rekordowo niski poziom **0,1399 USD**, wobec około **0,87 USD** w czerwcu. Spadł o **24,2% w jeden dzień** i **26,7% w tydzień**, podczas gdy cały rynek krypto wzrósł w tym samym czasie o około 2%.

Przyczyną nie były wiadomości. Problemem była płynność.

- **95,17% całego zgłoszonego obrotu** przypadało na **jedną giełdę, SafeTrade**, która nie ma oceny zaufania CoinGecko. Jedna para PRL/USDT odpowiadała za **738 399 USD z około 775 000 USD** obrotu w ciągu doby.
- Głębokość arkusza zleceń obu par SafeTrade wynosiła **0,00 USD**.

*Zwykłe zlecenie sprzedaży może przesunąć taki rynek o kilkadziesiąt procent. To strukturalna cecha tokena, a nie chwilowa sytuacja.*

Rozkład podaży pogarsza sprawę:

| Wskaźnik | Wartość |
|---|---|
| **Kapitalizacja rynkowa** | 55,7 mln USD |
| **Wycena po pełnym rozwodnieniu** | 458,6 mln USD |
| **Stosunek** | Ponad 8 razy |
| **Podaż w obiegu** | 255 mln z 2,1 mld, poniżej **13%** |

**Token wyceniany na płytkim arkuszu z 87% podaży nadal zablokowanej lub niewyemitowanej może mieć bardzo różne wiarygodne ceny.** Zaplanuj wykorzystanie wypłat i nie traktuj ceny spot jako wiarygodnej prognozy przychodu.

### Pula została zhakowana

Zgłoszenie otwarte **18 września 2026 roku** mówi, że Pearl Wallet 2.0.5 „nadal wstrzymywał wysyłanie i odbieranie po włamaniu do puli sprzed miesiąca”.

**Przeczytaj to zdanie jeszcze raz, zawiera dwa fakty.** Około **sierpnia 2026 roku** ktoś przejął pulę Pearl, a oficjalny portfel wstrzymał przelewy. Miesiąc później blokada nadal obowiązywała.

Wybrana pula przechowuje twoje wypłaty. Przed podłączeniem zestawu sprawdź jej historię incydentów.

### Witryna projektu jest niedostępna

W chwili pisania artykułu **pearlresearch.ai nie prowadzi do żadnego serwera.** Wszystkie publiczne resolvery zwracają `0.0.0.0` dla domeny głównej i subdomen, takich jak `compute` i `explorer`. Rejestracja domeny ma status `ACTIVE`, więc to celowy stan DNS, a nie wygaśnięcie.

**Trzy linki, które zwykle pojawiłyby się w poradniku kopania, nie działają**, w tym eksplorator bloków. Mining Pool Stats nadal je wymienia, przez co czytelnicy próbują otwierać adresy, które nigdy się nie ładują.

Do przeglądania bloków użyj **[eksploratora bloków PRL](https://prlscan.com)**. Potwierdziłem, że strona działa.

### Oprogramowanie nadal ma nierozwiązane błędy

Pod koniec września 2026 roku publiczny rejestr problemów pokazywał nierozwiązane usterki. Dodawanie zgłoszeń jest ograniczone, więc to niepełny obraz.

| Problem | Data | Skutek |
|---|---|---|
| **Nieaktywna obsługa RPC w portfelu desktopowym** | 22 wrz. | Portfel nie łączy się z węzłem |
| **Testnet nie synchronizuje się od zera**, węzły blokują się na wysokości 36760 | 22 wrz. | Blokujący błąd synchronizacji |
| **Wysyłanie i odbieranie w portfelu nadal zawieszone** po włamaniu do puli | 18 wrz. | Problemy z transferami |
| **Wydanie macOS ARM64 ma nieprawidłowy podpis kodu** | 17 wrz. | Nie działa bez omijania Gatekeepera |
| **Tryb przycinania usuwa certyfikaty potrzebne do weryfikacji nagłówków** | 30 sie. | Błąd walidacji |
| **Węzeł blokuje się bez końca, gdy żaden połączony peer nie może synchronizować** | 30 sie. | Niestabilna synchronizacja |
| **pearl-gemm nie działa na RTX 5070**: działają jądra haszujące, ale jądra GEMM zawodzą | 31 sie. | Najnowsze karty konsumenckie nie są obsługiwane |

*Wpis o RTX 5070 jest ważny, jeśli planujesz kupić nową kartę. Najnowsza architektura konsumencka nie działała z oficjalną ścieżką GEMM.*

**Wniosek:** oprogramowanie do kopania jest aktywnie rozwijane, natomiast warstwa użytkowa i rynkowa są słabe. SRBMiner wydał 3.6.9 z dużymi usprawnieniami dzień przed skargami na portfel.

## Czy łańcuch jest użyteczny?

To pytanie wymaga ostrożnej odpowiedzi, bo w wielu tekstach „użyteczna praca” oznacza dwie rzeczy. **Opisuje mechanizm konsensusu i tezę ekonomiczną, a odpowiedzi na nie są zupełnie różne.**

### Użyteczność funkcjonalna: częściowa

**Łańcuch działa. Otaczający go produkt nie działa w pełni.**

Co działa:

- **Sieć główna ruszyła 27 kwietnia 2026 roku** i od tego czasu tworzy bloki.
- **Pełny zestaw narzędzi istnieje**: węzeł, demon portfela, lekki klient SPV, system dowodów zerowej wiedzy i miner GPU w jednym repozytorium.
- **Podstawa jest sprawdzona na poziomie kodu.** Węzeł, portfel i lekki klient pochodzą z **btcd**, **btcwallet** i **neutrino**, projektów Bitcoin testowanych przez lata przez przeciwników.
- **Baza kodu świadczy o poważnej pracy.** Ma 315 gwiazdek, 76 forków, ponad 6800 commitów i publiczny rejestr z precyzyjnymi raportami błędów.
- **Kopanie działa.** SRBMiner wydał 247 wersji i wielokrotnie usprawniał `pearlhash`. Działa kilka pul. Kopanie łączone Nockchain także działa.

Co nie działa:

- **Transfery w oficjalnym portfelu są wstrzymane** po włamaniu do puli.
- **Portfel desktopowy nie może połączyć się z węzłem**, według własnego rejestru z końca września.
- **Synchronizacja ma blokujące błędy** zarówno w testnecie, jak i w sieci głównej.
- **Witryna projektu jest niedostępna.**
- **Najnowsze konsumenckie GPU nie działają ze ścieżką GEMM.**

**Uczciwe podsumowanie: Pearl działa na poziomie protokołu, ale jako produkt jest zawodna.** To ważne dla osób badających proof-of-useful-work. To ostrzeżenie dla tych, którzy liczą na regularne kopanie i wypłaty.

### Użyteczność techniczna: mechanizm tak, rynek nie

Uczciwa odpowiedź ma dwie części. Mieszanie ich to błąd wielu publikacji.

**Mechanizm jest rzeczywiście nowatorski.** NoisyGEMM wykonuje na GPU zaszumione mnożenie macierzy, haszuje wynik do postaci commitmentu i opakowuje pracę w dowód zerowej wiedzy, aby tanio ją weryfikować. Konstrukcja opiera się na artykule "Proofs of Useful Work from Arbitrary Matrix Multiplication" autorstwa Komargodskiego, Schena i Weinsteina, który szacuje narzut na około **1 + o(1)** względem naiwnego mnożenia macierzy.

**Jeśli ta granica się utrzyma, łańcuch zabezpiecza się niemal bez dodatkowego kosztu ponad obliczenia.** Tego nie udało się osiągnąć wcześniejszym próbom PoUW. Matematyka nie jest ozdobą.

**Rynek nie jest ugruntowany.** Hashrate Index napisał, że „dziś większość użytecznej pracy to wnioskowanie, którego nikt nie kupił, więc większość kopania przypomina proof-of-work w stylu AI”. To trafne podsumowanie. Obliczenia mają właściwy charakter, ale prawie nikt za nie nie płaci.

Istnieje ważny i prawdziwy wyjątek. Pearl zawarł ekskluzywne partnerstwo z **Together AI**, które uruchomiło produkcyjny punkt dostępu do wnioskowania Pearl po obniżonej cenie. To pierwszy klient i powód, dla którego projekt zasługuje na większe uznanie niż przeciętna moneta z marką AI.

**Jeden klient potwierdza koncepcję, nie rynek.**

### Użyteczność praktyczna: na razie, ale okno się zamyka

Dla kopiącego sytuacja jest mieszana i ograniczona w czasie.

**Co przemawia za Pearl:**

- Posiadane GPU, nawet starsze, coś zarabiają, bo wymagania sprzętowe są niewielkie
- Ciągłe usprawnienia minera zwiększają marżę na posiadanym sprzęcie
- Kopanie łączone Nockchain dodaje drugie źródło przychodu przy tym samym hashrate
- Znikomy narzut oznacza, że łańcuch nie zużywa prądu na bezsensowne haszowanie

**Co przemawia przeciw:**

- **Nagroda za blok maleje zgodnie z projektem.** To model Bitcoin, a emisja spada niezależnie od ceny.
- **Trudność tylko rośnie.** Przychód na GPU może tylko spadać.
- **Płynność jest niska.** Hashrate Index wskazuje, że warto śledzić, czy PRL zyskuje płynność poza małymi giełdami. Niska płynność oznacza szersze spready i gorsze ceny sprzedaży.
- **Aktualizacja protokołu.** Informacje SRBMiner 3.6.8 mówią, że nadchodząca aktualizacja Pearl uczyni konsumenckie GPU „praktycznie bezużytecznymi”. Potraktuj to poważnie. To słowa twórcy, który korzysta na kontynuowaniu kopania.

## Werdykt

**Pearl to dotąd najbardziej wiarygodna implementacja proof-of-useful-work, ale nie udowodniła ekonomicznej użyteczności swojej pracy.**

Cztery twierdzenia w kolejności pewności:

1. **Mechanizm konsensusu działa, a twierdzenie kryptograficzne jest prawdziwe.** Pearl rozwiązał trudny problem techniczny: taniej weryfikować PoUW. To realny wkład niezależnie od przyszłości tokena.

2. **Obliczenia są obietnicą, nie produktem.** Generowanie wnioskowania to nie to samo co jego sprzedaż. Dziś płatny udział to jedno partnerstwo wobec sieci pełnej spekulacyjnego hashrate. Mechanizm jest zaprojektowany, ale jeszcze nie działa.

3. **Okno kopania na konsumenckich GPU się zwęża, a protokół je zamknie.** Malejąca nagroda, rosnąca trudność, zapowiedziana aktualizacja eliminująca użyteczność GPU konsumenckich i soft fork, który już obniżył hashrate części kopiących nawet o 87,5%, tworzą okazję ograniczoną czasowo, a nie źródło dochodu.

4. **Rzeczywiste ryzyko dotyczy operacji i rynku, nie kryptografii.** Zhakowana pula, wstrzymane transfery portfela, niedostępna witryna, nierozwiązane błędy synchronizacji i 95% obrotu na giełdzie bez głębokości arkusza decydują o wypłacie. Protokół jest częścią, która działa.

*Najkrócej: Pearl rozwiązał trudny problem, ale nie ten pozornie łatwy. Udowodnienie użyteczności mnożenia macierzy to kryptografia. Znalezienie nabywcy wyniku to sprzedaż.*

**Jeśli chcesz kopać, potraktuj to jako krótkoterminowe wykorzystanie posiadanego sprzętu.** Nie kupuj GPU dla Pearl. Nie buduj zestawu, zakładając, że obecne liczby się utrzymają. Harmonogram emisji i notatki twórcy minera mówią inaczej.

**Jeśli chcesz zrozumieć proof-of-useful-work, Pearl jest dziś najważniejszą implementacją do zbadania.** Jako pierwsza osiągnęła rzeczywistą skalę. Dowody z kolejnych dwóch lat pokażą, czy „użyteczna praca” to prawdziwy fundament, czy powtarzająca się porażka z lepszą kryptografią.

{{< figure src="pearl-prl-usefulness-assessment.webp" alt="Ocena proof-of-useful-work Pearl w trzech wymiarach: wysoka dojrzałość funkcjonalna, mocny mechanizm techniczny przy niepotwierdzonym rynku płatnych usług oraz ograniczona w czasie praktyczna opłacalność kopania" >}}

## Najważniejsze wnioski

- **Pearl to łańcuch L1 wywodzący się z Bitcoin i zabezpieczany proof-of-useful-work.** Kopiący wykonują zaszumione mnożenie macierzy zamiast haszowania. Sieć główna ruszyła **27 kwietnia 2026 roku**.
- **Można kopać na dwa sposoby:** SRBMiner z `--algorithm pearlhash` przez pulę albo `vllm-miner` Pearl na zsynchronizowanym węźle.
- **Początkowa rentowność wynikała z emisji startowej**, nie z popytu na AI. Szacowany dzienny przychód RTX 5090 spadł mniej więcej o połowę kilka tygodni po wzroście zainteresowania.
- **Usprawnienia minera częściowo zrównoważyły spadek.** Wersja 3.6.9 zapewniła taki sam lub wyższy hashrate przy dużo niższym poborze mocy.
- **Soft fork z karą za rangę z 6 sierpnia 2026 obniżył efektywny hashrate o 50–87,5%** kopiących powyżej rangi 128. Aktualizuj minera po zmianie reguł.
- **Token jest notowany głównie na jednej giełdzie.** SafeTrade skupiał 95,17% obrotu i miał zerową głębokość arkusza. W obiegu jest mniej niż 13% podaży.
- **Pula została zhakowana około sierpnia 2026 roku**, a oficjalny portfel wciąż wstrzymywał przelewy miesiąc później.
- **Domena witryny projektu nie rozwiązuje się.** Do przeglądania bloków użyj `prlscan.com`.
- **Optymalizuj wydajność, nie częstotliwość zegara.** Pearl premiuje sprawność pamięci, a jej obniżenie zmniejsza pobór mocy bardziej niż hashrate.
- **Przy jednym konsumenckim GPU użyj portu 3360** i dodaj `+NOCK_ADDRESS`, aby kopać Nockchain łącznie.
- **Sprawdź MD5** pobranego minera przed uruchomieniem jako root.
- **Kop z użyciem posiadanego sprzętu.** Łańcuch działa na poziomie protokołu, jest zawodny jako produkt, a płatny rynek obliczeń opiera się na jednym partnerstwie.

## Następne kroki

1. **Przeczytaj repozytorium źródłowe** węzła, portfela i oficjalnego minera vLLM: **[Repozytorium Pearl Research Labs](https://github.com/pearl-research-labs/pearl)**
2. **Sprawdź historię minera przed strojeniem**, bo wydajność zmienia się między wersjami: **[Wydania SRBMiner-MULTI](https://github.com/doktor83/SRBMiner-Multi/releases)**
3. **Wybierz port puli** pasujący do zmierzonego hashrate: **[LuckyPool dla Pearl](https://pearl.luckypool.io)**
4. **Porównaj rozkład hashrate między pulami** przed wyborem: **[Statystyki pul kopania Pearl](https://miningpoolstats.stream/pearl)**
5. **Najpierw oblicz koszt prądu**, bo decyduje o rentowności: **[Zbuduj wydajne pudełko do dochodu pasywnego](/other/creating-profitable-low-powered-crypto-miners/)**
6. **Zastosuj zasady strojenia wielu GPU** z naszego poradnika o kopaniu z użyteczną pracą: **[Wydajne kopanie Spacemesh na wielu GPU](/other/efficient-spacemesh-mining-multiple-gpus-guide/)**

## Powiązane artykuły

| Artykuł | Temat |
|---|---|
| **[Wydajne kopanie Spacemesh na wielu GPU](/other/efficient-spacemesh-mining-multiple-gpus-guide/)** | Strojenie wielu GPU i zarządzanie energią w innym łańcuchu opartym na użytecznej pracy |
| **[Zbuduj wydajne pudełko do dochodu pasywnego](/other/creating-profitable-low-powered-crypto-miners/)** | Dobór sprzętu do kopania według kosztu prądu przed zakupem |
| **[Lokalne AI w 2026 roku: model 27B pokonuje Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Zastosowanie tych samych GPU do lokalnego wnioskowania zamiast kopania |
| **[Kopanie Verus na Androidzie: prosty poradnik kopania na telefonie](/other/mine-verus-on-android-guide/)** | Kopanie na CPU z użyciem posiadanego sprzętu |

## Źródła

1. [Pearl Research Labs - monorepo sieci](https://github.com/pearl-research-labs/pearl)
2. [Otwarte problemy w repozytorium Pearl](https://github.com/pearl-research-labs/pearl/issues)
3. [Pearl (PRL): jak matematyka macierzy zamienia się w obliczenia AI i kopanie - Hashrate Index](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
4. [Aktywacja soft forka z karą za rangę w sieci Pearl (PRL) - Cryptoage](https://cryptoage.com/en/5400-rank-penalty-softfork-activated-on-the-pearl-prl-network.html)
5. [Pearl osiąga nowy rekordowo niski poziom: 95% obrotu na giełdzie bez głębokości arkusza - CryptoNewsLive](https://www.cryptonewslive.org/article/pearl-hit-a-fresh-all-time-low-today-95-of-its-volume-sits-on-one-exchange-with-zero-order-book-depth)
6. [Wydania SRBMiner-MULTI - doktor83](https://github.com/doktor83/SRBMiner-Multi/releases)
7. [LuckyPool - pula kopania łączonego Pearl i Nock](https://pearl.luckypool.io)
8. [Statystyki pul kopania - Pearl (PRL) PearlHash](https://miningpoolstats.stream/pearl)
9. [Eksplorator bloków PRL - prlscan.com](https://prlscan.com)

**Uwaga o oficjalnej domenie:** w chwili pisania `pearlresearch.ai` oraz subdomeny `compute` i `explorer` zwracają pustą trasę. Artykuł celowo je pomija, zamiast publikować martwe linki, i wskazuje `prlscan.com` do przeglądania bloków.

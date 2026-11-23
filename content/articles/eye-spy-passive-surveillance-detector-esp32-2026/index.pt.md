---
title: "Eye Spy: detector passivo de vigilância e rastreadores para ESP32"
date: 2026-06-07
lastmod: 2026-11-22
toc: true
draft: false
description: "Referência técnica do Eye Spy v1.1, um detector passivo de BLE e WiFi para ESP32 que identifica câmeras, rastreadores, drones e sinais relacionados."
genre: ["Ferramentas de privacidade", "Contravigilância", "Segurança de IoT", "Sistemas embarcados", "Pesquisa em segurança", "Segurança WiFi", "Segurança Bluetooth", "Projetos ESP32", "Segurança de hardware", "Segurança de código aberto"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "Detecção de vigilância", "Contravigilância", "Detecção BLE", "Varredura WiFi", "Detecção AirTag", "Detecção ALPR", "Flock Safety", "Detecção de câmeras corporais", "Detecção de drones", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "Código aberto", "Privacidade", "BLE passivo", "Modo monitor", "Detecção OUI", "Detecção de rastreadores", "Câmera corporal Axon", "Ray-Ban Meta", "Samsung SmartTag", "Rastreador Tile", "Câmera oculta", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
cover: "/img/cover/eye-spy-passive-surveillance-detector-esp32-2026.webp"
coverAlt: "Ilustração de um pequeno M5Stack Atom Lite cercado por ondas coloridas de sinal sobre um fundo azul-marinho escuro, representando a detecção de vigilância por Bluetooth e WiFi."
coverCaption: ""
---

**Um sensor passivo do tamanho de um polegar que avisa quando algo está observando você**

## Introdução: o cenário de vigilância que você não vê

O mundo físico está cada vez mais equipado com dispositivos que observam, gravam e rastreiam: leitores de placas em cruzamentos, câmeras corporais de agentes da lei, câmeras em imóveis para aluguel, rastreadores comerciais semelhantes a AirTags escondidos em bolsas ou carros e câmeras de vigilância nas entradas de lojas. A maioria desses dispositivos se comunica sem fio por **Bluetooth LE** ou **WiFi**. *Grande parte dessas comunicações é transmitida pelo ar e pode ser detectada por qualquer pessoa com o receptor certo.*

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy) é uma ferramenta passiva de detecção de vigilância que aproveita exatamente esse fato. O Eye Spy funciona no **M5Stack Atom Lite**, uma placa de desenvolvimento ESP32-PICO-D4 aproximadamente do tamanho de um cubo de açúcar, e monitora continuamente as bandas BLE e WiFi em busca das assinaturas eletrônicas de dispositivos de gravação, câmeras de vigilância, sistemas **ALPR** (leitores automáticos de placas), drones e rastreadores pessoais. Quando encontra um sinal, a cor do LED RGB muda.

*Ele não se conecta a nada e não transmite.* Ele observa, atribui pontuações e acende.

Este artigo é uma referência técnica completa. Ele explica o que o Eye Spy detecta, como funciona o modelo de pontuação de confiança, a engenharia dos mecanismos de detecção, como construir e gravar o dispositivo e quais são suas limitações práticas.

**Prefere não construir um?** A STS Collective oferece **[detectores Eye Spy](https://stscollective.com/collections/eye-spy-passive-surveillance-detectors)** pré-gravados e prontos para uso. O código para leitores **SIMEONONSECURITY** oferece até 20% de desconto.

{{< stscollective-ad "eyespy" >}}

---

## Indicadores LED: toda a interface do usuário

Assim como o [ESP32 WiFi Canary: detecção passiva de ameaças em 2,4 GHz](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/), toda a saída do Eye Spy é um único NeoPixel RGB SK6812 conectado ao GPIO 27 do M5Stack Atom Lite. O LED comunica continuamente um dos quatro níveis de ameaça:

| Cor | Significado | Faixa de pontuação |
|-------|-------------|---------------------|
| 🔵 Pulso azul | Inicialização / primeira varredura | -- |
| 🟢 Verde fixo | Nenhum dispositivo detectado | 0–2 |
| 🟡 Amarelo fixo | Atenção: pode haver um dispositivo de gravação nas proximidades | 3–5 |
| 🔴 Vermelho piscando | Alerta: dispositivo de vigilância ou rastreamento detectado | 6+ |

**Uma única detecção de alta confiança (câmera corporal Axon, câmera Flock Safety, correspondência de OUI de ALPR ou AirTag) soma pontos suficientes para deixar o LED vermelho imediatamente em um ciclo de detecção.** Várias detecções de confiança média se acumulam até chegar ao amarelo e podem se combinar para atingir o vermelho.

---

## Hardware

### Alvo principal: M5Stack Atom Lite

| Componente | Detalhe |
|-----------|--------|
| Placa | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| LED | NeoPixel SK6812 no GPIO 27 |
| Botão | GPIO 39 (somente entrada) |
| Flash | 4 MB |

O Atom Lite é uma plataforma completa e independente. **Não precisa de solda, protoboard ou componentes externos.** Basta conectá-lo ao USB.

### ESP32 DevKit genérico

Um segundo ambiente de compilação do PlatformIO (`esp32dev`) funciona com qualquer ESP32 DevKit padrão que tenha um LED integrado no GPIO 2. Toda a lógica de detecção funciona da mesma forma. Essa compilação é útil para desenvolvimento, testes ou implantação quando o formato do Atom Lite não é necessário.

---

## O sistema de pontuação

O Eye Spy usa um **modelo de pontuação de confiança** que reúne os sinais de todos os mecanismos de detecção em um único número inteiro. A pontuação determina o estado do LED (verde, amarelo ou vermelho) e é controlada por dois mecanismos automáticos:

### Redução da pontuação

Sem novas detecções, a pontuação cai **1 ponto a cada 60 segundos**. Se você se afastar do dispositivo detectado, o LED volta ao verde em alguns minutos sem nenhuma intervenção.

### Intervalo antes de pontuar novamente

Cada *tipo* de detecção tem um **intervalo de 120 segundos** antes de poder somar pontos outra vez da mesma fonte. *Isso impede que um único dispositivo persistente acumule pontos indefinidamente.* Uma câmera Flock Safety que permanece no alcance soma +5 uma vez e aguarda 120 segundos antes de contribuir de novo.

Em conjunto, esses mecanismos significam que:

- **Detecções passageiras** (como um carro com AirTag que passa) são resolvidas automaticamente.
- **Vigilância persistente** (como uma operação fixa com câmeras corporais) mantém o LED em alerta enquanto você permanece no alcance.
- **Um único dispositivo não gera pontuação descontrolada** por ser detectado repetidamente.

---

## Mecanismos de detecção

{{< figure src="eye-spy-ble-wifi-detection-engines-overview.webp" alt="Diagrama dos mecanismos paralelos de BLE e WiFi do Eye Spy, que procuram AirTags, câmeras corporais, sistemas ALPR e drones e enviam os resultados ao modelo de ameaça com pontuação de confiança" >}}

O Eye Spy alterna continuamente entre três fases de varredura:

**BLE passivo (9 s) → varredura WiFi (~3 s) → captura promíscua (5 s) → repetir**

O Eye Spy interrompe explicitamente o BLE antes das operações de WiFi para respeitar o rádio compartilhado do ESP32. O BLE reinicia no começo de cada ciclo.

---

### Mecanismo 1: BLE, varredura passiva

A varredura BLE usa **NimBLE sem transmitir solicitações de varredura**. O dispositivo recebe pacotes de anúncio BLE sem enviar respostas. *Assim, o Eye Spy fica eletronicamente invisível para os equipamentos que procura: o alvo não detecta um scanner passivo.*

Dispositivos com sinal abaixo de **−90 dBm** são ignorados para reduzir falsos positivos em ambientes densos.

#### Tabela de detecção BLE

| # | Alvo | Método de detecção | Pontos |
|---|--------|-----------------|-------|
| 1 | **Câmera corporal Axon** | OUI da MAC BLE `00:25:df` (câmeras corporais, dispositivos Taser e equipamentos de agentes da lei da Axon) | +5 🔴 |
| 2 | **Óculos inteligentes Ray-Ban Meta** | UUID do serviço BLE `0xFD5F` | +5 🔴 |
| 3 | **BLE Flock Safety** | Nome do dispositivo BLE contém `Flock`, `Penguin`, `Pigvision` ou `FS Ext Battery` | +5 🔴 |
| 4 | **Clonador de cartão (HC-03/05/06)** | Nome BLE exato: módulos Bluetooth comuns em sobreposições de terminais de pagamento | +5 🔴 |
| 5 | **Apple AirTag** | Dados do fabricante `0x004C`, subtipo `0x12`/`0x1E`, ou payload bruto `1E FF 4C 00` / `4C 00 12` | +4 🔴 |
| 6 | **Drone (OpenDroneID BLE)** | UUID do serviço BLE `0xFFFA` ou payload de dados de serviço AD com código de aplicativo `0x0D` | +4 🔴 |
| 7 | **Samsung SmartTag** | UUID do serviço BLE `0xFD5A` | +3 🟡 |
| 8 | **Rastreador Tile** | UUID do serviço BLE `0xFEED` ou `0xFEEC` | +3 🟡 |
| 9 | **Nó MeshCore** | Prefixo do nome do dispositivo BLE `MeshCore-` | +2 🟡 |
| 10 | **iBeacon (rastreamento em lojas e locais)** | Dados do fabricante `0x004C 0x02 0x15`, usados em lojas, aeroportos e estádios para rastrear movimentos | +2 🟡 |
| 11 | **Dispositivo persistente desconhecido** | MAC BLE não classificada, detectada pelo menos 3 vezes em 5 minutos ou mais (detecção de reconhecimento ou perseguidor) | +2 🟡 |

#### Detalhes de detecções BLE importantes

**Câmera corporal Axon (+5)**: Axon (anteriormente TASER International) fabrica alguns dos sistemas de câmera corporal mais usados por agentes da lei nos Estados Unidos. O OUI `00:25:df` está registrado para a Axon e aparece em seus dispositivos vestíveis. **Uma detecção basta para alcançar o limite de alerta.**

**Óculos inteligentes Ray-Ban Meta (+5)**: A parceria Ray-Ban Meta produz óculos inteligentes para consumidores capazes de gravar vídeos e fotos. O UUID do serviço BLE `0xFD5F` é o anúncio característico desses dispositivos. *Como são produtos de consumo, podem aparecer em locais públicos movimentados.* Vale prestar atenção a qualquer detecção nesse nível, independentemente da intenção de quem os usa.

**Módulos Bluetooth de clonadores de cartão (+5)**: HC-03, HC-05 e HC-06 são módulos Bluetooth seriais baratos, encontrados com frequência em sobreposições de terminais de pagamento e em equipamentos de clonagem de caixas eletrônicos. A detecção compara o nome exato do dispositivo com os nomes padrão conhecidos do firmware desses módulos. **Um alerta vermelho justifica inspecionar fisicamente os terminais de pagamento próximos.**

**Apple AirTag (+4)**: Os AirTags anunciam sua presença usando o protocolo proprietário da Apple **Nearby Interaction**. A detecção procura o cabeçalho de dados específico do fabricante (`0x004C` = Apple) e os subtipos específicos do AirTag (`0x12` para o anúncio padrão e `0x1E` para o anúncio de item perdido). Os padrões do payload bruto oferecem uma forma redundante de detecção.

**OpenDroneID BLE (+4)**: O padrão **ASTM F3411 Remote ID**, também adotado pela FAA para drones comerciais nos EUA, define um protocolo de transmissão para que os drones anunciem identidade e posição. O Eye Spy procura o UUID de serviço GATT `0xFFFA` (o serviço Remote ID designado) e o código de aplicativo `0x0D` no payload de dados de serviço AD. *Um drone comercial próximo que cumpra o padrão ativará essa detecção.*

**Dispositivo persistente desconhecido (+2)**: Esse é o mecanismo de **detecção de perseguidor**. Ele rastreia qualquer MAC BLE não classificada pelas detecções específicas acima. A pontuação aumenta se a mesma MAC não classificada aparecer pelo menos três vezes durante cinco minutos ou mais. O rastreador de persistência monitora até 50 MACs desconhecidas simultaneamente e remove registros após 30 minutos sem sinal. **Isso identifica rastreadores personalizados ou modificados que não correspondem a UUIDs de serviço ou padrões de fabricantes conhecidos.**

**iBeacon (+2)**: Lojas, aeroportos e estádios usam o formato iBeacon da Apple (`0x4C 0x00 0x02 0x15`) para acompanhar o movimento dos dispositivos em espaços físicos. A detecção é ativada pelo formato padrão do anúncio, independentemente do UUID: o alvo é o tipo de implantação, não um UUID específico. *Uma detecção indica que provavelmente você está em um local que rastreia ativamente a presença de dispositivos Bluetooth.*

---

### Mecanismo 2: varredura WiFi, busca ativa por canais

O mecanismo de varredura WiFi usa a interface padrão do ESP32 para buscar pontos de acesso, enumerar os mais próximos e comparar seus BSSIDs e SSIDs com as impressões digitais de dispositivos de vigilância conhecidos.

#### Tabela de detecção WiFi

| # | Alvo | Método de detecção | Pontos |
|---|--------|-----------------|-------|
| 12 | **Câmera Flock Safety (OUI)** | BSSID corresponde à tabela de 22 OUIs da Flock Safety (`d4:bb:e6`, `3c:61:05` e prefixos FS-Ext-Battery) | +5 🔴 |
| 13 | **Câmera ALPR / LPR (OUI)** | BSSID corresponde ao OUI `00:0e:58` da Motorola Solutions / Vigilant Solutions | +5 🔴 |
| 14 | **SSID com palavras-chave Flock** | SSID contém `flock`, `flocksafety`, `fs ext`, `penguin` ou `pigvision` | +5 🔴 |
| 15 | **SSID com palavras-chave ALPR** | SSID contém `alpr`, `lpr`, `vigilant`, `plateread`, `licenseplat`, `motorola` ou `automate` | +4 🔴 |
| 16 | **Fabricante de câmeras de vigilância (OUI)** | BSSID corresponde a uma tabela de 31 OUIs de câmeras: Hikvision, Dahua, Axis, Ring, Nest, Arlo, Wyze, Reolink, FLIR, Amcrest, Vivotek, Hanwha, Mobotix ou Ubiquiti UniFi | +3 🟡 |
| 17 | **SSID com palavras-chave de câmera** | SSID contém, entre outras, `cam`, `ipcam`, `cctv`, `nvr`, `dvr`, `doorbell`, `surv`, `blink`, `lorex`, `protect` ou `genetec` | +2 🟡 |

#### Tabela de OUI da Flock Safety

A tabela `FLOCK_OUIS`, com 22 entradas, é a consulta mais detalhada do projeto. Ela inclui:

- `d4:bb:e6`: OUI da Flock Safety registrado no IEEE.
- `3c:61:05`: OUI da Flock Safety registrado no IEEE.
- Outros 20 prefixos MAC observados em campo em baterias Flock FS-Ext-Battery e câmeras WiFi da Flock.

Essas 22 entradas representam faixas de MACs de hardware observadas em sistemas de câmeras ALPR da Flock Safety implantados. **A detecção por OUI independe do SSID**: uma câmera Flock com SSID sem palavras-chave ainda recebe +5 se o OUI do BSSID corresponder.

Os OUIs da Flock Safety e da Vigilant Solutions ficam em tabelas separadas para que ambos possam pontuar de forma independente no mesmo ciclo de varredura. *Um local com os dois tipos de fornecedor pode acumular +10 em uma única varredura WiFi.*

#### Tabela de OUI de fabricantes de câmeras de vigilância

A tabela de 31 câmeras cobre os principais fabricantes de câmeras IP que podem aparecer em implantações comerciais, residenciais e de varejo:

- **Empresas e comércio**: Hikvision, Dahua, Axis, Vivotek, Hanwha (Samsung Techwin), Mobotix e Genetec.
- **Uso doméstico e pequenos escritórios**: Ring, Nest, Arlo, Wyze, Reolink, Blink, Lorex e Amcrest.
- **Infraestrutura**: Ubiquiti UniFi (pontos de acesso e câmeras compartilham faixas de OUI) e FLIR.

Uma correspondência soma +3 pontos, no nível de atenção, mesmo sem confirmação de palavra-chave. Se também houver correspondência com um SSID de palavra-chave, a mesma rede de câmeras soma +3 pelo OUI e mais +2 pelo SSID, alcançando o nível de alerta em um ciclo de varredura.

---

### Mecanismo 3: WiFi promíscuo, captura passiva de quadros

O mecanismo promíscuo coloca o rádio ESP32 em **modo monitor** e captura quadros de gerenciamento 802.11 brutos. Isso permite detectar dispositivos que não anunciam um SSID, especificamente drones que usam o protocolo **Remote ID** por meio do **WiFi Neighbor Awareness Networking (NaN)**.

Durante essa fase, o rádio **alterna entre os canais** `{1, 6, 11, 3, 8, 13}` a cada 400 ms para ampliar a cobertura dos canais de transmissão de quadros NaN de drones.

#### Tabela de detecção promíscua

| # | Alvo | Método de detecção | Pontos |
|---|--------|-----------------|-------|
| 18 | **Drone (OpenDroneID WiFi NaN)** | Quadro de gerenciamento 802.11 destinado a `51:6f:9a:01:00:00`: transmissão Remote ID ASTM F3411 | +4 🔴 |

**OpenDroneID WiFi NaN (+4)**: O padrão ASTM F3411 define o endereço multicast `51:6f:9a:01:00:00` para todos os quadros Remote ID WiFi NaN. Drones comerciais regulamentados que transmitem posição e identidade por WiFi enviam quadros para esse endereço. O Eye Spy simplesmente observa quadros de gerenciamento destinados a esse MAC multicast: a detecção é passiva e confiável. *O operador teria de desativar completamente o Remote ID para evitá-la, o que violaria as normas aplicáveis.*

Essa detecção complementa o mecanismo OpenDroneID por BLE (detecção n.º 6). *Um drone pode anunciar-se por BLE, WiFi ou ambos, conforme o hardware e a configuração.* O Eye Spy cobre as duas opções.

---

## Programação das fases e gerenciamento do rádio

```
BLE passivo (9 s) → varredura WiFi (~3 s) → captura promíscua (5 s) → repetir
```

O ESP32-PICO-D4 tem **um único rádio compartilhado de 2,4 GHz** que atende BLE e WiFi. O Eye Spy o gerencia com cuidado:

1. **Fase BLE** (9 segundos): pilha NimBLE ativa, varredura passiva em execução e nenhuma solicitação de varredura transmitida.
2. **Encerramento do BLE**: a pilha BLE é interrompida explicitamente antes de acessar o WiFi.
3. **Varredura WiFi** (~3 segundos): busca ativa por pontos de acesso em todos os canais e correspondência de OUI e SSID.
4. **Captura promíscua** (5 segundos): captura passiva de quadros 802.11 com alternância de canais.
5. **Encerramento do WiFi**: o WiFi é interrompido e o BLE reinicia para o próximo ciclo.

Esse gerenciamento explícito das fases evita conflitos de rádio e permite que os mecanismos BLE e WiFi usem o rádio de forma ordenada em cada ciclo.

---

## Saída serial

Todas as linhas começam com `[eyespy]` para facilitar a filtragem. O monitor serial funciona a **115200 baud**.

### Inicialização

```
[eyespy] Eye Spy v1.1 starting
[eyespy] init OK
```

### Ciclo normal

```
[eyespy] BLE scan start
[eyespy] WiFi scan
[eyespy] WiFi done  score=0
[eyespy] promisc ON
[eyespy] status  score=0  CLEAR  phase=PROMISC  tracked=3
```

### Eventos de detecção

```
[eyespy] Flock-cam OUI d4:bb:e6  "Flock_CAM_0032"
[eyespy] +5 (Flock-cam-OUI)  score=5
[eyespy] WiFi done  score=5
[eyespy] promisc ON
[eyespy] status  score=5  CAUTION  phase=PROMISC  tracked=12
[eyespy] Axon-cam  RSSI=-62
[eyespy] +5 (Axon-cam)  score=10
[eyespy] status  score=10  ALERT  phase=BLE  tracked=12
[eyespy] decay  score=9
```

O campo `tracked=N` mostra quantos endereços MAC BLE únicos estão no rastreador de persistência. Isso ajuda a entender a densidade do ambiente BLE.

### Campos da pontuação

Cada linha de status inclui:

- **score**: pontuação de ameaça atual.
- **state**: `CLEAR` / `CAUTION` / `ALERT`.
- **phase**: mecanismo ativo (`BLE` / `WIFI` / `PROMISC`).
- **tracked**: quantidade de MACs BLE únicos na tabela de persistência.

---

## Compilação e gravação

### Requisitos

- **PlatformIO** (CLI ou extensão para VS Code).
- **M5Stack Atom Lite** ou qualquer ESP32 DevKit.
- Cabo USB-C.

### Dependências

O PlatformIO as instala automaticamente:

```ini
lib_deps =
    adafruit/Adafruit NeoPixel @ ^1.15.1
    h2zero/NimBLE-Arduino @ ^1.4.3
```

**Adafruit NeoPixel** controla o LED RGB SK6812. **NimBLE-Arduino** fornece a pilha de varredura BLE passiva. Ela é preferida à biblioteca BLE padrão do ESP32 por oferecer suporte limpo ao modo passivo, evitar o envio de solicitações de varredura e consumir menos memória.

### Gravar no M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# Compilar e gravar para o Atom Lite
pio run -e atom-lite -t upload

# Abrir o monitor serial a 115200 baud
pio device monitor -b 115200
```

### Gravar em um ESP32 DevKit genérico

```bash
pio run -e esp32dev -t upload
```

### Estrutura do projeto

```
eye-spy/
├── src/
│   └── main.cpp          # Toda a lógica do firmware
├── platformio.ini         # Ambientes de compilação (atom-lite, esp32dev)
├── partitions_4mb.csv     # Tabela de partições para flash de 4 MB
└── README.md
```

### platformio.ini

```ini
[env:atom-lite]
platform = espressif32
board = m5stick-c
framework = arduino

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
```

*O ambiente `atom-lite` usa a definição da placa `m5stick-c`, que tem o mesmo chip ESP32-PICO-D4 e um mapeamento de pinos compatível com o NeoPixel no GPIO 27.*

---

## Observações de detecção e limitações práticas

{{< figure src="eye-spy-m5stack-atom-lite-pocket-size.webp" alt="Ilustração em estilo fotográfico do Eye Spy no M5Stack Atom Lite, aproximadamente do tamanho de um cubo de açúcar, segurado entre dois dedos para mostrar seu tamanho compacto" >}}

### O que o Eye Spy não faz

**WiFi de 5 GHz**: O ESP32 é um dispositivo **somente de 2,4 GHz**. Câmeras de vigilância, sistemas ALPR e pontos de acesso que operam exclusivamente em 5 GHz não serão visíveis aos mecanismos WiFi de varredura ou captura promíscua. *Muitas câmeras IP modernas também funcionam em 2,4 GHz, mesmo quando oferecem suporte a 5 GHz. Porém, implantações que usam apenas 5 GHz não serão detectadas.*

**BLE criptografado**: Alguns produtos avançados de vigilância criptografam ou ocultam seus anúncios BLE. O Eye Spy detecta dispositivos que transmitem assinaturas identificáveis em texto simples, como OUI, UUIDs de serviço e dados do fabricante. *Dispositivos que alternam endereços MAC, um recurso de privacidade cada vez mais comum em rastreadores de consumo, escapam da detecção baseada em MAC.* O rastreador de persistência pode identificá-los somente se a troca ocorrer em intervalos superiores a cinco minutos.

**Câmeras cabeadas**: **Câmeras IP conectadas por Ethernet e sem rádio WiFi não emitem sinais sem fio que o Eye Spy possa detectar.** Câmeras ocultas sem conexão de rede, que gravam apenas localmente, também não produzem assinatura RF.

**Limites de alcance**: Em ambientes internos, o alcance prático de recepção de sinais fortes pela antena ESP32 é de **20 a 40 metros**; sinais fracos ou bloqueados têm alcance menor. *Dispositivos no limite do alcance ou atrás de blindagem RF significativa podem não pontuar ou ficar abaixo do limite RSSI de −90 dBm.*

### Falsos positivos esperados

**Câmeras de consumo nas casas vizinhas**: Ring, Nest, Wyze, Arlo e Reolink são comuns em bairros residenciais. Seus OUIs aparecem na tabela de 31 câmeras. *Em áreas residenciais, espere algumas indicações amarelas de atenção (+3) causadas por câmeras de campainha dos vizinhos.* Não são falsos positivos no sentido técnico, pois o dispositivo *realmente* detecta uma câmera. O contexto importa.

**Instalações comerciais de iBeacon**: Grandes redes de varejo instalam infraestrutura iBeacon em praticamente todas as lojas. *Uma visita a um shopping ou supermercado provavelmente ativará a detecção de iBeacon (+2).* O dispositivo está funcionando como esperado: a infraestrutura de rastreamento comercial está presente.

**Infraestrutura Ubiquiti UniFi**: Pontos de acesso UniFi aparecem na tabela OUI de câmeras porque a Ubiquiti fabrica equipamentos de rede e câmeras de segurança com faixas OUI sobrepostas. *Uma rede que usa equipamentos UniFi pode receber +3 por correspondências OUI no mecanismo de varredura WiFi.*

**Samsung SmartTag e dispositivos de consumo**: O UUID SmartTag (`0xFD5A`) é um serviço registrado pela Samsung. *SmartTags são rastreadores de consumo com usos pessoais legítimos.* A presença de um SmartTag próximo ativará a detecção.

### O que cada nível de pontuação significa na prática

| Pontuação | Situação provável no mundo real |
|-------|-----------------------------|
| 6–10 (🔴) | Detecção confiável de alta confiança: câmera Axon a cerca de 30 m, câmera Flock Safety com OUI correspondente, padrão confirmado de AirTag seguindo alguém ou drone transmitindo Remote ID |
| 3–5 (🟡) | Vários rastreadores de consumo, câmeras vizinhas acumulando pontos, possível câmera Flock ou uma detecção OpenDroneID isolada |
| 0–2 (🟢) | Nenhuma assinatura importante de vigilância; há comunicações normais de dispositivos de consumo, mas a pontuação fica abaixo do limite |

---

## Comparação com projetos relacionados

O Eye Spy detecta vigilância física no ambiente; o [ESP32 WiFi Canary: detecção passiva de ameaças em 2,4 GHz](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/) detecta ataques WiFi de rede contra seus próprios dispositivos. *São ferramentas complementares para modelos de ameaça diferentes.*

| Capacidade | Eye Spy | ESP32 WiFi Canary |
|------------|---------|------------------|
| Detecção de AirTag e rastreadores | ✅ | ❌ |
| Detecção de câmeras ALPR / Flock | ✅ | ❌ |
| Detecção de câmeras corporais | ✅ | ❌ |
| Detecção de drones (Remote ID) | ✅ | ❌ |
| Detecção de ponto de acesso evil twin | ❌ | ✅ |
| Detecção de ataque de desautenticação | ❌ | ✅ |
| Detecção de redução da segurança | ❌ | ✅ |
| Aprendizado de linha de base | ❌ | ✅ |
| BLE passivo | ✅ | ❌ |
| Mesma plataforma de hardware | ✅ | ✅ |

Os dois projetos usam o mesmo M5Stack Atom Lite, os mesmos indicadores LED e o mesmo sistema de compilação PlatformIO. Para monitorar vigilância física e de rede, grave cada projeto em uma unidade Atom Lite diferente e leve as duas.

O Eye Spy também complementa o [projeto de detecção Flock You](https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/) para quem se preocupa especificamente com infraestrutura de vigilância ALPR.

---

## Casos de uso

### Consciência da vigilância nas proximidades

O público principal do Eye Spy inclui qualquer pessoa que queira conhecer a infraestrutura de vigilância próxima. Ao caminhar por um bairro, passar de carro por um cruzamento ou participar de um evento público, o Eye Spy transforma análises RF complexas em **um único estado de LED em tempo real**.

### Detecção de perseguição com AirTag

A perseguição com AirTag é um problema documentado. O **mecanismo de detecção de seguidores** do Eye Spy (MAC BLE desconhecida e persistente detectada pelo menos 3 vezes durante 5 minutos ou mais) procura rastreadores personalizados ou modificados que não correspondem ao formato conhecido de anúncio da Apple. Com a detecção direta de AirTag, há **dois caminhos independentes para identificar um rastreador seguindo você**.

### Inspeção de imóveis para aluguel e quartos de hotel

Entrar em um quarto de hotel ou imóvel para aluguel com o Eye Spy em funcionamento oferece uma primeira indicação de dispositivos BLE e WiFi inesperados. Uma correspondência de SSID com palavras-chave de câmera ou um OUI de vigilância encontrado na varredura WiFi soma pontos de atenção. *Isso não substitui uma varredura RF adequada*, mas acrescenta uma camada ambiental passiva à inspeção física.

### Implantações ALPR e pesquisa de privacidade

Pesquisadores que documentam infraestrutura de vigilância, jornalistas que trabalham em ambientes monitorados e defensores da privacidade podem usar o Eye Spy como equipamento de detecção portátil e barato. A saída serial registra cada detecção com RSSI, tornando-o adequado para coleta simples de dados.

### Segurança em viagens

Assim como o WiFi Canary, o Eye Spy foi projetado para viagens. O Atom Lite cabe no bolso ou pode ser preso a uma bolsa. Durante viagens por aeroportos, estações de trem ou eventos públicos com vigilância intensa, ele monitora o ambiente passivamente sem exigir interação.

---

## Observações sobre a arquitetura

### Por que o BLE passivo importa

A escolha do escaneamento BLE passivo, sem pacotes de solicitação, tem consequências importantes para a segurança. Em um escaneamento BLE padrão, o scanner transmite um pacote **SCAN_REQ** pedindo dados de anúncio adicionais a cada anunciante. *Isso torna o escaneamento BLE ativo observável por ambos os dispositivos*: o dispositivo escaneado vê o endereço do scanner na solicitação.

O modo passivo do NimBLE recebe apenas anúncios não direcionados (ADV_IND, ADV_NONCONN_IND, ADV_SCAN_IND) e nunca transmite SCAN_REQ. **O Eye Spy não transmite nada por BLE durante a fase de escaneamento.** Uma câmera corporal Axon, um dispositivo Flock ou um AirTag detectado não consegue observar nem reagir à presença do scanner.

### Projeto do rastreador de persistência

O rastreador de persistência de dispositivos desconhecidos mantém uma tabela com até **50 endereços MAC BLE**, além dos horários da primeira e da última detecção. A detecção é acionada quando uma MAC aparece pelo menos três vezes ao longo de cinco minutos ou mais.

O limite de 50 entradas e a exclusão após 30 minutos são escolhas de engenharia que equilibram a sensibilidade com as limitações de RAM do ESP32. *Em ambientes BLE densos (transporte público, conferências ou shoppings), a tabela pode encher rapidamente com dispositivos de consumo.* O limite RSSI de −90 dBm filtra dispositivos distantes e mantém o foco em fontes próximas e persistentes.

### Interação entre redução de pontuação e intervalo

O **intervalo de 120 segundos entre pontuações** impede que um dispositivo que permanece sempre no alcance acumule pontos a cada ciclo BLE de nove segundos. Sem esse intervalo, uma câmera Flock somaria +5 a cada 15 segundos e chegaria a centenas de pontos em minutos.

A **redução de 1 ponto a cada 60 segundos** diminui a pontuação quando um dispositivo sai do alcance e o intervalo termina sem nova detecção. *Uma única detecção de +5 que não se repete cai a zero em cinco minutos.* Assim, o dispositivo volta naturalmente ao estado normal durante deslocamentos comuns.

---

## Contribuições e estado do projeto

O Eye Spy está disponível sob a licença Apache-2.0 em [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy).

Possíveis áreas de expansão:

- **Adicionar entradas OUI**: ampliar as tabelas de OUI da Flock Safety e das câmeras conforme novos endereços MAC de hardware forem documentados em campo.
- **Adicionar UUIDs de serviços BLE**: novos óculos inteligentes, câmeras e rastreadores trazem novos UUIDs.
- **Ajustar o rastreador de persistência**: o limite de 50 entradas, o limiar de 3 observações e a janela de 5 minutos são constantes ajustáveis.
- **Registrar dados seriais**: o formato da saída serial foi projetado para análise programática. Um registrador externo pode agregar eventos de várias unidades Eye Spy.

O firmware está em um único arquivo `main.cpp` no diretório `src/`, o que facilita leitura, auditoria e modificação.

---

## Conclusão

O Eye Spy trata de um problema específico, mas relevante: o ambiente físico ao seu redor tem cada vez mais dispositivos de vigilância, e a maioria transmite assinaturas RF detectáveis. **Um M5Stack Atom Lite de US$ 15 com o firmware Eye Spy se torna um scanner ambiental contínuo**, transformando a complexidade da análise de pacotes BLE e das buscas de OUI WiFi em um único LED RGB.

O modelo de pontuação de confiança atribui pesos realistas às ameaças: uma câmera corporal Axon perto de uma operação policial recebe +5 e acende o LED vermelho imediatamente; um iBeacon comercial recebe +2 e contribui para a consciência do ambiente sem gerar sozinho um alarme falso. A redução da pontuação e os intervalos evitam que o dispositivo reaja demais a sinais transitórios ou persistentes de baixo nível.

Para contravigilância, segurança em viagens, detecção de AirTag ou simplesmente para saber se algo próximo está observando você, o Eye Spy é uma ferramenta prática, passiva e de código aberto que merece um lugar no kit de qualquer profissional de segurança.

**GitHub**: [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compre detectores Eye Spy e economize 20%
{{< /centerbutton >}}

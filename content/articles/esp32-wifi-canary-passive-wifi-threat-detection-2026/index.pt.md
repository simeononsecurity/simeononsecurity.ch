---
title: "ESP32 WiFi Canary: deteção passiva de ameaças em 2,4 GHz"
date: 2026-06-06
lastmod: 2026-11-22
toc: true
draft: false
description: "Análise técnica do ESP32 WiFi Canary, um sensor passivo de 2,4 GHz que deteta evil twins, desautenticação, degradações de segurança e inundações de beacons."
genre: ["Segurança de redes", "Segurança WiFi", "Segurança IoT", "Pesquisa de segurança", "Sistemas embarcados", "Ferramentas de privacidade", "Projetos ESP32", "Segurança de hardware", "Segurança sem fios", "Segurança de código aberto"]
tags: ["ESP32", "WiFi Canary", "M5Stack Atom Lite", "Deteção de desautenticação", "Deteção de evil twin", "Segurança WiFi", "Monitorização passiva WiFi", "Tramas de gestão 802.11", "Segurança de redes", "Segurança IoT", "NeoPixel", "SK6812", "PlatformIO", "C++", "Código aberto", "Sensor de segurança", "Deteção de ameaças sem fios", "Monitorização de BSSID", "Monitorização de SSID", "Deteção de degradação de segurança", "Deteção de inundação de beacons", "Monitorização WiFi", "LED RGB", "Modo promíscuo", "Segurança embarcada", "Segurança em viagem", "Segurança WiFi em hotéis", "WiFi em cafés", "Sensibilização para a segurança", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/"
cover: "/img/cover/esp32-wifi-canary-passive-wifi-threat-detection-2026.webp"
coverAlt: "Ilustração de um pequeno dispositivo semelhante ao ESP32 WiFi Canary ligado a uma porta USB. O LED RGB brilha em várias cores para representar as capacidades de deteção de ameaças."
coverCaption: ""
---

**Um sensor passivo de ameaças WiFi do tamanho de um polegar que nunca responde**

## O problema do WiFi público

Ao ligares-te ao WiFi de um hotel, café ou aeroporto, confias que o ponto de acesso é verdadeiro. O problema é que as **tramas de gestão 802.11**, que anunciam redes, gerem ligações e coordenam clientes, são *completamente não autenticadas na maioria das implementações*. Com equipamento simples, qualquer pessoa pode clonar um SSID, enviar tramas de desautenticação ou criar uma rede aberta de engodo junto a uma rede WPA2 legítima.

O [**ESP32 WiFi Canary**](https://github.com/simeononsecurity/esp32-wifi-canary) é um sensor passivo que ajuda a reconhecer este risco num formato muito pequeno. Cabe no M5Stack Atom Lite, aproximadamente do tamanho de um cubo de açúcar. Liga-se a USB, aprende o ambiente e acende um LED RGB quando deteta padrões associados a ameaças sem fios.

Não se liga a nada, não recolhe credenciais e não transmite tramas. Observa, atribui uma pontuação e comunica o estado por uma cor.

Este artigo é uma referência técnica completa do projeto: o que deteta, como funciona o modelo de confiança, como compilar e gravar o firmware e quais são as limitações práticas.

---

## O que o ESP32 WiFi Canary faz e não faz

### Sempre apenas passivo

O WiFi Canary utiliza dois modos de rádio, nunca ao mesmo tempo:

1. **Modo promíscuo**: recebe e inspeciona tramas de gestão 802.11, como desautenticação e desassociação, sem se associar a uma rede.
2. **Modo de pesquisa**: faz pesquisas WiFi ativas para enumerar pontos de acesso próximos e compará-los com uma linha de base aprendida.

O dispositivo nunca:
- se associa nem se liga a uma rede;
- recolhe tramas de dados ou credenciais;
- transmite tramas 802.11;
- guarda dados em memória flash persistente;
- comunica pela Internet.

**Tudo o que aprende fica na RAM e é apagado ao reiniciar.** É intencional: o canary é um **sensor**, não um dispositivo de captura.

### O LED é a interface

Não existe ecrã, aplicação ou interface web. Toda a saída do dispositivo é um único **NeoPixel RGB SK6812** no GPIO 27 do M5Stack Atom Lite. O LED apresenta quatro estados:

| Estado do LED | Significado |
|---|---|
| 🔵 Azul (pulso lento) | Arranque, criação da linha de base |
| 🟢 Verde (fixo) | Normal, sem problemas de elevada confiança |
| 🟡 Amarelo (fixo) | Cuidado, padrão suspeito detetado |
| 🔴 Vermelho (pulso rápido) | Alerta, ameaça de confiança superior detetada |

O arranque demora cerca de **24 segundos** (3 pesquisas de 8 segundos). Quando o LED deixa de estar azul, a linha de base está pronta e começa a monitorização.

---

## Hardware

### Alvo principal: M5Stack Atom Lite

O projeto foi concebido para o M5Stack Atom Lite, uma plataforma de desenvolvimento ESP32 completa numa caixa de 24 × 24 mm.

| Componente | Detalhe |
|---|---|
| MCU | ESP32-PICO-D4 |
| LED | Um NeoPixel RGB SK6812 (GPIO 27) |
| Botão | GPIO 39, ativo a nível baixo |
| USB | Ponte UART CP2104 |
| Alimentação | USB-C, cerca de 80–120 mA durante a pesquisa |

**Sem breadboard, componentes externos ou soldadura.** Liga-o à alimentação USB e funciona.

### ESP32 DevKit genérico para desenvolvimento e testes

O projeto inclui um segundo ambiente PlatformIO (`esp32dev`) para placas ESP32 padrão. Nesta configuração:

- o LED integrado no GPIO 2 substitui o NeoPixel;
- toda a saída de depuração série fica ativada;
- a lógica de deteção funciona como na versão Atom Lite.

Assim, qualquer pessoa com um ESP32 DevKit de $5 pode usar o projeto e testar a lógica sem o hardware-alvo.

---

## Processo de aprendizagem da linha de base

### Porque é importante uma linha de base

Um canary que dispara para todas as redes abertas de uma cidade seria inútil. O ESP32 WiFi Canary aprende primeiro o ambiente e só depois avalia ameaças. A primeira fase cria uma **tabela de referência** dos pontos de acesso que existem legitimamente na área.

### Três pesquisas, 24 segundos

Ao arrancar, o dispositivo faz três pesquisas WiFi sequenciais, com uma pausa entre elas. Quando terminam, guarda como linha de base os pontos de acesso aprendidos: SSID, BSSID, tipo de encriptação e intensidade do sinal.

A saída série nesta fase é semelhante a:

```
==============================================
 Travel WiFi Canary v1.0
 Passive 2.4 GHz awareness sensor
==============================================
[canary] setup done - starting baseline learning
[canary] baseline scan start (aps=0 score=0)
[canary] scan found 18 APs
[canary] baseline scan 1/3
[canary] baseline scan start (aps=18 score=0)
[canary] scan found 18 APs
[canary] baseline scan 2/3
[canary] baseline scan start (aps=18 score=0)
[canary] scan found 19 APs
[canary] baseline complete: 19 APs learned
  [00] MyHomeWifi                    aa:bb:cc:dd:ee:ff ch06 WPA2     -52 dBm
  [01] XFINITY                       11:22:33:44:55:66 ch01 WPA2     -71 dBm
  ...
[canary] STARTUP → NORMAL  (score=0  "")
```

Quando o LED muda de azul para verde, o dispositivo está a funcionar por completo.

---

## O que deteta: categorias de ameaças

O WiFi Canary monitoriza seis padrões de ameaça. Cada um acrescenta pontos a uma **pontuação de confiança** que controla o estado do LED. *Nenhum indicador isolado é tratado como certeza*: o modelo acumula indícios corroborantes antes de escalar.

### 1. Rajadas de desautenticação e desassociação

Os **subtipos 10 (desassociação) e 12 (desautenticação) das tramas de gestão 802.11** são ferramentas comuns de ataques WiFi. Qualquer dispositivo pode enviá-las, e os clientes que as recebem são desligados do ponto de acesso.

Em **modo promíscuo**, o canary conta estas tramas por MAC de origem numa janela móvel de **5 segundos**.

| Condição | Pontos adicionados |
|---|---|
| ≥ 8 tramas de uma origem em 5 s | +2 |
| ≥ 20 tramas de uma origem em 5 s | +4 |
| ≥ 5 tramas de desautenticação em broadcast | +1 |

**Os limites importam**: um cliente que muda entre pontos de acesso gera algumas tramas legítimas. As ferramentas de ataque geram centenas de tramas por segundo contra um alvo. A janela de 5 segundos e o mínimo de 8 tramas filtram o ruído normal de roaming e detetam rajadas sustentadas de ferramentas como `aireplay-ng`.

### 2. Clone aberto de uma rede encriptada conhecida (evil twin)

**É a deteção de maior confiança.** Um ataque evil twin costuma:

1. Criar uma cópia aberta, sem palavra-passe, de um SSID WPA2 conhecido.
2. Emitir com sinal mais forte do que o ponto real para os clientes se ligarem automaticamente.

Depois de aprender a linha de base, uma nova pesquisa deteta um SSID que antes só usava WPA/WPA2/WPA3, mas agora aparece como **OPEN**:

| Condição | Pontos adicionados |
|---|---|
| Mesmo SSID, antes encriptado e agora aberto | +3 |
| BSSID não visto na linha de base | +1 |
| Sinal do clone ≥ 10 dB mais forte que o ponto conhecido | +1 |

Um clone aberto do WiFi de hotel que seja 10 dB mais forte do que o ponto real é um exemplo clássico. *Esta combinação chega a 5 pontos (Cuidado) num único ciclo de pesquisa.*

**Exemplo série**:

```
[canary] OPEN CLONE: SSID='MyHomeWifi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'MyHomeWifi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'MyHomeWifi'")
```

### 3. Ponto de acesso encriptado original em falta e clone aberto presente

Uma variante avançada: o clone mais forte faz com que os clientes o prefiram, enquanto o ponto real é simultaneamente afastado do ar por desautenticação.

| Condição | Pontos adicionados |
|---|---|
| Ponto encriptado da linha de base desapareceu e surgiu uma rede aberta correspondente | +3 |

Isto cobre situações em que o ponto real continua a transmitir, mas perde a disputa da intensidade do sinal ou é ativamente interrompido.

### 4. Degradação de segurança

O mesmo SSID de uma entrada da linha de base é observado com encriptação mais fraca do que a registada.

| Condição | Pontos adicionados |
|---|---|
| WPA3 → WPA2 | +1 |
| WPA2 → WPA | +1 |
| Queda de pelo menos 2 níveis de encriptação | +3 |

*Degradações para rede aberta são tratadas pela deteção de evil twin com pontuações mais altas.* Esta categoria cobre degradações parciais que podem passar despercebidas numa comparação simples entre aberto e encriptado.

### 5. SSID duplicado de fornecedor inesperado

Mesmo SSID e mesmo tipo de segurança de um ponto da linha de base, mas com BSSID de um **OUI de fornecedor diferente** (os primeiros 3 bytes do endereço MAC).

| Condição | Pontos adicionados |
|---|---|
| OUI diferente do ponto da linha de base com o mesmo SSID | +1 |
| Clone também ≥ 10 dB mais forte | +2 |

*A pontuação é intencionalmente baixa.* Redes empresariais, sistemas mesh e pontos de acesso de ISP têm legitimamente vários BSSID com o mesmo SSID e fornecedores diferentes. Este sinal deve acumular-se com outros indícios, não disparar sozinho.

### 6. Inundação de beacon ou SSID

Conta SSID novos, ausentes da linha de base, que aparecem numa **janela móvel de 30 segundos**.

| Condição | Pontos adicionados |
|---|---|
| ≥ 15 SSID novos em 30 s | +2 |
| ≥ 30 SSID novos em 30 s | +3 |

Os **ataques de inundação de beacons** transmitem milhares de SSID falsos para confundir as tabelas de pesquisa ou impedir beacons legítimos. Quinze SSID novos e desconhecidos em 30 segundos são invulgares na maioria dos ambientes.

---

## Modelo de pontuação de confiança

Todos os sinais detetados contribuem para uma **pontuação de ameaça** inteira que controla o estado do LED:

| Intervalo da pontuação | Estado do LED |
|---|---|
| 0–2 | Normal (verde) |
| 3–5 | Cuidado (amarelo) |
| 6+ | Alerta (vermelho, pulso rápido) |

### Decaimento da pontuação

Sem novos eventos, a pontuação **desce 1 ponto a cada 60 segundos**. Esta é uma das decisões de projeto mais importantes:

- Uma rajada de desautenticação eleva a pontuação para Cuidado; se o ataque parar, regressa automaticamente a Normal em alguns minutos.
- Um ataque sustentado mantém o estado de Alerta.
- O dispositivo reinicia o estado sem intervenção nem reinício.

Isto significa que:
- **Anomalias breves** (roaming e alterações temporárias de redes vizinhas) desaparecem por si.
- **Ataques sustentados** continuam sinalizados.
- **Não há fadiga de alertas** por eventos isolados que não se repetem.

### Reposição com o botão

O botão GPIO 39 do Atom Lite executa duas ações:

1. Envia a tabela atual completa de AP para a saída série, útil para auditar o que o dispositivo vê.
2. Repõe a pontuação de ameaça em 0 e regressa imediatamente ao verde para observar o ciclo seguinte sem histórico.

---

## Compilar e gravar

### Requisitos

- **PlatformIO** (CLI ou extensão do VS Code)
- **M5Stack Atom Lite** (ou ESP32 DevKit para testes)
- Cabo USB-C

### Gravar no M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/esp32-wifi-canary.git
cd esp32-wifi-canary

# Compilar e gravar
pio run -e atom-lite --target upload

# Abrir o monitor série a 115200 baud
pio device monitor -b 115200
```

### Gravar num ESP32 DevKit genérico

```bash
pio run -e esp32dev --target upload
```

A compilação DevKit usa GPIO 2 (LED integrado) e apresenta o log série completo. Não aciona o NeoPixel. A lógica de deteção é igual à do Atom Lite.

### Estrutura do projeto

```
esp32-wifi-canary/
├── main.cpp              # Toda a lógica do firmware
├── platformio.ini        # Ambientes de compilação (atom-lite, esp32dev)
├── partitions_4mb.csv    # Tabela de partições flash de 4 MB
└── README.md
```

Todo o firmware está num **único ficheiro-fonte C++**. A lógica de deteção não usa bibliotecas externas, apenas o framework ESP32 Arduino para pesquisas WiFi, callbacks de modo promíscuo e controlo do NeoPixel.

### Ambientes platformio.ini

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

O ambiente `atom-lite` usa a definição de placa `m5stick-c` (mesmo chip ESP32-PICO-D4 e mapeamento de pinos compatível com o NeoPixel no GPIO 27).

---

## Referência da saída série

O dispositivo produz logs detalhados a **115200 baud**. Todas as linhas começam por `[canary]` para facilitar a filtragem.

### Sequência de arranque

```
==============================================
 Travel WiFi Canary v1.0
 Passive 2.4 GHz awareness sensor
==============================================
[canary] setup done - starting baseline learning
[canary] baseline scan start (aps=0 score=0)
[canary] scan found 18 APs
[canary] baseline scan 1/3
...
[canary] baseline complete: 19 APs learned
  [00] MyHomeWifi                    aa:bb:cc:dd:ee:ff ch06 WPA2     -52 dBm
  [01] XFINITY                       11:22:33:44:55:66 ch01 WPA2     -71 dBm
[canary] STARTUP → NORMAL  (score=0  "")
```

### Eventos de deteção

```
[canary] normal scan start (aps=19 score=0)
[canary] scan found 21 APs
[canary] OPEN CLONE: SSID='HotelWiFi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'HotelWiFi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'HotelWiFi'")
```

### Transições de pontuação

```
[canary] CAUTION → NORMAL  (score=2  "score decay")
[canary] NORMAL → ALERT    (score=6  "sustained deauth burst + open clone")
```

O log série mostra o que o dispositivo viu, quando viu e por que razão a pontuação mudou. Também funciona como **registo de auditoria passivo** sem ser preciso observar o LED.

---

## Notas de deteção e limitações práticas

O README explica com franqueza o que o dispositivo não consegue fazer. Convém detalhar essas limitações.

### Possíveis falsos positivos

**Redes empresariais e mesh** são a maior fonte de falsos positivos. Uma rede empresarial grande, um hotel ou um sistema mesh como Eero ou Google WiFi pode apresentar legitimamente:

- Vários BSSID para o mesmo SSID com OUI de fornecedores diferentes.
- Configurações de segurança distintas entre bandas.
- Pontos de acesso que aparecem e desaparecem quando a rede mesh se ajusta.

**Routers Airbnb e SOHO** com vários SSID para bandas diferentes também podem causar diferenças de OUI se os rádios de 2,4 e 5 GHz usarem blocos MAC consecutivos de fornecedores diferentes.

*Alterações temporárias em redes vizinhas*: uma rede encriptada que desaparece momentaneamente da pesquisa e regressa com outros parâmetros (atualização de firmware, reinício ou reconfiguração) pode ativar uma deteção passageira.

A pontuação e o decaimento foram concebidos para *reduzir, não eliminar*, falsos positivos.

### Possíveis falsos negativos

Um **ataque evil twin bem concebido** que:

- Suplante o BSSID exato do ponto legítimo para que o OUI corresponda.
- Use o mesmo tipo de segurança, com configuração IE WPA2 correta.
- Tenha sinal a menos de 10 dB do ponto real.

*Pode não acumular pontos suficientes para atingir Cuidado.* A desautenticação necessária para afastar clientes do ponto real acrescentaria pontos, mas um atacante sofisticado que limite as tramas poderá ficar abaixo do limiar.

### Intervalo durante a mudança de rádio

**O rádio ESP32 não pode estar em modo promíscuo e pesquisar ativamente pontos de acesso ao mesmo tempo.** O firmware alterna entre modos. Assim, **as tramas de desautenticação que chegam durante a janela de pesquisa de cerca de 3 segundos não são capturadas**. Um atacante poderia sincronizar as rajadas com essas janelas, mas precisaria de conhecer o calendário de pesquisa.

### Apenas 2,4 GHz

O rádio ESP32 funciona a 2,4 GHz. **As redes de 5 e 6 GHz não são pesquisadas nem monitorizadas.** O dispositivo não deteta evil twins que funcionem apenas a 5 GHz.

### Alcance passivo

A deteção exige que o dispositivo receba as tramas de desautenticação. Um atacante distante, com antena muito direcional, ou a visar um cliente longe do canary, pode emitir sinais demasiado fracos para ativar os contadores.

---

## Casos de uso

### Viajar com trabalho sensível

O canary foi pensado sobretudo para viagens. Liga-o à porta USB de um portátil, a uma tomada USB do hotel ou a uma bateria portátil e deixa-o aprender o ambiente do hotel ou centro de conferências. O aparecimento posterior de um clone aberto do SSID do hotel, o cenário de ataque mais comum, ativa pelo menos Cuidado.

### Cafés e WiFi público

Ambientes WiFi abertos são alvos frequentes para evil twins. A linha de base aprende o ponto legítimo do café à chegada e depois vigia SSID concorrentes.

### Sensibilização e formação de segurança

A saída série fornece um registo detalhado e legível do que o dispositivo observa. Em formação, mostrar uma rajada de desautenticação em tempo real e ver o LED mudar de cor é muito mais eficaz do que uma apresentação.

### Monitorização passiva de laboratório

Num laboratório doméstico ou pequeno escritório, o canary pode servir como monitor ambiental permanente. O LED mostra o estado rapidamente e o botão permite consultar a tabela de redes atual.

---

## Notas de arquitetura

### Porque usar uma pontuação única em vez de alertas separados

O modelo agrega sinais distintos num único número, em vez de apresentar categorias de alerta separadas. É uma escolha deliberada de interface: o dispositivo tem um LED com três estados. Alertas separados exigiriam um ecrã ou uma aplicação. *A pontuação transforma sinais ruidosos e parcialmente correlacionados num único indicador útil.*

### Porque a pontuação decai

Sem decaimento, um falso positivo isolado exigiria uma reposição manual. Com a descida a cada 60 segundos, anomalias breves desaparecem em minutos. **Assim, o canary funciona sem supervisão**, numa mala, quarto de hotel ou automóvel, e regressa ao normal após eventos temporários.

### Porque fazer três pesquisas da linha de base

Uma só pesquisa pode não detetar um ponto de acesso que não estivesse a transmitir naquele momento, devido a uma pausa ou falha temporária de energia. *Três pesquisas em cerca de 24 segundos oferecem uma visão mais completa do ambiente estável antes de começar a monitorização.*

---

## Contribuições e estado do projeto

O projeto está em [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary), sob uma licença para uso passivo. O código consiste num único `main.cpp`, fácil de ler, auditar e ampliar.

Quem usa PlatformIO e ESP32 pode compilar o projeto sem alterações tanto para Atom Lite como para um DevKit padrão.

---

## Comparação com outras abordagens de monitorização WiFi

| Abordagem | Passiva? | Sem credenciais | Saída num LED | Formato de viagem |
|---|---|---|---|---|
| ESP32 WiFi Canary | ✅ | ✅ | ✅ | ✅ |
| Kismet (portátil) | ✅ | ✅ | ❌ (requer ecrã) | ❌ (pesado) |
| WiFi Pineapple | ❌ (ativa) | ❌ | ❌ | Parcial |
| IDS sem fios (empresa) | ✅ | ✅ | ❌ (requer infraestrutura) | ❌ |
| Pesquisa manual (app do telemóvel) | Parcial | ✅ | ❌ | ✅ |

O canary ocupa um nicho específico: **monitorização ambiental contínua, sem interação nem rede**, num formato que cabe num porta-chaves ou mala de portátil.

---

## Conclusão

O ESP32 WiFi Canary faz uma coisa: observa o ambiente de 2,4 GHz e muda de cor quando algo parece suspeito. Não é um sistema completo de deteção de intrusões sem fios, uma ferramenta de captura de pacotes nem um analisador forense. É um canary, um sensor passivo que repara quando o ambiente se torna perigoso.

O **modelo de pontuação de confiança**, o **decaimento da pontuação** e a **linha de base em três fases** lidam com o problema dos falsos positivos dos sensores ambientais. O dispositivo pode funcionar sem supervisão num hotel ou centro de conferências e sinalizar anomalias importantes sem reagir à atividade normal da rede.

Para quem prepara um kit de segurança portátil, trabalha em ambientes com infraestrutura WiFi não fiável ou procura um projeto ESP32 útil, o WiFi Canary vale uma tarde e um M5Stack Atom Lite de $15.

**GitHub**: [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary)

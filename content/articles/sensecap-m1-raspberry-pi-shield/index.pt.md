---
title: "SenseCAP M1 Raspberry Pi Shield: pinagem e reutilização para LoRaWAN"
date: 2026-09-12
lastmod: 2026-11-07
toc: true
draft: false
description: "Entenda o shield SenseCAP M1, compare mapas GPIO conflitantes, inspecione o ATECC608 e planeje um gateway LoRaWAN com uma versão atual do Raspberry Pi OS."
genre: ["Raspberry Pi", "IoT", "Segurança de hardware"]
tags: ["SenseCAP M1", "Shield SenseCAP M1", "Pinagem SenseCAP M1", "Shield Raspberry Pi", "Raspberry Pi HAT", "Gateway LoRaWAN", "WM1302", "WM1303", "SX1302", "SX1303", "Seeed Studio", "Reutilização de hotspot Helium", "Concentrador LoRa", "SPI GPIO", "GPIO17", "LED GPIO22", "libgpiod", "Raspberry Pi OS", "ATECC608", "CryptoAuthLib", "Diagnóstico I2C", "STTS751", "LoRa Basics Station", "ChirpStack", "The Things Stack", "Engenharia reversa de hardware"]
cover: "/img/cover/sensecap-wm1302-shield-hardware.webp"
coverAlt: "Shield SenseCAP M1 com módulo Seeed WM1302, conector Raspberry Pi, cabo de antena, porta USB-C e conector de ventilador"
coverCaption: "Foto da placa: Clockwork Bird, 2023. Fonte e atribuição no fim do artigo."
coverCredit: "Clockwork Bird"
coverCreditURL: "https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/"
---

**O shield SenseCAP M1 é útil como hardware de gateway LoRaWAN, mas sua fiação exige mais análise do que um tutorial genérico de HAT Raspberry Pi oferece.** Este guia amplia [a investigação de Clockwork Bird de 2023](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/) com documentação do fabricante, análise de um driver upstream e orientações atuais de GPIO. Você identificará o hardware, separará fatos confirmados de evidências incompletas de pinagem e criará um registro de inicialização reproduzível.

> **Escopo:** Este é um guia de hardware baseado em documentação. Os comandos e mapas da placa não foram testados em um M1 físico para este artigo.

## Principais pontos

- **Identifique as duas placas:** O carrier M1 e o concentrador removível têm modelos e revisões próprios.
- **Audite os scripts de reset:** Os padrões CoreCell entram em conflito com sinais do pinout M1 publicado.
- **Confira as interfaces do sistema:** Arquivos de dispositivo SPI, numeração GPIO e versões de ferramentas GPIO respondem a perguntas diferentes.
- **Preserve o provisionamento do elemento seguro:** Ler informações do dispositivo não equivale a configurá-lo ou gerar chaves.
- **Comprove o caminho completo:** Detectar um concentrador não comprova a entrega dos dados do sensor.

## Antes de começar

**Dificuldade: intermediária.** Reserve cerca de uma a duas horas para inventário, preparação do sistema e verificações documentais. A verificação elétrica, a adaptação do driver e a implantação do servidor de rede exigem trabalho separado, principalmente se a revisão da placa for desconhecida.

| Item | Objetivo |
|---|---|
| **Shield M1 e concentrador** | Ler a revisão do carrier e o rótulo completo do módulo |
| **Raspberry Pi 4** | Começar com o host usado no projeto M1 original |
| **Cartão microSD reserva** | Preparar outro sistema sem perder a instalação original |
| **Fonte e antena adequadas** | Compatibilizar o conjunto e a banda RF do módulo |
| **SSH ou console local** | Registrar diagnósticos e editar a configuração |
| **Sensor e servidor LoRaWAN** | Verificar a entrega real ao aplicativo após iniciar o hardware |
| **Multímetro e experiência com hardware** | Resolver conexões não documentadas antes de acioná-las |

Fotografe os dois lados do conjunto desligado antes de remover qualquer peça. Registre orientação dos conectores, parafusos, espaçadores e trajeto da antena. Mantenha o cartão e a configuração originais disponíveis até que a nova instalação passe pelos testes de aceitação.

## Identifique as três camadas

**O M1 completo, o carrier shield e o concentrador são componentes distintos.** A documentação da Seeed descreve o hotspot montado com um Raspberry Pi 4 e um concentrador WM1302/SX1302 ou WM1303/SX1303. Um anúncio chamado “SenseCAP M1 shield” não informa qual desses componentes acompanha o carrier. [Visão geral do M1 pela Seeed Studio](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

O **carrier** conecta alimentação e sinais periféricos entre o Pi e o módulo. O **concentrador** cuida da recepção e transmissão de rádio. Um **encaminhador de pacotes** executado no host troca os pacotes de rádio recebidos e os downlinks agendados com um servidor. [Visão geral do SX1302 HAL pela Semtech](https://github.com/Lora-net/sx1302_hal)

Por exemplo, um sensor de temperatura de prateleira envia um uplink por rádio. O concentrador o recebe, o host o encaminha e os serviços de rede e aplicação o processam. Uma inicialização correta do Linux comprova apenas a parte do host nessa cadeia.

A foto de Clockwork Bird mostra um carrier M1 v1.1 com um módulo identificado como `WM1302-SPI-EU868`. Use a foto para localizar os rótulos no seu hardware. Os números de série identificam o equipamento fotografado, não os valores de configuração de outro gateway.

{{< figure src="m1-carrier-wm1302-board.webp" alt="Carrier M1 verde com módulo WM1302 SPI EU868 identificado, perto de USB-C, botão, conector de ventilador e cabo de antena" caption="Hardware M1 v1.1 fotografado por Clockwork Bird, também usado na capa deste artigo" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Conexões de alimentação e rádio

**Trate o conector USB-C do M1 como entrada de alimentação.** O fabricante especifica 5 V CC, 3 A para o gateway completo e identifica USB-C como interface da fonte. Chamá-lo de porta de carga sugere uma bateria que essas especificações não mencionam. [Especificações do SenseCAP M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

O diagrama de blocos do fabricante separa a fonte de 5 V do trilho regulado de 3,3 V do módulo. Essa diferença importa no diagnóstico: o Pi pode estar ligado enquanto o concentrador fica sem alimentação. Não injete 5 V em um pino de sinal nem presuma que as duas entradas de energia são isoladas.

**As versões SPI e USB do módulo exigem conexões diferentes ao host.** A documentação WM1302 da Seeed descreve acesso SPI direto para a versão SPI e uma ponte USB STM32L4 para a versão USB. O formato mini-PCIe descreve a forma do módulo, enquanto as interfaces elétricas documentadas são SPI ou USB. Encaixar em um soquete de laptop não comprova compatibilidade. [Documentação WM1302 da Seeed](https://github.com/seeed-lora/WM1302-doc)

Antes de energizar o conjunto, instale o módulo com a alimentação desligada e conecte uma antena adequada. Combine hardware RF, antena e plano regional pretendido. Alterar o nome de um arquivo de configuração não muda os componentes RF; o conector de alimentação M1 também não comprova suporte a uma variante USB do concentrador.

{{< figure src="m1-power-spi-system-diagram.webp" alt="Diagrama de blocos que conecta Raspberry Pi 4 ao shield M1 por alimentação, SPI, GPIO e I2C" caption="Diagrama do fabricante SenseCAP reproduzido no artigo original de Clockwork Bird, mostrando o projeto WM1302" credit="Seeed Studio / SenseCAP, via Clockwork Bird" attr="Seeed Studio / SenseCAP, via Clockwork Bird" attrlink="https://www.sensecapmx.com/docs/sensecap-m1/overview/" >}}

## Leia o pinout com atenção

**Registre números GPIO BCM e pinos físicos do conector em colunas separadas.** Por exemplo, o BCM GPIO17 fica no pino físico 11 do conector Pi. O conector de borda do módulo usa um terceiro sistema de numeração, portanto seu número de pino de reset não é um número GPIO do Raspberry Pi.

A tabela abaixo transcreve as conexões da imagem anotada de Clockwork Bird. Ela é uma **referência comunitária**, não um esquema completo do fabricante nem uma medição de todas as revisões M1. O desenho também usa rótulos `SX1262`, enquanto o script genérico de reset da Semtech usa nomes `SX1261`.

| Sinal no desenho | BCM / pino físico | Interpretação |
|---|---|---|
| **I2C SDA / SCL** | GPIO2 / 3, GPIO3 / 5 | Barramento de gerenciamento compartilhado |
| **Reset SX1302** | GPIO17 / 11 | Candidato a reset do concentrador |
| **LED do usuário** | GPIO22 / 15 | Anotação M1 |
| **SPI MOSI / MISO** | GPIO10 / 19, GPIO9 / 21 | Sinais de dados SPI |
| **Clock SPI** | GPIO11 / 23 | Sinal de clock SPI |
| **Seleção SX1302** | GPIO8 / 24 | SPI0 CE0 |
| **Reset SX1262** | GPIO5 / 29 | Candidato a reset do rádio auxiliar |
| **Seleção SX1262** | GPIO6 / 31 | GPIO6, diferente de SPI0 CE1 |
| **SX1262 BUSY** | GPIO18 / 12 | Saída de status do rádio auxiliar |
| **SX1262 IO1 / IO2** | GPIO23 / 16, GPIO24 / 18 | Sinais auxiliares a verificar antes de usar |

As anotações GPS/UART riscadas não comprovam que o M1 tenha GPS. Não inclua configurações de GPS sem esse hardware. O diagrama publicado também não esclarece o botão de usuário nem o controle do ventilador. [Investigação do pinout por Clockwork Bird](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)

{{< figure src="m1-community-header-pinout.webp" alt="Desenho anotado do conector Raspberry Pi com LED M1, reset do concentrador, sinais SPI e conexões GPS riscadas" caption="Referência comunitária anotada com cobertura incompleta das revisões, não é um esquema M1 completo" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Resolva conflitos dos scripts de reset

**Um script de reset seleciona saídas elétricas, não meras preferências de software.** O `reset_lgw.sh` upstream da Semtech destina-se ao projeto de referência CoreCell. Os padrões incluem GPIO23 para reset do concentrador, GPIO18 para habilitar a alimentação, GPIO22 para reset auxiliar e GPIO13 para reset do AD5338R. [Fonte do script de reset da Semtech](https://github.com/Lora-net/sx1302_hal/blob/master/tools/reset_lgw.sh)

As instruções antigas da Seeed alteram as duas atribuições de reset para GPIO17 e GPIO5, mas mantêm outras entradas do projeto de referência. Compare esses valores com a imagem M1 anotada antes de seguir o exemplo. [Instruções de configuração WM1302 da Seeed](https://github.com/seeed-lora/WM1302-doc)

| Atribuição | Evidência conflitante | Decisão necessária |
|---|---|---|
| **GPIO22 como reset auxiliar** | A imagem M1 o identifica como LED de usuário | Remova essa suposição antes de ativar o LED |
| **GPIO18 como habilitação de alimentação** | A imagem M1 o identifica como BUSY auxiliar | Verifique a rede e a direção antes de acioná-lo |
| **GPIO13 como reset do DAC** | O script genérico nomeia outro projeto de referência | Determine se o circuito existe |
| **Dispositivo SPI auxiliar** | A imagem M1 seleciona GPIO6 em vez de CE1 | Confirme o roteamento da seleção e o suporte do driver |

**Inferência:** Se GPIO18 estiver conectado à saída de um rádio auxiliar como desenhado, configurá-lo como saída no lado do Pi cria risco de contenção elétrica. A divergência exige verificação, mas não comprova dano nem um mapa de fiação universal para todos os M1.

Desconecte toda a alimentação e rastreie conexões acessíveis entre o conector e o módulo. Registre a revisão da placa e as duas pontas. A continuidade comprova conexão; a documentação do componente esclarece direção e limites elétricos do sinal.

Use o diagrama do módulo abaixo para não confundir pinos do conector de borda com os do Pi. Os rótulos do rádio auxiliar descrevem a referência publicada do módulo, não provam o mesmo silício ou recursos em todas as revisões. [Pinout do módulo WM1302 da Seeed](https://github.com/seeed-lora/WM1302-doc/blob/master/pinout.jpg)

{{< figure src="wm1302-module-edge-connector.webp" alt="Diagrama Seeed que identifica os dois lados do conector de borda WM1302 com alimentação, SPI, I2C e sinais de rádio auxiliares" caption="A numeração do conector de borda do módulo difere da numeração do conector Raspberry Pi" credit="Seeed Studio" attr="Seeed Studio, WM1302-doc" attrlink="https://github.com/seeed-lora/WM1302-doc" >}}

## Prepare o Raspberry Pi OS

Registre o ambiente do host na instalação reserva:

```bash
cat /etc/os-release
uname -r
tr -d '\0' < /proc/device-tree/model
```

A versão do sistema, o kernel e o modelo Pi formam o ponto de partida reproduzível. Registre-os antes de comparar resultados com um tutorial antigo.

Instale ferramentas de inspeção e compilação:

```bash
sudo apt update
sudo apt install git build-essential i2c-tools gpiod
sudo raspi-config
```

Em **Interface Options**, habilite SPI e I2C e reinicie. SPI atende ao caminho do concentrador, e I2C aos dispositivos de gerenciamento descritos adiante. Não copie alterações de porta serial GPS sem relação com este hardware de outro tutorial de HAT.

Inspecione as interfaces expostas:

```bash
ls -l /dev/spidev* /dev/i2c-*
i2cdetect -l
gpiodetect
gpioinfo
gpioset --version
```

Esses comandos listam nós de dispositivo, adaptadores, controladores GPIO, linhas e versão da ferramenta GPIO instalada. **`i2cdetect -l` lista adaptadores sem varrer endereços.** O arquivo `/dev/spidev0.0` comprova que a interface SPI está exposta, não que se comunica com um concentrador funcional. [Manual i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), [Orientações GPIO do Raspberry Pi](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

### Considere as versões de GPIO

**Não copie números GPIO globais de outra máquina.** Scripts antigos usam `/sys/class/gpio`, uma interface declarada obsoleta pela documentação do kernel. Novas integrações em espaço de usuário devem usar a interface GPIO character device com o controlador e o deslocamento de linha corretos. [Documentação Linux GPIO](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)

Confira também `gpioset --help` antes de adaptar um script. A sintaxe e o comportamento dos processos diferem entre as versões 1 e 2. A ferramenta atual mantém as linhas solicitadas por padrão, mas o contrato portátil não garante o estado depois que o processo termina. [Documentação gpioset do libgpiod](https://libgpiod.readthedocs.io/en/master/gpioset.html)

O Raspberry Pi documenta um comportamento de persistência de saída no kernel e opções para alterá-lo. Registre a configuração real do kernel, sem supor que todo Linux se comporta igual. Uma numeração nova ou ferramenta GPIO recente não corrige um mapa elétrico incorreto. [Guia de uso GPIO do Raspberry Pi](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

## Teste o LED do usuário

Após confirmar que GPIO22 pertence ao LED e remover usuários GPIO conflitantes, edite a configuração de inicialização:

```bash
sudoedit /boot/firmware/config.txt
```

Versões modernas do Raspberry Pi OS montam a configuração de inicialização em **`/boot/firmware/config.txt`**. Imagens antigas usam `/boot/config.txt`, o caminho citado no artigo de 2023. Faça uma cópia do arquivo ativo antes de editá-lo. [Documentação config.txt do Raspberry Pi](https://www.raspberrypi.com/documentation/computers/config_txt.html)

Adicione o overlay LED a uma seção aplicável ao Pi, como `[all]`:

```ini
dtoverlay=gpio-led,gpio=22,label=lorawan,trigger=heartbeat
```

O parâmetro **`gpio`** usa a numeração BCM. **`label`** nomeia o dispositivo LED Linux e **`trigger=heartbeat`** seleciona o gatilho heartbeat do kernel. Clockwork Bird relata essa atribuição para o M1, e a referência de overlays do Raspberry Pi documenta esses parâmetros. [Observação original do LED](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), [Referência do overlay gpio-led](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README)

Após reiniciar, inspecione o LED registrado:

```bash
ls -l /sys/class/leds/
cat /sys/class/leds/lorawan/trigger
```

O resultado esperado é uma entrada LED `lorawan` com `heartbeat` selecionado entre colchetes. O LED piscando demonstra o caminho GPIO/driver. Não indica registro LoRaWAN, recepção de rádio nem estado Helium.

## Investigue dispositivos I2C

**Um endereço I2C é uma pista, não uma identidade do dispositivo.** Clockwork Bird observou respostas em `0x60` e `0x39`, depois leu informações ATECC608 pela biblioteca criptográfica. A identificação do sensor de temperatura permaneceu provisória no artigo original.

Comece pela lista de adaptadores da seção anterior. Varreduras amplas do `i2cdetect` enviam transações de sondagem, não observam passivamente o tráfego, e o manual upstream alerta para interrupções. Evite sondagens rotineiras em um gateway ativo ou dispositivos conectados desconhecidos. [Comportamento de sondagem do i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)

| Observação | Conclusão sustentada | Questão em aberto |
|---|---|---|
| **Resposta em `0x60`** | Algo reconheceu a sondagem | É o elemento seguro esperado? |
| **Resposta em `0x39`** | Algo reconheceu a sondagem | Qual componente e revisão responderam? |
| **`UU` na varredura** | Um driver possui o endereço e a sondagem foi ignorada | Qual driver o possui? |
| **Sem resposta** | A sondagem não recebeu confirmação | Alimentação, barramento, proprietário ou protocolo? |

### Reforce a hipótese do sensor de temperatura

**STTS751 é um candidato a `0x39` respaldado por fontes.** O cabeçalho do driver de temperatura Semtech associa explicitamente `0x39` ao `STTS751-0DP3F`. Isso reforça a hipótese original, sem identificar todos os componentes ligados a esse endereço. [Cabeçalho do driver STTS751 Semtech](https://github.com/Lora-net/sx1302_hal/blob/master/libloragw/inc/loragw_stts751.h)

Após identificar um componente compatível e garantir que nenhum outro processo o utiliza, leia os registros de identificação:

```bash
sudo i2cget 1 0x39 0xfd b
sudo i2cget 1 0x39 0xfe b
```

Aqui, **`1`** seleciona o barramento verificado, **`0x39`** o dispositivo e **`b`** solicita leitura SMBus de byte de dados. Para STTS751-0, o ID do produto documentado em `0xFD` é `0x00`, e o ID do fabricante em `0xFE` é `0x53`. As transações selecionam endereços de registro, mas não gravam valores de configuração. [Datasheet STTS751, mapa e registros de identificação](https://www.st.com/resource/en/datasheet/stts751.pdf)

Compare as leituras com a marcação do chip e sua documentação. Um par correspondente aumenta a evidência de identificação; em caso de erro, verifique barramento e proprietário antes de alterar a configuração. O sensor mede sua temperatura local, diferente da temperatura da CPU do Pi.

## Inspecione o elemento seguro

**O ATECC608 é um componente de autenticação separado.** Trate configuração, número de série, chave pública e material de chave protegido como conceitos distintos. Ler uma chave pública não revela a chave privada correspondente.

A **CryptoAuthLib** da Microchip oferece a interface do dispositivo. O repositório **cryptoauthtools** contém exemplos baseados na biblioteca. Prepare a biblioteca nativa e os bindings Python para seu sistema seguindo as instruções desses projetos antes de executar um exemplo. Instalar um pacote Python sem relação ou copiar um script isolado não comprova que o backend I2C funciona. [CryptoAuthLib da Microchip](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools da Microchip](https://github.com/MicrochipTech/cryptoauthtools)

Em um diretório `cryptoauthtools/python/examples` preparado, execute o comando de inspeção do artigo original:

```bash
sudo python3 info.py -i i2c
```

O argumento **`-i i2c`** seleciona a interface. Em um ambiente virtual, use o interpretador Python explícito e confirme que ele localiza a biblioteca nativa correspondente. Em muitas instalações, `sudo python3` seleciona o interpretador do sistema, o que explica algumas falhas de importação.

O `info.py` revisado lê informações de revisão, número de série, configuração e estado de bloqueio. Se a zona de dados estiver bloqueada, tenta obter a chave pública do slot 0. Não executa a sequência de provisionamento do exemplo. Uma falha isolada ao ler a chave pública do slot 0 não comprova defeito no dispositivo. [Fonte do info.py da Microchip](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/info.py)

| Saída ou operação | Significado |
|---|---|
| **Configuração bloqueada** | Restrições de configuração estão ativas |
| **Zona de dados bloqueada** | Interprete o acesso conforme as políticas dos slots configuradas |
| **Chave pública exibida** | Informações públicas foram obtidas, não houve exportação de chave privada |
| **Execução de `config.py`** | Exemplo de provisionamento com escrita, bloqueio e geração de chaves |

**Não execute `config.py` para corrigir um erro de inspeção.** O código inclui gravações de configuração, chamadas para bloquear zonas e geração de chaves. O caminho padrão de geração de chave também importa em um dispositivo já configurado. [Fonte do config.py da Microchip](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/config.py)

Os perfis de provisionamento documentados pela Microchip mostram por que uma zona de dados bloqueada não significa que todos os slots tenham permissões iguais. Esses perfis não estabelecem a configuração exata do M1. Preserve a configuração existente e consulte a documentação da peça correspondente antes de planejar uma reutilização de chaves. [Políticas de memória e acesso a slots da Microchip](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html)

## Investigue dúvidas sobre ventilador e botão

**Um conector de ventilador de três pinos não informa tensão, polaridade nem método de controle.** Fotografe a numeração dos pinos e leia o rótulo do ventilador. Confirme alimentação e controle antes de conectar um substituto ou escolher um overlay GPIO.

A investigação original também não identifica o GPIO do botão. Procure um driver ou uma configuração vinculada à revisão da placa e verifique a conectividade com a alimentação desligada. Não configure todas as GPIOs aparentemente livres como saídas para encontrar o botão.

| Periférico | Evidência a coletar | Critério de aceitação |
|---|---|---|
| **Alimentação do ventilador** | Especificação do ventilador, terra e alimentação do conector | A fonte medida corresponde à especificação do ventilador |
| **Controle do ventilador** | Driver/configuração ou circuito de controle rastreado | Comportamento definido na inicialização e em temperatura elevada |
| **Botão de usuário** | Fiação dos contatos, mapa GPIO, polaridade de entrada | Um toque intencional produz o evento esperado |

Uma nova instalação do sistema operacional não reproduz automaticamente a política de refrigeração do equipamento original. No primeiro teste prolongado, observe ventilador e temperaturas juntos. Preserve o fluxo de ar do gabinete e interrompa o teste se o conjunto perder o resfriamento necessário.

## Escolha uma pilha de gateway

**Separe o suporte da placa do protocolo do servidor.** Um servidor LoRaWAN compatível não corrige uma rotina de reset errada nem uma calibração RF inadequada. Primeiro escolha software compatível com o concentrador, a fiação do carrier, o sistema e a configuração regional.

| Opção de software | Função útil | Verificar antes da implantação |
|---|---|---|
| **Semtech SX1302 HAL** | Inicialização no nível do código-fonte e ferramentas de diagnóstico | Rotina de reset da placa e configuração do módulo |
| **LoRa Basics Station** | Conexão autenticada do gateway a um servidor | Integração funcional da placa e credenciais do servidor |
| **ChirpStack Concentratord** | Serviço dedicado ao concentrador | Modelo compatível, calibração e mapa GPIO |

O ChirpStack lista o modelo SPI **`seeed_wm1302`**. Isso comprova suporte ao módulo, não uma imagem M1 completa nem suporte a todas as revisões. Não trate as instruções separadas de instalação SenseCAP M2 como firmware M1. [Suporte de hardware ChirpStack](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html), [Alvo de instalação Seeed no ChirpStack](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html)

Para o The Things Stack, a documentação recomenda **LoRa Basics Station** em vez do encaminhador UDP Semtech legado. Station oferece TLS e autenticação por token, além de funções de configuração centralizada. Exemplos UDP ajudam a entender o encaminhamento de pacotes, mas seus parâmetros de servidor não fornecem essas proteções. [Orientações UDP do The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [Documentação LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)

### Prepare as ferramentas upstream

Compile no Pi alvo em um novo diretório de trabalho:

```bash
git clone https://github.com/Lora-net/sx1302_hal.git
cd sx1302_hal
git rev-parse HEAD
make
```

Salve o identificador do commit com a saída do build. Uma compilação concluída comprova compatibilidade com o compilador, mas o rádio ainda exige uma rotina de reset verificada e configuração correta. A documentação Semtech explica a função do HAL e das ferramentas auxiliares. [Documentação de build e ferramentas SX1302 HAL](https://github.com/Lora-net/sx1302_hal)

Revise o arquivo de reset antes de executar ferramentas de acesso ao hardware:

```bash
sed -n '1,180p' tools/reset_lgw.sh
```

Não copie esse arquivo sem alterações para o diretório de execução. A Semtech documenta que seus programas de acesso ao hardware, inclusive ferramentas de identificação, usam o script de reset automaticamente. Revise cada pino atribuído, sentido do sinal, API GPIO e estado de inicialização/encerramento.

Depois de verificar a placa, siga as instruções da pilha escolhida para ler o EUI do concentrador e registrar o gateway. Preserve a calibração do módulo e as configurações RF ao adicionar os dados do servidor. Na configuração UDP Semtech, `gateway_ID` representa o EUI; o Gateway ID do console The Things Stack é o identificador legível usado no registro. [Configuração de gateway The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)

## Comprove a entrega do sensor

**Use evidências por etapas para localizar a primeira camada que falha.** Um gateway indicado como online comprova conexão ao servidor. O teste de aceitação também precisa de um sensor conhecido, plano de frequência correspondente e payload de aplicação decodificado.

A sequência abaixo é um plano de teste proposto, não resultados medidos em um M1:

| Etapa | Evidência a salvar | Significado |
|---|---|---|
| **Host pronto** | Sistema, kernel, alimentação e inventário de interfaces | Preparação Linux concluída |
| **Concentrador responde** | EUI e log de inicialização bem-sucedida | Comunicação host-concentrador funciona |
| **Recepção de rádio** | Pacote esperado do sensor e metadados de recepção | Caminho de recepção configurado funciona |
| **Servidor aceita** | Evento de gateway associado ao sensor | Encaminhamento e roteamento do servidor funcionam |
| **Aplicação decodifica** | Medição esperada e registro de data e hora | Caminho da aplicação funciona |
| **Recuperação após reinício** | As mesmas verificações após reiniciar | Configuração de inicialização é reproduzível |

Para um sensor **OTAA**, confirme também a troca de ativação e o uplink seguinte. OTAA significa ativação over-the-air, o processo de ingresso que estabelece uma sessão. Receber uma solicitação de ingresso não comprova ingresso concluído nem caminho de downlink. [Documentação de ativação The Things Stack](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/)

**Diagnóstico prático:** o gateway conecta ao servidor e informa seu EUI, mas o sensor não aparece. Priorize a configuração de transmissão do sensor, os canais de recepção selecionados, o trajeto da antena e os logs de rádio. Reprogramar o ATECC608 não resolveria a falta de evidências nesse cenário.

**Segundo diagnóstico:** um pacote do sensor aparece localmente, mas não chega à aplicação. Correlacione o horário do pacote com eventos do gateway e do servidor, depois examine roteamento, registro do dispositivo e decodificação. Um pacote RF no log não basta para culpar o decodificador antes que o servidor aceite o evento.

## Solucione problemas por sintoma

| Sintoma | Verifique primeiro | Próxima ação |
|---|---|---|
| **Arquivo de dispositivo SPI ausente** | Configuração de boot ativa e opções de interface | Ative a interface pretendida e reinicie |
| **SPI existe, rádio falha** | Alimentação, encaixe, sequência de reset e seleção do chip | Verifique o caminho elétrico antes de mudar o servidor |
| **Erro de exportação GPIO** | Premissas antigas de sysfs e kernel instalado | Use uma implementação revisada para a API GPIO |
| **GPIO ocupado** | Consumidor mostrado por `gpioinfo` | Resolva a propriedade antes de tentar novamente |
| **LED falha após configuração** | Aplicação do overlay e conflitos GPIO22 | Examine LEDs registrados e script de reset |
| **Dispositivo I2C ausente** | Número do barramento, alimentação e propriedade existente | Investigue sem repetir varreduras amplas |
| **Falha ao importar biblioteca criptográfica** | Interpretador, bindings e caminho da biblioteca nativa | Corrija o ambiente de software |
| **Falha ao ler chave pública** | Política do slot e leituras anteriores bem-sucedidas | Examine a configuração sem provisionar |
| **Ventilador não funciona** | Alimentação verificada e controle de refrigeração | Restaure a refrigeração antes de testes prolongados |
| **Uplinks chegam, ingresso falha** | Caminho downlink e configurações regionais/do dispositivo | Rastreie a resposta de ingresso e as janelas de recepção |

Trate cada correção como um experimento. Salve a configuração anterior, altere uma variável, repita o mesmo teste e registre se a evidência esperada apareceu.

## Crie seu registro de hardware

Use este modelo para transformar a investigação em um repasse reproduzível:

```text
Revisão do carrier e fotos:
Modelo do concentrador, interface e banda RF:
Modelo do host / sistema / kernel / versão da ferramenta GPIO:
Fonte / antena / arranjo de refrigeração:
Mapa de pinos verificado e evidências:
Redes não resolvidas e recursos excluídos:
Repositório do software e commit:
Implementação do reset e propriedade GPIO:
EUI do gateway / servidor / plano de frequência:
Ativação do sensor e evidência do uplink decodificado:
Resultado da recuperação após reinício:
Local do cartão original e procedimento de rollback:
```

**Exercício de decisão:** você tem um carrier simples barato sem rótulo do módulo e um conjunto mais caro com rótulos legíveis e funcionamento documentado. Decida qual atende ao projeto após incluir o Pi, concentrador, antena, fonte e tempo de verificação necessários. A melhor escolha considera o custo total e as evidências exigidas pelo serviço, não apenas o preço anunciado do carrier.

**Raciocínio esperado:** um projeto de aprendizagem tolera fiação não resolvida se houver instrumentos e tempo. Um gateway para sensores operacionais exige inicialização repetível, refrigeração, suporte de software e entrega demonstrada. Registre qual condição não resolvida interromperia a implantação.

## Próximas etapas

Comece completando o registro de hardware e resolvendo as divergências do script de reset. Em seguida, coloque um sensor conhecido em operação e salve evidências até a decodificação pela aplicação antes de adicionar mais dispositivos.

**Registro de aceitação:** salve a revisão da placa, rótulo do módulo, banda de rádio, medida de alimentação, dispositivo SPI ativo, nomes das linhas GPIO, sequência de reset, log do concentrador, conexão ao servidor e um uplink decodificado. Marque cada valor como observado, documentado ou ainda presumido. Não trate a inicialização de um processo como prova de desempenho RF ou entrega à aplicação.

Se seu objetivo for mensagens mesh, compare primeiro os papéis dos protocolos em nosso [guia Meshtastic, MeshCore e Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/). Compartilhar a tecnologia de rádio LoRa não comprova compatibilidade de firmware. Para uma implantação de mensagens, consulte a [documentação de hardware compatível com MeshtasticD](https://meshtastic.org/docs/meshtasticd/) em vez de tratar este procedimento LoRaWAN como conversão para Meshtastic.

## Fontes e créditos das imagens

Pesquisa verificada em 12 de setembro de 2026. Links sem data para documentos e repositórios referem-se às versões analisadas para este artigo. Figuras locais mantêm seus rótulos e atribuições originais.

| Editor | Fonte e data |
|---|---|
| **Clockwork Bird** | [SenseCAP M1 Raspberry Pi Shield](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), 2023-05-03. Foto da placa, conector anotado e diagrama de blocos do fabricante reproduzido |
| **Seeed Studio / SenseCAP** | [Visão geral e especificações do M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/), sem data. Atribuição do diagrama original |
| **Seeed Studio** | [Documentação WM1302 e pinout do módulo](https://github.com/seeed-lora/WM1302-doc), repositório |
| **Semtech** | [SX1302/SX1303 HAL](https://github.com/Lora-net/sx1302_hal), com fontes vinculadas do script de reset e driver de temperatura |
| **Raspberry Pi** | [Configuração de boot](https://www.raspberrypi.com/documentation/computers/config_txt.html), [guia de uso GPIO](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices) e [referência de overlays](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README) |
| **Linux / libgpiod** | [Interface GPIO sysfs obsoleta](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html) e [manual gpioset](https://libgpiod.readthedocs.io/en/master/gpioset.html), este último de agosto de 2026 |
| **i2c-tools** | [Manual i2cdetect](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), fonte v4.3 |
| **STMicroelectronics** | [Datasheet STTS751](https://www.st.com/resource/en/datasheet/stts751.pdf), revisão 7 |
| **Microchip** | [CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools) e [documentação da política de acesso aos slots](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html) |
| **ChirpStack** | [Suporte de hardware Concentratord](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html) e [alvo de instalação Seeed](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html) |
| **The Things Industries** | [Encaminhador UDP](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/) e [ativação de dispositivos](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/) |
| **Meshtastic** | [Documentação MeshtasticD](https://meshtastic.org/docs/meshtasticd/), sem data |

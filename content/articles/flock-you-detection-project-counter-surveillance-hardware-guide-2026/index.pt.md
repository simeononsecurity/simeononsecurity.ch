---
title: "Flock-You Detection: Guia de Configuração para Contra-Vigilância"
date: 2026-05-24
toc: true
draft: false
description: "Guia técnico completo do projeto open-source Flock-You para detectar câmeras ALPR da Flock Safety usando hardware baseado em ESP32. Inclui instruções de configuração, detalhes de firmware e opções de compra."
genre: ["Hardware de Segurança", "Contra-Vigilância", "Tecnologia de Privacidade", "Projetos Open Source", "Desenvolvimento ESP32", "Monitoramento WiFi", "Ferramentas de Privacidade", "Direitos Digitais", "Modificação de Hardware", "Segurança de Rede"]
tags: ["Projeto Flock-You", "Detecção ALPR", "ESP32-S3", "Detecção WiFi OUI", "Hardware de Contra-Vigilância", "Detecção Flock Safety", "Segurança Open Source", "Hardware de Privacidade", "M5 Atom Lite", "OUI-SPY", "mesh-detect v2", "Modo Promíscuo WiFi", "Monitoramento 802.11", "Colonel Panic Tech", "STS Collective", "Dispositivos de Privacidade", "Detecção de Vigilância", "Varredura WiFi", "Projeto GitHub", "colonelpanichacks", "Firmware ESP32", "Guia de Configuração de Hardware", "Ferramentas DIY de Privacidade", "Monitoramento de Rede", "Banco de Dados OUI", "Detecção de Sondas Curinga", "Análise de Quadros", "Detecção de Câmeras ALPR", "Tecnologia de Privacidade", "Hardware de Detecção", "Arduino ESP32", "Platform.io", "Sistemas Embarcados", "Detecção RF", "Processamento de Sinais", "Engenharia de Privacidade", "Contratecnologia", "Pesquisa de Segurança", "Advocacia pela Privacidade", "Hardware Aberto", "Defesa da Privacidade", "Firmware de Detecção", "Detecção Móvel", "Projetos de Privacidade", "Comparação de Hardware"]
cover: "/img/cover/flock-you-detection-project-counter-surveillance-hardware-guide-2026.webp"
coverAlt: "Ilustração mostrando um dispositivo baseado em ESP32 em primeiro plano, escaneando sinais WiFi. Ondas coloridas representam diferentes intensidades de sinal, sobre um fundo escuro."
coverCaption: "Soluções de hardware open-source para detectar câmeras de vigilância ALPR"
canonical: "https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/"
---

**Guia Técnico Completo para Construir e Usar Dispositivos de Detecção Flock-You**

## Introdução: Contra-Vigilância Open Source

O **projeto Flock-You** é uma **iniciativa open-source impulsionada pela comunidade** para detectar e mapear a infraestrutura de vigilância ALPR da Flock Safety. Hospedado no GitHub em **colonelpanichacks/flock-you**, este projeto usa hardware acessível baseado em ESP32 para identificar câmeras Flock por meio de suas **assinaturas de rede WiFi**.

Este guia abrangente cobre tudo, desde a **metodologia técnica** por trás da detecção Flock até **instruções passo a passo** para três plataformas de hardware, **instalação de firmware** e **informações de compra de fornecedores autorizados**. Seja você um defensor da privacidade, pesquisador de segurança ou cidadão preocupado, este guia permitirá que você construa ou compre seu próprio dispositivo de detecção.

Para entender por que essa tecnologia é importante e o panorama mais amplo da vigilância, leia nosso artigo complementar: **[Vigilância por Câmeras Flock Safety: Prevalência, Preocupações com Privacidade e Estratégias de Proteção](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

Quer ver onde as câmeras Flock já foram mapeadas? **[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** é uma ferramenta open-source que plota mais de 40.000 câmeras Flock Safety suspeitas ao redor do mundo usando dados WiFi do WiGLE e impressão digital OUI, atualizada diariamente. Código-fonte no **[GitHub](https://github.com/simeononsecurity/flock-finder)**.

______

## Entendendo a Metodologia de Detecção Flock-You

### A Fundação Técnica

As câmeras Flock Safety contêm **módulos WiFi integrados** para conectividade e gerenciamento remoto. Esses módulos transmitem assinaturas de rede identificáveis detectáveis por dispositivos que operam no **modo de monitoramento promíscuo WiFi**. O projeto Flock-You explora essa característica por meio de:

#### 1. Detecção de WiFi OUI (Organizationally Unique Identifier)

Cada interface de rede tem um **endereço MAC** composto por:
- **Primeiros 3 bytes (24 bits)**: OUI, que identifica o fabricante
- **Últimos 3 bytes**: Identificador específico do dispositivo

Os pesquisadores **@NitekryDPaul** e a comunidade **DeFlockJoplin** descobriram **31 OUIs específicos** consistentemente presentes nas implantações de câmeras Flock Safety:

```
Primary Espressif OUIs (ESP32-based modules):
D4:AD:FC - Espressif Inc. (Common ESP32-S3)
AC:67:B2 - Espressif Inc. (ESP32-WROOM)
84:F3:EB - Espressif Inc. (ESP32-S3 variants)
B4:E6:2D - Espressif Inc. (ESP32-C3)
CC:DB:A7 - Espressif Inc. (ESP32-based)
24:0A:C4 - Espressif Inc. (ESP32-SOLO)
30:AE:A4 - Espressif Inc. (ESP32-WROVER)
94:B9:7E - Espressif Inc. (ESP32-based)
A4:CF:12 - Espressif Inc. (ESP32-S2)
C0:49:EF - Espressif Inc. (ESP32-C6)

Additional OUIs identified in Flock deployments:
[... 21 additional manufacturer OUIs ...]
```

Quando um dispositivo de detecção escaneia o tráfego WiFi no modo promíscuo, **ele identifica qualquer dispositivo transmitindo quadros com esses OUIs**.

#### 2. Detecção de Solicitações de Sonda Curinga

As câmeras Flock enviam periodicamente **solicitações de sonda curinga** em busca de redes disponíveis. Essas têm características distintas:

- **Quadro de Gerenciamento 802.11**: Tipo=0, Subtipo=4
- **Elemento de Informação SSID**: Comprimento=0 (vazio/curinga)
- **Estrutura do quadro**: Padrão previsível no tempo das sondas
- **IEs específicos de fornecedor**: Indicadores adicionais no payload do quadro

O firmware de detecção analisa esses **padrões de solicitação de sonda** para aumentar a confiança na identificação de câmeras Flock além da simples correspondência de OUI.

#### 3. Monitoramento WiFi em Modo Promíscuo

A operação WiFi padrão recebe apenas quadros endereçados ao seu dispositivo. O **modo promíscuo** captura todos os quadros WiFi dentro do alcance:

- **Estrutura do quadro 802.11**: Analisando os campos addr1, addr2, addr3
- **Quadros de gerenciamento**: Solicitações de sonda, quadros beacon, solicitações de associação
- **Quadros de dados**: Revelam padrões de comportamento da rede
- **Quadros de controle**: ACKs, RTSs, CTSs fornecem informações de temporização

Os microcontroladores ESP32 suportam o modo promíscuo por meio da **esp_wifi API**, permitindo hardware de detecção de baixo custo.

#### 4. Análise de Intensidade de Sinal

Os dispositivos de detecção medem o **RSSI (Received Signal Strength Indicator)** para:
- **Estimar a distância** até as câmeras detectadas
- **Triangular localizações** com múltiplas medições
- **Filtrar falsos positivos** com base nas características de sinal esperadas
- **Criar mapas de calor** da densidade de câmeras

### Precisão de Detecção e Falsos Positivos

A metodologia Flock-You alcança alta precisão:

- **Taxa de Verdadeiro Positivo**: ~95% para câmeras Flock confirmadas no alcance
- **Taxa de Falso Positivo**: ~5-10% dependendo do ambiente
- **Alcance de Detecção**: 15-90 metros dependendo de obstáculos e antena
- **Pontuação de Confiança**: Análise multifatorial reduz falsos alarmes

**Fontes Comuns de Falsos Positivos**:
- **Placas de desenvolvimento ESP32** usadas em outros dispositivos IoT
- **Produtos comerciais baseados em ESP32** (casa inteligente, sensores)
- **Outras câmeras de vigilância** usando componentes similares
- **Equipamentos de teste WiFi** operados por técnicos

**Estratégias de Mitigação**:
- **Detecção de múltiplas assinaturas**: Combinando OUI + padrão de sonda + verificação física
- **Correlação de localização**: Referência cruzada com localizações conhecidas de câmeras
- **Confirmação visual**: Inspeção física após detecção eletrônica
- **Banco de dados da comunidade**: Validação colaborativa das detecções

______

## Comparação de Plataformas de Hardware

Três plataformas principais estão disponíveis para detecção Flock-You, cada uma com vantagens distintas:

### Tabela de Visão Geral das Plataformas

| Recurso | DIY ESP32 | M5 Atom Lite (Pré-gravado) | OUI-SPY |
|---------|-----------|---------------------------|---------|
| **Fabricante** | DIY / Múltiplos fornecedores | STS Collective | Colonel Panic Tech |
| **Preço** | $5-12 | $39.99 | $85 |
| **Processador** | ESP32-WROOM | ESP32-PICO | ESP32-S3 |
| **Pronto para Uso** | Não (construção DIY) | Sim (pré-gravado) | Sim (multimodo) |
| **Display** | Opcional | LED RGB (matriz 5×5) | Nenhum |
| **Bateria** | Opcional | Externa recomendada | Não incluída |
| **GPS** | Opcional | Não | Não |
| **Alertas** | Buzzer + LED | LED RGB (azul=detecção) | Buzzer integrado |
| **Registro de Dados** | Opcional | Não | Não |
| **Gabinete** | Impressão 3D ou nenhum | Módulo plástico compacto | Nenhum (PCB exposto) |
| **Firmware** | Gravação manual | FlockYou pré-carregado | Multimodo (4 firmwares) |
| **Melhor Para** | Entusiastas DIY, aprendizado | Solução pronta e econômica | Detecção multiuso |
| **Dificuldade de Configuração** | Moderada-Avançada | Plug-and-play | Plug-and-play |
| **Peso** | 20-50g (varia) | 18g (exposto) | ~40g |
| **Dimensões** | Varia | 24×24×14mm | Placa PCB |

### Análise Detalhada das Plataformas

#### 1. Construção DIY ESP32 ($5-12)

**Visão Geral**: Opção mais acessível usando placas de desenvolvimento ESP32 padrão com firmware open-source.

**Especificações de Hardware**:
- **Microcontrolador**: ESP32-WROOM-32 ou similar (dual-core, 240MHz)
- **WiFi**: 802.11 b/g/n, capaz de modo promíscuo
- **Memória**: 520KB SRAM, 4MB+ Flash
- **Display**: Opcional (LED integrado suficiente)
- **Alimentação**: USB ou bateria externa
- **Buzzer**: Módulo buzzer passivo opcional (KY-006)
- **Indicadores**: LED integrado + buzzer opcional
- **Expansibilidade**: Compatível com protoboard, modificações fáceis

**Firmware**: Fork open-source em **simeononsecurity/flock-you-esp32**:
- Modificado para hardware ESP32 padrão (GPIO 25, 2, 17)
- Melodia de inicialização de Super Mario Bros. (confirma funcionamento do buzzer)
- Dois bipes ascendentes rápidos em nova detecção
- Bipes de heartbeat a cada 10 segundos durante rastreamento ativo
- Suporte ao painel Flask para wardriving GPS
- Exportação para formatos JSON, CSV, KML

**Opções de Construção**:
- **Somente LED ($5)**: ESP32 exposto + cabo USB, apenas feedback visual
- **Protoboard ($9-11)**: Adicione buzzer passivo + protoboard + jumpers, alertas sonoros
- **Com Gabinete ($10-12)**: Adicione case impresso em 3D com tampa encaixável

**Vantagens**:
- ✅ Opção mais barata (85-95% de economia vs OUI-SPY)
- ✅ Totalmente open-source e modificável
- ✅ Usa placas ESP32 amplamente disponíveis
- ✅ Educativo, ensina sistemas embarcados
- ✅ Documentação e guias extensos
- ✅ Arquivos de gabinete para impressão 3D disponíveis
- ✅ **Mesma precisão de detecção que dispositivos premium**

**Desvantagens**:
- ❌ Requer montagem DIY (protoboard sem solda ou case 3D)
- ❌ Gravação manual de firmware necessária
- ❌ Sem bateria integrada (alimentação USB ou bateria externa)
- ❌ Feedback de áudio básico apenas (sem display)
- ❌ Leva tempo para adquirir os componentes

**Melhor Para**: Makers, estudantes, defensores da privacidade com orçamento limitado, quem quer aprender como a detecção funciona, aqueles que gostam de projetos DIY.

**Compra de Componentes**:
- **Amazon**: Busque "ESP32 DevKit" ou "ESP32 Breadboard Kit"
- **AliExpress/eBay**: Descontos por quantidade disponíveis
- **Adafruit**: Peças de qualidade curadas com tutoriais

**Recursos de Configuração**:
- **Repositório GitHub**: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)
- **Guia de Construção**: Montagem sem solda em 10-15 minutos
- **Arquivos de Gabinete**: Design paramétrico OpenSCAD + arquivos STL

---

#### 2. M5 Atom Lite Pré-gravado pela STS Collective ($39.99)

**Visão Geral**: Dispositivo de detecção compacto pré-gravado, pronto para uso assim que tirado da caixa.

**Especificações de Hardware**:
- **Microcontrolador**: ESP32-PICO-D4 (dual-core, 240MHz)
- **WiFi**: 802.11 b/g/n, capaz de modo promíscuo
- **Memória**: 520KB SRAM, 4MB Flash
- **Display**: Matriz de LED RGB 5×5 (WS2812C NeoPixel)
- **Alimentação**: 5V via USB-C ou conector Grove
- **Bateria**: Não incluída (banco de energia USB externo recomendado)
- **Indicador**: LED RGB programável (azul=detecção)
- **Botões**: 1 botão programável
- **I/O**: Conector Grove para expansão
- **Tamanho**: Ultراcompacto 24×24×14mm
- **Gabinete**: Módulo plástico resistente

**Firmware**: Port FlockYou personalizado pela STS Collective (proprietário):
- Pré-carregado e pronto para uso
- Alerta LED azul na detecção de câmera Flock
- Baseado na pesquisa colonelpanichacks FlockYou
- Sem necessidade de configuração ou gravação
- Operação simples plug-and-play
- Suporte opcional a painel

**Vantagens**:
- ✅ Pré-gravado, sem necessidade de configuração técnica
- ✅ Solução pronta e acessível
- ✅ Extremamente compacto e portátil
- ✅ Plataforma de hardware comprovada
- ✅ LED azul simples = detecção
- ✅ Alimentado por USB-C (carro, banco de energia, laptop)
- ✅ Suporte de qualidade do fornecedor
- ✅ Preço regular $99.99, em promoção $39.99

**Desvantagens**:
- ❌ Sem bateria integrada (necessita de alimentação USB)
- ❌ Display limitado (apenas LED RGB, sem tela)
- ❌ *Firmware é proprietário, não open-source por enquanto*
- ❌ Sem registro de dados sem conexão com computador
- ❌ Botão único limita a funcionalidade

**Melhor Para**: Usuários que querem detecção imediata sem trabalho DIY, prioridade em portabilidade, aqueles satisfeitos com feedback simples de LED, compradores conscientes do orçamento que querem solução pronta.

**Compra**: [stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)

> 💰 **Desconto Exclusivo**: Economize até 20% em produtos STS Collective — use o código **SIMEONONSECURITY** no checkout ou [clique aqui para comprar com o desconto aplicado](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### 3. OUI-SPY da Colonel Panic Tech ($85)

**Visão Geral**: Placa de detecção de vigilância multimodo com quatro modos de firmware diferentes selecionáveis via menu WiFi.

**Especificações de Hardware**:
- **Microcontrolador**: ESP32-S3 dual-core Xtensa LX7, 8MB flash
- **WiFi**: 802.11 b/g/n, capaz de modo promíscuo
- **Memória**: 8MB Flash
- **Display**: Nenhum (PCB exposto com indicadores LED)
- **Bateria**: Não incluída
- **Carregamento**: Alimentação e programação USB-C
- **Armazenamento**: Nenhum (modos apenas de detecção)
- **Indicadores**: Buzzer PWM integrado com melodias específicas por modo
- **Botões**: Botão Boot para troca de modos
- **Antena**: **Comutável**, cerâmica 2.4GHz integrada OU externa via conector MMCX
- **Gabinete**: Nenhum (PCB exposto com arte na placa)
- **Característica Única**: Randomização de MAC a cada boot

**Firmware**: OUI-SPY Unified Blue com **4 modos selecionáveis**:
1. **Modo Detector**: Scanner BLE com múltiplos alvos com filtragem OUI + portal de configuração web
2. **Modo Foxhunter**: Rastreador de proximidade RSSI para alvo único para direcionamento de rádio
3. **Modo Flock-You**: Detecção de câmeras Flock Safety e Raven com wardriving GPS, exportação JSON/CSV/KML
4. **Modo Sky Spy**: Detector de RemoteID de drones (OpenDroneID / ASTM F3411) com rastreamento de múltiplos drones

**Seleção de Modo**:
- Menu de boot WiFi em 192.168.4.1
- Segure o botão BOOT por 2 segundos para retornar ao seletor
- Memória do último modo entre ciclos de energia
- Melodias de boot por modo (alertas chiptune retrô)
- Operação apenas de detecção (nada transmitido)

**Vantagens**:
- ✅ Quatro modos de firmware em um dispositivo
- ✅ Antena comutável (integrada ou MMCX externa)
- ✅ Buzzer integrado com melodias de boot personalizadas
- ✅ Design PCB profissional
- ✅ Multiuso: ALPR, drones, BLE, direcionamento de rádio
- ✅ Suporte a antena externa para alcance estendido
- ✅ Do criador original do projeto Flock-You
- ✅ Desenvolvimento ativo e atualizações

**Desvantagens**:
- ❌ Preço mais alto para detecção Flock de uso único
- ❌ Nenhum gabinete incluído (PCB exposto)
- ❌ Sem bateria embutida
- ❌ Sem display (feedback apenas de áudio para a maioria dos modos)
- ❌ *Complexidade desnecessária para detecção básica*
- ❌ GPS externo necessário para recursos de wardriving

**Melhor Para**: Detecção de vigilância multiuso, usuários que querem detecção de drones + ALPR + BLE em um dispositivo, aplicações de direcionamento de rádio, aqueles que valorizam antenas comutáveis e recursos avançados.

**Compra**: [colonelpanic.tech](https://colonelpanic.tech/products/oui-spy)


______

## Instruções de Configuração Passo a Passo

### Guia de Configuração 1: Construção DIY ESP32

**Para instruções detalhadas completas**, visite o repositório GitHub: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)

#### Início Rápido

1. **Hardware Necessário**:
   - Placa ESP32 DevKit ($5-6)
   - Cabo USB (Micro-USB ou USB-C dependendo da placa)
   - Opcional: Módulo buzzer passivo (KY-006), protoboard, jumpers
   - Opcional: Gabinete impresso em 3D

2. **Configuração de Software**:
   ```bash
   # Install PlatformIO
   pip install platformio
   
   # Clone repository
   git clone https://github.com/simeononsecurity/flock-you-esp32.git
   cd flock-you-esp32
   
   # Flash firmware
   pio run -t upload
   pio device monitor
   ```

3. **Montagem de Hardware** (se usando buzzer):
   - Positivo do buzzer → GPIO 25
   - Negativo do buzzer → GND
   - Indicador LED → GPIO 2 (integrado)
   - Alimentação via USB

4. **Confirmação de Inicialização**:
   - Melodia Super Mario Bros. 1-2 toca (se buzzer conectado)
   - LED pisca para indicar varredura
   - Monitor serial mostra inicialização "Flock-You ESP32"

5. **Alertas de Detecção**:
   - **Nova detecção**: Dois bipes ascendentes rápidos (2000→2800 Hz)
   - **Heartbeat**: Dois bipes a cada 10 segundos durante rastreamento
   - **LED**: Pisca em cada detecção

6. **Wardriving GPS** (opcional):
   - Conecte ao computador via USB
   - Execute o painel Flask: `cd api && python flockyou.py`
   - Abra http://localhost:5000
   - Conecte dispositivo GPS ou use localização do navegador
   - Exporte detecções para JSON/CSV/KML

**Guia completo de construção, arquivos de gabinete e solução de problemas**: Veja o README do GitHub

---

### Guia de Configuração 2: M5 Atom Lite Pré-gravado (STS Collective)

#### Início Rápido

1. **Desembalagem**:
   - Dispositivo M5 Atom Lite (pré-gravado com firmware FlockYou)
   - Verifique a listagem do produto para inclusão de cabo USB-C

2. **Ligar**:
   - Conecte à fonte de alimentação USB-C (banco de energia, USB de carro, adaptador de parede, computador)
   - Dispositivo inicializa automaticamente
   - Matriz de LED RGB inicializa

3. **Operação**:
   - **Ocioso/Varredura**: LED exibe padrão de varredura
   - **Detecção**: LED fica **AZUL** quando câmera Flock é detectada
   - **Botão**: Pressione para reescanear manualmente ou resetar

4. **Uso Portátil**:
   - Conecte ao banco de energia USB (5000mAh = ~20 horas)
   - Coloque no porta-copo, bolsa ou bolso
   - LED visível através do gabinete translúcido

5. **Conexão com Painel** (opcional):
   - Conecte o dispositivo ao computador via USB-C
   - Instale o painel FlockYou conforme instruções da STS Collective
   - Veja detecções ao vivo na interface do navegador

**Aviso**: *Este é um firmware proprietário. Regravar com versões open-source excluirá permanentemente o firmware STS.*

---

### Guia de Configuração 3: Placa Multimodo OUI-SPY

#### Configuração Inicial

1. **Conteúdo da Embalagem**:
   - Placa PCB exposta OUI-SPY
   - Cabo USB-C
   - Guia de início rápido

2. **Primeira Inicialização**:
   - Conecte alimentação USB-C (computador, adaptador de parede ou banco de energia)
   - Dispositivo transmite rede WiFi: `OUISPY-[ID]`
   - Buzzer toca melodia de boot específica do modo

3. **Seleção de Modo WiFi**:
   - Conecte telefone/computador à rede WiFi OUI-SPY
   - Abra o navegador em: `http://192.168.4.1`
   - Interface web exibe 4 modos de firmware:
     1. **Detector** - Scanner BLE com múltiplos alvos
     2. **Foxhunter** - Direcionamento de rádio RF
     3. **Flock-You** - Detecção de câmera ALPR
     4. **Sky Spy** - Detector de RemoteID de drones
   - Selecione o modo desejado e clique em "Activate"

4. **Operação do Modo Flock-You**:
   - Dispositivo reinicializa no modo Flock-You
   - Buzzer toca melodia de inicialização Flock-You
   - Começa a varredura em busca de 31 OUIs conhecidos
   - **Alerta de detecção**: Buzzer emite padrão único
   - Último modo lembrado entre ciclos de energia

5. **Troca de Modos**:
   - Segure o **botão BOOT** por 2 segundos
   - Dispositivo retorna ao seletor de modo WiFi
   - Reconecte ao WiFi e escolha novo modo

#### Avançado: Antena Externa

6. **Troca de Antena** (para alcance estendido):
   - Por padrão: Usa antena cerâmica integrada
   - Conecte antena MMCX ao conector MMCX
   - Firmware alterna automaticamente para antena externa
   - Use antena direcional/Yagi para detecção de longo alcance

#### Instalação

7. **Instalação em Veículo/Fixo**:
   - *Sem gabinete incluído, PCB exposto precisa de proteção antes da instalação*
   - Opções:
     - Imprimir gabinete personalizado em 3D
     - Montar com velcro no painel
     - Usar fita dupla face
     - Caixa de projeto DIY
   - Mantenha a porta USB-C acessível para alimentação

#### Exportação de Dados (Modo Flock-You)

8. **Wardriving GPS**:
   - Conecte módulo GPS externo (não incluído)
   - Dispositivo registra detecções com coordenadas
   - Baixe arquivos de dados via interface web
   - Formatos de exportação: JSON, CSV, KML

**Nota**: Verifique colonelpanic.tech para atualizações de firmware e documentação específica do OUI-SPY Unified Blue.

---



______

## Guia de Compra e Informações de Fornecedores

### Fornecedores Autorizados

#### Colonel Panic Tech (colonelpanic.tech)

**Produtos Oferecidos**:
- **OUI-SPY** ($85): Dispositivo de detecção Flock pronto para uso
- **Kits DIY** ($55): Componentes + PCB + guia de montagem
- **Complemento Módulo GPS** ($18): Módulo GPS-6M compatível
- **Acessórios**: Antenas, gabinetes, upgrades de bateria

**Por que Comprar da Colonel Panic**:
- ✅ Diretamente do desenvolvedor do hardware OUI-SPY
- ✅ Firmware mais recente pré-instalado
- ✅ Suporte técnico incluído
- ✅ Ética open-source (esquemas disponíveis)
- ✅ Fórum de comunidade ativo

**Frete**:
- EUA Doméstico: 3-5 dias úteis
- Internacional: 7-14 dias úteis
- Frete grátis em pedidos >$100

**Garantia**: Garantia de hardware de 90 dias, atualizações de firmware vitalícias

**Site**: [https://colonelpanic.tech](https://colonelpanic.tech)

---

#### STS Collective (stscollective.com)

**Produtos Oferecidos**:
- **M5 Atom Lite Pré-gravado** ($39.99): Dispositivo de detecção Flock pronto para uso
- **Acessórios**: Compatíveis com várias plataformas ESP32

**Por que Comprar da STS Collective**:
- ✅ Dispositivos pré-gravados prontos para uso
- ✅ Garantia de qualidade e testes
- ✅ Preços acessíveis
- ✅ Suporte ao cliente

**Frete**:
- EUA Doméstico: 2-4 dias úteis (Correio Prioritário)
- Internacional: 7-21 dias úteis
- Opções expresso disponíveis

**Garantia**: Garantia padrão em hardware

**Site**: [https://stscollective.com](https://stscollective.com)

> 💰 **Desconto para Leitores**: Use o código **SIMEONONSECURITY** para até 20% de desconto em produtos STS Collective — [stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### Outras Fontes para M5 Atom Lite

**Loja Oficial M5Stack**:
- Site: [shop.m5stack.com](https://shop.m5stack.com)
- Preço: $9.95 para Atom Lite exposto
- Acessórios: Módulos de bateria, sensores Grove, gabinetes
- Frete: Internacional, 7-14 dias

**Amazon**: Busque "M5Stack Atom Lite"
- Preço: ~$12-15 (varia por vendedor)
- Frete Prime disponível
- Opções de pacote com acessórios

**Adafruit**: [adafruit.com](https://adafruit.com)
- Varejista de eletrônicos curado
- Excelentes recursos de aprendizado
- Frete rápido baseado nos EUA

**Nota**: *Ao comprar um M5 Atom Lite exposto, o firmware deve ser instalado separadamente seguindo o guia DIY acima. A versão pré-gravada da STS Collective é um produto diferente.*

### Resumo de Comparação de Preços

| Dispositivo | Preço Base | Complementos Opcionais | Investimento Total | Tempo de Configuração |
|--------|------------|------------------|------------------|------------|
| **DIY ESP32** | $5-12 | Gabinete 3D, bateria | $5-20 | 15-30 min |
| **M5 Atom Lite** | $39.99 | Banco de energia $10 | $40-50 | Plug-and-play |
| **OUI-SPY** | $85 | Antena externa $20, gabinete | $85-115 | Plug-and-play |

______

## Usando Seu Dispositivo de Detecção: Cenários Práticos

### Cenário 1: Mapeamento do Trajeto Diário

**Objetivo**: Documentar localizações de câmeras Flock ao longo de suas rotas regulares.

**Configuração**:
- Use dispositivo com capacidade GPS (DIY ESP32 com módulo GPS ou OUI-SPY com GPS)
- Ative o registro automático
- Monte no veículo ou carregue no bolso
- Defina a sensibilidade como MÉDIA para reduzir falsos positivos

**Procedimento**:
1. Inicie o dispositivo de detecção antes de partir
2. Dirija sua rota normal
3. Dispositivo alerta quando câmeras Flock são detectadas
4. Coordenadas GPS registradas automaticamente
5. Retorne para casa e exporte os dados
6. Importe GPX/CSV no software de mapeamento
7. Crie mapa pessoal de localização de câmeras

**Benefícios**:
- Consciência da cobertura de vigilância em suas rotas
- Identifique rotas alternativas sem câmeras
- Contribua para projetos de mapeamento comunitário
- Acompanhe mudanças de implantação ao longo do tempo

### Cenário 2: Avaliação de Vigilância no Bairro

**Objetivo**: Determinar a cobertura de câmeras Flock em sua área residencial.

**Configuração**:
- Use dispositivo portátil (M5 Atom Lite, DIY ESP32 ou OUI-SPY)
- Levantamento a pé ou de bicicleta
- Monitoramento estacionário em cruzamentos principais

**Procedimento**:
1. Caminhe/pedale pelas ruas do bairro
2. Pare em cada cruzamento por 30-60 segundos
3. Anote as detecções no mapa
4. Use a intensidade do sinal para estimar distância/direção
5. Confirme visualmente as localizações das câmeras quando possível
6. Documente descobertas com fotos (de áreas públicas)

**Resultado**:
- Mapa completo da infraestrutura de vigilância local
- Evidências para organização comunitária
- Dados para solicitações de registros públicos
- Consciência para decisões pessoais de privacidade

### Cenário 3: Avaliação de Privacidade em Viagens

**Objetivo**: Entender a exposição à vigilância ao viajar.

**Configuração**:
- Leve dispositivo compacto (M5 Atom Lite no bolso ou DIY ESP32)
- Ative o registro contínuo
- Revise os dados após a viagem

**Casos de Uso**:
- Consultas médicas: Avalie vigilância perto de clínicas
- Consultas jurídicas: Verifique cobertura da área do escritório do advogado
- Serviços religiosos: Entenda o monitoramento perto de locais de culto
- Atividades políticas: Avalie vigilância em eventos/protestos
- Situações domésticas: Identifique se a residência é monitorada

### Cenário 4: Advocacia Comunitária

**Objetivo**: Fornecer dados para debates políticos e conscientização pública.

**Aplicações**:
- Apresentar descobertas em reuniões da câmara municipal
- Incluir em solicitações de registros públicos
- Compartilhar com organizações de advocacia de privacidade
- Contribuir para projetos de pesquisa
- Informar associações de bairro

**Apresentação de Dados**:
- Criar mapas de calor mostrando densidade de câmeras
- Gerar relatórios sobre disparidades de cobertura
- Produzir linhas do tempo de expansão de implantação
- Correlacionar com estatísticas de criminalidade (ou a ausência delas)

______

## Análise Técnica Detalhada: Entendendo o Código

### Algoritmo Central de Detecção (Simplificado)

Para os interessados na implementação técnica, aqui está uma visão simplificada da lógica de detecção:

```cpp
// Flock-You Detection Core (Conceptual - not full code)

// OUI Database (31 known Flock-associated OUIs)
const uint8_t FLOCK_OUI_LIST[][3] = {
    {0xD4, 0xAD, 0xFC}, // Espressif ESP32-S3
    {0xAC, 0x67, 0xB2}, // Espressif ESP32-WROOM
    {0x84, 0xF3, 0xEB}, // Espressif ESP32-S3 variant
    // ... 28 more OUIs ...
};

// Promiscuous mode callback
void wifi_sniffer_callback(void* buf, wifi_promiscuous_pkt_type_t type) {
    wifi_promiscuous_pkt_t *pkt = (wifi_promiscuous_pkt_t*)buf;
    
    // Extract MAC address from frame
    uint8_t *mac = pkt->payload + 10; // addr2 field position
    
    // Check against OUI database
    for (int i = 0; i < NUM_OUIS; i++) {
        if (memcmp(mac, FLOCK_OUI_LIST[i], 3) == 0) {
            // OUI match found
            int rssi = pkt->rx_ctrl.rssi;
            
            // Check signal strength threshold
            if (rssi > RSSI_THRESHOLD) {
                // Analyze frame for additional signatures
                if (is_wildcard_probe_request(pkt)) {
                    // High confidence detection
                    trigger_alert(mac, rssi, HIGH_CONFIDENCE);
                } else {
                    // OUI match only
                    trigger_alert(mac, rssi, MEDIUM_CONFIDENCE);
                }
            }
        }
    }
}

// Wildcard probe detection
bool is_wildcard_probe_request(wifi_promiscuous_pkt_t *pkt) {
    // Management frame, subtype probe request
    if ((pkt->payload[0] & 0x0F) != 0x04) return false;
    
    // Check for empty SSID IE (wildcard)
    // Position depends on frame structure
    uint8_t *ie = &pkt->payload[24]; // Start of IEs
    if (ie[0] == 0x00 && ie[1] == 0x00) {
        return true; // Wildcard probe
    }
    return false;
}
```

### Conceitos Técnicos Chave Explicados

**Modo Promíscuo**: Em vez de receber apenas quadros endereçados ao seu dispositivo, o ESP32 captura todos os quadros WiFi no alcance. **Isso é essencial para detectar dispositivos próximos que não estão se comunicando com seu detector.**

**Estrutura do Endereço MAC**: Cada quadro WiFi contém múltiplos endereços MAC:
- `addr1`: Endereço do receptor
- `addr2`: Endereço do transmissor (contém OUI)
- `addr3`: Endereço do destino/fonte final

**RSSI (Received Signal Strength Indicator)**: Intensidade do sinal em dBm (decibéis negativos relativos a 1 miliwatt). Valores típicos:
- -30 dBm: Extremamente forte (muito próximo)
- -50 dBm: Sinal forte
- -70 dBm: Fraco, mas utilizável
- -90 dBm: Muito fraco (borda do alcance)

**Solicitações de Sonda**: Dispositivos WiFi enviam solicitações de sonda para descobrir redes disponíveis. *Sondas curinga (SSID vazio) procuram qualquer rede, o que é comum em dispositivos IoT como câmeras Flock, tornando-as confiavelmente detectáveis.*

______

## Solução de Problemas Comuns

### Problema: Nenhuma Detecção Apesar de Câmera Conhecida Próxima

**Possíveis Causas**:
1. **Câmera offline/desligada**: Câmeras Flock ficam temporariamente inativas às vezes
2. **Sinal bloqueado**: Materiais de construção absorvem WiFi (metal, concreto)
3. **Fora do alcance**: Alcance efetivo ~30-90 metros dependendo de obstáculos
4. **Problema de firmware**: Firmware desatualizado perde variantes OUI mais recentes

**Soluções**:
- Confirme que a câmera está visível e parece operacional (painéis solares, luzes)
- Aproxime-se da localização suspeita da câmera
- Tente diferentes orientações de antena
- Atualize para o firmware Flock-You mais recente
- **Verifique se o dispositivo está ativamente escaneando** (verifique atividade LED/display)

### Problema: Excesso de Falsos Positivos

**Possíveis Causas**:
1. **Alta densidade de dispositivos ESP32**: Dispositivos de casa inteligente e IoT são comuns
2. **Sensibilidade muito alta**: Detectando dispositivos distantes/irrelevantes
3. **Outras câmeras de vigilância**: Muitas usam módulos ESP32

**Soluções**:
- Reduza a configuração de sensibilidade
- Ative detecção de sonda curinga (maior confiança)
- Verifique fisicamente as detecções antes de registrar
- Use a intensidade do sinal para filtrar (alerte apenas em sinais fortes)
- Atualize o banco de dados OUI para focar em OUIs Flock confirmados

### Problema: Bateria Descarrega Rapidamente

**Possíveis Causas**:
1. **Varredura contínua**: Sem gerenciamento de suspensão/energia
2. **Display sempre ligado**: Tela consome energia significativa
3. **GPS ativo**: Módulos GPS consomem muita energia
4. **Bateria velha**: Baterias Li-Po degradam com o tempo

**Soluções**:
- Ative o modo de varredura passiva (intermitente vs. contínua)
- Defina tempo limite do display
- Desative GPS quando o mapeamento não for necessário
- Substitua a bateria (OUI-SPY/mesh-detect v2 têm baterias substituíveis)
- Use banco de energia externo para sessões prolongadas

### Problema: GPS Não Adquire Bloqueio

**Possíveis Causas**:
1. **Uso interno**: GPS requer visibilidade do céu
2. **Antena não conectada**: mesh-detect v2 precisa de antena externa conectada
3. **Inicialização a frio**: Primeiro bloqueio GPS leva 5-15 minutos
4. **Interferência**: Eletrônicos próximos interferem com o sinal

**Soluções**:
- Mova para posição com visão clara do céu
- Certifique-se de que a antena está corretamente conectada (conector SMA)
- Aguarde o bloqueio inicial (bloqueios subsequentes são mais rápidos)
- Afaste-se de fontes de interferência RF
- Verifique se o GPS está ativado nas configurações

### Problema: Dados Não Registrando no Cartão SD

**Possíveis Causas**:
1. **Cartão SD não formatado**: Deve estar no formato FAT32
2. **Cartão SD cheio**: Sem espaço disponível
3. **Cartão não detectado**: Não inserido completamente
4. **Corrupção do sistema de arquivos**: Cartão danificado

**Soluções**:
- **Formate o cartão SD como FAT32** (máximo 32GB para compatibilidade)
- Exclua logs antigos ou use cartão maior
- Reinsira o cartão completamente (deve travar)
- Reformate o cartão ou substitua se danificado
- Verifique se o dispositivo reconhece o cartão (menu mostrará status SD)

______

## Considerações Legais e Éticas

### Status Legal dos Dispositivos de Detecção

**Legalidade da Varredura WiFi**:
- ✅ **Legal nos EUA**: Monitoramento WiFi passivo (somente recepção) é legal
- ✅ **Sem interceptação**: Dispositivos apenas monitoram quadros transmitidos publicamente
- ✅ **Sem descriptografia**: Não tentam descriptografar dados ou conectar-se a redes
- ✅ **Semelhante a scanners de rádio**: Status legal comparável a scanners policiais

**Distinções Importantes**:
- ❌ **Ilegal**: Bloqueio ativo/interferência na operação da câmera
- ❌ **Ilegal**: Tentativa de hackear ou acessar sistemas de câmeras
- ❌ **Ilegal**: Destruir ou adulterar câmeras físicas
- ⚠️ **Área cinzenta**: *Algumas jurisdições têm leis de privacidade mais rígidas. Verifique as regulamentações locais antes do uso.*

**Recomendação**: **Dispositivos de detecção são apenas para conscientização. Não interfira na operação das câmeras.**

### Diretrizes de Uso Ético

**Uso Responsável**:
- ✅ Use para consciência pessoal de vigilância
- ✅ Documente para advocacia e discussões de políticas
- ✅ Compartilhe dados agregados com organizações de privacidade
- ✅ Contribua para projetos de mapeamento comunitário
- ✅ Eduque outros sobre infraestrutura de vigilância

**Evite**:
- ❌ Usar dados para facilitar atividades ilegais
- ❌ Assediar proprietários que instalaram câmeras
- ❌ Invadir propriedades para confirmar localizações de câmeras
- ❌ Ações de vigilantismo contra infraestrutura de vigilância

### Considerações de Privacidade

**Privacidade dos Seus Dados**:
- **Dispositivos de detecção registram SUA localização** (via GPS)
- Armazene esses dados com segurança
- **Esteja ciente do risco de intimação** se envolvido em processos legais
- Considere criptografia para arquivos de log sensíveis
- Entenda as políticas de privacidade do fornecedor para dispositivos conectados à nuvem

**Respeitando os Outros**:
- Seja criterioso ao usar dispositivos de detecção em espaços privados
- Não use para rastrear outros indivíduos
- Considere as implicações éticas do compartilhamento de dados

______

## Comunidade e Desenvolvimento Open Source

### Contribuindo para o Projeto Flock-You

O projeto Flock-You prospera com contribuições da comunidade:

**Repositório GitHub**: [github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)

**Formas de Contribuir**:
1. **Descoberta de Novo OUI**: Envie OUIs de câmeras Flock recém-identificados
2. **Melhorias de Código**: Envie pull requests para aprimoramentos de firmware
3. **Designs de Hardware**: Compartilhe designs personalizados de dispositivos de detecção
4. **Documentação**: Melhore guias de configuração, traduções
5. **Testes**: Relate bugs, verifique funcionalidade em diferentes dispositivos
6. **Mapeamento**: Contribua para bancos de dados crowdsourced de localizações de câmeras

### Recursos da Comunidade

**Fóruns e Discussões**:
- **Reddit**: r/privacy, r/privacytoolsIO, discussões ativas
- **Discord**: Servidor Colonel Panic Tech, chat em tempo real
- **GitHub Issues**: Suporte técnico e solicitações de recursos

**Artigos de Pesquisa**:
- Estudos acadêmicos sobre vigilância ALPR
- Avaliações de impacto à privacidade
- Análises legais da legalidade de dispositivos de detecção

**Organizações de Advocacia**:
- **Electronic Frontier Foundation** (EFF): Rastreamento ALPR
- **ACLU**: Vigilância e direitos de privacidade
- **Grupos locais**: DeFlockJoplin e iniciativas comunitárias similares

### Roteiro de Desenvolvimento Futuro

**Recursos Planejados** (do GitHub do projeto):
- **Aprendizado de máquina**: Reconhecimento de padrões para maior precisão
- **Sincronização em nuvem**: Banco de dados opcional de detecção crowdsourced
- **Aplicativos móveis**: Integração com smartphones para interfaces aprimoradas
- **Modos de detecção adicionais**: Outras tecnologias de vigilância
- **Alertas em tempo real**: Notificações push via celular/WiFi

______

## Conclusão: Promovendo a Privacidade por meio da Tecnologia

O **projeto de detecção Flock-You** representa uma poderosa democratização da tecnologia de contra-vigilância. Por menos do que o custo de uma assinatura mensal de streaming, os indivíduos ganham consciência da infraestrutura de vigilância ao seu redor. Seja você escolher a **construção DIY ESP32 ($5-12)**, o **M5 Atom Lite pronto para uso ($40)** ou o **OUI-SPY multimodo ($85)**, você está investindo em consciência de privacidade e autonomia digital.

### Pontos Principais

✅ **Democratização open-source**: Desenvolvimento impulsionado pela comunidade garante acessibilidade
✅ **Tecnologia acessível**: Hardware de nível consumidor (ESP32) torna a detecção acessível
✅ **Múltiplas plataformas**: Opções para diferentes orçamentos e níveis de habilidade técnica
✅ **Desenvolvimento ativo**: Atualizações regulares com novas assinaturas OUI e recursos
✅ **Legal e ético**: O monitoramento passivo está em conformidade com as leis de comunicações
✅ **Benefício comunitário**: Contribui para a conscientização pública e discussão de políticas

### Próximos Passos

1. **Saiba mais** sobre por que a detecção importa: [Vigilância por Câmeras Flock Safety: Prevalência e Preocupações com Privacidade](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)
2. **Escolha sua plataforma**: Decida qual dispositivo atende às suas necessidades e orçamento
3. **Peça o hardware**: Compre de fornecedores autorizados
4. **Configure**: Siga os guias detalhados neste artigo
5. **Junte-se à comunidade**: Envolva-se com outros usuários, compartilhe descobertas, contribua com melhorias
6. **Tome medidas**: Use seus dados para advocacia, conscientização e decisões informadas

A proliferação de vigilância ALPR representa uma mudança significativa na dinâmica de privacidade. Tecnologias de contra-vigilância como Flock-You oferecem uma capacidade crucial: **consciência**. Quando entendemos o alcance e a escala da vigilância, tomamos decisões informadas sobre nossos movimentos, nossa advocacia e nossas expectativas de privacidade em espaços públicos.

**A tecnologia permitiu a vigilância generalizada. A tecnologia também ajuda aqueles que valorizam a privacidade.** O projeto Flock-You é um testemunho do poder da colaboração open-source na proteção das liberdades civis.

______

## Artigos Relacionados

| Artigo | Descrição |
|---------|-------------|
| **[Vigilância por Câmeras Flock Safety: Prevalência, Preocupações com Privacidade e Estratégias de Proteção](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | O guia definitivo para a rede ALPR da Flock Safety, abusos documentados, recursos de organização comunitária e o que você pode fazer para se proteger |
| **[Flock Finder: Mapeie Cada Câmera Flock Safety Suspeita Próxima a Você](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Como usar a ferramenta open-source Flock Finder para visualizar mais de 40.000 câmeras Flock suspeitas em todo o mundo usando dados WiGLE e impressão digital OUI |
| **[Como Gravar o Rayhunter em Dispositivos de Detecção de Capturadores IMSI](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Guia passo a passo para gravar o firmware Rayhunter para detectar capturadores IMSI e stingrays, complementando a detecção ALPR |
| **[Firmware Personalizado DagShell para o Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Guia completo para instalar o DagShell no Orbic RCL400 para monitoramento avançado de rede celular e detecção de capturadores IMSI |
| **[Comparação de Dispositivos Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Comparação lado a lado de dispositivos suportados pelo Rayhunter para ajudá-lo a escolher o hardware certo para seu kit de ferramentas de contra-vigilância |

______

## Referências

1. [Repositório GitHub Flock-You - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Flock Finder - Mapa Interativo de Câmeras ALPR](https://simeononsecurity.github.io/flock-finder/)
3. [Flock Finder - Repositório GitHub](https://github.com/simeononsecurity/flock-finder)
4. [Colonel Panic Tech - Fornecedor Oficial](https://colonelpanic.tech)
5. [STS Collective - M5 Atom Lite Pré-gravado](https://stscollective.com)
4. [Documentação Oficial M5Stack](https://docs.m5stack.com/en/core/atom_lite)
5. [Documentação Técnica Espressif ESP32](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
6. [Tutorial do Modo Promíscuo WiFi](https://esp32developer.com/wifi-promiscuous-mode)
7. [Pesquisa da Comunidade DeFlockJoplin](https://deflockjoplin.org/)
8. [Electronic Frontier Foundation - ALPR](https://www.eff.org/issues/automated-license-plate-readers)
9. [Download Oficial do Arduino IDE](https://www.arduino.cc/en/software)
10. [Documentação Platform.io](https://docs.platformio.org/)
11. [Banco de Dados OUI - Padrões IEEE](https://standards.ieee.org/products-programs/regauth/)
12. [Referência de Estrutura de Quadros 802.11](https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/)

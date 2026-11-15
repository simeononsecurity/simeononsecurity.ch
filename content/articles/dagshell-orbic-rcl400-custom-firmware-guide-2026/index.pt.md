---
title: "Firmware personalizado DagShell para Orbic RCL400: guia de 2026"
date: 2026-05-28
lastmod: 2026-11-15
toc: true
draft: false
description: "Guia técnico do firmware DagShell para Orbic RCL400, com instalação, ferramentas de privacidade, wardriving e limites de pesquisa."
genre: ["Firmware personalizado", "Segurança móvel", "Ferramentas de privacidade", "Segurança de rede", "Wardriving", "Testes de penetração", "Hacking de IoT", "Pesquisa de segurança", "Hacking de hardware", "Tecnologia de privacidade"]
tags: ["DagShell", "Orbic RCL400", "Firmware personalizado", "Hacking de hotspot", "Ferramentas de privacidade", "Correção TTL", "Falsificação de MAC", "Detecção de IMSI catcher", "Wardriving", "Rastreamento GPS", "Ataque Evil Twin", "Portal cativo", "Sniffer DNS", "Scanner ARP", "Scanner de portas", "Companion para Raspberry Pi", "Segurança Wi-Fi", "Hotspot móvel", "Monitoramento de rede", "Testes de penetração", "Pesquisa de segurança", "Varredura Bluetooth", "Ataque de desautenticação", "Varredura Wi-Fi", "Consulta OUI", "Envio para WiGLE", "Monitoramento de torres celulares", "Comandos AT", "Gerenciador de firewall", "Bloqueio de anúncios", "Criptografia TLS", "Integração com RayHunter", "STS Collective", "Laboratório de segurança móvel", "Análise de rede", "Firmware de privacidade", "Segurança de código aberto", "Compilação cruzada ARM", "Linux embarcado", "Kit de ferramentas de segurança", "Ferramentas de hacker", "Red team", "Reconhecimento de rede"]
canonical: "https://simeononsecurity.com/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/"
cover: "/img/cover/dagshell-orbic-rcl400-custom-firmware-guide-2026.webp"
coverAlt: "Ilustração de um hotspot móvel Orbic RCL400 com uma interface verde iluminada e representações abstratas de ferramentas de segurança, como gráficos e mapas, sobre um fundo azul-marinho escuro."
coverCaption: ""
---

**Transforme seu Orbic RCL400 em um laboratório móvel de pesquisa de segurança**

## Introdução: um hotspot para hackers

**DagShell** é um firmware personalizado de código aberto para o **hotspot móvel Orbic RCL400**. Ele transforma um dispositivo celular comum em um **kit portátil de pesquisa de segurança e privacidade**. Criado pelo pesquisador de segurança "dag", este firmware com estilo de terminal oferece **ferramentas de hacking, recursos de privacidade e recursos de monitoramento de rede** em uma interface elegante, com estética de hacker em verde e preto.

Este guia completo aborda:
- **O que é o DagShell** e quais são seus recursos
- Instruções de instalação **passo a passo**, pelo web flasher e pelo método manual
- Explicações detalhadas de **todas as ferramentas e capacidades**
- Configuração do **Raspberry Pi Companion** para ampliar os recursos
- **Por que combinar o DagShell com o RayHunter** para obter uma solução móvel completa de segurança
- **Casos de uso reais** para pesquisadores de segurança e defensores da privacidade
- **Considerações legais e éticas**

**Em resumo**: DagShell + RayHunter no Orbic RCL400 = **laboratório móvel completo de segurança** para detectar IMSI catchers, fazer wardriving, analisar redes e proteger a privacidade.

**Dispositivos com firmware pré-instalado disponíveis**: Este artigo tem o patrocínio da **STS Collective**, que oferece hotspots Orbic RCL400 com o **RayHunter e o DagShell** pré-instalados e prontos para uso: [stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)

> 💰 **Desconto exclusivo para leitores**: Economize até 20% em produtos STS Collective, incluindo dispositivos Orbic RCL400 com firmware pré-instalado. Use o código **SIMEONONSECURITY** no checkout ou [compre com o desconto aplicado](https://stscollective.com/discount/SIMEONONSECURITY).

______

## O que é o DagShell?

### Visão geral

**DagShell** é um firmware personalizado de código aberto que substitui a interface web padrão do Orbic RCL400 por um **kit completo de ferramentas de segurança**, que inclui:

- **Interface em estilo de terminal** com arte ASCII e estética hacker
- Interface web **criptografada com TLS 1.2 ou superior** (certificado autoassinado)
- **Ferramentas de proteção da privacidade** (mascaramento de TTL, falsificação de MAC e bloqueio de anúncios por DNS)
- **Monitoramento de rede** (conexões ativas, tabelas de roteamento e consultas DNS)
- **Ferramentas de hacking** (detecção de IMSI catchers, varredura de portas e descoberta por ARP)
- **Recursos de ataque** (Evil Twin AP, phishing por portal cativo e ataques de desautenticação)
- **Rastreamento GPS e wardriving** com exportação CSV compatível com WiGLE
- **Raspberry Pi Companion** para GPS, varredura Bluetooth e reconhecimento de redes Wi-Fi
- **Acesso ao sistema de arquivos** com gerenciador de arquivos no navegador
- **Funções de SMS** por comandos AT
- **Persistência**: inicia automaticamente com o sistema

### Especificações técnicas

**Plataforma**: hotspot móvel Orbic RCL400\
**Arquitetura**: Linux ARM (kernel 3.18)\
**Linguagem**: C/C++ (binário ARM estático)\
**Criptografia**: TLS 1.2 ou superior com certificados autoassinados (PKI de dois níveis)\
**Servidor web**: servidor HTTPS embarcado personalizado (porta 8443)\
**Interface**: interface de terminal acessada pelo navegador\
**Licença**: MIT (código aberto)\
**GitHub**: [github.com/dagnazty/DagShell](https://github.com/dagnazty/DagShell)

### Design visual

O DagShell tem uma **estética hacker retrô**:
- **Logotipo em arte ASCII** em todas as páginas
- **Esquema de cores verde e preto** (estilo Matrix)
- **Fonte monoespaçada** (Fira Code)
- **Efeitos de linhas de varredura** e texto brilhante
- **Layout inspirado em terminais**

{{< figure src="dagshell-orbic-rcl400-hacker-terminal-interface-feature-overview.webp" alt="Firmware personalizado DagShell em execução no Orbic RCL400, com interface de terminal verde e preta, arte ASCII e menu de ferramentas de segurança" >}}

______

## Visão completa dos recursos

### 🏠 Painel

**Visão geral do sistema**:
- **Exibição do tempo de atividade**: por quanto tempo o dispositivo está em execução
- **Interface de comandos AT**: controle direto do modem para usuários avançados
- **Status rápido**: endereço IP e estado da conexão

Os **comandos AT** permitem o controle do modem em baixo nível:
```
Exemplos de comandos AT:
AT+CSQ       - Qualidade do sinal
AT+COPS?     - Operadora de rede atual
AT+CREG?     - Estado do registo na rede
AT+CIMI      - Obter IMSI (identidade do assinante)
AT+CGSN      - Obter IMEI (identificador do dispositivo)
```

### 🌐 Ferramentas de rede

**Informações da rede atual**:
- Detalhes do **endereço IP e da interface**
- **Máscara de sub-rede, gateway** e endereço de broadcast
- **Estatísticas da rede** (pacotes enviados e recebidos)

**Visualizador da tabela de roteamento**:
- Exibe todas as rotas de rede
- Informações do gateway padrão
- Mapeamento de interfaces

**Monitor de conexões ativas**:
- Lista em tempo real de **todas as conexões TCP/UDP**
- Endereços IP locais e remotos
- Números de porta e estados de conexão
- Útil para **monitorar com quais sistemas o dispositivo se comunica**

### 🔒 Conjunto de proteção da privacidade

#### Correção de TTL

**Finalidade**: Mascarar o tráfego do hotspot para evitar sua identificação pela operadora.

**Como funciona**:
- Altera para **65** o valor de **Time To Live (TTL)** nos pacotes IP.
- As operadoras detectam o tethering observando as reduções do TTL (telefone = 64, dispositivo conectado por tethering = 63).
- Definir o TTL como 65 faz com que **todo o tráfego pareça local**.

**Caso de uso**: Contornar restrições ou limitações de velocidade impostas pela operadora ao tethering.

**Comandos**:
```bash
# Ative a correção TTL
iptables -t mangle -A POSTROUTING -j TTL --ttl-set 65

# Desative a correção TTL
iptables -t mangle -D POSTROUTING -j TTL --ttl-set 65
```

#### Falsificação de endereço MAC

**Finalidade**: Alterar o endereço MAC do dispositivo para aumentar a privacidade.

**Como funciona**:
- Altera o endereço MAC de **wlan0** (interface Wi-Fi).
- Gera um **endereço MAC aleatório** ou aceita um valor personalizado.
- Torna o dispositivo **difícil de rastrear** entre sessões.

**Caso de uso**: Evitar o rastreamento baseado em MAC pelas redes às quais você se conecta.

**Etapas**:
1. A interface é desativada.
2. O novo endereço MAC é aplicado.
3. A interface é reativada.
4. A conexão é restabelecida.

#### Bloqueio de anúncios por DNS

**Finalidade**: Bloquear anúncios e rastreadores no nível do DNS.

**Como funciona**:
- Modifica o arquivo `/etc/hosts` com uma **lista de bloqueio**.
- Os domínios listados são resolvidos para **127.0.0.1** (localhost).
- Bloqueia anúncios **para todos os dispositivos conectados**.

**Caso de uso**: Bloquear anúncios em toda a rede sem configurar cada dispositivo individualmente.

**Origem da lista de bloqueio**: Domínios comuns de anúncios e rastreamento. A lista pode ser personalizada.

### 📱 Gerenciamento de SMS

**Envio de SMS**:
- Envia mensagens de texto ao modem por **comandos AT**.
- Útil para **notificações remotas** ou testes.

**Visualização de mensagens**:
- Link para a caixa de entrada nativa do Orbic.
- Leitura de mensagens SMS recebidas.

**Comando AT usado**:
```
AT+CMGS="PHONE_NUMBER"
Texto da mensagem aqui^Z
```

### 🔧 Ferramentas de hacking

#### Detector de IMSI catcher

**Finalidade**: Monitorar informações das torres celulares em busca de anomalias que indiquem dispositivos **IMSI catcher/Stingray**.

**Como funciona**:
- Consulta o modem para obter dados da **torre celular**:
  - **Cell ID** (identificador da torre)
  - **LAC** (código de área de localização)
  - **MCC/MNC** (código de país e de rede móvel)
  - **Intensidade do sinal** (RSSI)
  - **Geração da rede** (2G/3G/4G)
- **Registra alterações** para detectar trocas suspeitas de torre.
- **Cria uma referência de base**, estabelecendo quais torres são normais na região.

**Indicadores de detecção**:
- **Troca súbita de torre celular** enquanto o dispositivo está parado
- **Redução para 2G** *(IMSI catchers costumam forçar o uso de 2G para remover a criptografia)*
- Surgimento de um **Cell ID desconhecido**
- **Sinal fraco** de uma torre falsa
- **Reconexões frequentes**

**Integração com RayHunter**: O DagShell oferece **monitoramento de torres celulares**. O RayHunter oferece **detecção dedicada de IMSI catchers** com análise mais sofisticada (consulte a seção abaixo).

#### Scanner de portas

**Finalidade**: Verificar endereços IP de destino em busca de portas abertas.

**Como funciona**:
- **Varredura TCP SYN**: envia pacotes SYN às portas de destino.
- **Detecção por tempo limite**: identifica portas abertas, fechadas ou filtradas.
- **Suporte a intervalos**: verifica uma porta ou um intervalo de portas.

**Casos de uso**:
- **Reconhecimento de rede**
- **Descoberta de dispositivos IoT**
- **Auditoria de segurança** de redes locais
- **Identificação de serviços**

**Comando**:
```bash
# Verifique as portas 1–1000 no alvo
nc -zv -w 2 TARGET_IP 1-1000 2>&1
```

#### Gerenciador de firewall

**Finalidade**: Bloquear ou liberar endereços IP usando iptables.

**Como funciona**:
- Usa **regras do iptables** para DESCARTAR pacotes enviados por ou para IPs especificados.
- As **regras persistentes** sobrevivem a reinicializações se forem salvas.
- Oferece funções de **lista de permissões e lista de bloqueio**.

**Casos de uso**:
- **Bloquear IPs maliciosos**
- **Impedir acessos não autorizados**
- **Controlar ou filtrar o tráfego**
- **Controle parental**

**Comandos**:
```bash
# Bloqueie o IP
iptables -I INPUT -s IP_ADDRESS -j DROP
iptables -I OUTPUT -d IP_ADDRESS -j DROP

# Desbloqueie o IP
iptables -D INPUT -s IP_ADDRESS -j DROP
iptables -D OUTPUT -d IP_ADDRESS -j DROP
```

### ⚔️ Ferramentas de ataque

**AVISO LEGAL IMPORTANTE**: Estas ferramentas servem **SOMENTE para testes de segurança autorizados**. Na maioria das jurisdições, usá-las contra redes que você não possui ou para as quais não tem autorização explícita por escrito é **ILEGAL** (Computer Fraud and Abuse Act nos EUA, Computer Misuse Act no Reino Unido, entre outras leis). Use-as apenas **nas suas próprias redes** ou em **ambientes de laboratório controlados**.

#### Sniffer DNS

**Finalidade**: Registrar consultas DNS dos clientes conectados.

**Como funciona**:
- Registra o tráfego de **iptables** na porta 53 (DNS).
- **Não exige modo promíscuo**.
- Registra todas as consultas DNS dos clientes do hotspot.
- Revela **quais sites e serviços** os clientes acessam.

**Casos de uso** (autorizados):
- **Análise do tráfego de rede**
- **Monitoramento parental** (da própria família)
- **Pesquisa de segurança** nos próprios dispositivos
- **Análise do comportamento de malware**

*Esta ferramenta captura metadados (os domínios visitados) dos clientes conectados. Use-a somente em redes que você possui ou administra.*

#### Scanner ARP

**Finalidade**: Descobrir dispositivos na rede local.

**Como funciona**:
- Envia **solicitações ARP** a todos os IPs da sub-rede.
- Os dispositivos respondem com seus **endereços MAC**.
- A **consulta OUI** identifica o fabricante (Apple, Samsung e outros).
- Cria um **mapa da rede** com os dispositivos ativos.

**Casos de uso**:
- **Inventário da rede**
- **Detecção de dispositivos desconhecidos**
- **Análise de redes BYOD**
- **Descoberta de dispositivos IoT**

**Exemplo de saída**:
```
IP: 192.168.1.50
MAC: A4:83:E7:XX:XX:XX
Vendor: Apple, Inc.

IP: 192.168.1.75
MAC: 2C:54:91:XX:XX:XX
Vendor: Samsung Electronics
```

#### Traceroute

**Finalidade**: Visualizar o caminho de rede até um destino.

**Como funciona**:
- Envia pacotes com o valor de **TTL crescente**.
- Cada salto reduz o TTL e retorna **ICMP Time Exceeded**.
- Revela os **roteadores e o caminho** até o destino.
- Mede o **tempo de ida e volta (RTT)** de cada salto.

**Casos de uso**:
- **Diagnóstico de problemas de rede**
- **Análise de rotas**
- **Diagnóstico de latência**
- **Investigação de peering da operadora**

#### Evil Twin AP

**Finalidade**: Criar um ponto de acesso Wi-Fi falso que imita SSIDs existentes.

**Como funciona**:
- Usa **wlan1** (segunda interface Wi-Fi, se disponível pelo Pi Companion).
- Imita o **SSID e o tipo de criptografia** da rede de destino.
- **Captura clientes** que tentam se conectar.
- Exibe um **portal cativo** para coletar credenciais.

**Cenário de ataque** (ambiente de laboratório):
1. Procure redes Wi-Fi legítimas.
2. Crie um **AP falso** com o mesmo SSID.
3. Use um **ataque de desautenticação** para desconectar os clientes do AP verdadeiro.
4. Os clientes se conectam automaticamente ao **AP falso**.
5. O portal cativo captura as credenciais.

*Detecção: os clientes veem **SSIDs duplicados** se os dois APs estiverem visíveis ao mesmo tempo.*

#### Portal cativo

**Finalidade**: Usar modelos de páginas de phishing para coletar credenciais.

**Modelos incluídos**:
- **Página de login Wi-Fi** (estilo genérico de provedor ou hotel)
- **Páginas de login de redes sociais** (imitações de Facebook, Twitter e Instagram)
- Portais de **login corporativo**
- Páginas de acesso Wi-Fi de **aeroportos e cafeterias**

**Como funciona**:
1. O Evil Twin AP redireciona **todo o tráfego** ao portal.
2. O cliente vê uma **página de login**.
3. O cliente informa as credenciais.
4. As credenciais são **registradas em um arquivo**.
5. O cliente recebe acesso à internet ou vê uma mensagem de erro.

**Objetivo educacional**: Demonstrar os **riscos de engenharia social** e a importância de verificar URLs.

### 📍 Rastreador GPS e wardriving

#### Funcionalidade GPS

**Origem do GPS**: Somente o **Raspberry Pi Companion**.
- *O Orbic RCL400 **não tem GPS integrado**. Sem o Pi Companion, não há dados de localização.*
- O Pi se conecta a um **dongle GPS USB** (chipset U-Blox 7).
- O Pi envia as coordenadas ao Orbic por meio de **arquivos de dados compartilhados**.
- A conversão de **ECEF para latitude/longitude** ocorre automaticamente.

**Exibição no painel**:
- **Latitude/longitude** em graus decimais
- **Altitude** acima do nível do mar
- **Status de fixação GPS** (precisão)
- **Atualização automática** a cada 5 segundos
- **Sem solicitações de geolocalização do navegador** (a API do navegador não é usada)

**Estado GPS compartilhado**:
- Os dados GPS ficam disponíveis para **todos os processos DagShell**.
- O wardriving usa o GPS automaticamente.
- Não há conflitos entre os recursos.

#### Modo wardriving

**Finalidade**: Examinar redes Wi-Fi com coordenadas GPS para criar mapas.

**Como funciona**:
1. Aguarda uma **fixação GPS válida** (não registra coordenadas 0,0).
2. Examina redes Wi-Fi a cada **5 segundos**, em um ciclo contínuo.
3. Registra os dados da rede:
   - **SSID** (nome da rede)
   - **BSSID** (endereço MAC)
   - **Tipo de criptografia** (WPA2, WPA3 ou aberta)
   - **Intensidade do sinal** (RSSI em dBm)
   - **Número do canal**
   - **Coordenadas GPS** (latitude/longitude)
   - **Data e hora**
4. Exporta os dados em formato **CSV compatível com WiGLE**.

**Integração com WiGLE**:
- **WiGLE** (wigle.net) é um projeto global de mapeamento de redes Wi-Fi.
- O CSV do DagShell pode ser **enviado diretamente ao WiGLE**.
- O envio ocorre pelo navegador, na página Files, sem ferramentas externas.
- A contribuição integra o **banco de dados público** de localizações de redes Wi-Fi.

**Casos de uso**:
- **Mapeamento da cobertura Wi-Fi**
- **Levantamento de redes** para provedores de internet
- **Análise da intensidade do sinal**
- **Pesquisa de segurança** (redes abertas e criptografia fraca)
- **Análise baseada em localização**

**Exemplo de formato CSV**:
```csv
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,AltitudeMeters
A1:B2:C3:D4:E5:F6,HomeNetwork,WPA2,2026-05-28 10:30:15,6,-45,40.7128,-74.0060,10
```

{{< figure src="dagshell-wardriving-gps-wifi-network-mapping-wigle-csv-export.webp" alt="Modo wardriving do DagShell mostrando coordenadas GPS e redes Wi-Fi examinadas, com SSID, BSSID, tipo de criptografia e intensidade do sinal registrados em CSV compatível com WiGLE" >}}

### 🥧 Raspberry Pi Companion

O **Raspberry Pi Companion** amplia os recursos do DagShell com **hardware externo**:

#### Requisitos de hardware

**Mínimos**:
- **Raspberry Pi 3B+** ou posterior. *(O Pi Zero não fornece energia USB suficiente para os periféricos.)*
- **Dongle GPS USB** (recomenda-se o chipset U-Blox 7)
- **Fonte de alimentação** *(o Pi precisa de alimentação própria. A porta USB do Orbic não fornece energia suficiente.)*

**Opcionais**:
- **Adaptador Wi-Fi** (segunda interface para fazer varreduras enquanto mantém a conexão)
- **Dongle Bluetooth** (se o Bluetooth interno do Pi tiver sinal fraco)

#### Módulo GPS (U-Blox 7)

**Conexão**: Dongle GPS USB ligado ao Pi\
**Protocolo**: Sentenças NMEA pela serial\
**Conversão**: O Pi converte ECEF para latitude/longitude automaticamente\
**Compartilhamento de dados**: Grava as coordenadas GPS em um **arquivo compartilhado** no Orbic

**Análise de sentenças**:
```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
       |       |          |           |  |  |   |
       Hora  Latitude  Longitude  Estado  Satélites  Altitude
```

#### Varredura Bluetooth (BLE)

**Finalidade**: Descobrir dispositivos Bluetooth próximos.

**Como funciona**:
- Examina **anúncios BLE**.
- Captura **endereços MAC**.
- Faz **consulta OUI** para identificar fabricantes.
- Registra os resultados em **formato CSV**.

**Controle remoto**:
- Inicia e interrompe a varredura pela interface web do DagShell.
- Não é necessário acessar o Pi por SSH.
- Exibe atualizações de status em tempo real.

**Casos de uso**:
- **Rastreamento e contagem de dispositivos**
- **Análise de fluxo de pessoas**
- **Descoberta de dispositivos Bluetooth**
- **Pesquisa de segurança de IoT**

**Exemplo de saída CSV**:
```csv
Timestamp,MAC,RSSI,Name,Manufacturer
2026-05-28 10:30:15,AA:BB:CC:DD:EE:FF,-65,Fitbit Charge,Fitbit Inc.
```

#### Varredura Wi-Fi

**Finalidade**: O Pi examina redes Wi-Fi e envia os dados ao Orbic.

**Vantagem**: A interface dedicada faz a varredura enquanto o **Orbic mantém o hotspot ativo**.

**Como funciona**:
- O Pi usa um **segundo adaptador Wi-Fi** ou o Wi-Fi integrado, se ele não for necessário para conectividade.
- Examina **todos os canais** (1 a 14 em 2,4 GHz e 36 a 165 em 5 GHz, se houver suporte).
- Envia os resultados ao Orbic por meio do armazenamento compartilhado.
- O DagShell registra os dados em um **CSV de wardriving**.

**Coordenação**:
- O Pi e o Orbic **sincronizam** os dados pela marca temporal do GPS.
- Isso evita entradas duplicadas.
- As duas fontes de varredura são combinadas em um único registro.

#### Ataques de desautenticação

**Finalidade**: Desconectar clientes de redes Wi-Fi para testes em laboratório.

**Como funciona**:
- Envia **quadros de desautenticação 802.11**.
- Falsifica o **endereço MAC do AP**.
- O cliente recebe do AP uma solicitação de desconexão.
- O cliente **perde a conexão** e tenta se reconectar.

**Métodos de controle**:
- **Desautenticação única**: um único envio de quadros.
- **Desautenticação contínua**: impede a reconexão (DoS).
- **Controle remoto**: acionado pela página de varredura do DagShell.

**Casos de uso** (autorizados):
- **Remover dispositivos invasores** da própria rede
- **Teste de penetração** com autorização
- **Ataques Evil Twin** em laboratório (forçar clientes a usar um AP falso)

**⚠️ Aviso legal**: Ataques de desautenticação são **ilegais contra redes que não pertencem a você**. Podem violar regras da FCC e resultar em acusações com base na CFAA.

#### Serviço de inicialização automática

**Serviço systemd**: O Pi Companion inicia automaticamente com o sistema.

**Arquivo de serviço** (`/etc/systemd/system/pi-companion.service`):
```ini
[Unit]
Description=DagShell Pi Companion
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/dagshell/pi_companion.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

**Comandos**:
```bash
# Ative a inicialização automática
sudo systemctl enable pi-companion

# Inicie o serviço
sudo systemctl start pi-companion

# Verifique o estado
sudo systemctl status pi-companion
```

#### Banco de dados OUI

**Finalidade**: Consultar o fabricante associado a um endereço MAC.

**Banco de dados**: API baseada em prefixos do [OUI Master Database](https://standards.ieee.org/products-programs/regauth/).

**Como funciona**:
- Extrai os **três primeiros bytes** do endereço MAC (prefixo OUI).
- Consulta a API: `api.example.com/oui/A4:83:E7`.
- Retorna o **nome do fabricante**.

**Exemplo**:
```
MAC: A4:83:E7:12:34:56
OUI: A4:83:E7
Vendor: Apple, Inc.
```

**Integração**: Usado pelo scanner ARP, scanner BLE e wardriving Wi-Fi.

### 📁 Explorador de arquivos

**Finalidade**: Procurar e gerenciar arquivos no dispositivo.

**Localização**: Diretório `/data/` (partição com permissão de gravação).

**Recursos**:
- **Procurar arquivos** e subdiretórios
- **Baixar** arquivos para o computador
- **Excluir** arquivos, após confirmação
- **Ver tamanhos e datas** dos arquivos

**Arquivos comuns**:
- `wardrive_log.csv`: dados de varredura Wi-Fi
- `bluetooth_scan.csv`: dados de dispositivos BLE
- `gps_track.gpx`: trilhas GPS
- `dns_queries.log`: consultas DNS capturadas
- `arp_scan.txt`: lista de dispositivos de rede

**Envio para WiGLE**:
- Envio direto pelo navegador na página Files
- Autenticação com uma conta WiGLE
- Envio do CSV sem precisar baixá-lo primeiro

______

{{< stscollective-ad "rayhunter" >}}

## Guia de instalação

### Pré-requisitos

**Hardware**:
- **Hotspot móvel Orbic RCL400**
- **Computador** (Windows, macOS ou Linux)
- **Cabo USB** (para gravar o firmware diretamente)

**Software**:
- **Python 3** com os módulos `requests` e `cryptography`
- **Navegador web** (Chrome, Firefox, Edge ou Safari)

**Opcional**:
- **Raspberry Pi 3B+** ou mais recente (para GPS e recursos adicionais)
- **Dongle GPS USB** (chipset U-Blox 7)

### Método 1: Web flasher (recomendado)

**Método mais simples**. Não exige linha de comando.

**Etapa 1**: Acesse o DagShell Webflasher.
- URL: [dagnazty.github.io/DagShell/orbic.html](https://dagnazty.github.io/DagShell/orbic.html)

**Etapa 2**: Gere os certificados PKI.
- Clique no botão **"Generate Certificates"**.
- O navegador gera uma **PKI de dois níveis** (CA raiz e certificado do servidor).
- **Baixe os arquivos**: `root.der` e `server.der`.

**Etapa 3**: Ative o shell root no Orbic.
- Conecte-se à rede Wi-Fi do Orbic.
- Digite a **senha de administrador** no formulário web.
- Clique em **"Enable Shell"**.
- A página explora a API do Orbic para abrir um **shell root na porta 24**.

**Etapa 4**: Instale o firmware.
- Clique no botão **"Deploy DagShell"**.
- O script envia:
  - `orbic_app` (binário principal do firmware)
  - `root.der` (certificado raiz)
  - `server.der` (certificado TLS do servidor)
  - `dagshell_boot.sh` (script de persistência)
- A instalação leva **2 a 3 minutos**.

**Etapa 5**: Reinicie o Orbic.
- Desligue e ligue o dispositivo.
- O DagShell inicia automaticamente.

**Etapa 6**: Acesse o DagShell.
- Abra o navegador em `https://192.168.1.1:8443/`.
- Aceite o **aviso de segurança** (o certificado autoassinado é esperado).
- Se solicitado, use as credenciais padrão.

### Método 2: Instalação manual

Para **usuários avançados** que queiram compilar o firmware a partir do código-fonte.

#### Etapa 1: Instalar dependências

**Windows**:
```powershell
# Instale o Python 3
# Baixe de python.org

# Instale os módulos necessários
pip install requests cryptography

# O compilador cruzado ARM está na pasta gcc_win
```

**macOS**:
```bash
# Instale o Homebrew se ainda não estiver instalado
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instale o Python 3
brew install python3

# Instale os módulos necessários
pip3 install requests cryptography

# A cadeia de ferramentas ARM está na pasta gcc_mac
```

**Linux**:
```bash
# Instale o Python 3 e o pip
sudo apt-get update
sudo apt-get install python3 python3-pip

# Instale os módulos necessários
pip3 install requests cryptography

# Instale o compilador cruzado ARM
sudo apt-get install gcc-arm-linux-gnueabihf
```

#### Etapa 2: Clonar o repositório

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell
```

#### Etapa 3: Compilar o firmware

**Windows**:
```powershell
cd orbic_fw_c
python gen_pki.py          # Gere certificados
.\build.ps1                # Compile o firmware
```

**macOS/Linux**:
```bash
cd orbic_fw_c
python3 gen_pki.py         # Gere certificados
./build.sh                 # Compile o firmware, o BearSSL será compilado automaticamente
```

**Resultado**: `orbic_app` (binário ARM estático) e arquivos de certificado DER.

**⚠️ Observação para macOS**: A pasta `gcc_mac/` contém uma toolchain ARM personalizada, criada com **crosstool-ng**, e direcionada aos cabeçalhos do **kernel Linux 3.2** para compatibilidade com o kernel 3.18 do Orbic. *Compiladores ARM padrão do Homebrew são direcionados a kernels mais recentes e **não funcionarão**.*

#### Etapa 4: Ativar o shell root no Orbic

```bash
# Conecte-se ao WiFi do Orbic
# Substitua YOUR_ADMIN_PASSWORD pela senha real

python enable_shell.py YOUR_ADMIN_PASSWORD
```

Isso explora a API web do Orbic para abrir um shell root na **porta 24**.

#### Etapa 5: Instalar o firmware

```bash
python deploy_base64.py
```

O script envia e instala:
- `orbic_app` em `/data/orbic_app`
- Certificados em `/data/root.der` e `/data/server.der`
- Script de inicialização em `/etc/rc.d/dagshell_boot.sh`

**Persistência**: O firmware inicia automaticamente após a reinicialização, por meio do script init.

#### Etapa 6: Reiniciar e acessar

```bash
# Reinicie o Orbic (desligue e ligue a energia ou use SSH)
reboot

# Após reiniciar, acesse o DagShell
# Navegador: https://192.168.1.1:8443/
```

### Aviso sobre o certificado de segurança

Ao acessar o DagShell, você verá um aviso **"Not Secure" ou "Not Trusted"**:

**Navegadores de computador**:
- Clique em **"Advanced"**.
- Clique em **"Proceed to 192.168.1.1 (unsafe)"**.

**Navegadores de celular**:
- Toque em **"Show Details"**.
- Toque em **"visit this website"**.

**Por que isso acontece**:
- O certificado é **autoassinado**, não foi emitido por uma CA confiável como Let's Encrypt.
- O dispositivo não tem o certificado raiz no repositório de certificados confiáveis.
- *Esse comportamento é **esperado** para firmware personalizado e não indica comprometimento.*

**A conexão é segura?**:
- **Sim**. A conexão é **criptografada com TLS 1.2 ou superior**.
- Os dados não podem ser interceptados.
- *O certificado não tem uma cadeia de confiança vinculada a uma CA pública. A criptografia é válida.*

**Opcional**: Instale `root.der` no repositório de certificados confiáveis do dispositivo para remover o aviso.

______

## Configuração do Raspberry Pi Companion

**Opcional, mas altamente recomendado** para obter todos os recursos.

### Configuração do hardware

**Etapa 1**: Obtenha os componentes.
- **Raspberry Pi 3B+** ou mais recente (US$ 35 a 55)
- **Dongle GPS USB** com chipset U-Blox 7 (US$ 15 a 30)
- **Cartão microSD** de 16 GB ou mais para o Pi OS (US$ 10)
- **Fonte de alimentação** para o Pi (US$ 10)

**Etapa 2**: Instale o Raspberry Pi OS.
```bash
# Baixe o Raspberry Pi Imager
# https://www.raspberrypi.org/software/

# Grave o Raspberry Pi OS Lite no cartão SD
# Inicie o Pi e conclua a configuração
```

**Etapa 3**: Conecte o dongle GPS.
- Conecte o GPS USB ao Pi.
- Confira a detecção com `lsusb` (a saída deve mostrar o dispositivo GPS).
- Verifique a porta serial: `ls /dev/ttyUSB*` ou `/dev/ttyACM*`.

### Instalação do software

**Etapa 1**: Clone o repositório DagShell no Pi.

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell/pi_companion
```

**Etapa 2**: Instale as dependências.

```bash
# Atualize a lista de pacotes
sudo apt-get update

# Instale os pacotes necessários
sudo apt-get install python3-serial python3-requests gpsd gpsd-clients

# Instale os módulos Python
pip3 install pyserial gps3 bluetooth pybluez
```

**Etapa 3**: Configure o daemon GPS.

```bash
# Edite a configuração do gpsd
sudo nano /etc/default/gpsd

# Defina a linha DEVICES para a porta serial do GPS
DEVICES="/dev/ttyUSB0"  # Ajuste se necessário

# Reinicie o gpsd
sudo systemctl restart gpsd

# Teste o GPS
cgps -s  # Os dados de satélite devem aparecer após cerca de 30 segundos
```

**Etapa 4**: Configure o Pi Companion.

```bash
# Edite o arquivo de configuração
nano pi_companion/config.py

# Defina o endereço IP do Orbic
ORBIC_IP = "192.168.1.1"
ORBIC_PORT = "8443"

# Defina a porta serial do GPS
GPS_DEVICE = "/dev/ttyUSB0"

# Salve e saia
```

**Etapa 5**: Instale o serviço systemd.

```bash
# Copie o arquivo de serviço
sudo cp pi_companion.service /etc/systemd/system/

# Recarregue o systemd
sudo systemctl daemon-reload

# Ative a inicialização automática
sudo systemctl enable pi-companion

# Inicie o serviço
sudo systemctl start pi-companion

# Verifique o estado
sudo systemctl status pi-companion
```

**Etapa 6**: Verifique a comunicação.

```bash
# Verifique os logs
journalctl -u pi-companion -f

# As coordenadas GPS devem aparecer sendo enviadas ao Orbic
```

### Configuração da rede

**Opção A**: Conexão Wi-Fi

```bash
# O Pi se conecta ao hotspot do Orbic
# Edite a configuração do wpa_supplicant
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

# Adicione uma rede
network={
    ssid="Orbic_SSID"
    psk="PASSWORD"
}

# Reinicie o WiFi
sudo systemctl restart networking
```

**Opção B**: Ethernet USB (recomendado)

- Conecte o Pi ao Orbic com um **cabo USB** (porta USB do Pi à porta USB do Orbic).
- Ative o **modo USB gadget** no Pi.
- O Pi funciona como um **dispositivo Ethernet USB**.
- *É mais confiável que o Wi-Fi para transferências contínuas de dados.*
- O Pi acessa a internet pelo Orbic.

**Configuração do USB gadget**:
```bash
# Edite config.txt
sudo nano /boot/config.txt

# Adicione ao final
dtoverlay=dwc2

# Edite cmdline.txt
sudo nano /boot/cmdline.txt

# Adicione após rootwait
modules-load=dwc2,g_ether

# Reinicie
sudo reboot
```

______

## Por que combinar o DagShell com o RayHunter?

{{< figure src="dagshell-rayhunter-complementary-capabilities.webp" alt="Diagrama lado a lado que compara o wardriving e as ferramentas de ataque a redes Wi-Fi do DagShell com a detecção de anomalias em protocolos celulares do RayHunter. Ambos funcionam no mesmo hotspot Orbic RCL400." >}}

### Recursos complementares

O **DagShell** e o **RayHunter** são ferramentas de segurança **complementares** que abrangem aspectos diferentes da pesquisa de segurança móvel:

| Recurso | DagShell | RayHunter |
|---------|----------|-----------|
| **Detecção de IMSI catchers** | Monitoramento básico de torres celulares | Análise avançada de padrões |
| **Rastreamento GPS** | Sim (pelo Pi) | Sim (pelo modem) |
| **Wardriving Wi-Fi** | Sim | Não |
| **Varredura Bluetooth** | Sim (pelo Pi) | Não |
| **Ferramentas de rede** | Sim (sniffer DNS, scanner ARP e de portas) | Não |
| **Ferramentas de ataque** | Sim (Evil Twin, portal cativo e desautenticação) | Não |
| **Ferramentas de privacidade** | Sim (correção TTL, falsificação de MAC e bloqueio de anúncios) | Mínimas |
| **Banco de dados de torres celulares** | Básico | Abrangente |
| **Análise por IA/ML** | Não | Sim (detecção de anomalias) |
| **Análise de protocolos de operadoras** | Limitada | Aprofundada (SS7/Diameter) |

### Casos de uso combinados

#### 1. **Proteção completa contra IMSI catchers**

**Cenário**: Viagem por uma região com vigilância intensa.

**Contribuição do DagShell**:
- **Monitora mudanças de torre celular** em tempo real.
- **Registra a localização GPS** durante trocas suspeitas.
- **Armazena os dados das torres** para análise posterior.

**Contribuição do RayHunter**:
- **Detecta anomalias em protocolos celulares** com aprendizado de máquina.
- **Inspeciona pacotes SS7/Diameter** para identificar ataques sofisticados.
- Compara os dados com um **banco de torres conhecidas e confiáveis**.

**Resultado combinado**: O DagShell oferece **monitoramento contínuo** e o RayHunter faz uma **análise aprofundada**.

#### 2. **Wardriving com segurança**

**Cenário**: Mapeamento de redes Wi-Fi em uma área urbana.

**Contribuição do DagShell**:
- Faz **varreduras Wi-Fi** com coordenadas GPS.
- Oferece ferramentas de **análise de rede** (intensidade do sinal e criptografia).
- Exporta dados em CSV do **WiGLE** para mapeamento.

**Contribuição do RayHunter**:
- **Rastreia torres celulares** durante o wardriving.
- **Detecta IMSI catchers** enquanto você examina redes Wi-Fi.
- **Avisa se a segurança celular estiver comprometida**.

**Resultado combinado**: Wardriving com **atenção à segurança celular**.

#### 3. **Laboratório de pesquisa de segurança**

**Cenário**: Red team ou teste de penetração.

**Contribuição do DagShell**:
- **Evil Twin AP** para testes de redes Wi-Fi.
- **Portal cativo** para demonstrações de engenharia social.
- **Ataques de desautenticação** para testes de resiliência.
- Ferramentas de **reconhecimento de rede**.

**Contribuição do RayHunter**:
- **Detecta se você está sendo monitorado** durante os testes.
- Fornece **visibilidade da segurança das torres celulares**.
- Ajuda a evitar **contravigilância** durante os testes.

**Resultado combinado**: Ferramentas ofensivas com **visibilidade defensiva**.

#### 4. **Viagens com foco em privacidade**

**Cenário**: Jornalista ou ativista em um ambiente sensível.

**Contribuição do DagShell**:
- **Mascaramento de TTL** para ocultar o tethering.
- **Falsificação de MAC** para aumentar o anonimato.
- **Bloqueio de anúncios** para impedir rastreamento.
- **Monitoramento de IMSI catchers**.

**Contribuição do RayHunter**:
- **Detecção avançada de IMSI catchers**.
- **Detecção de ataques no nível do protocolo**.
- **Alertas de segurança celular**.

**Resultado combinado**: Privacidade máxima com **proteção em várias camadas**.

### Instalação conjunta

**Opção com firmware pré-instalado** (mais simples):
- Compre na **STS Collective**: [Orbic RCL400 com RayHunter e DagShell pré-instalados](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot).
- **Pronto para usar** assim que sai da caixa.
- Os dois firmwares foram **testados e verificados**.
- **Sem complicações de instalação**.

**Instalação por conta própria**:
1. **Instale primeiro o RayHunter** (consulte nosso [guia completo para instalar o RayHunter em dispositivos](/articles/how-to-flash-rayhunter-devices-complete-guide/)).
2. **Depois instale o DagShell**. Os dois podem coexistir.
3. O **RayHunter** usa as portas padrão.
4. O **DagShell** usa a porta 8443.
5. Acesse cada um em uma aba diferente do navegador.

**Sem conflitos**:
- O RayHunter usa as portas **80/443**.
- O DagShell usa a porta **8443**.
- Um não interfere no outro.
- Os dois funcionam **simultaneamente**.

Quer evitar a instalação manual? O **[Orbic RCL400 com RayHunter e DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)** da STS Collective vem pronto para uso. O código de leitor **SIMEONONSECURITY** dá até 20% de desconto na STS Collective.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compre o RCL400 com firmware pré-instalado e economize 20%
{{< /centerbutton >}}

______

## Casos de uso reais

### Caso de uso 1: Pesquisador de segurança

**Perfil**: Testador de penetração que avalia a segurança de redes Wi-Fi.

**Ferramentas DagShell usadas**:
- **Wardriving Wi-Fi** para mapear redes de clientes
- **Scanner ARP** para descobrir dispositivos
- **Scanner de portas** para identificar serviços
- **Evil Twin/portal cativo** para testar a resistência à engenharia social
- **Explorador de arquivos** para extrair resultados

**Fluxo de trabalho**:
1. Dirija ao redor do perímetro das instalações do cliente.
2. Faça wardriving para mapear a cobertura Wi-Fi.
3. Crie um Evil Twin da rede do cliente com autorização.
4. Monitore as tentativas de conexão dos clientes.
5. Prepare um relatório com os dados coletados.

**Integração com RayHunter**: Ajuda a garantir que o pesquisador não esteja sendo vigiado durante a avaliação.

### Caso de uso 2: Defensor da privacidade

**Perfil**: Jornalista em viagem internacional.

**Ferramentas DagShell usadas**:
- **Correção de TTL** para contornar restrições da operadora
- **Falsificação de MAC** para ocultar a identidade do dispositivo
- **Detector de IMSI catchers** para identificar possíveis sinais de vigilância
- **Sniffer DNS** para verificar se os dispositivos não vazam informações
- **Bloqueio de anúncios** para impedir rastreamento

**Fluxo de trabalho**:
1. Ative a correção de TTL antes de usar o dispositivo.
2. Gere um endereço MAC aleatório.
3. Mantenha o detector de IMSI catchers em monitoramento contínuo.
4. Use o bloqueio de anúncios em todos os dispositivos conectados.
5. Registre atividades celulares suspeitas.

**Integração com RayHunter**: Oferece detecção de IMSI catchers mais avançada que o monitoramento básico.

### Caso de uso 3: Administrador de rede

**Perfil**: Administrador de TI responsável por várias instalações.

**Ferramentas DagShell usadas**:
- **Wardriving Wi-Fi** para verificar a cobertura
- **Scanner ARP** para inventariar dispositivos
- **Scanner de portas** para auditorias de segurança
- **Monitor de conexões ativas** para detectar tráfego não autorizado
- **Gerenciador de firewall** para bloquear IPs

**Fluxo de trabalho**:
1. Faça wardriving nas instalações para validar a cobertura Wi-Fi.
2. Use o scanner ARP para descobrir todos os dispositivos da rede.
3. Verifique as portas dos servidores para identificar serviços expostos.
4. Bloqueie IPs maliciosos pelo firewall.
5. Exporte relatórios para a documentação.

**Integração com RayHunter**: Monitora a segurança celular em instalações com dispositivos móveis.

### Caso de uso 4: Pesquisador de segurança de IoT

**Perfil**: Pesquisador que analisa a segurança de dispositivos IoT.

**Ferramentas DagShell usadas**:
- **Scanner ARP** com consulta OUI para identificar dispositivos IoT
- **Scanner de portas** para encontrar serviços abertos
- **Sniffer DNS** para capturar padrões de tráfego de dispositivos IoT
- **Scanner Bluetooth** (Pi) para descobrir dispositivos IoT BLE
- **Traceroute** para analisar a conectividade

**Fluxo de trabalho**:
1. Instale o Orbic e o Pi em um ambiente de teste.
2. Use o scanner ARP para descobrir dispositivos IoT.
3. Verifique as portas em busca de serviços vulneráveis.
4. Faça uma varredura BLE para descobrir dispositivos IoT Bluetooth.
5. Examine o DNS para analisar o comportamento de conexão externa dos dispositivos.
6. Documente as vulnerabilidades.

**Integração com RayHunter**: Ajuda a detectar se os dispositivos IoT têm conectividade celular e monitora anomalias.

{{< figure src="dagshell-rayhunter-combined-mobile-security-research-use-cases.webp" alt="Diagrama com quatro casos de uso reais para DagShell e RayHunter: pesquisador de segurança, defensor da privacidade, administrador de rede e pesquisador de IoT" >}}

______

## Considerações legais e éticas

### Estrutura legal

**Ferramentas como o DagShell estão em áreas jurídicas pouco claras**:

**Usos legais**:
✅ **Suas próprias redes**: Teste seus próprios dispositivos e redes.
✅ **Testes autorizados**: Faça testes de penetração com autorização por escrito.
✅ **Fins educacionais**: Aprenda em ambientes de laboratório isolados.
✅ **Proteção da privacidade**: Use correção TTL e falsificação de MAC no seu dispositivo.
✅ **Pesquisa de segurança**: Pesquise vulnerabilidades e faça divulgação responsável.

**Usos ilegais**:
❌ **Acesso não autorizado**: Ataque redes que não são suas (violação da CFAA).
❌ **Ataques de desautenticação** contra outras redes (violação das regras da FCC e possível crime grave).
❌ **Ataques Evil Twin** contra o público (fraude eletrônica e roubo de identidade).
❌ **Sniffing de DNS** de outras pessoas sem consentimento (interceptação de comunicações).
❌ **Contornar controles de segurança** para cometer fraudes.

### Leis a conhecer

**Estados Unidos**:
- **Computer Fraud and Abuse Act (CFAA)**: Acesso não autorizado a computadores ou redes.
- **Wiretap Act**: Interceptação de comunicações eletrônicas.
- **Regulamentos da FCC**: Interferência em radiofrequência (ataques de desautenticação).

**Reino Unido**:
- **Computer Misuse Act 1990**: Lei semelhante à CFAA.
- **Regulation of Investigatory Powers Act (RIPA)**: Restrições à interceptação.

**União Europeia**:
- **GDPR**: Proteção de dados (varreduras Bluetooth/Wi-Fi podem capturar dados identificáveis).
- *As leis locais variam por país e sua aplicação também muda bastante.*

### Orientações éticas

**FAÇA**:
- ✅ Use em **seus próprios dispositivos** e redes.
- ✅ Obtenha **autorização por escrito** antes de testar os sistemas de terceiros.
- ✅ Faça **divulgação responsável** se encontrar vulnerabilidades.
- ✅ Use para **fins educacionais** em ambientes controlados.
- ✅ Proteja **sua própria privacidade**.

**NÃO FAÇA**:
- ❌ Ataque redes que não são suas.
- ❌ Colete credenciais de desconhecidos.
- ❌ Interfira em infraestruturas críticas.
- ❌ Use as ferramentas com intenção maliciosa.
- ❌ Distribua dados capturados.

### Declaração sobre o uso responsável

O DagShell é uma **ferramenta de pesquisa de segurança e privacidade**. Seus recursos são semelhantes aos de ferramentas profissionais de teste de penetração, como **Kali Linux**, **WiFi Pineapple** e **HackRF**.

**A intenção importa**: As mesmas ferramentas usadas por **hackers mal-intencionados** também são usadas por **profissionais de segurança**. A diferença está em:
- **Autorização** (permissão para testar)
- **Intenção** (melhorar a segurança ou causar danos)
- **Divulgação** (relatar descobertas ou explorá-las)

Use o DagShell de forma **responsável** e **ética**. *Se não souber se uma ação é legal, pare e consulte um advogado antes de continuar.*

{{< figure src="dagshell-legal-ethical-security-research-responsible-use.webp" alt="Estrutura legal e ética para pesquisa de segurança com DagShell, mostrando casos de uso autorizado e não autorizado e as leis relevantes" >}}

______

## Solução de problemas

### Problemas de instalação

**Problema**: `enable_shell.py` não consegue se conectar.

**Soluções**:
- Verifique se você está conectado ao **Wi-Fi do Orbic**.
- Confira se o endereço IP é **192.168.1.1** (padrão).
- Tente novamente a senha de administrador, respeitando maiúsculas e minúsculas.
- Confira se a porta 80 está acessível: `telnet 192.168.1.1 80`.

**Problema**: O envio do firmware falha.

**Soluções**:
- Primeiro, ative o shell root. Confirme que `enable_shell.py` funcionou.
- Verifique a estabilidade da rede. Se possível, use uma conexão com fio.
- Tente `deploy_net.py` em vez de `deploy_base64.py`.
- Confira se há espaço na partição `/data`: `df -h /data`.

**Problema**: O aviso do certificado não desaparece.

**Soluções**:
- *Isso é **normal** com certificados autoassinados. A conexão continua criptografada.*
- Clique em "Advanced" e em "Proceed anyway" a cada acesso.
- **Opcional**: Instale `root.der` no repositório de certificados confiáveis do dispositivo (procedimento avançado).

### Problemas durante a execução

**Problema**: O DagShell não inicia com o sistema.

**Soluções**:
- Confira o script de inicialização: `ls -la /etc/rc.d/dagshell_boot.sh`.
- Verifique se ele é executável: `chmod +x /etc/rc.d/dagshell_boot.sh`.
- Consulte os logs: `logread | grep dagshell`.
- Inicie manualmente: `/data/orbic_app &`.

**Problema**: O GPS não funciona.

**Soluções**:
- Verifique se o **Pi Companion** está em execução: `systemctl status pi-companion`.
- Confira se o GPS recebe sinal dos satélites: `cgps -s` (no Pi).
- Confirme que o dongle GPS está conectado: `lsusb`.
- *Aguarde de 5 a 10 minutos para obter uma fixação GPS a frio. Na primeira inicialização, o GPS demora mais ao ar livre.*

**Problema**: O wardriving não registra dados.

**Soluções**:
- Confirme que o GPS tem fixação antes de iniciar.
- Verifique se há permissão de gravação em `/data`.
- Confira se o arquivo CSV foi criado: `ls -la /data/wardrive_log.csv`.
- Verifique se a interface Wi-Fi está ativa: `ifconfig wlan0`.

**Problema**: O Pi Companion não se comunica com o Orbic.

**Soluções**:
- Verifique a conectividade de rede: `ping 192.168.1.1`.
- Confira se o arquivo de configuração contém o IP correto.
- Confirme que a porta 8443 está aberta: `telnet 192.168.1.1 8443`.
- Consulte os logs do Pi Companion: `journalctl -u pi-companion`.

### Problemas de desempenho

**Problema**: A interface web está lenta ou com atraso.

**Soluções**:
- Limpe o cache do navegador.
- Desative extensões do navegador (bloqueadores de anúncios podem interferir).
- Use uma conexão **com fio** com o Orbic em vez de Wi-Fi.
- Reinicie o DagShell: `killall orbic_app && /data/orbic_app &`.

**Problema**: As varreduras de wardriving demoram demais.

**Soluções**:
- Aumente o intervalo das varreduras nas configurações (menos frequência em troca de melhor desempenho).
- Reduza o número de canais examinados.
- *Um sinal GPS fraco torna as varreduras mais lentas. O sistema aguarda coordenadas válidas antes de registrar os dados.*

{{< figure src="dagshell-troubleshooting-installation-gps-wardriving-common-issues.webp" alt="Fluxo de solução de problemas do DagShell com falhas comuns de instalação, GPS e wardriving, e suas soluções passo a passo" >}}

______

## Configuração avançada

### Personalização do DagShell

**Modificação do código-fonte**:
- Edite os arquivos no diretório `orbic_fw_c/`.
- Recompile com `build.sh` ou `build.ps1`.
- Instale o firmware novamente.

**Adição de páginas personalizadas**:
- O DagShell incorpora o HTML ao código C++.
- Edite `main.cpp` para adicionar rotas.
- Recompile e instale o firmware.

**Certificado personalizado**:
- Gere sua própria PKI com `gen_pki.py`.
- Ou use o **OpenSSL** para criar certificados.
- Substitua `root.der` e `server.der`.

### Integração com outras ferramentas

**Exportação de dados para Wireshark**:
```bash
# Capture o arquivo pcap
tcpdump -i wlan0 -w /data/capture.pcap

# Baixe pelo navegador de arquivos
# Abra no Wireshark no PC
```

**Importação de trilhas GPS para QGIS**:
```bash
# Exporte no formato GPX
python gps_to_gpx.py /data/gps_coords.txt

# Importe no QGIS como camada vetorial
```

**Sincronização com banco de dados externo**:
```python
# Script personalizado para enviar dados de wardrive ao MySQL
import mysql.connector
import csv

conn = mysql.connector.connect(
    host="your_server",
    user="username",
    password="password",
    database="wardriving"
)

with open('/data/wardrive_log.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("INSERT INTO networks (ssid, bssid, lat, lon) VALUES (%s, %s, %s, %s)",
                      (row['SSID'], row['MAC'], row['Latitude'], row['Longitude']))
conn.commit()
```

### Ajuste de desempenho

**Otimização da velocidade de varredura**:
```bash
# Edite o intervalo de varredura wardrive
# Na interface web do DagShell, mude de 5 s para 3 s para acelerar a varredura
# Em troca, o uso de CPU aumenta e algumas redes podem passar despercebidas
```

**Otimização da bateria** (se usar uma bateria externa):
```bash
# Reduza o brilho da tela do Orbic
# Desative os recursos não usados (BT e GPS quando não forem necessários)
# Use o modo de suspensão entre sessões de wardrive
```

______

## Comparação com alternativas

### DagShell versus WiFi Pineapple

| Recurso | DagShell (Orbic RCL400) | WiFi Pineapple |
|---------|------------------------|----------------|
| **Preço** | US$ 60 a 80 + dispositivo | US$ 99 a 299 |
| **Rede celular** | ✅ 4G LTE integrado | ❌ Não (somente Wi-Fi) |
| **GPS** | ✅ Pelo Pi Companion | ⚠️ Pelo dongle USB |
| **Evil Twin** | ✅ Sim | ✅ Sim |
| **Portal cativo** | ✅ Sim | ✅ Sim |
| **Desautenticação** | ✅ Sim (pelo Pi) | ✅ Sim |
| **Wardriving** | ✅ Sim | ✅ Sim |
| **Detecção de IMSI** | ✅ Básica | ❌ Não |
| **Portabilidade** | ✅ Muito portátil | ⚠️ Moderada |
| **Bateria** | ✅ Integrada | ⚠️ Externa necessária |
| **Curva de aprendizagem** | Moderada | Baixa (interface refinada) |

**Vencedor**: DagShell para **segurança celular móvel**, enquanto o Pineapple atende a testes **específicos de Wi-Fi** com uma interface simples.

### DagShell versus Kali Linux no Pi

| Recurso | DagShell | Kali no Pi |
|---------|----------|-----------|
| **Tempo de configuração** | 15 minutos | 2 a 3 horas |
| **Rede celular LTE** | ✅ Integrada | ❌ Exige modem USB |
| **Interface web** | ✅ Sim | ⚠️ Limitada (exige VNC/SSH) |
| **Quantidade de ferramentas** | Cerca de 15 | Mais de 600 |
| **Especialização** | Segurança móvel | Testes gerais de penetração |
| **Portabilidade** | ✅ Cabe no bolso | ⚠️ Exige tela e alimentação |
| **Duração da bateria** | 8 a 10 horas | 2 a 4 horas |

**Vencedor**: DagShell para tarefas **específicas de dispositivos móveis**, enquanto o Kali oferece um **kit abrangente**.

### DagShell versus firmware padrão do Orbic

| Recurso | DagShell | Firmware padrão |
|---------|----------|-----------------|
| **Ferramentas de segurança** | ✅ Abrangentes | ❌ Nenhuma |
| **Recursos de privacidade** | ✅ Sim | ❌ Mínimos |
| **Personalização** | ✅ Totalmente personalizável | ❌ Bloqueado |
| **Wardriving** | ✅ Sim | ❌ Não |
| **GPS** | ✅ Sim (pelo Pi) | ❌ Não |
| **Código aberto** | ✅ Sim | ❌ Proprietário |
| **Suporte** | ⚠️ Comunidade | ✅ Oficial |
| **Estabilidade** | ⚠️ Beta | ✅ Produção |

**Vencedor**: DagShell para **pesquisadores**, enquanto o firmware padrão atende a **usuários comuns**.

______

## Conclusão: o laboratório móvel definitivo

O **DagShell** transforma o simples **hotspot Orbic RCL400** em um **laboratório móvel de segurança** que combina:

✅ **Proteção da privacidade** (mascaramento de TTL, falsificação de MAC e bloqueio de anúncios)\
✅ **Monitoramento de rede** (conexões, DNS e roteamento)\
✅ **Ferramentas de hacking** (detecção de IMSI, varredura de portas e descoberta ARP)\
✅ **Recursos de ataque** (Evil Twin, portal cativo e desautenticação)\
✅ **Wardriving GPS** com integração ao WiGLE\
✅ **Expansão pelo Raspberry Pi** (BLE, Wi-Fi e GPS)\
✅ **Portátil e alimentado por bateria**\
✅ **Código aberto e personalizável**

### Quando combinado com o RayHunter

**RayHunter + DagShell** = **plataforma móvel completa de segurança**:
- O **RayHunter** oferece detecção avançada de IMSI catchers.
- O **DagShell** oferece ferramentas ofensivas e de privacidade.
- Os dois funcionam **simultaneamente** no mesmo dispositivo.
- Os recursos são **complementares**, sem sobreposição.
- Um único **pacote portátil** atende às necessidades de segurança móvel.

### Comece hoje

**Opção 1: Firmware pré-instalado** (mais simples)
- **STS Collective**: [Orbic RCL400 com RayHunter e DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot).
- O dispositivo chega **pronto para uso**.
- Sem complicações de instalação.
- Configuração profissional.

**Opção 2: Instalação por conta própria**
- Siga este guia.
- É **gratuito** se você já tiver um Orbic RCL400.
- Aprenda o processo de instalação.
- Personalize o sistema conforme suas necessidades.

### Leituras relacionadas

- **[Como instalar o RayHunter em dispositivos: guia completo](/articles/how-to-flash-rayhunter-devices-complete-guide/)**: Instale o RayHunter primeiro.
- **[Comparação de dispositivos RayHunter: análise completa](/articles/rayhunter-device-comparison-2026-complete-review/)**: Escolha sua plataforma.
- **[Projeto de detecção Flock-You: guia de hardware contra vigilância](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**: Conheça outras ferramentas de detecção.

### Considerações finais

Seja você **pesquisador de segurança**, **testador de penetração**, **defensor da privacidade** ou **administrador de rede**, o DagShell oferece uma plataforma **portátil, eficiente e acessível** para atividades de segurança móvel.

**Aviso**: Use a ferramenta com responsabilidade. Teste apenas redes e dispositivos que você possui ou para os quais tem autorização explícita por escrito. Respeite a lei e a ética. Bom hacking! 🚀

{{< figure src="dagshell-orbic-rcl400-mobile-security-lab-conclusion-overview.webp" alt="Hotspot Orbic RCL400 com firmware DagShell, usado como laboratório portátil completo de pesquisa de segurança móvel" >}}

______

## Referências

1. [Repositório DagShell no GitHub](https://github.com/dagnazty/DagShell)
2. [Documentação do DagShell](https://dagnazty.github.io/DagShell/)
3. [STS Collective: dispositivos com firmware pré-instalado](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
4. [WiGLE: projeto de mapeamento Wi-Fi](https://wigle.net/)
5. [Computer Fraud and Abuse Act (CFAA)](https://www.law.cornell.edu/uscode/text/18/1030)
6. [Documentação oficial do Raspberry Pi](https://www.raspberrypi.org/documentation/)
7. [Documentação do módulo GPS U-Blox](https://www.u-blox.com/)
8. [Banco de dados OUI: padrões IEEE](https://standards.ieee.org/products-programs/regauth/)
9. [Tutorial do iptables](https://www.netfilter.org/documentation/)
10. [Documentação do OpenSSL](https://www.openssl.org/docs/)

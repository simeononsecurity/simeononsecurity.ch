---
title: "Fundamentos de redes: sub-redes, divisão em sub-redes e projeto de VLAN"
draft: false
toc: true
date: 2023-07-23
lastmod: 2026-11-13
description: "Aprenda os fundamentos de sub-redes, divisão em sub-redes e VLAN para administrar redes com eficiência e reforçar a segurança."
genre: ["Fundamentos de redes", "Divisão em sub-redes", "VLAN", "Gestão de redes", "Segurança de redes", "Endereçamento IP", "Segmentação de rede", "Uso eficiente de recursos", "Desempenho de rede", "IPv4"]
tags: ["fundamentos de redes", "sub-redes", "divisão em sub-redes", "VLAN", "gestão de redes", "segurança de redes", "endereçamento IP", "segmentação de rede", "uso eficiente de recursos", "desempenho de rede", "IPv4", "configuração de sub-rede", "máscaras de sub-rede", "alocação de endereços IP", "comunicação entre VLAN", "portas de switch", "configuração de VLAN", "interfaces VLAN", "conectividade de rede", "redes subdivididas", "domínios de broadcast", "medidas de segurança", "intervalo de endereços IP", "exemplos de sub-rede", "implantação de VLAN", "administração de rede", "configuração de switch", "configuração de roteador", "escalabilidade de rede", "comunicação e transferência de dados", "redes eficientes"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_comp.webp"
coverAlt: "Ilustração simbólica de redes de computadores interligadas com sub-redes e VLAN"
coverCaption: "Redes eficientes: sub-redes e VLAN explicadas de forma simples."
---

## Fundamentos de redes: sub-redes, divisão em sub-redes e projeto de VLAN

### Introdução

No mundo conectado de hoje, as redes de computadores são essenciais para a comunicação e a transferência de dados. Conhecer os fundamentos de redes é útil para profissionais de TI e usuários. Este artigo explica sub-redes, divisão em sub-redes e VLAN, seus objetivos e funcionamento.

## Sub-redes: uma explicação detalhada

### O que é uma sub-rede?

{{< youtube id="nR5xCmXJE5E" >}}

Uma **sub-rede** é uma subdivisão lógica de uma rede IP. Ela permite que o administrador divida uma rede grande em segmentos menores e mais fáceis de gerenciar. Cada sub-rede tem seu próprio intervalo de endereços IP, o que ajuda a usar os endereços disponíveis com eficiência.

### Por que usar sub-redes?

As redes de computadores usam sub-redes por vários motivos:

1. **Segmentação de rede:** As sub-redes dividem uma rede grande em redes menores. Isso melhora o desempenho e reduz o congestionamento.

2. **Mais segurança:** Separar dispositivos em sub-redes diferentes permite aplicar firewalls e listas de controle de acesso para gerenciar o tráfego e reforçar a segurança.

3. **Uso eficiente de recursos:** A divisão em sub-redes melhora a alocação de endereços IP, um recurso limitado no IPv4.

### Como criar sub-redes?

{{< youtube id="LdSAaSHfK3M" >}}

A divisão em sub-redes divide uma rede em sub-redes menores. Siga estas etapas:

1. **Determine os requisitos da rede:** Defina quantas sub-redes e hosts são necessários em cada uma.

2. **Escolha um esquema de endereçamento IP:** Selecione um esquema adequado ao número necessário de sub-redes e hosts.

3. **Calcule as máscaras de sub-rede:** Determine as máscaras conforme o número de sub-redes e hosts necessários.

4. **Atribua endereços IP:** Atribua endereços a cada sub-rede e confirme que pertencem ao intervalo correto.

5. **Teste e verifique:** Teste a conectividade e confira as atribuições de endereços IP.

### Exemplos de divisão em sub-redes

Considere este exemplo simples de divisão em sub-redes:

Suponha que temos o intervalo IP 192.168.0.0/24 e queremos criar quatro sub-redes com o mesmo número de hosts. Podemos dividir a rede assim:

1. **Etapa 1: Determine os requisitos da rede:** Precisamos de quatro sub-redes com o mesmo número de hosts.

2. **Etapa 2: Escolha um esquema de endereçamento IP:** Escolhemos uma máscara /26, que permite 64 endereços por sub-rede.

3. **Etapa 3: Calcule as máscaras de sub-rede:** A máscara /26 é 255.255.255.192.

4. **Etapa 4: Atribua endereços IP:** Atribuímos estes endereços às sub-redes:

   - sub-rede 1: 192.168.0.0/26
   - sub-rede 2: 192.168.0.64/26
   - sub-rede 3: 192.168.0.128/26
   - sub-rede 4: 192.168.0.192/26

5. **Etapa 5: Teste e verifique:** Conferimos a conectividade entre dispositivos de cada sub-rede.

### Tabelas úteis de divisão em sub-redes

#### Tabela de referência para calcular sub-redes

| Máscara de sub-rede | Notação CIDR | Total de endereços IP | Endereços IP utilizáveis |
|-------------|---------------|--------------------|---------------------|
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1,024 | 1,022 |
| /21 | 255.255.248.0 | 2,048 | 2,046 |
| /20 | 255.255.240.0 | 4,096 | 4,094 |
| /19 | 255.255.224.0 | 8,192 | 8,190 |
| /18 | 255.255.192.0 | 16,384 | 16,382 |
| /17 | 255.255.128.0 | 32,768 | 32,766 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /15 | 255.254.0.0 | 131,072 | 131,070 |
| /14 | 255.252.0.0 | 262,144 | 262,142 |
| /13 | 255.248.0.0 | 524,288 | 524,286 |
| /12 | 255.240.0.0 | 1,048,576 | 1,048,574 |
| /11 | 255.224.0.0 | 2,097,152 | 2,097,150 |
| /10 | 255.192.0.0 | 4,194,304 | 4,194,302 |
| /9 | 255.128.0.0 | 8,388,608 | 8,388,606 |
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
| /7 | 254.0.0.0 | 33,554,432 | 33,554,430 |
| /6 | 252.0.0.0 | 67,108,864 | 67,108,862 |
| /5 | 248.0.0.0 | 134,217,728 | 134,217,726 |
| /4 | 240.0.0.0 | 268,435,456 | 268,435,454 |
| /3 | 224.0.0.0 | 536,870,912 | 536,870,910 |
| /2 | 192.0.0.0 | 1,073,741,824 | 1,073,741,822 |
| /1 | 128.0.0.0 | 2,147,483,648 | 2,147,483,646 |
| /0 | 0.0.0.0 | 4,294,967,296 | 4,294,967,294 |

#### Tabela de sub-redes utilizáveis

| Notação CIDR | Número de sub-redes utilizáveis |
|---------------|-------------------------|
| /0 | 1 |
| /1 | 2 |
| /2 | 4 |
| /3 | 8 |
| /4 | 16 |
| /5 | 32 |
| /6 | 64 |
| /7 | 128 |
| /8 | 256 |
| /9 | 512 |
| /10 | 1024 |
| /11 | 2048 |
| /12 | 4096 |
| /13 | 8192 |
| /14 | 16384 |
| /15 | 32768 |
| /16 | 65536 |
| /17 | 131072 |
| /18 | 262144 |
| /19 | 524288 |
| /20 | 1048576 |
| /21 | 2097152 |
| /22 | 4194304 |
| /23 | 8388608 |
| /24 | 16777216 |
| /25 | 33554432 |
| /26 | 67108864 |
| /27 | 134217728 |
| /28 | 268435456 |
| /29 | 536870912 |
| /30 | 1073741824 |
| /31 | 2147483648 |
| /32 | 4294967296 |

#### Tabela de potências de dois

| Potência de dois | Valor |
|--------------|-------|
| 2^32 | 4294967296 |
| 2^31 | 2147483648 |
| 2^30 | 1073741824 |
| 2^29 | 536870912 |
| 2^28 | 268435456 |
| 2^27 | 134217728 |
| 2^26 | 67108864 |
| 2^25 | 33554432 |
| 2^24 | 16777216 |
| 2^23 | 8388608 |
| 2^22 | 4194304 |
| 2^21 | 2097152 |
| 2^20 | 1048576 |
| 2^19 | 524288 |
| 2^18 | 262144 |
| 2^17 | 131072 |
| 2^16 | 65536 |
| 2^15 | 32768 |
| 2^14 | 16384 |
| 2^13 | 8192 |
| 2^12 | 4096 |
| 2^11 | 2048 |
| 2^10 | 1024 |
| 2^9 | 512 |
| 2^8 | 256 |
| 2^7 | 128 |
| 2^6 | 64 |
| 2^5 | 32 |
| 2^4 | 16 |
| 2^3 | 8 |
| 2^2 | 4 |
| 2^1 | 2 |
| 2^0 | 1 |

## VLAN: redes locais virtuais

### O que é uma VLAN?

{{< youtube id="jC6MJTh9fRE" >}}

Uma **VLAN (Virtual Local Area Network)** é um grupo lógico de dispositivos em uma rede, independentemente da localização física. As VLAN criam domínios de broadcast separados e aumentam a flexibilidade, a segurança e a escalabilidade da rede.

### Por que usar VLAN?

As VLAN oferecem vários benefícios para a gestão de redes:

1. **Mais segurança:** As VLAN isolam dados confidenciais e limitam o acesso não autorizado. O tráfego fica contido em segmentos específicos e protege recursos importantes.

2. **Melhor desempenho:** As VLAN separam logicamente o tráfego, reduzem congestionamentos e melhoram o desempenho. O tráfego de broadcast fica limitado à VLAN.

3. **Gestão de rede simplificada:** As VLAN agrupam dispositivos por função, departamento ou outro critério, facilitando a administração e a configuração.

### Configuração de VLAN

A configuração de uma VLAN geralmente segue estas etapas:

1. **Identifique os requisitos da VLAN:** Defina o objetivo e o escopo da implantação. Identifique os dispositivos e a VLAN de cada um.

2. **Atribua IDs de VLAN:** Atribua um ID exclusivo a cada VLAN. Em geral, os IDs vão de 1 a 4094, com alguns valores reservados.

3. **Configure as portas do switch:** Atribua as portas às VLAN adequadas como portas de acesso ou trunk.

4. **Configure interfaces VLAN:** Se a comunicação entre VLAN for necessária, [configure interfaces VLAN](https://simeononsecurity.com/network-plus/ethernet-switching-vlans-port-configurations-security/) em um switch de camada 3 ou roteador.

5. **Teste e verifique:** Teste a conectividade entre os dispositivos de cada VLAN.

### Tabela de VLAN reservadas

| Tags VLAN | Descrição |
|-------------------|----------------------------------------------------|
| VLAN 0 | ID VLAN reservado, não deve ser usado |
| VLAN 1 | VLAN padrão de muitos dispositivos de rede |
| VLAN 2 | VLAN padrão para tráfego de gerenciamento |
| VLAN 3-4 | IDs VLAN reservados |
| VLAN 5 | Reservado para ID VLAN de Token Ring |
| VLAN 6-1001 | IDs VLAN reservados |
| VLAN 1002-1005 | VLANs padrão da Cisco para fins específicos |
| VLAN 1006-1024 | IDs VLAN reservados |
| VLAN 1025-4094 | Reservado para a faixa VLAN estendida |
| VLAN 4095 | ID VLAN reservado, não deve ser usado |

## Conclusão

[Entender sub-redes](https://simeononsecurity.com/articles/networking-basics-what-is-a-switch-router-gateway-subnet-firewall-and-dmz/) e VLAN é essencial para projetar e administrar redes de computadores eficientes. As sub-redes segmentam a rede e melhoram o desempenho e a segurança. As VLAN agrupam dispositivos de forma lógica, aumentando a flexibilidade e facilitando a gestão. Com estas etapas, administradores podem dividir redes e configurar VLAN conforme as necessidades.

Os fundamentos de redes são a base para redes robustas e escaláveis, preparadas para as necessidades atuais de comunicação e transferência de dados.

## Referências

- [Fundamentos de subnetting](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
- [Entender e configurar VLAN](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/12-2/25ew/configuration/guide/conf/vlans.pdf)
- [Padrão IEEE 802.1Q](https://standards.ieee.org/standard/802_1Q-2018.html)

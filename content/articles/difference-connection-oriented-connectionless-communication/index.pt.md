---
title: "Comunicação orientada à conexão e sem conexão"
date: 2023-07-02
lastmod: 2026-11-11
toc: true
draft: false
description: "Conheça as diferenças entre comunicação orientada à conexão e sem conexão, incluindo protocolos, serviços e métodos de roteamento."
genre: ["Tecnologia", "Redes", "Comunicação", "Protocolos", "Ciência da computação", "Transmissão de dados", "Infraestrutura de rede", "Internet", "Tecnologia da informação", "Telecomunicações"]
tags: ["orientada à conexão", "sem conexão", "comunicação", "protocolos", "serviços", "redes", "transmissão de dados", "TCP", "UDP", "métodos de roteamento", "confiabilidade", "eficiência", "controle de fluxo", "recuperação de erros", "latência", "TCP/IP", "infraestrutura de rede", "protocolos da Internet", "protocolos de rede", "aplicações em tempo real", "confiabilidade de rede", "eficiência de rede", "entrega de dados", "latência de rede", "simplicidade de rede", "sobrecarga de rede", "tratamento de erros de rede", "controle de congestionamento de rede", "roteamento de rede"]
cover: "/img/cover/An_illustration_showing_two_devices_connected.webp"
coverAlt: "Ilustração de dois dispositivos conectados por uma conexão confiável e ordenada."
coverCaption: "Comunicação confiável e ordenada: entenda a diferença"
---

## Introdução

Na comunicação de rede, dois métodos comuns são a comunicação orientada à conexão e a comunicação sem conexão. Eles diferem na forma como estabelecem e mantêm a comunicação entre dispositivos. Este artigo explica as principais diferenças, os protocolos, os serviços e os métodos de roteamento.

## Comunicação orientada à conexão

A comunicação orientada à conexão estabelece um link dedicado entre o emissor e o receptor antes da transferência de dados. Esse link permanece ativo durante toda a sessão. Um protocolo conhecido desse tipo é o **Protocolo de Controle de Transmissão (TCP)**.

### Como funciona a comunicação orientada à conexão

Antes de iniciar a transferência de dados, o emissor e o receptor trocam informações de controle para estabelecer a conexão. Essas informações incluem endereços de origem e destino, mecanismos de verificação de erros e dados de sequenciamento.

Depois que a conexão é estabelecida, os dados são transmitidos de forma confiável e ordenada. O TCP garante que os pacotes cheguem ao destino sem perda ou corrupção e na ordem correta. Esse método oferece recursos como controle de fluxo, controle de congestionamento e recuperação de erros, que ajudam a entregar os dados com confiabilidade.

### Vantagens da comunicação orientada à conexão

A comunicação orientada à conexão oferece várias vantagens:

1. **Confiabilidade**: garante a entrega confiável dos dados por meio de uma transmissão sem erros e ordenada.

2. **Recuperação de erros**: o TCP detecta e recupera erros de rede, preservando a integridade dos dados.

3. **Controle de fluxo**: protocolos orientados à conexão impedem que o receptor seja sobrecarregado por dados.

4. **Sequenciamento**: a ordem da transmissão é mantida, para que o receptor receba os dados na sequência correta.

5. **Controle de congestionamento**: o TCP ajusta a taxa de transmissão para evitar congestionamento e manter a estabilidade da rede.

## Comunicação sem conexão

Ao contrário da comunicação orientada à conexão, a comunicação sem conexão não estabelece um link dedicado antes da transferência de dados. Cada pacote é tratado como uma unidade independente e roteado separadamente pela rede. Um exemplo conhecido é o **Protocolo de Datagrama do Usuário (UDP)**.

### Como funciona a comunicação sem conexão

Os pacotes são enviados à rede sem configuração prévia nem confirmação de recebimento. Cada pacote contém as informações necessárias, incluindo os endereços de origem e destino, para ser roteado e entregue de forma independente. Sem o custo de estabelecer e manter uma conexão, esse método costuma ser mais rápido, mas menos confiável que o orientado à conexão.

### Vantagens da comunicação sem conexão

A comunicação sem conexão oferece algumas vantagens:

1. **Eficiência**: sem o custo de estabelecer e manter conexões, os recursos de rede e o processamento são usados com mais eficiência.

2. **Menor latência**: sem a necessidade de estabelecer uma conexão, a latência diminui. O método é adequado a aplicações em tempo real, como streaming de vídeo e jogos on-line.

3. **Simplicidade**: sem configuração e manutenção de conexão, o processo de comunicação fica mais simples e menos complexo.

## Comparação dos métodos de comunicação

Veja as principais diferenças entre comunicação orientada à conexão e sem conexão:

| | Comunicação orientada à conexão | Comunicação sem conexão |
|--------------------|----------------------------------------|---------------------------------------|
| Estabelecimento | Exige uma fase de estabelecimento da conexão | Não exige conexão |
| Confiabilidade | Transmissão confiável de dados | A transmissão não é garantida |
| Ordem | Os pacotes chegam na ordem correta | Os pacotes podem chegar fora de ordem |
| Sobrecarga | Maior devido à configuração da conexão | Menor por não haver conexão |
| Tratamento de erros | Há mecanismos de recuperação de erros | Não inclui mecanismos de recuperação |
| Aplicações | Adequada a aplicações que exigem | Adequada a aplicações em tempo real |
| | entrega confiável e ordenada de dados | com menor latência |

## Roteamento com e sem conexão

O tipo de comunicação também afeta o roteamento em uma rede. Roteamento é a seleção de um caminho adequado para transmitir dados da origem ao destino.

No roteamento orientado à conexão, a infraestrutura de rede estabelece um caminho predeterminado durante a criação da conexão. Esse caminho não muda durante a sessão. O roteamento sem conexão não exige um caminho predefinido. Cada pacote é roteado de forma independente, conforme as condições atuais da rede e as rotas disponíveis.

## Conclusão

A principal diferença é a criação ou não de um link dedicado antes da transferência de dados. A comunicação orientada à conexão, como TCP, oferece confiabilidade, recuperação de erros, controle de fluxo, sequenciamento e controle de congestionamento. A comunicação sem conexão, como UDP, oferece eficiência, menor latência e simplicidade. A escolha depende das necessidades da aplicação. Escolha a comunicação orientada à conexão quando precisar de entrega confiável e ordenada. Use a comunicação sem conexão para aplicações em tempo real que exigem menor latência.

______

## Referências

1. [Protocolo de Controle de Transmissão (TCP) - Internet Engineering Task Force (IETF)](https://tools.ietf.org/html/rfc793)
2. [Protocolo de Datagrama do Usuário (UDP) - Internet Engineering Task Force (IETF)](https://tools.ietf.org/html/rfc768)
3. [Arquitetura da informação - Interaction Design Foundation](https://www.interaction-design.org/literature/topics/information-architecture)
4. [National Institute of Standards and Technology (NIST) - Computer Security Resource Center](https://csrc.nist.gov/)
5. [Internet Engineering Task Force (IETF) - Padrões e protocolos](https://www.ietf.org/standards/)
______

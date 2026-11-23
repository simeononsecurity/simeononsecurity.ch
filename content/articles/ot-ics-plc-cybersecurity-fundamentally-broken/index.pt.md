---
title: "Por que a cibersegurança de OT, ICS e PLC continua falhando"
draft: false
toc: true
date: 2026-06-26
lastmod: 2026-11-22
description: "Entenda por que os controles de segurança de OT ficam atrás do projeto legado, das restrições operacionais e dos caminhos reais de ataque."
tags: ["segurança de OT", "segurança de ICS", "segurança de PLC", "segurança de IoT", "cibersegurança industrial", "segurança de SCADA", "NIST 800-82", "IEC 62443", "NERC CIP", "tecnologia operacional", "infraestrutura crítica", "sensores analógicos", "isolamento de rede", "sistemas legados", "opinião sobre cibersegurança", "sistemas de controle industrial", "SCADA", "Stuxnet", "segurança de sistemas de controle", "segurança ciberfísica", "segurança da cadeia de suprimentos", "cadeia de suprimentos de OT"]
cover: "/img/cover/ot-ics-plc-cybersecurity-fundamentally-broken.webp"
coverAlt: "Ilustração que contrasta um PLC antigo com recursos analógicos e um controlador moderno com recursos de cibersegurança e interfaces digitais, sobre um fundo escuro."
coverCaption: ""
---

Passei tempo suficiente em ambientes industriais para dizer isto com clareza: **a maioria dos programas de cibersegurança de OT, ICS e PLC é teatro**. Eles produzem documentação de conformidade. Não produzem segurança. É na lacuna entre as duas coisas que a infraestrutura crítica é atingida.

Isto não é um ataque a quem redige padrões. **NIST SP 800-82 Rev 3**, **IEC 62443** e **NERC CIP** são documentos tecnicamente sólidos. O problema não está nas orientações. *O problema está nos sistemas aos quais elas são aplicadas.*

## Os sistemas foram feitos para funcionar, não para serem protegidos

**PLCs, sistemas SCADA, sistemas de controle distribuído (DCS) e hardware industrial de IoT legado** foram projetados para uma coisa: funcionar de forma confiável por muito tempo. **A disponibilidade era o único objetivo de projeto que valia discutir.** Confidencialidade, integridade, autenticação e registro de eventos não eram requisitos. Em muitos casos, nem eram conceitos considerados quando esses sistemas foram desenvolvidos.

O NIST SP 800-82 Rev 3 (2023) reconhece isso com franqueza. Ele descreve ambientes OT com *"requisitos singulares de desempenho, confiabilidade e segurança"*, nos quais *"a segurança não pode interferir na operação do sistema"*. Leia de novo. **O principal documento de orientação de segurança para tecnologia operacional reconhece explicitamente que a segurança fica em segundo plano.** Isso não é uma falha do documento. É uma descrição precisa do ambiente.

Não é possível aplicar controle de acesso baseado em funções a um PLC sem o conceito de funções de usuário. Não é possível corrigir o firmware de um equipamento cujo fabricante não existe mais. **Protocolos seriais legados, como Modbus RTU e Profibus DP, não têm autenticação nativa.** Eles transmitem comandos e dados a quem os solicita. Não verificam quem está solicitando.

*As orientações são sólidas. Muitas vezes, os sistemas não têm capacidade de recebê-las.* São problemas diferentes.

## Existem duas categorias muito diferentes de sistemas OT

**PLCs legados dos anos 1980 ao início dos anos 2000** foram projetados para operação isolada e exclusivamente física. Eles executam sistemas operacionais proprietários. Muitas vezes, são administrados por estações de engenharia que também se conectam às redes corporativas. Suas configurações são armazenadas em formatos sem verificação de integridade. Esses sistemas representam uma parcela significativa da infraestrutura instalada em tratamento de água, geração de energia, manufatura e transporte.

**Controladores modernos com recursos de segurança são diferentes.** Siemens, Schneider, Rockwell, Beckhoff e Phoenix Contact já fornecem plataformas com inicialização segura, firmware assinado, controle de acesso baseado em funções, identidade apoiada por TPM e comunicações criptografadas. EtherNet/IP CIP Security, PROFINET Security Class e OPC UA com autenticação são recursos disponíveis no hardware atual.

Não estou desconsiderando a engenharia moderna de segurança OT. O progresso é real. **O problema é que a maioria da base instalada não é moderna.** Quando as pessoas dizem "cibersegurança OT", geralmente descrevem alguém tentando proteger um controlador programável de 20 anos com uma estrutura de cibersegurança escrita em 2023. Essa é a lacuna a que me refiro.

## O que realmente funciona

**Segurança física e isolamento de rede são os controles mais confiáveis disponíveis para ambientes OT legados.** Todas as principais estruturas de segurança de ICS dizem a mesma coisa. A IEC 62443 organiza ambientes OT em zonas de segurança com conduítes definidos. A intenção é exigir que o movimento lateral passe por limites controlados, em vez de atravessar uma rede plana.

O isolamento de rede reduz bastante a superfície de ataque baseada em rede. Não elimina todo o risco. Mídias removíveis, acesso interno, laptops de manutenção, conexões temporárias de engenharia e comprometimento da cadeia de suprimentos são caminhos documentados para sistemas sem exposição à rede. **Stuxnet**, que chegou a instalações iranianas de centrífugas isoladas da rede por meio de unidades USB infectadas, é o exemplo clássico. *O isolamento de rede é necessário. Não é suficiente.*

**O monitoramento humano de parâmetros do processo físico** continua sendo um dos mecanismos de detecção mais confiáveis disponíveis. Um operador treinado que acompanha pressão, temperatura e vazão em tempo real percebe coisas que nenhum sistema de detecção de intrusão verá, pois o IDS não consegue verificar se o valor digital corresponde à realidade física.

Controles que reduzem o risco nos contextos adequados:

- **Diodos de dados** permitem a saída de telemetria sem aceitar conexões de entrada
- **Listas de permissões de aplicativos** em estações HMI restringem o que é executado em máquinas com acesso aos sistemas de controle
- **Plataformas passivas de detecção de anomalias** da Claroty, Dragos e Nozomi analisam o tráfego sem tocar nas comunicações do plano de controle
- **Segmentação de rede** entre zonas OT desacelera o movimento lateral sem exigir isolamento físico completo
- **Princípios de confiança zero**, citados no NIST SP 800-82 Rev 3, acrescentam requisitos de verificação por sessão a algumas arquiteturas OT modernas

*Nenhum desses controles resolve as restrições fundamentais do projeto. Eles reduzem o risco nas bordas de sistemas que nunca foram feitos para isso.*

## Sinais analógicos não podem ser autenticados

**Loops de corrente de 4-20 mA, sinais de 0-10 V, saídas de termopares e leituras de RTD são transmitidos como sinais elétricos variáveis.** O sinal físico não tem mecanismo para verificar autenticidade. Quem colocar o sinal correto no fio será considerado legítimo.

O Stuxnet demonstrou isso concretamente. O ataque manipulou a lógica do PLC executada nos controladores Siemens S7 e, ao mesmo tempo, reproduziu dados normais do processo gravados anteriormente nas interfaces dos operadores. **Os operadores viam telas com leituras normais enquanto as centrífugas eram levadas além de seus limites operacionais.** O engano durou o suficiente para causar danos físicos que pareciam falha de equipamento, não um ataque.

Interferência eletromagnética de cabos de energia, inversores de frequência, raios e aterramento inadequado corrompe medições analógicas durante a operação normal. A IEC 61000 existe por esse motivo. Instalações industriais usam cabos blindados, aterramento correto, filtragem e separação física para lidar com isso.

Dispositivos de campo inteligentes modernos convertem medições analógicas em formato digital internamente antes de transmiti-las por HART-IP, WirelessHART, EtherNet/IP CIP Security ou OPC UA. O hardware moderno oferece comunicações digitais autenticadas no nível do dispositivo. **O fio analógico de 4-20 mA que conecta um transmissor legado a uma entrada de PLC legado não tem autenticação e nunca terá.** Uma parcela significativa da instrumentação instalada ainda usa esse fio.

## Validar sensores é um controle de segurança funcional, não de cibersegurança

Sistemas de segurança de processos usam **votação redundante de sensores**. Uma configuração 2 de 3, na qual dois sensores indicam 230 PSI e um indica 14 PSI, identifica o valor discrepante. Isso oferece resiliência limitada contra a manipulação de um único sensor. *É um controle de engenharia de segurança funcional, não um controle de cibersegurança.*

PLCs padrão não têm validação criptográfica para suas entradas analógicas. Um gerador de sinais conectado ao loop é indistinguível de um transmissor legítimo. O PLC lê a corrente e age com base nela.

**Os sistemas instrumentados de segurança deveriam ser a última linha de defesa independente.** Em 2017, **TRITON** (também conhecido como **TRISIS**) teve como alvo unidades SIS Triconex da Schneider Electric com o objetivo específico de desativar essa camada. Os invasores chegaram ao sistema de segurança pela rede das estações de engenharia. *A independência da camada dependia de uma separação de rede que não foi mantida.*

IEC 62443-3-3, IEC 62443-4-2 e a coordenação com a segurança funcional conforme a IEC 61511 agora refletem essa lição. Durante anos, equipes diferentes trataram segurança de processos e cibersegurança como disciplinas separadas. **TRITON demonstrou na prática o que análises independentes defendiam na teoria:** um invasor que neutraliza o sistema de segurança antes de provocar a condição perigosa remove o último controle que impede consequências físicas.

## A cadeia de suprimentos é um vetor que você provavelmente ignora

**A maioria dos programas de segurança OT se concentra na arquitetura de rede. Muitas invasões OT recentes usaram pontos de entrada que a arquitetura de rede não impede.**

Os riscos da cadeia de suprimentos de OT incluem:

- **Integridade do firmware antes da instalação**, em especial se o hardware chega da fábrica ou do distribuidor com firmware não verificado
- **Sessões de acesso remoto de fornecedores**, que continuam sendo exposições persistentes em locais que dependem do suporte do fabricante
- **Estações de engenharia** conectadas tanto à rede corporativa quanto à rede OT, muitas vezes por conveniência operacional
- A ausência de **listas de materiais de software (SBOMs)** na maioria das implantações OT legadas, o que torna quase impossível rastrear componentes de software
- **Empreiteiros de manutenção** que levam laptops e unidades USB para ambientes operacionais isolados
- **Suporte a atualizações de firmware assinadas**, que a maioria das plataformas antigas não oferece

O NIST SP 800-82 Rev 3 dedica seções específicas às dependências de fornecedores e ao acesso de terceiros. *Se seu isolamento de rede está intacto internamente, mas o fornecedor do equipamento mantém um portal persistente de acesso remoto à rede de engenharia, você não tem uma rede isolada. Tem uma brecha com uma porta controlada por outra pessoa.*

## Proteger sistemas legados custa mais do que deveria

Cada programa de PLC é escrito sob medida para um processo específico. A lógica que opera o sistema de controle de surtos de uma refinaria difere totalmente da lógica de uma sequência de cloração em tratamento de água ou de um regulador de turbina. Não é uma escolha. Os processos físicos são diferentes.

**Proteger sistemas OT legados costuma custar mais do que o previsto** por causa dos requisitos de validação de engenharia, do tempo de inatividade necessário, das limitações de suporte do fornecedor, das lacunas de documentação e dos ciclos de teste que superam as estimativas iniciais. Em alguns casos de hardware sem suporte do fornecedor, o custo de proteção se aproxima ou supera o custo de substituição do sistema.

**A conformidade com NERC CIP para ativos cibernéticos do sistema elétrico de grande porte custa milhões de dólares por ano a cada concessionária.** Uma pesquisa de 2019 da American Public Power Association documentou custos de conformidade muito variados. Concessionárias menores relataram uma carga desproporcional ao seu porte. Muitos sistemas de água e concessionárias menores não estão sujeitos aos requisitos NERC CIP e não têm obrigação de conformidade comparável.

## Os sistemas devem ser substituídos

**Substituir sistemas OT legados é a resposta correta.** Em grandes instalações, isso significa dezenas de milhões de dólares, longos períodos de transição e o risco de codificar incorretamente conhecimentos operacionais complexos durante a migração. São custos e riscos reais.

As orientações da indústria por meio da CISA e da ICS-CERT recomendam aplicar controles compensatórios enquanto o planejamento da substituição avança. É uma resposta racional às restrições. *Em termos simples, reconhece que não é possível obter segurança completa em equipamentos legados. Aplique os controles adequados e planeje a substituição futura.*

**Na prática, muitos desses sistemas continuarão em serviço por décadas.** Esse é um problema de financiamento e política. A comunidade técnica deixou claro o que precisa acontecer. Os orçamentos operacionais e os cronogramas de substituição não acompanharam essa necessidade.

## Adicionar conectividade de rede a sistemas OT costuma piorar as coisas

Muitas organizações adicionaram recursos de acesso remoto e monitoramento a ambientes OT antes isolados. O argumento operacional é simples: a visibilidade remota reduz o tempo de resposta, e o suporte de fornecedores é mais rápido com conexão remota. **A consequência para a segurança é que sistemas isolados, sem superfície de ataque remoto, agora têm uma.**

O **incidente de 2021 na estação de tratamento de água de Oldsmar** ocorreu por uma conexão de acesso remoto do TeamViewer. O invasor alterou as configurações de dosagem de hidróxido de sódio por meio de uma ferramenta legítima de acesso remoto adicionada por conveniência. O **incidente de 2021 da Colonial Pipeline** começou com o comprometimento de uma rede de TI. O operador interrompeu preventivamente as operações do oleoduto OT porque não conseguiu confirmar que a rede OT não havia sido afetada. *O ataque não invadiu diretamente a rede OT. A incerteza sobre uma possível invasão causou a interrupção.*

Adicionar conectividade de rede a sistemas OT legados para obter benefícios operacionais, sem projetar essa conectividade conforme padrões adequados, **gera em muitos casos mais risco do que o benefício justifica**. O Modelo Purdue continua útil como arquitetura de referência, mas o NIST já não o considera suficiente por si só. IIoT moderno, conectividade com nuvem, operações remotas e arquiteturas híbridas exigem um projeto mais deliberado do que apenas segmentar zonas.

## Conformidade com padrões escritos não é segurança

NIST SP 800-82 Rev 3, IEC 62443 e NERC CIP descrevem os controles adequados para esses sistemas. Não estou descartando esses padrões. Estou apontando o que dizem explicitamente: **nem todo sistema OT consegue implementar todos os controles.** As estruturas usam níveis de segurança graduados e disposições de controles compensatórios justamente porque os sistemas abrangidos muitas vezes não conseguem cumprir todos os requisitos.

A lacuna entre o que os padrões descrevem e o que uma implantação legada específica consegue alcançar não é um erro de documentação. Os sistemas não oferecem suporte aos controles. As orientações reconhecem isso. **Concluir uma auditoria de conformidade de OT legado não significa que o ambiente esteja seguro.** Significa que você documentou os controles compensatórios existentes e um auditor os aceitou.

A estrutura de gestão de riscos do NIST deixa claro que há risco residual após a aplicação dos controles. A aceitação de risco é um dos quatro resultados da estrutura, junto com transferência, redução e prevenção do risco. *O reconhecimento do risco residual faz parte das orientações oficiais.* **Quando alguém afirma que cumprir requisitos de conformidade torna seu ambiente OT seguro, está dizendo algo que as próprias estruturas citadas não sustentam.**

## O que fazer com OT legado

Se você opera ambientes OT legados:

- **Trate o isolamento de rede como seu controle principal** e audite tudo que cruza o limite OT
- **Crie um plano de proteção próprio para as estações de engenharia.** Elas conectam os dois ambientes e frequentemente são o ponto de entrada
- **Controle e registre todas as mídias removíveis** nas áreas OT
- **Audite o acesso remoto de fornecedores** e encerre todas as sessões que não estejam em uso
- Implemente monitoramento redundante de sensores quando o projeto do processo permitir
- **Crie um cronograma de substituição com estimativas reais de custo**, mesmo que a troca demore anos
- **Pare de tratar a conclusão da auditoria de conformidade como marco de segurança**

Se você está adquirindo novos sistemas OT:

- **Inclua requisitos de segurança na especificação de aquisição** antes de os fornecedores responderem
- Escolha plataformas com suporte documentado a comunicações autenticadas, atualizações de firmware assinadas e controle de acesso baseado em funções
- **Projete os limites de TI/OT como conduítes explícitos conforme a IEC 62443**, não como uma política vaga de "mantenha-os separados"
- **Exija SBOMs dos componentes de software OT** como entrega contratual

A indústria documentou bem o problema. Os padrões são tecnicamente corretos. *Os sistemas em operação muitas vezes não conseguem receber o que os padrões prescrevem.* Reconhecer isso abertamente é o ponto de partida para decidir como administrar o risco restante.

## Referências

- NIST SP 800-82 Rev 3: Guia de segurança de tecnologia operacional (OT) (2023)
- IEC 62443: série de segurança para sistemas de automação e controle industrial
- IEC 62443-3-3: requisitos de segurança de sistemas e níveis de segurança
- IEC 62443-4-2: requisitos técnicos de segurança para componentes de IACS
- IEC 61511: segurança funcional para sistemas instrumentados de segurança
- NERC CIP: padrões de proteção de infraestrutura crítica para o sistema elétrico de grande porte
- IEC 61000: padrões de compatibilidade eletromagnética
- Alertas e boas práticas de CISA ICS-CERT
- Estrutura MITRE ATT&CK para ICS
- Análise técnica do Stuxnet, Langner Communications, 2011
- Análise técnica de TRITON/TRISIS, Dragos, 2017
- Revisão do incidente da estação de tratamento de água de Oldsmar, CISA, 2021
- Pesquisa de custos de conformidade NERC CIP da American Public Power Association, 2019

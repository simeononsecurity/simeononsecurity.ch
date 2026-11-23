---
title: "Cibersegurança da IA em 2026: implantar rápido, proteger depois"
draft: false
toc: true
date: 2026-06-26
lastmod: 2026-11-23
description: "Avaliação da adoção da IA em cibersegurança, das lacunas operacionais, das orientações atuais e dos controles práticos para organizações em 2026."
tags: ["segurança de IA", "cibersegurança de IA 2026", "injeção de instruções", "agentes de IA", "segurança MCP", "cadeia de suprimentos de IA", "IA não gerenciada", "red teaming de IA", "segurança LLM", "observabilidade de IA", "IA agêntica", "ameaças de IA", "ataques com IA", "segurança de modelos", "governança de IA", "NIST AI 600-1", "OWASP LLM", "MITRE ATLAS", "resposta a incidentes de IA", "segurança de IA corporativa", "identidade de IA", "envenenamento de contexto", "envenenamento de ferramentas", "autorização de IA"]
cover: "/img/cover/state-of-ai-cybersecurity-2026.webp"
coverAlt: "Ilustração de sistemas de IA interconectados representados como nós luminosos em um fundo escuro. Linhas vibrantes mostram as conexões, e sombras ao redor de alguns nós indicam vulnerabilidades de segurança."
coverCaption: ""
---

As organizações implantaram sistemas de IA em 2023, 2024 e 2025 em um ritmo que as orientações defensivas, as ferramentas de segurança e as práticas operacionais não conseguiram acompanhar. **Em 2026, o resultado é uma grande superfície de ataque pouco monitorada, conectada a sistemas reais de negócios, enquanto as defesas ainda estão sendo montadas.**

Quero ser específico sobre o que me preocupa e por quê. Este não é um alerta geral sobre riscos da IA. É uma descrição da superfície de ataque real, das lacunas documentadas e do que as organizações precisam resolver.

## Por que essa lacuna existe

A segurança do software tradicional amadureceu ao longo de cerca de três décadas. Décadas de experiência em resposta a incidentes, pesquisa de vulnerabilidades, desenvolvimento de ferramentas e conhecimento operacional conquistado com esforço produziram as estruturas, os produtos e as práticas que sustentam os programas modernos de segurança.

**A IA generativa empresarial chegou a milhões de implantações em produção em cerca de dois anos.**

As disciplinas que tornam a segurança do software eficaz, como modelagem de ameaças para arquiteturas específicas, padrões de implantação reforçados, procedimentos maduros de resposta a incidentes e práticas estabelecidas de auditoria e observabilidade, não tiveram tempo de se desenvolver antes que as organizações começassem a implantar IA em larga escala. *As orientações chegaram depois da implantação. As ferramentas chegaram depois das orientações. A experiência operacional ainda está se desenvolvendo.*

Isso não é uma acusação. É uma explicação para as lacunas serem estruturais, não acidentais.

## As quatro camadas da segurança de IA

Grande parte da confusão nas discussões sobre segurança de IA vem de tratar documentos de governança, taxonomias de ameaças, orientações de engenharia e controles operacionais como se fossem a mesma coisa. Não são.

**A camada 1 é governança.** NIST AI RMF, ISO/IEC 42001 e EU AI Act atuam no nível organizacional e de processos. Eles descrevem como gerenciar riscos de IA, estruturar a supervisão e documentar responsabilidades. São estruturas de governança, não controles técnicos.

**A camada 2 é taxonomia de ameaças.** MITRE ATLAS documenta táticas adversárias contra sistemas de IA. OWASP Top 10 for LLMs e OWASP Agentic AI Top 10 enumeram classes específicas de ataques. Esses documentos nomeiam os ataques. Não prescrevem defesas.

**A camada 3 é orientação de engenharia.** Google SAIF, Microsoft AI SDL, OWASP AI Exchange e NIST AI 600-1 oferecem orientações para construir e implantar IA com segurança. NIST AI 600-1 é muito mais específico que o AI RMF básico e aborda injeção de prompt, envenenamento de dados e riscos informacionais em implantações de IA generativa.

**A camada 4 é operação.** Monitoramento, resposta a incidentes, controles em tempo de execução, registro, privilégio mínimo, pipelines de avaliação e governança de acesso são práticas operacionais. Exigem processos organizacionais, não apenas documentação.

*A maioria das organizações tem cobertura incompleta nas camadas 3 e 4. Quase todo o risco operacional está ali.*

## O que está em produção

A IA empresarial em 2026 não se resume a chatbots. Os sistemas em produção incluem:

- **Sistemas RAG** que buscam informações em repositórios internos de documentos, wikis, bancos de dados e registros de clientes
- **Agentes de atendimento ao cliente** com acesso a informações de contas e sistemas de gerenciamento de casos
- **Assistentes internos de produtividade** integrados a e-mail, calendários, sistemas de arquivos e plataformas de comunicação
- **Ferramentas de revisão e geração de código** com acesso a repositórios de código-fonte
- **Agentes automatizados** que executam fluxos de trabalho agendados com credenciais para APIs internas
- **Processadores de documentos, contratos e dados financeiros**
- **Modelos de IA incorporados à detecção de fraudes, à contratação e às decisões de controle de acesso**

Cada sistema representa uma superfície de ataque diferente. Um sistema RAG conectado à base de conhecimento interna é, ao mesmo tempo, um risco de divulgação de informações e um alvo de injeção de prompt. **Um agente com acesso ao e-mail e uma credencial persistente é um processo autônomo com influência real sobre sistemas reais.**

*Muitas vezes, as equipes de segurança não participaram da decisão de implantar esses sistemas. Elas descobrem implantações de IA existentes em auditorias, e não em revisões de projeto.*

## A IA agora está dos dois lados

**Os mesmos recursos de IA disponíveis para sua equipe de segurança estão disponíveis para os atacantes.**

**O desenvolvimento assistido por IA** reduz o tempo necessário para transformar divulgações públicas de vulnerabilidades em provas de conceito funcionais e ferramentas operacionais. Qualquer pessoa que use esses recursos, inclusive atacantes, chega mais rápido de uma CVE a um código funcional.

**Conteúdo de phishing gerado por IA** produz e-mails com gramática melhor, contexto mais convincente e menos erros detectáveis do que muitos ataques escritos por pessoas. Os sinais de formatação e os padrões de linguagem que os usuários aprenderam a identificar são menos confiáveis quando a IA gera o conteúdo.

**Clonagem de voz em campanhas de vishing** imita executivos e colegas em chamadas em tempo real. A barreira para a engenharia social direcionada caiu à medida que a síntese de voz melhorou e os custos de acesso diminuíram.

**Vídeos deepfake em fraudes de e-mail corporativo** passaram da teoria para a operação. Desde 2024, foram documentadas em vários setores fraudes financeiras com vídeos de executivos gerados por IA autorizando transações. *O treinamento de conscientização foi criado para outro modelo de ameaça.*

## Injeção de instruções e envenenamento do contexto

**Entender a injeção de prompt é o ponto de partida para entender a segurança de sistemas de IA.**

Um modelo de linguagem segue instruções inseridas em sua janela de contexto. A janela inclui o prompt de sistema, o histórico da conversa, as saídas de ferramentas e os documentos recuperados. **O modelo não consegue distinguir de forma confiável as instruções do desenvolvedor do aplicativo das instruções que um atacante inseriu no conteúdo que o modelo está processando.** Esse é o núcleo da injeção de prompt conforme a definição da OWASP.

A *injeção direta de prompt* ataca diretamente a entrada do modelo. O usuário fornece texto projetado para substituir as instruções do sistema.

A *injeção indireta de prompt* é mais séria em implantações empresariais. O agente RAG recupera um documento da base de conhecimento. Esse documento contém instruções para o agente realizar outra ação. A ferramenta de resumo processa uma página da web com diretivas ocultas. O bot de suporte lê um anexo de cliente que contém instruções. O agente processa essas instruções e age com base nelas.

**Envenenamento de contexto** é uma categoria mais ampla. Atacantes não precisam comprometer seu modelo para comprometer seu sistema de IA. Precisam inserir conteúdo malicioso no contexto do modelo. Isso inclui documentos RAG envenenados, entradas de memória envenenadas, mensagens de e-mail maliciosas processadas pelo agente, PDFs adversariais e páginas da web controladas pelo atacante que um agente de navegação visita. *Isso é diferente do envenenamento do modelo. O modelo está íntegro. O contexto não.*

A defesa em profundidade reduz esse risco. Filtragem de entrada, validação de saída, escopos limitados para ferramentas, execução isolada e aprovação humana para ações importantes ajudam. **Nenhuma dessas defesas elimina a classe de ataque.** OWASP, NIST, Anthropic, OpenAI e Microsoft recomendam abordagens em camadas porque nenhum controle isolado é suficiente.

*Projete considerando que a injeção de prompt terá sucesso em uma porcentagem das entradas. Limite as consequências de acordo.*

## Agentes de IA, limites de permissão e o problema do raio de impacto

Os agentes diferem dos chatbots em um aspecto operacionalmente crítico: **eles executam ações.**

Um agente conectado a e-mail, GitHub, Jira, Slack, Salesforce, AWS e APIs internas é um processo autônomo com acesso aos mesmos sistemas usados pelos funcionários mais conectados. **Uma injeção de prompt bem-sucedida contra esse agente não produz uma resposta de texto indesejada. Produz uma ação indesejada em um sistema real.**

**O raio de impacto de um comprometimento é determinado pelo que o agente pode acessar.** A maioria das implantações atuais de agentes tem acesso muito além do que uma tarefa individual exige. Um agente que precisa ler um tíquete do Jira não deve ter também acesso de gravação à branch principal do GitHub. Um agente que processa solicitações de suporte não deve guardar credenciais do sistema de faturamento.

**A autorização de IA é um problema distinto da autorização do usuário.** Aplicativos tradicionais perguntam se um usuário está autorizado a realizar uma ação. Arquiteturas de agentes precisam perguntar se esse agente está autorizado a realizar esta ação específica para este usuário específico, neste momento e com base no contexto atual. A maioria das implantações atuais de agentes não implementa isso.

**Envenenamento de ferramentas** é diferente de injeção de prompt. Uma ferramenta maliciosa ou comprometida conectada a um agente retorna descrições ou dados projetados para alterar o comportamento do agente. Pesquisadores tratam cada vez mais o envenenamento de ferramentas como uma classe de ataque separada, principalmente em integrações baseadas em MCP.

*Os fluxos de aprovação humana deveriam ser a última barreira para ações importantes de agentes. As organizações também estão descobrindo a fadiga de aprovação. Quando os agentes pedem aprovação frequente para ações rotineiras, os usuários passam a aprovar automaticamente sem analisar a solicitação. A barreira vira uma formalidade.*

## A identidade da IA é um problema de segurança empresarial

**Agentes têm credenciais.** Tokens OAuth, chaves de API, credenciais de contas de serviço e funções de IAM na nuvem aparecem em implantações de agentes de IA. São identidades não humanas com acesso real.

Lacunas específicas nas implantações atuais:

- **As credenciais dos agentes costumam durar muito** e não são rotacionadas em cronogramas comparáveis aos das contas de serviço
- **Os escopos dos tokens de agentes frequentemente são mais amplos** do que as tarefas exigem
- O registro de auditoria das ações realizadas sob identidades de agentes varia bastante
- **O vazamento de credenciais por prompts** é um risco documentado. Um agente que inclui suas chaves de API no contexto ou nas saídas as expõe a qualquer pessoa que leia a saída ou recupere a conversa.
- Agentes que obtêm credenciais adicionais por chamadas a ferramentas criam **cadeias de identidade difíceis de auditar**

*Governe as identidades dos agentes como governa contas de serviço privilegiadas. Isso exige esforço deliberado porque a maioria das ferramentas de governança de identidade não oferece suporte nativo a padrões de identidade de agentes de IA.*

## A memória persistente de agentes cria uma superfície de ataque de longo prazo

**Agentes com memória persistente têm uma superfície de ataque que não existe em sistemas sem estado.**

Um atacante capaz de inserir conteúdo na memória de um agente estabelece uma posição que persiste entre sessões. *O ataque não precisa ter sucesso em uma única interação. A influência acumulada na memória por dias ou semanas molda o comportamento futuro do agente.* Às vezes, isso é chamado de **ataque de longo prazo ou ataque de contexto adormecido**.

Há poucas orientações operacionais para esse risco específico. Organizações que implantam agentes com armazenamento persistente de memória precisam:

- Tratar **armazenamentos de memória como dados de alto valor** que exigem controles de acesso
- **Validar o conteúdo da memória** antes de os agentes agirem com base nele
- Incorporar à arquitetura a capacidade de **auditar e reverter o estado da memória**

## A cadeia de suprimentos de modelos não recebe o mesmo tratamento que a de programas

**Organizações que baixam modelos pré-treinados de repositórios públicos aceitam artefatos executáveis de IA de fontes externas. A análise desses downloads costuma ser menos rigorosa do que a que as mesmas organizações aplicam a pacotes npm, PyPI ou Maven.**

Riscos específicos em repositórios de modelos:

- **Arquivos de modelo PyTorch no formato pickle** executam código Python arbitrário durante o carregamento. Isso foi explorado em ataques documentados à cadeia de suprimentos. **SafeTensors** é o formato projetado especificamente para lidar com esse problema. Prefira-o quando estiver disponível.
- Carregadores de modelos maliciosos que instalam dependências ou executam código de instalação junto com o modelo
- Modelos treinados em **conjuntos de dados envenenados** que geram resultados sutilmente incorretos em determinados contextos
- Modelos com **backdoors incorporados** que são ativados sob condições específicas
- **Agachamento de nomes de repositórios** para distribuir modelos maliciosos sob nomes conhecidos

*Poucas organizações mantêm uma lista de materiais de software que cubra seus sistemas de IA.* A maioria não sabe dizer qual modelo base originou um sistema em produção, qual versão dos dados de treinamento foi usada no ajuste fino ou se os pesos implantados correspondem aos últimos pesos avaliados. Esse nível de rastreabilidade é pré-requisito para uma segurança significativa da cadeia de suprimentos. Hoje, não é comum.

## A IA paralela cria fluxos de dados sem controle

**Contas pessoais de IA para consumidores são o local para onde seus dados vão sem controles.**

ChatGPT Enterprise, Claude Enterprise e Microsoft Copilot para M365 incluem proteções contratuais para dados dos clientes. **Contas pessoais do ChatGPT, Claude, Gemini e serviços de consumo semelhantes não oferecem essas garantias por padrão.**

Funcionários que usam contas pessoais para processar documentos de trabalho transferem estratégias jurídicas, registros de clientes, código-fonte, projeções financeiras, decisões de pessoal e comunicações internas por fluxos que a organização não controla. *As equipes de segurança frequentemente não têm informações precisas sobre o volume dessa atividade ou sobre as categorias de dados envolvidas.*

Seus controles DLP não detectam dados que passam por um navegador até um serviço de IA para consumidores. Suas políticas de retenção não se aplicam ao histórico de conversas em uma plataforma de terceiros. **Suas obrigações regulatórias sob GDPR, HIPAA, SOX e regras setoriais não mudam conforme os dados tenham saído por acidente ou por uma aba do navegador.**

*Descobrir o escopo real antes de criar controles é o primeiro passo necessário. O que você supõe sobre esse problema quase certamente é uma subestimativa.*

## Sistemas de IA vazam dados de formas que aplicativos tradicionais não vazam

**A recuperação excessiva por RAG** retorna documentos a usuários que não deveriam acessá-los. Um funcionário faz uma pergunta. O componente de recuperação retorna um documento de um segmento restrito da base de conhecimento. A resposta inclui informações desse documento. *A falha de controle de acesso aconteceu na camada de recuperação, não na camada do aplicativo.* Muitas implantações de RAG foram criadas sem aplicar permissões por documento que correspondam às do sistema de origem.

**O vazamento do prompt de sistema** revela as instruções operacionais incorporadas ao produto de IA. Trate os prompts de sistema como confidenciais. O vazamento de credenciais por prompts, quando credenciais de agentes aparecem no contexto ou nas saídas do modelo, costuma ser uma exposição mais grave do que apenas o conteúdo do prompt de sistema.

**Falhas de isolamento de IA multi-inquilino** ocorrem quando modelos ajustados com dados de vários clientes expõem informações de um cliente no contexto de outro. Essa é uma categoria de risco documentada para produtos de IA SaaS multi-inquilino.

**A memorização do modelo** faz modelos reproduzirem conteúdo dos dados de treinamento literalmente. O risco não desaparece, principalmente em modelos ajustados com conjuntos de dados privados pequenos ou insuficientemente deduplicados. Organizações que fazem ajuste fino com dados internos sensíveis precisam avaliar o risco de memorização considerando a abordagem e os dados específicos.

## As organizações não têm visibilidade durante a inferência

Programas tradicionais de segurança mantêm cobertura extensa de logs da infraestrutura. **A maioria das implantações de IA não tem cobertura equivalente para os componentes de IA.**

Monitorar um modelo de linguagem ou agente implantado exige telemetria diferente da usada para monitorar um servidor de aplicativos. As organizações precisam coletar:

- **Conteúdo de prompts e saídas** em um formato adequado para revisão de políticas e detecção de anomalias
- **Logs de invocação de ferramentas** por agentes, incluindo nomes de ferramentas, argumentos e respostas
- **Logs de recuperação** de sistemas RAG, incluindo consultas, documentos retornados e decisões de controle de acesso
- **Sinais de classificação** de tentativas de jailbreak e injeção
- **Monitoramento da consistência das saídas** para detectar desvios de comportamento entre versões do modelo
- **Padrões de latência** que podem indicar tentativas de preenchimento do contexto

*Muitas organizações que implantaram IA em 2023 e 2024 têm códigos de status HTTP e métricas de latência. A telemetria necessária para detectar ou investigar um incidente de segurança de IA muitas vezes não existe nesses ambientes. Descobrir isso depois de um incidente é tarde demais.*

## A resposta a incidentes de IA exige procedimentos próprios

**Os procedimentos existentes de resposta a incidentes cobrem endpoints, redes, aplicativos e identidades. Não cobrem cenários específicos de IA.**

Perguntas que a equipe de resposta a incidentes enfrentará e que os procedimentos atuais não resolvem:

- Como determinar se um modelo foi envenenado durante uma execução de ajuste fino
- Como delimitar o raio de impacto de uma injeção indireta bem-sucedida contra um agente com acesso de gravação a vários sistemas
- Como avaliar se dados de treinamento ou ajuste fino foram exfiltrados durante um comprometimento da cadeia de suprimentos
- Como estabelecer uma **linha de base comportamental** de um modelo para comparar com o comportamento após o incidente
- Como responder quando uma atualização de modelo de um provedor terceirizado introduz um comportamento aparentemente intencional, e não acidental
- Como determinar se **a memória de um agente foi manipulada ao longo do tempo**

*Esses cenários exigem preparação antes que ocorram. A telemetria precisa existir antes do incidente. As linhas de base do comportamento do modelo precisam ser documentadas antes de serem necessárias para comparação.*

## Fluxos de avaliação estão se tornando prática padrão de engenharia

A segurança de IA depende cada vez mais de **avaliação estruturada antes da implantação**, e não apenas do monitoramento posterior.

A avaliação de segurança antes da implantação inclui:

- **Testes de injeção de prompt** usando conjuntos de dados de ataques estabelecidos e o caso de uso específico
- **Benchmarking de jailbreaks** com conjuntos publicados de prompts adversariais
- **Avaliação de robustez adversarial** para modelos que tomam decisões com consequências importantes
- **Testes de regressão** entre versões do modelo para identificar mudanças de comportamento
- **Avaliação de políticas** conforme requisitos documentados de uso aceitável
- **Exercícios de red teaming** realizados por pessoas que tentam superar defesas específicas

NIST, CISA, Anthropic, OpenAI, Microsoft e Google esperam cada vez mais essa prática em implantações de alto risco. *Criar pipelines mínimos de avaliação antes de implantações com consequências importantes é mais viável do que muitas organizações supõem.* OWASP AI Exchange e as estruturas de avaliação publicadas pelos principais provedores de IA são bons pontos de partida.

## Seu inventário de ativos de IA provavelmente está incompleto

A gestão tradicional de ativos cobre servidores, endpoints, aplicativos e dispositivos de rede. **Os sistemas de IA introduzem categorias de ativos que a maioria dos inventários ainda não acompanha.**

Um inventário de sistemas de IA precisa incluir:

- Cada **modelo implantado**, incluindo modelos base, variantes ajustadas e modelos de embedding
- Todos os **prompts e instruções de sistema** em operação na produção
- Cada **agente** em execução no ambiente e as ferramentas às quais tem acesso
- Todos os **índices RAG**, incluindo as fontes de dados e os controles de acesso aplicados durante a recuperação
- Todos os **bancos de dados vetoriais** e seu conteúdo
- Cada **servidor MCP ou estrutura de integração equivalente** conectado a qualquer agente
- **Serviços externos de IA** chamados pelos aplicativos, incluindo os dados enviados a cada um

*Não é possível governar o que não foi inventariado. Em 2026, a maioria das organizações que trabalham com segurança de IA está descobrindo ativos cuja existência desconhecia.*

## Onde a defesa realmente está

As ferramentas, estruturas e práticas defensivas para segurança de IA estão se desenvolvendo de forma ativa e significativa. O estágio atual é inicial, mas está melhorando.

**NIST AI 600-1** amplia o AI RMF básico para IA generativa com especificidade operacional muito maior. Organizações que mantêm programas de conformidade de IA devem ler AI 600-1, e não apenas a estrutura básica.

**MITRE ATLAS** fornece documentação de TTPs adversariais para sistemas de IA em formato ATT&CK. A modelagem de ameaças antes da implantação com ATLAS gera requisitos de segurança mais precisos do que trabalhar apenas com estruturas de governança.

**OWASP LLM Top 10** e **OWASP Agentic AI Top 10** oferecem atualmente as orientações públicas mais específicas do ponto de vista operacional. Ambos são mais úteis para profissionais do que a maioria dos currículos formais.

O **red teaming de IA** antes da implantação é cada vez mais esperado em implantações de alto risco por NIST, CISA e grandes provedores de IA. O mercado externo de testes por equipes vermelhas de IA existe e está crescendo para organizações sem capacidade interna.

Produtos de segurança específicos para IA que cobrem monitoramento, guardrails, autorização e aplicação de políticas em tempo de execução estão nos estágios comerciais iniciais. *A categoria existe e vale a pena ser avaliada. Como o mercado é novo, as alegações de marketing frequentemente superam a capacidade demonstrada. Avalie os produtos considerando sua arquitetura de implantação específica, não os cenários descritos pelos fornecedores.*

## O que você deve fazer

**Faça o inventário do que está implantado.** Saiba o que está em execução, quais dados acessa, quais credenciais possui, quais ferramentas chama e quais ações realiza. Esse é o pré-requisito para todo o resto.

**Trate agentes de IA como contas privilegiadas.** Aplique o privilégio mínimo. Limite as credenciais ao acesso mínimo necessário para cada tarefa. Audite o acesso de cada agente e remova o que não é necessário.

**Implemente observabilidade específica para IA antes da implantação**, não depois de um incidente. Registrar prompts e saídas, invocações de ferramentas e recuperações é a telemetria mínima para análise de segurança.

**Avalie sua exposição à IA paralela.** Descubra quais serviços de IA os funcionários usam em tarefas de trabalho. Determine quais categorias de dados passam por contas pessoais. Crie políticas e controles com base nos resultados reais.

**Aplique controles de acesso por documento em sistemas RAG.** Se a camada de recuperação não aplica as regras de acesso dos sistemas de origem, corrija isso antes que ela exponha um documento restrito a um usuário não autorizado.

**Audite sua cadeia de suprimentos de modelos.** Documente cada modelo base em uso. Prefira SafeTensors aos formatos pickle. Aplique aos artefatos de modelo um nível de análise da cadeia de suprimentos comparável ao usado para dependências de software.

**Governe as identidades dos agentes.** Gerencie tokens OAuth e chaves de API de agentes com as mesmas práticas de ciclo de vida, revisão de escopo e rotação aplicadas a contas de serviço privilegiadas.

**Crie agora procedimentos de resposta a incidentes específicos para IA.** Defina antes de um incidente como investigar cenários de IA, quais evidências são necessárias e quais opções de resposta estão disponíveis.

**Avalie antes de implantar IA em contextos de alto impacto.** Comece com estruturas públicas disponíveis se não tiver ferramentas internas.

*Não trate a conformidade de governança como postura de segurança. Estruturas de governança descrevem processos e gestão de riscos. Não descrevem sistemas tecnicamente defensivos. Ambos são necessários.*

## Referências

- NIST AI Risk Management Framework (AI RMF 1.0): estrutura de gerenciamento de riscos de IA, 2023
- NIST AI 600-1: perfil de IA generativa, 2024
- OWASP: 10 principais riscos para aplicativos de modelos de linguagem de grande porte, 2025
- OWASP: 10 principais riscos de IA agêntica
- OWASP AI Exchange
- MITRE ATLAS: panorama de ameaças adversariais a sistemas de IA
- Google Secure AI Framework (SAIF)
- Microsoft AI Security SDL
- CISA: orientações de cibersegurança de IA, 2024
- ISO/IEC 42001:2023 sistemas de gestão de inteligência artificial
- EU AI Act: Regulamento (UE) 2024/1689
- Hugging Face: documentação do formato SafeTensors

---
title: "Melhores harnesses de agentes de IA em 2026: escolha pelo fluxo de trabalho"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Compare Deep Agents, Claude Agent SDK, OpenAI Agents SDK, Pydantic AI, Pi e LangGraph por execução de ferramentas, memória, recuperação e esforço de integração."
genre: ["Inteligência Artificial", "Desenvolvimento de Software", "Segurança de IA"]
tags: ["harnesses de agentes de IA", "melhores frameworks de agentes", "Deep Agents", "Claude Agent SDK", "OpenAI Agents SDK", "Pydantic AI", "agente de código Pi", "LangGraph", "runtime de agente", "chamada de ferramentas", "memória de agente", "gestão de contexto", "execução durável", "permissões de agente", "segurança de agentes de IA", "agentes de IA locais", "avaliação de agentes", "humano no circuito", "comparação de SDKs de agentes", "agentes de produção"]
cover: "/img/cover/ai-agent-execution-components.webp"
coverAlt: "Componentes metálicos modulares ligados a um processador central brilhante por caminhos turquesa e laranja em uma superfície de trabalho escura"
coverCaption: "Ilustração conceitual dos componentes ao redor de um modelo de IA."
---

**Deep Agents é minha primeira opção para um agente geral com modelos configuráveis e gestão de contexto integrada.** Claude Agent SDK se encaixa bem na incorporação do comportamento de execução do Claude Code. OpenAI Agents SDK e Pydantic AI merecem um teste para agentes específicos de aplicações, enquanto Pi favorece um núcleo pequeno e extensível, e LangGraph favorece o controle explícito do fluxo.

**A melhor escolha depende do trabalho que você pretende aceitar.** Um assistente de pesquisa, um editor de repositório e um serviço que processa pedidos de clientes precisam de ferramentas e regras de recuperação diferentes. Estas recomendações são avaliações editoriais baseadas na documentação oficial verificada em **10 de outubro de 2026**, não resultados de um benchmark prático de desempenho.

<!--more-->

## Principais conclusões

- **Escolha primeiro a abstração:** agente montado, SDK de aplicação ou runtime de fluxo.
- **Verifique os limites de execução:** aprovação de ferramentas, isolamento do sistema de arquivos e política de rede resolvem problemas diferentes.
- **Teste a recuperação:** o histórico da conversa sozinho não impede ações externas duplicadas.
- **Meça o trabalho aceito:** inclua falhas, tempo de revisão e infraestrutura na comparação de custos.
- **Mantenha o modelo explícito:** mudar o modelo e o software do agente testa o sistema completo, não somente o software.

## O que um harness fornece

Um **harness de agente** é o software ao redor de uma chamada de modelo. Ele prepara o contexto, expõe ferramentas, executa ações aprovadas, devolve resultados e decide quando continuar ou parar. Conforme a implementação, também gerencia memória, delegação, permissões e recuperação.

Um **modelo** propõe a próxima ação. Uma **ferramenta** realiza uma operação. Um **runtime** executa e preserva o fluxo. Essas responsabilidades se misturam em produtos empacotados, mas separá-las ajuda a identificar capacidades ausentes.

| Componente | Pergunta |
|---|---|
| **Gestão de contexto** | Quais requisitos sobrevivem a uma execução longa? |
| **Execução de ferramentas** | Quem valida argumentos e limita a autoridade? |
| **Armazenamento de estado** | O que sobrevive ao reinício do processo? |
| **Verificação** | Que evidência confirma a conclusão? |

Considere um **agente de suporte ilustrativo** encarregado de verificar um pedido e preparar uma solicitação de substituição. Ler o pedido, propor a substituição e enviá-la devem ter autoridades separadas. Uma explicação convincente não autoriza o envio, e uma transcrição salva não confirma se o envio já ocorreu.

**Escopo:** este guia compara software incorporável e opções de runtime. Para interfaces de desenvolvimento diário, consulte a comparação separada de [agentes de código CLI](/articles/cli-coding-agents-comparison/) ou de [agentes de código GUI](/articles/gui-coding-agents-comparison/). Uma comparação de SDK não deve virar silenciosamente um ranking de ferramentas de terminal contra extensões de editor.

## Lista prática

| Requisito inicial | Primeira opção para avaliar | Responsabilidade principal que fica com você |
|---|---|---|
| **Agente geral** | Deep Agents | Configurar backend, permissões e modelo |
| **Claude Code em um app** | Claude Agent SDK | Operar e isolar o processo de execução |
| **Fluxo de ferramentas da aplicação** | OpenAI Agents SDK | Definir ferramentas, aprovações e aceitação |
| **Aplicação Python tipada** | Pydantic AI e seu pacote Harness | Selecionar capacidades e workspace |
| **Núcleo de código incorporável mínimo** | Pi SDK | Montar extensões e política de execução |
| **Fluxo durável explícito** | LangGraph | Projetar estado do grafo e recuperação |

**Estes são pontos de partida diferentes.** Deep Agents já usa LangGraph, então escolhê-lo não é necessariamente uma decisão excludente. Pydantic AI também separa seu framework central das capacidades montadas do harness. Compare o código da aplicação que você precisa manter, em vez de tratar cada linha como uma biblioteca intercambiável.

**Comece pela menor camada que passe no teste de aceitação.** Use um framework tipado para chamadas de ferramentas limitadas, um agente montado para trabalho aberto com arquivos ou pesquisa, e um grafo explícito quando recuperação e transições precisarem de estados nomeados. Adicione memória, shell ou subagentes somente depois de um teste mostrar por que a camada simples falha.

## Deep Agents: capacidades montadas

**Escolha Deep Agents primeiro para um agente que trabalha com arquivos, ferramentas e conversas longas.** Sua [visão oficial](https://docs.langchain.com/oss/python/deepagents/overview) documenta backends de arquivos, descarregamento de contexto, sumarização, subagentes e aprovação humana. Ele se baseia em LangChain e no runtime LangGraph, com integrações para vários provedores de modelos.

**A configuração ainda determina o comportamento.** A documentação atual informa que o planejamento de tarefas é opcional a partir da versão 0.7. Não presuma que um tutorial antigo descreve os padrões atuais. Registre a versão do pacote e o middleware ativado na avaliação.

**Inspecione o escopo de permissões com cuidado.** As regras documentadas do sistema de arquivos cobrem ferramentas internas de arquivos, não comandos shell arbitrários por backends de sandbox. Negar uma ferramenta de arquivo é insuficiente se outro caminho de execução alcança o mesmo arquivo. Teste o backend e o limite do shell juntos.

**Minha recomendação:** coloque-o na lista curta para um serviço de análise de documentos ou repositórios quando você quiser capacidades montadas e escolha de provedor. Prefira um ponto de partida menor quando o trabalho consistir em duas chamadas de API estreitas e uma resposta validada. Mais ferramentas criam mais comportamento para avaliar.

## Claude: execução incorporada

**Escolha Claude Agent SDK quando quiser colocar o agente do Claude Code dentro da aplicação.** A Anthropic descreve uma biblioteca Python e TypeScript com o mesmo loop de execução, ferramentas e gestão de contexto do Claude Code. O SDK executa o binário do Claude Code em um processo operado por você. Ele é diferente do cliente básico da API da Anthropic e dos Managed Agents hospedados. [Visão geral do Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview).

**A atração é reutilizar um sistema de execução existente.** Operações de arquivo, comandos, hooks, permissões, sessões e subagentes chegam como capacidades documentadas. Sua integração fornece o limite da aplicação e as verificações de aceitação específicas da tarefa.

**O hosting continua sendo uma decisão de engenharia.** O [guia de implantação da Anthropic](https://code.claude.com/docs/en/agent-sdk/secure-deployment) aborda controles de sistema de arquivos, restrições de rede e isolamento. Configure-os ao redor do processo, em vez de tratar um prompt de permissão como limite do sistema operacional.

**Minha recomendação:** avalie-o para automação de documentos ou código centrada no Claude, com trabalho substancial em arquivos e comandos. Escolha uma alternativa flexível entre provedores se comparar modelos locais e vários provedores hospedados for requisito central.

| Opção montada | Ênfase da integração |
|---|---|
| **Deep Agents** | Seleção de modelo, middleware e configuração do backend |
| **Claude Agent SDK** | Execução do Claude Code dentro do processo da aplicação |

## OpenAI: fluxos de ferramentas da aplicação

**Escolha OpenAI Agents SDK para uma aplicação organizada em torno de funções, tarefas delegadas e saídas explícitas.** Sua [visão geral](https://openai.github.io/openai-agents-python/) documenta o loop do agente, handoffs, guardrails, tracing e capacidades de agentes em sandbox. O SDK é uma interface para construtores, distinta do aplicativo de desenvolvimento Codex.

**A aprovação é um comportamento configurável.** O [guia human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/) descreve execuções interrompidas e estado serializado para retomar após uma decisão. Para ferramentas locais de shell e patch, a aprovação é opcional. Adicionar um callback de aprovação sozinho não ativa a exigência de aprovação.

**O suporte a modelos vai além da OpenAI.** A [documentação de provedores](https://openai.github.io/openai-agents-python/models/) descreve pontos de integração com provedores externos e adaptadores. Valide saídas estruturadas, chamadas de ferramentas e suporte de transporte para o endpoint escolhido, em vez de presumir paridade de recursos.

**Minha recomendação:** coloque-o na lista curta para um serviço cujas ações úteis já existam como funções bem definidas da aplicação. Por exemplo, buscar um pedido, calcular elegibilidade em código comum e preparar uma solicitação estruturada. Mantenha autorização e verificações de elegibilidade na aplicação mesmo quando o modelo escolhe a próxima ferramenta.

## Pydantic AI: aplicações tipadas

**Escolha Pydantic AI quando tipos Python e saídas validadas forem centrais para a aplicação.** Sua [documentação principal](https://pydantic.dev/docs/ai/overview/) cobre ferramentas tipadas, injeção de dependência, saídas estruturadas e integrações de execução durável. A validação estabelece a estrutura exigida. Ela não estabelece a verdade de cada campo.

**O pacote Harness separado adiciona capacidades montadas.** Sua [documentação](https://pydantic.dev/docs/ai/harness/) inclui stacks Coder e Researcher, acesso a arquivos e shell, memória e integrações de workspace. Um workspace local e um sandbox isolado são escolhas de execução diferentes. As capacidades relevantes do harness exigem um workspace, em vez de selecionar um silenciosamente.

**Minha recomendação:** coloque o framework central na lista curta para um serviço Python que retorne registros tipados. Adicione capacidades do harness quando a tarefa também exigir exploração do workspace ou pesquisa aberta. Assim, um serviço de extração limitado não herda acesso ao shell sem necessidade concreta.

Para um **agente ilustrativo de revisão de faturas**, a validação do esquema verifica se o total é numérico e se a moeda pertence a um conjunto permitido. A lógica separada da aplicação compara o total com as linhas e verifica evidência da fonte. Ambos os testes pertencem ao ensaio.

| Preocupação da aplicação | Teste de aceitação |
|---|---|
| **Saída estruturada** | Valide campos e verifique seu significado de forma independente |
| **Pausa de aprovação** | Persista a ação pendente exata e a decisão |
| **Mudança de provedor** | Repita testes de compatibilidade de chamadas e saídas |

## Pi: núcleo pequeno e extensível

**Escolha o SDK do Pi quando quiser controle direto sobre uma implementação compacta de agente de código.** A [documentação do projeto](https://github.com/earendil-works/pi/tree/main/packages/coding-agent) descreve a integração SDK e RPC junto da interface interativa. O conjunto padrão inclui leitura, escrita, edição e execução shell, com extensões para comportamentos adicionais.

**O minimalismo transfere trabalho ao integrador.** Pi omite de propósito pop-ups de permissão e orquestração de subagentes. A documentação direciona usuários a contêineres ou extensões próprias para fluxos de confirmação. Avalie aqui o SDK incorporado, não sua interface de terminal contra o editor gráfico de outro fornecedor.

**Minha recomendação:** coloque Pi na lista curta para um serviço de código sob medida quando você estiver preparado para cuidar de restrições de execução, revisão de extensões e política de recuperação. Seu núcleo pequeno facilita entender e mudar o comportamento. É menos adequado quando o requisito principal é um sistema de aprovação e orquestração já montado.

## LangGraph: controle explícito do fluxo

**Escolha LangGraph quando o próprio fluxo precisar de estado e transições explícitos.** Sua [documentação de persistência](https://docs.langchain.com/oss/python/langgraph/persistence) distingue checkpoints por thread de stores entre threads. Um checkpointer persistente permite recuperação após reinícios do processo. Um checkpointer em memória não permite.

**LangGraph é uma base de runtime.** Você define o fluxo e decide onde o comportamento orientado pelo modelo entra. Deep Agents já usa essa base, então descer para LangGraph faz sentido quando você precisa de mais controle sobre os caminhos de execução.

**Minha recomendação:** coloque-o na lista curta para um processo com etapas nomeadas, pausas de revisão e regras distintas de recuperação. Um fluxo de entrada de documentos pode extrair campos, validá-los, pedir revisão e publicar um registro aprovado. Transições fixas ajudam quando o modelo escolhe conteúdo, mas não deve inventar o processo de negócio.

| Etapa do fluxo | Evidência de conclusão |
|---|---|
| **Extrair** | Registro candidato ligado à fonte |
| **Validar** | Verificações determinísticas e exceções |
| **Revisar** | Decisão ligada ao candidato específico |
| **Publicar** | Recibo externo registrado para a operação |

**Efeitos externos precisam de um desenho próprio de recuperação.** Salvar o estado do grafo não torna atômica uma transação remota com o checkpoint. Use um identificador de operação e reconcilie o resultado externo antes de tentar o envio novamente.

## Teste as partes ausentes

**Uma lista de recursos é apenas o início.** Passe cada candidato por falhas semelhantes às do seu trabalho. Use um workspace descartável e serviços de teste com registros sintéticos.

| Teste | Evidência a guardar |
|---|---|
| **Envio interrompido** | Um efeito externo depois da recuperação |
| **Conversa longa** | Requisitos originais ainda satisfeitos |
| **Ação rejeitada** | Nenhum efeito por uma ferramenta alternativa |
| **Instrução não confiável no documento** | O texto não adquire autoridade |
| **Argumentos de ferramenta malformados** | Rejeição antes da mutação da aplicação |
| **Orçamento esgotado** | Parada limitada com trabalho parcial inspecionável |

**Defina a repetição explicitamente.** Para um serviço de pedidos de substituição, pare o worker depois que o serviço de teste aceitar um pedido, mas antes de salvar a conclusão local. Ao reiniciar, o fluxo deve consultar o identificador da operação em vez de enviar de novo cegamente. Este é um teste proposto, não um resultado observado para os produtos listados.

**Verifique as evidências depois da compactação.** Coloque um requisito importante no início da tarefa, depois forneça material realista suficiente para acionar a estratégia de contexto configurada. Peça ao agente o artefato final e as referências de fonte. Nossa [análise de CLM e memória de agentes](/articles/context-language-models-agent-memory-hallucinations/) explica por que guardar notas e guardar evidências corretas são preocupações separadas.

**Revise os destinos de telemetria.** Rastros de ferramentas e stores de memória costumam conter dados da tarefa. Registre quais sistemas os recebem e por quanto tempo ficam disponíveis. Inferência local não implica logging, recuperação ou execução somente locais.

## Compare o custo por tarefa aceita

**Use duas trilhas de avaliação.** Uma comparação controlada mantém modelo, ferramentas, conjunto de tarefas e orçamentos iguais quando houver suporte. Uma comparação de implantação usa a configuração pretendida para cada candidato. A primeira isola alguns efeitos do software. A segunda responde qual configuração completa atende melhor ao seu trabalho.

**Não force configurações sem suporte na trilha controlada.** Se dois candidatos não tiverem modelo ou interface de ferramentas em comum, informe a comparação como avaliação de sistema. Registre o esforço de configuração e a orientação humana.

```yaml
# Illustrative trial record, not a framework configuration file
candidate: "package and pinned version"
model: "provider and exact model identifier"
workspace: "isolated test environment"
task_set: "frozen fixtures and acceptance checks"
limits:
  elapsed_minutes: 15
  model_calls: 30
  tool_calls: 60
record:
  - accepted_result
  - unsupported_claims
  - duplicate_external_actions
  - inference_cost
  - infrastructure_cost
  - human_review_minutes
  - recovery_outcome
```

**Faça vários testes por tarefa.** Mantenha tentativas malsucedidas no denominador e informe contagens brutas junto das porcentagens. Um teste pequeno revela padrões de falha, não um ranking estável do setor.

**Cálculo ilustrativo:** suponha que a configuração A gaste 12 dólares em dez tentativas e produza oito resultados aceitos. Seu custo de inferência por tarefa aceita é 1,50 dólar. A configuração B gasta 8 dólares, mas produz quatro resultados aceitos, então o custo correspondente é 2,00 dólares. Nenhum valor inclui revisão humana ou infraestrutura, que devem entrar em um total separado.

**Defina falhas eliminatórias antes do teste.** Um envio não autorizado ou vazamento entre usuários não deve desaparecer em uma média de qualidade. Depois de impor esses requisitos, compare correção, recuperação, esforço de revisão e custo.

## Faça uma escolha limitada

**Comece com dois candidatos e um fluxo real.** Para um agente montado e flexível entre provedores, compare Deep Agents com uma alternativa mais estreita para sua aplicação. Para comportamento do Claude Code dentro de um serviço, teste Claude Agent SDK. Para trabalho em aplicações tipadas, compare Pydantic AI com OpenAI Agents SDK. Escolha Pi quando comportamento próprio justificar mais trabalho de integração, e LangGraph quando controle explícito do fluxo for a prioridade.

**Pré-requisitos do teste:** acesso aprovado ao modelo, fixtures sintéticas, workspace isolado quando necessário e critérios de aceitação escritos. Reserve uma tarde inicial para configuração e testes básicos de falha, depois colete execuções repetidas antes da decisão de produção. A dificuldade é intermediária ou avançada, conforme as ações externas e os requisitos de recuperação.

**Selecione o menor sistema que passe seus requisitos.** Preserve fixtures, versões de pacotes e registros de falha. Repita-os ao mudar modelo, estratégia de contexto, ferramentas ou backend de execução. Essas mudanças alteram o sistema avaliado.

## Referências

- [LangChain: visão geral do Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview)
- [Anthropic: visão geral do Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)
- [Anthropic: implantação segura](https://code.claude.com/docs/en/agent-sdk/secure-deployment)
- [OpenAI: Agents SDK](https://openai.github.io/openai-agents-python/)
- [OpenAI: execução human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [OpenAI: integração de modelos e provedores](https://openai.github.io/openai-agents-python/models/)
- [Pydantic: visão geral do framework de IA](https://pydantic.dev/docs/ai/overview/)
- [Pydantic: AI Harness](https://pydantic.dev/docs/ai/harness/)
- [Earendil: SDK de agente de código Pi e modos de integração](https://github.com/earendil-works/pi/tree/main/packages/coding-agent)
- [LangChain: persistência do LangGraph](https://docs.langchain.com/oss/python/langgraph/persistence)

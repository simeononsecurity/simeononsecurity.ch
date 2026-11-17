---
title: "OpenClaw e Hermes Agent: uma avaliação prática"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Avalie agentes de IA especializados e persistentes com um inventário de acessos, uma revisão de gatilhos, um registro do fluxo de dados e uma decisão de piloto."
genre: ["Inteligência artificial", "Engenharia de software", "Produtividade"]
tags: ["agentes de IA especializados", "OpenClaw", "Hermes Agent", "agentes de trabalho", "avaliação de agentes de IA", "agentes de IA persistentes"]
cover: "/img/cover/effective-ai-specialized-agent-evaluation.webp"
coverAlt: "Planilha com as ferramentas, a memória armazenada, os gatilhos, os registros e a decisão de revisão de um agente"
coverCaption: ""
---

[Voltar ao Curso Prático de Fluxos de Trabalho com IA](/effective-ai-course-start/)

**Escolha um agente especializado de acordo com a tarefa e os acessos necessários.** Um agente de trabalho que analisa um arquivo difere de um sistema persistente que recebe mensagens, armazena memória e executa ações agendadas. Esta lição opcional usa OpenClaw e Hermes Agent como exemplos e, em seguida, apresenta uma planilha de avaliação pré-instalação.

**Objetivo de aprendizagem:** você vai comparar os acessos e gatilhos dos agentes e registrar uma decisão de piloto limitado.

## Principais conclusões

- **Agente de trabalho com função delimitada:** agente designado para uma pergunta ou artefato.
- **Agente persistente:** serviço ou sessão que mantém estado ou reage a gatilhos posteriores.
- **Gatilho:** evento, mensagem ou agendamento que inicia o trabalho.
- **Inventário de acessos:** lista de ferramentas, contas, arquivos e permissões de gravação concedidas ao agente.
- **Decisão de piloto:** rejeitar, fazer um teste limitado ou aprovar um uso definido.

## Antes de começar

**Pré-requisitos:** [delegação](/articles/effective-ai-agent-delegation/), [ciclos delimitados por objetivos](/articles/effective-ai-bounded-agent-loops/) e um caso de uso fictício. Reserve 35 minutos. A dificuldade é intermediária. Esta lição não exige instalar um agente persistente.

**Caso de uso:** uma pessoa que coordena uma oficina quer que um assistente leia uma agenda e prepare um rascunho de lembrete. A solicitação não autoriza o envio do lembrete. Sua avaliação deve preservar esse limite.

## Contraste as funções

| Abordagem | Formato típico da tarefa | Primeira pergunta |
|---|---|---|
| **Um chat** | Redigir um lembrete | A agenda está disponível? |
| **Agente somente para leitura** | Conferir dados da agenda de forma independente | Qual fonte ele deve ler? |
| **Agente de programação** | Atualizar um programa local de relatórios | Quais arquivos e testes se aplicam? |
| **Plataforma persistente** | Reagir a mensagens ou agendas ao longo do tempo | Quais gatilhos, ferramentas e estados armazenados existem? |

**OpenClaw** é uma plataforma de agentes de código aberto com gateway, canais de mensagens, ferramentas, memória, conexões MCP e subagentes. A [visão geral](https://docs.openclaw.ai/start/why-openclaw), o [guia de conexão MCP](https://docs.openclaw.ai/tools/mcp) e o [guia de subagentes](https://docs.openclaw.ai/tools/subagents) descrevem esses componentes. Antes de um piloto, revise as configurações ativas de canais, ferramentas e sandbox.

**Hermes Agent** é o aplicativo de agentes da Nous Research. A família de modelos Hermes é separada. A [documentação](https://hermes-agent.nousresearch.com/docs/), o [guia de delegação](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation) e o [guia de configuração](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/) abordam CLI, mensagens, ferramentas, memória e tarefas delegadas. O [guia de memória](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/) descreve armazenamentos locais e aprovação de gravações. O padrão documentado para `memory.write_approval` e `skills.write_approval` é `false`. Ative a aprovação ou desabilite o armazenamento correspondente para um piloto que exija revisão de gravações. Verifique a configuração em execução antes de confiar em qualquer um desses controles.

| Ponto de avaliação | OpenClaw | Hermes Agent |
|---|---|---|
| **Ponto de entrada** | Gateway e canais conectados | CLI ou interface de mensagens configurada |
| **Trabalho delegado** | Subagentes com regras de sessão e ferramentas específicas da plataforma | Tarefas delegadas com regras de ferramentas específicas da plataforma |
| **Estado persistente** | Inspecionar memória habilitada e armazenamento de sessões | Inspecionar memória, perfil e gravações de habilidades |
| **Trabalho recorrente** | Inspecionar gatilhos e agendamentos configurados | Inspecionar [tarefas cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/) e estado do gateway |
| **Primeiro piloto** | Uma solicitação manual por um canal selecionado | Uma solicitação manual via CLI ou mensagens |

A tabela descreve pontos de revisão, não padrões de segurança equivalentes. Registre a versão instalada e a configuração ativa antes de conceder acesso a dados ou contas reais.

**Os nomes não definem um modelo comum de permissões.** Um “subagente” de um produto pode receber arquivos, ferramentas e histórico diferentes dos de um agente de trabalho de outro. Confira a documentação da versão instalada e as configurações ativas, sem transferir suposições entre ferramentas.

## Preencha uma planilha de acessos

**Crie uma linha para cada capacidade** antes de instalar ou conectar um sistema. Se o produto estiver disponível, use as configurações reais. Escreva “desconhecido” em vez de adivinhar.

| Pergunta | Resposta para o piloto da oficina |
|---|---|
| **Tarefa** | Redigir um lembrete com base em uma agenda sintética |
| **Entrada** | Um arquivo de agenda aprovado |
| **Arquivos** | Ler o arquivo da agenda, sem permissão de gravação |
| **Ferramentas externas** | Nenhuma no primeiro piloto |
| **Acesso a contas** | Nenhuma conta de e-mail ou calendário |
| **Gatilho** | Somente solicitação manual |
| **Gravações de memória e habilidades** | Registrar configurações ativas, desabilitar armazenamentos ou exigir aprovação de gravação durante o piloto |
| **Registros** | Registrar caminho de armazenamento, regra de retenção, prompt, revisão da fonte e rascunho |
| **Revisão** | Uma pessoa confere data, horário, local e lista de destinatários |
| **Reversão** | Descartar o rascunho e desabilitar o piloto |

**O fluxo de dados faz parte da planilha.** Anote onde as entradas saem do computador, qual fornecedor as processa e onde as transcrições ou a memória persistem. Se uma ferramenta se conectar ao e-mail, documente se ela lê, cria rascunhos ou envia. São permissões distintas.

## Tome uma decisão sobre o piloto

**Rejeitar:** o agente precisa de amplo acesso de gravação à caixa postal para uma tarefa que só exige um rascunho, ou seus gatilhos e registros são desconhecidos. Você não precisa instalar nada para rejeitar uma opção inadequada.

**Piloto:** limite a entrada à agenda sintética, use um gatilho manual, desabilite o envio e revise um rascunho. O resultado esperado é o horário correto, 19h, e nenhuma mensagem enviada. Registre sua própria observação se executar o piloto.

**Aprovar um uso definido:** somente depois que o piloto passar pelas verificações e a pessoa responsável aceitar os acessos, gatilho, retenção e etapas de revisão exatos. A aprovação para redigir não autoriza o envio ou uma automação futura.

## Diagnostique uma falha

**Suponha que um rascunho de lembrete use 18h.** Verifique se o agente leu a agenda atual ou se a memória armazenada ou uma mensagem antiga forneceu o horário desatualizado. Substitua a entrada antiga, repita um piloto manual e mantenha o envio desabilitado. Um segundo rascunho correto não apaga a primeira falha do registro.

**Suponha que uma conexão MCP apareça nas configurações, mas nenhuma ferramenta esteja acessível.** Consulte os [estados da conexão MCP](/articles/effective-ai-mcp-server-setup/). Uma entrada de servidor salva não comprova uma leitura bem-sucedida.

## Pratique e confira

**Seu artefato:** uma planilha de acessos preenchida e uma decisão: Rejeitar, Piloto ou Aprovar um uso definido. Indique um gatilho, um limite de permissões, uma pergunta sobre o fluxo de dados e uma forma de interromper o agente.

**Verificação de conclusão:** outra pessoa deve entender qual ação o agente executa, o que lê e armazena, quando funciona, quem confere o resultado e como desabilitá-lo. Se alguma resposta for desconhecida, escolha Rejeitar ou um Piloto mais restrito.

## Verifique sua compreensão

1. **Pergunta:** uma tarefa de lembrete limitada à redação precisa de permissão para enviar e-mail? **Resposta:** Não. Mantenha o envio fora do escopo do piloto.
2. **Pergunta:** quais configurações do Hermes precisam ser inspecionadas antes de um piloto com gravações controladas? **Resposta:** Confira as configurações ativas de gravação de memória e habilidades, inclusive os controles de aprovação.

## Próximas etapas

**Continue com o [projeto final do fluxo de trabalho com IA](/articles/effective-ai-capstone/)**. Para uma comparação mais ampla de ambientes de execução, consulte o [guia de ambientes para agentes](/articles/best-ai-agent-harnesses/).

**Navegação do curso:** [Anterior: Ciclos delimitados](/articles/effective-ai-bounded-agent-loops/), [Plano do curso](/effective-ai-course-start/).

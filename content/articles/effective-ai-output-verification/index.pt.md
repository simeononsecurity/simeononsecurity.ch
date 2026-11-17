---
title: "Como verificar resultados, fontes, testes e custos de IA"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Crie um registro de aceitação para um resultado de IA com verificações de fontes, escopo dos arquivos, evidências de testes, análise de privacidade e uso."
genre: ["Inteligência artificial", "Engenharia de software"]
tags: ["verificar resultados de IA", "verificação de fatos por IA", "revisão de agente de programação", "evidências de testes de IA", "acompanhamento de custos de IA", "revisão humana"]
cover: "/img/cover/effective-ai-output-verification.webp"
coverAlt: "Uma ficha de revisão compara uma afirmação da IA com um arquivo-fonte, um diff de código, a saída dos testes e o total de uso"
coverCaption: ""
---

[Voltar ao curso Fluxo de trabalho prático com IA](/effective-ai-course-start/)

**Aceite um resultado de IA somente depois de verificar as evidências adequadas à tarefa.** Uma explicação bem apresentada, uma ferramenta configurada e um indicador verde de testes respondem a perguntas diferentes. Esta lição cria um único registro de revisão para o laboratório da oficina.

**Objetivo de aprendizagem:** você produzirá um registro de aceitação para fontes, escopo dos arquivos, testes, privacidade e uso.

## Principais conclusões

- **Verificação de fontes:** compare uma afirmação baseada em fatos com um registro atual e confiável.
- **Verificação de escopo:** confira quais arquivos ou sistemas mudaram.
- **Verificação do comportamento:** execute testes e casos manuais relevantes.
- **Verificação de privacidade:** confira quais dados chegaram à ferramenta ou ao provedor.
- **Verificação do uso:** registre tokens, chamadas de ferramentas e a tarifa usada no cálculo do custo.

## Antes de começar

**Pré-requisitos:** o laboratório do curso, `docs/requirements.md`, um snapshot local do Git e a [lição de MCP](/articles/effective-ai-mcp-server-setup/) ou a alternativa no navegador. Reserve 40 minutos. A dificuldade é intermediária. Use o laboratório editado na primeira tarefa com um agente de programação. Se você pulou a edição, use uma extração nova e marque as verificações de recursos como não implementadas. A linha de base intacta ainda passa nos dois testes originais.

## Verificar uma afirmação baseada em fatos

**Afirmação:** “Os valores de status aprovados são `open` e `pending`.” Abra `docs/requirements.md`, revisão 1. O documento informa `open` e `done`. A afirmação está errada. Um tom confiante não altera o requisito.

**Para afirmações sobre produtos,** use a documentação oficial atual e registre o título da página e a data da revisão. Uma afirmação sobre um menu, plano, comando ou limite de contexto fica desatualizada antes de um princípio geral de fluxo de trabalho. A [documentação do Codex](https://learn.chatgpt.com/docs/codex/cli), a [documentação do Claude Code](https://code.claude.com/docs/en/overview) e a [documentação do OpenCode](https://opencode.ai/docs/) descrevem as interfaces atuais.

| Afirmação | Fonte | Decisão |
|---|---|---|
| **`open` e `pending`** | Requisito do laboratório, revisão 1 | Rejeitar, substituir `pending` por `done` |
| **A contagem sem filtro é 4** | Programa de linha de base e quatro entradas JSON | Confira executando o programa |
| **Ocorreu uma leitura MCP** | Transcrição das ferramentas da sessão | Aceite somente se uma chamada de ferramenta estiver visível |

## Inspecionar a alteração

**Em uma tarefa de programação,** use o Git para listar os arquivos alterados e ler o diff real. Um novo arquivo não rastreado aparece no status mesmo que não apareça em um diff comum, portanto inspecione os dois.

```bash
git status --short
git diff -- task_report.py tests
```

**Escopo esperado:** somente `task_report.py` e testes específicos mudam após a tarefa de filtro. Uma alteração em `tasks.json`, `docs/requirements.md` ou um arquivo de configuração oculto exige explicação e uma revisão separada. Se você não fez uma edição, espere não encontrar alterações.

## Testar o comportamento

**Execute as mesmas verificações de linha de base e dos recursos** na pasta extraída do laboratório. O relato de conclusão do agente deve apresentar os resultados observados dessas verificações.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**Na cópia editada,** os testes cobrem os novos casos, as contagens são 4, 2 e 2, e o valor inválido termina com um erro claro e código diferente de zero. Em uma cópia inicial nova, somente os dois testes de linha de base passam e o total é 4. Registre esse estado inicial separadamente.

**Um teste de recurso que falha exige diagnóstico.** Se `open` exibir 4, confira se o argumento do filtro chega à função de contagem e se o programa compara o campo `status` da tarefa. Não marque um teste que falhou como aprovado porque o agente declarou que concluiu a implementação.

## Verificar privacidade e acesso

**Registre quais arquivos o agente recebeu.** O laboratório contém dados sintéticos e nenhum segredo. Um projeto real pode incluir credenciais, dados de clientes ou documentos privados. Antes de compartilhar a saída, inspecione prompts, logs, capturas de tela e diffs em busca desses valores.

**Um teste local comprova somente o comportamento local.** Ele não comprova as permissões de uma conta na nuvem, o escopo de um servidor MCP nem o comportamento de um serviço implantado. Teste cada limite no ambiente relevante.

## Registrar uso e custos

**Tokens medem o volume de entrada e saída do modelo.** Os painéis variam entre produtos, portanto use os números de uso mostrados pelo seu provedor. Registre separadamente as chamadas de ferramentas e as cobranças por imagens ou ambientes hospedados, quando aplicável. Confira as tarifas atuais antes de calcular uma conta real.

**Abra a visualização de uso da conta que executou a tarefa.** Registre os tokens de entrada e saída exibidos, o modelo, o período de faturamento e qualquer categoria de entrada em cache. Para assinaturas ChatGPT ou Claude, um limite ou crédito de uso não equivale ao custo de API de uma tarefa. Em uma execução do OpenCode via API ou provedor, consulte o uso ou faturamento desse provedor e a tarifa atual. Se o produto não mostrar tokens por tarefa, escreva “indisponível” e não estime uma cobrança a partir do tamanho da conversa.

**Cálculo ilustrativo, não representa o preço de um provedor:** 30.000 tokens de entrada a US$ 1 por milhão custam US$ 0,03. 5.000 tokens de saída a US$ 5 por milhão custam US$ 0,025. A cobrança combinada do modelo neste exemplo é US$ 0,055, antes de taxas de ferramentas ou hospedagem.

```text
custo de entrada = tokens de entrada / 1.000.000 × tarifa de entrada
custo de saída = tokens de saída / 1.000.000 × tarifa de saída
total = custo de entrada + custo de saída + cobranças separadas de ferramentas
```

**Uma tarefa delegada também consome tokens.** A delegação transfere a saída detalhada para fora da conversa principal, mas não torna o trabalho gratuito. Compare o custo com o valor da verificação independente.

**Mantenha as categorias de cobrança separadas.** Entrada em cache, entrada nova, saída, chamadas de ferramentas e execução hospedada podem usar tarifas diferentes. Este exemplo usa apenas tarifas de entrada nova e saída. Ele não diz nada sobre uma cobrança de assinatura ou de ferramenta.

## Manter um registro de aceitação

| Campo | Exemplo preenchido após a edição |
|---|---|
| **Fonte** | `docs/requirements.md`, revisão 1, lido |
| **Arquivos alterados** | `task_report.py` e `tests/test_task_report.py` em `git status --short` |
| **Testes** | Testes de linha de base e de filtro novo aprovados, registre a contagem observada |
| **Saída manual** | `Total tasks: 4`, `2` e `2` observados, valor inválido rejeitado |
| **Estado do recurso** | `--status open` e `--status done` implementados |
| **Privacidade** | Somente arquivos sintéticos |
| **Uso** | Registre os números do seu provedor, se disponíveis |
| **Decisão** | Aceite somente após passar nas verificações da fonte, diff, testes e privacidade |

**Seu artefato:** copie este registro e preencha-o após sua própria execução. Substitua “observado” somente por uma saída que você viu. Escolha Aceitar quando todas as verificações necessárias passarem, Revisar quando o ajuste tiver escopo limitado e Parar quando a fonte, o escopo ou o acesso não estiver claro.

## Verificar sua compreensão

1. **Pergunta:** uma linha de base inicial aprovada comprova que o recurso solicitado existe? **Resposta:** Não. Teste o novo comportamento de aceitação após a edição.

2. **Pergunta:** o que deve constar em um registro de aceitação? **Resposta:** evidências da fonte, arquivos alterados, verificações de comportamento, escopo de acesso e uso observado.

## Solução de problemas

- **Sem fonte para uma afirmação:** marque-a como não verificada e procure um registro confiável.
- **Os testes passam, mas a saída difere:** adicione um caso manual e inspecione os dados.
- **Uso indisponível:** registre “indisponível” em vez de estimar um custo real.
- **O diff inclui dados privados:** pare de compartilhar a saída e remova os dados do registro de prática.

## Próximas etapas

**Continue com [Delegação de agentes](/articles/effective-ai-agent-delegation/)**. Para mais detalhes sobre custos e privacidade, leia [roteamento de provedores](/articles/openrouter-provider-routing-quality-cost/) e [limite de privacidade da IA local](/articles/local-ai-privacy-boundary/).

**Navegação do curso:** [Anterior: Configuração do MCP](/articles/effective-ai-mcp-server-setup/), [Visão geral do curso](/effective-ai-course-start/).

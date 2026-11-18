---
title: "Gestão da janela de contexto de IA: mantém os agentes de programação focados"
description: "Controla o contexto ativo de uma tarefa de IA com ficheiros selecionados, passagens concisas e respostas curtas dos trabalhadores, preservando decisões e provas."
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
genre: ["Inteligência artificial", "Engenharia de software"]
tags: ["gestão da janela de contexto de IA", "contexto de agente de programação", "passagem de IA", "compactação de contexto", "orquestração de agentes", "orçamento de tokens"]
cover: "/img/cover/effective-ai-context-window-management.webp"
coverAlt: "Uma nota concisa de passagem de contexto junto a ficheiros de projeto selecionados e uma transcrição de conversa muito maior descartada"
coverCaption: ""
---

[Voltar ao Curso prático de fluxos de trabalho com IA](/effective-ai-course-start/)

**A janela de contexto é o texto e os outros materiais que um modelo processa no turno atual.** Instruções, definições de ferramentas, excertos de ficheiros, resultados de ferramentas e histórico da conversa ocupam espaço. Esta lição mostra como manter a próxima tarefa focada e deixar uma passagem de contexto fiável.

**Objetivo de aprendizagem:** criar uma passagem concisa e testá-la numa sessão nova.

## Ideias principais

- **Tokens:** unidades que o modelo usa para processar entradas e saídas.
- **Contexto ativo:** material disponível durante um turno, dentro dos limites do produto.
- **Fontes duradouras:** ficheiros ou registos do projeto fora da conversa.
- **Compactação:** resume ou elimina contexto antigo e pode omitir um detalhe necessário.
- **Passagem de contexto:** encaminha uma sessão nova para as fontes atuais e o trabalho verificado.

## Antes de começar

**Pré-requisitos:** o laboratório editado da [primeira tarefa com um agente de programação](/articles/effective-ai-coding-agent-first-task/), o requisito aprovado e a [lição sobre pacotes de tarefas](/articles/effective-ai-task-packets/). Se seguiste o percurso de estudo, usa o laboratório que editaste manualmente. Reserva 35 minutos. A dificuldade é intermédia. Guarda as notas do curso fora da pasta extraída do laboratório para que `git status` mostre apenas alterações de código.

## Escolher contexto por tarefa

**Para editar o filtro de estado,** o agente precisa de `task_report.py`, `docs/requirements.md`, dos testes relevantes e de uma pequena amostra de `tasks.json`. Não precisa de todas as conversas antigas, de toda a documentação do site nem do histórico completo do Git. Consulta primeiro um mapa e carrega depois os ficheiros mínimos para a decisão seguinte.

| Tarefa | Contexto útil | Contexto excessivo |
|---|---|---|
| **Definir o comportamento** | Requisito aprovado e uma amostra de dados | Conversas exploratórias antigas |
| **Editar o programa** | Programa e testes focados | Diretórios de projetos sem relação |
| **Rever o resultado** | Diferenças, saída dos testes e requisito | Transcrição completa do agente |
| **Retomar mais tarde** | Nota de passagem e caminhos das fontes | Uma conversa de várias horas colada na íntegra |

**Esta é uma escolha de recuperação, não uma regra para ocultar provas.** Se um teste falhar, inclui a saída exata e o ficheiro envolvido. Remove registos irrelevantes, não os detalhes necessários para diagnosticar a falha.

**Conta o custo fixo antes de adicionar trabalhadores.** As instruções do agente e os esquemas das ferramentas disponíveis podem ocupar contexto antes de leres um ficheiro da tarefa. Um segundo trabalhador repete parte desse custo e acrescenta um relatório para o agente principal rever. Para editar dois ficheiros, usa um agente. Numa pesquisa independente por muitas fontes, um relatório curto pode reduzir o contexto da sessão principal, mesmo que o consumo total de tokens aumente.

## Criar uma passagem concisa

**Uma passagem de contexto é um registo curto para a sessão seguinte.** Deve separar o trabalho concluído do trabalho proposto. Guarda este exemplo como `course-notes/handoff.md`, fora do laboratório, e substitui as observações de exemplo pelas tuas.

```text
Objetivo: adicionar --status open|done ao relatório de tarefas do curso.
Fonte: docs/requirements.md, revisão 1.
Espaço de trabalho: pasta effective-ai-course-lab extraída.
Estado atual: o filtro de estado está em task_report.py e nos testes.
Verificado: registe o resultado observado dos testes e as contagens manuais 4, 2 e 2.
Decisão: tasks.json permaneceu inalterado.
Pendente: revisão independente do diff e da fonte.
Próxima verificação: execute novamente os testes e o caso de estado inválido.
Pare se: o requisito ou o valor de referência diferir deste registo.
```

**O exemplo não afirma que executaste esse trabalho.** Regista os resultados observados dos testes e os ficheiros alterados. Se a revisão da fonte mudar, atualiza a passagem depois de voltares a ler a fonte.

## Testar uma sessão nova

**Inicia uma conversa ou sessão nova de agente de programação** no laboratório. Numa conversa, cola a passagem e o `AGENTS.md` do laboratório sintético e indica os ficheiros a inspecionar. Num agente de programação, abre a pasta do laboratório e cola a passagem, permitindo leitura dos ficheiros indicados. Pergunta:

```text
Com esta passagem e os ficheiros atuais do repositório, indique os valores de estado aprovados, a contagem de referência e a próxima verificação. Não edite.
Se a passagem entrar em conflito com uma fonte atual, comunique o conflito.
```

**Raciocínio esperado:** a nova sessão encontra `open` e `done` em `docs/requirements.md`, identifica o valor inicial 4 e indica testes e verificações manuais. Se repetir o valor antigo `pending`, volta a ler o requisito e corrige a passagem.

## Manter o orquestrador pequeno

**Um orquestrador é o agente principal que coordena trabalhadores.** Dá a cada trabalhador uma pergunta delimitada e ficheiros de entrada identificados. Pede um resultado conciso: constatação, caminho da prova, confiança e questão por resolver. Guarda os registos detalhados num ficheiro ou na sessão do trabalhador. Traz apenas o que o agente principal precisa para decidir o passo seguinte.

**Exemplo:** pede a um trabalhador com acesso só de leitura para inspecionar os testes e responder «caso em falta, ficheiro e linha, verificação sugerida». Não peças que cole todos os testes na conversa principal. O agente principal confirma a constatação no repositório antes de editar. A [lição sobre delegação](/articles/effective-ai-agent-delegation/) acrescenta uma tarefa independente quando o âmbito justifica o custo.

**As sessões dos trabalhadores têm contexto próprio em muitos produtos,** mas a herança e o isolamento variam. Consulta as regras atuais do produto antes de assumir que um trabalhador vê as mesmas instruções, ficheiros ou ferramentas do agente principal. Os guias de [subagentes do Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents) e de [subagentes do Claude Code](https://code.claude.com/docs/en/sub-agents) descrevem o comportamento de cada produto.

## Usar a compactação com cuidado

**A compactação encurta o histórico ativo.** Codex, Claude Code e OpenCode diferem em quando e como compactam. Trata um resumo compactado como ajuda à continuação, não como registo completo do projeto. Guarda requisitos e decisões em ficheiros e volta a verificá-los após a compactação. Consulta as orientações atuais sobre [boas práticas do Codex](https://learn.chatgpt.com/docs/learn/best-practices), [comandos do Claude Code](https://code.claude.com/docs/en/commands) e [compactação do OpenCode 2](https://opencode.ai/v2/docs/compaction). OpenCode 1 e OpenCode 2 usam esquemas diferentes. Verifica `opencode --version` antes de copiares definições.

**Se o assistente perder uma restrição,** para a edição, reabre a fonte e volta a apresentar o pacote da tarefa. Uma sessão nova com uma passagem curta e verificada costuma exigir menos atenção do que corrigir repetidamente uma conversa longa e confusa.

## Praticar e verificar

**O teu artefacto:** uma passagem com menos de 180 palavras, guardada fora do laboratório. Identifica cada linha como fonte, resultado observado, decisão ou ação pendente. Dá a passagem a uma sessão nova e regista se ela identifica os dois valores de estado aceites e a verificação seguinte.

**Verificação final:** a sessão nova identifica `open`, `done`, o valor inicial 4 e um passo de teste sem depender da conversa antiga. Corrige omissões e volta a testar com outra sessão nova.

## Verificar a compreensão

1. **Pergunta:** o que deve incluir uma passagem para uma sessão nova? **Resposta:** objetivo, fonte autorizada, estado atual, resultado verificado e ação seguinte.

2. **Pergunta:** porque deve o relatório de um trabalhador ser curto? **Resposta:** um relatório conciso com provas dá ao orquestrador o resultado necessário sem repetir a transcrição do trabalhador.

## Resolução de problemas

- **O resumo omite uma decisão:** acrescenta uma linha curta com a decisão e a revisão da fonte.
- **A resposta do trabalhador é enorme:** pede uma tabela de provas limitada e referências a ficheiros.
- **A passagem está desatualizada:** relê os ficheiros de origem atuais antes de editar.
- **A pressão de contexto continua:** divide a tarefa em sessões menores com artefactos separados.

## Próximos passos

**Continua com a [Configuração do servidor MCP](/articles/effective-ai-mcp-server-setup/)**. Vais adicionar uma ferramenta externa só de leitura e limitar o âmbito da saída.

**Navegação do curso:** [Anterior: Primeira tarefa de programação](/articles/effective-ai-coding-agent-first-task/), [Índice do curso](/effective-ai-course-start/).

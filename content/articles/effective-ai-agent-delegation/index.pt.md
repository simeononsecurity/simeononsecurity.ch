---
title: "Delegação de agentes de IA: atribua tarefas e revise resultados"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Decida quando um segundo agente de IA ajuda, atribua uma tarefa delimitada a cada trabalhador, evite conflitos de edição e integre evidências na sessão principal."
genre: ["Inteligência artificial", "Engenharia de software"]
tags: ["delegação de agentes de IA", "subagentes", "agentes trabalhadores", "contexto do orquestrador", "worktrees de IA", "tarefas paralelas de IA"]
cover: "/img/cover/effective-ai-agent-delegation.webp"
coverAlt: "Um agente principal atribui tarefas independentes de pesquisa e revisão de testes e depois combina relatórios curtos de evidências"
coverCaption: ""
---

[Volte ao curso prático de fluxo de trabalho com IA](/effective-ai-course-start/)

**Delegue quando uma pergunta independente justificar uma sessão separada.** Um agente trabalhador examina fontes, revisa testes ou prepara uma alteração delimitada em seu próprio contexto. O agente principal verifica e integra o resultado. Esta lição compara documentações enquanto sua sessão principal mantém a pequena tarefa do laboratório.

**Objetivo de aprendizagem:** você atribuirá uma revisão independente a um trabalhador e verificará seu breve relatório de evidências.

## Principais pontos

- **Orquestrador:** agente principal que coordena a tarefa e a revisão final.
- **Trabalhador:** agente separado responsável por um resultado delimitado.
- **Trabalho independente:** subtarefa cuja resposta não depende do resultado inacabado de outro trabalhador.
- **Responsabilidade:** arquivo ou pergunta nomeados e atribuídos a um trabalhador.
- **Integração:** comparação, pelo agente principal, do resultado do trabalhador com as fontes atuais.

## Antes de começar

**Pré-requisitos:** seus registros de [transferência de contexto](/articles/effective-ai-context-window-management/) e [verificação de saída](/articles/effective-ai-output-verification/). Reserve 40 minutos. Dificuldade intermediária. A rota conectada exige um produto com suporte a trabalhadores. A rota de estudo usa outro chat e integração manual.

**Comece com uma cópia inicial limpa para esta lição.** Salve fora do laboratório o diff do filtro editado e o registro de testes. Extraia o ZIP original em uma nova pasta descartável. Execute o comando inicial e os dois testes de referência. Repita a base Git da lição de configuração do curso e recrie as instruções curtas `AGENTS.md` e o `CLAUDE.md` opcional da lição sobre contexto do repositório. Faça você mesmo o commit desses arquivos e confirme que `git status --short` está limpo. Guarde a cópia editada do filtro como referência, mas faça o exercício com a cópia inicial limpa.

## Decida se deve delegar

**Use um agente** para uma pequena edição sequencial. Delegar tem custos de configuração, tokens e revisão. Use um trabalhador quando uma pergunta independente somente de leitura, de outra forma, ocuparia o chat principal com muitos arquivos ou páginas de fontes.

| Tarefa do laboratório | Delegar? | Motivo |
|---|---|---|
| **Adicionar um filtro de dois valores** | Normalmente não | Um arquivo pequeno e testes focados |
| **Encontrar casos ausentes em dois testes de referência** | Normalmente não | A sessão principal lê um arquivo curto com mais rapidez |
| **Comparar documentos atuais de três produtos** | Sim, somente leitura | A leitura das fontes fica no contexto do trabalhador |
| **Editar a mesma função duas vezes** | Não | Edições simultâneas geram conflitos |

**O trabalhador deve receber menos contexto que o orquestrador,** não uma cópia da conversa inteira. Informe o objetivo, o caminho da fonte, os limites da tarefa e o formato de retorno. Mantenha um breve relatório de evidências na sessão principal. Inspecione você mesmo os arquivos citados antes de agir.

## Execute um trabalhador somente de leitura

**Mantenha pequena a tarefa principal.** Na sessão principal, leia o `AGENTS.md` local e anote qual arquivo contém o comando de teste. Atribua a pergunta de pesquisa separada abaixo a um trabalhador. Ele não precisa do laboratório inteiro nem do chat anterior.

**Rota conectada:** no Codex, Claude Code ou outro cliente com suporte a trabalhadores, abra o laboratório como projeto e peça ao agente principal para delegar a solicitação somente de leitura abaixo a um trabalhador. Confira no registro das ferramentas se um trabalhador real iniciou e devolveu um relatório. Se o produto não expuser trabalhadores, use uma sessão separada e identifique-a como tal. Os guias atuais de [subagentes Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), [subagentes Claude Code](https://code.claude.com/docs/en/sub-agents) e [agentes OpenCode](https://opencode.ai/docs/agents/) descrevem os controles atuais.

**Rota de estudo:** abra um novo chat para a mesma solicitação. Dê a ele os três links oficiais ou trechos das fontes. Identifique-o como trabalhador simulado. Um segundo chat é um contexto separado, não prova de execução de subagente nativo.

```text
Use a documentação oficial atual Codex AGENTS.md, Claude Code memory e OpenCode rules.
Compare como cada produto carrega arquivos de instrução do repositório.
Não edite arquivos.
Retorne no máximo três linhas: produto, arquivo de instrução, URL da fonte e um comportamento de carregamento.
Indique incertezas. Não cole páginas completas.
```

**Conjunto de fontes:** [instruções de projeto do Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [memória do Claude Code](https://code.claude.com/docs/en/memory) e [regras do OpenCode](https://opencode.ai/docs/rules/). O relatório esperado cita `AGENTS.md` para Codex e OpenCode. As versões atuais do Claude Code também carregam `AGENTS.md` diretamente quando `CLAUDE.md` ou `CLAUDE.local.md` não têm precedência. Este laboratório usa um arquivo `CLAUDE.md` com uma importação `@AGENTS.md`, que também atende sessões mais antigas ou configuradas de outra forma. Verifique as páginas atuais e a versão ativa antes de tratar o exemplo como saída observada de um trabalhador.

## Integre os resultados

**Abra você mesmo as páginas citadas.** Se o trabalhador disser que Claude Code sempre precisa importar `CLAUDE.md`, consulte seu guia memory e corrija o relatório. Compare-o com os arquivos de instrução locais. Escreva uma nota curta de integração:

```text
Aceito: Codex e OpenCode usam AGENTS.md para as instruções do projeto.
As versões atuais do Claude Code carregam AGENTS.md diretamente. Este laboratório
usa CLAUDE.md com importação @AGENTS.md para um mapa compartilhado estável.
Evidência: registre as três URLs oficiais atuais e a data da revisão.
Decisão: mantenha um mapa compartilhado curto e uma importação para Claude.
```

**Esta nota é o resultado útil do trabalhador.** O orquestrador precisa de conclusões verificadas e caminhos das fontes, não da transcrição de pesquisa. Delegar consome mais tokens no total. Mantenha menor a conversa principal apenas quando a sessão separada poupar atenção.

## Atribua a responsabilidade pelas edições

**Se trabalhadores editarem arquivos,** divida a responsabilidade por arquivo ou use worktrees separadas para tarefas sobrepostas no repositório. Uma worktree é outra cópia do mesmo repositório Git, com arquivos de trabalho próprios. Ela separa edições simultâneas. O agente principal revisa e transfere as alterações por merge, cherry-pick ou patch explícito e depois executa os testes novamente na árvore integrada.

| Trabalhador | Trabalho atribuído | Retorno |
|---|---|---|
| **Implementação** | `task_report.py` | Diff e comando de teste |
| **Autor de testes** | `tests/test_task_report.py` | Casos de teste e resultado observado |
| **Orquestrador** | Requisitos e integração final | Diff combinado e critérios de aceitação |

**O pequeno laboratório não precisa de edições paralelas.** Esta tabela ensina um padrão de responsabilidade para tarefas maiores. Testes em uma worktree não validam uma implementação ainda isolada em outra. Se dois trabalhadores precisarem da mesma função, trabalhe em sequência ou peça a um deles uma revisão sem edição. Worktrees separadas evitam colisões de arquivos, mas não resolvem requisitos contraditórios.

## Verifique o comportamento do produto

**Subagentes variam conforme o host.** Codex, Claude Code e OpenCode diferem na herança de contexto, nas permissões das ferramentas e na entrega dos resultados. Leia os guias de [subagentes Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), [subagentes Claude Code](https://code.claude.com/docs/en/sub-agents) e [agentes OpenCode](https://opencode.ai/docs/agents/) para o produto instalado. Não presuma que o trabalhador compartilha todo o contexto principal ou usa uma worktree isolada.

## Pratique e confira

**Seu resultado:** um relatório curto de um trabalhador sobre documentação e uma nota de integração. Na rota de estudo, use um novo chat e identifique-o como trabalhador simulado. Não afirme que um subagente nativo foi executado nessa rota.

**Verificação final:** o relatório nomeia três fontes oficiais, fica dentro da pergunta e respeita o limite de tamanho. A nota de integração confere as fontes e identifica os arquivos de instrução usados no laboratório.

## Confira sua compreensão

1. **Pergunta:** Quando um trabalhador ajuda mais que um único agente? **Resposta:** Quando possui uma pergunta ou entrega independente e fornece um relatório de evidências útil.

2. **Pergunta:** O que deve acontecer depois que dois trabalhadores alteram arquivos sobrepostos? **Resposta:** Integre as mudanças, inspecione o diff combinado e execute as verificações novamente.

## Solução de problemas

- **O trabalhador retorna uma transcrição longa:** peça uma tabela de evidências mais curta com referências a arquivos.
- **Os trabalhadores discordam:** releia o arquivo oficial antes de escolher uma resposta.
- **Duas edições se sobrepõem:** interrompa uma edição e defina a responsabilidade pelos arquivos ou separe as worktrees.
- **O acesso do trabalhador às ferramentas difere:** inspecione suas permissões em vez de presumir que são iguais às do agente principal.

## Próximos passos

**Continue com os [ciclos de objetivo delimitados](/articles/effective-ai-bounded-agent-loops/).** Para governança de equipe além deste pequeno laboratório, use o [curso de implementação de colaboração em IA](/ai-collaboration-course-start/).

**Navegação do curso:** [Anterior: verificação de saída](/articles/effective-ai-output-verification/), [Visão geral do curso](/effective-ai-course-start/).

---
title: "Pacotes de tarefas de IA: melhores instruções e critérios de aceitação"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Transforme pedidos vagos à IA em pacotes de tarefas com resultado, fonte, escopo de arquivos, verificações e condição de parada definidos."
genre: ["Inteligência artificial", "Produtividade", "Engenharia de software"]
tags: ["redação de instruções para IA", "pacote de tarefas", "instrução para agente de programação", "critérios de aceitação", "fluxo de trabalho de IA", "instruções para agentes de IA"]
cover: "/img/cover/effective-ai-task-packets.webp"
coverAlt: "Um pedido vago reescrito como um pacote curto de tarefas com fonte, escopo, verificação e condição de parada"
coverCaption: ""
---

[Voltar ao curso prático de fluxos de trabalho com IA](/effective-ai-course-start/)

**Uma boa instrução descreve o trabalho e como você avaliará o resultado.** Mais palavras não corrigem a falta de escopo. Esta lição transforma um pedido vago em um pacote de tarefas para o laboratório do curso.

**Objetivo de aprendizagem:** você escreverá um pacote de tarefas delimitado, com fonte, escopo de arquivos, verificações e condição de parada.

## Principais pontos

- **Resultado** nomeia o artefato ou comportamento desejado.
- **Escopo** nomeia os arquivos permitidos e as ações excluídas.
- **Fonte** identifica o requisito aprovado.
- **Critérios de aceitação** tornam o sucesso observável.
- **Condições de parada** evitam suposições e trabalho posterior sem autorização.

## Antes de começar

**Pré-requisitos:** o laboratório extraído, o arquivo `docs/requirements.md` e a [lição sobre o contexto do repositório](/articles/effective-ai-agents-md-context/). Reserve 30 minutos. O nível é iniciante. O exercício termina com um pacote escrito. Ainda não é preciso editar código.

## Compare dois pedidos

**Pedido vago:** “Melhore o script de tarefas.” Um agente poderia reescrever a saída, adicionar dependências, editar dados de exemplo ou pular testes. O pedido não determina nenhuma dessas escolhas.

**Pedido delimitado:** “Adicione um filtro de status opcional a `task_report.py` usando a revisão 1 de `docs/requirements.md`. Mantenha a saída padrão. Adicione testes. Não altere dados de exemplo. Pare antes do commit.” O agente ainda escolhe os detalhes de implementação, enquanto a tarefa define o que significa sucesso.

| Parte do pacote | Exemplo do laboratório | Verificação |
|---|---|---|
| **Resultado** | Adicionar `--status` ao relatório | Os dois valores aceitos funcionam |
| **Fonte** | `docs/requirements.md`, revisão 1 | O código corresponde aos valores aprovados |
| **Escopo** | Somente programa e testes | O diff não contém outros arquivos |
| **Restrições** | Manter a saída padrão e os dados de exemplo | A saída-base continua `Total tasks: 4` |
| **Evidência** | Comando de teste e execuções manuais | As saídas correspondem às contagens esperadas |
| **Parada** | Não fazer commit nem push | O histórico do Git e o repositório remoto não mudam |

## Use um modelo reutilizável

**Copie este modelo** para uma pequena tarefa de programação ou pesquisa. Exclua campos sem relação com a tarefa em vez de preenchê-los com texto vago.

```text
Resultado:
Fonte oficial e revisão:
Arquivos ou registros relevantes:
Alterações permitidas:
Alterações e ações excluídas:
Exemplos do comportamento desejado:
Verificações de conclusão:
Quando parar ou perguntar:
Relate:
```

**Para o laboratório,** o pacote preenchido fica assim:

```text
Objetivo: adicione um filtro --status opcional a task_report.py.
Fonte: docs/requirements.md, revisão 1.
Arquivos relevantes: task_report.py, tasks.json, tests/.
Alterações permitidas: task_report.py e testes direcionados.
Excluído: tasks.json, novas dependências, commits e envios.
Exemplos: sem filtro, exibe Total tasks: 4. open e done exibem 2 cada.
Verificações: execute os testes unitários e quatro comandos manuais: sem filtro, open, done e um valor inválido.
O valor inválido deve retornar um código diferente de zero com uma mensagem clara.
Pare ou pergunte se houver conflito entre fontes, arquivo ausente ou falha inicial sem relação com a tarefa.
Relatório: arquivos alterados, comandos, resultados observados e questões não resolvidas.
```

**No Windows,** use `py -3` nos comandos do pacote se o seu ambiente usar o inicializador Python.

**O pacote não prescreve cada linha de código.** Ele deixa o agente escolher uma implementação pequena e mantém o resultado verificável.

## Acrescente exemplos com cuidado

**Um exemplo preciso elimina ambiguidades.** Os exemplos `open` e `done` especificam a saída para o arquivo fornecido com quatro tarefas. Eles não estabelecem uma regra geral para todos os arquivos. Em outro arquivo, as contagens dependem dos registros.

**Separe o esperado do observado.** Antes de executar o programa, `Total tasks: 2` é o resultado esperado para cada status. Depois da execução, a saída do terminal é uma observação. Se os valores divergirem, examine os dados e a implementação antes de declarar sucesso.

## Pratique uma condição de parada

**Suponha que o arquivo de requisitos esteja ausente.** O pacote o nomeia como fonte aprovada. Pare e solicite o requisito em vez de inferir os valores aceitos de um chat antigo ou de uma tarefa de exemplo.

**Suponha que os testes-base falhem antes da edição.** Registre a falha e pergunte se deve corrigir primeiro o estado inicial. Uma execução posterior bem-sucedida não mostra se a diferença veio do filtro ou do estado de partida.

**Suponha que o agente queira fazer um commit.** O pacote exclui commits. Peça que ele pare após o diff e os testes. Você decide se um commit posterior se encaixa no fluxo do projeto.

## Confira o pacote

**Dê um ponto por resposta:** o resultado é concreto? A fonte que rege o trabalho está nomeada? O escopo dos arquivos está claro? Há pelo menos duas verificações observáveis? Existe uma condição de parada? Uma pontuação abaixo de cinco indica que o pacote precisa de revisão antes da delegação.

**Seu resultado:** salve o pacote final e uma explicação de uma linha para uma condição de parada. Entregue-o a um agente de programação na próxima lição prática ou responda manualmente aos resultados esperados no roteiro de estudos.

## Verifique o entendimento

1. **Pergunta:** o que torna um pacote de tarefas verificável? **Resposta:** Uma fonte, arquivos permitidos, verificações observáveis e uma condição de parada.
2. **Pergunta:** o que um agente deve fazer quando a fonte não traz um detalhe necessário? **Resposta:** Parar e informar o detalhe ausente em vez de inventá-lo.

## Solução de problemas

- **O agente altera demais:** nomeie os arquivos e as ações excluídas no pacote.
- **O agente faz muitas perguntas:** forneça a fonte ausente ou um exemplo concreto.
- **O agente declara sucesso cedo demais:** peça as saídas observadas dos comandos e inspecione os arquivos.
- **O pacote fica longo demais:** substitua o conteúdo copiado da fonte pelo caminho e pela revisão.

## Próximos passos

**Continue com [Sua primeira tarefa com um agente de programação](/articles/effective-ai-coding-agent-first-task/)**. Use o pacote para orientar uma pequena alteração no laboratório.

**Navegação do curso:** [Anterior: Contexto do repositório](/articles/effective-ai-agents-md-context/), [Programa do curso](/effective-ai-course-start/).

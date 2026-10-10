---
title: "GitHub Copilot CLI versus VS Code: comparação de fluxos de trabalho de 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Compare o agente de terminal do Copilot com a experiência no VS Code, incluindo contexto do editor, diferenças visuais, modo Agent, integração CLI e políticas da conta."
genre: ["Ferramentas de desenvolvimento", "Inteligência artificial", "Desenvolvimento de software"]
tags: ["GitHub Copilot CLI versus VS Code", "Copilot CLI", "GitHub Copilot", "VS Code", "modo Agent", "CLI versus GUI", "contexto do editor", "sugestões embutidas", "diferença visual", "sessões do Copilot", "agente de terminal", "fluxo do GitHub", "revisão de código", "integração IDE", "ferramentas MCP", "permissões do agente", "AI Credits", "ferramentas de desenvolvimento", "assistente de programação", "automação"]
cover: "/img/cover/github-copilot-cli-vs-vscode.webp"
coverAlt: "Prompt de terminal ligado a uma seleção do editor e a uma diferença visual em um espaço de programação azul e verde"
coverCaption: ""
---

**GitHub Copilot CLI e Copilot no VS Code oferecem pontos de entrada diferentes para o trabalho de programação.** O CLI começa com o shell e um prompt de tarefa. O VS Code combina contexto do editor, sugestões, chat e fluxos de agente. Avalie os dois dentro da mesma política de conta e repositório.

**A escolha não é exclusiva.** O GitHub documenta uma conexão entre Copilot CLI e VS Code. Uma tarefa orientada pelo terminal se beneficia da seleção do editor e da revisão visual quando você conecta os dois de forma explícita.

## Principais conclusões

- **Use Copilot CLI para tarefas orientadas pelo terminal** e chamadas programáticas compatíveis.
- **Use Copilot no VS Code para trabalho centrado no editor**, incluindo assistência embutida e modo Agent.
- **Conecte o CLI ao VS Code** quando quiser prompts de terminal com contexto e diferenças do editor.
- **Verifique as configurações de conta, modelo e política**, mesmo na mesma família de produtos.

**Escopo e data:** A documentação oficial foi verificada em 10 de outubro de 2026. Esta comparação cobre o CLI independente `copilot` e o Copilot no VS Code, não a extensão antiga `gh copilot` nem um agente de nuvem atribuído a uma issue do GitHub. Os pré-requisitos são um repositório testável e acesso permitido ao Copilot. Reserve uma hora para o teste.

## Três formas de trabalhar

| Fluxo | Interação principal | Tarefa de teste adequada |
|---|---|---|
| **CLI independente** | Prompt do terminal e saída de comandos | Explicar e corrigir uma falha de teste reproduzida |
| **Integração com VS Code** | Seleção do editor, chat, sugestões e diferenças | Alterar uma função selecionada e seus testes |
| **CLI conectado ao VS Code** | Tarefa de terminal com contexto e revisão do editor | Investigar no shell e inspecionar o patch visualmente |

**O modo híbrido continua sendo uma sessão CLI.** Executá-lo em um terminal integrado não o transforma automaticamente na conversa nativa do modo Agent do editor. Confira a sessão e a conexão ativas em vez de confiar na janela que contém o prompt.

## O que o CLI oferece

```bash
copilot
```

**O comando independente atual inicia o agente de terminal.** A [visão geral do Copilot CLI](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-cli) do GitHub descreve o uso interativo e programático, além de planejamento e permissões de ferramentas. Avalie-o quando a saída do terminal for a principal evidência.

**Uma primeira tarefa forte tem uma falha concreta.** Forneça o comando que falha, o comportamento esperado e uma restrição contra refatoração sem relação. Peça a reprodução antes de alterar arquivos. Confira se a explicação final corresponde à saída observada.

**A automação exige limites explícitos.** Use os [guias de uso do CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli) para a invocação e os controles atuais. Defina ferramentas permitidas, limites de tempo e tratamento da saída antes de executar trabalhos sem supervisão. Não converta uma política interativa de permissão em autorização ampla para um pipeline.

**O sandbox muda os limites do teste.** O GitHub documenta sandbox local para restrições de sistema de arquivos, rede e sistema, além de sandboxes de nuvem para execução isolada. Um prompt de diretório confiável e uma opção de aprovação não substituem esses limites. Teste o sandbox pretendido, o acesso de rede e o escopo de escrita com um fixture inofensivo antes de alterar um repositório real.

## O que o VS Code acrescenta

**A experiência do Copilot no IDE inclui sugestões, chat e tarefas de agente.** A [visão geral do IDE](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-in-ides) separa essas funções. A assistência embutida serve quando você continua sendo o editor principal. O modo Agent serve para um resultado limitado que exige mudanças em vários arquivos.

**O modo Agent edita e executa comandos de forma iterativa.** O [guia do modo Agent](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/use-copilot-agents/use-agent-mode?tool=vscode) descreve selecionar Agent no chat, revisar mudanças e ampliar ferramentas por MCP. A disponibilidade e a aprovação de comandos também dependem da configuração e da administração.

**Avalie a transferência de contexto de modo intencional.** Selecione uma função e peça uma explicação do tratamento de erros. Depois solicite uma pequena mudança com um teste independente. Registre se você precisou fornecer arquivos vizinhos ou corrigir uma suposição do agente sobre o código selecionado.

{{< figure src="copilot-terminal-editor-bridge.webp" alt="Prompt de terminal ligado a uma seleção do editor e a uma diferença de código lado a lado em um espaço de repositório" caption="Uma sessão CLI conectada combina entrada do terminal com revisão do editor" >}}

## Conecte as duas interfaces

```text
/ide
```

**Use `/ide` em uma sessão interativa do Copilot CLI** para inspecionar ou alterar a conexão do VS Code. O [guia de conexão](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/connecting-vs-code) documenta a correspondência de um workspace confiável, o compartilhamento da seleção e a exibição de edições propostas como diferenças.

**A conexão automática depende da correspondência do workspace.** Um CLI local não se conecta a um Codespace remoto apenas porque o nome do repositório coincide. Execute o CLI no ambiente correspondente. A autorização ampla de edição também ignora o fluxo de aprovação do diff proposto. Verifique as permissões se os prompts esperados desaparecerem.

**As transcrições do CLI aparecem na visualização Sessions do VS Code**, com continuação por Resume in Terminal. Isso preserva o fluxo do terminal. Não presuma que a conversa se tornou uma sessão nativa intercambiável do agente do editor.

| Antes de conectar | Verifique |
|---|---|
| **Workspace** | A pasta pretendida está aberta e confiável |
| **Local de execução** | CLI e integração do editor apontam para o mesmo ambiente |
| **Seleção** | O código destacado corresponde ao pedido atual |
| **Permissões** | A revisão da edição proposta continua ativa quando exigida |
| **Sessão** | A conversa pretendida continua |

## Modelos, cobrança e política

**Use o mesmo modelo selecionado para um teste das duas interfaces quando disponível.** Se as opções diferirem, registre a diferença. Outro modelo, contexto ou conjunto de ferramentas altera o experimento além da distinção entre gráfico e terminal.

**Verifique a contabilização atual do uso na sua conta.** A documentação do modo Agent do GitHub menciona AI Credits. Não aplique estimativas antigas de solicitações premium sem conferir o arranjo de cobrança atual. Um prompt do CLI e uma tarefa do editor não equivalem automaticamente a uma unidade de trabalho.

**O acesso da organização é um pré-requisito.** Se faltar um recurso, confira a política antes de reinstalar a extensão. Registre as ferramentas e integrações aprovadas para as duas superfícies. Um login do provedor não concede automaticamente autoridade para modificar todos os repositórios ou contatar todos os serviços externos.

## Faça um teste pareado

**Prepare duas cópias da mesma revisão inicial.** Use instruções e testes de aceitação iguais. Faça a primeira tentativa no CLI independente e a segunda no modo Agent do VS Code. Faça uma terceira tentativa com o CLI conectado somente se a interação mista servir ao seu trabalho normal.

| Medida | Motivo para registrar |
|---|---|
| **Contexto fornecido** | Revela o esforço manual de configuração |
| **Correção** | Distingue código plausível de uma correção verificada |
| **Etapas de aprovação** | Mostra o esforço de supervisão sob a mesma política |
| **Tempo de revisão** | Mede o esforço para entender o patch completo |
| **Reparos manuais** | Registra o trabalho restante após o agente |
| **Uso** | Relaciona custo a resultados aceitos |

**Mantenha a recuperação dentro do teste.** Rejeite uma abordagem proposta e explique o motivo. Observe se a próxima tentativa preserva o trabalho útil e respeita a correção. Isso revela mais sobre a usabilidade diária do que uma única demonstração sem interrupção.

## Solução de problemas e próximos passos

**Se o CLI se conectar à janela errada do editor**, inspecione `/ide` e selecione o workspace pretendido. Se a aprovação visual parar de aparecer, verifique as permissões amplas de edição. Se o modo Agent estiver indisponível, confira o estado da extensão e a política da organização.

**Escolha o CLI independente** quando o contexto do shell e a chamada repetível dominarem. **Escolha o VS Code** quando o contexto por seleção, o trabalho embutido e a revisão gráfica dominarem. **Use o CLI conectado** quando a entrada da tarefa no terminal e a inspeção do editor funcionarem bem juntas.

**Para escolhas entre fornecedores**, leia a [comparação principal de CLI](/articles/cli-coding-agents-comparison/) ou a [comparação principal de GUI](/articles/gui-coding-agents-comparison/). Mantenha essas avaliações separadas deste teste de interface dentro da mesma família.

---
title: "Configurar um servidor MCP: permissões, testes de ferramentas e remoção segura"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Ligue um servidor MCP de documentação só de leitura, inspecione as ferramentas, faça uma leitura real e remova a ligação."
genre: ["Inteligência artificial", "Ferramentas para programadores"]
tags: ["Configuração de servidor MCP", "Protocolo de contexto de modelos (MCP)", "Permissões MCP", "MCP no Codex", "MCP no Claude Code", "MCP no OpenCode"]
cover: "/img/cover/effective-ai-mcp-server-setup.webp"
coverAlt: "Cliente de IA ligado a um servidor de documentação só de leitura, com uma ferramenta e o limite de acesso visíveis"
coverCaption: ""
---

[Voltar ao curso Fluxo de trabalho prático com IA](/effective-ai-course-start/)

**Use um servidor MCP quando uma tarefa precisar de uma ferramenta reutilizável ou de informação atualizada fora do projeto.** O Model Context Protocol, ou MCP, define como cliente e servidor trocam informações sobre ferramentas, recursos e prompts. Uma entrada de servidor não prova que a ferramenta funciona. Esta lição testa uma ligação de documentação só de leitura.

**Objetivo de aprendizagem:** distinguir a configuração de uma leitura MCP real e registar como remover a ligação em segurança.

## Pontos principais

- **Anfitrião MCP:** aplicação de IA que coordena utilizadores, modelos, permissões e clientes.
- **Cliente MCP:** componente do protocolo que comunica com um servidor.
- **Servidor MCP:** programa ou serviço remoto que oferece ferramentas, recursos ou prompts.
- **Descoberta de ferramenta:** prova de que surge no cliente uma capacidade identificada por nome.
- **Execução de ferramenta:** prova de uma chamada real e do conteúdo devolvido.
- **Âmbito das permissões:** acesso concedido pelo anfitrião, servidor, conta e utilizador.

## Antes de começar

**Pré-requisitos:** [prática de contexto e passagem de trabalho](/articles/effective-ai-context-window-management/) e uma instalação atual do Codex CLI para o percurso acompanhado. Reserve 35 minutos. Dificuldade intermédia. Os outros agentes de programação têm guias de configuração próprios. O [servidor oficial OpenAI Docs MCP](https://learn.chatgpt.com/learn/docs-mcp) disponibiliza documentação de desenvolvimento só de leitura e não exige o envio de dados do curso.

**Use o laboratório sintético do curso.** Não ligue calendário, correio eletrónico ou sistema de produção neste exercício. Ler documentação basta para aprender os estados de ligação.

## Compreender os limites

| Estado | O que comprova | O que não comprova |
|---|---|---|
| **Configurado** | Existe uma entrada de servidor | Acessibilidade |
| **Ligado** | O cliente chegou ao servidor | Existência de ferramentas úteis |
| **Descoberto** | Aparece uma ferramenta identificada | Que a chamada terá êxito |
| **Executado** | Uma chamada devolveu conteúdo | Que a tarefa final está correta |
| **Verificado** | Fonte e resultado respondem à pergunta | Que as futuras chamadas funcionarão sempre |

**O MCP não concede, por si só, permissões de conta.** Também contam o anfitrião do cliente, servidor, autenticação, âmbito da conta e definições locais de aprovação. A [especificação MCP](https://modelcontextprotocol.io/specification/2026-07-28) define o protocolo, enquanto cada produto controla a sua experiência.

**Trate a saída do servidor como material de consulta.** Uma página obtida não substitui a tarefa nem autoriza a escrita de ficheiros. Cada definição de ferramenta também consome contexto. Ligue apenas o servidor necessário para esta leitura e remova-o no fim.

## Ligar um servidor só de leitura

**No Codex CLI,** execute estes comandos num terminal. O primeiro adiciona o servidor público de documentação. O segundo lista os servidores configurados.

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

**Prova de configuração esperada:** a lista contém `openaiDeveloperDocs`. Isto comprova apenas o registo. Inicie uma nova sessão Codex na pasta do laboratório extraído e consulte as ferramentas MCP com `/mcp`. Use os nomes mostrados pela versão instalada.

**Peça uma leitura real:**

```text
Use o servidor MCP da documentação de programadores da OpenAI para encontrar as orientações atuais de AGENTS.md.
Indique o título e o URL da página de origem, dois pontos relevantes para este laboratório e a ferramenta MCP usada.
Não edite ficheiros.
```
**Inspecione o resultado.** A página devolvida deve descrever `AGENTS.md` como orientações do repositório e incluir o URL exato da fonte. Abra a página citada e confirme o tema. Uma resposta sem chamada MCP na transcrição é uma resposta normal, não prova de execução da ferramenta.

## Diagnosticar uma falha

**Se `codex mcp list` mostrar o servidor, mas `/mcp` não mostrar ferramentas,** o registo funcionou, mas a descoberta falhou. Reinicie a sessão, consulte os servidores ativos com `/mcp` e a configuração guardada com `codex mcp get openaiDeveloperDocs`; depois verifique o URL do servidor e o acesso à rede. Não declare a configuração MCP bem-sucedida apenas com base na entrada.

**Se surgir uma ferramenta, mas a leitura falhar,** registe o erro e tente novamente uma vez após verificar a ligação. Se a mesma chamada voltar a falhar, use a página oficial citada no navegador como fonte alternativa e marque o exercício MCP como incompleto. Não invente resultados da ferramenta.

## Remover a ligação

**Depois da leitura,** remova o servidor de prática do Codex CLI e confirme que a entrada desapareceu.

```bash
codex mcp remove openaiDeveloperDocs
codex mcp list
```

**Prova de remoção esperada:** `openaiDeveloperDocs` não aparece na nova lista. Reinicie uma sessão Codex ativa antes de verificar se as ferramentas disponíveis mudaram. Remover uma definição local não revoga uma autorização de conta separada usada por outro serviço.

## Usar outro cliente

**Claude Code e OpenCode também suportam MCP.** Siga o [guia MCP do Claude Code](https://code.claude.com/docs/en/mcp) ou o [guia MCP do OpenCode](https://opencode.ai/docs/mcp-servers/) correspondente à versão instalada. Registe os mesmos cinco estados: configurado, ligado, descoberto, executado e verificado. O esquema de configuração e as permissões de agentes do OpenCode variam entre versões. Use exemplos do guia adequado à instalação.

**Para um percurso apenas no navegador,** leia a [página oficial AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) e preencha o mesmo registo de verificação. Marque a descoberta e execução de ferramentas como «não executadas». Este percurso ensina a verificar fontes, mas não comprova o funcionamento do MCP.

## Praticar e verificar

**O seu resultado:** um registo de ligação com cinco linhas: nome do servidor, nome da ferramenta, URL da fonte, resultado observado e prova de remoção. Não inclua tokens nem identificadores de conta em capturas ou registos.

**Critério de conclusão:** o percurso ligado só passa depois de uma leitura real pela ferramenta e da remoção posterior da configuração. O percurso alternativo conclui o exercício de fontes com o MCP marcado como não executado.

## Verificar a compreensão

1. **Pergunta:** uma entrada MCP guardada prova que uma ferramenta funcionou? **Resposta:** não. Verifique a descoberta, as permissões e uma leitura real.
2. **Pergunta:** que custo de contexto adicional tem uma ligação MCP ampla? **Resposta:** as descrições e os esquemas das ferramentas consomem parte do contexto ativo.

## Resolução de problemas

- **Comando `codex` desconhecido:** instale ou atualize o Codex CLI através do guia oficial ligado.
- **Servidor listado, sem ferramenta:** inspecione o estado da sessão e os diagnósticos do servidor.
- **A chamada devolveu conteúdo sem relação:** restrinja a consulta e verifique a página de origem.
- **A remoção parece não resultar:** inicie uma sessão nova e consulte a lista de servidores ativos.

## Próximos passos

**Continue com [Verificação dos resultados da IA](/articles/effective-ai-output-verification/).** Para extensões mais amplas, leia o [guia do site sobre extensões do Claude Code e ferramentas MCP](/articles/claude-code-plugins-skills-mcp-tools/).

**Navegação do curso:** [Anterior: Gestão do contexto](/articles/effective-ai-context-window-management/), [Índice do curso](/effective-ai-course-start/).

---
title: "Projetos do ChatGPT e Claude: configure contexto de IA reutilizável"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Configure projetos do ChatGPT e Claude com instruções focadas, arquivos de referência atualizados e um teste simples do contexto reutilizado."
genre: ["Inteligência artificial", "Produtividade"]
tags: ["Projetos do ChatGPT", "Projetos do Claude", "instruções de projeto de IA", "contexto de IA", "configuração de projeto do ChatGPT", "conhecimento de projeto do Claude"]
cover: "/img/cover/effective-ai-chat-projects.webp"
coverAlt: "Dois espaços de trabalho de projetos de IA organizados com um resumo do projeto, arquivos de referência e conversas separadas"
coverCaption: ""
---

[Voltar ao curso Fluxo de Trabalho Prático com IA](/effective-ai-course-start/)

**Crie um projeto quando várias conversas tiverem o mesmo objetivo.** Reúna instruções estáveis e arquivos de referência aprovados em um só lugar. Mantenha cada conversa concentrada em uma tarefa. Esta lição usa uma oficina comunitária fictícia para praticar sem dados privados.

**Objetivo de aprendizagem:** você criará um projeto com duas fontes controladas e testará os fatos delas em um novo chat.

## Principais pontos

- **As instruções do projeto** definem comportamentos reutilizáveis para chats relacionados.
- **As fontes do projeto** guardam referências que você quer que o assistente consulte.
- **O histórico da conversa** registra uma troca, mas não substitui uma fonte aprovada.
- **Um teste em um chat novo** mostra se a configuração fornece contexto suficiente.

## Antes de começar

**Pré-requisitos:** uma conta do ChatGPT ou Claude e o pacote de tarefas da [lição 1](/articles/effective-ai-workflow-foundations/). Reserve 35 minutos. O nível é iniciante. Use nomes, datas e locais inventados durante toda a prática.

**Crie dois arquivos pequenos** no computador. Abra um editor de texto simples, cole cada bloco abaixo em um arquivo próprio e salve com o nome `.md` indicado. Arquivos Markdown são texto simples. `workshop-brief.md` informa o público e o estilo. `approved-schedule.md` contém a programação oficial fictícia.

```text
workshop-brief.md, revisão 1
Público: pessoas inscritas numa oficina introdutória.
Estilo: frases curtas e tom cordial e factual.
Não invente preços, recursos de acessibilidade ou informações sobre estacionamento.
```

```text
approved-schedule.md, revisão 1
Marcador da fonte: WS-2026-11-12-R1
Evento: Introdução à segurança digital
Data: 2026-11-12
Início: 7 p.m.
Local: Community Room A
```

## Configurar o ChatGPT

1. **Abra “Projects”** na barra lateral do ChatGPT e crie um projeto chamado `Workshop Practice`.
2. **Adicione os dois arquivos** como fontes do projeto.
3. **Abra as configurações do projeto** e inclua as instruções abaixo.
4. **Confira as configurações de memória e compartilhamento** da sua conta e espaço de trabalho antes de adicionar material real.

```text
Use approved-schedule.md para os factos do evento.
Use workshop-brief.md para o público e o estilo.
Se faltar um facto pedido, solicite a fonte ou assinale-o como desconhecido.
Escreva apenas rascunhos. Não os envie nem publique.
Liste as alterações factuais após cada rascunho revisto.
```

**Os projetos do ChatGPT reúnem chats, arquivos e instruções relacionados.** As configurações e os recursos disponíveis variam conforme o plano e o espaço de trabalho. Se o processo de criação oferecer memória exclusiva do projeto, escolha-a para um teste de isolamento limpo. Com a memória padrão, um chat pode usar informações fora dos arquivos enviados. O marcador único abaixo ajuda a testar o arquivo sem tratar uma resposta da memória como prova de leitura do arquivo. Consulte o [guia oficial de projetos do ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) para conferir as opções atuais de memória.

## Configurar o Claude

1. **Abra “Projects”** no Claude e crie um projeto com o mesmo nome de prática.
2. **Adicione os dois arquivos** ao conhecimento do projeto.
3. **Defina as mesmas cinco linhas** como instruções do projeto.
4. **Inicie um chat novo no projeto** para testar a configuração.

**Estas etapas descrevem os projetos clássicos do Claude.** A Anthropic está disponibilizando uma beta separada de Projects para alguns usuários Pro e Max do Claude Code. Na beta, um projeto é uma conversa com threads paralelas na nuvem. Consulte [O que são projetos](https://support.claude.com/en/articles/9517075-what-are-projects) e siga a interface da sua conta. As instruções dos projetos clássicos se aplicam a todos os chats, e o conhecimento do projeto fornece referências compartilhadas. Use os arquivos enviados como fatos controlados. O comportamento da memória do projeto varia por conta e configuração, então não trate os detalhes de outro chat como a programação aprovada. Consulte o [guia de configuração de projetos do Claude](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) para ver os controles atuais.

| Modo do projeto | Material compartilhado para conferir | Novo teste |
|---|---|---|
| **Projeto do ChatGPT** | Arquivos enviados, instruções e modo de memória selecionado | Um novo chat do projeto cita o marcador da programação |
| **Projeto clássico do Claude** | Conhecimento e instruções do projeto compartilhados entre chats | Um novo chat do projeto cita o marcador da programação |
| **Beta do Claude Projects** | Fontes e contexto no projeto e nas threads na nuvem | Uma nova thread do projeto cita o marcador da programação |

**Um projeto reúne contexto, mas não aprova uma fonte.** O marcador mostra se um arquivo nomeado chegou ao chat. Compare por conta própria a data, o horário e a sala com o arquivo.

## Testar um chat novo

**Abra uma nova conversa de projeto no ChatGPT ou um novo chat de projeto clássico do Claude.** Na beta do Claude Projects, use uma nova thread no projeto. Peça um anúncio breve. Não inclua a programação no prompt, para que as fontes do projeto forneçam os dados.

```text
Escreva um rascunho de e-mail com 100 palavras para a próxima oficina.
Indique o ficheiro de origem e o marcador exato para a hora e o local.
Liste os dados em falta depois do rascunho.
Não envie a mensagem.
```

| Resultado | Significado | Próxima ação |
|---|---|---|
| **Horário, local e marcador correspondem** | O arquivo está disponível para este chat | Confira você mesmo os fatos no arquivo |
| **Um fato foi inventado** | As instruções ou o uso da fonte falharam | Remova o fato e restrinja a solicitação |
| **A fonte está ausente** | A referência não chegou a este chat | Confira a participação no projeto e o envio do arquivo |
| **Aparece uma revisão antiga** | O projeto contém material desatualizado | Substitua a fonte e teste novamente |

**Não deduza confiabilidade de uma única resposta correta.** A memória padrão do projeto pode fornecer um horário familiar sem ler o arquivo enviado. Exija o marcador exato `WS-2026-11-12-R1` e repita o teste com este rascunho conflitante:

```text
Revise esta frase segundo o calendário aprovado do projeto:
«A aula Introdução à segurança digital começa às 6 p.m. em Community Room A.»
Indique a alteração factual, o ficheiro de origem e o marcador. Não envie a mensagem.
```

**Resposta esperada:** a linha informa 19h e cita `approved-schedule.md` com o marcador `WS-2026-11-12-R1`. Registre qualquer falha observada. Um teste aprovado não precisa de uma falha inventada.

**Exemplo de registro do teste:** chat novo, primeiro prompt, horário 19h, local Community Room A, fonte `approved-schedule.md`, marcador `WS-2026-11-12-R1`, aprovado. Prompt conflitante, correção de 18h para 19h, aprovado. Este é um exemplo. Substitua-o pelas suas observações.

## Manter o projeto

**Mantenha curtas as instruções do projeto.** Coloque ali as regras estáveis. Inclua detalhes específicos de cada tarefa em seu prompt. Substitua arquivos desatualizados e identifique suas revisões. Separe trabalhos sem relação em outro projeto para evitar conflito entre fontes.

**Antes de compartilhar um projeto,** confira seus arquivos, chats, instruções e lista de acesso. Um projeto é um espaço de trabalho, não um sistema de aprovação. Mesmo um arquivo chamado “approved” precisa de um responsável real e de um registro de revisão para tarefas importantes.

## Praticar e conferir

**Seu resultado:** um projeto com dois arquivos de fonte sintéticos, cinco linhas de instruções e um breve registro de teste. Anote o horário e local observados, o nome e o marcador da fonte e qualquer fato inventado. Exclua o projeto de prática quando terminar, se não precisar mais dele.

**Raciocínio esperado:** um chat novo usa as fontes do projeto para fatos estáveis, enquanto seu prompt define a saída imediata. Confira a resposta no arquivo. Se faltar uma fonte ou aparecer uma revisão errada, volte à configuração do projeto.

## Verificar o entendimento

1. **Pergunta:** um novo chat de projeto do ChatGPT garante isolamento em qualquer configuração de memória? **Resposta:** não. Confira o modo de memória do projeto e teste com um marcador de fonte exclusivo.

2. **Pergunta:** o que fazer quando o projeto repete uma programação antiga? **Resposta:** confira a fonte anexada e o alcance da memória, depois substitua o material desatualizado.

## Solução de problemas

- **Controles do projeto ausentes:** confira seu plano atual e as configurações do espaço de trabalho no guia do fornecedor.
- **Respostas conflitantes:** remova arquivos de fonte duplicados ou desatualizados e inicie um novo chat.
- **Compartilhamento inesperado:** confira os membros do projeto e remova fontes confidenciais antes de continuar.
- **Desvio de estilo recorrente:** encurte as instruções e forneça um exemplo breve no prompt da tarefa.

## Próximas etapas

**Continue com [Contexto do repositório AGENTS.md](/articles/effective-ai-agents-md-context/)**. A próxima lição passa de um projeto de chat para um repositório de código local.

**Navegação do curso:** [Anterior: Fundamentos do fluxo de trabalho](/articles/effective-ai-workflow-foundations/), [Visão geral do curso](/effective-ai-course-start/).

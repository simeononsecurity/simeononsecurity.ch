---
title: "Qual modelo de IA local você deve executar? Guia de GPU, contexto e programação para outubro de 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Um guia prático de outubro de 2026 para escolher modelos de IA locais para agentes de programação. Compare memória da GPU, crescimento do KV cache, tamanho do contexto, qualidade da quantização, processamento de prompts, configurações de raciocínio e custos de aluguel na nuvem."
genre: ["IA local", "Hardware de IA", "IA autohospedada", "Benchmark de GPU", "Ferramentas de desenvolvimento", "Economia de IA"]
tags: ["modelos de IA locais", "agentes de programação", "guia de GPU", "VRAM", "KV cache", "janela de contexto", "Qwen 27B", "mixture of experts", "quantização", "llama.cpp", "Ollama", "decodificação especulativa", "predição de múltiplos tokens", "LLM local", "aluguel de GPU", "workstation de IA", "programação com agentes", "processamento de prompts", "velocidade de inferência"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Uma workstation mostrando escolhas de modelos de IA locais, uso de memória da GPU e janelas de contexto de agentes de programação"
coverCaption: ""
ref: ["/articles/32gb-vram-qwen-27b-hardware-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark", "/articles/local-ai-2026-build-your-rig-now"]
---

**O melhor modelo local para programação é aquele que mantém memória suficiente do seu projeto e o lê rápido o bastante para continuar útil.** O tamanho do modelo ainda importa. Um modelo que só cabe depois de usar RAM do sistema costuma parecer pior que um modelo menor com uma janela de contexto estável.

*Escolha o modelo e o orçamento de memória juntos. Não escolha um modelo de uma lista de níveis e depois o force em hardware inadequado.*

Este guia se concentra em agentes de programação, não em prompts curtos de autocomplete. Um agente lê arquivos, saídas de ferramentas, erros do compilador e resultados de testes antes de escrever uma correção. Essas entradas consomem contexto e mudam a decisão de hardware.

## O vídeo é uma referência

O vídeo a seguir compara modelos locais em vários níveis de memória de GPU. Ele é útil pelas observações práticas sobre seleção de modelos e pelos resultados de hardware relatados. Este artigo organiza a decisão por comportamento da memória, contexto do agente, processamento de prompts e custo total de propriedade.

{{< youtube id="C9M6iUFtVB4" enable="true" title="Testei todos os modelos de IA locais para que você não precisasse" description="Comparação prática de modelos de IA locais em vários níveis de memória de GPU, com atenção a cargas de programação e limites de hardware." >}}

## Por que listas de níveis falham

Uma lista de níveis de modelos costuma relacionar a quantidade de parâmetros a um número de memória da GPU. Esse atalho ajuda em uma primeira estimativa. Ele deixa de ajudar quando um agente de programação começa a ler um repositório real.

Os pesos do modelo são a primeira alocação. O **KV cache** é a alocação que cresce. Ele armazena chaves e valores de attention do contexto ativo para que o runtime não precise recalcular o prompt inteiro depois de cada token gerado.

| Consumidor de memória | O que armazena | Por que importa |
|---|---|---|
| **Pesos do modelo** | Parâmetros quantizados | Requisito de carregamento único |
| **KV cache** | Informações do contexto ativo | Cresce com o prompt e a conversa |
| **Buffers do runtime** | Espaço temporário de computação | Varia com o backend e o tamanho do batch |
| **Instruções do agente** | Prompts do sistema e definições de ferramentas | Usa contexto antes da chegada dos arquivos do projeto |

**O arquivo do modelo caber na placa não prova que o agente será utilizável.** O runtime precisa de espaço para o cache, buffers temporários, definições de ferramentas e a próxima resposta.

## Contexto é o orçamento real

Agentes de programação gastam contexto com mais do que arquivos-fonte. O orçamento também inclui instruções do sistema, esquemas de ferramentas, listas de diretórios, saída do shell, mensagens do compilador, resultados de testes e turnos anteriores da conversa.

Três conexões MCP com definições detalhadas de ferramentas costumam consumir vários milhares de tokens antes de o agente abrir um arquivo do projeto. Um contexto padrão pequeno deixa pouco espaço para código. O agente ainda responde, mas perde o conjunto de trabalho necessário para correções em várias etapas.

A [runtime FAQ do Ollama](https://docs.ollama.com/faq) lista um contexto padrão de 4.096 tokens. A configuração `OLLAMA_CONTEXT_LENGTH` muda o padrão, enquanto `OLLAMA_NUM_PARALLEL` aumenta a memória exigida conforme o número de solicitações simultâneas. Registre os dois valores antes de comparar um benchmark local com um resultado de solicitação única.

```bash
OLLAMA_CONTEXT_LENGTH=32768 OLLAMA_NUM_PARALLEL=1 ollama serve
```

Este exemplo define um padrão de 32K para uma solicitação ativa. Ele não reserva 32K tokens para arquivos do projeto. Instruções, definições de ferramentas, entrada e saída continuam compartilhando a janela.

### Um registro simples de contexto

Antes de comparar GPUs, registre estes valores:

- **Tamanho do projeto:** arquivos e número aproximado de linhas de código em uma tarefa normal.
- **Sobrecarga das ferramentas:** prompt do sistema, esquemas MCP, ferramentas do shell e instruções do editor.
- **Carga do erro:** tamanho normal da saída do compilador e dos testes.
- **Contexto-alvo:** o maior prompt que você quer manter sem truncamento.
- **Espaço para resposta:** espaço reservado para o patch planejado e a explicação.

Use o resultado como especificação de carga. Um desenvolvedor que edita um arquivo por vez tem uma necessidade de memória diferente de quem pede a um agente para rastrear uma API por um monorepo.

## KV cache muda a classificação

Dois modelos com contagens de parâmetros semelhantes costumam ter custos de contexto diferentes. Um modelo denso com todas as camadas contribuindo para o cache crescente pode precisar de mais memória que um modelo com design de attention híbrida.

Um modelo de programação 27B discutido no material de referência usa um conjunto limitado de camadas com attention completa, enquanto outras camadas usam um resumo de tamanho fixo. O custo relatado para contexto de 128K fica abaixo de 9GB para o cache. Um modelo de tamanho semelhante com attention completa crescente em todas as camadas precisa, segundo o relato, de mais de 21GB no mesmo comprimento de contexto.

Esses números descrevem arquiteturas específicas e configurações específicas de runtime. Use-os como motivo para inspecionar a arquitetura, não como uma fórmula universal de memória.

| Comportamento do modelo | Efeito no contexto | Implicação para o hardware |
|---|---|---|
| **Attention completa em todas as camadas** | Grande crescimento do cache | Precisa de mais memória para prompts longos |
| **Attention híbrida ou deslizante** | Menor crescimento do cache em algumas camadas | Mais espaço de contexto no mesmo tamanho de modelo |
| **Mixture of experts** | Menos parâmetros ativos por token | Menos computação por token, mas todos os pesos ainda precisam de armazenamento |
| **Extensão de contexto longo** | Janela de trabalho maior | Mais memória de cache e mais processamento de prompts |

**Leia a arquitetura antes de comprar memória.** A contagem de parâmetros sozinha esconde o custo de uma sessão longa de programação.

## Escolha pela faixa de memória da GPU

### Quatro a oito GB

Modelos densos pequenos continuam sendo a escolha prática. Eles cabem na placa, respondem rápido e funcionam bem para autocomplete, explicações curtas e edições pequenas de arquivos.

Um modelo maior com CPU offload pode produzir texto, mas o tempo de resposta costuma virar o limite. Um agente de programação precisa repetir leituras de arquivos e chamadas de ferramentas. Uma configuração de quatro tokens por segundo transforma cada correção em uma espera longa, mesmo quando o modelo roda tecnicamente.

Modelos mixture-of-experts oferecem outro caminho. Uma pequena parte ativa reduz a pressão de computação, enquanto o conjunto completo de pesos permanece parcialmente na memória do sistema. Essa abordagem favorece um sistema com bastante RAM e caminhos de transferência rápidos.

| Carga de trabalho | Direção sugerida |
|---|---|
| **Autocomplete** | Modelo denso pequeno com prompt curto |
| **Edições de um arquivo** | Modelo instruct pequeno com suporte a ferramentas |
| **Agente para todo o repositório** | Alugue uma GPU maior ou aumente a memória do sistema primeiro |
| **Código privado sob NDA** | Use um modelo local, aceitando escopo menor ou execuções mais lentas |

**Nesta faixa, compre RAM do sistema antes de perseguir um modelo grande.** Um modelo pequeno estável supera um modelo grande que passa a maior parte do tempo movendo dados pelo barramento.

### Doze a dezesseis GB

Esta faixa abre espaço para um modelo de programação 27B, mas a escolha da quantização passa a ser central. Um build 4-bit padrão de cerca de 17GB não cabe em uma placa de 16GB depois da sobrecarga do runtime.

Um build 3-bit de cerca de 13GB deixa mais espaço para o contexto. Uma placa de 12GB empurra a escolha para um build 2-bit ou para um modelo mixture-of-experts menor. A qualidade depende do quantizador e do processo de calibração específicos, então dois uploads com a mesma profundidade de bits costumam gerar resultados de programação diferentes.

Confira antes de baixar um modelo quantizado:

- **Autor do quantizador e notas da versão**
- **Dados de calibração e resultados de avaliação**
- **Compatibilidade do tokenizer**
- **Testes de chamadas de ferramentas**
- **Comprimento do contexto na quantização escolhida**
- **Suporte no Ollama, llama.cpp ou front end selecionado**

**Não trate “2-bit” ou “3-bit” como descrição completa de qualidade.** O método de empacotamento e o registro de calibração importam.

### Vinte e quatro a trinta e dois GB

Esta é a faixa mais flexível para um modelo de programação 27B. Uma placa de 24GB costuma comportar um build 4-bit com contexto útil, mas uma janela completa de 128K pode superar a memória restante. Uma placa de 32GB oferece mais espaço ao runtime para o cache e alocações temporárias.

Esta faixa também facilita justificar a propriedade. Uma GPU cuida da carga sem a complexidade de dividir entre duas placas. O sistema usa menos energia que uma configuração multi-GPU, e o suporte de software é mais fácil de testar.

| Capacidade | Posição prática |
|---|---|
| **24GB** | Modelo 4-bit forte com limites de contexto a medir |
| **32GB** | Modelo 4-bit ou 6-bit 27B com mais espaço para contexto |
| **48GB** | Maior precisão ou cache maior sem mudar o modelo principal |

**A faixa de 24GB a 32GB é a zona de compra sensata para programação privada frequente.** Ela evita o pior comportamento de offload sem exigir hardware de datacenter em um gabinete desktop.

### Quarenta e oito GB ou mais

Mais memória não significa automaticamente um modelo novo. O mesmo modelo 27B pode rodar com precisão 8-bit em uma placa de 48GB, com cache maior e menos compromissos. A melhoria está na consistência, no espaço de contexto e na qualidade da saída, não em um novo nível de raciocínio.

Com 128GB, a decisão muda. Um modelo mixture-of-experts muito maior se torna possível, mas o processamento do prompt vira uma preocupação séria. O modelo costuma gerar rápido e levar muito tempo para ingerir um repositório grande ou um resultado novo de ferramenta.

**Para modelos grandes, meça a velocidade de prefill separadamente da velocidade de decode.** Uma resposta rápida depois de uma leitura lenta do prompt ainda parece lenta no fluxo de um agente.

## Velocidade de decode é apenas metade do teste

**Velocidade de decode** mede tokens gerados por segundo. Ela responde: “Com que velocidade o modelo escreve?”. **Velocidade de prefill** mede o processamento do prompt. Ela responde: “Com que velocidade o modelo lê?”.

Um agente passa muito tempo lendo. Cada chamada de ferramenta adiciona texto. Um arquivo-fonte longo, stack trace ou log de teste entra no prompt antes do início da próxima resposta.

| Métrica | Experiência do usuário |
|---|---|
| **Tokens de decode por segundo** | Rapidez com que a resposta aparece após o processamento |
| **Tokens do prompt por segundo** | Quanto tempo o agente espera antes do início da resposta |
| **Tempo até o primeiro token** | Atraso combinado do processamento do prompt e da preparação |
| **Retenção de contexto** | Quanto do estado do projeto permanece disponível durante a tarefa |

**Faça benchmark com seus próprios tamanhos de prompt.** Um prompt sintético curto esconde o custo mais importante no trabalho com repositórios.

## Primeiro, configurações gratuitas do runtime

Upgrade de hardware não é o primeiro passo de desempenho. Teste as configurações do runtime antes de abrir uma página de compras.

### Predição de múltiplos tokens

Algumas combinações de modelo e backend preveem vários tokens futuros e depois os verificam em uma passagem. O recurso costuma aparecer como uma flag de runtime ou uma configuração de draft compatível.

Testes relatados no material de referência mostram ganhos grandes em algumas placas de alto desempenho. Os resultados variam conforme o arquivo do modelo, backend, driver e placa. Caminhos Apple Metal talvez não preservem o recurso necessário durante a conversão.

### Nível de raciocínio

Um modelo enviado com raciocínio máximo ativado passa mais tempo no trabalho interno antes de retornar um resultado. Raciocínio médio costuma equilibrar melhor a correção de código, sobretudo quando a tarefa já inclui uma mensagem de erro clara e um arquivo-alvo específico.

Use uma matriz de teste simples:

1. Execute a mesma tarefa de correção com raciocínio baixo, médio e alto.
2. Registre tempo até o primeiro token, tempo total, sucesso do patch e resultado do teste.
3. Repita com um prompt curto e um prompt do tamanho do repositório.
4. Mantenha a configuração que produz a melhor tarefa concluída, não a maior taxa de tokens.

**Raciocínio médio com um caminho compatível de múltiplos tokens é um bom ponto de partida.** Verifique a qualidade no seu código antes de torná-lo padrão.

## Hardware local ou GPU alugada?

Computação alugada vence para trabalho ocasional. Você paga pelas sessões ativas em vez de comprar, resfriar, atualizar e alimentar uma placa o ano inteiro.

Hardware próprio vence quando a carga é frequente, privada ou offline. Ele também elimina tempo de fila e fornece um ambiente estável para testes repetíveis.

| Situação | Melhor primeiro passo |
|---|---|
| **Poucas sessões por mês** | Alugue uma GPU ou use uma API |
| **Programação privada diária** | Compre um sistema compatível de 24GB a 32GB |
| **Repositório grande com recargas frequentes** | Alugue primeiro e meça a velocidade de prefill |
| **Nenhum código sai do local** | Tenha o menor sistema que atenda ao contexto-alvo |
| **Experimentação com um modelo novo** | Alugue antes de comprar hardware |

Calcule o ponto de equilíbrio com horas ativas, não horas do calendário. Inclua eletricidade, armazenamento, refrigeração, manutenção e o tempo necessário para manter o runtime funcionando.

**Uma GPU de alto nível comprada para experimentação ocasional é uma despesa de hobby.** Um sistema de 24GB a 32GB usado todos os dias para trabalho privado tem uma justificativa econômica mais forte.

## Uma lista de compra melhor

Use esta ordem ao comparar um modelo e uma GPU:

1. **Defina a tarefa.** Autocomplete, correção de um arquivo, agente de repositório ou análise de contexto longo.
2. **Meça o prompt.** Conte instruções normais do sistema, esquemas de ferramentas, arquivos e saída de testes.
3. **Inspecione o comportamento do cache.** Procure notas da arquitetura e medições de memória de contexto.
4. **Escolha uma quantização.** Confira resultados de qualidade do upload específico, não só a quantidade de bits.
5. **Teste prefill e decode.** Use prompts do seu próprio repositório.
6. **Ajuste o raciocínio.** Compare o tempo de tarefa concluída em vários níveis de raciocínio.
7. **Teste privacidade e manutenção.** Confirme para onde o código-fonte viaja e quem mantém o backend.
8. **Compare o custo do aluguel.** Use horas ativas esperadas e inclua energia na estimativa do sistema próprio.

## Recomendação final

**Abaixo de 12GB, execute um modelo menor ou um modelo mixture-of-experts com RAM suficiente.** Não force um modelo denso 27B em uma configuração que passa a maior parte do tempo fazendo offload.

**De 12GB a 16GB, concentre-se na qualidade da quantização e em um contexto-alvo controlado.** Um build 2-bit ou 3-bit bem testado com suporte a ferramentas é mais útil que um arquivo 4-bit que nunca cabe de forma limpa.

**De 24GB a 32GB, um modelo de programação 27B vira o padrão prático para trabalho privado diário.** Meça o uso do contexto e a velocidade do prompt antes de presumir que toda a janela anunciada está disponível.

**Com 48GB ou mais, use a memória extra para precisão, espaço de cache e sessões estáveis antes de migrar para um modelo maior.** Quando o modelo passa para a faixa de 128GB, a velocidade de leitura do prompt e a economia do aluguel merecem mais atenção que a capacidade bruta.

O nome do modelo é apenas o ponto de partida. A pergunta útil é quanto contexto do projeto sobra depois que o modelo, o runtime, as ferramentas e o cache ficam com suas partes.

## Leituras relacionadas

- [32GB de VRAM para Qwen 27B: guia de hardware para IA local](/articles/32gb-vram-qwen-27b-hardware-guide/), focado nos caminhos de hardware para uma carga 27B.
- [Benchmarks de GPU Llama 3.1 8B e Qwen3.8 27B na Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/), resultados medidos de GPUs alugadas e limites de contexto longo.
- [IA local em 2026: um modelo 27B supera o Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/), qualidade do modelo, quantização e economia do hardware local.

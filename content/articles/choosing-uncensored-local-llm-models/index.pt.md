---
title: "Como escolher um modelo local de IA sem censura"
date: 2026-11-15
lastmod: 2026-11-15
toc: true
draft: false
description: "Compare variantes locais pela conclusão das respostas, capacidades preservadas, uso do contexto, quantização e VRAM necessária."
genre: ["IA local", "IA autoalojada", "Segurança de IA", "Equipamento de GPU"]
tags: ["IA local sem censura", "abliteração", "LLM local", "VRAM", "comprimento do contexto", "quantização", "Ollama", "Qwen3.8", "Gemma 4"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Estação de trabalho local de IA com uma placa gráfica e monitores que mostram visualizações de modelos e inferência"
coverCaption: ""
ref: ["/articles/local-ai-model-gpu-context-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark"]
---

**Escolha do modelo:** avalie cada variante pelas respostas úteis que conclui, pela qualidade que preserva e pela memória necessária para a sua carga de trabalho. Um número baixo de recusas ou um cartão de modelo popular não comprova esses resultados.

A etiqueta **sem censura** não tem uma escala de desempenho padrão. Os publicadores usam-na para diferentes edições de pesos, ajustes finos e modelos de conversa. Compare cada candidato com o modelo original e teste-o nas tarefas que pretende executar.

{{< youtube id="j-VqPVjztJE" enable="true" title="Testei todos os modelos locais de IA sem censura (de 8 GB a 32 GB de VRAM)" description="Comparação de variantes de modelos locais, conclusão das respostas, definições de contexto e níveis de memória GPU." >}}

## O que a etiqueta indica

Um **modelo abliterado** teve os pesos alterados para modificar alguns comportamentos de recusa. O artigo de 2024 sobre a direção da recusa demonstrou um método em 13 modelos de conversa abertos. As ferramentas mais recentes oferecem outras abordagens. Por exemplo, Heretic 2 documenta tanto a ablação de posto arbitrário como a ablação direcional. A etiqueta do cartão do modelo não indica que comportamento mudou nem o efeito da edição.

Separe estas quatro propriedades ao comparar modelos:

| Propriedade | O que verificar |
|---|---|
| **Comportamento de recusa** | Que pedidos recebem uma recusa, uma resposta parcial ou uma resposta completa? |
| **Capacidades preservadas** | Como se comparam as tarefas factuais, de raciocínio, programação e formatação com o modelo original? |
| **Conclusão da resposta** | Com que frequência a geração termina antes do limite de tokens ou de tempo? |
| **Compatibilidade com o ambiente de execução** | O ficheiro quantizado exato funciona com memória suficiente para o contexto necessário? |

Um modelo editado continua a ser probabilístico. **Separe as verificações de qualidade:** precisão, fiabilidade e utilização segura. Mantenha disponível um modelo normalmente alinhado para tarefas em que as proteções são importantes.

## Porque é que a contagem de recusas é uma classificação fraca

**Uma pontuação de recusa** mede um resultado num conjunto de pedidos. Diz pouco sobre a precisão factual, a extensão das respostas ou se o modelo produz uma resposta final antes de esgotar o orçamento de geração.

**A comparação de Qwen3.8-27B de Sapwell, em setembro de 2026,** testou o modelo base e oito variantes com a mesma configuração de serviço. O conjunto de 13 tarefas mediu conhecimentos, matemática, programação e veracidade. Um conjunto HarmBench separado continha 400 pedidos prejudiciais, e um avaliador LLM analisou as respostas completas. Estes resultados abrangem uma família de modelos, uma GPU e um desenho de avaliação.

| Variante Qwen3.8-27B no estudo | Recusas explícitas em 400 pedidos | Respostas com raciocínio inacabado |
|---|---:|---:|
| **Modelo base** | 381 | 0% |
| **OrcaRouter** | 2 | 38% |
| **Trohrbaugh** | 122 | 15% |

O elevado número de recusas do modelo base coincidiu com menos respostas inacabadas. O baixo número de recusas do OrcaRouter coincidiu com uma taxa superior de respostas incompletas. O Trohrbaugh manteve mais recusas e produziu menos respostas incompletas. **Escolha em função da tarefa e dos compromissos que aceita.**

**Um estudo de 23 variantes Gemma 4 E4B** encontrou perdas substanciais em algumas medidas de capacidade na variante mais transferida, enquanto uma edição menor se manteve próxima do modelo base no teste. Popularidade e número de transferências descrevem a adoção. Não medem a qualidade.

Não reúna estas medições numa única pontuação. **Separe as medidas:** recusa, conclusão, correção e latência. Registe também o conjunto de pedidos, a revisão do modelo, o modelo de conversa, o ambiente de execução, o contexto e o limite de saída. Alterar qualquer uma destas definições muda o significado da comparação.

## Diagnostique respostas vazias antes de substituir um modelo

**Os tokens de raciocínio** contam para o limite de saída antes de surgir texto visível. Se o limite terminar durante o raciocínio interno, alguns ambientes devolvem uma resposta vazia ou truncada. Este resultado difere de uma recusa ou de uma resposta completa mas errada.

**O benchmark Qwen3.6-27B de Sapwell** mostrou como isto afeta os resultados principais. As pontuações brutas de matemática variaram muito porque algumas execuções nunca chegaram à resposta final. Entre as respostas concluídas, os valores de precisão medidos ficaram muito mais próximos. O benchmark separou a capacidade de resposta do esgotamento do orçamento de raciocínio.

**Se uma resposta estiver vazia, verifique o motivo de paragem e os registos do ambiente.** Registe a dimensão do pedido, a alocação do contexto, o limite de tokens de saída, o tempo decorrido e se o modelo produziu um marcador de resposta final. Depois, repita o pedido com um limite de saída maior se o equipamento tiver memória disponível.

| Resultado | Categoria provável a investigar |
|---|---|
| **Texto de recusa** | O modelo recusou o pedido. |
| **Saída vazia no limite de tokens** | A geração esgotou o orçamento de saída antes de uma resposta final. |
| **Saída truncada** | O limite de geração interrompeu uma resposta incompleta. |
| **Erro do ambiente** | O servidor, o ficheiro do modelo ou a alocação de memória falhou. |
| **Resposta completa mas errada** | O modelo devolveu texto, mas não passou na verificação de correção. |

**Saída vazia:** confirme o resultado do ambiente antes de considerar cada caso um defeito do modelo. Uma janela de contexto maior não corrige automaticamente um limite de saída pequeno, um modelo de conversa mal formado ou o tempo limite da aplicação.

## Reserve VRAM para pesos e contexto

O ficheiro do modelo é apenas um consumidor de memória. O ambiente também precisa de espaço para a **cache KV**, que guarda o estado de atenção do pedido e da resposta ativos, além dos buffers de cálculo e de outros processos carregados. Aumentar o comprimento do contexto aumenta o uso de memória.

**A documentação atual do Ollama** indica janelas de contexto predefinidas de 4K abaixo de 24 GiB de VRAM, 32K entre 24 e 48 GiB e 256K a partir de 48 GiB. Estes valores descrevem o comportamento predefinido do ambiente. Verifique o contexto atribuído e a colocação do processador com `ollama ps`.

**Exemplo para Linux:** este comando define 16K como valor predefinido para novas sessões do servidor Ollama:

```bash
OLLAMA_CONTEXT_LENGTH=16384 ollama serve
```

**Verifique o contexto atribuído** face aos tamanhos normais de entrada e resposta com o modelo carregado:

```bash
ollama ps
```

As colunas `CONTEXT` e `PROCESSOR` mostram a atribuição e se o modelo está na GPU ou parcialmente descarregado. **Atribuição de contexto:** um limite listado não garante que a janela inteira caiba na VRAM.

### Pontos de partida por memória GPU

**Candidatos iniciais:** estas famílias de modelos surgiram em comparações de variantes de 2026. As dimensões dos ficheiros vêm de repositórios quantizados específicos. Confirme o ficheiro exato, o suporte do ambiente e a memória medida antes de considerar um candidato adequado.

| Memória GPU | Candidato inicial | Restrição principal |
|---|---|---|
| **8 GB** | Gemma 4 E4B, como a variante `coder3101` | Mantém pequeno o ficheiro de pesos. Reserve memória para o contexto e os buffers do ambiente. |
| **12 GB** | Gemma 4 12B, como o ficheiro GGUF Q4 de 7,4 GB da `TrevorJS` | Oferece mais capacidade ao modelo, mas menos espaço para contexto longo do que uma variante menor. |
| **16 GB** | Um modelo menor ou um ficheiro Q3 de Qwen3.8-27B | O repositório de Qwen indica 13,72 GB para Q3_K_S. O publicador classifica este ficheiro como de baixa qualidade. O espaço para contexto será limitado. |
| **24 GB** | Qwen3.8-27B Q4_K_S ou Q4_K_M | O repositório atual indica ficheiros de 16,71 GB e 17,77 GB. Reserve espaço para cache e buffers. |
| **32 GB** | Qwen3.8-27B Q6_K | O repositório atual indica um ficheiro de 23,46 GB. Um ficheiro maior deixa menos memória para contexto do que uma quantização menor. |

*Use estas opções como ponto de partida. Os repositórios e as versões mudam, e a dimensão do ficheiro, por si só, não prevê a atribuição de memória pelo ambiente nem a qualidade da resposta.*

Os rótulos de quantização GGUF resumem uma escolha de codificação. **Diferenças entre repositórios:** ficheiros com a mesma profundidade nominal de bits não garantem qualidade equivalente. Um repositório de Qwen classifica Q3_K_S como de baixa qualidade e Q4_K_M como a opção predefinida. Antes de transferir, verifique o tamanho exato, o cartão do modelo, o formato do pedido e os resultados dos testes.

**Para calcular o tamanho da cache e verificar a compatibilidade com uma GPU local,** consulte o [guia de modelos locais, GPU e contexto](/articles/local-ai-model-gpu-context-guide/). As recomendações centram-se em tarefas de programação. Esta página centra-se no comportamento de recusa alterado e na avaliação.

## Examine o modelo de conversa e a origem do modelo

Um **modelo de conversa** envolve as mensagens em tokens e instruções esperados pelo modelo. Um pacote pode incluir um modelo personalizado ou uma instrução de sistema. Estas alterações afetam o comportamento medido, mesmo quando os pesos subjacentes não mudam.

**Efeito do modelo:** Sapwell encontrou uma variante Qwen3.8 cujo pacote incluía uma personalidade a instruir o modelo para nunca recusar nem avisar. A alegação de poucas recusas dependia do modelo de conversa. A comparação uniformizou os modelos de conversa para realçar as diferenças entre os pesos. Este controlo não demonstra que o modelo fornecido seja malicioso ou inutilizável.

**Antes de instalar:** verifique o publicador, o modelo base, a licença, o processo de conversão, o quantizador, o modelo de conversa e o histórico de revisões. Compare com o modelo original usando o mesmo modelo de conversa e ambiente. Se o cartão do modelo não indicar o método ou a configuração de teste, registe a origem como desconhecida.

## Execute uma pequena avaliação para a sua carga de trabalho

**Crie um conjunto de pedidos repetível** com tarefas comuns que lhe pertençam ou para as quais tenha autorização de teste. Inclua o trabalho que o modelo fará, perguntas factuais com respostas conhecidas e pedidos de formatação com critérios claros de aprovação. Acrescente alguns casos-limite seguros para incluir o comportamento de recusa na decisão.

**Mantenha as definições de teste constantes** entre o modelo original e a variante editada. Não altere a instrução do sistema, o modelo de conversa, a quantização, a versão do ambiente, o contexto, o limite de saída nem as definições de amostragem. Guarde a revisão do modelo ou o hash do ficheiro com os resultados.

Registe cada resultado separadamente:

- **Conclusão:** resposta final, recusa, saída vazia, truncagem ou erro do ambiente.
- **Correção:** aprovado ou reprovado segundo uma resposta esperada ou uma grelha de avaliação.
- **Utilidade:** se a resposta satisfaz os requisitos da tarefa.
- **Latência:** tempo até ao primeiro token e tempo total de geração.
- **Memória:** contexto atribuído, colocação na GPU e VRAM máxima.
- **Comportamento de segurança:** recusa ou continuação apropriadas em cada caso-limite.

Repita o conjunto depois de alterar uma variável. Se a resposta terminar após aumentar o limite de saída, a primeira falha deveu-se ao orçamento. Se as respostas continuarem incompletas, examine o modelo de conversa, o modo de raciocínio, o ambiente e a revisão do modelo. **Mantenha a variante apenas se melhorar a tarefa pretendida sem perdas inaceitáveis de precisão ou segurança.**

## Mantenha a implementação isolada

**Privacidade:** a inferência local depende de toda a sua pilha. Verifique a interface, os registos, as extensões, a telemetria e os percursos de rede. Trate pesos não confiáveis e modelos de conversa personalizados como código e configuração de terceiros.

**Acesso público:** nunca exponha diretamente o ponto final do modelo à Internet pública. Isole o acesso às ferramentas e use variantes editadas apenas em trabalho autorizado. Para acesso remoto, coloque o ponto final atrás de um gateway privado com autenticação, limites de pedidos e isolamento de rede. O artigo original sobre a direção de recusa indica as implicações de segurança de edições que removem recusas.

## Conclusão

**Regra de decisão:** escolha o modelo com os resultados verificados mais fortes no seu próprio conjunto de tarefas. Use a contagem de recusas como uma medida e depois verifique a conclusão das respostas, a correção, o comportamento do modelo e a margem de VRAM. Comece com um ficheiro adequado à sua GPU, defina o contexto para a carga de trabalho e compare-o com o modelo original usando definições idênticas.

**Para dimensionar a GPU,** compare estes resultados com o [benchmark de aluguer de GPU para Qwen 27B](/articles/qwen38-27b-vast-ai-gpu-benchmark/). Alugue ou peça equipamento emprestado antes de o comprar se tiver dúvidas sobre o ficheiro exato do modelo ou o contexto pretendido.

## Fontes

- [Benchmark de abliteração Qwen3.8-27B](https://nathan.sapwell.net/posts/qwen38-27b-abliteration/), Nathan Sapwell, 6 de setembro de 2026.
- [Benchmark de abliteração Qwen3.6-27B](https://nathan.sapwell.net/posts/qwen36-27b-abliteration/), Nathan Sapwell, 2026-05-17.
- [Benchmark das variantes Gemma 4 E4B](https://nathan.sapwell.net/posts/gemma4-e4b-abliteration/), Nathan Sapwell, 1 de agosto de 2026.
- [Benchmark das variantes Gemma 4 12B](https://nathan.sapwell.net/posts/gemma4-12b-abliteration/), Nathan Sapwell, 28 de agosto de 2026.
- [A recusa em modelos de linguagem é mediada por uma única direção](https://arxiv.org/abs/2406.11717), Arditi et al., 2024.
- [Documentação do projeto Heretic](https://github.com/p-e-w/heretic/).
- [Cartão oficial do modelo Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B).
- [Documentação do Ollama sobre comprimento do contexto](https://docs.ollama.com/context-length).
- [Cartão do modelo Gemma 4 E4B `coder3101`](https://huggingface.co/coder3101/gemma-4-E4B-it-heretic).
- [Ficheiros GGUF Gemma 4 12B da TrevorJS](https://huggingface.co/TrevorJS/gemma-4-12B-it-uncensored-GGUF).
- [Ficheiros GGUF OrcaRouter Qwen3.8-27B](https://huggingface.co/bartowski/orcarouter_Qwen3.8-27B-Uncensored-GGUF).
- [Formato GGUF e tipos de quantização](https://huggingface.co/docs/hub/en/gguf), documentação Hugging Face.
- [Fonte em vídeo: Testei todos os modelos locais de IA sem censura (de 8 GB a 32 GB de VRAM)](https://www.youtube.com/watch?v=j-VqPVjztJE).

---
title: "Quais modelos de IA funcionam num Raspberry Pi 4 ou 5?"
date: 2026-09-20
lastmod: 2026-11-07
toc: true
draft: false
description: "Use medições no Raspberry Pi 4 e 5 para escolher modelos de linguagem locais por memória, velocidade e carga de trabalho, dos pequenos LFM2.5 às opções 3B e maiores."
genre: ["Raspberry Pi", "Inteligência artificial", "Auto-hospedagem"]
tags: ["Raspberry Pi 4", "Raspberry Pi 5", "IA local", "modelos de linguagem pequenos", "Ollama", "GGUF", "LFM2.5", "Qwen2.5", "Gemma 3", "quantização de modelos", "IA de borda"]
cover: "/img/cover/raspberry-pi-4-5-local-ai-models.webp"
coverAlt: "Dois computadores Raspberry Pi sobre uma mesa escura, com ilustrações azuis e âmbar de redes neurais acima"
coverCaption: "Ilustração de modelos de IA locais executados em hardware Raspberry Pi."
---

Um Raspberry Pi pode executar localmente um modelo de linguagem útil, mas o modelo precisa caber na memória da placa e responder num prazo aceitável para a sua aplicação. Um Raspberry Pi 4 com 2 GB é mais adequado a modelos com menos de cerca de mil milhões de parâmetros. Um Raspberry Pi 5 com 8 GB executa modelos compactos de 1B–3B com folga e consegue carregar alguns modelos quantizados maiores, com compromissos consideráveis.

Testámos estes modelos com Ollama num **Pi 4B de 2 GB** e num **Pi 5 de 8 GB**, ambos com armazenamento microSD. As medições das tabelas usaram as mesmas cinco instruções curtas para o assistente, o mesmo prompt de sistema, uma seed fixa e um limite de saída de 140 tokens. Descarregámos os outros modelos antes de cada execução e medimos o tempo de carregamento a frio, o tempo até ao primeiro token visível, a duração total da resposta, a velocidade de saída e o pico de memória residente. Foram testes de passagem única para uma carga de respostas curtas. Os resultados são exemplos para dimensionar recursos, não classificações universais de velocidade ou qualidade. A [CPU Cortex-A76 e as configurações de memória disponíveis do Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) também diferem de forma relevante da [plataforma Cortex-A72 do Pi 4](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008341-DS-1-raspberry-pi-4-datasheet.pdf).

## Tipos de modelos adequados

| Tipo de modelo | Exemplos medidos | Uso prático |
|---|---|---|
| Modelos de texto pequenos, cerca de 230M–600M parâmetros | LFM2.5-230M, LFM2.5-350M, Qwen2.5-0.5B | Comandos locais curtos, resumos e perguntas com restrições; melhor ponto de partida para Pi 4 de 2 GB |
| Modelos de texto compactos, cerca de 1B–2B | LFM2.5-1.2B, Qwen2.5-1.5B, Gemma 3 1B, MiniCPM5-1B | Mais capacidade para instruções detalhadas num Pi 5 ou Pi 4 com mais memória, com respostas mais lentas que as dos modelos menores |
| Modelos de texto quantizados de 3B–4B | Qwen2.5-3B, Llama 3.2 3B, Gemma 3 4B | Opções mais capazes para Pi 5 de 8 GB quando é aceitável esperar alguns segundos por resposta |
| Modelos maiores, esparsos ou híbridos | LFM2.5 8B | Funciona tecnicamente no Pi 5 de 8 GB testado, mas ocupa muita memória e demora a carregar a frio |

Estes resultados referem-se à **geração de texto**. Não demonstram o desempenho em geração de imagens, reconhecimento de fala, visão ou treino. «Funciona» significa mais do que o ficheiro caber no cartão: o runtime, a cache de contexto, o sistema operativo e outros serviços também precisam de RAM. A quantização reduz o ficheiro dos pesos, mas pode baixar a qualidade das respostas, sobretudo com definições extremas, como pesos de 1 bit.

### O que os números medem

O benchmark enviou à API de chat do Ollama pedidos curtos sobre factos, procedimentos de segurança, contexto recuperado, meteorologia e ajuda. Todos os modelos receberam o mesmo conjunto de pedidos e a mesma seed. Descarregámos cada modelo antes da medição para incluir um carregamento a frio no pedido seguinte. O **tempo total** é o da solicitação completa; os **tokens por segundo** descrevem apenas a geração da saída. Também registámos o primeiro token *visível*, relevante quando o modelo raciocina antes de responder.

Para medir a memória, registámos a RAM e o swap disponíveis no Pi, bem como a memória residente do Ollama e do processo de inferência durante cada pedido. Os valores de **RSS** referem-se à memória residente do processo, não à necessidade total do anfitrião. Páginas apoiadas em ficheiros, o sistema operativo, um navegador ou outro serviço local ainda podem provocar swap num modelo que parece caber. As tabelas apresentam os testes iniciais de cinco pedidos, numa só passagem. Mais tarde, acrescentámos um pedido de notícias e verificações das regras de resposta. Essas verificações ajudam a saber o que observar, mas não transformam as medições de velocidade anteriores em resultados de conformidade com seis pedidos.

Nem tokens por segundo nem o número de parâmetros são uma pontuação de qualidade. Um modelo pode gerar texto depressa e omitir uma fonte pedida, ultrapassar o limite de palavras ou deixar uma frase incompleta. Compare os modelos com os pedidos que pretende enviar e leia as respostas antes de escolher um para uma aplicação.

## Raspberry Pi 4: prefira os modelos mais pequenos

O Pi 4 de 2 GB testado tinha pouca margem. Os modelos LFM2.5 mais pequenos concluíram os cinco pedidos, tal como `qwen2.5:0.5b`. São opções razoáveis para respostas curtas offline ou um pequeno assistente local.

| Modelo | Ficheiro do modelo | Velocidade de saída medida | Tempo médio de resposta | Memória ou resultado observado |
|---|---:|---:|---:|---|
| LFM2.5-230M, GGUF importado | 0.25 GB | 12.8 tokens/s | 7.2 s | Pico de memória residente de 383 MB; 5/5 pedidos |
| LFM2.5-350M, GGUF importado | 0.38 GB | 8.6 tokens/s | 8.6 s | Pico de memória residente de 516 MB; 5/5 pedidos |
| `qwen2.5:0.5b` | 0.40 GB | 8.0 tokens/s | 9.7 s | 5/5 pedidos; disponível diretamente no Ollama |
| MiniCPM5-1B, GGUF importado, raciocínio desligado | 0.69 GB | 5.9 tokens/s | 12.2 s | Pico de memória residente de 883 MB; 5/5 pedidos |
| MiniCPM5-1B, GGUF importado, raciocínio predefinido | 0.69 GB | 5.7 tokens/s | 33.3 s | Apenas 1/5 pedidos devolveu uma resposta visível útil |
| `qwen3:0.6b`, raciocínio predefinido | 0.52 GB | 6.4 tokens/s | 40.4 s | Uma resposta vazia; a placa reiniciou |
| `granite4:350m` | 0.71 GB | 4.6 tokens/s | 15.5 s | 913 MB RSS, sem swap nem reinício; lenta, mas estável |
| `gemma3:1b` | 0.82 GB | 4.0 tokens/s | 30.7 s | Swap elevado; a placa reiniciou durante o teste |
| `qwen3.5:0.8b` | 1.04 GB | — | — | Não terminou; a placa reiniciou |

Os resultados do Pi 4 dependem bastante do resto do sistema. Observámos reinícios durante os testes de modelos maiores, incluindo uma execução de `qwen3.5:0.8b` que nunca terminou. Isto descreve a nossa configuração de 2 GB, não significa que qualquer Pi 4 ou modelo 1B vá reiniciar. Um Pi 4 de 4 ou 8 GB tem mais memória, mas a CPU continuará a inferir mais lentamente do que no Pi 5 testado. Não medimos diretamente essas variantes de memória do Pi 4.

Um dos primeiros testes no Pi 4 também pareceu muito pior que as medições finais: cerca de 625 MB de ficheiros GGUF temporários ficaram em `/tmp`, apoiado por RAM, deixando apenas 500–600 MB livres e enviando centenas de megabytes para swap. Depois de mover esses ficheiros para armazenamento persistente, os resultados dos modelos pequenos mostraram melhor a memória de inferência. Numa placa de 2 GB, até *o local onde guarda um download* pode distorcer um benchmark.

**Recomendação:** O nosso modelo predefinido para esta placa de 2 GB é o LFM2.5-350M importado. Permaneceu estável com **516 MB RSS**, deixou cerca de **1 GB de RAM disponível** e passou **5/6** verificações das regras de resposta no teste do Pi 4. Nos testes repetidos do Pi 5, por vezes omitiu o nome da fonte; aplicações que exigem atribuição devem verificá-la. Escolha LFM2.5-230M quando a latência e a margem de memória forem prioritárias: foi mais rápido e leve, mas numa resposta médica transformou “nausea or vomiting” em “nausea/ventilator use”. Esse erro de conteúdo torna-o uma opção predefinida mais fraca para respostas sobre saúde ou segurança, apesar da pontuação mecânica repetida superior. Escolha `qwen2.5:0.5b` se precisar de um modelo do [registo Ollama](https://ollama.com/library/qwen2.5/tags), tendo em conta a sua menor conformidade com instruções. `granite4:350m` foi estável, mas demorou mais e usou mais memória; MiniCPM5-1B só é viável se o cliente desligar o raciocínio. Evite Gemma 3 1B e Qwen3.5 0.8B nesta configuração específica de 2 GB, pois as nossas execuções provocaram reinícios.

## Raspberry Pi 5: mais opções, com uma troca na velocidade

O Pi 5 de 8 GB executou os **25 modelos** do benchmark de velocidade e memória. A tabela inclui todas as execuções, mesmo as que não recomendamos para respostas curtas. † indica um GGUF importado. «Think off» regista a definição usada no teste de velocidade; o teste de conformidade separado pode ter usado outra.

| Modelo | Ficheiro GB | Saída tok/s | Resposta s | RSS máximo MB | Avaliação para respostas curtas |
|---|---:|---:|---:|---:|---|
| `lfm2.5-230m` † | 0.25 | 45.0 | 1.8 | 446 | Latência mínima; 78% de conformidade repetida |
| `bonsai-1.7b` †, Q1_0 | 0.25 | 15.3 | 8.2 | 871 | Evitar: pesos de 1 bit e conformidade de passagem única 3/6 |
| `lfm2.5-350m` † | 0.38 | 30.0 | 2.1 | 581 | Rápida, mas omitiu a fonte em 5 de 18 repetições |
| `qwen2.5:0.5b` | 0.40 | 28.4 | 3.6 | 675 | Opção simples do registo; 61% de conformidade repetida |
| `qwen3:0.6b`, raciocínio desligado | 0.52 | 23.0 | 4.3 | 1,069 | Condicional: 4/6; a definição de raciocínio importa |
| `bonsai-4b` †, Q1_0 | 0.57 | 6.8 | 18.1 | 1,343 | Modelo de 1 bit experimental; o 6/6 de uma só passagem não está confirmado |
| `minicpm5-1b` †, raciocínio desligado | 0.69 | 18.4 | 5.1 | 869 | Condicional: o raciocínio predefinido deu respostas vazias |
| `granite4:350m` | 0.71 | 12.1 | 6.6 | 892 | Cabe, mas é maior e mais lento que o LFM2.5 pequeno |
| `lfm2.5-1.2b` † | 0.73 | 15.5 | 4.7 | 967 | Melhor para a nossa carga; 89% de conformidade repetida |
| `llama3.2:1b-instruct-q4_K_M` | 0.81 | 13.0 | 7.5 | 1,244 | Alternativa do registo; 5/6 em conformidade |
| `gemma3:1b` | 0.82 | 11.2 | 10.9 | 1,262 | Melhor conformidade repetida entre modelos do registo: 83% |
| `qwen2.5:1.5b-instruct-q4_K_M` | 0.99 | 10.3 | 9.4 | 1,361 | 4/6; Gemma 3 1B seguiu melhor as regras |
| `qwen3.5:0.8b`, raciocínio desligado | 1.04 | 8.8 | 12.2 | 1,592 | 0/6 com raciocínio predefinido; evitar sem controlo do raciocínio |
| `spark-x2.5-1.7b` †, raciocínio desligado | 1.11 | 9.7 | 9.4 | 1,542 | 0/6 com raciocínio predefinido; evitar sem controlo do raciocínio |
| `qwen3:1.7b`, raciocínio desligado | 1.36 | 8.1 | 12.4 | 1,867 | Condicional; mais memória e atraso que modelos menores |
| `minicpm5-2b` †, raciocínio desligado | 1.56 | 7.7 | 10.9 | 1,787 | Condicional; 5/6 numa passagem, pontos de lista adicionais |
| `qwen2.5:3b-instruct-q4_K_M` | 1.93 | 5.2 | 14.7 | 2,366 | Opção 3B para experimentar; 5/6 numa passagem |
| `granite4:micro-h` | 1.94 | 3.9 | 23.7 | 2,486 | Evitar para uso interativo: descodificação lenta |
| `llama3.2:3b-instruct-q4_K_M` | 2.02 | 5.5 | 18.6 | 2,831 | Outra opção 3B; não foi relatado teste de conformidade |
| `granite4:micro` | 2.10 | 5.3 | 17.9 | 2,679 | Cabe, mas responde mais devagar que as alternativas menores |
| `qwen3.5:2b`, raciocínio desligado | 2.74 | 5.0 | 16.1 | 3,627 | Memória e atraso elevados; teste de conformidade não relatado |
| `gemma3:4b` | 3.34 | 3.9 | 30.3 | 4,267 | Evitar para respostas rápidas; 14.3 s até ao primeiro token |
| `ling-3.0-tiny` †, raciocínio desligado | 4.82 | 9.9 | 19.4 | 5,071 | Grande ocupação; 5/6 numa passagem com falha de fundamentação |
| `lfm2.5:8b`, raciocínio desligado | 5.16 | 8.7 | 54.6 | 5,317 | Cabe à justa; carregamento a frio de 34.4 s e respostas longas |
| `gemma3n:e2b` | 5.62 | 6.1 | 25.9 | 5,261 | Evitar: swap com outros serviços do Pi |

† GGUF importado. Os tempos de resposta e a memória vêm do teste de velocidade no Pi 5 com cinco pedidos; os resultados de conformidade vêm de testes separados com seis pedidos. Um modelo sem pontuação não demonstrou seguir as regras de resposta.

Os pequenos modelos LFM2.5 foram os mais rápidos *para esta carga de respostas curtas*. A versão 1.2B oferece um compromisso prático no Pi 5 testado. Gemma 3 1B é uma alternativa disponível apenas no registo e, nos testes posteriores, seguiu repetidamente as regras de resposta melhor que Qwen2.5 1.5B. Um modelo 3B pode compensar a saída mais lenta em pedidos que exijam mais capacidade, mas estes tempos não mostram por si só qual responde melhor.

Os atrasos de carregamento a frio e do primeiro token mudam a experiência. No Pi 5, LFM2.5-230M carregou em cerca de **0.21 segundos** e apresentou um token visível em **0.37 segundos**. Qwen2.5 1.5B demorou **2.59 segundos** a carregar e **3.66 segundos** até ao primeiro token visível; Qwen2.5 3B demorou **5.60** e **7.97 segundos**. Para uma pergunta ocasional, estes atrasos podem importar mais do que a velocidade de saída depois de começar a geração. Um modelo carregado continuamente reduz esse atraso, mas ocupa memória entre pedidos.

Outros candidatos medidos mostram por que não classificamos apenas pelo número de parâmetros. Com o raciocínio desligado, `qwen3:0.6b` atingiu **23.0 tokens/s** no Pi 5 com **1,069 MB RSS**, enquanto MiniCPM5-1B importado atingiu **18.4 tokens/s** com **869 MB RSS**. `granite4:350m` exigiu um download de **0.71 GB** e gerou **12.1 tokens/s**, apesar do rótulo 350M. O empacotamento e a arquitetura mudam a relação entre nome, tamanho do ficheiro, memória e velocidade.

Se o seu cliente conseguir enviar `think: false` de forma fiável, Qwen3 0.6B e MiniCPM5-1B são experiências razoáveis como alternativas a LFM2.5. MiniCPM5-2B, Qwen3 1.7B e Spark-X2.5 1.7B também funcionaram no Pi 5, mas não ofereceram uma vantagem clara de velocidade e memória sobre as opções principais. O teste de conformidade usou o raciocínio predefinido para MiniCPM5-1B e Spark-X2.5; as respostas vazias não devem ser apresentadas como resultado dos testes de velocidade com raciocínio desligado. Por outro lado, um tempo rápido com raciocínio desligado não prova que uma ponte sem essa definição receberá uma resposta útil.

Se a simplicidade de instalação importar mais que a velocidade bruta, Gemma 3 1B e Llama 3.2 1B são opções plausíveis do registo num Pi 5 de 8 GB. Gemma 3 1B seguiu as regras testadas em **15/18** respostas repetidas. Llama 3.2 1B passou **5/6** numa passagem, por isso a estimativa de conformidade é menos segura. Qwen2.5 1.5B carregou e respondeu mais depressa que Gemma 3 1B no teste de tempo, mas passou só **4/6** verificações no seu único teste de conformidade. Escolha segundo os requisitos dos seus pedidos.

Para pedidos de texto ocasionais mais longos ou difíceis, Qwen2.5 3B e Llama 3.2 3B quantizados são os candidatos 3B com uso moderado de memória no Pi 5 de 8 GB testado. Medimos velocidade e memória; Qwen2.5 3B passou **5/6** numa única verificação de conformidade. Não foi relatado um teste comparável para Llama 3.2 3B. O maior número de parâmetros justifica *testá-los* em tarefas nas quais os modelos menores falham, não prova que respondam melhor. Granite 4 Micro e Micro-H, Qwen3.5 2B, Gemma 3 4B, Ling-3.0-tiny e Gemma 3n E2B couberam ou carregaram nos testes do Pi 5, mas foram menos interessantes em latência, margem de memória ou fiabilidade para esta aplicação de respostas curtas.

Os dois modelos Bonsai mostram o custo da quantização extrema. Os ficheiros Q1_0 eram surpreendentemente pequenos para nomes com 1.7B e 4B parâmetros, mas o modelo 1.7B passou apenas **3/6** verificações das regras de resposta. O modelo 4B passou uma única prova de seis pedidos, mas demorou **18.1 segundos** por resposta e não teve confirmação repetida de conformidade. Trate ambos como experiências e não recomendações predefinidas, sobretudo quando a qualidade da resposta importa.

O resultado LFM2.5-8B precisa de contexto: a arquitetura híbrida usa menos parâmetros ativos por token, pelo que a velocidade de descodificação ultrapassou a dos modelos densos 3B medidos. Ainda assim, o carregamento a frio desde microSD demorou **34.4 segundos** e usou mais de **5.3 GB de memória residente**. Isto mostra o que cabe, mas não é uma escolha confortável para um Pi que também executa outros serviços. O `gemma3n:e2b` medido também usou cerca de 5.3 GB de memória residente e provocou swap junto com os restantes serviços do anfitrião de teste.

A execução LFM2.5 8B também atingiu o limite completo de **140 tokens**, em vez de manter a resposta curta. A execução Gemma 3 4B demorou **14.3 segundos** até ao primeiro token e **30.3 segundos** pela resposta completa. Ambos carregam neste Pi 5, mas não se comportaram como pequenos assistentes reativos nos nossos testes. Um modelo minúsculo com uma resposta curta adequada pode servir melhor uma interface de rádio ou comandos que um modelo maior com uma velocidade de descodificação teoricamente superior.

## Memória, raciocínio e formato do modelo

Uma estimativa inicial útil das nossas medições é **tamanho do download do modelo × 1.4** para a memória residente de inferência. É apenas uma regra prática: comprimento do contexto, definições do runtime, arquitetura e outros processos podem alterar a necessidade. Verifique a memória disponível durante a geração, mantenha apenas um modelo carregado num anfitrião pequeno e deixe margem para o sistema operativo. Uma placa de 4 GB pode começar com modelos pequenos ou compactos, mas as nossas recomendações para 4 GB são extrapolações, não testes diretos dessa variante.

Por exemplo, um ficheiro LFM2.5-1.2B de 0.73 GB correspondeu a cerca de **967 MB RSS** no Pi 5, enquanto o ficheiro Qwen2.5 1.5B de 0.99 GB atingiu **1,361 MB RSS**. A regra funciona razoavelmente para estes modelos, mas não é um limite rígido. Conte com mais memória do que a do processo medido se o Pi também executar uma interface, índice de pesquisa, biblioteca local ou serviço em segundo plano. Observe o swap durante um pedido real; um modelo que carrega mas usa swap continuamente não serve na prática.

Alguns modelos geram um bloco interno de raciocínio antes da resposta visível. Nos nossos testes, `qwen3:0.6b` no Pi 4 de 2 GB demorou muito mais a apresentar texto visível. MiniCPM5-1B respondeu de forma útil a apenas um dos cinco pedidos com a definição predefinida de raciocínio, contra cinco de cinco com o raciocínio desligado. Para respostas com limite curto, defina `think: false` num pedido compatível da API Ollama ou escolha um modelo sem raciocínio predefinido. Esta definição aplica-se a modelos e clientes compatíveis; não é um interruptor universal de velocidade.

A distinção importa porque o limite de tokens pode incluir tokens de raciocínio mesmo quando o utilizador não vê uma resposta. No Pi 4, `qwen3:0.6b` com raciocínio predefinido demorou em média **40.4 segundos por pedido**; um deles devolveu uma resposta visível vazia. MiniCPM5-1B demorou em média **33.3 segundos** com a definição predefinida e **12.2 segundos** com o raciocínio desligado. Nas execuções Pi 5 também desligámos o raciocínio de Qwen3, Qwen3.5, MiniCPM5, Ling-3.0 e Spark-X2.5 onde os nossos registos o indicavam. Compare cada modelo com a definição que o cliente usará.

### Verifique se a resposta serve

Na nossa carga curta de assistente mesh, o contrato da resposta importa tanto quanto a velocidade: até **90 palavras**, no máximo **três pontos de lista**, texto simples, uma frase completa e utilização do contexto recuperado fornecido com o nome da fonte. A ponte divide o texto em blocos de **180 caracteres**. Uma resposta longa ocupa mais tempo de rádio, mesmo que o modelo a gere depressa.

A versão posterior do benchmark verifica respostas vazias, limite de palavras específico do pedido, pontos em excesso, tabelas ou blocos de código Markdown, final incompleto, termos ausentes do contexto fornecido e nome da fonte em falta. Avaliados segundo o prompt de sistema do assistente implementado, os modelos pequenos violavam estas regras regularmente. As falhas mais importantes eram **respostas vazias** quando o raciocínio consumia o limite de tokens, seguidas de respostas que ignoravam o contexto recuperado ou omitiam a fonte. Ultrapassar o limite de palavras ou pontos ainda produzia texto visível, mas desperdiçava tempo de rádio. São verificações mecânicas e não substituem a leitura da resposta: não estabelecem a exatidão dos factos nem a qualidade dos conselhos de segurança.

#### Resultados repetidos de conformidade no Pi 5

Primeiro executámos seis pedidos uma vez por modelo, com um limite de **220 tokens** e o prompt de sistema implementado. Os modelos promissores foram testados mais duas vezes com outra seed, num total de **18 respostas por modelo**. Uma passagem perfeita não garante repetições perfeitas. Os resultados repetidos abaixo oferecem uma comparação mais sólida para as respostas mesh curtas testadas:

| Modelo | Respostas que cumpriram todas as regras verificadas | Principais falhas observadas |
|---|---:|---|
| LFM2.5-1.2B importado | 16/18 (89%) | Duas respostas incompletas |
| `gemma3:1b` | 15/18 (83%) | Três respostas incompletas |
| LFM2.5-230M importado | 14/18 (78%) | Respostas incompletas e nomes de fontes ausentes |
| LFM2.5-350M importado | 13/18 (72%) | Nomes de fontes ausentes |
| `qwen2.5:0.5b` | 11/18 (61%) | Demasiados pontos e palavras, nomes de fontes ausentes |

No **Pi 4 de 2 GB**, a verificação separada de seis pedidos deu **5/6** ao LFM2.5-350M, **4/6** ao LFM2.5-230M e **2/6** ao Qwen2.5-0.5B. MiniCPM5-1B melhorou de **1/6** com raciocínio predefinido para **5/6** com o raciocínio desligado. Estes resultados do Pi 4 são de uma só passagem. Por isso, damos mais peso aos resultados repetidos do Pi 5 ao discutir seguimento geral de instruções e usamos os testes Pi 4 para avaliar estabilidade e velocidade nessa placa.

As falhas têm consequências diferentes. Uma resposta **vazia** não ajuda o utilizador; ignorar o material fornecido pode induzir em erro. Sem o nome da fonte, os leitores não conseguem verificar a atribuição. Pontos ou palavras a mais consomem sobretudo pacotes adicionais de 180 caracteres. Uma frase incompleta pode indicar truncagem. O erro de termo médico do LFM2.5-230M lembra que uma resposta pode passar verificações mecânicas e ainda estar errada. Nenhum dos cinco candidatos testados repetidamente seguiu todas as regras em todas as 18 respostas. Uma aplicação com limites rígidos de tamanho ou formato também os deve impor depois da geração e rever separadamente o conteúdo de alto risco.

Também verificámos o endpoint real da ponte, `/v1/chat/completions` compatível com OpenAI do Ollama, com contexto WikiMed recuperado. No Pi 5, LFM2.5-1.2B devolveu uma resposta de 28 palavras que usou seis termos fornecidos; Qwen2.5-0.5B devolveu 38 palavras e usou sete. Ambas couberam em dois pacotes de 180 caracteres. A verificação confirma que o LFM2.5 importado funciona no caminho de pedidos da ponte, mas uma resposta bem-sucedida não garante fiabilidade.

Ollama publica muitos modelos prontos a descarregar, incluindo as [variantes Qwen2.5 de 0.5B, 1.5B e 3B](https://ollama.com/library/qwen2.5/tags). Importámos para Ollama os pequenos modelos LFM2.5 dos [lançamentos GGUF da Liquid AI](https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/tree/main). Confirme a tag exata ou o nome do ficheiro GGUF antes de descarregar: registos e repositórios podem mudar. Guarde os downloads GGUF em armazenamento persistente; nos nossos testes, o `/tmp` em RAM consumiu a escassa memória do Pi 4.

### Tags do registo e imports GGUF

Uma tag do Ollama é o caminho mais curto para um primeiro teste: obtenha a tag exata e execute-a. Os pequenos LFM2.5 das tabelas eram **imports GGUF**, não tags `lfm2.5-230m`, `lfm2.5-350m` ou `lfm2.5-1.2b` na biblioteca pública do Ollama. GGUF é um formato de ficheiro de modelo; nomes como `Q8_0` e `Q4_K_M` identificam opções de quantização. Os ficheiros LFM2.5 de 230M e 350M usados eram Q8_0, enquanto o ficheiro 1.2B era Q4_K_M. A mesma contagem de parâmetros noutra quantização pode, por isso, ter tamanho, memória ou qualidade diferentes.

Para importar a variante 350M testada, descarregue o GGUF para um diretório em armazenamento persistente, crie um Modelfile que aponte para ele e deixe o Ollama copiá-lo para o armazenamento de modelos:

```bash
mkdir -p "$HOME/gguf"
cd "$HOME/gguf"
curl -fL -C - --retry 5 --retry-all-errors -O \
  https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/resolve/main/LFM2.5-350M-Q8_0.gguf
printf 'FROM %s/LFM2.5-350M-Q8_0.gguf\n' "$PWD" > Modelfile-lfm2.5-350m
ollama create lfm2.5-350m -f Modelfile-lfm2.5-350m
ollama run lfm2.5-350m
```

A importação precisa temporariamente de espaço para o ficheiro descarregado e a cópia guardada pelo Ollama. Usámos downloads retomáveis porque transferências longas de GGUF por vezes eram interrompidas. Antes de importar, compare o SHA-256 do download com o hash publicado pela origem; uma transferência parcial pode parecer um problema do modelo. No nosso Pi, `/tmp` era apoiado por RAM, pelo que guardar lá um GGUF reduzia a memória disponível para inferência.

## Um ponto de partida prático

| Hardware e objetivo | Primeiro modelo a testar | Motivo |
|---|---|---|
| Pi 4 de 2 GB, predefinição | LFM2.5-350M importado | Estável a 516 MB RSS com cerca de 1 GB disponível; escolhido após erro de termo médico do 230M |
| Pi 4 de 2 GB, latência mínima | LFM2.5-230M importado | 383 MB RSS e resposta média de 7.2 s; verifique o conteúdo com cuidado, sobretudo em questões de saúde e segurança |
| Pi 4 de 2 GB, apenas registo | `qwen2.5:0.5b` | Download direto do Ollama e estabilidade no nosso teste Pi 4 de cinco pedidos; 61% de conformidade repetida no Pi 5 |
| Pi 4 de 4 GB ou Pi 5 | LFM2.5-1.2B importado e depois testar localmente | 967 MB RSS e 89% de conformidade repetida no Pi 5 de 8 GB; não testámos diretamente variantes de 4 GB |
| Pi 5 de 8 GB, assistente reativo | LFM2.5-1.2B importado | 15.5 tokens/s, resposta total de 4.7 s e maior conformidade repetida medida |
| Pi 5 de 8 GB, apenas registo | `gemma3:1b` | 11.2 tokens/s, 1,262 MB RSS e 83% de conformidade repetida |
| Pi 5 de 8 GB, testar texto maior | Qwen2.5 3B ou Llama 3.2 3B quantizados | Ambos correram a cerca de 5 tokens/s e usaram 2.4–2.8 GB RSS; Qwen2.5 3B passou 5/6 numa verificação única |

Estas opções dão prioridade a respostas curtas e úteis num Pi que também pode executar outros serviços. São pontos de partida, não a afirmação de que um modelo seja melhor em todas as tarefas. No nosso teste de conformidade de passagem única no Pi 5, `qwen3.5:0.8b` e Spark-X2.5 com raciocínio predefinido não deram respostas conformes; MiniCPM5-1B obteve 1/6. Se o cliente não conseguir desligar o raciocínio, evite-os para esta carga curta. Teste o modelo final com o prompt, contexto, concorrência e limite de resposta previstos para a implementação.

Para o modelo do registo, depois de [instalar Ollama para Linux](https://ollama.com/download/linux), execute:

```bash
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
```

Teste os seus prompts, o tamanho de resposta desejado e os restantes serviços ativos. Registe o tempo total de resposta e o uso de memória. Isso mostra melhor se um modelo serve para o seu Pi do que o número de parâmetros isoladamente.

Num nó com pouca memória, acompanhe o swap durante os testes. Se um modelo maior tornar a placa pouco reativa, use um modelo menor e defina um limite de memória adequado para o serviço Ollama, para que uma carga excessiva falhe antes de esgotar a memória do anfitrião. O limite do serviço é uma proteção, não uma forma de fazer caber um modelo demasiado grande. Os reinícios do Pi 4 nos nossos testes mostram por que a capacidade de resposta e a margem de memória também contam, além dos tokens por segundo.

## Transformar o benchmark numa decisão de implementação

Antes de usar um modelo diariamente, registe quatro limites: **tempo máximo de resposta, memória residente máxima, formato da resposta e comportamento em caso de falha**. Teste esses limites com os serviços que partilharão a placa. Um modelo que passa sozinho mas provoca swap ao lado da ponte de rádio ou do painel não satisfaz o requisito de implementação.

Mantenha um modelo pequeno de reserva instalado. Mude para ele se o modelo principal ultrapassar o limite de memória, devolver uma resposta vazia ou violar o contrato de resposta. Registe em cada comparação a tag do modelo, quantização, versão Ollama, prompt, comprimento do contexto e seed, para que uma atualização posterior do modelo não pareça uma melhoria do hardware.

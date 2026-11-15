---
title: "IA local em 2026: modelo 27B supera Sonnet 4.6 enquanto a janela para comprar equipamentos se fecha"
date: 2026-09-22
lastmod: 2026-11-15
toc: true
draft: false
description: "Planeje um PC de IA local para 2026 considerando tamanho do modelo, VRAM, largura de banda da memória, energia, custo e opções de atualização."
genre: ["IA local", "IA auto-hospedada", "Modelos de código aberto", "Hardware de IA", "Aprendizado de máquina", "Quantização", "Laboratório doméstico", "Privacidade", "Economia da IA", "Hardware de consumo"]
tags: ["IA local", "executar llm localmente", "qwen3.8", "qwen3.8 27b", "bonsai 2 27b", "ternary bonsai", "prism ml", "quantização ternária", "1,58 bit", "quantização de llm", "claude sonnet 4.6", "sonnet 4.6 vs modelo local", "pesos abertos", "modelo moe", "mistura de especialistas", "ollama", "llama.cpp", "rtx 5090", "vram", "inferência local", "preços de gpu 2026", "escassez de dram", "preços de memória", "montar pc de IA", "IA para laboratório doméstico", "custo de assinatura de IA", "openrouter", "artificial analysis", "guia de compra de gpu", "llm auto-hospedado", "IA que preserva privacidade", "hardware de IA 2026"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Espaço de trabalho tecnológico com uma placa de vídeo e várias telas iluminadas mostrando resultados e visualizações de IA em um fundo azul-marinho escuro."
coverCaption: ""
ref: ["/articles/ai-models-raspberry-pi-4-5", "/articles/building-a-privacy-preserving-meshtastic-ai-assistant"]
---

**Um modelo que você baixa e executa em uma única placa de vídeo de consumo agora supera um modelo de API de ponta no índice agregado de inteligência.** Qwen3.8 27B é um modelo aberto de visão e linguagem lançado em agosto de 2026. Sua versão reempacotada em formato ternário, Bonsai 2 27B, comprime os mesmos pesos para 5.53 GiB. Juntos, eles marcam o momento em que a inferência local deixou de ser uma concessão para entusiastas e passou a ser uma alternativa real a uma API paga.

*A janela para comprar hardware está se fechando rapidamente. Os preços da memória estão no pior nível em duas décadas e também elevam os preços das placas de vídeo.*

Este artigo analisa os resultados dos testes, o que há por trás dos dois modelos, onde o modelo aberto ainda perde e por que os próximos doze meses são um mau momento para esperar.

**O que você vai obter:** escolha modelo e capacidade de memória conforme sua carga de trabalho. Antes de comprar, compare custo do hardware, energia, tamanho do contexto e taxa de transferência medida. A comparação dos testes não prevê a qualidade em suas tarefas nem o preço futuro da GPU.

## Resposta curta

**A diferença de inteligência entre um modelo local 27B e uma API paga próxima da fronteira diminuiu, e as vantagens restantes do modelo pago são menores do que a diferença de preço sugere.**

Três coisas mudaram ao mesmo tempo:

- **Modelos abertos 27B alcançaram resultados próximos aos líderes.** Qwen3.8 27B marca 33.7 no Intelligence Index, contra 30.1 do Sonnet 4.6, na mesma bateria de avaliação.
- **A quantização ternária reduziu a necessidade de memória em cerca de dois terços.** Bonsai 2 27B executa o modelo completo 27B em **5.53 GiB**, espaço disponível em placas que custam algumas centenas de dólares.
- **A oferta de memória piorou.** Os preços contratuais da DRAM convencional subiram **90 a 95 por cento** em relação ao trimestre anterior no início de 2026, a maior alta trimestral registrada pela TrendForce, adiando as GPUs de próxima geração para 2028.

*Comprar ou montar o computador agora é a opção mais barata. Não é propaganda, é o que dizem os dados de oferta.*

## Veja o teste com uma única GPU

A afirmação acima merece uma demonstração, não só uma tabela. Bijan Bowen testou o Bonsai 2 27B em uma máquina com uma GPU e perguntou se é o melhor modelo disponível hoje para uma placa.

{{< youtube id="OA5cICIzD-c" enable="true" title="Primeiro teste do Bonsai 2 27B: ele é o melhor modelo de IA para uma GPU?" description="Primeira análise do modelo ternário Bonsai 2 27B em uma GPU de consumo, cobrindo velocidade, qualidade e alternativas." >}}

*Observe a qualidade das respostas, não o número de tokens por segundo. Velocidade é a parte mais fácil de melhorar.*

## Dois nomes, um modelo

Os dois modelos importantes aqui não são concorrentes. **São os mesmos pesos em duas precisões diferentes.**

| | Qwen3.8 27B | Bonsai 2 27B ternário |
|---|---|---|
| **O que é** | O modelo original de pesos abertos da Qwen | Reempacotamento ternário do Qwen3.8-27B pela Prism ML |
| **Pesos em disco** | **18 GB** | **5.53 GiB** (PTQ1_0) ou **6.70 GiB** (PQ2_0) |
| **Parâmetros** | 27B denso | 26.90B, mesma arquitetura |
| **Contexto** | 256K | 262,144 tokens |
| **Visão** | Sim, nativa | Sim, pacote de projetor CLIP separado |
| **Chamada de ferramentas** | Sim | Sim |
| **Licença** | Apache 2.0 | Apache 2.0 |
| **Runtime** | Ollama, llama.cpp, MLX | **Somente o fork do llama.cpp da Prism ML** |

A página da biblioteca Ollama para `qwen3.8` lista o modelo 27B com **18 GB**, contexto de 256K, suporte a visão e chamada de ferramentas, além de uma compilação MLX separada para Apple Silicon. A versão ternária no Ollama espelha os pacotes GGUF Apache-2.0 da Prism ML, republicados com os mesmos checksums.

**A pergunta prática não é qual modelo escolher.** É quanta memória você aceita gastar pela mesma inteligência. A versão ternária usa cerca de um terço da memória e perde pouco em troca.

{{< figure src="local-ai-architecture-comparison.webp" alt="Diagrama que compara o uso de memória do mesmo modelo 27B em precisão padrão, 18 GB, com pesos ternários, 5.53 GiB, mostrando que ambos cabem em uma GPU de consumo" >}}

## Comparação dos benchmarks

A Artificial Analysis avalia os dois modelos com a mesma bateria. Leia os resultados linha por linha, pois cada modelo vence em áreas diferentes.

| Métrica | Qwen3.8 27B | Claude Sonnet 4.6 | Líder |
|---|---|---|---|
| **Intelligence Index** | **33.7** | 30.1 | Aberto |
| **Coding Index** | **68.1** | 63.0 | Aberto |
| **Agentic Index** | **45.8** | 31.8 | Aberto |
| **GPQA Diamond** | **90.5%** | 87.5% | Aberto |
| **Humanity's Last Exam** | **33.9%** | 33.6% | Aberto |
| **AA-LCR (contexto longo)** | **82.0%** | 80.0% | Aberto |
| **GDPval-AA** | **45.4%** | 36.0% | Aberto |
| **CritPt (física de pesquisa)** | **5.4%** | 3.1% | Aberto |
| **Taxa sem alucinação** | **69.7%** | 51.6% | Aberto |
| **SciCode** | 46.6% | **50.1%** | Sonnet |
| **Precisão AA-Omniscience** | 15.6% | **40.9%** | Sonnet |

*O modelo aberto lidera nove das onze linhas comparáveis, incluindo todos os índices agregados.*

### Onde o modelo aberto lidera

Os três índices agregados resumem o resultado. **Intelligence: 33.7 contra 30.1, Coding: 68.1 contra 63.0, Agentic: 45.8 contra 31.8.** A diferença é maior no índice agentic. Isso importa mais para quem executa fluxos automatizados de várias etapas do que para quem envia prompts individuais.

Para dar contexto por percentil, a Artificial Analysis coloca Qwen3.8 27B **acima de 86 por cento dos modelos** no índice agentic e de 76 por cento em programação. Sonnet 4.6 fica nos percentis 68 e 72, respectivamente. Em raciocínio científico de nível de pós-graduação, o modelo aberto marca **90.5 por cento** no GPQA Diamond.

### Onde Sonnet 4.6 ainda lidera

Dois resultados favorecem o outro lado, e nenhum é insignificante.

**AA-Omniscience mede se o modelo responde corretamente a perguntas de conhecimento na primeira tentativa. Sonnet 4.6 marca 40.9 por cento contra 15.6 por cento.** É uma diferença grande em confiabilidade factual e o argumento mais forte para pagar por um modelo avançado.

A linha de não alucinação exige cuidado. Os 69.7 por cento de Qwen contra 51.6 por cento do Sonnet parecem uma vitória clara, e isoladamente são. Mas a métrica descreve a parcela de respostas *incorretas* que evita inventar informações. Um modelo menos preciso produz mais respostas incorretas, portanto as porcentagens descrevem conjuntos diferentes e não são diretamente comparáveis. **Leia primeiro a linha de precisão.**

Sonnet também vence no SciCode, com 50.1 por cento contra 46.6 por cento, e publica resultados em duas avaliações que não aparecem na ficha do modelo aberto: IFBench e Terminal-Bench Hard. Não há comparação possível.

### Duas ressalvas honestas

**As datas de lançamento estão separadas por seis meses.** Sonnet 4.6 foi lançado em fevereiro de 2026. Qwen3.8 27B saiu em agosto de 2026. Comparar um modelo de ponta de fevereiro com um modelo aberto de agosto não é uma disputa equivalente.

**Sonnet 4.6 já não é o modelo de ponta da Anthropic.** Sonnet 5 e Opus 5 agora estão acima dele na linha de produtos. O modelo aberto 27B alcançou um modelo topo de linha de meados de 2026, mas não o topo atual. Dizer o contrário é interpretar demais a tabela.

*Os testes medem o desempenho nos próprios testes. A única pontuação que importa é a da sua própria carga de trabalho.*

## O que os pesos ternários mudam

Bonsai 2 não é um modelo menor. É o mesmo modelo de 26.90B em uma precisão numérica muito inferior, e os metadados GGUF publicados deixam clara a troca.

| Propriedade | Valor |
|---|---|
| **Arquitetura** | `qwen35`, atenção híbrida com atenção completa a cada quatro camadas, além de camadas state-space |
| **Parâmetros** | 26.90B |
| **Blocos** | 64 |
| **Largura do embedding** | 5120 |
| **Atenção** | 24 cabeças de consulta, 4 cabeças KV, comprimento chave/valor 256 |
| **Contexto** | 262,144 tokens, base RoPE 1e7 |
| **Formato dos pesos** | Ternário, grupo de 128. PQ2_0 a 2.13 bits por peso, PTQ1_0 a 1.75 |
| **Torre de visão** | CLIP, 460.73M parâmetros, distribuída em um pacote de projetor separado |
| **Licença** | Apache 2.0 |

**Pesos ternários significam que cada parâmetro assume um de três valores em vez de dezesseis.** Essa compressão é o ponto principal e permite que um modelo 27B completo caiba em 5.53 GiB em vez de 18 GB.

### Taxa de transferência medida

Benchmark com `llama-bench` em uma RTX 5090 de 32 GB, todas as camadas na GPU, flash attention ativada, média de três execuções:

| Pacote | Pesos | Prefill (pp512) | Decodificação (tg128) |
|---|---|---|---|
| **PQ2_0** | 6.70 GiB | **3802.74 tok/s** | **135.41 tok/s** |
| **PTQ1_0** | 5.53 GiB | 1876.31 tok/s | 131.41 tok/s |

PQ2_0 processa o prefill **2.03 vezes mais rápido** que PTQ1_0, enquanto a decodificação empata estatisticamente. Por isso PQ2_0 é a escolha padrão sensata. PTQ1_0 serve quando os últimos 1.2 GiB fazem diferença. Com `llama-server` e contexto de 65K, a decodificação manteve **136.5 tok/s** em uma solicitação de streaming.

**A velocidade de decodificação é o número que você sente no uso diário.** 135 tokens por segundo ultrapassam com folga a velocidade de leitura. Latência não é motivo para executar inferência local, pois uma API hospedada já é rápida o suficiente. Os motivos são custo, privacidade e controle.

### A armadilha que ninguém menciona

**O Ollama padrão não carrega esses arquivos.** Os kernels ternários ficam no fork do llama.cpp da Prism ML. Verificado no Ollama 0.34.2, o carregamento falha com `unsupported tensor "output.weight" size overflows`. O runtime reconhece a arquitetura `qwen35`, mas nenhuma biblioteca contém `pq2_0` ou `ptq1_0`, nem um runtime de ativação Hadamard.

Há uma segunda armadilha que você deve conhecer antes de gastar uma noite nisso. **O pacote F16 desta família parece um fallback seguro, mas não é.** Seus tensores são F16 e F32 comuns, então ele é analisado e carregado sem reclamações, mas depois decodifica texto incoerente. Os pesos estão em uma base rotacionada indicada nos metadados `prism.hadamard.*`, e o runtime precisa aplicar a rotação correspondente ou produzirá bobagens. Com 50.1 GiB, o pacote F16 também não cabe totalmente em uma placa de 32 GB.

*Leia a ficha do modelo antes de baixar. Um espelho comunitário não é uma compilação suportada, e a página diz isso claramente.*

## A onda de MoE por trás disso

Modelos densos 27B são metade da história. Modelos mixture-of-experts ativam uma pequena parte dos parâmetros por token, o que muda a economia novamente.

| Modelo | Total / ativo | Contexto | Nota |
|---|---|---|---|
| **Qwen3.8 2.4T A95B** | 2.4T / 95B | 1.0M | Irmão de pesos abertos do Qwen3.8 Max |
| **Qwen3.6 35B A3B** | 35B / 3B | 262K | Apache 2.0, MoE esparso híbrido |
| **Qwen3 Coder Next** | 80B / 3B | 256K | Peso aberto, feito para agentes de programação sempre ativos |

**Qwen3 Coder Next é o modelo a observar para trabalho local.** Tem 80B parâmetros no total e apenas 3B ativos por token, voltado a agentes sempre ativos em ambientes CLI e IDE. Um modelo que ativa 3B parâmetros gera na velocidade de um modelo 3B, mas usa uma capacidade armazenada de 80B. As notas do projeto dizem que seu desempenho se compara ao de modelos com 10 a 20 vezes mais computação ativa.

*O modelo denso 27B é a escolha segura hoje. Modelos esparsos são onde a curva de eficiência ainda melhora.*

{{< figure src="local-ai-moe-dense-tradeoff.webp" alt="Gráfico que compara um modelo denso 27B, que ativa todos os parâmetros por token, com um modelo mixture-of-experts esparso, que ativa apenas 3 bilhões de 80 bilhões de parâmetros" >}}

## A janela para comprar equipamentos está se fechando

Esta é a parte da história com prazo definido.

A inferência local ficou barata exatamente quando a memória de que depende começou a encarecer. As duas tendências caminham para um choque, já visível nos preços do varejo.

### O que aconteceu com os preços da memória

**Os preços contratuais da DRAM convencional subiram de 90 a 95 por cento em relação ao trimestre anterior no primeiro trimestre de 2026**, a maior alta trimestral registrada pela TrendForce. A memória NAND flash subiu de 55 a 60 por cento no mesmo período.

A pressão não cedeu. Os dados da TrendForce mostram novo aumento de **58 a 63 por cento** para DRAM e de 70 a 75 por cento para NAND no segundo trimestre. Até a desaceleração do terceiro trimestre, com DRAM subindo de 13 a 18 por cento e NAND de 10 a 15 por cento, soma inflação a dois trimestres recordes em vez de aliviar os preços.

A causa é estrutural, não cíclica. A expansão de centros de dados de IA consome capacidade de memória que antes atendia celulares, laptops e consoles, e os fabricantes priorizam os pedidos com margens maiores. Analistas que acompanham a oferta de módulos projetam queda superior a 70 por cento no fornecimento de chips DRAM aos fabricantes de módulos em 2027.

**O CEO da Intel quantificou o problema.** No AI Infrastructure Summit em Santa Clara, em 15 de setembro de 2026, Lip-Bu Tan disse que os preços da memória já haviam subido "cinco, seis e sete vezes" em relação aos níveis anteriores. Alertou que a memória agora representa de 70 a 80 por cento da lista de materiais de um laptop barato. Separadamente, afirmou que não haverá alívio antes de 2028.

*A reportagem independente sobre a comparação por área entre wafers DRAM e wafers de lógica de ponta traz uma ressalva importante. Preços à vista não são preços contratuais, e a compra à vista de DDR5 é tão limitada que a comparação serve como indício, não como conclusão. A direção da tendência não está em dúvida.*

{{< figure src="local-ai-memory-price-trend-2026.webp" alt="Gráfico que mostra aumentos trimestrais nos preços contratuais de DRAM durante 2026, começando com alta de 90 a 95 por cento no primeiro trimestre e desacelerando para 13 a 18 por cento no terceiro" >}}

### O que isso fez com as placas de vídeo

A memória representa uma grande parte do custo de componentes de uma placa de vídeo, portanto preços de DRAM passam direto para preços de GPU.

| Placa | Início de 2025 | Setembro de 2026 |
|---|---|---|
| **Nvidia RTX 5090** | $1,999 | **mais de $5,000** |
| **Asus RTX 5080** | $1,199 | $1,595 |
| **AMD RX 9070 XT** | cerca de $830 | **mais de $1,037** |

Os aumentos chegaram em ondas coordenadas em 2026, não como picos isolados. A Nvidia elevou os preços em janeiro, novamente em maio especificamente para a RTX 5090 e outra vez no fim do ano. A AMD seguiu em agosto com alta de pelo menos 10 por cento em certas placas Radeon e kits de memória GDDR6, atribuindo o aumento diretamente ao custo da memória.

**A próxima geração foi adiada em vez de lançada.** Agora se espera que a série RTX 60 da Nvidia chegue em 2028, pulando 2027 por completo, devido à disponibilidade de memória.

*A placa que você compra hoje não concorre com uma placa mais barata no próximo ano. Ela concorre com uma versão mais cara de si mesma.*

## Por que esperar custa mais

O conselho habitual sobre hardware é aguardar a próxima geração. Em um mercado de memória com oferta restrita, esse conselho trabalha contra você.

Três pontos sustentam essa conclusão.

**Os preços já subiram e continuam crescendo.** Um salto de 90 a 95 por cento nos contratos de DRAM em um trimestre não é uma variação que se reverte no trimestre seguinte. A TrendForce prevê novos aumentos no terceiro trimestre, não queda, e o CEO da Intel situa o alívio em 2028.

**Não há produto de 2027 pelo qual valha esperar.** Quando as GPUs de consumo de próxima geração são adiadas para 2028, a estratégia de espera se estende por dois anos. Isso representa quase todo um ciclo de atualização de hardware sem retorno.

**Os modelos já são bons o suficiente.** Isso mudou em 2026. Dois anos atrás, hardware local oferecia uma experiência visivelmente pior. Hoje o mesmo dinheiro compra um modelo 27B a 135 tokens por segundo e janela de contexto de 262K, que supera um modelo avançado de API no índice agregado de inteligência.

*Se você esperava modelos locais melhores, a espera acabou. Se espera hardware mais barato, os dados de oferta dizem que terá de esperar até 2028.*

## O que montar

É simples ajustar o hardware aos modelos acima, pois os pesos ternários reduziram os requisitos.

| Categoria | Memória | O que executa com folga |
|---|---|---|
| **Entrada** | 8 a 12 GB de VRAM | 27B ternário com 5.53 a 6.70 GiB e espaço para contexto |
| **Prática** | 16 a 24 GB de VRAM | Qwen3.8 27B completo de 18 GB, ou o pacote ternário com contexto longo |
| **Confortável** | 32 GB de VRAM | 27B ternário no contexto máximo de 262K, ou MoE 80B com 3B ativos |
| **Memória unificada** | 64 a 128 GB | MoE esparsos maiores em Apple Silicon ou desktop de memória unificada |

Algumas observações práticas importam mais do que a tabela de categorias:

- **Compre memória, não a GPU topo de linha.** O pacote ternário de 5.53 GiB torna a categoria de entrada realmente útil. O dinheiro restante rende mais em RAM e armazenamento do que em uma placa topo de linha aos preços de 2026.
- **Sistemas de memória unificada oferecem bom valor.** Uma máquina com pelo menos 64 GB de memória compartilhada executa modelos esparsos maiores por uma fração do custo de uma placa dedicada com a mesma capacidade.
- **Energia e refrigeração contam.** Um computador executando inferência por horas se comporta de modo diferente de um que roda benchmarks por minutos.
- **Use o pacote ternário junto com um modelo menor.** Um modelo 3B responde perguntas simples; o 27B cuida das difíceis.

{{< centerbutton href="https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B" >}}
Baixar Ternary Bonsai 2 27B
{{< /centerbutton >}}

## Quando modelos avançados ainda valem o preço

A justificativa para a categoria avançada é real, mas mais restrita do que o marketing sugere.

**A resposta honesta é confiabilidade factual.** A precisão AA-Omniscience do Sonnet 4.6 é 40.9 por cento, contra 15.6 por cento do modelo aberto 27B. Quando uma resposta errada custa um cliente, um diagnóstico ou uma posição jurídica, uma diferença de 25 pontos importa mais do que qualquer índice agregado.

**Cadeias agentic longas são a segunda razão.** Sonnet 4.6 registra 53.0 por cento no Terminal-Bench Hard e 75.7 por cento no τ²-Bench Telecom, que medem uso prolongado de ferramentas e comportamento agentic em várias interações. A ficha do modelo aberto não apresenta resultados comparáveis, e essa ausência não é animadora.

**A terceira razão é operacional.** Uma API hospedada dispensa atualizações de drivers, peculiaridades de quantização, acompanhamento de um fork do llama.cpp e correção de uma base de pesos rotacionada. Outra equipe cuida da disponibilidade e recebe o alerta às três da manhã.

### A pergunta que vale fazer

Então, onde a categoria avançada faz sentido fora de grandes empresas?

**Ela ainda se justifica em trabalhos que exigem conhecimento confiável.** Pesquisa, análise jurídica, questões médicas, modelagem financeira e qualquer tarefa em que uma resposta errada e confiante seja cara. Essa categoria existe, e a diferença de precisão é um motivo real para pagar.

**Para trabalho generativo, a justificativa está diminuindo rapidamente.** Redigir, resumir, refatorar código, reformatar dados, classificar documentos e executar pipelines automatizados são tarefas cujos resultados são verificados antes de serem aceitos. A diferença de precisão custa pouco quando uma pessoa ou uma suíte de testes verifica a saída. Nesses trabalhos, é difícil defender o pagamento por token por um índice de 30.1 quando um índice de 33.7 roda sem custo adicional em um hardware que você já possui.

**A decisão passou da capacidade para a consequência.** Dois anos atrás, a pergunta era se um modelo local conseguia realizar o trabalho. Hoje, é quanto custa um erro e como você o detectaria.

*O adicional empresarial compra confiabilidade, conformidade e uma equipe de plantão. Os demais pagam por uma diferença que deixa de importar quando uma suíte de testes entra em ação.*

## Principais conclusões

- **Um modelo local 27B agora supera Claude Sonnet 4.6 no índice agregado de inteligência**, 33.7 contra 30.1, e lidera em programação, tarefas agentic, contexto longo e raciocínio científico de nível de pós-graduação.
- **Sonnet 4.6 ainda vence em precisão factual**, 40.9 por cento contra 15.6 por cento no AA-Omniscience, o argumento mais forte que resta para a categoria avançada.
- **A quantização ternária torna isso viável.** Bonsai 2 27B executa o mesmo modelo 26.90B em 5.53 GiB, em vez de 18 GB, e ambos usam licença Apache 2.0.
- **O Ollama padrão não executa os pacotes ternários.** Eles precisam do fork do llama.cpp da Prism ML, e o fallback F16 produz saída incoerente sem informar a falha.
- **A velocidade medida é de 135 tokens por segundo na decodificação** em uma RTX 5090, muito acima da velocidade de leitura.
- **Os preços da memória são motivo para agir agora.** Os contratos de DRAM subiram de 90 a 95 por cento em um único trimestre de 2026, e as GPUs de consumo de próxima geração foram adiadas para 2028.
- **A RTX 5090 passou de $1,999 para mais de $5,000** em menos de dois anos, e as outras categorias subiram junto.

## Próximas etapas

1. **Baixe o modelo e teste-o com sua própria carga de trabalho**: **[Ternary Bonsai 2 27B no Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)**
2. **Obtenha os pesos originais** em precisão total se tiver memória suficiente: **[Qwen3.8 no Ollama](https://ollama.com/library/qwen3.8)**
3. **Experimente o modelo antes de montar qualquer coisa** no endpoint hospedado gratuito: **[Qwen3.8 27B grátis no OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)**
4. **Compare com a categoria paga usando os mesmos prompts**: **[Claude Sonnet 4.6 no OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)**
5. **Dimensione o computador para a categoria de que precisa** usando a tabela de memória acima e compre a memória antes da placa de vídeo.
6. **Se tiver um Raspberry Pi parado**, veja se ele pode executar algo menor: **[Quais modelos de IA rodam em um Raspberry Pi 4 ou 5?](/articles/ai-models-raspberry-pi-4-5/)**

## Artigos relacionados

| Artigo | O que aborda |
|---|---|
| **[Quais modelos de IA rodam em um Raspberry Pi 4 ou 5?](/articles/ai-models-raspberry-pi-4-5/)** | O limite inferior da inferência local e o que placas pequenas conseguem executar de verdade |
| **[Como montar um assistente de IA que preserva a privacidade para Meshtastic](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Um assistente local em hardware fora da rede, onde privacidade é essencial |
| **[O papel da memória ECC na redução de corrupção de dados](/articles/the-role-of-ecc-memory-in-mitigating-data-corruption/)** | Por que a qualidade da memória importa mais quando um modelo grande depende dela |
| **[O que é um laboratório doméstico e você deveria ter um?](/articles/what-is-a-homelab-and-should-you-have-one/)** | Planejamento de espaço, energia e refrigeração para hardware que esquenta |

## Referências

1. [Ternary Bonsai 2 27B - espelho do modelo no Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)
2. [Qwen3.8 - biblioteca de modelos do Ollama](https://ollama.com/library/qwen3.8)
3. [Qwen3.8 27B (grátis) - benchmarks e preços no OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)
4. [Claude Sonnet 4.6 - benchmarks e preços no OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)
5. [Primeiro teste do Bonsai 2 27B: ele é o melhor modelo de IA para uma GPU? - Bijan Bowen](https://www.youtube.com/watch?v=OA5cICIzD-c)
6. [Artificial Analysis - avaliações independentes de modelos](https://artificialanalysis.ai/)
7. [TrendForce - previsões de preços contratuais de DRAM e NAND](https://www.trendforce.com/)
8. [Chips de memória agora custam mais que chips de computação por área - Tom's Hardware](https://www.tomshardware.com/pc-components/dram/dram-is-now-more-expensive-than-compute-chips-on-per-area-basis-ai-demand-drives-memory-die-value-past-leading-edge-silicon)
9. [Alívio para GPUs adiado para 2028 após recorde de 95% na DRAM - Tech Insider](https://tech-insider.org/gpu-relief-pushed-2028-dram-price-jump-2026/)
10. [Tan, da Intel: memória subiu 7 vezes e não haverá alívio até 2028 - shattered.io](https://shattered.io/intel-ceo-memory-shortage-no-relief-until-2028-2026/)
11. [Fork do llama.cpp da Prism ML - kernels ternários](https://github.com/PrismML-Eng/llama.cpp)
12. [Ternary-Bonsai-2-27B-gguf - pesos upstream](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)

---
title: "2x RTX 5060 Ti vs. GB10: benchmark local de IA com cinco modelos e contexto de 256K"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "Comparação de cinco modelos entre RTX 5060 Ti e GB10, além de um benchmark Qwen3.8 Flash-Next Strata no mesmo host até 256K de contexto."
genre: ["Inteligência artificial", "IA local", "Hardware de GPU", "Benchmarking", "Hardware de computador"]
tags: ["RTX 5060 Ti", "GB10", "DGX Spark", "Qwen3.8", "Qwen3.8 Flash-Next", "GSQ-RCO", "Qwen4Exp", "Strata", "Qwen3.5", "Qwen3.6", "GPT-OSS", "Nemotron", "LLM local", "inferência local", "memória unificada", "VRAM", "benchmark de GPU", "contexto longo", "sobrecarga PCIe", "hardware de IA", "NVIDIA Blackwell", "desempenho de LLM", "memória de GPU"]
cover: "/img/cover/nvidia-rtx-5060-ti-vs-gb10-memory-performance-comparison.webp"
coverAlt: "Ilustração de duas placas de vídeo NVIDIA RTX 5060 Ti à esquerda e um sistema NVIDIA GB10 à direita, ambos destacados contra um fundo escuro com cores vibrantes."
coverCaption: "O desempenho de modelos locais depende da arquitetura de memória, da escolha do modelo e do tamanho do contexto."
---

**Duas placas RTX 5060 Ti de 16 GB fornecem 32 GB de VRAM no total.** Um sistema NVIDIA GB10 oferece 128 GB de memória unificada coerente. O novo benchmark com cinco modelos apresenta um resultado mais equilibrado que o teste anterior, feito apenas com Qwen.

O sistema com duas placas lidera em velocidade de geração em quatro dos cinco modelos na configuração de 256K. O GB10 lidera com clareza no Qwen3.8 27B e mantém mais memória disponível para modelos, contexto e alocações do runtime. A melhor escolha depende do modelo e da carga de trabalho.

Um teste separado no mesmo host comparou Qwen3.8-Flash-Next IQ2_XS no Strata com Qwen3.8 27B Q4_K_M denso no Ollama. A mediana de geração após o aquecimento foi de 92.8 tokens por segundo para Flash-Next, com um prompt de 260,446 tokens. O Qwen3.8 denso atingiu 0.939 tokens por segundo com um prompt de 260,444 tokens.

O NVIDIA GB10 usa 128 GB de memória unificada coerente. A NVIDIA lista 128 GB de memória unificada LPDDR5x e TDP de 140 W para o chip da plataforma GB10. A RTX 5060 Ti usa 16 GB de GDDR7 por placa, interface de memória de 128 bits e potência gráfica total de 180 W. As [especificações da NVIDIA RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/) e do [NVIDIA GB10](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) descrevem essa diferença de hardware.

**Os dois sistemas expõem a memória de formas diferentes.** Duas placas criam dois pools separados de 16 GB. O GB10 mantém o modelo, os dados de contexto, os buffers do runtime e as alocações do sistema operacional em um único espaço de endereçamento compartilhado.

## Comparação de memória

| Sistema | Memória | Modelo de memória | Potência informada |
|---|---:|---|---:|
| **2x RTX 5060 Ti 16 GB** | 32 GB no total | Dois pools separados de memória de GPU | 360 W no total para as GPUs |
| **Sistema GB10** | 128 GB | Memória unificada coerente do sistema | TDP de 140 W do GB10 |

O GB10 não vence todos os testes de throughput por causa da largura de banda da memória LPDDR5x. Sua vantagem vem da capacidade e da alocação. CPU e GPU compartilham o mesmo espaço de endereçamento, então o conjunto de trabalho não precisa caber em dois dispositivos isolados de 16 GB.

O sistema com duas placas enfrenta um problema de alocação. O modelo precisa ser dividido entre as duas placas. O runtime precisa transferir dados entre elas. O tráfego PCIe aumenta a latência e consome largura de banda. Segundo as especificações da NVIDIA, a RTX 5060 Ti também não oferece suporte a NVLink.

## Benchmark com cinco modelos

A execução atualizada usou a mesma matriz de solicitações nos dois sistemas. Ela cobriu cinco modelos Ollama com configurações de contexto de 4K, 16K, 32K, 64K, 128K e 256K. Cada solicitação gerou 128 tokens com temperatura 0.

As tags dos modelos testados foram:

- **Qwen3.8 27B:** `qwen3.8:27b`
- **GPT-OSS 20B:** `gpt-oss:20b`
- **Qwen3.6 35B-A3B:** `qwen3.6:35b`
- **Qwen3.5 35B-A3B:** `qwen3.5:35b-a3b-q4_K_M`
- **Nemotron 3.5 Lightning 30B-A3B:** `nemotron-3.5-lightning:30b-a3b-q4_K_M`

O sistema com duas placas usou duas RTX 5060 Ti de 16 GB. O GB10 usou 128 GB de memória unificada. Os testes rodaram no Ollama, versão 0.34.2 no sistema com duas placas e 0.40.2 no GB10.

### Velocidade de geração

A velocidade de geração mede quantos tokens o modelo produz depois de processar o prompt. Essa métrica importa principalmente durante uma conversa interativa.

Sistema com duas RTX 5060 Ti:

| Contexto | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 91.518 | 162.027 | 117.547 | 156.104 | 55.654 |
| 16K | 87.176 | 161.377 | 112.903 | 140.596 | 51.656 |
| 32K | 82.372 | 157.055 | 106.455 | 144.833 | 47.369 |
| 64K | 74.661 | 135.106 | 95.979 | 125.008 | 38.863 |
| 128K | 62.767 | 130.924 | 79.572 | 115.352 | 26.399 |
| 256K | 67.853 | 106.221 | 58.947 | 67.159 | 1.079 |

GB10:

| Contexto | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 62.199 | 98.648 | 72.405 | 100.906 | 32.985 |
| 16K | 56.764 | 94.366 | 69.782 | 95.448 | 32.939 |
| 32K | 53.257 | 98.175 | 64.055 | 95.025 | 29.772 |
| 64K | 49.201 | 96.132 | 58.428 | 84.528 | 25.625 |
| 128K | 40.637 | 80.238 | 48.108 | 74.579 | 22.294 |
| 256K | 43.688 | 68.043 | 36.649 | 62.115 | 22.371 |

Em 256K, o sistema com duas placas gerou mais rápido em GPT-OSS, Nemotron, Qwen3.5 e Qwen3.6. O GB10 gerou mais rápido em Qwen3.8. A velocidade de Qwen3.8 caiu para 1.079 tokens por segundo no sistema com duas placas, enquanto o GB10 produziu 22.371 tokens por segundo.

O resultado de Qwen3.6 ficou próximo. O sistema com duas placas atingiu 67.159 tokens por segundo e o GB10, 62.115. O resultado não sustenta uma afirmação universal de que a memória unificada sempre vence ou de que duas GPUs discretas sempre vencem.

### Velocidade de processamento do prompt

O processamento do prompt mede a rapidez com que o runtime lê o contexto de entrada antes de gerar. Isso importa para documentos longos e recargas repetidas de contexto.

Sistema com duas RTX 5060 Ti:

| Contexto | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 4745.9 | 2409.0 | 2701.7 | 464.3 | 783.9 |
| 16K | 7617.0 | 3031.8 | 4175.3 | 2654.0 | 840.1 |
| 32K | 8099.5 | 3074.2 | 4335.8 | 2623.2 | 811.2 |
| 64K | 6809.5 | 2893.0 | 4129.9 | 2400.4 | 727.8 |
| 128K | 5089.9 | 2362.7 | 3084.0 | 1723.6 | 546.1 |
| 256K | 5838.3 | 1813.2 | 2229.1 | 1011.0 | 251.3 |

GB10:

| Contexto | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 3295.5 | 576.0 | 2067.9 | 628.8 | 756.9 |
| 16K | 4675.5 | 3006.7 | 2691.2 | 2556.3 | 812.6 |
| 32K | 4571.4 | 3077.9 | 2691.7 | 2563.9 | 794.1 |
| 64K | 3704.7 | 3066.9 | 2585.3 | 2444.9 | 714.0 |
| 128K | 2857.0 | 2802.9 | 2360.4 | 2229.9 | 655.5 |
| 256K | 3243.4 | 2325.4 | 1938.5 | 1817.6 | 535.1 |

Em 256K, o sistema com duas placas liderou o processamento de prompts em GPT-OSS e Qwen3.5. O GB10 liderou em Nemotron, Qwen3.6 e Qwen3.8. A arquitetura do modelo e o comportamento do runtime importam tanto quanto a interface de memória.

## Benchmarks suplementares de Qwen3.8 Flash-Next

Três execuções extras mediram pacotes GGUF de Qwen3.8 Flash-Next no sistema com duas RTX 5060 Ti, em configurações de contexto de 4K e 16K. Cada linha mostra a referência exata do modelo no Hugging Face e sua quantização.

| Modelo exato | Quantização | Geração em 4K | Geração em 16K |
|---|---:|---:|---:|
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS) | IQ2_XS | 31.77 tok/s | 28.20 tok/s |
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ3_S) | IQ3_S | 24.54 tok/s | 22.60 tok/s |
| [`hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M`](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF/tree/main) | Q4_K_M | 17.91 tok/s | 17.02 tok/s |

O pacote IQ2_XS atingiu o maior throughput desse grupo. O resultado em 4K foi de 31.77 tokens por segundo, contra 24.54 para IQ3_S e 17.91 para Q4_K_M. Em 16K, a mesma ordem se manteve, com 28.20, 22.60 e 17.02 tokens por segundo.

Execute as mesmas referências exatas de modelo no Ollama:

```bash
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S
ollama run hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M
```

Esses resultados suplementares anteriores são observações do sistema com duas GPUs. Eles são separados da matriz de solicitações comparável entre RTX 5060 Ti e GB10 acima. O registro informa as referências exatas dos modelos, as quantizações, as configurações de contexto solicitadas e a velocidade de geração. Ele não informa os digests de manifesto resolvidos, a contagem de tokens de prompt processados, o tamanho da saída, o estado de aquecimento, a divisão de dispositivos, CPU, RAM do sistema, refrigeração nem data de medição.

## Strata versus Ollama denso em 256K

**Um segundo benchmark, de 14 de outubro de 2026, comparou duas pilhas de modelo e runtime no mesmo host com duas RTX 5060 Ti.** A base densa usou [`qwen3.8:27b`](https://ollama.com/library/qwen3.8:27b), um modelo Qwen35 de 27.3 bilhões de parâmetros em Q4_K_M. A pilha Flash usou [Qwen3.8-Flash-Next IQ2_XS](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS), um modelo mixture-of-experts Qwen4Exp em um pacote nativo unificado do Strata.

Esta é uma comparação de pilhas completas. Arquitetura do modelo, quantização, empacotamento, roteamento de especialistas e mecanismo de inferência mudaram juntos. As variantes Flash IQ3_S e Q4_K_M ficaram fora desta etapa.

### Sistema e método de teste

| Componente | Configuração registrada |
|---|---|
| **GPUs** | 2x NVIDIA GeForce RTX 5060 Ti, 16 GiB cada, compute capability 12.0 |
| **Conexão das GPUs** | PCIe 4.0 x4 por placa, topologia PHB, sem NVLink |
| **CPU** | AMD Ryzen 9 5900XT, 32 threads |
| **Memória do host** | 62 GiB RAM e 15 GiB swap |
| **Driver NVIDIA** | 595.99.02 |

O harness gerou registros numerados sintéticos. Cada linha seguiu o formato `Record 00001: alpha beta gamma delta epsilon zeta eta theta iota kappa.` A instrução exigia `BENCHMARK_OK` primeiro, seguido de uma síntese técnica concisa até o limite de saída. Os seis prompts continham 180, 720, 1,500, 3,100, 6,200 e 12,400 registros.

Cada execução usou temperatura 0, seed 42 e comprimento máximo de saída de 128 tokens. Um aquecimento precedeu cinco solicitações medidas em cada contexto. Os testes Ollama usaram `/api/generate`. Os testes Strata usaram `/v1/chat/completions`. Todas as solicitações medidas foram concluídas sem erros de API.

Os controles de decodificação não foram iguais. O Strata definiu explicitamente `reasoning_effort` como `none` e desativou o thinking pelo template de chat. A solicitação Ollama densa não enviou `think: false`, e uma verificação posterior encontrou saída nos campos thinking e response. Interprete o resultado de geração como específico desses modos de decodificação.

| Configuração de contexto | Tokens de prompt densos | Tokens de prompt Flash |
|---:|---:|---:|
| **4K** | 3,824 | 3,826 |
| **16K** | 15,164 | 15,166 |
| **32K** | 31,544 | 31,546 |
| **64K** | 65,144 | 65,146 |
| **128K** | 130,244 | 130,246 |
| **256K** | 260,444 | 260,446 |

Os cabeçalhos dos dois modelos declaravam um contexto máximo de 262,144 tokens. Os prompts pareados diferiam por dois tokens em cada ponto de verificação.

### Mediana da velocidade de geração após o aquecimento

Cada mediana cobre cinco solicitações medidas após um aquecimento. Cada solicitação densa reutilizou todos os tokens do prompt anterior, exceto quatro. Cada solicitação Flash reutilizou todos, exceto sete. A tabela mede throughput de decodificação com cache de prefixo aquecido. Ela não mede a latência completa desde uma execução fria.

| Contexto | Flash IQ2_XS no Strata | Dense Q4_K_M no Ollama | Vantagem do Flash |
|---:|---:|---:|---:|
| **4K** | 98.4 tok/s | 65.0 tok/s | 1.51x |
| **16K** | 96.8 tok/s | 60.6 tok/s | 1.60x |
| **32K** | 95.3 tok/s | 64.4 tok/s | 1.48x |
| **64K** | 89.6 tok/s | 51.2 tok/s | 1.75x |
| **128K** | 92.9 tok/s | 31.5 tok/s | 2.95x |
| **256K** | 92.8 tok/s | 0.939 tok/s | 98.9x |

A pilha Flash ficou perto de 90 tokens por segundo de 64K a 256K. O Qwen3.8 denso desacelerou bastante depois de 64K e chegou a 0.939 token por segundo em 256K. A resposta Flash de 256K terminou normalmente após 67 tokens. A execução densa atingiu o limite de saída de 128 tokens.

### Processamento do primeiro prompt

| Contexto | Primeira solicitação Flash | Primeira solicitação densa |
|---:|---:|---:|
| **4K** | 1,134 tok/s | 832 tok/s |
| **16K** | 2,013 tok/s | 856 tok/s |
| **32K** | 2,386 tok/s | 799 tok/s |
| **64K** | 2,509 tok/s | 690 tok/s |
| **128K** | 2,538 tok/s | 489 tok/s |
| **256K** | 2,399 tok/s | 214 tok/s |

A primeira solicitação densa processou o prompt completo em cada ponto. O Strata reutilizou 16,384 tokens de prefixo em 64K, 49,152 em 128K e 114,688 em 256K. Considere as taxas Flash de 64K a 256K como throughput de continuação da primeira solicitação, não como prefill totalmente sem cache.

Em 256K, o Strata processou a primeira solicitação em 60.8 segundos. O Ollama levou cerca de 1,215.4 segundos. A reutilização do prefixo impede uma comparação direta de prefill frio nesse ponto.

### A alocação do runtime explica a diferença em contexto longo

O Ollama 0.34.2 usou llama-server 0.4.1-dev com offload de camadas CUDA, template ChatML e decodificação especulativa MTP com largura máxima de rascunho quatro. Os tamanhos de batch e microbatch foram 1,024 em 32K e 512 de 64K a 256K. Todas as 66 camadas densas permaneceram nas GPUs em 32K e 64K. Em 128K, 63 das 66 camadas ficaram nas GPUs e 1,404 MiB foram para memória mapeada pela CPU. Em 256K, 42 das 66 camadas ficaram nas GPUs e 6,002 MiB foram para memória mapeada pela CPU. A taxa de aceitação MTP em 256K foi de cerca de 69.4 por cento.

O Strata 0.1.44.1, com CUDA 13.0.3, manteve suas 48 camadas divididas entre as duas GPUs. A configuração de 4K e 16K colocou as camadas 0 a 23 na primeira GPU e 24 a 47 na segunda. Esta etapa usou uma reserva VRAM automática de 700 MiB e 16,047 slots de especialistas residentes.

A configuração de 32K a 256K colocou as camadas 0 a 24 na primeira GPU e 25 a 47 na segunda. Esta etapa usou prefill automático, probabilidade mínima especulativa de 0.5, armazenamento KV INT8, 32,768 células KV residentes por camada QSA, reserva VRAM de 832 MiB, cache de especialistas com 15,318 slots e 21,024 MiB, além de decodificação especulativa MTP com largura máxima de rascunho quatro.

O digest do blob nativo e PLE do Strata foi `sha256:1473e0664c2017095f9164b6d617d7a71893452c1180c83002c4f28fc8c2b0da`. A execução também dependia de um perfil de especialistas e de um pacote de rascunho MTP sem digests imutáveis publicados.

A execução Strata usou o modo padrão de ignorar a cauda de rota. Essa configuração altera um pouco a saída do modelo e torna o resultado específico à configuração de runtime registrada. As respostas Flash continham marcadores `BENCHMARK_OK`. As solicitações densas não tiveram erros de API, mas o harness principal não capturou o marcador. As linhas brutas registraram zero caracteres de resposta. Uma verificação posterior encontrou saída nos campos response e thinking e confirmou `BENCHMARK_OK` na resposta.

A configuração de 4K e 16K registrou 409 MiB livres em uma solicitação e recomendou uma reserva de 832 MiB. A configuração de contexto longo registrou 481 MiB livres em uma solicitação e recomendou uma reserva de 896 MiB. Ambos os valores ficaram abaixo do limite de paginação do driver de 512 MiB do mecanismo. Nenhuma solicitação falhou, mas esses estados de pouca memória afetam a repetibilidade.

**Interprete o valor de 98.9x como resultado de uma pilha completa em contexto longo, não como prova de uma vantagem de 98.9x do mecanismo isolado.** O teste manteve o host constante. Ele não isolou o modelo, a quantização nem o runtime.

## O tamanho real do prompt importa

O contexto solicitado não é igual à quantidade de tokens de prompt processados. Na configuração de 256K, as execuções de Qwen3.5, Qwen3.6, Nemotron e Qwen3.8 processaram cerca de 171,359 a 171,365 tokens de prompt reais nos dois sistemas.

O GPT-OSS processou 65,538 tokens de prompt reais na configuração de 256K em ambos os sistemas. Portanto, sua linha de 256K não representa o mesmo tamanho de entrada dos outros modelos.

O resultado de Qwen3.8 em 256K mostra a diferença mais clara. O sistema com duas placas processou 171,359 tokens de prompt a 251.3 tokens por segundo e gerou a 1.079 tokens por segundo. O GB10 processou a mesma quantidade a 535.1 tokens por segundo e gerou a 22.371 tokens por segundo.

**A configuração de contexto indica o limite solicitado.** A contagem real de tokens do prompt mostra quanto trabalho o runtime concluiu.

## Por que a VRAM agregada continua importante

### 1. O modelo não vê uma placa de 32 GB

Duas GPUs não juntam a memória em um único espaço de endereçamento local. Um runtime model-parallel divide camadas ou tensores entre dispositivos. Cada dispositivo precisa de espaço para os pesos atribuídos, buffers temporários e sua parte do estado de contexto.

A capacidade utilizável fica abaixo da soma simples. A sobrecarga exata depende do formato do modelo, da quantização, do backend de inferência, da divisão de tensores e do tamanho do contexto.

### 2. A memória de contexto cresce durante a geração

Os pesos do modelo são apenas parte do orçamento de memória. O cache de chave e valor, ou KV cache, armazena dados de atenção de tokens anteriores. Contextos mais longos exigem mais memória de cache. Um teste em 4K não prevê uma implantação em 128K ou 256K.

Os novos resultados mostram limites diferentes por modelo. Qwen3.8 sofre uma queda acentuada de geração no sistema com duas placas em 256K. Os outros quatro modelos mantêm velocidade de geração útil nos dois sistemas. A capacidade de memória continua importante porque determina quais combinações de modelo e contexto cabem com espaço para alocações do runtime.

### 3. Transferências PCIe acrescentam custo

Quando o runtime transfere ativações ou tensores entre GPUs, os dados passam pela interconexão do host. Isso cria pontos de sincronização e acrescenta latência a cada etapa. A penalidade depende da alocação dos tensores, da arquitetura do modelo, da quantização e do tamanho do contexto.

Isso não torna inútil um sistema com duas GPUs. A configuração do runtime e o modelo determinam o resultado. Um benchmark que relata apenas o processamento do prompt em 4K não mostra esse custo.

### 4. A eficiência energética é uma vantagem do sistema

O GB10 usa menos potência informada para o chip ou a GPU e oferece mais capacidade de memória. Duas RTX 5060 Ti representam 360 W de potência combinada das GPUs antes do restante do sistema. A NVIDIA lista TDP de 140 W para o GB10.

**O GB10 troca o throughput máximo em vários modelos por capacidade, um conjunto de trabalho compartilhado e menor potência informada das GPUs.** O sistema com duas placas entrega mais throughput medido em vários modelos MoE recentes.

## O sistema 5060ti-x2 custa muito menos

Uma workstation completa com duas RTX 5060 Ti de 16 GB estava listada por **$3,479** em 10 de outubro de 2026. A configuração inclui Intel Ultra 7 265K, placa-mãe Z890, 32 GB de DDR5, 1 TB de armazenamento, fonte de 1,000 W e as duas GPUs. [Veja a lista da workstation completa com duas GPUs](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white).

O marketplace dos EUA da NVIDIA lista o DGX Spark de 128 GB por **$6,950**. A oferta inclui 128 GB de memória unificada coerente e 4 TB de armazenamento NVMe, mas mostra o sistema sem estoque. [Consulte a lista atual do DGX Spark da NVIDIA](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/).

A AMD Ryzen AI Halo Developer Platform oferece outro ponto de comparação. Esse sistema Strix Halo está listado por **$3,999.99** na Micro Center com 128 GB de memória unificada LPDDR5x e 2 TB de armazenamento. O Strix Halo costuma ficar na mesma categoria prática de IA local que os sistemas GB10, embora testes independentes frequentemente coloquem o GB10 à frente em throughput e maturidade de software. [Consulte a oferta Linux atual da Micro Center](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false) e [leia a análise Strix Halo versus GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4).

| Sistema completo | Preço listado em 10 de outubro de 2026 | Diferença de preço |
|---|---:|---:|
| **Workstation 5060ti-x2** | $3,479 | Referência |
| **AMD Ryzen AI Halo, Strix Halo** | $3,999.99 | $520.99 a mais |
| **DGX Spark GB10 de 128 GB** | $6,950 | $3,471 a mais |

O GB10 oferece um pool maior de memória unificada e menor potência informada das GPUs. O sistema AMD oferece a mesma classe de memória de 128 GB por cerca de $4,000. A workstation 5060ti-x2 custa aproximadamente **50% do preço listado do GB10**, antes de impostos e frete.

São preços listados por fornecedores diferentes, não uma cesta de varejo controlada. A comparação também deixa o sistema 5060ti-x2 com menos memória do sistema e armazenamento. As placas RTX 5060 Ti de 16 GB estão listadas atualmente perto de **$789 a $830 cada**, muito acima do MSRP de lançamento de $429. A vantagem de preço do sistema com duas placas persiste durante o atual aumento de preços das GPUs. [Veja os preços atuais da RTX 5060 Ti](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/).

## O que isso significa para cargas de IA local

Uma configuração com duas placas de 16 GB executa vários modelos quantizados de 27B a 35B em contextos longos. O benchmark não aponta um único vencedor para todos os modelos.

Escolha o sistema com duas placas quando valorizar:

- **Maior velocidade de geração em GPT-OSS, Nemotron, Qwen3.5 e Qwen3.6** neste teste.
- **Maior throughput em contexto curto** nos cinco modelos.
- **Menor custo de compra** que o sistema GB10 listado.
- **Compatibilidade de software com GPUs discretas NVIDIA** e espaço para testar modelos futuros.

Escolha o GB10 quando valorizar:

- **Qwen3.8 27B em 256K**, onde o GB10 é mais de 20 vezes mais rápido na geração.
- **Um único pool de memória de 128 GB**, com mais espaço para pesos, KV cache e buffers do runtime.
- **Menor potência informada de GPU ou chip** que duas placas discretas.
- **Menos restrições de alocação entre dispositivos** para modelos que pressionam a configuração com duas placas.

Isso corresponde à orientação de dimensionamento em [16 GB de VRAM bastam para trabalhar seriamente com LLMs locais?](/articles/is-16gb-vram-enough-local-llm/), que considera pesos, contexto e alocações do runtime como um único orçamento. O [guia de 32 GB de VRAM para Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/) chega à mesma conclusão para sistemas com duas placas. Capacidade agregada não equivale a espaço utilizável.

Antes de comprar hardware para qualquer implantação de contexto longo, faça quatro perguntas:

- **A quantização escolhida cabe com os buffers do runtime?** Os pesos do modelo, sozinhos, não definem a necessidade de memória.
- **O contexto cabe sem pressão severa no KV cache?** Prompts longos mudam o resultado.
- **O runtime usa uma divisão eficiente entre dispositivos?** Transferências PCIe e alocação de tensores afetam cada token gerado.
- **O sistema conclui o contexto desejado?** Um resultado rápido em 4K não compensa uma carga de 256K que falha.

**O novo benchmark responde a essas perguntas por modelo.** Qwen3.8 favorece claramente o GB10 em 256K. Os outros quatro modelos favorecem o sistema com duas placas em velocidade de geração nesta configuração específica. O pool maior de memória unificada ainda oferece mais margem, mesmo sem gerar o maior throughput medido.

O mesmo hardware com duas GPUs também registrou uma mediana de 92.8 tokens por segundo após aquecimento em 256K com Flash-Next IQ2_XS no Strata. Esse resultado separado não muda o resultado do GB10 com Qwen3.8 denso. Flash-Next usa arquitetura mixture-of-experts, quantização, pacote, runtime e modo de decodificação diferentes. Este conjunto de dados não contém um resultado comparável de Flash-Next no GB10.

## Veredito

**O sistema com duas RTX 5060 Ti é mais rápido em geração para quatro dos cinco modelos testados em 256K.** Também custa cerca de metade do preço listado do GB10. O GB10 continua sendo a melhor escolha para Qwen3.8 27B em 256K, para margem de capacidade e para cargas que se beneficiam de um pool de memória coerente.

O resultado anterior, limitado ao Qwen, sugeria uma vitória simples do GB10. O novo teste com cinco modelos mostra por que essa conclusão era ampla demais. Arquitetura do modelo, versão do runtime, alocação de tensores e comportamento do contexto afetam o resultado.

Se você executa GPT-OSS, Nemotron 3.5 Lightning, Qwen3.5 ou Qwen3.6, o sistema com duas placas teve maior velocidade de geração neste benchmark. Se executa Qwen3.8 27B em 256K, o GB10 manteve uma velocidade útil enquanto o sistema com duas placas quase parou.

**Capacidade de memória e throughput são critérios de compra distintos.** O GB10 oferece quatro vezes a memória agregada e um conjunto de trabalho compartilhado mais simples. O sistema com duas placas oferece maior throughput observado na maioria dos modelos testados por um preço de sistema muito menor.

O resultado Strata acrescenta outra lição. A alocação do runtime, a arquitetura do modelo e o modo de decodificação mudaram o resultado em 256K no mesmo host com duas GPUs. Flash-Next IQ2_XS manteve uma mediana após aquecimento perto de 93 tokens por segundo, enquanto o Qwen3.8 denso enviou 24 camadas para fora das GPUs e caiu abaixo de um token por segundo.

## Limites do benchmark

O benchmark registra as tags dos modelos, os contextos solicitados, os tokens de prompt reais, a velocidade de processamento do prompt, a velocidade de geração, as versões do Ollama e o alvo de geração de 128 tokens. Ele não registra digests de manifesto resolvidos, potência da CPU, potência da tomada, velocidade dos ventiladores nem configuração de refrigeração.

As linhas GPT-OSS de 256K processaram 65,538 tokens de prompt reais nos dois sistemas. As outras linhas de 256K processaram cerca de 171K tokens de prompt reais. Trate os números como uma comparação observada entre sistemas, não como uma classificação universal de todos os pares de RTX 5060 Ti e de todas as implementações GB10.

A execução Strata versus dense registra contagens exatas de prompt, cinco solicitações medidas por contexto, versões do runtime, alocação dos dispositivos, configurações de cache e estado das solicitações. A comparação muda arquitetura do modelo, quantização, empacotamento, runtime e modo de decodificação ao mesmo tempo. O Strata também reutilizou prefixos de prompt acima de 32K. As solicitações de geração medidas nos dois stacks reutilizaram quase todo o prompt.

Não é possível reproduzir exatamente os testes com este artigo. O harness do benchmark, o layout do pacote Strata, o perfil de especialistas e o pacote de rascunho MTP não têm digests imutáveis publicados. O aviso de pouca VRAM também cria risco de variação entre execuções. O teste mantém o host constante, não o mecanismo de inferência.

As especificações de hardware acima vêm da NVIDIA. Os números de desempenho vêm da execução controlada do benchmark para este artigo.

## Referências

- [Biblioteca de modelos Qwen3.8 do Ollama](https://ollama.com/library/qwen3.8)
- [Modelos GGUF Qwen3.8 Flash-Next GSQ-RCO da ISTA-DASLab](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF)
- [Modelos GGUF Qwen3.8 Flash-Next Uncensored da orcarouter](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF)
- [Biblioteca de modelos Qwen3.5 do Ollama](https://ollama.com/library/qwen3.5)
- [Biblioteca de modelos Qwen3.6 do Ollama](https://ollama.com/library/qwen3.6)
- [Biblioteca de modelos Nemotron 3.5 Lightning do Ollama](https://ollama.com/library/nemotron-3.5-lightning)
- [Tags GPT-OSS do Ollama](https://ollama.com/library/gpt-oss/tags)
- [16 GB de VRAM bastam para trabalhar seriamente com LLMs locais?](/articles/is-16gb-vram-enough-local-llm/)
- [32 GB de VRAM para Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/)
- [Guia de contexto de GPU para IA local](/articles/local-ai-model-gpu-context-guide/)
- [Benchmarks de GPU Qwen3.8 27B na Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/)
- [Lista da workstation completa com duas RTX 5060 Ti de 16 GB](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white)
- [Lista do marketplace dos EUA NVIDIA DGX Spark](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)
- [Lista Linux AMD Ryzen AI Halo de 128 GB](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false)
- [Análise da Tom's Hardware sobre Strix Halo versus GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4)
- [Preços atuais da RTX 5060 Ti](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/)

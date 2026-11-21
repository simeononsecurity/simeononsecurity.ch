---
title: "Benchmarks de GPU para Llama 3.1 8B e Qwen3.8 27B na Vast.ai"
date: 2026-10-02
lastmod: 2026-11-20
toc: true
draft: false
description: "Compare resultados medidos do Ollama para Llama 3.1 8B e Qwen3.8 27B em GPUs da Vast.ai, custos e opções de hospedagem."
genre: ["IA local", "Benchmarks de GPU", "IA autohospedada", "Infraestrutura em nuvem", "Inteligência artificial", "Economia da IA"]
tags: ["Llama 3.1 8B", "llama3.1:8b", "Qwen3.8 27B", "Qwen3.8:27b", "Vast.ai", "benchmark de GPU", "Ollama", "H100", "RTX PRO 5000", "RTX 6000 Ada", "RTX PRO 6000 Max-Q", "A100", "CMP 170HX", "LLM local", "contexto longo", "aluguel de GPU", "IA autohospedada", "modelos abliterated", "modelos sem censura", "créditos de API", "assinatura de IA", "Q4_K_M", "tokens por segundo"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Espaço de trabalho de alta tecnologia com uma placa gráfica e telas exibindo resultados de benchmark de IA local"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**A H100 SXM foi a placa mais rápida nos dois testes de modelos do Ollama, mas não ofereceu o melhor custo-benefício.** A RTX PRO 5000 e a RTX 6000 Ada equilibraram melhor velocidade e custo de aluguel. A CMP 170HX teve a menor tarifa por hora entre as execuções concluídas do Qwen3.8 27B.

*Estes resultados medem um modelo, um wrapper do Ollama, uma quantização padrão e um padrão de serviço. Use-os para dimensionar esta carga de trabalho, não como um ranking universal de GPUs.*

Este artigo compara **Llama 3.1:8b**, uma compilação Q4_K_M do Ollama com 8,03 bilhões de parâmetros, com **Qwen3.8:27b**, uma compilação Q4_K_M do Ollama com cerca de 27,3 bilhões de parâmetros. Ambos foram testados em instâncias de GPU alugadas pela Vast.ai. Os testes mediram a taxa de decodificação em comprimentos reais de prompt até o limite de contexto suportado.

## Resposta curta

**Alugue uma RTX PRO 5000 ou RTX 6000 Ada para o uso regular de uma pessoa.** A RTX PRO 5000 liderou a comparação de custo-benefício em contextos curtos e médios. A RTX 6000 Ada custou menos e manteve uma vantagem útil sobre as placas A100. Alugue uma H100 SXM quando a velocidade de resposta importar mais que o preço por hora ou quando a carga incluir prompts longos.

| Objetivo | Recomendação | Motivo |
|---|---|---|
| **Menor custo de teste** | CMP 170HX | $0.420 por hora e VRAM suficiente para os modelos Q4_K_M testados |
| **Melhor custo-benefício abaixo de $1.25/h** | RTX PRO 5000 ou RTX 6000 Ada | Boa velocidade de decodificação sem o custo de aluguel da H100 |
| **Respostas mais rápidas** | H100 SXM | Maior velocidade de decodificação nos dois testes de modelo |
| **Qwen com contexto longo** | H100 SXM ou RTX PRO 6000 Max-Q | Ambas concluíram a execução do Qwen com cerca de 131k tokens e bastante VRAM disponível |
| **Referência popular de 8B** | Llama 3.1:8b | Comparação prática de 8B com limite de contexto de 128K |
| **Carga recorrente pequena** | Créditos de API ou assinatura de chat | Sem custo de GPU ociosa, manutenção ou trabalho de implantação |
| **Carga privada e frequente** | Workstation própria com GPU | O custo do hardware fica mais fácil de justificar com uso contínuo |
| **Testes de modelos abliterated ou sem censura** | Alugue primeiro e só compre após uso contínuo | Comportamento do modelo, licenciamento e risco operacional merecem testes próprios antes da compra de hardware |

## O que foi testado

**O benchmark usou o Ollama com a compilação padrão Q4_K_M do modelo.** Não foram adicionados quantização especial, decodificação especulativa, sampler personalizado ou outro stack de serviço. O objetivo foi uma comparação simples e reproduzível localmente entre as instâncias de GPU.

A Vast.ai descreve seu serviço como um mercado de GPUs em nuvem que conecta provedores de computação a usuários. A documentação lista opções sob demanda, reservadas, interrompíveis e sem servidor, além de filtros de busca por modelo de GPU, memória, preço e disponibilidade. As tarifas por hora abaixo vieram das instâncias selecionadas nesta sessão de benchmark, não de uma tabela permanente de preços da Vast.ai.

A saída medida foi a **taxa de decodificação**, expressa em tokens gerados por segundo. A taxa de prefill aparece separadamente porque mede o processamento do prompt, não a velocidade com que a resposta aparece. Um prompt longo costuma levar bastante tempo para ser processado mesmo quando a velocidade de decodificação continua alta.

O benchmark usou duas tentativas válidas por contexto e registrou a mediana do resultado de decodificação. Os níveis de prompt concluídos se basearam nos valores reais de `prompt_eval_count`:

- **Cerca de 16,4k tokens de prompt**
- **Cerca de 32,8k tokens de prompt**
- **Cerca de 65,5k tokens de prompt**
- **Cerca de 131k tokens de prompt**

A execução solicitada de 256k tokens não foi concluída. As placas A100 de 40 GB e várias placas menores ainda estavam processando ou não terminaram no comprimento de contexto alvo.

> **Limite do benchmark:** Os números descrevem duas cargas Q4_K_M no Ollama com um padrão de serviço. Eles não preveem velocidade de treinamento, taxa para vários usuários, geração de imagens, desempenho do vLLM ou resultado de outro modelo.

## Novo teste do Llama 3.1 8B

**O Llama 3.1:8b oferece uma referência prática útil para o mesmo conjunto de GPUs.** O Ollama lista cerca de 120 milhões de downloads do modelo, o que o torna uma opção razoável como segundo benchmark baseado em popularidade. A [página oficial do modelo no Ollama](https://ollama.com/library/llama3.1:8b) lista uma compilação Q4_K_M de 4,9 GB, 8,03 bilhões de parâmetros e uma janela de contexto de 128K.

O novo teste usou um executor de benchmark específico para o modelo e calibrou o gerador de prompts com o tokenizer do Ollama. Os rótulos abaixo usam contagens reais de prompt, não configurações de contexto solicitadas:

- **Cerca de 32.676 tokens reais de prompt** para o alvo de 32k
- **Cerca de 65.342 tokens reais de prompt** para o alvo de 64k
- **Cerca de 130.671 tokens reais de prompt** para o alvo de 128k

O nível de 256k não é compatível com o Llama 3.1 8B porque o limite de contexto listado para o modelo é 128K. O executor adicionou tentativas repetidas e linhas de status para que um timeout continue visível na tabela.

### Resultados do Llama 3.1 8B

| GPU | Decodificação ~32k tok/s | Decodificação ~64k tok/s | Decodificação ~128k tok/s |
|---|---:|---:|---:|
| **H100 SXM** | **163.5** | **124.0** | **82.4** |
| **H100 SXM** | **158.6** | **121.2** | **80.6** |
| **RTX PRO 5000** | 110.1 | 79.8 | 49.9 |
| **CMP 170HX 64GB** | 91.9 | 71.0 | 50.1 |
| **RTX 6000 Ada** | 88.3 | 53.9 | 29.3 |
| **RTX PRO 6000 Max-Q** | 66.7 | 53.0 | 40.3 |
| **RTX PRO 6000 S** | 60.3 | 42.5 | 33.9 |
| **A100 SXM4 40GB** | 2.0 | 40.6 | 38.5 |
| **A100 PCIe 40GB** | 1.2 | 20.3 | 20.3 |
| **2x RTX 5060 Ti** | 1.3 | 26.8 | Tempo esgotado |

As duas linhas da H100 vieram de instâncias válidas separadas da mesma classe de GPU. Ambas ficaram claramente à frente das demais placas. Seus resultados em 32k foram de 44% a 48% mais rápidos que os da RTX PRO 5000, e os resultados em 128k foram cerca de 61% a 65% mais rápidos.

Os resultados de 32k da A100 e da RTX 5060 Ti são baixos demais para representar execução comparável de GPU nesta carga. O host com RTX 5060 Ti também teve timeout na segunda tentativa de 128k. Considere esse host inadequado para comparações válidas de taxa de GPU, não um resultado real de ranking.

| Alvo de contexto | Resultado |
|---|---|
| **32k** | Concluído em todos os 10 hosts |
| **64k** | Concluído em todos os 10 hosts |
| **128k** | Concluído em 9 hosts. O host com 2x RTX 5060 Ti teve timeout na segunda tentativa |
| **256k** | Não suportado em nenhum host porque o Llama 3.1 8B aceita até 128K de contexto |

## Comparação entre os dois modelos

**O Llama menor foi mais rápido em todas as GPUs comparáveis, mas tamanho e qualidade do modelo não são a mesma coisa.** O Llama 3.1 8B é uma referência popular que exige menos memória. O Qwen3.8 27B precisa de mais memória e oferece outro perfil de recursos. Use os números para orientar a escolha do hardware, não para declarar um modelo universalmente melhor.

| Caso de uso | Melhor referência de benchmark | Motivo |
|---|---|---|
| **Assistente rápido de 8B** | Llama 3.1:8b | Maior velocidade de decodificação e menor demanda de memória do modelo |
| **Dimensionamento de modelo local de 27B** | Qwen3.8:27b | Representa melhor uma carga maior em uma única GPU |
| **Limite de contexto de 128K** | Llama 3.1:8b | O modelo tem limite explícito de 128K, então 256k não é um alvo válido |
| **Teste de margem de VRAM** | Qwen3.8:27b | O modelo maior revela antes os limites de memória e de contexto longo |
| **Referência entre provedores** | Llama 3.1:8b | Popularidade e tamanho do modelo facilitam reproduzir o resultado |

O teste anterior do Qwen também corrigiu as contagens reais do prompt para cerca de **32.770**, **65.538** e **131.074** tokens nos níveis de contexto suportados. Esses rótulos corrigidos substituem os valores solicitados de `num_ctx` ao comparar execuções do Qwen.

## Cerca de 16k tokens

**A H100 SXM liderou a execução de contexto curto com 134.4 tokens de decodificação por segundo.** A RTX PRO 5000 veio em seguida, com 113.9 tokens por segundo, e custou menos da metade por hora.

| Posição | GPU | VRAM | Decodificação tok/s | Processamento do prompt tok/s | Tarifa de aluguel |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **134.4** | 89,974 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **113.9** | 68,726 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **89.1** | 95,856 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **84.1** | 72,235 | $1.507/hr |
| 5 | **A100 SXM4** | 40 GB | **60.6** | 53,048 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **51.5** | 51,122 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **49.3** | 52,773 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | **38.4** | 38,886 | $0.565/hr |

Com esse comprimento de prompt, a RTX PRO 5000 atingiu cerca de 84,7% da velocidade de decodificação da H100 por 37,3% da tarifa horária. A RTX 6000 Ada atingiu cerca de 66,3% da velocidade da H100 por 30,2% da tarifa.

## Cerca de 32,8k tokens

**O ranking permaneceu estável na execução de contexto médio.** A H100 SXM caiu para 120.0 tokens por segundo, enquanto a RTX PRO 5000 chegou a 105.0 e a RTX 6000 Ada a 75.7.

| Posição | GPU | VRAM | Decodificação tok/s | Processamento do prompt tok/s | Tarifa de aluguel |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **120.0** | 139,748 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **105.0** | 103,707 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **75.7** | 141,678 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **66.9** | 120,537 | $1.507/hr |
| 5 | **RTX PRO 6000 S** | 95.6 GB | **65.9** | 109,280 | $1.756/hr |
| 6 | **A100 SXM4** | 40 GB | **51.1** | 81,929 | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | **46.2** | 77,984 | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | **36.1** | 73,377 | $0.565/hr |

A RTX PRO 5000 continuou sendo o aluguel mais atraente deste grupo. Foi apenas 12,5% mais lenta que a H100 e custou 62,7% menos por hora.

## Cerca de 65,5k tokens

**Prompts mais longos ampliaram a diferença entre placas com grande capacidade de memória e placas com menos margem.** A H100 permaneceu em primeiro lugar, com 112.0 tokens por segundo. A RTX PRO 6000 Max-Q passou à frente da RTX 6000 Ada em velocidade de decodificação.

| Posição | GPU | VRAM | Decodificação tok/s | Processamento do prompt tok/s | Tarifa de aluguel |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **112.0** | 195,252 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **96.9** | 148,897 | $1.005/hr |
| 3 | **RTX PRO 6000 Max-Q** | 95.6 GB | **75.7** | 156,443 | $1.507/hr |
| 4 | **RTX 6000 Ada** | 48 GB | **70.8** | 208,400 | $0.813/hr |
| 5 | **A100 SXM4** | 40 GB | **49.3** | 147,699 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **45.9** | 118,657 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **37.0** | 124,927 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | N/D | N/D | $0.565/hr |

A RTX PRO 5000 ainda ofereceu o melhor equilíbrio na tabela concluída. A RTX 6000 Ada foi mais lenta, mas sua tarifa de aluguel menor a torna atraente para orçamentos que priorizam disponibilidade em vez de velocidade máxima.

## Cerca de 131k tokens

**Nesse comprimento de contexto, apenas a H100 superou 100 tokens de decodificação por segundo.** A RTX PRO 6000 Max-Q concluiu a execução com 73.4 tokens por segundo, seguida pela RTX 6000 Ada com 61.7.

| Posição | GPU | VRAM | Decodificação tok/s | Processamento do prompt tok/s | Tarifa de aluguel |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **108.2** | 242,093 | $2.693/hr |
| 2 | **RTX PRO 6000 Max-Q** | 95.6 GB | **73.4** | 197,208 | $1.507/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **61.7** | 278,283 | $0.813/hr |
| 4 | **RTX PRO 6000 S** | 95.6 GB | **39.4** | 124,653 | $1.756/hr |
| 5 | **RTX PRO 5000** | 47.8 GB | N/D | N/D | $1.005/hr |
| 6 | **A100 SXM4** | 40 GB | N/D | N/D | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | N/D | N/D | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | N/D | N/D | $0.565/hr |

A RTX PRO 6000 Max-Q tornou-se a alternativa prática à H100 para prompts longos. Ela entregou 67,8% da velocidade de decodificação da H100 por 56,0% da tarifa por hora. A RTX 6000 Ada custou menos, mas seus 48 GB de VRAM deixam menos espaço para prompts longos, lotes maiores ou outra configuração do modelo.

## Comparação geral de decodificação

| GPU | ~16k | ~32,8k | ~65,5k | ~131k |
|---|---:|---:|---:|---:|
| **H100 SXM** | **134.4** | **120.0** | **112.0** | **108.2** |
| **RTX PRO 5000** | 113.9 | 105.0 | 96.9 | N/D |
| **RTX 6000 Ada** | 89.1 | 75.7 | 70.8 | 61.7 |
| **RTX PRO 6000 Max-Q** | 84.1 | 66.9 | 75.7 | 73.4 |
| **RTX PRO 6000 S** | 49.3 | 65.9 | 37.0 | 39.4 |
| **A100 SXM4** | 60.6 | 51.1 | 49.3 | N/D |
| **CMP 170HX** | 51.5 | 46.2 | 45.9 | N/D |
| **A100 PCIe** | 38.4 | 36.1 | N/D | N/D |

**A H100 liderou todos os comprimentos de contexto concluídos.** Sua vantagem sobre a RTX PRO 5000 caiu de 20.5 tokens por segundo com cerca de 16k tokens para 12.0 com cerca de 32,8k. O ranking de custo-benefício depende de você precisar da resposta inicial mais rápida ou do menor custo em uma sessão longa.

## Custo por milhão de tokens decodificados

**O preço por hora sozinho oculta a comparação útil.** Dividir a tarifa informada pela taxa de decodificação fornece uma estimativa grosseira do aluguel para um milhão de tokens gerados. Isso ignora processamento do prompt, tempo ocioso, armazenamento, transferência de dados, impostos, descontos e execuções com falha ou interrompidas.

| GPU | Tarifa para contexto curto | Custo aprox. por 1M de tokens decodificados |
|---|---:|---:|
| **CMP 170HX** | $0.420/hr | $2.27 |
| **RTX PRO 5000** | $1.005/hr | $2.45 |
| **RTX 6000 Ada** | $0.813/hr | $2.53 |
| **A100 SXM4** | $0.680/hr | $3.12 |
| **A100 PCIe** | $0.565/hr | $4.09 |
| **RTX PRO 6000 Max-Q** | $1.507/hr | $4.98 |
| **H100 SXM** | $2.693/hr | $5.57 |
| **RTX PRO 6000 S** | $1.756/hr | $9.89 |

**A CMP 170HX venceu esta comparação aritmética restrita.** A RTX PRO 5000 e a RTX 6000 Ada ficaram perto e ambas ofereceram mais taxa que a CMP 170HX. No uso interativo, o tempo de espera adicional costuma importar mais que o menor custo por token.

## Alugar, comprar créditos, assinar ou comprar hardware?

**A opção certa depende da utilização e dos requisitos de controle.** O aluguel de GPU gera uma conta variável de computação. Créditos de API geram uma conta variável do modelo. Uma assinatura de chat é uma tarifa fixa de acesso com limites de uso. Hardware próprio é uma compra de capital seguida por custos de energia, refrigeração, manutenção e depreciação.

| Orçamento mensal e carga de trabalho | Caminho recomendado | Motivo | Principal concessão |
|---|---|---|---|
| **Menos de $10** | Comprar créditos de API ou usar um modelo local gratuito | Testa o fluxo sem custo de GPU ociosa | Menos controle sobre hospedagem do modelo e limites de solicitações |
| **$10 a $30** | Créditos de API para uso ocasional ou assinatura de chat para interação diária | Assinatura serve para chat humano; créditos servem para scripts e chamadas medidas | Nenhuma opção oferece por padrão um endpoint privado de 27B |
| **$30 a $100** | Alugar uma RTX 6000 Ada ou RTX PRO 5000 apenas durante sessões ativas | O orçamento cobre breves sessões de pesquisa e evita custos de propriedade | A instância ainda exige configuração, armazenamento, monitoramento e desligamento disciplinado |
| **$100 a $250** | Alugar uma placa rápida para tarefas agendadas ou testar uma workstation própria | O uso mensal contínuo começa a tornar a utilização visível | Disponibilidade e tarifas de aluguel mudam |
| **$250 a $600** | Comparar um mês de aluguel da RTX PRO 5000 com uma GPU local usada ou nova | Este é o ponto de decisão para inferência privada frequente | Hardware acrescenta energia, calor, suporte e risco de revenda |
| **Acima de $600** | Comprar hardware apenas com alta utilização ou reservar aluguel de classe H100 para picos | Estratégia mista evita manter hardware de pico para demandas ocasionais | O capital permanece preso a uma configuração |

Estas faixas orientam decisões, não são cotações de provedores. As tarifas do benchmark mostram a questão do ponto de equilíbrio: uma H100 a $2.693 por hora custa cerca de $64.63 por um dia contínuo de 24 horas e cerca de $1,941.00 por 30 dias, antes do armazenamento ou de outras cobranças. Uma RTX PRO 5000 a $1.005 por hora custa cerca de $24.12 por dia e $723.60 por 30 dias contínuos. O total de uma GPU alugada apenas durante sessões ativas é diferente do de uma GPU ligada o mês inteiro.

### Quando créditos de API compensam

**Créditos de API compensam quando o uso é irregular, a automação importa e a tarefa não exige um modelo local específico.** Eles evitam provisionamento de GPU, downloads de modelos, problemas de driver e tempo ocioso. Também permitem comparar vários modelos hospedados antes de investir em hardware.

Os preços de API variam por modelo e provedor. O catálogo de modelos da OpenRouter ajuda a comparar tamanhos de contexto, provedores e preços por token. Consulte a calculadora atual do provedor antes de comparar uma fatura de API com este benchmark. Uma GPU local gera tokens sem cobrança por token do provedor, mas a hora de aluguel continua contando enquanto a instância aguarda.

### Quando uma assinatura compensa

**Uma assinatura é adequada para quem usa um assistente hospedado todos os dias.** Por exemplo, os planos individuais atuais do Claude separam acesso gratuito, Pro e Max, com limites de uso e recursos diferentes. Uma assinatura não é o mesmo que acesso por API. Muitas vezes oferece uma interface refinada e ferramentas incluídas, enquanto créditos de API oferecem controle programático.

Escolha uma assinatura quando o trabalho for principalmente escrita interativa, pesquisa, programação ou revisão de arquivos. Escolha créditos de API quando um script, aplicativo ou agente precisar de um endpoint medido.

### Quando a Vast.ai compensa

**A Vast.ai compensa quando você precisa de um modelo aberto, controle privado do runtime ou um pico curto de alta taxa.** Você seleciona a GPU, inicia uma instância, executa o Ollama, testa um modelo e encerra a instância ao terminar. É uma boa opção para Qwen3.8 27B, variantes abliterated e outros arquivos de modelo que não cabem em um laptop de consumo.

O custo é trabalho operacional. Confirme que o modelo está usando a GPU, monitore a VRAM, proteja o serviço exposto, preserve os arquivos de modelo necessários e encerre a instância após a execução. Uma tarifa horária baixa não corrige uma instância esquecida ligada.

### Quando comprar uma GPU compensa

**Comprar hardware compensa após uso contínuo, requisitos estáveis do modelo e necessidade de controle local.** A compra remove o risco de disponibilidade do aluguel e oferece um ambiente persistente. Também permite executar dados privados sem enviar prompts a um provedor hospedado.

O preço de compra é apenas uma parte da conta. Inclua o sistema host, a fonte de alimentação, armazenamento, refrigeração, energia, risco de substituição e o valor do tempo de configuração. Uma placa de ponta também fica ociosa nos períodos em que créditos de API ou uma assinatura custariam menos.

As especificações de referência da NVIDIA para a RTX 4090 listam 24 GB de memória, potência gráfica total de 450 W e recomendação de potência mínima do sistema de 850 W. É uma referência útil para inferência local, mas seus 24 GB ficam abaixo da capacidade das configurações Q4_K_M de 27B testadas aqui. Verifique o uso real de memória do modelo, em vez de presumir que uma placa cabe pelo número de parâmetros.

## Modelos abliterated e sem censura

**Variantes de modelos abliterated e sem censura alteram a decisão de compra.** O atrativo costuma ser menos comportamento de recusa ou menos restrições integradas. Os custos incluem comportamento de segurança mais fraco, procedência incerta, formato de prompt inconsistente, mais necessidade de revisão e possíveis limites de licença ou uso aceitável.

Alugue antes de comprar esses modelos. Um teste de um dia com a RTX PRO 5000 pela tarifa informada custa cerca de $24.12 antes de outras cobranças. Isso basta para confirmar compatibilidade, uso da GPU, qualidade das respostas e risco operacional.

**Não exponha um modelo sem censura diretamente à Internet pública.** Coloque autenticação, limites de solicitações, controles de log e isolamento de rede à frente dele. Evite enviar dados pessoais, confidenciais ou regulamentados a uma fonte de modelo que você não revisou.

Se o modelo se tornar uma ferramenta diária, compare o total mensal do aluguel com o custo integral de uma workstation própria. Se o uso for ocasional, o aluguel continua mais fácil de encerrar e substituir.

## Ressalvas do benchmark

**Os resultados ausentes também fazem parte do resultado.** Um valor `N/A` significa que a execução não produziu uma medição válida. Não significa que a GPU seja lenta na proporção sugerida pelo resultado de outra placa.

- **A segunda instância H100 não produziu um conjunto válido de benchmark** porque o download do modelo terminou tarde demais.
- **A instância com 2x RTX 5060 Ti foi excluída** porque o Ollama carregou o modelo na CPU em vez de usar as GPUs.
- **O prompt de 256k tokens do Qwen3.8 27B não foi concluído.** O nível válido mais alto foi cerca de 131k tokens reais de prompt. O Llama 3.1 8B marca 256k como incompatível porque seu limite de contexto é 128K.
- **O `num_ctx` solicitado não foi usado como rótulo do ranking.** As tabelas finais usam valores reais de `prompt_eval_count`.
- **Duas tentativas válidas por contexto foram resumidas pela mediana do resultado de decodificação.** Isso reduz o efeito de uma execução lenta, mas não substitui uma série maior de testes.
- **O wrapper foi simples de propósito.** Uma implantação ajustada de vLLM ou llama.cpp produzirá outro ranking.

## Recomendação final

**Comece alugando uma RTX 6000 Ada ou RTX PRO 5000.** A RTX 6000 Ada é a opção econômica quando a tarifa de $0.813 por hora está disponível. A RTX PRO 5000 é a opção mais rápida abaixo do preço da H100. Use a H100 SXM para prompts longos, latência interativa exigente ou uma janela curta de benchmark em que o tempo importa mais que o aluguel. Para um modelo de 8B, vale testar a CMP 170HX quando a tarifa horária menor importar mais que a velocidade máxima.

**Não compre uma GPU após um único teste bem-sucedido.** Alugue por um mês com cargas reais, registre horas ativas, comprimentos de prompt, concorrência e mudanças de modelo; depois compare o aluguel com o custo total de propriedade. Compre hardware quando a carga for frequente o bastante para manter a placa ocupada e estável o bastante para justificar a perda de flexibilidade.

Para uso ocasional, créditos de API ou assinatura de chat são mais simples. Para inferência local privada, experimentos com modelos abertos ou testes de modelos abliterated, a Vast.ai oferece um caminho com menor compromisso que comprar uma workstation de imediato. Use Llama 3.1 8B como referência de menor memória e Qwen3.8 27B quando o modelo maior for o alvo real de implantação.

## Próximos passos

Repita a comparação com seus próprios comprimentos de prompt e estimativa de horas ativas. Verifique o uso de GPU, registre a revisão do modelo e a versão do runtime, encerre a instância após cada execução e compare o aluguel mensal com o custo total de propriedade antes de comprar hardware.

## Referências

1. [Mercado de GPUs em nuvem da Vast.ai](https://vast.ai/)
2. [Documentação da Vast.ai: mercado, instâncias, preços e tipos de aluguel](https://docs.vast.ai/)
3. [Biblioteca de modelos Qwen3 do Ollama](https://ollama.com/library/qwen3)
4. [Página do modelo Llama 3.1 8B no Ollama](https://ollama.com/library/llama3.1:8b)
5. [Catálogo de modelos e comparação de preços da OpenRouter](https://openrouter.ai/models)
6. [Preços e planos individuais do Claude](https://www.anthropic.com/pricing)
7. [Especificações da NVIDIA GeForce RTX 4090](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)
8. [IA local em 2026: Qwen3.8 27B e hardware para modelos autohospedados](/articles/local-ai-2026-build-your-rig-now/)
9. [Testes de modelos Ollama em hardware Raspberry Pi](/articles/ai-models-raspberry-pi-4-5/)

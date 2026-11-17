---
title: "Benchmarks de modelos locais do Hermes: as combinações de GPU e modelo que eu escolheria"
date: 2026-10-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Minhas recomendações de modelos Hermes vêm de testes de contexto longo, ferramentas, streaming e visão nos sistemas RTX 5060 Ti, RTX 2000E Ada, RTX 3060 Ti e RTX 3070."
genre: ["Inteligência artificial", "IA local", "Informática"]
tags: ["Hermes Agent", "modelos de linguagem locais", "benchmarks de LLM", "inferência em GPU", "RTX 3060 Ti", "RTX 3070", "RTX 2000E Ada", "RTX 5060 Ti", "qualificação de modelo", "chamada de ferramentas", "contexto longo", "llama.cpp", "Ollama", "Qwen3.5", "Qwen3.6", "Qwen3.8"]
cover: "/img/cover/hermes-local-model-gpu-benchmarks.webp"
coverAlt: "Ilustração de placas gráficas com duas ventoinhas e de perfil baixo ao lado do título Hermes Model Benchmarks sobre fundo azul-escuro"
coverCaption: ""
---

Para tarefas do Hermes com contexto longo, eu começaria com Qwen3.5 35B em duas placas RTX 5060 Ti de 16 GB. A rota testada reteve 239.153 tokens de entrada pelo LiteLLM e passou por verificações separadas de ferramentas, streaming, visão, solicitações enfileiradas e cancelamento. Qwen3.6 é minha alternativa com uma placa. Nos sistemas RTX 3060 Ti e RTX 3070, eu começaria com Qwen3.5 2B ou 4B.

Essas escolhas vêm de executar modelos pelos caminhos de inferência usados pelo agente. Testei retenção de entradas longas, interações de ida e volta com ferramentas, respostas transmitidas, perguntas sobre imagens e liberação do modelo. Também testei os modos e as configurações de memória das rotas, porque carregar um modelo com sucesso diz pouco sobre sua utilidade durante uma solicitação longa do agente.

O Hermes exige pelo menos 64.000 tokens de contexto para uso de agentes com ferramentas. Usei 65.536 tokens de entrada reais como limite de qualificação de contexto longo. A contagem de tokens de entrada importa mais que o tamanho de contexto anunciado pelo servidor. ([Documentação de provedores do Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md))

## Quais GPUs havia em cada sistema

As letras dos sistemas identificam as combinações de hardware nos resultados.

| Sistema | GPUs usadas neste benchmark | Meu modelo inicial |
|---|---|---|
| A | 2 × GeForce RTX 5060 Ti, 16 GB cada | Qwen3.5 35B nas duas placas ou Qwen3.6 em uma placa |
| B | 1 × RTX 2000E Ada, 16 GB | Qwen3.5 9B quando o processamento de entrada longa por vários minutos serve à tarefa |
| C | 1 × RTX 2000E Ada, 16 GB | Gemma 3 4B para o caminho longo testado, Qwen3.5 0.8B sem raciocínio para tarefas de recuperação delimitadas |
| D | 1 × RTX 2000E Ada, 16 GB | Qwen3.5 9B, Gemma 4 12B-IT ou GPT-OSS 20B para as cargas testadas com modelos maiores |
| E | 9 × GeForce RTX 3060 Ti, 8 GB cada | Qwen3.5 2B ou 4B |
| F | 8 × GeForce RTX 3060 Ti, 8 GB cada | Qwen3.5 2B ou 4B |
| G | 3 × GeForce RTX 3070 | Qwen3.5 2B ou 4B |

O número de placas instaladas não significa que cada solicitação usou todas as GPUs. Os testes de Qwen3.5 35B e Flash Next usaram ambas as placas do sistema A. Qwen3.6 usou uma. A repetição de visão Qwen3.5 4B que teve sucesso no sistema E usou uma placa selecionada de um conjunto de oito, enquanto a nona ficou excluída de tarefas de IA.

Considere as durações abaixo como resultados conjuntos do modelo, do ambiente de execução e do sistema testados. Esses testes comparam configurações utilizáveis. Eles não isolam a arquitetura da GPU como causa das diferenças de velocidade.

## Duas RTX 5060 Ti fazem de Qwen3.5 35B minha escolha para contexto longo

Qwen3.5 35B produziu o maior resultado de retenção de entrada nesses testes. A progressão direta do Ollama reteve 248.279 tokens de entrada em um contexto de execução de 262.144 tokens. Uma solicitação separada de streaming pelo gateway reteve 239.153 tokens de entrada, retornou o marcador inicial e terminou naturalmente após 31 tokens de saída em 148,12 segundos.

O resultado do gateway importa para o Hermes porque a solicitação passou pelo broker e pelo LiteLLM. Outras solicitações completaram uma interação com ferramenta, reconheceram uma imagem vermelha e retornaram duas respostas corretas quando enviadas juntas. O broker enfileirou essas duas solicitações. Fechar uma solicitação em streaming liberou o broker e descarregou o modelo em 60,31 segundos.

| Solicitação Qwen3.5 35B | Tokens de entrada | Tokens de saída | Duração | Resultado |
|---|---:|---:|---:|---|
| Ollama direto, primeiro estágio progressivo | 69,429 | 31 | 38.783 s | Marcador inicial exato |
| Ollama direto, continuação com prefixo compartilhado | 124,179 | 31 | 28.472 s | Marcador inicial exato |
| Ollama direto, continuação com prefixo compartilhado | 182,579 | 31 | 38.974 s | Marcador inicial exato |
| Ollama direto, continuação com prefixo compartilhado | 248,279 | 31 | 54.215 s | Marcador inicial exato |
| Solicitação de streaming pelo broker | 69,427 | 29 | 38.872 s | Marcador inicial exato |
| Solicitação de streaming pelo LiteLLM | 239,153 | 31 | 148.12 s | Marcador inicial exato, descarga limpa |

As solicitações diretas progressivas reutilizaram um prefixo crescente. Suas durações descrevem o comportamento de continuação aquecida. O resultado de 54,215 segundos não é uma medição independente a frio do processamento de um novo prompt de 248K.

No maior estágio direto, o modelo informou cerca de 27,3 bilhões de bytes residentes nas duas GPUs. Os picos de memória por placa chegaram a 14.964 e 12.386 MiB.

As temperaturas máximas chegaram a 62 e 63 C, e a execução não registrou erros OOM ou Xid. A entrada deixou 13.865 tokens no contexto configurado para continuação. A resposta curta do marcador usou 31 deles.

Eu usaria essa rota quando reter um conjunto de trabalho grande importa mais que a resposta inicial mais curta. Os testes de ferramentas e visão demonstram comportamentos úteis do agente, enquanto o teste de entrada longa demonstra retenção. São cargas de trabalho distintas.

## Qwen3.6 é a opção de uma placa

Qwen3.6-35B-A3B UD-Q4_K_XL reteve 131.000 tokens de entrada em uma RTX 5060 Ti. A outra placa ficou ociosa durante o teste. Isso oferece ao sistema uma alternativa útil quando não se deseja dedicar as duas placas a um único modelo.

| Solicitação Qwen3.6 pelo gateway | Tokens de entrada | Tokens de saída | Duração | Resultado |
|---|---:|---:|---:|---|
| Solicitação longa inicial | 66,007 |  | 167.82 s | Marcador inicial retido |
| Solicitação mais longa | 90,000 | 11 | 159.92 s | Marcador inicial retido, nenhuma entrada em cache |
| Solicitação mais longa | 119,999 | 11 | 250.61 s | Marcador inicial retido, nenhuma entrada em cache |
| Perto do limite de execução | 131,000 | 11 | 287.09 s | Marcador inicial retido, nenhuma entrada em cache |

A solicitação de 131.000 tokens se aproximou do limite de execução de 131.072. Para um agente, eu deixaria mais espaço para a resposta e as mensagens posteriores das ferramentas. Uma retenção perto do limite é evidência útil de processamento de entrada, mas não representa um orçamento padrão sensato.

O uso de ferramentas passou com o raciocínio desativado. O raciocínio padrão consumiu a cota de teste de 512 tokens antes de emitir a chamada da ferramenta. O piloto bem-sucedido também passou por solicitações rápidas, de streaming e de visão. Sua verificação inicial de contexto com 65.845 tokens levou 139,57 segundos.

## Qwen3.8 27B vence a comparação de resposta equivalente em 66K

Para a mesma tarefa de marcador com 66.007 tokens no sistema A, Qwen3.8 27B retornou a resposta mais rapidamente. Eu manteria essa rota para solicitações próximas ao tamanho de entrada testado, junto de Qwen3.5 35B para o conjunto de trabalho maior.

| Rota do sistema A | Tokens de entrada | Duração | Resultado |
|---|---:|---:|---|
| Qwen3.8 27B | 66,007 | 54.64 s | Marcador inicial retido |
| Qwen3.6-35B-A3B UD-Q4_K_XL | 66,007 | 167.82 s | Marcador inicial retido |
| Qwen3.8-Flash-Next UD-IQ4_XS | 66,007 | 164.58 s | Marcador inicial retido |
| Alias de compatibilidade Flash Next IQ4 | 66,007 | 213.25 s | Marcador retido |

Qwen3.8 27B levou cerca de um terço do tempo das solicitações equivalentes de Qwen3.6 e Flash Next. São observações de solicitações completas com os ambientes testados, não uma comparação apenas de hardware.

Respostas rápidas, streaming e uso de ferramentas também passaram. O modo sem raciocínio completou a sequência de cores e a interação com a ferramenta, enquanto o teste com raciocínio retornou apenas parte da sequência dentro da cota de 512 tokens.

Flash Next continua sendo uma opção padrão menos atraente neste sistema por causa da pressão de memória. Seu piloto de 65.847 tokens passou em 201,41 segundos com contexto de execução de 98.304. Dois perfis anteriores de 131.072 atingiram os limites de memória antes de ficarem prontos.

A rota posterior chegou ao limite cgroup de 54 GiB. Para trabalho sem supervisão, eu escolheria uma rota com mais margem de memória.

A rota chamada `flash-iq2` serviu ao backend de compatibilidade Flash Next IQ4. O nome não identifica um resultado IQ2.

## A RTX 2000E Ada lida com entradas longas, mas o modelo altera a espera

Gemma 3 4B é minha rota testada preferida para entradas longas no sistema C. Dois caminhos retiveram mais de 84K tokens de entrada em cerca de 88 segundos. As rotas com modelos maiores também passaram por verificações úteis de retenção, mas suas solicitações levaram vários minutos.

| Sistema | Modelo e caminho | Tokens de entrada | Duração | Resultado |
|---|---|---:|---:|---|
| B | Qwen3.5 9B, gateway | 72,265 | 263 s | Ambos os marcadores retidos, verificação posterior de recuperação da mineração aprovada |
| C | Gemma 3 4B, gateway | 84,044 | 88.05 s | Marcador inicial retido |
| C | Gemma 3 4B, Aperture | 84,045 | 87.68 s | Marcador inicial retido |
| C | Gemma 4 12B-IT, gateway | 67,254 | 263.07 s | Marcador inicial retido |
| C | Gemma 4 12B-IT, Aperture sem streaming | 67,255 | 274.24 s | Marcador inicial retido |
| C | Gemma 4 12B-IT, streaming Aperture | 67,255 | 282.16 s | Marcador inicial retido |
| C | Qwen3.5 9B, gateway | 75,648 | 319.36 s | Marcador inicial retido, modelo descarregado |
| C | GPT-OSS 20B, gateway | 84,099 | 315.83 s | Marcador inicial retido, modelo descarregado |
| D | Qwen3.5 9B, Aperture | 81,051 | 324.07 s | Retenção aprovada no artefato instalado |
| D | Gemma 4 12B-IT, Aperture | 72,057 | 300.67 s | Retenção aprovada no artefato instalado |
| D | GPT-OSS 20B, Aperture | 72,104 | 245.94 s | Retenção aprovada no artefato instalado |

O streaming não removeu a longa espera de pré-processamento do Gemma 4 no sistema C. O primeiro conteúdo transmitido chegou após 277,49 segundos, mais tarde que a resposta completa de 274,24 segundos sem streaming. Uma tentativa anterior sem streaming expirou antes da repetição bem-sucedida. Eu reservaria essa rota para tarefas compatíveis com vários minutos de processamento inicial.

Gemma 3 4B também mostra por que eu qualificaria cada sistema testado separadamente. O sistema D não encontrou o marcador inicial em duas tentativas de recuperação de 65K, incluindo uma repetição com temperatura zero e 67.252 tokens de entrada. A solicitação determinística terminou naturalmente em 62,07 segundos com a GPU totalmente residente.

Uma conclusão rápida e uma resposta normal da API não tornaram a resposta correta. Eu usaria a rota bem-sucedida do sistema C e excluiria a rota malsucedida do sistema D da seleção do Hermes.

## O modo de raciocínio determina se Qwen3.5 0.8B é útil

Qwen3.5 0.8B tornou-se um candidato útil para recuperação delimitada no sistema C após desativar o raciocínio. O pequeno modelo Q8_0 reteve 75.649 tokens de entrada pelo gateway em 65,92 segundos. Esse resultado corresponde ao artefato Q8_0 testado e à rota sem raciocínio, não às configurações antigas de contexto 16K indicadas em outra parte da tabela.

| Solicitação Qwen3.5 0.8B no sistema C | Tokens de entrada | Tokens de saída | Duração | Resultado |
|---|---:|---:|---:|---|
| Raciocínio padrão, diagnóstico curto | 9,050 | 3,391 | 66.56 s | Marcador inicial exato |
| Raciocínio desativado, diagnóstico equivalente | 9,055 | 21 | 7.65 s | Marcador inicial exato, sem texto de raciocínio |
| Raciocínio padrão, tentativa longa |  |  | tempo limite de 600 s | Resposta não concluída |
| Raciocínio desativado, Ollama nativo | 75,656 | 22 | 69.80 s | Marcador inicial exato |
| Endpoint compatível com OpenAI sem raciocínio | 75,646 | 12 | 69.09 s | Marcador inicial exato |
| Broker com modo sem raciocínio imposto | 75,647 | 13 | 66.83 s | Marcador inicial exato |
| LiteLLM do sistema A para o sistema C | 75,649 | 15 | 65.92 s | Marcador inicial exato |

O diagnóstico equivalente caiu de 66,56 para 7,65 segundos, cerca de 8,7 vezes mais rápido, enquanto a saída gerada caiu de 3.391 para 21 tokens. Por isso eu definiria explicitamente o modo de raciocínio para tarefas simples de extração e roteamento. O raciocínio padrão gastou a maior parte do processamento em uma saída desnecessária para a tarefa.

Uma sondagem curta compatível com OpenAI não encontrou o marcador antes de uma repetição com temperatura zero passar. As verificações de rota bem-sucedidas usaram modo sem raciocínio e conclusão natural, sem limite de saída. Outros três gateways passaram solicitações curtas de marcador em 4,22, 4,37 e 3,85 segundos. Essas verificações estabelecem o roteamento, enquanto a solicitação de 75.649 tokens estabelece a retenção de entrada longa pelo gateway.

Eu testaria essa rota para recuperação e extração delimitadas. Escolheria um modelo maior para raciocínio aberto de agentes. Recuperar um marcador sintético é uma tarefa mais estreita que planejar, programar ou coordenar várias ferramentas.

## Os sistemas RTX 3060 Ti e RTX 3070 favorecem Qwen3.5 2B e 4B

Qwen3.5 2B e 4B são minhas escolhas práticas para começar nas placas de 8 GB. As solicitações de contexto textual nos sistemas E, F e G passaram com 65.579 tokens de entrada e durações de 30,343 a 93,753 segundos. As rotas 4B testadas também passaram por verificações de ferramentas, streaming e imagem.

A repetição do contexto de visão 4B no sistema E reteve ambos os marcadores e a ordem das cores da imagem com 65.637 tokens de entrada em 44,88 segundos. As solicitações com a ordem das cores direta e invertida também passaram. A repetição usou uma placa saudável depois que outra sofreu uma falha de link Xid 79 e o sistema reiniciou.

| Sistema | Contexto textual Qwen3.5 2B | Contexto textual Qwen3.5 4B | Contexto de visão Qwen3.5 4B |
|---|---|---|---|
| E, conjunto RTX 3060 Ti | 65,579 tokens, 30.343 s | 65,579 tokens, 53.787 s | 65,637 tokens, 44.88 s |
| F, conjunto RTX 3060 Ti | 65,579 tokens, 61.282 s | 65,579 tokens, 93.753 s | 65,635 tokens, 84.749 s |
| G, conjunto RTX 3070 | 65,579 tokens, 76.731 s | 65,579 tokens, 90.807 s | 65,635 tokens, 87.496 s |

Cada sistema registrou 29 verificações aprovadas. A diferença de tempo entre os dois sistemas RTX 3060 Ti também mostra por que eu escolheria um perfil de sistema testado em vez de classificar as placas com base nessas durações de solicitação.

Os sete sistemas voltaram à mineração após a janela de inferência. A verificação separada de recuperação após a parada no sistema B passou com novas shares aceitas. A placa que falhou no sistema E voltou à mineração após uma reinicialização e o reforço do link PCIe, mas continuou excluída do conjunto de IA. Restaurar a mineração no fim da janela é diferente da devolução automática após cada solicitação de inferência.

## Carregar um modelo não o qualifica

Eu excluiria DeepSeek Coder V2 16B das opções Hermes testadas para 65K. Seu teste com cache f16 reteve 50.477 tokens de entrada, mas a execução com alvo de 65K atingiu a proteção de VRAM. As alternativas de cache Q4 e Q8 carregaram os pesos nas GPUs, mas depois atingiram limites de memória do host ou baixa velocidade com prompts longos.

| Perfil de cache DeepSeek Coder V2 | Contexto de execução | Resultado observado | Minha avaliação |
|---|---:|---|---|
| f16 | 81,920 | Recuperação de 50.477 tokens aprovada, solicitação grande demais rejeitada | Resultado útil em contexto menor |
| f16 | 73,728 | Pré-processamento alvo de 65K parou com uso de GPU de 15.802 MiB | Não qualifica para 65K |
| Q4_0 | 98,304 | Pré-processamento longo caiu para 96.72 tokens/s antes da parada controlada | Pouco adequado a essa carga |
| Q8_0 | 77,824 | Pré-processamento longo caiu para 120.12 tokens/s antes da parada controlada | Pouco adequado a essa carga |
| Q4_0 / Q8_0, perfis maiores | 163,840 / 98,304 | Proteções de memória do host interromperam os testes | O encaixe de memória depende do sistema inteiro |

A lição prática é testar a solicitação que você pretende enviar. Residência na GPU, resposta curta e contexto configurado grande não demonstram retenção de entrada longa com latência útil.

Granite 4.2 8B e GPT-OSS 20B melhoraram após ajustes de rota no sistema A. A rota Q6_K do Granite reteve 66.082 tokens de entrada em 88,636 segundos sem entrada em cache. GPT-OSS completou a interação com ferramenta após a correção do broker, em 9,854 segundos para a chamada e 9,849 segundos para o acompanhamento. Eu manteria essas verificações de rota bem-sucedidas separadas das tentativas anteriores incompletas.

## Resultados completos dos benchmarks

A tabela contém 295 verificações em 59 combinações de modelos e sistemas. A matriz registra 273 aprovações, uma verificação de recuperação malsucedida e sete resultados incompletos, inconsistentes ou incompatíveis. Quatorze verificações ficam fora do escopo de qualificação de 65K. Cada linha mantém visível o resultado medido.

Minhas recomendações se aplicam às rotas e cargas aprovadas. Uma linha malsucedida ou incompleta não qualifica o comportamento correspondente.

Resultados de contexto curto e embeddings se aplicam às próprias cargas. Uma aprovação com contexto 16K ou 32K não qualifica uma rota para a carga Hermes de 65.536 tokens de entrada. Os nomes de modelo aqui são rótulos de rota. O rótulo `flash-iq2` serviu ao backend de compatibilidade IQ4.

A linha de contexto Qwen3.5 35B do sistema A corresponde ao estágio final de prefixo compartilhado da progressão acima. Durações de ferramentas com sinal de mais mostram a chamada e o acompanhamento separadamente.

A linha de concorrência fornece as durações das duas solicitações enfileiradas. A linha de cancelamento fornece o tempo de liberação após o cliente fechar o stream. As progressões adicionais de contexto e as comparações de rota Qwen3.5 0.8B aparecem em suas próprias tabelas acima.

### Sistema A

| Rótulo da rota do modelo | Verificação | Resultado | Tokens de entrada | Duração da solicitação |
|---|---|---|---:|---:|
| bonsai-2-27b | context | Aprovado | 65,621 | 88.746 s |
| bonsai-2-27b | quick | Aprovado | 57 | 6.429 s |
| bonsai-2-27b | stream | Aprovado |  | 9.371 s |
| bonsai-2-27b | tools | Aprovado |  | 10.478 s |
| deepseek-coder-v2:16b | context | Incompatível | 50,477 |  |
| deepseek-coder-v2:16b | quick | Aprovado | 77 | 43.239 s |
| flash-iq2 | context | Aprovado | 66,007 | 213.25 s |
| flash-iq2 | quick | Aprovado |  | 56.03 s |
| flash-iq2 | stream | Aprovado |  | 1.35 s |
| flash-iq2 | tools | Aprovado |  | 16.55 s |
| gemma-4-12b-it | context | Aprovado | 65,590 | 51.225 s |
| gemma-4-12b-it | quick | Aprovado | 21 | 5.166 s |
| gemma-4-12b-it | stream | Aprovado |  | 4.653 s |
| gemma-4-12b-it | tools | Aprovado |  | 18.72 s |
| gemma-4-12b-it | vision | Aprovado | 115 | 7.222 s |
| gemma-4-12b-it | vision_context | Aprovado | 65,685 | 56.06 s |
| gemma-4-12b-it | vision_reverse | Aprovado | 115 | 7.467 s |
| gemma-4-e4b-it | context | Aprovado | 65,590 | 21.889 s |
| gemma-4-e4b-it | quick | Aprovado | 21 | 17.919 s |
| gemma-4-e4b-it | stream | Aprovado |  | 4.25 s |
| gemma-4-e4b-it | tools | Aprovado |  | 8.734 s |
| gpt-oss-20b | context | Aprovado | 65,637 | 159.155 s |
| gpt-oss-20b | quick | Aprovado | 73 | 10.548 s |
| gpt-oss-20b | stream | Aprovado |  | 20.594 s |
| gpt-oss-20b | tools | Aprovado |  | 9.854 + 9.849 s |
| granite-4.2-3b | context | Aprovado | 65,589 | 70.968 s |
| granite-4.2-3b | quick | Aprovado | 20 | 4.009 s |
| granite-4.2-3b | stream | Aprovado |  | 5.365 s |
| granite-4.2-3b | tools | Aprovado |  | 6.086 s |
| granite-4.2-8b | context | Aprovado | 66,082 | 88.636 s |
| granite-4.2-8b | quick | Aprovado | 20 | 5.857 s |
| granite-4.2-8b | stream | Aprovado |  | 11.826 s |
| granite-4.2-8b | tools | Aprovado |  | 11.852 s |
| qwen27b | context | Aprovado | 66,007 | 54.64 s |
| qwen27b | quick | Aprovado | 57 | 31.5 s |
| qwen27b | stream | Aprovado |  | 0.92 s |
| qwen27b | tools | Aprovado |  | 4.25 s |
| qwen3-embedding-0.6b | context | Aprovado | 32,767 | 7.736 s |
| qwen3-embedding-0.6b | quick | Aprovado | 14 | 2.125 s |
| qwen3.5-0.8b | context | Aprovado | 16,429 | 10.5 s |
| qwen3.5-0.8b | quick | Aprovado | 17 | 14.316 s |
| qwen3.5-0.8b | stream | Aprovado |  | 2.125 s |
| qwen3.5-0.8b | tools | Aprovado |  | 4.416 s |
| qwen3.5-2b | context | Aprovado | 65,581 | 11.175 s |
| qwen3.5-2b | quick | Aprovado | 17 | 4.519 s |
| qwen3.5-2b | stream | Aprovado |  | 3.736 s |
| qwen3.5-2b | tools | Aprovado |  | 5.046 s |
| qwen3.5-4b | context | Aprovado | 65,579 | 36.451 s |
| qwen3.5-4b | quick | Aprovado | 15 | 19.935 s |
| qwen3.5-4b | stream | Aprovado |  | 17.496 s |
| qwen3.5-4b | tools | Aprovado |  | 7.308 s |
| qwen3.5-4b | vision | Aprovado | 70 | 7.848 s |
| qwen3.5-4b | vision_context | Aprovado | 65,635 | 28.24 s |
| qwen3.5-4b | vision_reverse | Aprovado | 70 | 4.386 s |
| qwen3.5-9b | context | Aprovado | 65,581 | 34.139 s |
| qwen3.5-9b | quick | Aprovado | 17 | 3.88 s |
| qwen3.5-9b | stream | Aprovado |  | 3.378 s |
| qwen3.5-9b | tools | Aprovado |  | 10.204 s |
| qwen3.5-9b | vision | Aprovado | 72 | 4.441 s |
| qwen3.5-9b | vision_context | Aprovado | 65,637 | 33.745 s |
| qwen3.5-9b | vision_reverse | Aprovado | 72 | 3.97 s |
| qwen3.5:35b-a3b-q4_K_M | cancellation | Aprovado |  | 60.31 s |
| qwen3.5:35b-a3b-q4_K_M | concurrency | Aprovado |  | 26.23 / 25.33 s |
| qwen3.5:35b-a3b-q4_K_M | context | Aprovado | 248,279 | 54.215 s |
| qwen3.5:35b-a3b-q4_K_M | gateway | Aprovado | 239,153 | 148.12 s |
| qwen3.5:35b-a3b-q4_K_M | quick | Aprovado | 79 | 10.08 s |
| qwen3.5:35b-a3b-q4_K_M | stream | Aprovado | 69,429 | 38.783 s |
| qwen3.5:35b-a3b-q4_K_M | tools | Aprovado |  | 15.22 + 14.83 s |
| qwen3.5:35b-a3b-q4_K_M | vision | Aprovado |  | 18.39 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | context | Aprovado | 65,845 | 139.57 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | quick | Aprovado | 15 | 3.97 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | stream | Aprovado |  | 0.45 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | tools | Aprovado | 293 | 5.48 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | vision | Aprovado | 38 | 0.59 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | context | Aprovado | 65,847 | 201.41 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | quick | Aprovado | 17 | 54.62 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | stream | Aprovado |  | 1.2 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | tools | Aprovado |  | 22.18 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | vision | Aprovado |  | 3.86 s |

### Sistema B

| Rótulo da rota do modelo | Verificação | Resultado | Tokens de entrada | Duração da solicitação |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Aprovado | 65,590 | 299.163 s |
| gemma-4-12b-it | quick | Aprovado | 21 | 15.261 s |
| gemma-4-12b-it | stream | Aprovado |  | 148.792 s |
| gemma-4-12b-it | tools | Aprovado |  | 34.124 s |
| gemma-4-12b-it | vision | Aprovado | 120 | 61.455 s |
| gemma-4-12b-it | vision_context | Aprovado | 65,690 | 295.581 s |
| gemma-4-12b-it | vision_reverse | Aprovado | 120 | 32.511 s |
| gemma3-4b | context | Aprovado | 65,584 | 67.382 s |
| gemma3-4b | quick | Aprovado | 15 | 6.329 s |
| gemma3-4b | stream | Aprovado |  | 24.138 s |
| gemma3-4b | vision | Aprovado | 306 | 7.018 s |
| gemma3-4b | vision_context | Aprovado | 65,876 | 70.912 s |
| gemma3-4b | vision_reverse | Aprovado | 306 | 5.762 s |
| gpt-oss-20b | context | Aprovado | 65,637 | 206.767 s |
| gpt-oss-20b | quick | Aprovado | 72 | 16.583 s |
| gpt-oss-20b | stream | Aprovado |  | 32.075 s |
| gpt-oss-20b | tools | Aprovado |  | 28.102 s |
| nomic-embed-text | context | Incompleto | 2,048 |  |
| nomic-embed-text | quick | Aprovado |  | 7.117 s |
| qwen3-14b | context | Incompleto |  | 1800.09 s |
| qwen3-14b | quick | Aprovado | 15 | 37.199 s |
| qwen3-14b | stream | Aprovado |  | 35.471 s |
| qwen3-14b | tools | Aprovado |  | 87.554 s |
| qwen3-8b | context | Fora do escopo abaixo de 65K, excluído |  |  |
| qwen3-8b | quick | Fora do escopo abaixo de 65K, aprovado | 15 | 21.059 s |
| qwen3-8b | stream | Fora do escopo abaixo de 65K, excluído |  |  |
| qwen3-8b | tools | Fora do escopo abaixo de 65K, excluído |  |  |
| qwen3.5-9b | context | Aprovado | 65,579 | 282.796 s |
| qwen3.5-9b | litellm_long_route | Aprovado | 72,265 | 263 s |
| qwen3.5-9b | post_external_stop_mining | Aprovado |  |  |
| qwen3.5-9b | quick | Aprovado | 15 | 25.881 s |
| qwen3.5-9b | stream | Aprovado |  | 143.44 s |
| qwen3.5-9b | tools | Aprovado |  | 31.812 s |
| qwen3.5-9b | vision | Aprovado | 75 | 32.015 s |
| qwen3.5-9b | vision_context | Aprovado | 65,640 | 396.288 s |
| qwen3.5-9b | vision_reverse | Aprovado | 75 | 28.626 s |

### Sistema C

| Rótulo da rota do modelo | Verificação | Resultado | Tokens de entrada | Duração da solicitação |
|---|---|---|---:|---:|
| gemma-4-12b-it | aperture_context | Aprovado | 67,255 | 274.24 s |
| gemma-4-12b-it | aperture_short | Aprovado | 35 | 39.32 s |
| gemma-4-12b-it | aperture_stream_context | Aprovado | 67,255 | 282.16 s |
| gemma-4-12b-it | context | Aprovado | 65,670 | 313.661 s |
| gemma-4-12b-it | gateway_context | Aprovado | 67,254 | 263.07 s |
| gemma-4-12b-it | gateway_short | Aprovado | 27 | 20.98 s |
| gemma-4-12b-it | quick | Aprovado | 21 | 16.447 s |
| gemma-4-12b-it | stream | Aprovado |  | 15.175 s |
| gemma-4-12b-it | tools | Aprovado |  | 37.821 s |
| gemma-4-12b-it | vision | Aprovado | 120 | 58.52 s |
| gemma-4-12b-it | vision_context | Aprovado | 65,690 | 308.759 s |
| gemma-4-12b-it | vision_reverse | Aprovado | 120 | 31.25 s |
| gemma3-4b | aperture_context | Aprovado | 84,045 | 87.68 s |
| gemma3-4b | aperture_after_system_d_route_change | Aprovado | 24 | 5.42 s |
| gemma3-4b | aperture_short | Aprovado | 22 | 5.45 s |
| gemma3-4b | aperture_stream | Aprovado |  | 3.72 s |
| gemma3-4b | context | Aprovado | 65,664 | 67.543 s |
| gemma3-4b | gateway_context | Aprovado | 84,044 | 88.05 s |
| gemma3-4b | gateway_short_via_system_a | Aprovado |  | 3.16 s |
| gemma3-4b | gateway_short_via_system_e | Aprovado |  |  |
| gemma3-4b | gateway_short_via_system_f | Aprovado |  | 4.15 s |
| gemma3-4b | gateway_short_via_system_g | Aprovado |  | 6.06 s |
| gemma3-4b | quick | Aprovado | 15 | 5.163 s |
| gemma3-4b | stream | Aprovado |  | 24.691 s |
| gemma3-4b | vision | Aprovado | 306 | 7.318 s |
| gemma3-4b | vision_context | Aprovado | 65,876 | 72.476 s |
| gemma3-4b | vision_reverse | Aprovado | 306 | 5.831 s |
| gpt-oss-20b | context | Aprovado | 65,716 | 216.594 s |
| gpt-oss-20b | gateway_context | Aprovado | 84,099 | 315.83 s |
| gpt-oss-20b | gateway_short | Inconsistente |  |  |
| gpt-oss-20b | quick | Aprovado | 72 | 21.603 s |
| gpt-oss-20b | stream | Aprovado |  | 31.957 s |
| gpt-oss-20b | tools | Aprovado |  | 26.096 s |
| nomic-embed-text | context | Fora do escopo abaixo de 65K, incompleto | 2,048 |  |
| nomic-embed-text | quick | Fora do escopo abaixo de 65K, aprovado |  | 4.178 s |
| qwen3-14b | context | Fora do escopo abaixo de 65K, incompleto |  | 1800.06 s |
| qwen3-14b | quick | Fora do escopo abaixo de 65K, aprovado | 15 | 35.809 s |
| qwen3-14b | stream | Fora do escopo abaixo de 65K, aprovado |  | 35.43 s |
| qwen3-14b | tools | Fora do escopo abaixo de 65K, aprovado |  | 87.723 s |
| qwen3-8b | context | Fora do escopo abaixo de 65K, excluído |  |  |
| qwen3-8b | quick | Fora do escopo abaixo de 65K, aprovado | 15 | 21.293 s |
| qwen3-8b | stream | Fora do escopo abaixo de 65K, incompleto |  | 900.01 s |
| qwen3-8b | tools | Fora do escopo abaixo de 65K, excluído |  |  |
| qwen3.5-9b | context | Aprovado | 65,662 | 287.984 s |
| qwen3.5-9b | gateway_context | Aprovado | 75,648 | 319.36 s |
| qwen3.5-9b | gateway_short | Aprovado | 21 | 72.14 s |
| qwen3.5-9b | quick | Aprovado | 15 | 24.635 s |
| qwen3.5-9b | stream | Aprovado |  | 143.157 s |
| qwen3.5-9b | tools | Aprovado |  | 30.395 s |
| qwen3.5-9b | vision | Aprovado | 75 | 27.756 s |
| qwen3.5-9b | vision_context | Aprovado | 65,640 | 398.797 s |
| qwen3.5-9b | vision_reverse | Aprovado | 75 | 28.645 s |

### Sistema D

| Rótulo da rota do modelo | Verificação | Resultado | Tokens de entrada | Duração da solicitação |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Aprovado | 65,590 | 275.395 s |
| gemma-4-12b-it | exact_digest_aperture_65k | Aprovado | 72,057 | 300.67 s |
| gemma-4-12b-it | exact_digest_broker_short | Aprovado | 34 | 30.74 s |
| gemma-4-12b-it | quick | Aprovado | 21 | 15.05 s |
| gemma-4-12b-it | stream | Aprovado |  | 14.722 s |
| gemma-4-12b-it | tools | Aprovado |  | 33.869 s |
| gemma-4-12b-it | vision | Aprovado | 120 | 56.315 s |
| gemma-4-12b-it | vision_context | Aprovado | 65,690 | 282.174 s |
| gemma-4-12b-it | vision_reverse | Aprovado | 120 | 29.978 s |
| gemma3-4b | context | Aprovado | 65,584 | 63.564 s |
| gemma3-4b | exact_digest_65k_recall | Falhou | 67,252 | 62.07 s |
| gemma3-4b | quick | Aprovado | 15 | 5.151 s |
| gemma3-4b | stream | Aprovado |  | 22.552 s |
| gemma3-4b | vision | Aprovado | 306 | 8.276 s |
| gemma3-4b | vision_context | Aprovado | 65,876 | 67.575 s |
| gemma3-4b | vision_reverse | Aprovado | 306 | 5.651 s |
| gpt-oss-20b | context | Aprovado | 65,637 | 189.07 s |
| gpt-oss-20b | exact_digest_aperture_65k | Aprovado | 72,104 | 245.94 s |
| gpt-oss-20b | exact_digest_broker_short | Aprovado | 84 | 15.96 s |
| gpt-oss-20b | quick | Aprovado | 72 | 15.431 s |
| gpt-oss-20b | stream | Aprovado |  | 31.052 s |
| gpt-oss-20b | tools | Aprovado |  | 23.65 s |
| nomic-embed-text | context | Incompleto | 2,048 |  |
| nomic-embed-text | quick | Aprovado |  | 2.798 s |
| qwen3-14b | context | Incompleto | 40,939 | 872.209 s |
| qwen3-14b | quick | Aprovado | 15 | 36.021 s |
| qwen3-14b | stream | Aprovado |  | 33.491 s |
| qwen3-14b | tools | Aprovado |  | 82.471 s |
| qwen3-8b | context | Incompleto |  | 1800.07 s |
| qwen3-8b | quick | Aprovado | 15 | 19.283 s |
| qwen3-8b | stream | Aprovado |  | 19.401 s |
| qwen3-8b | tools | Aprovado |  | 65.054 s |
| qwen3.5-9b | context | Aprovado | 65,579 | 258.048 s |
| qwen3.5-9b | exact_digest_aperture_65k | Aprovado | 81,051 | 324.07 s |
| qwen3.5-9b | exact_digest_broker_short | Aprovado | 29 | 94.48 s |
| qwen3.5-9b | quick | Aprovado | 15 | 27.16 s |
| qwen3.5-9b | stream | Aprovado |  | 28.62 s |
| qwen3.5-9b | tools | Aprovado |  | 28.129 s |
| qwen3.5-9b | vision | Aprovado | 75 | 25.047 s |
| qwen3.5-9b | vision_context | Aprovado | 65,640 | 369.477 s |
| qwen3.5-9b | vision_reverse | Aprovado | 75 | 27.602 s |

### Sistema E

| Rótulo da rota do modelo | Verificação | Resultado | Tokens de entrada | Duração da solicitação |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Aprovado | 65,590 | 49.086 s |
| gemma-4-e4b-it | quick | Aprovado | 21 | 23.911 s |
| gemma-4-e4b-it | stream | Aprovado |  | 28.136 s |
| gemma-4-e4b-it | tools | Aprovado |  | 56.756 s |
| granite-4.0-h-tiny | context | Aprovado | 65,566 |  |
| granite-4.0-h-tiny | quick | Aprovado | 35 | 10.408 s |
| granite-4.0-h-tiny | stream | Aprovado |  | 27.798 s |
| granite-4.0-h-tiny | tools | Aprovado |  | 43.304 s |
| granite-4.2-3b | context | Aprovado | 65,589 | 1014.03 s |
| granite-4.2-3b | quick | Aprovado | 20 | 14.569 s |
| granite-4.2-3b | stream | Aprovado |  | 6.948 s |
| granite-4.2-3b | tools | Aprovado |  | 56.376 s |
| qwen3-embedding-0.6b | context | Aprovado | 32,767 | 20.387 s |
| qwen3-embedding-0.6b | quick | Aprovado | 14 | 9.592 s |
| qwen3.5-0.8b | context | Aprovado | 16,429 | 9.128 s |
| qwen3.5-0.8b | quick | Aprovado | 17 | 452.417 s |
| qwen3.5-0.8b | stream | Aprovado |  | 11.163 s |
| qwen3.5-0.8b | tools | Aprovado |  | 39.214 s |
| qwen3.5-2b | context | Aprovado | 65,579 | 30.343 s |
| qwen3.5-2b | quick | Aprovado | 15 | 12.509 s |
| qwen3.5-2b | stream | Aprovado |  | 26.165 s |
| qwen3.5-2b | tools | Aprovado |  | 42.056 s |
| qwen3.5-4b | context | Aprovado | 65,579 | 53.787 s |
| qwen3.5-4b | quick | Aprovado | 15 | 26.736 s |
| qwen3.5-4b | stream | Aprovado |  | 26.02 s |
| qwen3.5-4b | tools | Aprovado |  | 57.293 s |
| qwen3.5-4b | vision | Aprovado | 72 | 10.09 s |
| qwen3.5-4b | vision_context | Aprovado | 65,637 | 44.88 s |
| qwen3.5-4b | vision_reverse | Aprovado | 72 | 9.96 s |

### Sistema F

| Rótulo da rota do modelo | Verificação | Resultado | Tokens de entrada | Duração da solicitação |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Aprovado | 65,590 | 98.443 s |
| gemma-4-e4b-it | quick | Aprovado | 21 | 27.51 s |
| gemma-4-e4b-it | stream | Aprovado |  | 28.042 s |
| gemma-4-e4b-it | tools | Aprovado |  | 73.891 s |
| granite-4.0-h-tiny | context | Aprovado | 65,599 | 19.692 s |
| granite-4.0-h-tiny | quick | Aprovado | 35 | 43.818 s |
| granite-4.0-h-tiny | stream | Aprovado |  | 27.296 s |
| granite-4.0-h-tiny | tools | Aprovado |  | 75.377 s |
| granite-4.2-3b | context | Aprovado | 65,589 | 145.179 s |
| granite-4.2-3b | quick | Aprovado | 20 | 15.703 s |
| granite-4.2-3b | stream | Aprovado |  | 35.482 s |
| granite-4.2-3b | tools | Aprovado |  | 52.539 s |
| qwen3-embedding-0.6b | context | Aprovado | 32,767 | 20.656 s |
| qwen3-embedding-0.6b | quick | Aprovado | 14 | 8.122 s |
| qwen3.5-0.8b | context | Aprovado | 16,429 | 13.326 s |
| qwen3.5-0.8b | quick | Aprovado | 17 | 445.22 s |
| qwen3.5-0.8b | stream | Aprovado |  | 13.266 s |
| qwen3.5-0.8b | tools | Aprovado |  | 40.825 s |
| qwen3.5-2b | context | Aprovado | 65,579 | 61.282 s |
| qwen3.5-2b | quick | Aprovado | 15 | 16.738 s |
| qwen3.5-2b | stream | Aprovado |  | 25.29 s |
| qwen3.5-2b | tools | Aprovado |  | 47.444 s |
| qwen3.5-4b | context | Aprovado | 65,579 | 93.753 s |
| qwen3.5-4b | quick | Aprovado | 15 | 33.039 s |
| qwen3.5-4b | stream | Aprovado |  | 25.658 s |
| qwen3.5-4b | tools | Aprovado |  | 71.731 s |
| qwen3.5-4b | vision | Aprovado | 70 | 43.053 s |
| qwen3.5-4b | vision_context | Aprovado | 65,635 | 84.749 s |
| qwen3.5-4b | vision_reverse | Aprovado | 70 | 27.518 s |

### Sistema G

| Rótulo da rota do modelo | Verificação | Resultado | Tokens de entrada | Duração da solicitação |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Aprovado | 65,590 | 92.696 s |
| gemma-4-e4b-it | quick | Aprovado | 21 | 38.329 s |
| gemma-4-e4b-it | stream | Aprovado |  | 43.549 s |
| gemma-4-e4b-it | tools | Aprovado |  | 66.616 s |
| granite-4.0-h-tiny | context | Aprovado | 65,599 | 69.777 s |
| granite-4.0-h-tiny | quick | Aprovado | 35 | 33.17 s |
| granite-4.0-h-tiny | stream | Aprovado |  | 31.751 s |
| granite-4.0-h-tiny | tools | Aprovado |  | 63.338 s |
| granite-4.2-3b | context | Aprovado | 65,589 | 100.849 s |
| granite-4.2-3b | quick | Aprovado | 20 | 23.355 s |
| granite-4.2-3b | stream | Aprovado |  | 28.75 s |
| granite-4.2-3b | tools | Aprovado |  | 44.226 s |
| qwen3-embedding-0.6b | context | Aprovado | 32,767 | 23.055 s |
| qwen3-embedding-0.6b | quick | Aprovado | 14 | 8.924 s |
| qwen3.5-0.8b | context | Aprovado | 16,429 | 16.74 s |
| qwen3.5-0.8b | quick | Aprovado | 17 | 504.813 s |
| qwen3.5-0.8b | stream | Aprovado |  | 15.095 s |
| qwen3.5-0.8b | tools | Aprovado |  | 36.672 s |
| qwen3.5-2b | context | Aprovado | 65,579 | 76.731 s |
| qwen3.5-2b | quick | Aprovado | 15 | 20.949 s |
| qwen3.5-2b | stream | Aprovado |  | 25.194 s |
| qwen3.5-2b | tools | Aprovado |  | 37.552 s |
| qwen3.5-4b | context | Aprovado | 65,579 | 90.807 s |
| qwen3.5-4b | quick | Aprovado | 15 | 41.84 s |
| qwen3.5-4b | stream | Aprovado |  | 40.812 s |
| qwen3.5-4b | tools | Aprovado |  | 54.999 s |
| qwen3.5-4b | vision | Aprovado | 70 | 29.619 s |
| qwen3.5-4b | vision_context | Aprovado | 65,635 | 87.496 s |
| qwen3.5-4b | vision_reverse | Aprovado | 70 | 26.283 s |

## Como testei a viabilidade do Hermes

Usei um marcador sintético perto do início de um prompt longo e pedi o marcador após o texto de preenchimento. A resposta precisava retornar o valor esperado. A contagem de tokens de entrada informada pelo servidor determinou o tamanho da solicitação. Um modelo que respondia normalmente após um prompt grande ainda falhava se o marcador inicial estivesse errado.

A progressão Qwen3.5 35B usou registros de preenchimento numerados, temperatura 0 e comprimentos crescentes de 3.800, 6.800, 10.000 e 13.600 registros. Esses estágios retornaram 69.429, 124.179, 182.579 e 248.279 tokens de prompt. O modelo permaneceu carregado entre os estágios, permitindo a reutilização de prefixo. As verificações separadas de Qwen3.6 perto do limite informaram zero tokens em cache.

O prompt longo de 0.8B repetiu `river stone lantern orchard circuit velvet compass marble` 8.400 vezes entre uma chave de resposta inicial e uma pergunta final de recuperação. A execução nativa enviou `think:false`, `num_ctx:131072`, `stream:false` e `keep_alive:0`. A rota compatível com OpenAI usou `reasoning_effort:"none"`. O broker impôs o modo sem raciocínio na rota, então os clientes do gateway não precisaram de uma substituição no cliente.

### Verificações de ferramentas, visão e liberação

Os testes de ferramentas verificaram a solicitação e a resposta após o retorno do resultado da ferramenta. Um teste simples usou `add_numbers(7, 11)` e esperou 18. O teste Qwen3.5 35B usou `lookup_square` e esperou 49. GPT-OSS fez uma consulta de inventário e precisava incorporar o resultado retornado.

As verificações de visão usaram perguntas sobre imagens vermelhas e azuis, inverteram a ordem das imagens e incluíram cores de imagens e marcadores inicial e final em prompts longos. O teste Qwen3.5 35B usou um PNG vermelho de 256 × 256. Foi necessária uma correção na conversão de conteúdo de imagem do broker antes de a solicitação passar. O teste longo de visão 4B no sistema E exigiu que ambos os marcadores e a ordem das cores sobrevivessem à entrada.

Verifiquei memória de GPU, residência do modelo, temperaturas, pressão de memória do host, eventos OOM e falhas de GPU durante e em torno das execuções longas. A proteção Qwen3.5 35B também verificou a liberação após uma interrupção controlada. Verificações posteriores de cancelamento do cliente e solicitações enfileiradas exercitaram o caminho do broker. Duas solicitações na fila demonstram o tratamento de solicitações sob a carga testada, não dois backends GPU independentes e simultâneos.

### Como interpretar os resultados de desempenho

As durações das solicitações incluem o pré-processamento de entradas longas e a resposta retornada. Elas não são tokens gerados por segundo. O atraso até o primeiro conteúdo importa no streaming, e as progressões de prefixo em cache precisam de uma interpretação própria.

As execuções posteriores bem-sucedidas dos modelos maiores nos sistemas A e C usaram janelas de inferência dedicadas com a mineração inativa. Os modelos foram descarregados após essas solicitações. A mineração foi restaurada nos sete sistemas ao fim da janela de teste. Esses resultados descrevem o serviço do modelo durante uma janela de inferência, não mineração e inferência simultâneas.

## Perfis de backend usados nos testes

Escolha o perfil vinculado à carga que deseja reproduzir. Quantização, contexto de execução, tipo de cache, modo de raciocínio e distribuição de GPU influenciam o resultado.

| Sistema e modelo | Perfil de backend testado |
|---|---|
| A, Qwen3.5 35B-A3B Q4_K_M | Ollama 0.34.2, cache KV f16, ambas as RTX 5060 Ti de 16 GB, 64 GiB de RAM do host e contexto de execução 262.144 para a progressão grande. As solicitações nativas usaram `think:false`, temperatura 0, streaming e cinco minutos de permanência entre estágios. Solicitações do gateway usaram o broker e o LiteLLM. Sem limite de saída da solicitação. |
| A, Qwen3.8 27B | llama.cpp sob demanda pelo broker e LiteLLM, contexto de execução 262.144, um slot de inferência, cache K/V Q4 e ambas as RTX 5060 Ti. A solicitação de 66.007 tokens não tinha limite de saída. |
| A, Qwen3.6-35B-A3B UD-Q4_K_XL | Strata 0.1.48, contexto 131.072, cache KV INT8, uma GPU selecionada, limite de memória de grupo de processos de 55 GiB, limite de execução de 30 minutos, carregamento preguiçoso, descarregamento após 60 segundos ocioso. Resposta longa piloto: 217 tokens de saída. Resposta do gateway perto do limite: 11 tokens de saída, sem limite de saída da solicitação. |
| A, Qwen3.8-Flash-Next UD-IQ4_XS | Strata 0.1.48, contexto 98.304, cache KV Q4, cache de especialistas residente de 8 GiB e ambas as RTX 5060 Ti. Limite de memória piloto de 52 GiB, rota posterior de 54 GiB. Resposta longa piloto: 10 tokens de saída. Combinações anteriores de contexto/cache maiores pararam nos limites de memória. |
| A, Granite 4.2 8B | Pesos GGUF Q6_K, processo de trabalho compartilhado do llama.cpp, contexto 131.072, cache K/V Q4_0, `--n-predict -1`. A solicitação longa usou temperatura 0, streaming de uso e sem limite de saída. |
| A, DeepSeek Coder V2 16B | Pesos GGUF Q4_0, Ollama 0.34.2, duas RTX 5060 Ti e 64 GiB de RAM do host. Testes separados de cache f16, Q4_0 e Q8_0 usaram os contextos de execução mostrados na tabela comparativa. Sem limite de saída da solicitação. |
| B, C, D, serviço Ollama auditado | Ollama 0.34.2, contexto 131.072, paralelismo 1, um modelo carregado, fila de tamanho 128, permanência 0, Flash Attention, cache KV Q4_0. |
| B, piloto de gateway Qwen3.5 9B | Tempo limite de rota LiteLLM de 1.800 segundos, zero novas tentativas e sem limite de contexto ou de tokens de saída. Ambos os marcadores foram retidos com 72.265 tokens de entrada. A verificação separada de recuperação da mineração passou. |
| C, Qwen3.5 0.8B | Pesos Q8_0 em uma RTX 2000E Ada com perfil de energia de 30 W. Contexto de execução 131.072. `think:false` nativo, `reasoning_effort:"none"` compatível com OpenAI, sem limite de saída. O alias do broker fixou o contexto de execução e impôs o modo sem raciocínio. |
| C, Gemma 4 12B-IT | Perfil Ollama de uma GPU, contexto de execução 131.072, solicitações Aperture com e sem streaming, sem limite de saída. A execução direta do Aperture atingiu pico de 75 C e 30,64 W no perfil configurado de 30 W e depois descarregou o modelo. |
| D, Qwen3.5 9B, Gemma 4 12B-IT, GPT-OSS 20B | Artefatos instalados exatos testados via Aperture, contexto de execução 131.072, residência completa em uma GPU e conclusão natural sem limite de saída da solicitação. |
| E, F, G, processos de chat do llama.cpp | Build 11669, 99 camadas de GPU, paralelismo 1, Flash Attention, cache K/V Q4_0, `--n-predict -1`. O contexto de execução variou pela família do modelo. |

Os perfis de serviço registrados descrevem suas próprias configurações de execução. O perfil Qwen3.5 35B com cache f16 testado separadamente no sistema A não herda as configurações de cache Q4_0 dos sistemas Ollama menores.

### Impressões digitais dos modelos nas novas execuções de retenção de entrada

Esses identificadores distinguem os artefatos testados de outros downloads ou aliases com nomes parecidos.

| Artefato | Quantização | Digest registrado ou SHA-256 do arquivo |
|---|---|---|
| Tag Ollama Qwen3.5 35B-A3B | Q4_K_M | `72aac7c28be8ff9b81c2a270eb489c88e6d822a76ec0cb7bf34d965768848567` |
| Tag Ollama base Qwen3.5 0.8B | Q8_0 | `de63045f29755d4721c09d54c9b45c2dadb644f4fd7d604d4cac90d96049971c` |
| Arquivo GGUF Granite 4.2 8B | Q6_K | `5ad3d67f6fe09a448031029bead7f6a088697ca2787c0c5640bf964c59df1a21` |

Digests de manifesto Ollama e valores SHA-256 de arquivos de pesos identificam objetos diferentes. Associe o identificador ao tipo de artefato na tabela.

## O que eu executaria com Hermes

Eu faria de Qwen3.5 35B a principal rota de contexto alto no sistema com duas RTX 5060 Ti. Seu resultado de retenção de 239.153 tokens pelo gateway, as aprovações separadas de ferramentas e visão e a liberação de solicitações verificada sustentam essa escolha mais que um modelo anunciado com uma grande janela de contexto. Eu manteria Qwen3.8 27B para respostas mais rápidas na comparação de 66K e Qwen3.6 quando usar uma placa for importante.

Nos sistemas RTX 2000E Ada, eu escolheria a rota Gemma 3 4B verificada do sistema C para a carga testada de resposta com entrada longa. Testaria a rota Qwen3.5 0.8B sem raciocínio para recuperação e extração delimitadas. Rotas maiores Gemma, Qwen e GPT-OSS servem para tarefas que aceitam a resposta inicial testada de quatro a cinco minutos. Eu excluiria a rota Gemma 3 malsucedida do sistema D.

Para as placas RTX 3060 Ti e RTX 3070 de 8 GB, começaria com Qwen3.5 2B ou 4B. Seus resultados textuais de 65K e as verificações de imagem 4B sustentam uma configuração inicial útil sem dedicar as duas placas de 16 GB a cada solicitação. A pressão de memória do Flash Next e o comportamento incompleto em 65K do DeepSeek Coder V2 tornam essas opções padrão mais fracas nos perfis testados.

Os testes sustentam essas escolhas de modelo e sistema para fluxos de trabalho específicos. Retenção de entrada, uma interação correta com ferramenta, reconhecimento de imagem e liberação limpa respondem a aspectos diferentes da viabilidade do Hermes. Uma configuração confiável precisa dos comportamentos usados pelo seu agente, com contexto suficiente para a resposta e o tráfego das ferramentas.

## Fontes e leitura relacionada

- [Configuração de provedores e requisitos de contexto do Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md)
- [Especificações NVIDIA GeForce RTX 3060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3060-3060ti/)
- [Especificações NVIDIA GeForce RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/)
- [Visão geral do Hermes Agent](/hermes-local-ai-broker-course/01-hermes-agent-overview/)
- [Escolher um backend de modelo local](/hermes-local-ai-broker-course/02-choose-a-backend/)

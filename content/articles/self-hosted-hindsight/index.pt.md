---
title: "Hindsight auto-hospedado: memória local de agentes e roteamento privado de modelos"
date: 2026-11-08
lastmod: 2026-11-12
toc: true
draft: false
description: "Estudo de caso do Hindsight auto-hospedado, das rotas locais Qwen observadas e do uso de GPU por solicitação sem assinatura de inferência hospedada nos caminhos inspecionados."
genre: ["IA local", "IA auto-hospedada", "Agentes de IA", "Infraestrutura de IA", "Privacidade"]
tags: ["Hindsight", "Hindsight auto-hospedado", "memória de agentes", "IA local", "LLM local", "Qwen3.5", "LiteLLM", "VPN privada", "gateway de modelos", "embeddings", "reranking", "agendamento de GPU", "inferência privada", "Docker", "bancos de memória", "páginas de conhecimento", "roteamento local de modelos"]
cover: "/img/cover/self-hosted-hindsight-local-model-routing.webp"
coverAlt: "Um serviço privado de memória abstrato encaminha tarefas para servidores locais de modelos em CPU e GPU"
coverCaption: "O armazenamento e a recuperação da memória, além das rotas de modelos inspecionadas, usam hardware próprio"
---

**Nosso serviço de memória Hindsight funciona em hardware sob nosso controle.** O mecanismo de memória, o banco de dados, o modelo de embeddings e o reranker funcionam em uma implantação auto-hospedada. O Hindsight envia solicitações de geração a um gateway privado. O backend Qwen compartilhado inspecionado e a rota testada de atualização de páginas usam servidores locais de modelos sem assinatura de inferência hospedada.

Esta é a descrição de uma implantação funcional. **Auto-hospedado não significa offline.** A VPN usa um serviço externo de coordenação, e as imagens de software e os pesos dos modelos precisam ser baixados. A afirmação aqui diz respeito ao processamento de memória e à inferência dos modelos, não a todas as conexões de rede feitas pelos nossos dispositivos ou por outras ferramentas de agentes.

<!--more-->

## Principais conclusões

- **O Hindsight gerencia o fluxo de trabalho da memória.** Um contêiner Docker fornece a API, os workers e o plano de controle, com os dados dos bancos em um volume persistente.
- **Modelos pequenos de recuperação permanecem locais.** Os embeddings e o reranking funcionam na CPU dentro do processo do Hindsight.
- **O Qwen gera texto.** Retain, Reflect e consolidação solicitam o alias privado Qwen3.5-4B, com o raciocínio desativado e a saída limitada. O backend inspecionado atende localmente.
- **Atualizações longas de páginas recebem uma GPU.** Um alias de modelo separado aluga uma placa para uma solicitação em segundo plano e a libera depois.
- **O gateway oculta a localização física.** O Hindsight seleciona um alias de modelo. Serviços privados de roteamento selecionam um endpoint de atendimento.

## Defina o limite antes de escolher modelos

**O Hindsight é o mecanismo de memória, não o servidor de modelos.** A imagem Docker completa inclui modelos locais de embeddings e reranking, mas a geração por modelo de linguagem precisa de um endpoint. O [guia de instalação do Hindsight](https://hindsight.vectorize.io/developer/installation) documenta essa divisão e apresenta servidores locais llama.cpp, Ollama e vLLM como alternativas a provedores hospedados.

**A API de memória permanece na rede privada.** O plano de controle web fica em uma interface local. Um volume persistente armazena o banco de dados incorporado, então recriar um contêiner não descarta os bancos. A autenticação protege a API, e bancos separados organizam o contexto dos projetos.

**O gateway de geração fornece nomes de modelos estáveis.** O Hindsight envia solicitações compatíveis com OpenAI pelo gateway privado através de uma VPN. O gateway encaminha as solicitações para endpoints locais de atendimento. A rota Qwen inspecionada chega a uma implantação LiteLLM mapeada para um servidor local de CPU. A [documentação do roteador LiteLLM](https://docs.litellm.ai/docs/routing) descreve esse padrão de alias de modelo. Um roteador equivalente compatível com OpenAI cumpre a mesma função.

{{< figure src="hindsight-private-request-path.webp" alt="Diagrama com agentes, um serviço Hindsight privado, modelos locais de recuperação, um gateway privado e servidores Qwen locais" caption="O diagrama omite nomes de host, endereços, chaves de acesso e identificadores físicos de hosts" >}}

[Abra o diagrama completo do caminho da solicitação](hindsight-private-request-path.webp).

**Uma API interna ainda existe.** O Hindsight chama um gateway privado usando o formato compatível com OpenAI. As rotas de modelos inspecionadas realizam a inferência localmente. Não auditamos todas as regras de contingência do gateway. Revise a política do gateway antes de considerar o processamento local uma garantia para todas as solicitações.

## Atribua cada tarefa de memória à computação adequada

As operações do Hindsight fazem trabalhos diferentes. **Retain** extrai fatos de novos materiais. **Recall** encontra memórias relevantes. **Reflect** pesquisa e escreve uma resposta sintetizada. **Consolidation** combina fatos relacionados. A **knowledge-page refresh** em segundo plano reconstrói um resumo atualizado do banco.

| Operação | Local do modelo | Motivo |
| --- | --- | --- |
| **Retain** | Qwen3.5-4B pelo gateway privado | Extração estruturada local com um orçamento de saída limitado |
| **Recall** | Embeddings e reranking locais na CPU | A pesquisa não precisa chamar a API de geração |
| **Reflect** | Qwen3.5-4B pelo gateway privado | A síntese precisa gerar texto após recuperar memórias |
| **Consolidation** | Qwen3.5-4B pelo gateway privado | Lotes pequenos limitam respostas estruturadas longas |
| **Knowledge-page refresh** | Rota Qwen local dedicada em GPU | A síntese longa em segundo plano excedeu o limite de tempo da rota CPU |

*Mantenha tarefas pequenas de recuperação na CPU e reserve a inferência em GPU para tarefas longas com duração medida.*

O contêiner Hindsight carrega **BAAI/bge-small-en-v1.5** para embeddings e **hindsight-ai/hs-rerank-1** para reranking. Os registros de inicialização confirmam que ambos funcionam localmente na CPU. A [referência de modelos do Hindsight](https://hindsight.vectorize.io/developer/models) documenta opções locais e o caminho opcional de modelo de decisão.

Mantivemos o modelo de embeddings existente porque mudar o espaço de embeddings exige reconstruir os vetores armazenados. O reranker já funciona localmente, então um serviço hospedado de reranking criaria um novo limite para os dados sem resolver o timeout de geração observado. Um teste local com **hs-decide-1-flash** produziu uma resposta Reflect correta, mas o resultado terminou perto do limite de tempo do teste. Os dados sintéticos de consolidação não exercitaram o caminho de decisão. Por isso, o modelo de decisão não faz parte do roteamento de produção.

## Reserve uma GPU para tarefas lentas em segundo plano

**O nome comum do modelo é diferente do nome usado para atualização.** Retain, Reflect e consolidação usam o alias Qwen compartilhado. A atualização de páginas em segundo plano usa um alias de GPU específico do nó, com uma chamada simultânea de modelo de linguagem. Isso limita uma tarefa longa de manutenção a uma GPU por vez.

**Uma reserva por solicitação limita o uso da GPU.** O pool de GPU inicia um worker de modelo quando chega uma solicitação. O controlador reserva uma placa, atende à solicitação, encerra o worker e libera a reserva. O diagrama omite o inventário físico de hosts.

{{< figure src="hindsight-gpu-lease-cycle.webp" alt="Diagrama de uma GPU reservada para atualizar uma página em segundo plano e liberada após a conclusão da solicitação" caption="Uma concessão por solicitação reserva uma GPU para atualizar uma página" >}}

[Abra o diagrama completo do ciclo de concessão de GPU](hindsight-gpu-lease-cycle.webp).

Essa divisão surgiu de uma falha medida. **Uma atualização de página priorizando CPU atingiu o limite de uma hora.** Depois de encaminhar as atualizações em segundo plano para o pool local de GPU, cinco páginas que haviam falhado antes terminaram em cerca de dois a seis minutos em uma execução de recuperação. Esses números descrevem aquelas páginas e configurações. Não são um benchmark geral de throughput do Qwen.

## Corrija os padrões e os timeouts

**Os limites de saída anteriores do Hindsight não funcionavam com nosso roteador local.** O roteador aceita no máximo 8.192 tokens de saída e aplica um limite de 256 tokens quando uma solicitação não informa um. Um limite anterior de 64.000 tokens para Retain gerou HTTP 400. Lotes de consolidação com oito fatos atingiram o limite de comprimento de saída, e Reflect precisou de um limite explícito para evitar o fallback de 256 tokens do roteador.

**Definimos limites explícitos para cada tarefa.** O raciocínio do Qwen fica desativado nessas operações de memória. Agora o Hindsight permite quatro chamadas LLM simultâneas no total, incluindo no máximo uma chamada de atualização de página em segundo plano. O timeout global do LLM é de 1.800 segundos, com uma nova tentativa do modelo.

| Carga de trabalho | Limite de saída ou lote | Limites de chamadas e operações |
| --- | --- | --- |
| **Retain** | 8.192 tokens de saída | Timeout global de 1.800 segundos por chamada |
| **Reflect** | 4.096 tokens de saída | 900 segundos por chamada, 3.600 segundos para a operação |
| **Consolidation** | 4.096 tokens de saída, quatro fatos por chamada | 900 segundos por chamada, 14.400 segundos para a operação |
| **Page refresh** | Uma chamada simultânea de modelo | 900 segundos por chamada, rota GPU dedicada |

*Esses valores descrevem nossa implantação e nosso roteador local em novembro de 2026.*

**O timeout de uma chamada e o limite total de uma operação restringem etapas diferentes.** Algumas chamadas válidas do Qwen excederam o timeout anterior de 300 segundos. Os limites maiores da operação permitem trabalho com várias chamadas, enquanto o limite de 900 segundos por chamada ainda restringe cada tentativa.

Na execução de recuperação, várias tarefas Retain terminaram com **1.042 a 2.076 tokens de saída**. Duas execuções de consolidação concluíram **41 de 41** e **30 de 30** itens. Um timeout posterior de atualização de página levou à rota GPU separada descrita acima. Esses resultados de recuperação não comprovam confiabilidade de longo prazo.

## Quais são os custos dessa arquitetura?

**Não pagar por modelos hospedados não significa custo zero.** A implantação usa hardware próprio, eletricidade, armazenamento, tempo de manutenção e tempo de GPU durante as atualizações de página. Cada escolha de posicionamento troca capacidade por latência ou simplicidade operacional.

| Escolha | Benefício | Custo da escolha |
| --- | --- | --- |
| **Geração priorizando CPU** | Preserva a disponibilidade da GPU | Uma atualização de página testada atingiu o limite de uma hora |
| **Atualização de página em GPU** | Cinco páginas terminaram em cerca de dois a seis minutos em uma execução | Usa capacidade de GPU e depende da rota dedicada |
| **Banco de dados incorporado** | Mantém a implantação compacta | Reduz o domínio de falha e exige testar backups |

*Use uma rota de atualização em GPU depois que a latência medida na CPU exceder sua janela de manutenção.*

O [guia de instalação do Hindsight](https://hindsight.vectorize.io/developer/installation) recomenda PostgreSQL separado para implantações de produção maiores. **Nosso banco incorporado precisa de um processo testado de backup e recuperação** à medida que o banco de memória cresce.

**A inferência privada depende do caminho da solicitação.** Verifique o provedor selecionado pelo Hindsight, o mapeamento de modelos do gateway, as regras de contingência, o processo local do modelo, a retenção de logs e o tráfego de saída da rede. Os IDs de rastreamento do Hindsight ajudam a correlacionar solicitações, e o Docker rotaciona os logs do contêiner. Nenhuma dessas medidas prova que uma solicitação subsequente permaneceu local. Uma auditoria do gateway fornece a evidência ponta a ponta que falta.

## Recomendação

**Comece com modelos locais de recuperação e limites explícitos de geração.** Execute o Hindsight e seus modelos de embeddings e reranking em hardware próprio. Encaminhe a geração por um gateway privado compatível com OpenAI através de uma VPN. Meça cada operação antes de atribuir capacidade de CPU ou GPU e reserve a rota GPU para tarefas em segundo plano cuja latência na CPU exceda sua janela de manutenção.

*Revise cada regra de contingência do gateway e teste a recuperação dos bancos antes de considerar a implantação privada e resiliente.* O [guia sobre limites de privacidade de IA local](/articles/local-ai-privacy-boundary/) oferece uma lista inicial de verificação.

## Conclusão

**Esta implantação mantém a memória do Hindsight e os caminhos de inferência inspecionados em hardware próprio, sem assinatura de inferência hospedada.** A recuperação em CPU, as chamadas Qwen limitadas e a rota de atualização em GPU com uma única chamada atendem a diferentes cargas de trabalho. As execuções de recuperação concluíram tarefas Retain, consolidação e atualização de páginas com essas configurações. Uma auditoria completa das regras de contingência do gateway, um teste de backup e uma observação de confiabilidade mais longa são as próximas verificações.

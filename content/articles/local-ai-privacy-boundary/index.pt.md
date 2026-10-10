---
title: "Privacidade da IA local: o que permanece no seu computador e o que não permanece"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Rastreie prompts, arquivos de modelos, ferramentas, logs, exposição de rede e custos de energia antes de escolher inferência local ou um serviço de IA hospedado."
genre: ["IA local", "Privacidade", "Self-Hosted AI", "Cibersegurança", "Economia da IA"]
tags: ["privacidade de IA local", "inferência local", "cloud AI", "privacidade de dados de IA", "self-hosted AI", "privacidade de LLM", "custo de propriedade da GPU", "custo de eletricidade da IA", "RTX 5070", "Claude Haiku 5.5", "privacidade do Ollama", "llama.cpp", "segurança de IA", "offline AI", "modelos de linguagem locais", "privacidade de prompts", "modelo de ameaças de IA", "break-even da GPU", "limite de dados da IA", "IA privada"]
cover: "/img/cover/local-ai-vs-chatgpt-comparison-illustration.webp"
coverAlt: "Uma estação de trabalho de IA local conectada a um serviço de nuvem por caminhos de dados visíveis"
coverCaption: "Ilustração dos caminhos de dados de IA locais e hospedados"
---

**A IA local oferece um limite de dados menor.** Um prompt processado por um runtime local permanece no seu dispositivo quando o modelo, as ferramentas, os logs e o caminho de rede permanecem locais. Uma GPU local não transforma um computador em um sistema isolado.

Runtimes de modelos, plugins de ferramentas, extensões do navegador, acesso remoto, APIs expostas e downloads de modelos ainda definem seu risco. O custo também importa. A eletricidade pode custar menos que um token hospedado, enquanto a propriedade do hardware empurra o ponto de equilíbrio total para o futuro.

Este guia mapeia primeiro o limite de privacidade. Depois verifica o custo usando preços atuais de fornecedores, uma hipótese explícita de energia e os números relatados no vídeo fornecido.

<!--more-->

Esta comparação de custos local e hospedado fornece contexto para as fórmulas abaixo. Não copie os números de throughput sem testar o mesmo arquivo de modelo e runtime no seu hardware.

{{< youtube id="DmkuFpoMYmc" enable="true" title="Is local AI worth it? We did the math vs Claude Haiku 5.5" description="A local-versus-hosted AI cost comparison." >}}

O vídeo relata um runtime de 2 minutos e 31 segundos. Verifiquei seu título e runtime pela página de exibição. Não repeti o teste de hardware, então suas velocidades continuam sendo medições relatadas pela fonte.

## A resposta curta

- **Escolha inferência local para um caminho de dados controlado.** Mantenha o servidor do modelo no dispositivo, vincule-o ao loopback e restrinja o acesso às ferramentas.
- **Escolha inferência hospedada para trabalho ocasional.** Evite gastar com hardware quando sua carga é pequena ou seu modelo preferido não cabe no sistema.
- **Trate o custo local como dois números.** Separe a eletricidade por hora ativa da propriedade do hardware.
- **Trate a privacidade como uma propriedade do sistema.** Um modelo privado perde o benefício quando um plugin envia arquivos ou uma API local escuta em todas as interfaces de rede.

A inferência local ajuda quando texto sensível precisa permanecer em uma estação de trabalho ou rede isolada. Também ajuda quando você precisa de operação offline, uma versão fixa do modelo ou acesso previsível sem cota de fornecedor.

Esses benefícios não provam respostas melhores. Um modelo hospedado pode se encaixar melhor em uma tarefa, terminar mais rápido ou exigir menos manutenção. Meça a carga antes de comprar hardware.

## Rastreie o caminho dos dados

Mapeie cada componente envolvido em uma solicitação. O nome do modelo sozinho não mostra por onde os dados passam.

| Componente | Pergunta de privacidade | Evidência a coletar |
|---|---|---|
| **Servidor de modelo local** | O prompt permanece no host? | Configuração do processo, endereço de escuta e tráfego de saída |
| **Modelo na nuvem** | Quais textos, arquivos e resultados de ferramentas deixam o host? | Endpoint da API, termos do fornecedor, logs de solicitações e configurações da conta |
| **Modo de nuvem em um app local** | O modelo selecionado roda no dispositivo? | Identificador do modelo, rótulo do fornecedor e conexão de rede |
| **Plugin de ferramenta** | O modelo recebe arquivos, saída do shell ou conteúdo do navegador? | Lista de ferramentas, permissões e dados capturados das solicitações |
| **Download do modelo** | Que código e pesos entram no host? | Repositório de origem, licença, checksum da versão e caminho de download |
| **Logs locais** | Onde prompts e resultados de ferramentas persistem? | Logs do runtime, histórico do shell, relatórios de falha e escopo dos backups |

**Um modelo local remove um fornecedor do caminho do prompt.** Ele não remove a necessidade de revisar o restante do caminho.

## Local não significa privado por padrão

[Ollama's privacy policy](https://ollama.com/privacy) declara que o Ollama não vê prompts ou dados quando um modelo roda localmente. A política também separa a operação local dos modelos hospedados na nuvem. Um modelo de nuvem ainda cria um limite de serviço, mesmo quando o mesmo aplicativo inicia os dois modos.

[llama.cpp's server documentation](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) mostra um servidor local escutando em `127.0.0.1:8080` por padrão. Seus exemplos Docker também mostram `--host 0.0.0.0`, que expõe o serviço em todas as interfaces. Um endereço de bind mais amplo muda o limite de acesso.

Confira o endereço de escuta antes de enviar texto sensível:

```bash
lsof -nP -iTCP -sTCP:LISTEN | rg 'ollama|llama|8080|11434'
```

`127.0.0.1` ou `localhost` limita o acesso ao mesmo host no caso normal. Um endereço LAN ou `0.0.0.0` exige uma regra de firewall e um plano de autenticação. Não exponha um endpoint de modelo à rede antes de testar os dois casos.

Confira também o nome do modelo selecionado. A documentação de nuvem do Ollama descreve modelos de nuvem como um caminho de serviço separado. Uma interface local não prova execução local.

O [FAQ do Ollama](https://docs.ollama.com/faq) documenta um modo somente local. Defina `disable_ollama_cloud` em `~/.ollama/server.json`, ou defina `OLLAMA_NO_CLOUD=1` antes de reiniciar o serviço. Isso remove modelos de nuvem do Ollama e a busca na web do runtime selecionado. Não restringe outros aplicativos, ferramentas do navegador, plugins ou acesso de rede no host.

```json
{
  "disable_ollama_cloud": true
}
```

Verifique a configuração depois do reinício. Um runtime somente local reduz um caminho. Ele não estabelece um host privado.

## Calcule o custo hospedado

Os preços dos tokens separam entrada e saída. [Anthropic lists Claude Haiku 5.5 at $0.10 per million input tokens and $0.50 per million output tokens for prompts up to 100,000 tokens](https://www.anthropic.com/claude/haiku). Prompts acima de 100.000 tokens usam as tarifas maiores listadas.

[OpenAI's token guide](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens) explica por que uma contagem de palavras não equivale a uma contagem de tokens. Ela também separa tokens de entrada, saída, entrada em cache e raciocínio. Use os campos de uso do fornecedor, não uma estimativa por palavras.

Para uma comparação simples, use um milhão de tokens gerados e um milhão de tokens de entrada como cargas separadas. Um agente de programação costuma enviar contexto repetido e produzir uma resposta menor, então um único número combinado esconde a mistura de custos.

## Calcule a energia local

[NVIDIA's RTX 5070 launch announcement](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/) listou preço inicial de $549. [NVIDIA's RTX 5070 family page](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/) lista 12 GB de memória e 250 W de potência gráfica total para o design de referência Founders Edition. A página de produto da NVIDIA ainda lista $549 e mostrou a placa sem estoque durante esta revisão.

A potência da GPU não é a potência do sistema inteiro. Use um medidor de tomada no seu PC. O exemplo abaixo assume **consumo de 400 W no sistema inteiro**, incluindo GPU, processador, memória, armazenamento, ventoinhas e perdas da fonte. Isso é uma hipótese para a aritmética, não um resultado medido.

[The U.S. Energy Information Administration forecast](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os) usou 18,2 centavos por quilowatt-hora como preço residencial médio de eletricidade para 2026. Sua tarifa muda o resultado.

Use esta fórmula para a saída gerada:

```text
local cost per 1M output tokens =
(whole_system_watts / 1,000)
× (1,000,000 / output_tokens_per_second / 3,600)
× electricity_price_per_kWh
```

Com 400 W e $0.182 por quilowatt-hora, o sistema custa $0.0728 por hora ativa.

| Velocidade de saída | Tempo para 1M tokens | Custo de energia para 1M tokens |
|---:|---:|---:|
| **20 tokens per second** | 13 horas 53 minutos | **$1.01** |
| **50 tokens per second** | 5 horas 33 minutos | **$0.40** |
| **94 tokens per second** | 2 horas 57 minutos | **$0.22** |

A 50 tokens de saída por segundo, a energia local custa menos que o preço de saída de $0.50 do Haiku 5.5. A 20 tokens por segundo, a energia local custa mais. O limite de velocidade de saída nestas hipóteses é cerca de 40 tokens por segundo.

O cálculo de entrada usa a mesma fórmula. A 2.650 tokens de entrada por segundo, um milhão de tokens de entrada leva cerca de 6 minutos e 17 segundos e custa cerca de $0.008 em energia. A 1.000 tokens por segundo, o mesmo trabalho custa cerca de $0.020.

A transcrição fornecida relata 94 tokens de saída por segundo e 2.650 tokens de entrada por segundo para seu exemplo com RTX 5070. A aritmética acima concorda com esses números sob a hipótese de 400 W. A transcrição não fornece registro independente de laboratório, hash do arquivo do modelo, build do runtime, prompt ou leitura do medidor. Trate essas velocidades como resultado de referência, não como garantia de compra.

## O hardware muda o break-even

Economia de energia não paga o hardware sozinha. Compare a compra completa com a diferença entre o custo hospedado da saída e o custo variável local.

A 50 tokens de saída por segundo:

```text
$0.50 hosted output price - $0.40 local power = $0.10 saved per 1M tokens
$549 GPU price / $0.10 = about 5.5 billion output tokens
```

A 94 tokens por segundo, a economia arredondada sobe para cerca de $0.28 por milhão de tokens. Recuperar uma GPU de $549 exige então cerca de 2 bilhões de tokens de saída. Ambos os números excluem memória do sistema, armazenamento, placa-mãe, fonte, refrigeração, manutenção e valor de revenda.

O preço de lançamento não é uma cotação universal. A página atual da NVIDIA mostrou o preço oficial sem estoque. Uma oferta de vendedor a $819 precisa de verificação separada antes de entrar no modelo de break-even. Use sua nota fiscal e a potência medida na tomada.

**Hardware existente muda a decisão.** Se sua estação já tem memória suficiente e uma GPU adequada, o custo do hardware está amortizado para a próxima tarefa. Compare energia, tempo, qualidade, privacidade e manutenção. Se precisa comprar um sistema completo, compare o sistema inteiro com o uso hospedado.

Para detalhes de adequação dos modelos, leia o [local AI model and GPU context guide](/articles/local-ai-model-gpu-context-guide/) e o [16GB VRAM sizing guide](/articles/is-16gb-vram-enough-local-llm/). Para uma configuração de agente de programação local relatada, leia o [Strata and OpenCode guide](/articles/strata-opencode-local-coding-agent-16gb/).

## O que a privacidade local oferece

- **Caminho de dados menor:** o prompt não precisa chegar a um provedor de modelos quando a inferência permanece local.
- **Operação offline:** um modelo baixado e um runtime local não precisam de conexão ativa com um provedor para gerar texto.
- **Controle de versão:** você escolhe o arquivo do modelo e a versão do runtime em vez de receber uma mudança automática do fornecedor.
- **Controle de uso:** a inferência local evita um medidor de nuvem por solicitação depois de contabilizar propriedade e energia.
- **Controle da política de rede:** seu firewall e os controles do host definem quem alcança o endpoint do modelo.

Esses ganhos importam mais para código-fonte, registros de clientes, projetos não lançados, notas privadas e trabalho em ambiente desconectado. A inferência local ainda precisa de criptografia de disco, atualizações do host, separação de contas e ferramentas restritas.

## O que a privacidade local não oferece

- **Garantia de qualidade:** modelos menores ou quantizados precisam de testes contra seus critérios reais de aceitação.
- **Garantia da cadeia de suprimentos:** arquivos de modelos, runtimes, plugins e imagens de contêiner precisam de fontes confiáveis e verificações de integridade.
- **Host limpo:** malware, extensões do navegador, backups, relatórios de falhas e administração remota ainda veem dados do host.
- **Endpoint de rede seguro:** um servidor vinculado a todas as interfaces cria um novo serviço para defender.
- **Sistema gratuito:** eletricidade, armazenamento, refrigeração, desgaste do hardware e manutenção continuam tendo custo.

O [Strata local coding-agent guide](/articles/strata-opencode-local-coding-agent-16gb/) mostra por que memória do sistema, contexto, acesso às ferramentas e configurações do runtime entram na avaliação. A memória da GPU sozinha não define o limite de privacidade ou desempenho.

## Escolha o limite certo

| Situação | Primeira escolha melhor | Motivo |
|---|---|---|
| **Documentos sensíveis e PC compatível existente** | Local inference | Mantenha prompts no host controlado e evite gasto com hardware novo |
| **Redação genérica ocasional** | Hosted API ou chat service | Pague pela carga pequena e evite manutenção |
| **Modelo de fronteira ou ferramenta especializada na nuvem** | Hosted service | O modelo ou ferramenta exigido não está disponível no host local |
| **Grande volume recorrente com modelo local verificado** | Local ou híbrido | Compare energia, qualidade, tempo de suporte e preços do fornecedor |
| **Cargas mistas** | Hybrid routing | Mantenha tarefas sensíveis locais e envie tarefas genéricas aprovadas a um modelo hospedado |

**O roteamento híbrido precisa de uma regra explícita de classificação.** Marque os dados como somente locais, aprovados para processamento hospedado ou proibidos até revisão. Não confie no nome do modelo ou no ícone do aplicativo para aplicar a regra.

## Verifique antes de confiar

1. **Nomeie o caminho do modelo.** Registre identificador do modelo, runtime, versão e fonte do download.
2. **Confira o endereço de bind.** Confirme que o servidor escuta no loopback, salvo necessidade documentada de um caminho mais amplo.
3. **Liste cada ferramenta.** Revise acesso a arquivos, shell, navegador, rede e plugins.
4. **Inspecione a persistência.** Encontre logs de prompts, saída de ferramentas, relatórios de falhas, backups e diretórios compartilhados de modelos.
5. **Teste o comportamento de rede.** Observe conexões durante um teste sensível com um prompt representativo.
6. **Meça o sistema.** Registre potência na tomada, velocidade de saída, velocidade de entrada, tamanho do contexto e tentativas.
7. **Teste o trabalho aceito.** Compare tarefas concluídas e esforço de revisão, não somente tokens por segundo.

O [local AI versus ChatGPT guide](/articles/local-ai-vs-chatgpt-how-close-are-we/) cobre os compromissos de capacidade dos modelos. Use esta lista de privacidade junto com o teste de qualidade.

## Referências

- [Video, Is local AI worth it? We did the math vs Claude Haiku 5.5](https://www.youtube.com/watch?v=DmkuFpoMYmc)
- [NVIDIA Blackwell GeForce RTX 50 Series launch announcement](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/)
- [NVIDIA GeForce RTX 5070 family specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/)
- [NVIDIA GeForce RTX 5070 product page](https://marketplace.nvidia.com/en-us/consumer/graphics-cards/geforce-rtx-5070/)
- [U.S. Energy Information Administration, October 2026 Short-Term Energy Outlook](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os)
- [Anthropic Claude Haiku 5.5](https://www.anthropic.com/claude/haiku)
- [Anthropic Claude Platform pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI, Understanding and counting tokens](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens)
- [Ollama privacy policy](https://ollama.com/privacy)
- [llama.cpp server documentation](https://github.com/ggml-org/llama.cpp/tree/master/tools/server)

---
title: "Mineração de Pearl (PRL) em 2026: configuração, rentabilidade e utilidade da rede"
date: 2026-09-22
lastmod: 2026-11-20
toc: true
draft: false
description: "Configure a mineração de Pearl PRL com SRBMiner, entenda a prova de trabalho útil, estime margens e avalie a utilidade prática da rede."
genre: ["Criptomoedas", "Mineração com GPU", "Computação de IA", "DePIN", "Blockchain", "Linux", "Laboratório doméstico", "Equipamentos"]
tags: ["mineração de Pearl", "mineração de PRL", "Pearl PRL", "prova de trabalho útil", "PoUW", "NoisyGEMM", "SRBMiner Pearlhash", "pool de mineração Pearl", "LuckyPool Pearl", "mineração com GPU 2026", "cripto e computação de IA", "Pearl Research Labs", "mineração combinada Nockchain", "mineração combinada Nock", "mineração de RTX 3070", "configuração do SRBMiner", "rig de mineração Linux", "serviço de mineração systemd", "mineração por multiplicação de matrizes", "minerador vLLM", "carteira Pearl", "endereço prl1", "rentabilidade da mineração", "mineração de computação de IA", "guia de mineração de criptomoedas", "mineração NVIDIA", "ajustes de overclock para mineração"]
cover: "/img/cover/pearl-blockchain-gpu-mining-matrix-multiplication-2026.webp"
coverAlt: "Ilustração de um rig moderno de mineração com GPU executando multiplicação de matrizes para a blockchain Pearl, com fluxos de dados dinâmicos e cores vibrantes sobre um fundo escuro."
coverCaption: ""
ref: ["/other/efficient-spacemesh-mining-multiple-gpus-guide", "/articles/local-ai-2026-build-your-rig-now"]
---

**Pearl é a primeira rede de prova de trabalho útil a alcançar escala real de produção. Ela remunera mineradores pela multiplicação de matrizes em vez da geração de hashes.** A rede principal foi lançada em **27 de abril de 2026** e, em poucas semanas, provocou uma corrida pela mineração com GPU baseada na promessa de proteger uma blockchain e produzir computação de IA na mesma operação.

*A alegação é tecnicamente real, mas ainda não foi comprovada em termos econômicos. A diferença entre essas duas coisas é o ponto central.*

Este guia explica como minerar PRL, quais cálculos o minerador executa, por que as margens caíram tão depressa depois do lançamento e se a rede produz algo de valor.

**Ao terminar:** você terá uma carteira, um minerador verificado, o consumo de energia medido e um cálculo de rentabilidade baseado na sua tarifa elétrica. Trate as estimativas dos pools e a receita do lançamento como observações de uma data específica, não como garantia de compra.

## Resposta curta

**Pearl é uma conquista técnica real que enfrenta o problema econômico da mineração comum a toda moeda nova.**

| Pergunta | Resposta curta |
|---|---|
| **O que é?** | Uma blockchain L1 derivada do Bitcoin e protegida por prova de trabalho útil. Os mineradores executam multiplicação ruidosa de matrizes em vez de SHA-256 |
| **Como minerar?** | SRBMiner-MULTI com `--algorithm pearlhash` conectado a um pool, ou o minerador vLLM da Pearl conectado ao seu próprio nó |
| **Por que foi rentável?** | As emissões iniciais superaram a dificuldade por algumas semanas, até a dificuldade subir |
| **Ainda é rentável?** | Depende do hardware, e a janela está diminuindo. Veja a seção de margens abaixo |
| **A rede é útil?** | **O mecanismo é; o mercado ainda não.** Veja os detalhes na avaliação final |

**O ponto mais importante antes de montar um rig:** as notas da versão 3.6.8 do próprio desenvolvedor do minerador dizem que uma atualização da Pearl tornará GPUs de consumo "praticamente inúteis" para mineração. Essa avaliação vem de quem escreve o minerador, não de um crítico externo.

## O que é a Pearl

Pearl é uma blockchain L1 criada pela **Pearl Research Labs** e descrita no repositório oficial assim:

> "Pearl é uma blockchain L1 baseada no protocolo de prova de trabalho útil, em que a mineração ocorre como subproduto da multiplicação arbitrária de matrizes."

O repositório inclui um nó completo, um daemon de carteira, um cliente leve SPV, um sistema de provas de conhecimento zero e um minerador para GPU. O projeto usa a **licença ISC**, permissiva e sem copyleft, e sua infraestrutura deriva de projetos Bitcoin testados: **btcd** para o nó, **btcwallet** para a carteira e **neutrino** para o cliente leve.

**O projeto se inspira deliberadamente no Bitcoin**, inclusive no limite de **2,1 bilhões de PRL**, exatamente 100 vezes os 21 milhões do Bitcoin, com recompensa por bloco decrescente e blocos de cerca de dois minutos.

*A infraestrutura é conservadora por escolha. A novidade está inteiramente na função de trabalho.*

### Entenda a prova de trabalho útil

A prova de trabalho útil é uma ideia antiga com um histórico ruim. A proposta sempre foi substituir o hashing deliberadamente dispendioso do Bitcoin por cálculos que também produzam algo valioso. Quase todas as tentativas anteriores falharam pelo mesmo motivo: o trabalho "útil" não era útil ou não podia ser verificado a baixo custo para proteger uma rede.

A Pearl implementa o conceito com uma rotina chamada **NoisyGEMM**. Na prática, um minerador executa multiplicações ruidosas de matrizes na GPU, transforma o resultado em um compromisso criptográfico e inclui uma **prova de conhecimento zero** para que a rede o verifique com baixo custo.

O esquema se baseia em um artigo de criptografia de 2025, **"Provas de trabalho útil por multiplicação arbitrária de matrizes"**, de Komargodski, Schen e Weinstein. O artigo afirma que a sobrecarga é aproximadamente **1 + o(1) em relação a uma multiplicação ingênua de matrizes**. Essa é a alegação central do projeto. Se proteger a rede quase não acrescenta custo ao cálculo original, produzir esse cálculo fica praticamente gratuito.

**A proposta oferece dois resultados pelo preço de um. Uma operação na GPU, dois resultados.**

Essa alegação diferencia Pearl de uma década de conceitos PoUW que fracassaram. A maioria não tinha um limite semelhante.

{{< figure src="pearl-noisygemm-proof-of-useful-work-flow.webp" alt="Diagrama de como a prova de trabalho útil da Pearl transforma uma multiplicação de matrizes na GPU em um compromisso de hash e uma prova de conhecimento zero que a rede verifica com baixo custo" >}}

### O que o minerador realmente calcula

Há dois caminhos, e eles não são equivalentes.

**O caminho oficial** está no repositório da Pearl. Ele tem dois componentes: `pearl-gateway`, que se conecta ao seu nó, e `vllm-miner`, que executa o trabalho na GPU por meio do vLLM. O gateway se comunica por JSON-RPC com um nó `pearld` local e oferece uma interface de mineração por socket Unix ou pela porta TCP 8337.

**O caminho por pool** é o que a maioria usa. O SRBMiner-MULTI implementa Pearl com o algoritmo `pearlhash`, que você aponta para um pool.

Essa diferença importa para avaliar a utilidade. **O minerador oficial carrega um modelo de linguagem real.** O exemplo da documentação da Pearl executa `pearl-ai/Llama-3.3-70B-Instruct-pearl` em um contêiner Docker com acesso à GPU. É um modelo de 70 bilhões de parâmetros que executa inferência enquanto a mesma operação protege a rede.

*Executar inferência é uma capacidade real. Executar inferência que ninguém compra é um centro de custos acoplado a uma blockchain. Mantenha essas ideias separadas.*

## Por que foi rentável e por que isso mudou

A rentabilidade inicial da Pearl não era um mistério nem tinha relação com IA. Era a curva de emissão típica de uma moeda nova.

| Quando | O que aconteceu |
|---|---|
| **27 de abril de 2026** | Lançamento da rede principal |
| **Fim de maio de 2026** | Começa uma corrida de mineração com GPU, cinco semanas após o início da rede |
| **Junho de 2026** | A receita diária estimada da RTX 5090 **caiu aproximadamente pela metade** com o aumento da dificuldade |
| **Meados ao fim de 2026** | A eficiência do software de mineração melhora bastante e compensa parte da queda |

O mecanismo de compressão é direto:

1. **As emissões iniciais são altas e a dificuldade é baixa.** Os primeiros mineradores recebem recompensas maiores por unidade de hashrate.
2. **As recompensas atraem hashrate.** Mais GPUs passam a minerar na rede.
3. **A dificuldade aumenta para acompanhar.** A recompensa por GPU cai.

Pearl acrescenta outra pressão de queda porque a recompensa por bloco diminui por projeto. **A receita tem dois motivos para cair, enquanto a dificuldade tem um motivo para subir.**

### A força contrária: eficiência do software

As margens não caíram por igual, porque os mineradores ficaram mais rápidos. O changelog do pearlhash no SRBMiner registra essa evolução:

| Versão | Mudança no Pearlhash |
|---|---|
| **3.6.1** | Adicionou suporte à B300. A B300 SXM6 em `--gpu-cclock 1600` registrou cerca de **706 TH/s a 920 W** |
| **3.6.2** | Melhorias para H100, H200 e série 4000 |
| **3.6.8** | Aumento de hashrate, sobretudo na série 3000 |
| **3.6.9** | **Grandes ganhos de eficiência.** O mesmo hashrate ou um valor maior com muito menos energia na maioria das arquiteturas |

**Para quem minera em casa, a eletricidade é o principal custo operacional.** Uma versão que mantém o hashrate e reduz o consumo melhora a margem diretamente, sem alterar o preço do token nem a dificuldade da rede. Por isso, o mesmo rig que parecia pouco rentável em junho pode fazer sentido em setembro.

*Ganhos de eficiência ajudam, mas são temporários, porque também permitem que todos os outros mineradores aumentem a dificuldade.*

## O soft fork da penalidade de classificação

Na noite de **6 de agosto de 2026**, um soft fork foi ativado na Pearl por volta de **02:00 UTC, bloco 96251**. Muitos mineradores só souberam na manhã seguinte, quando o hashrate caiu.

O protocolo da Pearl tem um parâmetro de **rank de ruído**. Um rank mais alto facilitava ganhar um prêmio com a mesma quantidade de trabalho. **Alguns mineradores usavam ranks altos de propósito e obtinham hashrate efetivo e recompensas desproporcionais.** A equipe investigou o que chamou de otimizações anormais de mineração e respondeu com um mecanismo de penalidade.

| Mudança de regra | Efeito |
|---|---|
| **Rank mínimo permitido** | 128 |
| **Limite do prêmio** | Agora é escalado pela fórmula `128 / rank` |
| **Vantagem de ranks altos** | Eliminada por completo |

**Impacto nos mineradores:**

- Minerar acima do rank 128 custou **50% a 87,5% do hashrate efetivo** aos operadores
- Minerar no rank 128 ou abaixo custou quase nada

Duas lições valem para quem está começando.

**Seu hashrate depende do software e das regras da rede, não apenas da GPU.** Uma configuração que teve bons resultados em julho talvez não medisse o que o operador imaginava.

**Atualize o minerador quando a rede mudar.** Versões antigas perdem eficiência ou deixam de funcionar corretamente com as novas regras. Os softwares de pool foram atualizados antes do fork, incluindo PearlFortune v2.1.0 e Krig (Kryptex) v1.1.0, além de mineradores como Tw-pearl-miner v3.3.0 e Wildrig 0.49.8.

*Um soft fork que reduz a recompensa em até 87,5% mostra por que você deve acompanhar os anúncios do projeto, não apenas o painel de pagamentos.*

## Duas formas de mineração de Pearl

| | Mineração em pool | Minerador oficial vLLM |
|---|---|---|
| **Software** | SRBMiner-MULTI | `pearl-gateway` e `vllm-miner` |
| **Algoritmo** | `pearlhash` | NoisyGEMM pelo vLLM |
| **Exige um nó** | Não | **Sim, um `pearld` sincronizado** |
| **Pagamento** | Pool, PPLNS ou solo | Direto para seu endereço de mineração |
| **Executa um modelo real** | Não | **Sim, por exemplo Llama-3.3-70B-Instruct** |
| **Esforço de configuração** | Baixo | Alto, exige o toolkit CUDA e Python 3.12 |
| **Melhor para** | Começar a minerar na rede rapidamente | Contribuir diretamente com computação para a rede |

**Comece pela mineração em pool.** Ela não exige nó, sincronização nem download de modelo e permite minerar e configurar o endereço de pagamento em poucos minutos. Use o minerador oficial apenas se quiser servir inferência ou executar um nó.

{{< figure src="pearl-mining-pool-vs-vllm-miner-comparison.webp" alt="Diagrama que compara a mineração Pearl em pool com SRBMiner ao minerador oficial vLLM, mostrando o nó, o gateway e os componentes de inferência exigidos por cada opção" >}}

## Equipamentos para GPUs de consumo

Pearl se destaca pelo que não exige. A Hashrate Index observou que o perfil de hardware é **incomumente leve: pouca RAM, pouco armazenamento, pouca CPU e nenhuma rede cara de múltiplas fibras necessária em um cluster de treinamento real.** Um analista a descreveu como "uma ótima forma de aproveitar equipamentos".

Esse é o apelo real. **GPUs existentes, inclusive modelos antigos, geram alguma receita.**

| Categoria de GPU | Observação |
|---|---|
| **RTX 5090 e 4090** | Maior receita por placa e categorias em que se mediu a queda inicial de receita |
| **Série RTX 3000** | Beneficiou-se em particular da melhoria de hashrate da versão 3.6.8. Ainda é viável, mas eficiência importa mais que velocidade bruta |
| **Aceleradores de datacenter** | H100, H200 e B300 foram adicionadas e aprimoradas em 2026. A corrida de hashrate segue nessa direção |
| **Placas antigas ou com pouca VRAM** | Rentabilidade apertada. Consulte uma calculadora de rentabilidade atualizada antes de montar um rig |

**O padrão em todas as versões de 2026 é o mesmo.** A equipe adicionou e melhorou primeiro os aceleradores topo de linha, porque eles rendem mais hashrate. As placas de consumo receberam atenção quando a série 3000 ainda tinha margem para melhorar.

*Ajustar a eficiência gera mais receita do que perseguir frequência de clock. A maioria dos guias de mineração ensina o contrário.*

## Configuração no sistema Linux

A opção por pool exige quatro itens: o binário do SRBMiner, um endereço de carteira Pearl, o endereço do pool e um serviço para manter o minerador em execução.

### Primeiro, obtenha um endereço de carteira

Os endereços de mineração Pearl começam com **`prl1`**. A carteira oficial é **Oyster**, o daemon de carteira HD do repositório Pearl, que oferece interfaces JSON-RPC e gRPC. Gere nela um endereço de mineração **Taproot**.

Não pule esta etapa nem reutilize um endereço de outra rede. **As recompensas enviadas a um endereço que você não controla se perdem.**

### Pool, portas e mineração combinada

O maior pool Pearl é o LuckyPool, que oferece portas escalonadas conforme o hashrate esperado:

| Porta | Dificuldade inicial | Hashrate recomendado |
|---|---|---|
| **3360** | 2M | Abaixo de 500 TH/s |
| **3361** | 4M | 500 a 1000 TH/s |
| **3362** | 8M | Acima de 1000 TH/s |

Escolha a porta compatível com o hashrate real do rig. **Uma GPU de consumo sozinha deve usar a porta 3360.** Uma máquina pequena em uma porta de alta dificuldade passa longos períodos sem shares e sofre maior variação sem benefício.

Dois recursos do pool merecem atenção:

- **Mineração solo** funciona em qualquer porta ao colocar `solo:` antes da carteira. Você recebe a recompensa inteira se encontrar um bloco e não recebe nada se não encontrar. Com hashrate de consumo, espere bastante.
- **A mineração combinada com Nockchain** gera NOCK junto com PRL para o mesmo hashrate. Acrescente `+NOCK_ADDRESS` à sua carteira Pearl. O pool paga NOCK na própria Nockchain, então um endereço de token encapsulado iniciado por `0x` não pode recebê-lo. **Seu minerador precisa oferecer suporte à mineração combinada. Sem esse recurso, ele continua minerando Pearl normalmente.**

O pool publica hosts `luckypool.io` e hosts de rota `lproute.com`. Se sua rede bloquear tráfego direto de mineração, mantenha a porta e troque o domínio.

## Um script funcional de instalação

O script abaixo configura o SRBMiner como serviço systemd em um host Debian ou Ubuntu. Ele detecta todas as GPUs, aplica opções de overclock por placa, verifica o download com o MD5 publicado, grava a unidade e uma política do logrotate e reinicia o serviço.

```bash
#!/usr/bin/env bash
# install-pearl-miner.sh -- configura SRBMiner (Pearl / PRL) como serviço systemd.
# Executar: sudo bash install-pearl-miner.sh
set -euo pipefail

ALGO="pearlhash"
POOL="${POOL:-pearl-us-east.luckypool.io:3360}"
WALLET="${WALLET:-<YOUR_PR1_ADDRESS>}"   # prl1... adicione +NOCK_ADDRESS para mineração combinada
WORKER="${WORKER:-rig-1}"
SRB_VERSION="${SRB_VERSION:-3.6.9}"
MINER_DIR="/opt/srbminer"
UNIT="/etc/systemd/system/pearl-miner.service"
SVC="pearl-miner.service"
LOG="/var/log/pearl-miner.log"

# Ajuste para a classe RTX 3070. MCORE fixa o clock da memória em um valor bem abaixo do
# padrão da placa, 7001 MHz. É um underclock intencional para eficiência, não um overclock de desempenho.
# Defina qualquer valor como "" para desativar essa opção.
CCLOCK="${CCLOCK:-1560}"
MCLOCK="${MCLOCK:-5001}"
COFFSET="${COFFSET:-150}"
PLIMIT="${PLIMIT:-180}"
FAN="${FAN:-}"
THERMAL="${THERMAL:-88}"
```

O bloco de ajuste merece uma observação, porque parece errado à primeira vista. **`MCORE=5001` fica abaixo do clock de memória padrão de uma 3070.** Isso é intencional. Pearl recompensa eficiência de memória, e reduzir o clock diminui o consumo mais do que reduz o hashrate. **Não copie números de overclock de uma linha de banco de hashrates sem verificar qual GPU foi usada no teste.** Muitas vezes, os resultados se referem a uma placa diferente da sua.

```bash
[ "$(id -u)" -eq 0 ] || { echo "execute como root (sudo)"; exit 1; }
command -v nvidia-smi >/dev/null || { echo "nvidia-smi ausente, instale o driver primeiro"; exit 1; }

GPU_N=$(nvidia-smi --query-gpu=index --format=csv,noheader | wc -l)
echo "== GPUs NVIDIA detectadas: $GPU_N =="
nvidia-smi --query-gpu=index,name,memory.total,power.limit --format=csv,noheader

# Cria opções de overclock para cada GPU detectada
OC=""
for i in $(seq 0 $((GPU_N - 1))); do
    [ -n "$COFFSET" ] && OC="$OC --gpu-coffset$i $COFFSET"
    [ -n "$CCLOCK" ]  && OC="$OC --gpu-cclock$i $CCLOCK"
    [ -n "$MCLOCK" ]  && OC="$OC --gpu-mclock$i $MCLOCK"
    [ -n "$PLIMIT" ]  && OC="$OC --gpu-plimit$i $PLIMIT"
    [ -n "$FAN" ]     && OC="$OC --gpu-fan$i $FAN"
done
THERMAL_ARG=""
[ -n "$THERMAL" ] && THERMAL_ARG=" --shutdown-temperature $THERMAL"

# Baixa e verifica a versão
STEM="SRBMiner-Multi-$(echo "$SRB_VERSION" | tr . -)-Linux"
BASE="https://github.com/doktor83/SRBMiner-Multi/releases/download/$SRB_VERSION"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
curl -fsSL -o "$TMP/$STEM.tar.gz"  "$BASE/$STEM.tar.gz"
curl -fsSL -o "$TMP/$STEM.tar.md5" "$BASE/$STEM.tar.md5"
(cd "$TMP" && md5sum -c <(tr -d '\r' < "$STEM.tar.md5"))

# Para o serviço antes de substituir o binário aberto pelo processo
systemctl stop "$SVC" 2>/dev/null || true
tar -xzf "$TMP/$STEM.tar.gz" -C "$TMP"
SRC=$(find "$TMP" -maxdepth 1 -type d -name 'SRBMiner-Multi-*' | head -1)
mkdir -p "$MINER_DIR"
[ -f "$MINER_DIR/SRBMiner-MULTI" ] && \
    cp -a "$MINER_DIR/SRBMiner-MULTI" "$MINER_DIR/SRBMiner-MULTI.bak-$(date +%F-%H%M%S)"
cp -a "$SRC"/. "$MINER_DIR"/
chown -R root:root "$MINER_DIR"
chmod 755 "$MINER_DIR/SRBMiner-MULTI"
```

**Verifique o MD5 antes de executar qualquer binário de mineração.** As versões publicam hashes por arquivo, e o minerador roda com privilégios de root e acessa sua GPU. Ignorar a verificação significa confiar em um download que você não inspecionou.

Dois detalhes operacionais da unidade de serviço:

```bash
cat >"$UNIT" <<EOF
[Unit]
Description=Minerador Pearl (PRL) SRBMiner v$SRB_VERSION - $WORKER
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=$MINER_DIR
ExecStart=$MINER_DIR/SRBMiner-MULTI --algorithm $ALGO --pool $POOL --wallet $WALLET --worker $WORKER --disable-cpu --gpu-reset-oc$OC$THERMAL_ARG --api-enable --api-port 21550 --api-rig-name $WORKER
Restart=always
RestartSec=10
StandardOutput=append:$LOG
StandardError=append:$LOG
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
EOF
```

- **`--disable-cpu`** impede o minerador de usar a CPU, algo importante em uma máquina que executa outras tarefas.
- **`--shutdown-temperature 88`** interrompe o minerador em vez de superaquecer a placa quando uma ventoinha falha.
- **`--gpu-reset-oc`** limpa configurações de clock anteriores antes de aplicar as novas e evita que valores antigos permaneçam ativos.
- **`Restart=always` com `RestartSec=10`** tolera falhas momentâneas do driver, comuns em rigs com várias GPUs.
- **`--api-enable` abre uma porta de monitoramento.** Confirme em qual interface a porta 21550 fica vinculada e mantenha-a fora de redes não confiáveis. O endpoint de monitoramento do rig não precisa ser acessível de fora da máquina.

Por fim, configure a rotação dos logs, que crescem sem limite durante a mineração:

```bash
cat >/etc/logrotate.d/pearl-miner <<EOF
$LOG {
    weekly
    rotate 4
    compress
    delaycompress
    missingok
    notifempty
    copytruncate
}
EOF

systemctl daemon-reload
systemctl enable "$SVC" >/dev/null 2>&1 || true
systemctl restart "$SVC"
```

*`copytruncate` é importante aqui. O SRBMiner mantém o arquivo de log aberto. Se a rotação renomear o arquivo, o minerador continua escrevendo em um inode excluído e o disco acaba cheio mesmo assim.*

Acompanhe o progresso com uma busca filtrada em vez de exibir o log bruto:

```bash
grep -aE 'Hashrate|accepted|Pool:' /var/log/pearl-miner.log | tail -20
```

## Problemas encontrados

**Um guia de mineração Pearl precisa começar pelos problemas, porque todos afetam seus pagamentos.** Quatro coisas deram errado entre julho e setembro de 2026.

### O mercado depende de uma única corretora

Em **23 de julho de 2026**, o PRL atingiu a mínima histórica de **US$ 0,1399**, após cerca de **US$ 0,87** em junho. Caiu **24,2% em um único dia** e **26,7% na semana**, enquanto o mercado cripto mais amplo subiu cerca de 2% no mesmo período.

A causa não foi uma notícia. Foi a falta de liquidez.

- **95,17% de todo o volume reportado** estava em **uma exchange chamada SafeTrade**, sem pontuação de confiança da CoinGecko. Um único par PRL/USDT respondeu por **US$ 738.399 dos cerca de US$ 775.000** negociados em 24 horas.
- Os dois pares da SafeTrade registravam **US$ 0,00 de profundidade no livro de ofertas**.

*Uma ordem de venda comum altera em dois dígitos um mercado assim. Isso é uma característica estrutural do token, não uma condição passageira.*

A distribuição da oferta agrava o quadro:

| Métrica | Valor |
|---|---|
| **Capitalização de mercado** | US$ 55,7 milhões |
| **Avaliação totalmente diluída** | US$ 458,6 milhões |
| **Proporção** | Mais de 8x |
| **Oferta em circulação** | 255 milhões de 2,1 bilhões, menos de **13%** |

**Um token cotado em um único livro pouco líquido, com 87% da oferta ainda bloqueada ou não emitida, admite uma ampla faixa de preços plausíveis.** Planeje o que fazer com os pagamentos e não trate a cotação à vista como uma estimativa confiável de receita.

### Um pool de mineração foi invadido

Uma issue aberta em **18 de setembro de 2026** relata que a carteira Pearl 2.0.5 "ainda suspendeu envios e recebimentos depois do ataque ao pool ocorrido um mês atrás".

**Leia novamente, pois há dois fatos nessa frase.** Um pool Pearl foi comprometido por volta de **agosto de 2026**, e a carteira oficial respondeu suspendendo transferências. A suspensão continuava um mês depois.

O pool escolhido mantém seus pagamentos. Verifique o histórico de incidentes antes de apontar seu rig para ele.

### O site do projeto está inacessível

No momento da redação, **pearlresearch.ai não chega a nenhum servidor.** Todos os resolvedores públicos retornam uma rota nula, `0.0.0.0`, para o domínio principal e subdomínios como `compute` e `explorer`. O registro do domínio mostra `ACTIVE`, então esse estado de DNS é deliberado, não resultado de expiração.

**Três links que um guia de mineração normalmente indicaria estão mortos**, inclusive o explorador de blocos. O Mining Pool Stats ainda os lista, levando leitores a tentar acessar um endereço que nunca carrega.

Use **[prlscan.com](https://prlscan.com)** para explorar blocos. Confirmei que a página está funcionando.

### O software ainda tem falhas em aberto

O rastreador público de issues mostra problemas sem solução no fim de setembro de 2026. A criação de issues está restrita, então esta visão é parcial.

| Issue | Data | Consequência |
|---|---|---|
| **Código RPC da carteira de desktop inativo** | 22 de set. | A carteira não consegue acessar um nó |
| **A testnet não sincroniza do zero**, nós travam na altura 36760 | 22 de set. | Há um defeito bloqueante na sincronização |
| **Envios e recebimentos da carteira continuam suspensos** após o ataque ao pool | 18 de set. | Transferências afetadas |
| **A versão macOS ARM64 tem uma assinatura de código inválida** | 17 de set. | Não executa sem contornar o Gatekeeper |
| **O modo prune descarta certificados necessários para verificar cabeçalhos** | 30 de ago. | Defeito de validação |
| **O nó trava indefinidamente quando nenhum peer conectado pode sincronizar** | 30 de ago. | Sincronização frágil |
| **`pearl-gemm` falha na RTX 5070**: kernels de hash funcionam, mas os kernels GEMM falham | 31 de ago. | As GPUs de consumo mais recentes não têm suporte |

*A entrada da RTX 5070 merece atenção se você pensa em comprar uma placa atual para isso. A arquitetura de consumo mais recente não funcionava com o caminho GEMM oficial.*

**O quadro geral:** o software de mineração recebe manutenção ativa, enquanto as camadas voltadas ao usuário e ao mercado são pontos fracos. O SRBMiner lançou a versão 3.6.9 com grandes ganhos de eficiência um dia antes das reclamações sobre a carteira.

## A rede é útil?

Esta pergunta exige cuidado porque boa parte da cobertura usa "trabalho útil" com dois sentidos. **O termo descreve um mecanismo de consenso e uma alegação econômica, e cada um tem uma resposta bem diferente.**

### Utilidade funcional: parcial

**A rede funciona. O produto ao redor dela ainda não funciona por completo.**

O que funciona:

- **A rede principal foi lançada em 27 de abril de 2026** e produz blocos desde então.
- **A pilha completa existe e está disponível**: um nó, um daemon de carteira, um cliente leve SPV, um sistema de provas de conhecimento zero e um minerador para GPU, tudo em um repositório.
- **A infraestrutura tem histórico comprovado no código.** O nó, a carteira e o cliente leve derivam de **btcd**, **btcwallet** e **neutrino**, projetos Bitcoin com anos de testes adversariais.
- **A base de código é um trabalho sério.** Tem 315 estrelas, 76 forks, mais de 6.800 commits e um rastreador público onde contribuidores registram bugs precisos.
- **A mineração funciona.** O SRBMiner publicou 247 versões e otimizou `pearlhash` repetidas vezes. Vários pools operam e a mineração combinada com Nockchain funciona.

O que não funciona:

- **As transferências estão suspensas na carteira oficial** após o ataque ao pool.
- **A carteira de desktop não consegue acessar um nó**, segundo seu rastreador, no fim de setembro.
- **A sincronização tem defeitos bloqueantes** tanto na testnet quanto na rede principal.
- **O site do projeto está inacessível.**
- **As GPUs de consumo mais recentes falham no caminho GEMM.**

**A conclusão honesta é que Pearl funciona na camada do protocolo e é pouco confiável na camada do produto.** Para quem estuda prova de trabalho útil, isso merece atenção. Para quem espera minerar e receber pagamentos regularmente, é um alerta.

### Utilidade técnica: o mecanismo sim, o mercado não

A resposta honesta se divide em duas partes. Confundi-las é o erro de grande parte da cobertura.

**O mecanismo é realmente inovador.** A rotina NoisyGEMM da Pearl executa multiplicações ruidosas de matrizes na GPU, transforma o resultado em um compromisso criptográfico e inclui uma prova de conhecimento zero para manter a verificação barata. A construção se baseia no artigo real "Provas de trabalho útil por multiplicação arbitrária de matrizes", de Komargodski, Schen e Weinstein, que afirma uma sobrecarga de aproximadamente **1 + o(1)** em relação à multiplicação ingênua de matrizes.

**Se esse limite se confirmar, a rede se protege com custo quase nulo além da computação subjacente.** Foi isso que as tentativas anteriores de PoUW não conseguiram. A matemática não é decorativa.

**O mercado ainda não está estabelecido.** A Hashrate Index descreveu a situação assim: "hoje, a maior parte do trabalho útil é inferência que ninguém comprou, o que transforma a maior parte da mineração atual em uma prova de trabalho com formato de IA". É um resumo justo. A computação tem o formato certo, mas ninguém paga pela maior parte dela.

A exceção importa e é real. Pearl fechou uma parceria exclusiva com a **Together AI**, que colocou em produção um endpoint de inferência da Pearl com desconto. Esse é o primeiro cliente e o motivo para dar ao projeto mais crédito que à moeda média com marca de IA.

**Um cliente prova o conceito. Não forma um mercado.**

### Utilidade prática: por enquanto, com uma janela se fechando

Para quem minera, o cenário prático é misto e limitado no tempo.

**Pontos a favor da Pearl:**

- GPUs existentes geram alguma receita, inclusive placas antigas, porque o perfil de hardware é leve
- Melhorias contínuas na eficiência do minerador aumentam diretamente a margem do hardware que você já possui
- A mineração combinada com Nockchain acrescenta uma segunda fonte de receita ao mesmo hashrate
- A sobrecarga quase nula significa que a rede não consome sua eletricidade com hashing sem utilidade

**Pontos contra:**

- **A recompensa por bloco diminui por projeto.** Esse é o modelo do Bitcoin, e as emissões caem mesmo se o preço subir.
- **A dificuldade só aumenta.** A receita por GPU só pode seguir uma direção.
- **A liquidez é baixa.** A Hashrate Index aponta como questão a acompanhar se o PRL alcançará liquidez fora das exchanges pequenas. Pouca liquidez significa spreads maiores e preços realizados piores.
- **A atualização do protocolo.** As notas da versão 3.6.8 do SRBMiner dizem que uma futura atualização da Pearl tornará GPUs de consumo "praticamente inúteis". Leve isso a sério. A declaração vem do desenvolvedor que se beneficia da continuidade da mineração.

## Veredito

**Pearl é a implementação mais convincente de prova de trabalho útil já criada, mas ainda não provou que seu trabalho seja útil no sentido econômico.**

Quatro afirmações, em ordem de confiança:

1. **O mecanismo de consenso funciona e a alegação criptográfica é real.** Pearl resolveu o problema técnico difícil: tornar barata a verificação de PoUW. Isso é uma contribuição genuína, independentemente do futuro do token.

2. **A computação é uma promessa, não um produto.** Produzir inferência não é o mesmo que vendê-la. Hoje, a parcela paga consiste em uma parceria numa rede cheia de hashrate especulativo. O ciclo de crescimento foi projetado, mas não está girando.

3. **A janela para mineração com GPUs de consumo está diminuindo, e o protocolo vai fechá-la.** Recompensa em queda, dificuldade em alta, uma atualização declarada que elimina a viabilidade para consumidores e um soft fork que já reduziu em até 87,5% o hashrate de alguns mineradores formam uma oportunidade limitada no tempo, não uma fonte de renda.

4. **Os riscos reais estão nas camadas operacional e de mercado, não na criptografia.** Um pool invadido, transferências suspensas na carteira, um site inacessível, falhas de sincronização sem solução e 95% do volume em uma exchange sem profundidade no livro de ofertas são os fatores que determinam se a mineração paga. O protocolo é a parte que funciona.

*Em termos diretos: Pearl resolveu o problema difícil, mas ainda não resolveu o que parecia simples. Provar que a multiplicação de matrizes é útil é criptografia. Encontrar compradores para o resultado é vendas.*

**Se você veio para minerar, trate isso como uso de curto prazo para hardware que já possui.** Não compre GPUs para Pearl. Não monte um rig supondo que os números atuais vão durar, pois o cronograma de emissão e as notas do próprio desenvolvedor dizem o contrário.

**Se você quer entender a prova de trabalho útil, Pearl é a implementação mais importante para estudar agora.** É a primeira a alcançar escala real. As evidências dos próximos dois anos mostrarão se "trabalho útil" é um primitivo genuíno ou uma falha recorrente com criptografia melhor.

{{< figure src="pearl-prl-usefulness-assessment.webp" alt="Diagrama que avalia a prova de trabalho útil da Pearl em três eixos: maturidade funcional alta, mecanismo técnico forte mas mercado pago não comprovado, e viabilidade prática da mineração limitada no tempo" >}}

## Principais conclusões

- **Pearl é uma blockchain L1 derivada do Bitcoin e protegida por prova de trabalho útil**, em que mineradores executam multiplicação ruidosa de matrizes em vez de hashing. A rede principal foi lançada em **27 de abril de 2026**.
- **Há duas formas de minerar:** SRBMiner com `--algorithm pearlhash` conectado a um pool ou o `vllm-miner` da Pearl conectado a um nó sincronizado.
- **A rentabilidade inicial veio da curva de emissão do lançamento**, não da demanda por IA. A receita diária estimada da RTX 5090 caiu aproximadamente pela metade poucas semanas após a corrida de mineração.
- **As versões mais eficientes do minerador compensaram parte da queda.** A versão 3.6.9 manteve ou aumentou o hashrate com consumo bem menor.
- **O soft fork da penalidade de rank em 6 de agosto de 2026 reduziu o hashrate efetivo em 50% a 87,5%** para mineradores acima do rank 128. Atualize o minerador quando as regras da rede mudarem.
- **O token depende de uma única exchange para ter liquidez.** 95,17% do volume estava na SafeTrade, sem profundidade no livro de ofertas, e menos de 13% da oferta circula.
- **Um pool foi invadido por volta de agosto de 2026**, e as transferências da carteira oficial continuavam suspensas um mês depois.
- **O site do projeto não resolve.** Use `prlscan.com` para explorar blocos.
- **Ajuste para eficiência, não para frequência de clock.** Pearl recompensa a eficiência da memória, e reduzir o clock da memória economiza mais energia do que custa em hashrate.
- **Use a porta 3360 com uma única GPU de consumo** e acrescente `+NOCK_ADDRESS` para minerar Nockchain em conjunto.
- **Verifique o MD5** de qualquer download de minerador antes de executá-lo como root.
- **Minere com hardware que você já possui.** A rede funciona na camada do protocolo, é pouco confiável na camada do produto e seu mercado de computação paga tem apenas uma parceria.

## Próximos passos

1. **Leia o repositório fonte** do nó, da carteira e do minerador oficial vLLM: **[pearl-research-labs/pearl](https://github.com/pearl-research-labs/pearl)**
2. **Confira o changelog do minerador antes de ajustar qualquer parâmetro**, pois a eficiência muda entre versões: **[versões do SRBMiner-Multi](https://github.com/doktor83/SRBMiner-Multi/releases)**
3. **Escolha uma porta do pool** adequada ao seu hashrate real: **[LuckyPool Pearl](https://pearl.luckypool.io)**
4. **Compare a distribuição de hashrate dos pools** antes de decidir: **[Estatísticas dos pools de mineração de Pearl](https://miningpoolstats.stream/pearl)**
5. **Calcule primeiro o custo de energia**, pois a eletricidade determina se a mineração é rentável: **[Monte um equipamento de renda passiva rentável](/other/creating-profitable-low-powered-crypto-miners/)**
6. **Aplique as práticas de ajuste para várias GPUs** do nosso outro guia de mineração por trabalho útil: **[Mineração eficiente de Spacemesh com várias GPUs](/other/efficient-spacemesh-mining-multiple-gpus-guide/)**

## Artigos relacionados

| Artigo | Conteúdo |
|---|---|
| **[Mineração eficiente de Spacemesh com várias GPUs](/other/efficient-spacemesh-mining-multiple-gpus-guide/)** | Ajustes para várias GPUs e gerenciamento de energia em outra rede de trabalho útil |
| **[Monte um equipamento de renda passiva rentável](/other/creating-profitable-low-powered-crypto-miners/)** | Dimensionamento do hardware de mineração segundo o custo de eletricidade antes da compra |
| **[IA local em 2026: um modelo 27B supera o Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | O que as mesmas GPUs fazem ao executar inferência local em vez de mineração |
| **[Minere Verus no Android: guia simples para mineração no celular](/other/mine-verus-on-android-guide/)** | Mineração com CPU em hardware que você já possui |

## Referências

1. [pearl-research-labs/pearl - monorepo da rede](https://github.com/pearl-research-labs/pearl)
2. [pearl-research-labs/pearl - issues em aberto](https://github.com/pearl-research-labs/pearl/issues)
3. [Pearl (PRL): como a matemática de matrizes transforma computação de IA em mineração - Hashrate Index](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
4. [Soft fork da penalidade de rank ativado na rede Pearl (PRL) - Cryptoage](https://cryptoage.com/en/5400-rank-penalty-softfork-activated-on-the-pearl-prl-network.html)
5. [Pearl atinge nova mínima histórica - CryptoNewsLive](https://www.cryptonewslive.org/article/pearl-hit-a-fresh-all-time-low-today-95-of-its-volume-sits-on-one-exchange-with-zero-order-book-depth)
6. [Versões do SRBMiner-Multi - doktor83](https://github.com/doktor83/SRBMiner-Multi/releases)
7. [LuckyPool - pool de mineração combinada Pearl e Nock](https://pearl.luckypool.io)
8. [Estatísticas de pools - Pearl (PRL) PearlHash](https://miningpoolstats.stream/pearl)
9. [prlscan.com - explorador de blocos PRL](https://prlscan.com)

**Observação sobre o domínio oficial:** no momento da redação, `pearlresearch.ai` e seus subdomínios `compute` e `explorer` retornam uma rota nula. O artigo os omite deliberadamente em vez de publicar links quebrados e indica `prlscan.com` para explorar blocos.

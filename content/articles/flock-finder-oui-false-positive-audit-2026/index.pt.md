---
title: "Mapeamos 146.526 «câmeras Flock». 50.278 eram sistemas ClickShare"
date: 2026-09-21
lastmod: 2026-11-14
toc: true
draft: false
description: "Uma auditoria do Flock Finder identifica ClickShare e outros falsos positivos, explica as evidências e registra as mudanças."
genre: ["Pesquisa de segurança", "Tecnologia de privacidade", "Projetos de código aberto", "Jornalismo de dados", "Contravigilância"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Fingerprinting OUI", "WiGLE", "Falsos positivos", "Qualidade dos dados", "Barco ClickShare", "Endereço MAC", "IEEE OUI", "Fingerprinting de elementos de informação", "ESP32", "Flock-You", "NitekryDPaul", "DeFlockJoplin", "Responsabilidade de código aberto", "Mapeamento de vigilância", "WiFi", "Solicitação de sondagem", "Randomização de MAC"]
cover: "/img/cover/flock-finder-oui-false-positive-audit-2026.webp"
coverAlt: "Um mapa urbano escuro com muitos pinos vermelhos que correspondem a dispositivos WiFi de escritórios, enquanto alguns pinos verdes indicam detecções mais fortes"
coverCaption: "A auditoria de 146.526 registros do Flock Finder mostrou como uma observação de campo útil virou uma afirmação exagerada no mapa."
canonical: "https://simeononsecurity.com/articles/flock-finder-oui-false-positive-audit-2026/"
---

**Colocamos 146.526 pontos em um mapa de câmeras de vigilância. Pelo menos 50.278 eram sistemas de apresentação Barco ClickShare. Equipamentos de salas de conferência representavam mais de um terço do que nosso título chamou de «câmeras mapeadas».**

Este era nosso projeto, nosso pipeline de dados e nosso erro. O Flock Finder consultava o WiGLE todos os dias em busca de prefixos MAC observados em câmeras Flock Safety, publicava os resultados com coordenadas de precisão total e mostrava todos como pinos equivalentes. Os metadados continham a palavra `suspected` e a documentação mencionava falsos positivos. Mesmo assim, o mapa e o título comunicavam certeza.

**Resultado para o leitor:** reproduza a auditoria, separe observação de atribuição e mostre o nível de confiança junto ao pino e ao título. Uma correspondência de prefixo é uma pista de investigação, não prova de que seja uma câmera.

Quando finalmente calculamos um histograma de frequência da coluna SSID, o conjunto de dados explicou a falha em minutos. ClickShare era apenas a maior categoria. Outros 6.099 registros se chamavam `SMARTGATE_*`, 3.801 começavam com o prefixo genérico WiFi Direct `DIRECT-`, 314 tinham exatamente o nome `AndroidAP`, 138 diziam `Audi HUD`, 133, `MAX-PRINTER`, e 30 continham a string de veredito de outro detector. Ao todo, **60.793 linhas, ou 41,5%, correspondiam às regras conhecidas de nomes de outros dispositivos na auditoria original.**

Agora o Flock Finder publica uma classe de evidência por registro, exclui por padrão da visualização e do título os equipamentos conhecidos como outros, disponibiliza filtros, sinaliza registros fora do mercado principal e separa prefixos de alta confiança dos prefixos de fabricantes contratados. Este artigo documenta o erro, as evidências e os limites que permanecem.

______

## Como funciona a detecção comunitária de ALPR

Detectores Flock criados pela comunidade costumam combinar três tipos de evidência sem fio:

1. **Prefixos WiFi MAC/OUI.** Os primeiros bytes de um endereço MAC administrado globalmente podem identificar a organização que recebeu o bloco de endereços.
2. **Comportamento WiFi.** Um SSID, uma solicitação de sondagem curinga, um endereço de receptor, um padrão de canal ou uma sequência de elementos de informação 802.11 pode restringir a classe do dispositivo.
3. **Evidência Bluetooth.** IDs do fabricante e UUIDs de serviço podem identificar rádios expostos por um produto ou geração de firmware.

A correspondência OUI se popularizou porque é barata e passiva. Um ESP32 acessível pode inspecionar quadros 802.11 próximos sem entrar em uma rede. Uma base histórica como [WiGLE](https://wigle.net/) também permite pesquisar observações antigas sem instalar scanners próprios.

O método seguiu uma linhagem comunitária: o mapeamento e a organização local de [DeFlock](https://deflock.org/), [colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you), forks e projetos complementares, como nosso [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32), e, por fim, [Flock Finder](https://github.com/simeononsecurity/flock-finder), que aplicou a lista de prefixos aos dados globais do WiGLE.

O trabalho de campo original merece crédito claro. [@NitekryDPaul](https://github.com/NitekryDPaul) observou 30 prefixos em equipamentos Flock reais por meio de pesquisa em modo promíscuo. [DeFlockJoplin](https://github.com/DeflockJoplin/flock-you) contribuiu com outro durante testes de campo. Essas observações eram legítimas. Nosso erro posterior foi tratar **«observado em uma câmera Flock» como se significasse «exclusivo das câmeras Flock».**

______

## A falha estrutural: um OUI é um dado da cadeia de suprimentos

A IEEE descreve um OUI como um identificador de 24 bits atribuído a um fornecedor, fabricante ou outra organização. Junto a mais 24 bits escolhidos pelo destinatário, ele forma um endereço MAC. A [IEEE Registration Authority](https://standards.ieee.org/products-programs/regauth/) publica o registro.

Isso informa quem recebeu um bloco de endereços. Não necessariamente informa a marca em um produto finalizado. Fabricantes contratados criam módulos de rádio para vários clientes. O mesmo fornecedor de chips pode aparecer em câmeras, projetores, impressoras, veículos e placas de hobby.

As atribuições do registro por trás da nossa lista deixavam o risco claro:

| Registrante | Prefixos na lista auditada |
|---|---|
| Liteon Technology | `74:4C:A1`, `F4:6A:DD`, `9C:2F:9D`, `C0:35:32`, `E4:AA:EA`, `14:5A:FC` e outros |
| Universal Global Scientific Industrial (USI) | `E0:4F:43`, `08:3A:88` |
| Espressif | `A4:CF:12`, `3C:71:BF` |
| Silicon Laboratories | `58:8E:81`, `90:35:EA`, `EC:1B:BD` |
| Flock Safety | `B4:1E:52` |

As entradas da Espressif deveriam ter nos alertado. Dois prefixos de uma suposta lista de câmeras pertenciam ao fabricante de uma das plataformas WiFi embarcadas mais comuns do mundo, incluindo o chip usado por muitos detectores comunitários.

`B4:1E:52` é diferente porque está registrado diretamente para a Flock Safety. Ele entrou na lista de 38 prefixos no commit auditado, **mas ainda não tinha sido consultado**: `scan_stats.json` informava 31 prefixos consultados. O mesmo ocorria com seis prefixos recém-adicionados de baterias. Portanto, o snapshot não prova se o prefixo próprio da Flock é comum ou raro. Não transformaremos «não consultado» em «zero resultados».

O repositório atual contém 39 prefixos após a inclusão de `E0:0A:F6` para acompanhar o firmware do detector. O resumo de varredura mantido ainda mostra dados de 31 prefixos. Assim, os novos itens aguardam um recálculo completo e não são prefixos com zero resultado comprovado.

______

## O conjunto de dados se auditou

Cada número histórico de auditoria abaixo foi regenerado de `data/flock_cameras.csv` no commit do Flock Finder [`5551829`](https://github.com/simeononsecurity/flock-finder/tree/5551829), usando `csv` e `collections.Counter` da biblioteca padrão do Python. Não foi preciso fazer outro teste de campo. Os nomes, a geografia e a composição dos prefixos já contradiziam o título. Os números da implementação corrigida vêm do resumo `scan_stats.json` mantido no repositório atual.

### A geografia foi um alerta inicial

Das 146.526 linhas, 75.818 estavam nos Estados Unidos, 70.674 fora do país e 34 não tinham valor de país. A Alemanha tinha 13.491 registros, seguida pelo Canadá com 6.251, França com 5.839, Grã-Bretanha com 4.836, Países Baixos com 4.636 e Suíça com 4.515.

{{< figure src="flock-finder-us-non-us-split.webp" alt="Gráfico de barras empilhadas com 75.818 registros dos Estados Unidos, 70.674 de fora e 34 sem país" caption="O histograma dos países soma 146.492 porque 34 linhas têm país nulo." >}}

A geografia é um sinal para triagem, não uma prova. A Flock descreve sua rede como «nacional» e diz conectar clientes em [49 estados dos EUA](https://www.flocksafety.com/flock-ecosystem). A expansão internacional também pode mudar o limite do mercado. Por isso marcamos registros fora do mercado para revisão, em vez de apagá-los ou declarar falsos todos os registros fora dos EUA.

A conclusão prudente é suficiente: quase metade dos registros estava fora do mercado principal dos EUA. Sem outro sinal, uma correspondência OUI global não poderia ser considerada igualmente plausível.

### Mais de 60.000 dispositivos diziam seu próprio nome

| Família SSID na auditoria original | Registros | Proporção | O que o nome indica |
|---|---:|---:|---|
| Contém `ClickShare` | 50.278 | 34,3% | Equipamento de apresentação sem fio Barco |
| `SMARTGATE_*` | 6.099 | 4,2% | Família de gateway ou dispositivo tipo OBD |
| `DIRECT-*` | 3.801 | 2,6% | Dispositivos WiFi Direct, como impressoras, TVs e adaptadores |
| Nome exato `AndroidAP` | 314 | 0,2% | Hotspots Android |
| Nome exato `Audi HUD` | 138 | 0,1% | WiFi de infoentretenimento ou head-up display Audi |
| Nome exato `MAX-PRINTER` | 133 | 0,1% | Impressoras de escritório |
| `Flock ALPR [...]` | 30 | <0,1% | Veredito de outro detector armazenado como SSID |
| **Total da auditoria original** | **60.793** | **41,5%** | Identificáveis como outro equipamento ou saída de detector |

A documentação de suporte da Barco informa que o nome de rede padrão de uma unidade base ClickShare é [`ClickShare-<serial base number>`](https://www.barco.com/en/support/knowledge-base/2675-how-to-connect-to-your-clickshare-base-unit-wifi). Isso confirma a família do produto por fonte primária, sem suposições sobre geografia ou registro do fornecedor.

O classificador de produção substituiu essas verificações de nomes exatos por expressões regulares sem distinção entre maiúsculas e minúsculas. Inclui ClickShare, SmartGate, WiFi Direct, AndroidAP, Audi HUD, MAX-PRINTER e rótulos de saída de detectores. Nas mesmas 146.526 linhas, identifica 629 variantes de AndroidAP, 139 de Audi HUD e 134 de MAX-PRINTER. Assim, o repositório atual informa **61.110 registros `identified_other`**, um pouco acima dos 60.793 encontrados na auditoria original.

### O sinal de confirmação era só 2,4%

Apenas **3.502 linhas** tinham um SSID genuíno no padrão Flock. Outras 24.964 não tinham SSID. O restante indicava outro equipamento ou usava um OUI com nome não classificado.

As 3.502 linhas confirmadas continham 161 variantes reais de SSID: 3.342 ocorrências do nome simples `Flock`, 157 nomes de provisionamento únicos `Flock-XXXXXX` ou `FLOCK-XXXXXX` e três outros nomes com `flock`. Um antigo total de 166 variantes no README incluía cinco strings distintas de anotação `Flock ALPR [...]` do detector. Elas são evidências do detector, não da câmera.

{{< figure src="flock-finder-evidence-class-breakdown.webp" alt="Barra empilhada de 100% divide 146.526 registros em 3.502 confirmados por SSID, 57.267 nomeados não classificados, 24.964 só com OUI oculto, 60.763 identificados como outros e 30 retornos do detector" caption="O antigo título reuniu cinco classes de evidência materialmente diferentes em uma só contagem." >}}

### A qualidade dos prefixos variava muito

A taxa de falsos positivos não era uniforme. Alguns prefixos mantinham um sinal Flock útil. Outros eram dominados por dispositivos nomeados de escritório ou de consumo.

{{< figure src="flock-finder-per-oui-composition.webp" alt="Barras empilhadas horizontais para 31 prefixos OUI: SSIDs Flock em verde, SSIDs conhecidos de outros dispositivos em vermelho, SSIDs ocultos em cinza claro e registros não classificados em cinza escuro" caption="Os maiores prefixos costumavam conter mais dispositivos conhecidos como outros. Dados do snapshot de auditoria de 146.526 linhas." >}}

Compare dois prefixos que o mapa antigo rotulava da mesma forma:

- `70:C9:4E` tinha 495 linhas: 133 nomes no padrão Flock e 29 nomes conhecidos de outros dispositivos.
- `74:4C:A1` tinha 11.872 linhas: 211 nomes no padrão Flock e 8.385 nomes conhecidos de outros dispositivos.

{{< figure src="flock-finder-prefix-signal-contrast.webp" alt="Comparação: prefixo 70 C9 4E com 26,9% de SSID Flock e 5,9% conhecidos como outros, prefixo 74 4C A1 com 1,8% de SSID Flock e 70,6% conhecidos como outros" caption="Um rótulo único ocultava relações sinal-ruído opostas." >}}

O mesmo padrão aparece nos maiores grupos: `F4:6A:DD` tinha 8.422 nomes conhecidos de outros contra 327 nomes Flock, `D0:39:57` tinha 8.270 contra 473, `E0:4F:43` incluía 6.238 nomes conhecidos de outros contra 66 nomes Flock. O volume de um prefixo não provava qualidade.

______

## O ciclo de feedback escondido em 30 linhas

Trinta registros do Texas tinham SSIDs que claramente eram a saída de outro detector:

| Rótulo do detector armazenado como SSID | Confiança declarada pela ferramenta | Registros |
|---|---:|---:|
| `Flock ALPR [wifi_receiver_oui;low]` | baixa | 20 |
| `Flock ALPR [wifi_oui_wildcard_probe;medium]` | média | 4 |
| `Flock ALPR [wifi_bssid_oui;low]` | baixa | 3 |
| `Flock ALPR [flock_receiver_oui;low]` | baixa | 2 |
| `Flock ALPR [wifi_hidden_ssid_oui;low]` | baixa | 1 |

A ferramenta que criou 26 dos 30 registros os classificou como de baixa confiança. Um envio ao WiGLE armazenou depois o veredito dessa ferramenta no campo SSID. Nosso pipeline encontrou a palavra `Flock` e poderia ter tratado o rótulo como confirmação independente.

Trinta linhas são pouco em termos estatísticos. O mecanismo é relevante: ferramentas que compartilham uma base de dados colaborativa podem ingerir os resultados umas das outras e transformar um palpite de baixa confiança em aparente corroboração. A correção bloqueia todo o padrão `Flock ALPR [` antes de procurar a substring confirmatória `flock`.

______

## Onde erramos

O título do README dizia **«Câmeras mapeadas | 146.526»**. O mapa publicava coordenadas com precisão total e desenhava todos os resultados com o mesmo tipo de pino. Atualizações programadas pelo GitHub Actions faziam uma heurística fraca parecer um inventário mantido.

Incluímos ressalvas. Cada item tinha `match_confidence: "suspected"`. O README citava ClickShare como possível equipamento coexistente, e o projeto mantinha uma trilha separada para candidatos descobertos por SSID. Essas ressalvas não determinavam o número, o marcador nem a visualização padrão que os leitores viam.

Usamos ressalvas no texto e números no título. O mapa fez a afirmação.

A parte mais evitável é que o firmware do nosso [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32) já separava identificadores de alta confiança dos de fabricantes contratados e avaliava evidência fraca abaixo do limiar de alerta. O conceito existia na mesma organização, mas o pipeline do mapa não o incorporou.

Encontramos a escala do erro ao gerar um histograma da nossa própria coluna SSID. Levou minutos. Todos os dias, estávamos publicando 146.526 linhas de evidência contra a nossa apresentação.

______

## O que mudamos

A correção está implementada no modelo de dados e na interface do Flock Finder:

- **Evidência por registro:** `ssid_confirmed`, `oui_high`, `oui_mfr` ou `identified_other`.
- **Níveis OUI:** os prefixos se dividem entre alta confiança observada em campo e níveis compartilhados de fabricantes contratados.
- **Exclusão de outros equipamentos conhecidos:** ClickShare, SmartGate, WiFi Direct, hotspots Android, Audi HUD, MAX-PRINTER e SSIDs de saída de detectores ficam fora do mapa e do título por padrão.
- **Incerteza visível:** cores dos pinos, pop-ups, contagens e filtros mostram a classe de evidência.
- **Sinalização de mercado:** registros fora do mercado principal dos EUA recebem `out_of_market: true` e continuam disponíveis para revisão.
- **Título detalhado:** 3.502 confirmados por SSID, 73.691 suspeitos por OUI de nível alto, 8.223 suspeitos por OUI de fabricantes contratados e 61.110 identificados como outros.

O número corrigido e útil para ação é **85.416**, e ainda inclui 81.914 correspondências OUI sem confirmação. É uma contabilidade defensável do que passou pelas regras atuais, não um inventário verificado de câmeras.

`identified_other` também é um classificador operacional, não um oráculo. ClickShare conta com documentação primária sólida sobre seu SSID padrão, enquanto um padrão amplo como `DIRECT-` descreve uma convenção WiFi Direct usada por muitos tipos de produtos. Publicar a regra de correspondência e o campo `blocked_reason` permite que pesquisadores auditem essas exclusões e as revisem quando houver evidências melhores.

### A resposta de longo prazo é o fingerprinting de firmware

A classificação de OUI limita danos, mas não torna um prefixo compartilhado de fabricante específico de um produto. O caminho mais forte é a estrutura ordenada dos elementos de informação nas solicitações de sondagem 802.11. O trabalho upstream documenta esta assinatura TLV:

```text
2,12,127,221:506f9a16030103,45,191,221:0050f208000000
```

Essa sequência descreve o comportamento de uma pilha de firmware específica, não a propriedade de um bloco MAC. Fingerprinting de solicitações de sondagem é uma técnica estabelecida de identificação de dispositivos. [Pesquisas publicadas sobre fingerprinting da camada MAC 802.11](https://doi.org/10.1155/2017/6235484) mostram que elementos de informação das solicitações podem continuar identificando dispositivos mesmo quando os endereços MAC mudam. Também aborda o problema relatado em [flock-you issue #43](https://github.com/colonelpanichacks/flock-you/issues/43): `Flock Camera net.` aparece em endereços MAC locais sequenciais nas bandas de 2,4 e 5 GHz.

A assinatura ainda precisa de validação de campo independente em diferentes equipamentos e versões de firmware, e capturas malformadas exigem análise defensiva. Ainda assim, esse é o rumo certo. A randomização de MAC torna a correspondência baseada só em OUI uma saída sem futuro.

______

## Por que isso importa além de um repositório

As pessoas usam mapas de vigilância para decidir onde dirigir, estacionar, denunciar, pesquisar e se organizar. Um pino falso desvia a atenção. Dezenas de milhares podem desacreditar observações corretas próximas.

Também existe uma assimetria de credibilidade. Um fornecedor ou crítico precisa de um único pino ClickShare comprovadamente falso para contestar todo o conjunto de dados. Nós fornecemos 50.278. Jornalistas e grupos de defesa repetem um título simples mais rápido do que uma correção posterior consegue alcançá-los.

O trabalho de transparência de código aberto ganha confiança com métodos inspecionáveis e incerteza visível. Publicar os dados brutos ajudou a expor nosso erro, mas o acesso aos dados não desculpa uma interface que exagera a conclusão. A correção deve aparecer onde o leitor encontra a afirmação: campo, filtro, pino, legenda e título.

### Um pedido a todos os mapas Flock e ALPR

Outros projetos de mapeamento Flock e ALPR também deveriam auditar seus conjuntos de dados. É um convite para comparar métodos, não uma acusação de que todos os mapas herdaram nosso erro.

O [WiGLE](https://www.wigle.net/stats/) é o maior conjunto público de observações WiFi pesquisável globalmente que conhecemos. Esse alcance tornou o Flock Finder atraente: uma API poderia converter uma lista de assinaturas pesquisada em campo em um mapa mundial. Também tornou o erro grande o bastante para medir. Uma base global retorna todos os produtos sem relação que compartilham o espaço de endereços de um fornecedor de rádio, não apenas o produto que motivou a busca.

Outros mapas usam evidências diferentes. Alguns dependem de fotos e observações voluntárias em campo. Outros importam etiquetas de vigilância do OpenStreetMap, registros públicos, divulgações de fornecedores ou dados de outro projeto comunitário. Seus totais não são diretamente comparáveis aos resultados do nosso WiGLE, e nossa taxa de 2,4% confirmada por SSID não deve ser projetada em um conjunto verificado em campo. O risco comum é uma classificação de um projeto chegar aos dados de origem de outro e parecer confirmação independente.

Todo mapa público deve responder a uma auditoria breve:

1. **O que um pino significa?** Um dispositivo fotografado, registro governamental, correspondência OUI, denúncia de usuário ou importação de outro mapa?
2. **Quantos registros têm evidência direta do produto?** Publique a contagem por classe de evidência, não um total agregado de câmeras.
3. **Quais fontes são independentes?** Acompanhe a origem das importações para não contar a mesma observação como várias confirmações.
4. **O que contradiz a classificação?** Gere tabelas de frequência de SSIDs, fornecedores, países, etiquetas de colaboradores e outros campos categóricos.
5. **Como a incerteza e as disputas são mostradas?** Coloque confiança e status de correção nos pinos, filtros, exportações e títulos.
6. **Outro pesquisador consegue reproduzir a contagem?** Publique a consulta, o snapshot de origem, as regras de classificação e a data.

Esta auditoria não reduz o problema Flock. Uma rede de câmeras ALPR ainda pode registrar deslocamentos, viabilizar pesquisas entre jurisdições e afetar pessoas que nunca consentiram com a coleta. Contagens precisas tornam essa crítica mais difícil de descartar. Se vamos contestar sistemas de vigilância, nossos mapas precisam distinguir o que observamos, inferimos e confirmamos.

Cometemos um erro bem informado. Os prefixos vieram de pesquisa de campo legítima, o pipeline era reproduzível e as ressalvas existiam. Ainda assim, a inferência excedeu as evidências. Boas intenções e bons dados de entrada não eliminam a obrigação de testar os resultados de um sistema em escala.

______

## Reproduza a auditoria

Faça checkout do commit `5551829` e execute o código a seguir na raiz do repositório. Ele usa apenas a biblioteca padrão do Python e imprime o total, a geografia, SSIDs comuns e famílias selecionadas de dispositivos nomeados.

```bash
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder
git checkout 5551829

python3 - <<'PY'
import csv
from collections import Counter

with open("data/flock_cameras.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

ssids = Counter((row["ssid"] or "").strip() for row in rows)
countries = Counter((row["country"] or "").strip() for row in rows)

families = {
    "clickshare": lambda s: "clickshare" in s.lower(),
    "smartgate": lambda s: s.lower().startswith("smartgate_"),
    "direct": lambda s: s.lower().startswith("direct-"),
    "androidap": lambda s: s.lower().startswith("androidap"),
    "detector_output": lambda s: s.lower().startswith("flock alpr ["),
}

print("linhas", len(rows))
print("EUA", countries["US"])
print("fora dos EUA", sum(countries.values()) - countries["US"] - countries[""])
print("país ausente", countries[""])
print("SSIDs mais frequentes", ssids.most_common(20))
for name, matches in families.items():
    print(name, sum(matches(ssid) for ssid in ssids.elements()))
PY
```

Para usar a entrada histórica exata, use o CSV daquele commit em vez de um conjunto atual gerado. Depois da auditoria, o projeto deixou de versionar o CSV grande, o GeoJSON e os arquivos por OUI, pois cada varredura reescrevia centenas de megabytes e aumentava muito o repositório. Os dados gerados atuais são restaurados e publicados na versão contínua [`data-latest`](https://github.com/simeononsecurity/flock-finder/releases/tag/data-latest). O pequeno resumo `scan_stats.json` continua no Git. A ausência de um arquivo gerado no branch atual não quer dizer que os dados históricos foram apagados ou que a contagem virou zero.

______

## A lição

**Uma heurística marcada como «suspected» nos metadados, mas desenhada como um pino confiante no mapa, é uma afirmação.** O rótulo precisa estar no modelo de dados e na visualização, não apenas na documentação.


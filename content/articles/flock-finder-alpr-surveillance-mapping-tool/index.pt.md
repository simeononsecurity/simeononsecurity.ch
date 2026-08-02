---
title: "Flock Finder: Mapeie Câmeras ALPR do Flock Safety"
date: 2026-07-22
toc: true
draft: false
description: "O Flock Finder é uma ferramenta de código aberto que mapeia mais de 40.000 câmeras ALPR do Flock Safety em todo o mundo usando dados WiFi do WiGLE e impressão digital OUI. Saiba como funciona, suas limitações e as ferramentas de hardware para detecção em tempo real."
genre: ["Tecnologia de Privacidade", "Contra-Vigilância", "Projetos de Código Aberto", "Direitos Digitais", "Segurança de Rede", "Ferramentas de Privacidade", "Hacking de Hardware", "Pesquisa de Segurança"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Leitor de Placa", "Impressão Digital OUI", "WiGLE", "Vigilância WiFi", "Contra-Vigilância", "STS Collective", "FlockYou", "ESP32", "Ferramentas de Privacidade", "NitekryDPaul", "DeFlockJoplin", "Detecção ALPR", "Segurança de Código Aberto", "Mapeamento de Vigilância", "Vigilância em Massa", "WiFi OUI", "Proteção de Privacidade", "Endereço MAC", "Modo Promíscuo", "802.11", "Detecção em Tempo Real", "Wardriving", "Direitos Digitais", "Liberdades Civis", "Consciência de Vigilância", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "Um mapa interativo exibindo marcadores coloridos indicando localizações de câmeras ALPR do Flock Safety, com sinais WiFi abstratos emanando dos marcadores sobre um fundo escuro."
coverCaption: "O Flock Finder mapeia mais de 40.000 câmeras ALPR suspeitas do Flock Safety usando dados WiFi do WiGLE e impressão digital OUI."
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**Uma ferramenta de conscientização de vigilância de código aberto que mapeia câmeras ALPR do Flock Safety usando dados WiFi coletivos.**

## O que é o Flock Finder?

O **[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** é um projeto de código aberto que mapeia **câmeras ALPR (Leitores Automáticos de Placas de Veículos) do Flock Safety** nos Estados Unidos e em outros 108 países. Ele combina **31 prefixos OUI (Identificadores Únicos Organizacionais) WiFi conhecidos do Flock Safety** com o **banco de dados WiFi coletivo WiGLE** para identificar e plotar localizações suspeitas de câmeras em um mapa interativo.

O projeto está em **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**, é atualizado automaticamente diariamente via GitHub Actions e, em julho de 2026, mapeou **mais de 40.000 câmeras suspeitas** em 964 regiões ao redor do mundo.

| Métrica | Valor |
|---------|-------|
| **Câmeras Mapeadas** | 40.026+ |
| **Prefixos OUI Conhecidos** | 31 |
| **Países Cobertos** | 109 |
| **Regiões Cobertas** | 964 |
| **Retenção de Dados** | 730 dias (2 anos) |
| **Frequência de Atualização Automática** | Diária |

*Esta é uma ferramenta de conscientização geral, não um inventário definitivo. Leia a seção de limitações antes de tirar conclusões dos dados.*

Para contexto sobre por que a vigilância ALPR do Flock Safety importa para a privacidade, leia **[Vigilância com Câmeras Flock Safety: Prevalência, Preocupações com Privacidade e Estratégias de Proteção](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

______

## Como Funciona: Impressão Digital OUI via WiGLE

### O Insight Central

As câmeras do Flock Safety contêm **transceivers WiFi** que periodicamente acordam do modo de espera para enviar dados de placas capturadas para a nuvem. Durante essas breves janelas ativas, a câmera transmite quadros WiFi que contêm seu **endereço MAC** — e os primeiros três bytes de cada endereço MAC identificam o fabricante. Este é o **OUI (Identificador Único Organizacional)**.

O pesquisador de segurança **@NitekryDPaul** descobriu **30 prefixos OUI** consistentemente associados ao hardware das câmeras do Flock Safety por meio de **análise de modo promíscuo a 2,4 GHz**. Um 31º prefixo (`82:6B:F2`) foi contribuído por **Michael / DeFlockJoplin** durante testes de campo em Joplin, MO.

O Flock Finder pega esses 31 OUIs, consulta o WiGLE por quaisquer redes WiFi registradas que correspondam a esses prefixos e plota os resultados em um mapa.

### Os 31 Prefixos OUI Conhecidos do Flock Safety

| # | Prefixo OUI | Fonte | # | Prefixo OUI | Fonte |
|---|-------------|-------|---|-------------|-------|
| 1 | **70:C9:4E** | @NitekryDPaul | 17 | **D0:39:57** | @NitekryDPaul |
| 2 | **3C:91:80** | @NitekryDPaul | 18 | **E8:D0:FC** | @NitekryDPaul |
| 3 | **D8:F3:BC** | @NitekryDPaul | 19 | **E0:4F:43** | @NitekryDPaul |
| 4 | **80:30:49** | @NitekryDPaul | 20 | **B8:1E:A4** | @NitekryDPaul |
| 5 | **B8:35:32** | @NitekryDPaul | 21 | **70:08:94** | @NitekryDPaul |
| 6 | **14:5A:FC** | @NitekryDPaul | 22 | **58:8E:81** | @NitekryDPaul |
| 7 | **74:4C:A1** | @NitekryDPaul | 23 | **EC:1B:BD** | @NitekryDPaul |
| 8 | **08:3A:88** | @NitekryDPaul | 24 | **3C:71:BF** | @NitekryDPaul |
| 9 | **9C:2F:9D** | @NitekryDPaul | 25 | **58:00:E3** | @NitekryDPaul |
| 10 | **C0:35:32** | @NitekryDPaul | 26 | **90:35:EA** | @NitekryDPaul |
| 11 | **94:08:53** | @NitekryDPaul | 27 | **5C:93:A2** | @NitekryDPaul |
| 12 | **E4:AA:EA** | @NitekryDPaul | 28 | **64:6E:69** | @NitekryDPaul |
| 13 | **F4:6A:DD** | @NitekryDPaul | 29 | **48:27:EA** | @NitekryDPaul |
| 14 | **F8:A2:D6** | @NitekryDPaul | 30 | **A4:CF:12** | @NitekryDPaul |
| 15 | **24:B2:B9** | @NitekryDPaul | 31 | **82:6B:F2** | DeFlockJoplin |
| 16 | **00:F4:8D** | @NitekryDPaul | | | |

### A Técnica de Detecção addr1

A descoberta chave de @NitekryDPaul vai além de simplesmente corresponder ao endereço MAC do transmissor. As câmeras Flock passam a maior parte do ciclo de trabalho **dormindo**. Quando um ponto de acesso próximo envia um quadro endereçado *a* uma câmera, o MAC da câmera aparece como **addr1 (o endereço do receptor)** nos quadros 802.11 — mesmo enquanto a câmera não está transmitindo ativamente.

Combinado com a **detecção de solicitação de sondagem curinga** (quadros de gerenciamento 802.11 tipo=0, subtipo=4, SSID vazio), isso produz uma assinatura de detecção muito precisa. Testes de campo em Joplin, MO alcançaram **11 de 12 câmeras detectadas com apenas 2 falsos positivos**.

> ⚠️ **Importante**: O mapa Flock Finder baseado em WiGLE **não** implementa a técnica addr1. O WiGLE é um conjunto de dados histórico, coletado passivamente — registra apenas transmissores, não receptores. Para detecção em tempo real que realmente usa o método de @NitekryDPaul, você precisa de hardware dedicado funcionando em campo.

______

## Usando o Mapa ao Vivo

O mapa interativo está disponível em **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)**. Ele exibe:

- **Marcadores de câmeras agrupados** codificados por cores por prefixo OUI
- **Pesquisa** por cidade, estado ou BSSID
- **Tabela de dados OUI** com contagens de câmeras por prefixo
- **Painel de estatísticas** mostrando total de câmeras, regiões e timestamp da última atualização
- **Página Sobre ALPRs** com danos de privacidade documentados, contexto legal e recursos comunitários

As exportações de dados do mapa também estão disponíveis diretamente:

- `data/flock_cameras.geojson` — GeoJSON para uso no QGIS, Leaflet ou outras ferramentas
- `data/flock_cameras.csv` — formato compatível com planilhas
- `data/scan_stats.json` — estatísticas de varredura e contagens

### Principais Limitações

**Considere o mapa com cautela.** O WiGLE é um conjunto de dados coletivo e atualizado esporadicamente, não um feed ao vivo.

- **As câmeras Flock não transmitem continuamente.** Elas acordam brevemente para enviar dados, então os registros do WiGLE dependem inteiramente de um wardriver estar nas proximidades no momento exato.
- **Os dados podem ter meses ou anos de idade.** Câmeras que foram realocadas ou removidas ainda podem aparecer.
- **A correspondência OUI é uma heurística.** OUIs podem ser compartilhados, reatribuídos ou falsificados. Cada resultado é um dispositivo Flock *suspeito*, não confirmado.
- **A cobertura é desigual.** Áreas metropolitanas densas têm mais dados WiGLE; áreas rurais têm muito menos.

*Use o mapa para desenvolver consciência geral sobre a densidade de vigilância em sua área. Para detecção em tempo real baseada em evidências, veja as opções de hardware abaixo.*

______

## Executando o Flock Finder Você Mesmo

### Pré-requisitos

- Python 3.8+
- Uma conta gratuita no [WiGLE](https://wigle.net/account) com credenciais de API

### Configuração

```bash
# Clonar o repositório
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder

# Instalar dependências
pip install -r requirements.txt

# Configurar suas credenciais de API do WiGLE
cp .env.example .env
# Edite .env com seu Nome e Token de API do WiGLE
```

### Executando o Scanner

```bash
# Varredura completa — todos os 31 prefixos OUI, em todo o mundo
python3 scripts/wigle_query.py

# Teste de OUI único
python3 scripts/wigle_query.py --oui 70:C9:4E

# Somente EUA
python3 scripts/wigle_query.py --country US

# Caixa delimitadora específica (lat1,lon1,lat2,lon2)
python3 scripts/wigle_query.py --bbox 37,-97,39,-94

# Execução a seco — verificar autenticação, sem consultas de API
python3 scripts/wigle_query.py --dry-run
```

### Visualizando o Mapa Localmente

```bash
python3 -m http.server 8080 --directory docs/
# Abra http://localhost:8080 no seu navegador
```

### Atualizações Diárias Automatizadas via GitHub Actions

Faça um fork do repositório e adicione suas credenciais do WiGLE como **segredos do repositório** (`WIGLE_API_NAME` e `WIGLE_API_TOKEN`). O fluxo de trabalho incluído é executado às 6h UTC diariamente e confirma automaticamente arquivos de dados atualizados sempre que novas câmeras são encontradas.

______

## Detecção em Tempo Real: Hardware FlockYou do STS Collective

O mapa WiGLE informa onde as câmeras *foram observadas*. Para detecção em tempo real enquanto você dirige — usando o método real de correspondência OUI de @NitekryDPaul no tráfego WiFi ao vivo — você precisa de hardware dedicado.

O **[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** fabrica detectores portáteis baseados em ESP32 que varrem as assinaturas OUI do Flock e alertam você no momento em que uma assinatura correspondente é detectada.

### Linha de Dispositivos FlockYou

| Dispositivo | Descrição |
|-------------|-----------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | Detector Flock compacto, de bolso. Pré-gravado, plug-and-play. Alertas LED na detecção. |
| **FlockYou Pro — LED + Áudio** | Adiciona alertas de áudio junto com indicadores LED. Nunca perca uma câmera enquanto dirige. |
| **FlockYou Atom VoiceS3R** | Detector com voz e alertas de áudio falados para operação sem as mãos, com os olhos na estrada. |

Todos os dispositivos:
- **Pré-gravados**, prontos para usar na caixa
- Varrem o tráfego WiFi ao vivo para todos os 31 OUIs Flock conhecidos
- Compactos e portáteis — cabem em um porta-copo ou bolso
- Alimentados via USB-C (adaptador de carro, banco de energia ou laptop)

> 💰 **Descontos Exclusivos**: Use o código **FLOCKFINDER** para **20% de desconto** em todos os dispositivos FlockYou do STS Collective — ou use o código **SIMEONONSECURITY** para até 20% de desconto em seu pedido inteiro. [Compre em stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

Para um detalhamento técnico completo desses dispositivos e alternativas DIY, leia o **[Projeto de Detecção Flock-You: Guia Completo de Hardware de Contra-Vigilância e Configuração](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**.

______

## Estrutura do Projeto

```
flock-finder/
├── scripts/
│   └── wigle_query.py        # Pipeline de consulta e dados da API WiGLE
├── data/
│   ├── flock_ouis.csv         # 31 prefixos OUI conhecidos do Flock Safety
│   ├── flock_cameras.geojson  # Localizações das câmeras (GeoJSON)
│   ├── flock_cameras.csv      # Localizações das câmeras (CSV)
│   └── scan_stats.json        # Estatísticas de varredura
├── docs/
│   └── index.html             # Mapa Leaflet interativo
└── .github/workflows/
    └── update-data.yml        # Fluxo de trabalho de atualização diária automática
```

______

## Perguntas Frequentes

### Isso é legal?

Sim. **O Flock Finder usa apenas dados disponíveis publicamente** do banco de dados WiGLE, que agrega dados de levantamento WiFi contribuídos voluntariamente. Nenhum hacking, acesso não autorizado ou sistemas proprietários estão envolvidos. O monitoramento WiFi passivo para assinaturas OUI é legal nos Estados Unidos.

### Toda câmera mapeada é definitivamente uma câmera Flock?

Não. A correspondência OUI é uma **heurística**. Prefixos OUI podem ser compartilhados entre fabricantes, reatribuídos ou falsificados. Cada registro no banco de dados é um dispositivo Flock *suspeito* — não confirmado. Leia a [Política de Dados](https://github.com/simeononsecurity/flock-finder/blob/main/docs/data-policy.md) para detalhes sobre como solicitar uma correção.

### Por que alguns prefixos OUI não mostram câmeras?

A cobertura do WiGLE é desigual. Se nenhum wardriver varreu uma determinada área com esse OUI específico ativo, não haverá registros. *A ausência de dados não significa ausência de câmeras.*

### Quão atuais são os dados?

O fluxo de trabalho do GitHub Actions é executado diariamente e puxa os resultados mais recentes do WiGLE. No entanto, o próprio WiGLE pode ter registros que variam de dias a anos atrás para qualquer local. Verifique o arquivo `scan_stats.json` para o timestamp da varredura mais recente.

### Posso contribuir com meus próprios dados de wardriving?

Sim. Faça upload dos seus dados de wardriving para o [WiGLE](https://wigle.net) — eles automaticamente alimentam a próxima varredura diária do Flock Finder. Você também pode contribuir com prefixos OUI ou melhorias de código via o [Guia de Contribuição](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md).

______

## Comunidade e Projetos Relacionados

O Flock Finder não existe sozinho. Um ecossistema crescente de ferramentas e organizações está trabalhando para documentar e combater a vigilância ALPR:

- **[DeFlock.org](https://deflockjoplin.org/)** — Rastreamento, documentação e defesa de ALPR orientados pela comunidade
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — Verifique se sua placa foi pesquisada no sistema do Flock
- **[FlockHopper](https://flockhopper.com/)** — Planejamento de rotas que evita câmeras ALPR conhecidas
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — Banco de dados da EFF de tecnologias de vigilância usadas por agências de aplicação da lei
- **[NoALPRs.com](https://noalprs.com/)** — Recursos para comunidades que combatem implantações de ALPR
- **[DeFlockJoplin](https://deflockjoplin.org/)** — Firmware de código aberto e pesquisa de campo; contribuiu com o 31º prefixo OUI

______

## Créditos

- **Pesquisa OUI**: @NitekryDPaul — todos os 30 prefixos OUI originais e a estratégia de detecção addr1/modo promíscuo
- **Testes de Campo**: Michael / DeFlockJoplin — 31º prefixo OUI (`82:6B:F2`) e ajuste de sondagem curinga
- **Fonte de Dados**: [WiGLE](https://wigle.net) — banco de dados WiFi/rede celular coletivo
- **Inspirado por**: [DeFlock](https://deflockjoplin.org/) e track-openroaming-passpoint
- **Parceiro de hardware**: [STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — detectores ESP32 FlockYou

______

## Conclusão

O **Flock Finder** dá a qualquer pessoa uma noção visual rápida de quão amplamente as câmeras ALPR do Flock Safety foram implantadas — mais de 40.000 localizações estimadas em 109 países, atualizadas automaticamente todos os dias a partir de dados WiFi coletivos.

É uma **ferramenta de transparência**, não um rastreador ao vivo. Seus dados são históricos, incompletos e probabilísticos. Mas torna a escala da vigilância ALPR visível de uma forma que abstrações e relatórios não conseguem.

Para proteção genuína em tempo real enquanto você se move por áreas vigiadas, combine o mapa com hardware dedicado. Os **[dispositivos FlockYou do STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** implementam o método de detecção de @NitekryDPaul diretamente em um ESP32 e alertam você no momento em que uma assinatura de câmera ao vivo é detectada — disponível em **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** com o código **FLOCKFINDER** ou **SIMEONONSECURITY** para até 20% de desconto.

### Artigos Relacionados

| Artigo | O que cobre |
|--------|-------------|
| **[Vigilância com Câmeras Flock Safety: Privacidade e Proteção](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | O quadro completo: estatísticas de prevalência, questões de liberdades civis, kit de ferramentas da ACLU, estatísticas DeFlock, guia FOIA e estratégias de proteção |
| **[Projeto de Detecção Flock-You: Guia de Hardware de Contra-Vigilância](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Guia técnico completo para detectores Flock baseados em ESP32 — OUI-SPY, M5 Atom Lite, build DIY, configuração de firmware passo a passo |
| **[Como Gravar Dispositivos Rayhunter: Guia Completo](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Detecte IMSI catchers (simuladores de estação base) ao lado de câmeras ALPR para consciência completa de contra-vigilância |
| **[Firmware Personalizado DagShell para Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Transforme um hotspot móvel em uma plataforma de pesquisa de segurança — combina bem com hardware de detecção Flock |
| **[Comparação de Dispositivos Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Compare opções de hardware de detecção nas categorias de ameaças ALPR e vigilância celular |

______

## Referências

1. [Repositório GitHub do Flock Finder](https://github.com/simeononsecurity/flock-finder)
2. [Mapa Interativo do Flock Finder](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — Dispositivos FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — Mapeamento de Redes Sem Fio](https://wigle.net)
5. [DeFlock — Consciência Comunitária sobre ALPR](https://deflockjoplin.org/)
6. [DeFlockJoplin — Firmware de Detecção de Código Aberto](https://deflockjoplin.org/)
7. [Electronic Frontier Foundation — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — Você Está Sendo Rastreado](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)

---
title: "Proteja o Windows contra ataques de canal lateral de execução especulativa"
date: 2020-06-18
toc: true
draft: false
description: "Saiba como proteger seu sistema Windows contra ataques de canal lateral de execução especulativa com script de mitigação e atualizações de firmware da Microsoft"
tags: ["Script de Mitigação do Windows Spectre Meltdown", "Ataques de canal lateral de execução especulativa", "Microsoft", "Intel", "AMD", "ATRAVÉS DA", "BRAÇO", "Android", "cromada", "iOS", "Mac OS", "Injeção de alvo de ramificação", "Desvio de verificação de limites", "Carregamento de Cache de Dados Rogue", "Ignorar loja especulativa", "Amostragem de dados microarquiteturais", "CVEs", "Atualizações de firmware", "Repositório GitHub", "PowerShell"]
---
 https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in
**Script simples para implementar proteções contra vulnerabilidades de canal lateral de execução especulativa em sistemas Windows.**

A Microsoft está ciente de uma nova classe de vulnerabilidades divulgada publicamente chamada de “ataques de canal lateral de execução especulativa” e que afeta muitos processadores modernos, incluindo Intel, AMD, VIA e ARM.

**Observação:** esse problema também afeta outros sistemas operacionais, como Android, Chrome, iOS e macOS. Portanto, aconselhamos os clientes a buscar orientação desses fornecedores.

Lançamos várias atualizações para ajudar a mitigar essas vulnerabilidades. Também tomamos medidas para proteger nossos serviços de nuvem. Consulte as seções a seguir para obter mais detalhes.

Ainda não recebemos nenhuma informação que indique que essas vulnerabilidades foram usadas para atacar clientes. Estamos trabalhando de perto com parceiros do setor, incluindo fabricantes de chips, OEMs de hardware e fornecedores de aplicativos para proteger os clientes. Para obter todas as proteções disponíveis, são necessárias atualizações de firmware (microcódigo) e software. Isso inclui microcódigo de OEMs de dispositivos e, em alguns casos, atualizações de software antivírus.

**Este artigo aborda as seguintes vulnerabilidades:**
- CVE-2017-5715 – "Injeção de alvo de ramificação"
- CVE-2017-5753 – "Bypass de verificação de limites"
- CVE-2017-5754 – "Carga de cache de dados não autorizados"
- CVE-2018-3639 – "Desvio de Loja Especulativa"
- CVE-2018-11091 – “Microarchitectural Data Sampling Uncacheable Memory (MDSUM)”
- CVE-2018-12126 – “Microarchitectural Store Buffer Data Sampling (MSBDS)”
- CVE-2018-12127 – “Microarchitectural Fill Buffer Data Sampling (MFBDS)”
- CVE-2018-12130 – “Microarchitectural Load Port Data Sampling (MLPDS)”

** ATUALIZADO EM 6 DE AGOSTO DE 2019 ** Em 6 de agosto de 2019, a Intel divulgou detalhes sobre uma vulnerabilidade de divulgação de informações do kernel do Windows. Esta vulnerabilidade é uma variante da vulnerabilidade do canal lateral de execução especulativa Spectre Variant 1 e foi atribuída como CVE-2019-1125.

** ATUALIZADO EM 12 DE NOVEMBRO DE 2019 ** Em 12 de novembro de 2019, a Intel publicou um comunicado técnico sobre a vulnerabilidade de interrupção assíncrona de transações Intel® Transactional Synchronization Extensions (Intel® TSX) atribuída a CVE-2019-11135. A Microsoft lançou atualizações para ajudar a atenuar essa vulnerabilidade e as proteções do sistema operacional são habilitadas por padrão para Windows Client OS Editions.

## Ações Recomendadas
Os clientes devem tomar as seguintes ações para ajudar a se proteger contra as vulnerabilidades:

- Aplique todas as atualizações disponíveis do sistema operacional Windows, incluindo as atualizações mensais de segurança do Windows.
- Aplique a atualização de firmware aplicável (microcódigo) fornecida pelo fabricante do dispositivo.
- Avalie o risco para o seu ambiente com base nas informações fornecidas nos Comunicados de Segurança da Microsoft: ADV180002, ADV180012, ADV190013 e nas informações fornecidas neste artigo da Base de Conhecimento.
- Tome as medidas necessárias usando os avisos e as informações da chave do registro fornecidas neste artigo da Base de conhecimento.

## Baixe os arquivos necessários:

Baixe os arquivos necessários do[GitHub Repository](https://github.com/simeononsecurity/Windows-Spectre-Meltdown-Mitigation-Script)

## Como executar o script:

**O script pode ser iniciado a partir do download extraído do GitHub assim:**
```
.\sos-spectre-meltdown-mitigations.ps1
```

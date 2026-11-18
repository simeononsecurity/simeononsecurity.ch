---
title: "Vulnerabilidades nas câmeras Flock Safety: mais de 50 falhas encontradas"
date: 2026-05-24
lastmod: 2026-11-15
toc: true
draft: false
description: "A pesquisa sobre vulnerabilidades nas câmeras Flock Safety analisa credenciais expostas, proteções frágeis, acesso físico e limites da divulgação."
genre: ["Pesquisa de segurança", "Análise de vulnerabilidades", "Tecnologia de vigilância", "Cibersegurança", "Proteção da privacidade", "Segurança de IoT", "Segurança física", "Segurança de rede", "Infraestrutura crítica", "Tecnologia governamental"]
tags: ["Vulnerabilidades Flock Safety", "Segurança ALPR", "Invasão de câmeras", "Falhas de segurança de IoT", "Senhas embutidas no código", "Vulnerabilidades do Android Things", "Exploração por acesso físico", "Segurança de rede", "Falhas de criptografia", "Violações de privacidade de dados", "Divulgações de CVE", "Pesquisa de segurança", "Pesquisa da GainSec", "Investigação de Ben Jordan", "Segurança de câmeras de vigilância", "Falhas em tecnologia governamental", "Vulnerabilidades críticas", "Divulgação responsável", "Análise de cibersegurança", "Tecnologia policial", "Segurança pública", "Ponto de acesso sem fio", "Contorno de autenticação", "Credenciais em texto simples", "Vazamento de RF", "Ataque Tempest", "Divulgação de informações", "Acesso a shell root", "Execução remota de código", "Auditoria de segurança", "Avaliação de vulnerabilidades", "Risco à segurança nacional", "Investigação do Senado", "Programa de recompensas por bugs", "Vulnerabilidade de dia zero", "Desenvolvimento de exploits", "Teste de intrusão", "White paper de segurança", "Cobertura da 404 Media", "Pesquisa independente", "Segurança de hardware", "Análise de firmware", "Exploração de sistemas"]
cover: "/img/cover/flock-safety-camera-security-vulnerabilities-research-2026.webp"
coverAlt: "Uma câmera de vigilância avançada aparece com destaques azuis e verdes sobre um fundo escuro. Formas e linhas abstratas ao redor representam vulnerabilidades de segurança digital."
coverCaption: "Falhas críticas expõem mais de 80 mil câmeras de vigilância a acessos não autorizados"
canonical: "https://simeononsecurity.com/articles/flock-safety-camera-security-vulnerabilities-research-2026/"
---

**Mais de 50 vulnerabilidades críticas de segurança expõem a maior rede privada de vigilância do país**

## Introdução: uma crise de segurança nacional

No fim de 2024 e ao longo de 2025, pesquisadores independentes de segurança descobriram o que pode ser **a falha de segurança mais significativa da história da tecnologia de vigilância policial dos Estados Unidos**. Mais de **50 vulnerabilidades críticas** foram encontradas nos sistemas de câmeras da Flock Safety, as mesmas câmeras que fotografam e rastreiam mais de **150 milhões de veículos por dia** em mais de **80.000 instalações** pelo país.

Este artigo apresenta uma análise técnica abrangente dessas vulnerabilidades, com base em:

- **O artigo técnico formal da GainSec**, “Examining the Security Posture of an Anti-Crime Ecosystem” (51 constatações, 22 CVEs atribuídos e 8 pendentes)
- **A reportagem investigativa de Ben Jordan** e seus testes práticos de segurança
- **A cobertura da 404 Media** sobre transmissões de câmeras expostas publicamente
- **As respostas oficiais** da Flock Safety e de senadores dos Estados Unidos
- **As divulgações publicadas no National Vulnerability Database (NVD)**
- **A imagem do sistema de arquivos publicada em setembro de 2026** pela organização Distributed Denial of Secrets, com análise técnica linha por linha de Micah Lee e uma investigação conjunta da WIRED e da 404 Media

Para entender **por que essas câmeras existem** e suas **implicações para a privacidade**, consulte nosso artigo: **[Vigilância por câmeras Flock Safety: prevalência, preocupações com a privacidade e estratégias de proteção](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**

Para saber **como detectar essas câmeras**, consulte: **[Projeto de detecção Flock-You: guia de hardware contra vigilância](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**

______

## A dimensão do problema

### Escala da infraestrutura vulnerável

Em maio de 2026:

- **Mais de 80.000 câmeras Flock Safety** instaladas nos Estados Unidos
- **Mais de 5.000 cidades e municípios** usam os serviços da Flock
- **Mais de 3.500 órgãos policiais** têm acesso ao sistema
- **Mais de 22.000 usuários policiais** acessam os bancos de dados
- **Bilhões de pontos de dados** armazenados em bancos pesquisáveis

### Linha do tempo das vulnerabilidades

- **Final de 2024**: o pesquisador de segurança Jon “GainSec” Gaines descobre as primeiras vulnerabilidades
- **Fevereiro de 2025**: começa a divulgação responsável à Flock Safety
- **Abril de 2025**: são publicados os primeiros CVEs
- **Novembro de 2025**: artigo técnico formal é publicado com 51 constatações
- **Dezembro de 2025**: Ben Jordan demonstra vulnerabilidades em vídeo
- **Janeiro de 2026**: a 404 Media encontra mais de 60 transmissões de câmeras acessíveis publicamente
- **Fevereiro de 2026**: senadores dos EUA pedem uma investigação da FTC
- **Maio de 2026**: o processo de divulgação continua

### Categorias de vulnerabilidades

As mais de 50 vulnerabilidades abrangem várias categorias:

1. **Autenticação e autorização** (senhas embutidas no código e ausência de MFA)
2. **Criptografia** (dados sem criptografia em repouso e em trânsito)
3. **Segurança de rede** (pontos de acesso Wi-Fi expostos e credenciais em texto simples)
4. **Segurança física** (exploração por pressionamento de botão e portas USB expostas)
5. **Privacidade de dados** (coleta não autorizada e retenção prolongada)
6. **Projeto do sistema** (software desatualizado e controles de acesso inadequados)
7. **Divulgação de informações** (chaves de API expostas e transmissões públicas de câmeras)

______

## A imagem do sistema de arquivos de setembro de 2026

**Em setembro de 2026, a organização sem fins lucrativos de transparência Distributed Denial of Secrets publicou imagens completas do sistema de arquivos extraídas de uma câmera Flock em serviço.** Um coletivo que se identifica como **stegan0gram** desparafusou o equipamento do poste, copiou o armazenamento interno e publicou as imagens. **A 404 Media** e a **WIRED** fizeram uma investigação conjunta, e o pesquisador de segurança **Micah Lee** publicou uma análise técnica do conteúdo.

Todas as constatações anteriores deste artigo vieram de um equipamento de laboratório de um pesquisador ou de uma unidade comprada. Este conjunto de dados vem de uma câmera em serviço municipal ativo, o que o torna a evidência mais sólida publicada até hoje.

*A câmera não foi invadida pela rede. Ela foi removida fisicamente.*

### O que a imagem contém

A publicação inclui imagens de três partições, cada uma com uma parte diferente da história.

| Partição | Tamanho | Relevância |
|-----------|------|----------------|
| **system** | 1,5 GB | Imagem do sistema Android com **19 aplicativos desenvolvidos pela Flock**, entre eles `flock-sambuca`, `flock-collins` e `flock-phone-home` |
| **persist** | 32 MB | Credenciais do dispositivo em `flock/auth0/auth0_cred`, numa **partição sem criptografia, projetada para sobreviver a uma restauração de fábrica** |
| **media** | 18 GB | Registros e imagens num contêiner cuja **chave de descriptografia fica na mesma partição** |

### O problema das credenciais, confirmado

A imagem esclarece se as credenciais embutidas no código são teóricas ou estão implantadas. Elas estão implantadas.

**Uma chave de API que permite acesso ao backend da Flock aparece embutida nos binários dos aplicativos.** O valor fica numa classe chamada `CameraSettings`, dentro de `com.flocksafety.android.common.lib`. A Flock inclui a biblioteca compartilhada nos 19 aplicativos, então a chave é enviada dentro de todos eles. O aplicativo `flock-sambuca` a usa durante o provisionamento.

**O fluxo de autenticação funciona assim:**

1. Cada câmera solicita credenciais a um servidor da Flock e se identifica pelo **endereço MAC**.
2. O serviço de autenticação **Okta Auth0** da Flock retorna um `FlockAuth0Token` de curta duração.
3. A câmera armazena as credenciais recebidas **em texto simples**.

O ID de cliente e o segredo de cliente do Auth0 ficam na **partição `/persist` sem criptografia**, num arquivo projetado para sobreviver à restauração de fábrica. Um invasor recupera primeiro a partição persist, pois nada a protege.

A [Vulnerabilidade crítica nº 4](#critical-vulnerability-4-hardcoded-credentials-throughout-system) aborda o padrão mais amplo de segredos embutidos na plataforma.

### A chave de criptografia enviada junto com o cadeado

A Flock descreve as câmeras como protegidas por **criptografia no dispositivo**. A imagem revela como isso funciona na prática.

A partição media de 18 GB fica dentro de um contêiner criptografado. A chave de descriptografia fica na mesma partição, num arquivo cujo nome termina em `.key`. O coletivo stegan0gram recuperou a chave, desbloqueou o contêiner e leu o conteúdo. **As imagens estão criptografadas no mesmo sentido em que uma caixa trancada está protegida quando a chave fica presa com fita na tampa.**

Os registros recuperados também revelaram a posição da própria câmera. As coordenadas GPS aparecem **155 vezes** nos registros, agrupadas num raio de aproximadamente 100 metros, uma variação normal para um receptor preso a um poste. As coordenadas apontam para **Wauwatosa, Wisconsin**, um subúrbio de Milwaukee, onde a câmera estava instalada na N Mayfair Road. Micah Lee comparou os registros com o Google Street View e identificou a unidade específica pelo número de série e pelo endereço MAC.

*A criptografia em repouso não protege nada quando a chave fica armazenada junto com o texto cifrado.*

### O que a Flock disse

A resposta da Flock repetiu sua posição sobre as constatações anteriores da GainSec. Um porta-voz declarou:

> “A Flock leva a segurança a sério e mantém uma Política pública de Divulgação de Vulnerabilidades para que pesquisadores de segurança nos relatem possíveis vulnerabilidades diretamente. Não recebemos nenhum relato por esse processo e, com base nas informações limitadas fornecidas, não temos detalhes suficientes para avaliar as alegações feitas.”

É difícil conciliar essa resposta com a linha do tempo. As vulnerabilidades no sistema operacional da câmera receberam correções públicas em **2018 e 2021**, e os padrões de armazenamento de credenciais e gerenciamento de chaves já eram conhecidos muito antes do envio da câmera. **Revisar uma década de histórico público de vulnerabilidades não exige um relato externo.**

A Flock também caracterizou como ilegal a remoção e análise da câmera, o que é verdade segundo a legislação atual. Ainda assim, as constatações de segurança se sustentam por si só, independentemente de como o equipamento foi obtido.

### Por que isso importa mais do que a pesquisa anterior

O artigo técnico da GainSec documentou 51 constatações em dispositivos obtidos legalmente. A Flock contestou a gravidade e alegou que o acesso exigia proximidade física.

Esta imagem elimina essas ressalvas. A configuração padrão de uma câmera de produção, sem alterações feitas por seus operadores, contém credenciais de infraestrutura em texto simples, chaves armazenadas ao lado dos dados que deveriam proteger e um sistema operacional sem oito anos de correções de segurança. **Nada disso exigiu uma exploração. Bastou uma chave de boca.**

______

## A frota de dispositivos

A Flock vende uma linha de produtos, não uma única câmera, e as propriedades de segurança variam conforme o dispositivo. As especificações abaixo vêm das análises da GainSec e da análise de firmware compilada pela comunidade de detecção na **[WiFi Mothership](https://wifimothership.com/flock)**.

| Dispositivo | Função | Plataforma | Sistema operacional |
|--------|------|----------|-----|
| **Falcon** | Câmera ALPR alimentada por energia solar | Qualcomm MSM8953 (Snapdragon 625) / OpenQ 624A SoM | Android 8.1 |
| **Sparrow** | Câmera ALPR com alimentação por fio | Igual à Falcon | Android 8.1 |
| **Raven** | Detecção de disparos e sons de emergência | ESP32-WROOM-32D com DSP Syntiant NDP120-B0 | FreeRTOS / ESP-IDF |
| **Bravo** | Caixa de computação de borda com IA | Qualcomm QCS6490 / TurboX QCS6490-U8B | **Android 13, kernel 5.4.180** |
| **Picard** | Caixa de computação antiga | Descontinuada em favor da Bravo | |
| **Condor** | Câmera PTZ | Não documentada por completo | |
| **Alpha** | Drone autônomo | Projetado pela Flock, em conformidade com a NDAA | Piloto automático proprietário |
| **Aerodome M350** | Drone antigo | DJI Matrice M350 / M300 RTK | Firmware DJI |
| **LPR Trailer (ATS-5)** | Plataforma ALPR móvel | Chassi da All Traffic Solutions com uma câmera Flock | Igual à Falcon |
| **Wing** | Ponte de software para câmeras de terceiros | Nenhuma, encapsula câmeras IP existentes | |

*A diferença entre gerações é o primeiro ponto a observar. A caixa de computação executa Android 13, enquanto as câmeras que atende usam Android 8.1, lançado em 2017.*

**A Falcon é o dispositivo que merece atenção.** Ela executa a carga de trabalho ALPR, continua no Android 8.1 e armazena dados em **eMMC de 32 GB sem criptografia**. Foi nesse mesmo eMMC que ficaram os arquivos de mídia e os registros recuperados pelo coletivo stegan0gram. A Sparrow usa a mesma plataforma, mas recebe energia por fio.

**A Bravo representa o caso oposto.** Uma caixa de computação moderna com Android 13 e inferência de IA para as transmissões das câmeras mostra que a empresa está disposta a enviar software atual quando decide fazê-lo.

## Identificadores CVE verificados

Quinze CVEs foram atribuídos às famílias Falcon, Sparrow, Raven e Bravo. Cada identificador abaixo foi conferido no **registro do CVE.org** em setembro de 2026, em vez de ser citado de uma fonte secundária.

### Dispositivos de detecção de disparos e áudio

| CVE | Constatação | CVSS |
|-----|---------|------|
| **CVE-2025-47818** | Senha codificada para uma conexão | 2.2 |
| **CVE-2025-47819** | Interface de depuração no chip com controle de acesso inadequado | 6.4 |
| **CVE-2025-47820** | Armazenamento de código em texto simples | 2.0 |
| **CVE-2025-47821** | Senha codificada para um sistema | 2.2 |

Os quatro afetam dispositivos de detecção de disparos **anteriores à versão 1.3**.

### Leitores de placas

| CVE | Constatação | CVSS |
|-----|---------|------|
| **CVE-2025-47822** | Interface de depuração no chip com controle de acesso inadequado | 6.4 |
| **CVE-2025-47823** | Senha codificada para um sistema | 2.2 |
| **CVE-2025-47824** | Armazenamento de código em texto simples | 2.0 |

Esses três afetam o firmware dos leitores de placas **até a versão 2.2**.

### Falhas nos aplicativos de toda a frota

| CVE | Constatação | CVSS |
|-----|---------|------|
| **CVE-2025-59403** | O aplicativo Collins expõe endpoints administrativos na **porta 8080 sem autenticação**: `/reboot`, `/logs`, `/crashpack` e `/adb/enable`. O último inicia o ADB por TCP sem confirmação de depuração, dando a um invasor na mesma rede acesso a um shell | **9.8 CRÍTICO** |
| **CVE-2025-59407** | O aplicativo DetectionProcessing inclui um keystore Java e sua **senha codificada**, e o keystore contém uma chave privada | **9.8 CRÍTICO** |
| **CVE-2025-59405** | O aplicativo Peripheral contém uma chave de API do DataDog em texto simples | 7.5 |
| **CVE-2025-59409** | O firmware de produção Falcon e Sparrow é enviado com **credenciais de Wi-Fi de desenvolvimento em texto simples** | 7.5 |
| **CVE-2025-59406** | O aplicativo Pisco incorpora um **segredo de cliente do Auth0** em texto simples | 6.2 |

### Caixa de computação Bravo

| CVE | Constatação | CVSS |
|-----|---------|------|
| **CVE-2025-59402** | Aceita o carregador Firehose padrão Thundercomm TurboX 6490, permitindo gravar firmware e descarregar partições | 5.4 |
| **CVE-2025-59404** | É enviado com o bootloader desbloqueado, contornando o Android Verified Boot | 7.5 |
| **CVE-2025-59408** | É enviado com o Secure Boot desativado | 7.3 |

**Quatro dessas falhas têm vetor de ataque pela rede e pontuação de 7.5 ou superior, o que significa que nenhuma exige acesso físico.** O CVE-2025-59403 identifica o caminho de API sem autenticação e inclui a chamada `/adb/enable`, da qual a [Vulnerabilidade crítica nº 1](#critical-vulnerability-1-button-press-wireless-access-point) depende para alcançar um shell raiz.

*Os registros CVE importam também por outro motivo. Eles confirmam o problema das chaves em texto simples em registros independentes, não apenas nos relatórios dos pesquisadores, e a própria página de alertas de segurança da Flock aparece como referência nas entradas do Raven e do LPR.*

______

## Vulnerabilidade crítica nº 1: ponto de acesso sem fio ativado por botão {#critical-vulnerability-1-button-press-wireless-access-point}

### CVE-2025-59403

**Gravidade**: CRÍTICA (CVSS 9.8)

### A exploração

A vulnerabilidade mais alarmante permite que **qualquer pessoa com acesso físico** a uma câmera Flock Safety assuma o controle total em menos de 60 segundos:

**Etapa 1**: pressione o botão na parte traseira da câmera Falcon/Sparrow **três vezes**
**Etapa 2**: o dispositivo cria um ponto de acesso Wi-Fi aberto
**Etapa 3**: conecte-se à rede Wi-Fi (a senha codificada está documentada no artigo técnico GainSec)
**Etapa 4**: envie o comando para ativar o ADB (Android Debug Bridge)
**Etapa 5**: conecte-se pelo ADB e obtenha acesso a um shell raiz

### Detalhes técnicos

```
Dispositivo: câmera ALPR Flock Safety Falcon/Sparrow
Hardware: Android Things 8.0/8.1 (suporte encerrado em 2021)
Vetor de ataque: sequência de pressões físicas do botão
Autenticação: senha WiFi codificada (igual em todos os dispositivos)
Impacto: comprometimento total do dispositivo, exfiltração de dados e instalação de malware
```

### O que isso permite

Depois de obter acesso ao shell, um invasor pode:

- **Extrair todas as imagens armazenadas** (incluindo pessoas, não apenas veículos)
- **Alterar ou apagar evidências** armazenadas no dispositivo
- **Instalar malware persistente** (que sobrevive a reinicializações)
- **Clonar a identidade do dispositivo** para falsificação
- **Interceptar e modificar** transmissões de vídeo
- **Usar o dispositivo como cliente de botnet** em ataques DDoS
- **Capturar credenciais de Wi-Fi** de dispositivos próximos (ataques de honeypot)
- **Desativar a câmera** ou causar negação de serviço

### Demonstração

O pesquisador de segurança Ben Jordan demonstrou essa exploração no YouTube, mostrando:

- Conexão ao ponto de acesso Wi-Fi em **menos de 30 segundos**
- Acesso ao shell raiz em **menos de 60 segundos no total**
- Acesso completo ao sistema de arquivos, imagens armazenadas e memória do sistema
- Capacidade de instalar aplicativos Android arbitrários

**Trecho da demonstração**:

> “A senha desse ponto de acesso é [REDACTED] em letras minúsculas. Todas as câmeras que testamos têm a mesma senha codificada. Depois, basta enviar um comando para ativar o ADB... em menos de 30 segundos, você consegue abrir um shell no dispositivo e obter acesso total.”

### Resposta do fornecedor

A Flock Safety afirmou inicialmente que a vulnerabilidade afetava apenas **dispositivos não conectados à nuvem**, comparando-os a **“um iPhone roubado de um caminhão antes de ser conectado”**.

*Essa alegação foi refutada.* Os pesquisadores reproduziram a vulnerabilidade **em dispositivos conectados à nuvem**, em vários modelos de câmera com **a mesma vulnerabilidade** e em dispositivos obtidos de **fontes diferentes**. Todos apresentaram a falha.

______

## Vulnerabilidade crítica nº 2: sistema operacional Android desatualizado

### CVE-2025-47822 até CVE-2025-47824

**Gravidade**: MÉDIA a BAIXA (CVSS 6.4, 2.2 e 2.0)

### O problema

As câmeras Flock Safety executam **Android Things 8.0 ou 8.1**, que:

- Foi **descontinuado pelo Google em 2021**
- **Não recebe atualizações de segurança desde 2021**
- Tem **mais de 900 vulnerabilidades publicadas** até 2026
- Está **sem suporte há mais de cinco anos**

### Análise técnica

**Sistema operacional**: Android Things 8.0/8.1
**Fim de vida**: janeiro de 2021
**Vulnerabilidades conhecidas**: mais de 900
**Correções de segurança**: nenhuma desde o fim de vida
**Dispositivos afetados**: câmeras Falcon, Sparrow, Condor e caixas de computação Bravo

### O que a imagem de setembro de 2026 mostra

As imagens do sistema de arquivos publicadas em setembro de 2026 revelam as versões exatas de uma câmera em serviço ativo, em vez de uma unidade de laboratório.

| Componente | Versão na câmera | Situação |
|-----------|----------------------|--------|
| **Android** | 8.1, compilação datada de 5 de junho de 2025 | Nível da correção de segurança: **2018-06-05** |
| **Kernel Linux** | 3.18.71 | Lançado em 2017, e a série 3.18 terminou na versão 3.18.140 em maio de 2019 |
| **Versão atual do Android** | Android 17, junho de 2026 | Nove versões principais à frente |

A compilação da câmera é recente. **O sistema operacional por baixo dela não é**, e o nível da correção mostra que o dispositivo não recebe atualizações de segurança do Android há **oito anos**. O kernel está **69 versões de correção atrás** até mesmo do fim de sua própria linha de manutenção, que ocorreu há mais de nove anos.

### Duas vulnerabilidades presentes nesta compilação

Micah Lee identificou duas falhas conhecidas publicamente que afetam componentes enviados com a câmera. As datas das correções provam que a câmera antecede todas elas.

| CVE | Componente | Efeito | Corrigida |
|-----|-----------|--------|---------|
| **CVE-2021-1905** | Driver de GPU Qualcomm Adreno | Uso após liberação que permite que **qualquer código no dispositivo, inclusive aplicativos sem privilégios, corrompa a memória do kernel e assuma o controle total** | Maio de 2021 |
| **CVE-2018-9568** “WrongZone” | Manipulação de sockets no kernel Linux | Confusão de tipos sobre IPv6 que permite a um programa **escalar privilégios para raiz**. Há código público de exploração | Dezembro de 2018 |

As duas foram corrigidas anos antes da compilação do firmware desta câmera. **Nenhuma depende de acesso físico, pois ambas podem ser alcançadas por software já em execução no dispositivo.** A ressalva de proximidade usada pela Flock para minimizar as constatações da GainSec não se aplica a nenhuma delas.

### Comparação com dispositivos de consumo

Para ter uma referência:

- Seu **smartphone** deixa de receber atualizações após cerca de cinco anos, e os fabricantes **param de vendê-lo**
- Uma **câmera de segurança doméstica** com software de cinco anos seria considerada **criticamente insegura**
- Órgãos governamentais exigem **software atualizado e com suporte** para sistemas sensíveis

*Ainda assim, a Flock Safety continua implantando e vendendo câmeras com software sem suporte do fornecedor, sem correções de segurança, com centenas de explorações conhecidas e que processa dados policiais sensíveis.*

### Por que isso importa

Executar **software em fim de vida** em dispositivos de vigilância significa:

- **Qualquer vulnerabilidade publicada do Android 8.x** funciona nessas câmeras
- Há **código de exploração disponível publicamente** para muitas vulnerabilidades
- **Nenhuma correção resolverá** problemas descobertos no futuro
- É impossível alcançar a **conformidade regulatória** (FISMA, NIST, CMMC)

______

## Vulnerabilidade crítica nº 3: ausência de criptografia em tempo de execução

### CVE-2025-47824 e CVE-2025-59407

**Gravidade**: ALTA a CRÍTICA (CVSS 2.0 a 9.8)

### Alegações da Flock Safety e realidade

**O site da Flock Safety afirma**:

> “Os dados e as imagens são criptografados durante todo o ciclo de vida.”

**Constatações da pesquisa independente** (GainSec e Ben Jordan):

> “Em toda a nossa pesquisa, não descriptografamos nem quebramos nada. Tudo estava sem criptografia em tempo de execução.”

*A distância entre a alegação de marketing e a realidade técnica é total.*

### O que não está criptografado

Ao examinar os dispositivos, os pesquisadores encontraram estes dados **sem criptografia**:

1. **Vídeos e imagens armazenados**
2. **Dados de placas e metadados**
3. **Credenciais de Wi-Fi e chaves de API**
4. **Arquivos de banco de dados com registros de detecção**
5. **Tráfego de rede** (veja a Vulnerabilidade nº 6)
6. **Registros do sistema com informações sensíveis**

### Contradição sobre retenção de dados

**A Flock Safety afirma**: os dados são removidos automaticamente após sete dias.
**Constatações da pesquisa**: foram encontradas imagens que remontam à **fabricação do dispositivo**, meses ou anos antes.

Trecho do artigo técnico GainSec:

> “Encontramos imagens com mais de sete dias. Na verdade, algumas imagens armazenadas foram capturadas quando a câmera foi acionada dentro da fábrica onde o dispositivo foi fabricado.”

*Isso significa que as políticas de privacidade declaradas não são aplicadas no próprio dispositivo.*

### Implicações para a privacidade

Essa falha de criptografia significa:

- **Roubo físico do dispositivo** = violação imediata de dados
- **Interceptação de rede** expõe dados em texto simples
- **Ameaças internas** conseguem exfiltrar dados com facilidade
- **As proteções de mandados** talvez não se apliquem aos dados sem criptografia
- **Violações de conformidade** com vários regulamentos (HIPAA, CCPA etc.)

______

## Vulnerabilidade crítica nº 4: credenciais codificadas em todo o sistema {#critical-vulnerability-4-hardcoded-credentials-throughout-system}
### CVE-2025-47818, CVE-2025-47821, CVE-2025-47823, CVE-2025-59407 e CVE-2025-59409

**Gravidade**: CRÍTICA (CVSS 9.8 no limite superior da escala)

### Categorias de segredos codificados

Pesquisadores de segurança descobriram **muitas credenciais codificadas**:

#### 1. Senhas do ponto de acesso Wi-Fi

- **Senha universal** em todas as câmeras Falcon/Sparrow
- **Usuários e administradores não conseguem alterá-la**
- **Conhecida pelos pesquisadores** e publicada no artigo técnico (com trechos omitidos)
- **Confirmada pelo CVE-2025-59409**: o firmware de produção Falcon e Sparrow (compilação `OPM1.171019.026`) é enviado com **credenciais de Wi-Fi de desenvolvimento em texto simples**

#### 2. Chaves de API e tokens

- **Codificados no firmware** e no código dos aplicativos
- **Concedem acesso ao backend** de vários serviços
- **Encontrados por engenharia reversa** dos APKs Android
- **Confirmados pela imagem de setembro de 2026**: uma chave de API do backend está codificada em `CameraSettings`, dentro de `com.flocksafety.android.common.lib`, uma biblioteca compartilhada incluída em **todos os 19 aplicativos Flock** no dispositivo
- **O ID e o segredo de cliente do Auth0 ficam na partição `/persist` sem criptografia**, em `flock/auth0/auth0_cred`, um local projetado para sobreviver à restauração de fábrica
- **As credenciais recebidas ficam em texto simples** depois que a câmera se autentica no serviço Okta Auth0 da Flock usando seu próprio endereço MAC

#### 3. Credenciais de bancos de dados

- **Bancos SQLite** sem proteção por senha
- Credenciais **MySQL/PostgreSQL** em arquivos de configuração
- **Acesso direto ao banco de dados** a partir do shell local

#### 4. Keystores criptográficos

- **Confirmados pelo CVE-2025-59407**: o aplicativo DetectionProcessing inclui um keystore Java junto com sua senha codificada, e o keystore contém uma **chave privada**
- **Gravidade**: CRÍTICA (CVSS 9.8), pois o material da chave acompanha o binário que deveria protegê-lo

#### 5. Nomes de redes Wi-Fi

- Uma **lista de redes preferenciais** está codificada no firmware
- Permite ataques com **pontos de acesso maliciosos** (veja a Vulnerabilidade nº 6)

#### 6. Credenciais de serviços em nuvem

- **Tokens AWS/Azure** incorporados ao código
- **Chaves de API de terceiros** (ArcGIS e serviços de mapas)
- **Tokens OAuth** que nunca são renovados

### Cenário de ataque: rede maliciosa

Com nomes de redes Wi-Fi codificados, os pesquisadores demonstraram o seguinte:

1. O invasor configura uma **rede Wi-Fi falsa** com o SSID codificado
2. A câmera **se conecta automaticamente** (prioriza redes codificadas)
3. O invasor captura **todo o tráfego de rede** por meio de um ataque intermediário
4. Credenciais em texto simples são extraídas do tráfego
5. O invasor obtém **acesso ao sistema de backend**

**Não é necessário acesso físico à câmera.** Basta estar dentro do alcance do Wi-Fi.

______

{{< figure src="flock-safety-hardcoded-credentials-attack-vectors-diagram.webp" alt="Diagrama que apresenta cinco vetores de ataque com credenciais codificadas nas câmeras Flock Safety, incluindo senhas de Wi-Fi, chaves de API, credenciais de bancos de dados e tokens de serviços em nuvem" >}}

______

## Vulnerabilidade crítica nº 5: ausência de autenticação multifator

### Falha de política organizacional

**Gravidade**: ALTA (organizacional)

### A revelação

**A Flock Safety não exige autenticação de dois fatores ou MFA** para alguns órgãos policiais, *os mesmos órgãos que acessam dados de rastreamento de 150 milhões de veículos por dia.*

Trecho de um pesquisador de segurança:

> “Quando descobri isso, simplesmente não acreditei. O processo de segurança exigido para entrar no Disney Plus é demais para alguns departamentos de polícia adotarem ao acessar informações confidenciais e a localização, em alguns casos, de praticamente todas as pessoas.”

### Por que isso importa

Sem MFA/2FA:

- **Uma única senha comprometida** dá acesso total ao sistema
- **Ataques de phishing** são muito eficazes
- **Ataques de preenchimento de credenciais** usam senhas de outras violações
- **Ameaças internas** são mais fáceis de executar
- **Dispositivos roubados** concedem acesso imediato

### Comparação

Requisitos de segurança para sistemas **menos sensíveis**:

- **Disney+**: 2FA disponível
- **Gmail**: 2FA ativado por padrão para contas novas
- **Serviços bancários**: 2FA exigido por lei
- **Redes sociais**: 2FA padrão

Requisitos de segurança para rastrear **mais de 150 milhões de veículos por dia**:

- **Flock Safety**: 2FA opcional (alguns órgãos não o usam)

### Resposta de um senador dos EUA

Essa constatação foi destacada especificamente na **carta do senador Wyden** que pede uma investigação da FTC. A carta cita como evidência de que a Flock Safety:

> “expôs desnecessariamente dados pessoais sensíveis dos americanos ao roubo por hackers e espiões estrangeiros”

### Solução simples

**Chaves de segurança USB/NFC** custam **US$ 10 a US$ 25** e oferecem:

- Autenticação **resistente a phishing**
- **Nenhum aplicativo ou código adicional** necessário
- Conformidade com os padrões **FIDO2/WebAuthn**
- **Uso simples** (conecte ou aproxime o dispositivo)

*Se isso dá “trabalho demais” para agentes policiais, eles **não deveriam ter acesso** a sistemas nacionais de vigilância.*

______

## Vulnerabilidade crítica nº 6: tráfego de rede em texto simples
### Aguardando atribuição de identificador

**Gravidade**: ALTA (CVSS 7.8 estimado pelos pesquisadores)

**Nenhum identificador CVE foi atribuído a esta categoria.** O registro atribuído mais próximo, CVE-2025-59406, inclui a classificação CWE-319 para transmissão em texto simples, mas trata de um segredo Auth0 incorporado, não da interceptação de dados em trânsito. As constatações nesta seção ainda se baseiam nos relatórios de pesquisa citados acima.

### A vulnerabilidade

Quando as câmeras se conectam a redes (LTE ou Wi-Fi), transmitem dados **sem criptografia adequada**:

**Tráfego afetado**:

- Imagens e texto das placas
- Metadados de detecção
- Registros do sistema
- Dados de configuração
- Credenciais (em alguns casos)

### Vetor de ataque nº 1: rede Wi-Fi maliciosa

Os pesquisadores demonstraram o seguinte:

1. Remova o cartão SIM da câmera **ou** configure uma rede falsa com o SSID codificado
2. A câmera se conecta ao Wi-Fi malicioso
3. Capture o tráfego com o **Wireshark** ou analisador de pacotes semelhante
4. Analise-o com ferramentas como **NetworkMiner** ou **Unblo**
5. Extraia **credenciais em texto simples** e dados sensíveis

Trecho da pesquisa GainSec:

> “Capturei por um tempo os dados pcap transmitidos por uma dessas câmeras e os analisei com o Wireshark e o Unblo... e, como esperado, havia credenciais em texto simples nos dados.”

### Vetor de ataque nº 2: capturador de IMSI / Stingray

Um ataque mais sofisticado não exige proximidade física:

1. Use um **capturador de IMSI** (dispositivo Stingray improvisado) ou SDR profissional
2. **Sequestre a conexão LTE** simulando uma torre de celular
3. A câmera se conecta à **estação rádio base maliciosa**
4. Intercepte todo o tráfego com um ataque **intermediário**
5. Extraia credenciais, imagens e metadados

**Não é necessário acesso físico.** O ataque funciona a **centenas de pés de distância**.

### Potencial de ataques Tempest modernos

A transmissão em texto simples também permite **ataques no estilo Tempest**, nos quais:

- É possível capturar as emissões de RF da câmera
- O fluxo de vídeo pode ser **reconstruído remotamente**
- A técnica se assemelha às usadas pela **CIA na Guerra Fria**
- Equipamento SDR moderno torna isso **acessível a entusiastas**

______

## Vulnerabilidade crítica nº 7: transmissões públicas de câmeras expostas

### Descoberta em janeiro de 2026

**Gravidade**: CRÍTICA (CVSS 10.0, exposição completa do sistema)

### A descoberta

Em janeiro de 2026, Ben Jordan e a **404 Media** descobriram que, usando **pesquisas simples no Google**, era possível encontrar:

- Mais de **60 interfaces administrativas de câmeras Flock Safety completamente expostas**
- **Nenhum nome de usuário ou senha** exigido
- **Transmissões de vídeo ao vivo** e 30 dias de gravações arquivadas
- Acesso completo ao painel de **controle das câmeras**

### O que estava acessível

Qualquer pessoa poderia usar essas interfaces expostas para:

- **Assistir a transmissões ao vivo** em tempo real
- **Revisar 30 dias** de gravações arquivadas
- **Baixar arquivos de vídeo** diretamente
- **Controlar câmeras PTZ** (panorâmica/inclinação/zoom) das unidades Condor
- **Ver caminhos e hashes de arquivos** de evidências
- **Apagar evidências** com um único clique
- **Alterar as configurações das câmeras**
- **Ver números de série e localizações dos dispositivos**

### Violações de privacidade observadas

Ben Jordan documentou cenas que presenciou:

- **Uma família colocando um bebê no carro** no estacionamento da Lowe’s
- **Um homem saindo de casa** em Nova York pela manhã
- **Uma mulher correndo sozinha** numa trilha na floresta da Geórgia
- **Um casal discutindo** num mercado de rua em Atlanta (o zoom automático de IA focou nos rostos)
- **Um policial e uma ambulância** atendendo uma crise de saúde mental em Iowa
- **Crianças brincando** num parque na região da Baía da Califórnia
- **Um homem num balanço** de um parque vazio, num momento particular

Trecho de Ben Jordan:

> “Só de falar essas coisas em voz alta me dá náusea. Mas estou tentando mostrar apenas uma fração das informações que qualquer pessoa no mundo com acesso a um mecanismo de busca comercial teve sobre quem esteve nesse mercado ou caminhou por essa trilha nos últimos 31 dias.”

### Recursos de rastreamento

As câmeras Condor PTZ expostas têm **rastreamento com IA**:

- **Aproximam automaticamente** a imagem de pessoas
- **Seguem indivíduos** enquanto se movem
- **Detectam e focam** em smartphones (para ler telas)
- **Rastreiam vários alvos** ao mesmo tempo
- **Gravam continuamente** sem supervisão

### Potencial de doxing

Ben Jordan demonstrou como as gravações expostas podem revelar identidades:

> “Em dois minutos de OSINT com um mecanismo comercial de reconhecimento facial, descobri que uma dessas pessoas acabou de terminar a faculdade de medicina e que a outra lida com síndrome do intestino irritável crônica. O casal também teve um bebê no ano passado... Também sei que dirigiram mais de 45 minutos desde seu endereço nos subúrbios.”

O cruzamento com:

- Serviços de **reconhecimento facial**
- Perfis de **redes sociais**
- Bancos de **registros públicos**
- Informações de **vazamentos de dados** (Park Mobile etc.)
- **Registros de chamadas de emergência** (publicados por muitas cidades)

Resultado: **desanonimização completa em minutos**

______

{{< figure src="flock-exposed-camera-feed-ptz-ai-tracking-privacy-violation-overview.webp" alt="Diagrama que mostra como câmeras PTZ Flock Safety expostas, com rastreamento automático por IA, permitiam acesso público a vídeos ao vivo de pessoas em parques, trilhas e estacionamentos" >}}

______

## Vulnerabilidade crítica nº 8: coleta não autorizada de dados

### Contradição com declarações públicas

**Gravidade**: ALTA (implicações de privacidade e legais)

### Alegações da Flock Safety

**Declaração no site oficial**:

> “A Flock Safety não captura nem grava dados de pessoas, apenas de veículos.”

### Constatações da pesquisa independente

**O que as câmeras realmente fazem**:

1. **A detecção de movimento** aciona a câmera **por qualquer movimento**, não apenas veículos
2. A **IA procura placas** na imagem
3. **Se não encontra uma placa**, a imagem ainda assim é **armazenada** (não apagada)
4. Uma **pasta separada** guarda imagens sem placas
5. **Pessoas, pedestres e ciclistas** são capturados e mantidos

*A alegação de que são “apenas veículos” é falsa. A câmera armazena imagens de qualquer pessoa que passe em frente a ela.*

### Observações verificadas

Os pesquisadores documentaram câmeras capturando:

- **Uma pessoa caminhando** em frente à câmera (imagem armazenada)
- **Uma mão acenando** para a lente (imagem armazenada)
- **Uma mesa ou objeto** movido perto da câmera (imagem armazenada)
- **Funcionários da fábrica** nas instalações de produção (armazenados por meses)

Trecho da GainSec:

> “Quando passei em frente à câmera, o módulo de radar acionou o módulo da câmera para tirar uma foto minha. Depois, a IA embarcada procurou uma placa, não encontrou nenhuma e, mesmo assim, armazenou a imagem numa pasta separada.”

### Implicações legais

Essa coleta de dados não autorizada pode:

- **Violar as políticas de privacidade declaradas** (práticas enganosas)
- **Descumprir contratos de aquisição** (se as cidades especificaram “apenas veículos”)
- **Provocar violações do GDPR/CCPA** (cidadãos da UE e residentes da Califórnia)
- **Invalidar acordos de consentimento**
- **Expor a empresa a processos** por publicidade enganosa

### Expansão do escopo da vigilância

As **câmeras Condor PTZ** (instaladas em 2025–2026) foram **projetadas explicitamente** para rastrear pessoas:

- **Detecção de pessoas com IA**
- **Zoom automático** nos rostos
- **Rastreamento contínuo** do movimento das pessoas
- **Sem mecanismo para recusar**
- **Frequentemente instaladas** em parques, trilhas e estações de transporte

*Isso representa uma enorme ampliação de “leitores de placas” para vigilância da população em geral, sem mudança de política, novos contratos ou aviso público.*

______

## Vulnerabilidade crítica nº 9: portas USB expostas a ataques Rubber Ducky
### Exploração por acesso físico

**Gravidade**: ALTA (com acesso físico)

### A vulnerabilidade

As **caixas de computação Bravo** e alguns modelos de câmera têm:

- **Portas USB-C expostas** no exterior
- **Nenhuma segurança física** (lacres no gabinete)
- **Execução automática** de dispositivos USB
- **Nenhuma autenticação** exigida

### Ataque Rubber Ducky / BadUSB

Um **dispositivo BadUSB** (custa US$ 5 a US$ 15):

- Aparece como **teclado USB** para o sistema
- **Executa scripts pré-programados** (cargas úteis)
- **É executado automaticamente** quando conectado
- **Não exige interação do usuário**

### Cenário de ataque

A GainSec demonstrou estes passos:

1. Aproxime-se de um dispositivo Flock instalado
2. Conecte o **dispositivo BadUSB** à porta exposta
3. O dispositivo executa a carga útil (script)
4. A carga instala **malware persistente**
5. O invasor **vai embora**
6. O malware **se comunica com o servidor de comando e controle** por LTE/Wi-Fi

**Tempo total**: menos de 30 segundos

### O que as cargas úteis podem fazer

Scripts automatizados podem:

- **Ativar um ponto de acesso sem fio** (contornando o pressionamento de botão)
- **Instalar uma porta dos fundos** para acesso remoto
- **Exfiltrar dados** para um servidor remoto
- **Alterar gravações** ou evidências
- **Desativar a câmera** ou causar negação de serviço
- **Adicionar o dispositivo a uma botnet** para ataques DDoS
- **Capturar credenciais** de outros sistemas

### Por que isso importa

Como existem **mais de 80.000 câmeras**, muitas em **áreas semirrurais** com **pouca visibilidade**:

- É relativamente fácil obter **acesso físico**
- **Não há guardas** nem monitoramento constante
- As câmeras são presas com **abraçadeiras de mangueira simples**
- Muitas ficam instaladas a **2,1 metros do chão** (ao alcance de um pequeno escadote)

Trecho de Ben Jordan:

> “Essas câmeras não são exatamente pequenas fortalezas impenetráveis. São câmeras Android de plástico e caixas de computação instaladas a 2,1 metros do chão com abraçadeiras de mangueira.”

______

{{< figure src="badusb-rubber-ducky-flock-camera-usb-exploit-attack-chain.webp" alt="Diagrama do ataque que mostra como um dispositivo BadUSB conectado à porta USB exposta de uma câmera Flock Safety pode instalar malware persistente em menos de 30 segundos" >}}

______

## Vulnerabilidade crítica nº 10: chaves de API expostas publicamente

### Descoberta por pesquisador de OSINT

**Gravidade**: CRÍTICA (CVSS 9.5)

### A descoberta

Em 2025, o pesquisador de **OSINT Joshua Michael** descobriu:

- Um **site de demonstração da Flock Safety exposto**, encontrado por meio de Google dorking
- **5.000 linhas de código-fonte** visíveis
- Uma **chave de API ativa** incorporada ao código
- Acesso a mais de **50 camadas privadas** de dados geoespaciais

### O que a chave de API permitia acessar

A **chave de API do ArcGIS** exposta concedia acesso a:

**1. Dados de cadastro**

- Nomes de clientes
- Endereços de e-mail
- Número de câmeras por local
- Recursos para anexar arquivos

**2. Localização de viaturas em patrulha** (vários órgãos)

- Rastreamento GPS em tempo real de veículos policiais
- Instalação em Aurora, Colorado
- Departamento de Polícia de Carrollton
- **Risco à segurança nacional**

**3. Informações pessoais de agentes**

- Nomes e números de telefone
- Endereços de e-mail
- Áreas de patrulha previstas
- Jurisdições de origem

**4. Banco de alertas de listas de veículos procurados** (Dallas, Texas)

- **6.000 registros** de veículos sinalizados
- Placas e motivos das sinalizações
- Locais e horários de detecção
- IDs das câmeras que capturaram os veículos
- **Cinco meses de rastreamento de movimentos**

Trecho de Joshua Michael:

> “Qualquer pessoa poderia pesquisar no Google, encontrar este mapa e rastrear os padrões de movimento dessas pessoas por cinco meses. Também observo que a categoria do motivo inclui alguém apenas como ‘suspeito’, e vários outros registros não apresentam motivo algum ou estão em branco.”

### Superfície de ataque

Chaves de API expostas permitem:

- **Perseguir veículos específicos**
- **Comprometer a segurança dos agentes** (endereços residenciais e padrões de patrulha)
- **Violar a segurança operacional** (saber onde a polícia está ou não está)
- **Intimidar testemunhas** (rastrear quem denunciou crimes)
- **Coletar inteligência criminal** para o crime organizado

### Contexto da violação: Flax Typhoon

Poucas semanas antes dessa descoberta, o grupo de hackers **Flax Typhoon**, **patrocinado pelo Estado chinês**, comprometeu o ArcGIS, segundo os pesquisadores de segurança Alexa Feminina e James Zhang.

Trecho da InfoSecurity Magazine:

> “Os hackers teriam mirado um aplicativo legítimo do ArcGIS voltado ao público... usado para recuperação de desastres, gestão de emergências e outras funções críticas.”

**Isso significa que Estados-nação hostis poderiam ter acesso** às localizações de viaturas policiais, identidades de agentes, posições das câmeras de vigilância e padrões de resposta a emergências.

______

## Vulnerabilidades adicionais (resumo de mais de 50)
### Vulnerabilidades 11 a 51

O artigo técnico da GainSec documenta **41 constatações adicionais**, incluindo:

**Falhas de projeto do sistema**:

- Modo de depuração ativado no firmware de produção
- Processo de inicialização inseguro permite comprometer o bootloader
- Nenhum elemento seguro ou TPM para armazenar chaves
- Mecanismo previsível de atualização do firmware

**Problemas de autenticação**:

- Tokens de sessão nunca expiram
- Nenhuma restrição de acesso por endereço IP
- Credenciais compartilhadas entre frotas de dispositivos
- Nenhum pinning de certificado

**Segurança de rede**:

- Portas abertas com serviços de depuração
- Telnet ativado em algumas unidades
- Servidores FTP com credenciais fracas
- Vulnerabilidades de DNS rebinding

**Privacidade e retenção de dados**:

- Imagens armazenadas além do prazo de retenção declarado
- Metadados nunca eliminados
- Dados de reconhecimento facial coletados
- Rastreamento de localização além dos veículos

**Segurança física**:

- Gabinetes fáceis de desmontar
- Interfaces seriais expostas
- Portas de depuração JTAG acessíveis
- Nenhum lacre que indique violação

**Falhas criptográficas**:

- Geração fraca de números aleatórios
- Chaves de criptografia codificadas
- MD5 ainda usado na cadeia de hashes
- Validação de certificados desativada

**Divulgação de informações**:

- Mensagens de erro detalhadas revelam dados internos
- Listagem de diretórios ativada em servidores web
- Comentários no código-fonte contêm credenciais
- Cópias de segurança da configuração podem ser lidas por qualquer pessoa

### Situação dos CVEs

Em maio de 2026:

- **22 CVEs atribuídos** e publicados
- **8 CVEs pendentes** de atribuição pelo MITRE
- **21 constatações** não enviadas para atribuição de CVE, a critério dos pesquisadores
- **Todas as constatações** documentadas no artigo técnico GainSec

Detalhes técnicos completos: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)

______

## Resposta da Flock Safety

### Declarações oficiais

**Publicação no blog de novembro de 2025**:

> “A Flock está comprometida a melhorar a segurança continuamente... Nenhuma das vulnerabilidades detalhadas no relatório afeta a capacidade de nossos clientes de cumprir seus objetivos de segurança pública.”

**Alegação**: as vulnerabilidades exigem acesso físico e “conhecimento íntimo”

**Evidências em contrário**:

- Para encontrar transmissões de câmeras expostas, bastava uma **pesquisa no Google**
- As explorações sem fio exigem apenas **proximidade**
- A exposição da chave de API era **totalmente remota**
- Após a divulgação, **as senhas codificadas eram conhecidas por todos**

### Desqualificação dos dispositivos de pesquisa

A Flock alegou inicialmente que os dispositivos de pesquisa:

> “Não estavam conectados à nuvem... como um iPhone roubado de um caminhão antes de ser conectado.”

*Isso foi refutado.* Os pesquisadores testaram **dispositivos conectados à nuvem** e obtiveram os mesmos resultados. Câmeras expostas ao público apresentaram **as mesmas vulnerabilidades**, e a 404 Media encontrou **mais de 60 câmeras de produção expostas**.

### Resposta aos pesquisadores

Segundo a GainSec, as tentativas de divulgação responsável receberam estas respostas:

- **Programa de recompensa por bugs com NDA** (silenciando a divulgação)
- **Nenhuma confirmação** das correções
- **Comunicado de imprensa** divulgado antes do prazo de 90 dias
- **Nenhum reconhecimento** do pesquisador no comunicado
- **Perda do emprego** do pesquisador em até 48 horas da publicação do vídeo

Ben Jordan relatou:

- **Visitas da polícia** à sua propriedade
- Suspeitos de serem **investigadores particulares** fotografando sua casa
- **Assédio por vizinhos**
- Ameaças de **notificação extrajudicial para cessar e desistir** pela Flock Safety

Trecho de Ben:

> “Não vejo essas coisas como consequências ou punição por pesquisar vulnerabilidades de segurança. Vejo como consequências e punição por fazer isso de forma ética e transparente.”

### Continuidade das instalações

*Apesar de tudo isso*, a Flock Safety:

- **Continua vendendo** dispositivos vulneráveis
- Não lançou **atualizações de firmware** que resolvam as causas principais
- Continua usando **Android Things 8.x** (fim de vida em 2021)
- Não exige **MFA obrigatório** para órgãos policiais

______

## Resposta legislativa e de políticas públicas

### Pedido de investigação do Senado dos EUA

**Fevereiro de 2026**: os senadores **Ron Wyden** (Oregon) e **Raja Krishnamoorthi** (Illinois) enviaram uma carta formal à FTC pedindo uma investigação.

**Trecho da carta**:

> “A Flock expôs desnecessariamente dados pessoais sensíveis dos americanos ao roubo por hackers e espiões estrangeiros.”

**Fundamentos citados**:

- Riscos à segurança nacional
- Alegações de privacidade enganosas
- Práticas de segurança inadequadas
- Ausência de exigência de MFA

### Ações de conselhos municipais

**Denver, Colorado**:

- Em dezembro de 2025, o conselho municipal **votou contra** renovar o contrato com a Flock
- Citou o **“desrespeito à honestidade e à prestação de contas”** da Flock
- Em janeiro de 2026, o prefeito **anulou a decisão** por meio de um “acordo nos bastidores”
- A reação pública continua

**Evanston, Illinois**:

- Descobriu que o **ICE usava as câmeras** sem consentimento
- Votou para **retirar as câmeras**
- *A Flock reinstalou as câmeras sem autorização*
- A cidade usa dinheiro dos contribuintes para **cobrir as câmeras** com lona e buscar medidas legais

**Oakland, Califórnia**:

- Adiou a votação sobre uma **expansão de US$ 2,25 milhões**
- Encomendou uma auditoria de segurança independente
- Considerou **enganosas** as alegações de eficácia da Flock

### Pedidos de acesso a registros públicos

Várias cidades estão conduzindo investigações com base em:

- Pesquisas de segurança disponíveis publicamente
- Pedidos FOIA de contratos da Flock
- Requisitos de auditoria independente
- Pressão de ativistas comunitários

______

## Análise técnica: cenários de ataque no mundo real

### Cenário 1: vigilância por Estado-nação

**Agente de ameaça**: serviço de inteligência estrangeiro

**Objetivo**: rastrear autoridades governamentais

**Método**:

1. Usar um capturador de IMSI para interceptar o tráfego LTE das câmeras
2. Extrair credenciais em texto simples do fluxo
3. Acessar o backend com chaves de API comprometidas (ou uma camada ArcGIS já exposta)
4. Consultar o banco de dados para encontrar veículos registrados em instalações governamentais
5. Rastrear os movimentos de autoridades e militares

**Tempo para executar**: dias (depois que a infraestrutura estiver montada)
**Probabilidade de detecção**: baixa (C2 criptografado que imita tráfego legítimo)

### Cenário 2: contravigilância pelo crime organizado

**Agente de ameaça**: organização de tráfico de drogas

**Objetivo**: identificar padrões de patrulha policial

**Método**:

1. Comprar um dispositivo BadUSB (US$ 15)
2. Dirigir até câmeras na área de operação
3. Conectar o BadUSB a uma porta USB exposta (30 segundos)
4. A carga desativa a câmera ou altera as gravações
5. Alternativamente, a carga exfiltra o rastreamento de viaturas policiais para um servidor remoto

**Tempo para executar**: 30 segundos por câmera
**Probabilidade de detecção**: baixa (parece uma atividade legítima do dispositivo)

### Cenário 3: perseguidor ou violência doméstica

**Agente de ameaça**: ex-parceiro abusivo

**Objetivo**: rastrear os movimentos da vítima

**Método**:

1. Obter a placa da vítima (informação pública)
2. Pesquisar no Google uma interface de câmera Flock exposta (vulnerabilidade de janeiro de 2026)
3. Consultar 30 dias de gravações em busca de aparições do veículo
4. Cruzar os dados com bancos públicos (endereço de trabalho, residência etc.)
5. Determinar rotina e horários

**Tempo para executar**: de minutos a horas
**Probabilidade de detecção**: zero (não há registros de autenticação)

### Cenário 4: adulteração de evidências

**Agente de ameaça**: réu em processo criminal

**Objetivo**: destruir evidências antes do julgamento

**Método**:

1. Descobrir a localização da câmera durante a análise do mandado
2. Obter acesso físico à câmera (sequência de pressionamento de botão)
3. Obter um shell raiz
4. Navegar até a pasta de evidências
5. Apagar imagens ou vídeos específicos ou alterar os registros de data e hora

**Tempo para executar**: menos de cinco minutos
**Probabilidade de detecção**: baixa (a menos que a câmera seja examinada por perícia antes do acesso da defesa)

### Cenário 5: ativista de privacidade ou jornalista

**Agente de ameaça**: defensor da transparência

**Objetivo**: documentar o excesso de vigilância

**Método**:

1. Usar dispositivos de detecção (veja nosso [guia de hardware Flock-You](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. Mapear as câmeras na comunidade
3. Enviar pedidos FOIA sobre as políticas de gravação
4. Demonstrar vulnerabilidades ao conselho municipal
5. Defender a remoção das câmeras ou sua supervisão

**Tempo para executar**: contínuo
**Probabilidade de detecção**: alta (atividade pública)

______

{{< figure src="flock-camera-attack-scenario-threat-actor-matrix-nation-state-crime.webp" alt="Matriz que compara cinco cenários de ataque no mundo real contra câmeras Flock Safety, incluindo vigilância por Estado-nação, contravigilância pelo crime organizado, perseguição, adulteração de evidências e defesa da privacidade" >}}

______

## Como se defender dessas vulnerabilidades

### Para órgãos policiais

**Ações imediatas**:

1. **Exigir MFA/2FA** de todos os usuários (chaves de segurança USB)
2. **Auditar registros de acesso** mensalmente para encontrar consultas não autorizadas
3. **Restringir o compartilhamento** às jurisdições estritamente necessárias
4. **Isolar a rede**: colocar as câmeras em VLANs dedicadas
5. **Proteger fisicamente**: usar lacres que indiquem violação e monitorar as câmeras
6. **Criar um plano de resposta a incidentes** para casos de comprometimento

**Requisitos contratuais**:

1. **Auditorias regulares de segurança** por empresas independentes
2. **Atualizações obrigatórias de firmware** em até 30 dias da publicação da correção
3. **Notificação de CVEs** em até 24 horas
4. **Armazenamento criptografado de evidências** com chaves controladas pelo cliente
5. **Penalidades de SLA** por violações de segurança
6. **Direito de auditar** instalações e código do fornecedor

**Estratégia de longo prazo**:

1. **Plano de migração** para sair de sistemas operacionais em fim de vida
2. **Infraestrutura hospedada pela própria organização** (reduzir a dependência da nuvem)
3. **Avaliar alternativas de código aberto**
4. **Dar transparência à comunidade** sobre a localização e as políticas das câmeras

### Para a Flock Safety (recomendações)

**Prioridade crítica** (imediata):

1. **Desativar a criação** de ponto de acesso sem fio por pressionamento de botão
2. **Exigir MFA** em todas as contas, sem exceções
3. **Renovar todas as credenciais codificadas** em todo o sistema
4. **Corrigir emergencialmente** as interfaces públicas expostas
5. **Criptografar dados em repouso** com gerenciamento adequado de chaves

**Alta prioridade** (30 dias):

1. **Migrar para um sistema operacional com suporte** (Android 12+ ou Linux)
2. Criar um **programa de recompensa por bugs sem NDAs**
3. Fazer **auditoria de segurança por terceiros** e publicar os resultados
4. **Criptografar o tráfego de ponta a ponta**
5. **Melhorar a segurança física** (remover portas USB expostas e reforçar gabinetes)

**Prioridade média** (90 dias):

1. **Redesenhar completamente** o sistema de autenticação
2. Implementar **inicialização segura** com firmware verificado
3. Integrar um **módulo de segurança de hardware**
4. Obter **certificações de conformidade** (FedRAMP, SOC 2, ISO 27001)
5. Criar um **painel de segurança para clientes** com notificações de violações

**Longo prazo** (um ano):

1. **Abrir os componentes de segurança** (para gerar confiança)
2. Criar um programa de **testes adversariais** (equipe vermelha)
3. Definir requisitos para funções de **engenharia de segurança**
4. Integrar segurança ao **ciclo de vida de desenvolvimento de software** (DevSecOps)
5. Participar de **normas do setor** (OWASP, CIS)

### Para indivíduos

**Estratégias de proteção**:

1. **Usar dispositivos de detecção** (veja nosso [guia de hardware](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. **Mapear as câmeras** na sua região
3. **Variar trajetos e horários** para reduzir a análise de padrões
4. **Defender supervisão e transparência** no conselho municipal
5. Fazer **pedidos FOIA** sobre seus dados (quando permitido por lei)
6. **Apoiar leis de privacidade** estaduais e federais

**Medidas de segurança operacional (OpSec)**:

1. **Evitar veículos únicos** (escolha uma marca, modelo e cor comuns)
2. Usar **veículos diferentes** em atividades sensíveis (quando legal)
3. Preferir **transporte alternativo** (bicicleta, transporte público, caminhar)
4. Usar **coberturas de placa que protejam a privacidade** (somente se forem legais na jurisdição)
5. Usar **bolsas Faraday** para telefones quando houver risco de correlação

{{< stscollective-ad "flockyou" >}}

______

{{< figure src="flock-safety-security-remediation-priority-roadmap.webp" alt="Roteiro de correção priorizado que mostra as soluções imediatas, de 30 dias, de 90 dias e de longo prazo que a Flock Safety deve implementar para corrigir as vulnerabilidades críticas" >}}

______

## A equipe de pesquisa

### GainSec (Jon “GainSec” Gaines)

**Histórico**: profissional de segurança ofensiva com mais de dez anos de experiência

**Contribuições**:

- Descobriu **47 das 51** vulnerabilidades
- Publicou **artigo técnico formal** com detalhes técnicos
- Coordenou a **divulgação responsável** com a Flock Safety
- Registrou **30 CVEs** (22 publicados e 8 pendentes)
- Criou uma **lista de verificação para defensores** da área de segurança

**Contato**: whitepaper@gainsecmail.com
**Pesquisa**: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)
**Blog**: [gainsec.com](https://gainsec.com)

### Ben Jordan (Benn Jordan)

**Histórico**: jornalista, músico e investigador de tecnologia

**Contribuições**:

- **Documentou vulnerabilidades em vídeo**
- Fez **demonstrações públicas** para jornalistas (The Guardian e 404 Media)
- Descobriu **mais de 60 transmissões de câmeras expostas** por meio do Google
- Atuou na **defesa e educação do público**
- Coordenou **ações legislativas** com os gabinetes dos senadores

**Contato**: pelo canal do YouTube
**Trabalho**: YouTube, Benn Jordan

### Joshua Michael (Next AI)

**Histórico**: especialista em OSINT e pesquisador de privacidade

**Contribuições**:

- Descobriu **chaves de API expostas** por meio de Google dorking
- Documentou **exposições de camadas ArcGIS**
- Desenvolveu **metodologia de OSINT** para rastrear pesquisas
- Fez **correlações de dados** com violações públicas

**Organização**: Next AI, empresa de inteligência de fontes abertas

### Colaboradores de apoio

- **404 Media**: jornalismo investigativo e divulgação pública
- **The Guardian**: cobertura internacional
- **Lucy Parsons Labs**: anos de defesa e pesquisa sobre ALPR
- **Sassy South**: organização comunitária e transparência
- **DeFlock / Will Freeman**: projeto de mapeamento de câmeras
- **Ed Vogel**: análise jurídica e de políticas públicas

______

## Considerações éticas
### Linha do tempo da divulgação responsável

A comunidade de segurança seguiu as práticas recomendadas de **divulgação responsável**:

**Protocolo padrão**:

1. Descobrir a vulnerabilidade
2. Fazer **notificação privada ao fornecedor por 90 dias**
3. O fornecedor desenvolve e implanta uma correção
4. Fazer a **divulgação pública** após a correção ou 90 dias, o que ocorrer primeiro
5. Publicar uma análise detalhada para fins de aprendizado defensivo

**O que realmente aconteceu**:

1. A GainSec descobriu vulnerabilidades (final de 2024)
2. Fez **contatos repetidos** com a Flock Safety (fevereiro de 2025 em diante)
3. A Flock ofereceu **recompensa por bugs com NDA** (para silenciar a divulgação)
4. A Flock publicou um **comunicado de imprensa antecipadamente** (sem reconhecer o pesquisador)
5. **Nenhuma confirmação** de que as correções foram implantadas
6. A GainSec prosseguiu com a **divulgação pública** após os prazos de 90 dias
7. Ben Jordan e a 404 Media **verificaram de forma independente** em sistemas de produção

### Retaliação contra pesquisadores

A GainSec e Ben Jordan relataram:

- **Perda de emprego** ou dificuldades profissionais
- **Visitas policiais** a residências particulares
- **Suspeita de vigilância** de casas e propriedades
- **Assédio por vizinhos**
- Ameaças de **notificação extrajudicial para cessar e desistir**
- **Ataques nas redes sociais** (o CEO da Flock os chamou de “terroristas”)

Esse **efeito intimidador** sobre a pesquisa de segurança:

- Desestimula a divulgação de vulnerabilidades
- Atrasa correções críticas de segurança
- Prejudica a segurança pública
- Viola as normas éticas da comunidade de segurança

*A resposta da Flock Safety aos pesquisadores que seguiram os protocolos de divulgação cria um precedente perigoso para toda a comunidade de pesquisa em segurança.*

Trecho de Ben Jordan:

> “Não tenho condições de dedicar ainda mais meses a outra vulnerabilidade da Flock Safety, mas, como você pode ver, esta é urgente e, francamente, temo que já esteja sendo explorada.”

### Interesse público

Esses pesquisadores atuaram **em defesa do interesse público** ao:

- **Seguir protocolos de divulgação responsável**
- **Notificar o fornecedor primeiro**, antes da divulgação pública
- **Omitir detalhes sensíveis** que facilitem a exploração
- **Fornecer orientações defensivas** a profissionais
- **Defender mudanças nas políticas públicas** pelos canais adequados
- **Aceitar riscos pessoais** para informar o público

Sem o trabalho deles:

- Mais de **80.000 câmeras vulneráveis** continuariam sem correção
- Mais de **150 milhões de leituras diárias de veículos** permaneceriam desprotegidas
- **Milhões de americanos** continuariam expostos sem saber
- A **segurança nacional** ficaria comprometida
- **Nenhuma ação legislativa** estaria em andamento

______

## Conclusão: o caminho adiante

{{< figure src="flock-safety-vulnerability-disclosure-timeline-2026.webp" alt="Linha do tempo que resume o processo de divulgação de vulnerabilidades da Flock Safety entre 2024 e 2026, desde a descoberta inicial até a divulgação responsável e a exposição contínua sem correções" >}}

### Situação atual (maio de 2026)

- Mais de **50 vulnerabilidades críticas** documentadas e divulgadas parcialmente
- Mais de **80.000 câmeras** continuam instaladas com falhas sem correção
- Nenhuma **correção abrangente** do fornecedor
- **Ação regulatória limitada** (foi pedida uma investigação da FTC, mas ela não começou)
- **Risco contínuo de exploração** para a segurança nacional e a privacidade individual

### O que precisa acontecer

**Em todo o setor**:

1. **Auditorias de segurança obrigatórias** antes da implantação governamental
2. **Testes independentes** por terceiros qualificados
3. **Divulgação pública** dos resultados das auditorias
4. **Responsabilidade dos fornecedores** por falhas de segurança
5. **Conformidade com normas** (NIST, ISO etc.)

**Especificamente para a Flock Safety**:

1. **Correções emergenciais imediatas** para vulnerabilidades críticas
2. **Migração do sistema operacional** para uma plataforma com suporte
3. **Reconhecimento público** do escopo
4. **Compensação** aos pesquisadores afetados
5. **Relatórios de transparência** sobre a postura de segurança

**Para órgãos policiais**:

1. **Requisitos de segurança** nos contratos de aquisição
2. **Auditorias regulares** dos sistemas instalados
3. **MFA obrigatório** para todos os usuários
4. **Planos de resposta a incidentes**
5. **Transparência comunitária** sobre programas de vigilância

**Para legisladores**:

1. **Normas federais** para tecnologia de vigilância
2. **Divulgação obrigatória** de vulnerabilidades às partes afetadas
3. **Proteção a denunciantes** para pesquisadores de segurança
4. **Medidas judiciais civis** para violações de privacidade
5. **Mecanismos de supervisão** para sistemas de vigilância

### O panorama mais amplo

Este estudo de caso representa **mais do que a Flock Safety**. Ele exemplifica:

- Um **setor de vigilância** que prioriza o crescimento em detrimento da segurança
- **Compras governamentais** sem conhecimento técnico suficiente
- **Alegações de fornecedores** que não são contestadas nem verificadas
- **Incentivos financeiros** desalinhados da segurança pública
- **Lacunas regulatórias** na supervisão de tecnologias emergentes

*Cada cidade que assina um contrato com a Flock sem verificação independente de segurança aceita esses riscos em nome de seus residentes.*

### Ação necessária

**Para profissionais de segurança**:

- **Apoiar esforços de divulgação responsável**
- **Contribuir para ferramentas de segurança de código aberto**
- **Defender a proteção dos pesquisadores**

**Para órgãos policiais**:

- **Exigir prestação de contas** dos fornecedores
- **Exigir auditorias de segurança** antes da implantação
- **Implementar MFA imediatamente**
- **Consultar a comunidade de segurança**

**Para formuladores de políticas públicas**:

- **Aprovar leis que exijam normas de segurança**
- **Financiar auditorias independentes** de tecnologia de vigilância
- **Proteger denunciantes** e pesquisadores
- **Criar órgãos de supervisão** com conhecimento técnico

**Para o público**:

- **Informar-se** sobre a vigilância na sua comunidade
- **Participar de reuniões do conselho municipal** quando contratos forem discutidos
- **Apoiar organizações** que lutam por transparência
- **Contatar representantes** para apresentar preocupações
- **Usar ferramentas de detecção** para mapear a vigilância (veja nosso [guia de hardware](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))

### Leitura relacionada

- **[Vigilância por câmeras Flock Safety: prevalência, preocupações com a privacidade e estratégias de proteção](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**: entenda o cenário de vigilância
- **[Projeto de detecção Flock-You: guia de hardware contra vigilância](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**: construa seu próprio dispositivo de detecção

Esperar que o setor corrija essas falhas não é uma estratégia de proteção. Os **[dispositivos de detecção FlockYou](https://stscollective.com/collections/flockyou-alpr-flock-safety-awareness-devices)** da STS Collective funcionam hoje, e o código de leitor **SIMEONONSECURITY** dá até 20% de desconto.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Comprar detectores FlockYou e economizar 20%
{{< /centerbutton >}}

______

## Referências

1. [Pesquisa GainSec sobre o ecossistema anticrime, GitHub](https://github.com/GainSec/anti-crime-ecosystem-research)
2. [Artigo técnico GainSec, DOI Zenodo: 10.5281/zenodo.17529423](https://zenodo.org/records/17584876)
3. [Blog da GainSec, análises técnicas informais](https://gainsec.com/)
4. [Resposta oficial da Flock Safety, novembro de 2025](https://www.flocksafety.com/blog/response-to-compiled-security-research-on-flock-safety-devices)
5. [404 Media, transmissões de câmeras Flock expostas](https://www.404media.co/)
6. [Canal de Ben Jordan no YouTube, demonstrações de vulnerabilidades](https://www.youtube.com/@BennJordan)
7. [National Vulnerability Database](https://nvd.nist.gov/)
8. [Banco de dados CVE da MITRE](https://cve.mitre.org/)
9. [Electronic Frontier Foundation, vigilância ALPR](https://www.eff.org/issues/automated-license-plate-readers)
10. [Carta do senador Wyden à FTC](https://www.wyden.senate.gov/)
11. [Lucy Parsons Labs, pesquisa sobre ALPR](https://lucyparsonslabs.com/)
12. [Projeto DeFlock, mapeamento de câmeras](https://deflockproject.org/)
13. [Distributed Denial of Secrets, imagens do sistema de arquivos de câmera ALPR Flock](https://ddosecrets.org/article/flock-alpr-camera)
14. [Micah Lee, câmeras Flock têm muitas vulnerabilidades de segurança e credenciais codificadas](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
15. [WIRED e 404 Media, hackers entraram numa câmera Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
16. [Hackaday, esta semana em segurança: câmeras Flock são antigas](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
17. [NVD, CVE-2021-1905, uso após liberação na GPU Qualcomm Adreno](https://nvd.nist.gov/vuln/detail/CVE-2021-1905)
18. [NVD, CVE-2018-9568, confusão de tipos em sockets do kernel Linux](https://nvd.nist.gov/vuln/detail/CVE-2018-9568)
19. [WiFi Mothership, referência de detecção e dispositivos ALPR da Flock Safety](https://wifimothership.com/flock)
20. [CVE.org, pesquisa de registros do programa CVE](https://www.cve.org/)
21. [Alerta de segurança Flock Safety, detecção de disparos e leitores de placas](https://www.flocksafety.com/articles/gunshot-detection-and-license-plate-reader-security-alert)
22. [GainSec, Fly By Device 2: RCE sem fio, feeds de câmera, negação de serviço e divulgação de informações na Falcon e Sparrow](https://gainsec.com/2025/09/27/fly-by-device-2-the-falcon-sparrow-gated-wireless-rce-camera-feed-dos-information-disclosure-and-more/)
23. [GainSec, Root from the Coop Device 3: shell raiz na caixa de computação Bravo da Flock Safety](https://gainsec.com/2025/09/19/root-from-the-coop-device-3-root-shell-on-flock-safetys-bravo-compute-box/)

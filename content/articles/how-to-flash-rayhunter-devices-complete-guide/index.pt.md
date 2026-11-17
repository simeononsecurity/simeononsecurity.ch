---
title: "Como instalar Rayhunter em dispositivos: guia completo"
draft: false
toc: true
date: 2026-03-09
lastmod: 2026-11-15
description: "Instale e configure Rayhunter para detectar capturadores de IMSI. Confira os dispositivos compatíveis, instale o firmware, verifique o funcionamento e resolva problemas comuns."
tags: ["Rayhunter", "capturador de IMSI", "simulador de estação celular", "segurança móvel", "detecção de vigilância", "proteção de privacidade", "Orbic RC400L", "TP-Link M7350", "hotspot móvel", "instalação de dispositivos", "cibersegurança", "segurança sem fio", "contramedidas de vigilância", "EFF", "ferramentas de privacidade", "comprar Rayhunter", "guia de instalação", "configuração", "dispositivos compatíveis", "segurança de rede"]
cover: "/img/cover/rayhunter.webp"
coverAlt: "Um dispositivo Rayhunter detecta sinais sem fio e capturadores de IMSI, cercado por escudos de segurança"
coverCaption: "Sistema de detecção de capturadores de IMSI Rayhunter, protegendo comunicações móveis contra vigilância"
---

**Guia completo para instalar e configurar Rayhunter, o sistema de detecção de capturadores de IMSI.**

## Resumo

**Rayhunter** é um sistema de código aberto para detectar capturadores de IMSI, executado em hotspots móveis modificados. Ele alerta quando equipamentos de vigilância tentam interceptar comunicações celulares. Este guia explica a instalação completa nos dispositivos Orbic RC400L e TP-Link M7350, as opções de configuração, a análise dos agentes de ameaça e a eficácia em redes 5G. É necessário usar um dispositivo compatível com Qualcomm. O sistema detecta vigilância em redes 2G, 3G e 4G por meio de várias heurísticas. Ele continua útil apesar da adoção do 5G, pois ataques de downgrade ainda acontecem. Oferece proteção importante a jornalistas, ativistas e pessoas que valorizam a privacidade contra vigilância governamental, criminosa e corporativa.

**Rayhunter** é uma ferramenta de código aberto que detecta capturadores de IMSI (simuladores de estação celular), capazes de interceptar comunicações móveis. Se você quer **comprar Rayhunter** ou aprender a instalar e configurar esses dispositivos corretamente, este guia abrangente cobre a instalação, a configuração e o uso dos sistemas **Rayhunter**.

**Informação sobre patrocínio:** Este artigo tem o patrocínio da [STS Collective](https://stscollective.com), principal fornecedora de dispositivos compatíveis com Rayhunter. Apesar do patrocínio, todas as informações técnicas, análises e recomendações deste guia são imparciais e se baseiam exclusivamente na documentação oficial do Rayhunter, no retorno da comunidade e em avaliações técnicas objetivas.

> 💰 **Desconto exclusivo para leitores:** Economize até 20% em dispositivos Rayhunter e em todos os produtos da STS Collective. Use o código **SIMEONONSECURITY** no pagamento ou [compre diretamente com o desconto aplicado](https://stscollective.com/discount/SIMEONONSECURITY).

## Introdução ao Rayhunter

**Rayhunter** é um sistema avançado de detecção de capturadores de IMSI desenvolvido pela **Electronic Frontier Foundation (EFF)**, uma importante organização sem fins lucrativos dedicada a defender liberdades civis no mundo digital. Desde 1990, a EFF defende privacidade digital, liberdade de expressão e inovação por meio de litígios de impacto, análise de políticas públicas, ativismo de base e desenvolvimento de tecnologia.

Esta ferramenta funciona em hotspots móveis compatíveis e monitora continuamente redes celulares à procura de atividades suspeitas que indiquem a presença de simuladores de estação celular ou “Stingrays” usados para vigilância. **Rayhunter** representa o compromisso da EFF de oferecer ferramentas práticas de proteção de privacidade a pessoas e organizações que precisam se proteger da vigilância.

**Rayhunter** emite alertas em tempo real quando detecta comportamentos celulares possivelmente maliciosos. É uma ferramenta importante de privacidade para jornalistas, ativistas, profissionais de segurança e pessoas que valorizam a privacidade. Você encontra dispositivos compatíveis **[à venda como Rayhunter](https://stscollective.com/collections/rayhunter)** na STS Collective, principal fornecedora desses dispositivos especializados.

### Apoie o projeto Rayhunter

**Rayhunter** é um projeto de código aberto que se beneficia do apoio da comunidade. Você pode contribuir para o desenvolvimento contínuo de várias formas:

- **Compre pela STS Collective:** A STS Collective doa à EFF parte do lucro obtido em cada venda de dispositivo Rayhunter, apoiando o desenvolvimento contínuo do **Rayhunter** e a pesquisa sobre privacidade.
- **Faça uma doação direta:** Apoie diretamente o trabalho de defesa da privacidade da EFF e o desenvolvimento do **Rayhunter** por meio de uma **[doação à EFF](https://supporters.eff.org/donate/donate)**.
- **Participe da comunidade:** Contribua com discussões, documentação e testes no repositório oficial do GitHub.

Seu apoio ajuda a manter o **Rayhunter** gratuito, de código aberto e em constante melhoria para enfrentar ameaças de vigilância que evoluem.

## Suporte, comentários e comunidade

**Rayhunter** conta com uma comunidade ativa de pesquisadores de segurança, defensores da privacidade e pessoas preocupadas com o tema. Você encontra suporte e contribui para o projeto em vários canais:

- **Documentação oficial:** [Documentação do Rayhunter](https://efforg.github.io/rayhunter/introduction.html), com guias completos de instalação, configuração e uso.
- **Repositório GitHub:** [EFForg/rayhunter](https://github.com/EFForg/rayhunter)
- **Discussões da comunidade:** Abra discussões no GitHub sobre compatibilidade de dispositivos e solução de problemas.
- **Pesquisa de segurança:** Colabore com pesquisadores para melhorar os recursos de detecção do **Rayhunter**.

Se você procura dispositivos compatíveis, há opções de **[Rayhunter à venda](https://stscollective.com/collections/rayhunter)** na STS Collective.

## Perguntas frequentes

### Preciso de um cartão SIM ativo para usar Rayhunter?

**Rayhunter** exige que haja um cartão SIM no dispositivo, mas o cartão não precisa ter um plano de serviço ativo. O SIM permite que o dispositivo se conecte às redes celulares e monitore atividades suspeitas. Se você também quiser usar o dispositivo como hotspot enquanto executa o **Rayhunter**, precisará de um plano ativo.

### Como posso testar se meu dispositivo Rayhunter está funcionando?

Ative a heurística de teste nas configurações do **Rayhunter**. Ela gera alertas sempre que o dispositivo detecta uma torre celular, permitindo confirmar que o sistema funciona. Esse modo gera muitos alertas, então desative-o após o teste.

### Devo comprar um dispositivo bloqueado ou desbloqueado?

Para ter compatibilidade com **Rayhunter**, dispositivos desbloqueados costumam ser a melhor opção, principalmente se você pretende usar cartões SIM que não sejam da Verizon. Muitos Orbic da Verizon já vêm desbloqueados, mas confirme a compatibilidade antes da compra. Você encontra dispositivos compatíveis verificados **[à venda como Rayhunter](https://stscollective.com/collections/rayhunter)** na STS Collective.

{{< stscollective-ad "rayhunter" >}}

## Guia de instalação

### Instalação da versão mais recente

A instalação do **Rayhunter** foi testada no macOS e no Ubuntu 24.04. Se houver problemas com os pacotes pré-compilados, talvez seja necessário instalar a partir do código-fonte.

#### Pré-requisitos

Antes de instalar o **Rayhunter**, confirme que você tem um dispositivo compatível. Em dispositivos TP-Link, insira um cartão SD formatado em FAT para armazenar gravações.

#### Download e configuração

1. **Baixe a versão mais recente:** Baixe o arquivo `rayhunter-vX.X.X-PLATFORM.zip` adequado na página oficial de versões:
   - Linux x64: `linux-x64`
   - Linux ARM64: `linux-aarch64`
   - Linux ARM v7/v8: `linux-armv7`
   - macOS Intel: `macos-intel`
   - macOS ARM (M1/M2): `macos-arm`
   - Windows: `windows-x86_64`

2. **Extraia o arquivo e acesse a pasta:**
   ```bash
   unzip ~/Downloads/rayhunter-vX.X.X-PLATFORM.zip
   cd ~/Downloads/rayhunter-vX.X.X-PLATFORM
   ```

3. **Conecte ao dispositivo:** Ligue o aparelho e conecte-se por WiFi ou tethering USB. Você deve conseguir acessar:
   - Dispositivos Orbic: `http://192.168.1.1`
   - Dispositivos TP-Link: `http://192.168.0.1`

#### Instalação específica para cada dispositivo

**Dispositivos Orbic RC400L** (disponíveis **[à venda como Rayhunter](https://stscollective.com)**):

O **Rayhunter** oferece dois métodos de instalação nos dispositivos Orbic RC400L. O método WiFi é recomendado para a maioria das pessoas. O método USB oferece recursos adicionais de depuração.

**Instalação por WiFi (recomendada):**
```bash
# Usuários do macOS devem executar isto primeiro:
xattr -d com.apple.quarantine installer

# Verizon RC400L (a senha administrativa é igual à senha do WiFi):
./installer orbic --admin-password 'YourWiFiPassword'

# Kajeet/Smartspot RC400L:
./installer orbic --admin-password='$m@rt$p0tc0nf!g'

# Dispositivos Moxee (formato da senha: 12$ + os três últimos dígitos da senha do WiFi):
./installer orbic --admin-password='12$XXX'
```

**Instalação por USB (usuários avançados):**
```bash
# AVISO: o instalador USB não é recomendado para a maioria dos usos
./installer orbic-usb
```

Este método força o dispositivo a entrar no modo de depuração para habilitar o acesso ADB, instala o rootshell e o **Rayhunter** e reinicia o aparelho. Use esse método somente se precisar do ADB para outros fins.

**Dispositivos TP-Link M7350** (disponíveis **[à venda como Rayhunter](https://stscollective.com)**):
```bash
./installer tplink
```

O instalador conclui a instalação do **Rayhunter** e reinicia o dispositivo. Uma linha verde na tela indica que o **Rayhunter** está funcionando.

### Instalação a partir do código-fonte

Para desenvolvedores ou pessoas que precisam compilar o **Rayhunter** a partir do código-fonte, o projeto inclui:

- **Frontend:** aplicação JavaScript SvelteKit (`./daemon/web/`)
- **Backend:** binário Rust `rayhunter-daemon` (`./daemon/`)
- **Instalador:** binário Rust que reúne tudo (`./installer`)

#### Dependências de compilação

Instale:
- Linguagem de programação Rust
- Node.js/npm
- Ferramentas de compilação C (`build-essential` no Linux, `xcode-select --install` no macOS)

#### Processo de compilação

```bash
./scripts/build-dev.sh
./scripts/install-dev.sh orbic  # Substitua 'orbic' pelo tipo do dispositivo
```

Para desenvolver o frontend com atualização automática:
```bash
cd daemon/web
npm run dev
# Ou com um destino personalizado:
API_TARGET=http://192.168.1.1:8080 npm run dev
```

### Atualização do Rayhunter

A atualização do **Rayhunter** é igual à instalação. Repita os passos de instalação com a versão mais recente para atualizar o dispositivo para a versão mais nova do **Rayhunter**.

## Configuração

Você pode configurar o **Rayhunter** pela interface web ou editar `/data/rayhunter/config.toml` diretamente no dispositivo.

### Configuração pela interface web

Conecte-se à rede do dispositivo e abra a interface web do **Rayhunter**:
- Orbic: `http://192.168.1.1:8080`
- TP-Link: `http://192.168.0.1:8080`

{{< figure src="rayhunter-dashboard.webp" alt="Painel da interface web do Rayhunter" caption="A interface web do Rayhunter oferece opções abrangentes de monitoramento e configuração" >}}

#### Principais opções de configuração

**Nível da interface do dispositivo:** Controla o que o **Rayhunter** mostra na tela:
- **Modo invisível:** Não exibe nada.
- **Modo discreto:** Mostra uma linha colorida (verde=seguro, vermelho=alerta, branco=pausado).
- **Modo de demonstração:** Exibe gráficos de orca com uma linha de status.
- **Logotipo da EFF:** Exibe o logotipo da EFF com uma linha de status.
- **Alta visibilidade:** Exibe cores em tela cheia.

**Modo de entrada do dispositivo:** Configura o comportamento do botão liga/desliga:
- **Desativar controle pelo botão:** Desativa o botão liga/desliga para o **Rayhunter**.
- **Toque duplo para reiniciar gravação:** Limpa os alertas e reinicia o monitoramento.

**Configurações de notificação:** Configure o URL do ntfy para alertas remotos e habilite ou desabilite notificações de aviso e bateria fraca.

**Heurísticas do analisador:** Habilite ou desabilite algoritmos de detecção específicos do **Rayhunter** conforme o ambiente e o modelo de ameaça.

## Desinstalação do Rayhunter

### Dispositivos Orbic

Para remover o **Rayhunter** dos dispositivos Orbic:

```bash
./installer util orbic-shell --admin-password mypassword
```

No shell:

> **Aviso:** Os comandos a seguir removem permanentemente os arquivos do Rayhunter e os ganchos de inicialização. Confirme que você está no shell do dispositivo correto, copie gravações ou configurações que queira guardar e mantenha o instalador e o firmware compatível disponíveis antes de continuar. Depois, confirme que os arquivos foram removidos e que o dispositivo reinicia sem o serviço Rayhunter. Para reverter, reinstale a versão correspondente do repositório oficial.

```bash
echo 3 > /usrdata/mode.cfg
rm -rf /data/rayhunter /etc/init.d/rayhunter_daemon /bin/rootshell
reboot
```

### Dispositivos TP-Link

Para desinstalar o Rayhunter de dispositivos TP-Link:

> **Aviso:** Estes comandos removem arquivos do Rayhunter e seu gancho de inicialização do dispositivo TP-Link. Exporte as gravações e configurações primeiro. Execute-os somente no shell do aparelho e depois confirme que os caminhos foram removidos e que o dispositivo inicia normalmente. Para reverter, reinstale a versão correspondente do repositório oficial.

```bash
./installer util tplink-shell
rm /data/rayhunter /etc/init.d/rayhunter_daemon
update-rc.d rayhunter_daemon remove
```

Remova qualquer acionador de porta restante na interface administrativa TP-Link em Settings > NAT Settings > Port Triggers.

## Como usar o Rayhunter

Após a instalação, o **Rayhunter** inicia automaticamente e monitora continuamente redes celulares em busca de atividade suspeita. A tela do dispositivo mostra uma linha verde durante a operação normal; ela muda para pontos amarelos, traços laranja ou uma linha vermelha contínua quando há um possível capturador de IMSI.

### Heurísticas de detecção do Rayhunter

O **Rayhunter** usa vários algoritmos sofisticados para identificar atividade possivelmente relacionada a capturadores de IMSI:

#### Detecção de solicitação de IMSI

Esta heurística identifica sequências suspeitas nas quais torres celulares solicitam a identidade do dispositivo (IMSI, Identidade Internacional de Assinante Móvel) sem seguir os procedimentos corretos de autenticação. O **Rayhunter** monitora o momento e o contexto dessas solicitações e sinaliza padrões anormais que indicam possível equipamento de vigilância.

Redes celulares legítimas seguem procedimentos padronizados de autenticação antes de solicitar identificadores confidenciais. Capturadores de IMSI costumam ignorar esses procedimentos para coletar rapidamente as identidades dos dispositivos, criando anomalias detectáveis na sequência de autenticação. Este método é particularmente eficaz contra capturadores de IMSI “passivos” básicos, que apenas coletam informações do dispositivo.

#### Detecção de liberação de conexão/rebaixamento para 2G

O **Rayhunter** monitora continuamente tentativas suspeitas de desconectar dispositivos móveis de redes 4G/5G seguras e reconectá-los a redes 2G menos seguras. Esse ataque de rebaixamento é comum entre capturadores de IMSI, pois redes 2G têm criptografia mais fraca e são mais fáceis de interceptar.

O sistema analisa padrões de liberação de conexão em busca de frequência, momento ou contexto anormais que indiquem intenção maliciosa, em vez de otimização normal da rede. Redes legítimas às vezes sugerem rebaixamentos por motivos de cobertura ou capacidade, mas o **Rayhunter** consegue distinguir esse comportamento de possíveis atividades de vigilância.

#### Detecção de rebaixamento LTE SIB6/7

Blocos de Informação do Sistema (SIB) são mensagens de transmissão usadas por redes celulares para enviar dados de configuração a dispositivos móveis. O **Rayhunter** monitora especificamente as mensagens SIB6 e SIB7, que contêm informações sobre células vizinhas e redirecionamento de frequência.

Atores maliciosos podem transmitir mensagens SIB6/7 falsas para levar dispositivos a abandonar conexões 4G seguras e se conectar a redes 2G controladas pelo invasor. O **Rayhunter** analisa essas transmissões em busca de inconsistências, padrões anormais de redirecionamento e outros sinais de estações-base clandestinas tentando rebaixar conexões para interceptar comunicações.

#### Detecção de cifra nula

Este método essencial identifica quando uma rede celular sugere não usar criptografia (cifra nula) nas comunicações. Redes celulares comerciais legítimas nunca devem propor conexões sem criptografia, pois isso violaria normas de segurança e exigências regulatórias.

O **Rayhunter** sinaliza como altamente suspeita qualquer rede que proponha o uso de cifra nula. *Uma rede legítima nunca proporá cifra nula.* Isso indica claramente que um equipamento de vigilância tenta interceptar comunicações em texto puro. Esta heurística é particularmente eficaz contra capturadores de IMSI que priorizam a coleta de dados e não tentam parecer operações legítimas.

#### Detecção de SIB incompleto

Estações-base celulares legítimas transmitem blocos de informação do sistema completos, com dados essenciais de configuração da rede. O **Rayhunter** monitora estações-base que fornecem informações incompletas ou ausentes, algo que muitas vezes indica equipamento de vigilância implantado às pressas ou configurado incorretamente.

Capturadores de IMSI frequentemente não implementam todas as funções de uma rede celular. Eles se concentram nos recursos mínimos para conectar dispositivos e interceptar dados. Detectando implementações incompletas, o **Rayhunter** identifica estações-base possivelmente maliciosas sem o conjunto completo de recursos esperado da infraestrutura legítima.

{{< figure src="rayhunter-heuristics-overview.webp" alt="Diagrama que resume cinco heurísticas de detecção do Rayhunter: solicitação de IMSI sem autenticação, ataque de rebaixamento para 2G, redirecionamento LTE SIB6/7, proposta de cifra nula e transmissão incompleta de informações do sistema" >}}

## Agentes de ameaça e possíveis alvos

Entender quem implanta capturadores de IMSI e quem eles visam é essencial para avaliar seu modelo pessoal de ameaça e escolher configurações adequadas do **Rayhunter**. Os agentes de ameaça têm níveis variados de sofisticação, e suas estratégias ajudam a definir quais atividades de vigilância o **Rayhunter** procura detectar.

### Órgãos governamentais e forças policiais

**Sofisticação da ameaça:** avançada a profissional
**Alvos principais:**
- Suspeitos sob investigação criminal
- Pessoas de interesse em casos de segurança nacional
- Manifestantes e ativistas em protestos
- Vigilância da população em áreas de alta segurança
- Estrangeiros e representantes diplomáticos

**Padrões de detecção:** Capturadores de IMSI operados pelo governo podem usar equipamentos sofisticados que não acionam heurísticas básicas. Mesmo assim, costumam empregar **ataques de rebaixamento para 2G** e **padrões de liberação de conexão** para forçar dispositivos a usar redes menos seguras, facilitando a interceptação. A detecção de rebaixamento LTE SIB6/7 e o monitoramento de liberação de conexão do **Rayhunter** são particularmente úteis contra técnicas de vigilância policial.

**Cenários comuns:**
- Vigilância durante protestos, manifestações ou reuniões públicas
- Monitoramento perto de instalações governamentais ou infraestrutura sensível
- Vigilância direcionada de pessoas específicas sob investigação
- Operações de vigilância em fronteiras e aeroportos

### Agências de inteligência nacionais e estrangeiras

**Sofisticação da ameaça:** profissional a militar
**Alvos principais:**
- Agentes e recursos de inteligência estrangeiros
- Autoridades governamentais e diplomáticas
- Contratados e pesquisadores de defesa
- Executivos de empresas em setores estratégicos
- Jornalistas que cobrem segurança nacional
- Ativistas envolvidos em temas políticos sensíveis

**Padrões de detecção:** Equipamentos de nível de inteligência são projetados para permanecer discretos, mas a detecção de cifra nula e o monitoramento de SIB incompleto do **Rayhunter** podem identificar até algumas operações sofisticadas. Agências de inteligência costumam usar equipamentos que solicitam informações de **IMSI** em operações direcionadas, acionando os algoritmos de detecção de solicitação de IMSI do **Rayhunter**.

**Cenários comuns:**
- Vigilância prolongada de alvos de inteligência de alto valor
- Espionagem industrial perto de sedes corporativas
- Monitoramento diplomático e de embaixadas
- Operações de contrainteligência
- Serviços de inteligência estrangeiros visando ativos nacionais

### Organizações criminosas

**Sofisticação da ameaça:** básica a intermediária
**Alvos principais:**
- Pessoas ricas visadas para sequestro ou extorsão
- Concorrentes comerciais, para obter inteligência corporativa
- Agentes da lei que investigam o crime organizado
- Testemunhas e informantes em casos criminais
- Vítimas de perseguição, assédio ou violência doméstica

**Padrões de detecção:** Organizações criminosas normalmente usam capturadores de IMSI mais baratos e disponíveis comercialmente, que acionam várias heurísticas do **Rayhunter** ao mesmo tempo. Esses dispositivos costumam ter **implementações SIB incompletas**, usar **cifras nulas** para maximizar a coleta de dados e empregar ataques agressivos de **rebaixamento para 2G** por causa da sofisticação técnica limitada.

**Cenários comuns:**
- Monitoramento de possíveis alvos de sequestro ou roubo
- Monitoramento das comunicações policiais durante operações criminosas
- Espionagem industrial e coleta de inteligência competitiva
- Campanhas de perseguição e assédio
- Intimidação de testemunhas e rastreamento de localização

### Espionagem corporativa e inteligência privada

**Sofisticação da ameaça:** intermediária a avançada
**Alvos principais:**
- Lideranças de empresas concorrentes
- Equipes de pesquisa e desenvolvimento
- Negociadores de fusões e aquisições
- Titulares de propriedade intelectual
- Guardiões de segredos comerciais
- Denunciantes corporativos e fontes de ameaças internas

**Padrões de detecção:** Operações corporativas de vigilância costumam usar equipamentos intermediários que equilibram preço e capacidade. Esses recursos frequentemente acionam a **detecção de liberação de conexão** e os **alertas de solicitação de IMSI** ao visar pessoas específicas durante negociações comerciais ou ciclos de desenvolvimento de produtos.

**Cenários comuns:**
- Vigilância durante negociações de fusões e aquisições
- Coleta de inteligência competitiva em feiras e conferências
- Operações de roubo de propriedade intelectual
- Monitoramento de funcionários e detecção de ameaças internas
- Coleta de dados de clientes para obter vantagem competitiva

### Investigadores particulares e empresas de vigilância

**Sofisticação da ameaça:** básica a intermediária
**Alvos principais:**
- Pessoas investigadas por fraude em seguros
- Cônjuges em processos de divórcio
- Funcionários suspeitos de má conduta
- Pessoas envolvidas em disputas legais
- Celebridades e alvos de grande visibilidade

**Padrões de detecção:** Operações de vigilância particulares geralmente usam equipamentos comerciais com pouca personalização. Por limites de custo e capacidade técnica, esses sistemas costumam acionar as heurísticas básicas de detecção do **Rayhunter**, especialmente a **detecção de cifra nula** e o **monitoramento de SIB incompleto**.

**Cenários comuns:**
- Investigações de divórcio e custódia
- Vigilância por fraude de seguro
- Investigações de má conduta de funcionários
- Perseguição de celebridades e operações de paparazzi
- Investigação de casos e coleta de evidências

### Indivíduos mal-intencionados e hacktivistas

**Sofisticação da ameaça:** básica a intermediária
**Alvos principais:**
- Inimigos pessoais ou interesses românticos
- Figuras públicas e celebridades
- Vítimas aleatórias em locais públicos
- Participantes de eventos ou locais específicos
- Membros de comunidades ou grupos visados

**Padrões de detecção:** Indivíduos normalmente usam configurações básicas ou improvisadas de capturadores de IMSI, que acionam vários algoritmos de detecção do **Rayhunter**. Essas instalações frequentemente usam **cifra nula**, transmitem **SIB incompleto** e tentam ataques rudimentares de **rebaixamento para 2G**.

**Cenários comuns:**
- Campanhas de perseguição e assédio
- Roubo de identidade e fraude financeira
- Ativismo político e interrupção de protestos
- Atividades de cibercrime em geral
- Vigilância oportunista em eventos públicos

### Avaliação de ameaças e configuração do Rayhunter

**Pessoas de alto risco** (jornalistas, ativistas, autoridades e executivos) devem habilitar todas as heurísticas do **Rayhunter** e usar o modo de exibição de **alta visibilidade** para obter a detecção máxima.

**Pessoas de risco moderado** (usuários em geral que valorizam a privacidade) podem usar o modo de exibição **discreto**, mantendo habilitadas as heurísticas de detecção principais para proteção diária sem atrair atenção.

**Proteção em eventos** (protestos, reuniões sensíveis, viagens) justifica habilitar temporariamente todos os métodos de detecção e sistemas de notificação para obter maior consciência sobre vigilância.

Entender seu modelo de ameaça ajuda a otimizar a configuração do **Rayhunter** conforme seu perfil de risco e a manter cobertura de detecção adequada contra os agentes de ameaça com maior probabilidade de visar você ou suas atividades.

{{< figure src="imsi-catcher-threat-actors-surveillance.webp" alt="Diagrama que mostra agentes de ameaça de capturadores de IMSI, como órgãos governamentais, organizações criminosas e operadores de espionagem corporativa, visando dispositivos móveis" >}}

## Eficácia do Rayhunter na era 5G

{{< figure src="rayhunter-5g-downgrade-attack-persistence.webp" alt="Diagrama que mostra um telefone compatível com 5G sendo forçado por um ataque de rebaixamento a usar uma rede 4G ou 3G monitorada, técnica que o Rayhunter continua detectando na era 5G" >}}

À medida que as redes celulares passam à tecnologia 5G, surgem dúvidas sobre a eficácia contínua do **Rayhunter**, que detecta redes 2G, 3G e 4G/LTE, mas não os métodos nativos de vigilância 5G. Entender as limitações atuais e a utilidade do **Rayhunter** em um mundo 5G é importante para planejar estratégias de detecção de vigilância a longo prazo.

### Por que o Rayhunter continua eficaz em redes 5G

#### Persistência dos ataques de rebaixamento

A principal via de ataque detectada pelo **Rayhunter**, que força dispositivos a se conectarem a redes menos seguras, continua relevante em redes 5G. **Capturadores de IMSI continuam dependendo de ataques de rebaixamento para 2G e 3G**, porque:

- **Menor custo de implementação:** Criar equipamento de vigilância para protocolos antigos exige muito menos investimento que desenvolver sistemas compatíveis com 5G.
- **Compatibilidade mais ampla com dispositivos:** Visar redes 2G/3G permite monitorar dispositivos antigos que talvez não sejam compatíveis com 5G.
- **Métodos de ataque conhecidos:** Técnicas de vigilância em redes 2G/3G têm documentação e testes extensos.
- **Vantagens regulatórias:** Algumas tecnologias antigas podem enfrentar menos restrições legais do que métodos avançados de interceptação 5G.

#### Compatibilidade retroativa da rede

Redes 5G mantêm **compatibilidade retroativa com 4G/LTE**, e a maioria dos dispositivos móveis é compatível com várias gerações ao mesmo tempo. Essa compatibilidade cria oportunidades contínuas para os ataques de rebaixamento que o **Rayhunter** detecta:

- **Mecanismos automáticos de retorno:** Dispositivos voltam naturalmente ao 4G quando a cobertura 5G é fraca, criando oportunidades de interceptação durante a transição.
- **Vulnerabilidades na negociação de protocolos:** O handshake entre gerações da rede pode ser manipulado por capturadores de IMSI sofisticados.
- **Exploração de lacunas de cobertura:** Equipamentos de vigilância implantados estrategicamente em áreas sem cobertura 5G completa podem forçar dispositivos a usar redes 4G/LTE monitoradas.

#### Cronograma gradual de implantação do 5G

A **lentidão na expansão da cobertura 5G completa** garante que o **Rayhunter** continue relevante por vários anos:

- **Diferenças entre áreas urbanas e rurais:** Muitas regiões ainda dependem principalmente de redes 4G/LTE, nas quais a detecção do **Rayhunter** se aplica diretamente.
- **Limitações de cobertura interna:** Sinais 5G têm dificuldade para atravessar edifícios, levando dispositivos a voltar para redes 4G que o **Rayhunter** consegue monitorar.
- **Considerações sobre viagens internacionais:** A implantação global do 5G varia muito entre países, então a vigilância 4G/LTE continua sendo uma preocupação para viajantes.

#### Atraso tecnológico dos agentes de ameaça

Os ciclos de **aquisição e implantação de equipamentos de vigilância** costumam ficar atrás da tecnologia comercial de rede:

- **Prazos de aquisição governamental:** Órgãos policiais e de inteligência talvez continuem usando por vários anos equipamentos atuais compatíveis com 4G, mesmo depois da implantação do 5G.
- **Análise de custo-benefício:** Muitas operações atingem seus objetivos com interceptação 4G/LTE mais barata, reduzindo o incentivo para migrar a sistemas 5G.
- **Requisitos de formação e conhecimento:** Operar equipamentos de vigilância 5G exige conhecimentos especializados que as organizações podem levar algum tempo para desenvolver.

### Limitações do Rayhunter em ambientes 5G verdadeiros

#### Pontos cegos de vigilância 5G nativa

*Esta é a principal limitação do Rayhunter.* **O Rayhunter não detecta operações nativas de capturadores IMSI 5G que não dependam de ataques de rebaixamento:**

- **Redes 5G standalone (SA):** Quando dispositivos se conectam a redes totalmente 5G sem voltar ao 4G, o **Rayhunter** não consegue monitorar essas comunicações.
- **Equipamentos avançados de vigilância 5G:** Agentes de ameaça sofisticados com acesso a tecnologia avançada podem interceptar comunicações 5G sem acionar as heurísticas de detecção do **Rayhunter**.
- **Exploração de network slicing:** Os recursos de fatiamento de rede do 5G podem ser abusados para vigilância de formas que o **Rayhunter** não detecta.

#### Recursos aprimorados de segurança 5G

As redes 5G incorporam **medidas de segurança melhores**, que podem reduzir a eficácia de técnicas tradicionais de vigilância:

- **Protocolos de criptografia mais fortes:** O 5G usa padrões de criptografia mais robustos e difíceis de quebrar que os das gerações anteriores.
- **Procedimentos de autenticação aprimorados:** A autenticação melhorada dos dispositivos no 5G pode dificultar a coleta de IMSI.
- **Monitoramento de segurança de rede:** A infraestrutura 5G inclui melhores recursos de detecção de intrusão, capazes de identificar e combater tentativas de vigilância.

#### Mudanças no comportamento dos dispositivos

Com a popularização do 5G, **o comportamento dos dispositivos móveis pode mudar** e afetar a capacidade de detecção do **Rayhunter**:

- **Menor disposição para rebaixar:** Atualizações futuras de software podem aumentar a resistência dos dispositivos a ataques de rebaixamento.
- **Preferência por conexões 5G:** Dispositivos podem priorizar cada vez mais o 5G e desconfiar de solicitações para usar protocolos antigos.
- **Maior consciência de segurança:** Sistemas operacionais móveis podem implementar melhores recursos para detectar comportamento de rede suspeito.

### Considerações estratégicas para implantar o Rayhunter

#### Recomendações atuais

Para implantação imediata e a curto prazo, o **Rayhunter** oferece **recursos abrangentes de detecção de vigilância**:

- **Uso urbano:** Mesmo em grandes cidades com ampla cobertura 5G, o **Rayhunter** detecta tentativas de vigilância direcionadas às redes 4G/LTE.
- **Proteção em eventos críticos:** Em protestos, reuniões sensíveis ou atividades de alto risco, o **Rayhunter** oferece detecção importante independentemente da cobertura 5G.
- **Segurança em viagens:** O **Rayhunter** continua muito eficaz para detectar vigilância em viagens nacionais e internacionais.

#### Estratégias para preparar-se para o futuro

Organizações e indivíduos que planejam detecção de vigilância a longo prazo devem considerar:

- **Abordagens híbridas de detecção:** Combinar o **Rayhunter** com outras ferramentas e técnicas de monitoramento oferece cobertura abrangente em várias vias de ameaça.
- **Atualizações regulares da avaliação de ameaças:** Acompanhar a evolução da tecnologia de vigilância ajuda a decidir quando complementar ou substituir o **Rayhunter**.
- **Apoio ao desenvolvimento comunitário:** Apoiar o desenvolvimento de código aberto do **Rayhunter** aumenta a chance de recursos de detecção 5G serem adicionados em versões futuras.

#### Acompanhamento da evolução tecnológica

A comunidade do **Rayhunter** e a EFF continuam pesquisando recursos de **detecção de vigilância 5G**:

- **Pesquisa de análise de protocolos:** Pesquisas contínuas de protocolos 5G podem revelar novas oportunidades de detecção para versões futuras do **Rayhunter**.
- **Estudos de compatibilidade de hardware:** Avaliam se os dispositivos compatíveis atuais podem ser aprimorados para detectar tentativas de vigilância 5G com **Rayhunter**.
- **Monitoramento do cenário de ameaças:** Acompanhar o desenvolvimento e a implantação de equipamentos de vigilância 5G orienta prioridades futuras do **Rayhunter**.

O **Rayhunter** continua sendo uma **ferramenta essencial de detecção de vigilância** no cenário atual de telecomunicações, e deve permanecer relevante por vários anos à medida que o 5G avança gradualmente e agentes de ameaça continuam usando métodos conhecidos de ataque de rebaixamento.

### Reanálise de gravações

O **Rayhunter** melhora continuamente seus recursos de detecção. Você pode reanalisar gravações antigas com heurísticas atualizadas clicando em “N warnings” na interface web e escolhendo “re-analyze”.

### Análise em computadores

Para usuários avançados, o **Rayhunter** inclui `rayhunter-check`, uma ferramenta de linha de comando para analisar arquivos PCAP e QMDL em computadores:

```bash
rayhunter-check -p ~/Downloads/myfile.qmdl
rayhunter-check -p ~/Downloads/myfile.pcap
rayhunter-check -d -p ~/Downloads/myfile.qmdl  # Modo de depuração
```

## Dispositivos compatíveis

O **Rayhunter** é compatível com vários hotspots móveis que usam modems Qualcomm com a interface `/dev/diag` disponível.

{{< figure src="/img/rayhunter-device-regions.svg" alt="Compatibilidade de dispositivos Rayhunter por região" caption="Compatibilidade de dispositivos e recomendações regionais para instalações do Rayhunter" >}}

### Dispositivos recomendados

Estes dispositivos passaram por testes extensos e são bastante usados na comunidade **Rayhunter**:

#### Orbic RC400L (às vezes vendido como Kajeet RC400L)
- **Região recomendada:** Américas
- **Bandas compatíveis:**
  - 5G: n260/n261, n77, n2/5/48/66
  - 4G: 2/4/5/12/13/48/66
  - Global e roaming: n257/n78
- **Disponibilidade:** **[Novo Rayhunter Orbic RC400L](https://stscollective.com/products/new-rayhunter-orbic-rc400l-imsi-catcher-detector-premium?variant=51361976811822)** e **[Kajeet RC400L](https://stscollective.com/products/rayhunter-imsi-catcher-detector-kajeet-rc400lx-4g-lte-hotspot?variant=51411271844142)**, dispositivos compatíveis disponíveis.
- **Faixa de preços:** Modelos profissionais disponíveis pela STS Collective.

#### TP-Link M7350
- **Região recomendada:** África, Europa e Oriente Médio (também funciona nas Américas, mas normalmente custa mais).
- **Requisitos especiais:** Precisa de um cartão SD formatado em FAT para gravações.
- **Disponibilidade:** **[TP-Link M7350 Rayhunter](https://stscollective.com/collections/rayhunter)**, com modelos compatíveis verificados.

### Dispositivos funcionais

Foi confirmado que o **Rayhunter** também funciona nos dispositivos:

- **Wingtech CT2MHS01** (Américas), **[Rayhunter à venda](https://stscollective.com/collections/rayhunter)**
- **Tmobile TMOHS1** (Américas), **[Rayhunter à venda](https://stscollective.com/collections/rayhunter)**
- **TP-Link M7310** (África, Europa, Oriente Médio), **[Rayhunter à venda](https://stscollective.com)**
- **PinePhone e PinePhone Pro** (global), **[Rayhunter à venda](https://stscollective.com)**
- **FY UZ801** (Ásia, Europa), **[Rayhunter à venda](https://stscollective.com)**
- **Hotspot Moxee** (Américas), **[Moxee K779HSDL Rayhunter](https://stscollective.com/products/rayhunter-imsi-catcher-stingray-detector-moxee-k779hsdl-hotspot-professionally-refurbished-pre-installed-4g-lte-cellular-threat-detection-device?variant=51309010420014)**

### Observações de instalação por dispositivo

#### Orbic/Kajeet RC400L

O Orbic RC400L é o dispositivo original para o qual o **Rayhunter** foi desenvolvido. Está disponível **[à venda como Rayhunter](https://stscollective.com)** na STS Collective.

**Métodos de instalação:**
- **Pela rede:** `./installer orbic` (recomendado, funciona por WiFi)
- **Por USB:** `./installer orbic-usb` (oferece acesso ADB e shell root)

**Senhas padrão:**
- **Verizon RC400L:** A senha administrativa é sempre a mesma do WiFi (veja o menu do aparelho).
- **Kajeet/Smartspot RC400L:** `$m@rt$p0tc0nf!g`
- **Dispositivos Moxee:** A senha segue o formato `12$XXX`, em que XXX são os últimos três dígitos da senha do WiFi (veja a senha sob a bateria).

**Acesso ao shell:** Use `./installer util orbic-shell` após a instalação.

#### TP-Link M7350/M7310

Estes aparelhos executam o **Rayhunter** de modo confiável e estão **[à venda como Rayhunter](https://stscollective.com)**.

**Instalação:** `./installer tplink` (não exige senha administrativa)
**Armazenamento:** Insira um cartão SD formatado em FAT antes da instalação
**Acesso ao shell:** `./installer util tplink-shell`

#### Dispositivos especializados

**PinePhone e PinePhone Pro:** Compatibilidade global, **[Rayhunter à venda](https://stscollective.com)**
**UZ801:** Popular nas regiões da Ásia e Europa, **[Rayhunter à venda](https://stscollective.com)**
**Wingtech CT2MHS01:** Aparelho voltado às Américas, **[Rayhunter à venda](https://stscollective.com)**

### Adição de novos dispositivos

O **Rayhunter** talvez seja compatível com qualquer aparelho que tenha um modem Qualcomm com a interface `/dev/diag`. Se quiser que o **Rayhunter** seja compatível com outro aparelho, abra uma discussão no repositório oficial do GitHub.

## Documentação da API REST

O **Rayhunter** oferece uma API REST abrangente para acessar programaticamente o estado, as gravações e a configuração do dispositivo. A API permite integração com outras ferramentas de segurança e sistemas de monitoramento automatizado.

### Documentação oficial da API

Para consultar a referência completa da API, incluindo detalhes dos endpoints, exemplos de solicitações e respostas e métodos de autenticação, visite a **[documentação oficial da API REST do Rayhunter](https://efforg.github.io/rayhunter/api-docs/)**.

### Endpoints da API

A API do **Rayhunter** está disponível em `http://[device-ip]:8080/api/` e oferece endpoints para:

- **Estado do sistema:** Monitorar a integridade do dispositivo e a operação do **Rayhunter**
- **Gerenciamento de gravações:** Iniciar, interromper e baixar gravações
- **Consulta de alertas:** Acessar alertas de detecção e resultados da análise
- **Configuração:** Atualizar as opções do **Rayhunter** por código
- **Controle de heurísticas:** Habilitar ou desabilitar algoritmos de detecção específicos
- **Informações do dispositivo:** Consultar especificações e recursos do aparelho
- **Monitoramento da rede:** Acessar dados da rede celular em tempo real
- **Registro de eventos:** Consultar eventos e alertas de detecção anteriores

### Autenticação

O acesso à API usa a mesma autenticação da interface web. Proteja corretamente o dispositivo **Rayhunter** e permita acesso somente a usuários autorizados.

### Exemplos de integração

A API REST do **Rayhunter** pode ser integrada a várias plataformas de monitoramento de segurança, sistemas SIEM e ferramentas de automação personalizadas. Consulte a **[documentação oficial da API](https://efforg.github.io/rayhunter/api-docs/)** para ver exemplos completos de implementação e boas práticas.

## Solução de problemas

### Problemas comuns de instalação

**Problemas de conexão USB:** Teste outros cabos ou portas USB. Conexões defeituosas frequentemente causam falhas de instalação. *Esta é a causa mais comum de falhas na instalação.*

**Problemas de segurança no macOS:** Se aparecer “No Orbic device found”, altere temporariamente “Allow accessories to connect” para “Always” nas configurações de segurança.

**Detecção do dispositivo:** Após a instalação, habilite a heurística de teste para confirmar que o **Rayhunter** funciona.

### Como obter ajuda

Para suporte de instalação e solução de problemas:
- Consulte a documentação oficial do **Rayhunter**.
- Use `./installer --help` e `./installer util --help` para ver as opções dos comandos.
- Participe das discussões no GitHub para receber apoio da comunidade.
- Entre em contato com a **[STS Collective](https://stscollective.com)** para tirar dúvidas sobre compatibilidade.

## Perguntas frequentes (FAQ)

### Perguntas gerais

#### O que é um capturador de IMSI e como funciona?

Um capturador de IMSI (também chamado StingRay, simulador de estação celular ou torre falsa) é um equipamento de vigilância que imita torres celulares legítimas para interceptar as comunicações de dispositivos móveis. Ele força os aparelhos próximos a se conectar ao equipamento malicioso em vez de usar torres legítimas. Assim, os operadores podem coletar identificadores de dispositivos (números IMSI), dados de localização, metadados de chamadas e, possivelmente, interceptar comunicações. O **Rayhunter** detecta esses equipamentos ao identificar padrões anormais de comportamento da rede celular.

#### Rayhunter detecta todos os tipos de equipamento de vigilância?

O **Rayhunter** detecta especificamente capturadores de IMSI e simuladores de estação celular que operam em redes 2G, 3G e 4G/LTE. Ele não detecta outros tipos de vigilância, como monitoramento WiFi, rastreadores GPS, vigilância física ou vigilância nativa em 5G sem ataques de rebaixamento. O **Rayhunter** é um componente de uma estratégia abrangente de proteção da privacidade.

#### É legal usar Rayhunter?

O uso do **Rayhunter** é legal na maioria das jurisdições, pois ele é uma ferramenta passiva de monitoramento que não interfere em redes celulares nem em outros dispositivos. Ele apenas analisa os sinais celulares recebidos naturalmente pelo seu aparelho. As leis variam, portanto verifique as regras locais. A EFF desenvolveu o **Rayhunter** como uma ferramenta legítima de proteção da privacidade.

### Perguntas técnicas

#### Por que o Rayhunter precisa de um cartão SIM se não requer um serviço ativo?

O cartão SIM fornece a Identidade Internacional de Assinante Móvel (IMSI), necessária para autenticar o dispositivo nas redes celulares e participar das trocas de protocolo celular monitoradas pelo **Rayhunter**. Sem um SIM, o aparelho não se conecta às redes celulares, e o **Rayhunter** não tem atividades de rede para analisar em busca de padrões suspeitos.

#### Quantos dados o Rayhunter consome durante a operação normal?

O **Rayhunter** usa poucos dados no monitoramento básico, pois analisa principalmente informações do protocolo celular, e não o tráfego da internet. Porém, o consumo aumenta se você habilitar notificações remotas via ntfy ou usar o dispositivo como hotspot ao mesmo tempo. O monitoramento em si consome largura de banda insignificante.

#### Posso usar o Rayhunter enquanto o aparelho funciona como hotspot móvel?

Sim, o **Rayhunter** pode funcionar ao mesmo tempo que o dispositivo atua como hotspot móvel. Para isso, é necessário ter um plano de serviço celular ativo. O monitoramento do **Rayhunter** funciona de forma independente do hotspot, embora o uso simultâneo dos recursos consuma mais bateria.

#### Qual é a diferença entre a instalação por WiFi e por USB?

O **método WiFi**, recomendado para a maioria das pessoas, instala o **Rayhunter** pela interface sem fio do dispositivo e oferece os recursos padrão. O **método USB** habilita o Android Debug Bridge (ADB) para usuários avançados que precisam depurar o sistema, mas é mais complexo e desnecessário para instalações comuns.

### Perguntas sobre dispositivos e compatibilidade

#### Por que o Rayhunter funciona apenas em certos dispositivos?

O **Rayhunter** requer modems Qualcomm que exponham a interface `/dev/diag`, que dá acesso às informações do protocolo celular. Por motivos de segurança, a maioria dos dispositivos de consumo não disponibiliza essa interface. Os dispositivos compatíveis foram testados especificamente e funcionam conforme os requisitos do **Rayhunter**.

#### Posso instalar Rayhunter no meu smartphone comum?

Não. O **Rayhunter** não pode ser instalado em smartphones comuns. Ele requer hotspots móveis especializados, com modems Qualcomm específicos que exponham interfaces de diagnóstico. Entre os aparelhos compatíveis estão o Orbic RC400L, o TP-Link M7350 e outros modelos de hotspot móvel.

#### O que acontece se eu tentar instalar Rayhunter em um aparelho incompatível?

O instalador do **Rayhunter** inclui detecção do dispositivo e normalmente se recusa a instalar em hardware incompatível. Forçar a instalação em dispositivos não compatíveis pode danificá-los ou torná-los inoperáveis. Sempre confirme a compatibilidade antes de tentar instalar.

#### Preciso de dispositivos diferentes para cada região?

Sim. As bandas de frequência celular variam por região geográfica. O Orbic RC400L foi otimizado para redes das Américas, enquanto o TP-Link M7350 funciona bem na Europa, África e Oriente Médio. As informações de compatibilidade do **Rayhunter** incluem recomendações regionais para ajudar você a escolher um aparelho adequado à sua localização.

### Perguntas sobre uso e configuração

#### Como saber se meu dispositivo Rayhunter funciona corretamente?

Habilite a heurística de teste nas configurações do **Rayhunter**. Ela gera alertas sempre que o dispositivo detecta uma torre celular, confirmando que o sistema funciona. A tela deve mostrar uma linha verde durante a operação normal. Desative a heurística após a verificação, pois ela gera muitos alertas.

#### O que devo fazer se o Rayhunter emitir um alerta?

Quando o **Rayhunter** detectar atividade suspeita, anote primeiro sua localização e as circunstâncias. A otimização da rede ou problemas com equipamentos podem causar falsos positivos. Se os alertas persistirem no mesmo local ou durante atividades sensíveis, considere mudar de local e consultar os detalhes do alerta na interface web para entender o que foi detectado.

#### Com que frequência devo atualizar o Rayhunter?

**Atualize mensalmente.** Consulte a página de versões para encontrar novas heurísticas e melhorias de compatibilidade, que são adicionadas com frequência. A EFF melhora continuamente os recursos do **Rayhunter** com base nas técnicas de vigilância em evolução. A atualização usa o mesmo processo da instalação inicial.

#### O Rayhunter pode proteger várias pessoas ao mesmo tempo?

O **Rayhunter** detecta capturadores de IMSI nas proximidades e, portanto, pode proteger várias pessoas dentro do alcance (normalmente algumas centenas de metros, dependendo da intensidade do sinal). Mesmo assim, cada pessoa que leva a sério a detecção de vigilância deve considerar usar seu próprio dispositivo **Rayhunter** para obter a máxima proteção e controle da configuração.

### Perguntas sobre segurança e privacidade

#### Usar Rayhunter me torna mais visível para quem vigia?

O **Rayhunter** funciona passivamente e não transmite sinais que permitam que equipamentos de vigilância o identifiquem. Porém, o uso de qualquer ferramenta de segurança indica preocupação com privacidade. Os benefícios da detecção costumam superar os riscos, especialmente para pessoas de alto risco, como jornalistas e ativistas.

#### Equipamentos de vigilância conseguem detectar que estou usando Rayhunter?

O **Rayhunter** é um sistema passivo de monitoramento e não transmite sinais de identificação. Operadores de vigilância não conseguem detectar o uso do **Rayhunter** no nível do protocolo celular. A observação física do dispositivo ou a análise do tráfego de rede podem revelar o uso se as notificações remotas do **Rayhunter** estiverem habilitadas.

#### Que informações o Rayhunter coleta sobre mim?

O **Rayhunter** analisa informações do protocolo celular e armazena alertas de detecção localmente no dispositivo. Ele não coleta informações pessoais, conteúdo de comunicações ou dados de localização além do necessário para os algoritmos de detecção. Todos os dados ficam no dispositivo, a menos que você habilite notificações remotas.

### Perguntas avançadas

#### Posso analisar dados do Rayhunter no computador?

Sim. O **Rayhunter** inclui a ferramenta de linha de comando `rayhunter-check` para analisar arquivos PCAP e QMDL gravados em computadores. Isso permite que usuários avançados façam análises detalhadas de eventos de detecção e investiguem atividades suspeitas usando os recursos completos do computador.

#### Como o Rayhunter funciona em áreas urbanas densas?

Áreas urbanas densas, com muitas torres celulares legítimas, podem aumentar falsos positivos porque a otimização de rede e as transferências entre torres acontecem com mais frequência. Os algoritmos do **Rayhunter** distinguem comportamentos normais da rede de atividades de vigilância, mas usuários em áreas densas talvez precisem ajustar a sensibilidade.

#### O Rayhunter funciona durante viagens internacionais?

A eficácia do **Rayhunter** durante viagens depende da compatibilidade do dispositivo com as bandas celulares locais e os acordos de roaming. Os algoritmos de detecção funcionam globalmente, mas confirme se o aparelho aceita as bandas usadas no destino. O roaming internacional talvez seja necessário para o funcionamento completo.

{{< figure src="rayhunter-faq-privacy-protection.webp" alt="Pessoa analisando alertas do Rayhunter em um laptop enquanto carrega um hotspot móvel em uma área urbana com torres celulares próximas" >}}

______

O **Rayhunter** representa um avanço importante na proteção da privacidade pessoal e na detecção de vigilância. Ao instalar e configurar corretamente o **Rayhunter** em dispositivos compatíveis, você obtém recursos eficazes para detectar capturadores de IMSI e proteger suas comunicações móveis contra vigilância não autorizada.

Seja você jornalista, ativista, profissional de segurança ou alguém que valoriza a privacidade, o **Rayhunter** oferece ferramentas para manter a segurança móvel em um mundo cada vez mais monitorado. Para conferir dispositivos compatíveis verificados, veja as opções de **[Rayhunter à venda](https://stscollective.com)** em fornecedores confiáveis de equipamentos de segurança.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compre dispositivos Rayhunter e economize 20%
{{< /centerbutton >}}

## Referências

- [Repositório oficial do Rayhunter no GitHub](https://github.com/EFForg/rayhunter)
- [Versão mais recente do Rayhunter](https://github.com/EFForg/rayhunter/releases/tag/v0.10.2)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [STS Collective, fornecedora de equipamentos Rayhunter](https://stscollective.com)

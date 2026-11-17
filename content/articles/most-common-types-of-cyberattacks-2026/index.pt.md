---
title: "Os tipos mais comuns de ataques cibernéticos e como detectá-los"
date: 2026-09-11
lastmod: 2026-11-13
toc: true
draft: false
description: "Conheça os tipos mais comuns de ataques cibernéticos, as evidências que deixam em logs e telemetria e pratique a detecção em um laboratório de segurança doméstico."
genre: ["Cibersegurança", "Detecção de ameaças", "Blue Team", "Operações de segurança", "Desenvolvimento profissional"]
tags: ["tipos de ataque cibernético", "malware", "ransomware", "phishing", "spear phishing", "engenharia social", "spoofing", "ataques baseados em identidade", "credential stuffing", "password spraying", "injeção SQL", "cross-site scripting", "ataque à cadeia de suprimentos", "ameaça interna", "tunelamento DNS", "ataques IoT", "ataques com IA", "negação de serviço", "engenharia de detecção", "analista SOC", "Blue Team", "laboratório doméstico", "análise de logs", "resposta a incidentes", "MITRE ATT&CK", "carreira em cibersegurança", "caça a ameaças", "centro de operações de segurança", "telemetria", "triagem de alertas"]
cover: "/img/cover/types-of-cyberattacks-icons-illustration.webp"
coverAlt: "Ilustração digital com ícones abstratos e coloridos que representam vários tipos de ataques cibernéticos, como ransomware, phishing e negação de serviço, sobre um fundo escuro."
coverCaption: ""
---

**Um tipo de ataque** é uma categoria de técnicas, não uma ferramenta específica. Ransomware, phishing e credential stuffing são métodos que um adversário repete contra muitos alvos com pequenas variações. Conhecer essas categorias ajuda você a organizar mentalmente os alertas que encontrará em uma equipe de segurança.

*Famílias específicas de malware surgem e desaparecem em questão de meses. As categorias de ataque abaixo permanecem estáveis há anos, e cada uma deixa rastros reconhecíveis na telemetria de endpoints, identidades, rede ou e-mail.*

<!--more-->

## Principais pontos

- **Aprenda o padrão, não a carga útil.** As categorias de ataque mudam muito mais devagar do que as ferramentas individuais.
- **Toda categoria deixa evidências.** A detecção começa quando você sabe qual telemetria registra a atividade.
- **Reproduza um ataque para entendê-lo.** Um laboratório doméstico transforma uma categoria abstrata em uma observação registrada.
- **Documente o que encontrou.** Uma breve nota de investigação comprova o trabalho e ensina quais evidências foram coletadas.

## Os tipos de ataque em resumo

A tabela lista as categorias que as equipes de segurança encontram com mais frequência. As seções seguintes descrevem cada categoria, suas variantes comuns e os dados que um defensor analisa para detectá-la.

| Tipo de ataque | O que faz |
|---|---|
| **Malware** | Executa software malicioso, como ransomware, spyware e trojans |
| **Negação de serviço** | Inunda um serviço com tráfego até que usuários legítimos percam o acesso |
| **Phishing** | Engana uma pessoa para que revele credenciais ou execute um arquivo malicioso |
| **Spoofing** | Disfarça o atacante como um sistema, remetente ou endereço confiável |
| **Ataques baseados em identidade** | Abusam de credenciais roubadas ou falsificadas para agir como um usuário válido |
| **Injeção de código** | Insere código malicioso em um aplicativo para mudar seu comportamento |
| **Ataques à cadeia de suprimentos** | Comprometem um fornecedor, uma biblioteca ou um canal de atualização confiável |
| **Engenharia social** | Manipula uma pessoa para que tome uma ação insegura |
| **Ameaças internas** | Abusam do acesso de um funcionário atual ou antigo |
| **Tunelamento DNS** | Codifica dados em consultas DNS para passar pelos controles |
| **Ataques a IoT** | Miram dispositivos conectados para se mover pela rede, espionar ou entrar em uma botnet |
| **Ataques com IA** | Usam aprendizado de máquina para gerar conteúdo, imitar pessoas ou contornar filtros |

**Nota sobre o escopo:** essas categorias se sobrepõem. Um e-mail de phishing costuma distribuir malware, e o roubo de credenciais geralmente precede um ataque baseado em identidade. Veja a lista como um conjunto de perspectivas, não como divisões rígidas.

______

## Malware

**Malware** é qualquer programa criado para prejudicar, controlar ou lucrar com um sistema. O termo inclui ransomware, malware sem arquivo, spyware, adware, trojans, worms, rootkits, keyloggers e botnets.

| Subtipo | Comportamento |
|---|---|
| **Ransomware** | Criptografa arquivos e exige pagamento pela chave de descriptografia |
| **Malware sem arquivo** | Usa ferramentas incorporadas ao sistema e grava pouco no disco |
| **Spyware** | Coleta dados de atividade sem o conhecimento do usuário |
| **Trojan** | Finge ser software legítimo para ser executado |
| **Worm** | Copia a si próprio entre hosts sem ação do usuário |
| **Rootkit** | Esconde-se no sistema operacional para manter o controle persistente |

**Onde encontrar as evidências:** ferramentas de detecção e resposta de endpoints, ou **EDR**, registram árvores de processos, linhas de comando, gravações de arquivos e alterações no registro. Um ataque sem arquivo também gera telemetria de processos e scripts, pois o sistema operacional ainda inicia as ferramentas exploradas pelo ataque.

______

## Negação de serviço

**Um ataque de negação de serviço (DoS)** inunda um alvo com solicitações até que usuários legítimos percam o acesso. **Um ataque distribuído de negação de serviço (DDoS)** repete a mesma ideia a partir de muitos sistemas ao mesmo tempo, o que dificulta muito mais filtrar o tráfego pelo endereço de origem.

| Característica | DoS | DDoS |
|---|---|---|
| **Origem** | Um sistema | Muitos sistemas |
| **Dificuldade para bloquear** | Moderada | Alta, pois as origens se espalham por muitas redes |
| **Impacto típico** | Perda de disponibilidade | Perda de disponibilidade em maior escala |

**Onde encontrar as evidências:** volume de tráfego comparado a uma linha de base, conexões por origem, picos na taxa de solicitações e mudanças na taxa de erros. O monitoramento de disponibilidade costuma alertar antes que a equipe de segurança perceba o evento.

______

## Phishing

**Phishing** usa e-mails, mensagens de texto, telefonemas ou redes sociais para levar alguém a revelar credenciais ou executar um anexo malicioso. As variantes mudam de acordo com o alvo e o canal.

| Variante | Alvo e canal |
|---|---|
| **Spear phishing** | Uma pessoa ou equipe específica, geralmente por e-mail |
| **Whaling** | Dirigentes e executivos, muitas vezes para movimentar dinheiro ou dados |
| **Smishing** | Mensagens de texto fraudulentas |
| **Vishing** | Telefonemas ou mensagens de voz fraudulentos |

**Onde encontrar as evidências:** logs do gateway de e-mail, resultados da análise de URLs, análise de anexos e relatos de usuários. O relato de um funcionário atento é um dos sinais mais valiosos desta lista.

______

## Spoofing

**Spoofing** esconde um atacante atrás de uma identidade confiável para que o alvo aceite uma conexão, mensagem ou endereço. O disfarce ganha tempo e contorna verificações baseadas em confiança.

| Tipo | O que é falsificado |
|---|---|
| **Spoofing de domínio** | Site ou domínio de e-mail parecido que imita uma marca real |
| **Spoofing de e-mail** | O endereço do remetente de uma mensagem |
| **Spoofing de ARP** | Um endereço de rede local para interceptar o tráfego entre dois hosts |

**Onde encontrar as evidências:** resultados de SPF, DKIM e DMARC nos cabeçalhos de e-mail, idade do registro do domínio, incompatibilidades de certificados e alertas de endereço duplicado na rede local.

______

## Ataques baseados em identidade

**Ataques baseados em identidade** usam uma conta válida em vez de uma falha de software. O atacante tem credenciais funcionais, então a atividade parece normal e se mistura ao ruído de fundo. Essa categoria gera uma parcela grande dos alertas que um **centro de operações de segurança (SOC)** trata todos os dias.

*Se você praticar apenas uma categoria em um laboratório doméstico, escolha esta. Os sinais são ricos, os exercícios se repetem e a configuração é pequena.*

| Técnica | O que acontece |
|---|---|
| **Kerberoasting** | Solicita um tíquete de serviço e depois quebra a senha criptografada offline |
| **Ataque man-in-the-middle (MITM)** | Fica entre duas partes para ler ou alterar uma sessão |
| **Ataque de reutilização do hash (Pass-the-Hash)** | Reutiliza um hash de senha roubado para abrir uma nova sessão |
| **Golden ticket** | Falsifica um tíquete Kerberos para obter amplo acesso ao domínio |
| **Silver ticket** | Falsifica um tíquete de serviço para um serviço específico |
| **Coleta de credenciais** | Reúne nomes de usuário e senhas em grande quantidade |
| **Credential stuffing** | Reutiliza o mesmo conjunto de credenciais em muitos sites sem relação entre si |
| **Password spraying** | Experimenta uma senha comum em muitas contas |
| **Força bruta** | Experimenta muitas senhas contra uma conta |
| **Downgrade** | Força uma conexão a usar uma versão mais fraca do protocolo |

**Onde encontrar as evidências:** registros de login, contagem de autenticações malsucedidas, anomalias de tokens, alertas de deslocamentos impossíveis e detecções de risco de identidade. **O phishing adversary-in-the-middle (AiTM)** também se encaixa aqui, pois o atacante rouba um token de sessão ativo em vez de uma senha. A reutilização do token a partir de uma infraestrutura desconhecida aciona o mecanismo de risco de identidade.

______

## Injeção de código

**Injeção de código** coloca código controlado pelo atacante em um aplicativo vulnerável para que o aplicativo o execute como parte do trabalho normal. É o aplicativo, não o atacante, que realiza a ação prejudicial.

| Tipo | Alvo |
|---|---|
| **Injeção SQL** | Uma consulta ao banco de dados construída com entradas não validadas |
| **Cross-site scripting (XSS)** | Uma página da Web que executa o script do atacante no navegador de um visitante |
| **Malvertising** | Um espaço publicitário legítimo preenchido com código malicioso |
| **Envenenamento de dados** | Um conjunto de treinamento para um modelo de IA ou aprendizado de máquina |

**Onde encontrar as evidências:** logs de aplicativos Web, registros de consultas ao banco de dados, relatórios da política de segurança de conteúdo e padrões de solicitações diferentes do uso normal do aplicativo.

______

## Ataques à cadeia de suprimentos

**Um ataque à cadeia de suprimentos** mira um terceiro confiável cujo produto ou serviço chega a muitos clientes. **Um ataque à cadeia de suprimentos de software** injeta código malicioso em um aplicativo, biblioteca ou atualização, levando-o a todos os usuários do produto. **Um ataque à cadeia de suprimentos de hardware** compromete um componente físico antes do envio.

*O software moderno depende de bibliotecas de terceiros. Por isso, uma dependência comprometida chega muito além do fornecedor original.*

**Onde encontrar as evidências:** análise da composição de software, registros do pipeline de compilação, conexões de saída inesperadas de uma atualização confiável e verificações de integridade dos artefatos distribuídos.

______

## Engenharia social

**Engenharia social** usa pressão psicológica para levar uma pessoa a uma ação insegura. O atacante apela à autoridade, urgência, medo, dinheiro ou confiança.

| Técnica | Abordagem |
|---|---|
| **Pretexting** | Inventa uma situação plausível para ganhar confiança |
| **Comprometimento de e-mail comercial (BEC)** | Imita um colega confiável para redirecionar um pagamento ou obter dados |
| **Desinformação** | Espalha narrativas falsas por redes sociais e bots |
| **Quid pro quo** | Oferece uma recompensa em troca de informações ou acesso |
| **Armadilha romântica** | Constrói uma relação falsa para obter dinheiro, dados ou acesso |
| **Tailgating** | Segue um funcionário por uma porta protegida |

**Onde encontrar as evidências:** resultados da autenticação de e-mail, pedidos incomuns de alteração de pagamentos, registros da central de atendimento e logs de acesso físico.

______

## Ameaças internas

**Uma ameaça interna** é o uso indevido de acesso por um funcionário atual ou antigo, contratado ou parceiro. Algumas pessoas agem de propósito, motivadas por dinheiro ou ressentimento. Outras agem por negligência, como ao deixar credenciais em um documento compartilhado.

*Relatórios de incidentes mencionam pessoas internas negligentes com mais frequência do que as maliciosas. Nos dois casos, aplica-se o mesmo controle de detecção: compare os acessos a uma linha de base definida para a função.*

**Onde encontrar as evidências:** volume de transferência de dados, atividade fora do horário normal, alterações de privilégios e downloads em massa de repositórios confidenciais.

______

## Tunelamento DNS

**Tunelamento DNS** codifica dados em consultas e respostas DNS. Quase todas as redes permitem DNS, então essa técnica transporta dados para além dos controles criados para inspecionar o tráfego da Web.

*A detecção depende do volume e do formato. Um host que envia milhares de consultas para um único domínio se destaca da linha de base normal, e subdomínios incomumente longos indicam uma carga útil codificada.*

**Onde encontrar as evidências:** registros de consultas DNS, comprimento e volume das consultas por host, tipos de registro raros como TXT e consultas a domínios registrados poucos dias antes.

______

## Ataques a dispositivos IoT

**Um ataque a IoT** mira um dispositivo conectado, como uma câmera, impressora, termostato ou sensor. Credenciais padrão fracas e atualizações de firmware pouco frequentes tornam esses dispositivos pontos de entrada comuns. Depois de comprometido, um dispositivo entra em uma botnet, vaza dados ou cria um caminho para a rede maior.

*A implantação do 5G acrescenta dispositivos conectados em grande escala, e cada dispositivo novo é outro alvo com um ciclo de atualização longo.*

**Onde encontrar as evidências:** inventário de dispositivos, padrões de conexões de saída, transferência anormal de dados de um dispositivo com função fixa e diferenças de versão de firmware em uma frota.

______

## Ataques com IA

**Ataques com IA** aplicam aprendizado de máquina ao trabalho do atacante.

| Técnica | Uso |
|---|---|
| **IA/ML adversarial** | Manipula dados de treinamento ou entradas para enganar um modelo |
| **Dark AI** | Usa IA e aprendizado de máquina especificamente para explorar vulnerabilidades |
| **Deepfake** | Gera áudio, vídeo ou imagens falsas e realistas |
| **Engenharia social gerada por IA** | Conduz conversas convincentes por chat ou voz em grande escala |

*Uma ligação com voz deepfake ou uma conversa de phishing fluente aumenta a credibilidade de um truque antigo. A técnica subjacente continua familiar, por isso habilidades de detecção baseadas em comportamento duram mais do que habilidades ligadas a uma única ferramenta.*

**Onde encontrar as evidências:** sinais de procedência do conteúdo, verificação por outro canal de pedidos de dinheiro ou acesso e anomalias comportamentais ligadas a mudanças de identidade e pagamentos.

______

## Associar ataques à telemetria

Cada categoria se relaciona a uma fonte de dados diferente. A tabela faz essa associação e oferece um ponto de partida para o trabalho de detecção.

| Tipo de ataque | Telemetria principal |
|---|---|
| **Malware** | Registros EDR de processos, arquivos e registro do sistema |
| **Negação de serviço** | Fluxos de rede e monitores de disponibilidade |
| **Phishing** | Registros do gateway de e-mail e da análise de URLs |
| **Spoofing** | Registros de autenticação de e-mail e de endereços de rede |
| **Baseado em identidade** | Registros de login e proteção de identidade |
| **Injeção de código** | Logs de aplicativos Web e consultas ao banco de dados |
| **Cadeia de suprimentos** | Pipeline de compilação e inventário de dependências |
| **Engenharia social** | Registros de e-mail, central de atendimento e acesso físico |
| **Ameaça interna** | Registros de acesso e transferência de dados |
| **Tunelamento DNS** | Registros de consultas DNS |
| **IoT** | Inventário de dispositivos e registros de fluxos de saída |
| **Baseado em IA** | Registros de identidade, pagamentos e procedência do conteúdo |

*Comece a detecção pela coluna de telemetria. Uma regra útil vem de uma fonte de dados e de um comportamento conhecidos, não do nome de uma ferramenta.*

**As categorias se sobrepõem durante um incidente.** Uma mensagem de phishing pode levar ao roubo de credenciais, à execução de malware e a uma invasão baseada em identidade. Classifique a técnica de acesso inicial e registre separadamente os comportamentos seguintes. Assim, um evento não vira quatro alertas sem relação, e a investigação ganha uma linha do tempo mais clara.

______

## Pratique a detecção em um laboratório

Uma categoria continua abstrata até você observar sua ocorrência. Um laboratório doméstico permite gerar a atividade, coletar a telemetria e comparar o alerta ao registro bruto. O [vídeo de carreira sobre a criação de um centro de operações de segurança](https://www.youtube.com/watch?v=s3g8o7Np1_g) mostra a montagem completa para você ganhar experiência profissional antes de ser contratado.

{{< youtube id="s3g8o7Np1_g" >}}

Comece pela categoria de identidade. Crie um usuário de teste, habilite o registro de login e execute uma sequência de logins malsucedidos e bem-sucedidos. Depois leia o registro e anote os campos que distinguem o uso normal do exercício.

**Um exercício repetível:**

1. **Escolha uma categoria** na tabela de telemetria acima.
2. **Reproduza uma versão inofensiva** da atividade no seu sistema ou conta de teste.
3. **Colete a telemetria** que a categoria produz.
4. **Descreva a ideia de detecção** como regra, busca salva ou consulta.
5. **Teste a regra** com o exercício e confirme se ela é acionada pelo comportamento esperado.
6. **Registre os limites** da regra, inclusive as atividades que ela não detecta.

O guia [Microsoft SOC Home Lab](/articles/microsoft-soc-home-lab-2026/) detalha a montagem do ambiente: licenciamento, segmentação de rede, coleta de logs e testes de controle de identidade. O guia [Mad Hat Cyber Range](https://madhat.io/pages/cyber-range-guide) amplia a mesma ideia com uma estrutura de workshop que inclui exercícios de ataque, detecção e defesa.

Para usar vocabulário consistente, associe o comportamento observado à técnica correspondente do [MITRE ATT&CK](https://attack.mitre.org/). Trate essa associação como um auxílio para analistas, não como prova de atribuição. Guarde o evento bruto, a consulta, a versão da regra e os pontos cegos conhecidos junto ao registro do exercício.

{{< centerbutton href="/articles/microsoft-soc-home-lab-2026/" >}}
  Leia o guia Microsoft SOC Home Lab
{{< /centerbutton >}}

______

## Próximos passos

Comece com uma categoria e um exercício. Adicione uma segunda categoria depois de concluir e documentar a primeira. O objetivo é aprofundar uma investigação, não criar uma lista de ferramentas.

- **[Guia Microsoft SOC Home Lab](/articles/microsoft-soc-home-lab-2026/)** monta o ambiente para esses exercícios.
- **[Como montar um laboratório de TI em casa](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/)** aborda a infraestrutura por trás de um laboratório de segurança.
- **[Dicas para escrever um currículo de TI](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/)** mostra como apresentar um laboratório documentado como experiência prática.
- **[Os cinco principais vetores de ataque cibernético e suas mitigações](/articles/the-top-five-cyber-attack-vectors-and-mitigations/)** restringe a lista aos vetores mais frequentes.

**Fontes:** as categorias de ataque e seus subtipos seguem a [visão geral da CrowdStrike sobre ataques cibernéticos comuns](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/common-cyberattacks/) de Kurt Baker. Os links de produtos e referências apontam para a documentação da Microsoft.

---
title: "Chaves SSH do Bitbucket Cloud: acesso Git somente leitura para agentes de IA"
date: 2026-10-11
lastmod: 2026-11-13
toc: true
draft: false
description: "Configure chaves SSH do Bitbucket Cloud, acesso Git CLI, tokens REST API, 1Password e ferramentas MCP para fluxos de trabalho de agentes de IA somente leitura."
genre: ["Segurança em nuvem", "Ferramentas para desenvolvedores", "Administração de sistemas"]
tags: ["Bitbucket Cloud", "chaves SSH do Bitbucket", "chaves de acesso ao repositório", "chaves de acesso ao projeto", "chaves de acesso ao espaço de trabalho", "Git CLI", "Bitbucket CLI", "1Password CLI", "1Password SSH Agent", "MCP", "Model Context Protocol", "REST API", "escopos de tokens API", "permissões de agentes", "automação somente leitura", "chaves de host SSH"]
cover: "/img/cover/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation.webp"
coverAlt: "Fluxo de terminal conectando o acesso Git do Bitbucket Cloud, chaves SSH de escopo limitado, 1Password, leituras REST API e ferramentas MCP"
coverCaption: ""
---

**Um fluxo de agente delimitado separa leituras do repositório, leituras da API, tratamento de segredos e gravações remotas.** Use Git por Secure Shell (SSH) para acessar o código-fonte, uma chave de acesso do Bitbucket somente leitura para checkout automatizado, REST API para metadados e um servidor Model Context Protocol (MCP) para ferramentas aprovadas. Guarde chaves privadas e tokens API no 1Password. Exija aprovação humana antes de qualquer gravação.

<!--more-->

## Principais pontos

- **Somente leitura por padrão:** use uma chave de acesso ao repositório ou ao projeto para o checkout do agente. Nenhuma delas permite push.
- **Identidade pessoal:** use uma chave SSH pessoal para trabalho interativo vinculado a uma conta de usuário.
- **Custódia de segredos:** use 1Password SSH Agent para que o Git solicite uma assinatura autorizada sem ler a chave privada.
- **Significado de CLI:** considere `git`, `curl` e um pequeno wrapper de API auditado como a linha de comando prática do Bitbucket.
- **Limite do MCP:** exponha ferramentas de leitura com escopo restrito. Desative ferramentas de gravação ou coloque-as atrás de uma aprovação separada.
- **Controle de gravação:** permita que o agente inspecione, compare e prepare uma alteração. Exija aprovação humana antes de um push, pull request, merge ou atualização de configurações.

## Antes de começar

**Pré-requisitos:** acesso ao Bitbucket Cloud, Git, cliente OpenSSH, 1Password 8, 1Password CLI, uma CLI conectada ou conta de serviço aprovada e um host MCP com controles de aprovação de servidores. Reserve 45 minutos. Dificuldade intermediária.

Use um repositório de teste na primeira tentativa. Substitua todos os marcadores nos exemplos. Os comandos abaixo são exemplos não testados. Eles não representam uma conta ou um repositório Bitbucket ativo.

**Versões:** este artigo traz orientações de projeto, não um procedimento fixado a versões específicas. Confirme as versões instaladas de Git, OpenSSH, 1Password CLI, Teamwork Graph CLI, host MCP e servidor MCP antes de testar. Configure 1Password SSH Agent para o sistema operacional atual antes de usar `ssh-add -l`.

**Mantenha credenciais fora de shells, logs, URLs, remotos Git e arquivos de origem.** Use marcadores como `<workspace>`, `<repository>`, `<api-token>` e `<socket-path>`. Não cole uma chave privada real em uma transcrição do terminal.

## Escolher o limite de acesso

O Bitbucket Cloud aceita chaves de acesso nos níveis de repositório, projeto e espaço de trabalho. O escopo muda o impacto de uma chave copiada. A [comparação oficial de chaves de acesso](https://support.atlassian.com/bitbucket-cloud/kb/difference-between-repository-project-and-workspace-access-keys/) descreve diretamente a diferença de permissões.

| Caminho de acesso | Escopo | Permite gravação | Uso adequado |
|---|---|---:|---|
| **Chave de acesso ao repositório** | Um repositório | Não | Checkout padrão do agente |
| **Chave de acesso ao projeto** | Repositórios de um projeto | Não | Tarefas somente leitura em um pequeno grupo de repositórios |
| **Chave de acesso ao espaço de trabalho** | Repositórios de um espaço de trabalho | Sim | Automação de serviço controlada com plano de gravação separado |
| **Chave SSH pessoal** | Repositórios permitidos para um usuário | Segue a conta do usuário | Administração interativa |
| **Token API** | Escopos API vinculados ao usuário e acesso da conta | Depende dos escopos | Leituras REST API ou tarefa temporária de gravação |

**Comece pelo menor limite útil.** Escolha uma chave de repositório quando um repositório for suficiente. Escolha uma chave de projeto quando vários repositórios compartilharem um projeto e a leitura bastar. Trate uma chave de espaço de trabalho como identidade de gravação, não como opção padrão conveniente.

Crie e registre a chave mais restrita pelo caminho correspondente nas configurações do Bitbucket:

1. Abra Repository settings, Access keys e Add key para um repositório. Cole a chave pública e mantenha a chave somente leitura.
2. Abra Project settings, Access keys e Add key quando vários repositórios precisarem de uma identidade de leitura limitada ao projeto.
3. Use uma chave de espaço de trabalho somente em um espaço compartilhado com um projeto de gravação aprovado. Espaços pessoais não oferecem o mesmo caminho no nível do espaço de trabalho.
4. Registre o rótulo da chave, o escopo, a impressão digital da chave pública, o proprietário e a data de rotação. Guarde a chave privada no 1Password.

Após o registro, execute um teste exato de conexão somente leitura:

```bash
git ls-remote git@bitbucket.org:<workspace>/<repository>.git HEAD
```

**Resultado esperado:** uma referência de commit para `HEAD`. Exemplo não testado. Um resultado positivo prova que uma identidade SSH permitida chegou ao repositório indicado. Não prova que a chave registrada foi selecionada nem que há acesso de gravação. Repita o teste depois de configurar uma chave por repositório.

Para a custódia de chaves privadas e o consentimento do 1Password SSH Agent, consulte [1Password CLI e SSH Agent: chaves SSH seguras para agentes de IA](/articles/1password-cli-ssh-keys-mcp-agent-administration/).

## Definir “Bitbucket CLI” corretamente

A expressão **Bitbucket CLI** costuma misturar três interfaces diferentes. Mantenha-as separadas.

- **Git CLI:** `git clone` e `git fetch` transferem dados do repositório por SSH ou HTTPS. `git diff` compara arquivos locais ou revisões.
- **Cliente REST:** `curl` ou um wrapper revisado chama a API Representational State Transfer (REST) do Bitbucket Cloud. Uma API é uma interface programática para solicitar dados ou ações. A [referência REST API do Bitbucket Cloud](https://developer.atlassian.com/cloud/bitbucket/rest/) lista recursos de repositório, origem, branch, pull request, pipeline e status.
- **Atlassian CLI:** `acli` é a linha de comando oficial da Atlassian. Sua [introdução](https://developer.atlassian.com/cloud/acli/guides/introduction/) descreve o produto, enquanto a [referência de comandos](https://developer.atlassian.com/cloud/acli/reference/commands/) lista as superfícies `admin`, `jira`, `feedback` e `rovodev`. A referência não documenta comandos do Bitbucket Cloud.

**A referência oficial de comandos `acli` da Atlassian não documenta comandos do Bitbucket Cloud.** Não invente um comando como `acli bitbucket clone`. Use Git para operações Git e REST API para dados do Bitbucket Cloud.

### Teamwork Graph CLI opcional

**A Atlassian também publica a Teamwork Graph CLI, ou `twg`.** Sua [visão geral](https://developer.atlassian.com/cloud/twg-cli/) e o [catálogo de comandos](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/commands/commands-catalog/) documentam famílias de comandos do Bitbucket. O comando de configuração é:

```bash
twg setup
```

O comando de configuração altera o estado de autenticação local. Siga as instruções da versão instalada para configurar opcionalmente um token do Bitbucket. O caminho do token Bitbucket na CLI é separado do OAuth da Atlassian. Ajuste a sintaxe exata à versão instalada e ao catálogo atual. Use um perfil separado, token restrito, habilidades instaladas revisadas e aprovação humana para comandos que alteram dados.

**Resultado esperado, não testado:** o perfil isolado recebe as configurações de autenticação do Bitbucket. Registre o estado anterior do perfil antes da configuração. Para reverter, remova a credencial salva pelo procedimento documentado de logout ou remoção de configuração da versão instalada.

Se um projeto de terceiros se apresentar como Bitbucket CLI, audite seu código-fonte, processo de lançamento, checksums, caminho de atualização, fluxo de autenticação, escopos solicitados, destinos de rede, tratamento de logs e comandos de gravação. Um nome de binário familiar não comprova suporte do fornecedor nem permissões seguras.

## Manter as chaves SSH sob controle do 1Password

O [1Password SSH Agent](https://www.1password.dev/ssh/agent) disponibiliza ao Git e aos clientes SSH as chaves armazenadas no 1Password. O cliente faz uma solicitação de assinatura autorizada. A chave privada permanece dentro do aplicativo 1Password, que pede consentimento antes de um cliente aprovado usar uma chave.

A [referência do 1Password CLI](https://www.1password.dev/cli/reference) tem outra função. Use `op` para acesso controlado a itens, tokens API, contas de serviço e configuração de automação. Use SSH Agent para assinatura SSH. Evite exportar uma chave privada para um arquivo temporário para facilitar o fluxo do agente.

Verifique o estado local da CLI e do agente com comandos somente leitura:

```bash
op --version
ssh-add -l
```

**Resultado esperado:** uma versão do 1Password CLI e uma ou mais impressões digitais de chaves públicas do agente ativo. Exemplo não testado. Um resultado vazio de `ssh-add -l` significa que nenhuma chave está disponível pelo socket de agente selecionado.

Para uma chave nova, crie um item SSH Key Ed25519 no 1Password ou importe uma gerada por um processo local confiável. Defina um rótulo conforme a finalidade, o escopo e a data de rotação. Adicione somente a chave pública ao Bitbucket Cloud. O [guia Linux de chaves de acesso ao repositório](https://support.atlassian.com/bitbucket-cloud/docs/set-up-repository-access-keys-on-linux/) descreve o caminho nas configurações do repositório e o limite somente leitura.

## Verificar primeiro a chave de host do Bitbucket

A autenticação SSH do usuário não comprova a identidade do servidor. O cliente deve verificar a chave de host do Bitbucket Cloud antes de enviar uma solicitação de autenticação. O [guia da Atlassian sobre SSH e verificação em duas etapas](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/) lista as chaves de host públicas e mostra o endpoint oficial para recuperar entradas known-hosts.

Busque os dados públicos da chave de host para comparação:

```bash
curl --fail --silent --show-error https://bitbucket.org/site/ssh
```

**Resultado esperado:** linhas OpenSSH `known_hosts` para `bitbucket.org`. Exemplo não testado. Compare a chave ou a impressão digital retornada com uma cópia independente confiável antes de colocar a linha em `~/.ssh/known_hosts`.

Use a verificação estrita de host depois que a entrada aprovada existir:

```sshconfig
Host bitbucket.org
    StrictHostKeyChecking yes
    UserKnownHostsFile ~/.ssh/known_hosts
```

**Não aceite uma chave de host alterada durante a execução de um agente.** Pare a execução, verifique o registro atual de chaves de host do Bitbucket Cloud e revise a entrada local de `known_hosts`. A aceitação automática remove um limite de segurança baseado em chave.

## Selecionar uma chave por repositório

Um dispositivo costuma ter várias chaves do Bitbucket. Um agente SSH amplo oferece várias identidades em uma conexão. Um servidor ou política com um limite baixo de tentativas de autenticação pode rejeitar a chave correta depois que as anteriores falharem.

O [guia da Atlassian sobre várias chaves de acesso a repositórios](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) usa `core.sshCommand` em um arquivo de configuração Git do repositório e `includeIf` na configuração Git global. Siga o mesmo padrão para usar uma chave por repositório.

Exemplo portátil baseado em arquivos:

```ini
# .gitconfig dentro de um repositório local
[core]
    sshCommand = ssh -o IdentitiesOnly=yes -i ~/.ssh/<repository-automation-key>
```

```ini
# ~/.gitconfig
[includeIf "gitdir:~/src/<repository>/"]
    path = ~/src/<repository>/.gitconfig
```

O bloco acima é uma exceção com arquivo de chave privada para uma identidade de automação dedicada. Ele não configura o 1Password SSH Agent. Para o 1Password SSH Agent, configure o valor `IdentityAgent` ou `SSH_AUTH_SOCK` específico da plataforma pelo [guia de configuração do 1Password](https://www.1password.dev/ssh/get-started). Algumas configurações OpenSSH usam um arquivo `.pub` como seletor de identidade do agente. Confirme o suporte da plataforma antes de usar. Uma configuração baseada em arquivo precisa do caminho da chave privada correspondente. Nunca passe um arquivo `.pub` a um comando que espera material de chave privada nem exporte uma chave privada pessoal.

Use uma configuração explícita do repositório quando um clone local precisar de uma chave. Use `includeIf` quando um diretório contiver vários clones com o mesmo limite de acesso. O [guia de várias chaves](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) mostra as duas configurações no fluxo do Bitbucket.

Clone pelo Git via SSH:

```bash
git clone git@bitbucket.org:<workspace>/<repository>.git <local-directory>
```

**Resultado esperado:** Git cria `<local-directory>` e busca o repositório por `bitbucket.org`. Exemplo não testado. Uma chave de acesso ao repositório permite apenas clone e pull.

## Usar tokens API para leituras REST restritas

Use SSH para transporte Git. Use REST API para metadados ou operações fora do transporte Git. O [guia de permissões de tokens API](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/) lista escopos de repositório como Read, Write, Admin e Delete. Repository Read corresponde a `read:repository:bitbucket` e não inclui acesso a pull requests.

Para automação de leitura, prefira um token de acesso de repositório ou projeto Bitbucket quando o destino oferecer suporte ao endpoint necessário. Um token API de usuário mantém o acesso mais amplo da conta. Use um token de espaço de trabalho apenas quando o registro da tarefa especificar esse limite maior. Consulte o [guia de tokens de acesso do Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/) antes de escolher o tipo.

Para um caminho de leitura do agente, comece com `read:repository:bitbucket`. Adicione `read:pullrequest:bitbucket` somente se o agente precisar de dados de pull request. Adicione escopos de espaço de trabalho ou pipeline apenas quando o registro da tarefa especificar o endpoint e o resultado. Escopos de gravação e administração exigem uma aprovação separada.

Crie cada token API para uma finalidade, defina uma data de expiração, registre-a no controle de rotação e substitua o token antes do vencimento. O [guia da Atlassian para criar um token API](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/) exige nome, validade, seleção de aplicativo e escopos. O token aparece uma vez após a criação.

Guarde o valor no 1Password ou em um segredo de runtime gerenciado. Não o coloque em uma URL remota. Passe um token bearer por variável de ambiente somente ao processo que precisa fazer uma leitura:

```bash
op run --env-file=/path/to/agent.env -- \
sh -c 'curl --fail --silent --show-error \
  --request GET \
  --url "https://api.bitbucket.org/2.0/repositories/<workspace>/<repository>" \
  --header "Authorization: Bearer ${BITBUCKET_API_TOKEN}" \
  --header "Accept: application/json"'
```

Mantenha `/path/to/agent.env` fora do repositório. Guarde no arquivo uma referência como `BITBUCKET_API_TOKEN=op://synthetic-vault/synthetic-api-token/credential`. `op run` resolve a referência e expõe o valor ao processo filho curl durante a vida do subprocesso. Isso não impede o processo filho de ler o valor da variável de ambiente ou registrá-lo em log. Não substitua o marcador por um token literal.

**Resultado esperado:** metadados JSON do repositório selecionado. Exemplo não testado. O marcador nunca deve virar um token real em um arquivo commitado ou log.

Para automações mais longas, deixe o 1Password injetar um segredo no ambiente do processo pelo fluxo CLI ou de conta de serviço aceito. Ajuste a validade do token à tarefa. Revogue-o se a tarefa terminar cedo ou se o proprietário do host mudar.

## Oferecer ao MCP uma superfície pequena de leitura

Use a [especificação MCP atual](https://modelcontextprotocol.io/specification/2026-07-28) e suas [regras de autorização](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) ao revisar um servidor novo. Servidores HTTP precisam verificar a audiência do token e tratar claramente respostas 401 e 403.

O host MCP obtém o consentimento do usuário. O cliente mantém uma conexão com um servidor. O servidor expõe ferramentas, recursos ou prompts. Trate cada servidor como código não confiável até que sua origem, transporte, conta e permissões sejam revisados.

A URL da especificação 2025-06-18 no próximo parágrafo é uma versão histórica. Use a especificação atual 2026-07-28 para novas revisões.

A [especificação MCP](https://modelcontextprotocol.io/specification/2025-06-18) define a comunicação entre host MCP, cliente e servidor. Um servidor expõe ferramentas, recursos ou prompts pelo protocolo. MCP padroniza o formato de conexão. O host, a implementação do servidor, a conta, o escopo do token e a política de aprovação ainda determinam o alcance de uma chamada.

Use um servidor MCP como adaptador restrito sobre Git e REST API do Bitbucket Cloud.

Proteja o adaptador contra repasse de tokens, falsificação de requisição no lado do servidor (SSRF) e comportamento de agente confuso. SSRF permite que um servidor envie solicitações a destinos inesperados. O comportamento de agente confuso ocorre quando um servidor usa privilégios mais amplos em nome de quem o chamou. Proteja também contra servidores locais maliciosos, redirecionamentos OAuth inseguros e respostas grandes demais com dados de origem. Fixe as origens permitidas do Bitbucket e os identificadores dos repositórios. Execute servidores locais em sandbox sob um usuário de sistema operacional dedicado. Oculte segredos nos resultados das ferramentas e nos logs.

Esta seção descreve um projeto, não uma configuração MCP testada. Nenhum cliente, servidor, transporte, versão ou fixture está fixado. Valide um servidor somente leitura em um perfil de teste separado antes de conectar um agente a um repositório de produção.

Exemplos de ferramentas de leitura:

| Ferramenta | Resultado delimitado |
|---|---|
| **`get_repository_metadata`** | Retorna os metadados de um repositório |
| **`read_source_file`** | Lê um caminho em uma revisão |
| **`list_branches`** | Lista branches de um repositório |
| **`get_pull_request`** | Retorna uma pull request se o token tiver escopo de leitura de pull request |
| **`get_build_status`** | Retorna dados de status de um commit |

Esses nomes descrevem um projeto. Não são comandos da Atlassian. Não permita que o servidor aceite URLs arbitrárias, comandos shell arbitrários, tokens brutos, pedidos de exportação de chaves privadas ou identificadores de repositório sem restrição.

Defina permissões em quatro camadas:

1. **Bitbucket Cloud:** chave de leitura de repositório ou projeto para Git, mais os escopos mínimos de token API para leituras REST.
2. **1Password:** um cofre ou conta de serviço para a tarefa, sem caminho de exportação de chave privada.
3. **Servidor MCP:** lista de permissão de ferramentas de leitura, endpoints fixos do Bitbucket Cloud, validação de entradas, limites de tempo e logs com segredos ocultos.
4. **Host MCP:** aprovação do usuário para o servidor e cada ação que permita gravação, com ferramentas de gravação desativadas no perfil padrão.

*Uma lista de ferramentas MCP comprova sua descoberta. Não comprova autorização, escopo correto, tratamento seguro de entradas nem um resultado correto.*

## Organizar o fluxo do agente

Mantenha o fluxo explícito. Cada etapa fornece evidências para a seguinte.

| Etapa | Ação do agente | Permissão | Aprovação humana |
|---|---|---|---|
| **Preparar** | Ler configuração, registro da chave de host, rótulo da chave, escopo e validade do token | Leitura local | Aprovar o registro de configuração |
| **Inspecionar** | Clonar ou fazer fetch com Git por SSH e consultar metadados REST | Leitura do repositório e da API | Nenhuma após a configuração |
| **Analisar** | Ler arquivos, branches, pull requests e status de build com ferramentas aprovadas | Ferramentas MCP somente leitura | Nenhuma para leituras delimitadas |
| **Preparar alteração** | Produzir um patch, plano de branch ou rascunho de pull request no espaço local | Somente gravação local | Revisar o diff e o destino |
| **Aprovar gravação** | Apresentar ação remota exata, escopo e caminho de reversão | Ainda sem gravação remota | Aprovação humana |
| **Executar gravação** | Fazer push de uma branch, criar pull request ou chamar um endpoint de gravação | Identidade de gravação de curta duração | Confirmar cada ação |
| **Verificar** | Ler o commit, pull request ou status resultante | Novamente somente leitura | Confirmar o resultado esperado |

O perfil padrão do agente deve parar depois de **Analisar** ou **Preparar alteração**. Um perfil separado de gravação deve usar outro token ou chave, validade curta, destino fixo e pedido de aprovação. Uma chave de acesso ao repositório não permite a etapa de gravação, o que cria um limite técnico útil.

## Reversão e remoção

Comece a reversão removendo o acesso e depois limpe a configuração local:

1. Remova a chave de acesso ao repositório, projeto ou espaço de trabalho da página correspondente de configurações do Bitbucket.
2. Revogue o token API de repositório, projeto, espaço de trabalho ou usuário na página de segurança correspondente do Bitbucket.
3. Remova a credencial salva do Teamwork Graph pelo [procedimento de autenticação documentado](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/getting-started/how-authentication-works/) para a versão instalada da CLI. Preserve a credencial anterior somente no gerenciador de segredos aprovado. Confirme que o perfil isolado não lista mais a credencial de teste.
4. Após o teste, remova o arquivo `.gitconfig` do repositório e sua entrada `includeIf`. Mantenha inalterada a configuração Git não relacionada.
5. Remova somente a linha verificada da chave de host do Bitbucket adicionada para o teste. Mantenha as demais chaves de host aprovadas.
6. Remova o arquivo externo `agent.env` e a saída temporária. Remova a entrada do servidor MCP da configuração do host e reinicie o host.

Registre cada remoção, o operador e o horário. Faça a rotação de uma chave ou token se um valor aparecer em um log, registro de processo ou transcrição inesperados.

## Ciclo de leitura remota com atualizações locais de referências

Use um ciclo pequeno para inspeções recorrentes do repositório:

```bash
LOCAL_REPO="<local-directory>"
git -C "$LOCAL_REPO" fetch --no-tags
git -C "$LOCAL_REPO" status --short --branch
git -C "$LOCAL_REPO" log -1 --format='%H %ad %s' --date=iso-strict
```

`HEAD` é a referência atualmente selecionada no repositório. Um resultado positivo prova que uma identidade SSH permitida chegou ao repositório indicado. Não prova qual chave foi selecionada nem se há acesso a push.

**Resultado esperado:** resultado do fetch, status da branch e uma linha de commit. Exemplo não testado. `fetch` não grava no remoto, mas atualiza referências locais e `FETCH_HEAD`. O ciclo não faz push nem troca branches.

O servidor MCP deve expor o mesmo limite de leitura por operações nomeadas. Um wrapper shell local ou ferramenta MCP deve rejeitar um verbo de gravação antes de enviar uma solicitação. Registre o nome da ferramenta, marcador do repositório, revisão, classe do resultado e duração. Oculte tokens, cookies, caminhos privados e conteúdo de arquivos, a menos que a tarefa precise de um arquivo específico.

## Solução de problemas

### `Permission denied (publickey)`

Verifique o socket do agente ativo, a chave pública selecionada, a entrada de chave de acesso ao repositório e `IdentitiesOnly`. Uma chave de repositório precisa existir no repositório ou projeto de destino. Uma chave pessoal exige permissão da conta. Uma chave de espaço de trabalho tem outro limite de gravação.

### A chave de repositório errada é oferecida

Use uma chave por repositório com `core.sshCommand` ou agrupe clones em um diretório controlado por `includeIf`. Liste as chaves do agente com `ssh-add -l`. Se houver muitas chaves do 1Password, use um seletor de identidade explícito ou um bookmark SSH do 1Password. O [guia 1Password Agent](https://www.1password.dev/ssh/agent) documenta limites de quantidade de chaves e o uso de bookmarks.

### SSH informa que a chave de host mudou

Pare o agente. Não exclua `known_hosts` como primeira resposta. Compare o registro atual de chaves de host do Bitbucket Cloud com a entrada local por um canal independente. Remova ou substitua uma entrada somente após a comparação passar.

### A API retorna `401` ou `403`

Verifique validade e tipo do token, escopo do endpoint e limite da conta ou espaço de trabalho. Um escopo de leitura do repositório não inclui pull requests. Um endpoint de gravação exige escopo de gravação e perfil de gravação aprovado. Não amplie os escopos antes de identificar o endpoint que falhou.

### A API retorna dados do repositório, mas nenhuma pull request

Adicione o menor escopo de leitura de pull request a um token novo ou rotacionado. Não reutilize um token amplo de usuário para um servidor MCP somente leitura.

### O servidor MCP lista ferramentas, mas uma chamada falha

Separe registro do servidor, conexão, descoberta de ferramentas, execução e verificação do resultado. Inspecione o log do servidor sem expor o token. Verifique o endpoint e o formato de entrada. Tente novamente uma vez após verificar a conectividade. Marque a operação como incompleta se a segunda chamada falhar.

### Uma CLI Bitbucket de terceiros solicita acesso amplo

Interrompa a instalação. Compare o acesso solicitado com o registro da tarefa. Revise o código-fonte, assinaturas ou checksums de lançamentos, destinos de rede, armazenamento de segredos e comportamento de gravação. A referência oficial de comandos da Atlassian CLI não comprova suporte a um binário Bitbucket de terceiros.

## Próximas etapas

Crie um registro curto de acesso com escopo do repositório ou projeto, rótulo da chave, data de verificação da chave de host, escopos API, validade do token, responsável pelo 1Password, lista permitida de ferramentas MCP, política de logs e responsável pela aprovação de gravações.

Execute um clone somente leitura, uma leitura de metadados REST e uma leitura de ferramenta MCP com marcadores na transcrição. Compare os resultados. Mantenha o perfil do agente somente leitura até a revisão do registro e dos logs.

Quando surgir uma tarefa de gravação, prepare primeiro um diff local. Apresente a branch de destino, caminhos alterados, método API solicitado, escopo do token e etapa de reversão. Use uma identidade de gravação separada e de curta duração apenas depois que uma pessoa aprovar a ação exata.

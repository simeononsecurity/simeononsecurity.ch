---
title: "1Password SSH Agent e CLI: Acesso de Agente de IA Somente Leitura"
date: 2026-10-11
lastmod: 2026-10-28
toc: true
draft: false
description: "Projete um fluxo de trabalho SSH somente leitura com 1Password CLI, o SSH Agent e o MCP. Use comandos sintéticos, permissões restritas e aprovação humana antes de testes ao vivo."
genre: ["Administração de Sistemas", "Segurança em Nuvem", "Automação"]
tags: ["1Password CLI", "Chaves SSH", "1Password SSH Agent", "MCP", "Model Context Protocol", "administração de agentes", "administração de sistemas", "Bitbucket Cloud", "Git via SSH", "referências de segredos", "contas de serviço", "menor privilégio", "autenticação por chave pública", "gerenciamento de segredos", "segurança de linha de comando", "segurança de automação"]
cover: "/img/cover/1password-cli-ssh-keys-mcp-agent-administration.webp"
coverAlt: "Diagrama abstrato de um agente usando uma referência de segredo, um agente SSH e ferramentas MCP sem exibir chaves privadas."
coverCaption: ""
---

**Um agente de linha de comando precisa de acesso útil, não de uma cópia de todas as credenciais.** Este guia apresenta um design limitado para o 1Password CLI, o Agente SSH do 1Password, o acesso Git do Bitbucket e o Model Context Protocol (MCP). O primeiro fluxo de trabalho usa nomes sintéticos, ações somente de leitura e aprovação humana na fronteira SSH.

<!--more-->

A distinção fundamental é simples. **O SSH interativo usa consentimento por meio do Agente SSH do 1Password. A automação não supervisionada precisa de uma identidade separada, acesso restrito e um ciclo de vida de chaves diferente.** Não trate uma conexão MCP como permissão para executar qualquer um dos fluxos de trabalho.

## Pontos-chave

- **Proteção de chave privada:** O Agente SSH do 1Password executa a autenticação SSH mantendo as chaves privadas dentro do aplicativo 1Password.
- **Gerenciamento de chave pública:** Publique apenas uma chave pública no Bitbucket ou em uma conta remota. Mantenha a metade privada em um item de Chave SSH.
- **Consentimento interativo:** Uma pessoa aprova uma sessão de cliente ou terminal antes que o Agente SSH use uma chave.
- **Separação não supervisionada:** Um trabalho agendado precisa de uma conta de serviço dedicada e de um escopo de cofre restrito. Uma aprovação do Agente SSH interativo não atende a essa necessidade.
- **Limites do MCP:** O MCP conecta um agente a ferramentas e recursos. O cliente, o servidor, o sistema operacional e a política do 1Password ainda controlam o acesso.

## Antes de Começar

**Pré-requisitos:** Instale o 1Password 8 e o 1Password CLI 2.20.0 ou posterior. Faça login por meio de uma conta 1Password suportada. Use um cliente OpenSSH. Crie um repositório de teste do Bitbucket ou outro alvo não de produção. Mantenha um segundo caminho administrativo disponível para reversão.

**Tempo:** 30 a 45 minutos para uma revisão de design e uma demonstração sintética.

**Dificuldade:** Intermediário. Você precisa de conhecimento básico de Git, SSH, shell e controle de acesso.

Este guia cobre design e planejamento. O artigo do Bitbucket vinculado cobre os limites de acesso específicos do Bitbucket. Este guia não testa uma conta ao vivo, não cria uma chave real, não se conecta a um host real e não registra um servidor MCP real. Todos os identificadores abaixo são sintéticos. **Substitua os placeholders apenas dentro do seu próprio ambiente controlado.**

**Postura de versão:** Use o 1Password 8 e [1Password CLI 2.20.0 ou posterior](https://www.1password.dev/ssh/manage-keys) para este fluxo de trabalho. [1Password CLI 1 está obsoleto](https://www.1password.dev/cli/upgrade/). [1Password 7 será descontinuado no início de 2027](https://support.1password.com/add-account/). A geração, importação e compartilhamento de chaves SSH exigem o 1Password 8. Confirme as versões do Git, OpenSSH, host MCP e servidor MCP instalados antes de testar. Os exemplos abaixo permanecem não testados.

Um **vault** é uma coleção protegida de itens do 1Password. **OpenSSH** é o software de cliente e servidor SSH utilizado por muitos sistemas operacionais. **MCP**, ou Model Context Protocol, conecta um agente a ferramentas ou recursos aprovados.

## Por que manter chaves privadas inacessíveis

Um par de chaves SSH possui uma chave pública e uma chave privada. Um serviço Git remoto ou servidor armazena a chave pública. O cliente prova a posse da chave privada durante a autenticação. A chave privada não precisa ser enviada ao serviço remoto.

O [1Password SSH Agent](https://www.1password.dev/ssh/agent) estende esse modelo. Sua documentação afirma que clientes SSH e Git se autenticam por meio do agente, enquanto a chave privada permanece no aplicativo 1Password. O cliente recebe um resultado de assinatura, não um arquivo de chave privada.

Essa fronteira reduz várias vias de exposição:

- **Controle de versão:** Uma chave privada não entra em um repositório ou em uma solicitação de pull.
- **Histórico do shell:** Um valor de chave privada não aparece em um argumento de comando.
- **Arquivos temporários:** Um script não precisa escrever uma chave privada em `~/.ssh/`.
- **Contexto do agente:** Um modelo de linguagem grande (LLM) não precisa do texto da chave privada para solicitar uma operação SSH.
- **Reuso acidental:** Uma chave copiada não permanece em um espaço de trabalho antigo após o término de uma tarefa.

A fronteira não torna o SSH inofensivo. Um processo com permissão para usar o soquete do agente pode executar ações como a chave aprovada. A verificação da chave do host, as limitações da conta remota, as permissões do repositório, a política de comandos e o isolamento de processos ainda são importantes.

*A fronteira da chave privada protege o material da chave. A fronteira não aprova um comando remoto nem prova que o host de destino é confiável.*

## Consentimento interativo SSH

Configure um vault dedicado para chaves de agente. Use o arquivo de configuração do SSH Agent para selecionar o conjunto de chaves mais restrito e uma chave específica para o host. Não exponha todas as chaves elegíveis de todos os vaults integrados a um processo de automação.

O [modelo de segurança do 1Password SSH Agent](https://www.1password.dev/ssh/agent/security) vincula a aprovação a uma chave e a um processo solicitante. O prompt identifica o processo e a chave. A pessoa então aprova a solicitação por meio do método de autenticação configurado.

O 1Password documenta vários escopos de aprovação. A aprovação por chave e por aplicativo é o padrão. Um escopo de sessão de terminal restringe a aprovação a uma aba ou sessão. A aprovação por solicitação pede novamente para cada solicitação. Existe uma opção de aprovação para todos os processos, mas essa opção concede a todos os processos sob o usuário do sistema operacional atual acesso para a sessão.

**Use o escopo de aprovação mais restrito adequado para a tarefa.** Um agente de administração de sistemas deve ser executado em um terminal dedicado ou em um ambiente isolado (sandbox). Não aprove todos os processos quando uma única sessão de terminal for suficiente.

A sessão de aprovação não é uma concessão permanente. O 1Password registra a autorização pelo período configurado ou até que o aplicativo seja bloqueado ou encerrado. Quando o aplicativo está bloqueado, o agente não retém chaves privadas para uso posterior. O processo do SSH Agent continua em segundo plano quando a configuração suportada está habilitada, mesmo com o 1Password fechado, mas uma nova solicitação de assinatura requer que o 1Password esteja desbloqueado.

O [guia de configuração do SSH do 1Password](https://www.1password.dev/ssh/get-started) mostra o fluxo geral: gerar ou importar uma chave, publicar a chave pública, habilitar o SSH Agent, configurar o cliente SSH, executar um comando SSH ou Git e aprovar a solicitação. O caminho do socket exato varia conforme o sistema operacional. Use as instruções da plataforma atual em vez de copiar um caminho de outra máquina.

O aplicativo 1Password deve estar desbloqueado antes que uma nova solicitação de assinatura tenha sucesso. O processo do agente pode continuar em segundo plano enquanto o aplicativo está fechado. Um aplicativo bloqueado não libera material de chave privada para assinatura.

## Chaves Públicas e Bitbucket

O [guia de gerenciamento de chaves do 1Password](https://www.1password.dev/ssh/manage-keys) documenta itens de Chave SSH, geração de chaves, importação de chaves, chaves públicas, impressões digitais (fingerprints) e chaves privadas. O exemplo da CLI usa `op item create --category ssh` para criar um item de Chave SSH. A CLI do 1Password gera uma chave Ed25519 por padrão para este exemplo e oculta a chave privada em sua saída.

O Bitbucket Cloud usa o fluxo de trabalho de linha de comando padrão do Git e OpenSSH. Seu [guia de linha de comando](https://support.atlassian.com/bitbucket-cloud/docs/find-the-command-line/) descreve operações do Git a partir de um repositório local. Seu [guia de configuração SSH](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) lista os formatos remotos SSH e os formatos de chave pública suportados.

**Trate o Bitbucket como o consumidor da chave pública.** Registre a chave pública ou a impressão digital (fingerprint) por meio da configuração de conta ou repositório aprovada do Bitbucket. Mantenha a chave privada no 1Password. O cliente Git solicita ao SSH Agent que assine. O cliente não lê um arquivo de chave privada.

Para o escopo da chave de acesso do Bitbucket, o caminho de registro e o teste de leitura somente do Git, consulte [Bitbucket Cloud SSH Keys and Git CLI: Read-Only Access for AI Agents](/articles/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation/).

A documentação do Bitbucket chama isso de fluxo de trabalho da CLI do Git. Este artigo não pressupõe um servidor MCP separado do Bitbucket ou um produto chamado Bitbucket CLI. Uma CLI específica do Bitbucket precisa de sua própria documentação atual e de sua própria revisão de permissões.

## A Fronteira entre o Agente e o MCP

Use a especificação atual [MCP](https://modelcontextprotocol.io/specification/2026-07-28) ao revisar um novo servidor.

A URL da especificação de 2025-06-18 no parágrafo de contexto a seguir é uma versão histórica. Use a especificação de 2026-07-28 para novas revisões.

[MCP](https://modelcontextprotocol.io/specification/2025-06-18) padroniza as conexões entre uma aplicação de LLM, um conector de cliente e um servidor. Um servidor oferece ferramentas, recursos ou prompts. A especificação também determina que os hosts devem obter o consentimento do usuário antes de expor dados ou invocar ferramentas.

**O próprio MCP não concede permissões.** Uma ferramenta MCP ainda é executada dentro das permissões do processo do servidor, do usuário do sistema operacional, do caminho de rede, da conta em nuvem e das credenciais configuradas. Uma descrição de ferramenta não é uma política de autorização.

A [documentação de Segurança para IA da 1Password](https://www.1password.dev/security-for-ai) descreve um Servidor MCP de Ambientes e padrões de configuração segura do MCP. A mesma página descreve o carregamento em tempo de execução de valores de configuração do MCP a partir da 1Password. Essas páginas não definem um produto MCP de chave SSH genérico da 1Password nem um fluxo de trabalho SSH universal para todos os clientes de agente.

Use o MCP como uma superfície de controle restrita:

- **Ferramentas de leitura:** Inspecionar status de serviço, metadados de repositório ou logs aprovados.
- **Ferramentas de planejamento:** Preparar um comando ou registro de alteração sem executar o comando.
- **Ferramentas de aprovação:** Solicitar uma decisão humana antes de uma gravação remota.
- **Ferramentas de gravação:** Manter desativadas até que o destino, o comando, o escopo e o plano de reversão sejam explícitos.

O agente deve receber referências, metadados e resultados de operações. **O agente não deve receber o texto de uma chave privada, um despejo de itens de todo o cofre ou um shell irrestrito.**

## Uma Política Inicial Segura

Comece com uma política por escrito antes de habilitar um agente. Mantenha a política próxima à configuração do MCP, mas não coloque credenciais no arquivo.

```yaml
agent_policy:
  purpose: "Read-only repository and system inspection"
  identities:
    interactive_ssh: "1Password SSH Agent with per-terminal consent"
    unattended_jobs: "Dedicated service account with one narrow vault"
  allowed:
    - "Read repository metadata through Git"
    - "Read approved service status and logs"
    - "Run one synthetic SSH connectivity check"
  approval_required:
    - "Any remote write"
    - "Any package, firewall, clock, or service change"
    - "Any new host-key acceptance"
    - "Any private-key export"
  denied:
    - "Read or print private-key fields"
    - "List every vault or every item"
    - "Write tokens or secrets to shell profiles"
    - "Run arbitrary commands from tool output"
  rollback:
    - "Revoke the service account"
    - "Remove the public key from the target"
    - "Disable the MCP server entry"
    - "Lock 1Password and end the agent session"
```

Esta política é um exemplo, não um formato de configuração da 1Password. Armazene a política real no plano de controle usado pelo seu cliente de agente. Revise cada ferramenta contra a política antes de habilitar cada ferramenta.

## Contas de Serviço e Referências de Segredos

Uma **conta de serviço** fornece a um processo automatizado sua própria identidade. O [guia de scripts da CLI da 1Password](https://www.1password.dev/cli/secrets-scripts) recomenda contas de serviço para acesso com privilégios mínimos a cofres selecionados. Isso separa um trabalho não supervisionado do SSO, MFA, inventário de cofres e conta diária de uma pessoa.

Uma **referência secreta** nomeia um valor sem colocar o valor no código-fonte. A [referência da CLI do 1Password](https://www.1password.dev/cli/reference) usa a forma `op://vault/item/field`. A referência é segura para armazenamento apenas quando o processo circundante ainda tem acesso restrito. Uma referência não contorna a política.

Use `op read` quando um comando precisa de um valor. Use `op run` quando um processo filho precisa de um conjunto controlado de valores de tempo de execução. Use `op item create` quando um novo item de Chave SSH precisa existir no cofre aprovado.

Não confunda injeção em tempo de execução com proteção de chave privada. Um token de API passado como variável de ambiente ainda é visível para o processo filho. Uma chave privada passada por meio de uma variável de ambiente é pior, pois o valor expande a exposição para inspeção de processo, relatórios de falha, saída de depuração, rastreamento de shell e registro acidental.

**Prefira uma referência no código-fonte e um valor em tempo de execução no menor processo possível.** Mantenha o processo de vida curta. Desative o rastreamento do shell. Não imprima o ambiente. Remova arquivos temporários após uma execução falha.

## Fluxo de Trabalho Seguro Inicial

A sequência abaixo separa o registro de chave pública, SSH interativo, descoberta MCP e design não supervisionado.

### 1. Definir o alvo

Anote a classe do alvo, a conta remota, o repositório ou comando pretendido, a fonte da chave do host, o responsável pela aprovação e a ação de reversão. Use um registro sintético durante o primeiro exercício.

```text
target_class: test-repository
remote_account: git
operation: read-only connectivity check
host_key_source: approved administrator record
approval_owner: named operator
rollback: remove public key and revoke test identity
```

**Resultado esperado, não testado:** O registro identifica um alvo e uma operação. O registro não contém um nome de host, endereço IP, token, chave privada ou dados pessoais.

### 2. Criar ou selecionar o item de Chave SSH

O guia oficial de [chave SSH do 1Password](https://www.1password.dev/ssh/manage-keys) documenta o padrão de criação via CLI. O comando abaixo usa um título sintético e um cofre de teste nomeado.

```bash
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
```

**Saída esperada, não testada:** O 1Password cria um item de Chave SSH no cofre de teste nomeado e oculta a chave privada na saída do terminal. O comando altera o estado do 1Password. A saída legível por humanos exata depende da versão da CLI e do estado de login.

Capture o identificador de item retornado no registro de teste sem copiar o campo da chave privada. Use o identificador ou o título exato do item para leituras específicas de campo posteriores apenas após a confirmação do esquema do item.

Não redirecione esta saída para um log compartilhado. Capture apenas o identificador do item, a impressão digital da chave pública e o registro de aprovação quando o procedimento local suportar saída estruturada segura.

### 3. Tratar a chave pública

Abra o item de Chave SSH no 1Password e use a ação Copiar Chave Pública. Use uma referência específica de campo apenas depois de confirmar o rótulo do campo da chave pública na sua própria conta. Não despeje o item completo.

```bash
PUBLIC_KEY_REF="op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
op read "$PUBLIC_KEY_REF"
```

**Saída esperada, não testada:** Uma linha sintética de chave pública OpenSSH ou um valor de chave pública do campo confirmado. O nome do campo de exemplo acima não é uma garantia sobre o rótulo do campo do seu item.

Registre a chave pública na conta aprovada do Bitbucket, no repositório do Bitbucket ou na conta remota. Nunca cole a chave privada correspondente no Bitbucket. O [guia SSH do Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) também recomenda registrar a chave de host do Bitbucket antes da primeira conexão.

Para o Bitbucket, obtenha o registro de chave de host publicado e compare o registro com uma cópia confiável independente antes de adicionar uma linha a `~/.ssh/known_hosts`. Use verificação estrita de host após a comparação passar. Não aceite uma chave de host alterada durante a execução de um agente.

### 4. Habilitar SSH interativo

Ative o Agente SSH do 1Password no aplicativo de desktop. Configure o OpenSSH com o valor específico da plataforma `IdentityAgent` ou `SSH_AUTH_SOCK` do [guia oficial de configuração](https://www.1password.dev/ssh/get-started). Limite o primeiro teste a um repositório ou a uma conta não de produção.

No macOS ou Linux, defina o soquete do guia de configuração da plataforma e execute `ssh-add -l`. No Windows, use a configuração de pipe nomeado suportada e verifique as chaves disponíveis através da interface do Agente SSH do 1Password ou de um teste SSH documentado para Windows. Não apresente `ssh-add -l` como um comando de verificação multiplataforma.

Apenas no macOS ou Linux:

```bash
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Saída esperada, não testada:** No macOS ou Linux, `ssh-add -l` lista as impressões digitais do agente ativo. No Windows, use o teste de pipe nomeado documentado ou a interface do Agente SSH do 1Password. Uma leitura bem-sucedida do Git retorna uma referência de commit. O repositório de exemplo acima requer substituição em um teste controlado.

O comando usa um repositório de exemplo. Substitua o exemplo apenas em um teste controlado. **Não aprove uma solicitação para um destino ou processo que você não esperava.**

### 5. Adicionar MCP após o caminho SSH funcionar

Primeiro, verifique o cliente SSH e o destino sem MCP. Em seguida, adicione um servidor MCP somente leitura ou um conector local. Dê ao agente uma ferramenta como `read_status` ou `prepare_command`. Não comece com uma ferramenta de shell geral.

A configuração do MCP deve referenciar valores de tempo de execução por meio do mecanismo de ambiente suportado pelo cliente. O [guia de segurança de IA da 1Password](https://www.1password.dev/security-for-ai) descreve a substituição de tokens de configuração MCP em texto puro por variáveis de ambiente carregadas da 1Password. **Mantenha a referência ou o nome da variável na configuração. Mantenha o valor resolvido fora do transcript do agente.**

Esta seção descreve um design, não uma configuração MCP testada. Nenhum cliente, servidor, transporte, versão ou fixture é fixado aqui. Valide um servidor somente de leitura em um perfil de teste separado antes de conectar um agente a um sistema de produção.

### 6. Registre o resultado

Registre a classe do alvo, o nome da ferramenta, a decisão de aprovação, a impressão digital da chave pública, o resultado do comando e o resultado da limpeza. Omita valores secretos. Marque cada saída como observada ou esperada.

**Resultado esperado, não testado:** O agente lê o status, propõe um comando limitado, recebe aprovação explícita para a solicitação SSH, completa a operação somente de leitura e produz um registro sem texto de chave privada.

## Sequência de Comandos Sintéticos

A sequência a seguir mostra a ordem sem usar infraestrutura real. Estes comandos são apenas exemplos. Eles não foram executados durante a preparação do artigo.

```bash
op --version
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
op read "op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
# macOS or Linux only
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Saída esperada, não testada:**

```text
2.x.y
SSH Key item created. Private key: redacted
ssh-ed25519 AAAA<synthetic-public-key> synthetic-key-label
256 SHA256:<synthetic-fingerprint> synthetic-agent-admin-key (ED25519)
<synthetic-commit-id>        HEAD
```

O bloco de saída é ilustrativo. O bloco não representa uma execução contra uma conta da 1Password, Bitbucket, provedor Git ou host remoto. Um registro de produção deve armazenar apenas metadados aprovados e um estado de sucesso ou falha.

## Acesso Interativo versus Não Supervisionado

| Modo de acesso | Identidade | Caminho da chave privada | Modelo de aprovação |
|---|---|---|---|
| **SSH interativo** | Conta humana por meio do 1Password SSH Agent | A chave privada permanece no aplicativo 1Password | Humano aprova um processo, sessão de terminal ou solicitação |
| **Leitura agendada** | Conta de serviço dedicada | `op run` fornece valores de tempo de execução restritos | Política do trabalho e escopo da conta de serviço |
| **SSH agendado** | Identidade de automação dedicada | A exportação da chave permanece como design de último recurso | Isolamento do trabalho, vida útil curta, restrição de host e rotação |
| **Escrita do agente** | Identidade humana ou específica da tarefa | Depende da integração aprovada | Aprovação humana antes de cada mudança definida |

*Não agende um fluxo de trabalho em torno de um prompt do Agente SSH interativo. Use um design de automação separado ou mantenha a etapa operada por um humano.*

Para tarefas não supervisionadas, crie uma conta de serviço com acesso a um cofre ou a um pequeno conjunto de itens. Dê à tarefa um único propósito. Use um repositório ou uma conta de servidor dedicada. Adicione verificação de chave de host. Defina um tempo limite de execução. Registre metadados de ações sem segredos. Rode ou revogue a identidade após o teste.

Se uma tarefa não supervisionada realmente precisar de uma chave privada SSH, use uma chave de automação dedicada com uma conta remota restrita e uma data de término documentada. A busca da chave privada com `op read` ainda exporta material de chave através de uma fronteira de processo. Este design tem um raio de impacto maior do que o 1Password SSH Agent. Prefira uma identidade de plataforma, um serviço de implantação ou outra identidade de carga de trabalho quando o destino suportar uma delas.

## Por que variáveis de ambiente em texto simples aumentam o risco

Variáveis de ambiente mantêm segredos fora dos arquivos de código-fonte, mas não tornam os segredos invisíveis. Um processo filho lê seu ambiente. Inspeção de processos, manipuladores de falha, saída de depuração, rastreamento de shell e registros de comandos copiados podem expor valores.

O 1Password documenta `op run` como um método de tempo de execução para carregar referências em um subprocesso. Use `op run` para valores de que um processo realmente precisa. Mantenha o processo filho de vida curta e restrinja seu comando. Não passe uma chave privada através de `SSH_PRIVATE_KEY`, `KEY` ou de uma variável semelhante quando o SSH Agent elimina a necessidade de exportação.

A ordem mais segura é:

1. **Usar o SSH Agent** para SSH interativo.
2. **Usar o registro de chave pública** para o Bitbucket ou a conta remota.
3. **Usar `op run`** para um processo filho não supervisionado restrito.
4. **Usar `op read`** para um único valor quando um processo filho não precisar de um ambiente completo.
5. **Exportar uma chave privada** apenas após uma exceção por escrito, escopo restrito, plano de limpeza e plano de rotação.

## Tabela de Decisão

| Necessidade | Caminho preferido | Motivo para parar ou redesenhar |
|---|---|---|
| Humano executa Git via SSH | 1Password SSH Agent | Parar se o prompt nomear um processo ou chave inesperado |
| Registrar uma chave de repositório | Ler ou preencher automaticamente a chave pública | Nunca copiar a chave privada para o serviço de repositório |
| Agente lê status do serviço | Ferramenta MCP somente leitura com escopo em nível de SO | Parar se a ferramenta expuser um shell irrestrito |
| Agente propõe uma alteração remota | Ferramenta de plano seguida de aprovação humana | Parar se o alvo, o comando ou a reversão estiverem claros |
| Trabalho lê um token de API | Conta de serviço mais `op read` ou `op run` | Parar se o token entrar no código-fonte, logs ou perfil global |
| Trabalho precisa de acesso SSH | Identidade de carga de trabalho ou chave de automação dedicada | Parar se o trabalho exigir uma chave pessoal ou conta ampla |
| Configuração MCP precisa de um token | Referência em tempo de execução carregada pelo cliente suportado | Parar se um token em texto puro for commitado na configuração |

## Tratamento de Falhas

**Prompt de consentimento SSH inesperado:** Negar o prompt. Verificar o nome do processo, a sessão do terminal, a impressão digital da chave, o alvo do repositório e a chave do host. Revisar a configuração do cliente SSH antes de tentar novamente.

**Socket do SSH Agent ausente:** Confirmar que o aplicativo desktop do 1Password está instalado por um método suportado, que o SSH Agent está habilitado e que o cliente usa o socket específico da plataforma. A [página oficial do SSH Agent](https://www.1password.dev/ssh/agent) lista os requisitos do sistema operacional e os links de configuração do socket.

**Falha na autenticação por chave pública:** Verificar a chave pública selecionada, a conta remota, a permissão do repositório, a chave do host e a configuração SSH. Usar uma comparação de impressão digital pública. Não resolver o erro exportando uma chave privada não relacionada.

**`op read` nega acesso:** Verificar o escopo do cofre da conta de serviço, o identificador do item, a referência do campo, o estado de login e o status do item. Reduzir a referência a um item aprovado. Não ampliar a concessão do cofre como primeira resposta.

**`op run` expõe um valor:** Parar o trabalho. Preservar apenas o registro mínimo do incidente. Remover logs copiados e arquivos temporários de acordo com o seu procedimento de retenção. Rotacionar o segredo ou a chave afetados. Revisar o rastreamento do shell, a inspeção de processos, os relatórios de falha e a retenção do transcrito MCP.

**Comportamento inesperado da ferramenta MCP:** Trate a saída da ferramenta como dados não confiáveis. Pare antes de executar comandos sugeridos pela saída. Inspecione o código-fonte do servidor, a configuração, as permissões e o transporte. O host MCP deve obter o consentimento do usuário. A especificação também fornece orientações para implementadores sobre consentimento e controles de acesso, mas o protocolo não substitui sua revisão.

## Rollback e Remoção

O rollback começa com a remoção do acesso, não com a exclusão de arquivos.

1. **Pare o agente ou o trabalho agendado.** Desative a entrada do servidor MCP ou desconecte o cliente.
2. **Bloqueie o 1Password.** Encerre a sessão interativa de autorização SSH.
3. **Remova a chave pública.** Exclua a chave de teste do Bitbucket, do repositório ou da conta remota.
4. **Revogue a conta de serviço.** Remova seu acesso ao cofre e invalide seu token.
5. **Exclua o item de Chave SSH de teste** após confirmar que nenhum fluxo de trabalho aprovado utiliza o item.
6. **Remova a configuração temporária.** Exclua referências de teste, substituições de socket local e logs gerados.
7. **Revise as evidências.** Confirme que o registro de rollback não contém chave privada, token ou despejo de ambiente.

*Um arquivo local excluído não revoga uma chave pública, conta de serviço, token em cache ou autorização remota. Remova cada concessão em sua origem.*

## Solução de Problemas

### O agente pede uma chave em cada comando

Verifique o escopo de autorização selecionado. A aprovação por solicitação é mais restritiva. Uma sessão de terminal ou aplicativo pode ter terminado. O 1Password também pede novamente após um evento de bloqueio ou saída.

### O agente vê uma chave privada em seu transcript

Pare o fluxo de trabalho e rotacione a chave. Inspecione a resposta do servidor MCP, o comando do shell, o log de depuração e o wrapper da ferramenta. Substitua as leituras de chave privada pelo uso do SSH Agent para tarefas interativas. Para trabalhos, substitua uma chave pessoal por uma identidade dedicada e uma exceção documentada.

### Uma lista de chaves contém muitas identidades

O SSH Agent do 1Password expõe chaves elegíveis de seus cofres configurados. Use uma configuração de agente com escopo definido ou uma configuração SSH específica do host. A [documentação do agente](https://www.1password.dev/ssh/agent) também menciona o limite de seis chaves do servidor OpenSSH.

### Um comando funciona manualmente, mas falha em um trabalho

Compare a identidade, o escopo do cofre, o ambiente, os dados da chave do host, o diretório de trabalho e as premissas de aprovação. Uma sessão interativa do 1Password inclui o consentimento humano. Um trabalho agendado não. Projete o trabalho como um modo de acesso separado.

### O servidor MCP está conectado, mas a tarefa falha

A conexão não prova a autorização. Verifique a descoberta de ferramentas, as credenciais do servidor, o consentimento do cliente, as permissões do sistema operacional, o acesso à rede e as permissões no lado do destino em etapas separadas. Mantenha o primeiro teste somente de leitura.

## Próximas Etapas

Utilize a especificação MCP atual de 2026-07-28 para novas aprovações. Qualquer link para a especificação de 2025-06-18 neste artigo é contexto histórico.

Comece com um repositório sintético e uma ferramenta MCP somente de leitura. Registre cada resultado esperado como não testado até que um ambiente controlado produza evidências. Em seguida, repita o fluxo de trabalho com um destino não produtivo, um operador nomeado, uma chave de host verificada e um registro escrito de reversão.

Leia a [referência da CLI do 1Password](https://www.1password.dev/cli/reference) para as opções de comando atuais. Leia [Carregar segredos em scripts](https://www.1password.dev/cli/secrets-scripts) antes de criar automação de conta de serviço. Leia a [especificação MCP](https://modelcontextprotocol.io/specification/2026-07-28) antes de aprovar ferramentas de um novo servidor.

**Mantenha o SSH interativo aprovado por humanos. Mantenha o acesso não supervisionado separado. Mantenha as chaves privadas ilegíveis sempre que o destino suportar autenticação baseada em agente.**

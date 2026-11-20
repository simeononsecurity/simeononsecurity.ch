---
title: "Tailscale Aperture: configure clientes de IA para inferência e MCP em 2026"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Encaminhe solicitações de modelos e ferramentas MCP pelo Tailscale Aperture. Configure Codex, Claude Code, Claude Desktop, OpenCode e Hermes em outro dispositivo ou gateway."
genre: ["Inteligência artificial", "Ferramentas para desenvolvedores", "Redes"]
tags: ["Tailscale Aperture", "Configuração do Aperture", "Proxy de IA", "Gateway de LLM", "Gateway MCP", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "Proxy de inferência de IA", "API Responses", "API Anthropic Messages", "MCP remoto", "HTTP Streamable", "Tailscale", "IA auto-hospedada", "Agentes de programação", "Configuração de cliente de IA"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "Aperture conecta painéis de clientes a serviços de modelos e ferramentas MCP por rotas separadas, azul para inferência e verde para ferramentas"
coverCaption: ""
---

## Introdução

O Tailscale Aperture oferece aos clientes de IA um gateway conectado à tailnet para inferência de modelos e ferramentas do Model Context Protocol (MCP). Cada cliente precisa usar uma rota compatível com seu protocolo de API. As ferramentas MCP usam um endpoint separado, e as concessões do Aperture controlam quais modelos e conectores cada identidade Tailscale pode acessar.

Este guia explica como configurar Codex, Claude Code, Claude Desktop, OpenCode e Hermes no macOS, Linux e Windows. Ele cobre configurações de linha de comando e desktop, mostra como descobrir IDs de modelos disponíveis para sua identidade e inclui um prompt anonimizado para reutilização na configuração de outro dispositivo ou instância do Aperture.

**Escolha da rota:** Os caminhos dos endpoints dependem do gateway e de cada protocolo de API. Uma rota Responses como `/codex` não atende ao tráfego Anthropic Messages nem MCP. Confirme o nome do host do gateway e a rota de inferência de cada cliente. Descubra os IDs de modelos com seu próprio acesso ao Aperture antes de alterar as configurações dos clientes.

## Principais pontos

- **O tráfego de modelos** precisa da rota de API correspondente ao protocolo do cliente.
- **O tráfego MCP** usa o endpoint separado `/v1/mcp`.
- **As permissões do gateway** precisam permitir que sua identidade Tailscale use cada modelo e conector.
- **A configuração do cliente** comprova apenas que as configurações foram salvas. Verifique uma solicitação real e uma chamada a uma ferramenta MCP.

## Como as rotas se encaixam

| Finalidade | Solicitação do cliente | Rota do Aperture | Serviço da rota |
|---|---|---|---|
| Codex e modelos compatíveis com Responses | API OpenAI Responses | Normalmente `/v1`. Um caminho personalizado como `/codex` depende da implantação. | Inferência de modelos |
| Inferência de modelos Claude | API Anthropic Messages | URL base do gateway. O Aperture lida com `/v1/messages` | Inferência compatível com Claude |
| Ferramentas MCP | MCP HTTP Streamable | `/v1/mcp` | Ferramentas e recursos dos conectores configurados |

{{< figure src="aperture-client-routes.webp" alt="Codex e Hermes usam uma rota Responses, Claude usa Anthropic Messages, e clientes MCP usam a rota separada /v1/mcp para acessar conectores do Aperture" caption="A inferência de modelos e o tráfego MCP usam endpoints separados do Aperture" >}}

**Raízes dos provedores:** O Aperture acrescenta os caminhos das solicitações do cliente à URL base do provedor. Defina `baseurl` do provedor como a raiz da API dele. Não acrescente `/v1` a uma URL base upstream quando o caminho recebido já inclui `/v1`. Consulte a [referência de configuração do Aperture](https://tailscale.com/docs/aperture/configuration) para ver a construção de URLs, o registro de modelos e as concessões.

## Prepare o gateway

**Antes de editar**, peça estes valores a um administrador do Aperture:

- **Nome do host do gateway:** Use `http://` com a maioria dos clientes conectados à tailnet. A inferência do Claude Desktop exige `https://` com certificado confiável.
- **Rotas de inferência:** OpenAI Responses e Anthropic Messages usam formatos de solicitação diferentes.
- **IDs de modelos:** Descubra os modelos disponíveis para sua identidade Tailscale com o endpoint abaixo. Use os IDs literais retornados para essa identidade.
- **Autenticação:** Confira se o cliente envia uma chave de API fictícia ou uma credencial de usuário.
- **Endpoint MCP:** Normalmente `http://<APERTURE_HOST>/v1/mcp` para clientes da tailnet. A inferência do Claude Desktop exige HTTPS com certificado confiável.
- **Concessões de acesso:** Verifique as permissões de modelos e conectores da sua identidade Tailscale.

**Acesso à rede:** O dispositivo cliente precisa alcançar o gateway pela tailnet. O nome do host sozinho não concede acesso a modelos nem ferramentas. O Aperture nega o acesso sem uma concessão correspondente ao modelo ou conector.

### Encontre modelos disponíveis para seu usuário

**Consulte a lista de modelos** em um dispositivo conectado à mesma tailnet. O Aperture usa a identidade Tailscale do dispositivo e retorna os modelos concedidos a esse usuário, conforme descrito no [guia de concessão de modelos](https://tailscale.com/docs/aperture/how-to/grant-model-access):

```sh
# macOS ou Linux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShell, use curl.exe para evitar o alias antigo curl
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**Leia o resultado:** Use cada `id` retornado como ID do modelo. Confira `metadata.provider.id` para identificar o provedor do Aperture. Escolha um modelo que aceite o formato de API do cliente. Por exemplo, o Claude Desktop precisa de um modelo Anthropic Messages. O [diretório de modelos](https://tailscale.com/docs/aperture/reference/chat) do Aperture também lista os identificadores disponíveis para o usuário conectado.

**Modelos ausentes:** Se um modelo esperado não aparecer, peça a um administrador do Aperture para conferir a configuração do provedor e sua concessão de modelo. O endpoint não permite que usuários concedam acesso a si mesmos.

**Esquema da URL:** O Tailscale recomenda `http://` para a maioria dos clientes conectados à mesma tailnet. O WireGuard criptografa esse tráfego. O Claude Desktop exige `https://` e um certificado confiável pelo sistema operacional. Use o esquema mostrado para cada cliente abaixo.

### Adicione um provedor de inferência

**OpenAI Responses:** Adicione o provedor upstream ao Aperture e habilite o formato de API usado pelo cliente. Para um provedor OpenAI, adicione um fragmento como este:

```json
{
  "providers": {
    "openai": {
      "baseurl": "https://api.openai.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "models": ["<MODEL_ID>"],
      "compatibility": {
        "openai_chat": true,
        "openai_responses": true
      }
    }
  }
}
```

**Anthropic Messages:** Use a raiz da API Anthropic, o formato de autorização `x-api-key` e a compatibilidade `anthropic_messages`. O ID do modelo também precisa constar na lista `models` do provedor. Adicione um fragmento como este:

```json
{
  "providers": {
    "anthropic": {
      "baseurl": "https://api.anthropic.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "authorization": "x-api-key",
      "models": ["<CLAUDE_MODEL_ID>"],
      "compatibility": {
        "anthropic_messages": true
      }
    }
  }
}
```

**Alterações de configuração:** Substitua cada marcador pelos valores upstream. Acrescente os fragmentos à configuração existente do Aperture. Preserve o restante do arquivo atual. Defina sinalizadores de compatibilidade para as APIs aceitas pelo provedor.

**Concessões de acesso:** O Aperture controla o acesso de cada usuário a cada modelo ou conector. Conceda a cada usuário Tailscale previsto apenas os direitos necessários. Este exemplo concede a um usuário acesso a um modelo de provedor e a um conector:

```json
{
  "grants": [
    {
      "src": ["<TAILSCALE_USER>"],
      "app": {
        "tailscale.com/cap/aperture": [
          {"role": "user", "models": "openai/<MODEL_ID>"},
          {"connectors": ["teamtools/**"]}
        ]
      }
    }
  ]
}
```

**Concessão de modelo:** Use o ID do provedor e o ID do modelo no padrão da concessão. O [guia de configuração de conectores](https://tailscale.com/docs/aperture/connectors/get-started) mostra a configuração atual `connectors.servers`. A configuração antiga de nível superior `mcp.servers` está obsoleta.

### Adicione um conector MCP

**Conector MCP:** O Aperture se conecta a servidores MCP upstream e expõe as ferramentas em `/v1/mcp`:

```json
{
  "connectors": {
    "servers": {
      "teamtools": {
        "protocol": "mcp",
        "url": "<UPSTREAM_MCP_ENDPOINT>"
      }
    }
  }
}
```

**URL do conector:** Use o endpoint MCP completo do servidor upstream. Depois conceda ao seu usuário Tailscale acesso a `teamtools/**` ou a um padrão de ferramentas mais restrito. A [referência do proxy MCP](https://tailscale.com/docs/aperture/mcp-server) explica o endpoint único do cliente e o comportamento dos conectores.

## Codex CLI e desktop

**Configurações compartilhadas:** Codex CLI e o app desktop usam a mesma configuração. No macOS e Linux, edite `~/.codex/config.toml`. No Windows, edite `%USERPROFILE%\.codex\config.toml` (o caminho `~/.codex/config.toml` também funciona em shells que expandem a pasta pessoal). A [apresentação do app Codex](https://openai.com/index/introducing-the-codex-app/) diz que o app desktop usa a configuração do Codex CLI. As configurações do usuário Codex ficam em `~/.codex/config.toml`. A documentação de [configuração básica](https://learn.chatgpt.com/docs/config-file/config-basic) descreve os campos de provedor e MCP do usuário. Adicione o provedor a esse arquivo, reinicie o app e confirme que o provedor e o modelo aparecem na interface.

```toml
model = "<MODEL_ID>"
model_provider = "aperture"

[model_providers.aperture]
name = "Aperture Proxy"
base_url = "http://<APERTURE_HOST>/v1"
wire_api = "responses"
requires_openai_auth = true
supports_websockets = false
```

**Campos opcionais:** Esses dois valores correspondem a uma configuração de provedor do Codex. Mantenha-os apenas quando o gateway e a configuração do Codex exigirem. O [guia atual do Tailscale para Codex Aperture](https://tailscale.com/docs/aperture/how-to/use-codex) os omite, usa `wire_api = "responses"` e informa que o Aperture injeta credenciais upstream. Use a URL Responses exata fornecida pelo administrador do gateway. `/codex` é uma rota específica da implantação. A rota padrão documentada pelo Tailscale é `/v1`.

**Configuração MCP:** Adicione o servidor à mesma configuração do usuário:

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**Verifique o Codex:** Execute `codex mcp list`, inicie uma nova sessão e confira `/mcp`. A lista de servidores comprova o registro. Uma ferramenta listada e uma chamada bem-sucedida comprovam a descoberta e a execução. A [referência de configuração do Codex](https://learn.chatgpt.com/docs/config-file/config-reference) documenta as configurações de provedor e MCP do usuário.

## Claude Code CLI

**Protocolo:** Claude Code usa Anthropic Messages. Aponte o arquivo global de configurações do Claude Code para o gateway do Aperture compatível com Anthropic. Use `~/.claude/settings.json` no macOS e Linux ou `%USERPROFILE%\.claude\settings.json` no Windows. No PowerShell, use o caminho equivalente `$HOME\.claude\settings.json`. A rota precisa atender `/v1/messages`. Codex Responses usa outro protocolo e outra rota. O Tailscale recomenda HTTP para Claude Code na tailnet porque o WireGuard criptografa a conexão.

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**Autenticação do cliente:** O guia de cliente do Aperture usa um marcador em `apiKeyHelper` porque o Aperture injeta a credencial upstream. Para encaminhar uma assinatura Claude, o provedor Anthropic do Aperture precisa encaminhar a credencial Claude do usuário. Nesse caso, deixe `ANTHROPIC_API_KEY` e `ANTHROPIC_AUTH_TOKEN` sem definição. Essas variáveis substituem a credencial da assinatura. Siga as instruções atuais do [Claude Code com Aperture](https://tailscale.com/docs/aperture/how-to/use-claude-code) para sua versão do Claude Code e o [guia de gateway da Anthropic](https://code.claude.com/docs/en/llm-gateway-connect) para opções de autenticação.

**MCP por HTTP:** Adicione o endpoint com:

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**Verifique Claude Code:** Inicie uma sessão e execute `/mcp` para confirmar a conexão. A Anthropic recomenda HTTP para servidores MCP remotos na [documentação do MCP](https://code.claude.com/docs/en/mcp).

## Interface gráfica do Claude Desktop

**Configurações separadas:** O Claude Desktop tem uma tela de inferência de terceiros. Essa configuração encaminha solicitações de modelos do Claude Desktop pelo Aperture. A configuração MCP exige outra etapa.

1. No Claude Desktop para macOS ou Windows, selecione **Ajuda > Solução de problemas > Ativar modo de desenvolvedor**. Na versão beta do Linux, use o mesmo menu se estiver disponível. Reinicie o app se solicitado. Se o menu não aparecer, atualize o Claude Desktop e consulte as notas de versão da plataforma.
2. Selecione **Desenvolvedor > Configurar inferência de terceiros**.
3. Defina **Tipo de conexão** como **Gateway** e **Tipo de credencial** como **Chave de API estática**.
4. Digite `https://<APERTURE_HOST>` como **URL base do gateway**. Use o nome de host completo coberto por um certificado TLS confiável.
5. Digite uma chave fictícia não vazia, como `aperture`, para o gateway. O Aperture ignora o marcador e autentica pela tailnet.
6. Deixe vazios os cabeçalhos de inferência personalizados.
7. Adicione um modelo ativado usando um ID exato retornado por `GET /v1/models` para sua identidade Tailscale. Filtre um modelo Anthropic Messages. Digite manualmente o ID, o nome de exibição e um alias de nível opcional. O Claude Desktop não descobre modelos nessa tela.
8. Selecione **Salvar alterações** e depois **Aplicar alterações**. Encerre o Claude Desktop e abra-o novamente.

**Verificação de protocolo:** O [guia do Claude Desktop para Aperture](https://tailscale.com/docs/aperture/how-to/use-claude-desktop) diz que o Claude Desktop usa Anthropic Messages em `/v1/messages`. Não use a rota Codex `/codex` nem escolha um tipo de conexão compatível com OpenAI.

### Conecte Claude Desktop ao MCP

**Acesso MCP privado:** Execute uma ponte local de stdio no mesmo computador do Claude Desktop. Adicione isto à configuração MCP local do Claude Desktop:

```json
{
  "mcpServers": {
    "aperture": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "http://<APERTURE_HOST>/v1/mcp"]
    }
  }
}
```

**Como a ponte funciona:** O processo local alcança o Aperture pela conexão Tailscale do computador. Use o caminho de configuração do seu sistema: macOS, `~/Library/Application Support/Claude/claude_desktop_config.json`; Windows, `%APPDATA%\Claude\claude_desktop_config.json`; versão beta do Linux, abra **Configurações > Desenvolvedor > Editar configuração** e use o caminho aberto pelo Claude Desktop. O caminho do Linux varia conforme o pacote. Reinicie o Claude Desktop, confira a lista de conectores e faça uma chamada inofensiva a uma ferramenta. O [projeto `mcp-remote`](https://github.com/punkpeye/mcp-remote) documenta essa ponte local-remota.

**Conectores remotos:** O fluxo Configurações > Conectores da Anthropic precisa de um servidor remoto acessível pelo serviço Anthropic. Um nome de host exclusivo da tailnet é privado para seus dispositivos, então use a ponte local para o endpoint privado. Se expuser um serviço MCP público, configure autenticação e permissões antes de adicioná-lo como conector na nuvem. Consulte o [guia de conectores MCP remotos](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) da Anthropic.

## OpenCode CLI e desktop

**Configurações compartilhadas:** OpenCode CLI e o app desktop leem a mesma configuração do OpenCode. A documentação atual do OpenCode V2 usa o mapa `providers` para provedores personalizados e coloca servidores MCP em `mcp.servers`. Este exemplo usa o endpoint de chat compatível com OpenAI em `/v1`. Confira se o provedor do Aperture aceita OpenAI Chat Completions antes de usar esse caminho de modelo.

**Configuração global:** No macOS e Linux, edite `~/.config/opencode/opencode.json`. No Windows, use `%USERPROFILE%\.config\opencode\opencode.json`. Adicione um provedor compatível com OpenAI e substitua `<MODEL_ID>` pelo ID exato do modelo Aperture. O OpenCode também aceita `opencode.jsonc` na mesma pasta para comentários. A [referência de configuração](https://opencode.ai/docs/config/) explica a precedência entre as configurações globais e as do projeto.

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "model": "aperture/<MODEL_ID>",
  "providers": {
    "aperture": {
      "env": ["APERTURE_API_KEY"],
      "package": "@opencode/ai/providers/openai-compatible",
      "settings": {
        "baseURL": "http://<APERTURE_HOST>/v1"
      },
      "models": {
        "<MODEL_ID>": { "modelID": "<MODEL_ID>" }
      }
    }
  },
  "mcp": {
    "servers": {
      "aperture": {
        "type": "remote",
        "url": "http://<APERTURE_HOST>/v1/mcp",
        "oauth": false
      }
    }
  }
}
```

**Autenticação do cliente:** `oauth: false` ignora o fluxo OAuth padrão do OpenCode. O Aperture identifica o chamador pelo Tailscale. O OpenCode também exige uma entrada de autenticação do provedor, então defina `APERTURE_API_KEY=-` no ambiente local. O app desktop também precisa receber a variável. Se ele não herdar o ambiente do shell, execute `/connect` no app e digite `-` para o Aperture. Não coloque a chave do provedor upstream neste arquivo. O [guia de provedores](https://opencode.ai/docs/providers/) e o [guia MCP](https://opencode.ai/docs/mcp-servers/) do OpenCode descrevem o formato atual. Execute `opencode mcp list` para conferir o servidor e use `/mcps` no app para ver o status.

## Hermes CLI e desktop

**Configurações compartilhadas:** O Hermes Agent armazena provedores nomeados e servidores MCP em `~/.hermes/config.yaml` no macOS e Linux. Instalações nativas do Windows usam `%LOCALAPPDATA%\hermes\config.yaml`. Execute `hermes config path` para confirmar o arquivo ativo no seu sistema. `HERMES_HOME` pode substituir o local padrão. O Hermes Desktop local usa a mesma pasta Hermes e o mesmo perfil da CLI. Se o Desktop se conectar a um gateway Hermes remoto, configure o Aperture na máquina que executa Hermes e confirme que o servidor alcança a tailnet. Consulte o [guia do Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) para a configuração local e remota.

**Provedor Responses:** Adicione um provedor nomeado. O valor `api` precisa corresponder ao endpoint Responses da sua instância Aperture:

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # Adicione key_env somente se a configuração do Aperture exigir uma chave do cliente.
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**Seleção do protocolo:** Para OpenAI Chat Completions, defina `transport: chat_completions`. Para Anthropic Messages, escolha `transport: anthropic_messages` e use a URL do gateway Anthropic Messages. O guia atual de [provedores](https://hermes-agent.nousresearch.com/docs/integrations/providers) descreve os campos `api`, `transport` e `default_model` de provedores nomeados do Hermes.

**Configuração MCP:** Adicione o Aperture MCP ao mesmo arquivo YAML:

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**Verifique o Hermes:** Execute `hermes mcp` e inspecione cada conexão no seletor interativo de servidores. O Desktop local expõe o mesmo perfil de configuração. O Hermes documenta [servidores MCP HTTP remotos](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) e a [referência completa de configuração MCP](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference).

## Verifique os dois caminhos

**Faça verificações separadas** para inferência de modelos e MCP:

1. Confirme que o dispositivo tem conectividade Tailscale e consegue alcançar o gateway. No Claude Desktop, confirme que o gateway apresenta um certificado TLS confiável.
2. Envie um prompt curto por cada cliente configurado. Confirme que uma solicitação correspondente aparece na lista de sessões do Aperture.
3. Confirme que o ID do modelo selecionado corresponde a um modelo concedido à sua identidade Tailscale.
4. Abra a tela de status MCP de cada cliente ou execute o comando de listagem. Confirme que o servidor Aperture se conecta e disponibiliza as ferramentas esperadas.
5. Chame uma ferramenta somente de leitura. Compare o conteúdo retornado com a fonte upstream.
6. Confira os registros do Aperture se a chamada ao modelo ou à ferramenta falhar. Uma configuração salva não comprova que uma solicitação foi concluída.

| Sintoma | Verificação |
|---|---|
| A solicitação do modelo retorna 404 ou 405 | Confirme que o endpoint do cliente usa a rota e o protocolo corretos. Não reutilize `/codex` para Anthropic Messages ou MCP. |
| Modelo indisponível | Consulte `/v1/models` como o usuário Tailscale previsto. Verifique se o ID exato aparece e se o formato de API corresponde ao cliente. Peça a um administrador para conferir provedores ou concessões ausentes. |
| Solicitação não autorizada | Verifique se o cliente precisa de um marcador, token bearer ou encaminhamento de assinatura. Nunca copie uma chave de provedor upstream para um arquivo público do projeto. |
| O servidor MCP aparece, mas nenhuma ferramenta é exibida | Confira `/v1/mcp`, a integridade do conector, as concessões do conector e o caminho de rede do cliente até o Aperture. |
| Claude Desktop não conecta a uma URL MCP privada | Execute uma ponte local como `mcp-remote` ou use um conector público aprovado com autenticação adequada. |

## Recrie a configuração em outro dispositivo

**Novo dispositivo:** Instale o mesmo cliente e conecte primeiro o dispositivo à tailnet. Consulte `/v1/models` no novo dispositivo para descobrir os modelos concedidos à sua identidade Tailscale. Copie a estrutura da configuração e mantenha as credenciais localmente. Substitua `<APERTURE_HOST>`, `<MODEL_ID>` e `<UPSTREAM_MCP_ENDPOINT>` pelos valores da instância Aperture de destino. Mantenha um endpoint separado para cada protocolo de API e configure depois o caminho `/v1/mcp` para o tráfego das ferramentas. Por fim, verifique uma solicitação de modelo e uma chamada a uma ferramenta MCP.

**Vários gateways:** Use uma configuração separada para cada instância Aperture. Um dispositivo precisa de um endpoint Responses para Codex e Hermes, de um endpoint Anthropic Messages para Claude e do endpoint de agregação MCP para as ferramentas. Salve as credenciais de API no armazenamento local de segredos de cada cliente ou em uma variável de ambiente. Não copie chaves de API para arquivos compartilhados `config.toml`, `opencode.json`, `config.yaml` ou para um repositório público.

## Prompt reutilizável para configurar o Aperture

**Copie este prompt anonimizado** para seu assistente de programação. Substitua os marcadores pelos detalhes do gateway. O assistente precisa consultar o Aperture como sua identidade Tailscale antes de selecionar IDs de modelos.

```text
Configure meu gateway Tailscale Aperture existente e os clientes de IA instalados neste dispositivo.

Clientes incluídos: Codex CLI e desktop, Claude Code, Claude Desktop, OpenCode CLI e desktop, Hermes CLI e desktop.

Primeiro detecte se este dispositivo executa macOS, Linux ou Windows, identifique o shell ativo (por exemplo, zsh, bash ou PowerShell) e use em todo o processo os caminhos e a sintaxe de comandos dessa plataforma. Inspecione primeiro o gateway atual, a conexão Tailscale, as versões dos clientes e as configurações existentes. Consulte a documentação oficial atual. Preserve configurações sem relação com a tarefa e faça backup de cada arquivo antes de editar. Não adivinhe nomes de host, IDs de modelos, rotas de API ou credenciais. Mantenha as chaves de provedores upstream no Aperture, nunca nos arquivos dos clientes ou neste repositório.

Descubra os modelos disponíveis neste dispositivo conectado ao Tailscale:
1. Consulte `http://<APERTURE_HOST>/v1/models` usando a identidade Tailscale dos meus clientes. Se for diferente, use a URL personalizada documentada para listar modelos do gateway.
2. Leia `id` e `metadata.provider.id` de cada modelo. Essa lista representa os modelos concedidos à minha identidade. Não use a lista do administrador nem invente IDs.
3. Combine a compatibilidade de API de cada modelo com cada cliente. Codex usa OpenAI Responses. Os clientes Claude usam Anthropic Messages. OpenCode e Hermes precisam de um provedor e transporte compatíveis configurados.
4. Reutilize o modelo padrão existente de cada cliente sempre que possível. Se um cliente precisar de um padrão e eu não tiver preferência, mostre os modelos compatíveis e peça minha escolha. Claude Desktop exige que o ID exato do modelo seja digitado manualmente.
5. Se o endpoint não retornar um modelo adequado, confira a configuração do provedor e as concessões somente se eu tiver acesso administrativo. Caso contrário, informe qual acesso a modelo um administrador precisa adicionar. Não conceda acesso a si mesmo.

Localize a implantação do Aperture e a fonte da configuração. Não presuma um caminho de arquivo nem substitua a configuração inteira. OpenAI Responses exige `openai_responses`. Clientes Anthropic exigem `anthropic_messages`. Os conectores MCP ficam na configuração atual `connectors.servers`, e os clientes se conectam por `/v1/mcp`.

Antes de alterar um gateway compartilhado, prepare o diff mínimo para provedores, conectores e concessões. Aplique-o somente se eu tiver autoridade administrativa e esta solicitação autorizar alterações no gateway. Se eu não tiver essa autoridade, informe as alterações exatas propostas ao proprietário da instância. Nunca crie ou amplie concessões sem autorização explícita do proprietário. Preserve todas as configurações existentes do gateway.

Configure cada cliente instalado usando o formato oficial atual e o local específico do sistema operacional:
- Codex CLI e desktop compartilham `~/.codex/config.toml` no macOS/Linux e `%USERPROFILE%\.codex\config.toml` no Windows. Defina o provedor Aperture, um modelo compatível, `wire_api = "responses"` e MCP em `mcp_servers`.
- Claude Code usa `ANTHROPIC_BASE_URL` e MCP remoto por HTTP. Use `~/.claude/settings.json` no macOS/Linux e `%USERPROFILE%\.claude\settings.json` no Windows.
- Claude Desktop usa Modo de desenvolvedor, Configurar inferência de terceiros, Gateway, Chave de API estática, uma URL HTTPS do gateway com certificado confiável e um ID de modelo descoberto para meu usuário. Use uma ponte local `mcp-remote` para MCP privado da tailnet. Procure a configuração MCP em Configurações > Desenvolvedor > Editar configuração quando disponível. Caso contrário, use o caminho documentado para o sistema detectado.
- OpenCode usa o esquema V2 atual `providers` e `mcp.servers`. A configuração global fica em `~/.config/opencode/opencode.json` no macOS/Linux e `%USERPROFILE%\.config\opencode\opencode.json` no Windows. Defina `oauth: false` para MCP do Aperture. Use uma chave de API fictícia local quando necessário.
- Hermes usa um provedor nomeado, um transporte correspondente à API do modelo e `mcp_servers`. Use `~/.hermes/config.yaml` no macOS/Linux. No Windows, confira `hermes config path`, normalmente `%LOCALAPPDATA%\hermes\config.yaml`. Confirme se o Hermes Desktop compartilha o perfil local do Hermes.

Use HTTP para tráfego da tailnet quando o cliente aceitar. A inferência do Claude Desktop exige HTTPS com certificado confiável. Use `/v1` salvo se este gateway documentar outra rota.

Reinicie os clientes configurados. Verifique no Aperture uma solicitação de modelo por cliente e uma chamada inofensiva, somente de leitura, a uma ferramenta MCP. Informe os modelos descobertos para minha identidade, os clientes e arquivos alterados, os resultados da verificação e qualquer ação administrativa restante. Não instale software, não exponha o gateway publicamente, não faça commit nem publique.
```

## Conclusão

Uma configuração funcional do Aperture depende de três elementos: um gateway acessível, uma rota de modelo compatível com o protocolo do cliente e concessões para os modelos e conectores MCP necessários. Os mesmos padrões de configuração funcionam no macOS, Linux e Windows, mas cada cliente armazena as configurações em um local próprio do sistema operacional.

Descubra os IDs dos modelos usando a identidade Tailscale que os utilizará. Configure separadamente a inferência de modelos e `/v1/mcp`, depois verifique uma solicitação real e uma chamada somente de leitura a uma ferramenta. Ao migrar para outro dispositivo ou instância do Aperture, reutilize a estrutura deste guia, confirme as rotas e concessões dessa instância e mantenha as credenciais no armazenamento local de segredos.

## Próximos passos

**Prática com MCP:** Para entender a diferença entre um servidor salvo e uma chamada de ferramenta verificada, leia [Configuração de servidor MCP: permissões, testes de ferramentas e remoção segura](/articles/effective-ai-mcp-server-setup/). Para a arquitetura auto-hospedada mais ampla, consulte [Frota híbrida de agentes de IA: Tailscale, LiteLLM e Hermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/).

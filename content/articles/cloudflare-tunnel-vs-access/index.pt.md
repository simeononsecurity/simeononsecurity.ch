---
title: "Cloudflare Tunnel e Access: você precisa dos dois?"
date: 2026-09-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Entenda a diferença entre Cloudflare Tunnel e Access, escolha a proteção para um painel doméstico e evite publicar um aplicativo privado sem autenticação."
genre: ["Segurança de rede", "Auto-hospedagem", "Segurança em nuvem"]
tags: ["Cloudflare Tunnel", "Cloudflare Access", "Cloudflare Tunnel e Access", "Cloudflare Zero Trust", "cloudflared", "aplicativos auto-hospedados", "segurança de homelab", "acesso remoto", "provedor de identidade", "políticas de acesso", "autenticação de aplicativos", "hostname público", "proteção da origem", "túnel de saída", "tokens de serviço", "Service Auth", "MFA", "painel privado", "proxy reverso", "CGNAT"]
cover: "/img/cover/cloudflare-tunnel-vs-access.webp"
coverAlt: "Um servidor doméstico se conecta por uma passagem transparente a um gateway na nuvem com uma etapa separada de verificação de identidade."
coverCaption: ""
---

**Cloudflare Tunnel** conecta seu aplicativo ao Cloudflare. **Cloudflare Access** controla quem pode acessá-lo. Para um painel doméstico privado publicado por um hostname público, use os dois. Um túnel funcional sozinho não adiciona uma verificação de identidade. O [guia do Cloudflare para publicar aplicativos](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) explica essa diferença.

## Principais conclusões

- **Explique o caminho:** diferencie o conector, a origem e a verificação de identidade.
- **Configure uma política:** permita que pessoas específicas acessem um único painel privado.
- **Avalie a proteção:** teste caminhos de acesso permitidos, negados e alternativos.
- **Planeje o acesso:** documente requisitos separados para visitantes e automação.

## Antes de começar

**Público:** proprietários de servidores domésticos que querem proteger um painel acessado pelo navegador. O exemplo pressupõe um domínio ativo no Cloudflare, um aplicativo Web local funcionando e permissão para administrar ambos. **Esforço estimado:** 20 a 30 minutos para o exercício de política após configurar o conector. **Dificuldade:** iniciante a intermediária.

**Roteiro de leitura:** comece pelas funções dos produtos, acompanhe uma solicitação e configure e revise uma política simples. Termine escrevendo uma especificação de acesso para seu serviço.

## O que cada produto faz

A **origem** é o servidor que executa seu aplicativo. O conector **`cloudflared`** inicia conexões da sua infraestrutura para o Cloudflare, por isso a origem não precisa de um endereço IP publicamente roteável. Solicitações e respostas passam então pela conexão estabelecida. [Visão geral do Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

| Pergunta | Tunnel | Access |
|---|---|---|
| **Como o Cloudflare chega ao meu servidor?** | Estabelece a conexão | Não substitui a conectividade com a origem |
| **Quem recebe acesso?** | Não oferece login de usuário por conta própria | Avalia as políticas de acesso configuradas |
| **O que devo configurar?** | Conector e rota do aplicativo | Aplicativo, provedor de identidade e políticas |
| **O que o sucesso comprova?** | A origem está acessível pela rota | Uma solicitação atendeu à política configurada |

Um **provedor de identidade (IdP)** autentica o visitante. Uma **política do Access** define uma ação e critérios de correspondência. Allow autoriza os usuários correspondentes. Bypass desativa a aplicação do Access para o tráfego correspondente. [Referência de políticas do Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

## Acompanhe uma solicitação do navegador

Para **`dashboard.example.com`**, o caminho lógico da solicitação é:

```text
Navegador -> Cloudflare Access -> conexão do túnel -> cloudflared -> painel
                     |
                     +-> provedor de identidade quando a autenticação é necessária
```

O **conector inicia a conexão do túnel de saída** a partir da sua rede. As solicitações do navegador seguem pela conexão estabelecida até a origem. Uma conexão de saída que transporta solicitações de entrada do aplicativo é o principal motivo para o Tunnel funcionar sem o encaminhamento convencional de uma porta da origem. [Modelo de conexão do Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

**As permissões do aplicativo** exigem outra decisão. O acesso a um painel não define automaticamente quem pode alterar configurações ou excluir dados. Se o aplicativo tiver funções de visualização e administração, configure e teste cada uma separadamente.

Por exemplo, **um familiar com acesso de visualização** precisa ver o estado dos backups, enquanto você precisa alterar os destinos. Registre esses requisitos antes de escolher as identidades. Duas pessoas que passam pela mesma verificação do Access não devem receber automaticamente os mesmos privilégios no aplicativo.

## Quando você precisa dos dois

**O público determina a proteção.** Compare estas opções antes de publicar uma rota:

| Público pretendido | Configuração sugerida | Revise antes de usar |
|---|---|---|
| **Qualquer pessoa que leia um site público** | Tunnel, se necessário para conectar à origem | A exposição pública é intencional |
| **Você e alguns familiares** | Tunnel e Access | Permita apenas as identidades pretendidas |
| **Uma origem pública existente** | Access com proteção separada da origem | O acesso direto à origem não deve ignorar a verificação |
| **Um script agendado** | Tunnel e uma política Service Auth | O cliente aceita o método de autenticação |

**Access sem Tunnel** funciona com uma origem que já está acessível. Proteja também os caminhos alternativos até o servidor. O Cloudflare recomenda criar o aplicativo Access primeiro ao publicar uma nova rota de túnel. [Requisitos para aplicativos auto-hospedados](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/).

*Para um painel doméstico privado acessado por um hostname público, comece com Tunnel e Access.*

## Configure a política do painel

Use esta **configuração guiada** para dois visitantes pretendidos. Substitua os dois endereços de exemplo por identidades que você controla. Crie o aplicativo Access antes de adicionar a rota pública do túnel.

1. **Aplicativo:** abra Zero Trust → Access controls → Applications e crie um aplicativo auto-hospedado com um hostname público.
2. **Hostname:** informe o hostname exclusivo do painel. Deixe o caminho sem restrições neste exemplo que abrange o hostname inteiro.
3. **Política:** crie uma política Allow chamada `Dashboard viewers`.
4. **Seletor de identidade:** adicione uma regra Include usando Emails e substitua `alice@example.com` e `bob@example.com` pelos dois endereços pretendidos.
5. **Login:** selecione o provedor de identidade usado pelos visitantes e escolha deliberadamente a duração da sessão.
6. **Rota:** salve o aplicativo e conecte o hostname ao painel pelo túnel.

O [fluxo oficial de configuração de aplicativos](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) documenta essas opções. **Resultado esperado:** um novo visitante encontra a autenticação antes de acessar o aplicativo. Conclua o teste com identidade negada abaixo antes de confiar na política.

## Entenda a lógica das regras

**Include** combina alternativas com OR. **Require** adiciona condições obrigatórias com AND. **Exclude** remove os usuários correspondentes. Adicionar outra condição Include amplia o grupo elegível. [Semântica das regras do Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

| Trecho da política | Efeito lógico |
|---|---|
| **Include Alice or Bob** | Uma das identidades indicadas é suficiente |
| **Include Alice, Include a country** | Pessoas que correspondem ao país também são admitidas |
| **Include Alice, Require a country** | Alice também precisa atender à condição de país |

**Exercício de revisão da política:** seu requisito cita apenas Alice e Bob, mas um colega adiciona um país como outra condição Include. Rejeite a alteração porque ela admite uma população adicional. A localização geográfica não comprova que alguém pertença à sua família.

## Autentique scripts agendados

Um **token de serviço** contém um Client ID e um Client Secret para solicitações automatizadas. Configure a política do aplicativo para aceitar o token por meio do **Service Auth**. Criar um token sem a política correspondente não concede acesso ao aplicativo. [Tokens de serviço do Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

Para um script de backup ou uma verificação de monitoramento, mantenha o **segredo** no armazenamento protegido de credenciais da ferramenta. Dê a cada integração um nome de token exclusivo e uma data de validade definida conscientemente. Troque ou revogue o token ao desativar a integração. A documentação dos tokens de serviço explica essas etapas do ciclo de vida.

**Verifique explicitamente a compatibilidade do cliente.** Uma ferramenta que espera uma resposta de API talvez não aceite login interativo pelo navegador. Antes de escolher a política, confirme o suporte a cabeçalhos de solicitação ou a outro método de autenticação aceito.

## Teste as decisões de acesso

Use estes **critérios de aceitação** para sua implantação:

| Verificação | Evidência a registrar |
|---|---|
| **Visitante desconectado** | O Access intercepta uma solicitação de uma nova sessão do navegador |
| **Identidade permitida** | O aplicativo pretendido carrega após o login |
| **Identidade negada** | Uma conta não listada não consegue acessar o aplicativo |
| **Rota alternativa** | Nomes DNS antigos e portas da origem não oferecem acesso não intencional |
| **Automação** | O cliente aprovado funciona e uma solicitação sem credencial falha |

**Uma tela de login visível** comprova apenas que um caminho exigiu autenticação. Teste também a rejeição e os caminhos alternativos. São verificações sugeridas, não resultados de um exemplo implantado.

## Verifique o limite da origem

Uma **origem que confia na identidade do Access** deve validar o token de aplicativo assinado. O Cloudflare o encaminha no cabeçalho **`Cf-Access-Jwt-Assertion`**. A presença do cabeçalho, por si só, não comprova autenticidade. [Validação de JWT do Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/).

Um **JSON Web Token (JWT)** contém declarações assinadas. Ao integrar a identidade do Access a uma origem, use o método de validação documentado, incluindo o emissor esperado e o público-alvo do aplicativo. Decodificar um token e ler um campo de e-mail não é validação suficiente.

**Issuer** identifica a autoridade que emite o token. **Audience** identifica o aplicativo pretendido. Verifique a validade e a expiração do token usando uma biblioteca de validação compatível, em vez de implementar as verificações da assinatura por conta própria.

**Defina o limite com clareza:** identifique onde ocorre a validação e quais rotas chegam ao aplicativo. Uma antiga regra de encaminhamento de porta ou um hostname alternativo merece uma revisão própria, mesmo depois que o hostname principal passar por todos os testes no navegador.

## Resolva incompatibilidades nas políticas

| Observação | Próxima verificação |
|---|---|
| **Um visitante inesperado consegue entrar** | Revise as condições Include, as políticas Bypass e a cobertura de hostnames |
| **Um visitante pretendido é negado** | Compare a identidade autenticada com os valores exatos do seletor |
| **Um script recebe uma página de login** | Revise a credencial e a política Service Auth |
| **Um visitante autorizado altera configurações** | Revise as funções da própria aplicação |

**O comportamento da sessão** também afeta os novos testes. O Access tem várias durações de sessão, incluindo sessões de aplicativo e globais. Registre a configuração e use uma nova sessão ao testar outra identidade. [Gerenciamento de sessões do Access](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/).

## Escreva sua especificação de acesso

Prepare uma **especificação curta** antes de adicionar outro serviço:

```text
Serviço e hostname:
Identidades humanas permitidas:
Funções exigidas no aplicativo:
Credencial de automação e validade:
Outras rotas até a origem:
Local de validação dos tokens do Access:
Resultado do teste com identidade permitida:
Resultado do teste com identidade negada:
```

**Critério de conclusão:** outro administrador deve entender quem tem acesso, como cada cliente se autentica e qual evidência comprova a rejeição. Se você adicionar uma integração de monitoramento, atualize a credencial e repita a verificação da solicitação sem autenticação.

## Próximos passos

Siga o [guia de configuração do Cloudflare Tunnel](/guides/how-to-setup-and-use-cloudflare-tunnels/) para configurar o conector e depois aplique o [fluxo oficial do aplicativo Access](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/). Para uma conexão celular, consulte os [limites de encaminhamento de portas da T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/) antes de escolher a rota de acesso remoto.

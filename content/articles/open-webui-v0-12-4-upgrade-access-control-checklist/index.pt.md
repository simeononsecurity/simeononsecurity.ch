---
title: "Open WebUI v0.12.4: checklist de atualização e controle de acesso 2026"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Faça backup e atualize o Open WebUI para a versão v0.12.4. Em seguida, teste o compartilhamento de conversas, as permissões de exportação, as concessões de recursos, as contas e o acesso à rede."
genre: ["IA auto-hospedada", "Cibersegurança", "Administração de sistemas"]
tags: ["Open WebUI", "Open WebUI v0.12.4", "atualização do Open WebUI", "segurança do Open WebUI", "controle de acesso do Open WebUI", "IA auto-hospedada", "atualização do Docker", "atualização do pip", "backup do Open WebUI", "permissões do Open WebUI", "funções do Open WebUI", "grupos do Open WebUI", "permissão de exportação de conversas", "conversas compartilhadas", "conversas arquivadas", "acesso à base de conhecimento", "acesso a modelos", "permissões de ferramentas", "segurança de chaves de API", "segurança da conta de administrador", "desativar inscrições", "autenticação do proxy reverso", "acesso VPN", "fixação da imagem do contêiner"]
---

**O Open WebUI v0.12.4 contém correções de segurança que os mantenedores ainda não detalharam.** As notas da versão recomendam atualizar as instalações prontamente e dizem que os avisos virão após a atribuição de CVEs. As mudanças mencionadas abaixo sobre compartilhamento de conversas e permissões são os itens visíveis nas notas, não uma lista completa das correções de segurança ainda não divulgadas. [Notas da versão do Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

<!--more-->

## Principais pontos

- **Faça backup primeiro.** Mantenha uma cópia recuperável do volume de dados ou banco de dados e dos uploads antes de alterar a aplicação.
- **Fixe a versão oficial.** Use `ghcr.io/open-webui/open-webui:v0.12.4` para a imagem Docker padrão ou `open-webui==0.12.4` para pip.
- **Teste permissões com funções reais de usuário.** Um botão oculto não comprova uma verificação de autorização no lado da API.
- **Mantenha o acesso privado.** Exija autenticação da aplicação e restrinja o acesso à rede por VPN ou proxy reverso autenticado.

## Antes de atualizar

**Pré-requisitos:** identifique o método de instalação atual, a variante da imagem do contêiner, o local dos dados persistentes, o banco de dados externo, o proxy reverso e o provedor de autenticação. Agende uma janela de indisponibilidade e mantenha a configuração atual do contêiner ou a definição do serviço. Reserve tempo para ensaiar uma restauração em uma instância separada. Os comandos abaixo são padrões documentados pelo fornecedor e adaptados a esta versão fixada. Eles não resultam de uma atualização real feita para este guia. [Atualizar o Open WebUI](https://docs.openwebui.com/getting-started/updating/)

1. **Faça o inventário do armazenamento.** Na configuração Docker padrão, `open-webui` é montado em `/app/backend/data`. Registre os bind mounts, o banco de dados externo, o armazenamento de objetos e as variáveis de ambiente personalizadas. Com pip, localize o diretório de dados ativo da aplicação e o banco de dados antes de alterar o ambiente. Não suponha que uma exportação de conversa seja um backup completo.
2. **Faça backup com as gravações interrompidas.** Pare a aplicação ou use um snapshot consistente do banco de dados. Depois, copie o volume, qualquer banco externo e os uploads para um armazenamento separado. O fornecedor documenta um arquivo de volume Docker. Adapte o nome do volume e o caminho de backup à sua instalação. Confirme que o arquivo abre e ensaie uma restauração em outra instância antes de confiar nele. [Backup e restauração](https://docs.openwebui.com/getting-started/updating/#backup--restore)
3. **Leia as notas da versão e as instruções de migração.** As notas da v0.12.4 não enumeram as correções de segurança pendentes nem informam o intervalo de versões afetadas. Não atribua um CVE a essas correções nem suponha que toda versão anterior à v0.12.4 seja afetada por uma falha específica. O guia de atualização alerta sobre migrações de banco de dados unidirecionais e réplicas com versões diferentes. Se vários workers ou réplicas compartilham um banco de dados, interrompa-os juntos e siga o [procedimento de migração para várias réplicas](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations). Uma reversão talvez exija o backup do banco de dados anterior à atualização.

## Atualize o pacote instalado

**Docker, procedimento do fornecedor adaptado a uma tag fixada:** após o backup, baixe a imagem padrão oficial e recrie o contêiner com o *mesmo* volume persistente, configuração e `WEBUI_SECRET_KEY`. O exemplo pressupõe o volume nomeado padrão e um proxy upstream vinculado localmente. Não cole a chave real no histórico do shell. Forneça-a pelo mecanismo protegido de ambiente ou de gerenciamento de segredos existente. Preserve as opções de GPU, Ollama, rede personalizada, banco de dados e demais opções da instalação atual. [Atualizar o Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Tags oficiais das imagens](https://docs.openwebui.com/getting-started/quick-start/)

```bash
docker pull ghcr.io/open-webui/open-webui:v0.12.4
docker rm -f open-webui
docker run -d --name open-webui --restart always \
  -p 127.0.0.1:3000:8080 \
  -v open-webui:/app/backend/data \
  --env-file ./open-webui.env \
  ghcr.io/open-webui/open-webui:v0.12.4
```

**Confira `./open-webui.env` antes de executar:** o arquivo já deve existir, ter permissões restritivas e conter o `WEBUI_SECRET_KEY` atual e a configuração necessária. A vinculação ao loopback atende a um proxy no mesmo host, não a um proxy em outra máquina. Com Compose, altere somente a imagem do serviço para a tag fixada. Depois, execute `docker compose pull open-webui` e `docker compose up -d open-webui` no projeto existente. Mantenha o mesmo volume e a configuração de ambiente. Esses são comandos sugeridos, não uma migração testada da sua instalação.

**pip, procedimento do fornecedor com versão fixa:** no ambiente virtual existente, pare o serviço, instale a versão exata do pacote e reinicie-o com o mesmo diretório de dados e ambiente. Evite um segundo ambiente Python ou um novo banco de dados vazio. A instrução genérica do fornecedor usa `pip install -U open-webui`. A restrição de versão abaixo fixa esta checklist na v0.12.4. [Atualizar o Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Início rápido](https://docs.openwebui.com/getting-started/quick-start/)

```bash
python -m pip install --upgrade 'open-webui==0.12.4'
python -m pip show open-webui
```

**Verifique o serviço em execução, não apenas o artefato instalado.** Confira a versão de inicialização em `docker logs open-webui` ou nos logs do serviço pip e compare-a à versão exibida pela aplicação após entrar. O guia de atualização do fornecedor recomenda conferir os logs do contêiner e abrir a página de login. Se a interface exibir recursos desatualizados, force a atualização do navegador. Se a inicialização indicar erro de migração, mantenha o serviço indisponível até diagnosticar a causa. Não instale um binário antigo sobre um banco migrado sem conferir os requisitos de restauração. [Verificações pós-atualização](https://docs.openwebui.com/getting-started/updating/)

## Verifique o acesso após reiniciar

**Comportamento informado pelo fornecedor:** a v0.12.4 oculta as ações de exportar pastas, exportar conversas arquivadas e copiar conversas para usuários sem **Allow Chat Export**. Também oculta os controles de acesso a modelos, prompts, ferramentas, conhecimentos, habilidades, notas e pastas para quem não tem a permissão de compartilhamento correspondente. Quem visualiza uma pasta compartilhada deixa de receber atualizações de conversa ao vivo depois que o proprietário arquiva uma conversa. Quem acessa um link compartilhado deixa de receber essas atualizações depois que o proprietário cancela o compartilhamento de todas as conversas. Controles ocultos são um comportamento da interface, não uma prova de correção no servidor para uma vulnerabilidade não especificada. [Notas da versão](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

**Verificação recomendada ao operador:** com uma conta de teste sem permissões de exportação e compartilhamento, confirme que as ações indicadas não aparecem. Com uma conta autorizada, confirme que as ações esperadas continuam funcionando. Crie uma conversa de teste não sensível em uma pasta compartilhada, abra-a por outra conta, arquive-a como proprietário e confirme que as novas atualizações deixam de chegar ao outro usuário. Repita com um link compartilhado e **Unshare All Chats**. Confira novamente as concessões salvas e os links antigos. Não suponha que conteúdo arquivado ou cópias históricas foram apagados.

| Área de revisão | O que verificar |
|---|---|
| **Funções e grupos** | Remova membros e atribuições de administrador obsoletos. Confira as permissões efetivas de um usuário recém-aprovado e de um usuário restrito. |
| **Modelos e ferramentas** | Revise as concessões de acesso de cada modelo, as ferramentas anexadas, os direitos de criação de ferramentas e as credenciais do provedor. Teste com uma conta sem privilégios de administrador. |
| **Conhecimentos e arquivos** | Inspecione colaboradores da base de conhecimento, concessões de recursos, anexos e configurações de compartilhamento. Confira uma conta cujo acesso foi removido. |
| **Conversas e exportações** | Revise pastas compartilhadas, links, conversas arquivadas e atribuições de Allow Chat Export. Revogue links desnecessários. |

Essas verificações de inventário são **recomendações ao operador**, não novas garantias introduzidas pela v0.12.4. O [guia de hardening](https://docs.openwebui.com/getting-started/advanced-topics/hardening/) do fornecedor documenta funções em camadas, grupos, concessões por recurso, permissões do espaço de trabalho, chaves de API e posicionamento na rede.

## Feche as lacunas de conta e rede

- **Inscrições, configuração do fornecedor:** desative inscrições abertas quando um administrador ou provedor de identidade provisionar contas. Confira `ENABLE_SIGNUP` e as configurações persistentes de administrador no [guia de hardening](https://docs.openwebui.com/getting-started/advanced-topics/hardening/). Mantenha regras restritivas de aprovação para novas contas.
- **Chaves de API, revisão do operador:** inventarie as chaves emitidas, exclua as sem uso e restrinja a criação e o acesso aos endpoints às funções e rotas necessárias. Segundo o guia do fornecedor, uma chave atua com as permissões de quem a criou. Mantenha as chaves fora dos exemplos e dos logs da aplicação.
- **Administradores, revisão do operador:** remova contas de administrador abandonadas, aplique controles de login fortes, confira a disponibilidade de MFA e investigue alterações inesperadas de contas. Teste a recuperação da conta antes de desativar um administrador redundante.
- **Limite de rede, orientação do fornecedor:** coloque o serviço atrás de uma VPN, proxy de acesso ou proxy reverso com autenticação e lista de IPs permitidos. Não o exponha publicamente sem autenticação. Evite `WEBUI_AUTH=False` em um serviço acessível. Um proxy reverso sem autenticação própria não substitui o login da aplicação. [Proteja o Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)

**Escopo:** esta checklist cobre o lançamento oficial do Open WebUI e os caminhos padrão documentados de instalação. Ela não verifica forks, imagens derivadas ou pacotes de terceiros. As notas da v0.12.4 não afirmam que exista exploração ativa. Consulte os [avisos de segurança do projeto](https://github.com/open-webui/open-webui/security/advisories) para divulgações posteriores e suas próprias versões afetadas e corrigidas. Não atribua à v0.12.4 a correção de um aviso anterior sem ler seu intervalo de versões.

## Fontes e referências

- [Notas da versão do Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)
- [Avisos de segurança do Open WebUI](https://github.com/open-webui/open-webui/security/advisories)
- [Atualizar o Open WebUI, incluindo backup, reversão e migrações](https://docs.openwebui.com/getting-started/updating/)
- [Início rápido do Open WebUI e tags oficiais das imagens](https://docs.openwebui.com/getting-started/quick-start/)
- [Fortalecer o Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)
- [Atualizações e migrações para várias réplicas](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations)

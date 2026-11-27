---
title: "Guia de SSH: acesso remoto seguro, chaves e transferência de arquivos"
date: 2023-06-14
lastmod: 2026-11-26
toc: true
draft: false
description: "Saiba o que o SSH faz, como criar chaves, verificar chaves de host, transferir arquivos e gerenciar as configurações do cliente e do servidor."
tags: ["SSH", "Secure Shell", "acesso remoto", "administração remota", "criptografia", "autenticação", "integridade de dados", "portabilidade", "transferência de arquivos", "SCP", "SFTP", "chaves SSH", "Ed25519", "configuração SSH", "hosts conhecidos", "protocolo de rede", "execução remota de comandos", "OpenSSH", "autenticação de dois fatores", "criptografia de chave pública", "endereço IP", "nome de domínio", "terminal", "prompt de comando", "segurança", "administradores de sistemas", "desenvolvedores", "métodos de autenticação", "tunelamento"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_securely_connecting.webp"
coverAlt: "Ilustração em estilo cartoon de uma pessoa conectando-se com segurança a um servidor usando SSH."
coverCaption: ""
---

**O que é SSH e como usá-lo?**

**SSH** (Secure Shell) é um protocolo de rede para login remoto criptografado, execução de comandos, encaminhamento de portas e transferência de arquivos. Um cliente SSH conecta-se a um servidor SSH por uma rede não confiável. O servidor comprova sua identidade com uma chave de host. Depois, o usuário se autentica com uma senha, uma chave pública ou outro método configurado.

O [manual do comando `ssh(1)` do OpenBSD](https://man.openbsd.org/ssh) descreve o cliente como uma ferramenta para comunicação criptografada segura entre hosts não confiáveis. Este guia se concentra no **OpenSSH**, a implementação encontrada em muitos sistemas Linux, macOS, BSD e Windows.

{{< youtube id="Atbl7D_yPug" enable="true" >}}

**Dificuldade:** iniciante. **Tempo:** 15 minutos.

## Principais pontos

- O SSH verifica a chave de host do servidor antes da autenticação do usuário.
- Uma chave Ed25519 protegida por frase secreta é uma boa opção inicial para novos usuários.
- Use `ssh` para comandos remotos, `scp` para copiar arquivos e `sftp` para transferências interativas.
- Teste uma chave nova em outra sessão antes de desativar a autenticação por senha.

## Antes de começar

- Instale um cliente OpenSSH no computador local.
- Obtenha o nome de host ou endereço IP remoto, o nome da conta, a porta SSH e um método de autenticação aprovado.
- Obtenha a impressão digital da chave de host do servidor em um console confiável, registro administrativo ou outra fonte independente.
- Mantenha disponível uma sessão de login por senha ou um console local ao instalar uma chave pública ou alterar as configurações do servidor.

Os comandos de shell deste guia usam sintaxe POSIX no Linux, macOS, BSD ou em um ambiente compatível. Usuários do OpenSSH no Windows devem adaptar caminhos de arquivos e comandos de permissões para PowerShell ou WSL. Execute comandos do cliente no computador local. Execute comandos do servidor, inclusive `sshd -t`, no servidor SSH com acesso à configuração e às chaves de host.

## SSH em resumo

| Tarefa | Ferramenta | Resultado |
|------|------|--------|
| **Login remoto** | `ssh` | Abrir um shell ou executar um comando em um host remoto |
| **Criação de chave** | `ssh-keygen` | Criar uma chave privada e uma chave pública correspondente |
| **Cópia de arquivos** | `scp` | Copiar arquivos por uma conexão SSH |
| **Transferência interativa** | `sftp` | Navegar e transferir arquivos por SFTP |
| **Configurações do cliente** | `~/.ssh/config` | Armazenar opções de conexão por host |
| **Configurações do servidor** | `/etc/ssh/sshd_config` | Configurar o daemon OpenSSH |

*O canal criptografado protege o transporte. Ainda é preciso verificar o destino, restringir as chaves e revisar cada comando remoto.*

## Benefícios do SSH

O SSH separa a **autenticação do host** da **autenticação do usuário**. O cliente verifica a chave de host do servidor, uma identidade criptográfica do servidor. Em seguida, o servidor verifica a senha, a chave pública ou outro método permitido do usuário.

1. **Segurança:** o SSH criptografa a sessão entre o cliente e o servidor. A criptografia protege credenciais, comandos e dados retornados enquanto atravessam uma rede não confiável.

2. **Autenticação:** o SSH oferece suporte a senhas, chaves públicas, métodos interativos por teclado e outros métodos aprovados pelo servidor. A autenticação por chave pública mantém a chave privada no cliente e envia uma prova de posse durante o login.

3. **Integridade dos dados:** o transporte SSH protege as mensagens contra modificações não detectadas. Uma sessão criptografada válida ainda depende da verificação correta da chave de host.

4. **Portabilidade:** há clientes e servidores OpenSSH para Linux, macOS, BSD e Windows. O fluxo básico com `ssh`, `scp` e `sftp` funciona nessas plataformas.

5. **Flexibilidade:** o SSH oferece comandos remotos, transferência de arquivos, encaminhamento de portas e outros recursos de conexão. Use cada recurso somente para uma finalidade e um destino aprovados.

| Opção de autenticação | Vantagem | Compromisso operacional |
|-----------------------|----------|-----------------------|
| **Senha** | Familiar e fácil de implantar | Sujeita a tentativas de adivinhação e reutilização de credenciais |
| **Chave pública** | A chave privada permanece no cliente | Exige planejamento do ciclo de vida e da recuperação da chave |
| **Chave pública com frase secreta** | Acrescenta proteção caso o arquivo de chave privada seja copiado | Exige informar a frase secreta ou usar um agente SSH |
| **Autenticação interativa ou multifator (MFA)** | Acrescenta um desafio controlado pelo servidor | Requer suporte no servidor e no cliente |

***Uma chave de usuário protegida por frase secreta é a escolha padrão para administração interativa.***

## Como usar o SSH

### Gerar chaves SSH

Antes de usar autenticação por chave pública, crie um par de chaves SSH. O par contém uma **chave pública** para a conta remota e uma **chave privada** para o cliente local. Coloque a chave pública no arquivo `~/.ssh/authorized_keys` da conta remota. Mantenha a chave privada no cliente e proteja-a com uma frase secreta.

1. Instale o **OpenSSH** no computador local se ainda não estiver instalado. Consulte a documentação oficial do sistema operacional.

2. Abra um terminal ou prompt de comando e execute o comando a seguir para gerar o exemplo RSA original:

```shell

ssh-keygen -t rsa -b 4096

```

Para uma nova chave de usuário, use **Ed25519** em sistemas com suporte a versões atuais do OpenSSH:

```shell
ssh-keygen -t ed25519 -C "reader@example.com"
```

O manual atual do OpenBSD lista Ed25519 como o tipo de chave padrão quando `ssh-keygen` não recebe a opção `-t`. O comando RSA original ainda é útil em sistemas antigos ou por requisitos de compatibilidade. A opção `-b` controla o tamanho da chave RSA. Ed25519 usa um tamanho fixo.

3. Quando solicitado, informe um nome de arquivo e uma frase secreta forte. Pressione Enter para aceitar o nome padrão somente se essa chave atender à conta pretendida. Uma frase secreta em branco deixa uma chave privada copiada sem proteção em repouso.

4. O par de chaves será gerado. O nome da chave pública termina em `.pub`. A chave privada não tem extensão e deve permanecer privada.

Instale a chave pública por um login existente com senha ou por uma sessão no console local. Em um sistema com `ssh-copy-id`, execute:

```shell
ssh-copy-id -i ~/.ssh/id_ed25519.pub username@remote_server_ip
```

Use `~/.ssh/id_ed25519.pub` com o comando Ed25519. O comando RSA preservado cria `~/.ssh/id_rsa.pub`; substitua o caminho pelo arquivo RSA ao instalar uma chave RSA. Se `ssh-copy-id` não estiver disponível, execute isto no cliente por meio de um login existente com senha:

```shell
cat ~/.ssh/id_ed25519.pub | ssh username@remote_server_ip 'umask 077 && mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys'
```

O comando cria um diretório remoto `.ssh` privado e acrescenta uma linha de chave pública. Verifique se o arquivo remoto `~/.ssh/authorized_keys` contém a chave pretendida. O arquivo `authorized_keys` lista as chaves públicas autorizadas a fazer login. Se um console local for o único caminho de acesso, acrescente a mesma linha de chave pública por ele e defina as permissões de `~/.ssh` como `700` e de `authorized_keys` como `600`.

Se você escolheu o exemplo RSA, substitua cada caminho `id_ed25519` posterior por `id_rsa`.

Abra outro terminal e teste a chave antes de alterar as configurações de autenticação do servidor:

```shell
ssh -o PreferredAuthentications=publickey -o PasswordAuthentication=no -i ~/.ssh/id_ed25519 username@remote_server_ip
```

Confirme que a nova sessão abre com a conta pretendida. Mantenha a sessão existente disponível para recuperação caso o teste falhe.

Confira a impressão digital de uma chave pública antes de instalá-la ou auditá-la:

```shell
ssh-keygen -l -f ~/.ssh/id_ed25519.pub
```

*Não cole uma chave privada em um chamado, conversa, histórico do shell ou comando remoto. Substitua a chave privada após suspeita de exposição e remova a chave pública de todas as contas autorizadas.*

### Conectar a um servidor remoto

Para conectar-se a um servidor remoto por SSH, siga estas etapas:

1. Obtenha o **endereço IP** ou nome de domínio do servidor remoto desejado.

2. Abra um terminal ou prompt de comando e use o comando abaixo para iniciar uma conexão SSH:

```shell
ssh username@remote_server_ip
```

Substitua `username` pelo seu nome de usuário no servidor remoto e `remote_server_ip` pelo endereço IP real ou nome de domínio do servidor.

3. Na primeira conexão, o SSH exibe um aviso sobre a chave de host. Compare a impressão digital com a de um console confiável, registro administrativo ou outra fonte independente antes de aceitar a chave. O cliente armazena as chaves de host aceitas em `~/.ssh/known_hosts`.

4. Quando solicitado, informe a senha da conta ou a frase secreta da chave privada selecionada. Selecione uma chave específica com a opção `-i`:

```shell
ssh -i ~/.ssh/id_ed25519 username@remote_server_ip
```

5. Se a autenticação funcionar, o SSH abre um shell remoto. Investigue uma alteração na chave de host antes de tentar fazer login novamente. Não ignore a verificação da chave de host para silenciar um aviso.

Para examinar impressões digitais já armazenadas para hosts conhecidos:

```shell
ssh-keygen -l -f ~/.ssh/known_hosts
```

### Transferir arquivos com SSH

O SSH também oferece transferência segura de arquivos. O **SCP** copia arquivos por uma conexão SSH. O **SFTP** fornece uma sessão interativa de transferência de arquivos.

1. Abra um terminal ou prompt de comando no computador local.

2. Use o comando abaixo para copiar um arquivo do computador local para o servidor remoto:

```shell

scp /path/to/local/file username@remote_server_ip:/path/to/remote/location

```

Substitua `/path/to/local/file` pelo caminho e nome reais do arquivo no computador local. Do mesmo modo, substitua `username@remote_server_ip:/path/to/remote/location` pelo usuário apropriado, endereço IP do servidor ou local remoto do arquivo.

Selecione uma chave privada específica com `-i` quando a configuração do cliente não escolher a chave pretendida:

```shell
scp -i ~/.ssh/id_ed25519 /path/to/local/file username@remote_server_ip:/path/to/remote/location
```

3. Na primeira conexão, costuma aparecer um aviso sobre a autenticidade do host. Verifique a impressão digital do servidor antes de continuar.

4. Se solicitado, informe a senha da conta ou a frase secreta da chave privada selecionada. O arquivo será copiado pela conexão SSH.

Para uma sessão interativa do Protocolo de Transferência de Arquivos SSH (SFTP), use:

```shell
sftp username@remote_server_ip
```

Desde o OpenSSH 9.0, `scp` usa SFTP por padrão nas transferências. A opção `-O` seleciona o protocolo SCP legado para compatibilidade com um servidor ou padrão de nome de arquivo que exige o modo antigo. Prefira o modo padrão, a menos que uma necessidade de compatibilidade documentada exija `-O`.

### Configuração do SSH

Os arquivos de configuração do SSH personalizam o comportamento do cliente e do servidor. O arquivo principal do servidor costuma ser `/etc/ssh/sshd_config`. O arquivo do cliente por usuário é `~/.ssh/config`.

Crie um alias de cliente para reutilizar as mesmas configurações revisadas nas conexões:

```sshconfig
Host lab-server
    HostName remote_server_ip
    User username
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
```

Conecte-se usando o alias:

```shell
ssh lab-server
```

`IdentityFile` seleciona a chave. `IdentitiesOnly yes` limita as tentativas de autenticação às identidades configuradas. Proteja o diretório e o arquivo de configuração do cliente:

```shell
chmod 700 ~/.ssh
chmod 600 ~/.ssh/config
```

Por padrão, o daemon OpenSSH lê chaves públicas de `~/.ssh/authorized_keys`. No servidor, antes de aplicar uma alteração de configuração, teste a sintaxe da configuração do daemon e a disponibilidade da chave de host com:

```shell
sshd -t
```

Execute esta verificação no servidor com as permissões necessárias para ler a configuração e as chaves de host. Ela não testa a chave autorizada de um usuário nem comprova que o login por chave pública funciona. Mantenha uma sessão existente aberta ao testar uma chave nova. Defina `PasswordAuthentication no` somente depois que um login separado com chave pública funcionar e houver um caminho de recuperação.

| Área de configuração | Arquivo ou opção | Pergunta de revisão |
|-------------------|----------------|-----------------|
| **Alias do cliente** | `~/.ssh/config` | O alias aponta para o host e o usuário corretos? |
| **Identidade do cliente** | `IdentityFile` | A chave pertence à conta pretendida? |
| **Seleção de identidade** | `IdentitiesOnly` | O cliente oferecerá somente a chave revisada? |
| **Autorização do servidor** | `~/.ssh/authorized_keys` | Cada chave tem responsável e plano de remoção? |
| **Alternativa por senha** | `PasswordAuthentication` | Há um caminho de recuperação testado antes da alteração? |

## Solução de problemas de SSH

Comece pela configuração efetiva do cliente e pela saída detalhada. Essas verificações revelam aliases ou usuários incorretos, chaves inesperadas e caminhos dos arquivos de chave de host sem alterar as configurações do servidor:

```shell
ssh -G lab-server
ssh -vvv lab-server
```

Se a autenticação por chave falhar, verifique estes itens nesta ordem:

- **Identidade do host:** compare a impressão digital apresentada com um registro confiável.
- **Par de chaves:** compare a impressão digital da chave pública local com a chave instalada para a conta remota.
- **Permissões de arquivos:** mantenha `~/.ssh` privado e proteja `config`, chaves privadas e `authorized_keys` contra outros usuários.
- **Seleção do cliente:** confira `IdentityFile` e `IdentitiesOnly` na configuração efetiva.
- **Sintaxe do servidor:** execute `sshd -t` antes de recarregar uma configuração alterada.
- **Recuperação:** mantenha uma sessão administrativa separada até que um novo login funcione.

Se a conexão falhar, separe a verificação da rede da verificação da autenticação:

- **Resolução de nomes:** teste o host com as ferramentas DNS do sistema operacional. Tente o IP do servidor somente após confirmar o endereço por uma fonte confiável.
- **Porta e firewall:** use a porta SSH configurada no servidor. Confirme se o firewall permite a rede do cliente.
- **Conexão recusada:** verifique se o daemon SSH está em execução e escutando no endereço e na porta esperados.
- **Tempo limite:** verifique roteamento, grupos de segurança, firewalls do host e acesso à VPN antes de alterar chaves.
- **Logs do servidor:** examine os logs do daemon SSH para identificar o usuário, a chave ou a política rejeitados.
- **Permissões da chave remota:** confirme que a conta é proprietária de `~/.ssh`, que `authorized_keys` tem permissões restritas e que o diretório pessoal permite que o SSH leia o caminho.

## Conclusão

SSH é um protocolo seguro para acesso remoto e administração de servidores e computadores. A criptografia, as verificações de chaves de host, os métodos de autenticação e as ferramentas de transferência de arquivos atendem administradores, desenvolvedores e outros usuários autorizados.

Comece com uma chave protegida por frase secreta, verifique a impressão digital do servidor, use um alias de cliente por host e mantenha uma sessão de recuperação aberta durante alterações no servidor. Essas medidas criam um fluxo de trabalho repetível sem tratar a criptografia como substituta do controle de acesso.

Como próximo passo, leia o [guia de fortalecimento da segurança do Linux](/articles/dos-and-donts-for-hardening-linux/) para controles no host. Para uma administração repetível, veja [Ansible para iniciantes](/articles/ansible-for-beginners/) e seu fluxo de conexão baseado em SSH.

______

## Próximas etapas

- Substitua nomes de host, nomes de usuário e caminhos de exemplo por valores revisados para o seu ambiente.
- Registre as impressões digitais das chaves de host e a propriedade das chaves nos registros de administração.
- Teste um segundo login administrativo antes de alterar as configurações de senha ou firewall.
- Inclua a revisão da configuração SSH no processo de fortalecimento da segurança e automação de sistemas.

## Referências

- [SSH na Wikipédia](https://en.wikipedia.org/wiki/Secure_Shell)
- [Documentação do SCP](https://man.openbsd.org/scp)
- [Documentação do arquivo de configuração SSH](https://man.openbsd.org/sshd_config)
- [Manual `ssh-keygen(1)` do OpenSSH](https://man.openbsd.org/ssh-keygen)
- [Manual `ssh(1)` do OpenSSH](https://man.openbsd.org/ssh)
- [Manual `ssh_config(5)` do OpenSSH](https://man.openbsd.org/ssh_config)
- [Manual `sshd(8)` do OpenSSH](https://man.openbsd.org/sshd)
- [Notas de versão do OpenSSH](https://www.openssh.org/releasenotes.html)

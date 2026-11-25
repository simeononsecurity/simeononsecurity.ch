---
title: "O que fazer e o que evitar para reforçar seu sistema Linux"
date: 2023-02-28
lastmod: 2026-11-25
toc: true
draft: false
description: "Orientações para reforçar a segurança do Linux com atualizações, firewalls, SELinux ou AppArmor, políticas de senha e monitoramento de logs."
tags: ["segurança do Linux", "reforço do sistema", "firewall", "SELinux", "AppArmor", "política de senhas", "atualizações do sistema", "logs do sistema", "módulos de segurança", "políticas de controle de acesso", "cibersegurança", "segurança do sistema", "segurança de rede", "gerenciamento de vulnerabilidades", "boas práticas de segurança", "segurança de TI", "segurança da informação", "atualizações de software", "acesso root", "gerenciador de senhas"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.webp"
coverAlt: "Um cadeado de desenho animado segura um escudo com a palavra Linux, enquanto uma flecha bate e ricocheteia no escudo."
coverCaption: ""
---


Linux é um sistema operacional popular entre pessoas e empresas. Embora muitas vezes seja considerado mais seguro que outros sistemas operacionais por ser de código aberto, ainda exige medidas adequadas de reforço para proteger o sistema e os dados armazenados nele. Este artigo apresenta recomendações e práticas a evitar para ajudar a manter seu sistema Linux seguro.

## O que fazer:

### Mantenha o sistema atualizado

Manter seu [sistema Linux](https://simeononsecurity.com/articles/how-do-i-learn-linux/) atualizado é essencial para preservar sua segurança. Atualizações regulares corrigem vulnerabilidades e erros, ajudando a proteger o sistema contra possíveis ataques. Veja exemplos de como atualizar o Linux usando os gerenciadores de pacotes **apt-get** ou **yum**:

#### Atualizando o Ubuntu com apt-get

Para atualizar o Ubuntu com **apt-get**, abra um terminal e digite:
```bash
sudo apt-get update
```

Isso baixará as listas de pacotes mais recentes dos repositórios do Ubuntu. Quando o comando terminar, você poderá instalar as atualizações disponíveis com o comando a seguir:

```bash
sudo apt-get upgrade

```

Isso baixará e instalará as atualizações disponíveis para o sistema.

### Atualizando o CentOS com yum

Para atualizar o CentOS com **yum**, abra um terminal e digite:

```bash
sudo yum update
```

Isso baixará e instalará as atualizações disponíveis. Você também pode executar o comando abaixo para remover pacotes antigos ou não utilizados:

```bash
sudo yum autoremove
```

Isso removerá os pacotes que não são mais necessários no sistema.

Verifique e instale atualizações regularmente para manter a segurança e a estabilidade do Linux.


### Use um firewall

Um firewall é uma medida de segurança essencial para qualquer sistema Linux, pois ajuda a impedir acessos não autorizados e outras ameaças cibernéticas. Veja como usar o firewall **ufw** no Linux:

#### Instalando e habilitando o ufw em sistemas baseados no Ubuntu

Para instalar e habilitar o **ufw**, abra um terminal e digite:

```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```

Para permitir tráfego HTTP de entrada (porta 80):

```bash
sudo ufw allow http
```

Para bloquear tráfego de entrada de um endereço IP específico:

```bash
sudo ufw deny from <ip_address>
```

Para excluir uma regra:
```bash
sudo ufw delete <rule_number>
```

Para ver as regras atuais do **ufw**, digite:

```bash
sudo ufw status
```


Isso exibirá as regras atuais e seus status.

Revise e atualize regularmente as regras do **ufw** para proteger o sistema contra possíveis ameaças.


#### Instalando e habilitando o firewalld em sistemas baseados no CentOS

Para instalar e habilitar o firewall padrão do CentOS, o **firewalld**, use os comandos a seguir:

```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

Isso instalará e habilitará o **firewalld** no sistema.

#### Configurando regras do firewalld em sistemas baseados no CentOS

Depois de habilitar o **firewalld**, você pode configurar regras para permitir ou bloquear tráfego de entrada e saída. Veja alguns exemplos:

Para permitir tráfego SSH de entrada (porta 22):

```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

Para permitir tráfego HTTP de entrada (porta 80):

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

Para bloquear tráfego de entrada de um endereço IP específico:

```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```

Para excluir uma regra:

```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```

Para ver as regras atuais do **firewalld**, digite:

```bash
sudo firewall-cmd --list-all
```

Isso exibirá as regras atuais e seus status.

Revise e atualize regularmente as regras do **firewalld** para garantir que o sistema

### Habilite o SELinux ou o AppArmor

SELinux (Security-Enhanced Linux) e AppArmor são módulos de segurança que aplicam políticas obrigatórias de controle de acesso em sistemas Linux. A maioria das distribuições modernas já inclui um deles, e ambos podem ser habilitados e configurados para reforçar a segurança do sistema.

#### Habilitando o SELinux em sistemas baseados no CentOS

Para verificar se o SELinux está habilitado, execute o comando a seguir:

```bash
sestatus
```

Se o SELinux não estiver instalado, você poderá instalá-lo com este comando:

```bash
sudo yum install selinux-policy selinux-policy-targeted
```

Para habilitar o SELinux, edite o arquivo **/etc/selinux/config** e defina a variável **SELINUX** como **enforcing**:

```bash
sudo nano /etc/selinux/config
```
**Altere SELINUX=enforcing**
```
SELINUX=enforcing
```

Salve o arquivo e saia pressionando CTRL+X, depois Y e Enter. Em seguida, reinicie o sistema.

#### Habilitando o AppArmor em sistemas baseados no Ubuntu

Para verificar se o AppArmor está habilitado, execute o comando a seguir:
```bash
sudo apparmor_status
```


Se o AppArmor não estiver instalado, você poderá instalá-lo com este comando:
```bash
sudo apt-get install apparmor
```

Para habilitar o AppArmor, edite o arquivo **/etc/default/grub** e adicione o parâmetro **security=apparmor** à variável **GRUB_CMDLINE_LINUX**:

```bash
sudo nano /etc/default/grub
```
**Adicione security=apparmor**
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```

Salve o arquivo e saia pressionando CTRL+X, depois Y e Enter. Em seguida, execute o comando abaixo para atualizar a configuração do carregador de inicialização:

```bash
sudo update-grub
```

Por fim, reinicie o sistema.

Depois de habilitar SELinux ou AppArmor, configure as políticas para limitar privilégios dos processos e restringir seu acesso aos recursos do sistema. Isso reduz o possível impacto de um ataque bem-sucedido e melhora a segurança geral.


### Configure políticas de senha

Configurar políticas de senha é uma etapa importante para reforçar a segurança do Linux. Ao exigir senhas fortes, você ajuda a proteger as contas de usuário contra possíveis ataques. Veja como configurar essas políticas no Linux:

#### Configurando políticas de senha no Ubuntu

No Ubuntu, você pode usar o módulo **pam_pwquality** para aplicar políticas de senha. Ele oferece verificações de força de senha. Para instalar o **pam_pwquality**, abra um terminal e digite:

```bash
sudo apt-get install libpam-pwquality
```

Depois de instalar o módulo, edite o arquivo **/etc/pam.d/common-password** para configurar suas opções. Por exemplo, para exigir pelo menos 8 caracteres, uma letra maiúscula, uma minúscula, um dígito e um caractere especial, adicione esta linha ao arquivo:

```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

Você também pode configurar outros parâmetros, como o prazo máximo de validade da senha, adicionando linhas ao arquivo.

#### Configurando políticas de senha no CentOS

No CentOS, você pode usar a ferramenta **authconfig** para configurar políticas de senha. Ela oferece várias opções. Para exigir pelo menos 8 caracteres, uma letra maiúscula, uma minúscula, um dígito e um caractere especial, use este comando:

```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```

Isso atualizará os arquivos **/etc/pam.d/system-auth** e **/etc/pam.d/password-auth** para aplicar as políticas especificadas.

Revise e atualize as políticas de senha regularmente para que continuem eficazes contra possíveis ataques.


### Monitore os logs do sistema

Monitorar os logs é importante para manter a segurança do Linux. Eles registram atividades do sistema, como tentativas de login malsucedidas, erros e outros eventos relevantes, e ajudam a identificar ameaças ou problemas que exigem atenção. Veja como monitorá-los:

#### Usando o comando journalctl

Na maioria das distribuições modernas, você pode usar **journalctl** para consultar os logs do sistema. O comando oferece várias opções para filtrar e pesquisar entradas.

Para ver todas as entradas, execute o comando a seguir:

```bash
sudo journalctl
```

Isso exibirá todas as entradas, com as mais recentes no final.

Para filtrar por uma unidade específica, como um serviço ou processo, use a opção **-u** seguida do nome da unidade. Por exemplo, para ver os logs do serviço **sshd**, execute:
```bash
sudo journalctl -u sshd
```


Para filtrar por período, use as opções **--since** e **--until** seguidas de um horário ou intervalo. Por exemplo, para ver a última hora, execute:

```bash
sudo journalctl --since "1 hour ago"
```

#### Usando uma ferramenta de gerenciamento de logs

Em sistemas maiores ou mais complexos, uma ferramenta de gerenciamento de logs pode ajudar a coletar e analisar os registros. Essas ferramentas oferecem recursos como monitoramento em tempo real, agregação e análise, e ajudam a identificar e responder a ameaças com mais eficiência.

Exemplos de ferramentas de gerenciamento de logs para Linux:

- **Logwatch**: ferramenta simples que envia resumos diários dos logs do sistema por e-mail
- **Logrotate**: ferramenta que rotaciona e compacta arquivos de log automaticamente para economizar espaço em disco
- **ELK stack**: ferramenta popular de código aberto que combina Elasticsearch, Logstash e Kibana para monitorar e analisar logs em tempo real

Revise e analise os logs regularmente para detectar possíveis ameaças e responder a elas a tempo.

______

## O que evitar:

### Não use senhas fracas

Usar senhas fracas é um erro comum que deixa o Linux vulnerável a ataques. Atacantes podem tentar adivinhar senhas com base em palavras, nomes ou datas comuns. Use senhas fortes, únicas e difíceis de adivinhar.

Você pode criar senhas fortes combinando letras maiúsculas e minúsculas, números e caracteres especiais. Também é recomendável usar um [gerenciador de senhas](https://simeononsecurity.com/articles/bitwarden-and-keepassxc-vs-the-rest/) para gerar e armazenar senhas complexas com segurança. [Gerenciadores de senhas](https://simeononsecurity.com/articles/bitwarden-and-keepassxc-vs-the-rest/) também ajudam a memorizar as senhas e evitar reutilizá-las em várias contas.

### Não permita acesso SSH à conta root

Permitir acesso SSH à conta root é um risco de segurança que pode dar aos atacantes controle total do Linux. Em vez disso, entre com uma conta que não seja root e eleve os privilégios com o comando **sudo**. Isso reduz o possível impacto de um ataque ao limitar os privilégios das contas de usuário.

### Não instale software desnecessário

Instalar software desnecessário aumenta a superfície de ataque do Linux e o deixa mais vulnerável. Instale apenas o que for necessário e remova o restante. Isso reduz o número de vulnerabilidades potenciais e o risco de um ataque bem-sucedido.

### Não use software desatualizado

Software desatualizado pode deixar o sistema vulnerável a ataques que exploram falhas conhecidas. Use as versões mais recentes e atualize-as regularmente para corrigir vulnerabilidades e proteger o sistema.

______

## Conclusão

Reforçar a segurança do Linux é essencial para proteger o sistema e os dados armazenados nele. Siga as recomendações e evite as práticas descritas neste artigo para reduzir o risco de ameaças cibernéticas. Mantenha o sistema atualizado, use um firewall, configure políticas de senha e monitore os logs. Evite senhas fracas, desativar atualizações automáticas, permitir acesso SSH à conta root, instalar software desnecessário e usar software desatualizado. Essas boas práticas ajudam a manter o Linux seguro.

## Referências:

- [The Center for Internet Security's Linux Hardening Guide](https://www.cisecurity.org/cis-hardened-images/)
- [Red Hat Enterprise Linux Security Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
- [Ubuntu Security Documentation](https://ubuntu.com/security)
- [Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)

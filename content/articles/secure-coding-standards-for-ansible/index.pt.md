---
title: "Orientações de programação segura para Ansible: boas práticas"
date: 2023-03-02
lastmod: 2026-11-19
toc: true
draft: false
description: "Conheça as boas práticas para escrever código seguro com Ansible, uma ferramenta popular de gestão de configuração e implementação."
tags: ["Programação segura","Ansible","Gestão de configuração","Implementação","Princípio do menor privilégio","Ansible Vault","Palavras-passe fortes","Controlo de acesso","Sistema de controlo de versões","Protocolos de comunicação seguros","SSH","WinRM","Certificados TLS","Sanitização da entrada do utilizador","Validação da entrada","Tratamento de erros","Práticas de programação segura","Injeção de código","Orientações de programação segura","Segurança da infraestrutura","Orientações de programação segura para Ansible","Boas práticas de código seguro com Ansible","Gestão segura de configuração com Ansible","Práticas de implementação segura com Ansible","Princípio do menor privilégio no Ansible","Utilizar Ansible Vault para proteger código","Criar palavras-passe fortes no Ansible","Controlo de acesso no Ansible","Sistema de controlo de versões para playbooks Ansible","Protocolos de comunicação seguros no Ansible","Segurança SSH no Ansible","Segurança WinRM no Ansible","Certificados TLS no Ansible","Sanitização da entrada do utilizador no Ansible","Validação da entrada no Ansible","Tratamento de erros no Ansible","Práticas de programação segura no Ansible","Prevenção de injeção de código no Ansible","Orientações de programação segura para infraestruturas geridas com Ansible","Proteger a infraestrutura Ansible"]
cover: "/img/cover/A_cartoon_image_of_a_castle_protected_by_a_shield.webp"
coverAlt: "Ilustração de um castelo protegido por um escudo, que representa as medidas de segurança da infraestrutura gerida com Ansible."
coverCaption: ""
---

À medida que as organizações adotam cada vez mais a automatização, o **Ansible** tornou-se uma ferramenta preferida para a **gestão de configuração** e a **implementação**. No entanto, como qualquer software, o Ansible não está imune a vulnerabilidades de segurança. Por isso, é essencial dar prioridade ao desenvolvimento de **código seguro** para proteger e manter a integridade da infraestrutura gerida com Ansible. Este artigo apresenta as **boas práticas** essenciais para escrever **código seguro** com Ansible e reforçar os fluxos de automatização contra potenciais ameaças.

## Compreender a segurança do Ansible

Antes de analisar as orientações, é importante compreender as funcionalidades de segurança do Ansible. O Ansible **encripta** as comunicações entre os nós de controlo e os nós geridos. Também disponibiliza **armazenamento seguro** de **segredos** e de outras informações sensíveis através do **Vault**. Além disso, inclui um mecanismo de **isolamento** para proteger contra a execução de código potencialmente malicioso.

Estas funcionalidades não dispensam os programadores de escrever código seguro. Seguir as orientações abaixo ajuda a complementar as funcionalidades de segurança integradas no Ansible com código seguro.

## Importância do código seguro no Ansible

Escrever **código seguro** é essencial ao utilizar Ansible para gerir infraestrutura. Ao seguir as **boas práticas de segurança**, as organizações podem reduzir riscos como o acesso não autorizado, as violações de dados e as interrupções do serviço. O **código seguro** no Ansible protege a confidencialidade, a integridade e a disponibilidade dos ativos críticos, reforçando também a robustez e a fiabilidade do ambiente automatizado.

## Orientação 1: Utilize a versão mais recente do Ansible

O Ansible é atualizado continuamente para corrigir vulnerabilidades de segurança e erros. Utilizar a versão mais recente dá aos programadores acesso às correções e melhorias de segurança mais atuais.

Os programadores devem procurar atualizações regularmente e instalá-las assim que possível. Também podem subscrever a lista de correio Ansible Security Announcements para receber notificações sobre atualizações de segurança. Atualizar para a versão mais recente é uma medida simples que pode melhorar significativamente a segurança da infraestrutura gerida com Ansible.

## Orientação 2: Siga o princípio do menor privilégio

O **princípio do menor privilégio** é um princípio de segurança fundamental que também se aplica ao Ansible. Significa que cada utilizador deve ter apenas o nível mínimo de acesso necessário para desempenhar a sua função. Os nós geridos também devem receber apenas o acesso mínimo necessário para executar as tarefas pretendidas.

Por exemplo, se um playbook só precisar de ler um ficheiro específico, conceda-lhe apenas permissão de leitura, não de escrita nem de execução. Limite também o número de utilizadores com acesso ao Ansible. O acesso deve ficar restrito aos utilizadores autorizados que precisam de gerir a infraestrutura com Ansible.

O Ansible disponibiliza vários mecanismos para aplicar o princípio do menor privilégio, como a diretiva `become`. Esta diretiva permite executar tarefas com os privilégios de outro utilizador, como `sudo`. Utilize `become` apenas quando necessário e conceda somente os privilégios indispensáveis.

Aplicar o princípio do menor privilégio limita os danos potenciais que um atacante pode causar na sequência de uma violação de segurança. Esta orientação pode melhorar significativamente a segurança da infraestrutura gerida com Ansible.

## Orientação 3: Utilize Ansible Vault para informações sensíveis

Não guarde informações sensíveis, como palavras-passe, chaves de API e certificados, em texto simples nos playbooks Ansible. Isso pode comprometer a segurança da infraestrutura gerida com Ansible. O Ansible disponibiliza o **Vault** para armazenar informações sensíveis em segurança.

O Vault encripta as informações sensíveis com uma palavra-passe ou um ficheiro de chave. Pode utilizar o comando `ansible-vault` para criar um ficheiro encriptado, editar um ficheiro encriptado existente ou visualizá-lo. O comando também permite encriptar ou desencriptar variáveis individuais. Para criar um novo ficheiro encriptado, execute:

```bash
ansible-vault create secret.yml
```

Este comando cria um novo ficheiro encriptado com o nome `secret.yml`. Pode editar o ficheiro com o comando `ansible-vault edit`, que lhe pedirá a palavra-passe do Vault.

Guarde também as palavras-passe e os ficheiros de chave em segurança. Não os mantenha em texto simples. Utilize uma localização protegida, como um gestor de palavras-passe ou um servidor de ficheiros seguro.

Armazenar informações sensíveis no Vault é uma medida essencial para proteger a infraestrutura gerida com Ansible. Assim, essas informações não ficam expostas em texto simples e só estão acessíveis aos utilizadores autorizados.

## Orientação 4: Utilize palavras-passe fortes

As palavras-passe utilizadas para autenticação devem ser **fortes** e **únicas**. Palavras-passe fracas ou comuns podem comprometer a segurança da infraestrutura gerida com Ansible. Evite palavras-passe predefinidas e não as introduza diretamente nos playbooks. Guarde-as em segurança com o Vault.

Uma palavra-passe forte deve ter pelo menos 12 caracteres e combinar letras maiúsculas e minúsculas, números e símbolos especiais. Evite informações fáceis de adivinhar, como nomes ou datas de nascimento. Pode utilizar um gestor de palavras-passe para gerar palavras-passe fortes e únicas.

Guarde as palavras-passe dos playbooks em formato encriptado com o Vault. Evite também inseri-las diretamente nos playbooks. Em vez disso, utilize variáveis. Por exemplo, defina a variável `db_password` num ficheiro encriptado separado e faça referência a ela no playbook com esta sintaxe:

```yml
db_password: "{{ vault_db_password }}"
```

Esta sintaxe faz referência à variável `db_password` do ficheiro encriptado e desencripta-a com o Vault.

Utilizar palavras-passe fortes e guardá-las em segurança ajuda a impedir o acesso não autorizado à infraestrutura gerida com Ansible. É uma medida simples que melhora a segurança.

## Orientação 5: Limite o acesso aos playbooks

Limite o acesso aos playbooks Ansible aos utilizadores autorizados. Utilize um **sistema de controlo de versões**, como o **Git**, para gerir os playbooks. O Git disponibiliza funcionalidades de **controlo de acesso** e **auditoria** que ajudam a aplicar políticas de segurança.

## Orientação 6: Utilize protocolos de comunicação seguros

O Ansible suporta vários protocolos de comunicação, incluindo SSH e WinRM. SSH é o protocolo recomendado para anfitriões Linux e macOS; WinRM é recomendado para anfitriões Windows. Certifique-se de que a comunicação entre os nós de controlo e os nós geridos está **encriptada**.

SSH é um protocolo de comunicação seguro que encripta a comunicação entre os nós de controlo e os nós geridos. Utilize chaves SSH fortes para autenticação, com pelo menos 2048 bits. Desative também a autenticação por palavra-passe no SSH.

WinRM também encripta a comunicação entre os nós de controlo e os nós geridos. Utilize WinRM através de HTTPS para garantir a encriptação da comunicação. Utilize igualmente certificados fortes para autenticação.

Certifique-se de que os certificados TLS utilizados nas comunicações HTTPS são válidos e não expiraram. Pode utilizar ferramentas como `openssl` para gerar e gerir certificados TLS.

Utilizar protocolos de comunicação seguros é uma medida essencial para proteger a infraestrutura gerida com Ansible. Assim, a comunicação entre os nós de controlo e os nós geridos permanece encriptada e segura.

## Orientação 7: Verifique as identidades dos anfitriões

Verifique a identidade dos nós geridos antes de lhes permitir ligar-se aos nós de controlo. O Ansible disponibiliza vários mecanismos de verificação, incluindo **impressões digitais de chaves SSH** e **certificados TLS**. Mantenha as configurações de SSH e TLS atualizadas e seguras.

As impressões digitais de chaves SSH são identificadores únicos das chaves SSH utilizadas pelos nós geridos para autenticação. Verifique-as antes de permitir a ligação aos nós de controlo. Pode gerar impressões digitais com o comando `ssh-keygen` e compará-las com as fornecidas pelos nós geridos.

Os nós geridos utilizam certificados TLS para se autenticarem perante os nós de controlo. Verifique se os certificados são válidos e não expiraram. Certifique-se também de que os nós de controlo confiam nos certificados utilizados pelos nós geridos.

Mantenha as configurações de SSH e TLS atualizadas e seguras. Devem utilizar algoritmos fortes de encriptação e autenticação e rejeitar cifras e protocolos fracos.

Verificar a identidade dos nós geridos é essencial para proteger a infraestrutura gerida com Ansible. Ajuda a prevenir ataques de intermediário e garante que apenas os nós geridos autorizados se podem ligar aos nós de controlo.

## Orientação 8: Higienize a entrada do utilizador

Higienize a entrada do utilizador para impedir a **injeção de código** e outras vulnerabilidades de segurança. Sempre que possível, utilize **entradas validadas** para reduzir o risco.

## Orientação 9: Siga práticas de programação segura

Siga **práticas de programação segura**, como a **validação da entrada**, o **tratamento de erros** e a **higienização** da entrada. Siga também as **orientações de programação segura** da linguagem utilizada com Ansible.

Higienize a entrada do utilizador para impedir a **injeção de código** e outras vulnerabilidades. Num ataque de injeção de código, o atacante introduz código malicioso numa aplicação ao explorar vulnerabilidades na entrada do utilizador. Utilize entradas validadas sempre que possível para reduzir o risco.

Pode utilizar o filtro `regex_replace` do Ansible para higienizar a entrada do utilizador. Este filtro substitui padrões numa cadeia por outros padrões. Por exemplo, o código seguinte remove todos os caracteres não alfanuméricos:

```yaml
- name: Higienizar a entrada do utilizador
  vars:
    user_input: "Olá! Esta cadeia contém caracteres não alfanuméricos."
    sanitized_input: "{{ user_input | regex_replace('[^A-Za-z0-9]', '') }}"
  debug:
    var: sanitized_input
```

Neste exemplo, o filtro `regex_replace` substitui por uma cadeia vazia todos os caracteres não alfanuméricos de `user_input`. A entrada higienizada é guardada em `sanitized_input`.

A validação da entrada também reduz o risco de vulnerabilidades. Consiste em verificar se a entrada do utilizador cumpre critérios definidos, como conter apenas caracteres alfanuméricos. Pode ser implementada com condicionais e expressões regulares do Ansible.

Higienizar e validar a entrada do utilizador ajuda a prevenir a injeção de código e outras vulnerabilidades nos playbooks Ansible. É uma medida simples para melhorar a segurança.

## Conclusão

À medida que as organizações adotam a automatização, o **Ansible** destaca-se como uma opção popular para a **gestão de configuração** e a **implementação**. Ainda assim, é necessário dar prioridade ao **código seguro** para proteger a integridade e a fiabilidade da infraestrutura gerida com Ansible.

Seguir as **orientações** deste artigo ajuda os programadores a aplicar **boas práticas de segurança** nos fluxos de trabalho do Ansible. Isso inclui utilizar **controlo de acesso baseado em funções (RBAC)**, proteger os canais de comunicação com **Transport Layer Security (TLS)** ou **Secure Shell (SSH)**, gerir segredos e dados sensíveis com **Ansible Vault** e atualizar o Ansible regularmente para se proteger contra vulnerabilidades conhecidas.

Utilize sempre a versão mais recente do Ansible, siga o princípio do menor privilégio, utilize Ansible Vault para informações sensíveis, escolha palavras-passe fortes, limite o acesso aos playbooks, utilize protocolos de comunicação seguros, verifique as identidades dos anfitriões, higienize a entrada do utilizador e siga práticas de programação segura. Estas orientações ajudam os programadores a escrever código seguro e a proteger a infraestrutura contra vulnerabilidades.

Ao integrar estas **boas práticas**, as organizações podem tirar partido da automatização do Ansible e manter uma infraestrutura segura e fiável. Proteger ativos críticos com código seguro e com as funcionalidades integradas do Ansible permite adotar a automatização sem comprometer a segurança.

## Referências

- [Documentação do Ansible](https://docs.ansible.com/)
- [Documentação do Ansible Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html)
- [Documentação do Git](https://git-scm.com/doc)
- [Documentação do OpenSSH](https://www.openssh.com/)
- [Documentação do Transport Layer Security (TLS)](https://tools.ietf.org/html/rfc8446)
- [Documentação da OWASP sobre injeção de código](https://owasp.org/www-community/attacks/Code_Injection)

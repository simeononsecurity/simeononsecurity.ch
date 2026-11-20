---
title: "Padrões de codificação segura para Python: práticas recomendadas"
date: 2023-02-26
lastmod: 2026-11-19
toc: true
draft: false
description: "Conheça as práticas recomendadas de codificação segura em Python para reduzir o risco de violações de segurança e proteger dados confidenciais."
tags: ["Python", "Codificação segura", "Riscos de segurança", "Validação de entrada", "Bibliotecas criptográficas", "Privilégio mínimo", "Analisador estático de código", "Aplicações Web", "Frameworks Python", "Django", "Flask", "Sistema de autenticação", "Hash de senhas", "Sistema de templates", "Gerenciamento de sessões", "MarkupSafe", "WTForms", "Blinker", "Proteção de dados", "Vulnerabilidades", "Codificação segura", "Python", "Riscos de segurança", "Validação de entrada", "Bibliotecas criptográficas", "Privilégio mínimo", "Analisador estático de código", "Aplicações Web", "Frameworks Python", "Django", "Flask", "Sistema de autenticação", "Hash de senhas", "Sistema de templates", "Gerenciamento de sessões", "MarkupSafe", "WTForms", "Blinker", "Proteção de dados", "Vulnerabilidades", "Segurança de código Python", "Revisão de código", "Ferramentas de análise estática", "Desenvolvimento Web seguro", "Práticas de codificação segura", "Vulnerabilidades de segurança", "Práticas recomendadas de segurança de código", "Criptografia de dados", "Princípio do privilégio mínimo", "Análise de código", "Segurança na Web"]
cover: "/img/cover/A_cartoon_shield_with_the_word_Python.webp"
coverAlt: "Escudo de desenho animado com a palavra Python para representar os padrões de codificação segura"
coverCaption: ""
---
**Práticas recomendadas de padrões de codificação segura em Python**

### 1. Valide as entradas

As entradas do usuário costumam ser uma fonte importante de riscos de segurança. **A validação de entrada** verifica se os dados fornecidos pelo usuário atendem aos critérios esperados e são seguros para uso na aplicação.

Por exemplo, um número de cartão de crédito deve conter apenas dígitos, sem caracteres especiais. Para validar a entrada, os desenvolvedores podem usar funções integradas como `isdigit()` ou expressões regulares.

```python
import re

def validate_input(input_string):
    """
    Função para validar a entrada usando expressões regulares.
    """
    pattern = r"^[0-9]+$"
    if re.match(pattern, input_string):
        return True
    else:
        return False
```

### 2. Evite funções inseguras

O Python tem funções que podem causar problemas de segurança quando usadas sem cuidado. `exec()`, `eval()` e `pickle` podem permitir que invasores executem código malicioso. Os desenvolvedores devem **evitar essas funções** ou usá-las com cautela, restringindo os parâmetros de entrada e somente quando necessário.

Por exemplo, para converter uma string em um número inteiro, use `int()` em vez de `eval()`.

```py
# Em vez de usar eval
x = eval('10')

# Use int
x = int('10')
```

### 3. Use bibliotecas criptográficas

Bibliotecas **criptográficas** como [cryptography](https://pypi.org/project/cryptography/) e [PyCryptodome](https://pypi.org/project/pycryptodome/) oferecem uma maneira segura de criptografar e descriptografar. Use essas bibliotecas em vez de criar métodos próprios de criptografia, que podem apresentar vulnerabilidades.

Por exemplo, para criptografar uma senha, use a biblioteca [cryptography](https://pypi.org/project/cryptography/) assim:

```py
from cryptography.fernet import Fernet

def encrypt_password(password):
    """
    Função para criptografar uma senha usando a biblioteca cryptography.
    """
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode('utf-8'))
    return encrypted_password

password = "senhaExemplo"
encrypted_password = encrypt_password(password)
```
O objeto `Fernet` gera uma chave, usada para criptografar a senha com o método `encrypt()`.

### 4. Siga o princípio do privilégio mínimo

**O princípio do privilégio mínimo** restringe usuários ou processos ao menor nível de acesso necessário para suas funções. Os desenvolvedores devem seguir esse princípio para reduzir o impacto de violações de segurança.

Por exemplo, se uma aplicação precisa apenas ler um banco de dados, use uma conta com permissão somente de leitura, em vez de uma conta com permissões completas. Isso reduz o risco de um invasor usar a aplicação para modificar ou excluir dados.

### 5. Mantenha bibliotecas e frameworks atualizados

Bibliotecas e frameworks podem conter vulnerabilidades que invasores exploram. Os desenvolvedores devem **manter bibliotecas e frameworks atualizados** para a versão mais recente e evitar problemas de segurança conhecidos.

Por exemplo, se uma biblioteca de terceiros como [requests](https://pypi.org/project/requests/) tiver uma vulnerabilidade, atualize-a para a versão mais recente que corrige o problema.

### 6. Use um analisador estático de código

**Um analisador estático de código** identifica possíveis vulnerabilidades antes da execução. Use ferramentas como [Bandit](https://pypi.org/project/bandit/), [Pylint](https://pypi.org/project/pylint/) e [Pyflakes](https://pypi.org/project/pyflakes/) para detectar e corrigir problemas antes da implantação.

Por exemplo, [Bandit](https://pypi.org/project/bandit/) examina código Python em busca de vulnerabilidades, como senhas embutidas no código, injeção de SQL e uso de funções inseguras.

### 7. Adote práticas de codificação segura em aplicações Web

Aplicações Web enfrentam riscos como cross-site scripting, injeção de SQL e injeção de comandos. Os desenvolvedores devem **adotar práticas de codificação segura**, como validação de entrada, codificação de saída e consultas parametrizadas.

Por exemplo, ao escrever consultas SQL, use **consultas parametrizadas** em vez de concatenar a entrada do usuário. Elas tratam a entrada como dado, e não como código executável, o que impede ataques de injeção de SQL.

```py
# Em vez disso
query = "SELECT * FROM users WHERE username = '" + username + "';"

# Use uma consulta parametrizada
query = "SELECT * FROM users WHERE username = %s;"
cursor.execute(query, (username,))
```
Os desenvolvedores também devem **validar todas as entradas do usuário**, codificar as saídas e usar HTTPS para criptografar os dados transmitidos pela rede.

## Padrões de codificação segura para frameworks Python

Frameworks Python como [Django](https://www.djangoproject.com/) e [Flask](https://flask.palletsprojects.com/) têm seus próprios padrões de codificação segura. Siga-os ao desenvolver aplicações com esses frameworks. Alguns padrões:

### 1. [Django](https://www.djangoproject.com/)

[Django](https://www.djangoproject.com/) é um framework Web popular para Python. Siga estes padrões de codificação segura para [Django](https://www.djangoproject.com/):

- Use o **sistema de autenticação** integrado do [Django](https://www.djangoproject.com/) em vez de criar um sistema próprio.
- Use as **funções integradas de hash de senhas** do [Django](https://www.djangoproject.com/) em vez de criar métodos próprios.
- Use o **sistema de templates** do [Django](https://www.djangoproject.com/) para manter a saída segura e livre de vulnerabilidades de cross-site scripting.

Por exemplo, para usar a função integrada de hash de senha, use `make_password()` do módulo `django.contrib.auth.hashers` [Django](https://www.djangoproject.com/).

```python
from [Django](https://www.djangoproject.com/).contrib.auth.hashers import make_password

password = "senhaExemplo"
hashed_password = make_password(password)
```

### 2. [Flask](https://flask.palletsprojects.com/)
[Flask](https://flask.palletsprojects.com/) é um microframework Web para Python. Siga estes padrões [Flask](https://flask.palletsprojects.com/):

- Use o **sistema integrado de gerenciamento de sessões** do [Flask](https://flask.palletsprojects.com/) para tratar sessões com segurança.
- Use [Flask](https://flask.palletsprojects.com/) com [MarkupSafe](https://pypi.org/project/MarkupSafe/) para manter a saída segura e livre de vulnerabilidades de cross-site scripting.
- Use [Flask](https://flask.palletsprojects.com/) com [WTForms](https://pypi.org/project/WTForms/) para validar entradas e reduzir riscos de segurança.
- Use [Flask](https://flask.palletsprojects.com/) com [Blinker](https://pypi.org/project/blinker/) para tratar sinais com segurança.

Por exemplo, use [Flask](https://flask.palletsprojects.com/) com [MarkupSafe](https://pypi.org/project/MarkupSafe/) e use a biblioteca para escapar tags HTML da saída.

```py
from markupsafe import escape

@app.route('/')
def hello():
    name = "<script>alert('xss');</script>"
    return 'Olá, ' + escape(name)
```
______

## Como aplicar o que você aprendeu e o que fazer agora?

1. **Comece hoje a adotar essas práticas no seu código Python** para reduzir o risco de violações e proteger dados confidenciais. Identifique áreas vulneráveis, como validação de entrada, hash de senhas e gerenciamento de sessões. Depois, use expressões regulares integradas ao Python ou uma biblioteca segura de hash de senhas, como [bcrypt](https://pypi.org/project/bcrypt/).

2. **Revise sua base de código em busca de vulnerabilidades** e use analisadores estáticos como [Bandit](https://pypi.org/project/bandit/), [Pylint](https://pypi.org/project/pylint/) e [Pyflakes](https://pypi.org/project/pyflakes/) para encontrá-las e corrigi-las. Faça também revisões manuais para identificar problemas que essas ferramentas não detectam. Procure injeção de SQL, cross-site scripting e falhas de validação de entrada.

3. **Mantenha-se atualizado sobre práticas e ferramentas de segurança.** Acompanhe blogs, participe de conferências e comunidades online. Mantenha bibliotecas e frameworks atualizados para usar versões seguras recentes.

4. **Participe de comunidades online e eventos** para aprender sobre codificação segura em Python com especialistas e outros desenvolvedores. Procure fóruns de segurança, compartilhe conhecimento e participe de conferências, webinars e encontros.

5. **Compartilhe essas práticas com sua equipe ou colegas** para promover a conscientização sobre segurança e incentivar a codificação segura em projetos Python. Organize treinamentos, compartilhe recursos e dê o exemplo ao aplicar essas práticas no seu código.

## Conclusão

Os padrões de codificação segura são essenciais para manter o código seguro, confiável e livre de vulnerabilidades. Python é uma linguagem popular e seus desenvolvedores devem seguir esses padrões para prevenir riscos de segurança. Validar entradas, evitar funções inseguras, usar bibliotecas criptográficas e manter bibliotecas e frameworks atualizados ajuda a proteger o código. Ao usar frameworks Python, siga os padrões recomendados por cada framework.

Adotar padrões de codificação segura é um processo contínuo que exige atualização sobre práticas e ferramentas de segurança. Integrar esses padrões ao desenvolvimento reduz o risco de violações e protege dados confidenciais.

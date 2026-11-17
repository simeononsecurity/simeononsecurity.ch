---
title: "Como funciona o DNS: DNS raiz, importância e solução de problemas"
draft: false
toc: true
date: 2023-07-20
lastmod: 2026-11-13
description: "Entenda o funcionamento do DNS e do DNS raiz, a hierarquia, o processo de resolução, o cache e a solução de problemas."
genre: ["Fundamentos de DNS", "DNS raiz", "Sistema de Nomes de Domínio", "Resolução DNS", "Hierarquia DNS", "Cache DNS", "Solução de problemas de DNS", "Registros DNS", "Gerenciamento de DNS", "Comandos DNS"]
tags: ["DNS", "DNS raiz", "Sistema de Nomes de Domínio", "Resolução DNS", "Hierarquia DNS", "Cache DNS", "Registros DNS", "Gerenciamento de DNS", "Solução de problemas de DNS", "redes", "infraestrutura da Internet", "endereços IP", "acesso a sites", "consulta recursiva", "servidores de nomes autoritativos", "TTL", "mecanismos de cache", "limpar o cache DNS", "servidores DNS raiz", "roteamento anycast", "ICANN", "colaboração DNS", "registro A", "registro AAAA", "registro CNAME", "registro MX", "registro TXT", "registro SRV", "registro NS", "registro PTR", "registro SOA", "comandos de diagnóstico DNS", "Windows", "macOS", "Linux", "Prompt de Comando", "terminal do sistema"]
cover: "/img/cover/An_image_depicting_interconnected_computer_ne.webp"
coverAlt: "Imagem de redes de computadores interconectadas com nomes de domínio e endereços IP, representando o funcionamento do DNS e do DNS raiz."
coverCaption: "Entenda o DNS e domine o Sistema de Nomes de Domínio"
---

## Como funcionam o DNS e o DNS raiz

### Introdução

O Domain Name System (DNS) é uma parte essencial da infraestrutura da Internet. Ele permite acessar sites usando nomes de domínio em vez de endereços IP. O DNS funciona como uma agenda telefônica, convertendo nomes legíveis por pessoas em endereços IP compreendidos pelos computadores. O DNS raiz é o núcleo desse sistema hierárquico e distribuído, que participa da resolução dos nomes. Este artigo explica o funcionamento do DNS, do DNS raiz e dos registros associados aos domínios.

{{< youtube id="mpQZVYPuDGU" >}}

## O Domain Name System (DNS)

O **Domain Name System (DNS)** é um sistema descentralizado que associa nomes de domínio a endereços IP. Ele permite acessar sites e outros recursos da Internet digitando um nome no navegador. O DNS elimina a necessidade de memorizar endereços IP complexos.

### Hierarquia DNS

O DNS funciona em uma estrutura hierárquica com vários níveis. No topo está a zona raiz, seguida pelos domínios de nível superior (TLDs), domínios de segundo nível e subdomínios. Cada nível forma parte do nome completo. Em `www.example.com`, "www" é o subdomínio, "example" é o domínio de segundo nível e "com" é o TLD.

### Processo de resolução DNS

Quando você digita um nome de domínio no navegador, começa a resolução DNS. O navegador envia uma consulta a um resolvedor DNS, geralmente fornecido pelo provedor de Internet (ISP). O resolvedor segue várias etapas para encontrar o endereço IP correspondente ao nome.

1. **Cache DNS local**: o resolvedor primeiro procura o nome de domínio e o endereço IP solicitados no cache local. Se encontrar os dados, retorna o resultado sem fazer novas consultas.

2. **Consulta recursiva**: se os dados não estiverem no cache, o resolvedor inicia uma consulta recursiva. Primeiro, contata os servidores DNS raiz, responsáveis pela zona "." (ponto). Eles retornam os endereços IP dos servidores TLD do domínio solicitado.

3. **Consulta TLD**: o resolvedor contata os servidores TLD identificados na etapa anterior e solicita os endereços IP dos servidores de nomes autoritativos do domínio.

4. **Consulta ao servidor de nomes autoritativo**: o resolvedor consulta os servidores autoritativos indicados pelos servidores TLD. Eles armazenam os registros autoritativos do domínio e respondem com o endereço IP associado ao nome.

5. **Resposta ao cliente**: o resolvedor recebe o endereço IP dos servidores autoritativos e o envia ao navegador. Em seguida, o navegador pode se conectar ao servidor web usando esse endereço.

### Cache DNS

Os resolvedores DNS usam cache para melhorar o desempenho e reduzir a carga nos servidores DNS. Depois de receber uma resposta, o resolvedor armazena localmente a associação entre o nome de domínio e o endereço IP. Consultas futuras para o mesmo nome podem ser respondidas pelo cache, sem percorrer novamente a hierarquia DNS.

O cache existe em vários níveis, como no resolvedor local, no resolvedor do ISP e em dispositivos como roteadores e sistemas operacionais. O valor Time-to-Live (TTL) da resposta DNS determina por quanto tempo um registro fica armazenado. Quando o TTL expira, o resolvedor remove o registro e faz uma nova consulta.

#### Limpar o cache DNS local

Limpar o cache DNS ajuda a resolver alguns problemas e faz o sistema buscar registros atualizados. Veja como fazer isso em diferentes sistemas operacionais:

##### Windows

Para limpar o cache DNS no Windows:

1. Pressione `Win + R`, digite `cmd` e pressione Enter para abrir o Prompt de Comando.

2. Digite o comando abaixo e pressione Enter:

```bash
ipconfig /flushdns
```

Esse comando limpa o cache do resolvedor DNS do Windows.

##### macOS

Para limpar o cache DNS no macOS:

1. Abra o Terminal em Aplicativos > Utilitários ou procure-o com o Spotlight.

2. Digite o comando abaixo no Terminal e pressione Enter:

```bash
sudo killall -HUP mDNSResponder
```

Esse comando reinicia o processo mDNSResponder, responsável pela resolução DNS no macOS.

##### Linux

O método para limpar o cache DNS no Linux depende da distribuição e do resolvedor DNS. Veja duas opções comuns:

1. **Sistemas baseados em systemd (como Ubuntu e Fedora)**:

Abra o Terminal e execute o comando abaixo com privilégios de administrador:

```bash
sudo systemd-resolve --flush-caches

```

Esse comando limpa o cache DNS em sistemas que usam systemd-resolved como resolvedor.

2. **Sistemas sem systemd**:

Abra o Terminal e execute o comando abaixo com privilégios de administrador:

```bash
sudo /etc/init.d/nscd restart

```

Esse comando reinicia o Name Service Cache Daemon (nscd), responsável pelo cache DNS em distribuições Linux sem systemd.

Estas são orientações gerais. Os comandos e métodos podem variar um pouco conforme a versão do sistema operacional. Limpar o cache DNS resolve alguns problemas, mas não todos os problemas de conectividade de rede.

## Como funciona o sistema DNS raiz

O sistema DNS raiz é uma parte fundamental da infraestrutura DNS. Veja como ele funciona:

### 1. Zona raiz e servidores raiz

O sistema DNS raiz começa na **zona raiz**, o nível mais alto da hierarquia DNS. Ela contém informações sobre os servidores de nomes autoritativos de todos os domínios de nível superior (TLDs), como .com, .org, .net e domínios nacionais como .us e .uk.

O sistema DNS raiz tem 13 servidores raiz, identificados pelas letras de A a M. Eles ficam distribuídos geograficamente pelo mundo para garantir redundância e confiabilidade.

### 2. Roteamento anycast

Para lidar com o grande volume de tráfego DNS, os servidores raiz usam **roteamento anycast**. Vários servidores compartilham o mesmo endereço IP, mas ficam em locais diferentes. As condições da rede direcionam cada consulta ao servidor adequado e distribuem a carga.

Quando uma pessoa inicia uma consulta DNS, o anycast a encaminha ao servidor raiz disponível mais próximo. A infraestrutura de rede escolhe o caminho mais curto conforme as condições da rede. O anycast distribui a carga e ajuda a evitar gargalos.

### 3. Resolvedores DNS recursivos

Quando um resolvedor DNS recebe uma consulta para um nome de domínio, inicia uma resolução recursiva e contata um dos servidores raiz.

O servidor raiz responde com uma referência aos endereços IP dos servidores de nomes TLD responsáveis pelo TLD solicitado. Esses servidores TLD contêm informações sobre os servidores autoritativos dos domínios dentro do TLD.

### 4. Referências e servidores de nomes autoritativos

Depois de receber a referência do servidor raiz, o resolvedor contata o servidor de nomes TLD apropriado.

O servidor TLD responde com outra referência, que contém os endereços IP dos servidores de nomes autoritativos do domínio solicitado.

Em seguida, o resolvedor pede a esses servidores o endereço IP associado ao nome de domínio.

### 5. Cache e TTL

Durante a resolução DNS, o cache melhora o desempenho e reduz a carga nos servidores. Os resolvedores armazenam associações entre nomes de domínio e endereços IP.

Os registros DNS ficam no cache pelo período determinado pelo Time-to-Live (TTL). O TTL informa por quanto tempo um registro permanece válido. Quando o período termina, o resolvedor o remove e faz uma nova consulta para obter o endereço IP atualizado.

### 6. Colaboração e gerenciamento

O sistema DNS raiz é gerenciado em colaboração pela Internet Corporation for Assigned Names and Numbers (ICANN) e pelos operadores dos servidores raiz.

A ICANN supervisiona o gerenciamento e a coordenação geral do DNS e trabalha com os operadores dos servidores raiz. Juntos, eles mantêm o arquivo da zona raiz, que contém informações sobre os 13 servidores DNS raiz e seus endereços IP.

Os operadores dos servidores raiz garantem o funcionamento e a disponibilidade dos servidores raiz. Assim, contribuem para a estabilidade e a resiliência de toda a infraestrutura DNS.

O sistema DNS raiz é o ponto inicial da resolução DNS. Ele associa nomes de domínio a endereços IP e permite o acesso eficiente a sites e outros recursos da Internet.

#### Os 13 servidores DNS raiz

Os 13 servidores DNS raiz são identificados pelas letras de A a M. Cada servidor é hospedado em vários locais físicos para oferecer redundância e tolerância a falhas. Eles processam consultas à zona raiz, incluindo TLDs como .com, .org, .net e domínios nacionais como .us e .uk.

#### ICANN e gerenciamento do DNS raiz

A Internet Corporation for Assigned Names and Numbers (**ICANN**) gerencia e coordena o DNS e a atribuição de endereços IP. Ela trabalha com os operadores dos servidores raiz para manter a estabilidade e a segurança do DNS raiz. Juntos, mantêm o arquivo da zona raiz com informações sobre os 13 servidores raiz e seus endereços IP.

______

## Tipos de registros DNS e suas funções

{{< youtube id="HnUDtycXSNE" >}}

Os registros DNS são componentes essenciais do Domain Name System (DNS) e fornecem vários tipos de informações associadas a um domínio. Veja alguns tipos comuns e suas funções:

| Tipo de registro | Descrição | Exemplo |
|-------------|-----------------------------------------------------------------------------|-------------------------------------------|
| A | Associa um nome de domínio a um endereço IPv4. | `example.com     IN A 192.0.2.1` |
| AAAA | Associa um nome de domínio a um endereço IPv6. | `example.com     IN AAAA 2001:db8::1` |
| CNAME | Associa um alias (nome canônico) ao nome de domínio real. | `www.example.com IN CNAME example.com` |
| MX | Indica os servidores de e-mail que recebem mensagens do domínio. | `example.com     IN MX 10 mail.example.com` |
| TXT | Armazena texto arbitrário, geralmente para SPF, DKIM ou verificação do domínio. | `example.com     IN TXT "v=spf1 a mx -all"`|
| NS | Indica os servidores de nomes autoritativos do domínio. | `example.com     IN NS ns1.example.com` |
| SOA | Define propriedades globais da zona (registro start of authority). | `example.com     IN SOA ns1.example.com` |
| SRV | Define a localização de um serviço específico do domínio. | `_service._proto.example.com IN SRV 10 20 5060 target.example.com` |
| PTR | Associa um endereço IP a um nome de domínio (consulta DNS reversa). | `1.2.0.192.in-addr.arpa IN PTR example.com` |

### 1. Registro A (registro de endereço)

O **registro A** associa um nome de domínio a um endereço IPv4. É o tipo de registro DNS mais básico e comum. Quando você digita um domínio no navegador, ele ajuda a encontrar o endereço IP do servidor web que hospeda o site.

### 2. Registro AAAA (registro de endereço IPv6)

O **registro AAAA** tem a mesma função que o registro A, mas associa o domínio a um endereço IPv6. Com a transição para IPv6, ele se torna importante para a conectividade em redes IPv6.

### 3. Registro CNAME (registro de nome canônico)

O **registro CNAME** cria um alias ou nome canônico para um domínio. Ele é usado quando um domínio ou subdomínio deve apontar para outro. Por exemplo, você pode criar um CNAME que direcione "www" para "mywebsite.com".

### 4. Registro MX (registro de troca de e-mail)

O **registro MX** especifica o servidor de e-mail responsável por receber mensagens de um domínio. É possível definir vários registros MX com prioridades que determinam a ordem das tentativas quando o servidor principal fica indisponível.

### 5. Registro TXT (registro de texto)

O **registro TXT** armazena informações de texto associadas a um domínio. Ele é usado para verificar domínios, publicar registros SPF (Sender Policy Framework) para autenticação de e-mail e guardar informações ou observações gerais.

### 6. Registro SRV (registro de serviço)

O **registro SRV** define a localização de um serviço ou recurso específico do domínio. É usado em VoIP, mensagens instantâneas e outros aplicativos que precisam localizar servidores ou serviços específicos.

### 7. Registro NS (registro de servidor de nomes)

O **registro NS** especifica os servidores de nomes autoritativos do domínio. Esses servidores armazenam os registros DNS do domínio. O resolvedor consulta os registros NS para encontrar os servidores autoritativos.

### 8. Registro PTR (registro de ponteiro)

O **registro PTR** associa um endereço IP a um nome de domínio em consultas DNS reversas. É usado para verificar a identidade de servidores de e-mail e ajudar a combater spam. A consulta reversa ajuda a validar a autenticidade do servidor.

### 9. Registro SOA (registro de início de autoridade)

O **registro SOA** contém informações administrativas do domínio, como o servidor de nomes autoritativo principal, o e-mail do administrador e parâmetros de tempo dos registros DNS.

Estes são apenas alguns dos muitos tipos de registros DNS. Cada um tem uma função específica e permite resolver nomes de domínio para os recursos associados de forma eficiente e precisa.

______

## Comandos de diagnóstico DNS para diferentes sistemas operacionais

Quando há problemas de DNS, os comandos de diagnóstico ajudam a encontrar a causa. Estes são alguns comandos comuns por sistema operacional:

### Windows

#### 1. `ipconfig /flushdns`

Esse comando limpa o cache DNS do Windows e pode resolver problemas causados por registros desatualizados ou incorretos. Abra o Prompt de Comando e execute-o.

#### 2. `ipconfig /all`

`ipconfig /all` mostra informações detalhadas sobre as interfaces de rede do Windows, incluindo os servidores DNS configurados. Assim, você pode verificar se os servidores corretos estão em uso.

### macOS

#### 1. `sudo killall -HUP mDNSResponder`

Esse comando reinicia o mDNSResponder no macOS, o processo responsável pela resolução DNS. Ele pode atualizar as configurações e ajudar a resolver problemas. Abra o Terminal e execute-o com privilégios de administrador.

#### 2. `nslookup`

O comando `nslookup` permite consultar registros DNS, testar a resolução e verificar a conectividade com servidores DNS. No Terminal, execute `nslookup` seguido do domínio ou endereço IP que deseja investigar.

### Linux

#### 1. `systemd-resolve --flush-caches`

Em sistemas Linux que usam systemd como resolvedor DNS, `systemd-resolve --flush-caches` limpa o cache DNS. Isso pode resolver problemas causados por entradas antigas. Abra o Terminal e execute o comando com privilégios de administrador.

#### 2. `dig`

`dig` é uma ferramenta versátil de diagnóstico DNS disponível no Linux. Ela fornece detalhes sobre consultas, respostas e configurações dos servidores DNS. Use `dig` para consultar registros, testar a resolução e investigar problemas. No Terminal, execute `dig` seguido do domínio ou endereço IP que deseja verificar.

Esses comandos ajudam a diagnosticar e resolver problemas DNS em diferentes sistemas operacionais. Eles permitem examinar configurações DNS, servidores e problemas de conectividade.

Os comandos e as opções podem variar conforme a versão do sistema operacional e a distribuição. Consulte a documentação da sua versão para obter detalhes de uso.
______


## Conclusão

O Domain Name System (DNS) e o DNS raiz desempenham funções essenciais na Internet. O DNS permite acessar sites por nomes de domínio fáceis de ler, enquanto o DNS raiz é a base de toda a hierarquia DNS. Entender como eles funcionam ajuda a navegar na Web e a compreender a infraestrutura por trás dos serviços on-line.

______

## Referências

- [DNS na Wikipédia](https://en.wikipedia.org/wiki/Domain_Name_System)
- [Como o DNS funciona, segundo a Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [Site oficial da ICANN](https://www.icann.org/)
- [operadores dos servidores raiz](https://www.root-servers.org/)

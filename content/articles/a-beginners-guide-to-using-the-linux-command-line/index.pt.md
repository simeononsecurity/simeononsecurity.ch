---
title: "Guia para iniciantes: usando a linha de comando do Linux em segurança cibernética"
date: 2023-03-13
lastmod: 2026-11-15
toc: true
draft: false
description: "Aprenda a usar a linha de comando do Linux em segurança cibernética com comandos básicos e avançados."
tags: ["Linux", "Linha de comando", "Segurança cibernética", "Guia para iniciantes", "Varredura de rede", "Teste de vulnerabilidades", "Análise de malware", "Permissões", "Tráfego de rede", "Estado dos processos", "Estatísticas de rede", "Busca de arquivos", "Wireshark", "TCPDump", "Nmap", "CLI do Linux", "Segurança", "Teste de invasão", "Perícia digital"]
cover: "/img/cover/a-beginners-guide-to-using-the-linux-command-line.webp"
coverAlt: "Ilustração de uma tela com comandos verdes da linha de comando do Linux em um fundo escuro, cercada por cadeados digitais e linhas de rede."
coverCaption: ""
---

**Linux** é um sistema operacional versátil e seguro, usado amplamente no setor de segurança cibernética por ser de código aberto. Ainda assim, usar a interface de linha de comando do Linux (CLI) para tarefas de segurança pode parecer difícil para iniciantes. Este guia apresenta comandos básicos e avançados da CLI do Linux que ajudam em tarefas de segurança cibernética.

## Comandos básicos do Linux para segurança cibernética

### Exibir o diretório atual

O comando **pwd** (print working directory) exibe o diretório de trabalho atual na CLI. Esse é o diretório em que você está no sistema de arquivos. O comando ajuda na navegação e a entender sua localização em relação a outros diretórios. Por exemplo, se você está no diretório pessoal e quer abrir o diretório de documentos, use estes comandos:

```bash
$ pwd
/home/user
$ cd documents
$ pwd
/home/user/documents
```

No exemplo acima, o primeiro comando exibe o diretório atual, que é o diretório pessoal. O segundo muda para o diretório de documentos, e o terceiro exibe o novo diretório atual.

### Listar arquivos

O comando **ls** lista o conteúdo de um diretório na CLI. Ele mostra os nomes dos arquivos e diretórios no local atual. Use-o para identificar o que existe em um caminho específico. Para ver o conteúdo do diretório de documentos, por exemplo, use:

```bash
$ ls documents
file1.txt file2.pdf file3.docx
```

No exemplo acima, o comando lista o conteúdo do diretório de documentos, que contém três arquivos: file1.txt, file2.pdf e file3.docx. Você também pode executar o comando sem argumentos para listar o conteúdo do diretório atual. Por exemplo:

```bash
$ ls
Desktop Documents Downloads Music Pictures Public Templates Videos
```

No exemplo acima, o comando lista o conteúdo do diretório pessoal, incluindo subdiretórios como Desktop, Documents e Downloads.

### Mudar de diretório

O comando **cd** (change directory) muda o diretório de trabalho atual na CLI. Ele permite navegar pelo sistema de arquivos e acessar arquivos em outros locais. Para mudar para o diretório de documentos, use:

```bash
$ cd documents
```

No exemplo acima, o comando muda para o diretório de documentos dentro do diretório atual. Você também pode usar um caminho absoluto ou relativo para acessar um diretório que não esteja no diretório atual. Por exemplo:

```bash
$ cd /usr/local/bin
```

No exemplo acima, o comando muda para /usr/local/bin usando um caminho absoluto. Também é possível usar um caminho relativo. Por exemplo:

```bash
$ cd ../..
```

No exemplo acima, o comando sobe dois níveis a partir do diretório atual. A notação ".." representa o diretório pai e permite subir na árvore de diretórios.

### Concatenar arquivos

O comando **cat** (concatenate) exibe o conteúdo de um arquivo na CLI. Ele é útil para ler arquivos de texto, como logs e arquivos de configuração. Para ver o conteúdo de um arquivo chamado "file1.txt", use:

```bash
$ cat file1.txt
```

No exemplo acima, o comando exibe o conteúdo de "file1.txt". Você também pode usá-lo para concatenar vários arquivos e mostrar o conteúdo na CLI. Por exemplo:

```bash
$ cat file1.txt file2.txt file3.txt
```

No exemplo acima, o comando exibe o conteúdo de três arquivos: file1.txt, file2.pdf e file3.docx. Também é possível usar curingas para concatenar todos os arquivos que correspondam a um padrão. Por exemplo:

```bash
$ cat *.txt
```

No exemplo acima, o comando exibe o conteúdo de todos os arquivos com extensão ".txt" no diretório atual. Assim, você consulta vários arquivos rapidamente sem abri-los um por um.

### Busca com expressões regulares

O comando **grep** (global regular expression print) busca strings ou padrões específicos em um arquivo ou conjunto de arquivos pela CLI. Ele ajuda a encontrar padrões em logs ou informações específicas em arquivos de configuração. Para buscar todas as ocorrências da palavra "error" em um arquivo chamado "logfile.txt", use:

```bash
$ grep "error" logfile.txt
```

No exemplo acima, o comando busca todas as ocorrências de "error" em "logfile.txt" e exibe as linhas correspondentes. Você também pode usar expressões regulares para buscar padrões mais complexos. Para encontrar linhas com uma palavra que começa com "p" e termina com "y", use:

```bash
$ grep "p.*y" logfile.txt
```

No exemplo acima, o comando busca em "logfile.txt" linhas com uma palavra que começa com "p" e termina com "y". A expressão "p.*y" corresponde a qualquer string que comece com "p" e termine com "y", com qualquer quantidade de caracteres entre elas. Essa busca ajuda a encontrar padrões em logs que indiquem ameaças ou problemas de desempenho.

### Alterar permissões

O comando **chmod** (change mode) altera as permissões de um arquivo ou diretório na CLI. Ele é essencial para proteger arquivos e diretórios e controlar quem pode acessá-los. Três dígitos representam as permissões do proprietário, do grupo e dos demais usuários. Os valores seguem esta fórmula:

```
4 = ler
2 = escrever
1 = executar
```

Por exemplo, para dar permissões de leitura e gravação ao proprietário e somente leitura ao grupo e aos demais usuários em "file1.txt", use:

```bash
$ chmod 644 file1.txt
```

No exemplo acima, o comando define as permissões de "file1.txt" como 644. O primeiro dígito (6) representa leitura e gravação para o proprietário (4 + 2 = 6). O segundo dígito (4) dá somente leitura ao grupo. O terceiro dígito (4) também dá somente leitura aos demais usuários.

Você também pode usar letras para alterar permissões. Para dar leitura e gravação ao proprietário e ao grupo, e remover todas as permissões dos demais usuários em "file2.txt", use:

```bash
$ chmod ug=rw,o= file2.txt
```

No exemplo acima, o comando define as permissões de "file2.txt" como ug=rw,o=. "ug" representa proprietário e grupo, "r" representa leitura e "w" representa gravação. O sinal "=" define as permissões indicadas, e "o=" remove todas as permissões dos demais usuários. Esse comando ajuda a controlar o acesso a arquivos e diretórios sensíveis e a impedir acessos não autorizados.

## Comandos avançados do Linux para segurança cibernética

{{< figure src="linux-cli-advanced-security-commands-overview.webp" alt="Diagrama de um terminal Linux executando nmap, netstat e find para varredura de rede, monitoramento de processos e investigação de arquivos em tarefas de segurança cibernética" >}}

### Mapeamento de rede

O comando **nmap** é uma ferramenta poderosa de varredura de rede na CLI. Ele identifica hosts e serviços em uma rede, além de possíveis vulnerabilidades. Há várias técnicas de varredura, como descoberta de hosts, varredura de portas e detecção do sistema operacional.

Um uso básico do nmap é verificar um único endereço IP ou host. Para buscar portas abertas no IP 192.168.1.1, use:

```bash
$ nmap 192.168.1.1
```

O comando acima executa uma varredura TCP SYN no IP de destino e retorna uma lista de portas abertas. A saída mostra as portas, o serviço em cada porta e o estado dela (aberta ou fechada). Às vezes, também exibe informações como o sistema operacional do destino.

O nmap também verifica vários hosts ou endereços IP de uma vez. Para buscar portas abertas em uma faixa de IPs (192.168.1.1-255), use:

```bash
$ nmap 192.168.1.1-255
```

O comando acima verifica todos os endereços IP da faixa e retorna as portas e os serviços abertos em cada destino.

Além da descoberta de hosts e da varredura de portas, o nmap detecta serviços e versões, identifica sistemas operacionais e procura vulnerabilidades. Essas verificações ajudam a encontrar possíveis falhas na rede e protegê-la contra ataques.

### Captura de pacotes TCP

O comando **tcpdump** captura e analisa o tráfego de rede pela CLI. Ele ajuda a solucionar problemas de rede, analisar seu comportamento e identificar possíveis ameaças. O comando captura pacotes em tempo real e pode filtrá-los por critérios como IP de origem ou destino, protocolo e porta.

Um uso básico do tcpdump é capturar todo o tráfego de uma interface. Para capturar o tráfego da interface eth0, use:

```bash
$ sudo tcpdump -i eth0
```

O comando acima captura todos os pacotes da interface eth0 e os exibe em tempo real na CLI. A saída mostra os endereços IP de origem e destino, o protocolo e outras informações sobre cada pacote.

O tcpdump também filtra pacotes por vários critérios. Para capturar pacotes enviados a um IP específico ou recebidos dele, use:

```bash
$ sudo tcpdump host 192.168.1.1
```

O comando acima captura pacotes enviados ao IP 192.168.1.1 ou recebidos dele e os exibe em tempo real. Você também pode filtrar pelo protocolo (como TCP ou UDP), pelo número da porta ou por outros critérios.

O tcpdump também salva pacotes em um arquivo para análise posterior. Para capturar todo o tráfego de eth0 e salvá-lo em "capture.pcap", use:

```bash
$ sudo tcpdump -i eth0 -w capture.pcap
```

O comando acima captura os pacotes de eth0 e os salva em formato pcap no arquivo "capture.pcap". Depois, você pode analisá-los com ferramentas como Wireshark. Isso ajuda a analisar o comportamento da rede e identificar possíveis ameaças.

### Estado dos processos

O comando **ps** exibe informações sobre processos em execução em um sistema Linux pela CLI. Ele ajuda a identificar processos suspeitos que podem comprometer a segurança do sistema. Entre as informações exibidas estão o identificador do processo (PID), o usuário, o uso de CPU e memória e o nome do comando.

Um uso básico do ps é listar todos os processos em execução no sistema. Para isso, use:

```bash
$ ps aux
```

O comando acima mostra os processos em execução, seus PIDs, usuários, uso de CPU e memória e nomes dos comandos. Essa visão geral ajuda a localizar processos suspeitos.

O ps também mostra informações sobre um processo ou grupo específico. Para exibir dados de um processo com PID conhecido, como 1234, use:

```bash
$ ps -p 1234
```

O comando acima exibe informações do processo com PID 1234, incluindo usuário, uso de CPU e memória e nome do comando. Você também pode informar vários PIDs para exibir um grupo de processos.

O ps também monitora processos em tempo real. Para acompanhar o uso de CPU e memória de um processo, como o PID 1234, use:

```bash
$ ps -p 1234 -o %cpu,%mem
```

O comando acima exibe o uso de CPU e memória do processo com PID 1234 e atualiza a saída a cada segundo. Ele ajuda a monitorar processos importantes e identificar possíveis gargalos de desempenho.

### Estatísticas de rede

O comando **netstat** exibe informações sobre conexões de rede ativas em um sistema Linux pela CLI. Ele ajuda a identificar conexões não autorizadas e possíveis ameaças. Pode exibir endereços locais e remotos, o protocolo (como TCP ou UDP) e o estado da conexão.

Um uso básico do netstat é listar todas as conexões de rede ativas no sistema. Use:

```bash
$ netstat -a
```

O comando acima lista as conexões ativas, seus endereços locais e remotos, o protocolo e o estado. Essa visão geral ajuda a identificar conexões não autorizadas.

O netstat também mostra conexões de um protocolo específico, como TCP. Para listar as conexões TCP ativas, use:

```bash
$ netstat -at
```

O comando acima lista as conexões TCP ativas, seus endereços locais e remotos e o estado.

O netstat também mostra estatísticas de um protocolo específico. Para consultar as estatísticas de todas as conexões TCP, use:

```bash
$ netstat -st
```

O comando acima mostra estatísticas de conexões TCP, como o número de conexões ativas, quantas estão em cada estado e o total de erros. Isso ajuda a acompanhar a integridade da rede e identificar possíveis problemas de desempenho.

### Localizar arquivos

O comando **find** busca arquivos e diretórios em um sistema Linux pela CLI. Ele ajuda a localizar itens que estejam ocultos ou sejam difíceis de encontrar. A busca aceita vários critérios, como nome, tamanho, data de modificação e permissões.

Um uso básico do find é buscar pelo nome. Para localizar todos os arquivos chamados "example.txt" no diretório atual e nos subdiretórios, use:

```bash
$ find . -name example.txt
```

O comando acima busca arquivos chamados "example.txt" no diretório atual e nos subdiretórios e exibe o caminho completo de cada um.

O find também busca por tamanho. Para localizar arquivos maiores que 1 MB no diretório atual e nos subdiretórios, use:

```bash
$ find . -size +1M
```

O comando acima busca arquivos maiores que 1 MB no diretório atual e nos subdiretórios e exibe seus caminhos completos.

Além de nome e tamanho, o find busca por data de modificação e permissões. Para localizar arquivos modificados nos últimos sete dias, use:

```bash
$ find . -mtime -7
```

O comando acima busca arquivos modificados nos últimos sete dias no diretório atual e nos subdiretórios e exibe seus caminhos completos.

O find é uma ferramenta poderosa para localizar arquivos e diretórios por vários critérios. Ele é útil em tarefas de administração de sistemas e segurança cibernética.

______

Usar a linha de comando do Linux para segurança cibernética pode parecer difícil para iniciantes. Os comandos básicos e avançados deste guia ajudam você a aproveitar a CLI. Tenha cuidado ao executar comandos e entenda o que cada um faz antes de usá-lo.

Para aprender mais sobre Linux em segurança cibernética, baixe o sistema operacional **[Kali Linux](https://www.kali.org/downloads/)**, projetado para testes de invasão e perícia digital.

## Conclusão

A interface de linha de comando do Linux é uma ferramenta poderosa para profissionais de segurança cibernética, mas pode ser difícil para iniciantes. Aprenda os comandos básicos e avançados deste guia para usar a CLI a seu favor. Tenha cuidado e entenda cada comando antes de executá-lo. Com prática e experiência, você dominará a linha de comando do Linux e desenvolverá suas habilidades de segurança cibernética.

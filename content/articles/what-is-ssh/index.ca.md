---
title: "Guia de SSH: accés remot segur, claus i transferència de fitxers"
date: 2023-06-14
lastmod: 2026-11-26
toc: true
draft: false
description: "Aprèn què fa SSH, com crear claus, verificar claus d'amfitrió, transferir fitxers i gestionar la configuració del client i del servidor."
tags: ["SSH", "Secure Shell", "accés remot", "administració remota", "xifratge", "autenticació", "integritat de dades", "portabilitat", "transferència de fitxers", "SCP", "SFTP", "claus SSH", "Ed25519", "configuració SSH", "amfitrions coneguts", "protocol de xarxa", "execució remota d'ordres", "OpenSSH", "autenticació de dos factors", "criptografia de clau pública", "adreça IP", "nom de domini", "terminal", "indicador d'ordres", "seguretat", "administradors de sistemes", "desenvolupadors", "mètodes d'autenticació", "túnels"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_securely_connecting.webp"
coverAlt: "Il·lustració de dibuixos animats d'una persona que es connecta de manera segura a un servidor amb SSH."
coverCaption: ""
---

**Què és SSH i com s'utilitza?**

**SSH** (Secure Shell) és un protocol de xarxa per iniciar sessió remotament amb xifratge, executar ordres, reenviar ports i transferir fitxers. Un client SSH es connecta a un servidor SSH a través d'una xarxa no fiable. El servidor demostra la seva identitat amb una clau d'amfitrió. A continuació, l'usuari s'autentica amb una contrasenya, una clau pública o un altre mètode configurat.

El [manual d'OpenBSD de `ssh(1)`](https://man.openbsd.org/ssh) descriu el client com una eina de comunicació xifrada segura entre amfitrions no fiables. Aquesta guia se centra en **OpenSSH**, la implementació disponible en molts sistemes Linux, macOS, BSD i Windows.

{{< youtube id="Atbl7D_yPug" enable="true" >}}

**Dificultat:** iniciació. **Temps:** 15 minuts.

## Punts clau

- SSH comprova la clau d'amfitrió del servidor abans d'autenticar l'usuari.
- Una clau Ed25519 protegida amb una frase de contrasenya és una bona opció inicial per a usuaris nous.
- Fes servir `ssh` per a ordres remotes, `scp` per copiar fitxers i `sftp` per a transferències interactives.
- Prova una clau nova en una sessió separada abans de desactivar l'autenticació amb contrasenya.

## Abans de començar

- Instal·la un client OpenSSH a l'ordinador local.
- Aconsegueix el nom d'amfitrió o l'adreça IP remota, el nom del compte, el port SSH i un mètode d'autenticació aprovat.
- Aconsegueix l'empremta digital de la clau d'amfitrió del servidor des d'una consola fiable, un registre d'administració o una altra font independent.
- Mantén disponible una sessió d'inici de sessió amb contrasenya o una consola local quan instal·lis una clau pública o canviïs la configuració del servidor.

Les ordres de shell d'aquesta guia fan servir sintaxi POSIX a Linux, macOS, BSD o un entorn compatible. Els usuaris d'OpenSSH a Windows han d'adaptar els camins dels fitxers i les ordres de permisos a PowerShell o WSL. Executa les ordres del client a l'ordinador local. Executa les ordres del servidor, inclosa `sshd -t`, al servidor SSH amb accés a la configuració i a les claus d'amfitrió.

## SSH d'un cop d'ull

| Tasca | Eina | Resultat |
|------|------|--------|
| **Inici de sessió remot** | `ssh` | Obre un shell o executa una ordre en un amfitrió remot |
| **Creació de claus** | `ssh-keygen` | Crea una clau privada i una clau pública corresponent |
| **Còpia de fitxers** | `scp` | Copia fitxers mitjançant una connexió SSH |
| **Transferència interactiva** | `sftp` | Navega i transfereix fitxers amb SFTP |
| **Configuració del client** | `~/.ssh/config` | Desa opcions de connexió per amfitrió |
| **Configuració del servidor** | `/etc/ssh/sshd_config` | Configura el dimoni OpenSSH |

*El canal xifrat protegeix el transport. Encara cal verificar la destinació, restringir les claus i revisar cada ordre remota.*

## Avantatges de SSH

SSH separa l'**autenticació de l'amfitrió** de l'**autenticació de l'usuari**. El client comprova la clau d'amfitrió del servidor, una identitat criptogràfica del servidor. Després, el servidor comprova la contrasenya, la clau pública o un altre mètode permès de l'usuari.

1. **Seguretat:** SSH xifra la sessió entre el client i el servidor. El xifratge protegeix les credencials, les ordres i les dades retornades mentre travessen una xarxa no fiable.

2. **Autenticació:** SSH admet contrasenyes, claus públiques, mètodes interactius de teclat i altres mètodes aprovats pel servidor. L'autenticació amb clau pública manté la clau privada al client i envia una prova de possessió durant l'inici de sessió.

3. **Integritat de dades:** el transport SSH protegeix els missatges contra modificacions no detectades. Una sessió xifrada vàlida encara depèn de la verificació correcta de la clau d'amfitrió.

4. **Portabilitat:** hi ha clients i servidors OpenSSH per a Linux, macOS, BSD i Windows. El mateix flux bàsic de `ssh`, `scp` i `sftp` funciona en aquestes plataformes.

5. **Flexibilitat:** SSH admet ordres remotes, transferència de fitxers, reenviament de ports i altres funcions de connexió. Fes servir cada funció només amb una finalitat i una destinació aprovades.

| Opció d'autenticació | Avantatge | Compromís operatiu |
|-----------------------|----------|-----------------------|
| **Contrasenya** | Coneguda i fàcil d'implantar | Exposada a intents d'endevinació i a la reutilització de credencials |
| **Clau pública** | La clau privada es queda al client | Cal planificar-ne el cicle de vida i la recuperació |
| **Clau pública amb frase de contrasenya** | Afegeix protecció si es copia el fitxer de clau privada | Cal introduir la frase o fer servir un agent SSH |
| **Autenticació interactiva o multifactor (MFA)** | Afegeix un repte controlat pel servidor | Necessita suport del servidor i del client |

***Una clau d'usuari protegida amb frase de contrasenya és l'opció predeterminada per a l'administració interactiva.***

## Com fer servir SSH

### Generar claus SSH

Abans de fer servir l'autenticació amb clau pública, crea un parell de claus SSH. El parell conté una **clau pública** per al compte remot i una **clau privada** per al client local. Col·loca la clau pública al fitxer `~/.ssh/authorized_keys` del compte remot. Mantén la clau privada al client i protegeix-la amb una frase de contrasenya.

1. Instal·la **OpenSSH** a l'ordinador local si no hi és. Consulta la documentació oficial del sistema operatiu.

2. Obre un terminal o indicador d'ordres i executa l'ordre següent per generar l'exemple RSA original:

```shell

ssh-keygen -t rsa -b 4096

```

Per a una clau d'usuari nova, fes servir **Ed25519** en sistemes amb suport per a versions actuals d'OpenSSH:

```shell
ssh-keygen -t ed25519 -C "reader@example.com"
```

El manual actual d'OpenBSD indica Ed25519 com a tipus de clau predeterminat quan `ssh-keygen` no rep l'opció `-t`. L'ordre RSA original continua sent útil en sistemes antics o per requisits de compatibilitat. L'opció `-b` controla la mida de la clau RSA. Ed25519 fa servir una mida fixa.

3. Quan se't demani, introdueix un nom de fitxer i una frase de contrasenya robusta. Prem Enter per acceptar el nom predeterminat només si la clau predeterminada servirà per al compte previst. Una frase buida deixa una clau privada copiada sense protecció emmagatzemada.

4. Es generarà el parell de claus. El nom de la clau pública acaba en `.pub`. La clau privada no té extensió i ha de continuar sent privada.

Instal·la la clau pública mitjançant una sessió existent amb contrasenya o una consola local. En un sistema amb `ssh-copy-id`, executa:

```shell
ssh-copy-id -i ~/.ssh/id_ed25519.pub username@remote_server_ip
```

Fes servir `~/.ssh/id_ed25519.pub` amb l'ordre Ed25519. L'ordre RSA conservada crea `~/.ssh/id_rsa.pub`, així que substitueix el camí per l'arxiu RSA quan instal·lis una clau RSA. Si `ssh-copy-id` no està disponible, executa això al client mitjançant una sessió existent amb contrasenya:

```shell
cat ~/.ssh/id_ed25519.pub | ssh username@remote_server_ip 'umask 077 && mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys'
```

L'ordre crea un directori remot `.ssh` privat i hi afegeix una línia de clau pública. Comprova que el fitxer remot `~/.ssh/authorized_keys` conté la clau prevista. El fitxer `authorized_keys` enumera les claus públiques autoritzades a iniciar sessió. Si una consola local és l'únic camí d'accés, afegeix-hi la mateixa línia de clau pública i estableix els permisos de `~/.ssh` a `700` i els d'`authorized_keys` a `600`.

Si has triat l'exemple RSA, substitueix cada camí `id_ed25519` posterior per `id_rsa`.

Obre un terminal nou i prova la clau abans de canviar la configuració d'autenticació del servidor:

```shell
ssh -o PreferredAuthentications=publickey -o PasswordAuthentication=no -i ~/.ssh/id_ed25519 username@remote_server_ip
```

Confirma que la sessió nova s'obre amb el compte previst. Mantén disponible la sessió existent per recuperar l'accés si la prova falla.

Comprova l'empremta digital d'una clau pública abans d'instal·lar-la o auditar-la:

```shell
ssh-keygen -l -f ~/.ssh/id_ed25519.pub
```

*No enganxis una clau privada en un tiquet, una conversa, l'historial del shell ni una ordre remota. Substitueix-la si sospites que s'ha divulgat i elimina la clau pública de tots els comptes autoritzats.*

### Connectar-se a un servidor remot

Per connectar-te a un servidor remot amb SSH, segueix aquests passos:

1. Aconsegueix l'**adreça IP** o el nom de domini del servidor remot al qual et vols connectar.

2. Obre un terminal o indicador d'ordres i fes servir l'ordre següent per iniciar una connexió SSH:

```shell
ssh username@remote_server_ip
```

Substitueix `username` pel teu nom d'usuari al servidor remot i `remote_server_ip` per l'adreça IP real o el nom de domini del servidor.

3. En la primera connexió, SSH mostra un avís sobre la clau d'amfitrió. Compara'n l'empremta digital amb la d'una consola fiable, un registre d'administració o una altra font independent abans d'acceptar-la. El client desa les claus d'amfitrió acceptades a `~/.ssh/known_hosts`.

4. Quan se't demani, introdueix la contrasenya del compte o la frase de la clau privada seleccionada. Tria una clau concreta amb l'opció `-i`:

```shell
ssh -i ~/.ssh/id_ed25519 username@remote_server_ip
```

5. Si l'autenticació té èxit, SSH obre un shell remot. Investiga qualsevol canvi de la clau d'amfitrió abans de tornar a provar l'inici de sessió. No et saltis la verificació de la clau per silenciar un avís.

Per examinar les empremtes digitals desades per als amfitrions coneguts:

```shell
ssh-keygen -l -f ~/.ssh/known_hosts
```

### Transferir fitxers amb SSH

SSH també permet transferir fitxers de manera segura. **SCP** copia fitxers mitjançant una connexió SSH. **SFTP** ofereix una sessió interactiva de transferència de fitxers.

1. Obre un terminal o indicador d'ordres a l'ordinador local.

2. Fes servir l'ordre següent per copiar un fitxer de l'ordinador local al servidor remot:

```shell

scp /path/to/local/file username@remote_server_ip:/path/to/remote/location

```

Substitueix `/path/to/local/file` pel camí i el nom reals del fitxer local. Igualment, substitueix `username@remote_server_ip:/path/to/remote/location` pel nom d'usuari adequat, l'adreça IP del servidor i la ubicació remota del fitxer.

Tria una clau privada concreta amb `-i` quan la configuració del client no seleccioni la clau prevista:

```shell
scp -i ~/.ssh/id_ed25519 /path/to/local/file username@remote_server_ip:/path/to/remote/location
```

3. La primera connexió sovint mostra un avís sobre l'autenticitat de l'amfitrió. Verifica l'empremta digital del servidor abans de continuar.

4. Si se't demana, introdueix la contrasenya del compte o la frase de la clau privada seleccionada. El fitxer es copiarà per la connexió SSH.

Per a una sessió interactiva del Protocol de transferència de fitxers SSH (SFTP), fes servir:

```shell
sftp username@remote_server_ip
```

Des de l'OpenSSH 9.0, `scp` fa servir SFTP per defecte per a les transferències. L'opció `-O` selecciona el protocol SCP antic per compatibilitat amb un servidor o un patró de nom de fitxer que requereixi el mode antic. Fes servir el mode predeterminat tret que una necessitat de compatibilitat documentada exigeixi `-O`.

### Configuració SSH

Els fitxers de configuració SSH personalitzen el comportament del client i del servidor. El fitxer principal del servidor acostuma a ser `/etc/ssh/sshd_config`. El fitxer del client per a cada usuari és `~/.ssh/config`.

Crea un àlies de client per reutilitzar la mateixa configuració revisada en les connexions repetides:

```sshconfig
Host lab-server
    HostName remote_server_ip
    User username
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
```

Connecta't amb l'àlies:

```shell
ssh lab-server
```

`IdentityFile` selecciona la clau. `IdentitiesOnly yes` limita els intents d'autenticació a les identitats configurades. Protegeix el directori i el fitxer de configuració del client:

```shell
chmod 700 ~/.ssh
chmod 600 ~/.ssh/config
```

Per defecte, el dimoni OpenSSH llegeix les claus públiques de `~/.ssh/authorized_keys`. Al servidor, abans d'aplicar un canvi de configuració, comprova la sintaxi del dimoni i la disponibilitat de la clau d'amfitrió amb:

```shell
sshd -t
```

Executa aquesta comprovació al servidor amb els permisos necessaris per llegir-ne la configuració i les claus d'amfitrió. No comprova la clau autoritzada d'un usuari ni demostra que l'inici de sessió amb clau pública funcioni. Mantén oberta una sessió existent mentre proves una clau nova. Estableix `PasswordAuthentication no` només quan l'inici de sessió separat amb clau pública funcioni i hi hagi una via de recuperació.

| Àrea de configuració | Fitxer o opció | Pregunta de revisió |
|-------------------|----------------|-----------------|
| **Àlies del client** | `~/.ssh/config` | L'àlies apunta a l'amfitrió i l'usuari previstos? |
| **Identitat del client** | `IdentityFile` | La clau pertany al compte previst? |
| **Selecció d'identitat** | `IdentitiesOnly` | El client oferirà només la clau revisada? |
| **Autorització del servidor** | `~/.ssh/authorized_keys` | Cada clau té un responsable i un pla de retirada? |
| **Alternativa amb contrasenya** | `PasswordAuthentication` | Hi ha una via de recuperació provada abans del canvi? |

## Solucionar problemes de SSH

Comença amb la configuració efectiva del client i la sortida detallada. Aquestes comprovacions mostren àlies o usuaris incorrectes, claus inesperades i camins dels fitxers de claus d'amfitrió sense canviar la configuració del servidor:

```shell
ssh -G lab-server
ssh -vvv lab-server
```

Si falla l'autenticació amb clau, comprova aquests punts en ordre:

- **Identitat de l'amfitrió:** compara l'empremta digital mostrada amb un registre fiable.
- **Parell de claus:** compara l'empremta digital de la clau pública local amb la clau instal·lada per al compte remot.
- **Permisos dels fitxers:** mantén `~/.ssh` privat i protegeix `config`, les claus privades i `authorized_keys` dels altres usuaris.
- **Selecció del client:** comprova `IdentityFile` i `IdentitiesOnly` a la configuració efectiva.
- **Sintaxi del servidor:** executa `sshd -t` abans de tornar a carregar una configuració modificada.
- **Recuperació:** mantén una sessió administrativa separada fins que l'inici de sessió nou funcioni.

Si falla una connexió, separa la comprovació de xarxa de la d'autenticació:

- **Resolució de noms:** prova el nom d'amfitrió amb les eines DNS del sistema operatiu. Prova la IP del servidor només després de confirmar-la amb una font fiable.
- **Port i tallafoc:** fes servir el port SSH configurat al servidor. Confirma que el tallafoc del servidor permet la xarxa del client.
- **Connexió refusada:** comprova si el dimoni SSH està en execució i escolta a l'adreça i al port esperats.
- **Temps d'espera esgotat:** comprova l'encaminament, els grups de seguretat, els tallafocs de l'amfitrió i l'accés VPN abans de canviar les claus.
- **Registres del servidor:** consulta els registres del dimoni SSH per veure quin usuari, clau o política s'ha rebutjat.
- **Permisos de la clau remota:** confirma que el compte és propietari de `~/.ssh`, que `authorized_keys` té permisos restrictius i que el directori personal permet que SSH llegeixi el camí.

## Conclusió

SSH és un protocol segur per accedir remotament i administrar servidors i ordinadors. El xifratge, les comprovacions de claus d'amfitrió, els mètodes d'autenticació i les eines de transferència de fitxers serveixen a administradors, desenvolupadors i altres usuaris autoritzats.

Comença amb una clau protegida amb frase de contrasenya, verifica l'empremta del servidor, fes servir un àlies de client per amfitrió i mantén oberta una sessió de recuperació durant els canvis al servidor. Així tindràs un flux de treball SSH repetible sense tractar el xifratge com a substitut del control d'accés.

Com a pas següent, llegeix la [guia de reforç de Linux](/articles/dos-and-donts-for-hardening-linux/) per als controls de l'amfitrió. Per a una administració repetible, consulta [Ansible per a principiants](/articles/ansible-for-beginners/) i el seu flux de connexió basat en SSH.

______

## Passos següents

- Substitueix els noms d'amfitrió, els noms d'usuari i els camins d'exemple per valors revisats per al teu entorn.
- Registra les empremtes de les claus d'amfitrió i la propietat de les claus als registres d'administració.
- Prova un segon inici de sessió administratiu abans de canviar la configuració de contrasenya o del tallafoc.
- Afegeix la revisió de la configuració SSH al procés de reforç i automatització dels sistemes.

## Referències

- [SSH a la Viquipèdia](https://en.wikipedia.org/wiki/Secure_Shell)
- [Documentació de SCP](https://man.openbsd.org/scp)
- [Documentació del fitxer de configuració SSH](https://man.openbsd.org/sshd_config)
- [Manual d'OpenSSH de `ssh-keygen(1)`](https://man.openbsd.org/ssh-keygen)
- [Manual d'OpenSSH de `ssh(1)`](https://man.openbsd.org/ssh)
- [Manual d'OpenSSH de `ssh_config(5)`](https://man.openbsd.org/ssh_config)
- [Manual d'OpenSSH de `sshd(8)`](https://man.openbsd.org/sshd)
- [Notes de la versió d'OpenSSH](https://www.openssh.org/releasenotes.html)

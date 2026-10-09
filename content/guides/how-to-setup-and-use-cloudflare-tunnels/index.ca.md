---
title: "Configuració de Cloudflare Tunnels"
draft: false
toc: true
date: 2023-05-26
description: Apreneu a configurar Cloudflare Tunnels per simplificar i protegir el trànsit de la vostra xarxa, millorant el rendiment i la seguretat.
tags:
- Cloudflare Tunnels
- Seguretat de Xarxa
- Rendiment del Lloc Web
- Servidor Proxy
- Trànsit Web
- Configuració de Xarxa
- Servidor Ubuntu
- Compte de Cloudflare
- Autenticació
- Creació de Túnel
- Enrutament de Trànsit
- Registres DNS
- Connexió Segura
- Allotjament de Lloc Web
- Servei Proxy
- Protecció de Xarxa
- Optimització del Rendiment
- Integració amb Cloudflare
- Configuració del Servidor
- Xifrat del Trànsit
- Gestió del Trànsit de Xarxa
- Allotjament Web Segur
- Seguretat del Lloc Web
- Configuració d’Ubuntu
- Tecnologia de Túnels
- Serveis de Cloudflare
- Rendiment de Xarxa
- Seguretat Web
- Seguretat del Servidor
- Gestió del Trànsit
- Proxy de Cloudflare
cover: /img/cover/An_illustration_showing_a_network_tunnel_connecting_a_local.webp
coverAlt: Una il·lustració que mostra un túnel de xarxa connectant un servidor local amb el logotip de Cloudflare, simbolitzant el trànsit de xarxa segur i simplificat.
coverCaption: ''
lastmod: 2026-10-08
---

**Una Guia per Configurar Cloudflare Tunnels**

## Introducció
Cloudflare Tunnels ofereixen una manera segura d’allotjar llocs web establint una connexió directa entre la vostra xarxa local i Cloudflare. Aquesta guia us guiarà pel procés de configuració de Cloudflare Tunnels per millorar la seguretat i el rendiment del vostre lloc web.

______

## Per què Cloudflare Tunnels?
Cloudflare Tunnels ofereixen diversos avantatges, incloent la reducció dels vectors d’atac i la simplificació de les configuracions de xarxa. Utilitzant Cloudflare com a proxy, podeu tancar ports externs i assegurar que tot el trànsit passi per la xarxa segura de Cloudflare. Això proporciona una capa addicional de protecció per al vostre lloc web.

______

## Prerequisits
Abans de configurar Cloudflare Tunnels, assegureu-vos que disposeu del següent:

1. Un compte actiu de Cloudflare.
2. Un servidor amb Ubuntu.

______

## Pas 1: Instal·lació
Per començar, heu d’instal·lar el paquet de Cloudflare Tunnels al vostre servidor Ubuntu. Seguiu aquests passos:

1. Obriu el terminal al vostre servidor Ubuntu.
2. Descarregueu la versió més recent del paquet de Cloudflare Tunnels executant la següent comanda:

```shell
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
```

## Pas 2: Autenticació
A continuació, heu d’autenticar el vostre compte de Cloudflare amb el servei de Cloudflare Tunnels. Seguiu aquests passos:

1. Executeu la següent comanda al terminal:

```shell
cloudflared tunnel login
```

2. Feu clic al lloc que voleu utilitzar amb el vostre túnel per completar el procés d’autenticació.

## Pas 3: Creació d’un Túnel

Ara és el moment de crear el vostre Cloudflare Tunnel. Seguiu aquests passos:

1. Executeu la següent comanda al terminal per crear un túnel:

```shell
cloudflared tunnel create name_of_tunnel
```

2. Trieu un nom per al vostre túnel que sigui fàcil de recordar i descriptiu. Tingueu en compte que el nom del túnel no es podrà canviar més endavant.

3. Després de crear el túnel, se us proporcionarà informació important, inclòs el UUID del vostre túnel. Apunteu aquest UUID ja que serà necessari per a la configuració posterior.

4. Per veure una llista de tots els túnels actius, utilitzeu la comanda:

```shell
cloudflared tunnel list
```

Això mostrarà els noms i UUID dels vostres túnels.

### Pas 4: Configuració del Túnel

Per configurar el vostre túnel i començar a enrutar el trànsit, seguiu aquests passos:

1. Navegueu al directori de Cloudflare Tunnels al vostre servidor. La ubicació per defecte és `/etc/cloudflared`.

2. Dins d’aquest directori, creeu un fitxer nou anomenat `config.yml` amb un editor de text al vostre gust.

3. Ompliu el fitxer config.yml amb el següent contingut:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json
```

Assegureu-vos de substituir `<your_tunnels_uuid>` pel UUID del vostre túnel i actualitzeu la ruta al fitxer de credencials si cal.

## Pas 5: Enrutament del Trànsit

Per especificar els serveis interns que voleu servir a través del vostre túnel, seguiu aquests passos:

1. Editeu el fitxer `Open the `config.yml` de nou.

2. Afegiu els paràmetres ingress al fitxer per definir els serveis que voleu enrutar a través de Cloudflare. Per exemple:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json

ingress:
  - hostname: example.com
    service: http://10.10.10.123:1234
  - hostname: subdomain.example.com
    service: http://10.10.10.123:8888
  - service: http_status:404

```

Substituïu `<your_tunnels_uuid>` pel UUID del vostre túnel i actualitzeu el nom d’amfitrió i els detalls del servei segons la vostra configuració.

3. Deseu el fitxer config.yml.


## Pas 6: Creació de Registres DNS

Per crear registres DNS per al nom d’amfitrió i serveis del vostre túnel, seguiu aquests passos:

1. Obriu el terminal.

2. Utilitzeu la següent comanda per crear un registre DNS:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> <hostname>
```
Substituïu `<UUID or NAME of tunnel>` pel UUID o nom del vostre túnel i `<hostname>` pel nom d’amfitrió desitjat per al vostre servei.

3. Per exemple, per crear un registre DNS per example.com, executeu la comanda:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> example.com
```

Tingueu en compte que els canvis es reflectiran a la secció DNS del vostre tauler de Cloudflare.

## Pas 7: Inici del Túnel

Per provar i iniciar el vostre Cloudflare Tunnel, seguiu aquests passos:

1. Obriu el terminal.

2. Executeu la següent comanda per iniciar el túnel:

```shell
cloudflared tunnel run <UUID or NAME of tunnel>
```

Substituïu `<UUID or NAME of tunnel>` pel UUID o nom del vostre túnel.

3. Cloudflared configurarà ara el vostre túnel i mostrarà informació sobre el seu estat. Un cop el túnel estigui actiu i funcionant correctament, podeu continuar amb el següent pas.

4. Per evitar que el túnel es tanqui quan sortiu del terminal, heu d’executar Cloudflared com a servei systemd. Utilitzeu la següent comanda:

```shell
cloudflared --config /path/to/config.yml service install
```

Substituïu `/path/to/config.yml` per la ruta al vostre fitxer `config.yml`.

## Conclusió

En aquesta guia, hem cobert els passos per configurar Cloudflare Tunnels a Ubuntu. Seguint aquestes instruccions, podeu millorar la seguretat i el rendiment del vostre lloc web utilitzant la xarxa de Cloudflare. Recordeu monitoritzar regularment els vostres túnels i ajustar la configuració segons calgui.

Si teniu algun problema o necessiteu més ajuda, consulteu la [documentació oficial de Cloudflare Tunnels](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/).


## Referències
- [Documentació de Cloudflare Tunnels](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)
- [Repositori GitHub de Cloudflare Tunnels](https://github.com/cloudflare/cloudflared)
- [tcude - Com Configurar Cloudflare Tunnels a Ubuntu](https://tcude.net/creating-cloudflare-tunnels-on-ubuntu/)

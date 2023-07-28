---
title: "Configurarea tunelurilor Cloudflare: Simplificați și securizați traficul de rețea"
draft: false
toc: true
date: 2023-05-26
description: "Aflați cum să configurați tunelurile Cloudflare pentru a simplifica și proteja traficul din rețea, îmbunătățind performanța și securitatea."
tags: ["Tuneluri Cloudflare", "Securitatea rețelelor", "Performanța site-ului web", "Server Proxy", "Trafic web", "Configurarea rețelei", "Server Ubuntu", "Cont Cloudflare", "Autentificare", "Crearea tunelului", "Rutarea traficului", "Înregistrări DNS", "Conexiune securizată", "Găzduire site web", "Serviciul Proxy", "Protecția rețelei", "Optimizarea performanței", "Integrarea Cloudflare", "Configurația serverului", "Criptarea traficului", "Managementul traficului de rețea", "Găzduire web securizată", "Securitatea site-ului web", "Configurarea Ubuntu", "Tehnologia tunelurilor", "Servicii Cloudflare", "Performanța rețelei", "Securitate web", "Securitatea serverului", "Managementul traficului", "Cloudflare Proxy"]
cover: "/img/cover/An_illustration_showing_a_network_tunnel_connecting_a_local.png"
coverAlt: "O ilustrație care arată un tunel de rețea care conectează un server local la logo-ul Cloudflare, simbolizând traficul de rețea securizat și simplificat."
coverCaption: ""
---

**Un ghid de configurare a tunelurilor Cloudflare**

## Introducere
Tunelurile Cloudflare oferă o modalitate sigură de a găzdui site-uri web prin stabilirea unei conexiuni directe între rețeaua dvs. locală și Cloudflare. Acest ghid vă va ghida prin procesul de configurare a Tunelurilor Cloudflare pentru a spori securitatea și performanța site-ului dvs. web.

______

## De ce Cloudflare Tunnels?
Tunelurile Cloudflare oferă mai multe beneficii, inclusiv reducerea vectorilor de atac și simplificarea configurațiilor de rețea. Utilizând Cloudflare ca proxy, puteți închide porturile externe și vă puteți asigura că tot traficul trece prin rețeaua securizată a Cloudflare. Acest lucru oferă un nivel suplimentar de protecție pentru site-ul dvs. web.

______

## Condiții prealabile
Înainte de a configura tunelurile Cloudflare, asigurați-vă că aveți următoarele:

1. Un cont Cloudflare activ.
2. Un server care rulează Ubuntu.

______

## Pasul 1: Instalare
Pentru a începe, trebuie să instalați pachetul Cloudflare Tunnels pe serverul dumneavoastră Ubuntu. Urmați acești pași:

1. Deschideți terminalul pe serverul Ubuntu.
2. Descărcați cea mai recentă versiune a pachetului Cloudflare Tunnels prin rularea următoarei comenzi:

```shell
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
```

## Pasul 2: Autentificarea
În continuare, trebuie să vă autentificați contul Cloudflare cu serviciul Cloudflare Tunnels. Urmați acești pași:

1. Rulați următoarea comandă în terminal:

```shell
cloudflared tunnel login
```

2. Faceți clic pe site-ul pe care doriți să îl utilizați cu tunelul dvs. pentru a finaliza procesul de autentificare.

## Pasul 3: Crearea unui tunel

Acum este timpul să vă creați Tunelul Cloudflare. Urmați acești pași:

1. Rulați următoarea comandă în terminal pentru a crea un tunel:

```shell
cloudflared tunnel create name_of_tunnel
```

2. Alegeți un nume pentru tunelul dumneavoastră care să fie memorabil și descriptiv. Rețineți că numele tunelului nu poate fi schimbat ulterior.

3.După crearea tunelului, vi se vor furniza informații importante, inclusiv UUID-ul tunelului dumneavoastră. Notați acest UUID, deoarece va fi necesar pentru configurarea ulterioară.

4. Pentru a vizualiza o listă cu toate tunelurile active, utilizați comanda:

```shell
cloudflared tunnel list
```

Aceasta va afișa numele și UUID-urile tunelurilor dumneavoastră.

### Pasul 4: Configurarea tunelului

Pentru a configura tunelul dvs. și a începe să rutați traficul, urmați acești pași:

1. Navigați în directorul Cloudflare Tunnels de pe serverul dvs. Locația implicită este `/etc/cloudflared`

2. În acest director, creați un nou fișier numit `config.yml` utilizând un editor de text la alegere.

3. Umpleți fișierul config.yml cu următorul conținut:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json
```

Asigurați-vă că înlocuiți `<your_tunnels_uuid>` cu UUID-ul tunelului dvs. și actualizați calea către fișierul de credențiale, dacă este necesar.

## Pasul 5: Rutarea traficului

Pentru a specifica serviciile interne pe care doriți să le serviți prin intermediul tunelului, urmați acești pași:

1. `Open the ` din nou.

2. Adăugați parametrii de intrare în fișier pentru a defini serviciile pe care doriți să le direcționați prin Cloudflare. De exemplu:

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

Înlocuiți `<your_tunnels_uuid>` cu UUID-ul tunelului dumneavoastră și actualizați numele de gazdă și detaliile serviciului în funcție de configurația dumneavoastră.

3. Salvați fișierul config.yml.


## Pasul 6: Crearea înregistrărilor DNS

Pentru a crea înregistrări DNS pentru numele de gazdă și serviciile tunelului, urmați acești pași:

1. Deschideți terminalul.

2. Utilizați următoarea comandă pentru a crea o înregistrare DNS:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> <hostname>
```
Înlocuiți `<UUID or NAME of tunnel>` cu UUID sau numele tunelului dvs. și `<hostname>` cu numele de gazdă dorit pentru serviciul dumneavoastră.

3. De exemplu, pentru a crea o înregistrare DNS pentru example.com, executați comanda:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> example.com
```

Vă rugăm să rețineți că modificările se vor reflecta în secțiunea DNS din tabloul de bord Cloudflare.

## Pasul 7: Pornirea tunelului

Pentru a testa și a porni tunelul Cloudflare, urmați acești pași:

1. Deschideți terminalul.

2. Rulați următoarea comandă pentru a porni tunelul:

```shell
cloudflared tunnel run <UUID or NAME of tunnel>
```

Înlocuiți `<UUID or NAME of tunnel>` cu UUID sau numele tunelului dumneavoastră.

3. Cloudflared va configura acum tunelul dvs. și va afișa informații despre starea acestuia. Odată ce tunelul este instalat și funcționează cu succes, puteți trece la pasul următor.

4. Pentru a împiedica închiderea tunelului atunci când ieșiți din terminal, trebuie să rulați Cloudflared ca serviciu systemd. Utilizați următoarea comandă:

```shell
cloudflared --config /path/to/config.yml service install
```

Înlocuiți `/path/to/config.yml` cu calea de acces la fișierul `config.yml` dosar.

## Concluzie

În acest ghid, am acoperit pașii pentru a configura Cloudflare Tunnels pe Ubuntu. Urmând aceste instrucțiuni, puteți îmbunătăți securitatea și performanța site-ului dvs. web prin utilizarea rețelei Cloudflare. Nu uitați să monitorizați în mod regulat tunelurile și să ajustați configurația după cum este necesar.

Dacă întâmpinați probleme sau dacă aveți nevoie de asistență suplimentară, consultați pagina [official Cloudflare Tunnels documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)


## Referințe
- [Cloudflare Tunnels Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)
- [Cloudflare Tunnels GitHub Repository](https://github.com/cloudflare/cloudflared)
- [tcude - How to Set Up Cloudflare Tunnels on Ubuntu](https://tcude.net/creating-cloudflare-tunnels-on-ubuntu/)
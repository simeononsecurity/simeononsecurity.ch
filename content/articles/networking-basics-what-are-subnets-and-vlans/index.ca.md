---
title: "Conceptes bàsics de xarxes: subxarxes, divisió en subxarxes i disseny de VLAN"
draft: false
toc: true
date: 2023-07-23
lastmod: 2026-11-13
description: "Aprèn els conceptes bàsics de subxarxes i VLAN per gestionar les xarxes amb eficiència i més seguretat."
genre: ["Conceptes bàsics de xarxes", "Divisió en subxarxes", "VLAN", "Gestió de xarxes", "Seguretat de xarxes", "Adreçament IP", "Segmentació de xarxa", "Ús eficient dels recursos", "Rendiment de xarxa", "IPv4"]
tags: ["conceptes bàsics de xarxes", "subxarxes", "divisió en subxarxes", "VLAN", "gestió de xarxes", "seguretat de xarxes", "adreçament IP", "segmentació de xarxa", "ús eficient dels recursos", "rendiment de xarxa", "IPv4", "configuració de subxarxes", "màscares de subxarxa", "assignació d’adreces IP", "comunicació entre VLAN", "ports del commutador", "configuració VLAN", "interfícies VLAN", "connectivitat de xarxa", "xarxes subdividides", "dominis de difusió", "mesures de seguretat", "rang d’adreces IP", "exemples de subxarxes", "desplegament VLAN", "administració de xarxa", "configuració de commutador", "configuració d’encaminador", "escalabilitat de xarxa", "comunicació i transferència de dades", "xarxes eficients"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_comp.webp"
coverAlt: "Il·lustració simbòlica de xarxes d’ordinadors connectades amb subxarxes i VLAN"
coverCaption: "Xarxes eficients: subxarxes i VLAN explicades de manera senzilla."
---

## Conceptes bàsics de xarxes: subxarxes, divisió en subxarxes i disseny de VLAN

### Introducció

En el món connectat actual, les xarxes informàtiques són essencials per a la comunicació i la transferència de dades. Els conceptes bàsics de xarxes són útils per als professionals de TI i per als usuaris. Aquest article explica les subxarxes, la divisió en subxarxes i les VLAN, així com el seu propòsit i funcionament.

## Subxarxes: una explicació detallada

### Què és una subxarxa?

{{< youtube id="nR5xCmXJE5E" >}}

Una **subxarxa** és una subdivisió lògica d’una xarxa IP. Permet a l’administrador dividir una xarxa gran en segments més petits i fàcils de gestionar. Cada subxarxa té un rang d’adreces IP propi, fet que ajuda a aprofitar millor les adreces disponibles.

### Per què fer servir subxarxes?

Les xarxes informàtiques fan servir subxarxes per diversos motius:

1. **Segmentació de xarxa:** Les subxarxes divideixen una xarxa gran en xarxes més petites. Això millora el rendiment i redueix la congestió.

2. **Més seguretat:** Separar els dispositius en subxarxes diferents permet aplicar tallafocs i llistes de control d’accés per gestionar el trànsit.

3. **Ús eficient dels recursos:** La divisió en subxarxes ajuda a assignar millor les adreces IP, un recurs limitat en IPv4.

### Com crear subxarxes?

{{< youtube id="LdSAaSHfK3M" >}}

La divisió en subxarxes divideix una xarxa en subxarxes més petites. Segueix aquests passos:

1. **Determina els requisits de xarxa:** Calcula quantes subxarxes i quants hosts necessites a cadascuna.

2. **Tria un esquema d’adreçament IP:** Selecciona un esquema adequat als hosts i subxarxes necessaris.

3. **Calcula les màscares de subxarxa:** Determina les màscares segons els requisits de subxarxes i hosts.

4. **Assigna les adreces IP:** Assigna adreces a cada subxarxa i comprova que siguin del rang correcte.

5. **Prova i verifica:** Comprova la connectivitat i l’assignació d’adreces IP.

### Exemples de divisió en subxarxes

Considerem un exemple senzill de divisió en subxarxes:

Suposem que tenim el rang IP 192.168.0.0/24 i volem crear quatre subxarxes amb el mateix nombre de hosts. Podem dividir la xarxa així:

1. **Pas 1: Determina els requisits de xarxa:** Necessitem quatre subxarxes amb el mateix nombre de hosts.

2. **Pas 2: Tria un esquema d’adreçament IP:** Triem una màscara /26, que permet 64 adreces per subxarxa.

3. **Pas 3: Calcula les màscares de subxarxa:** La màscara /26 és 255.255.255.192.

4. **Pas 4: Assigna les adreces IP:** Assignem aquestes adreces a les subxarxes:

   - subxarxa 1: 192.168.0.0/26
   - subxarxa 2: 192.168.0.64/26
   - subxarxa 3: 192.168.0.128/26
   - subxarxa 4: 192.168.0.192/26

5. **Pas 5: Prova i verifica:** Comprovem la connectivitat entre els dispositius de cada subxarxa.

### Taules útils de divisió en subxarxes

#### Taula de referència per calcular subxarxes

| Màscara de subxarxa | Notació CIDR | Adreces IP totals | Adreces IP utilitzables |
|-------------|---------------|--------------------|---------------------|
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1,024 | 1,022 |
| /21 | 255.255.248.0 | 2,048 | 2,046 |
| /20 | 255.255.240.0 | 4,096 | 4,094 |
| /19 | 255.255.224.0 | 8,192 | 8,190 |
| /18 | 255.255.192.0 | 16,384 | 16,382 |
| /17 | 255.255.128.0 | 32,768 | 32,766 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /15 | 255.254.0.0 | 131,072 | 131,070 |
| /14 | 255.252.0.0 | 262,144 | 262,142 |
| /13 | 255.248.0.0 | 524,288 | 524,286 |
| /12 | 255.240.0.0 | 1,048,576 | 1,048,574 |
| /11 | 255.224.0.0 | 2,097,152 | 2,097,150 |
| /10 | 255.192.0.0 | 4,194,304 | 4,194,302 |
| /9 | 255.128.0.0 | 8,388,608 | 8,388,606 |
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
| /7 | 254.0.0.0 | 33,554,432 | 33,554,430 |
| /6 | 252.0.0.0 | 67,108,864 | 67,108,862 |
| /5 | 248.0.0.0 | 134,217,728 | 134,217,726 |
| /4 | 240.0.0.0 | 268,435,456 | 268,435,454 |
| /3 | 224.0.0.0 | 536,870,912 | 536,870,910 |
| /2 | 192.0.0.0 | 1,073,741,824 | 1,073,741,822 |
| /1 | 128.0.0.0 | 2,147,483,648 | 2,147,483,646 |
| /0 | 0.0.0.0 | 4,294,967,296 | 4,294,967,294 |

#### Taula de subxarxes utilitzables

| Notació CIDR | Nombre de subxarxes utilitzables |
|---------------|-------------------------|
| /0 | 1 |
| /1 | 2 |
| /2 | 4 |
| /3 | 8 |
| /4 | 16 |
| /5 | 32 |
| /6 | 64 |
| /7 | 128 |
| /8 | 256 |
| /9 | 512 |
| /10 | 1024 |
| /11 | 2048 |
| /12 | 4096 |
| /13 | 8192 |
| /14 | 16384 |
| /15 | 32768 |
| /16 | 65536 |
| /17 | 131072 |
| /18 | 262144 |
| /19 | 524288 |
| /20 | 1048576 |
| /21 | 2097152 |
| /22 | 4194304 |
| /23 | 8388608 |
| /24 | 16777216 |
| /25 | 33554432 |
| /26 | 67108864 |
| /27 | 134217728 |
| /28 | 268435456 |
| /29 | 536870912 |
| /30 | 1073741824 |
| /31 | 2147483648 |
| /32 | 4294967296 |

#### Taula de potències de dos

| Potència de dos | Valor |
|--------------|-------|
| 2^32 | 4294967296 |
| 2^31 | 2147483648 |
| 2^30 | 1073741824 |
| 2^29 | 536870912 |
| 2^28 | 268435456 |
| 2^27 | 134217728 |
| 2^26 | 67108864 |
| 2^25 | 33554432 |
| 2^24 | 16777216 |
| 2^23 | 8388608 |
| 2^22 | 4194304 |
| 2^21 | 2097152 |
| 2^20 | 1048576 |
| 2^19 | 524288 |
| 2^18 | 262144 |
| 2^17 | 131072 |
| 2^16 | 65536 |
| 2^15 | 32768 |
| 2^14 | 16384 |
| 2^13 | 8192 |
| 2^12 | 4096 |
| 2^11 | 2048 |
| 2^10 | 1024 |
| 2^9 | 512 |
| 2^8 | 256 |
| 2^7 | 128 |
| 2^6 | 64 |
| 2^5 | 32 |
| 2^4 | 16 |
| 2^3 | 8 |
| 2^2 | 4 |
| 2^1 | 2 |
| 2^0 | 1 |

## VLAN: xarxes d’àrea local virtuals

### Què és una VLAN?

{{< youtube id="jC6MJTh9fRE" >}}

Una **VLAN (Virtual Local Area Network)** és un grup lògic de dispositius d’una xarxa, independentment de la seva ubicació física. Les VLAN creen dominis de difusió separats i milloren la flexibilitat, la seguretat i l’escalabilitat.

### Per què fer servir VLAN?

Les VLAN ofereixen diversos avantatges per gestionar xarxes:

1. **Més seguretat:** Les VLAN aïllen dades sensibles i limiten els accessos no autoritzats. El trànsit queda dins de segments concrets i protegeix els recursos importants.

2. **Millor rendiment:** Les VLAN separen lògicament el trànsit, redueixen la congestió i milloren el rendiment. El trànsit de difusió queda limitat a la VLAN.

3. **Gestió més senzilla:** Les VLAN agrupen dispositius per funció, departament o altres criteris, i simplifiquen l’administració i la configuració.

### Configuració de VLAN

Per configurar una VLAN, normalment se segueixen aquests passos:

1. **Identifica els requisits de VLAN:** Determina la finalitat i l’abast del desplegament. Identifica els dispositius i les VLAN on aniran.

2. **Assigna ID de VLAN:** Assigna un ID únic a cada VLAN. Normalment són números de l’1 al 4094, amb alguns valors reservats.

3. **Configura els ports del commutador:** Assigna els ports a les VLAN adequades com a ports d’accés o troncals.

4. **Configura les interfícies VLAN:** Si cal comunicar-se entre VLAN, [configura les interfícies VLAN](https://simeononsecurity.com/network-plus/ethernet-switching-vlans-port-configurations-security/) en un commutador de capa 3 o un encaminador.

5. **Prova i verifica:** Comprova la connectivitat entre els dispositius de cada VLAN.

### Taula de VLAN reservades

| Etiquetes VLAN | Descripció |
|-------------------|----------------------------------------------------|
| VLAN 0 | ID de VLAN reservat, no s’ha d’utilitzar |
| VLAN 1 | VLAN per defecte de molts dispositius de xarxa |
| VLAN 2 | VLAN per defecte per al trànsit de gestió |
| VLAN 3-4 | ID de VLAN reservats |
| VLAN 5 | Reservat per a l’ID VLAN Token Ring |
| VLAN 6-1001 | ID de VLAN reservats |
| VLAN 1002-1005 | VLAN per defecte que Cisco fa servir per a usos específics |
| VLAN 1006-1024 | ID de VLAN reservats |
| VLAN 1025-4094 | Reservat per al rang VLAN ampliat |
| VLAN 4095 | ID de VLAN reservat, no s’ha d’utilitzar |

## Conclusió

[Entendre les subxarxes](https://simeononsecurity.com/articles/networking-basics-what-is-a-switch-router-gateway-subnet-firewall-and-dmz/) i les VLAN és essencial per dissenyar i gestionar xarxes eficients. Les subxarxes segmenten la xarxa i milloren el rendiment i la seguretat. Les VLAN agrupen dispositius lògicament i faciliten la gestió. Seguint aquests passos, els administradors poden dividir les xarxes i configurar VLAN segons les necessitats.

Els conceptes bàsics de xarxes són la base per crear xarxes robustes i escalables que satisfacin les necessitats actuals de comunicació i transferència de dades.

## Referències

- [Conceptes bàsics de subnetting](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
- [Comprendre i configurar VLAN](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/12-2/25ew/configuration/guide/conf/vlans.pdf)
- [Estàndard IEEE 802.1Q](https://standards.ieee.org/standard/802_1Q-2018.html)

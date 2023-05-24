---
title: "Bypassare il BGW-320: utilizzo di un COTS ONT delle Azzorre: una guida dettagliata"
draft: false
toc: true
date: 2023-04-30
description: "Scopri come bypassare il BGW-320 e utilizzare un COTS ONT realizzato da Azores per connetterti alla rete del tuo ISP con questa guida facile da seguire."
tags: ["CULLE SOPRA", "BGW-320", "Azzorre", "fibra", "rete", "XGS-PON", "Ethernet", "passaggio IP", "personalizzazione", "ISP", "documento d'identità", "Indirizzo MAC", "ID dell'attrezzatura", "versione dell'immagine", "versione hardware", "telnet", "Applicazione CLI", "GUI web", "modalità di configurazione di fabbrica", "problemi di compatibilità"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "Un tecnico dei cartoni animati che tiene in mano un COTS ONT con un cavo in fibra sullo sfondo."
coverCaption: ""
---

## Come bypassare il BGW-320 e utilizzare un Azzorre WAG-D20

La maggior parte delle persone con fibra ha due modi per connettersi a Internet: fibra a un ONT, Ethernet a un gateway o fibra direttamente al gateway. In questo articolo, ci concentreremo su come bypassare il BGW-320 e utilizzare un COTS ONT prodotto da Azores.

### Aspetti tecnici

IL [Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### Accesso al dispositivo

L'indirizzo IP predefinito del dispositivo è 192.168.1.1 e il suo indirizzo Gateway ha un errore di battitura di fabbrica utilizzando un indirizzo IP pubblico, ovvero mostra 192.162.1.1 invece di 192.168.1.1.

Una volta avviato, è necessario premere invio per ottenere una richiesta di accesso sull'interfaccia seriale TTL (115200 8N1). Questo dispositivo ha un sistema di immagini A/B con una partizione sovrapposta che contiene tutti i file personalizzati.
 
### Credenziali

- `admin``ADMIN123!@#` - Accesso amministratore per la GUI Web
- `Guest``welcome` - Accesso ospite
- `test``default` - Login di fabbrica

### Interfaccia Ethernet

Collega il tuo client alla porta Ethernet 10G e configuralo con un indirizzo nella rete 192.168.1.x/24 come - 192.168.1.2/255.255.255.0.

Dopo aver eseguito una scansione delle porte da 1-65535, noterai alcune porte aperte:

- Porti `23` & `8009` - Telnet, richiede il login, esegue l'applicazione CLI.
- Porto `10002` - Sconosciuto
- Porto `80` - WebUI, solo due funzioni

### Personalizzazione dell'ONT

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

Ora arriva la parte importante, ovvero la modifica di alcune informazioni sul dispositivo per renderlo compatibile con la rete del tuo ISP.

Innanzitutto, prendi le seguenti informazioni dal tuo ISP Gateway o ONT:

1. **IDENTIFICATIVO**
2. **Indirizzo MAC**
3. **ID attrezzatura**
4. **Versione immagine**
5. **Versione hardware**

Nota: questi sono i valori OMCI e non quelli dell'interfaccia utente web.

Telnet al tuo ONT personale (telnet 192.168.1.1), accedi come **`test` usando il **`default` password ed eseguire il comando 'test' per passare alla modalità di configurazione di fabbrica.

Visualizza i valori attualmente impostati con il comando 'show':

- `show gpon mac`
- `show sn`
- `show equipment id`

Al termine, personalizza le impostazioni con i seguenti comandi sostituendo x con i valori del tuo dispositivo:

- `set gpon mac xx:xx:xx:xx:xx:xx`
- `set sn <insert ONT ID here>`

Per HUMMAX:

- `set equipment id “iONT320500G”`
- `config ONU-G_Version "BGW320-500_2.1”`

PerNokia:

- `set equipment id “iONT320505G”`
- `config ONU-G_Version "BGW320-505_2.2”`

Nota: gli ultimi due comandi devono essere applicati da telnet connesso come **`test` utente.

### Riavvia e goditi il vero passthrough IP

Dopo la personalizzazione, riavvia l'ONT e goditi il vero passthrough IP.

### Risoluzione dei problemi e passaggi aggiuntivi
Per ulteriori informazioni su questo argomento, consultare il [8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### Conclusione

Seguendo questi passaggi è possibile bypassare con successo il BGW-320 e utilizzare COTS ONT realizzato da Azores per connettersi alla rete del proprio ISP. Tuttavia, fai attenzione mentre inserisci i comandi e assicurati di sostituire correttamente 'x' con i valori del tuo dispositivo, altrimenti potresti riscontrare problemi di compatibilità che potrebbero causare errori di connessione.



---
title: "Bypassare il BGW-320: Utilizzo di un ONT COTS Azores - Guida passo per passo"
draft: false
toc: true
date: 2023-04-30
description: "Imparate a bypassare il BGW-320 e a utilizzare un ONT COTS di Azores per connettervi alla rete del vostro ISP con questa guida facile da seguire."
tags: ["COTS ONT", "BGW-320", "Azzorre", "fibra", "rete", "XGS-PON", "Ethernet", "Passaggio IP", "personalizzazione", "ISP", "avere un ID", "Indirizzo MAC", "ID attrezzatura", "versione immagine", "hardware version", "telnet", "Applicazione CLI", "web GUI", "modalità di configurazione di fabbrica", "problemi di compatibilità"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "Un tecnico dei cartoni animati che tiene in mano un ONT COTS con un cavo in fibra sullo sfondo."
coverCaption: ""
---

## Come bypassare il BGW-320 e utilizzare un Azores WAG-D20

La maggior parte delle persone che dispongono della fibra ottica hanno due modi per connettersi a Internet: la fibra a un ONT, l'Ethernet a un gateway o la fibra direttamente al gateway. In questo articolo ci concentreremo su come bypassare il BGW-320 e utilizzare un ONT COTS di Azores.

### Aspetti tecnici

Il[Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### Accesso al dispositivo

L'indirizzo IP predefinito del dispositivo è 192.168.1.1 e il suo indirizzo gateway presenta un errore di fabbrica che utilizza un indirizzo IP pubblico, ovvero indica 192.162.1.1 invece di 192.168.1.1.

Una volta avviato, è necessario premere invio per ottenere un prompt di login sull'interfaccia seriale TTL (115200 8N1). Questo dispositivo ha un sistema di immagini A/B con una partizione di overlay che contiene i file personalizzati.
 
### Credenziali

-`admin``ADMIN123!@#` - Accesso amministratore per la GUI web
-`Guest``welcome` - Accesso ospite
-`test``default` - Accesso alla fabbrica

### Interfaccia Ethernet

Collegare il client alla porta Ethernet 10G e configurarlo con un indirizzo della rete 192.168.1.x/24 come 192.168.1.2/255.255.255.0.

Eseguendo una scansione delle porte da 1-65535, si noteranno alcune porte aperte:

- Porte`23` &`8009` - Telnet, richiede il login, esegue l'applicazione CLI.
- Porta`10002` - Sconosciuto
- Porto`80` - WebUI, solo due funzioni

### Personalizzazione dell'ONT

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

Ora viene la parte importante, ovvero la modifica di alcune informazioni sul dispositivo per renderlo compatibile con la rete del vostro ISP.

Per prima cosa, prendete le seguenti informazioni dal gateway o dall'ONT del vostro ISP:

1. **ID ONT**
2. **Indirizzo MAC**
3. **ID apparecchiatura**
4. **Versione immagine**
5. **Versione hardware**

Nota: questi sono i valori OMCI e non quelli dell'interfaccia web.

Collegarsi al proprio ONT personale (telnet 192.168.1.1), effettuare il login come **`test` utilizzando il **`default` ed eseguire il comando "test" per passare alla modalità di configurazione di fabbrica.

Visualizzare i valori attualmente impostati con il comando "show":

-`show gpon mac`
-`show sn`
-`show equipment id`

Una volta fatto, personalizzare le impostazioni con i seguenti comandi, sostituendo la x con i valori del dispositivo:

-`set gpon mac xx:xx:xx:xx:xx:xx`
-`set sn <insert ONT ID here>`

Per HUMAX:

-`set equipment id “iONT320500G”`
-`config ONU-G_Version "BGW320-500_2.1”`

Per Nokia:

-`set equipment id “iONT320505G”`
-`config ONU-G_Version "BGW320-505_2.2”`

Nota: gli ultimi due comandi devono essere applicati da telnet con accesso come **`test` utente.

### Riavviare e godere del vero IP Passthrough

Dopo la personalizzazione, riavviare l'ONT e godersi il vero IP passthrough.

### Risoluzione dei problemi e passi aggiuntivi
Per ulteriori informazioni su questo argomento, consultare la sezione[8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### Conclusione

Seguendo questi passaggi è possibile bypassare con successo il BGW-320 e utilizzare l'ONT COTS prodotto da Azores per connettersi alla rete del proprio ISP. Tuttavia, fate attenzione durante l'inserimento dei comandi e assicuratevi di sostituire correttamente le 'x' con i valori del vostro dispositivo, altrimenti potreste incorrere in problemi di compatibilità che potrebbero causare problemi di connessione.



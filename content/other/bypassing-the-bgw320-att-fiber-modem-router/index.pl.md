---
title: "Obejście BGW-320: Użycie Azores COTS ONT - przewodnik krok po kroku"
draft: false
toc: true
date: 2023-04-30
description: "Dowiedz się, jak obejść BGW-320 i użyć COTS ONT firmy Azores, aby połączyć się z siecią ISP za pomocą tego łatwego do wykonania przewodnika."
tags: ["COTS ONT", "BGW-320", "Azory", "włókno", "sieć", "XGS-PON", "Ethernet", "Przełączanie IP", "dostosowanie", "ISP", "mieć identyfikator", "Adres MAC", "identyfikator sprzętu", "wersja obrazu", "wersja sprzętowa", "telnet", "Aplikacja CLI", "internetowy GUI", "tryb konfiguracji fabrycznej", "kwestie kompatybilności"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "Karykatura technika trzymającego COTS ONT z kablem światłowodowym w tle."
coverCaption: ""
---

## Jak ominąć BGW-320 i użyć Azores WAG-D20

Większość ludzi posiadających światłowód ma dwa sposoby na podłączenie się do internetu - światłowód do ONT, Ethernet do bramy lub światłowód bezpośrednio do bramy. W tym artykule skupimy się na tym, jak ominąć BGW-320 i użyć COTS ONT firmy Azores.

### Aspekty techniczne

Strona[Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### Dostęp do urządzenia

Domyślny adres IP urządzenia to 192.168.1.1, a jego adres Gateway ma fabryczną literówkę z użyciem publicznego adresu IP tj. pokazuje 192.162.1.1 zamiast 192.168.1.1.

Po uruchomieniu trzeba nacisnąć enter, aby uzyskać monit o zalogowanie na interfejsie szeregowym TTL (115200 8N1). Urządzenie posiada system obrazów A/B z partycją nakładkową, na której znajdują się dowolne pliki dostosowane do potrzeb użytkownika.
 
### Credentials

-`admin``ADMIN123!@#` - Login administratora dla GUI sieciowego
-`Guest``welcome` - Login gościa.
-`test``default` - Login fabryczny

### Interfejs Ethernet

Podłącz klienta do portu ethernet 10G i skonfiguruj go z adresem w sieci 192.168.1.x/24 jak - 192.168.1.2/255.255.255.0.

Po uruchomieniu skanowania portów od 1-65535, zauważysz kilka otwartych portów:

- Porty`23` &`8009` - Telnet, wymaga logowania, uruchamia aplikację CLI.
- Port`10002` - Nieznany
- Port`80` - WebUI, tylko dwie funkcje

### Dostosowywanie ONT

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

Teraz następuje ważna część, czyli zmiana niektórych informacji o urządzeniu, aby było ono kompatybilne z siecią dostawcy usług internetowych.

Najpierw należy pobrać poniższe informacje z bramy lub urządzenia ONT operatora ISP:

1. **ONT ID**
2. **Adres MAC**
3. **Equipment ID**
4. **Wersja obrazu**.
5. **Wersja sprzętowa**.

Uwaga: To są wartości OMCI, a nie te z web UI.

Telnet do twojego osobistego ONT (telnet 192.168.1.1), zaloguj się jako **.`test` przy użyciu **.`default` hasło i uruchomić polecenie 'test', aby przejść do trybu konfiguracji fabrycznej.

Wyświetlić aktualnie ustawione wartości za pomocą polecenia 'show':

-`show gpon mac`
-`show sn`
-`show equipment id`

Po zakończeniu dostosuj ustawienia za pomocą następujących poleceń, zastępując x wartościami urządzenia:

-`set gpon mac xx:xx:xx:xx:xx:xx`
-`set sn <insert ONT ID here>`

Dla HUMAX:

-`set equipment id “iONT320500G”`
-`config ONU-G_Version "BGW320-500_2.1”`

Dla Nokii:

-`set equipment id “iONT320505G”`
-`config ONU-G_Version "BGW320-505_2.2”`

Uwaga: Ostatnie dwa polecenia należy wykonać z telnetu zalogowanego jako **.`test` użytkownik.

### Uruchom ponownie komputer i ciesz się prawdziwym IP Passthrough

Po dostosowaniu, zrestartuj ONT i ciesz się prawdziwym IP Passthrough.

### Rozwiązywanie problemów i dodatkowe kroki
Więcej informacji na ten temat można znaleźć na stronie[8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### Wniosek

Wykonując powyższe kroki można z powodzeniem obejść BGW-320 i użyć COTS ONT wykonanego przez Azores do połączenia się z siecią ISP. Jednakże, należy być ostrożnym podczas wprowadzania komend i upewnić się, że zastąpiono 'x' wartościami urządzenia poprawnie, w przeciwnym razie, możesz napotkać problemy z kompatybilnością, co może skutkować niepowodzeniem połączenia.



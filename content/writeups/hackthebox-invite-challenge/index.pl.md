---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "Dowiedz się, jak wygenerować kod zaproszenia i dołączyć do platformy online HackTheBox, aby przetestować i rozwinąć swoje umiejętności w zakresie testów penetracyjnych i cyberbezpieczeństwa w systemach Windows i Linux."
tags: ["HackTheBox", "Zaproś do wyzwania", "Testy penetracyjne", "Cyberbezpieczeństwo", "Windows", "Linux", "Platforma internetowa", "HTTP POST", "Kod zaproszenia", "Kodowanie Base64", "Powershell", "Linux Bash", "Dekodowanie Base64", "Generowanie kodu zaproszenia", "Programowanie", "Tworzenie stron internetowych", "Technologia", "Bezpieczeństwo IT", "Szkolenie IT"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "Kreskówkowy ekran komputera przedstawiający stronę internetową HackTheBox z drzwiami skarbca otwieranymi kluczem, odsłaniającymi trofeum lub medal, na tle miejskiego krajobrazu w kolorystyce logo HackTheBox (niebiesko-białej)."
coverCaption: ""
---
 Instrukcje krok po kroku dotyczące ukończenia wyzwania z zaproszeniem HackTheBox w systemie Windows lub Linux. Dowiedz się, jak wygenerować kod zaproszenia i dołączyć do platformy online, aby przetestować i rozwinąć swoje umiejętności w zakresie testów penetracyjnych i cyberbezpieczeństwa. Artykuł przedstawia zarówno proste, jak i zaawansowane rozwiązania, ułatwiając użytkownikom na wszystkich poziomach ukończenie wyzwania i uzyskanie dostępu do platformy.

______

## Co to jest Hack the Box?

HackTheBox to platforma internetowa do testowania i rozwijania umiejętności w zakresie testów penetracyjnych i cyberbezpieczeństwa.

## Jak dołączyć do Hack the box ?

Aby utworzyć konto na HackTheBox (HTB), musisz ukończyć wyzwanie zaproszenia lub zhakować sobie drogę. Nie martw się jednak, nie jest to trudne, a ten artykuł pomoże ci nie ukończyć wyzwania.

Najpierw przejdź do strony [HackTheBox Website](https://hackthebox.eu) i kliknij przycisk dołączania.

Pojawi się okno z wyraźną prośbą o podanie kodu zaproszenia.

Wyraźnie widać pole tekstowe z prośbą o podanie kodu zaproszenia.

Naciśnij ***"F12"*** na klawiaturze lub ***"Ctrl + Shift + I "***, aby otworzyć narzędzia programistyczne przeglądarki.

Na karcie "Elementy" znajdziesz skrypt **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

Przeglądając javascript i funkcję makeInviteCode, odkryjesz, że musisz wysłać **HTTP POST** do **/api/invite/generate**, aby otrzymać kod zaproszenia.

Możesz wykonać następujące czynności, aby uzyskać kod zaproszenia zakodowany w Base64:

### Rozwiązanie:

#### Proste:
- **Windows**: ```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" ```

Co wygeneruje następującą zawartość: ```json {"success":1,"data":{"code":"Tk9ULVRIRS1GTEFHLVlPVSdSRS1MT09LSU5HLUZPUg==","format":"encoded"},"0":200} ```

Jeśli weźmiesz zakodowany kod zaproszenia do [base64decode.org](https://www.base64decode.org/) otrzymasz kod zaproszenia!

#### Advanced (natychmiast wydrukuj kod zaproszenia):
 - **Windows**: ```powershell $base64api=((Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON).Data).Code ; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($base64api)) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" | jq -r '.data.code' | base64 -d ```
 - Uwaga**: Będziesz musiał zainstalować [jq](https://stedolan.github.io/jq/download/) pakiet.

______

### Kod zaproszenia Ex:
```XXXXX-XXXXX-XXXXX-XXXXX-XXXXX```



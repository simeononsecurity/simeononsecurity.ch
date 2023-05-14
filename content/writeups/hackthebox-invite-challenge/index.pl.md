---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "Dowiedz się, jak wygenerować kod zaproszenia i dołączyć do platformy online HackTheBox, aby sprawdzić i rozwinąć swoje umiejętności w zakresie testów penetracyjnych i cyberbezpieczeństwa zarówno w systemie Windows, jak i Linux."
tags: ["HackTheBox", "Zaproś wyzwanie", "Testy penetracyjne", "Cybersecurity", "Windows", "Linux", "Platforma internetowa", "HTTP POST", "Kod zaproszenia", "Zakodowany w Base64", "Powershell", "Linux Bash", "Dekodowanie Base64", "Zaproś do generowania kodu", "Programowanie", "Rozwój stron internetowych", "Technologia", "Bezpieczeństwo IT", "Szkolenie IT"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "Komiksowy ekran komputera przedstawiający stronę internetową HackTheBox z drzwiami skarbca odblokowywanymi kluczem, odsłaniającymi trofeum lub medal, z tłem w postaci pejzażu miejskiego w kolorystyce logo HackTheBox (niebieski i biały)."
coverCaption: ""
---
 instrukcje krok po kroku, aby ukończyć wyzwanie zaproszenia HackTheBox w systemie Windows lub Linux. Dowiedz się, jak wygenerować kod zaproszenia i dołączyć do platformy online, aby sprawdzić i rozwinąć swoje umiejętności w zakresie testów penetracyjnych i cyberbezpieczeństwa. Artykuł prezentuje zarówno proste, jak i zaawansowane rozwiązania, ułatwiając użytkownikom na każdym poziomie ukończenie wyzwania i uzyskanie dostępu do platformy.

______

## Czym jest Hack the Box ?

HackTheBox to platforma online, która pozwala sprawdzić i rozwinąć swoje umiejętności w zakresie testów penetracyjnych i cyberbezpieczeństwa.

## How do you join Hack the box ?

Aby założyć konto na HackTheBox (HTB) musisz ukończyć wyzwanie zaproszenia, lub zhakować sobie drogę. Nie martw się jednak to nie jest trudne i ten artykuł pomoże Ci w ukończeniu wyzwania.

Po pierwsze, przejdź do[HackTheBox Website](https://hackthebox.eu) i kliknij na przycisk dołącz.

Pojawi się okienko z wyraźną prośbą o podanie kodu zapraszającego.

Wyraźnie widać pole tekstowe z prośbą o podanie kodu zaproszenia.

Naciśnij albo ***"F12"*** na klawiaturze lub ***"Ctrl + Shift + I "***, aby otworzyć narzędzia deweloperskie przeglądarki.

Na karcie "Elementy", znajdziesz skrypt **.[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

Przeglądając javascript i funkcję makeInviteCode, odkryjesz, że musisz wysłać **HTTP POST** do **/api/invite/generate**, aby uzyskać kod zaproszenia.

Możesz wykonać następujące czynności, aby uzyskać kod zaproszenia zakodowany w Base64:

### Rozwiązanie:

#### Proste:
- **Windows**:```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" ```

Which will generate the following content: ```json {"success":1,"data":{"code":"Tk9ULVRIRS1GTEFHLVlPVSdSRS1MT09LSU5HLUZPUg==","format":"encoded"},"0":200} ```

If you take the encoded invite code to [base64decode.org](https://www.base64decode.org/), you'll get your invite code!

#### Advanced (Instantly print out invite code):
 - **Windows**: ```powershell $base64api=((Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON).Data).Code ; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($base64api)) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" | jq -r '.data.code' | base64 -d ```
 - **Note**: You'll need to install the [jq](https://stedolan.github.io/jq/download/) package.

______

### Invite Code Ex:
```XXXXX-XXXXX-XXXXX-XXXXX-XXXXX```



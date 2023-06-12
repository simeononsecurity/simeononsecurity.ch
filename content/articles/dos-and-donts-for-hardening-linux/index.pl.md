---
title: "Podstawowe zasady i zalecenia dotyczące wzmacniania systemu Linux"
date: 2023-02-28
toc: true
draft: false
description: "Zapoznaj się z podstawowymi zaleceniami i zaleceniami dotyczącymi zabezpieczania systemu Linux, w tym aktualizacji, korzystania z zapór ogniowych, włączania SELinux lub AppArmor, konfigurowania zasad haseł i monitorowania dzienników systemowych."
tags: ["Bezpieczeństwo systemu Linux", "utwardzanie systemu", "firewall", "SELinux", "AppArmor", "polityka haseł", "aktualizacje systemu", "logi systemowe", "moduły bezpieczeństwa", "zasady kontroli dostępu", "cyberbezpieczeństwo", "bezpieczeństwo systemu", "bezpieczeństwo sieci", "zarządzanie podatnościami", "najlepsze praktyki bezpieczeństwa", "Bezpieczeństwo IT", "bezpieczeństwo informacji", "aktualizacje oprogramowania", "dostęp roota", "menedżer haseł"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "Kreskówkowy zamek trzymający tarczę z napisem Linux, podczas gdy strzała odbija się od tarczy."
coverCaption: ""
---


Linux to popularny system operacyjny używany zarówno przez użytkowników indywidualnych, jak i firmy. Chociaż często jest uważany za bezpieczniejszy niż inne systemy operacyjne ze względu na swój charakter open source, nadal wymaga odpowiedniego zabezpieczenia, aby zapewnić bezpieczeństwo systemu i przechowywanych w nim danych. W tym artykule omówimy kilka ogólnych zaleceń i zakazów dotyczących hartowania, które mogą pomóc w zapewnieniu bezpieczeństwa systemu Linux.

## Do's:

### Aktualizuj swój system

Utrzymywanie [Linux](https://simeononsecurity.ch/articles/how-do-i-learn-linux/) Aktualizowanie systemu ma kluczowe znaczenie dla utrzymania jego bezpieczeństwa. Regularne aktualizacje pomagają naprawić luki w zabezpieczeniach i błędy, zapewniając, że system pozostaje bezpieczny przed potencjalnymi atakami. Oto kilka przykładów, jak zaktualizować system Linux za pomocą menedżera pakietów **apt-get** lub **yum**:

#### Aktualizacja Ubuntu za pomocą apt-get

Aby zaktualizować system Ubuntu za pomocą **apt-get**, otwórz okno terminala i wpisz:
```bash
sudo apt-get update
```

Spowoduje to pobranie najnowszych list pakietów z repozytoriów pakietów Ubuntu. Po zakończeniu tego polecenia można zainstalować wszystkie dostępne aktualizacje za pomocą następującego polecenia:

```bash
sudo apt-get upgrade

```

Spowoduje to pobranie i zainstalowanie wszelkich dostępnych aktualizacji systemu.

### Aktualizacja CentOS przy użyciu yum

Aby zaktualizować system CentOS za pomocą **yum**, otwórz okno terminala i wpisz:

```bash
sudo yum update
```

Spowoduje to pobranie i zainstalowanie wszelkich dostępnych aktualizacji dla systemu. Możesz także użyć następującego polecenia, aby wyczyścić stare lub nieużywane pakiety:

```bash
sudo yum autoremove
```

Spowoduje to usunięcie wszystkich pakietów, które nie są już potrzebne w systemie.

Pamiętaj, aby regularnie sprawdzać i instalować aktualizacje w swoim systemie Linux, aby zapewnić jego bezpieczeństwo i stabilność.


### Używaj zapory sieciowej

Zapora sieciowa jest niezbędnym środkiem bezpieczeństwa dla każdego systemu Linux, ponieważ pomaga chronić przed nieautoryzowanym dostępem i innymi zagrożeniami cybernetycznymi. Oto jak używać zapory **ufw** w systemie Linux:

#### Instalowanie i włączanie ufw dla systemów opartych na Ubuntu

Aby zainstalować i włączyć **ufw**, otwórz okno terminala i wpisz:

```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```

Aby zezwolić na przychodzący ruch HTTP (port 80):

```bash
sudo ufw allow http
```

Aby zablokować ruch przychodzący z określonego adresu IP:

```bash
sudo ufw deny from <ip_address>
```

Aby usunąć regułę:
```bash
sudo ufw delete <rule_number>
```

Bieżące reguły **ufw** można wyświetlić wpisując:

```bash
sudo ufw status
```


Spowoduje to wyświetlenie bieżących reguł i ich statusu.

Pamiętaj, aby regularnie przeglądać i aktualizować reguły **ufw**, aby zapewnić ochronę systemu przed potencjalnymi zagrożeniami.


#### Instalowanie i włączanie firewalld dla systemów opartych na CentOS

Aby zainstalować i włączyć domyślną zaporę sieciową w systemie CentOS, którą jest **firewalld**, można użyć następujących poleceń:

```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

Spowoduje to zainstalowanie **firewalld** i włączenie go w systemie.

#### Konfigurowanie reguł firewalld dla systemów opartych na CentOS

Po włączeniu **firewalld** można skonfigurować jego reguły, aby zezwalać lub blokować ruch przychodzący i wychodzący. Oto kilka przykładów:

Aby zezwolić na przychodzący ruch SSH (port 22):

```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

Aby zezwolić na przychodzący ruch HTTP (port 80):

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

Aby zablokować ruch przychodzący z określonego adresu IP:

```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```

Aby usunąć regułę:

```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```

Bieżące reguły **firewalld** można wyświetlić wpisując:

```bash
sudo firewall-cmd --list-all
```

Spowoduje to wyświetlenie bieżących reguł i ich statusu.

Pamiętaj, aby regularnie przeglądać i aktualizować reguły **firewalld**, aby upewnić się, że system

### Włącz SELinux lub AppArmor

SELinux (Security-Enhanced Linux) i AppArmor to dwa moduły bezpieczeństwa, które mogą być używane do egzekwowania obowiązkowych zasad kontroli dostępu w systemach Linux. Domyślnie większość nowoczesnych dystrybucji Linuksa ma zainstalowane SELinux lub AppArmor, które można włączyć i skonfigurować w celu zwiększenia bezpieczeństwa systemu.

#### Włączanie SELinux dla systemów opartych na CentOS

Aby sprawdzić, czy SELinux jest włączony w systemie, uruchom następujące polecenie:

```bash
sestatus
```

Jeśli SELinux nie jest zainstalowany, można go zainstalować za pomocą następującego polecenia:

```bash
sudo yum install selinux-policy selinux-policy-targeted
```

Aby włączyć SELinux, należy edytować plik **/etc/selinux/config** i ustawić zmienną **SELINUX** na **enforcing**:

```bash
sudo nano /etc/selinux/config
```
**Zmień SELINUX=wymuszanie**
```
SELINUX=enforcing
```

Zapisz i zamknij plik, używając kombinacji klawiszy CTRL+X i Y, a następnie Enter, po czym uruchom ponownie system.

#### Włączanie AppArmor dla systemów opartych na Ubuntu

Aby sprawdzić, czy AppArmor jest włączony w systemie, uruchom następujące polecenie:
```bash
sudo apparmor_status
```


Jeśli AppArmor nie jest zainstalowany, można go zainstalować za pomocą następującego polecenia:
```bash
sudo apt-get install apparmor
```

Aby włączyć AppArmor, należy edytować plik **/etc/default/grub** i dodać parametr **security=apparmor** do zmiennej **GRUB_CMDLINE_LINUX**:

```bash
sudo nano /etc/default/grub
```
**Dodaj zabezpieczenie=pancerz**
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```

Zapisz i zamknij plik, używając CTRL + X i Y, a następnie wprowadź, a następnie uruchom następujące polecenie, aby zaktualizować konfigurację bootloadera systemu:

```bash
sudo update-grub
```

Na koniec uruchom ponownie system.

Po włączeniu SELinux lub AppArmor można skonfigurować ich zasady, aby ograniczyć uprawnienia procesów i ograniczyć ich dostęp do zasobów systemowych. Może to pomóc zminimalizować potencjalny wpływ udanego ataku i zwiększyć ogólne bezpieczeństwo systemu.


### Konfiguracja zasad dotyczących haseł

Konfigurowanie zasad dotyczących haseł jest ważnym krokiem w zwiększaniu bezpieczeństwa systemu Linux. Egzekwując silne wymagania dotyczące haseł, można zapewnić, że konta użytkowników są bezpieczne i chronione przed potencjalnymi atakami. Oto jak skonfigurować zasady haseł w systemie Linux:

#### Konfigurowanie zasad haseł w Ubuntu

Aby skonfigurować zasady dotyczące haseł w systemie Ubuntu, można użyć modułu **pam_pwquality**. Moduł ten zapewnia zestaw kontroli siły haseł, które mogą być wykorzystane do egzekwowania zasad dotyczących haseł. Aby zainstalować moduł **pam_pwquality**, otwórz okno terminala i wpisz:

```bash
sudo apt-get install libpam-pwquality
```

Po zainstalowaniu modułu można skonfigurować jego ustawienia, edytując plik **/etc/pam.d/common-password**. Na przykład, aby wymusić minimalną długość hasła wynoszącą 8 znaków i wymagać co najmniej jednej wielkiej litery, jednej małej litery, jednej cyfry i jednego znaku specjalnego, można dodać następujący wiersz do pliku:

```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

Można również skonfigurować inne ustawienia, takie jak maksymalny wiek hasła, dodając wiersze do pliku.

#### Konfigurowanie zasad haseł w systemie CentOS

Aby skonfigurować zasady haseł w systemie CentOS, można użyć narzędzia **authconfig**. Narzędzie to udostępnia zestaw opcji, które można wykorzystać do skonfigurowania zasad dotyczących haseł. Na przykład, aby wymusić minimalną długość hasła wynoszącą 8 znaków i wymagać co najmniej jednej wielkiej litery, jednej małej litery, jednej cyfry i jednego znaku specjalnego, można użyć następującego polecenia:

```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```

Spowoduje to aktualizację systemowych plików **/etc/pam.d/system-auth** i **/etc/pam.d/password-auth** w celu wymuszenia określonych zasad dotyczących haseł.

Pamiętaj, aby regularnie przeglądać i aktualizować swoje zasady dotyczące haseł, aby upewnić się, że pozostają one skuteczne przeciwko potencjalnym atakom.


### Monitoruj logi systemowe

Monitorowanie logów systemowych jest ważnym aspektem utrzymania bezpieczeństwa systemu Linux. Dzienniki systemowe rejestrują aktywność systemu, taką jak nieudane próby logowania, błędy i inne ważne zdarzenia, i mogą zapewnić cenny wgląd w potencjalne zagrożenia bezpieczeństwa lub inne kwestie wymagające uwagi. Oto jak monitorować dzienniki systemowe:

#### Za pomocą polecenia journalctl

W większości nowoczesnych dystrybucji Linuksa można użyć polecenia **journalctl** do przeglądania dzienników systemowych. Polecenie to udostępnia szereg opcji, które można wykorzystać do filtrowania i przeszukiwania wpisów dziennika.

Aby wyświetlić wszystkie wpisy dziennika, wystarczy uruchomić następujące polecenie:

```bash
sudo journalctl
```

Spowoduje to wyświetlenie wszystkich wpisów dziennika, z najnowszymi wpisami na dole.

Aby filtrować wpisy dziennika według określonej jednostki, takiej jak usługa lub proces, można użyć opcji **-u**, po której następuje nazwa jednostki. Na przykład, aby wyświetlić wpisy dziennika dla usługi **sshd**, można uruchomić następujące polecenie:
```bash
sudo journalctl -u sshd
```


Aby filtrować wpisy dziennika według określonego zakresu czasu, można użyć opcji **--since** i **--until**, po których następuje znacznik czasu lub zakres czasu. Na przykład, aby wyświetlić wpisy dziennika z ostatniej godziny, można uruchomić następujące polecenie:

```bash
sudo journalctl --since "1 hour ago"
```

#### Korzystanie z narzędzia do zarządzania logami

W przypadku większych lub bardziej złożonych systemów przydatne może być użycie narzędzia do zarządzania dziennikami w celu gromadzenia i analizowania dzienników systemowych. Narzędzia do zarządzania dziennikami mogą zapewniać zaawansowane funkcje, takie jak monitorowanie dzienników w czasie rzeczywistym, agregacja dzienników i analiza dzienników, a także mogą pomóc w skuteczniejszym identyfikowaniu i reagowaniu na potencjalne zagrożenia bezpieczeństwa.

Przykłady narzędzi do zarządzania logami dla systemu Linux obejmują:

- **Logwatch**: proste narzędzie do analizy logów, które zapewnia codzienne e-mailowe podsumowania logów systemowych
- Logrotate**: narzędzie, które automatycznie rotuje i kompresuje pliki logów w celu zaoszczędzenia miejsca na dysku.
- **ELK stack**: popularne narzędzie do zarządzania logami o otwartym kodzie źródłowym, które łączy Elasticsearch, Logstash i Kibana w celu zapewnienia możliwości monitorowania i analizy logów w czasie rzeczywistym.

Pamiętaj, aby regularnie przeglądać i analizować dzienniki systemowe, aby wykrywać i reagować na potencjalne zagrożenia bezpieczeństwa w odpowiednim czasie.

______

## Zakazy:

### Używaj słabych haseł

Używanie słabych haseł jest częstym błędem, który może sprawić, że system Linux będzie podatny na ataki. Atakujący mogą używać narzędzi do odgadywania haseł opartych na popularnych słowach, nazwach lub datach. Ważne jest, aby używać silnych i unikalnych haseł, które nie są łatwe do odgadnięcia.

Silne hasła można tworzyć przy użyciu kombinacji wielkich i małych liter, cyfr i znaków specjalnych. Dobrą praktyką jest również używanie [password manager](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) to generate and store complex passwords securely. [Password managers](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) może również pomóc w zapamiętaniu haseł i uniknięciu używania tego samego hasła do wielu kont.

### Zezwalaj na dostęp roota SSH

Zezwolenie na dostęp roota do SSH jest zagrożeniem bezpieczeństwa, które może dać atakującym pełną kontrolę nad systemem Linux. Zamiast tego należy użyć konta użytkownika innego niż root, aby zalogować się do systemu, a następnie podnieść uprawnienia za pomocą polecenia **sudo**. Pomaga to ograniczyć potencjalny wpływ ataku poprzez ograniczenie uprawnień kont użytkowników.

### Instalowanie niepotrzebnego oprogramowania

Instalowanie niepotrzebnego oprogramowania może zwiększyć powierzchnię ataku systemu Linux, czyniąc go bardziej podatnym na ataki. Ważne jest, aby instalować tylko to oprogramowanie, które jest niezbędne dla systemu i usuwać wszelkie niepotrzebne programy. Pomoże to zmniejszyć liczbę potencjalnych luk w systemie i zminimalizować ryzyko udanego ataku.

### Używanie przestarzałego oprogramowania

Korzystanie z nieaktualnego oprogramowania może sprawić, że system będzie podatny na ataki wykorzystujące znane luki w zabezpieczeniach. Ważne jest, aby zawsze używać najnowszej wersji oprogramowania i regularnie je aktualizować w celu zapewnienia bezpieczeństwa. Pomaga to załatać znane luki i chronić system przed potencjalnymi atakami.

______

## Wnioski

Podsumowując, wzmocnienie systemu Linux ma kluczowe znaczenie dla zapewnienia jego bezpieczeństwa i ochrony przechowywanych w nim danych. Postępując zgodnie z zaleceniami i zakazami opisanymi w tym artykule, można podjąć ważne kroki w celu zabezpieczenia systemu i zmniejszenia ryzyka cyberzagrożeń. Pamiętaj, aby zawsze aktualizować system, korzystać z zapory sieciowej, konfigurować zasady haseł i monitorować dzienniki systemowe. Unikaj używania słabych haseł, wyłączania automatycznych aktualizacji, zezwalania na dostęp roota SSH, instalowania niepotrzebnego oprogramowania i korzystania z przestarzałego oprogramowania. Pamiętając o tych najlepszych praktykach, możesz zapewnić, że twój system Linux pozostanie bezpieczny i chroniony.

## Referencje:

- [The Center for Internet Security's Linux Hardening Guide](https://www.cisecurity.org/cis-hardened-images/)
- [Red Hat Enterprise Linux Security Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
- [Ubuntu Security Documentation](https://ubuntu.com/security)
- [Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)

---
title: "Niezbędne Do's i Don'ts dla Hardening Your Linux System"
date: 2023-02-28
toc: true
draft: false
description: "Dowiedz się, jak utwardzić system Linux, włączając w to aktualizację, używanie zapór sieciowych, włączenie SELinux lub AppArmor, konfigurację zasad dotyczących haseł i monitorowanie logów systemowych."
tags: ["Bezpieczeństwo systemu Linux", "utwardzanie systemu", "firewall", "SELinux", "AppArmor", "polityka haseł", "aktualizacje systemu", "dzienniki systemowe", "moduły bezpieczeństwa", "polityki kontroli dostępu", "cybersecurity", "bezpieczeństwo systemu", "bezpieczeństwo sieci", "zarządzanie podatnością", "najlepsze praktyki bezpieczeństwa", "Bezpieczeństwo informatyczne", "bezpieczeństwo informacji", "aktualizacje oprogramowania", "dostęp do roota", "menedżer haseł"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "Kreskówkowy zamek trzymający tarczę z napisem Linux na niej, podczas gdy strzała odbija się od tarczy."
coverCaption: ""
---


Linux jest popularnym systemem operacyjnym używanym zarówno przez osoby prywatne jak i firmy. Chociaż jest często uważany za bardziej bezpieczny niż inne systemy operacyjne ze względu na jego otwartą naturę, nadal wymaga odpowiedniego hartowania, aby zapewnić bezpieczeństwo systemu i przechowywanych w nim danych. W tym artykule, przejdziemy przez niektóre ogólne do's i don'ts hartowania, które mogą pomóc utrzymać system Linux bezpieczne.

## Do's:

### Aktualizuj swój system

Utrzymywanie[Linux](https://simeononsecurity.ch/articles/how-do-i-learn-linux/) Aktualizowanie systemu jest kluczowe dla utrzymania jego bezpieczeństwa. Regularne aktualizacje pomagają naprawić luki w zabezpieczeniach i błędy, zapewniając, że twój system pozostanie bezpieczny przed potencjalnymi atakami. Oto kilka przykładów, jak zaktualizować swój system Linux za pomocą **apt-get** lub **yum** menedżera pakietów:

#### Aktualizacja Ubuntu za pomocą apt-get

Aby zaktualizować swój system Ubuntu za pomocą **apt-get**, otwórz okno terminala i wpisz:
```bash
sudo apt-get update
```

Spowoduje to pobranie najnowszych list pakietów z repozytoriów pakietów Ubuntu. Po zakończeniu tego polecenia, można zainstalować wszelkie dostępne aktualizacje za pomocą następującego polecenia:

```bash
sudo apt-get upgrade

```

Spowoduje to pobranie i zainstalowanie wszelkich dostępnych aktualizacji dla Twojego systemu.

### Aktualizacja CentOS za pomocą yum

Aby zaktualizować swój system CentOS za pomocą **yum**, otwórz okno terminala i wpisz:

```bash
sudo yum update
```

Spowoduje to pobranie i zainstalowanie wszelkich dostępnych aktualizacji dla twojego systemu. Możesz również użyć następującego polecenia, aby wyczyścić wszystkie stare lub nieużywane pakiety:

```bash
sudo yum autoremove
```

To usunie wszystkie pakiety, które nie są już potrzebne w twoim systemie.

Pamiętaj, aby regularnie sprawdzać i instalować aktualizacje w swoim systemie Linux, aby zapewnić mu bezpieczeństwo i stabilność.


### Użyj firewalla

Zapora sieciowa jest niezbędnym środkiem bezpieczeństwa dla każdego systemu Linux, ponieważ pomaga chronić przed nieautoryzowanym dostępem i innymi zagrożeniami cybernetycznymi. Oto jak używać **ufw** firewall w systemie Linux:

#### Instalacja i włączenie ufw dla systemów opartych na Ubuntu

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

Można przejrzeć aktualne zasady **ufw** wpisując:

```bash
sudo ufw status
```


Spowoduje to wyświetlenie aktualnych reguł i ich statusu.

Pamiętaj, aby regularnie przeglądać i aktualizować swoje reguły **ufw**, aby zapewnić ochronę systemu przed potencjalnymi zagrożeniami.


#### Instalacja i włączenie firewalld dla systemów opartych na CentOS

Aby zainstalować i włączyć domyślny firewall w systemie CentOS, którym jest **firewalld**, możesz użyć następujących poleceń:

```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

To zainstaluje **firewalld** i włączy go w twoim systemie.

#### Konfiguracja reguł firewalld dla systemów opartych na CentOS

Po włączeniu **firewalld** możesz skonfigurować jego reguły, aby zezwolić lub zablokować ruch przychodzący i wychodzący. Oto kilka przykładów:

Aby zezwolić na ruch przychodzący SSH (port 22):

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

Aktualne reguły **firewalld** można przeglądać wpisując:

```bash
sudo firewall-cmd --list-all
```

Spowoduje to wyświetlenie aktualnych reguł i ich statusu.

Pamiętaj, aby regularnie przeglądać i aktualizować swoje reguły **firewalld**, aby zapewnić, że twój system

### Włącz SELinux lub AppArmor

SELinux (Security-Enhanced Linux) i AppArmor to dwa moduły bezpieczeństwa, które mogą być używane do egzekwowania obowiązkowych zasad kontroli dostępu w systemach Linux. Większość nowoczesnych dystrybucji Linuksa ma domyślnie zainstalowany SELinux lub AppArmor, które można włączyć i skonfigurować, aby zwiększyć bezpieczeństwo systemu.

#### Włączanie SELinux w systemach opartych na CentOS-ie

Aby sprawdzić, czy SELinux jest włączony w Twoim systemie, wykonaj następujące polecenie:

```bash
sestatus
```

Jeśli SELinux nie jest zainstalowany, można go zainstalować za pomocą następującego polecenia:

```bash
sudo yum install selinux-policy selinux-policy-targeted
```

Aby włączyć SELinux, należy edytować plik **/etc/selinux/config** i ustawić zmienną **SELINUX** na **wzmacniającą**:

```bash
sudo nano /etc/selinux/config
```
**Zmień SELINUX=wymuszanie**
```
SELINUX=enforcing
```

Zapisz i wyjdź z pliku, używając CTRL+X i Y następnie enter, a następnie zrestartuj system.

#### Włączenie AppArmor dla systemów opartych na Ubuntu

Aby sprawdzić, czy AppArmor jest włączony w Twoim systemie, uruchom następujące polecenie:
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
**Dodaj zabezpieczenie=apparmor**
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```

Zapisz i wyjdź z pliku, używając CTRL+X i Y następnie enter, a następnie uruchom następujące polecenie, aby zaktualizować konfigurację bootloadera systemu:

```bash
sudo update-grub
```

Na koniec należy ponownie uruchomić system.

Po włączeniu SELinux lub AppArmor można skonfigurować ich polityki, aby ograniczyć uprawnienia procesów i ograniczyć ich dostęp do zasobów systemowych. Może to pomóc zminimalizować potencjalne skutki udanego ataku i zwiększyć ogólne bezpieczeństwo systemu.


### Konfiguracja zasad dotyczących haseł

Konfiguracja zasad dotyczących haseł jest ważnym krokiem w utwardzaniu bezpieczeństwa systemu Linux. Poprzez egzekwowanie silnych wymagań dotyczących haseł, można zapewnić, że konta użytkowników są bezpieczne i chronione przed potencjalnymi atakami. Oto jak skonfigurować politykę haseł w systemie Linux:

#### Konfiguracja polityk haseł na Ubuntu

Aby skonfigurować polityki haseł na Ubuntu, możesz użyć modułu **pam_pwquality**. Moduł ten zapewnia zestaw kontroli siły hasła, które mogą być używane do egzekwowania polityki haseł. Aby zainstalować moduł **pam_pwquality**, otwórz okno terminala i wpisz:

```bash
sudo apt-get install libpam-pwquality
```

Po zainstalowaniu modułu można skonfigurować jego ustawienia, edytując plik **/etc/pam.d/common-password**. Na przykład, aby wymusić minimalną długość hasła na poziomie 8 znaków i wymagać co najmniej jednej dużej litery, jednej małej litery, jednej cyfry i jednego znaku specjalnego, możesz dodać do pliku następującą linię:

```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

Możesz również skonfigurować inne ustawienia, takie jak maksymalny wiek hasła, dodając linie do pliku.

#### Konfiguracja polityki haseł w systemie CentOS

Aby skonfigurować polityki haseł w systemie CentOS, można użyć narzędzia **authconfig**. Narzędzie to dostarcza zestaw opcji, które mogą być użyte do skonfigurowania polityk haseł. Na przykład, aby wymusić minimalną długość hasła 8 znaków i wymagać co najmniej jednej dużej litery, jednej małej litery, jednej cyfry i jednego znaku specjalnego, można użyć następującego polecenia:

```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```

Zaktualizuje to systemowe pliki **/etc/pam.d/system-auth** i **/etc/pam.d/password-auth**, aby wymusić określone zasady dotyczące haseł.

Pamiętaj, aby regularnie przeglądać i aktualizować swoje zasady dotyczące haseł, aby zapewnić, że pozostają one skuteczne wobec potencjalnych ataków.


### Monitoruj logi systemowe

Monitorowanie logów systemowych jest ważnym aspektem utrzymania bezpieczeństwa systemu Linux. Logi systemowe rejestrują aktywność systemu, taką jak nieudane próby logowania, błędy i inne ważne zdarzenia, i mogą dostarczyć cennych informacji na temat potencjalnych zagrożeń bezpieczeństwa lub innych problemów, które wymagają uwagi. Oto jak monitorować logi systemowe:

#### Za pomocą polecenia journalctl.

W większości nowoczesnych dystrybucji systemu Linux można użyć polecenia **journalctl** do przeglądania dzienników systemowych. Polecenie to udostępnia wiele opcji, które mogą być użyte do filtrowania i przeszukiwania wpisów dziennika.

Aby wyświetlić wszystkie wpisy dziennika, wystarczy uruchomić następujące polecenie:

```bash
sudo journalctl
```

Spowoduje to wyświetlenie wszystkich wpisów dziennika, z najnowszymi wpisami na dole.

Aby filtrować wpisy dziennika według określonej jednostki, takiej jak usługa lub proces, można użyć opcji **-u**, a następnie nazwy jednostki. Na przykład, aby wyświetlić wpisy dziennika dla usługi **sshd**, można wykonać następujące polecenie:
```bash
sudo journalctl -u sshd
```


Aby filtrować wpisy dziennika według określonego zakresu czasu, można użyć opcji **--od kiedy** i **-do kiedy**, a następnie znacznika czasu lub zakresu czasu. Na przykład, aby wyświetlić wpisy dziennika z ostatniej godziny, można wykonać następujące polecenie:

```bash
sudo journalctl --since "1 hour ago"
```

#### Korzystanie z narzędzia do zarządzania dziennikami

W przypadku większych lub bardziej złożonych systemów przydatne może być użycie narzędzia do zarządzania dziennikami w celu gromadzenia i analizowania dzienników systemowych. Narzędzia do zarządzania dziennikami mogą udostępniać zaawansowane funkcje, takie jak monitorowanie dzienników w czasie rzeczywistym, agregacja dzienników i ich analiza, a także mogą pomóc w skuteczniejszym identyfikowaniu potencjalnych zagrożeń bezpieczeństwa i reagowaniu na nie.

Przykłady narzędzi do zarządzania dziennikami dla systemu Linux obejmują:

- **Logwatch**: proste narzędzie do analizy dzienników, które dostarcza codzienne podsumowania dzienników systemowych pocztą elektroniczną.
- **Logrotate**: narzędzie, które automatycznie rotuje i kompresuje pliki dziennika, aby zaoszczędzić miejsce na dysku.
- StosELK**: popularne narzędzie open-source do zarządzania dziennikami, które łączy Elasticsearch, Logstash i Kibana, aby zapewnić monitorowanie i analizę dzienników w czasie rzeczywistym.

Pamiętaj, aby regularnie przeglądać i analizować logi systemowe, aby w porę wykrywać i reagować na potencjalne zagrożenia bezpieczeństwa.

______

## Don'ts:

### Use weak passwords

Używanie słabych haseł jest częstym błędem, który może sprawić, że twój system Linux będzie podatny na ataki. Atakujący mogą używać narzędzi do odgadywania haseł, które są oparte na popularnych słowach, nazwach lub datach. Ważne jest, aby używać silnych i unikalnych haseł, które nie są łatwe do odgadnięcia.

Silne hasła można tworzyć, stosując kombinację dużych i małych liter, cyfr i znaków specjalnych. Dobrą praktyką jest również używanie[password manager](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) to generate and store complex passwords securely. [Password managers](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) może również pomóc w zapamiętaniu haseł i unikaniu używania tego samego hasła do wielu kont.

### Pozwól na dostęp do SSH rootowi

Zezwolenie na dostęp root do SSH jest zagrożeniem bezpieczeństwa, które może dać napastnikom pełną kontrolę nad systemem Linux. Zamiast tego należy użyć konta użytkownika niebędącego rootem do zalogowania się do systemu, a następnie podnieść uprawnienia za pomocą polecenia **sudo**. Pomaga to ograniczyć potencjalny wpływ ataku poprzez ograniczenie przywilejów kont użytkowników.

### Instalowanie zbędnego oprogramowania

Instalowanie zbędnego oprogramowania może zwiększyć powierzchnię ataku systemu Linux, czyniąc go bardziej podatnym na ataki. Ważne jest, aby instalować tylko oprogramowanie, które jest niezbędne dla systemu i usuwać wszelkie zbędne oprogramowanie. Pomaga to zmniejszyć liczbę potencjalnych luk w systemie i zminimalizować ryzyko udanego ataku.

### Używanie przestarzałego oprogramowania

Używanie przestarzałego oprogramowania może sprawić, że Twój system będzie podatny na ataki wykorzystujące znane luki. Ważne jest, aby zawsze używać najnowszej wersji oprogramowania i regularnie je aktualizować w celu zapewnienia bezpieczeństwa. Pomaga to załatać znane luki i chronić system przed potencjalnymi atakami.

______

## Wnioski

Podsumowując, utwardzenie twojego systemu Linux jest krytyczne dla zapewnienia jego bezpieczeństwa i ochrony przechowywanych w nim danych. Stosując się do porad i wskazówek zawartych w tym artykule, możesz podjąć ważne kroki w celu zabezpieczenia swojego systemu i zmniejszenia ryzyka wystąpienia cyberzagrożeń. Pamiętaj, aby zawsze aktualizować swój system, używać zapory sieciowej, konfigurować politykę haseł i monitorować logi systemowe. Unikaj używania słabych haseł, wyłączania automatycznych aktualizacji, zezwalania na dostęp root SSH, instalowania niepotrzebnego oprogramowania i używania przestarzałego oprogramowania. Pamiętając o tych najlepszych praktykach, możesz mieć pewność, że twój system Linux pozostanie bezpieczny i chroniony.

## Referencje:

-[The Center for Internet Security's Linux Hardening Guide](https://www.cisecurity.org/cis-hardened-images/)
-[Red Hat Enterprise Linux Security Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
-[Ubuntu Security Documentation](https://ubuntu.com/security)
-[Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)

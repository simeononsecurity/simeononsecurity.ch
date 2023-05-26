---
title: "Wprowadzenie do Ansible: Automatyzacja zarządzania infrastrukturą IT"
draft: false
toc: true
date: 2023-02-25
description: "Poznaj podstawy Ansible, narzędzia do automatyzacji o otwartym kodzie źródłowym, które upraszcza zarządzanie infrastrukturą IT za pomocą języka deklaratywnego."
tags: ["Wprowadzenie do Ansible", "Automatyzacja zarządzania infrastrukturą IT", "Podstawy Ansible", "Automatyzacja infrastruktury IT", "Zarządzanie konfiguracją", "Wdrażanie aplikacji", "Udostępnianie", "Ciągłe dostarczanie", "Zgodność z przepisami bezpieczeństwa", "Orkiestracja", "YAML", "Moduły Ansible", "Role", "Najlepsze praktyki", "Kontrola wersji", "Testowanie", "Red Hat", "Administratorzy systemu", "Linux", "macOS", "Windows", "Instalacja Ansible", "Inwentaryzacja Ansible", "Podręczniki Ansible", "Moduły Ansible", "Role Ansible", "Najlepsze praktyki Ansible", "Testowanie Ansible", "Narzędzie do automatyzacji infrastruktury IT", "Samouczek Ansible", "Automatyzacja zarządzania infrastrukturą"]
cover: "/img/cover/A_cartoon_character_sitting_at_a_desk_surrounded_by_servers.png"
coverAlt: "Postać z kreskówki siedząca przy biurku, otoczona serwerami i kablami, z logo Ansible na ekranie komputera, uśmiechająca się, gdy zadania są automatyzowane."
coverCaption: ""
---

Ansible to narzędzie do automatyzacji o otwartym kodzie źródłowym, które umożliwia administratorom systemów automatyzację zarządzania infrastrukturą IT. Zapewnia prosty język do opisania pożądanego stanu infrastruktury i automatycznie wymusza ten stan. Zmniejsza to czas i wysiłek potrzebny do zarządzania złożonymi systemami na dużą skalę.

Jeśli dopiero zaczynasz korzystać z Ansible, ten artykuł zawiera wprowadzenie do tego narzędzia, w tym jego podstawowe pojęcia i sposób rozpoczęcia korzystania z niego.

## Wprowadzenie do Ansible

Ansible zostało opracowane przez Michaela DeHaana w 2012 roku i przejęte przez Red Hat w 2015 roku. Od tego czasu stało się jednym z najpopularniejszych narzędzi do automatyzacji w branży.

Ansible wykorzystuje prosty, deklaratywny język o nazwie YAML (skrót od "YAML Ain't Markup Language") do definiowania pożądanego stanu infrastruktury. Dzięki temu jest łatwy do odczytania i zrozumienia, nawet dla osób niebędących programistami.

Ansible może być używany do automatyzacji szerokiego zakresu zadań, w tym:

- **Zarządzanie konfiguracją**
- Wdrażanie aplikacji**
- ciągłe dostarczanie**
- provisioning**
- Zgodność z zabezpieczeniami**
- Orkiestracja**

## Pierwsze kroki z Ansible

Aby rozpocząć pracę z Ansible, musisz zainstalować go w swoim systemie. Ansible można zainstalować na wielu systemach operacyjnych, w tym Linux, macOS i Windows.

Aby zainstalować Ansible w systemie Linux, w tym przypadku Ubuntu, można użyć następujących poleceń:
```bash
sudo apt-get update
sudo apt-get install ansible -y
```
W przeciwnym razie możesz skorzystać z poniższych przewodników, aby zainstalować ansible:
- [Installing Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- [Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html)

Po zainstalowaniu Ansible można sprawdzić, czy działa, uruchamiając następujące polecenie:
```bash
ansible --version
```

Powinno to wyświetlić zainstalowaną wersję Ansible.

## Ansible Inventory

Pierwszym krokiem w korzystaniu z Ansible jest zdefiniowanie inwentarza. Inwentarz to lista serwerów, którymi Ansible będzie zarządzać. Inwentarz można zdefiniować w różnych formatach, w tym INI, YAML i JSON.

Oto przykład pliku inwentarza w formacie INI:

```ini
[webservers]
webserver1.example.com
webserver2.example.com

[databases]
dbserver1.example.com
dbserver2.example.com
```

Ten plik inwentaryzacji definiuje dwie grupy serwerów, "webserwery" i "bazy danych", i wymienia nazwy hostów serwerów w każdej grupie.

## Ansible Playbooks

Po zdefiniowaniu inwentarza, następnym krokiem jest zdefiniowanie playbooka. Playbook to plik YAML opisujący zestaw zadań, które Ansible powinien wykonać na serwerach w inwentarzu.

Oto przykład prostego playbooka:
```yml
name: Install Nginx
hosts: webservers
become: yes

tasks:
    - name: Install Nginx package
        apt:
        name: nginx
        state: present
```

Ten playbook instaluje serwer WWW Nginx na wszystkich serwerach z grupy "webservers".

The `hosts` określa grupę serwerów, na których powinien zostać uruchomiony playbook. Parametr `become` parametr określa, że zadania powinny być uruchamiane z podwyższonymi uprawnieniami (przy użyciu `sudo` lub `su`

The `tasks` zawiera listę poszczególnych zadań, które playbook powinien wykonać. W tym przypadku jest tylko jedno zadanie, które instaluje pakiet Nginx przy użyciu polecenia `apt` moduł.

## Moduły Ansible

Moduły Ansible to jednostki kodu wielokrotnego użytku, które mogą być używane do wykonywania określonych zadań. Ansible zawiera szeroką gamę wbudowanych modułów, a także dostępnych jest wiele modułów innych firm.

Oto kilka przykładów wbudowanych modułów:

- `apt` - Zarządzanie pakietami w systemach opartych na Debianie
- `yum` - Zarządzanie pakietami w systemach opartych na Red Hat
- `file` - Zarządzanie plikami
- `service` - Zarządzanie usługami systemowymi
- `user` - Zarządzanie użytkownikami i grupami
- `copy` - Kopiowanie plików z maszyny sterującej na serwery zarządzane

Pełną listę wbudowanych modułów można znaleźć w sekcji [Ansible documentation](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)

## Role Ansible i struktura folderów

Rola Ansible to sposób na organizowanie i ponowne wykorzystywanie typowych zadań i konfiguracji. Jest to struktura katalogów zawierająca zadania, programy obsługi, szablony, pliki i inne zasoby.

Oto przykład prostej roli Ansible do instalacji i konfiguracji Nginx:
```
roles/
└── nginx/
    ├── tasks/
    │   ├── main.yml
    ├── handlers/
    │   ├── main.yml
    ├── templates/
    │   ├── nginx.conf.j2
    ├── files/
    ├── vars/
    ├── defaults/
    ├── meta/
```
W tym przykładzie rola nginx jest katalogiem zawierającym kilka podkatalogów, z których każdy służy określonemu celowi:

- **tasks**: zawiera zadania, które będą wykonywane przez rolę.
- **handlers**: zawiera programy obsługi, które mogą być powiadamiane przez zadania.
- **templates**: zawiera szablony Jinja2, które będą używane do generowania plików konfiguracyjnych dla Nginx.
- files**: zawiera wszelkie pliki statyczne wymagane przez rolę.
- **vars**: zawiera zmienne, które są specyficzne dla roli.
- **defaults**: zawiera domyślne zmienne dla roli.
- **meta**: zawiera metadane o roli, takie jak jej zależności.

Role można łatwo udostępniać i ponownie wykorzystywać w wielu playbookach i projektach.

Oto przykład pliku main.yml w katalogu zadań:
```yaml
---
- name: Install Nginx
  apt:
    name: nginx
    state: present
  notify: restart nginx

- name: Enable Nginx
  systemd:
    name: nginx
    enabled: yes
    state: started
```

To zadanie instaluje Nginx przy użyciu modułu apt oraz włącza i uruchamia usługę Nginx przy użyciu modułu systemd. Powiadamia również program obsługi restart nginx, który ponownie uruchomi Nginx, jeśli wprowadzono jakiekolwiek zmiany w konfiguracji.

Korzystanie z takiej roli Ansible może uprościć proces zarządzania i konfigurowania oprogramowania na wielu serwerach lub środowiskach. Oddzielając zadania, programy obsługi, szablony i inne zasoby w jednej strukturze katalogów, można łatwiej zarządzać i ponownie wykorzystywać te komponenty w różnych playbookach i projektach.

## Najlepsze praktyki dla Ansible

Oto kilka najlepszych praktyk, których należy przestrzegać podczas korzystania z Ansible:

### 1. Używaj kontroli wersji

Przechowywanie playbooków i ról Ansible w systemie kontroli wersji, takim jak Git, jest najlepszą praktyką, która może pomóc w śledzeniu zmian i współpracy z innymi. Kontrola wersji zapewnia historię zmian wprowadzonych w bazie kodu, umożliwiając w razie potrzeby cofnięcie się do poprzednich wersji. Ułatwia również współpracę z innymi poprzez udostępnianie kodu i zarządzanie konfliktami.

### 2. Użyj ról, aby zorganizować swoje Playbooki

Role to potężny sposób na organizowanie playbooków i zadań Ansible. Grupując powiązane zadania w role, można uczynić swoje playbooki bardziej modułowymi i wielokrotnego użytku. Role ułatwiają również współdzielenie kodu w różnych projektach.

Oto przykład playbooka, który wykorzystuje rolę do instalacji i konfiguracji Nginx:

```yml
name: Install and configure Nginx
hosts: webservers
become: yes
roles:
  - nginx
```

Ten playbook używa roli o nazwie "nginx" do instalacji i konfiguracji Nginx na grupie hostów "webservers".

### 3. Używanie tagów do grupowania zadań

Tagi mogą być używane do grupowania powiązanych zadań w playbookach Ansible. Ułatwia to uruchamianie określonych części playbooka, zwłaszcza podczas pracy z dużymi, złożonymi playbookami.

Oto przykład użycia tagów w playbooku Ansible:
```yml
name: Install and configure Nginx
hosts: webservers
become: yes
tasks:
  - name: Install Nginx
    apt:
    name: nginx
    state: present
    tags: nginx_install

  - name: Configure Nginx
    template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    tags: nginx_config
```

Ten playbook zawiera dwa zadania, jedno do instalacji Nginx i jedno do konfiguracji Nginx. Każde zadanie ma przypisany tag, co ułatwia uruchamianie tylko tych zadań, które są potrzebne.

### 4. Używanie zmiennych w celu uelastycznienia playbooków

Zmienne mogą być używane do uczynienia playbooków Ansible bardziej elastycznymi i wielokrotnego użytku. Używając zmiennych, możesz uczynić swoje playbooki bardziej ogólnymi i adaptowalnymi do różnych środowisk.

Oto przykład użycia zmiennych w playbooku Ansible:
```yml
name: Install and configure Nginx
hosts: webservers
become: yes

vars:
nginx_port: 80
nginx_user: www-data

tasks:
  - name: Install Nginx
    apt:
    name: nginx
    state: present
  - name: Configure Nginx
    template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    notify: restart nginx

handlers:
  - name: restart nginx
    service:
    name: nginx
    state: restarted
```

Ten playbook używa zmiennych do określenia portu, na którym Nginx powinien nasłuchiwać oraz użytkownika, który powinien uruchomić Nginx. Dzięki temu playbook jest bardziej elastyczny i można go dostosować do różnych środowisk.

### 5. Przetestuj swoje playbooki

Testowanie playbooków Ansible to najlepsza praktyka, która może pomóc w wychwyceniu błędów i upewnieniu się, że playbooki działają zgodnie z oczekiwaniami. Jednym z popularnych narzędzi do testowania playbooków Ansible jest Molecule.

Molecule to framework testowy, który umożliwia testowanie playbooków w spójny i zautomatyzowany sposób. Molecule może tworzyć maszyny wirtualne, stosować playbooki, a następnie weryfikować, czy wszystko działa zgodnie z oczekiwaniami. Może to pomóc w wychwyceniu błędów i upewnieniu się, że playbooki działają poprawnie przed wdrożeniem do produkcji.

Oto przykład użycia Molecule do testowania roli Ansible:

```bash
molecule init role myrole
cd myrole
molecule test
```

## Wnioski

W tym artykule przedstawiliśmy Ansible, potężne narzędzie do automatyzacji, które może pomóc w zarządzaniu złożoną infrastrukturą IT. Omówiliśmy podstawowe koncepcje Ansible, w tym inwentarze, playbooki, moduły i role.

Omówiliśmy również najlepsze praktyki korzystania z Ansible, w tym korzystanie z kontroli wersji, organizowanie playbooków za pomocą ról, używanie tagów i zmiennych oraz testowanie playbooków.

Jeśli jesteś nowym użytkownikiem Ansible, zalecamy rozpoczęcie od eksperymentowania z kilkoma prostymi playbookami i stopniowe rozwijanie swoich umiejętności i wiedzy w miarę upływu czasu. Dzięki praktyce będziesz w stanie z łatwością zautomatyzować nawet najbardziej złożone zadania związane z infrastrukturą!

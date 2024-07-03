---
title: "Автоматизация OSINT с помощью модулей Shodan PowerShell"
date: 2020-11-14
---

Коллекция модулей PowerShell для взаимодействия с API Shodan

**Примечания:**
- Вам потребуется ключ Shodan API, который можно найти на вашем компьютере [Shodan Account](https://account.shodan.io/)
- Примеры API, используемых в модулях, можно найти на сайте [Shodan Developers Page](https://developer.shodan.io/api)
- Некоторые модули могут использовать кредиты на сканирование или запросы Кредиты на запросы используются при загрузке данных через веб-сайт, CLI или API (что делают эти скрипты).
  Поскольку мы используем API, важно отметить, что кредиты за запросы списываются, если:
  1.  Используется поисковый фильтр
  2.  Запрашивается страница 2 или выше.
      Кредиты возобновляются в начале месяца, и 1 кредит позволяет загрузить 100 результатов.
      Что касается кредитов на сканирование, то 1 кредит на сканирование позволяет отсканировать 1 IP, и они также возобновляются в начале месяца.
      Пожалуйста, ознакомьтесь со справочным центром Shodan [HERE](https://help.shodan.io/the-basics/credit-types-explained) для получения полной информации.

## Оглавление
- [Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
- [Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **Модули**
  - [Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - Возвращает информацию о плане API, принадлежащем заданному ключу API.
  - [Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Показывает HTTP-заголовки, которые отправляет клиент при подключении к веб-серверу.
  - [Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - Получает ваш текущий IP-адрес, видимый из Интернета.
  - [Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - Получает все поддомены и другие записи DNS для заданного домена
  - [Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  - [Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - Поиск имен хостов, которые были определены для заданного списка IP-адресов.
  - [Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - Выполняет поиск эксплойтов, но возвращает только информацию об общем количестве совпадений, связанных с поисковым термином, и, опционально, об авторе эксплойта, платформе, порте, источнике или типе.
  - [Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  - [Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - Возвращает общее количество результатов поиска по запросу "/shodan/host/search".
  - [Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - Поиск на Shodan с IP-адресом.
  - [Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Поиск в Shodan с использованием того же синтаксиса запросов, что и на сайте, и использование фасетов для получения сводной информации по различным свойствам.
  - [Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - Этот модуль возвращает список поисковых фильтров, которые могут быть использованы в поисковом запросе.
  - [Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - Этот модуль возвращает список поисковых фильтров, которые могут быть использованы в поисковом запросе.
  - [Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Перечислите все порты, которые Shodan просматривает в Интернете.
  - [Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - Возвращает информацию об учетной записи Shodan, связанной с данным ключом API
  - [Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - Проверка хода выполнения ранее отправленного запроса на сканирование
  - [Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Перечислите все протоколы, которые могут быть использованы при выполнении сканирования Интернета по требованию через Shodan
  - [Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP) - С помощью этого модуля можно запросить у Shodan "ползание" по сети.

<a name="Download"></a>

## Download

Вам необходимо клонировать или загрузить скрипты на свой компьютер.

Вы можете воспользоваться выпадающим меню Code на этой странице репозитория, прокрутив ее вверх, или просто скопировать и вставить следующую ссылку: [https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

В данном примере мы будем клонировать репозиторий в Git Bash. После щелчка на значке буфера обмена, как показано выше, мы можем набрать git clone и, щелкнув правой кнопкой мыши на окне Git Bash, выбрать пункт paste из выпадающего меню:

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

Подробные инструкции по клонированию приведены в разделе [the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

После получения файлов необходимо скопировать их в C:\Program Files\WindowsPowerShell\Modules, при этом появится диалоговое окно с сообщением о том, что доступ запрещен, нажмите кнопку continue, чтобы завершить копирование файлов в это место, а затем переходите к инструкции по установке [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**OR**

Вы можете воспользоваться выпадающим меню Code на этой странице репо, прокрутив ее вверх, или просто щелкнуть по следующей ссылке:
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

Разархивируйте файл main.zip, щелкнув правой кнопкой мыши на нем и выбрав из выпадающего меню пункт extract here.

После получения файлов необходимо скопировать их в C:\Program Files\WindowsPowerShell\Modules, при этом появится диалоговое окно с сообщением о том, что доступ запрещен, нажмите кнопку continue, чтобы завершить копирование файлов в это место, а затем переходите к инструкции по установке [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

## Установка

<a name="Install"></a>

Для установки модулей необходимо запустить окно PowerShell от имени администратора.
Это можно сделать двумя способами:

Первый способ - щелкнуть правой кнопкой мыши на значке PowerShell на рабочем столе и выбрать в выпадающем меню пункт Run as Administrator.

![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**OR**

Набрав в строке поиска p (или столько символов, сколько потребуется PowerShell для появления) и нажав кнопку Run as Administrator.

![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

Вам необходимо находиться в каталоге, в который вы скопировали скрипты.
Выполните следующую команду для изменения рабочего каталога:

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

На клиентских компьютерах Windows нам необходимо изменить политику выполнения PowerShell, которая по умолчанию является ограниченной (Restricted).

Для получения более подробной информации ознакомьтесь с этой статьей [Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

Выполните следующую команду, чтобы установить политику на RemoteSigned, и введите y, чтобы выбрать, что Yes вы хотите изменить политику.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

После изменения политики выполнения можно выполнить следующую команду для импорта модулей.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

Теперь любой из скриптов можно запустить как модуль через powershell.

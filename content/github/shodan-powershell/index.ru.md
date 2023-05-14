---
title: "Автоматизируйте OSINT с помощью модулей Shodan PowerShell"
date: 2020-11-14
---

Коллекция модулей PowerShell для взаимодействия с API Shodan.

**Примечания:**
- Вам понадобится API-ключ Shodan, который можно найти на вашем[Shodan Account](https://account.shodan.io/)
- Примеры API, используемых в модулях, можно найти на[Shodan Developers Page](https://developer.shodan.io/api)
- Некоторые модули могут использовать кредиты сканирования или запроса. Кредиты запроса используются, когда вы загружаете данные через веб-сайт, интерфейс командной строки или API (что делают эти скрипты).
  Поскольку мы используем API, важно отметить, что кредиты запросов вычитаются, если:
  1. Используется поисковый фильтр
  2. Требуется страница 2 или выше
      Кредиты обновляются в начале месяца, и 1 кредит позволяет загрузить 100 результатов.
      Что касается кредитов на сканирование, 1 кредит на сканирование позволяет сканировать 1 IP-адрес, и они также продлеваются в начале месяца.
      Пожалуйста, посетите Справочный центр Shodan[HERE](https://help.shodan.io/the-basics/credit-types-explained) для получения полной информации.

## Оглавление
-[Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
-[Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **Модули**
  -[Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - Возврат информации о плане API, принадлежащем данному ключу API.
  -[Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Показывает заголовки HTTP, которые ваш клиент отправляет при подключении к веб-серверу.
  -[Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - Получает ваш текущий IP-адрес, как видно из Интернета.
  -[Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - Получает все поддомены и другие записи DNS для данного домена
  -[Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  -[Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - Ищет имена хостов, которые были определены для данного списка IP-адресов.
  -[Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - Выполняет поиск эксплойтов, но возвращает только информацию об общем количестве совпадений, связанных с условием поиска, и, при необходимости, об авторе эксплойта, платформе, порте, источнике или типе.
  -[Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  -[Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - Возвращает общее количество результатов "/shodan/host/search".
  -[Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - Поиск Shodan с IP-адресом.
  -[Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Поиск в Shodan с использованием того же синтаксиса запроса, что и на веб-сайте, и использование фасетов для получения сводной информации по различным свойствам.
  -[Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - Этот модуль возвращает список поисковых фильтров, которые можно использовать в поисковом запросе.
  -[Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - Этот модуль возвращает список поисковых фильтров, которые можно использовать в поисковом запросе.
  -[Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Перечислите все порты, которые Shodan сканирует в Интернете.
  -[Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - Возвращает информацию об учетной записи Shodan, связанной с этим ключом API.
  -[Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - Проверьте ход ранее отправленного запроса на сканирование
  -[Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Перечислите все протоколы, которые можно использовать при выполнении сканирования Интернета по запросу через Shodan.
  -[Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP)- Используйте этот модуль, чтобы запросить у Shodan сканирование сети.<a name="Download"></a> ## Загрузка Вам потребуется клонировать или загрузить скрипты на свой компьютер. Вы можете использовать раскрывающееся меню «Код» на этой странице репозитория, прокрутив вверх или просто скопировав и вставив следующую ссылку:[https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

В этом примере мы будем клонировать репозиторий в Git Bash, после нажатия на значок буфера обмена, как показано выше, мы можем ввести git clone и щелкнуть правой кнопкой мыши окно Git Bash, чтобы выбрать вставку из раскрывающегося меню:

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

For detailed instructions on cloning please view [the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

Once you have the files, you need to copy the files to C:\Program Files\WindowsPowerShell\Modules, doing this will prompt dialog saying that access is denied, click continue to finish copying the files to this location and then proceed to the installation instructions [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**OR**

You can use the Code dropdown menu on this repo page by scrolling up, or just click on the following link:
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

Unzip main.zip by right clicking on the file and selecting extract here from the dropdown menu.

Once you have the files, you need to copy the files to C:\Program Files\WindowsPowerShell\Modules, doing this will prompt dialog saying that access is denied, click continue to finish copying the files to this location and then proceed to the installation instructions [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

# Install

<a name="Install"></a>

To install the modules You will need to run a PowerShell window as administrator.
There are two ways of doing this:

The first way is by right clicking the PowerShell icon on the Desktop and selecting Run as Administrator from the dropdown menu.

![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**OR**

By typing p (or however many characters it takes PowerShell to show up) into the search bar and clicking on Run as Administrator.

![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

You will need to be in the directory that you copied the scripts to.
Run the following command to change your working directory:

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

On Windows client computers we need to change the PowerShell execution policy which is Restricted by default.

For more information please read this [Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

Run the following command to set the policy to RemoteSigned and enter y to select that Yes you want to change the policy.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

Once the execution policy has been changed, you can run the following command to Import the modules.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

Теперь вы можете запускать любой из скриптов как модуль через powershell.

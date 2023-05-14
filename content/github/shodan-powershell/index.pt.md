---
title: "Automatize OSINT com módulos Shodan PowerShell"
date: 2020-11-14
---

Uma coleção de módulos PowerShell para interagir com a API Shodan

**Notas:**
- Você precisará de sua chave de API Shodan, que pode ser encontrada em seu[Shodan Account](https://account.shodan.io/)
- Exemplos das APIs utilizadas nos módulos podem ser encontrados no[Shodan Developers Page](https://developer.shodan.io/api)
- Certos módulos podem usar créditos de verificação ou consulta Os créditos de consulta são usados quando você baixa dados por meio do site, CLI ou API (o que esses scripts fazem).
  Como estamos usando a API, é importante observar que os créditos da consulta são deduzidos se:
  1. Um filtro de pesquisa é usado
  2. A página 2 ou além é solicitada
      Os créditos renovam-se no início do mês e 1 crédito permite descarregar 100 resultados.
      Quanto aos créditos de varredura, 1 crédito de varredura permite que você escaneie 1 IP, e eles também renovam no início do mês.
      Por favor, veja o Centro de Ajuda Shodan[HERE](https://help.shodan.io/the-basics/credit-types-explained) para detalhes completos.

## Índice
-[Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
-[Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **Módulos**
  -[Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - Retorna informações sobre o plano de API pertencente à chave de API fornecida.
  -[Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Mostra os cabeçalhos HTTP que seu cliente envia ao se conectar a um servidor web.
  -[Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - Obtém seu endereço IP atual visto da Internet.
  -[Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - Obtém todos os subdomínios e outras entradas de DNS para o domínio fornecido
  -[Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  -[Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - Procura os nomes de host que foram definidos para a lista fornecida de endereços IP.
  -[Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - Pesquisa explorações, mas retorna apenas informações sobre o número total de correspondências relacionadas ao termo de pesquisa e, opcionalmente, o autor, plataforma, porta, fonte ou tipo da exploração.
  -[Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  -[Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - Retorna o número total de resultados de "/shodan/host/search" fornece.
  -[Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - Pesquise Shodan com endereço IP.
  -[Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Pesquise Shodan usando a mesma sintaxe de consulta do site e use facetas para obter informações resumidas para diferentes propriedades.
  -[Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - Este módulo retorna uma lista de filtros de pesquisa que podem ser usados na consulta de pesquisa.
  -[Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - Este módulo retorna uma lista de filtros de pesquisa que podem ser usados na consulta de pesquisa.
  -[Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Liste todas as portas que o Shodan está rastreando na Internet.
  -[Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - Retorna informações sobre a conta Shodan vinculada a esta chave de API
  -[Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - Verifique o progresso de uma solicitação de digitalização enviada anteriormente
  -[Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Liste todos os protocolos que podem ser usados ao realizar varreduras de Internet sob demanda via Shodan
  -[Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP)- Use este módulo para solicitar que Shodan rastreie uma rede.<a name="Download"></a> ## Download Você precisará clonar ou baixar os scripts para o seu computador. Você pode usar o menu suspenso Código nesta página de repositório rolando para cima ou apenas copiando e colando o seguinte link:[https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

Para este exemplo estaremos clonando o repositório dentro do Git Bash, depois de clicar no ícone da área de transferência como visto acima, podemos digitar git clone e clicar com o botão direito na janela do Git Bash para selecionar colar no menu suspenso:

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

Agora você pode executar qualquer um dos scripts como um módulo via powershell.

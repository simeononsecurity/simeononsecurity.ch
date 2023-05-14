---
title: "ਸ਼ੋਡਨ ਪਾਵਰਸ਼ੇਲ ਮੋਡੀਊਲ ਨਾਲ OSINT ਨੂੰ ਆਟੋਮੈਟਿਕ ਕਰੋ"
date: 2020-11-14
---

ਸ਼ੋਡਨ API ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਲਈ PowerShell ਮੋਡੀਊਲ ਦਾ ਸੰਗ੍ਰਹਿ

**ਨੋਟ:**
- ਤੁਹਾਨੂੰ ਸ਼ੋਡਨ API ਕੁੰਜੀ ਦੀ ਲੋੜ ਪਵੇਗੀ, ਜੋ ਤੁਹਾਡੇ 'ਤੇ ਲੱਭੀ ਜਾ ਸਕਦੀ ਹੈ[Shodan Account](https://account.shodan.io/)
- ਮੋਡਿਊਲਾਂ ਵਿੱਚ ਵਰਤੇ ਗਏ APIs ਦੀਆਂ ਉਦਾਹਰਨਾਂ 'ਤੇ ਮਿਲ ਸਕਦੀਆਂ ਹਨ[Shodan Developers Page](https://developer.shodan.io/api)
- ਕੁਝ ਮੌਡਿਊਲ ਸਕੈਨ ਜਾਂ ਪੁੱਛਗਿੱਛ ਕ੍ਰੈਡਿਟ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹਨ ਜਦੋਂ ਤੁਸੀਂ ਵੈੱਬਸਾਈਟ, CLI ਜਾਂ API (ਇਹ ਸਕ੍ਰਿਪਟਾਂ ਕੀ ਕਰਦੀਆਂ ਹਨ) ਰਾਹੀਂ ਡਾਟਾ ਡਾਊਨਲੋਡ ਕਰਦੇ ਹੋ ਤਾਂ ਪੁੱਛਗਿੱਛ ਕ੍ਰੈਡਿਟ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।
  ਕਿਉਂਕਿ ਅਸੀਂ API ਦੀ ਵਰਤੋਂ ਕਰ ਰਹੇ ਹਾਂ, ਇਹ ਨੋਟ ਕਰਨਾ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਪੁੱਛਗਿੱਛ ਕ੍ਰੈਡਿਟ ਕੱਟੇ ਜਾਂਦੇ ਹਨ ਜੇਕਰ:
  1. ਇੱਕ ਖੋਜ ਫਿਲਟਰ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ
  2. ਪੰਨਾ 2 ਜਾਂ ਇਸ ਤੋਂ ਬਾਅਦ ਦੀ ਬੇਨਤੀ ਕੀਤੀ ਗਈ ਹੈ
      ਮਹੀਨੇ ਦੀ ਸ਼ੁਰੂਆਤ 'ਤੇ ਕ੍ਰੈਡਿਟ ਰੀਨਿਊ ਹੁੰਦੇ ਹਨ ਅਤੇ 1 ਕ੍ਰੈਡਿਟ ਤੁਹਾਨੂੰ 100 ਨਤੀਜੇ ਡਾਊਨਲੋਡ ਕਰਨ ਦਿੰਦਾ ਹੈ।
      ਸਕੈਨ ਕ੍ਰੈਡਿਟ ਲਈ, 1 ਸਕੈਨ ਕ੍ਰੈਡਿਟ ਤੁਹਾਨੂੰ 1 IP ਸਕੈਨ ਕਰਨ ਦਿੰਦਾ ਹੈ, ਅਤੇ ਉਹ ਮਹੀਨੇ ਦੇ ਸ਼ੁਰੂ ਵਿੱਚ ਨਵਿਆਉਣ ਵੀ ਦਿੰਦਾ ਹੈ।
      ਕਿਰਪਾ ਕਰਕੇ ਸ਼ੋਡਨ ਮਦਦ ਕੇਂਦਰ ਦੇਖੋ[HERE](https://help.shodan.io/the-basics/credit-types-explained) ਪੂਰੇ ਵੇਰਵਿਆਂ ਲਈ।

## ਵਿਸ਼ਾ - ਸੂਚੀ
-[Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
-[Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **ਮੌਡਿਊਲ**
  -[Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - ਦਿੱਤੀ API ਕੁੰਜੀ ਨਾਲ ਸਬੰਧਤ API ਯੋਜਨਾ ਬਾਰੇ ਜਾਣਕਾਰੀ ਵਾਪਸ ਕਰੋ।
  -[Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - HTTP ਹੈਡਰ ਦਿਖਾਉਂਦਾ ਹੈ ਜੋ ਤੁਹਾਡਾ ਕਲਾਇੰਟ ਇੱਕ ਵੈਬਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰਨ ਵੇਲੇ ਭੇਜਦਾ ਹੈ।
  -[Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - ਇੰਟਰਨੈੱਟ ਤੋਂ ਦੇਖਿਆ ਗਿਆ ਤੁਹਾਡਾ ਮੌਜੂਦਾ IP ਪਤਾ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ।
  -[Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - ਦਿੱਤੇ ਗਏ ਡੋਮੇਨ ਲਈ ਸਾਰੇ ਸਬਡੋਮੇਨ ਅਤੇ ਹੋਰ DNS ਐਂਟਰੀਆਂ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ
  -[Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  -[Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - IP ਪਤਿਆਂ ਦੀ ਦਿੱਤੀ ਗਈ ਸੂਚੀ ਲਈ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤੇ ਗਏ ਹੋਸਟਨਾਂ ਨੂੰ ਵੇਖਦਾ ਹੈ।
  -[Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - ਸ਼ੋਸ਼ਣਾਂ ਦੀ ਖੋਜ ਕਰਦਾ ਹੈ ਪਰ ਖੋਜ ਸ਼ਬਦ ਨਾਲ ਸੰਬੰਧਿਤ ਮਿਲਾਨ ਦੀ ਕੁੱਲ ਸੰਖਿਆ, ਅਤੇ ਵਿਕਲਪਿਕ ਤੌਰ 'ਤੇ ਸ਼ੋਸ਼ਣ ਲੇਖਕ, ਪਲੇਟਫਾਰਮ, ਪੋਰਟ, ਸਰੋਤ ਜਾਂ ਕਿਸਮ ਬਾਰੇ ਜਾਣਕਾਰੀ ਦਿੰਦਾ ਹੈ।
  -[Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  -[Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - ਪ੍ਰਦਾਨ ਕੀਤੇ ਗਏ "/shodan/host/search" ਦੇ ਨਤੀਜਿਆਂ ਦੀ ਕੁੱਲ ਸੰਖਿਆ ਵਾਪਸ ਕਰਦਾ ਹੈ।
  -[Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - IP ਐਡਰੈੱਸ ਨਾਲ ਸ਼ੋਡਨ ਦੀ ਖੋਜ ਕਰੋ.
  -[Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - ਵੈਬਸਾਈਟ ਦੇ ਸਮਾਨ ਪ੍ਰਸ਼ਨ ਸੰਟੈਕਸ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਸ਼ੋਡਨ ਦੀ ਖੋਜ ਕਰੋ ਅਤੇ ਵੱਖ-ਵੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਲਈ ਸੰਖੇਪ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਪਹਿਲੂਆਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।
  -[Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - ਇਹ ਮੋਡੀਊਲ ਖੋਜ ਫਿਲਟਰਾਂ ਦੀ ਇੱਕ ਸੂਚੀ ਵਾਪਸ ਕਰਦਾ ਹੈ ਜੋ ਖੋਜ ਪੁੱਛਗਿੱਛ ਵਿੱਚ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ।
  -[Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - ਇਹ ਮੋਡੀਊਲ ਖੋਜ ਫਿਲਟਰਾਂ ਦੀ ਇੱਕ ਸੂਚੀ ਵਾਪਸ ਕਰਦਾ ਹੈ ਜੋ ਖੋਜ ਪੁੱਛਗਿੱਛ ਵਿੱਚ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ।
  -[Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - ਉਹਨਾਂ ਸਾਰੀਆਂ ਪੋਰਟਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ ਜੋ ਸ਼ੋਡਨ ਇੰਟਰਨੈੱਟ 'ਤੇ ਘੁੰਮ ਰਿਹਾ ਹੈ।
  -[Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - ਇਸ API ਕੁੰਜੀ ਨਾਲ ਜੁੜੇ ਸ਼ੋਡਨ ਖਾਤੇ ਬਾਰੇ ਜਾਣਕਾਰੀ ਦਿੰਦਾ ਹੈ
  -[Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - ਪਹਿਲਾਂ ਪੇਸ਼ ਕੀਤੀ ਗਈ ਸਕੈਨ ਬੇਨਤੀ ਦੀ ਪ੍ਰਗਤੀ ਦੀ ਜਾਂਚ ਕਰੋ
  -[Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - ਉਹਨਾਂ ਸਾਰੇ ਪ੍ਰੋਟੋਕੋਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ ਜੋ ਸ਼ੋਡਨ ਦੁਆਰਾ ਆਨ-ਡਿਮਾਂਡ ਇੰਟਰਨੈਟ ਸਕੈਨ ਕਰਨ ਵੇਲੇ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ
  -[Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP)- ਸ਼ੋਡਨ ਨੂੰ ਇੱਕ ਨੈਟਵਰਕ ਕ੍ਰੌਲ ਕਰਨ ਲਈ ਬੇਨਤੀ ਕਰਨ ਲਈ ਇਸ ਮੋਡੀਊਲ ਦੀ ਵਰਤੋਂ ਕਰੋ।<a name="Download"></a> ## ਡਾਊਨਲੋਡ ਕਰੋ ਤੁਹਾਨੂੰ ਆਪਣੇ ਕੰਪਿਊਟਰ &#39;ਤੇ ਸਕ੍ਰਿਪਟਾਂ ਨੂੰ ਕਲੋਨ ਜਾਂ ਡਾਊਨਲੋਡ ਕਰਨ ਦੀ ਲੋੜ ਹੋਵੇਗੀ। ਤੁਸੀਂ ਇਸ ਰੈਪੋ ਪੇਜ &#39;ਤੇ ਕੋਡ ਡ੍ਰੌਪਡਾਉਨ ਮੀਨੂ ਨੂੰ ਸਕ੍ਰੋਲ ਕਰਕੇ, ਜਾਂ ਹੇਠਾਂ ਦਿੱਤੇ ਲਿੰਕ ਨੂੰ ਕਾਪੀ ਅਤੇ ਪੇਸਟ ਕਰ ਸਕਦੇ ਹੋ:[https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

ਇਸ ਉਦਾਹਰਨ ਲਈ ਅਸੀਂ Git Bash ਦੇ ਅੰਦਰ ਰੇਪੋ ਨੂੰ ਕਲੋਨ ਕਰਾਂਗੇ, ਉੱਪਰ ਦਿੱਤੇ ਗਏ ਕਲਿੱਪਬੋਰਡ ਆਈਕਨ 'ਤੇ ਕਲਿੱਕ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਅਸੀਂ git clone ਟਾਈਪ ਕਰ ਸਕਦੇ ਹਾਂ ਅਤੇ ਡ੍ਰੌਪਡਾਉਨ ਮੀਨੂ ਤੋਂ ਪੇਸਟ ਚੁਣਨ ਲਈ Git Bash ਵਿੰਡੋ 'ਤੇ ਸੱਜਾ ਕਲਿੱਕ ਕਰ ਸਕਦੇ ਹਾਂ:

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

ਹੁਣ ਤੁਸੀਂ ਪਾਵਰਸ਼ੇਲ ਰਾਹੀਂ ਕਿਸੇ ਵੀ ਸਕ੍ਰਿਪਟ ਨੂੰ ਮੋਡੀਊਲ ਵਜੋਂ ਚਲਾ ਸਕਦੇ ਹੋ।


Write-Host "Installing Chocolatey"
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
choco feature enable -n=allowGlobalConfirmation
choco feature enable -n useFipsCompliantChecksums
choco upgrade all

Write-Host "Install Latest Windows Updates"
choco install pswindowsupdate
Add-WUServiceManager -ServiceID 7971f918-a847-4430-9279-4a52d1efe18d -Confirm:$false
Install-WindowsUpdate -MicrosoftUpdate -AcceptAll 
Get-WuInstall -AcceptAll -IgnoreReboot

Write-Host "Installing Browsers"
choco install googlechrome firefox chromium microsoft-edge tor-Browser flashplayerppapi flashplayerplugin

Write-Host "Installing Java"
choco install jre8

Write-Host "Installing Networking and Administration Tools"
choco install putty.install winscp.install teamviewer sysinternals driverbooster openvpn wireguard etcher rufus.install cheatengine sleuthkit sandboxie.install veracrypt wireshark nmap windirstat mysql.workbench cpu-z.install winbox rsat hxd ida-free ghidra adb universal-adb-drivers

Write-Host "Installing Terminals"
choco install powershell powershellhere-elevated powershell.portable microsoft-windows-terminal docker-cli azure-cli awstools.powershell awscli kubernetes-cli powertoys

Write-Host "Installing Hugo and Node Stack Tools"
choco install hugo hugo-extended nodejs.install

Write-Host "Installing IDE and Dev Tools"
choco install vscode visualstudio2019enterprise notepadplusplus.install python pip 

Write-Host "Installing GIT Tools"
choco install github-desktop gh git.install git-lfx gnupg gpg4win openssh markdownmonster postman

Write-Host "Installing Game Clients"
choco install steam 

Write-Host "Installing Chat Clients"
choco install microsoft-teams.install rocketchat discord.install discord-canary pidgin

Write-Host "Installing Misc."
choco install installroot 7zip.install vlc winlogbeat gimp curl k-litecodecpackfull ossec-client suricata clamav audacity audacity-lame autohotkey handbreak.install obs-studio burp-suite-free-edition 

Write-Host "Installing Office Suite and Document Readers"
choco install officeproplus2013 adobereader

Write-Host "Installing VMware"
choco install vmwareworkstation vmware-horizon-client vmware-powercli-psmodule vmrc

Write-Host "Configuring Windows - Optimizations, Debloating, and Hardening"
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.ch/scripts/windowsoptimizeandharden.ps1'))




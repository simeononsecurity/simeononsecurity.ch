$github = "Standalone-Windows-Server-STIG-Script"
$Url = "https://github.com/simeononsecurity/$github/archive/master.zip"
$scriptname = "sos-secure-standalone-server.ps1"
$ZipFile = "C:\temp\" + $(Split-Path -Path $Url -Leaf)
$Destination= "C:\temp\"
New-Item "C:\" -Name "temp" -ItemType "directory" -Force
Invoke-WebRequest -Uri $Url -OutFile $ZipFile
$ExtractShell = New-Object -ComObject Shell.Application
$Files = $ExtractShell.Namespace($ZipFile).Items()
$ExtractShell.NameSpace($Destination).CopyHere($Files)
Write-Output "Extracting ZIP..... This might take a little while"
CD $Destination\"$github"-master
PowerShell.exe -ExecutionPolicy Bypass -File C:\temp\"$github"-master\"$scriptname"

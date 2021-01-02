$github = "Windows-Optimize-Debloat"
$Url = "https://github.com/simeononsecurity/$github/archive/main.zip"
$scriptname = "sos-optimize-windows.ps1"
$ZipFile = "C:\temp\" + $(Split-Path -Path $Url -Leaf)
$Destination= "C:\temp\"
New-Item "C:\" -Name "temp" -ItemType "directory" -Force
Invoke-WebRequest -Uri $Url -OutFile $ZipFile
$ExtractShell = New-Object -ComObject Shell.Application
$Files = $ExtractShell.Namespace($ZipFile).Items()
Write-Output "Extracting ZIP..... This might take a little while"
$ExtractShell.NameSpace($Destination).CopyHere($Files)
Write-Output "Executing Script..."
Set-Location $Destination\"$github"-master
PowerShell.exe -ExecutionPolicy Bypass -File C:\temp\"$github"-main\"$scriptname"
Write-Output "Finished"




foreach ($file in (get-childitem)){
    $URL = "https://simeononsecurity.ch/img/cover/$file"
    $Path = $file.fullname
    Write-Host $URL
    Write-Host $Path
    Invoke-WebRequest -URI $URL -OutFile $Path
}
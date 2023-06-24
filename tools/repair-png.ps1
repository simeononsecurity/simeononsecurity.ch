param (
    [Parameter(Mandatory=$true, Position=0)]
    [ValidateNotNullOrEmpty()]
    [Alias("Path")]
    [string]$Target
)

# Check if the target path is a file or a folder
if (Test-Path -PathType Leaf $Target) {
    # Target is a file
    $pngFiles = @(Get-Item -Path $Target)
}
elseif (Test-Path -PathType Container $Target) {
    # Target is a folder
    $pngFiles = Get-ChildItem -Path $Target -Filter *.png -File -Recurse
}
else {
    Write-Host "Invalid path: $Target"
    $Target = "C:\Users\Simeon\Documents\GitHub\1-simeononsecurity.ch\assets\img\cover"
    Exit 1
}

# Loop through each PNG file
foreach ($file in $pngFiles) {
    $inputFilePath = $file.FullName
    $outputFilePath = [System.IO.Path]::ChangeExtension($inputFilePath, ".fixed.png")

    try {
        # Start the pngcrush process
        $process = Start-Process -FilePath "C:\Users\Simeon\Documents\GitHub\1-simeononsecurity.ch\tools\pngcrush.exe" -ArgumentList "-ow", "-fix", $inputFilePath, $outputFilePath -NoNewWindow -PassThru

        if ($process.ExitCode -eq 0) {
            Write-Host "Fixed: $($file.Name)"
        } else {
            Write-Host "Error fixing $($file.Name): Exit code $($process.ExitCode)"
        }
    }
    catch {
        Write-Host "Error fixing $($file.Name): $_"
    }
}

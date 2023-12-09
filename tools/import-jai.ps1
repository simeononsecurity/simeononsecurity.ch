# Function to recursively rename content.md to index.en.md
function Rename-ContentFiles {
    param (
        [string]$folderPath
    )

    # Get all content.md files within the folder
    $contentFiles = Get-ChildItem -Path $folderPath -Recurse -Filter 'content.md'

    # Rename each content.md file to "index.en.md"
    foreach ($file in $contentFiles) {
        $newFileName = Join-Path -Path $file.DirectoryName -ChildPath "index.en.md"
        $file | Rename-Item -NewName $newFileName -Force
    }
}

# Function to recursively rename thumbnail.jpeg to the folder name and copy to destination
function Rename-And-Copy-Thumbnail {
    param (
        [string]$folderPath,
        [string]$destinationPath
    )

    # Get all thumbnail.jpeg files within the folder
    $thumbnailFiles = Get-ChildItem -Path $folderPath -Recurse -Filter 'thumbnail.jpeg'

    # Rename each thumbnail.jpeg file to the folder name and copy to destination
    foreach ($file in $thumbnailFiles) {
        $newFileName = Join-Path -Path $file.DirectoryName -ChildPath "$($file.Directory.Name).jpeg"
        $file | Rename-Item -NewName $newFileName -Force
        Copy-Item -Path $newFileName -Destination $destinationPath -Force
    }
}

$folders = Get-ChildItem

# Iterate through each folder
foreach ($folder in $folders) {
    # Extract the folder name by removing the first 6 characters
    $newFolderName = $folder.Name.Substring(6)
    
    # Convert the folder name to lowercase and replace spaces with dashes
    $newFolderName = $newFolderName.ToLower().Replace(' ', '-')
    
    # Set the new folder name
    $folder | Rename-Item -NewName $newFolderName -Force
}

# Get the list of folders in the specified directory
$folders = Get-ChildItem

foreach ($folder in $folders) {
    # Rename content.md files within the folder and its subfolders
    Rename-ContentFiles -folderPath $folder

    # Rename thumbnail.jpeg files and copy to destination
    Rename-And-Copy-Thumbnail -folderPath $folder -destinationPath ''
}

# Set the root folder path
$rootFolderPath = Get-Location

# Get all index.en.md files recursively
$mdFiles = Get-ChildItem -Path $rootFolderPath -Filter "index.en.md" -Recurse

# Set the initial date
$currentDate = Get-Date "2024-03-11"

foreach ($file in $mdFiles) {

    # Read the original content
    $originalContent = Get-Content $file.FullName -Raw

    # Update date and cover path
    $frontMatter = @"
---
title: ""
date: $($currentDate.ToString("yyyy-MM-dd"))
toc: true
draft: false
description: ""
genre: []
tags: []
cover: "/img/cover/$($file.Directory.Name).jpeg"
---


"@

    # Combine front matter and original content
    $newContent = $frontMatter + $originalContent

    # Write the combined content back to the file
    $newContent | Set-Content $file.FullName

    # Increment the date for the next file
    $currentDate = $currentDate.AddDays(1)
}

# Display the updated directory structure
Get-ChildItem -Recurse


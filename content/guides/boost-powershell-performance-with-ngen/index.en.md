---
title: "Boost PowerShell Performance: Harness Ngen for Effortless Speed"
date: 2023-11-26
toc: true
draft: false
description: "Learn how to supercharge PowerShell startup and execution with Ngen, enhancing performance effortlessly."
genre: ["Technology", "Software Optimization", "PowerShell Tips", "Performance Improvement", "Scripting", "Native Image Generation", "Command Line", "IT Efficiency", "Developer Tools", "Coding Techniques"]
tags: ["Improve PowerShell Speed", "Boost Script Execution", "Optimize PowerShell Performance", "Ngen Tutorial", "Enhance PowerShell Efficiency", "Pre-Compile Assemblies", "PowerShell Tips and Tricks", "PowerShell Performance Hacks", "Native Image Generation Benefits", "Scripting Best Practices", "PowerShell", "Ngen", "Native Image Generator", "Performance Optimization", "Scripting", "PowerShell Assemblies", "Startup Time", "Efficient Coding", "Developer Tools", "Command Line"]
cover: "/img/cover/boost-efficiency-rocket.png"
coverAlt: "A rocket speeding ahead of a computers terminal window with code on it."
coverCaption: "Unlock Efficiency"
---
**Using Ngen to Pre-Emptively Create Native Images for the Assemblies That PowerShell Relies On**

In the realm of optimizing **PowerShell's performance**, one often-overlooked technique is the use of **Ngen, the Native Image Generator**. This powerful tool can significantly enhance the **startup time** and **execution speed** of PowerShell scripts. In this article, we'll explore what **Ngen** is, how it works, and why it's beneficial for **PowerShell**. Let's dive in.

## What is Ngen?
**Ngen** stands for **Native Image Generator**, and it's a critical component of the **.NET Framework**. Its primary purpose is to create **native images** from managed assemblies. But what exactly does that mean?

When you run a **.NET application**, such as **PowerShell**, it typically involves compiling **CIL (Common Intermediate Language) code** into machine code during runtime. This **just-in-time (JIT) compilation** adds a small overhead to the application's **startup time**. **Ngen eliminates this overhead by pre-compiling the CIL code into native machine code**. Essentially, it's like translating a book from one language to another ahead of time, making it ready for immediate consumption.

## Why Does PowerShell Need Ngen?
**PowerShell** relies on various assemblies and libraries to function properly. These assemblies contain the code that makes PowerShell work, but they are initially in **CIL format**. Without **Ngen**, PowerShell would have to compile this code every time it starts, which can be **time-consuming**.

By using **Ngen** to pre-emptively create **native images** for the assemblies that **PowerShell relies on**, we can achieve a **significant boost in performance**. Here's why it matters:

### 1. Faster Startup Times
When you open **PowerShell**, you want it to be ready for action as quickly as possible. **Ngen** helps achieve this by **reducing the time** it takes to load and initialize **essential assemblies**.

### 2. Improved Script Execution
If you frequently run **PowerShell scripts**, you'll notice that they execute **faster** with **Ngen**. The **pre-compiled native images** allow scripts to start running **immediately** without the **JIT compilation overhead**.

### 3. Consistent Performance
With **Ngen**, the performance of **PowerShell** remains **consistent** over time. You won't experience **slowdowns** due to **JIT compilation**, especially when dealing with **complex** or **lengthy scripts**.

## How to Use Ngen with PowerShell
Using Ngen with PowerShell is relatively straightforward, but it does require administrative privileges. Here are the steps:

1. **Open PowerShell as an Administrator:** Right-click on the PowerShell icon and choose "Run as administrator."

2. **Optimize Assemblies:** You can use the [`Optimize-PowershellAssemblies`](https://docs.ansible.com/ansible/latest/os_guide/windows_performance.html#optimize-powershell-performance-to-reduce-ansible-task-overhead) script we discussed earlier, or you can manually optimize assemblies using the following commands:
   
    ```powershell
        function Optimize-PowershellAssemblies {
        # NGEN powershell assembly, improves startup time of powershell by 10x
        $old_path = $env:path
        try {
            $env:path = [Runtime.InteropServices.RuntimeEnvironment]::GetRuntimeDirectory()
            [AppDomain]::CurrentDomain.GetAssemblies() | % {
            if (! $_.location) {continue}
            $Name = Split-Path $_.location -leaf
            if ($Name.startswith("Microsoft.PowerShell.")) {
                Write-Progress -Activity "Native Image Installation" -Status "$name"
                ngen install $_.location | % {"`t$_"}
            }
            }
        } finally {
            $env:path = $old_path
        }
        }
        Optimize-PowershellAssemblies
    ```
   1. (Optional) **Optimize All Installed Assemblies**
        Optionally, you can also optimize all Microsoft Assemblies for additional performance gains both inside and outside of PowerShell.
        ```powershell
            $ErrorActionPreference = 'Stop'

            Function Get-SystemArchitecture {
                $isWow64 = Get-WmiObject -Query "SELECT * FROM Win32_ComputerSystem" | ForEach-Object {
                    $_.SystemType -match "x64"
                }

                if ($isWow64) {
                    return "64"
                } else {
                    return "32"
                }
            }

            Function Invoke-Ngen {
                $architecture = Get-SystemArchitecture
                $cmd = "$($env:windir)\Microsoft.NET\Framework$($architecture)\v4.0.30319\ngen.exe"

                if (Test-Path -LiteralPath $cmd) {
                    $arguments = "update /queue /force"
                    try {
                        $ngen_result = Invoke-Expression "$cmd $arguments"
                    }
                    catch {
                        Write-Error "Failed to execute '$cmd $arguments': $($_.Exception.Message)"
                    }

                    $arguments = "executeQueuedItems"
                    try {
                        $executed_queued_items = Invoke-Expression "$cmd $arguments"
                    }
                    catch {
                        Write-Error "Failed to execute '$cmd $arguments': $($_.Exception.Message)"
                    }
                    $executed_queued_items
                }
            }

            # Invoke Ngen with automatically detected architecture
            Invoke-Ngen
        ```

3. **Monitor Progress**
Ngen will display progress as it generates native images for the specified assemblies.

1. **Restart PowerShell**
After optimizing the assemblies, close and reopen PowerShell to enjoy the benefits of improved performance.

## Conclusion
In the world of **PowerShell optimization**, **Ngen** is a **valuable tool** that often flies under the radar. By **pre-emptively creating native images** for the assemblies that **PowerShell relies on**, you can **significantly enhance its startup time and overall performance**. This optimization technique is particularly beneficial for those who **frequently work with PowerShell scripts**.

Incorporating **Ngen** into your **PowerShell workflow** is a **simple yet powerful step** towards a **smoother** and **more efficient experience**. Give it a try, and you'll notice the **difference in performance**.

## References
- [Native Image Generator (Ngen.exe)](https://learn.microsoft.com/en-us/dotnet/framework/tools/ngen-exe-native-image-generator#WhenToUse)
- [Microsoft .NET Framework](https://dotnet.microsoft.com/)
- [Common Intermediate Language (CIL)](https://en.wikipedia.org/wiki/Common_Intermediate_Language)
- [Understanding JIT Compilation in .NET](https://docs.microsoft.com/en-us/dotnet/standard/managed-code)
- [PowerShell Documentation](https://docs.microsoft.com/en-us/powershell/)
- [Optimize PowerShell performance to reduce Ansible task overhead](https://docs.ansible.com/ansible/latest/os_guide/windows_performance.html#optimize-powershell-performance-to-reduce-ansible-task-overhead)
- 
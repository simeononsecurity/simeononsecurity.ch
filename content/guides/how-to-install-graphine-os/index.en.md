---
title: "Ultimate Guide: Installing GrapheneOS on Your Google Pixel Device"
draft: false
toc: true
date: 2023-05-21
lastmod: 2026-05-24
description: "Learn how to install GrapheneOS on your Google Pixel device for enhanced privacy and security using the web installer or CLI method."
tags: ["GrapheneOS", "Google Pixel", "privacy", "security", "Android", "mobile devices", "operating system", "installation guide", "custom ROM", "privacy-focused", "data protection", "secure OS", "open-source", "device security", "privacy features", "personal data", "mobile privacy", "data privacy", "device customization", "technology", "Pixel installation", "privacy-focused operating system", "GrapheneOS installation", "mobile security", "privacy and security", "Pixel device customization", "privacy enhancements", "data protection guide", "secure operating system", "Pixel privacy features", "mobile data privacy", "fastboot", "bootloader", "verified boot", "Pixel 10", "Pixel 9"]
cover: "/img/cover/A_colorful_cartoon_illustration_showcasing_a_Google_Pixel.png"
coverAlt: "A colorful cartoon illustration showcasing a Google Pixel device with a shield symbolizing enhanced privacy and security features."
coverCaption: ""
---

**How to Install GrapheneOS on Your Google Pixel Device**

GrapheneOS is an open-source, privacy-focused operating system based on Android. It offers significantly enhanced security hardening and privacy protections, making it an excellent choice for anyone concerned about data privacy and security. If you own a supported Google Pixel device and want to switch to GrapheneOS, this guide covers both the recommended **web installer** method and the traditional **command-line (CLI)** method.

> **Tip:** If you have trouble with the installation process, ask for help on the [official GrapheneOS chat channel](https://grapheneos.org/contact#community). Before asking for help, make an attempt to follow the guide on your own and then ask for help with anything you get stuck on.

## Prerequisites

### Hardware & System Requirements

- A computer with at least **2GB of free memory** and **32GB of free storage space**.
- A **high-quality USB-C cable** packaged with the device (or a USB-C to USB-A cable if needed). Avoid USB hubs - connect directly to a rear desktop port or laptop port.
- Installing from a virtual machine is **not recommended** due to unreliable USB passthrough.

> It's best practice to update your Pixel device before installing GrapheneOS to have the latest firmware. Either way, GrapheneOS flashes the latest firmware early in the installation process.

### Officially Supported Operating Systems

#### Web Installer

- Windows 10 / Windows 11
- macOS Sonoma (14), macOS Sequoia (15), macOS Tahoe (26)
- Arch Linux
- Debian 12 (bookworm), Debian 13 (trixie)
- Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, Ubuntu 25.04
- Linux Mint 21 (follow Ubuntu 22.04 LTS instructions), Linux Mint 22 (follow Ubuntu 24.04 LTS instructions)
- Linux Mint Debian Edition 6 (follow Debian 12 instructions)
- ChromeOS
- GrapheneOS
- Android 13, 14, 15, and 16 with Play Protect certification

#### CLI Method

All of the above except ChromeOS, GrapheneOS, and Android (which can only use the web installer).

Older end-of-life versions of these platforms can also be used but are not officially supported. **Make sure your operating system is up-to-date before proceeding.**

### Officially Supported Browsers (Web Installer Only)

- **Chromium** (outside Ubuntu - their Snap package lacks working WebUSB)
- **Vanadium** (GrapheneOS)
- **Google Chrome**
- **Microsoft Edge**
- **Brave** (with Brave Shields disabled - it caps storage usage to avoid fingerprinting)

> - On Android, **disable desktop mode** in your browser. Desktop mode prevents the web installer from detecting Android and requesting reconnect permission after reboots. It is enabled by default on large tablets with 8GB+ RAM (e.g., Pixel Tablet).
> - Avoid Flatpak and Snap browser versions - they cause issues during installation.
> - Do **not** use Incognito / private browsing mode - these modes restrict storage space needed to extract the downloaded release.

### Supported Devices

You need one of the [officially supported Pixel devices](https://grapheneos.org/faq#supported-devices). **Avoid carrier variants** - carrier Pixels have a non-zero carrier ID flashed at the factory that disables bootloader and carrier unlocking. Get a carrier-agnostic (unlocked) device.

---

## Enabling OEM Unlocking

OEM unlocking must be enabled from within the operating system before you can proceed.

1. Go to **Settings → About phone/tablet** and repeatedly tap **Build number** until developer mode is enabled.
2. Go to **Settings → System → Developer options** and toggle on **OEM unlocking**. On some carrier-capable SKUs, this requires an active internet connection so the stock OS can verify the device was not sold as a carrier-locked unit.

> **Pixel 6a note:** OEM unlocking won't work with the factory stock OS version. Update to the **June 2022** release or later via OTA, then perform a factory reset to fix OEM unlocking.

---

## Installation Method 1: Web Installer (Recommended)

The [GrapheneOS Web Installer](https://grapheneos.org/install/web) is the recommended approach for most users. It uses WebUSB directly in your browser - no software installation required.

### Step 1: Work Around fwupd Bugs (Linux Only)

On Linux, `fwupd` is known to incorrectly connect to devices using the fastboot protocol, blocking the installer. Stop it before connecting your device:

```bash
sudo systemctl stop fwupd.service
```

This won't persist across reboots.

### Step 2: Set Up udev Rules (Linux Only)

On Arch Linux:

```bash
sudo pacman -S android-udev
```

On Debian and Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Step 3: Boot into Bootloader Interface

Hold the **volume down** button while the device boots (either power it on from off while holding volume down, or reboot and hold volume down). The device must display a **red warning triangle** and the words **"Fastboot Mode"** - do not press the power button to activate "Start."

### Step 4: Connect Your Device

Connect the device to your computer via USB. On Linux, reconnect the cable if udev rules weren't set up before the first connection.

> **Pixel Tablet:** Disconnect from the stand before connecting via USB - the tablet can't use both simultaneously.

> **Windows:** Current Windows 10/11 include a generic fastboot driver for Pixel 4a (5G) and later. For older Pixels or outdated Windows, install the driver from Windows Update (look under "View optional updates" → "LeMobile Android Device").

### Step 5: Unlock the Bootloader

Go to [https://grapheneos.org/install/web](https://grapheneos.org/install/web) and click the **Unlock the bootloader** button. Confirm on the device using the volume buttons to switch selection and the power button to confirm. **This wipes all data.**

### Step 6: Obtain and Flash Factory Images

1. Click **Download release** to download the factory images for your device.
2. Click **Flash factory images** and wait for the process to complete. It will automatically flash firmware, reboot into the bootloader interface, and flash the OS. **Do not interact with the device until finished.**

### Step 7: Lock the Bootloader

After flashing, click **Lock the bootloader** in the web installer. Confirm on-device. **This wipes all data again** - locking the bootloader enables full verified boot.

---

## Installation Method 2: Command-Line (CLI)

### Step 1: Open a Terminal

On Windows, open a **regular (non-administrator) PowerShell** window. Remove the legacy `curl` alias:

```powershell
Remove-Item Alias:Curl
```

### Step 2: Install fastboot

You need fastboot version **≥ 35.0.1**.

**Arch Linux:**

```bash
sudo pacman -S android-tools
```

**Debian / Ubuntu** - their packages are outdated. Use the standalone release:

```bash
# Debian / Ubuntu
sudo apt install libarchive-tools
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-linux.zip
echo 'acfdcccb123a8718c46c46c059b2f621140194e5ec1ac9d81715be3d6ab6cd0a  platform-tools_r35.0.2-linux.zip' | sha256sum -c
bsdtar xvf platform-tools_r35.0.2-linux.zip
export PATH="$PWD/platform-tools:$PATH"
```

**macOS:**

```bash
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-darwin.zip
echo 'SHA256 (platform-tools_r35.0.2-darwin.zip) = 1820078db90bf21628d257ff052528af1c61bb48f754b3555648f5652fa35d78' | shasum -c
tar xvf platform-tools_r35.0.2-darwin.zip
export PATH="$PWD/platform-tools:$PATH"
```

**Windows:**

```powershell
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-win.zip
(Get-FileHash platform-tools_r35.0.2-win.zip).hash -eq "2975a3eac0b19182748d64195375ad056986561d994fffbdc64332a516300bb9"
tar xvf platform-tools_r35.0.2-win.zip
$env:Path = "$pwd\platform-tools;$env:Path"
```

Verify your version:

```bash
fastboot --version
# Expected: fastboot version 35.0.2-12147458
```

### Step 3: Set Up udev Rules (Linux Only)

Arch Linux:

```bash
sudo pacman -S android-udev
```

Debian / Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Step 4: Work Around fwupd Bugs (Linux Only)

```bash
sudo systemctl stop fwupd.service
```

### Step 5: Boot into Bootloader Interface

Hold **volume down** while booting until the device shows **"Fastboot Mode"** with the red warning triangle.

### Step 6: Connect and Unlock the Bootloader

Connect via USB, then run:

```bash
fastboot flashing unlock
```

Confirm on-device (volume buttons to switch selection, power button to confirm). **This wipes all data.**

### Step 7: Install OpenSSH (for image verification)

macOS and Windows include OpenSSH by default.

Arch Linux:

```bash
sudo pacman -S openssh
```

Debian / Ubuntu:

```bash
sudo apt install openssh-client
```

### Step 8: Download and Verify Factory Images

Download the signing key:

```bash
curl -O https://releases.grapheneos.org/allowed_signers
```

Expected content:

```
contact@grapheneos.org ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIUg/m5CoP83b0rfSCzYSVA4cw4ir49io5GPoxbgxdJE
```

Download the factory images (replace `DEVICE_NAME` and `VERSION` with actual values):

```bash
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip.sig
```

Verify the signature (Linux / macOS):

```bash
ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" \
  -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip
```

Windows:

```powershell
cmd /c 'ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip'
```

Expected output:

```
Good "factory images" signature for contact@grapheneos.org with ED25519 key SHA256:AhgHif0mei+9aNyKLfMZBh2yptHdw/aN7Tlh/j2eFwM
```

### Step 9: Flash Factory Images

Extract the images:

```bash
# Linux
bsdtar xvf DEVICE_NAME-install-VERSION.zip

# macOS / Windows
tar xvf DEVICE_NAME-install-VERSION.zip
```

Enter the directory and run the flash script:

```bash
cd DEVICE_NAME-install-VERSION

# Linux / macOS
bash flash-all.sh

# Windows
./flash-all.bat
```

Wait for the process to finish. It handles firmware flashing, bootloader reboots, and OS flashing automatically. **Do not interact with the device until it completes.**

> **Linux tmpfs troubleshooting:** If `/tmp` doesn't have enough space, use:
> ```bash
> mkdir tmp && TMPDIR="$PWD/tmp" ./flash-all.sh
> ```

### Step 10: Lock the Bootloader

```bash
fastboot flashing lock
```

Confirm on-device. **This wipes all data again.** Locking enables full verified boot and prevents fastboot from modifying partitions.

---

## Post-Installation

### Booting

Press the power button with the default **Start** option selected in the bootloader interface to boot GrapheneOS.

### Disabling OEM Unlocking

During first setup, the final screen contains a toggle for OEM unlocking (checked by default - leaving it checked **disables** OEM unlocking). This is recommended. You can change it later in **Developer options**.

### Verifying the Installation

GrapheneOS leverages verified boot and hardware attestation. Verified boot checks all firmware and OS images on every boot against keys burned into the SoC fuses. GrapheneOS flashes its own verified boot public key to the secure element - each boot, this key verifies the OS.

#### Verified Boot Key Hashes

When an alternate OS is loaded, the device shows a **yellow notice** with the OS identifier (sha256 of the verified boot key). 4th and 5th generation Pixels only display the first 32 bits; **6th generation Pixels onwards show the full hash**. Compare against the official hashes:

| Device | Verified Boot Key Hash |
|--------|----------------------|
| Pixel 10a | `d8f879d10419eddc9fcda6280718be763f6bf12299e1f72df3ea8ad8a8eb7f80` |
| Pixel 10 Pro Fold | `55a2d44103e56d5ec65496399c417987ba77730e6488fc60ba058d09fc3caee3` |
| Pixel 10 Pro XL | `141d7fc32af7958a416f2661b37cf6f27bfb376fb5ce616aeaa27a82c7a04f74` |
| Pixel 10 Pro | `4e8ee8f717754052198ca6d2d3aaa232e2461b4293c0d6f297e519cc778de093` |
| Pixel 10 | `3f7415ea26f5df5b14ea6d153256071a7a1af9ce7b0970b7311cc463c7ea02c7` |
| Pixel 9a | `0508de44ee00bfb49ece32c418af1896391abde0f05b64f41bc9a2dfb589445b` |
| Pixel 9 Pro Fold | `af4d2c6e62be0fec54f0271b9776ff061dd8392d9f51cf6ab1551d346679e24c` |
| Pixel 9 Pro XL | `55d3c2323db91bb91f20d38d015e85112d038f6b6b5738fe352c1a80dba57023` |
| Pixel 9 Pro | `f729cab861da1b83fdfab402fc9480758f2ae78ee0b61c1f2137dd1ab7076e86` |
| Pixel 9 | `9e6a8f3e0d761a780179f93acd5721ba1ab7c8c537c7761073c0a754b0e932de` |
| Pixel 8a | `096b8bd6d44527a24ac1564b308839f67e78202185cbff9cfdcb10e63250bc5e` |
| Pixel 8 Pro | `896db2d09d84e1d6bb747002b8a114950b946e5825772a9d48ba7eb01d118c1c` |
| Pixel 8 | `cd7479653aa88208f9f03034810ef9b7b0af8a9d41e2000e458ac403a2acb233` |
| Pixel Fold | `ee0c9dfef6f55a878538b0dbf7e78e3bc3f1a13c8c44839b095fe26dd5fe2842` |
| Pixel Tablet | `94df136e6c6aa08dc26580af46f36419b5f9baf46039db076f5295b91aaff230` |
| Pixel 7a | `508d75dea10c5cbc3e7632260fc0b59f6055a8a49dd84e693b6d8899edbb01e4` |
| Pixel 7 Pro | `bc1c0dd95664604382bb888412026422742eb333071ea0b2d19036217d49182f` |
| Pixel 7 | `3efe5392be3ac38afb894d13de639e521675e62571a8a9b3ef9fc8c44fd17fa1` |
| Pixel 6a | `08c860350a9600692d10c8512f7b8e80707757468e8fbfeea2a870c0a83d6031` |
| Pixel 6 Pro | `439b76524d94c40652ce1bf0d8243773c634d2f99ba3160d8d02aa5e29ff925c` |
| Pixel 6 | `f0a890375d1405e62ebfd87e8d3f475f948ef031bbf9ddd516d5f600a23677e8` |

#### Hardware-Based Attestation with Auditor

GrapheneOS provides the [Auditor app](https://attestation.app/) to verify hardware, firmware, and OS integrity using verified boot and remote attestation. Results are shown on a second Android device running Auditor (not on the device being verified), or via the optional [device integrity monitoring service](https://attestation.app/) for automatic scheduled verifications with email alerts.

---

## Replacing GrapheneOS with the Stock OS

Installation of the stock OS via Google's [web flashing tool](https://flash.android.com/) is similar to the process above. However, before flashing and locking, you must erase the GrapheneOS verified boot key to fully revert to stock:

**Web installer:** Use the "Erase non-stock key" button on the GrapheneOS web installer.

**CLI:**

```bash
fastboot erase avb_custom_key
```

Then flash the stock factory images and lock the bootloader.

---

## Conclusion

Installing GrapheneOS on your Google Pixel device provides industry-leading privacy and security features. Use the **web installer** at [grapheneos.org/install/web](https://grapheneos.org/install/web) for the easiest experience, or follow the CLI steps above for a traditional approach. Always lock the bootloader after flashing to enable full verified boot, and optionally use the Auditor app to confirm the integrity of your installation.

## References

1. [GrapheneOS Website](https://grapheneos.org/)
2. [GrapheneOS Web Installer](https://grapheneos.org/install/web)
3. [GrapheneOS CLI Install Guide](https://grapheneos.org/install/cli)
4. [GrapheneOS Releases](https://grapheneos.org/releases)
5. [GrapheneOS Usage Guide](https://grapheneos.org/usage)
6. [GrapheneOS FAQ](https://grapheneos.org/faq)
7. [Auditor App](https://attestation.app/)
8. [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools)

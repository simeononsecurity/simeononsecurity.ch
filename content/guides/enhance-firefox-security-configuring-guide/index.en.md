---
title: "Mozilla FireFox STIG and Hardening: Complete Guide for Configuring Safe Browsing"
date: 2023-11-02
toc: true
draft: false
description: "Boost security with comprehensive Firefox configurations for safe browsing, adhering to compliance standards."
genre: ["Technology", "Cybersecurity", "Internet", "Browsers", "Information Security", "Web Safety", "Digital Privacy", "Network Security", "IT Security", "Web Browsing"]
tags: ["Firefox Security", "Secure Browsing", "Cybersecurity", "Browser Configurations", "Compliance Guide", "Web Safety", "Information Security", "IT Security", "Online Privacy", "Network Security", "Browsing Tips", "Security Measures", "Digital Security", "Internet Safety", "STIG", "Mozilla Firefox", "Online Security", "Hardening Configuration", "Privacy Enhancements", "Data Protection", "Safe Internet", "Web Security", "Browser Settings", "Security Guidelines", "Security Best Practices", "Browser Privacy", "Security Compliance", "Secure Web Surfing", "Online Threats", "Web Security Tips", "Browser Security"]
cover: "/img/cover/Secure_Browsing_Lock_Symbol.png"
coverAlt: "Secure Browsing with Lock Symbol with FireFox Colors Purple and Orange"
coverCaption: "Navigate Fearlessly: Your Guide to Enhanced Browser Security"
---

**Configuring Secure Firefox Settings: A Compliance Guide**

In the realm of cybersecurity, maintaining a secure browsing environment is paramount. This article delves into key configurations for Mozilla Firefox, addressing various findings aimed at bolstering security while adhering to administrative requirements.

______

## Introduction

In the digital age, browser security is crucial, especially in sensitive environments. This guide outlines critical configurations for **Mozilla Firefox** to ensure optimal security and compliance.

______

{{< inarticle-dark >}}

______

## Implementing Hardening Configuration for Firefox

To achieve the security enhancements required by the Security Technical Implementation Guides (STIGs), follow these steps to configure Firefox settings and install the necessary files.

### Automation Script

SimeonOnSecurity has developed both PowerShell and Bash based [FireFox STIG Scripts](https://github.com/simeononsecurity/FireFox-STIG-Script/tree/master). 
Click the link above to learn more.

### GPO Methods

The new Mozilla FireFox STIG revision includes some new configurations. Not all of the STIG can be accomplished with GPO, especially on Linux distros, so that is why we prefer to just do it with the mozilla .cfg files. However if you wish to do it that way and are wondering why some of those options don't show up in group policy, it's because you need the [Mozilla Firefox ADMX Templates](https://github.com/mozilla/policy-templates/releases). You'll extract the files from that link and install them into `%systemroot%\Policydefinitions` for Local GPO and for domain level gpo, you'll need to install them into your [central policy store](https://learn.microsoft.com/en-us/troubleshoot/windows-client/group-policy/create-and-manage-central-store).

### Applying Configuration Settings

#### Creating Mozilla.cfg Configuration File

The `mozilla.cfg` file contains various configuration settings that enforce security measures in Firefox. These settings address multiple security findings and strengthen the browser's defenses against potential threats.

1. **Create or Modify mozilla.cfg**: Open the `mozilla.cfg` file and add the provided lockPref entries for each security finding. This will enforce the specified configurations in Firefox.

   Example `mozilla.cfg`:
   ```cfg
   // SV-223179 - DTBG010
   lockPref("security.enterprise_roots.enabled", true);
   // SV-16707 - DTBF050
   lockPref("security.default_personal_cert", "Ask Every Time");
   // ... (other lockPref entries)
   ```
    See a full and [working example of a STIG'ed mozilla.cfg](https://github.com/simeononsecurity/FireFox-STIG-Script/blob/master/Files/Config/mozilla.cfg).

2. Place `mozilla.cfg` in Firefox Directory: Save the modified `mozilla.cfg` file in the appropriate directory based on your operating system. On Windows, you can place it in the Firefox installation folder, and on Linux, you can place it in the appropriate directory structure.

3. Download or create an equivalent [`autoconfig.js`](https://github.com/simeononsecurity/FireFox-STIG-Script/blob/master/Files/Config/browser/defaults/preferences/autoconfig.js)

    ```js
    //
    pref("general.config.filename", "mozilla.cfg");
    pref("general.config.obscure_value", 0);
    ```

#### Installing Configuration Files

##### Windows
Please place the created `mozilla.cfg` file in one of the appropriate directories

- **64 Bit**: `C:\Program Files\Mozilla Firefox`
- **32 Bit**: `C:\Program Files (x86)\Mozilla Firefox`

We'll also be creating an `autoconfig.js` file which goes into

- **64 Bit**: `C:\Program Files\Mozilla Firefox\browser\defaults\preferences\`
- **32 Bit**: `C:\Program Files (x86)\Mozilla Firefox\browser\defaults\preferences\`

##### Linux 

Please place the created `mozilla.cfg` file the appropriate directories

- `/lib/firefox/`

We'll also be creating an `autoconfig.js` file which goes into

- `/lib/firefox/browser/defaults/preferences/`
______

## STIG - Mozilla.cfg

### Finding ID: V-251546 - Enabling Strong TLS Encryption

**Transport Layer Security (TLS)** is fundamental for secure communication online. **Configure Firefox to allow only TLS 1.2 or above**, as earlier versions like SSL 2.0 and SSL 3.0 harbor vulnerabilities. This aligns with stringent security standards and the need to disable outdated protocols. 

```js
// SV-16925 - DTBF030
lockPref("security.enable_tls", true);
// SV-16925 - DTBF030
lockPref("security.tls.version.min", 2);
// SV-16925 - DTBF030
lockPref("security.tls.version.max", 4);
```

______

### Finding ID: V-251545 - Supported Firefox Versions

Using unsupported browser versions poses security risks. **Maintain a supported Firefox version** to benefit from vendor-supplied patches and updates addressing security vulnerabilities. This practice mitigates potential security gaps and ensures an up-to-date browser. 

#### Linux (Ubuntu) Script using APT
```bash
#!/bin/bash

# Update the package list
sudo apt update

# Install Firefox
sudo apt install firefox -y

# Update Firefox
sudo apt upgrade firefox -y

echo "Firefox installation and update complete."
```

#### Windows Script using Chocolatey

```powershell
# Install or update Chocolatey (if not already installed)
if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
}

# Install or update Firefox using Chocolatey
choco install firefox -y

echo "Firefox installation and update complete."
```
______

{{< inarticle-dark >}}

______

### Finding ID: V-251567 - Protecting Against Fingerprinting

Enable **Firefox's fingerprinting protection** through Content Blocking/Tracking Protection. This shields against malicious content loading from websites, safeguarding user privacy. Take measures to prevent websites from tracking users' online activities. 


```js
// SV-111841 - DTBF210
lockPref("privacy.trackingprotection.fingerprinting.enabled", true);
```
______

### Finding ID: V-252881 - Retaining Data Upon Shutdown

For diagnostics, it's essential to maintain data when the browser closes. This practice aligns with non-repudiation controls, ensuring data accountability even after browser sessions.

```js
// V-252881 - Retaining Data Upon Shutdown
lockPref("browser.sessionstore.privacy_level", 0);
```
______

{{< inarticle-dark >}}

______

## Secure Configuration and Privacy Enhancements

Firefox can be further configured to enhance security and protect user privacy. 

### Finding ID: V-251573 - Customizing the New Tab Page

Prevent the New Tab page from displaying **Top Sites, Sponsored Recommendations, and Snippets**. Limiting exposure to potentially insecure sites ensures a focused and secure browsing experience.

```js
// SV-251573 - Customizing the New Tab Page
lockPref("browser.newtabpage.activity-stream.enabled", false);
lockPref("browser.newtabpage.activity-stream.feeds.section.topstories", false);
lockPref("browser.newtabpage.activity-stream.showSponsored", false);
lockPref("browser.newtabpage.activity-stream.feeds.snippets", false);
```

### Finding ID: V-251580 - Disabling Feedback Reporting

Disable Firefox's feedback reporting menus to minimize unnecessary functionality and reduce the risk of information leakage.

```js
// V-251580 - Disabling Feedback Reporting
lockPref("browser.chrome.toolbar_tips", false);
lockPref("browser.selfsupport.url", "");
lockPref("extensions.abuseReport.enabled", false);
lockPref("extensions.abuseReport.url", "");
```

### Finding ID: V-251558 - Controlling Data Submission

Prevent background data submission to Mozilla servers, ensuring sensitive information stays within the organization's secure perimeter.

```js
// V-251558 - Controlling Data Submission
lockPref("datareporting.policy.dataSubmissionEnabled", false);
lockPref("datareporting.healthreport.uploadEnabled", false);
lockPref("datareporting.policy.firstRunURL", "");
lockPref("datareporting.policy.notifications.firstRunURL", "");
lockPref("datareporting.policy.requiredURL", "");
```

### Finding ID: V-252909 - Disabling Firefox Studies

In a DoD context, disable Firefox Studies to prevent the inadvertent exposure of beta software that doesn't align with the user's mission.

```js
// V-252909 - Disabling Firefox Studies
lockPref("app.shield.optoutstudies.enabled", false);
lockPref("app.normandy.enabled", false);
lockPref("app.normandy.api_url", "");
```

### Finding ID: V-252908 - Disabling Pocket

Disable **Pocket**, a cloud-based bookmarking service, to mitigate the risks associated with data gathering services in sensitive environments.

```js
// V-252908 - Disabling Pocket
lockPref("extensions.pocket.enabled", false);
```

______

{{< inarticle-dark >}}

______

## Secure Browsing Practices and User Privacy

Enhancing user privacy and security involves configuring Firefox to prevent potential vulnerabilities.

### Finding ID: V-251555 - Preventing Improper Script Execution

Configure Firefox to prevent JavaScript from raising or lowering browser windows without user consent. This safeguards against potential attacks leveraging improper input.

```js
// V-251555 - Preventing Improper Script Execution
lockPref("dom.disable_window_flip", true);
```

### Finding ID: V-251554 - Restricting Window Movement and Resizing

Prevent JavaScript from altering the browser's appearance and disguising attacks by configuring Firefox to prevent scripts from moving or resizing windows.

```js
// V-251554 - Restricting Window Movement and Resizing
lockPref("dom.disable_window_move_resize", true);
```

### Finding ID: V-251557 - Disabling Extension Installation

Configure Firefox to disable extension installation, reducing the risk of introducing potentially malicious or unauthorized functionality.

```js
// V-251557 - Disabling Extension Installation
lockPref("xpinstall.enabled", false);
```

### Finding ID: V-251551 - Disabling Form Fill Assistance

Enhance user privacy by configuring Firefox to disable the storage of form data, mitigating the risk of websites collecting sensitive information.

```js
// V-251551 - Disabling Form Fill Assistance
lockPref("browser.formfill.enable", false);
```

### Finding ID: V-251550 - Blocking Unauthorized MIME Types

Prevent automatic execution or download of unauthorized MIME types, enhancing security by reducing the potential for malicious file execution.

```js
// V-251550 - Blocking Unauthorized MIME Types
lockPref("plugin.disable_full_page_plugin_for_types", "application/pdf,application/fdf,application/xfdf,application/lso,application/lss,application/iqy,application/rqy,application/lsl,application/xlk,application/xls,application/xlt,application/pot,application/pps,application/ppt,application/dos,application/dot,application/wks,application/bat,application/ps,application/eps,application/wch,application/wcm,application/wb1,application/wb3,application/rtf,application/doc,application/mdb,application/mde,application/wbk,application/ad,application/adp");
```

______

{{< inarticle-dark >}}

______

## Conclusion

Properly configuring Mozilla Firefox in accordance with these findings is pivotal in maintaining a secure browsing environment. From strong encryption protocols to privacy-enhancing configurations, Firefox can be tailored to align with security standards and administrative requirements.

______

## References

1. [Supported Firefox Versions](https://www.mozilla.org/en-US/firefox/organizations/all/#legacy)
2. [Firefox Content Blocking](https://support.mozilla.org/en-US/kb/content-blocking)
3. [Configure Firefox Privacy Settings](https://support.mozilla.org/en-US/kb/settings-privacy-browsing-history-do-not-track)
4. [Mozilla Firefox Developer Guide](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox)
5. [Mozilla Security Blog](https://blog.mozilla.org/security/)
6.  [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
7.  [Cyber.mil - DoD STIGs](https://public.cyber.mil/stigs/)

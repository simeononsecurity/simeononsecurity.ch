---
title: "Brave ADMX Templates"
date: 2020-07-25T19:30:39-05:00
draft: true
---

# BraveADMX

Brave, as a company, has failed to release ADMX templates for the brave browser siteing pushing pure registries as the only supported option.
As the Brave Browser is build off of Chromium, it should support most, if not all, the same policies from the Chromium and Google Chrome ADMX templates.
With that in mind, we've modified the Google Chrome ADMX templates to reflect the Brave Browser's registry path. After some initial troubleshooting and testing, the templatates seem to work.

**These Policy Definitions are in a Pre-Alpha state. They should be used for testing purposes only**

## Download the required files.

**Download the required files from the [GitHub Repository](https://github.com/simeononsecurity/BraveADMX)**

## Notes

Modified Google Chrome Policy Definitions according to:
[Brave Group Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)

**Note:**
Replaced "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" with "HKEY_LOCAL_MACHINE\Software\Policies\BraveSoftware\Brave"

**Note:**
Do not install SOS'es Chromium and Brave Browser ADMX templates at the same time.

## How to install

1.) Copy all files except readme.md to "C:\Windows\PolicyDefinitions" and/or "\\\domain.tld\domain\Policies\PolicyDefinitions"
2.) Profit?
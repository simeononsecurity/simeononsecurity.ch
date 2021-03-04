---
title: "Chromium ADMX Templates"
date: 2020-07-25T19:30:33-05:00
draft: false
description: "Proper ADMX Template for the Chromium Browser"
tags: ['ADMX', 'ADMX Templates', 'Chromium Browser', 'Chromium', 'Group Policy', 'GPO']
---

# ChromiumADMX
Proper ADMX Template for the Chromium Browser

Chromium, as a company, has failed to release ADMX templates for the Chromium Browser that may be installed at the same time as the Google Chrome templates.
With that in mind, we've modified the Google Chrome ADMX templates to reflect the Chromium Browser's registry path and placed in tandum in the Google ADMX Folder in GPO.

**These Policy Definitions are in a Pre-Alpha state. They should be used for testing purposes only**

## Download the required files

**Download the required files from the [GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)**

## Notes

Modified Google Chrome Policy Definitions according to:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Note:** Replaced "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" with "HKEY_LOCAL_MACHINE\Software\Policies\Chromium\"

**Note:** Do not install SOS'es Chromium and Brave Browser ADMX templates at the same time.

## How to install

1.) Copy all files except readme.md to "C:\Windows\PolicyDefinitions" and/or "\\\domain.tld\domain\Policies\PolicyDefinitions"

2.) Profit?





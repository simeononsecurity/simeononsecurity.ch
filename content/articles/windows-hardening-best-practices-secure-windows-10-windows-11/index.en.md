---
title: "Basic Windows Hardening Best Practices for Secure Windows 10 and Windows 11"
date: 2023-07-27
toc: true
draft: false
description: "Discover effective strategies for enhancing the security of your Windows 10 and Windows 11 systems through comprehensive hardening techniques and best practices."
genre: ["Windows hardening", "Windows security", "Windows 10 hardening", "Windows 11 hardening", "Windows security best practices", "Windows security tips", "Windows security guidelines", "Securing Windows operating systems", "Windows system hardening", "Windows security measures"]
tags: ["Windows hardening", "Windows security", "Windows 10", "Windows 11", "operating system security", "Windows Defender", "User Account Control", "BitLocker encryption", "firewall configuration", "AppLocker policies", "Windows updates", "strong passwords", "data backup", "Windows Hello", "Secure Boot", "TPM", "Microsoft Defender Antivirus", "Windows Sandbox", "Microsoft Defender Application Guard", "Controlled Folder Access", "Best practices for securing Windows 10 and Windows 11", "How to harden Windows operating systems", "Windows security measures for individuals and organizations", "Enhancing Windows system security", "Protecting data with BitLocker encryption", "Isolating browser sessions with Microsoft Defender Application Guard", "Windows 10 security tips and guidelines", "Implementing Windows security features", "Securing Windows with hardware-based isolation", "Ensuring Windows system integrity"]
cover: "/img/cover/A_cartoon_illustration_of_a_shield_protecting-windows.png"
coverAlt: "A cartoon illustration of a shield protecting a Windows logo from various cyber threats."
coverCaption: "Secure your Windows fortress with effective hardening techniques."
---

## Introduction

Windows operating systems are widely used by individuals and organizations around the world. To ensure the security and integrity of these systems, it is essential to implement **Windows hardening best practices**. Hardening involves securing the operating system by reducing its attack surface and mitigating potential vulnerabilities. This article will explore the best practices for hardening both **Windows 10** and the newer **Windows 11** operating systems, providing valuable insights to enhance the security of your Windows environment.

______

## Understanding Windows Hardening

Windows hardening is the process of strengthening the security of a Windows operating system. It involves configuring various settings and implementing security measures to protect against unauthorized access, malware, and other threats. By hardening your Windows system, you can minimize the risks associated with cyberattacks and ensure the confidentiality, integrity, and availability of your data.

### [Hardening Windows 10](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 10 is one of the most widely used operating systems globally. To harden your Windows 10 environment, consider the following best practices:

#### 1. [**Enable Windows Defender**](https://github.com/simeononsecurity/Windows-Defender-Hardening)

Windows Defender is a **robust antivirus solution** included with Windows 10. It offers a range of security features to protect your system from various types of **malware**, including **viruses, spyware, and ransomware**. By enabling Windows Defender, you can significantly enhance the security of your Windows 10 environment.

To enable Windows Defender, follow these steps:

- Open the **Windows Security** app by clicking on the Windows Security icon in the taskbar or by searching for "Windows Security" in the Start menu.
- In the Windows Security app, click on "**Virus & threat protection**" in the left-hand navigation pane.
- Click on "**Manage settings**" under the "Virus & threat protection settings" section.
- Ensure that the "**Real-time protection**" toggle switch is set to "**On**". This enables Windows Defender to actively scan and protect your system in real-time.
- Additionally, you can customize the scan options and exclusions by clicking on "**Scan options**" and "**Add or remove exclusions**", respectively.

It is crucial to **regularly update** Windows Defender to ensure it has the latest **malware definitions** and **security enhancements**. Microsoft releases regular updates to address new threats and vulnerabilities. To update Windows Defender, you can follow these steps:

- Open the Windows Security app.
- Go to "**Virus & threat protection**" in the left-hand navigation pane.
- Click on "**Check for updates**" under the "Virus & threat protection updates" section.
- Windows will check for available updates and download/install them if necessary.

By enabling and keeping Windows Defender up to date, you can proactively protect your Windows 10 system from malware and other security threats. It is also recommended to perform **regular system scans** using Windows Defender to ensure the detection and removal of any potential threats.

Remember, while Windows Defender provides a solid level of protection, it is essential to complement it with **safe browsing habits**, **regular software updates**, and other security measures to maintain a secure Windows 10 environment.

#### 2. [**Keep Windows 10 Updated**](https://support.microsoft.com/en-us/windows/windows-update-faq-8a903416-6f45-0718-f5c7-375e92dddeb2)
Regularly installing Windows updates is a critical aspect of **hardening Windows 10**. These updates include **security patches**, bug fixes, and performance improvements that help **patch security vulnerabilities** and improve system stability.

Microsoft releases **regular updates** for Windows 10 to address newly discovered security issues and enhance the overall user experience. By keeping your system updated, you ensure that your operating system has the latest **security enhancements** to defend against emerging threats.

To keep Windows 10 updated, you can follow these steps:

1. **Enable Automatic Updates**: By default, Windows 10 is configured to download and install updates automatically. This ensures that your system receives the necessary updates without manual intervention. To check if automatic updates are enabled, follow these steps:
   - Go to **Settings** by clicking on the Start menu and selecting the gear icon.
   - Click on **Update & Security**.
   - In the left-hand navigation pane, click on **Windows Update**.
   - Ensure that the **"Automatic"** option is selected under **"Windows Update settings"**. If it is not selected, click on the **"Change active hours"** link to customize the active hours during which Windows should avoid installing updates.

2. **Manually Install Updates**: If you prefer to have more control over the update process, you can manually install updates on your Windows 10 system. Here's how:
   - Go to **Settings** > **Update & Security** > **Windows Update**.
   - Click on **"Check for updates"** to see if any updates are available for your system.
   - If updates are found, click on **"Download"** and **"Install"** to initiate the installation process.

It is essential to emphasize the importance of **regularly restarting your system** after installing updates. Some updates may require a system restart to fully apply the changes and ensure their effectiveness.

By **keeping your Windows 10 system updated**, you not only enhance its security but also benefit from the latest features, performance improvements, and compatibility fixes. It is a proactive measure to ensure that your system remains resilient against potential security threats.

#### 3. [**Configure User Account Control (UAC)**](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-overview)
User Account Control (UAC) is a security feature in Windows 10 that helps prevent unauthorized changes to your system by prompting for administrator approval when needed. It acts as a safeguard against malicious software or unauthorized users attempting to make changes that could impact system security or stability.

Configuring UAC settings to an appropriate level is crucial for **hardening Windows 10**. It involves finding a balance between security and usability to ensure that UAC effectively protects your system without causing unnecessary interruptions.

To configure UAC settings in Windows 10, you can follow these steps:

1. Open the **Control Panel** by typing "Control Panel" in the search bar and selecting it from the search results.

2. In the Control Panel, click on **"User Accounts"**.

3. Click on **"Change User Account Control settings"**.

4. You will see a slider with different levels of UAC settings. Here are the available options:
   - **"Always notify"**: This is the highest level of UAC security where you are prompted for consent for any system changes, even for simple tasks.
   - **"Notify me only when apps try to make changes to my computer (default)"**: This is the recommended setting that provides a balance between security and usability. You are prompted for consent when apps make changes, but not for Windows settings changes.
   - **"Notify me only when apps try to make changes to my computer (do not dim my desktop)"**: Similar to the previous option, but the desktop does not get dimmed when UAC prompts appear.
   - **"Never notify"**: This is the lowest level of UAC security, where you are not prompted for any system changes.

5. Choose the level of UAC security that suits your needs by moving the slider to the desired position.

6. Click on **"OK"** to save the changes.

It is recommended to keep UAC enabled and set to a level that provides an appropriate balance between security and usability. Disabling UAC entirely can leave your system more vulnerable to unauthorized changes and potentially compromise its security.

By configuring UAC settings, you enhance the security of your Windows 10 system by ensuring that administrative privileges are required for critical system changes, reducing the risk of unauthorized access and malware infections.

#### 4. [**Use Strong Passwords**](https://simeononsecurity.com/articles/how-to-create-strong-passwords/)
Using strong passwords is essential for maintaining the security of your Windows 10 system and protecting against unauthorized access. Weak or easily guessable passwords can make your system vulnerable to attacks, such as brute-force attacks or password cracking.

To ensure that all user accounts on your Windows 10 system have strong passwords, follow these password best practices:

1. **Complexity**: Encourage users to create passwords that are complex and not easily guessable. A strong password should include a combination of uppercase and lowercase letters, numbers, and special characters. Avoid using common words or predictable patterns.

2. **Length**: Longer passwords are generally more secure. Encourage users to create passwords that are at least 8 characters long, but preferably longer. The more characters in a password, the harder it is to crack.

3. **Uniqueness**: Each user account should have a unique password. Using the same password for multiple accounts increases the risk of a security breach. Encourage users to use different passwords for different accounts.

4. **Avoid Personal Information**: Advise users against using personal information such as names, birthdates, or addresses in their passwords. This information can be easily obtained or guessed by attackers.

5. **Password Managers**: Consider using a password manager tool to securely store and manage passwords. Password managers can generate strong, unique passwords for each account and store them in an encrypted database.

6. **Regularly Change Passwords**: Encourage users to periodically change their passwords to maintain security. Set a policy for password expiration and educate users on the importance of regularly updating their passwords.

By implementing strong password practices, you significantly enhance the security of your Windows 10 system and reduce the risk of unauthorized access or data breaches. Regularly educate users about password security and provide resources, such as password strength meters or password creation guidelines, to assist them in creating strong passwords.

For more detailed information on creating strong passwords and best practices, you can refer to this [article](https://simeononsecurity.com/articles/how-to-create-strong-passwords/). It provides comprehensive guidance on password security and offers tips for creating strong and memorable passwords.

Remember, using strong passwords is a fundamental aspect of system security and should be prioritized to protect sensitive data and ensure the integrity of your Windows 10 environment.

#### 5. [**Enable BitLocker Encryption**](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)
One of the most effective ways to protect sensitive data on your Windows 10 system is by enabling BitLocker encryption. BitLocker provides full-disk encryption, ensuring that even if your device is lost or stolen, your data remains secure and inaccessible to unauthorized individuals.

To enable BitLocker encryption and safeguard your sensitive information, follow these steps:

1. **Check System Requirements**: Ensure that your Windows 10 edition supports BitLocker encryption. BitLocker is available in Windows 10 Pro, Enterprise, and Education editions.

2. **Enable BitLocker**: Open the Control Panel and navigate to the "System and Security" category. Click on "BitLocker Drive Encryption" and select the drive(s) you want to encrypt. Follow the on-screen instructions to start the encryption process.

3. **Choose Encryption Options**: During the BitLocker setup, you will have the option to choose between different encryption methods, such as using a password, a smart card, or both. Select the appropriate method based on your security requirements and preferences.

4. **Backup Recovery Key**: It is crucial to back up the BitLocker recovery key. This key acts as a failsafe in case you forget your password or encounter any issues accessing the encrypted drive. Store the recovery key in a secure location separate from your device.

5. **Manage BitLocker Settings**: After enabling BitLocker, you can customize additional settings, such as auto-unlock for specific drives or configuring the use of TPM (Trusted Platform Module) for added security. These settings can be accessed through the BitLocker management interface.

By enabling BitLocker encryption, you add an extra layer of protection to your Windows 10 system, ensuring that even if your device falls into the wrong hands, your data remains safe and inaccessible. It is important to regularly update and maintain your BitLocker settings to stay up to date with security best practices.

For more detailed information on enabling and managing BitLocker encryption, you can refer to the official [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview). It provides comprehensive guidance on BitLocker encryption, including advanced features and configuration options.

Remember, enabling BitLocker encryption helps safeguard your sensitive data and provides peace of mind, knowing that your information is secure even in the event of loss or theft.

#### 6. **Disable Unnecessary Services and Features**
To enhance the security of your Windows 10 system, it is essential to review and disable any unnecessary services and features. By doing so, you reduce the attack surface and minimize the potential for exploitation by malicious actors.

Here are the steps to disable unnecessary services and features on your Windows 10 system:

1. **Identify Unnecessary Services**: Start by identifying the services running on your system. Open the "Services" management console by pressing **Windows key + R**, typing **services.msc**, and hitting **Enter**. Review the list of services and research their purpose to determine which ones are essential for your system's functionality.

2. **Disable Unnecessary Services**: Once you have identified the unnecessary services, right-click on each service and select **Properties**. In the Properties window, change the **Startup type** to **Disabled**. This prevents the service from starting automatically when your system boots up. Exercise caution and ensure that you are only disabling services that are not required for your system's normal operation.

3. **Disable Unnecessary Features**: In addition to services, Windows 10 also includes various features that may not be necessary for your system. Open the **Control Panel**, navigate to **Programs** or **Programs and Features**, and click on **Turn Windows features on or off**. Uncheck any features that you do not require. This step helps reduce the attack surface further and minimizes the resources consumed by unnecessary features.

4. **Regularly Review and Update**: It is crucial to regularly review the list of services and features enabled on your Windows 10 system. As your system's requirements change over time, you may need to re-evaluate the services and features that are necessary. Stay vigilant and update your configuration as needed.

By disabling unnecessary services and features, you limit the potential entry points for attackers and reduce the overall attack surface of your Windows 10 system. This practice improves your system's security posture and mitigates the risk of exploitation.

For more information on managing services and features in Windows 10, you can refer to the following [article](https://www.tweakhound.com/2015/07/27/windows-10-default-services/#:~:text=Windows%2010%20Default%20Services%20%20%20%20Name,%20%20%20%2044%20more%20rows%20) for detailed guidance.

Remember, it is crucial to exercise caution when disabling services and features, as disabling essential components can negatively impact your system's functionality. Always research and understand the purpose of a service or feature before making any changes.

#### 7. **Implement Firewall Rules**
The built-in firewall in Windows 10 acts as a crucial line of defense against unauthorized network traffic. By configuring firewall rules, you can control which inbound and outbound connections are allowed, thereby enhancing the security of your system.

Follow these steps to implement firewall rules on your Windows 10 system:

1. **Access Firewall Settings**: To access the firewall settings, open the **Control Panel**, search for **Windows Defender Firewall**, and click on the corresponding result. Alternatively, you can right-click the **Start** button, select **Settings**, and navigate to **Network & Internet > Windows Firewall**.

2. **Configure Inbound Rules**: Inbound rules control incoming network connections to your system. Click on **Advanced settings** in the Windows Defender Firewall window. In the new window, select **Inbound Rules** and click **New Rule**. Follow the on-screen instructions to create rules that allow only necessary inbound connections. Consider the services and applications that require network access and create rules accordingly.

3. **Configure Outbound Rules**: Outbound rules control outgoing network connections from your system. Follow the same steps as above but select **Outbound Rules** instead. Create rules to allow outbound connections for essential services and applications while blocking suspicious or unnecessary connections.

4. **Regularly Review and Update**: It is important to regularly review and update your firewall rules to ensure they align with your system's requirements. As your network environment and usage patterns change, you may need to modify or create new rules. Stay vigilant and keep your rules up to date to maintain an effective firewall configuration.

By implementing and maintaining firewall rules, you can significantly reduce the risk of unauthorized network access and enhance the security of your Windows 10 system. Additionally, consider enabling the **Stealth Mode** option in the firewall settings to make your system less visible to potential attackers.

For more detailed information on configuring firewall rules in Windows 10, you can refer to the official [Microsoft documentation](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/best-practices-configuring) for step-by-step instructions.

Remember, a well-configured firewall is an essential component of a comprehensive security strategy, but it should be used in conjunction with other security measures to provide robust protection for your system.

#### 8. [**Use AppLocker**](https://github.com/simeononsecurity/AppLocker)
[AppLocker](https://simeononsecurity.com/github/applocker-hardening/) is a powerful feature in Windows 10 that enables you to control which applications can run on your system. By implementing AppLocker policies, you can restrict the execution of unauthorized or potentially malicious applications, enhancing the security of your Windows 10 environment.

Follow these steps to use AppLocker on your Windows 10 system:

1. **Access AppLocker Settings**: To access AppLocker settings, open the **Local Group Policy Editor** by pressing **Windows key + R**, typing **gpedit.msc**, and clicking **OK**. Alternatively, you can search for **Group Policy Editor** in the **Start** menu.

2. **Configure AppLocker Policies**: In the Local Group Policy Editor, navigate to **Computer Configuration > Windows Settings > Security Settings > Application Control Policies > AppLocker**. Here, you can configure various policies such as **Executable Rules**, **Windows Installer Rules**, **Script Rules**, and **Packaged App Rules**.

3. **Create AppLocker Rules**: To create an AppLocker rule, right-click on the desired policy folder (e.g., **Executable Rules**) and select **Create New Rule**. Follow the on-screen instructions to specify the conditions and exceptions for the rule. You can create rules based on file path, publisher, file hash, or other attributes to allow or deny application execution.

4. **Test and Refine Policies**: After creating AppLocker rules, it is important to test them to ensure they function as intended. Deploy the policies to a test group or system and verify that only authorized applications are allowed to run. Make any necessary refinements to the rules based on the test results.

5. **Regularly Review and Update**: As your application landscape evolves, it is crucial to regularly review and update your AppLocker policies. New applications may require permission to run, while others may become obsolete or pose security risks. Stay proactive and keep your policies up to date to maintain an effective application control mechanism.

AppLocker provides granular control over application execution, helping you prevent unauthorized or malicious software from running on your Windows 10 system. By using AppLocker, you can reduce the risk of malware infections, unauthorized software installations, and other security incidents.

For more detailed information on implementing AppLocker policies, you can refer to the official [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-overview) or visit our [AppLocker GitHub repository](https://github.com/simeononsecurity/AppLocker) for additional resources and examples.

Remember to regularly review and update your AppLocker policies to adapt to changing application requirements and emerging security threats. AppLocker is a valuable tool in your defense against unauthorized and potentially harmful applications on your Windows 10 system.

#### 9. [**Regularly Backup Your Data**](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/)
Regularly backing up your data is an essential practice to protect against data loss caused by security incidents, hardware failures, or other unexpected events. By creating regular backups and verifying their integrity, you can ensure that your important data remains safe and can be restored in the event of a disaster.

Follow these steps to regularly backup your data on a Windows 10 system:

1. **Identify Critical Data**: Start by identifying the data that is critical and needs to be backed up. This may include important documents, personal files, system configurations, application settings, and any other data that you consider valuable.

2. **Choose a Backup Solution**: Select a reliable backup solution that meets your requirements. Windows 10 offers built-in backup tools like **File History** and **Windows Backup and Restore**. Alternatively, you can opt for third-party backup software that provides additional features and flexibility.

3. **Define Backup Frequency**: Determine how frequently you want to perform backups based on the criticality of your data and the frequency of changes. Some data may require daily backups, while others can be backed up on a weekly or monthly basis.

4. **Select Backup Storage**: Choose a suitable storage medium to store your backups. This can include external hard drives, network-attached storage (NAS) devices, cloud storage services, or a combination of multiple storage options. Ensure that the storage medium is secure and reliable.

5. **Configure Backup Settings**: Set up the backup solution according to your preferences. Specify the data to be backed up, the backup destination, and any additional settings such as encryption or compression.

6. **Perform Test Restores**: Regularly test the restore process by performing test restores from your backups. This ensures that your backups are working correctly and that you can successfully recover your data when needed.

7. **Monitor and Update**: Monitor the backup process regularly to ensure it is running as expected. Update your backup solution and adjust the backup settings as your data and requirements change.

By following these steps and adhering to a regular backup routine, you can minimize the impact of data loss and maintain the availability of your important information. Remember to store your backups securely, away from the original data, and consider implementing the **3-2-1 backup rule** by having at least three copies of your data, stored on two different storage media, with one copy stored off-site.

For more detailed information on backup best practices and the **3-2-1 backup rule**, you can refer to the article on [What is the 3-2-1 Backup Rule and Why You Should Use It](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/). It provides valuable insights and recommendations for implementing an effective backup strategy.

Remember, regular backups are crucial in safeguarding your data and ensuring its availability in case of unforeseen events. Make data backup an integral part of your Windows 10 hardening efforts to protect your valuable information.

______

{{< inarticle-dark >}}


### [Hardening Windows 11](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 11 is the latest version of the Windows operating system, offering enhanced features and improved security. To harden your Windows 11 environment, consider the following best practices:

#### 1. **Secure Boot and TPM**
Secure Boot and TPM (Trusted Platform Module) are essential security features available in Windows 11 that help protect against unauthorized access and ensure the integrity of the operating system. By enabling Secure Boot and TPM, you can enhance the security of your Windows 11 system.

Follow these steps to enable Secure Boot and TPM on your Windows 11 device:

1. **Check Compatibility**: Before enabling Secure Boot and TPM, ensure that your device supports these features. Verify that your system's hardware and firmware meet the requirements for Secure Boot and TPM functionality.

2. **Access UEFI/BIOS Settings**: Restart your Windows 11 device and access the UEFI (Unified Extensible Firmware Interface) or BIOS (Basic Input/Output System) settings. The specific key or combination of keys to access these settings may vary depending on your device. Common keys include Del, F2, F10, or Esc. Refer to your device's documentation or manufacturer's website for detailed instructions.

3. **Enable Secure Boot**: Once in the UEFI/BIOS settings, navigate to the Secure Boot settings. Enable Secure Boot to ensure that only trusted operating systems and components are allowed to run during the boot process. This prevents the loading of unauthorized or malicious software that may compromise the system's security.

4. **Enable TPM**: Locate the TPM settings in the UEFI/BIOS and enable TPM. TPM is a dedicated microchip on the device's motherboard that provides hardware-based security features. Enabling TPM allows Windows 11 to leverage its capabilities for enhanced system security.

5. **Configure TPM Security**: After enabling TPM, you may have additional options to configure its security settings. Depending on your device and firmware, you may be able to set a TPM password, enable TPM firmware updates, or adjust other related settings. Review the available options and configure them based on your security requirements.

6. **Save and Exit**: Once you have enabled Secure Boot and TPM and made any necessary configurations, save the changes in the UEFI/BIOS settings and exit. The system will restart, and the new settings will take effect.

Enabling Secure Boot and TPM in Windows 11 helps protect your device from unauthorized modifications, rootkits, and other security threats. These features establish a foundation of trust for the operating system and contribute to a more secure computing environment.

Note that the availability and specific steps to enable Secure Boot and TPM may vary depending on your device's manufacturer and firmware version. It is recommended to consult your device's documentation or manufacturer's website for accurate instructions tailored to your system.

By enabling Secure Boot and TPM on your Windows 11 device, you enhance the overall security posture and strengthen the protection of your operating system and sensitive data.

#### 2. [**Enable Microsoft Defender Antivirus**](https://github.com/simeononsecurity/Windows-Defender-Hardening)
Windows 11 comes with built-in antivirus protection called **Microsoft Defender Antivirus**. It offers comprehensive security against various types of **malware**, including viruses, ransomware, and spyware. By **enabling** and **regularly updating** Microsoft Defender Antivirus, you can ensure **real-time threat detection and prevention** on your Windows 11 system.

Follow these steps to enable and update Microsoft Defender Antivirus on your Windows 11 device:

1. **Check Antivirus Status**: First, check the status of Microsoft Defender Antivirus on your system. Open the **Windows Security app** by clicking on the Start menu, searching for "Windows Security," and selecting the app from the search results. Once the app opens, navigate to the **"Virus & threat protection"** section to verify the status of Microsoft Defender Antivirus. It should be **enabled** by default on a fresh installation of Windows 11.

2. **Enable Real-Time Protection**: In the Windows Security app, make sure that **real-time protection** is enabled for Microsoft Defender Antivirus. Real-time protection continuously monitors your system for malware and other malicious activities, providing **immediate response** and **blocking threats** in real-time. If real-time protection is not enabled, click on the **toggle switch** to enable it.

3. **Update Definitions**: Regularly updating the **virus definitions** is crucial to ensure that Microsoft Defender Antivirus can detect and protect against the latest threats. In the Windows Security app, navigate to the **"Virus & threat protection"** section and click on the **"Check for updates"** button to update the antivirus definitions. This process ensures that your system is equipped with the **latest signatures** and **detection capabilities**.

4. **Schedule Scans**: Microsoft Defender Antivirus allows you to schedule regular **system scans** to proactively detect and remove any potential threats. In the Windows Security app, go to the **"Virus & threat protection"** section and click on the **"Quick scan"** or **"Full scan"** option to initiate a scan. You can also click on the **"Scan options"** link to customize the scan settings and schedule regular scans according to your preference.

5. **Configure Additional Settings**: Microsoft Defender Antivirus provides additional settings and features that you can configure based on your security requirements. In the Windows Security app, explore the various sections such as **"App & browser control," "Device security,"** and **"Firewall & network protection"** to customize the antivirus settings and leverage advanced protection features.

Enabling and regularly updating Microsoft Defender Antivirus in Windows 11 is essential for maintaining a strong defense against malware and other security threats. By following these steps and keeping Microsoft Defender Antivirus up to date, you can ensure that your Windows 11 system is well protected.

Note that while Microsoft Defender Antivirus provides robust protection, it's always recommended to practice **safe browsing habits**, exercise caution while **downloading files** or **opening email attachments**, and keep your **operating system and applications updated** to further enhance your overall security posture.

#### 3. **Apply Default Hardware-Based Isolation**
Windows 11 leverages hardware-based isolation features like **Virtualization-based Security (VBS)** and **Hypervisor-protected Code Integrity (HVCI)** to provide enhanced security and protect critical system components.

By enabling and applying these default hardware-based isolation features, you can establish robust security boundaries and mitigate various attack vectors. Here are some key steps to ensure the proper configuration:

1. **Enable Virtualization Technology**: First, you need to verify if your system supports virtualization technology and ensure it is enabled in the system's **BIOS** or **UEFI firmware** settings. The steps to access and enable virtualization technology may vary depending on the motherboard or firmware manufacturer. Consult your system documentation or the manufacturer's website for specific instructions.

2. **Enable Virtualization-based Security (VBS)**: Windows 11 incorporates VBS, which uses hardware virtualization capabilities to create isolated containers called **Virtual Secure Mode (VSM)**. VSM provides a secure execution environment for critical system components, protecting them from potential attacks. To enable VBS, follow these steps:

   - Press the **Windows key + R** to open the Run dialog box.
   - Type "**gpedit.msc**" and press **Enter** to open the Local Group Policy Editor.
   - Navigate to **Computer Configuration -> Administrative Templates -> System -> Device Guard**.
   - Double-click on **"Turn on Virtualization Based Security"** policy.
   - Select **"Enabled"** and click **OK** to apply the changes.

   Enabling VBS may require compatible hardware and certain system requirements. Refer to the official **Microsoft documentation** for more information.

3. **Enable Hypervisor-protected Code Integrity (HVCI)**: HVCI is a feature that uses the hypervisor to enforce code integrity policies, preventing unauthorized code execution and enhancing the overall security posture. To enable HVCI, follow these steps:

   - Press the **Windows key + R** to open the Run dialog box.
   - Type "**msconfig**" and press **Enter** to open the System Configuration utility.
   - Navigate to the **"Boot"** tab.
   - Click on **"Advanced options"**.
   - Check the **"Enable Hypervisor-protected Code Integrity"** option.
   - Click **OK** to save the changes and restart your system.

   Enabling HVCI requires compatible hardware and certain system requirements. Refer to the official **Microsoft documentation** for more details.

By applying default hardware-based isolation features, such as VBS and HVCI, you can significantly enhance the security posture of your Windows 11 system. These features help protect critical system components from various attacks, including those attempting to modify or exploit system code and configurations.

Ensure that you regularly update your system with the latest security patches and firmware updates to benefit from the most up-to-date security enhancements and mitigations offered by these hardware-based isolation features.

Note that the availability and requirements of hardware-based isolation features may vary depending on your system configuration and edition of Windows 11. It's recommended to consult official **Microsoft documentation** and perform compatibility checks to ensure the proper implementation of these security features.

#### 4. [**Use Windows Sandbox**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)
**Windows Sandbox** is a valuable tool that allows you to run untrusted applications or test software in an isolated environment, providing an extra layer of security for your system. By using Windows Sandbox, you can mitigate potential risks associated with running untrusted programs.

Windows Sandbox creates a lightweight, temporary desktop environment that is completely separate from your main operating system. Any changes made within the Sandbox are discarded once you close it, ensuring that your primary system remains unaffected.

To use Windows Sandbox, follow these steps:

1. **Check System Requirements**: Before proceeding, ensure that your system meets the requirements for running Windows Sandbox. Generally, you need a Windows 10 Pro or Enterprise edition and a processor with virtualization capabilities enabled in the BIOS/UEFI firmware. Consult the official [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview) for specific system requirements.

2. **Enable Windows Sandbox**: Windows Sandbox is a built-in feature in Windows 10 Pro and Enterprise editions. To enable Windows Sandbox, follow these steps:

   - Press the **Windows key + R** to open the Run dialog box.
   - Type "**appwiz.cpl**" and press **Enter** to open the Programs and Features window.
   - Click on **"Turn Windows features on or off"** on the left-hand side.
   - Scroll down and locate **"Windows Sandbox"** in the features list.
   - Check the box next to **"Windows Sandbox"** and click **OK** to enable it.
   - Windows will install the necessary components, and you may need to restart your system for the changes to take effect.

3. **Launch Windows Sandbox**: Once Windows Sandbox is enabled, you can launch it by following these steps:

   - Open the **Start** menu and search for **"Windows Sandbox"**.
   - Click on the **"Windows Sandbox"** application to open it.
   - The Sandbox will launch in a separate window, providing you with a secure environment to run untrusted applications or test software.

While running applications in Windows Sandbox, keep in mind that the Sandbox environment is isolated and designed to discard any changes made inside it. Therefore, it's crucial to save your files or data outside of the Sandbox if you need to retain them.

Windows Sandbox is an effective tool for testing unknown software, opening suspicious files, or exploring potentially risky websites. It adds an extra layer of protection by ensuring that any malicious activity or unwanted changes are confined within the Sandbox and do not impact your main operating system.

By incorporating Windows Sandbox into your security practices, you can significantly reduce the risks associated with running untrusted applications, protecting your system from potential threats.

For more information on Windows Sandbox and its usage, refer to the official [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview).

#### 5. [**Implement Microsoft Defender Application Guard**](https://github.com/simeononsecurity/Windows-Defender-Application-Guard-Hardening)
Microsoft Defender Application Guard is a powerful security feature that isolates Microsoft Edge browser sessions from the underlying operating system. By running Edge in a secure, isolated environment, Application Guard helps protect your system from browser-based attacks and malicious websites.

To implement Microsoft Defender Application Guard and enhance your browser security, follow these steps:

1. **Check Compatibility**: Before proceeding, ensure that your system meets the requirements for running Microsoft Defender Application Guard. Typically, you need a Windows 10 Pro or Enterprise edition, a compatible processor with virtualization capabilities, and at least 8 GB of RAM. Refer to the official [**Microsoft documentation**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard) for specific system requirements.

2. **Enable Application Guard**: Application Guard is available as an optional feature in Windows 10. To enable Microsoft Defender Application Guard, follow these steps:

   - Press the **Windows key + R** to open the Run dialog box.
   - Type "**appwiz.cpl**" and press **Enter** to open the Programs and Features window.
   - Click on **"Turn Windows features on or off"** on the left-hand side.
   - Scroll down and locate **"Microsoft Defender Application Guard"** in the features list.
   - Check the box next to **"Microsoft Defender Application Guard"** and click **OK** to enable it.
   - Windows will install the necessary components, and you may need to restart your system for the changes to take effect.

3. **Configure Application Guard**: Once Application Guard is enabled, you can configure its settings to suit your security needs. Application Guard allows you to define the level of isolation and control how it handles untrusted websites and files. You can adjust these settings through the **Windows Security** app or Group Policy settings.

4. **Test and Verify**: After enabling and configuring Microsoft Defender Application Guard, it's essential to test and verify its functionality. Open Microsoft Edge and visit a known malicious website or a site with potential risks to check if Application Guard successfully isolates the browser session and prevents any potential attacks.

By implementing Microsoft Defender Application Guard, you add an extra layer of protection to your system by isolating the browser sessions and containing any potential threats within the secure environment. This helps safeguard your system and data from browser-based attacks, such as drive-by downloads, malicious scripts, and zero-day exploits.

For more detailed information on configuring and utilizing Microsoft Defender Application Guard, refer to the official [**Microsoft documentation**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard).

#### 6. [**Controlled Folder Access**](https://github.com/simeononsecurity/Windows-Defender-Hardening)
Controlled Folder Access is a powerful security feature available in Windows 11 that helps protect important folders from unauthorized changes by ransomware and other malicious software. By enabling Controlled Folder Access and adding necessary folders to the protected list, you can enhance the security of your system and prevent potential data loss.

To implement Controlled Folder Access and protect your important folders, follow these steps:

1. **Open Windows Security**: Press the **Windows key** on your keyboard, type "**Windows Security**," and select the **Windows Security** app from the search results.

2. **Navigate to Virus & Threat Protection Settings**: In the Windows Security app, click on the **"Virus & threat protection"** tab in the left-hand menu.

3. **Configure Controlled Folder Access**: Under the **"Ransomware protection"** section, click on **"Manage ransomware protection"** to access the settings for Controlled Folder Access.

4. **Enable Controlled Folder Access**: In the Controlled Folder Access settings, toggle the switch to **"On"** to enable the feature. Windows will display a warning about allowing only trusted applications to access protected folders.

5. **Add Protected Folders**: To specify which folders should be protected, click on **"Protected folders"** and then select **"Add a protected folder"**. Choose the folders you want to safeguard and click **"OK"**.

   - It is recommended to add important folders such as Documents, Pictures, Videos, and any other directories containing valuable data.

6. **Allow or Block Applications**: By default, Controlled Folder Access allows trusted applications to access protected folders. However, you can customize this behavior by clicking on **"Allow an app through Controlled folder access"**. From there, you can either allow or block specific applications from accessing the protected folders.

7. **Monitor and Review**: After enabling Controlled Folder Access, Windows will continuously monitor and log any attempts by unauthorized applications to access protected folders. You can review these logs by clicking on **"Review"** under the **"Recently blocked apps"** section in the Controlled Folder Access settings.

By implementing Controlled Folder Access, you add an extra layer of protection to your important folders, mitigating the risk of unauthorized changes and potential data loss caused by ransomware attacks. Regularly review the Controlled Folder Access settings to ensure the protected folders align with your security requirements.

For more detailed information on configuring and utilizing Controlled Folder Access, refer to the official [**Microsoft documentation**](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/controlled-folders?view=o365-worldwide).


#### 7. **Enable Windows Automatic Maintenance**
Windows 11 includes a convenient feature called Automatic Maintenance that helps keep your system optimized and protected by performing regular maintenance tasks. By enabling Automatic Maintenance, you ensure that your system runs smoothly and remains secure.

To enable Windows Automatic Maintenance, follow these steps:

1. **Open Windows Settings**: Press the **Windows key** on your keyboard, type "**Settings**," and select the **Settings** app from the search results.

2. **Access the Maintenance Settings**: In the Settings app, click on the **"System"** category and then select **"About"** from the left-hand menu. Scroll down to the bottom of the page and click on the **"System info"** link.

3. **Open Maintenance Settings**: In the System Information window, click on the **"Maintenance"** link located at the bottom of the page.

4. **Enable Automatic Maintenance**: In the Maintenance settings, toggle the switch next to **"Automatic Maintenance"** to the **"On"** position.

5. **Configure Maintenance Settings**: By default, Windows will automatically schedule maintenance tasks to run daily at 2:00 AM. If you prefer a different schedule, click on **"Change maintenance settings"** and customize the desired options, such as the maintenance start time and the frequency of maintenance tasks.

6. **Review Additional Settings**: Below the Automatic Maintenance toggle switch, you can find additional settings related to maintenance, such as **"Allow scheduled maintenance to wake up my computer at the scheduled time"** and **"Allow scheduled maintenance to run even when I'm on battery power"**. Adjust these settings according to your preferences and requirements.

7. **Monitor Maintenance Activities**: Once Automatic Maintenance is enabled, Windows will automatically perform maintenance tasks in the background at the scheduled time. You can monitor these activities by checking the **"Maintenance"** section in the **"Windows Security"** app or by reviewing the **"Maintenance"** logs in the Event Viewer.

Enabling Windows Automatic Maintenance ensures that your system stays optimized and protected by regularly performing essential maintenance tasks such as software updates, disk optimization, and security scans. By keeping your system in good health, you can enjoy a smoother and more secure computing experience.

For more detailed information on Windows Automatic Maintenance and its configuration options, refer to the official [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-maintenence).

______

{{< inarticle-dark >}}

## Conclusion

Implementing these **Windows hardening best practices** is essential for ensuring the security of your Windows systems. By regularly **updating your operating system**, you can patch security vulnerabilities and improve system stability. Enabling security features like **antivirus** and **encryption** adds an additional layer of protection to your data. Configuring appropriate **access controls** helps prevent unauthorized changes and restricts access to sensitive resources.

By adhering to these best practices, you can enhance the security of your **Windows environment**, protect your data, and maintain the integrity of your **digital infrastructure**. It is important to stay **proactive** and regularly review and update your security measures to stay ahead of potential threats.

Remember, **Windows hardening** is an ongoing process, and it is essential to stay informed about the latest security updates and practices. By staying proactive and implementing these best practices, you can effectively mitigate security risks and ensure the safety of your Windows systems.

For more information on Windows hardening and best practices, refer to reputable sources such as **Microsoft documentation**, **security forums**, and trusted **cybersecurity websites**.

______

## References:

- [Microsoft Windows Security](https://www.microsoft.com/en-us/security)
- [NIST Special Publication 800-171: Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final)
- [CIS Microsoft Windows 10 Benchmark](https://www.cisecurity.org/benchmark/microsoft_windows_10/)
- [CIS Microsoft Windows 11 Benchmark](https://www.cisecurity.org/benchmark/microsoft_windows_11/)
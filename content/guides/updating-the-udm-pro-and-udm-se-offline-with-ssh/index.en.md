---
title: "Offline Firmware Update for Ubiquiti Unifi UDM Pro and UDM SE via Command-line SSH"
draft: false
toc: true
date: 2023-05-28
description: "Learn how to update the firmware of Ubiquiti Unifi UDM Pro and UDM SE offline through command-line SSH for optimal performance and security."
tags: ["Ubiquiti firmware update", "UDM Pro", "UDM SE", "offline firmware update", "command-line SSH", "network management", "network security", "firmware upgrade", "SSH connection", "firmware file", "UniFi Network Controller", "bug fixes", "performance improvements", "security patches", "networking", "network devices", "technology", "IT management", "firmware update process", "network optimization"]
cover: "/img/cover/A_colorful_illustration_depicting_a_computer_connecting.png"
coverAlt: "A colorful illustration depicting a computer connecting to a router through SSH, symbolizing the offline firmware update process for Ubiquiti Unifi UDM Pro and UDM SE devices."
coverCaption: ""
---

**Update the Ubiquiti Unifi UDM Pro and UDM SE Offline Through SSH**

In the world of networking, **Ubiquiti Networks** has gained recognition for its innovative solutions. The **Ubiquiti Unifi Dream Machine Pro (UDM Pro)** and **Unifi Dream Machine SE (UDM SE)** are two popular products that offer comprehensive network management features. Updating the firmware of these devices is crucial to ensure optimal performance and security. In this article, we will explore how to update the firmware of the UDM Pro and UDM SE **offline** using command-line SSH.

______

## Why Update Firmware?

Firmware updates are essential for any network device, as they often contain bug fixes, performance improvements, and security patches. Regularly updating the firmware of your UDM Pro and UDM SE is crucial to ensure your network remains secure and operates smoothly.

______

## Offline Firmware Update

Updating the firmware of the UDM Pro and UDM SE can be done through the **UniFi Dashboard**. However, in some scenarios, an internet connection may not be available or desirable. In such cases, an offline update using command-line SSH provides an alternative solution.

______

## Preparing for the Offline Update

Before proceeding with the offline update, make sure you have the following prerequisites:

1. A computer or device with an SSH client installed.
2. The latest firmware file for your UDM Pro or UDM SE. You can obtain the firmware file from the [Ubiquiti Downloads](https://www.ui.com/download/unifi) for the [UDM Pro](https://www.ui.com/download/unifi/unifi-dream-machine-pro) page. For early access firmwares, you can see them on the [community releases page](https://community.ui.com/releases) once you've signed into your.[**ui.com**](https://account.ui.com/) account

______

## Establishing SSH Connection

To update the UDM Pro or UDM SE through command-line SSH, follow these steps:

1. Ensure your computer or device is connected to the same network as the UDM Pro or UDM SE.
2. Open your preferred SSH client and establish an SSH connection to the **UDM Pro or UDM SE's IP address**. For example, using the **OpenSSH client** in Linux or macOS, you can use the following command:

```bash
ssh root@<UDM_IP_ADDRESS>
```

Replace `<UDM_IP_ADDRESS>` with the actual IP address of your UDM Pro or UDM SE.

3. Enter the **username** and **password** when prompted. The default credentials for Ubiquiti devices are usually `ubnt` for both the username and password.

______

## Updating Firmware

Once you have established the SSH connection, you can proceed with the firmware update:

1. Upload the firmware file to the UDM Pro or UDM SE using **SCP (Secure Copy)**. SCP allows secure file transfer over SSH. Assuming the firmware file is located on your local machine, you can use the following command:

```bash
scp <FIRMWARE_FILE_PATH> ubnt@<UDM_IP_ADDRESS>:/root/fwupdate.bin
```

Replace `<FIRMWARE_FILE_PATH>` with the path to the firmware file on your local machine, and `<UDM_IP_ADDRESS>` with the IP address of your UDM Pro or UDM SE.

2. Once the firmware file is uploaded, you can initiate the firmware update process. Execute the following command:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "ubnt-tools fwupdate /root/fwupdate.bin"
```

3. The UDM Pro or UDM SE will start the firmware update process. This may take several minutes. **Do not interrupt the process** until the update is complete.

4. After the update is finished, you can verify the firmware version by logging into the UniFi Network Controller or by executing the following command:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "show version"
```
Please note that the above process assumes you have the necessary firmware file for your UDM Pro or UDM SE. Ensure you have the correct firmware file for your specific device model and version.

## Conclusion

Updating the firmware of your Ubiquiti Unifi UDM Pro and UDM SE devices is a crucial step to ensure optimal performance and security. While the UniFi Network Controller provides a convenient way to update the firmware, performing an offline update through command-line SSH offers a viable solution when an internet connection is not available or desirable.

By following the steps outlined in this article, you can successfully update the firmware of your UDM Pro and UDM SE devices using command-line SSH. Remember to always use the latest firmware version provided by Ubiquiti Networks to take advantage of bug fixes, performance improvements, and security patches.

## References

- [Ubiquiti Downloads](https://www.ui.com/download/unifi/) - Official Ubiquiti Downloads page for firmware files.
- [Unifi Advanced Updating Techniques](https://help.ui.com/hc/en-us/articles/204910064-UniFi-Upgrade-the-Firmware-of-a-UniFi-Device)

---
title: "Migrate a Hyper-V VM to Proxmox VE: A Reversible Checklist"
date: 2026-10-11
lastmod: 2026-10-11
toc: true
draft: false
description: "Move one Hyper-V virtual machine to Proxmox VE with a stopped-source export, matched firmware, disk import, isolated boot test, and rollback plan."
genre: ["Virtualization", "System Administration", "Homelab"]
tags: ["Hyper-V to Proxmox", "Hyper-V migration", "Proxmox VE migration", "VHDX import", "qm disk import", "virtual machine cutover", "Hyper-V export", "Proxmox Windows VM", "Proxmox VirtIO", "VM rollback", "UEFI migration", "Hyper-V checkpoints", "virtual TPM", "BitLocker recovery", "homelab migration"]
cover: "/img/cover/hyper-v-to-proxmox-migration-checklist.webp"
coverAlt: "A disk moves across a bridge from a blue server rack to an orange server rack, with a separate return path and a shield by the target."
coverCaption: "Keep the source VM available until the new guest passes its cutover checks."
---

A **Hyper-V export** preserves a virtual machine's files, while Proxmox VE needs a new guest configuration and an imported disk. A successful copy alone does not prove the guest will boot or serve users. This checklist moves one VM through a stopped-source export, a controlled boot test, and a cutover with a clear return path.

## Key Takeaways

- **Record the source:** Capture firmware generation, disk paths, checkpoints, network settings, and encryption before export.
- **Stop writes:** Shut down the Hyper-V VM before the final export and keep it off during the Proxmox test.
- **Match the boot path:** Hyper-V Generation 1 uses legacy BIOS. Generation 2 uses UEFI.
- **Validate the service:** Check data, network access, backups, and guest health before retiring the source.

## Before You Begin

Plan a maintenance window and a test on a disposable VM first. You need administrator access to Hyper-V, Proxmox VE, storage for the export, and a verified backup separate from the migration copy. Allow time to transfer every virtual disk and test the guest application. Disk size and transfer speed set the downtime.

This procedure covers a conventional VM with virtual disks. **Shielded VMs, pass-through disks, shared disks, clustered workloads, and hardware-bound licensing** need workload-specific plans. Record who owns the cutover decision and the latest time you will roll back. Do not start both copies on the production network with the same machine identity.

| Source detail | Why you need it |
|---|---|
| **VM generation and firmware** | Select SeaBIOS or OVMF on Proxmox |
| **Secure Boot state and template** | Match the boot policy and enroll compatible keys |
| **Boot and data disks** | Import every required disk in the right order |
| **Checkpoints and AVHDX files** | Avoid treating a differencing disk as an independent base disk |
| **IP, DNS, MAC, and VLAN** | Restore reachability without creating a duplicate identity |
| **vTPM and BitLocker** | Prepare recovery before virtual hardware changes |
| **Services and data checks** | Define evidence for success and rollback |

## Inventory the Hyper-V VM

Run these read-only commands in an elevated PowerShell session on the Hyper-V host. Enter the VM name when prompted:

```powershell
$vmName = Read-Host "Hyper-V VM name"
Get-VM -Name $vmName | Select-Object Name, State, Generation, ProcessorCount, MemoryAssigned
Get-VMHardDiskDrive -VMName $vmName | Select-Object ControllerType, ControllerNumber, ControllerLocation, Path
Get-VMSnapshot -VMName $vmName | Select-Object Name, CreationTime
Get-VMNetworkAdapter -VMName $vmName | Select-Object Name, SwitchName, MacAddress
```

The [Hyper-V PowerShell module](https://learn.microsoft.com/en-us/powershell/module/hyper-v/) documents these inventory commands. Compare disk paths with the VM settings and list any attached ISO, data disk, virtual switch, static address, or DHCP reservation. Record the guest OS and application versions. Verify the backup by restoring a test copy or checking a recent documented restore result. A file copy without a recovery test is weaker evidence.

For a **Generation 2** VM, record its firmware and security settings as well:

```powershell
Get-VMFirmware -VMName $vmName | Format-List *
Get-VMSecurity -VMName $vmName | Format-List *
```

Record the **Secure Boot** state, template, and vTPM setting. Microsoft's [**`Get-VMFirmware`** reference](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmfirmware) limits the command to Generation 2. [**`Get-VMSecurity`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmsecurity) reports the VM security configuration. Do not run **`Get-VMFirmware`** against a Generation 1 guest.

**Resolve checkpoints before the final export.** Microsoft says a Hyper-V export gathers checkpoint files as well as VHDX disks. Deleting a checkpoint through Hyper-V merges its differencing disk. Never delete an **`.avhdx`** file in the filesystem to clear a checkpoint. If a merge fails or a disk chain looks incomplete, stop and follow [Microsoft's checkpoint recovery guidance](https://learn.microsoft.com/en-us/troubleshoot/windows-server/virtualization/hyper-v-snapshots-checkpoints-differencing-disks). [Microsoft's checkpoint guide](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/checkpoints) explains normal deletion and merging.

For a Windows guest using **BitLocker** or a **virtual TPM**, obtain and verify the recovery key before changing virtual hardware. Hyper-V's [Generation 2 security documentation](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features) describes vTPM-backed encryption. Microsoft's [BitLocker FAQ](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-key-management-faq) explains why boot changes trigger recovery. A new Proxmox TPM device does not reproduce the old TPM state. Keep the key outside the exported VM.

## Export a Stopped VM

Shut down the guest cleanly. Confirm Hyper-V shows **Off**, not Saved. Wait for any checkpoint merge to finish, then export the VM to a location with enough free space. In Hyper-V Manager, right-click the VM, choose **Export**, and select the destination. The PowerShell equivalent is:

```powershell
$vmName = Read-Host "Stopped Hyper-V VM name"
$exportPath = Read-Host "Export destination directory"
Export-VM -Name $vmName -Path $exportPath
```

[Microsoft's export guide](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines) says an export contains virtual disks, configuration, and checkpoint files. Its [**`Export-VM`** reference](https://learn.microsoft.com/en-us/powershell/module/hyper-v/export-vm) defines the command. Confirm the expected disk files and sizes at the destination. Retain the stopped source VM and its independent backup. **Do not modify the exported files while importing them.**

Transfer the VHDX files to a path accessible from the Proxmox host. Check available capacity on both the transfer location and target storage. Preserve an untouched export for rollback. If the export contains **`.avhdx`** files, do not pick a base **`.vhdx`** by filename and assume it contains the latest writes. Resolve the disk chain on Hyper-V before continuing.

## Create the Proxmox Shell

Create a new VM in the Proxmox web interface with the guest OS type, CPU, and memory recorded earlier. Choose a new unused VM ID. Do not install a fresh operating system. Remove the empty disk created by the wizard before you import the source disk. Leave the network adapter disconnected from the production bridge for the first boot, or attach it to an isolated test network.

| Hyper-V source | Proxmox target |
|---|---|
| **Generation 1, legacy BIOS** | SeaBIOS |
| **Generation 2, UEFI** | OVMF with an EFI disk and matching Secure Boot policy |
| **Windows boot disk without VirtIO storage driver** | Attach initially as SATA |
| **Windows with vTPM or BitLocker** | New TPM state device when needed, recovery key ready before first boot |

Microsoft's [VM generation guide](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/Should-I-create-a-generation-1-or-2-virtual-machine-in-Hyper-V) maps Generation 1 to legacy BIOS and Generation 2 to UEFI. Proxmox's [VM documentation](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) documents SeaBIOS, OVMF, and the EFI disk used to keep UEFI settings. **Match the source boot mode.** Changing it during migration creates another boot problem to diagnose.

For a Generation 2 source, match whether **Secure Boot** was enabled. Check the source template and select compatible enrolled keys for the guest. Hyper-V template names do not transfer to Proxmox. Proxmox's 4 MB EFI disk and **Pre-Enroll keys** option supply Secure Boot keys and enable Secure Boot by default. Verify the target's boot behavior before cutover. [Microsoft's firmware reference](https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmfirmware) describes the source template requirement. [Proxmox's EFI disk documentation](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) describes the target keys.

If the source uses a **vTPM**, add **TPM State** in Proxmox's Hardware panel before the first boot. Select **version 2.0** unless the source guest has a documented requirement for version 1.2. This creates new TPM state, not a copy of the Hyper-V vTPM. A BitLocker guest needs its verified recovery key at first boot. Proxmox's [TPM documentation](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) describes the Hardware action and versions.

For Windows, start with a SATA boot disk unless the guest already has the required VirtIO storage driver. After a successful boot, install the supported VirtIO drivers and change one virtual device at a time. Proxmox recommends VirtIO SCSI for performance, but a missing boot driver leaves Windows unable to access its system disk. For Linux, check whether the initramfs includes the target storage driver before switching buses. [Proxmox VM documentation](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) describes the disk controllers.

## Import and Attach Disks

On the Proxmox host, check the copied VHDX path. The following command illustrates an import for VM ID **230** into a storage ID named **`local-lvm`**. Replace all three values with your own:

```bash
qm disk import 230 /path/to/exported/boot.vhdx local-lvm
```

Proxmox's [**`qm disk import`** reference](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc) says the source image is imported as an **unused disk**. [QEMU's image documentation](https://www.qemu.org/docs/master/system/images) lists VHDX as a supported conversion format. Import each additional data disk separately. Wait for each import task to finish and compare the imported disk sizes with the source inventory.

In the VM's **Hardware** panel, attach the unused boot disk as **SATA** for the first Windows boot. Attach data disks in a documented order. In **Options > Boot Order**, select the boot disk. For a Generation 2 guest, verify **OVMF** and the EFI disk. Keep the import files and source VM intact until validation passes.

## Test Before Cutover

Start the Proxmox guest on the isolated network. Use the console to check the boot screen, operating system login, disk volumes, application data, and service logs. A login prompt alone does not prove migration success. Use the checks you recorded before export, including a representative transaction or read of recent data.

For a BitLocker guest, unlock with the recovery key if prompted. After Windows starts, check the operating system volume's protection status and protectors from an elevated prompt:

```powershell
manage-bde -status C:
manage-bde -protectors -get C:
```

Microsoft's [BitLocker operations guide](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) documents protector inspection and recovery-key backup. The output includes sensitive recovery material. Do not paste it into a ticket or public log. Verify the intended protector and escrow a current recovery method under your policy. Restart the guest and confirm it boots without another recovery prompt before cutover. Repeated recovery is a failed migration check, not a prompt to discard the original key.

| Test | Pass condition |
|---|---|
| **Boot and disks** | Guest starts and every expected volume mounts |
| **Secure Boot and BitLocker** | Intended boot policy holds and encrypted guest restarts without repeated recovery |
| **Application** | A representative read or transaction succeeds |
| **Network** | Required peers reach the test guest on intended ports |
| **Recovery** | Proxmox backup and isolated restore test succeed before source retirement |
| **Operations** | Monitoring, time sync, shutdown, and guest agent behave as intended |

When the application checks pass, switch its production network path or address during the maintenance window. Keep Hyper-V powered off. A changed virtual NIC might require a new DHCP reservation or a corrected static address inside the guest. Check DNS, firewall rules, and dependent services from a separate client. Proxmox's [VM documentation](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) covers network device and guest-agent options.

## Troubleshoot and Roll Back

| Symptom | First check |
|---|---|
| **No boot device** | Boot order, imported boot disk, BIOS versus UEFI mode, and Secure Boot keys |
| **Windows storage error** | SATA attachment and missing VirtIO storage driver |
| **Repeated BitLocker recovery prompt** | New TPM state, Secure Boot policy, boot measurements, and protectors |
| **Guest boots without network** | New virtual NIC, bridge, VLAN, DHCP reservation, and static address |
| **Data is old or missing** | Wrong VHDX, incomplete export, checkpoint chain, or missing data disk |

If a required test fails before the rollback deadline, stop the Proxmox VM and disconnect its production network. Restore the source network path, then start the original Hyper-V VM. **Never run both copies with the same production identity.** Record any writes accepted by the Proxmox copy before returning to Hyper-V. Those writes need separate recovery or reconciliation because the source disk did not receive them.

Keep the source VM and export until the Proxmox guest has passed your service checks, a new backup, an isolated restore test, and an agreed observation period. The site's [virtualization comparison](/articles/vmware-esxi-citrix-xenserver-hyper-v-comparison/) helps with platform choice. The [Proxmox upgrade guide](/articles/proxmox-ve-8-to-9-upgrade-guide/) covers a later maintenance task. **A migration ends after the workload and recovery path work on the new host, not when the disk import completes.**

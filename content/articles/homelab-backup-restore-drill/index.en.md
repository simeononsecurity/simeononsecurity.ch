---
title: "Run a Homelab Backup Restore Drill With Restic"
date: 2026-10-10
lastmod: 2026-10-11
toc: true
draft: false
description: "Test whether a homelab backup restores usable files. Set a recovery target, restore to a separate location with Restic, check data, and record the result."
genre: ["Homelab", "Backup", "Disaster Recovery"]
tags: ["homelab backup", "restore drill", "Restic restore", "backup verification", "recovery test", "disaster recovery", "RPO", "RTO", "backup repository", "Restic check", "NAS backup", "server backup", "VM recovery", "file restore", "backup encryption", "backup monitoring", "recovery plan", "backup test", "offsite backup", "data integrity"]
cover: "/img/cover/homelab-backup-restore-drill.webp"
coverAlt: "A homelab server and NAS backed up to a separate drive, with a verified restore folder on an isolated test computer and a stopwatch."
coverCaption: "Restore to a separate target, then check the data and the time required."
---

A backup job reporting success does not show whether you can restore a usable file. A **restore drill** tests the path from stored backup to working data without replacing your live files. This guide uses Restic for a file-level example and gives you a record to repeat after the lab changes.

## Key Takeaways

- **Pick a target:** Choose the files or service you need to recover and define an acceptable recovery point and time.
- **Restore separately:** Use an empty test destination so the drill cannot overwrite live data.
- **Check the result:** Open restored files, verify application data where possible, and measure elapsed time.
- **Record failures:** Keep the snapshot ID, missing items, permissions, and repair actions with your recovery plan.

## Before You Begin

You need a working backup repository, its password or key, a destination with enough free space, and permission to read both the backup and test location. This example assumes Restic is installed and the repository contains a recent file backup. Restic's [quickstart](https://restic.readthedocs.io/en/stable/010_introduction.html) covers repository creation and first backups. The site's [3-2-1 backup guide](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) covers copy placement. The [homelab overview](/articles/what-is-a-homelab-and-should-you-have-one/) includes a short backup test checklist.

This drill checks files in one snapshot. A database, virtual machine, or application also needs its own recovery steps. Keep the test system isolated when starting a restored service might conflict with the live one. Do not treat a successful file copy as proof that every service will boot.

> **Warning:** Do not restore over a live path for the first test. Use an empty test directory on a separate filesystem or test host. Keep the repository password out of screenshots, tickets, and shell history.

## Define the Recovery Goal

Write down what you need after a failure. A **recovery point objective (RPO)** is the oldest acceptable recovered data. A **recovery time objective (RTO)** is how long the service can remain unavailable. NIST defines both in its [contingency planning guide](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf). Your own targets should reflect how often the data changes and how long a restore takes on your hardware.

| Item | Illustrative target | What to record |
|---|---|---|
| **Family documents** | Latest nightly backup | Last snapshot time and opened files |
| **Home service config** | Last known good change | Config version and required secrets |
| **NAS media library** | Weekly backup | Sample playback and restore time |

The targets above are examples, not measured results. In your recovery plan, record the backup storage location and how an authorized person retrieves the repository password or encryption key. Do not place secret values in the plan or drill record. Store the secrets through a protected path independent of the failed host. A repository that survives while its only password does not is not recoverable.

Choose one **critical file set** for this drill. Add one small file you know should be present in the latest snapshot. For a service, also list the configuration, database export, certificates, and application version needed to start it. Confirm that your backup method captures consistent application data before relying on a file-level copy of a running database.

## Find a Snapshot

Use repository access approved for a restore drill. Restic normally creates repository locks, so the commands below assume that the repository permits those lock writes. Keep the live source and test target separate. Replace `/path/to/repository` with your actual Restic repository path, then list snapshots:

```bash
restic -r /path/to/repository snapshots
```

Restic prompts for the repository password if you have not supplied it through a configured secret method. Its [snapshot listing](https://restic.readthedocs.io/en/stable/010_introduction.html) shows the ID, date, host, and source paths. Record the snapshot ID and timestamp you intend to test. Compare the timestamp with your RPO. A current job log cannot replace this check, since the snapshot you need might be older than you think.

If the expected snapshot is absent, stop the drill and investigate the backup schedule, source selection, and repository path. Do not quietly choose an older snapshot and report the recovery goal as met.

## Restore to an Empty Test Target

Create an **empty target directory** on a test filesystem with enough room for the snapshot. Do not point Restic at the original source, a mounted production share, or an existing folder containing data you want to keep. Replace `SNAPSHOT_ID` and both example paths before running this command:

```bash
restic -r /path/to/repository restore SNAPSHOT_ID \
  --target /path/to/empty-restore-drill
```

Restic's [restore guide](https://restic.readthedocs.io/en/stable/050_restore.html) describes the snapshot ID and `--target` path. The restored tree keeps the source path underneath the target directory, so locate the actual files before judging the result. If you need only a small subset, use the documented [restore include filters](https://restic.readthedocs.io/en/stable/050_restore.html) and record what you excluded. Do not use `--delete` in a drill. Restic says that option removes files in the target that are absent from the snapshot.

Start a timer when the restore begins. Stop it when the required files are present and usable, not when a command first prints progress. Record repository location, network link, data size, and test host because those conditions affect a later recovery.

> **Expected Result:** The selected snapshot restores into a separate target without modifying the live source.

## Verify Data and Service Recovery

Open a few restored files with the application that normally reads them. Include a recent file, an older file, and a file from a nested directory. Compare known sizes or checksums if you recorded them before backup. Check ownership and permissions on Linux, since a readable file for the test account might still fail under the service account.

For a service, restore into an isolated test instance. Check its configuration, required secrets, database consistency, startup, and one representative user action. A file restore that omits a database or secret is an incomplete service recovery. Never start the test instance against the live database or production address unless you have a controlled cutover plan.

Run Restic's repository check after the sample restore:

```bash
restic -r /path/to/repository check
```

For a full repository data read, use `check --read-data` during a maintenance window. Restic warns that it reads the whole repository and may download substantial data from a remote backend. The [Restic troubleshooting guide](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) describes both the check and its cost. A clean check adds confidence, but it does not replace opening restored files or starting the service.

```bash
restic -r /path/to/repository check --read-data
```

Compare the snapshot age with your RPO and the measured recovery time with your RTO. If either target fails, the drill failed even if Restic exited without an error. Adjust backup frequency, storage placement, bandwidth, or the recovery procedure and test again.

## Keep a Restore Record

Write a short record after every drill. NIST's [SP 800-53 backup control](https://csrc.nist.gov/CSRC/media/Projects/risk-management/800-53%20Downloads/800-53r5/SP_800-53_v5_1-derived-OSCAL.pdf) includes restoration of sampled system functions as a way to test recovery. A repeatable record helps you see whether the plan improves.

| Field | Result to enter |
|---|---|
| **Date and operator** | When you ran the drill and who ran it |
| **Repository and snapshot** | Location, ID, timestamp, and source paths |
| **Recovery target** | Files or service tested, plus RPO and RTO |
| **Measured result** | Snapshot age, restore time, and file or service checks |
| **Failures** | Missing data, key access, permission, network, or startup issues |
| **Next action** | Owner, repair, and next test date |

Do not put the repository password, recovery key, or sensitive file contents in the record. Keep those in a protected secret store and document how an authorized person retrieves them during an outage.

## Troubleshooting

- **Password is unavailable:** Check the independent key escrow path. Do not assume the failed host will be available to retrieve its own key.
- **Snapshot is too old:** Check the schedule, job failures, source paths, and whether the expected host backed up to a different repository.
- **Restore is too slow:** Measure the storage read speed, network link, and amount of data. Test a smaller critical subset, then revise the RTO or recovery design.
- **File exists but service fails:** Check database exports, application version, ownership, permissions, certificates, and missing secrets.
- **Repository check reports errors:** Preserve the output and a copy of the repository if possible. Follow Restic's [damage troubleshooting](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) before attempting repairs.
- **Test changed live data:** Stop the test service, verify the production data, and revise the isolation plan before repeating the drill.

## Next Steps

Repeat this drill after changing backup software, storage, encryption keys, or critical services. Rotate through different file sets and a full service recovery over time. Keep an independent backup copy according to your [3-2-1 plan](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/). The goal is a measured restore you can repeat when the original host is gone.

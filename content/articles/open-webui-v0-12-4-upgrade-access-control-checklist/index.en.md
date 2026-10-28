---
title: "Open WebUI v0.12.4: Upgrade and Access-Control Checklist 2026"
date: 2026-10-28
lastmod: 2026-10-28
toc: true
draft: false
description: "Back up and upgrade Open WebUI to v0.12.4, then test chat sharing, export permissions, resource grants, accounts, and network access."
genre: ["Self-Hosted AI", "Cybersecurity", "System Administration"]
tags: ["Open WebUI", "Open WebUI v0.12.4", "Open WebUI upgrade", "Open WebUI security", "Open WebUI access control", "self-hosted AI", "Docker upgrade", "pip upgrade", "Open WebUI backup", "Open WebUI permissions", "Open WebUI roles", "Open WebUI groups", "chat export permission", "shared chats", "archived chats", "knowledge base access", "model access", "tool permissions", "API key security", "admin account security", "disable signup", "reverse proxy authentication", "VPN access", "container image pinning"]
---

**Open WebUI v0.12.4 contains security fixes the maintainers have not yet itemized.** Its release notes recommend updating deployments promptly and say advisories will follow CVE assignment. The named chat-sharing and permission changes below are visible release-note items, not a complete list of the undisclosed security fixes. [Open WebUI v0.12.4 release notes](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

<!--more-->

## Key takeaways

- **Back up first.** Keep a recoverable copy of the data volume or database and uploads before changing the application.
- **Pin the official release.** Use `ghcr.io/open-webui/open-webui:v0.12.4` for the standard Docker image or `open-webui==0.12.4` for pip.
- **Test permissions with real user roles.** A hidden button is not proof of an API-side authorization check.
- **Keep access private.** Require application authentication and restrict network access through a VPN or an authenticated reverse proxy.

## Before you upgrade

**Prerequisites:** Identify the current installation method, container image variant, persistent data location, external database, reverse proxy, and authentication provider. Arrange an outage window and retain the existing container configuration or service definition. Allow time for a restore rehearsal on a separate instance. The commands below are vendor-documented patterns adapted to this pinned release, not results of a live upgrade performed for this guide. [Updating Open WebUI](https://docs.openwebui.com/getting-started/updating/)

1. **Inventory storage.** For the standard Docker setup, `open-webui` mounts at `/app/backend/data`. Record any bind mounts, external database, object storage, and custom environment variables. For pip, locate the active application data directory and database before changing the environment. Do not assume a chat export is a full backup.
2. **Back up with writes stopped.** Stop the application or use a database-consistent snapshot, then copy the volume and any external database and uploads to separate storage. The vendor documents a Docker volume archive. Adapt the volume name and backup path to your deployment. Confirm the archive opens and rehearse a restore on a separate instance before relying on it. [Backup and restore](https://docs.openwebui.com/getting-started/updating/#backup--restore)
3. **Read the release notes and migration guidance.** The v0.12.4 notes do not enumerate the pending security fixes or give an affected-version range for them. Do not assign those fixes a CVE or assume every version before v0.12.4 is affected by one named flaw. The updating guide warns of one-way database migrations and mixed-version replicas. If several workers or replicas share a database, stop them together and follow the [multi-replica migration procedure](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations). A rollback might require the pre-upgrade database backup.

## Upgrade the installed package

**Docker, vendor procedure adapted to a pinned tag:** After the backup, pull the official standard image and recreate the container with the *same* persistent volume, configuration, and `WEBUI_SECRET_KEY`. This example assumes the default named volume and a locally bound proxy upstream. Do not paste your real key into shell history. Supply it through your existing protected environment or secret-management mechanism. Preserve any GPU, Ollama, custom network, database, or other options from your current deployment. [Updating Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Official image tags](https://docs.openwebui.com/getting-started/quick-start/)

```bash
docker pull ghcr.io/open-webui/open-webui:v0.12.4
docker rm -f open-webui
docker run -d --name open-webui --restart always \
  -p 127.0.0.1:3000:8080 \
  -v open-webui:/app/backend/data \
  --env-file ./open-webui.env \
  ghcr.io/open-webui/open-webui:v0.12.4
```

**Check `./open-webui.env` before running:** It must already exist, have restrictive file permissions, and contain your existing `WEBUI_SECRET_KEY` and required configuration. The loopback binding fits a proxy on the same host, not a proxy on another machine. For Compose, change only the service image to the pinned tag, then use `docker compose pull open-webui` and `docker compose up -d open-webui` in the existing project. Keep the same volume and environment configuration. These are suggested commands, not a tested migration of your deployment.

**pip, vendor update procedure with a fixed version:** In the existing virtual environment, stop the running service, install the exact package release, and restart it with the same data directory and environment. Avoid a second Python environment or a new empty database. The vendor's generic update instruction uses `pip install -U open-webui`. The version constraint below pins this checklist to v0.12.4. [Updating Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Quick Start](https://docs.openwebui.com/getting-started/quick-start/)

```bash
python -m pip install --upgrade 'open-webui==0.12.4'
python -m pip show open-webui
```

**Verify the running service, not only the installed artifact.** Check the startup version in `docker logs open-webui` or your pip service logs and compare it with the application's displayed version after signing in. The vendor's update guide recommends checking the container logs and loading the login page. If the UI shows stale assets, hard-refresh the browser. If startup reports a migration error, keep the service unavailable until you diagnose it. Do not roll an older binary onto a migrated database without checking restore requirements. [Post-update checks](https://docs.openwebui.com/getting-started/updating/)

## Check access after restart

**Vendor release behavior:** v0.12.4 hides folder Export, archived-chat Export, and chat Copy actions for users without **Allow Chat Export**. It also hides Access controls on models, prompts, tools, knowledge, skills, notes, and folders for users without the corresponding sharing permission. Shared-folder viewers stop receiving live chat updates after the owner archives a chat. Share-link viewers stop receiving live updates after the owner unshares all chats. Hidden controls are UI behavior, not evidence of a server-side fix for an unspecified vulnerability. [Release notes](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

**Operator verification, recommended:** With a test account lacking export and sharing permissions, check for the absence of the named actions. With a permitted account, confirm intended actions still work. Create a non-sensitive test chat in a shared folder, view it from another account, archive it as owner, and confirm new updates stop reaching the viewer. Repeat with a share link and **Unshare All Chats**. Recheck saved grants and old links rather than assuming archived content or historical copies are erased.

| Review area | What to verify |
|---|---|
| **Roles and groups** | Remove stale members and administrator assignments. Check the effective permissions of a newly approved user and a restricted user. |
| **Models and tools** | Review each model's access grants, attached tools, tool creation rights, and provider credentials. Test with a non-admin account. |
| **Knowledge and files** | Inspect knowledge-base collaborators, resource grants, attachments, and sharing settings. Check an account whose access was removed. |
| **Chats and exports** | Review shared folders, share links, archived chats, and Allow Chat Export assignments. Revoke links no longer needed. |

These inventory checks are **operator recommendations**, not new guarantees introduced by v0.12.4. The vendor's [hardening guide](https://docs.openwebui.com/getting-started/advanced-topics/hardening/) documents layered roles, groups, per-resource grants, workspace permissions, API keys, and network placement.

## Close account and network gaps

- **Signup, vendor setting:** Disable open signup when accounts are provisioned by an administrator or identity provider. Check `ENABLE_SIGNUP` and any persistent admin settings against the [hardening guide](https://docs.openwebui.com/getting-started/advanced-topics/hardening/). Keep approval rules for new accounts restrictive.
- **API keys, operator review:** Inventory issued keys, delete unused ones, and restrict creation and endpoint access to the roles and routes needed. A key acts with its creator's permissions according to the vendor's hardening guide. Store keys outside article examples and application logs.
- **Admins, operator review:** Remove abandoned admin accounts, enforce strong sign-in controls, review MFA availability, and investigate unexpected account changes. Test the account recovery path before disabling a redundant admin.
- **Network boundary, vendor guidance:** Put the service behind a VPN, access proxy, or reverse proxy with authentication and IP allowlisting. Do not expose it publicly without authentication. Avoid `WEBUI_AUTH=False` on a reachable service. A reverse proxy without its own authentication is not, by itself, a substitute for application sign-in. [Hardening Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)

**Scope:** This checklist applies to the official Open WebUI release and its documented standard installation paths. It does not verify forks, derivative images, or third-party packages. The v0.12.4 notes do not claim active exploitation. Check the [project security advisories](https://github.com/open-webui/open-webui/security/advisories) for later disclosures and their own affected and fixed versions. Do not attribute an earlier advisory's fix to v0.12.4 without reading its version range.

## Sources and references

- [Open WebUI v0.12.4 release notes](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)
- [Open WebUI security advisories](https://github.com/open-webui/open-webui/security/advisories)
- [Updating Open WebUI, including backup, rollback, and migrations](https://docs.openwebui.com/getting-started/updating/)
- [Open WebUI Quick Start and official image tags](https://docs.openwebui.com/getting-started/quick-start/)
- [Hardening Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)
- [Multi-replica updates and migrations](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations)

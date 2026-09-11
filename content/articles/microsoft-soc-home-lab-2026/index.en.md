---
title: "Microsoft SOC Home Lab: Build Cybersecurity Experience in 2026"
date: 2026-09-11
lastmod: 2026-09-11
toc: true
draft: false
description: "Build a Microsoft SOC home lab with Sentinel, Defender, Intune, and Entra. Practice incident investigation, validate passkey policies, and document portfolio evidence."
genre: ["Cybersecurity", "Cloud Security", "Career Development"]
tags: ["SOC home lab", "Microsoft Sentinel", "Microsoft Defender XDR", "Defender for Endpoint", "Defender for Cloud", "Defender for Servers", "Microsoft Intune", "Microsoft Entra ID", "Azure home lab", "cybersecurity experience", "SOC analyst", "security operations center", "incident response", "KQL", "Log Analytics", "Conditional Access", "phishing-resistant MFA", "passkeys", "identity security", "cybersecurity portfolio", "cloud cost management", "endpoint security"]
cover: "/img/cover/microsoft-soc-home-lab.webp"
coverAlt: "A laptop showing security incident timelines on a home desk beneath a cloud containing servers and endpoints."
coverCaption: ""
---

A **security operations center (SOC) home lab** gives you a place to investigate alerts, explain evidence, and test defensive changes. Build a small Microsoft environment, collect its telemetry, and write up each investigation. The useful result is a repeatable investigation with supporting evidence.

This guide develops the lab approach described in Mad Hat's cybersecurity career video and supplied Cyber Range runbook. It uses Microsoft documentation for product requirements and separates setup, detection, and validation into measurable tasks.

## Key Takeaways

- **Start small:** one managed Windows client and one test identity support the first exercises.
- **Verify telemetry:** a visible device or connected portal does not prove logs are arriving.
- **Complete the investigation:** record the trigger, evidence, response, and retest.
- **Control spending:** track licenses, retained data, networking, and compute separately.
- **Describe experience accurately:** list the environment as a lab project on your resume.

## Before You Begin

**Prerequisites:** basic Windows administration, networking, and familiarity with virtual machines. Use a dedicated Microsoft Entra tenant and an Azure subscription reserved for the lab. Keep production identities, personal files, and employer systems outside the exercise.

**Estimated effort:** allow a weekend for the initial setup, followed by focused investigation sessions. This is a planning estimate. Trial approval, quota availability, and service provisioning affect elapsed time. **Difficulty:** intermediate.

Prepare a separate administrative account and an unprivileged test user. Before testing access policies, establish and verify emergency access. Assign privileges for each setup task, then use a lower-privilege account for routine investigation.

| Component | Lab purpose |
|---|---|
| **Sentinel** | Security information and event management, or SIEM, for connected log sources |
| **Defender XDR** | Correlation and investigation across licensed Microsoft security services |
| **Defender for Endpoint** | Endpoint detection and response, or EDR, on onboarded devices |
| **Intune** | Device enrollment and endpoint security policy management |
| **Entra ID** | Identity, sign-in records, and access policy evaluation |
| **Defender for Servers** | Server protection through Defender for Cloud |

## Check Licenses First

**Microsoft 365 E5** is one route to a broad lab, but access depends on the service plans and licenses assigned to the participating users. Office 365 E5 and Microsoft 365 E5 are different bundles. A single administrator's license does not establish coverage for every test user or workload. Review the [Defender XDR prerequisites](https://learn.microsoft.com/en-us/defender-xdr/prerequisites) before selecting a subscription.

**Sentinel in the Defender portal** works without E5 or Defender XDR. Adding XDR introduces its own licensing and configuration requirements. An empty incident view is not evidence of missing E5 licensing. Microsoft's [Sentinel onboarding documentation](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard) explains both configurations.

**Server protection** has a separate licensing path. Defender for Servers integrates with Defender for Endpoint for supported server workloads. Windows client operating systems need appropriate client coverage. Do not treat every Azure VM as an automatically licensed server. See Microsoft's [Defender for Endpoint integration documentation](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

**Trial planning:** confirm eligibility, expiration, renewal settings, and included services in your own account. Avoid budgeting around a promised trial duration or a fixed monthly total from a video.

## Set a Spending Plan

**Azure budgets** send notifications. They do not stop consumption when you reach a threshold. Cost reporting also has a delay. Create alerts early and review spending after each session, following Microsoft's [budget setup guide](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets).

| Cost category | Planning question |
|---|---|
| **User licenses** | Which users need which service plans, and when do trials expire? |
| **Compute** | How many VM hours will each exercise require? |
| **Storage** | Which disks and snapshots remain after shutdown? |
| **Log collection** | Which tables need ingestion and how long should data remain? |
| **Networking** | Does the design include paid Bastion, public IPs, or outbound services? |
| **Server protection** | Which workloads have a paid Defender plan enabled? |

**Design choice:** begin with one client. Add a server when an exercise needs server telemetry. Four clients and several servers add administration and cost before they add useful investigation practice.

## Build the Network

**Suggested layout:** put Azure resources in a clearly named group such as **`rg-soc-lab`**. Use separate client and server subnets, explicit network security group rules, and private management access. Subnet separation alone does not block traffic between workloads.

For a dedicated **Azure Bastion** deployment, follow the SKU requirements, including the reserved **`AzureBastionSubnet`** name and a **`/26`** or larger subnet for current deployments. Developer SKU uses a different deployment model. Review [Bastion configuration settings](https://learn.microsoft.com/en-us/azure/bastion/configuration-settings) before choosing a design.

Keep RDP and SSH closed to the public internet. Restrict management traffic to the selected management path. Allow the outbound service connectivity needed for enrollment and security telemetry.

**Validation:** establish private management access and verify effective network rules before installing workloads. If you add a deliberately vulnerable application later, keep it inside the exercise network and restrict access to the test machines.

## Connect Sentinel and Logs

**Portal setup:** create a Log Analytics workspace and enable Sentinel on it. If the workspace is absent from the Defender portal, open **System > Settings > Microsoft Sentinel > Connect a workspace**. Verify the tenant and required Azure and Entra roles against the [onboarding prerequisites](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard).

**Log collection is a separate step.** In Entra, configure diagnostic settings to send the required activity categories to the same workspace. Start with interactive sign-ins and audit events. Microsoft's [Entra log integration guide](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs) covers the permissions and destination setup.

```kusto
SigninLogs
| where TimeGenerated > ago(24h)
| where UserPrincipalName =~ "soc-test@YOUR-TENANT.onmicrosoft.com"
| project TimeGenerated, UserPrincipalName, AppDisplayName,
          IPAddress, ResultType, ConditionalAccessStatus, CorrelationId
| order by TimeGenerated desc
```

Run this **Kusto Query Language (KQL)** example in the workspace's Logs view after generating a fresh test sign-in. Replace the sample user principal name with your lab user. The columns follow the [SigninLogs table schema](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs).

**Expected result:** a row matching the test account and sign-in time. No rows means you need to check the time range, identity, collection settings, destination, and ingestion delay. A missing table points to a collection or workspace issue before it points to a detection issue.

## Onboard the First Endpoint

**Intune enrollment and EDR onboarding** are separate checkpoints. Connect Intune and Defender for Endpoint, enroll a supported Windows client, then assign an endpoint detection and response onboarding policy to its lab group. Entra registration alone does not establish either checkpoint.

In Intune, check **Endpoint security > Defender for Endpoint**. If the connection is unavailable, enable the Intune connection in Defender's endpoint advanced features. Follow the platform-specific steps in Microsoft's [Intune and Defender integration guide](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/configure-integration).

| Checkpoint | Evidence to capture |
|---|---|
| **Enrollment** | Client appears in Intune with a recent check-in |
| **Policy assignment** | Onboarding policy applies to the intended device group |
| **Sensor reporting** | Defender shows onboarded status and recent telemetry |
| **Detection test** | A documented test produces the expected security signal |

**For servers**, enable the chosen Defender for Servers plan and its endpoint integration, then verify sensor deployment and reporting. Defender for Cloud also discovers machines before onboarding completes. Inventory presence alone is insufficient, as Microsoft explains in its [resource discovery and onboarding guidance](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

## Investigate a Test Alert

**Start with Microsoft's documented EDR detection test** on the lab endpoint. Follow the [current test instructions](https://learn.microsoft.com/en-us/defender-endpoint/edr-detection), including platform prerequisites and troubleshooting. Record the execution time before opening the alert queue.

Treat the resulting alert as an investigation exercise. A security product's title gives you a starting point. Your job is to establish what happened and support the disposition with evidence.

1. **Triage:** identify the alert source, device, account, and event time.
2. **Inspect:** review the process tree, command line, file details, and network activity available for the event.
3. **Scope:** search for related activity on the test identity and other lab devices.
4. **Assess:** explain whether the evidence matches the planned exercise or an unrelated event.
5. **Respond:** document the selected response, its impact, and the recovery steps. Perform supported containment only when the exercise requires it.
6. **Retest:** repeat the relevant test after changing a control and compare the evidence.

**Do not manufacture missing results.** If the alert fails to arrive, preserve the execution record and troubleshoot collection. If a control blocks the test before the expected event, document the prevention result.

## Test Identity Controls

**Adversary-in-the-middle (AiTM) phishing** places an attacker-controlled intermediary in a sign-in flow. The supplied runbook uses this scenario to motivate stronger authentication. For the first identity exercise, test policy behavior directly with your own unprivileged account.

Begin by recording a legitimate sign-in and its authentication details. Review Microsoft's [Entra risk detection reference](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) before interpreting risk signals. Detection prerequisites and processing differ by signal. A new IP address or a failed sign-in does not guarantee an AiTM alert.

**Passkeys (FIDO2)** use credentials bound to the legitimate service rather than reusable codes entered into a relayed login page. Enable an appropriate passkey profile for the pilot group and register the method before enforcing a policy. Follow Microsoft's [passkey configuration guide](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2) for supported authenticators and restrictions.

**Conditional Access exercise:** create a policy targeting only the lab pilot group, exclude emergency access accounts, and select **Require authentication strength > Phishing-resistant MFA strength**. Start in **Report-only**, review its impact, then enable it. This adapts Microsoft's [administrator policy example](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa) to a narrow test group.

| Test | Evidence to collect |
|---|---|
| **Report-only policy** | Sign-in record showing how the proposed policy evaluates |
| **Enforced policy, weaker method** | Fresh authentication requires a stronger method before access |
| **Enforced policy, registered passkey** | Successful sign-in satisfying the required strength |

Use fresh authentication for each comparison and inspect the policy details. Existing sessions complicate comparisons. **Scope of proof:** this exercise validates the authentication requirement. It does not demonstrate universal protection against endpoint compromise or theft of an existing session.

## Write Portfolio Evidence

**A useful portfolio entry** explains a decision another analyst is able to review. Include a short architecture description, the collection prerequisites, the event timeline, and the reasoning behind your response.

```text
Exercise:
Date and UTC time window:
Lab scope and prerequisites:
Trigger and expected signal:
Observed alert or prevention:
Evidence and queries:
Affected identities and devices:
Disposition and reasoning:
Response and recovery:
Control change and retest:
Limitations and follow-up:
```

Replace every field with your own observations. **Sanitize exports:** remove credentials, session material, personal information, and unnecessary identifiers before publishing screenshots or query results.

**Resume example:** "Built a Microsoft security lab, connected identity logs to Sentinel, investigated endpoint test alerts, and documented Conditional Access validation." Use this wording only after completing those tasks. Put it under projects or practical training with the actual dates and scope.

A lab demonstrates independent practice. **Production SOC work** also involves business impact, escalation, service commitments, and coordination with other teams. Explain which parts you practiced and which remain outside your experience.

## Troubleshooting

| Symptom | First check |
|---|---|
| **Workspace absent from Defender** | Same tenant, Sentinel enabled, and onboarding role requirements |
| **SigninLogs absent or empty** | Diagnostic categories, destination workspace, fresh events, and time range |
| **Client absent from Intune** | Enrollment prerequisites and enrollment status |
| **Device visible without telemetry** | Actual onboarding state, sensor health, and outbound connectivity |
| **Onboarding policy unapplied** | Assignment scope, device platform, and recent check-in |
| **No identity risk alert** | Signal prerequisites and recorded activity, without assuming deterministic detection |
| **Unexpected access allowed** | Report-only status, exclusions, resource scope, and existing session |
| **Charges after shutdown** | Allocation state and resources billed independently of compute |

**Troubleshooting order:** prove the event happened, prove collection worked, then investigate detection logic. Record each failure and fix in the project notes.

## Pause or Remove the Lab

**Deallocation** releases VM compute allocation. A guest operating system shutdown alone does not guarantee deallocation. Check Azure's displayed power state and review Microsoft's [VM states and billing documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing).

**Retained resources** still need review. Disks, snapshots, networking services, log retention, and user subscriptions have separate lifecycles. Set a reminder before each trial expires and verify the next usage report after cleanup.

Before deleting the lab resource group, export the evidence you intend to retain and inspect its contents. **Resource group deletion is destructive** for contained resources. Tenant users, Intune policies, Conditional Access policies, subscriptions, and subscription-level security settings require separate cleanup where applicable.

## Next Steps

**Finish one documented investigation** before adding another workload. Then add a server, an identity exercise, or a detection rule with a clear test condition. Track what the added component teaches and what it costs.

Use the [IT home lab guide](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/) for infrastructure practice and the [IT resume guide](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/) to present the work. Keep the next project small enough to explain from setup through evidence and cleanup.

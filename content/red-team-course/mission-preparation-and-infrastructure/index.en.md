---
title: "Module 2: Mission Preparation and Infrastructure"
date: 2026-09-12
lastmod: 2026-09-17
toc: true
draft: false
description: "Everything required before an attack: scope and rules of engagement, deconfliction, hardening the attack platform, standing up redirectors, and validating the infrastructure before go."
genre: ["Red Team", "Offensive Security", "Infrastructure"]
tags: ["red team", "mission preparation", "rules of engagement", "scope", "deconfliction", "redirectors", "attack platform", "red team infrastructure", "C2 infrastructure", "red team course"]
cover: "/img/cover/red-team-mission-preparation-infrastructure.webp"
coverAlt: "An illustration of a high-tech workstation with multiple screens showing network maps and security documents, surrounded by visual elements like firewalls and encrypted data streams, all against a dark background."
coverCaption: "Module 2: ready the paperwork and the platform before the first packet."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Mission preparation** makes an assessment reproducible and controllable before the first test action. Scope, contacts, infrastructure ownership, evidence storage, and teardown belong in the same plan. This module turns the methodology test card into an operational readiness record.

*Allow 25 minutes for reading and 30 minutes for a preparation review. Complete Module 1 and use your own isolated lab for technical checks.*

## Learning Outcomes

- **Define scope:** name approved assets, accounts, actions, and time windows.
- **Explain dependencies:** separate the management path, assessment traffic, and evidence storage.
- **Inspect readiness:** verify the paths the test depends on without assuming a webpage proves everything works.
- **Resolve uncertainty:** pause for a recorded decision when a dependency or target is ambiguous.
- **Create an asset register:** account for ownership, expiration, collection, and removal.

## Scope Is More Than Addresses

**An address list** is only one part of scope. An approved IP might host several tenants, a public hostname might point to a shared provider, and a login might expose both permitted and excluded resources. Record the relevant identities and actions as well as network locations.

**Rules of engagement (ROE)** describe how the assessment is conducted. The document should connect the objective, permitted work, exclusions, contacts, and response to unexpected events. NIST provides a rules-of-engagement template and assessment-planning guidance. [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)

| Boundary | Example entry |
|---|---|
| **Assets** | Named lab hosts and an application tenant identifier |
| **Identities** | Two designated synthetic accounts |
| **Actions** | Approved discovery and one sample-file permission test |
| **Time** | Explicit start, pause, and end times with a time zone |
| **Exclusions** | Production customer data and unrelated tenants |
| **Limits** | Maximum requests, data volume, and permitted configuration changes |

**Asset ownership and authorization are separate facts.** A registration record, DNS response, or customer brand on a page is insufficient to establish permission to test the underlying service. Record any required provider or tenant authorization through the agreed engagement process.

## Make Stop Conditions Operational

**A stop condition** names an observable event and an immediate response. “Be careful” is not a useful instruction. “Pause if the sample query returns a real customer record, preserve the minimal incident reference, and contact the controller” is specific enough for another operator to follow.

**A restart decision** also needs an owner. After a pause, document what changed, who approved resumption, and which actions remain permitted. A timed outage window expiring does not silently renew itself.

| Trigger | Immediate action | Decision owner |
|---|---|---|
| **Unexpected production data** | Stop collection and preserve the minimal reference | Exercise controller |
| **Service health degrades** | Pause the action and record timestamps | Service owner and controller |
| **Unrecognized callback or host** | Stop interaction pending scope verification | Controller |
| **Customer reports an incident** | Compare records through the deconfliction channel | Incident lead |

**Deconfliction should work during an outage.** Test a backup contact path which does not depend on the same application or network under assessment. Record who is able to stop work when the primary controller is unavailable.

## Separate Infrastructure Roles

**The operator workstation** is the management endpoint. A **team server** coordinates the assessment platform when one is used. A **redirector** forwards an approved traffic path, while an **evidence store** retains the records required for analysis and reporting. Some labs combine roles, but their permissions and failure dependencies still differ.

**A redirector is not a guarantee of anonymity.** Hosting, DNS, certificates, network logs, and server administration produce records. Its placement should follow the authorized test architecture and the customer's expected observation points.

{{< figure src="engagement-infrastructure-responsibilities.webp" alt="Diagram separating operator management, assessment infrastructure, approved target systems, and controlled evidence storage" caption="Map ownership and allowed communication for every assessment component" >}}

| Role | Required inventory detail |
|---|---|
| **Operator endpoint** | Responsible operator, authentication, and approved management access |
| **Assessment server** | Owner, version, listeners, and retention settings |
| **Redirector** | Domain, address, forwarding purpose, and expiration |
| **Evidence store** | Access list, encryption, retention, and deletion owner |
| **Target dependency** | Service owner, test boundary, and restoration contact |

**Choose the smallest sufficient topology.** A second approved path helps only if it addresses a real dependency and has its own cleanup plan. Two hosts on one provider, account, or network still share failure conditions. Redundancy is a design decision, not a fixed required number of servers.

## Build a Lab Redirector

Create the redirector as a **small public edge VM** in the customer-approved cloud account or provider account. Keep it separate from the operator workstation, assessment server, and target network. Select a region and jurisdiction approved by the engagement owner. A nearby region reduces avoidable latency, while provider reputation, data handling, and ownership matter more than a particular country.

**The redirector should have one public address and one narrowly defined upstream path.** Put the assessment server behind a private tunnel or an allowlisted origin address. Do not place the redirector inside the customer production network, give it a broad internal route, or reuse it as the evidence store. Those choices turn a forwarding host into an unnecessary bridge.

| Placement decision | Recommended lab choice |
|---|---|
| **Public edge** | Separate low-cost VM in the approved provider account |
| **Origin** | Assessment server on a private tunnel or fixed allowlist |
| **Management** | Provider console or restricted admin source, separate from test traffic |
| **Ingress** | TCP 80/443 only when the test requires them |
| **Egress** | Origin address and approved update or monitoring services |
| **Expiration** | Provider, address, domain, certificate, and VM teardown dates |

For a benign HTTP exercise, install **Nginx** on the edge VM and proxy one named test path to a harmless origin service. The configuration below is a template for a disposable lab. Replace the example names and address with values in the connection matrix.

```bash
sudo apt update
sudo apt install nginx
sudo install -d -m 0750 /etc/nginx/lab
sudoedit /etc/nginx/sites-available/lab-redirector
```

```nginx
server {
    listen 80;
    server_name redirector.lab.example;

    access_log /var/log/nginx/lab-redirector.access.log;
    error_log /var/log/nginx/lab-redirector.error.log warn;

    location = /healthz {
        add_header Content-Type text/plain;
        return 200 "lab redirector ready\n";
    }

    location /lab/ {
        proxy_pass http://10.30.0.10:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Request-ID $request_id;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

**Enable the single site, check the syntax, and reload only after the configuration review:**

```bash
sudo ln -s /etc/nginx/sites-available/lab-redirector /etc/nginx/sites-enabled/lab-redirector
sudo nginx -t
sudo systemctl reload nginx
```

The origin address **must be reachable from the redirector through the approved path**. An RFC 1918 address in `proxy_pass` requires a private tunnel or a routed lab network. It does not create connectivity by itself. The origin should expose only the harmless test service and accept traffic from the redirector's fixed address.

**Test each leg with a unique request identifier.** First query the edge health endpoint, then request the lab path, and finally compare the edge and origin logs. Do not use a payload, credential collector, or unrestricted forward rule for this readiness test.

```bash
curl --fail http://redirector.lab.example/healthz
curl --fail -H 'X-Lab-Request: prep-001' http://redirector.lab.example/lab/healthz
sudo journalctl -u nginx --since '5 minutes ago'
```

**Expected result:** The health endpoint returns the fixed readiness text. The second request appears in the edge access log and the origin log with the same test identifier. A successful edge response without an origin record indicates a configuration, route, or collection problem. These commands are documentation examples for an authorized lab.

**For HTTPS, use a certificate whose name matches the approved test domain** and record its issuer, renewal owner, and expiry. Keep certificate automation separate from the test path. Validate TLS from the same client class used by the exercise, then preserve the certificate and access-log references in the readiness register. [Nginx proxy module documentation](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)

**Backout for the redirector** is part of the build. Remove the enabled site, reload Nginx, revoke or delete the test certificate, remove the DNS record, destroy the VM, and verify the provider account has no remaining address, firewall rule, snapshot, or access key. Retain the agreed logs and teardown evidence instead of deleting the assessment record.

## Protect Management and Evidence

**Management access** should expose only the services and sources needed by the assessment team. Define inbound and outbound requirements independently. A rule permitting all traffic from a broad customer subnet is different from a narrowly scoped management rule.

**Protect the records as well as the listener.** Assessment data includes credentials, screenshots, transcripts, and customer configuration. Restrict access to the people who need it, keep secrets out of command histories and shared notes, and document a retention deadline. [NIST assessment data-handling guidance](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-115.pdf)

| Control | Readiness question |
|---|---|
| **Authentication** | Does each operator have accountable access? |
| **Network policy** | Are necessary sources, destinations, ports, and address families explicit? |
| **Host updates** | Are the selected versions and relevant maintenance decisions recorded? |
| **Secret storage** | Are operational secrets separated from general documentation? |
| **Evidence access** | Is the reviewer able to read the required records without broad administrative access? |
| **Recovery** | Is a known recovery path available before firewall or service changes? |

**Do not apply an incomplete firewall snippet remotely.** A copied default-drop sequence often omits established connections, loopback, management recovery, IPv6, or required infrastructure traffic. Review the actual policy against a connection matrix and test it from a recoverable lab console.

## Inspect Listening Services

On your **Linux assessment server**, inspect current listeners and nftables policy without changing either:

```bash
sudo ss -lntup
sudo nft list ruleset
```

**`ss`** reports socket information. **`-l`** selects listeners, **`-n`** keeps numeric addresses, **`-t`** and **`-u`** include TCP and UDP, and **`-p`** requests process information. Permissions affect which process details appear. [ss manual](https://man7.org/linux/man-pages/man8/ss.8.html)

**`nft list ruleset`** displays nftables configuration. Interpret an empty output in the context of the host's actual firewall stack and any provider firewall. A host-level ruleset alone does not describe every control on the network path. [Netfilter ruleset-management documentation](https://wiki.nftables.org/wiki-nftables/index.php/Operations_at_ruleset_level)

**Expected exercise result:** Every listening socket has a documented purpose and owner. An unexpected listener is a finding to explain before launch, not something to terminate blindly. Compare the output with the connection matrix and preserve the timestamp.

## Verify Each Connection Leg

**A browsable HTTPS endpoint** establishes only the behavior of the request you sent. It does not establish the management path, an internal forwarding rule, the intended application exchange, or evidence collection. Test the intended path in a closed range using harmless test traffic.

| Leg | Check | Evidence |
|---|---|---|
| **Name resolution** | Resolve the approved domain through the intended resolver | Name, address, resolver, and time |
| **TLS endpoint** | Check the certificate and successful negotiation | Hostname, validity, and observed endpoint |
| **Forwarded request** | Send the designated harmless lab request | Matching ingress and application records |
| **Management path** | Authenticate through the approved operator route | Operator identity and access log |
| **Evidence collection** | Locate the test record in the chosen store | Record identifier and collection time |

**Correlation beats assumption.** Give the harmless test request a unique lab identifier and follow it through the expected logs. If the public endpoint succeeds but the downstream record is absent, investigate forwarding or collection before treating the entire path as ready.

## Domains, Certificates, and Mail

**A TLS certificate** supports authentication of the endpoint named in the certificate under the client's trust rules. It does not certify the purpose or authorization of an assessment. Domain categorization also does not guarantee a filtering product permits traffic. Verify actual policy behavior in the approved test conditions.

**A mail exercise** needs a separate delivery plan. Record the sending service, approved recipients, expected message handling, and reporting channel. Begin with an inert message and a synthetic destination so routing and attribution are checked before the campaign-specific work in Module 10.

| Item | What to record |
|---|---|
| **Domain** | Registrant or responsible owner, purpose, and expiration |
| **Certificate** | Subject names, issuer, validity, and renewal owner |
| **Mail sender** | Account, sending service, authentication, and permitted recipients |
| **Delivery test** | Message identifier, expected route, and observed result |
| **Teardown** | Required revocation, removal, and evidence of completion |

**Reputation is not a substitute for measurement.** A newly registered domain being blocked is a meaningful observation about the tested policy. Whether the test should continue through another route depends on the objective and a recorded controller decision.

## Supplemental Video

{{< youtube id="X4VuzccCDTU" enable="true" title="Micro Emulation Plans: Making Adversary Emulation Accessible" >}}

**Watch:** [Micro Emulation Plans: Making Adversary Emulation Accessible](https://www.youtube.com/watch?v=X4VuzccCDTU), published by SANS Offensive Operations and featured by the [MITRE Center for Threat-Informed Defense](https://ctid.mitre.org/videos/micro-emulation-plans/). Use the discussion of bounded tests to identify which infrastructure a particular objective needs.

**Viewing task:** Choose one proposed test and list its required identities, hosts, network paths, and observations. Remove components which do not support the test. Explain the remaining dependencies and how the operator would recognize a failed prerequisite.

## Rehearse Deconfliction

**Tabletop scenario:** At 14:20 UTC, the customer reports an unexpected connection from an address assigned to the exercise. Your notes contain a different destination and a test completed ten minutes earlier. The address is shared by two approved operators.

**Expected reasoning:** The shared source is insufficient attribution. Compare the destination, time, account, process or request identifier, and each operator's record. Pause relevant activity while the incident lead determines whether the event belongs to the assessment. Do not label unmatched activity as yours to simplify the conversation.

```text
Exercise and action ID:
Time, time zone, and known clock offset:
Operator and approved source:
Target asset and account context:
Intended action and expected effect:
Observed result and evidence reference:
Unexpected behavior:
Pause/resume decision and owner:
```

**Review the rehearsal** by checking whether another operator reconstructs the sequence from the record alone. Missing timestamps or shared anonymous access make the record less useful. Correct those gaps before the launch decision.

## Create the Readiness Register

**Build one row per asset** using the template below. Include temporary domains, provider accounts, test identities, storage locations, and any persistent assessment component. An artifact absent from the register is easy to miss during teardown.

```text
Asset identifier and purpose:
Owner and approved operator:
Address / domain / tenant / host:
Required inbound and outbound paths:
Authentication and secret location:
Evidence and retention location:
Expiration or removal deadline:
Recovery and teardown procedure:
Verification result and reviewer:
```

**Go/no-go exercise:** Your listeners are reachable, but the backup contact has not been tested and the evidence store rejects writes. Decide whether the operational prerequisites are satisfied. Separate technical connectivity from the ability to control and document the assessment.

**Expected answer:** The launch criteria are incomplete. Fix the failed evidence path, test the contact path, and record the verification. A functional connection alone does not satisfy the preparation requirements.

## Next Steps

**Retain the readiness register** alongside the Module 1 test card. Continue with **[Module 3: Networking and Active Directory Foundations](/red-team-course/foundations-networking-and-active-directory/)** to interpret the connections and identities the plan depends on. Return to the **[course hub](/red-team-course-start/)** for the complete sequence.

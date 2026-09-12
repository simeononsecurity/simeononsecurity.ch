---
title: "Cloudflare Tunnel vs Access: Do You Need Both?"
date: 2026-09-11
lastmod: 2026-09-11
toc: true
draft: false
description: "Understand Cloudflare Tunnel vs Access, choose protection for a home dashboard, and avoid publishing a private application without authentication."
genre: ["Network Security", "Self-Hosted", "Cloud Security"]
tags: ["Cloudflare Tunnel", "Cloudflare Access", "Cloudflare Tunnel vs Access", "Cloudflare Zero Trust", "cloudflared", "self-hosted applications", "homelab security", "remote access", "identity provider", "access policies", "application authentication", "public hostname", "origin protection", "outbound tunnel", "service tokens", "Service Auth", "MFA", "private dashboard", "reverse proxy", "CGNAT"]
cover: "/img/cover/cloudflare-tunnel-vs-access.webp"
coverAlt: "A home server connects through a transparent passage to a cloud gateway with a separate identity checkpoint."
coverCaption: ""
---

**Cloudflare Tunnel** connects your application to Cloudflare. **Cloudflare Access** controls who reaches it. For a private home dashboard exposed through a public hostname, use both. A functioning tunnel alone does not add an identity check. [Cloudflare's application publishing guide](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) explains this distinction.

## Key Takeaways

- **Explain the route:** distinguish the connector, origin, and identity check.
- **Configure a policy:** admit named people to one private dashboard.
- **Evaluate protection:** test allowed, denied, and alternate access paths.
- **Design access:** document separate requirements for visitors and automation.

## Before You Begin

**Audience:** home-server owners deciding how to protect a browser dashboard. The worked example assumes an active domain on Cloudflare, a working local web application, and permission to administer both. **Estimated effort:** 20–30 minutes for the policy exercise after connector setup. **Difficulty:** beginner to intermediate.

**Reading path:** start with the product roles, follow one request, then configure and review a small policy. Finish by writing an access specification for your own service.

## What Each Product Does

The **origin** is the server running your application. The **`cloudflared`** connector initiates connections from your infrastructure to Cloudflare, so the origin does not need a publicly routable IP address. Requests and responses then travel over the established connection. [Cloudflare Tunnel overview](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

| Question | Tunnel | Access |
|---|---|---|
| **How does Cloudflare reach my server?** | Establishes the connection | Does not replace origin connectivity |
| **Who gets through?** | Does not supply a user login by itself | Evaluates configured access policies |
| **What do I configure?** | Connector and application route | Application, identity provider, and policies |
| **What does success prove?** | The origin is reachable through the route | A request satisfied the configured policy |

An **identity provider (IdP)** authenticates the visitor. An **Access policy** defines an action and matching criteria. Allow admits matching users. Bypass disables Access enforcement for matching traffic. [Access policy reference](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

## Follow One Browser Request

For **`dashboard.example.com`**, the logical request path is:

```text
Browser -> Cloudflare Access -> tunnel connection -> cloudflared -> dashboard
               |
               +-> identity provider when authentication is needed
```

The **connector initiates the tunnel connection outward** from your network. Browser requests then travel toward the origin over this established connection. An outbound connection carrying inbound application requests is the central reason Tunnel works without a conventional forwarded origin port. [Tunnel connection model](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

**Application permissions** remain another decision. Admission to a dashboard does not automatically specify who should edit its settings or delete its data. If the application has viewer and administrator roles, configure and test those roles separately.

For example, **a family viewer** needs permission to see backup status, while you need permission to change backup destinations. Write those requirements before selecting identities. Two people passing the same Access check should not automatically receive the same application privileges.

## When You Need Both

**The audience determines the protection.** Compare these arrangements before publishing a route:

| Intended audience | Suggested arrangement | Review before use |
|---|---|---|
| **Anyone reading a public website** | Tunnel if needed for origin connectivity | Public exposure is intentional |
| **You and a few family members** | Tunnel plus Access | Allow only the intended identities |
| **An existing public origin** | Access with separate origin protection | Direct origin access must not bypass the check |
| **A scheduled script** | Tunnel plus a Service Auth policy | The client supports the authentication method |

**Access without Tunnel** is supported for an already reachable origin. Protect alternate routes to the server as well. Cloudflare recommends creating the Access application first when publishing a new tunnel route. [Self-hosted application requirements](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/).

*For a private home dashboard reached through a public hostname, start with Tunnel plus Access.*

## Configure a Dashboard Policy

Use this **worked configuration** for two intended visitors. Replace both example addresses with identities you control. Create the Access application before adding the public tunnel route.

1. **Application:** open Zero Trust → Access controls → Applications and create a self-hosted application with a public hostname.
2. **Hostname:** enter the dedicated dashboard hostname. Leave the path unrestricted for this whole-hostname example.
3. **Policy:** create an Allow policy named `Dashboard viewers`.
4. **Identity selector:** add an Include rule using Emails, with `alice@example.com` and `bob@example.com` replaced by your two intended addresses.
5. **Login:** select the identity provider used by those visitors and choose a deliberate session duration.
6. **Route:** save the application, then connect the hostname to the dashboard through your tunnel.

The [official application workflow](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) documents these settings. **Expected result:** a new visitor encounters authentication before reaching the application. Complete the denied-identity test below before relying on the policy.

## Interpret the Rule Logic

**Include** combines alternatives with OR. **Require** adds mandatory conditions with AND. **Exclude** removes matching users. Adding another Include condition broadens the eligible group. [Access rule semantics](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

| Policy fragment | Logical effect |
|---|---|
| **Include Alice or Bob** | Either named identity qualifies |
| **Include Alice, Include a country** | People matching the country also qualify |
| **Include Alice, Require a country** | Alice must also match the country |

**Policy-review exercise:** your requirement names only Alice and Bob, but your colleague adds a country as another Include condition. Reject the change because it admits an additional population. Geography does not establish membership in your household.

## Authenticate Scheduled Scripts

A **service token** contains a Client ID and Client Secret for automated requests. Configure the application policy to accept the token using **Service Auth**. Creating a token without the corresponding policy does not grant application access. [Cloudflare service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

For a backup script or monitoring check, keep the **secret** in the tool's protected credential storage. Give each integration a distinct token name and a deliberate expiration date. Rotate or revoke its token when retiring the integration. The service-token documentation covers these lifecycle operations.

**Client compatibility** deserves an explicit check. A tool expecting an API response will not necessarily handle an interactive browser login. Confirm its support for request headers or another supported authentication method before choosing the policy.

## Test Access Decisions

Treat these as **acceptance checks** for your deployment:

| Check | Evidence to record |
|---|---|
| **Signed-out visitor** | Access intercepts a request from a fresh browser session |
| **Allowed identity** | The intended application loads after sign-in |
| **Disallowed identity** | An unlisted account receives no application access |
| **Alternate route** | Old DNS names and origin ports provide no unintended access |
| **Automation** | The approved client succeeds and a request without its credential fails |

**A visible login screen** proves only one path encountered authentication. Test the denied case and alternate routes too. These are suggested checks, not results from a deployed example.

## Check the Origin Boundary

**An origin trusting Access identity** should validate the signed application token. Cloudflare forwards it in the **`Cf-Access-Jwt-Assertion`** header. A header's presence alone does not prove authenticity. [Cloudflare JWT validation](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/).

A **JSON Web Token (JWT)** carries signed claims. Use the documented validation approach, including the expected issuer and application audience, when integrating Access identity into an origin. Decoding a token and reading an email field is insufficient validation.

**Issuer** identifies the authority issuing the token. **Audience** identifies its intended application. Check token validity and expiration through a supported validation library, instead of implementing signature checks from scratch.

**Keep the boundary explicit:** identify where validation happens and which routes reach the application. An old port forward or alternate hostname deserves its own review, even after the main hostname passes every browser test.

## Troubleshoot Policy Mismatches

| Observation | Next check |
|---|---|
| **An unexpected visitor gets through** | Review Include conditions, Bypass policies, and hostname coverage |
| **An intended visitor is denied** | Compare the signed-in identity with the exact selector values |
| **A script receives a login page** | Review its credential and Service Auth policy |
| **An admitted viewer edits settings** | Review the application's own role assignments |

**Session behavior** also affects retesting. Access has several session durations, including application and global sessions. Record the session setting and use a fresh session when checking a new identity. [Access session management](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/).

## Write Your Access Specification

Create a **short specification** before adding another service:

```text
Service and hostname:
Human identities allowed:
Application roles required:
Automation credential and expiry:
Other routes to the origin:
Where Access tokens are validated:
Allowed-identity test result:
Denied-identity test result:
```

**Completion criterion:** another administrator should understand who gets access, how each client authenticates, and which evidence proves denial. If you add a monitoring integration later, update its credential entry and repeat the unauthenticated request check.

## Next Steps

Follow the site's [Cloudflare Tunnel setup guide](/guides/how-to-setup-and-use-cloudflare-tunnels/) for connector setup, then apply the [official Access application workflow](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/). For a cellular connection, read [T-Mobile Home Internet port-forwarding limits](/articles/t-mobile-home-internet-port-forwarding/) before choosing your remote-access route.

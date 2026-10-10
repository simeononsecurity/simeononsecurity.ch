---
title: "Setting Up Cloudflare Tunnels"
draft: false
toc: true
date: 2023-05-26
lastmod: 2026-10-10
description: "Learn how to set up Cloudflare Tunnels to simplify and protect your network traffic, enhancing performance and security."
tags: ["Cloudflare Tunnels", "Network Security", "Website Performance", "Proxy Server", "Web Traffic", "Network Configuration", "Ubuntu Server", "Cloudflare Account", "Authentication", "Tunnel Creation", "Traffic Routing", "DNS Records", "Secure Connection", "Website Hosting", "Proxy Service", "Network Protection", "Performance Optimization", "Cloudflare Integration", "Server Configuration", "Traffic Encryption", "Network Traffic Management", "Secure Web Hosting", "Website Security", "Ubuntu Setup", "Tunneling Technology", "Cloudflare Services", "Network Performance", "Web Security", "Server Security", "Traffic Management", "Cloudflare Proxy"]
cover: "/img/cover/An_illustration_showing_a_network_tunnel_connecting_a_local.webp"
coverAlt: "An illustration showing a network tunnel connecting a local server to the Cloudflare logo, symbolizing the secure and simplified network traffic."
coverCaption: ""
---

**A Guide on Setting Up Cloudflare Tunnels**

## Introduction
Cloudflare Tunnels provide a secure way to host websites by establishing a direct connection between your local network and Cloudflare. This guide will walk you through the process of setting up Cloudflare Tunnels to enhance the security and performance of your website.

______

## Why Cloudflare Tunnels?
Cloudflare Tunnels offer several benefits, including reducing attack vectors and simplifying network configurations. By using Cloudflare as a proxy, you can close off external ports and ensure all traffic goes through Cloudflare's secure network. This provides an additional layer of protection for your website.

______

## Prerequisites
Before setting up Cloudflare Tunnels, make sure you have the following:

1. An active Cloudflare account.
2. A server running Ubuntu.

______

## Current Linux Installation

Cloudflare's current Linux instructions use the Cloudflare package repository. The GitHub download command in Step 1 stays below as an alternate installation path. Check the installed version before creating a tunnel.

```bash
sudo mkdir -p --mode=0755 /usr/share/keyrings
curl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared any main" | sudo tee /etc/apt/sources.list.d/cloudflared.list
sudo apt-get update
sudo apt-get install cloudflared
cloudflared --version
```

See Cloudflare's [current download instructions](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/) for packages and architectures other than Ubuntu amd64.

______

## Step 1: Installation
To begin, you need to install the Cloudflare Tunnels package on your Ubuntu server. Follow these steps:

1. Open the terminal on your Ubuntu server.
2. Download the latest version of the Cloudflare Tunnels package by running the following command:

```shell
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
```

## Step 2: Authentication
Next, you need to authenticate your Cloudflare account with the Cloudflare Tunnels service. Follow these steps:

1. Run the following command in the terminal:

```shell
cloudflared tunnel login
```

2. Click on the site you'd like to use with your tunnel to complete the authentication process.

The login command opens a browser and writes `cert.pem` in the current user's `~/.cloudflared` directory. This certificate authorizes local tunnel management. Store the certificate on the administrator's system with restrictive file permissions. The JSON file created in Step 3 belongs to one tunnel, so protect the file separately.

______

## Step 3: Creating a Tunnel

Now it's time to create your Cloudflare Tunnel. Follow these steps:

1. Run the following command in the terminal to create a tunnel:

```shell
cloudflared tunnel create name_of_tunnel
```

2. Choose a name for your tunnel that is memorable and descriptive. Note that the tunnel name can't be changed later.

3. After creation, note the UUID in the command output. Use the UUID for later configuration.

4. To view a list of all active tunnels, use the command:

```shell
cloudflared tunnel list
```

This will display the names and UUIDs of your tunnels.

### Named Tunnel Workflow

The name maps to a stable tunnel UUID. Record both values and the credentials file path in your deployment notes.

```bash
cloudflared tunnel create app-prod
cloudflared tunnel list
cloudflared tunnel info app-prod
```

Cloudflare's [current local-management guide](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/) covers named tunnel creation and inspection.

### Step 4: Configuring the Tunnel

To configure your tunnel and start routing traffic, follow these steps:

1. Navigate to the Cloudflare Tunnels directory on your server. The default location is `/etc/cloudflared`.

2. Within this directory, create a new file named `config.yml` using a text editor of your choice.

3. Populate the config.yml file with the following contents:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json
```

Make sure to replace `<your_tunnels_uuid>` with the UUID of your tunnel, and update the path to the credentials file if necessary.

For a Linux service, place `config.yml` and the JSON credentials file in the service user's `.cloudflared` directory, or pass the configuration path explicitly. Running the installer with `sudo` changes `$HOME` to `/root`, so a file under a normal user's home directory needs an explicit path. See [Cloudflare's Linux service instructions](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/linux/).

## Step 5: Routing Traffic

To specify the internal services you want to serve through your tunnel, follow these steps:

1. Open the `config.yml` file again.

2. Add the ingress parameters to the file to define the services you want to route through Cloudflare. For example:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json

ingress:
  - hostname: example.com
    service: http://10.10.10.123:1234
  - hostname: subdomain.example.com
    service: http://10.10.10.123:8888
  - service: http_status:404

```

Replace `<your_tunnels_uuid>` with your tunnel's UUID, and update the hostname and service details according to your configuration.

3. Save the config.yml file.

### Ingress Rule Order

Cloudflared evaluates ingress rules from top to bottom. Put specific host and path rules before broad rules. Keep the final `http_status:404` rule. The final rule rejects unmatched hostnames instead of sending them to an unintended origin.

Validate the file before starting the tunnel, then test which rule matches a hostname:

```bash
cloudflared tunnel ingress validate
cloudflared tunnel ingress rule https://example.com
```

The [current configuration reference](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/) documents rule matching, path behavior, and validation.


## Step 6: Creating DNS Records

To create DNS records for your tunnel's hostname and services, follow these steps:

1. Open the terminal.

2. Use the following command to create a DNS record:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> <hostname>
```
Replace `<UUID or NAME of tunnel>` with the UUID or name of your tunnel, and `<hostname>` with the desired hostname for your service.

3. For example, to create a DNS record for example.com, run the command:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> example.com
```

Please note that the changes will be reflected in the DNS section of your Cloudflare dashboard.

### DNS and Origin Requirements

The zone must exist in Cloudflare and use active Cloudflare nameservers. The DNS route creates a CNAME to `<UUID>.cfargotunnel.com`. The route does not start the tunnel and does not repair an origin service.

Check the origin from the host running `cloudflared`:

```bash
curl -I http://10.10.10.123:1234
ss -ltnp
```

The service address and port in `config.yml` must match a listener reachable from the `cloudflared` process. Use `127.0.0.1` for a service on the same host when no other local network client needs access. For a service on another host, restrict the origin firewall to the tunnel host or an approved internal path.

For an HTTPS origin, the certificate name must match the hostname expected by `cloudflared`. Set an explicit origin server name when the certificate uses a name different from the local service address. Do not disable TLS verification as a first troubleshooting step. See [Cloudflare's origin parameters](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/).

The tunnel connection uses outbound port `7844` over UDP or TCP. Permit outbound traffic and return traffic on the selected protocol. No inbound port forwarding is required for the tunnel connection. Cloudflare lists the checks in its [connectivity pre-check guide](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/).

## Step 7: Starting the Tunnel

To test and start your Cloudflare Tunnel, follow these steps:

1. Open the terminal.

2. Run the following command to start the tunnel:

```shell
cloudflared tunnel run <UUID or NAME of tunnel>
```

Replace `<UUID or NAME of tunnel>` with the UUID or name of your tunnel.

3. Cloudflared will now set up your tunnel and display information about its status. Once the tunnel is successfully up and running, you can proceed to the next step.

4. To prevent the tunnel from closing when you exit the terminal, you need to run Cloudflared as a systemd service. Use the following command:

```shell
cloudflared --config /path/to/config.yml service install
```

Replace `/path/to/config.yml` with the path to your `config.yml` file.

## Service Operation

Use an explicit config path when the file lives under a normal user's home directory:

```bash
sudo cloudflared --config /home/<USER>/.cloudflared/config.yml service install
sudo systemctl enable --now cloudflared
sudo systemctl status cloudflared
sudo journalctl -u cloudflared -f
```

After changing `config.yml`, restart the service and check its status. The service keeps the connector running after logout and across reboots. Cloudflare's [service guidance](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/) covers the supported service modes.

## Access Policy Boundaries

Cloudflare Tunnel provides the connection between Cloudflare and the origin. It does not authenticate application users by itself. A published hostname without an Access application follows the exposure rules in DNS, tunnel ingress, and the origin firewall.

| Control | Purpose |
|----------|---------|
| **Tunnel** | Connects `cloudflared` to the Cloudflare network through outbound connections |
| **Ingress rule** | Selects the origin service for a hostname or path |
| **Cloudflare Access** | Checks identity, group, device, session, and other policy conditions |
| **Origin firewall** | Limits direct access to the service and protects the origin if another route appears |

For a private web application, create a self-hosted Access application for the exact hostname. Add an Allow policy for the intended identity group, then test an allowed account and an unlisted account. Access policies define who receives access. They do not replace the tunnel route or the origin service. See [Cloudflare's Access policy guide](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/policy-management/).

Use application paths when one hostname contains areas with different access rules. A more specific path takes precedence, so protect administrative paths with their own policy. See [Cloudflare's application path guidance](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/app-paths/).

## Logging and Monitoring

Systemd sends service output to the journal. Follow journal output during startup and after configuration changes:

```bash
sudo journalctl -u cloudflared --since "15 minutes ago"
sudo journalctl -u cloudflared -f
```

For a short interactive test, run the tunnel with debug logging. For persistent local logs, use a log directory and apply the host's normal retention controls:

```bash
cloudflared tunnel --loglevel debug run <UUID or NAME>
cloudflared tunnel --loglevel info --log-directory /var/log/cloudflared run <UUID or NAME>
```

For account-level live logs, authenticate `cloudflared` and use:

```bash
cloudflared tail <UUID or NAME>
cloudflared tunnel diag
```

Tunnel logs cover the connector-to-Cloudflare connection and requests between `cloudflared` and the origin. Remote log streaming drops entries under high throughput, so use local service logs when a complete record matters. Cloudflare documents [log streams](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/) and [diagnostic logs](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/).

## Troubleshooting

| Symptom | First checks |
|---------|--------------|
| **Healthy tunnel, failed application** | Run `curl` against the origin from the `cloudflared` host. Check the service scheme, port, bind address, and origin TLS name. |
| **Inactive or Down tunnel** | Run `sudo systemctl status cloudflared`, inspect `journalctl`, and review `cloudflared tunnel list`. |
| **Degraded tunnel** | Check outbound and return traffic on port `7844`, then inspect connector errors. |
| **Hostname does not resolve** | Confirm the zone's nameservers, rerun `cloudflared tunnel route dns`, and inspect the CNAME. |
| **Access denies an expected user** | Check the hostname and path in the Access application, policy order, identity group, identity provider, and session state. |
| **Unexpected origin exposure** | Review every ingress rule, public DNS record, origin listener, and inbound firewall rule. |

Tunnel status reports the connector's relationship with Cloudflare. A `Healthy` status does not prove reachability of the internal origin. Cloudflare lists this boundary and the status meanings in [Common errors](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/).

When Cloudflare connectivity fails, run the network checks from the same host. When the host reaches Cloudflare but the application fails, test the origin locally before changing tunnel settings. This separates connector failures from origin failures.

## Safe Exposure Checks

Run these checks before declaring a published service ready:

1. Confirm the public hostname resolves to a Cloudflare CNAME and does not publish the origin's public IP.
2. Confirm the origin service responds from the tunnel host.
3. Confirm the public hostname returns the expected application response.
4. Request an unmatched hostname and confirm the final ingress rule returns `404`.
5. Confirm the origin firewall blocks unwanted inbound access and permits only the intended internal source.
6. Test an allowed Access identity and an unlisted identity in separate browser sessions.
7. Record the tunnel UUID, hostname, origin address, policy name, service unit, and last validation date.

The [Cloudflare firewall guidance](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/) describes a positive model with blocked ingress and only the required `cloudflared` egress.

## Current Deployment Checks

Cloudflare's current documentation separates published applications from private-network routes. A published application becomes reachable at its hostname. A private CIDR route requires enrolled client devices and an access policy. Read the [current tunnel creation guide](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/) before choosing the route type.

For a locally managed tunnel, the core command sequence remains:

```shell
cloudflared tunnel create my-app
cloudflared tunnel route dns my-app app.example.com
cloudflared tunnel --config /etc/cloudflared/config.yml run my-app
```

The configuration should end with a catch-all rule so unmatched requests fail instead of reaching an unintended service:

```yaml
ingress:
  - hostname: app.example.com
    service: http://127.0.0.1:8080
  - service: http_status:404
```

Before publishing, test the origin locally, confirm the service binds to the intended interface, and place authentication in front of administrative applications. A tunnel removes the need for an inbound port in the common outbound-connector model. A tunnel does not replace application authentication, authorization, patching, logging, or data classification.

When a connector fails, run `cloudflared tunnel list`, inspect the service logs, confirm outbound connectivity to Cloudflare, and verify the credentials-file path. Cloudflare's [useful commands](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/tunnel-useful-commands/) and [tunnel troubleshooting guide](https://developers.cloudflare.com/cloudflare-one/troubleshooting/tunnel/) cover the current command names and common errors. Treat a tunnel token as a secret. Rotate a token after exposure in shell history, logs, screenshots, or a shared repository.

## Conclusion

In this guide, we have covered the steps to set up Cloudflare Tunnels on Ubuntu. By following these instructions, you can enhance the security and performance of your website by using Cloudflare's network. Remember to regularly monitor your tunnels and adjust the configuration as needed.

If you encounter any issues or need further assistance, refer to the [official Cloudflare Tunnels documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/).


## References
- [Cloudflare Tunnels Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)
- [Cloudflare Tunnels GitHub Repository](https://github.com/cloudflare/cloudflared)
- [tcude - How to Set Up Cloudflare Tunnels on Ubuntu](https://tcude.net/creating-cloudflare-tunnels-on-ubuntu/)

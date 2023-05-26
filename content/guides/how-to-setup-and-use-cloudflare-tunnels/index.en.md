---
title: "Setting Up Cloudflare Tunnels: Streamline and Secure Your Network Traffic"
draft: false
toc: true
date: 2023-05-26
description: "Learn how to set up Cloudflare Tunnels to streamline and protect your network traffic, enhancing performance and security."
tags: ["Cloudflare Tunnels", "Network Security", "Website Performance", "Proxy Server", "Web Traffic", "Network Configuration", "Ubuntu Server", "Cloudflare Account", "Authentication", "Tunnel Creation", "Traffic Routing", "DNS Records", "Secure Connection", "Website Hosting", "Proxy Service", "Network Protection", "Performance Optimization", "Cloudflare Integration", "Server Configuration", "Traffic Encryption", "Network Traffic Management", "Secure Web Hosting", "Website Security", "Ubuntu Setup", "Tunneling Technology", "Cloudflare Services", "Network Performance", "Web Security", "Server Security", "Traffic Management", "Cloudflare Proxy"]
cover: "/img/cover/An_illustration_showing_a_network_tunnel_connecting_a_local.png"
coverAlt: "An illustration showing a network tunnel connecting a local server to the Cloudflare logo, symbolizing the secure and streamlined network traffic."
coverCaption: ""
---

**A Guide on Setting Up Cloudflare Tunnels**

## Introduction
Cloudflare Tunnels provide a secure way to host websites by establishing a direct connection between your local network and Cloudflare. This guide will walk you through the process of setting up Cloudflare Tunnels to enhance the security and performance of your website.

______

## Why Cloudflare Tunnels?
Cloudflare Tunnels offer several benefits, including reducing attack vectors and simplifying network configurations. By utilizing Cloudflare as a proxy, you can close off external ports and ensure all traffic goes through Cloudflare's secure network. This provides an additional layer of protection for your website.

______

## Prerequisites
Before setting up Cloudflare Tunnels, make sure you have the following:

1. An active Cloudflare account.
2. A server running Ubuntu.

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

## Step 3: Creating a Tunnel

Now it's time to create your Cloudflare Tunnel. Follow these steps:

1. Run the following command in the terminal to create a tunnel:

```shell
cloudflared tunnel create name_of_tunnel
```

2. Choose a name for your tunnel that is memorable and descriptive. Note that the tunnel name cannot be changed later.

3.After creating the tunnel, you will be provided with important information, including the UUID of your tunnel. Make a note of this UUID as it will be required for further configuration.

4. To view a list of all active tunnels, use the command:

```shell
cloudflared tunnel list
```

This will display the names and UUIDs of your tunnels.

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

## Step 5: Routing Traffic

To specify the internal services you want to serve through your tunnel, follow these steps:

1. `Open the `config.yml` file again.

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

## Conclusion

In this guide, we have covered the steps to set up Cloudflare Tunnels on Ubuntu. By following these instructions, you can enhance the security and performance of your website by leveraging Cloudflare's network. Remember to regularly monitor your tunnels and adjust the configuration as needed.

If you encounter any issues or need further assistance, refer to the [official Cloudflare Tunnels documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/).


## References
- [Cloudflare Tunnels Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)
- [Cloudflare Tunnels GitHub Repository](https://github.com/cloudflare/cloudflared)
- [tcude - How to Set Up Cloudflare Tunnels on Ubuntu](https://tcude.net/creating-cloudflare-tunnels-on-ubuntu/)
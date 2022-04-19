---
title: "Improve Helium Syncing Speeds by Creating a Helium Blockchain Cache"
draft: false
toc: true
description: "The helium network is experiencing multiple issues, including syncing. Implement this to improve things and increase your profitability."
tags: ['Fix Helium Miner Syncing Issues', 'Helium Miner', 'HNT', 'Fix Syncing Issues', 'Helium Blockchain', 'Docker', 'Docker Watchtower', 'Virtual Private Server', 'Cron', 'Cron Jobs']
---

# Improve Helium Syncing Speeds by Creating a Helium Blockchain Cache

What we are going to do today is install the official helium miner docker container, the same one that runs on your actual helium miner, but on a VPS or Linux VM. We are doing this because we want a centralized copy of the helium blockchain that we control. Additionally, we'll have at least two devices downloading the blockchain data so at the bare minimum this will improve syncing speeds. This does scale, very well in fact, with multiple miners. Just duplicate the cron script below.


## Required:
- General Linux Knowledge
- A Port Forwarded and Not Relayed Helium Miner 
- A VPS or Linux VM

## Setting up a Linux VM:
I'm going to assume that you have some basic linux skills and know how to set up a VPS or linux vm. 
If you need some help, check out the following resources to create a ubuntu VPS for as little as $5/month:
 - [https://docs.digitalocean.com/products/droplets/how-to/create/](https://docs.digitalocean.com/products/droplets/how-to/create/)
 - [https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)

## Setting up the Helium Blockchain "Cache":
### Installing the Required Software:
***Note:*** Anywhere where you see "xxx.xxx.xxx.xxx" replace it with your helium miner's public IPv4 address.
Run the following commands to install docker and install the docker, the helium docker container, and watchtower for automatic updates:
```bash
#Install Docker
#https://docs.docker.com/engine/install/ubuntu/
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

#Install the helium docker container
sudo mkdir /root/miner_data
docker run -d --env REGION_OVERRIDE=US915 --restart always --publish 1680:1680/udp --publish 44158:44158/tcp --name miner --mount type=bind,source=/root/miner_data,target=/var/data quay.io/team-helium/miner:latest-amd64

#Set the miner to auto restart when the host restarts
sudo docker update --restart unless-stopped $(docker ps | grep miner | awk '{print $1}')

#Install Watchtower for auto docker container updates
#https://github.com/containrrr/watchtower
docker run --detach --name watchtower --volume /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower
```
### Creating the Syncing Script:
Now we have the miner docker container setup, we'll need to set up syncing to and from your helium miners.
Modify this script with your helium miners public IPv4 addresses:
```bash
docker exec miner miner peer connect /ip4/xxx.xxx.xxx.xxx/tcp/44158 

docker exec miner miner peer sync /ip4/xxx.xxx.xxx.xxx/tcp/44158

docker exec miner miner peer fastforward /ip4/xxx.xxx.xxx.xxx/tcp/44158

docker exec miner miner peer book -s

docker exec miner miner repair sync_state
docker exec miner miner info p2p_status
docker exec miner miner info height
docker exec miner miner versions
docker exec miner miner info summary
```
then run ```nano ./miner_sync.sh``` paste your modified script and hit ```ctrl+x``` and ```y``` to save.

### Testing the script:
```bash
chmod +x ~/miner_sync.sh
~/miner_sync.sh
```

### Setting Up the Cron Job:
Now we need to set up a cron job to run this every 30 minutes at least. How long is up to you but use [crontab guru](https://crontab.guru/) to figure out the cron syntax to change the interval if you'd like.

Run the following command:
```bash
crontab -e
```
Select your editor of choice, then paste the following as the last line of the script.
```*/30 * * * * ~/miner_sync.sh >> ~/synclog.txt```
Save the file and exit.

Now the script will run every thirty minutes and sync from and to each of your miners.

### Profit?

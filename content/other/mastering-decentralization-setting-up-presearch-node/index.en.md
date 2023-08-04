---
title: "Mastering Decentralization: How to Set Up a Presearch Node"
date: 2023-09-26
toc: true
draft: false
description: "Discover how to create and operate a Presearch Node, contributing to a decentralized search engine while earning rewards."
genre: ["Technology", "Decentralization", "Search Engine", "Blockchain", "Node Setup", "Digital Freedom", "Crypto", "Internet", "Information", "Online Privacy"]
tags: ["Operating a Presearch Node", "Setting Up a Decentralized Search Node", "Earn Rewards with Presearch Node", "How to Create a Node for Presearch", "Decentralized Internet Search", "Decentralization", "Presearch Node", "Search Engine", "Blockchain", "Node Setup", "Digital Freedom", "Crypto", "Internet", "Online Privacy", "Rewards"]
cover: "/img/cover/decentralized-search-node.png"
coverAlt: "A person operating a search node in a decentralized digital world."
coverCaption: "Empower Your Search: Operate a Presearch Node"
---

## Creating a Presearch Node: A Comprehensive Guide

In the world of decentralized search engines, operating a Presearch Node can be a rewarding endeavor. Presearch Nodes play a vital role in processing user search requests and contributing to the decentralized network. This guide will walk you through the steps of setting up and running your own Presearch Node, highlighting the benefits, requirements, and potential challenges.

## Introduction

Presearch is a decentralized search engine that offers an alternative to the dominance of Big Tech companies in the online search landscape. By operating a Presearch Node, you contribute to a more open and decentralized internet while earning Presearch PRE tokens.

______
{{< inarticle-dark >}}
______

## Prerequisites 

To get started with setting up a Presearch Node, you'll need to complete the following prerequisite:

#### Purchase 4,000 PRE tokens

To be eligible for rewards as a Presearch Node operator, you'll need to purchase a minimum of 4,000 PRE tokens. You can acquire these tokens through the following link: [Purchase PRE tokens on KuCoin](https://www.kucoin.com/r/af/QBSSSM2W).

## Getting Started

### 1. Install Docker

To begin, you'll need to install [Docker](https://docs.docker.com/engine/install/ubuntu/) on your computer or virtual server. Docker provides a platform for running applications in isolated containers, which is essential for running a Presearch Node. You can also explore turn-key solutions like [ThreeFold.io](https://threefold.io/) that come with Docker pre-installed.

### 2. Register Your Node

First, create your [Presearch Account](https://presearch.com/signup?rid=3518896), if you haven't already

Visit the [Presearch Node Dashboard](https://nodes.presearch.com/dashboard?rid=3518896) to register your node. Upon registration, you'll receive a unique registration code that will be used in the setup process.

### 3. Setting Up Your Node

Run the following commands in your terminal to set up your Presearch Node. Replace `YOUR_REGISTRATION_CODE_HERE` with the code you obtained in the previous step.

```bash
docker stop presearch-node ; 
docker rm presearch-node ; 
docker stop presearch-auto-updater ; 
docker rm presearch-auto-updater ; 
docker run -d --name presearch-auto-updater --restart=unless-stopped -v /var/run/docker.sock:/var/run/docker.sock presearch/auto-updater --cleanup --interval 900 presearch-auto-updater presearch-node ;
docker pull presearch/node ; 
docker run -dt --name presearch-node --restart=unless-stopped -v presearch-node-storage:/app/node -e REGISTRATION_CODE=YOUR_REGISTRATION_CODE_HERE presearch/node ;
docker logs -f presearch-node
```

## Server Requirements

Presearch Nodes do not require significant disk space, memory, or CPU power. Fast internet and low latency connection to the Presearch Gateway are prioritized for optimal performance. It's recommended to run multiple lightweight nodes to maximize rewards relative to server costs.

## Node Operator Rewards

Node operators who stake at least 4,000 PRE tokens to their node are eligible for rewards. Each staked node qualifies for the base reward, while staking more than **4,000 PRE tokens** opens the door to additional rewards. For detailed information on staking and rewards, visit the [Node Rewards](https://nodes.presearch.com/rewards?rid=3518896) page.

## Potential Risks and Cautions

While running a Presearch Node can be rewarding, there are some considerations to keep in mind:

- **Privacy Concerns**: Running a node locally could associate queries with your IP address. If privacy is a concern, consider running the node on an external server.

- **Repressive Countries**: Operating a node in certain repressive countries may pose risks. Be aware of potential consequences in regions like Iran, North Korea, or China.

- **IP Address Logging**: Your node's IP address is logged for identification within the system.

- **Tax Implications**: Depending on your country, node rewards may need to be reported as income for tax purposes.

- **Software Verification**: The current software is not open source. While the developers assure its integrity, verification options are limited.

- **Beta Software**: The software is in beta, and undiscovered bugs may exist. Updates are frequent, but running the latest version is not guaranteed.

______
{{< inarticle-dark >}}
______

## Conclusion

Operating a Presearch Node is a step toward a more decentralized and open internet. By following the steps outlined in this guide, you can contribute to the Presearch network while potentially earning rewards. Keep in mind the risks and benefits, and make an informed decision based on your goals and circumstances.

For more information and updates, visit the [Presearch Node Documentation](https://nodes.presearch.com/?rid=3518896) and join the Presearch community.

______

**References:**

1. [Presearch Node Dashboard](https://nodes.presearch.com/dashboard?rid=3518896)
2. [ThreeFold.io](https://threefold.io/)
3. [Node Rewards](https://nodes.presearch.com/rewards?rid=3518896)
4. [Presearch Node Documentation](https://nodes.presearch.com/?rid=3518896)

*Disclaimer: This article provides information and guidance related to Presearch Nodes. Readers are advised to conduct further research and consider their own circumstances before proceeding.*

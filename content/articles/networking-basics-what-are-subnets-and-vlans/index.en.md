---
title: "Networking Basics: Subnetting, VLANs, and Efficient Network Management"
draft: false
toc: true
date: 2023-07-23
description: "Learn the essentials of subnets, subnetting, and VLANs for efficient network management and enhanced security"
genre: ["Networking Basics", "Subnetting", "VLANs", "Network Management", "Network Security", "IP Addressing", "Network Segmentation", "Efficient Resource Utilization", "Network Performance", "IPv4"]
tags: ["networking basics", "subnets", "subnetting", "VLANs", "network management", "network security", "IP addressing", "network segmentation", "efficient resource utilization", "network performance", "IPv4", "subnet configuration", "subnet masks", "IP address allocation", "inter-VLAN communication", "switch ports", "VLAN configuration", "VLAN interfaces", "network connectivity", "subnetworks", "broadcast domains", "security measures", "IP address range", "subnet examples", "VLAN deployment", "network administration", "switch configuration", "router configuration", "network scalability", "communication and data transfer", "efficient networks"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_comp.png"
coverAlt: "A symbolic illustration of interconnected computer networks with subnets and VLANs"  
coverCaption: "Building Efficient Networks: Subnets and VLANs Simplified."
---

## Networking Basics | What is a Subnet, How to Subnet, and What is a VLAN

### Introduction

In today's interconnected world, computer networks play a crucial role in facilitating communication and data transfer. Understanding networking basics is essential for both IT professionals and everyday users. In this article, we will explore the concepts of subnets, subnetting, and VLANs, providing a comprehensive overview of their purpose and functionality.

## Subnets: A Deeper Understanding

### What is a Subnet?

{{< youtube id="nR5xCmXJE5E" >}}

A **subnet** is a logical subdivision of an IP network. It allows the network administrator to divide a large network into smaller, more manageable segments. Each subnet has its own unique IP address range, which helps in efficient utilization of available IP addresses.

### Why Use Subnets?

There are several reasons why subnets are used in computer networks:

1. **Network Segmentation:** Subnets enable the division of a large network into smaller subnetworks, improving network performance and reducing congestion.

2. **Improved Security:** By separating devices into different subnets, network administrators can implement security measures, such as firewalls and access control lists, to control traffic flow and enhance network security.

3. **Efficient Resource Utilization:** Subnetting allows for better allocation and utilization of IP addresses, which are a limited resource in the IPv4 addressing scheme.

### How to Subnet?

{{< youtube id="LdSAaSHfK3M" >}}

Subnetting involves dividing a network into smaller subnets. To perform subnetting, the following steps can be followed:

1. **Determine the Network Requirements:** Understand the number of required subnets and the number of hosts per subnet.

2. **Choose an IP Addressing Scheme:** Decide on an appropriate IP addressing scheme, considering factors like the number of subnets and hosts required.

3. **Calculate Subnet Masks:** Determine the subnet masks based on the number of required subnets and hosts per subnet.

4. **Assign IP Addresses:** Allocate IP addresses to each subnet, ensuring they fall within the appropriate subnet range.

5. **Test and Verify:** Validate the subnet configuration by testing network connectivity and verifying IP address assignments.

### Subnetting Examples

Let's consider a simple example to illustrate subnetting:

Suppose we have the IP address range 192.168.0.0/24, and we want to create four subnets with equal numbers of hosts. Here's how we can subnet this network:

1. **Step 1: Determine Network Requirements:** We need four subnets with equal numbers of hosts.

2. **Step 2: Choose an IP Addressing Scheme:** We decide to use a /26 subnet mask, which allows for 64 hosts per subnet.

3. **Step 3: Calculate Subnet Masks:** With a /26 subnet mask, we have a subnet mask of 255.255.255.192.

4. **Step 4: Assign IP Addresses:** We assign the following IP addresses to the subnets:

   - Subnet 1: 192.168.0.0/26
   - Subnet 2: 192.168.0.64/26
   - Subnet 3: 192.168.0.128/26
   - Subnet 4: 192.168.0.192/26

5. **Step 5: Test and Verify:** We validate the subnet configuration by checking network connectivity between devices within each subnet.

### Useful Subnetting Tables

#### Subnet Calculation Reference Table

| Subnet Mask | CIDR Notation | Total IP Addresses | Usable IP Addresses | 
|-------------|---------------|--------------------|---------------------|
| /30         | 255.255.255.252 | 4                  | 2                   |
| /29         | 255.255.255.248 | 8                  | 6                   |
| /28         | 255.255.255.240 | 16                 | 14                  |
| /27         | 255.255.255.224 | 32                 | 30                  |
| /26         | 255.255.255.192 | 64                 | 62                  |
| /25         | 255.255.255.128 | 128                | 126                 |
| /24         | 255.255.255.0   | 256                | 254                 |
| /23         | 255.255.254.0   | 512                | 510                 |
| /22         | 255.255.252.0   | 1,024              | 1,022               |
| /21         | 255.255.248.0   | 2,048              | 2,046               |
| /20         | 255.255.240.0   | 4,096              | 4,094               |
| /19         | 255.255.224.0   | 8,192              | 8,190               |
| /18         | 255.255.192.0   | 16,384             | 16,382              |
| /17         | 255.255.128.0   | 32,768             | 32,766              |
| /16         | 255.255.0.0     | 65,536             | 65,534              |
| /15         | 255.254.0.0     | 131,072            | 131,070             |
| /14         | 255.252.0.0     | 262,144            | 262,142             |
| /13         | 255.248.0.0     | 524,288            | 524,286             |
| /12         | 255.240.0.0     | 1,048,576          | 1,048,574           |
| /11         | 255.224.0.0     | 2,097,152          | 2,097,150           |
| /10         | 255.192.0.0     | 4,194,304          | 4,194,302           |
| /9          | 255.128.0.0     | 8,388,608          | 8,388,606           |
| /8          | 255.0.0.0       | 16,777,216         | 16,777,214          |
| /7          | 254.0.0.0       | 33,554,432         | 33,554,430          |
| /6          | 252.0.0.0       | 67,108,864         | 67,108,862          |
| /5          | 248.0.0.0       | 134,217,728        | 134,217,726         |
| /4          | 240.0.0.0       | 268,435,456        | 268,435,454         |
| /3          | 224.0.0.0       | 536,870,912        | 536,870,910         |
| /2          | 192.0.0.0       | 1,073,741,824      | 1,073,741,822       |
| /1          | 128.0.0.0       | 2,147,483,648      | 2,147,483,646       |
| /0          | 0.0.0.0         | 4,294,967,296      | 4,294,967,294       |

#### Usable Subnets Table

| CIDR Notation | Number of Usable Subnets |
|---------------|-------------------------|
| /0            | 1                       |
| /1            | 2                       |
| /2            | 4                       |
| /3            | 8                       |
| /4            | 16                      |
| /5            | 32                      |
| /6            | 64                      |
| /7            | 128                     |
| /8            | 256                     |
| /9            | 512                     |
| /10           | 1024                    |
| /11           | 2048                    |
| /12           | 4096                    |
| /13           | 8192                    |
| /14           | 16384                   |
| /15           | 32768                   |
| /16           | 65536                   |
| /17           | 131072                  |
| /18           | 262144                  |
| /19           | 524288                  |
| /20           | 1048576                 |
| /21           | 2097152                 |
| /22           | 4194304                 |
| /23           | 8388608                 |
| /24           | 16777216                |
| /25           | 33554432                |
| /26           | 67108864                |
| /27           | 134217728               |
| /28           | 268435456               |
| /29           | 536870912               |
| /30           | 1073741824              |
| /31           | 2147483648              |
| /32           | 4294967296              |

#### Powers of Two Table

| Power of Two | Value |
|--------------|-------|
| 2^32         | 4294967296  |
| 2^31         | 2147483648  |
| 2^30         | 1073741824  |
| 2^29         | 536870912   |
| 2^28         | 268435456   |
| 2^27         | 134217728   |
| 2^26         | 67108864    |
| 2^25         | 33554432    |
| 2^24         | 16777216    |
| 2^23         | 8388608     |
| 2^22         | 4194304     |
| 2^21         | 2097152     |
| 2^20         | 1048576     |
| 2^19         | 524288      |
| 2^18         | 262144      |
| 2^17         | 131072      |
| 2^16         | 65536       |
| 2^15         | 32768       |
| 2^14         | 16384       |
| 2^13         | 8192        |
| 2^12         | 4096        |
| 2^11         | 2048        |
| 2^10         | 1024        |
| 2^9          | 512         |
| 2^8          | 256         |
| 2^7          | 128         |
| 2^6          | 64          |
| 2^5          | 32          |
| 2^4          | 16          |
| 2^3          | 8           |
| 2^2          | 4           |
| 2^1          | 2           |
| 2^0          | 1           |

## VLANs: Virtual Local Area Networks

### What is a VLAN?

{{< youtube id="jC6MJTh9fRE" >}}

A **VLAN (Virtual Local Area Network)** is a logical grouping of devices within a network, regardless of their physical location. VLANs provide enhanced network flexibility, security, and scalability by enabling the creation of separate broadcast domains.

### Why Use VLANs?

VLANs offer numerous benefits in network management:

1. **Improved Security:** VLANs can be used to isolate sensitive data and restrict unauthorized access. By separating devices into different VLANs, traffic can be contained within specific segments, preventing unauthorized users from accessing critical resources.

2. **Enhanced Performance:** VLANs allow for the logical separation of network traffic, reducing congestion and improving overall network performance. Broadcast traffic is limited to the VLAN, minimizing unnecessary network noise.

3. **Simplified Network Management:** VLANs provide a way to group devices based on function, department, or any other logical criteria, simplifying network administration and configuration.

### VLAN Configuration

To configure a VLAN, the following steps are generally followed:

1. **Identify VLAN Requirements:** Determine the purpose and scope of the VLAN deployment. Identify the devices and their placement within VLANs.

2. **Assign VLAN IDs:** Assign unique VLAN IDs to each VLAN. VLAN IDs are usually numbers between 1 and 4094, with certain reserved IDs.

3. **Configure Switch Ports:** Assign the switch ports to the appropriate VLANs. This can be done by configuring the switch port as an access port or a trunk port.

4. **Configure VLAN Interfaces:** If inter-VLAN communication is required, [configure VLAN](https://simeononsecurity.ch/network-plus/ethernet-switching-vlans-port-configurations-security/) interfaces, such as VLAN interfaces on a layer 3 switch or router.

5. **Test and Verify:** Validate the VLAN configuration by testing network connectivity between devices within each VLAN.

### Reserved VLAN Table
| Claimed VLAN Tags | Description                                        |
|-------------------|----------------------------------------------------|
| VLAN 0            | Reserved VLAN ID and should not be used             |
| VLAN 1            | Default VLAN for many network devices               |
| VLAN 2            | Default VLAN for management traffic                 |
| VLAN 3-4          | Reserved VLAN IDs                                  |
| VLAN 5            | Reserved for Token Ring VLAN ID                     |
| VLAN 6-1001       | Reserved VLAN IDs                                  |
| VLAN 1002-1005    | Default VLANs used by Cisco for specific purposes  |
| VLAN 1006-1024    | Reserved VLAN IDs                                  |
| VLAN 1025-4094    | Reserved for extended range VLANs                   |
| VLAN 4095         | Reserved VLAN ID and should not be used             |

## Conclusion

[Understanding subnets](https://simeononsecurity.ch/articles/networking-basics-what-is-a-switch-router-gateway-subnet-firewall-and-dmz/) and VLANs is crucial for designing and managing efficient computer networks. Subnets allow for network segmentation, improving performance and security. VLANs provide logical grouping of devices, enhancing network flexibility and management. By following the steps outlined in this article, network administrators can effectively subnet their networks and configure VLANs to meet specific requirements.

Remember, networking basics are the foundation for building robust and scalable networks that cater to the needs of modern-day communication and data transfer.

## References

- [Subnetting Basics](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
- [Understanding and Configuring VLANs
](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/12-2/25ew/configuration/guide/conf/vlans.pdf)
- [IEEE 802.1Q Standard](https://standards.ieee.org/standard/802_1Q-2018.html)


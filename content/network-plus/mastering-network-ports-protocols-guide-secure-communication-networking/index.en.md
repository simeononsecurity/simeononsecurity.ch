---
title: "CompTIA Network+ N10-009: Ports and Protocols"
date: 2023-07-03
lastmod: 2026-10-10
toc: true
draft: false
description: "Learn Network Skills for CompTIA Network+ N10-009 through service identification, packet capture, a controlled fault, saved evidence, and recovery proof."
genre: ["CompTIA Network+", "N10-009", "Networking", "Certification Course"]
tags: ["CompTIA Network+", "N10-009", "Ports and Protocols", "network lab", "network troubleshooting", "exam prep"]
cover: "/img/cover/An_animated_illustration_showcasing_interconnted.webp"
coverAlt: "An animated illustration showcasing interconnected devices exchanging secure data over a network."
coverCaption: "Secure communication and efficient networking for enhanced productivity."
---

[Click Here to Return To the Network Plus Course Page](/network-plus-start)

## Introduction

In the world of computer networks, ports, protocols, and network services play a crucial role in enabling communication between devices. Understanding these concepts is essential for network administrators, IT professionals, and anyone interested in the workings of computer networks. This article will explain common ports and protocols, their applications, and introduce encrypted alternatives for secure communication. We will also delve into IP protocol types and explore the difference between connection-oriented and [connectionless protocols](https://simeononsecurity.com/articles/difference-connection-oriented-connectionless-communication/).

## Explaining Common Ports and Protocols

{{< youtube id="fgC8hk4IfDk" >}}

| Protocol                                       | Port   | Secure Protocol          | Secure Port | Description                                              |
|------------------------------------------------|--------|--------------------------|-------------|----------------------------------------------------------|
| File Transfer Protocol (FTP)                    | 20/21  | SFTP over SSH          | 22          | FTP transfers files. SFTP is a separate SSH protocol.     |
| Telnet                                         | 23     | Secure Shell (SSH)        | 22          | Provides secure remote login and command execution.       |
| Simple Mail Transfer Protocol (SMTP)            | 25     | -                        | -           | Used for sending email messages between servers.          |
| Domain Name System (DNS)                        | 53     | -                        | -           | Translates domain names into IP addresses.                |
| Dynamic Host Configuration Protocol (DHCP)      | 67/68  | -                        | -           | Assigns IP addresses to devices on a network.             |
| Trivial File Transfer Protocol (TFTP)           | 69     | -                        | -           | Used for simple file transfers without security.          |
| Hypertext Transfer Protocol (HTTP)              | 80     | Hypertext Transfer Protocol Secure (HTTPS) | 443 | HTTPS protects web traffic with TLS.                    |
| Post Office Protocol v3 (POP3)                  | 110    | -                        | -           | Retrieves email messages from a mail server.              |
| Network Time Protocol (NTP)                     | 123    | -                        | -           | Synchronizes timekeeping among network devices.           |
| Internet Message Access Protocol (IMAP)         | 143    | IMAP over SSL             | 993         | Retrieves email messages from a mail server securely.     |
| Simple Network Management Protocol (SNMP)       | 161/162| -                        | -           | Manages network devices and monitors performance.         |
| Lightweight Directory Access Protocol (LDAP)    | 389    | Lightweight Directory Access Protocol (over SSL) (LDAPS) | 636 | Accesses and maintains directory information securely. |
| Server Message Block (SMB)                      | 445    | -                        | -           | Provides shared access to files, printers, and more.      |
| Syslog                                         | 514    | -                        | -           | Collects and forwards log messages in a network.          |
| Message submission (SMTP)                      | 587    | STARTTLS when configured | 587       | Clients submit mail. TLS depends on server policy.        |
| Structured Query Language (SQL) Server          | 1433   | -                        | -           | Database management system for SQL.                       |
| SQLnet                                         | 1521   | -                        | -           | Oracle database listener for client connections.          |
| MySQL                                          | 3306   | -                        | -           | Database management system for MySQL.                     |
| Remote Desktop Protocol (RDP)                   | 3389   | -                        | -           | Provides remote desktop access to a computer.             |
| Session Initiation Protocol (SIP)               | 5060/5061 | -                     | -           | Establishes and terminates multimedia sessions.           |

SFTP uses SSH on port 22. It is not FTP with TLS. **FTPS** is FTP protected by TLS. Explicit FTPS typically starts on port 21, while implicit FTPS commonly uses port 990. Port 587 is for mail submission. A client and server commonly upgrade the connection with STARTTLS, but the port number alone does not prove encryption. See [RFC 4217](https://www.rfc-editor.org/rfc/rfc4217) and [RFC 6409](https://www.rfc-editor.org/rfc/rfc6409).

______

## IP Protocol Types

{{< youtube id="NAI-gE51VXg" >}}


The Internet Protocol (IP) suite consists of various protocol types that play crucial roles in the functioning of computer networks. Understanding these protocols is essential for network administrators and IT professionals. Let's delve into some important IP protocol types:

### Internet Control Message Protocol (ICMP)

**Internet Control Message Protocol (ICMP)** is an integral part of the IP suite. It is used for diagnostic and error reporting purposes in network communication. ICMP enables network devices to communicate information about network conditions, such as unreachable hosts or network congestion. It helps in troubleshooting network issues and ensuring efficient network operation.

### TCP - Connection-Oriented Protocol

**Transmission Control Protocol (TCP)** is a connection-oriented protocol that provides reliable, ordered, and error-checked delivery of data packets. It establishes a connection between the sending and receiving hosts before transmitting data, ensuring data integrity and delivery.

### UDP - Connectionless Protocol

**User Datagram Protocol (UDP)** is a connectionless protocol that allows the transmission of data packets without establishing a dedicated connection. It is often used for real-time applications, such as voice and video streaming, where speed and low latency are prioritized over reliability.

### Generic Routing Encapsulation (GRE)

**Generic Routing Encapsulation (GRE)** is a protocol used to encapsulate various network layer protocols inside IP packets. It provides a mechanism for creating private networks over a public network infrastructure. GRE is commonly used in virtual private networks (VPNs) and allows the transmission of diverse protocols across a network.

### Internet Protocol Security (IPSec)

**Internet Protocol Security (IPSec)** is a protocol suite used to secure IP communication by authenticating and encrypting IP packets. IPSec provides a framework for secure communication over IP networks, ensuring the confidentiality, integrity, and authenticity of data transmitted between network devices.

### Authentication Header (AH) / Encapsulating Security Payload (ESP)

**Authentication Header (AH)** and **Encapsulating Security Payload (ESP)** are two protocols used in IPSec to provide different security services. AH provides data integrity and authentication, ensuring that the received data has not been tampered with. ESP, on the other hand, provides confidentiality, integrity, and authentication by encrypting the IP packet payload.

### Connectionless vs. Connection-Oriented Protocols

Connectionless and connection-oriented protocols differ in their approach to data transmission. 

Connectionless protocols, such as UDP, do not establish a dedicated connection before transmitting data. Each packet is treated independently and can take different routes to reach the destination. Connectionless protocols are faster but offer no guarantee of delivery or sequencing.

Connection-oriented protocols, like TCP, establish a connection before data transmission. The connection is maintained until all data is successfully delivered. Connection-oriented protocols ensure reliable delivery of data by implementing error-checking mechanisms and retransmission of lost packets.

Understanding the differences between connectionless and connection-oriented protocols is essential for designing and optimizing network applications based on specific requirements.

______

## Conclusion

Ports, protocols, and network services are fundamental elements of computer networks. They enable communication, facilitate secure data transmission, and ensure the smooth operation of various network applications. By understanding common ports and protocols, their applications, and encrypted alternatives, individuals can enhance network security and make informed decisions regarding network configuration and administration. Additionally, having knowledge of IP protocol types allows for better network troubleshooting and optimization.


## Progressive Lab Checkpoint 04: Ports and Protocols

This checkpoint extends the [shared course topology](/network-plus-start/#progressive-n10-009-lab). Work inside an isolated simulator copy. Save `04-before` before changing state.

**Build and verify:** Create one topic-specific diagram, configuration, capture, log, ticket, or test record covering service identification, packet capture, firewall rules, SFTP, FTPS, SMTP submission, DoT, DoH, DNSSEC, SNMPv3, syslog TLS, and SIP TLS. Tie every choice to R1, R2, SW1, SW2, AP1, SRV1, or an endpoint in the shared topology. Record expected and observed results.

### Fault injection and recovery

Block DNS while leaving HTTPS open. Record failed lookup and successful direct-address access, then remove the rule.

### Deliverable and pass gate

Submit **`04-mastering-network-ports-protocols-guide-secure-communication-networking.md`** with purpose, affected nodes, risk, rollback, before evidence, fault evidence, recovery evidence, and cleanup statement.

**Pass:** The artifact covers each named topic, supports the diagnosis with evidence, restores required service, and proves cleanup.

[Previous checkpoint](/network-plus/cables-connectors-ip-addressing-guide/) | [Next checkpoint](/network-plus/network-services-connectivity-options-architecture/)

### Reproducible route and filled sample

Turn on DNS and HTTP under **SRV1 > Services**. Add `app.lab.example -> 10.10.30.10`. From PC-A run `nslookup app.lab.example` and open `http://app.lab.example`. Expected DNS address is `10.10.30.10` and HTTP status is successful. Packet Tracer does not prove TLS, SFTP, FTPS, DoT, DoH, DNSSEC, syslog TLS, or SIP TLS. For those rows, use the RFC-backed service matrix and label the result `design evidence`.

### Primary reference

- [CompTIA Network+ N10-009 exam objectives](https://comptiacdn.azureedge.net/webcontent/docs/default-source/exam-objectives/comptia-network-n10-009-exam-objectives-%284-0%29-%281%29.pdf?sfvrsn=f31cc6c4_4)

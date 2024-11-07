# 🕸️ Network Packets with Scapy

**Author**: Lithiokride (Lithi0)

**Repository**: [Network-Packets-with-Scapy](https://github.com/Lithi0/Network-Packets-with-Scapy)

This project is a comprehensive toolkit of network packet examples, written in Python and leveraging the power of **Scapy**. Each script simulates or manipulates different types of network traffic and protocols, providing a hands-on resource for learning and experimenting with network communication techniques. Please use this repository responsibly, as it is meant for educational and research purposes only. ![Cat Wink Emoji](https://cdn3.emoji.gg/emojis/9724_cat_wink.png)


---

## 🌐 Project Overview

Each file within this repository serves as a standalone script that performs a specific network task, from **flooding attacks** and **spoofing** to **protocol emulation** and **custom packet crafting**. Below is a list of each script included, with a brief description of its functionality.

### 📑 Table of Contents
1. [Flooding Scripts](#flooding-scripts)
2. [Spoofing & Manipulation Scripts](#spoofing--manipulation-scripts)
3. [Protocol Emulation](#protocol-emulation)
4. [Network Discovery & Utility](#network-discovery--utility)
5. [Injection & Exploitation](#injection--exploitation)

---

### Flooding Scripts

These scripts are designed to send a large volume of packets to a target, overwhelming the service and potentially causing disruptions.

- **`ACK_Flood(randsrc).py`**: Generates a flood of TCP ACK packets with randomized source addresses to bypass IP-based filtering.
- **`HTTP_Flood.py`**: Initiates an HTTP request flood, targeting web servers and potentially causing a denial of service.
- **`SCTP_INIT_Flood.py`**: Floods SCTP INIT packets, which can strain SCTP-based services.
- **`TCP_Flood(randsrc).py`**: Generates a large number of TCP packets to overload a target.
- **`UDP_Flood.py`**: Sends a flood of UDP packets, useful for disrupting UDP-based services.

### Spoofing & Manipulation Scripts

These scripts modify packet headers and emulate packet responses to deceive network devices or alter the network behavior.

- **`Arp_Reply.py`**: Sends ARP reply packets, allowing for ARP spoofing to intercept or manipulate LAN traffic.
- **`DNSspoofing.py`**: Performs DNS spoofing, redirecting traffic meant for one domain to a different IP address.
- **`ICMP_Redirect.py`**: Sends ICMP redirect packets, modifying routing paths.
- **`IPv6_Router_Solicitation.py`**: Spoofs IPv6 router advertisements, influencing devices to change their default route.
- **`Rouge_DHCP_Offer.py`**: Mimics a DHCP server to send unauthorized IP leases, potentially intercepting traffic.

### Protocol Emulation

These scripts demonstrate packet crafting techniques to emulate various protocols, useful for learning protocol behavior and crafting test traffic.

- **`BGP_Update.py`**: Simulates BGP update messages, showcasing how route announcements work.
- **`RADIUS.py`**: Crafts RADIUS packets, useful for testing network access control configurations.
- **`SIP_INVITE.py`**: Emulates a SIP INVITE message, often used in VoIP communication.
- **`Telnet_Login_Attempt.py`**: Mimics a Telnet login attempt, useful for testing Telnet server security.
- **`TFTP_Read_Req.py`**: Creates a TFTP read request, which is a common protocol for file transfers in embedded systems.

### Network Discovery & Utility

Scripts in this section include various network reconnaissance techniques and general packet utilities.

- **`Arp_Req.py`**: Sends ARP requests to gather MAC addresses of devices on the network.
- **`NetBIOS_Name_Service.py`**: Explores NetBIOS network services to identify hostnames on a network.
- **`Wireless_Probe_Req.py`**: Broadcasts wireless probe requests to discover nearby Wi-Fi networks.

### Injection & Exploitation

These scripts include basic examples of network injections and simple exploitations for educational purposes.

- **`MSSQL_Injection.py`**: Demonstrates a basic MSSQL injection, showing how vulnerable SQL queries can be exploited.
- **`Malicious_SMB.py`**: Sends malicious SMB packets, potentially useful for exploring vulnerabilities in SMB implementations.
- **`TCP_Reset.py`**: Sends TCP reset packets, forcefully terminating TCP connections.
- **`Malformed_Packet.py`**: Generates malformed packets to test how devices handle unexpected or incorrectly structured packets.

---

### ⚠️ **Disclaimer**

All scripts are intended for **educational and research purposes only**. Misuse of these scripts, including unauthorized testing on networks, is illegal and against ethical hacking standards. By using this repository, you agree to take full responsibility for your actions. ![Cat Wink Emoji](https://cdn3.emoji.gg/emojis/9724_cat_wink.png)


---

**Enjoy exploring the depths of network protocols with Scapy! Happy learning, and stay ethical!**


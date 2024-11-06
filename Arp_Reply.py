from scapy.all import ARP, Ether, send
# Written by Lithiokride

# Parameters
target_ip = "192.168.1.1"  # IP address being replied to
target_mac = "00:aa:bb:cc:dd:ee"  # MAC address of the requester
source_ip = "192.168.1.100"  # Your IP address
source_mac = "00:11:22:33:44:55"  # Your MAC address

# Create the ARP reply
arp_reply = ARP(op=2,  # 2 for ARP reply
                hwsrc=source_mac,
                psrc=source_ip,
                hwdst=target_mac,
                pdst=target_ip)

# Create the Ethernet frame
ether = Ether(src=source_mac, dst=target_mac)

# Combine Ethernet and ARP
packet = ether / arp_reply

# Send the packet
send(packet, verbose=0)

print(f"Sent ARP Reply for {target_ip}")

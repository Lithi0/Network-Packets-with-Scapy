from scapy.all import ARP, Ether, send
# Written by Lithiokride

# Parameters
target_ip = "192.168.1.1"  # IP address to query
source_ip = "192.168.1.100"  # Your IP address
source_mac = "00:11:22:33:44:55"  # Your MAC address

# Create the ARP request
arp_request = ARP(op=1,  # 1 for ARP request
                  psrc=source_ip,
                  pdst=target_ip)

# Create the Ethernet frame
ether = Ether(src=source_mac, dst="ff:ff:ff:ff:ff:ff")  # Broadcast

# Combine Ethernet and ARP
packet = ether / arp_request

# Send the packet
send(packet, verbose=0)

print(f"Sent ARP Request for {target_ip}")

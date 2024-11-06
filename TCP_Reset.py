from scapy.all import IP, TCP, send
# Written by Lithiokride

# Parameters
target_ip = "192.168.1.1"  # Target IP address
target_port = 80            # Target port (e.g., HTTP port)
source_port = 12345         # Source port (arbitrary)

# Create the IP layer
ip = IP(dst=target_ip)

# Create the TCP layer for the RST packet
tcp = TCP(sport=source_port, dport=target_port, flags='R')  # RST flag

# Construct the packet
reset_packet = ip / tcp

# Send the TCP Reset packet
send(reset_packet)

print("TCP Reset packet sent.")

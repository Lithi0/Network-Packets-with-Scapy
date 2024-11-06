from scapy.all import *
# Written by Lithiokride

def gre_packet(target_ip, inner_payload, key=None):
    # Define the GRE header
    gre = GRE(flags=0, proto=0x0800)  # Protocol type for IP

    # If a key is specified, include it
    if key:
        gre.key = key

    # Create the IP header
    ip = IP(dst=target_ip, src=RandIP())

    # Create the complete packet with the inner payload
    packet = ip / gre / inner_payload

    return packet

# Example usage
target_ip = "192.168.1.100"  # Replace with the target IP
inner_payload = IP(dst="192.168.2.1") / ICMP()  # Replace with your inner payload

# Craft the GRE packet
packet = gre_packet(target_ip, inner_payload)

# Send the packet
send(packet, verbose=True)

print(f"Sent GRE packet to {target_ip}")

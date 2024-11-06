from scapy.all import *
# Written by Lithiokride

# Define target IP and port
target_ip = "192.168.1.10"  # Replace with the target IP
target_port = 12345          # Replace with the target port

# Create the UDP packet
packet = IP(dst=target_ip) / UDP(dport=target_port) / Raw(load="Hello, World!")

# Send the packet
send(packet)

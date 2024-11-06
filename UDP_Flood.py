from scapy.all import IP, UDP, send
import time
# Written by Lithiokride

# Parameters
target_ip = "192.168.1.1"  # Target IP address
source_port = 12345         # Source UDP port
destination_port = 80       # Destination UDP port
packet_count = 1000         # Number of packets to send

# Create the IP layer
ip_packet = IP(dst=target_ip)

# Create the UDP layer
udp_packet = UDP(sport=source_port, dport=destination_port)

# Combine IP and UDP layers
packet = ip_packet / udp_packet

def send_packets():
    try:
        # Send packets in a loop with a counter
        for count in range(1, packet_count + 1):
            send(packet, verbose=0)
            time.sleep(0.01)  # Adjust delay as needed
            
            # Print packet count every 100 packets
            if count % 100 == 0:
                print(f"Packets sent: {count}")

    except KeyboardInterrupt:
        print(f"\nStopped. Total packets sent: {count}")

    print(f"Sent {packet_count} UDP packets to {target_ip}:{destination_port}")

# Start sending packets
send_packets()

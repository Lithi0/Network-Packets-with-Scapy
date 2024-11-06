from scapy.all import IP, TCP, send
# Written by Lithiokride

# Parameters
target_ip = "192.168.1.1"  # Target IP address
target_port = 80            # HTTP port (default 80)

# Create the IP layer
ip = IP(dst=target_ip)

# Create the TCP layer for the GET request
tcp = TCP(sport=12345, dport=target_port, flags='S')  # SYN flag

# Send SYN to establish connection
syn_packet = ip / tcp
send(syn_packet)

# Create the HTTP GET request
http_get = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nConnection: close\r\n\r\n"

# Update TCP layer for the actual GET request
tcp = TCP(sport=12345, dport=target_port, flags='A', seq=1, ack=1)

# Send the HTTP GET request
get_packet = ip / tcp / http_get
send(get_packet)

print("HTTP GET request sent.")

from scapy.all import IP, TCP, send
# Written by Lithiokride

# Parameters
target_ip = "192.168.1.1"  # Target IP address
target_port = 80            # HTTP port (default 80)

# Create the IP layer
ip = IP(dst=target_ip)

# Create the TCP layer for the POST request
tcp = TCP(sport=12345, dport=target_port, flags='S')  # SYN flag

# Send SYN to establish connection
syn_packet = ip / tcp
send(syn_packet)

# Create the HTTP POST request
http_post = f"POST /submit HTTP/1.1\r\nHost: {target_ip}\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 27\r\nConnection: close\r\n\r\nname=example&value=test"

# Update TCP layer for the actual POST request
tcp = TCP(sport=12345, dport=target_port, flags='A', seq=1, ack=1)

# Send the HTTP POST request
post_packet = ip / tcp / http_post
send(post_packet)

print("HTTP POST request sent.")

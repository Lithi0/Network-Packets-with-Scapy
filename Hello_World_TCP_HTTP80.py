from scapy.all import *
# Written by Lithiokride

# Define target IP and port
target_ip = "192.168.1.10"  # Replace with the target IP
target_port = 80             # Use port 80

# Create an HTTP response with "Hello, World!" message
http_response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/plain\r\n"
    "Content-Length: {}\r\n".format(len("Hello, World!")) +
    "\r\n" + 
    "Hello, World!"
)

# Create the TCP packet with the HTTP response
packet = IP(dst=target_ip) / TCP(dport=target_port, sport=RandShort(), flags='PA') / Raw(load=http_response)

# Send the packet
send(packet)

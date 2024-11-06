from scapy.all import sendp, Ether, IP, UDP, Raw
# Written by Lithiokride

# Define the parameters for the RADIUS packet
radius_server_ip = "192.0.2.1"  # The IP address of the RADIUS server
client_ip = "192.0.2.2"          # The IP address of the client sending the request
secret_key = b"mysecret"         # The shared secret key for RADIUS authentication
radius_id = 1                     # Identifier for the RADIUS packet

# Function to create a RADIUS Access-Request packet
def create_radius_request():
    # RADIUS packet structure
    code = 1              # Code for Access-Request
    length = None         # Length will be calculated later

    # Create the RADIUS attributes (here we use a simple Username attribute)
    username = b'username'  # Example username
    username_attr = bytes([0x01, len(username)]) + username  # Type 1 for Username, followed by its length and value

    # Combine to form the RADIUS packet
    radius_packet = (
        bytes([code]) +              # Code
        bytes([radius_id]) +         # Identifier
        b'\x00\x00' +                # Length placeholder (will set later)
        bytes(secret_key) +          # Shared secret key
        username_attr                 # Username attribute
    )

    # Calculate the total length of the RADIUS packet
    length = len(radius_packet)
    radius_packet = radius_packet[:2] + pack('!H', length) + radius_packet[4:]  # Set the length in the packet

    return radius_packet

# Create the RADIUS Access-Request packet
radius_request_packet = create_radius_request()

# Create the Ethernet layer (for local networks)
ether = Ether(src="00:11:22:33:44:55", dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address

# Create the IP layer
ip = IP(src=client_ip, dst=radius_server_ip)

# Create the UDP layer (RADIUS uses UDP port 1812)
udp = UDP(sport=12345, dport=1812)  # Random source port and destination port 1812

# Combine Ethernet, IP, UDP, and RADIUS to form the complete packet
packet = ether / ip / udp / Raw(load=radius_request_packet)

# Send the packet
sendp(packet, verbose=0)

print(f"Sent RADIUS Access-Request to {radius_server_ip}")  # Inform the user that the packet was sent

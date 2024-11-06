from scapy.all import IP, TCP, send
from struct import pack
# Written by Lithiokride

# Define the IP addresses and Autonomous System (AS) number
bgp_router_ip = "192.0.2.1"  # The IP address of the BGP router sending the update
bgp_peer_ip = "192.0.2.2"     # The IP address of the BGP peer receiving the update
bgp_as = 65001                 # The Autonomous System Number for this router

# Function to create a BGP Update message
def create_bgp_update():
    # Create the BGP Header
    marker = b'\xff' * 16  # A special marker that is always 16 bytes of 'ff'
    type_ = 2              # Type '2' indicates this is an Update message

    # Withdrawn Routes Length (0 means no routes are being withdrawn)
    withdrawn_length = 0
    withdrawn_routes = b''  # No routes to withdraw

    # Path Attributes: This is where we tell the peer about the next hop and AS path
    path_attributes = b''
    
    # Next Hop attribute (the next router to send packets to)
    next_hop = b'\xC0\xA8\x02\x01'  # This is 192.0.2.1 in hexadecimal
    path_attributes += b'\x40' + b'\x02' + b'\x04' + next_hop  # Add the Next Hop attribute

    # AS_PATH attribute (list of AS numbers this route has passed through)
    as_path = pack('!H', bgp_as)  # Create a byte representation of the AS number
    path_attributes += b'\x40' + b'\x02' + bytes([len(as_path)]) + as_path  # Add the AS_PATH attribute

    # NLRI (Network Layer Reachability Information): This is the prefix we are advertising
    nlri_prefix = b'\xCB\x00\x71\x00'  # This represents the IP prefix 203.0.113.0 in bytes
    nlri_length = len(nlri_prefix) + 1  # Length of the NLRI prefix

    # Combine everything to create the full BGP Update message
    bgp_update = (
        marker +                               # Marker
        b'\x00\x00' +                         # Withdrawn Routes Length (0)
        bytes([len(path_attributes)]) +       # Total Path Attribute Length
        path_attributes +                      # Path Attributes
        bytes([24]) +                         # Prefix length (24 bits for /24)
        nlri_prefix                            # NLRI (the prefix being advertised)
    )

    # Calculate the total length of the BGP Update message
    length = len(bgp_update)
    bgp_update = bgp_update[:16] + pack('!H', length) + bgp_update[18:]  # Set the length in the header

    return bgp_update

# Create the BGP Update packet
bgp_update_packet = create_bgp_update()

# Create the IP layer (this defines the source and destination IP addresses)
ip = IP(src=bgp_router_ip, dst=bgp_peer_ip)

# Create the TCP layer (BGP runs over TCP, using port 179)
tcp = TCP(sport=179, dport=179, flags='PA', seq=0, ack=0)

# Combine the IP, TCP, and BGP Update to form the complete packet
packet = ip / tcp / bgp_update_packet

# Send the packet to the BGP peer
send(packet, verbose=0)

print(f"Sent BGP Update to {bgp_peer_ip}")  # Inform the user that the packet was sent

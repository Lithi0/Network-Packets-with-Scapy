from scapy.all import *
# Written by Lithiokride

# Function to create and send a NetBIOS Name Service packet
def send_nbns_query():
    # Define the NetBIOS Name Service query
    nbns_packet = (
        IP(dst='255.255.255.255') /  # Broadcast address
        UDP(sport=137, dport=137) /  # NetBIOS Name Service port
        Raw(load=b'\x00\x00\x00\x00' +  # Transaction ID (4 bytes)
             b'\x00\x00\x00\x00' +  # Flags (0 for a query)
             b'\x00\x01' +          # Questions (1)
             b'\x00\x00' +          # Answers (0)
             b'\x00\x00' +          # Authority records (0)
             b'\x00\x00' +          # Additional records (0)
             b'YourHostName' +      # Name (replace with the target hostname)
             b'\x00' +              # Name termination
             b'\x20\x00' +          # Type (0x20 for unique name)
             b'\x01\x00' +          # Class (1 for Internet)
             b'\x00\x00\x00\x00' +  # TTL (0)
             b'\x00\x00'            # Length (0)
        )
    )
    
    # Send the packet
    send(nbns_packet, iface="eth0")  # Replace "eth0" with your network interface

    print("NetBIOS Name Service query packet sent.")

# Send the NBNS query
send_nbns_query()

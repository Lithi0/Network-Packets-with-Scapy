from scapy.all import Ether, IP, TCP, Raw, sendp
# Written by Lithiokride

# Parameters
target_ip = "192.168.1.10"  # Target IP address
source_ip = "192.168.1.5"    # Source IP address
target_port = 445             # SMB port

# Create Ethernet layer
eth = Ether()

# Create IP layer
ip = IP(src=source_ip, dst=target_ip)

# Create TCP layer
tcp = TCP(sport=12345, dport=target_port, flags='S', seq=1000)

# Create SMB packet (malicious payload)
# Here we could craft a payload that exploits a vulnerability
smb_payload = b'\x00\x00\x00\x00'  # Placeholder for SMB payload

# Combine the layers into a single packet
malicious_smb_packet = eth / ip / tcp / Raw(load=smb_payload)

# Send the malicious SMB packet
sendp(malicious_smb_packet)

print("Malicious SMB packet sent.")

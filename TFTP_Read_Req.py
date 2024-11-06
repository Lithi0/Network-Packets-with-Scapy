from scapy.all import *
# Written by Lithiokride

# Parameters
target_ip = "192.168.1.10"  # Target TFTP server IP
local_port = 69              # Standard TFTP port
filename = "example.txt"     # File to request
mode = "octet"               # Transfer mode (binary)

# Construct the TFTP Read Request packet
# TFTP Opcode for RRQ is 1
tftp_rrq = (
    UDP(sport=12345, dport=local_port) /  # Source port (random) / Destination port (TFTP)
    Raw(load=f"\x00\x01{filename}\x00{mode}\x00")  # Opcode (RRQ) + filename + mode
)

# Send the TFTP Read Request packet
send(tftp_rrq, iface="eth0")  # Replace "eth0" with your network interface

print("TFTP Read Request packet sent.")

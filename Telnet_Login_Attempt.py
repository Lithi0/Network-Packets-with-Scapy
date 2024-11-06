from scapy.all import *
# Written by Lithiokride

def send_telnet_login():
    # Define the target IP and port for Telnet
    target_ip = "192.168.1.100"  # Replace with the target IP
    target_port = 23  # Default Telnet port

    # Craft the Telnet login payload (username and password)
    username = "admin"  # Replace with the actual username
    password = "password123"  # Replace with the actual password

    # Construct the Telnet login packet
    payload = f"{username}\n{password}\n"

    # Craft the packet
    packet = (
        IP(dst=target_ip) /
        TCP(sport=12345, dport=target_port, flags="S") /  # SYN flag for initial connection
        Raw(load=payload)
    )

    # Send the SYN packet to initiate the connection
    send(packet)

    print("Telnet login attempt packet sent.")

# Send the Telnet login packet
send_telnet_login()

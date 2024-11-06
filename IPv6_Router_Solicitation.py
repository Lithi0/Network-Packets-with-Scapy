from scapy.all import *
# Written by Lithiokride

# Function to create and send IPv6 Router Solicitation packet
def send_router_solicitation():
    # Define the IPv6 Router Solicitation packet
    rs_packet = (
        IPv6(dst='ff02::1', src='::1') /  # Destination multicast address for all routers
        ICMPv6MLQuery()  # ICMPv6 Router Solicitation message
    )
    
    # Send the packet
    send(rs_packet, iface="eth0")  # Replace "eth0" with your network interface

    print("IPv6 Router Solicitation packet sent.")

# Send the Router Solicitation
send_router_solicitation()

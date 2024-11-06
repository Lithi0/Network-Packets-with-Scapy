from scapy.all import *
# Written by Lithiokride

def send_probe_request(ssid):
    # Define the interface to send the packet (e.g., wlan0)
    interface = "wlan0"  # Replace with your wireless interface

    # Craft the Probe Request packet
    probe_request = (
        RadioTap() /
        Dot11(addr1='ff:ff:ff:ff:ff:ff',  # Broadcast MAC address
              addr2='00:11:22:33:44:55',  # Source MAC (your device's MAC)
              addr3='00:11:22:33:44:55',  # BSSID (optional, can be your MAC)
              subtype=0) /  # Probe Request subtype
        Dot11ProbeReq() /
        Dot11Elt(ID='SSID', info=ssid)  # Include the SSID to probe for
    )

    # Send the Probe Request
    sendp(probe_request, iface=interface, count=1)

    print(f"Probe Request sent for SSID: {ssid}")

# Example usage
send_probe_request("MySSID")  # Replace "MySSID" with the target SSID

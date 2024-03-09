import socket
def start_dns_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('127.0.0.1', 55)

    while True:
        hostname = input("Enter hostname to resolve (or type 'exit' to quit): ").strip()
        if hostname.lower() == 'exit':
            break

        client_socket.sendto(hostname.encode(), server_address)
        response, _ = client_socket.recvfrom(1024)
        print("Response from DNS server:", response.decode())

        choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    start_dns_client()

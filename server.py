import socket
DataBase = {
    'apple.com': '17.253.144.10',
    'www.apple.com': 'www.apple.com.edgekey.net',
}
def process_dns_request(data):
    domain = data.decode().strip()
    if domain in DataBase:
        return DataBase[domain]
    else:
        return "Domain not found"
def start_dns_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('127.0.0.1', 55))
    print("DNS Server is running...")
    while True:
        data, addr = server_socket.recvfrom(1024)
        response = process_dns_request(data)
        server_socket.sendto(response.encode(), addr)

if __name__ == "__main__":
    start_dns_server()

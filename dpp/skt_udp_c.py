import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 6000

while True:
    message = input("Client: ")
    client_socket.sendto(message.encode(), (host, port))

    data, addr = client_socket.recvfrom(1024)
    print("Server:", data.decode())

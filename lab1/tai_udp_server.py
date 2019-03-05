from socket import *


def udp_server():
    server_port = 3001
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(('', server_port))
    print("The server is ready to receive")
    while True:
        message, client_address = server_socket.recvfrom(2048)
        print("received bytes from: ", end=" ")
        print(client_address)
        modified_message = message.decode().upper()
        server_socket.sendto(modified_message.encode(), client_address)


udp_server()


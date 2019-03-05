from socket import *


def udp_client():
    server_name = 'www.stoplagging.com'
    server_port = 3001
    client_socket = socket(AF_INET, SOCK_DGRAM)
    message = input('Input lowercase sentence: ')
    client_socket.sendto(message.encode(), (server_name, server_port))
    modified_message, server_address = client_socket.recvfrom(2048)
    print(modified_message.decode())
    client_socket.close()


udp_client()

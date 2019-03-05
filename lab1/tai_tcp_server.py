from socket import *
import re


def udp_server():
    server_port = 3002
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print("The server is ready to receive data...")

    while True:
        connection_socket, addr = server_socket.accept()
        data = connection_socket.recv(1024).decode()

        print("Received data from: ", end=" ")
        print(addr)

        formatted_data = re.findall(r'[0-9]+', data)  # Using RegEx converts string to string list
        list_of_ints = []

        # This for loop creates a copy that converted the list of strings to a list of integers
        for elements in formatted_data:
            list_of_ints.append(int(elements))

        # Get total from int list
        result_total = 0
        for number in list_of_ints:
            result_total = result_total + number

        # Get min, max, and mean from int list
        result_min = min(list_of_ints)
        result_max = max(list_of_ints)
        result_mean = get_mean_from_list(list_of_ints)

        # Concatenate results as strings
        cat_result = str(result_total) + "," + str(result_min) + "," + str(result_max) + "," + str(result_mean)

        # Send encoded cat_result to client
        connection_socket.send(cat_result.encode())

        connection_socket.close()


def get_mean_from_list(int_list):
    the_sum = float(sum(int_list))
    count = float(len(int_list))
    if not int_list:  # if list is empty
        return False
    return float(the_sum / count)


udp_server()


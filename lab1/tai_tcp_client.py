"""
    This is a TCP client program that takes in integer command line arguments.
    It then sends a formatted string of the arguments to a udp_server.
    After the udp_server does calculations it sends data back to this client.
    Then this client prints the results.

    Written By: Tai Dao
    Date: 3/3/2019
"""
from socket import *
import sys
import re


def udp_client():
    server_name = 'www.stoplagging.com'
    server_port = 3002
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(server_name, server_port)

    set_of_integers = str(sys.argv)  # This set is the result of the command line arguments

    if check_input(sys.argv) == 0:
        pass
    else:
        print("\nData sent to server: " + set_of_integers)

        client_socket.send(set_of_integers.encode())
        received_data, server_address = client_socket.recvfrom(2048)
        print("Data was received from server...\n")
        decoded_data = received_data.decode()

        list_of_data = re.split(",", decoded_data)  # Split decoded data using regex and store it as a list of strings

        result_total = list_of_data[0]
        result_min = list_of_data[1]
        result_max = list_of_data[2]
        result_mean = list_of_data[3]

        print("Formatted data below")
        print("Total:", result_total)
        print("Lowest:", result_min)
        print("Highest:", result_max)
        print("Mean:", result_mean + "\n")

        client_socket.close()


def check_input(set_input):
    """
    This function checks the input to see if the command line arguments is only integers, and isn't null
    :param set_input:
    :return 1 or 0: 0 for false 1 for true
    """

    if len(set_input) == 1:  # If input is only 1 element long
        print("No arguments specified. Please enter some integers as command line arguments.\n")
        print("Program exiting...\n")
        return 0
    else:
        # Skipping first element in set
        inter_set = iter(set_input)
        next(inter_set)

        # Concatenating second to n elements to string
        cat_set = ""
        for element in inter_set:
            cat_set = cat_set + element

        # Checks input for dots with RegEx
        check_dots = re.search(r'\.', cat_set)
        if check_dots:
            print("Invalid Input: Please use integers as arguments not floating point values.\n")
            print("Program exiting...\n")
            return 0

        # Checks input for other characters besides numbers with RegEx
        else:
            check_numbers = re.search(r'[^0-9]+', cat_set)
            if check_numbers:
                print("Invalid Input: Please use integers as arguments not letters or symbols.\n")
                print("Program exiting...\n")
                return 0
            else:
                return 1


udp_client()

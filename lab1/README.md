# Readme for UDP Client and UDP Server
## Requirements:
* This optionally requires two host machines. One to run the server and the other to run the client.
* If you just want to run the client only you may, because by default it connects to my server at www.stoplagging.com:3001 if this is the case you only need one host machine.
* You must have python3 installed on your computer.

## How to run server:
1. First you must edit line 16 of tai_udp_server.py so that server_name is your server host's IP.
3. The host server must have UDP port 3001 open in the firewall. Your router must also unblock this port.
4. Then on the serving host navigate to and start the program with "python tai_udp_server.py" in a command line terminal.

## How to run client:
1. Navigate to the program and type "python tai_udp_client.py 2 4 8" in the command line terminal of the client host.
2. You may try other inputs besides 2 4 8 as long as they are integer inputs

## Test Cases
### Case 1: No arguments
> python .\tai_udp_client.py
> No arguments specified. Please enter some integers as command line arguments.
>
> Program exiting...

Result is expected Test Case 1 passed...


### Case 2: Floating point arguments
> python .\tai_udp_client.py 12 3 4.4
> Invalid Input: Please use integers as arguments not floating point values.
> 
> Program exiting...

Result is expected Test Case 2 passed...

### Case 3: Symbols in arguments
> python .\tai_udp_client.py 12 3 %!
> Invalid Input: Please use integers as arguments not letters or symbols.
> 
> Program exiting...

Result is expected Test Case 3 passed...


### Case 4: Letters in arguments
> python .\tai_udp_client.py 48 12 a b
> Invalid Input: Please use integers as arguments not letters or symbols.
> 
> Program exiting...

Result is expected Test Case 4 passed...


### Case 5: Valid arguments
> python .\tai_udp_client.py 2 4 8
> 
> Data sent to server: ['.\\tai_udp_client.py', '2', '4', '8']
> Data was received from server...
> 
> Formatted data below <br>
> Total: 14 <br>
> Lowest: 2 <br>
> Highest: 8 <br>
> Mean: 4.666666666666667 <br>

Result is expected Test Case 5 passed...



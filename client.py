__author__ = 'Vincent'
#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
while True:
    s = socket.socket()         # Create a socket object
    #host = socket.gethostname() # Get local machine name
    port = 7777 # Reserve a port for your service.

    s.connect(('localhost', port))

    command = raw_input('ENTER TX: ')

    s.send(command)

    received = s.recv(1024)

    print received

    s.close                     # Close the socket when done

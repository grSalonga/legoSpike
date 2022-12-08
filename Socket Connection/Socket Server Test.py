# Simple socket server test. This needs a third party spike prime board.
# https://antonsmindstorms.com/product/spike-ri-wifi-i2c-board/
# This should be run on the spike hub.
# Must manually input the ESP8266's IP address at the moment
# - Aren

import socket

HostIPAddresss = 'Insert IP Address Here'
Port = 56765    
Backlog = 1
DataTransferSize = 1024

# Sequence of socket API calls and data flow
# 1. create socket
# 2. bind socket to a specific MAC address and port
# 3. begin listening for x connection requests from clients
# 4. when a client connections, accept to complete the connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) 
s.bind((HostIPAddresss, Port))
s.listen(Backlog)

try:
    connection, address = s.accept()

    while 1:
        data = connection.recv(DataTransferSize)
        if data:
                print(data)
                connection.send(data)
                s.send(bytes('data recieved, hello client!', 'utf-8'))
except:
    connection.close()
    s.close()
    print("Socket Closed")
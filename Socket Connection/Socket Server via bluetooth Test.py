# This won't work, no support for bluetooth addressing families on micropython.
# Only able to use INET (IPv4) and INET6 (IPV6).


# Simple socket server via bluetooth test.
# This should be run on the spike hub.
# Must manually input the bluetooth adapter's MAC Address at the moment
# It's possible to find the local bluetooth adapter's MAC Address using system commands
# on linux, but I'm still looking into a way to do it using just python.
# Unsure if normal sockets will function the same as bluetooth sockets
# on micropython.
# - Aren

import socket

HostMACAddresss = 'Insert MAC Address Here'
Port = 56765    
Backlog = 1
DataTransferSize = 1024

# Sequence of socket API calls and data flow
# 1. create socket
# 2. bind socket to a specific MAC address and port
# 3. begin listening for x connection requests from clients
# 4. when a client connections, accept to complete the connection
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) 
s.bind((HostMACAddresss, Port))
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



# Simple socket client. This needs a third party spike prime board.
# https://antonsmindstorms.com/product/spike-ri-wifi-i2c-board/
# This should be run on the device connecting to the spike hub.
# Must manually input the server's IP address the moment.
# - Aren

import socket

HostIPAddress = 'Insert IP Address Here'
Port = 56765    # must be same port as server

# Creates a socket, then attempts to connect to 
# the designated IP address and port.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
s.connect((HostIPAddress, Port))

while 1:
    send = input()
    if send == ("exit" or "quit" or "stop"):
        break
    s.send(bytes(send, 'utf-8'))
s.close()
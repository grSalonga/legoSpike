# Simple socket client. This needs a third party spike prime board.
# https://antonsmindstorms.com/product/spike-ri-wifi-i2c-board/
# This should be run on the device connecting to the spike hub.
# Must manually input the server's IP address the moment.
# - Aren

# Extension of original Socket Client Test.py
# - Daniel

import socket
import ujson

HostIPAddress = 'Insert IP Address Here'
Port = 56765    # must be same port as server

# Creates a socket, then attempts to connect to 
# the designated IP address and port.
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
	s.connect((HostIPAddress, Port))
except:
	connection.close()
    s.close()
    print("Socket Closed")

# Connection secured
# Now we read in the input
contents = []
with open('anyfile.txt') as f:
    contents = f.readlines()

# For each line in the input file, send the JSON string to the robot
for line in contents:
    send = ujson.dumps(line)
    s.send(bytes(send, 'utf-8'))
s.close()
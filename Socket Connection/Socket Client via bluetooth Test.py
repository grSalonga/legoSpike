# This won't work for two reasons
# 1. AF_BLUETOOTH and BTPROTO_RFCOMM are for linux and Winsock's AF_BTH is for windows.
# 2. The spike doesn't run linux or windows. Micropython only supports INET (IPv4) and INET6 (IPV6).
#    The spike doesn't have wifi capabilities, so it doesn't support internet protocols natively.

# Simple socket client via bluetooth test.
# This should be run on the device connecting to the spike hub.
# Must manually input the bluetooth server device's name at the moment.
# Unsure if normal sockets will function the same as bluetooth sockets
# on micropython.
# - Aren

import socket
import bluetooth

DeviceName = 'Insert Servers Device Name Here'
HostMACAddresss = ''
Port = 56765    # must be same port as server

# Gets nearby bluetooth devices. This theoretically should find the MAC address of the designated 
# bluetooth device's name. Since the bluetooth library's mainly for BLE, it's uncertain
# if it will find the correct MAC address though.
devices = bluetooth.discover_devices()
for bluetoothAddress in devices:
    if DeviceName == bluetooth.lookup_name( bluetoothAddress):
        HostMACAddress = bluetoothAddress

# Creates a socket, then attempts to connect to 
# the designated MAC address and port.
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((HostMACAddress, Port))

while 1:
    send = input()
    if send == ("exit" or "quit" or "stop"):
        break
    s.send(bytes(send, 'utf-8'))
s.close()
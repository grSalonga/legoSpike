import serial
import time

ser = serial.Serial('COM4') #Test for port 1
ser2 = serial.Serial('COM5') #Test for port 2
#Listen on bluetooth port for message from hub
print("Waiting for message...\n")

while ser.in_waiting == 0 and ser2.in_waiting == 0: #Loop until message is received
    time.sleep(2) #Sleep to allow for port to send message
    
num = ser.in_waiting #Check for number of bytes in message
num2 = ser2.in_waiting #Check for number of bytes in message

#Receive message from hub, then send message back
if num != 0:
    msg = ser.read(num) #Read from port 1
    msg = msg.decode("utf-8")
    #Port 1 says:
    print("Message from LEGO Hub: ")
    print(msg, "\n")
    ser.write(str.encode('Hi!'))
elif num2 != 0:
    msg2 = ser2.read(num2) #Read from port 2
    msg2 = msg2.decode("utf-8")
    #Port 2 says:
    print("Message from LEGO Hub: ")
    print(msg2, "\n")
    ser2.write(str.encode('Hi!'))

print("Received and sent message...\n")
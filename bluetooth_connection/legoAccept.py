#Program to test basic communication over bluetooth with python
#Mainly tested with /bluetooth_connection/receiveAndSendHello.py

from spike import Motor
import hub
import utime
import ujson

#################################################################################################
#Code from SpikeReader.py implemented as functions for testing
class Parsing:

    def dataParser(self, data, btc):
        iter = 0

        # Motor tree
        # {"Class of command", "Port", "Specific command", "Params1", "Param2", ...}
        if(data[iter] == "Motor"):
            iter+=1
            motor = Motor(data[iter])
            iter+=1

            # ACTIONS ---
            # run_to_position(degrees, direction='shortest path', speed=None)
            # **can have multiple params
            if (data[iter] == "run_to_position"):
                iter+=1
                # 1st param = degrees
                degrees = data[iter]
                # if there are more parameters, save them for the call
                # otherwise use defaults
                if (len(data) == 5):
                    # 2nd param = direction
                    iter+=1
                    direction = data[iter]
                    if (len(data) == 6):
                        # 3rd param = speed
                        iter+=1
                        speed = data[iter]
                    else:
                        speed = motor.get_default_speed()
                else:
                    direction = "shortest path"
                # Function call
                motor.run_to_position(degrees, direction, speed)

                btc.write("Success!")
                return
            # run_to_degrees_counted(degrees, speed=None)
            # **can have multiple params
            elif (data[iter] == "run_to_degrees_counted"):
                iter+=1
                # 1st param = degrees
                degrees = data[iter]
                # if there are more parameters, save them for the call
                # otherwise use defaults
                if (len(data) == 5):
                    # 2nd param = speed
                    iter+=1
                    speed = data[iter]
                else:
                    speed = motor.get_default_speed()
                # Function call
                motor.run_to_degrees_counted(degrees, speed)

                btc.write("Success!")
                return
            # run_for_degrees(degrees, speed=None)
            elif (data[iter] == "run_for_degrees"):
                iter+=1
                # 1st param = degrees
                degrees = data[iter]
                # if there are more parameters, save them for the call
                # otherwise use defaults
                if (len(data) == 5):
                    # 2nd param = speed
                    iter+=1
                    speed = data[iter]
                else:
                    speed = motor.get_default_speed()
                # Function call
                motor.run_for_degrees(degrees, speed)

                btc.write("Success!")
                return
            # run_for_rotations(rotations, speed=None)
            elif (data[iter] == "run_for_rotations"):
                iter+=1
                # 1st param = rotations
                rotations = data[iter]
                # if there are more parameters, save them for the call
                # otherwise use defaults
                if (len(data) == 5):
                    # 2nd param = speed
                    iter+=1
                    speed = data[iter]
                else:
                    speed = motor.get_default_speed()
                # Function call
                motor.run_for_rotations(rotations, speed)

                btc.write("Success!")
                return
            # run_for_seconds(seconds, speed=None)
            elif (data[iter] == "run_for_seconds"):
                iter+=1
                # 1st param = seconds
                seconds = data[iter]
                # if there are more parameters, save them for the call
                # otherwise use defaults
                if (len(data) == 5):
                    # 2nd param = speed
                    iter+=1
                    speed = data[iter]
                else:
                    speed = motor.get_default_speed()
                # Function call
                motor.run_for_seconds(seconds, speed)

                btc.write("Success!")
                return
            # start(speed=None)
            elif (data[iter] == "start"):
                if (len(data) == 4):
                    # 1st param = speed
                    iter+=1
                    speed = data[iter]
                else:
                    speed = motor.get_default_speed()
                # Function call
                motor.start(speed)

                btc.write("Success!")
                return
            # stop()
            elif (data[iter] == "stop"):
                # Function call
                motor.stop()

                btc.write("Success!")
                return
            # start_at_power(power)
            elif (data[iter] == "start_at_power"):
                if (len(data) == 4):
                    # 1st param = power
                    iter+=1
                    power = data[iter]
                else:
                    power = motor.get_default_speed()
                # Function call
                motor.start_at_power(power)

                btc.write("Success!")
                return
            # MEASUREMENTS ---
            # get_speed()
            elif (data[iter] == "get_speed"):
                # Function call
                speed = motor.get_speed()
                btc.write(speed)
                return

            # get_position()
            elif (data[iter] == "get_position"):
                # Function call
                pos = motor.get_position()
                btc.write(pos)
                return

            # get_degrees_counted()
            elif (data[iter] == "get_degrees_counted"):
                # Function call
                degreesCounted = motor.get_degrees_counted
                btc.write(degreesCounted)
                return

            # get_default_speed()
            elif (data[iter] == "get_default_speed"):
                # Function call
                defaultSpeed = motor.get_default_speed
                btc.write(defaultSpeed)
                return

            # EVENTS ---
            # was_interrupted()
            elif (data[iter] == "was_interrupted"):
                if (motor.was_interrupted()):
                    btc.write("Motor was interrupted.")
                else:
                    btc.write("Motor was not interrupted.")
            
            # was_stalled()
            elif (data[iter] == "was_stalled"):
                if (motor.was_stalled()):
                    btc.write("Motor was stalled.")
                else:
                    btc.write("Motor was not stalled.")
                return

            # SETTINGS ---
            # set_degrees_counted()
            elif(data[iter] == "set_degrees_counted"):
                iter+=1
                # param = degrees counted
                degreesCounted = data[iter]
                # Function call
                motor.set_degrees_counted(degreesCounted)
                
                btc.write("Success!")
                return

            # set_default_speed()
            elif(data[iter] == "set_default_speed"):
                iter+=1
                # param = default speed from -100 to 100
                if (data[iter] > 100):
                    defaultSpeed = 100
                elif (data[iter] < -100):
                    defaultSpeed = -100
                else: 
                    defaultSpeed = data[iter]
                # Function call
                motor.set_default_speed(defaultSpeed)
                
                btc.write("Success!")
                return

            # set_stop_action()
            elif(data[iter] == "set_stop_action"):
                # param = default action either coast, brake, or hold
                if (len(data) == 4):
                    iter+=1
                    stopAction = data[iter]
                else:
                    stopAction = "coast"
                # Function call
                motor.set_stop_action(stopAction)

                btc.write("Success!")
                return

            # set_stall_detection()
            elif(data[iter] == "set_stall_detection"):
                # param = boolean for on or off
                if (len(data) == 4):
                    iter+=1
                    stallDetection = data[iter]
                else:
                    stallDetection = True
                # Function call
                motor.set_stall_detection(stallDetection)

                btc.write("Success!")
                return

     #############################################################   MOTOR PAIR TREE   #####################################################
        # Motor Pair Tree
        # {"Class of command", "Port1", "Port2", "Specific command", "Param1", "Param2", ...}
        if(data[iter] == "MotorPair"):
            iter+=1
            motor_pair = MotorPair(data[iter], data[iter+1])
            iter+=2

            # ACTIONS ---
            # move()
            if(data[iter] == "Move"):
                amount = 0
                unit = "cm"
                steering = 0
                speed = get_default_speed()
                if(len(data) == 5):
                    iter+=1
                    amount = data[iter]
                    if(len(data) == 6):
                        iter+=1
                        unit = data[iter]
                        if(len(data)==7):
                            iter+=1
                            steering = data[iter]
                            if(len(data)==8):
                                iter+=1
                                speed = data[iter]

                motor_pair.move(amount, unit, steering, speed)
                btc.write("Success!")
                return

            # start()
            elif(data[iter] == "Start"):  
                steering = 0
                speed = get_default_speed()
                if(len(data) == 5):
                    iter+=1
                    steering = data[iter]
                    if(len(data) == 6):
                        iter+=1
                        speed = data[iter]  

                motor_pair.start(steering, speed)
                btc.write("Success!")
                return

            # stop()
            elif(data[iter] == "Stop"):
                motor_pair.stop()
                btc.write("Success!")
                return

            # move_tank()
            elif(data[iter] == "MoveTank"):
                amount = 0
                unit = "cm"
                left_speed = get_default_speed()
                right_speed = get_default_speed()
                if(len(data) == 5):
                    iter+=1
                    amount = data[iter]
                    if(len(data) == 6):
                        iter+=1
                        unit = data[iter]
                        if(len(data) == 7):
                            iter+=1
                            left_speed = data[iter]
                            if(len(data) == 8):
                                iter+=1
                                right_speed = data[iter]                      

                motor_pair.move_tank(amount, unit, left_speed, right_speed)
                btc.write("Success!")
                return

            # start_tank()
            elif(data[iter] == "StartTank"):
                left_speed  = 0
                right_speed = 0
                if(len(data) == 5):
                    iter+=1
                    left_speed = data[iter]
                    if(len(data) == 6):
                        iter+=1
                        right_speed = data[iter]

                motor_pair.start_tank(left_speed, right_speed)
                btc.write("Success!")
                return
                
            # start_at_power()
            elif(data[iter] == "StartAtPower"):
                power = 100
                steering = 0

                if(len(data) == 5):
                    iter+=1
                    power = data[iter]
                    if(len(data) == 6):
                        iter+=1
                        steering = data[iter]

                motor_pair.start_at_power(power, steering)
                btc.write("Success!")
                return

            # start_tank_at_power()
            elif(data[iter] == "StartTankAtPower"):
                left_power  = 0
                right_power = 0
                if(len(data) == 5):
                    iter+=1
                    left_power = data[iter]
                    if(len(data) == 6):
                        iter+=1
                        right_power = data[iter]                       
                
                motor_pair.start_tank_at_power(left_power, right_power)
                btc.write("Success!")
                return

            # MEASUREMENTS ---
            # get_default_speed()
            elif(data[iter] == "GetDefaultSpeed"):
                get_default_speed()
                btc.write("Default Speed = " + get_default_speed())
                btc.write("Success!")
                return

            # SETTINGS ---
            # set_motor_rotation()
            elif(data[iter] == "SetMotorRotation"):
                amount = 17.6
                unit = "cm"
                if(len(data) == 5):
                    iter+=1
                    amount = data[iter]
                    if(len(data) == 6):
                        iter+=1
                        unit = data[iter]
                
                motor_pair.set_motor_rotation(amount, unit)
                btc.write("Success!")
                return

            # set_default_speed()
            elif(data[iter] == "SetDefaultSpeed"):
                if(len(data) == 5):
                    iter+=1
                    speed = data[iter]
                else:
                    speed = 100

                motor_pair.set_default_speed(speed)
                btc.write("Success!")
                return

            # set_stop_action()   
            elif(data[iter] == "SetStopAction"):
                if(len(data) == 5):
                    iter+=1
                    action = data[iter]
                else:
                    action = "coast"
                
                motor_pair.set_stop_action(action)
                btc.write("Success!")
                return
                
        #if you get here, then the command fell through the if tree
        btc.write("Failure!")
        return
        




#End of SpikeReader.py implementation
########################################################################################


#Used for feedback that something executed properly
def song():
    hub.sound.beep(220, 1000)
    utime.sleep(1)
    hub.sound.beep(146, 1000)
    utime.sleep(1)
    hub.sound.beep(174, 1000)
    utime.sleep(1)
    hub.sound.beep(195, 1000)
    utime.sleep(0.5)
    hub.sound.beep(174, 1000)
    utime.sleep(0.5)
    hub.sound.beep(164, 1000)
    utime.sleep(1)
    hub.sound.beep(195, 1000)
    utime.sleep(1)
    hub.sound.beep(184, 2000)
    utime.sleep(1)

def songConfirmation():
    if hub.button.right.is_pressed():
        song()
        utime.sleep(2)
        return true
#Start of main program, Happy Halloween 2021
hub.display.show(hub.Image.GHOST)
utime.sleep(2)

#Object to read and write over bluetooth
bt = hub.BT_VCP(0)

#If the bt object was successfully created, there should be a open connection
#Unsuccesful connection
if not bt:
    print("FALSE")
    hub.display.show(hub.Image.SAD)

#Console and hub confirmation
print("TRUE")
hub.display.show(hub.Image.HAPPY)
bt.write("Testing reading JSON...")
bt.readline() #clear buffer

parser = Parsing()

# Commented out in case original script is still being used.
# Attempting to recieve, parse, and eventually evaluate recieved JSON info.
while True:
    #jsonRecieved = bt.recv(data, 1000)    # If sending json objects (?)
    #newObject = ujson.load(jsonRecieved)
    jsonRecieved = ""

    while jsonRecieved == "" or jsonRecieved == None:
        hub.display.show("Waiting...")
        jsonRecieved = bt.readline()        # If sending json strings
    jsonRecieved = jsonRecieved.decode("utf-8")
    newObject = ujson.loads(jsonRecieved)
    if (newObject == ValueError):
        bt.write("Error: JSON string not correctly formed.")
        continue
    hub.display.show(hub.Image.YES)
    utime.sleep(2)

    print(newObject)
    parser.dataParser(newObject, bt)
    #parser.dataParser2(newObject)
    
    
    # At this point the json should be translated into their respective python counterparts
    # JSON object = python dict, array = list, string = unicode, number(int) = int,long
    # number(real) = float, true = True, false = False, null = None
    # https://docs.python.org/2/library/json.html#json-to-py-table

    # Access python dict by iterating. Just writing back to client here.
    #for key, value in newObject.items():
    #bt.write("Key = " + key + ", Value = " + value)

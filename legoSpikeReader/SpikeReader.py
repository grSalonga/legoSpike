import json
#import PrimeHub

#This is going to need to be changed to however we are going to send json data
with open("Kiki.json") as jsonFile:
    data = json.load(jsonFile)

#hub = PrimeHub()

#while(True):

iter = 0
#Button tree
if(data[iter] == "Button"):
    iter+=1
    #right button
    if(data[iter] == "Left"):  
        iter+=1
        if(data[iter] == "WaitUntilPressed"):
            iter+=1
            print("hub.left_button.wait_until_pressed()")

    #left button
    elif(data[iter] == "right"):
        iter+=1
        if(data[iter] == "WaitUntilPressed"):
            iter+=1
            print("hub.right_button.wait_until_pressed()")

#color_sensor tree
elif(data[iter] == "color_sensor"):
    iter+=1
    if(data[iter] == "wait_until_color"):
        iter+=1
        if(data[iter] == "blue"):
            print("color_sensor.wait_until_color('blue')")
        elif(data[iter] == "green"):
            print("color_sensor.wait_until_color('green')")


# Possible alternate approach to nested if's?
# Create defs of possible inputs, then just call them if that input comes up. 
# Increment iter to continue along the read json info.
def button(temp = ("Left" or "Right" or "Center")):
    dict = {
        "Left": waitUntilPressed("Left"),
        "Right": waitUntilPressed("Right"),
        "Center": waitUntilPressed("Center")
    }
    return dict.get(temp, "Invalid")

def waitUntilPressed(temp = ("Left" or "Right")):
    dict = {
        "Left": "hub.left_button.wait_until_pressed()",
        "Right": "hub.right_button.wait_until_pressed()",
        "Center": "hub.center_button.wait_until_pressed()"
    }
    return dict.get(temp, "Invalid")

def colorSensor(temp = "wait_until_color", color = ("blue" or "green")):
    dict = {
        "wait_until_color": waitUntilColor(color)
    }
    return dict.get(temp, "Invalid")

def waitUntilColor(color = ("blue" or "green")):
    dict = {
        "blue": "color_sensor.wait_until_color('blue')",
        "green": "color_sensor.wait_until_color('green')"
    }
    return dict.get(color, "Invalid")

iter = 0
if(data[iter] == "Button"):
    iter+=1
    print(button(data[iter]))

if(data[iter] == "color_sensor"):
    iter+=1
    print(colorSensor("wait_until_color", data[iter])





        
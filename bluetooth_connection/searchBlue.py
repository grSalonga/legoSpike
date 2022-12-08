'''This program should look for nearby devices for 20 seconds.
        -Everything it finds should be but in the nearby_devcies array.
        -After looking, it will iterate on the array looking for 
            what ever the spike name is.(I didn't know what it was so it put LegoSpikeName)
        -If it finds it sets a bool variable which is checked
        -We can send a message if its true
        -Error if not
    I could not get it to work on my machine but that might because 
    of my environement. I was thinking that this could be to be used on our laptops
    to find the spike and send hello world to it
    
    -Gregg'''

import bluetooth

found = False
print("Starting search")

'''This should have the bluetooth look around for 20 seconds?'''
nearby_devices = bluetooth.discover_devices(duration = 20, lookup_names = True,
                                            flush_cache = True, lookup_class = False)

print("Search Done")

for address in nearby_devices:
    if "LegoSpikeName" == bluetooth.lookup_name(address):
        print("The lego spike has been found")
        found = True
        break

if found == True:
    print("Send Message")
else:
    print("Error")
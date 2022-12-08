#https://docs.micropython.org/en/latest/library/bluetooth.html
#This is what I used as a source.
'''This documentation is not very good and I'm not sure '''
import bluetooth
#from spike import PrimeHub


'''These are all codes that i found in the documentation.
I think what happens is when gap_scan finds something it will call bt_irq which we have to define with one of these 
codes as the event parameter.

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE = const(3)
_IRQ_GATTS_READ_REQUEST = const(4)
_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_DONE = const(6)
_IRQ_PERIPHERAL_CONNECT = const(7)
_IRQ_PERIPHERAL_DISCONNECT = const(8)
_IRQ_GATTC_SERVICE_RESULT = const(9)
_IRQ_GATTC_SERVICE_DONE = const(10)
_IRQ_GATTC_CHARACTERISTIC_RESULT = const(11)
_IRQ_GATTC_CHARACTERISTIC_DONE = const(12)
_IRQ_GATTC_DESCRIPTOR_RESULT = const(13)
_IRQ_GATTC_DESCRIPTOR_DONE = const(14)
_IRQ_GATTC_READ_RESULT = const(15)
_IRQ_GATTC_READ_DONE = const(16)
_IRQ_GATTC_WRITE_DONE = const(17)
_IRQ_GATTC_NOTIFY = const(18)
_IRQ_GATTC_INDICATE = const(19)
_IRQ_GATTS_INDICATE_DONE = const(20)
_IRQ_MTU_EXCHANGED = const(21)
_IRQ_L2CAP_ACCEPT = const(22)
_IRQ_L2CAP_CONNECT = const(23)
_IRQ_L2CAP_DISCONNECT = const(24)
_IRQ_L2CAP_RECV = const(25)
_IRQ_L2CAP_SEND_READY = const(26)
_IRQ_CONNECTION_UPDATE = const(27)
_IRQ_ENCRYPTION_UPDATE = const(28)
_IRQ_GET_SECRET = const(29)
_IRQ_SET_SECRET = const(30)
'''
#These codes should be the only ones that are used
_IRQ_SCAN_RESULT = 5
_IRQ_SCAN_DONE = 6

#I think this is called by gap_scan
def bt_irq(event, data):
    #This should be the case where the lego scanned something
    if event == _IRQ_SCAN_RESULT:
        print("do things with the messege")
    #This should be the case where gap_scan is done scanning
    elif event ==  _IRQ_SCAN_DONE:
        print("done")
    

#hub = PrimeHub()

# This should make blueFinder a BLE object, I don't know if this syntax is correct
# My text editor isn't flagging it
blueFinder = bluetooth
blueFinder.config(addr_mode = 0x00)

#This is used in gap_scan
#When it is set to 0 it should scan idefinetly until it finds something
scanTime = 0

#What I intend for the loop to do is every iteration, scan indefintly with gap scan
while True:
    #BLE.gap_scan(duration_ms, interval_us=1280000, window_us=11250, active=False, /)
    #gap_scan should run a scan operation lasting for the specified time, since 
    #duration is 0, it will scan indefinetly until it finds something
    #I think this calls bt_irq which is defined above
    blueFinder.gap_scan(scanTime, interval_us=1280000, window_us=11250, active = False)

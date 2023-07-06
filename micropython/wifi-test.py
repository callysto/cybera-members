import network
from time import sleep

nic = network.WLAN(network.STA_IF)
nic.active(True)

'''
accessPoints = nic.scan()
for ap in accessPoints:
    print(ap)
'''

# set power mode to get WiFi power-saving off (if needed)
nic.config(pm = 0xa11140)

nic.connect('CyberaGuests', 'Seven-Sisters-Peak')

'''
status codes
3: link up
2: link no IP
1: link join
0: link down
-1: link fail
-2: link no net
-3: link bad auth
'''

#while not nic.isconnected() and nic.status() >= 0:
for x in range(20):
    if not nic.isconnected() and nic.status() >= 0:
        print('Waiting to connect... status code:', nic.status())
        sleep(1)

print(nic.ifconfig())

    

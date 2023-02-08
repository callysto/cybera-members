from machine import Pin
from time import sleep
import network
import urequests as requests

led = Pin("LED", Pin.OUT)
led.on()

passwords = [['SSID','password']]

# connect the network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(passwords[0][0], passwords[0][1])
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    sleep(1)
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('WiFi connection failed')
else:
    ip = wlan.ifconfig()[0]
    print('IP: ', ip)
    led.off()


# try to get cybera.py from online, otherwise run local version
try:
    r = requests.get('https://callysto.github.io/cybera-members/cybera.py')
    with open('cybera.py', 'w') as f:
        f.write(r.text)
except:
    pass
import cybera
cybera

from machine import Pin
from neopixel import NeoPixel
from time import sleep
import network
import urequests as requests
import ujson

# connect the network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID','password')  # update these values
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    sleep(1)
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    print('connected')
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)

# get online file
response = requests.get('https://gist.githubusercontent.com/misterhay/4d2fcc46f1386cf97d95d62805bf8fc2/raw/b0ae3cd42559c5c30f1580bceb7909e4f57a66df/neopixel.txt')
values = []
for value in response.text.split('\n'):
    colors = value.split(' , ')
    values.append((int(colors[0]), int(colors[1]), int(colors[2])))
print(values)

n_pixels = 18
np = NeoPixel(Pin(0), n_pixels)

color = (50, 0, 50)

for i in range(n_pixels):
    #np[i] = (100, 0, 0)
    #np[i] = (0, i, 0)
    np[i] = values[i]
    np.write()


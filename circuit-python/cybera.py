import urequests as requests
from machine import Pin
from neopixel import NeoPixel

#import ujson


# writing files works as expected
#with open('testing.txt', 'w') as f:
#    f.write('this is a test')

#from machine import Timer
#tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
#tim.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))  # 2000 microseconds





# get online file, add a try except here with default values for neopixel colors
response = requests.get('https://gist.githubusercontent.com/misterhay/4d2fcc46f1386cf97d95d62805bf8fc2/raw/b0ae3cd42559c5c30f1580bceb7909e4f57a66df/neopixel.txt')
values = []
for value in response.text.split('\n'):
    colors = value.split(' , ')
    values.append((int(colors[0]), int(colors[1]), int(colors[2])))
#print(values)

n_pixels = 18
np = NeoPixel(Pin(0, Pin.OUT), n_pixels)

#color = (50, 0, 50)

for i in range(n_pixels):
    #np[i] = (100, 0, 0)
    #np[i] = (0, i, 0)
    # add some data validation and defaults here
    np[i] = values[i]
    np.write()


import urequests as requests
from machine import Pin
from neopixel import NeoPixel

#from machine import Timer
#tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
#tim.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))  # 2000 microseconds

leds = {}
# get online file, add a try except here with default values for neopixel colors
try:
    r = requests.get('https://callysto.github.io/cybera-members/status.csv')
    status = r.text.split('\n')
    header = status[0]
    led_index, red_index, green_index, blue_index = 1, 3, 4, 5
    for n, value in enumerate(header.split(',')):
        if value.lower() == 'led':
            led_index = n
        if value.lower() == 'red':
            red_index = n
        if value.lower() == 'green':
            green_index = n
        if value.lower() == 'blue':
            blue_index = n

    for line in status[1:]: # skip header
        values = line.split(',')
        try:
            leds[int(values[led_index])] = (int(values[red_index]), int(values[green_index]), int(values[blue_index]))
        except:
            pass # in case there's a blank line
except:
    for n in range(28):
        leds[n] = (200,200,200)

n_pixels = len(leds)
np = NeoPixel(Pin(0, Pin.OUT), n_pixels)
for i in range(n_pixels):
    np[i] = leds[i]
np.write()
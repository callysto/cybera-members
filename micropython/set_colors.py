#import urequests as requests
import requests

leds = {}
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
print(leds)
# Cybera Members Status Art

The purpose of this project is to create a physical map of Cybera members around Alberta. Each pixel represents a city or town home to one or more Cybera members, and the brightness and colour can be adjusted to display data about that location.

## Setup

* The [MicroPython code](https://github.com/callysto/cybera-members/blob/main/micropython/main.py) should be on the Raspberry Pi Pico W.
  * Change the WiFi SSID and passphrase to approprate values for your location.
  * It should connect to the WiFi, then retrieve and run the code from [cybera.py](https://github.com/callysto/cybera-members/blob/main/docs/cybera.py) which then retrieves the [status.csv](https://github.com/callysto/cybera-members/blob/main/docs/status.csv) file to set LED colors.
* The status.csv file can be edited manually, or via code similar to [this Jupyter notebook](https://github.com/callysto/cybera-members/blob/main/map/map.ipynb).

## Materials

* [Birch Plywood](https://www.windsorplywood.com/product/birch-import-plywood/)
* [NeoPixels](https://www.amazon.ca/gp/product/B01DC0J3UM/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&th=10) [Guide](https://learn.adafruit.com/adafruit-neopixel-uberguide)
* [Raspberry Pi Pico W](https://www.pishop.ca/product/raspberry-pi-pico-w/)
  * [Pico W MicroPython](https://micropython.org/download/rp2-pico-w/)
* Three-strand wire (approximately 24 gage)
* solder
* hot glue and tape

## Tools

* CNC router
  * v-bit
  * drill bit
* soldering iron
* wire cutters and strippers

## Software and Code

* [VCarve Pro](https://www.vectric.com/products/vcarve-pro) or other such as [Fusion 360](https://www.autodesk.ca/en/products/fusion-360/overview)
* [Jupyter Notebook](https://github.com/callysto/cybera-members/blob/main/map/map.ipynb) to generate the [map](https://github.com/callysto/cybera-members/blob/main/map/membermap.svg) and the [CSV file](https://github.com/callysto/cybera-members/blob/main/docs/status.csv) for the pixel values
* [MicroPython](https://github.com/callysto/cybera-members/blob/main/docs/cybera.py) to fetch the CSV and set the pixel colours

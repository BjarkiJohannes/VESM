import time
import digitalio
import board
from Adafruit_IO import *
ADAFRUIT_IO_KEY = "aio_jdIv63zci6qTM6Iy0RKMzKiMEhat" # Set your APIO Key
 # Set to your Adafruit IO username.
ADAFRUIT_IO_USERNAME = 'potatoinmyass'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
    digital = aio.feeds("led")
except RequestError: 
    feed = Feed(name="led")
    LED = aio.create_feed(led)
# led set up
led = digitalio.DigitalInOut(board.D6)
led.direction = digitalio.Direction.OUTPUT
while True:
    data = aio.receive(digital.key)
    if int(data.value) == 1:
        print('received <- ON\n')
    elif int(data.value) == 0:
        print('received <- OFF\n')
 
    led.value = int(data.value)
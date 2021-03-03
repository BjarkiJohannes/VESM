from Adafruit_IO import Client, Feed, RequestError
import RPI.GPIO as GPIO
import time

ADAFRUIT_IO_USERNAME = "potatoinmyass"
ADAFRUIT_IO_KEY = "aio_DYHH50snptqmvcCOfcCiGq8OP9MB"
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
try: # if we have a 'analog' feed
    digital = aio.feeds('digital')
except RequestError: # create a analog feed
    feed = Feed(name='digital')
    analog = aio.create_feed(digital)

takki = 24
GPIO.setmode(GPIO.BCM)
GPIO.setmode(takki, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    lesa_takka = GPIO.input(takki)
    aio.send(analog.key, lesa_takka)
    time.sleep(1)
    
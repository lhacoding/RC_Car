from machine import Pin
from neopixel import NeoPixel
import time

PIXEL_PIN=3
PIXEL_COUNT=36

pin = Pin(PIXEL_PIN, Pin.OUT)
np = NeoPixel(pin, PIXEL_COUNT)

for cnt in range(5):
    np.fill((0,0,64))
    np.write()
    time.sleep(0.5)

    np.fill((0,0,0))
    np.write()
    time.sleep(0.5)
    
    
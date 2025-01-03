from machine import Pin
from neopixel import NeoPixel
import time

# 5% 밝기로 설정
BLACK = (0, 0, 0)
RED = (13, 0, 0)       
YELLOW = (13, 7, 0)    
GREEN = (0, 13, 0)     
CYAN = (0, 13, 13)     
BLUE = (0, 0, 76) # 30%    
PURPLE = (7, 0, 13)    
WHITE = (13, 13, 13)   

COLORS = (RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE, BLACK)

PIXEL_PIN = 3
PIXEL_COUNT = 36

pin = Pin(PIXEL_PIN, Pin.OUT)
np = NeoPixel(pin, PIXEL_COUNT)

for cnt in range(2):
    for color in COLORS:
        np.fill(color)
        np.write()
        time.sleep(0.3)


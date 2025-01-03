from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=200000)
display = SSD1306_I2C(128, 32, i2c)

try:
    while True:
        for i in range(0, 128, 2):
            display.fill(0)
            display.text('Moving...', i, 0)
            display.show()
            time.sleep(0.1)
        
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")


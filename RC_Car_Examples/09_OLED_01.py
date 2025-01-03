from ssd1306 import SSD1306_I2C
from machine import Pin, I2C
i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=200000)
display = SSD1306_I2C(128, 32, i2c)

display.text('Hello World', 0, 0, 1)
display.show()


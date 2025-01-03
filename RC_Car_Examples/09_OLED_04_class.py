from ssd1306 import SSD1306_I2C
from machine import Pin, I2C

class OLED:
    def __init__(self):
        self.i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=200000)
        self.display = SSD1306_I2C(128, 32, self.i2c)
        self.display.fill(0)
        self.display.show()

    def oled_print(self, msg, msg2=None, msg3=None, msg4=None):
        self.display.fill(0)
        self.display.text(msg, 0, 0, 1)
        if msg2:
            self.display.text(msg2, 0, 8, 1)
        if msg3:
            self.display.text(msg3, 0, 16, 1)
        if msg4:
            self.display.text(msg4, 0, 24, 1)
        self.display.show()

if __name__ == '__main__':
    oled = OLED()
    oled.oled_print("Hello python~")


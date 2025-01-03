from _31_ssd1306 import SSD1306_I2C
from machine import Pin, I2C

class OLED:
    @classmethod
    def begin(cls):
        i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=200000)
        cls.display = SSD1306_I2C(128, 32, i2c)
        cls.display.fill(0)
        cls.display.show() 
    @classmethod
    def print(cls,msg,msg2=None,msg3=None,msg4=None):
        cls.display.fill(0)
        cls.display.text(msg,0,0,1)
        msg2 and cls.display.text(msg2,0,8,1)
        msg3 and cls.display.text(msg3,0,16,1)
        msg4 and cls.display.text(msg4,0,24,1)
        cls.display.show()
if __name__=='__main__':
    OLED.begin()
    OLED.print("Hello python~")
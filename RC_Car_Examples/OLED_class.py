from ssd1306 import SSD1306_I2C
from machine import Pin, I2C

class OLED:
    @classmethod
    def begin(cls):
        i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=200000)
        cls.display = SSD1306_I2C(128, 32, i2c)
        cls.display.fill(0)
        cls.display.show()    
    @classmethod
    def oled_print(cls,msg,msg2=None,msg3=None,msg4=None):
        cls.display.fill(0)
        cls.display.text(msg,0,0,1)
        msg2 and cls.display.text(msg2,0,8,1)
        msg3 and cls.display.text(msg3,0,16,1)
        msg4 and cls.display.text(msg4,0,24,1)
        cls.display.show()
        
class OLED2:
    @classmethod
    def begin(cls):
        i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=200000)
        cls.display = SSD1306_I2C(128, 32, i2c)
        cls.display.fill(0)
        cls.display.show()    
    @classmethod
    def oled_print(cls, row, msg):
        #지정된 줄 번호(row)에 메시지(msg)를 출력합니다.
        y = row * 8  # 줄 번호를 y 좌표로 변환 (8px 간격)
        cls.display.fill_rect(0, y, 128, 8, 0)  # 해당 줄만 초기화
        cls.display.text(msg, 0, y, 1)
        cls.display.show()
        
if __name__=='__main__':
    OLED2.begin()
    OLED2.oled_print(1, "Hello")
    OLED2.oled_print(2, "python")


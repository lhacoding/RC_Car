from machine import ADC
import time
from OLED_class import OLED

OLED.begin()
batterySensor=ADC(26)

try:
    while True:
        batteryValue=batterySensor.read_u16()    
        batteryVoltage=batteryValue/65535*3.3
        batteryVoltage=batteryVoltage*3.077
        OLED.oled_print(f'BAT : {batteryVoltage:.2f}')
        time.sleep(1)
        
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
        


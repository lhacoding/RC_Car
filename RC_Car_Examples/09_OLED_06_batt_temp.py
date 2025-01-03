from machine import ADC
import time
from OLED_class import OLED

OLED.begin()
batterySensor=ADC(26)
sensorChannel = machine.ADC(4)
conversionFactor = 3.3/65535
try:
    while True:
        batteryValue=batterySensor.read_u16()    
        batteryVoltage=batteryValue/65535*3.3
        batteryVoltage=batteryVoltage*3.077
    
        sensorInput = sensorChannel.read_u16()
        sensorConversion = sensorInput*conversionFactor
        temperature = 27 - (sensorConversion - 0.706)/0.001721
    
        OLED.oled_print(f'BAT  : {batteryVoltage:.2f} V', f'TEMP : {temperature:.2f}C')  
        time.sleep(1)
        
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")


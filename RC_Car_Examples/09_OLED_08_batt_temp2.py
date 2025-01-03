from machine import ADC
from OLED_class import OLED2

OLED2.begin()
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
    
        OLED2.oled_print(1, f'BAT  : {batteryVoltage:.2f} V')  
        OLED2.oled_print(2, f'TEMP : {temperature:.2f}C')  
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    
    
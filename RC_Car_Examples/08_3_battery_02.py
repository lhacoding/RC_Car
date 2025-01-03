from machine import ADC
import time

batterySensor=ADC(0) # 채널번호

try:
    while True:
        batteryValue=batterySensor.read_u16()
        batteryVoltage=batteryValue/65535*3.3
        batteryVoltage=batteryVoltage*3.077
        print(batteryValue, batteryVoltage)
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    
    
from machine import ADC,Timer
import time

batterySensor=ADC(26) # 핀번호 
tim = Timer()

def tick(timer):
    batteryValue=batterySensor.read_u16()
    batteryVoltage=batteryValue/65535*3.3
    batteryVoltage=batteryVoltage*3.077
    print(f'BAT : {batteryVoltage:.3f} V')
    time.sleep(0.1)
tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)        

    
    
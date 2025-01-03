import machine
import time
sensorChannel = machine.ADC(4)
conversionFactor = 3.3/65535
try:
    while True:
        sensorInput = sensorChannel.read_u16()
        sensorConversion = sensorInput*conversionFactor
        temperature = 27 - (sensorConversion - 0.706)/0.001721
        print(temperature)
        time.sleep(2)
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    
    
   
   
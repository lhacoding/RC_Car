from machine import ADC
import time

rotationSensor=ADC(28) # 핀번호

try:
    while True:
        sensorInput=rotationSensor.read_u16()
        print(sensorInput)
        time.sleep(0.1)
    
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    
    
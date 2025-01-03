from ultrasonic_class import UltraSonicSensor
import time

ultraSonicSensor=UltraSonicSensor()
try:
    while True:
        distance_cm=ultraSonicSensor.getDistance()
        print(f'Distance : {distance_cm} cm')
        time.sleep_ms(500)
        
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    
    
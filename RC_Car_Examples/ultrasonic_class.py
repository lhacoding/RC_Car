from machine import Pin,time_pulse_us
import time

class UltraSonicSensor:
    SOUND_SPEED=340
    TRIG_PULSE_DURATION_US=10
    def __init__(self):
        self.trigPin=Pin(15,Pin.OUT)
        self.echoPin=Pin(14,Pin.IN)
    
    def trigger(self):
        self.trigPin.value(0)
        time.sleep_us(5)
        self.trigPin.value(1)
        time.sleep_us(self.TRIG_PULSE_DURATION_US)
        self.trigPin.value(0)
    
    def getDistance(self):
        self.trigger()
        ultrasonic_duration=time_pulse_us(self.echoPin,1,30000)
        distance_cm=self.SOUND_SPEED*ultrasonic_duration/20000
        return distance_cm
    
if __name__=='__main__':
    ultraSonicSensor=UltraSonicSensor()
    while True:
        distance_cm=ultraSonicSensor.getDistance()
        print(f'Distance : {distance_cm} cm')
        time.sleep_ms(500)


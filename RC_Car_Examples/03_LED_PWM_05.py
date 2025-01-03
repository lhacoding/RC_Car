from machine import Pin, PWM
import time

led_pin = PWM(Pin(25))
led_pin.freq(1000)

try:
    while True:
        for i in range(0,65025,int(65025*0.01)):
            led_pin.duty_u16(i)
            time.sleep(0.01)
        for i in range(65025,0,-int(65025*0.01)):
            led_pin.duty_u16(i)
            time.sleep(0.01)
            
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    led_pin.duty_u16(0)

        
from machine import Pin, PWM
import time
led_pin = PWM(Pin(6))

led_pin.freq(262)
led_pin.duty_u16(int(65025*0.5))
time.sleep(2)
led_pin.duty_u16(0)
            


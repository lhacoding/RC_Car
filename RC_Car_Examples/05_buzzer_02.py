from machine import Pin, PWM
import time

buzzer_pin = PWM(Pin(6))
melody = [262,294,330,349,392,440,494,523]

for note in range(len(melody)):
    buzzer_pin.freq(melody[note])
    buzzer_pin.duty_u16(int(65025*0.5))
    time.sleep(0.5)
    buzzer_pin.duty_u16(0)
    time.sleep(0.05)
            


from machine import Pin, PWM
led_pin = PWM(Pin(25))

led_pin.freq(1000)
led_pin.duty_u16(int(65025*0.5)) # 50% 듀티 사이클로 설정

from machine import Pin
import time
pins = [13,12,22,2]
leds = [ Pin(pn, Pin.OUT) for pn in pins ]
try:
    while True:
        # 모든 LED ON
        for led_pin in leds:
            led_pin.value(1)
        time.sleep(0.5)
        # 모든 LED OFF
        for led_pin in leds:
            led_pin.value(0)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    # 모든 LED 끄기
    for led_pin in leds:
        led_pin.value(0)


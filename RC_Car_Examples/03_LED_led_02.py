from machine import Pin
import time

led_pin = Pin(25, Pin.OUT)

try:
    while True:
        led_pin.value(1)  # LED ON
        time.sleep(0.05)
        led_pin.value(0)  # LED OFF
        time.sleep(0.05)

except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    led_pin.value(0)  # LED OFF

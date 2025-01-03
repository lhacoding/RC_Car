from machine import Pin
import time

led_pin = Pin(25,Pin.OUT)

try:
    while True:
        for i in range(0,11):
            for _ in range(10):  # 10번 반복
                # LED ON
                led_pin.value(1)
                time.sleep(i*0.001)
                # LED OFF
                led_pin.value(0)
                time.sleep((10-i)*0.001)
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    led_pin.value(0)  # LED OFF


from machine import Pin
import time
led1 = Pin(13, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(22, Pin.OUT)
led4 = Pin(2, Pin.OUT)
try:
    while True:
        # LED ON
        led1.value(1)
        led2.value(1)
        led3.value(1)
        led4.value(1)
        time.sleep(0.5)
        # LED OFF
        led1.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    # 모든 LED 끄기
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)

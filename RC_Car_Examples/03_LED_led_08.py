from machine import Pin
import time
led_pin = Pin(25,Pin.OUT)
try:
    while True:
        # LED 밝아지기
        for i in range(0,11):         # 0에서 10까지
            for _ in range(10):       # 10번 반복
                led_pin.value(1)      # LED ON
                time.sleep(i*0.001)
                led_pin.value(0)      # LED OFF
                time.sleep((10-i)*0.001)
        # LED 어두워지기
        for i in range(10, -1, -1):   # 10에서 0까지
            for _ in range(10):       # 10번 반복
                led_pin.value(1)      # LED ON
                time.sleep(i * 0.001)
                led_pin.value(0)      # LED OFF
                time.sleep((10 - i) * 0.001)
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    led_pin.value(0)  # LED OFF

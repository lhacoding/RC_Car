import _thread
import time
from machine import Pin
led = Pin(25, Pin.OUT)
running = True          # 쓰레드 실행 제어 플래그
def blink_led():
    while running:
        led.value(1)
        time.sleep(0.5)
        if running==False:
            break
        led.value(0)
        time.sleep(0.5)
    print("Thread 종료")
_thread.start_new_thread(blink_led, ())
try:
    while True:
        print("LED_On")
        time.sleep(0.5)
        print("LED_Off")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    running = False      # 쓰레드 종료 요청
    time.sleep(2)        # 쓰레드 종료 대기
finally:
    led.value(0)
    print("프로그램 종료 완료")



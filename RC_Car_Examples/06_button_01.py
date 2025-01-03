from machine import Pin
import time

buttonLeft=Pin(5,Pin.IN)
buttonRight=Pin(4,Pin.IN)
try:
    while True:
        buttonInputLeft=buttonLeft.value()
        buttonInputRight=buttonRight.value()
        print(f'left button : {buttonInputLeft}, right button : {buttonInputRight}')
        time.sleep(0.01)
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
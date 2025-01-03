from machine import Pin
import time
button_pin = Pin(5, Pin.IN)
led_pin = Pin(13, Pin.OUT)
buttonInputPrev = False
ledOn = False
try:
    while True:
        # 버튼 입력 값 (누르면 True, 아니면 False)
        buttonInput = not button_pin.value()
        # 버튼이 눌렸을 때
        if buttonInput and not buttonInputPrev:
            print("rising edge")
            # ledOn이 False일 때는 True로 변경하고, True일 때는 False로 변경
            ledOn = True if not ledOn else False
            led_pin.value(ledOn)
        # 버튼에서 손을 뗄 때
        elif not buttonInput and buttonInputPrev:
            print("falling edge")
        buttonInputPrev = buttonInput  # 이전 버튼 상태 업데이트
        time.sleep(0.01)               # 안정성을 위한 짧은 대기
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    led_pin.value(0)                   # 프로그램 종료 시 LED 끄기



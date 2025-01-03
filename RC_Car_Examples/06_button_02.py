from machine import Pin

button_pin = Pin(5, Pin.IN)
led_pin = Pin(13, Pin.OUT)
try:
    while True:
        buttonInput = not button_pin.value()
        led_pin.value(buttonInput)
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
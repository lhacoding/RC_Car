from machine import UART,Pin
import time

uart1=UART(0,9600,bits=8,parity=None,stop=1,tx=Pin(16),rx=Pin(17))

try:
    while True:
        txData=b'[Hello World]'
        uart1.write(txData)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")

    
from machine import UART,Pin
import time

uart1=UART(0,9600,bits=8,parity=None,stop=1,tx=Pin(16),rx=Pin(17))

try:
    while True:
        if uart1.any()>0:                    # 수신 버퍼에 데이터가 있는지 확인
            rxData=uart1.read()              # 데이터를 읽음
            print(rxData,rxData.decode())    # 데이터 출력
            
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    
    
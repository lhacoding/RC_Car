from machine import UART,Pin
import time

uart1=UART(0,9600,bits=8,parity=None,stop=1,tx=Pin(16),rx=Pin(17))

while True:
    name=input("블루투스 이름? : ")
    atName=f'AT+NAME{name}'
    txData=atName.encode()
    uart1.write(txData)
    time.sleep(1)    
    
    if uart1.any()>0:
        rxData=uart1.read()
        print(rxData.decode())

    

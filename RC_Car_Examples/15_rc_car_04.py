from DCmotor_class import DCMotor
from servo_steering_class import SteeringMotor
from rc_car_class import RCCar

from machine import UART,Pin,ADC,Timer

uart1=UART(0,9600,bits=8,parity=None,stop=1,tx=Pin(16),rx=Pin(17))

dcMotor=DCMotor(1,0)
steeringMotor=SteeringMotor(7)
rcCar=RCCar(dcMotor,steeringMotor)
rcCar.stop()

batterySensor=ADC(26)
tim = Timer()                                 # 타이머 객체 생성
def tick(timer):
    batteryValue=batterySensor.read_u16()     # 배터리 센서 값 읽기
    batteryVoltage=batteryValue/65536*3.3     # 배터리 전압 계산
    batteryVoltage=batteryVoltage*3.077       # 배터리 전압 출력
    print(f'BAT : {batteryVoltage:.3f} V')
    
# 타이머를 1초 간격으로 실행하여 tick 함수 호출
tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)

while True:
    if uart1.any()>0:          # 수신 버퍼에 데이터가 있는지 확인
        cmd=uart1.read()       # 데이터를 읽어 cmd에 저장
        cmd=cmd.decode()[0]    # # 첫 번째 문자만 추출하여 cmd에 저장
        print(cmd)
        if cmd=='w': rcCar.goForward()
        elif cmd=='q': rcCar.goForwardLeft()
        elif cmd=='e': rcCar.goForwardRight()
        elif cmd=='s': rcCar.stop()
        elif cmd=='x': rcCar.goBackward()
        elif cmd=='z': rcCar.goBackwardLeft()
        elif cmd=='c': rcCar.goBackwardRight()
    




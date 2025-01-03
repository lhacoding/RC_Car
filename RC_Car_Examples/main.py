from DCmotor_class import DCMotor
from servo_steering_class import SteeringMotor
from rc_car_class import RCCar
from machine import UART,Pin,ADC,Timer
from OLED_class import OLED2
from ultrasonic_class import UltraSonicSensor
import _thread, time
uart1=UART(0,9600,bits=8,parity=None,stop=1,tx=Pin(16),rx=Pin(17))
dcMotor=DCMotor(1,0)
steeringMotor=SteeringMotor(7)
rcCar=RCCar(dcMotor,steeringMotor)
rcCar.stop()
batterySensor=ADC(26)
tim = Timer()
def tick(timer):
    batteryValue=batterySensor.read_u16()    
    batteryVoltage=batteryValue/65536*3.3
    batteryVoltage=batteryVoltage*3.077
    print(f'BAT : {batteryVoltage:.3f}(V)')                # 배터리 전압 출력
    OLED2.oled_print(1,f'BAT : {batteryVoltage:.3f}(V)')   # OLED 1번째 줄에 출력
tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)
OLED2.begin()
ultraSonicSensor=UltraSonicSensor()
def t1():
    while True:
        distance_cm=ultraSonicSensor.getDistance()    
        print(f'Distance : {distance_cm}(cm)')                # 초음파 센서값 출력
        OLED2.oled_print(2,f'Distance : {distance_cm}(cm)')   # OLED 2번째 줄에 출력
        # 터미널에 초음파 센서값 출력
        txData=f'Distance : {distance_cm:.1f}(cm)\n\r'.encode()   # 거리 값을 소수점 첫째 자리까지 바이트 형태로 인코딩
        uart1.write(txData)
        time.sleep_ms(500)
_thread.start_new_thread(t1, ())
while True:
    if uart1.any()>0:
        cmd=uart1.read()
        cmd=cmd.decode()[0]
        print(cmd)
        if cmd=='w': rcCar.goForward()
        elif cmd=='q': rcCar.goForwardLeft()
        elif cmd=='e': rcCar.goForwardRight()
        elif cmd=='s': rcCar.stop()
        elif cmd=='x': rcCar.goBackward()
        elif cmd=='z': rcCar.goBackwardLeft()
        elif cmd=='c': rcCar.goBackwardRight()


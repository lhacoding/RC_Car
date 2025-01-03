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
tim = Timer()
def tick(timer):
    batteryValue=batterySensor.read_u16()    
    batteryVoltage=batteryValue/65536*3.3
    batteryVoltage=batteryVoltage*3.077
    print(f'BAT : {batteryVoltage:.3f} V')

tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)

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
    




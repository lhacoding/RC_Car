from DCmotor_class import DCMotor
from servo_steering_class import SteeringMotor
from rc_car_class import RCCar

from machine import UART,Pin

uart1=UART(0,9600,bits=8,parity=None,stop=1,tx=Pin(16),rx=Pin(17))

dcMotor=DCMotor(1,0)
steeringMotor=SteeringMotor(7)
rcCar=RCCar(dcMotor,steeringMotor)

rcCar.stop()

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
    



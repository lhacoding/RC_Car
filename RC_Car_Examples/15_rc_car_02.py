from DCmotor_class import DCMotor
from servo_steering_class import SteeringMotor
from rc_car_class import RCCar
import time    
    
dcMotor=DCMotor(1,0)
steeringMotor=ServoMotor(7)
rcCar=RCCar(dcMotor,steeringMotor)
    
rcCar.goForward()
time.sleep(3)
    
rcCar.goForwardLeft()
time.sleep(3)
    
rcCar.goForwardRight()
time.sleep(3)
    
rcCar.stop()
time.sleep(1)
    
rcCar.goBackward()
time.sleep(3)
    
rcCar.goBackwardLeft()
time.sleep(3)
    
rcCar.goBackwardRight()
time.sleep(3)
    
rcCar.stop()
    
    
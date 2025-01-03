from DCmotor_class import DCMotor
from servo_steering_class import SteeringMotor
import time

dcMotor=DCMotor(1,0)
steeringMotor=SteeringMotor(7)

# go forward
dcMotor.rotateForward()
steeringMotor.turnForward()
time.sleep(3)

# go forward left
dcMotor.rotateForward()
steeringMotor.turnLeft()
time.sleep(3)

# go forward right
dcMotor.rotateForward()
steeringMotor.turnRight()
time.sleep(3)

# stop
dcMotor.stop()
steeringMotor.turnForward()
time.sleep(3)

# go backward
dcMotor.rotateBackward()
steeringMotor.turnForward()
time.sleep(3)

# go backward left
dcMotor.rotateBackward()
steeringMotor.turnLeft()
time.sleep(3)

# go backward right
dcMotor.rotateBackward()
steeringMotor.turnRight()
time.sleep(3)

# stop
dcMotor.stop()
steeringMotor.centerForward()



from servo_motor_class import ServoMotor
import time
    
servoMotor=ServoMotor(7)
    
for i in range(3):
    for angle in range(0,180,1):
        servoMotor.setAngle(angle)
        time.sleep(0.01)
    for angle in range(180,00,-1):
        servoMotor.setAngle(angle)
        time.sleep(0.01)

servoMotor.setAngle(90)


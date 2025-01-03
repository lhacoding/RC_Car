from DCmotor_class import DCMotor
import time

dcMotor=DCMotor(1,0)
# 전진
dcMotor.rotateForward()
time.sleep(1)
# 정지
dcMotor.stop()
time.sleep(1)
# 후진
dcMotor.rotateBackward()
time.sleep(1)
# 정지
dcMotor.stop()


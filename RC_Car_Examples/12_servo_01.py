from machine import Pin,PWM
import time

pwm=PWM(Pin(7))
pwm.freq(50)

MIN_ANGLE=1600                       # 서보모터가 0도일 때의 PWM 값
MAX_ANGLE=7900                       # 서보모터가 180도일 때의 PWM 값
MID_ANGLE=(MIN_ANGLE+MAX_ANGLE)//2   # 서보모터가 90도일 때의 PWM 값

def setServoDutyCycle(position):
    pwm.duty_u16(position)
    
for i in range(3):
    for pos in range(MIN_ANGLE,MAX_ANGLE,50):
        setServoDutyCycle(pos)
        time.sleep(0.01)
    for pos in range(MAX_ANGLE,MIN_ANGLE,-50):
        setServoDutyCycle(pos)
        time.sleep(0.01)

setServoDutyCycle(MID_ANGLE)


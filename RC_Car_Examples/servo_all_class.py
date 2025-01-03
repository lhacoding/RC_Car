from machine import Pin,PWM

class ServoMotor:
    MIN_ANGLE = 1600                              # 서보모터가 0도일 때의 PWM 값
    MAX_ANGLE = 7900                              # 서보모터가 180도일 때의 PWM 값
    MID_ANGLE = (MIN_ANGLE + MAX_ANGLE) // 2      # 서보모터가 90도일 때의 PWM 값
    DEGREE_1 = (MAX_ANGLE - MIN_ANGLE) // 180     # 1도에 해당하는 PWM값 증가량 (7900-1600)//180=35
    
    def __init__(self,pwm):
        self.pwm=PWM(Pin(pwm))
        self.pwm.freq(50)                         # 서보모터는 50Hz PWM 신호를 사용

    def setDutyCycle(self,position):
        self.pwm.duty_u16(position)
    
    def setAngle(self, angle):
        if 0<=int(angle)<=180:                    # 각도가 0 ~ 180 범위 내에 있는지 확인
            # 각도를 PWM 값으로 변환하여 듀티 사이클 설정
            self.setDutyCycle(self.MIN_ANGLE+self.DEGREE_1*angle)
            
class SteeringMotor(ServoMotor):
    def __init__(self,pwm):
        super().__init__(pwm)
    def turnLeft(self):
        self.setAngle(0)
    def turnForward(self):
        self.setAngle(int(90*0.85))
    def turnRight(self):
        self.setAngle(180)

class SteeringMotorRemote:
    def __init__(self):
        self.steeringMotor=SteeringMotor(7)
    def control(self, cmd):
        if cmd=='l':
            self.steeringMotor.turnLeft()
        elif cmd=='m':
            self.steeringMotor.turnForward()
        elif cmd=='r':
            self.steeringMotor.turnRight()

if __name__=='__main__':
    steeringMotorRemote=SteeringMotorRemote()
    while True:
        cmd = input('left:l, middle:m, right:r >> ')
        print(cmd)
        steeringMotorRemote.control(cmd)

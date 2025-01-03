from servo_steering_class import SteeringMotor

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
        
        
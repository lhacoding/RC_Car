from servo_class import ServoMotor

class RobotFace:
    def __init__(self):
        self.servoLR=ServoMotor(18)
        self.servoUD=ServoMotor(19)

        self.servoLR.setAngle(90)
        self.servoUD.setAngle(90)

    def left(self):
        self.servoLR.setAngle(120)
        self.servoUD.setAngle(90)
    def right(self):
        self.servoLR.setAngle(60)
        self.servoUD.setAngle(90)
    def forward(self):
        self.servoLR.setAngle(90)
        self.servoUD.setAngle(90)
    def upward(self):
        self.servoLR.setAngle(90)
        self.servoUD.setAngle(60)
    def downward(self):
        self.servoLR.setAngle(90)
        self.servoUD.setAngle(120)
    def leftUpward(self):
        self.servoLR.setAngle(120)
        self.servoUD.setAngle(60)
    def rightUpward(self):
        self.servoLR.setAngle(60)
        self.servoUD.setAngle(60)
    def leftDownward(self):
        self.servoLR.setAngle(120)
        self.servoUD.setAngle(120)
    def rightDownward(self):
        self.servoLR.setAngle(60)
        self.servoUD.setAngle(120)

if __name__=='__main__':
    
    robotFace=RobotFace()

    cmd_menu = '''
    fl: face left
    fr: face right
    ff: face forward
    fu: face up
    fd: face down
    flu: face left upward
    fru: face right upward
    fld: face left down
    frd: face right down
    >> '''
    
    while True:
        cmd = input(cmd_menu)
        print(cmd)
    
        if cmd=='fl':
            robotFace.left()
        elif cmd=='fr':
            robotFace.right()
        elif cmd=='ff':
            robotFace.forward()
        elif cmd=='fu':
            robotFace.upward()
        elif cmd=='fd':
            robotFace.downward()
        elif cmd=='flu':
            robotFace.leftUpward()
        elif cmd=='fru':
            robotFace.rightUpward()
        elif cmd=='fld':
            robotFace.leftDownward()
        elif cmd=='frd':
            robotFace.rightDownward()

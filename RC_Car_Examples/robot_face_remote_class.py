from robot_face_class import RobotFace

class RobotFaceRemote:
    def __init__(self):
        self.robotFace=RobotFace()    
    
    def control(self,cmd):
        if cmd=='fl':
            self.robotFace.left()
        elif cmd=='fr':
            self.robotFace.right()
        elif cmd=='ff':
            self.robotFace.forward()
        elif cmd=='fu':
            self.robotFace.upward()
        elif cmd=='fd':
            self.robotFace.downward()
        elif cmd=='flu':
            self.robotFace.leftUpward()
        elif cmd=='fru':
            self.robotFace.rightUpward()
        elif cmd=='fld':
            self.robotFace.leftDownward()
        elif cmd=='frd':
            self.robotFace.rightDownward()

if __name__=='__main__':
    
    robotFaceRemote=RobotFaceRemote()

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
        
        robotFaceRemote.control(cmd)

        
        
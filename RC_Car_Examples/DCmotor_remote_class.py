from DCmotor_class import DCMotor

class DCMotorRemote:
    def __init__(self):
        self.dcMotor=DCMotor(1,0)
        self.driving='stop'
    def control(self, cmd='s'):
        if cmd=='f':
            self.driving='forward'
        elif cmd=='b':        
            self.driving='backward'
        elif cmd=='s':
            self.driving='stop'
        print(f'driving {self.driving}!')
        if self.driving=='forward':
            self.dcMotor.rotateForward()
        elif self.driving=='backward':
            self.dcMotor.rotateBackward()
        else:
            self.dcMotor.stop()
if __name__=='__main__':
    dcMotorRemote=DCMotorRemote()
    while True:
        cmd=input("f:forward, s:stop, b:backward >> ")
        print(cmd)
        dcMotorRemote.control(cmd)
        
    
    
    

class RCCar:
    def __init__(self, dcMotor, steeringMotor):
        self.dcMotor=dcMotor
        self.steeringMotor=steeringMotor
    
    def goForward(self):
        self.dcMotor.rotateForward()
        self.steeringMotor.faceForward()
    def goForwardLeft(self):
        self.dcMotor.rotateForward()
        self.steeringMotor.turnLeft()
    def goForwardRight(self):
        self.dcMotor.rotateForward()
        self.steeringMotor.turnRight()
    def goBackward(self):
        self.dcMotor.rotateBackward()
        self.steeringMotor.faceForward()
    def goBackwardLeft(self):
        self.dcMotor.rotateBackward()
        self.steeringMotor.turnLeft()
    def goBackwardRight(self):
        self.dcMotor.rotateBackward()
        self.steeringMotor.turnRight()
    def stop(self):
        self.dcMotor.stop()
        self.steeringMotor.faceForward()
    
if __name__=='__main__':
    
    from _02_dc_motor import DCMotor
    from _13_steering_motor import SteeringMotor
    import time    
    
    dcMotor=DCMotor(1,0)
    steeringMotor=SteeringMotor(7)
    
    rcCar=RCCar(dcMotor,steeringMotor)
    
    rcCar.goForward()
    time.sleep(3)
    
    rcCar.goForwardLeft()
    time.sleep(3)
    
    rcCar.goForwardRight()
    time.sleep(3)
    
    rcCar.stop()
    time.sleep(3)
    
    rcCar.goBackward()
    time.sleep(3)
    
    rcCar.goBackwardLeft()
    time.sleep(3)
    
    rcCar.goBackwardRight()
    time.sleep(3)
    
    rcCar.stop()
    


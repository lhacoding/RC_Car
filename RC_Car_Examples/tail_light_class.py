from machine import Pin
from neopixel import NeoPixel
import time

class TailLight:
    PIXEL_PIN = 3
    PIXEL_COUNT = 36
    
    def __init__(self):
        self.pin = Pin(self.PIXEL_PIN, Pin.OUT)
        self.np = NeoPixel(self.pin, self.PIXEL_COUNT)

    def powerOff(self):
        for i in range(len(self.np)):
            self.np[i] = (0, 0, 0)
        self.np.write()
    
    def powerOn(self):
        for i in range(len(self.np)):
            self.np[i] = (13, 0, 0)  
        self.np.write()
    
    def powerOnAnimation(self, color):
        for i in range(len(self.np)):
            if i >= 1:
                self.np[i - 1] = (0, 0, 0)
            self.np[i] = color
            self.np.write()
            time.sleep(0.05)
        self.np[i] = (0, 0, 0)
        self.np.write()
    
    def powerOnAnimation2(self, color):
        for i in range(len(self.np) // 2):
            if i >= 1:
                self.np[i - 1] = (0, 0, 0)
                self.np[len(self.np) - 1 - (i - 1)] = (0, 0, 0)
            self.np[i] = color
            self.np[len(self.np) - 1 - i] = color
            self.np.write()
            time.sleep(0.05)
        self.np[i] = (0, 0, 0)
        self.np[len(self.np) - 1 - i] = (0, 0, 0)
        self.np.write()
        
    def powerOnAnimation3(self, color):
        self.powerOnAnimation2(color)
        numPixels = len(self.np)
        for i in range(numPixels // 2, numPixels):
            self.np[i] = color
            self.np[numPixels - 1 - i] = color
            self.np.write()
            time.sleep(0.05)
        
    def powerOnAnimation4(self, color):
        self.powerOnAnimation3(color)
        color = (13, 0, 0)  
        numPixels = len(self.np)
        for i in range(numPixels // 2, numPixels):
            self.np[i] = color
            self.np[numPixels - 1 - i] = color
            self.np.write()
            time.sleep(0.05)
            
    def powerOnAnimation5(self, color):
        self.powerOnAnimation4(color)
        for br in range(255, 15, -5):
            for i in range(len(self.np)):
                self.np[i] = (int(br * 0.05), 0, 0)  
            self.np.write()
            time.sleep(0.08)
            
    def powerOnBrake(self):
        for i in range(len(self.np)):
            self.np[i] = (64, 0, 0)  
        self.np.write()
            
    def leftTurnSignal(self):
        self.powerOff()
        numPixels = len(self.np)
        for i in range(numPixels // 4, numPixels):
            self.np[i] = (13, 0, 0)  
        self.np.write()
        time.sleep(0.1)
        for i in range(numPixels // 4 - 1, -1, -1):
            self.np[i] = (13, 13, 0)  
            self.np.write()
            time.sleep(0.1)        
    
    def rightTurnSignal(self):
        self.powerOff()
        numPixels = len(self.np)
        for i in range(numPixels // 4 * 3):
            self.np[i] = (13, 0, 0)  
        self.np.write()
        time.sleep(0.1)
        for i in range(numPixels // 4 * 3, numPixels):
            self.np[i] = (13, 13, 0)  
            self.np.write()
            time.sleep(0.1)
    
    def leftTurnSignalBrake(self):
        self.powerOff()
        numPixels = len(self.np)
        for i in range(numPixels // 4, numPixels):
            self.np[i] = (64, 0, 0)  
        self.np.write()
        time.sleep(0.1)
        for i in range(numPixels // 4 - 1, -1, -1):
            self.np[i] = (13, 13, 0)  
            self.np.write()
            time.sleep(0.1)
        
    def rightTurnSignalBrake(self):
        self.powerOff()
        numPixels = len(self.np)
        for i in range(numPixels // 4 * 3):
            self.np[i] = (64, 0, 0)  
        self.np.write()
        time.sleep(0.1)
        for i in range(numPixels // 4 * 3, numPixels):
            self.np[i] = (13, 13, 0)  
            self.np.write()
            time.sleep(0.1)
        
    def hazardLight(self):
        self.powerOff()
        numPixels = len(self.np)
        for i in range(numPixels // 4, numPixels // 4 * 3):
            self.np[i] = (13, 0, 0)  
        self.np.write()
        time.sleep(0.1)
        
        left = numPixels // 4 - 1
        for right in range(numPixels // 4 * 3, numPixels):
            self.np[right] = (13, 13, 0)  
            self.np[left] = (13, 13, 0)  
            self.np.write()
            time.sleep(0.1)
            left -= 1
            
    def hazardLightBrake(self):
        self.powerOff()
        numPixels = len(self.np)
        for i in range(numPixels // 4, numPixels // 4 * 3):
            self.np[i] = (64, 0, 0)  
        self.np.write()
        time.sleep(0.1)
        
        left = numPixels // 4 - 1
        for right in range(numPixels // 4 * 3, numPixels):
            self.np[right] = (13, 13, 0)  
            self.np[left] = (13, 13, 0)  
            self.np.write()
            time.sleep(0.1)
            left -= 1

    def reverseLight(self):
        for i in range(len(self.np)):
            self.np[i] = (13, 13, 13)  
        self.np.write()
        
    def reverseLightBrake(self):
        self.powerOnBrake()            

if __name__ == '__main__':
    
    tail_light = TailLight()
    
    tail_light.powerOff()
    time.sleep(1)
    
    cmd_menu = '''
        1: 자동차 시동 걸기
        2: 브레이크
        3: 좌이동 깜빡이
        4: 우이동 깜빡이
        5: 좌이동 브레이크
        6: 우이동 브레이크
        7: 비상 깜빡이
        8: 비상 깜빡이 브레이크
        9: 후진하기
        0: 후진 중 브레이크
        q: 종료 
        >> '''
    
    while True:
        cmd = input(cmd_menu)
        print(cmd)
        
        if(cmd == '1'):
            tail_light.powerOnAnimation5((13, 0, 0))  
        elif(cmd == '2'):
            for i in range(2):
                tail_light.powerOn()
                time.sleep(1)
                tail_light.powerOnBrake()
                time.sleep(1)
            tail_light.powerOn()
        elif(cmd == '3'):
            for i in range(5):
                tail_light.leftTurnSignal()
            tail_light.powerOn()
        elif(cmd == '4'):
            for i in range(5):
                tail_light.rightTurnSignal()
            tail_light.powerOn()
        elif(cmd == '5'):
            for i in range(2):
                tail_light.leftTurnSignal()
            for i in range(2):
                tail_light.leftTurnSignalBrake()
            for i in range(2):
                tail_light.leftTurnSignal()
            tail_light.powerOn()
        elif(cmd == '6'):
            for i in range(2):
                tail_light.rightTurnSignal()
            for i in range(2):
                tail_light.rightTurnSignalBrake()
            for i in range(2):
                tail_light.rightTurnSignal()
            tail_light.powerOn()
        elif(cmd == '7'):
            for i in range(5):
                tail_light.hazardLight()
            tail_light.powerOn()
        elif(cmd == '8'):
            for i in range(2):
                tail_light.hazardLight()
            for i in range(2):
                tail_light.hazardLightBrake()
            for i in range(2):
                tail_light.hazardLight()
            tail_light.powerOn()
        elif(cmd == '9'):
            tail_light.powerOn()
            time.sleep(1)
            tail_light.reverseLight()
            time.sleep(1)
        elif(cmd == '0'):
            tail_light.reverseLightBrake()
            time.sleep(1)
            tail_light.powerOn()
        elif(cmd == 'q'): 
            tail_light.powerOff()
            print("프로그램을 종료합니다.")
            break

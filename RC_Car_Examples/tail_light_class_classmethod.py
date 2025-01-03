from machine import Pin
from neopixel import NeoPixel
import time

class TailLight:
    PIXEL_PIN = 3
    PIXEL_COUNT = 36
    
    @classmethod
    def begin(cls):
        pin = Pin(cls.PIXEL_PIN, Pin.OUT)
        cls.np = NeoPixel(pin, cls.PIXEL_COUNT)
    
    @classmethod
    def powerOff(cls):
        for i in range(len(cls.np)):
            cls.np[i] = (0, 0, 0)
        cls.np.write()
    
    @classmethod
    def powerOn(cls):
        for i in range(len(cls.np)):
            cls.np[i] = (13, 0, 0)  # 5% 밝기 빨간색
        cls.np.write()
    
    @classmethod
    def powerOnAnimation(cls, color):
        for i in range(len(cls.np)):
            if i >= 1:
                cls.np[i - 1] = (0, 0, 0)
            cls.np[i] = color
            cls.np.write()
            time.sleep(0.05)
        cls.np[i] = (0, 0, 0)
        cls.np.write()
    
    @classmethod
    def powerOnAnimation2(cls, color):
        for i in range(len(cls.np) // 2):
            if i >= 1:
                cls.np[i - 1] = (0, 0, 0)
                cls.np[len(cls.np) - 1 - (i - 1)] = (0, 0, 0)
            cls.np[i] = color
            cls.np[len(cls.np) - 1 - i] = color
            cls.np.write()
            time.sleep(0.05)
        cls.np[i] = (0, 0, 0)
        cls.np[len(cls.np) - 1 - i] = (0, 0, 0)
        cls.np.write()
        
    @classmethod
    def powerOnAnimation3(cls, color):
        cls.powerOnAnimation2(color)
        numPixels = len(cls.np)
        for i in range(numPixels // 2, numPixels):
            cls.np[i] = color
            cls.np[numPixels - 1 - i] = color
            cls.np.write()
            time.sleep(0.05)
        
    @classmethod
    def powerOnAnimation4(cls, color):
        cls.powerOnAnimation3(color)
        color = (13, 0, 0)  # 5% 밝기 빨간색
        numPixels = len(cls.np)
        for i in range(numPixels // 2, numPixels):
            cls.np[i] = color
            cls.np[numPixels - 1 - i] = color
            cls.np.write()
            time.sleep(0.05)
            
    @classmethod
    def powerOnAnimation5(cls, color):
        cls.powerOnAnimation4(color)
        for br in range(255, 15, -5):
            for i in range(len(cls.np)):
                cls.np[i] = (int(br * 0.05), 0, 0)  # 5% 밝기 빨간색
            cls.np.write()
            time.sleep(0.08)
            
    @classmethod
    def powerOnBrake(cls):
        for i in range(len(cls.np)):
            cls.np[i] = (13, 0, 0)  
        cls.np.write()
            
    @classmethod
    def leftTurnSignal(cls):
        cls.powerOff()
        numPixels = len(cls.np)
        for i in range(numPixels // 4, numPixels):
            cls.np[i] = (13, 0, 0)  
        cls.np.write()
        time.sleep(0.1)
        for i in range(numPixels // 4 - 1, -1, -1):
            cls.np[i] = (13, 13, 0)  
            cls.np.write()
            time.sleep(0.1)        
    
    @classmethod
    def rightTurnSignal(cls):
        cls.powerOff()
        numPixels = len(cls.np)
        for i in range(numPixels // 4 * 3):
            cls.np[i] = (13, 0, 0)  
        cls.np.write()
        time.sleep(0.1)
        for i in range(numPixels // 4 * 3, numPixels):
            cls.np[i] = (13, 13, 0)  
            cls.np.write()
            time.sleep(0.1)
    
    @classmethod
    def leftTurnSignalBrake(cls):
        cls.powerOff()
        numPixels = len(cls.np)
        for i in range(numPixels // 4, numPixels):
            cls.np[i] = (64, 0, 0)  
        cls.np.write()
        time.sleep(0.1)
        for i in range(numPixels // 4 - 1, -1, -1):
            cls.np[i] = (13, 13, 0)  
            cls.np.write()
            time.sleep(0.1)
        
    @classmethod
    def rightTurnSignalBrake(cls):
        cls.powerOff()
        numPixels = len(cls.np)
        for i in range(numPixels // 4 * 3):
            cls.np[i] = (64, 0, 0)  
        cls.np.write()
        time.sleep(0.1)
        for i in range(numPixels // 4 * 3, numPixels):
            cls.np[i] = (13, 13, 0)  
            cls.np.write()
            time.sleep(0.1)
        
    @classmethod
    def hazardLight(cls):
        cls.powerOff()
        numPixels = len(cls.np)
        for i in range(numPixels // 4, numPixels // 4 * 3):
            cls.np[i] = (13, 0, 0)  
        cls.np.write()
        time.sleep(0.1)
        
        left = numPixels // 4 - 1
        for right in range(numPixels // 4 * 3, numPixels):
            cls.np[right] = (13, 13, 0)  
            cls.np[left] = (13, 13, 0)  
            cls.np.write()
            time.sleep(0.1)
            left -= 1
            
    @classmethod
    def hazardLightBrake(cls):
        cls.powerOff()
        numPixels = len(cls.np)
        for i in range(numPixels // 4, numPixels // 4 * 3):
            cls.np[i] = (64, 0, 0)  
        cls.np.write()
        time.sleep(0.1)
        
        left = numPixels // 4 - 1
        for right in range(numPixels // 4 * 3, numPixels):
            cls.np[right] = (13, 13, 0)  
            cls.np[left] = (13, 13, 0)  
            cls.np.write()
            time.sleep(0.1)
            left -= 1

    @classmethod
    def reverseLight(cls):
        for i in range(len(cls.np)):
            cls.np[i] = (13, 13, 13)  
        cls.np.write()
        
    @classmethod
    def reverseLightBrake(cls):
        cls.powerOnBrake()            

if __name__ == '__main__':
    
    TailLight.begin()
    
    TailLight.powerOff()
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
            TailLight.powerOnAnimation5((13, 0, 0))  
        elif(cmd == '2'):
            for i in range(2):
                TailLight.powerOn()
                time.sleep(1)
                TailLight.powerOnBrake()
                time.sleep(1)
            TailLight.powerOn()
        elif(cmd == '3'):
            for i in range(5):
                TailLight.leftTurnSignal()
            TailLight.powerOn()
        elif(cmd == '4'):
            for i in range(5):
                TailLight.rightTurnSignal()
            TailLight.powerOn()
        elif(cmd == '5'):
            for i in range(2):
                TailLight.leftTurnSignal()
            for i in range(2):
                TailLight.leftTurnSignalBrake()
            for i in range(2):
                TailLight.leftTurnSignal()
            TailLight.powerOn()
        elif(cmd == '6'):
            for i in range(2):
                TailLight.rightTurnSignal()
            for i in range(2):
                TailLight.rightTurnSignalBrake()
            for i in range(2):
                TailLight.rightTurnSignal()
            TailLight.powerOn()
        elif(cmd == '7'):
            for i in range(5):
                TailLight.hazardLight()
            TailLight.powerOn()
        elif(cmd == '8'):
            for i in range(2):
                TailLight.hazardLight()
            for i in range(2):
                TailLight.hazardLightBrake()
            for i in range(2):
                TailLight.hazardLight()
            TailLight.powerOn()
        elif(cmd == '9'):
            TailLight.powerOn()
            time.sleep(1)
            TailLight.reverseLight()
            time.sleep(1)
        elif(cmd == '0'):
            TailLight.reverseLightBrake()
            time.sleep(1)
            TailLight.powerOn()
        elif(cmd == 'q'):  
            TailLight.powerOff()
            print("LED가 꺼졌습니다. 프로그램을 종료합니다.")
            break

from tail_light_class import TailLight
import time

tail_light = TailLight()
tail_light.powerOff()

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
    
    if(cmd == '1'):    # 자동차 시동 걸기
        tail_light.powerOnAnimation5((13, 0, 0))  
    elif(cmd == '2'):  # 브레이크
        for i in range(2):
            tail_light.powerOn()
            time.sleep(1)
            tail_light.powerOnBrake()
            time.sleep(1)
        tail_light.powerOn()
    elif(cmd == '3'):  # 좌이동 깜빡이
        for i in range(5):
            tail_light.leftTurnSignal()
        tail_light.powerOn()
    elif(cmd == '4'):  # 우이동 깜빡이
        for i in range(5):
            tail_light.rightTurnSignal()
        tail_light.powerOn()
    elif(cmd == '5'):  # 좌이동 브레이크
        for i in range(2):
            tail_light.leftTurnSignal()
        for i in range(2):
            tail_light.leftTurnSignalBrake()
        for i in range(2):
            tail_light.leftTurnSignal()
        tail_light.powerOn()
    elif(cmd == '6'):  # 우이동 브레이크
        for i in range(2):
            tail_light.rightTurnSignal()
        for i in range(2):
            tail_light.rightTurnSignalBrake()
        for i in range(2):
            tail_light.rightTurnSignal()
        tail_light.powerOn()
    elif(cmd == '7'):  # 비상 깜빡이
        for i in range(5):
            tail_light.hazardLight()
        tail_light.powerOn()
    elif(cmd == '8'):  # 비상 깜빡이 브레이크
        for i in range(2):
            tail_light.hazardLight()
        for i in range(2):
            tail_light.hazardLightBrake()
        for i in range(2):
            tail_light.hazardLight()
        tail_light.powerOn()
    elif(cmd == '9'):  # 후진하기
        tail_light.powerOn()
        time.sleep(1)
        tail_light.reverseLight()
        time.sleep(1)
    elif(cmd == '0'):  # 후진 중 브레이크
        tail_light.reverseLightBrake()
        time.sleep(1)
        tail_light.powerOn()
    elif(cmd == 'q'):  # 'q'를 눌렀을 때 LED 끄고 종료
        tail_light.powerOff()
        print("프로그램을 종료합니다.")
        break

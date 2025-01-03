from servo_all_class2 import ServoMotor

steeringMotorRemote=ServoMotor(7)

try:
    while True:
        cmd = input('left:l, middle:m, right:r >> ')
        print(cmd)
        if cmd == 'q':
            break
        steeringMotorRemote.control(cmd)
        
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")

finally:
    steeringMotorRemote.control('m')
    
    
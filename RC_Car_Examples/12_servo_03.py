from servo_steering_remote_class import SteeringMotorRemote

steeringMotorRemote=SteeringMotorRemote()

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
    
    
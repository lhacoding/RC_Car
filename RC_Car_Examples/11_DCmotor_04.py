from DCmotor_remote_class import DCMotorRemote

dcMotorRemote=DCMotorRemote()

try:
    while True:
        cmd=input("f:forward, s:stop, b:backward >> ")
        print(cmd)
        if cmd == 'q':  
            print("Exiting...")
            break
        dcMotorRemote.control(cmd)
    
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
finally:
    dcMotorRemote.control('s')


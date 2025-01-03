from robot_face_remote_class import RobotFaceRemote

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
        
try:    
    while True:
        cmd = input(cmd_menu)
        print(cmd)
        if cmd == 'q':
            break
        robotFaceRemote.control(cmd)
        
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")

finally:
    robotFaceRemote.control('m')
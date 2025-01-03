from DCmotor_class import DCMotor
dcMotor=DCMotor(1,0)
driving='stop'
try:
    while True:
        cmd=input("f:forward, s:stop, b:backward >> ")
        print(cmd)
        if cmd=='f':
            driving='forward'
        elif cmd=='b':        
            driving='backward'
        elif cmd=='s':
            driving='stop'
        print(f'driving {driving}!')
        if driving=='forward':
            dcMotor.rotateForward()
        elif driving=='backward':
            dcMotor.rotateBackward()
        else:
            dcMotor.stop()
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
finally:
    dcMotor.stop()
    
    
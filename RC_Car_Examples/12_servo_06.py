from servo_class import ServoMotor

servoLR=ServoMotor(18)
servoUD=ServoMotor(19)

servoLR.setAngle(90)
servoUD.setAngle(90)

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
while True:
    cmd = input(cmd_menu)
    print(cmd)
    
    if cmd=='fl':
        servoLR.setAngle(120)
        servoUD.setAngle(90)
    elif cmd=='fr':
        servoLR.setAngle(60)
        servoUD.setAngle(90)
    elif cmd=='ff':
        servoLR.setAngle(90)
        servoUD.setAngle(90)
    elif cmd=='fu':
        servoLR.setAngle(90)
        servoUD.setAngle(60)
    elif cmd=='fd':
        servoLR.setAngle(90)
        servoUD.setAngle(120)
    elif cmd=='flu':
        servoLR.setAngle(120)
        servoUD.setAngle(60)
    elif cmd=='fru':
        servoLR.setAngle(60)
        servoUD.setAngle(60)
    elif cmd=='fld':
        servoLR.setAngle(120)
        servoUD.setAngle(120)
    elif cmd=='frd':
        servoLR.setAngle(60)
        servoUD.setAngle(120)
        
        
        
        
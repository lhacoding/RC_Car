import time

def t1():
    print("t1")
    time.sleep(0.5)
def t2():
    print("t2")
    time.sleep(0.5)
    
try:
    while True:
        t1()
        t2()
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    

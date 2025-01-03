import _thread
import time
def t1():
    while True:  
        print("\tt1")              # \t : tap간격 띄우기
        time.sleep(0.5)
# 쓰레드 시작
_thread.start_new_thread(t1, ())   # t1함수에 매개변수 없으므로 ()빈 튜플 넣음
try:
    while True:
        print("t2")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    
    
    

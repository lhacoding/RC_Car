import _thread
import time
def t1():
    while True:
        print("\tt1")
        time.sleep(0.5)  
_thread.start_new_thread(t1, ())
try:
    while True:
        userInput = input()   # 키보드로 입력받기
        print(userInput)
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    
    
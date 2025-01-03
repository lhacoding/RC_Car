import _thread
import time
running = True            # 쓰레드 실행 제어 플래그
def t1():
    while running:
        print("\tt1")
        time.sleep(0.2)
    print("Thread 종료")
_thread.start_new_thread(t1, ())
try:
    while True:
        print("main")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    running = False      # 쓰레드 종료 요청
    time.sleep(2)        # 쓰레드 종료 대기
finally:
    print("프로그램 종료 완료")



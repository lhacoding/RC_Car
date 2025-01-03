from machine import Pin
import time

# 시계방향 회전
C1,C2=Pin(1,Pin.OUT),Pin(0,Pin.OUT)  # 핀 할당

# 전진
C1.value(1)
C2.value(0)
time.sleep(1)
# 정지
C1.value(0)
C2.value(0)
time.sleep(1)
# 후진
C1.value(0)
C2.value(1)
time.sleep(1)
# 정지
C1.value(0)
C2.value(0)


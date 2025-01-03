from machine import Pin,time_pulse_us
import time

SOUND_SPEED=340                                # 음속 (m/s)
TRIG_PULSE_DURATION_US=10                      # 트리거 펄스의 지속 시간 (마이크로초)

# 초음파 센서의 트리거 핀 및 에코 핀 설정
trigPin=Pin(15,Pin.OUT)                        # GPIO 15번 핀을 출력 모드로 설정
echoPin=Pin(14,Pin.IN)                         # GPIO 14번 핀을 입력 모드로 설정
try:
    while True:
        # 초음파 센서 트리거 신호 초기화
        trigPin.value(0)                       # 트리거 핀을 0으로 설정 (LOW 상태)
        time.sleep_us(5)                       # 안정화를 위해 5마이크로초 대기
        # 초음파 센서 트리거 신호 발생
        trigPin.value(1)                       # 트리거 핀을 1로 설정 (HIGH 상태)
        time.sleep_us(TRIG_PULSE_DURATION_US)  # 트리거 펄스를 10마이크로초 동안 유지
        trigPin.value(0)                       # 트리거 핀을 다시 0으로 설정
        # 에코 핀에서 신호 지속 시간 측정
        ultrasonic_duration=time_pulse_us(echoPin,1,30000) # 초음파 반사 시간 측정 (최대 30ms 대기)
        # 거리 계산 (cm 단위)
        distance_cm=SOUND_SPEED*ultrasonic_duration/20000  # 음속과 반사 시간으로 거리 계산
    
        print(f'Distance : {distance_cm} cm')   # 측정된 거리를 출력
        time.sleep_ms(500)                      # 500ms 대기 후 다음 측정 진행

except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")
    
    
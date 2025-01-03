from tail_light_class import TailLight
import time

tail_light = TailLight()
tail_light.powerOff()

# 자동차 시동 걸기
tail_light.powerOnAnimation5((13, 0, 0))
# 브레이크
tail_light.powerOn()
time.sleep(1)
tail_light.powerOnBrake()
time.sleep(1)
tail_light.powerOn()
time.sleep(1)
tail_light.powerOff()


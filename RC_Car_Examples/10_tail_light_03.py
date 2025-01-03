from tail_light_class import TailLight
import time

tail_light = TailLight()
tail_light.powerOff()

# 비상 깜빡이
tail_light.hazardLight()
tail_light.powerOn()
# 비상 깜빡이 브레이크
tail_light.hazardLight()
tail_light.hazardLightBrake()
tail_light.hazardLight()
tail_light.powerOn()
# 후진하기
tail_light.powerOn()
time.sleep(1)
tail_light.reverseLight()
time.sleep(1)
# 후진 중 브레이크
tail_light.reverseLightBrake()
time.sleep(1)
tail_light.powerOn()
tail_light.powerOff()
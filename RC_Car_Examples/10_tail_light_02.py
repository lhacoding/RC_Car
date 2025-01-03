from tail_light_class import TailLight
import time

tail_light = TailLight()
tail_light.powerOff()

# 좌이동 깜빡이
tail_light.leftTurnSignal()
tail_light.powerOn()
# 우이동 깜빡이
tail_light.rightTurnSignal()
tail_light.powerOn()
# 좌이동 브레이크
tail_light.leftTurnSignal()
tail_light.leftTurnSignalBrake()
tail_light.leftTurnSignal()
tail_light.powerOn()
# 우이동 브레이크
tail_light.rightTurnSignal()
tail_light.rightTurnSignalBrake()
tail_light.rightTurnSignal()
tail_light.powerOn()
tail_light.powerOff()
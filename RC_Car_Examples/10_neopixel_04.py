from machine import Pin
from neopixel import NeoPixel
import time

# 5% 밝기로 설정된 무지개 색
RAINBOW_COLORS = [
    (13, 0, 0),      # 빨간색
    (13, 6, 0),      # 주황색
    (13, 13, 0),     # 노란색
    (0, 13, 0),      # 초록색
    (0, 0, 13),      # 파란색
    (6, 0, 13),      # 남색
    (12, 0, 13)      # 보라색
]

PIXEL_PIN = 3
PIXEL_COUNT = 36

pin = Pin(PIXEL_PIN, Pin.OUT)
np = NeoPixel(pin, PIXEL_COUNT)

for cnt in range(2):
    for color in RAINBOW_COLORS:
        for i in range(PIXEL_COUNT):
            np[i] = color
        np.write()
        time.sleep(0.3)
np.fill((0,0,0))
np.write()


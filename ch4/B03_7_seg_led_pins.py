# -*- coding:utf-8 -*-
"""
7 segment LED (Common-Cathode (CC))

"""
from __future__ import annotations

import time, RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#      [a,  b,  c,  d,  e, f,  g, dp]
seg7 = [5, 33, 19, 15, 13, 7, 21, 11]
# scan =[23, 31, 29, 3]
for x in seg7:
    GPIO.setup(x, GPIO.OUT)

# for x in scan:
#     GPIO.setup(x, GPIO.OUT)

for x in seg7:
    GPIO.output(x, 0)

try:
    while True:
        for x in seg7:
            time.sleep(0.3)
            GPIO.output(x, 1)
        time.sleep(0.6)
        for x in seg7:
            time.sleep(0.3)
            GPIO.output(x, 0)
        time.sleep(1.0)

except KeyboardInterrupt:
    for x in seg7:
        GPIO.output(x, 0)

# for x in range(4):
#     GPIO.output(scan[x], 1)
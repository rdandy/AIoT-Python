# -*- coding:utf-8 -*-
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

for x in range(len(seg7)):
    GPIO.output(seg7[x], 1)

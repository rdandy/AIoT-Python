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
#      [   0,    1,    2,    3,    4,    5,    6,    7,    8,    9,    .,     ]
font = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x27, 0x7F, 0x6F, 0x80, 0x00]


def out(n):
    for x in range(len(seg7)):
      if n % 2 == 1:
         GPIO.output(seg7[x], 1)
      else:
         GPIO.output(seg7[x], 0)
      n = n // 2

for x in seg7:
    GPIO.setup(x, GPIO.OUT)

# for x in scan:
#     GPIO.setup(x, GPIO.OUT)

for x in range(len(seg7)):
    GPIO.output(seg7[x], 0)

try:
    while True:
        # for x in range(len(seg7)):
        #     GPIO.output(seg7[x], 1)
        # for x in range(4):
        #     GPIO.output(scan[x], 1)
        for x in range(len(font)):
            out(font[x])
            time.sleep(0.5)
except KeyboardInterrupt:
    for x in range(len(seg7)):
        GPIO.output(seg7[x], 0)

# for x in range(4):
#     GPIO.output(scan[x], 1)
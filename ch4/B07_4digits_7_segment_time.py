# -*- coding:utf-8 -*-
"""
4 digits 7 segment LED (3461BS Common-Cathode (CC))
show system time
"""
from __future__ import annotations
import time, RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
seg7 = [5, 7, 11, 13, 15, 19, 21, 33]
scan = [3, 23, 29, 31]
font = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x27, 0x7F, 0x6F, 0x00]
delaytime = 0.0001
for x in seg7:
    GPIO.setup(x, GPIO.OUT)
for x in scan:
    GPIO.setup(x, GPIO.OUT)


def out(n):
  for x in seg7:
      if n % 2 == 1:
         GPIO.output(x, 0)
      else:
         GPIO.output(x, 1)
      n = n // 2

try:
    while True:
        ss = int(time.strftime("%S"))
        mm = int(time.strftime("%M"))

        out(font[ss % 10])
        GPIO.output(scan[3], 1)
        time.sleep(delaytime)
        GPIO.output(scan[3], 0)

        temp = ss // 10
        out(font[temp % 10])
        GPIO.output(scan[2], 1)
        time.sleep(delaytime)
        GPIO.output(scan[2], 0)

        out(font[mm % 10] + 128)
        GPIO.output(scan[1], 1)
        time.sleep(delaytime)
        GPIO.output(scan[1], 0)

        temp = mm // 10
        out(font[temp % 10] + 128)
        GPIO.output(scan[0], 1)
        time.sleep(delaytime)
        GPIO.output(scan[0], 0)
except KeyboardInterrupt:
    for x in seg7:
        GPIO.output(x, 1)
    for x in scan:
        GPIO.output(x, 1)

# -*- coding:utf-8 -*-
"""
4 digits 7 segment LED (3461BS Common-Cathode (CC))
count from 0 to 9999
"""
from __future__ import annotations
import time, RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
seg7 = [5, 7, 11, 13, 15, 19, 21, 33]
scan = [3, 23, 29, 31]
font = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x27, 0x7F, 0x6F, 0x00]
cnt = 0
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
        while cnt <= 9999:
            for x in range(100):
                out(font[cnt % 10])
                GPIO.output(scan[3], 1)
                time.sleep(delaytime)
                GPIO.output(scan[3], 0)

                temp = cnt // 10
                out(font[temp % 10])
                GPIO.output(scan[2], 1)
                time.sleep(delaytime)
                GPIO.output(scan[2], 0)

                temp = temp // 10
                out(font[temp % 10])
                GPIO.output(scan[1], 1)
                time.sleep(delaytime)
                GPIO.output(scan[1], 0)

                temp = temp // 10
                out(font[temp % 10])
                GPIO.output(scan[0], 1)
                time.sleep(delaytime)
                GPIO.output(scan[0], 0)

            cnt = cnt + 1
            if cnt > 9999:
                cnt = 0
except KeyboardInterrupt:
    for x in seg7:
        GPIO.output(x, 1)
    for x in scan:
        GPIO.output(x, 1)
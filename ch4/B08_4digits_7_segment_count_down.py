# -*- coding:utf-8 -*-
"""
4 digits 7 segment LED (3461BS Common-Cathode (CC))
count down, push button to turn off the alarm
"""
from __future__ import annotations
import time, RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
seg7 = [5, 7, 11, 13, 15, 19, 21, 33]
scan = [3, 23, 29, 31]
alarm_pin = 35
turn_off_pin = 37
font = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x27, 0x7F, 0x6F, 0x00]
mm = int(input("Input start minute = "))
ss = int(input("\nInput start second = "))

delaytime = 0.0001
GPIO.setup(alarm_pin, GPIO.OUT)
GPIO.setup(turn_off_pin, GPIO.IN)
GPIO.output(alarm_pin, 0)
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
        for x in range(2000):
            out(font[ss % 10])

            GPIO.output(scan[3], 1)
            time.sleep(delaytime)
            GPIO.output(scan[3], 0)

            temp = int(ss / 10)
            out(font[temp % 10])
            GPIO.output(scan[2], 1)
            time.sleep(delaytime)
            GPIO.output(scan[2], 0)

            out(font[mm % 10] + 128)
            GPIO.output(scan[1], 1)
            time.sleep(delaytime)
            GPIO.output(scan[1], 0)

            temp = int(mm / 10)
            out(font[temp % 10] + 128)
            GPIO.output(scan[0], 1)
            time.sleep(delaytime)
            GPIO.output(scan[0], 0)
        if mm == 0 and ss == 0:
            GPIO.output(alarm_pin, 1)
        elif ss > 0:
            ss = ss - 1
        else:
            ss = 59
            mm = mm - 1
        if GPIO.input(turn_off_pin) == 0:
            GPIO.output(alarm_pin, 0)
            break
except KeyboardInterrupt:
    GPIO.output(alarm_pin, 0)

for x in seg7:
    GPIO.output(x, 1)
for x in scan:
    GPIO.output(x, 1)

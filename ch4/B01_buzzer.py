# -*- coding:utf-8 -*-
from __future__ import annotations

import RPi.GPIO as GPIO

PIN_OUT = 35
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_OUT, GPIO.OUT)

while True:
    ans = int(input("選擇聲音輸出種類<1-4>,按0離開："))
    if ans == 0:
       GPIO.output(PIN_OUT, 0)
       break

    if ans == 1:
       for r in range(10000):
           for x in range(250):
               GPIO.output(PIN_OUT, 1)
           for x in range(250):
               GPIO.output(PIN_OUT, 0)

    if ans == 2:
       for r in range(10000):
           for x in range(250):
               GPIO.output(PIN_OUT, 1)
           for x in range(1000):
               GPIO.output(PIN_OUT, 0)

    if ans == 3:
       for r in range(10000):
           for x in range(1000):
               GPIO.output(PIN_OUT, 1)
           for x in range(250):
               GPIO.output(PIN_OUT, 0)

    if ans == 4:
       for r in range(10000):
           for x in range(500):
               GPIO.output(PIN_OUT, 1)
           for x in range(300):
               GPIO.output(PIN_OUT, 0)
# -*- coding:utf-8 -*-
from __future__ import annotations
import time, RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED_16 = 16
LED_15 = 15
LED_18 = 18
GPIO.setup(LED_16, GPIO.OUT)
GPIO.setup(LED_18, GPIO.OUT)
GPIO.setup(LED_15, GPIO.OUT)
p1 = GPIO.PWM(LED_16, 1000)
p2 = GPIO.PWM(LED_18, 10)
p3 = GPIO.PWM(LED_15, 50)

while True:
    for dc in range(1, 101, 5):
        p1.start(dc)
        p2.start(dc)
        p3.start(dc)
        time.sleep(0.2)
    time.sleep(0.2)

    for dc in range(100, 0, -10):
        if dc < 0:
            dc = 0
        p1.start(dc)
        p2.start(dc)
        p3.start(dc)
        time.sleep(0.2)
    time.sleep(0.4)
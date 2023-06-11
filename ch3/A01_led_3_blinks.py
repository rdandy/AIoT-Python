import time
import RPi.GPIO as GPIO 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)

# pin 15 is GPIO 22
PIN_15 = 15
GPIO.setup(PIN_15, GPIO.OUT)
# pin 16 is GPIO 23
PIN_16 = 16
GPIO.setup(PIN_16, GPIO.OUT)
# pin 18 is GPIO 24
PIN_18 = 18
GPIO.setup(PIN_18, GPIO.OUT)

delay_time = 0.2

while True:
   GPIO.output(PIN_15, 1)
   time.sleep(delay_time)
   GPIO.output(PIN_15, 0)
   time.sleep(delay_time)
   GPIO.output(PIN_16, 1)
   time.sleep(delay_time)
   GPIO.output(PIN_16, 0)
   time.sleep(delay_time)
   GPIO.output(PIN_18, 1)
   time.sleep(delay_time)
   GPIO.output(PIN_18, 0)
   time.sleep(delay_time)

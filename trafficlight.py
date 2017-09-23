#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

SleepTimeL = 1
pinList = [17, 27, 22]

# Setup
for pin in pinList:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def on(pin):
    GPIO.output(pin, GPIO.LOW)
    print(pin)
    time.sleep(SleepTimeL)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(SleepTimeL)

# Main loop
try:
    while True:
        [on(pin) for pin in pinList]
except KeyboardInterrupt:
    pass

GPIO.cleanup()

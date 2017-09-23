#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

SleepTimeL = input('fuck you, enter a #')
pinList = [17, 27, 22]

# Setup
for pin in pinList:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,1)

def on(pin):
    GPIO.output(pin,1)
    print([pin,' on'])
    print(GPIO.input(pin))
    time.sleep(SleepTimeL)
    GPIO.output(pin,0)
    print([pin,' off'])
    print(GPIO.input(pin))
    time.sleep(SleepTimeL)

# Main loop
try:
    while True:
        [on(pin) for pin in pinList]
except KeyboardInterrupt:
    pass

GPIO.cleanup()

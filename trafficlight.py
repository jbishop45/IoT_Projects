#!/usr/bin/python
import RPi.GPIO as GPIO
import time

SleepTimeL = 0.5
pinList = [17, 27, 22]


GPIO.setmode(GPIO.BCM)

# Setup
for pin in pinList: 
    GPIO.setup(pin, GPIO.OUT) 
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(SleepTimeL);
    GPIO.output(pin, GPIO.LOW)
    time.sleep(SleepTimeL);
    GPIO.output(pin, GPIO.HIGH)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(SleepTimeL);
def on(pin):
  GPIO.output(pin, GPIO.LOW)
  print(pin)
  time.sleep(SleepTimeL);
  GPIO.output(pin, GPIO.HIGH)  

# Main loop
try:
  while True:
    [on(pin) for pin in pinList]
except KeyboardInterrupt:
  pass

GPIO.cleanup()
import RPi.GPIO as GPIO            # import RPi.GPIO module 
import sys 
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

wait = input('fuck you, enter a #')


try:
    while True:
		GPIO.output(17, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
		sleep(wait)                   # wait a second
		GPIO.output(17, 0)         # set GPIO24 to 0/GPIO.LOW/False  
		sleep(0.1)                 # wait a second
		GPIO.output(27, 1)          
		sleep(wait)
		GPIO.output(27, 0)
		sleep(wait)
		GPIO.output(22, 1)
		sleep(wait)
		GPIO.output(22, 0)
		sleep(wait)



except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
	GPIO.cleanup()                 # resets all GPIO ports used by this program
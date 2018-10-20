import RPi.GPIO as GPIO            # import RPi.GPIO module 
import random
from time import sleep             # lets us have a delay  
GPIO.setwarnings(False) # Ignore warning
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)



#wait = input('fuck you, enter a nombre ')


try:
	while True:

		#if GPIO.input(2) == GPIO.HIGH:
		num = random.randint(1,3)
		interval = random.randint(1,15)
		if num == 1:
			GPIO.output(17, 1)          
			sleep(interval)
			GPIO.output(17, 0)
		if num == 2:
			GPIO.output(27, 1)          
			sleep(interval)
			GPIO.output(27, 0)
		if num == 3:
			GPIO.output(22, 1)          
			sleep(interval)
			GPIO.output(22, 0)



	
#		GPIO.output(17, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
#		sleep(wait)                   # wait a second
#		GPIO.output(17, 0)         # set GPIO24 to 0/GPIO.LOW/False  
#		sleep(0.1)                 # wait a second
#		GPIO.output(27, 1)          
#		sleep(wait)
#		GPIO.output(27, 0)
#		sleep(.1)
#		GPIO.output(22, 1)
#		sleep(wait)
#		GPIO.output(22, 0)
#		sleep(.1)



except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
	GPIO.cleanup()                 # resets all GPIO ports used by this program
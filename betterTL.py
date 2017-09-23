    import RPi.GPIO as GPIO            # import RPi.GPIO module  
    from time import sleep             # lets us have a delay  
    GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)  
      
    try:  
        while True:  
            GPIO.output(17, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
            sleep(2)                   # wait a second  
            GPIO.output(17, 0)         # set GPIO24 to 0/GPIO.LOW/False  
            sleep(0.5)                 # wait a second
            GPIO.output(27, 1)          
            sleep(2)
            GPIO.output(27, 0)
            sleep(0.5)
            GPIO.output(22, 1)
            sleep(2)
            GPIO.output(22, 0)
            sleep(0.5)
      
    except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
        GPIO.cleanup()                 # resets all GPIO ports used by this program  
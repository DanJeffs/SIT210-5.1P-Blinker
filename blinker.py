import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setwarnings(False)

try:
    while 1:
        GPIO.output(4,GPIO.HIGH)
        time.sleep(0.25)
	GPIO.output(4,GPIO.LOW)
	time.sleep(0.25)
except KeyboardInterrupt:
        GPIO.output(4,GPIO.LOW)

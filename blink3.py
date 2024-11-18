import RPi.GPIO as gpio
from time import sleep
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
pin = 18
bt  = 4
gpio.setup (pin, gpio.OUT)
gpio.setup (bt, gpio.IN)

def button(bt):
	if gpio.input(bt):
		gpio.output (pin, False)
		sleep(1)
		print ("desligado")
	else:
		gpio.output (pin, True)
		print ("ligado")
		sleep(1)
gpio.setup(bt,gpio.IN, gpio.PUD_UP)
gpio.add_event_detect(bt,gpio.BOTH,callback=button, bouncetime=200)
#gpio.add_event_detect(bt,gpio.RISING,callback=button, bouncetime=200)


try: 
	while 1: 
		pass 
except KeyboardInterrupt:
	gpio.cleanup()

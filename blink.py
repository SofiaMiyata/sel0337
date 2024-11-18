from gpiozero import LED
from time import sleep

pin = LED(18)

while 1:
	pin.on()
	print("ligeds")
	sleep (1)
	pin.off()
	print("desligeds")
	sleep(0.5)

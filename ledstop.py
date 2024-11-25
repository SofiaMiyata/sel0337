from gpiozero import LED
from time import sleep

pin = LED(18)

while True:
	pin.on()

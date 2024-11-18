import random
import threading
import RPi.GPIO as gpio
from time import sleep
from gpiozero import PWMLED

def blink3():
	gpio.setmode(gpio.BCM)
	pin = 21
	bt  = 4
	gpio.setup (pin, gpio.OUT)
	gpio.setup (bt, gpio.IN)

	def button(bt):
		if gpio.input(bt):
			gpio.output (pin, False)
			sleep(1)
			print ("Thread1: desligado")
		else:
			gpio.output (pin, True)
			print ("Thread1: ligado")
			sleep(1)
	gpio.setup(bt,gpio.IN, gpio.PUD_UP)
	gpio.add_event_detect(bt,gpio.BOTH,callback=button, bouncetime=200)
	#gpio.add_event_detect(bt,gpio.RISING,callback=button, bouncetime=200)


	try: 
		while 1: 
			pass 
	except KeyboardInterrupt:
		gpio.cleanup()

def pwm_led():
	led = PWMLED(26)

	while True:
		print ("Thread2: PWM begin")
		led.value = 0
		sleep(0.5)
		led.value = 0.25
		sleep(0.5)
		led.value = 0.5
		sleep(0.5)
		led.value = 1
		sleep(0.5)

if __name__ == '__main__':
	print("inicializado")
	# Cria e inicia as threads
	thread1 = threading.Thread(target=blink3)
	thread2 = threading.Thread(target=pwm_led)
	thread1.start() # Inicia a execução da primeira função em uma nova thread
	thread2.start() # Inicia a execução da segunda função em outra nova thread
	thread1.join() # Aguarda a conclusão da primeira thread
	thread2.join() # Aguarda a conclusão da segunda thread
try:
	while 1:
		pass
except KeyboardInterrupt:
	gpio.cleanup()

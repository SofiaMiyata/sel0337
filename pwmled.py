from gpiozero import PWMLED #importa o pwm da biblioteca gpiozero
from time import sleep  #Importa a função sleep da biblioteca time para criar a base de tempo 

led = PWMLED(18) 		#funcao que permite controlar o LED por PWM(com valores entre 0 e 1)

while True: # loop infinito
	led.value = 0 		# brilho do LED em 0%
	sleep(0.5)    		# brilho em 0% durante 0,5 segundos
	led.value = 0.25	#brilho em 25%
	sleep(0.5)			# brilho em 25% durante 0,5 segundos
	led.value = 0.5		#brilho em 50%
	sleep(0.5)			# brilho em 50% durante 0,5 segundos
	led.value = 1	     #brilho em 100%
	sleep(0.5)			# brilho em 100% durante 0,5 segundos

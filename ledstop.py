from gpiozero import LED #importa o pwm da biblioteca gpiozero
from time import sleep #Importa a função sleep da biblioteca time para criar a base de tempo 

pin = LED(18) #Define-se o pino do led como 18

while True: #Loop infinito
	pin.on()  #Permanece com o led aceso após pausar o serviço

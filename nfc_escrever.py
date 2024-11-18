
# Para descobrir qual a codificação da Tag com texto gravado anteriormente
from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
verde = 22
vermelho = 27
GPIO.setup (verde, GPIO.OUT)
GPIO.setup (vermelho, GPIO.OUT)

#desabilitar os avisos
GPIO.setwarnings(False)
#cria o objeto "leitor" para a instância "SimpleMFRC522" da biblioteca
leitor = SimpleMFRC522()
print("Aproxime a tag do leitor para leitura.")

while True: #loop
    #cria as variáveis "id" e "texto", e as atribui as leituras da id e do texto coletado da tag pelo leitor, respectivamente
    id,texto = leitor.read()
    print("ID: {}\nTexto: {}".format(id, texto)) #exibe as informações coletadas
    
    if (id == 82510128764):
        print ("Liberado!")
        GPIO.output (verde, True)
        GPIO.output (vermelho, False)
    else:
        print ("Acesso negado")
        GPIO.output (verde, False)
        GPIO.output (vermelho, True)

    sleep(3) #aguarda 3 segundos para nova leitura

try: 
	while 1: 
		pass 
except KeyboardInterrupt:
	GPIO.cleanup()


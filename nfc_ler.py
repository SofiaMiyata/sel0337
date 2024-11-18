#para gravação de texto na Tag
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
#desabilita os avisos
GPIO.setwarnings(False)
#cria o objeto "leitor" para a instância "SimpleMFRC522" da biblioteca
leitor = SimpleMFRC522()

# Definindo qual número USP será colocado na tag
flag = 0
while (flag == 0):
    x = input("Rafael -> 1; Sofia -> 2: ")
    if (x == "1" or x == "2"):
        flag = 1
    else:
        print ("Invalido")

#criacao da variavel que armazena o texto que será gravado na tag
if (x == "1"):
    texto = "13782435"

elif (x == "2"):
    texto = "11419414"

#escreve a tag assim que ela for aproximada do leitor, e informa a conclusão
print("Aproxime a tag do leitor para gravar.")
leitor.write(texto) #função que realiza a gravação do texto configurado
print("Concluído!")

try: 
	while 1: 
		pass 
except KeyboardInterrupt:
	GPIO.cleanup()

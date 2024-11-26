 e criand# SEL0337 Prática 5
### Sofia Yuka Lazzarini Miyata N° USP:11419414 
### Rafael Moura Zampirolli     N°USP:13782435

## Parte 1

Com o intuito de estudar a adição de uma unidade de  serviço personalizada, criou-se o _unit file_ para a execução do programa junto ao boot da raspberry pi. Após verificar o funcionamento do systemd pelo exemplo blink.sh, colocou-se um programa python no serviço. Para a prática utilizou-se `pwmled.py` com um PWM de 0%, 25%, 50% e 100% a cada 0,5 segundos, seguindo os comandos do roteiro da prática e criando _unit file_ `pwmled.service`, para especificar o serviço a ser utilizado e adicionado. 

![image](https://github.com/user-attachments/assets/10058596-4f0a-41ef-98f8-98d6378a4ea4)

Por ser um código python foi necessário colocar o próprio Python no serviço,  feita por meio de/bin/python , o qual coloca o python em execução também na inicialização.







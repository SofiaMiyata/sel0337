 e criand# SEL0337 Prática 5
### Sofia Yuka Lazzarini Miyata N° USP:11419414 
### Rafael Moura Zampirolli     N°USP:13782435

## Parte 1

Com o intuito de estudar a adição de uma unidade de  serviço personalizada, criou-se o _unit file_ para a execução do programa junto ao boot da raspberry pi. Após verificar o funcionamento do systemd pelo exemplo blink.sh, colocou-se um programa python no serviço. Para a prática utilizou-se `pwmled.py` com um PWM de 0%, 25%, 50% e 100% a cada 0,5 segundos, seguindo os comandos do roteiro da prática e criando _unit file_ `pwmled.service`, para especificar o serviço a ser utilizado e adicionado. 

![image](https://github.com/user-attachments/assets/10058596-4f0a-41ef-98f8-98d6378a4ea4)

Definiu-se em `[Unui]` a descrição do serviço como blink pwm e configurou a ordem do serviço. Em `[Service]`, configurou-se a execução do `pwmled.py` quando inicializar e a do `ledstop.py` quando pausar o serviço, por meio do `Execstop`, fazendo o LED permanecer aceso. Além disso, especifica-se o usuário que será acessado para esta execução. Por ser um código python foi necessário colocar o próprio Python no serviço,  feita por meio de `/bin/python` , indicando o caminho para a busca de bibliotecas do programa. Por último, em `[Install]` define-se comoo serviço se comporta na inicialização e o grupo alvo.
Copiou-se o arquivo acima para o diretório de serviços do systemd , por meio do comando `sudo cp pwmled.service /lib/systemd/system`, e inicializou-o por `sudo systemctl start pwmled`. Para habilitar o código na inicialização foi efetuando o `enable` por meio de `sudo systemctl enable pwmled`.
A figura abaixo mostra a montagem e a execução do pwm após reiniciar a Raspberry Pi.

![20241125_111542](https://github.com/user-attachments/assets/5acbe1d3-f1c9-4e2a-a850-5d773c4b922f)

Executando posteriormente o comando `sudo systemctl stop pwmled`, o LED permaneceu aceso no seu brilho máximo, mostrado na figura a seguir:

![20241125_111550](https://github.com/user-attachments/assets/15ef6f08-48fd-48fc-a294-d03a7d87f1f5)

## Parte 2

Para o prática com o GitHub, foram utulizados os comandos no terminal Linux e adicionou-se os códigos dos projetos anteriores ao respositório sel0337, incluinndo o `pwmled.py`, `ledstop.py` `pwmled.service`, além do txt contendo o `git log`.









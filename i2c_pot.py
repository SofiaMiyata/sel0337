from smbus import SMBus
from time import sleep

bus = SMBus(1)
while 1:
	data = bus.read_i2c_block_data(0x8, 0,2)
	value = data[0]*256+data[1]
	print(value)
	sleep(0.5)
	
	
	

 

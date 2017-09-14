#!usr/bin/python3
import random


c=["1","2","3"]

print("please select:")
print("1 rock")
print("2 paper")
print("3 scissor")

player = input("choose from 1-3:")
cpu=c[random.randint(0,2)]

print("cpu choose",cpu)

if (player==cpu):
		print("draw")

		
if player=='1':
	print("u choose rock")
	if(cpu==2):
			print("cpu wins")
		else:
			print("player wins")


if player ==3:
	print("u choose scisssor")
	sleep(2)
	if(cpu==2):
		print("u win!")

	else:
		print("u choose scisasor")
		sleep(2)
		print("cpu choose rock")
		print("u lose ,u never win")	
	

	  
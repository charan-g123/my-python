#!/usr/bin/python3
import random
count=0
r=0
while count<=100:
	roll=input("press r to roll the dice")
	if roll=="r":
		r=random.randint(1,6)
		count=count+r
		print("your random num is",r)
		print("you are on count",count)	
	if count==8:
		count=37
		print("you climb the ladder",count)
	if count==40:
		count=68
		print("you climb the ladder",count)
	if count==52:
		count=81
		print("you climb the ladder",count)
	if count==76:
		count=97
		print("you climb the ladder",count)
	if count==2:
		count=34
		print("you climb the ladder",count)
	if count==11:
		count=2
		print("down the ladder",count)
	if count==38:
		count=9
		print("down the ladder",count)
	if count==25:
		count=4
		print("down the ladder",count)
	if count==65:
		count=46
                print("down the ladder",count)
	if count==40:
		count=37
		print("you climb the ladder",count)
	if count==40:
		count=68
		print("you climb the ladder",count)
	if count==52:
		count=81
		print("you climb the ladder",count)
	if count==76:
		count=97
		print("you climb the ladder",count)
	if count==2:
		count=34
		print("you climb the ladder",count)
	if count==11:
		count=2
		print("down the ladder",count)
	if count==38:
		count=9
		print("down the ladder",count)
	if count==25:	
		print=4
		print("down the ladder",count)
	if count==65:
		count=46
		print("down the ladder",count)
	if count==89:
		count=70
		print("downn the ladder",count)
	if count==93:
		count=64
		print("down the ladder",count)
	if count>=100:
		count=100
		print("congrats you are always the winner",count)							

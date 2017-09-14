while(i<=100)
    n=int(input("press 4 to roll the dice:"))
    if(n==4):
    	r=random.randint(1,6)
    	i=i=5
    	print("you got:",r)
    	print("your position is:",i)
    	if(i==3):
    	   i=34
    	   print("congrats!you got a ladder to 34")
    	elif(i==8):
    	     i=37
    	   print("congrats! you got a ladder to 37")
    	elif(i==40):
    	     i=68
    	    print("congrats! you got a ladder to 68") 
    	elif(i==52):
    	     i=81
    	     print    
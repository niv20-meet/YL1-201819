a= input("pls enter a num ")
isprime =True 
for i in a :
	if i != 0 and i != 1 and i!=a and a % i ==0:  
		print("not a prime number ")
		isprime =False 



if isprime == True: 
	print ("prime NUMBER ")

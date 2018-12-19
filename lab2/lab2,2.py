a = [1,1,2,3,5,13,21,34,55,89]
b =[1,2,3,4,5,6,7,8,9,0,11,22,21]
common = []
for i in a: 
	if i in b:
		common.append(i)
print(common)
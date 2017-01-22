for i in range(1,18):
	if i<=9:
		for j in range(1,i+1):
			print("*",end='')
		print(end='\n')
	else:
		for j in range(1,10-(i-9)):
			print("*",end='')		
		print(end='\n')
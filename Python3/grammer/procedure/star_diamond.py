for i in range(1,18):
	if i<=9:
		for k in range(1,10-i):
			print(end=' ')
		for j in range(1,i+i):
			print("*",end='')
		print(end='\n')
	else:
		for k in range(1,i-8):
			print(end=' ')
		for j in range(1,(8-(i-9))*2+2):
			print("*",end='')		
		print(end='\n')

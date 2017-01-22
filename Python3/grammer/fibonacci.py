#fibonacci sequence

def fibonacci(n):
	if n==1:
		return 1
	elif n==0:
		return 0
	else:
		return fibonacci(n-2)+fibonacci(n-1)

# nterms=int(input("斐波那契项数："))
nterms=10

# if nterms<=0:
# 	print("请输入正数")
# else:
# 	print("数列为：")
for i in range(nterms):
	print(fibonacci(i),end=" ")
print(end='\n')
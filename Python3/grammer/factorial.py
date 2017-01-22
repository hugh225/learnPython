# factorial
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

#better
def fact1(n):
	return fact_iter(n,1)
def fact_iter(num,product):
	if num==1:
		return product
	else:
		return fact_iter(num-1,num*product)

nterm=5
for i in range(1,nterm+1):
	print(fact(i),fact1(i))
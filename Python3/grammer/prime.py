def _odd_iter():
#产生一个从3开始的奇数生成器
	n=1
	while True:
		n=n+2
		yield n

def _not_divisible(n):
#判断函数
	return lambda x:x%n!=0

def prime():
	yield 2
	it=_odd_iter()
	while True:
		n=next(it)
		yield n
		it=filter(_not_divisible(n),it)

for n in prime():
	if n<100:
		print(n)
	else:
		break

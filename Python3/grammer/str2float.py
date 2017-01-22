from functools import reduce
#方法1
def str2float(s):
	n=s.index('.')
	a=map(int,s[:n])
	b=map(int,s[n+1:])
	m=len(s)-n-1
	return reduce(lambda x,y:10*x+y,a)+reduce(lambda x,y:10*x+y,b)/10**m
#方法2
def str2float1(s):
	def str2int(a):
		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '.':-1}[a]
	def fn(x,y):
		if y != -1:
			return 10*x+y
		else:
			return x
	n=len(s)-s.index('.')-1
	return reduce(fn,map(str2int,s))/10**n

print(str2float('123.4576'),str2float1('123.4576'))
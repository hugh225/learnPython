#coding:utf-8
def hanoi(n,a,b,c):
	#只有一个盘的情况
	if n == 1:
		print(a,'->',c)
	#大于一个盘子的情况
	else:
		hanoi(n-1,a,c,b)#将n-1个盘子从a通过c移动到b
		print(a,'->',c)#将第n个盘子从a移动到c
		hanoi(n-1,b,a,c)#再将n-1个盘子从b通过a移动到c

hanoi(3,'a','b','c')

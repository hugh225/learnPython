def q_srot(a, left, right):
	# 递归出口
	if left>right:
		return

	i=left
	j=right
	pivot=a[left]

	while i!=j:
		while a[j]>pivot and i<j:
			j-=1
		while a[i]<=pivot and i<j:#由于第一个元素就是其本身，而本身直接不需要进行交换（下标要略过）所以要加上等号。
			i+=1

		if i<j:
			a[i], a[j]=a[j], a[i]

	a[left], a[i]=a[i], a[left] #数字归位

	q_srot(a, left, i-1)
	q_srot(a, i+1, right)

a = [int(n) for n in input().split(',')]

q_srot(a, 0, len(a)-1)

for a in a:
	print(a)
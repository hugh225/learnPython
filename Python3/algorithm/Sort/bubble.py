a = [int(n) for n in input().split(',')]

for i in range(len(a)):
	for j in range(len(a)-1-i):
		if a[j] < a[j+1]:
			a[j],a[j+1] = a[j+1],a[j]

for a in a:
	print(a)
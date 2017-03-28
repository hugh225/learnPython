
def quick_sort(a, left, right):
	if left>right:
		return

	i=left
	j=right
	pivot=a[left]

	while i!=j:
		while a[j]>=pivot and i<j:
			j-=1;
		while a[i]<=pivot and i<j:
			i+=1;

		if i<j:
			a[i],a[j]=a[j],a[i]

	a[left],a[i]=a[i],a[left]

	quick_sort(a, left, i-1)
	quick_sort(a, i+1, right)

a=[int(n) for n in input().split(',')]

quick_sort(a, 0, len(a)-1)

print(a[0])
for i in range(1, len(a)):
	if a[i] != a[i-1]:
		print(a[i])


		
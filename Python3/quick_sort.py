def q_sort(a, left, right):
	if left>right:
		return

	pivotIndex=left
	storeIndex=pivotIndex+1
	pivot=a[left]

	for i in range(pivotIndex+1, right+1):
		if a[i]<pivot:
			a[storeIndex], a[i]=a[i],a[storeIndex]
			storeIndex+=1
	a[storeIndex-1], a[pivotIndex]=a[pivotIndex], a[storeIndex-1]

	q_sort(a, left, storeIndex-2)
	q_sort(a, storeIndex, right)

a = [int(n) for n in input().split(',')]
q_sort(a, 0 ,len(a)-1)
for a in a:
	print(a)
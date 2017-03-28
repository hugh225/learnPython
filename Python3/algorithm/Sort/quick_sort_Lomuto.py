a = [int(n) for n in input().split(",")]

def qucik_sort(a, left, right):
	if left > right:
		return
	
	pivotIndex = left
	storeIndex = pivotIndex + 1
	for x in range(pivotIndex + 1,right+1):
		if a[x] < a[pivotIndex]:
			a[storeIndex],a[x] = a[x],a[storeIndex]
			storeIndex += 1
	a[pivotIndex],a[storeIndex-1] = a[storeIndex-1],a[pivotIndex]

	qucik_sort(a,left,storeIndex-2)
	qucik_sort(a,storeIndex,right)
# 调用
qucik_sort(a,0,len(a)-1)
# 输出
for a in a:
	print(a)
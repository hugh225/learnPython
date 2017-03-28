def quick_sort(arr):
	if len(arr)<2:
		return arr	

	pivot=arr[0]

	left=[i for i in arr if i<pivot]
	middle=[i for i in arr if i==pivot]
	right=[i for i in arr if i>pivot]

	return quick_sort(left)+middle+quick_sort(right)

b=[6,4,5,2,1,9]
t=quick_sort(b)
print(t)
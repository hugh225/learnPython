def sum_re(n):
	if n == 1:
		return 1
	else:
		return n+sum_re(n-1)
#better
def sum1_re(n):
	return sum_iter(n,1)
def sum_iter(n,sumary):
	if n == 1:
		return sumary
	else:
		return sum_iter(n-1,n+sumary)

print(sum_re(3),sum1_re(3))
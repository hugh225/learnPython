#!/usr/bin/env python
a = [0 for i in range(11)]
b = [int(n) for n in input().split(',')]
# print(a)
# print(b)
for i in b:
	a[i] += 1
for m in range(10,-1,-1):
	for k in range(a[m]):
		print(m)
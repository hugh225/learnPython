import string
str='{([{}()])}'
a=list(str)

def match(a, b):
	if (a =='(' and b ==')') or (a=='[' and b==']') or (a=='{' and b=='}'):
		return True
	else:
		return False
s=[]
i=0
if a[0] in [')',']','}']:
	print("no")
else:
	while True:
		# print("输入",a[i])
		if a[i] in ['(','[','{']:
			s.append(a[i])
		elif a[i] in [')',']','}']:
			# print("栈最后一个元素为：",s[-1])
			if match(s[-1], a[i]):
				s.pop()
			else:
				s.append(a[i])
		# print("栈",s)
		# 每处理一个括号字符list下标加一，以处理下一个字符
		i+=1
		if i==len(a):
			break
# print(a)
# print(s)
	if len(s)==0:
		print("yes")
	else:
		print("no")




while True:
	value = input("Integer please: [Type 'q' to quit.]")
	if value == 'q':
		break
	num = int(value)
	if num % 2 == 0:
		continue
	print(num*num)

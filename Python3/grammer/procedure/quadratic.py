import math
def quadratic(a,b,c):
	return (-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a)
print(quadratic(2,3,1))
print(quadratic(1,3,-4))
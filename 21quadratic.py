import math 
def quadratic(a,b,c):
	d = b**2 - 4*a*c >0
	if d >= 0:
		e = (-b + math.sqrt(d)) / (2*a)
		f = (-b - math.sqrt(d)) / (2*a)
		return e, f
	else:
		print("no real answer")
x = quadratic(1,5,1)
print(x)
y = quadratic (-1, -4, -1)
print(y)
z = quadratic(0.21, 0.68, 0.15)
print(z)
z1 = quadratic(3,5,1)
print(z1)
z2 = quadratic(1,0,0)
print(z2)
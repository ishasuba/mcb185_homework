# 20demo.py by Isha Suba

print('hello, again') # greeting

# practice math 
print (1 + 1)
print (5 % 2)
print (2**3)

import math 
math.log10(50)

# pythagorean theorem
a = 7
b = 5
c = math.sqrt(a**2 + b**2)
print(c)

# functions
def greeting():
	print('hello yourself')
def pythagoras(a, b):
	assert(a > 0)
	assert(b > 0)
	c = math.sqrt(a**2 + b**2)
	return c
x = pythagoras(3,4)
print(x)

# practice
def neg_to_pause(a):
	return(-1*a)
print(neg_to_pause(5))
print(neg_to_pause(-5))

def celsius_to_kelvin(a):
	return(a+273.15)
print(celsius_to_kelvin(50))
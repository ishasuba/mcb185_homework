import random
import math 

inside_circle = 0
total = 0

while True:
	x = random.random()
	y = random.random()
	distance = math.sqrt(x**2 + y**2)
	if distance < 1: 
		inside_circle += 1
	total += 1
	pi = (inside_circle / total)
	print(4 * pi)
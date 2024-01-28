import math 

def entropy(a, c, g, t): 
	total = a + c + g + t
	per_a = a / total
	per_c = c / total 
	per_g = g / total 
	per_t = t / total
	H = 0
	if a > 0: H = H + per_c * math.log2(per_a)
	if c > 0: H = H + per_c * math.log2(per_c)
	if g > 0: H = H + per_g * math.log2(per_g)
	if t > 0: H = H + per_t * math.log2(per_t)
	return(-H)
y = entropy(1, 1, 1, 1)
print(y)
z = entropy(4, 6, 3, 10)
print(z)
z1 = entropy(0, 4, 4, 4)
print(z1)
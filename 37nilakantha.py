# edits inspired by TA OH, when Lilith was helping Adele & George 

def nilakantha(n):
	sign = 1
	d = 2
	x = 3
	for i in range(n):  
		x =  x + (sign * (4 / (d * (d+1) * (d+2))))
		sign = (sign) * (-1)
		d = d + 2
	return x

print(nilakantha(3))
print(nilakantha(5))
print(nilakantha(200000))
# 38quiz.py by Isha Suba, Co-authors: Francesca Gasperini, Amina Muhic

def GregoryLeibniz(n): 
	sign = (-1)
	d = 3
	x = 0
	for i in range(n): 
		x = (sign*1) / d
		sign = sign * (-1)
		d = d + 2
	return 1 - x

print(GregoryLeibniz(6))
		
def oligotemp(A, T, C, G):
	if A+T+C+G <=13: x = (A+T)*2 + (G+C)*2
	else: x = 64.9 + 41*(G+C -16.4) / (A+T+C+G)
	return x
y = oligotemp(1, 1, 1, 1)
print(y)
z = oligotemp(2, 3, 4, 4)
print(z)
b = oligotemp(5, 5, 5, 5)
print(b)	
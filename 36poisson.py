import math

def poisson(k, n):
	prob = ((n ** k) * (math.e ** (-1 * n))) / math.factorial(k)
	print("The poisson probability is", round(prob, ndigits=3))

print(poisson(1, 2))
print(poisson(6, 2))
print(poisson(4, 4))
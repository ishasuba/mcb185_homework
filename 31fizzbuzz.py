a = 1
b = 101
for i in range(a, b):
	if i % 3 == 0 and i % 5 == 0: 
		print('Fizzbuzz')
	elif i % 3 == 0: 
		print('Fizz')
	elif i % 5 == 0: 
		print('Buzz')
	else: 
		print(i)

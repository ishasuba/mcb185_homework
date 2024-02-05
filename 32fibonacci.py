n = 10
n1 = 0
n2 = 1
print(n1)
print(n2)
for i in range(0, n):
	next_num = n1 + n2
	n1 = n2 
	n2 = next_num
	print(next_num)
		
		
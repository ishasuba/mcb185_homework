# edits inspired by TA OH, when Lilith was helping Yutong

nts = 'ACGT'
print('   ', end='')
row1 = ''
for nt in nts:
	print(nt, row1, end = ' ')
print()

for b1 in nts:
	print(b1, end=' ')
	for b2 in nts:
		if b1 == b2:
			print('+1', end= ' ')
		else: 
			print('-1', end= ' ')
	print()

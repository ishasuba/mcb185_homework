import random

sequence_num = 0
for sequence_num in range(5):
	print("seq-", sequence_num + 1)
	for i in range(60):
		bases = 'ATCG'
		print(random.choice(bases), end='')
	print("\n")
	
# This code is based on Jordan's demo in class 2/8

import random

trials = 10000

print('normal')
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for n in range(trials):
		normal_roll = random.randint(1, 20)
		if normal_roll >= dc: success += 1
	print(success / trials)
print('\n')

print('advantage')
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	max_score = 0
	for n in range(trials):
		roll_a1 = random.randint(1, 20)
		roll_a2 = random.randint(1, 20)
		if roll_a1 > roll_a2: max_score = roll_a1
		else: max_score = roll_a2
		if max_score >= dc: success += 1
	print(success / trials)
print('\n')

print('disadvantage')
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	min_score = 0
	for n in range(trials):
		roll_d1 = random.randint(1, 20)
		roll_d2 = random.randint(1, 20)
		if roll_d1 < roll_a2: min_score = roll_d1
		else: min_score = roll_d2
		if min_score >= dc: success += 1
	print(success / trials)
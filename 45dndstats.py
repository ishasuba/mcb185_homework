# Modifications made based on Amina's demo in class on 2/8
# Modifications made based on 2/8 Coderie, when Prof. Korf was helping Khalid

import random 

rolls = 10000
total = 0

#3D6
for i in range(rolls):
	score_1 = 0
	for j in range(3):
		score_1 += random.randint(1, 6)
	total += score_1
print(total / rolls)

#3D6r1
total = 0
for i in range(rolls):
	for j in range(3):
		d1 = random.randint(1, 6)
		if d1 == 1:
			d1 = random.randint(1, 6)
		total += d1
print(total / rolls)

#3D6x2
total = 0
for i in range(rolls):
	score_3 = 0
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 > d2:
			score_3 += d1
		else:
			score_3 += d2
	total += score_3
print(total / rolls)

# 4D6d1
total = 0
for i in range(rolls):
	score_4 = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	if d1 < d2 and d1 < d3 and d1 < d4: score_4 += d2 + d3 + d4
	elif d2 < d1 and d2 < d3 and d2 < d4: score_4 += d1 + d3 + d4
	elif d3 < d1 and d3 < d2 and d3 < d4: score_4 += d1 + d2 + d4
	else: score_4 = d1 + d2 + d3
	total += score_4
print (total / rolls)

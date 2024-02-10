# Modifications made based on Amina's demo in class on 2/8
# Modifications made based on 2/8 Coderie, when Prof. Korf was helping Khalid

import random 

rolls = 10000

#3D6
total_d1 = 0
for i in range(rolls):
	score_1 = 0
	for j in range(3):
		score_1 += random.randint(1, 6)

#3D6r1
for i in range(rolls):
	score_2 = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	if d1 == 0:
		d1 = random.randint(1, 6)
	elif d1 == 0:
		d2 = random.randint(1, 6)
	elif d3 == 0:
		d3 = random.randint(1, 6)
	else:
		score_2 = d1 + d2 + d3

#3D6x2
for i in range(rolls):
	score_3 = 0
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 >= d2:
			score_3 = score_3 + d1
		else:
			score_3 = score_3 + d2

# 4D6d1
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

average = (score_1 + score_2 + score_3 + score_4) / rolls
print(average)
import random 
import sys

games = 1000000
log = games // 100
total = 0
zeroes = 0 
for i in range(games):
	if i % log == 0: print(f'{100 * i/games:.0f}', file=sys.stderr)
	score = 0
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target: 
			score += target
	if score == 0: zeroes += 1
	total += score
print(total / games)
print(zeroes / games)

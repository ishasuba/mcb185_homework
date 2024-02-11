import random 
import math

trials = 1000

stable = 0
revive = 0
dead = 0

for n in range(trials):
	failure = 0
	success = 0
	while failure < 3 and success < 3:
		roll = random.randint(1, 20)
		if roll == 20: 
			revive += 1
		elif roll == 1:
			failure += 2
		elif roll >= 10:
			success += 1
		elif roll < 10:
			failure += 1
		if success >= 3:
			stable += 1
		if failure >= 3:
			dead += 1

final_count = stable + revive + dead
p_dead = (dead / final_count)
p_stable = (stable / final_count)
p_revive = (revive / final_count)

print('die:', round(p_dead, ndigits=3))
print('stabilize:', round(p_stable, ndigits=3))
print('revive:', round(p_revive, ndigits=3))
		
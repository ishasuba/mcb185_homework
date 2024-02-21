import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

success = 0

for i in range(trials):
	calendar = [] 				
	for j in range(1, 366):				
		calendar.append(0)
	for k in range(people):
		birthday = random.randint(0, 364)
		calendar[birthday] += 1
		if calendar[birthday] == 2:
			success += 1
			break

print(success / trials)
		
		
	
	
# major diagonal minus half matrix or sort as you go

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

success = 0

for i in range(trials):
	all_birthdays = []
	for j in range(people):
		birthday = random.randint(0, days)
		if birthday in all_birthdays:
			success += 1
			break
		else:
			all_birthdays.append(birthday)
		
print(success / trials)			
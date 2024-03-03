# based on class demo 2.29

import sys
import mcb185
import dogma

path = sys.argv[1]

def hydro(seq, w, t):
	for i in range(len(seq) - w + 1):
		frame = seq[i:i+w]
		avgkdh = dogma.avg_kdh(frame)
		if avgkdh >= t and 'P' not in frame:
			return True
		
	return False

for defline, seq in mcb185.read_fasta(path):
	words = defline.split(']')
	name = words[0]
	if hydro(seq[:30], 8, 2.5) and hydro(seq[30:], 11, 2.0):
		print(name + ']')
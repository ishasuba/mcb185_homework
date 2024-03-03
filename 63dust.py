import sys
import mcb185
import dogma

file = sys.argv[1]
w = int(sys.argv[2])
h_t = float(sys.argv[3])

x = []

for defline, seq in mcb185.read_fasta(file):
	print(f'>{defline}')
	
	
	for i in range(0, len(seq) -w + 1, w):
		s = seq[i:i+w]
		a = s.count('A')
		c = s.count('C')
		g = s.count('G')
		t = s.count('T')
		h = dogma.entropy(a, c, g, t)
		
		for j in s:
			if h < h_t:
				s = s.replace(j, "N")
		
		x.append(s)
final_result = ''.join(x)

# similar to translation 
for i in range(0, len(final_result), 60):
	print(final_result[i:i+60])
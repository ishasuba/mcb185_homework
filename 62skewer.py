# when window moves: G leaves, subtract 1 from G count and GC count
# when window moves: C leaves, subtract 1 from C count and GC count
# if G or C enter the window: add 1 
# edits made in class 2/29

import sys
import mcb185

path = sys.argv[1]
w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(path):
	c_nt = seq[0:w].count('C')
	g_nt = seq[0:w].count('G')
	
	for i in range(0, len(seq) -w + 1):
		nt_old = seq[i]
		nt_new = seq[i+w]
		
		if nt_old == 'C': 
			c_nt -= 1
		elif nt_old == 'G': 
			g_nt -= 1
			
		if nt_new == 'C': 
			c_nt += 1
		elif nt_new == 'G': 
			g_nt += 1
			
		gc_count = c_nt + g_nt
		gc_comp = (c_nt + g_nt) / w
		if gc_count > 0:
			gc_skew = (g_nt - c_nt) / gc_count
		else:
			gc_skew = 0

		print(i, comp, skew)
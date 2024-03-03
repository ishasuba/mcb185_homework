import math

def transcribe(dna):
	return dna.replace('T', 'U')

def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if nt == 'A': rc.append('T')
		elif nt =='C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:			rc.append('N')
	return ''.join(rc)

def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon == 'ATG': aas.append('M')
		elif codon == 'TTT': aas.append('F')
		elif codon == 'TTC': aas.append('F')
		elif codon == 'AAA': aas.append('K')
		elif codon == 'AAG': aas.append('K')
		elif codon == 'TCT': aas.append('S')
		elif codon == 'TCC': aas.append('S')
		elif codon == 'TCA': aas.append('S')
		elif codon == 'TCG': aas.append('S') 
		elif codon == 'AGT': aas.append('S') 
		elif codon == 'AGC': aas.append('S') 
		elif codon == 'TAT': aas.append('Y')
		elif codon == 'TAC': aas.append('Y')
		elif codon == 'TGT': aas.append('C') 
		elif codon == 'TGC': aas.append('C') 
		elif codon == 'TGG': aas.append('W')
		elif codon == 'TTA': aas.append('L')
		elif codon == 'TTG': aas.append('L')
		elif codon == 'CTT': aas.append('L')
		elif codon == 'CTC': aas.append('L')
		elif codon == 'CTA': aas.append('L') 
		elif codon == 'CTG': aas.append('L')
		elif codon == 'CCT': aas.append('P')
		elif codon == 'CCC': aas.append('P') 
		elif codon == 'CCA': aas.append('P')
		elif codon == 'CCG': aas.append('P')
		elif codon == 'CAT': aas.append('H')
		elif codon == 'CAC': aas.append('H')
		elif codon == 'CGT': aas.append('R')
		elif codon == 'CGC': aas.append('R')
		elif codon == 'CGA': aas.append('R')
		elif codon == 'CGG': aas.append('R')
		elif codon == 'AGA': aas.append('R') 
		elif codon == 'AGG': aas.append('R')
		elif codon == 'ATT': aas.append('I')
		elif codon == 'ATC': aas.append('I')
		elif codon == 'ATA': aas.append('I')
		elif codon == 'ACT': aas.append('T')
		elif codon == 'ACC': aas.append('T')
		elif codon == 'ACA': aas.append('T')
		elif codon == 'ACG': aas.append('T')
		elif codon == 'GTT': aas.append('V')
		elif codon == 'GTC': aas.append('V')
		elif codon == 'GTA': aas.append('V')
		elif codon == 'GTG': aas.append('V')
		elif codon == 'AAT': aas.append('N')
		elif codon == 'AAC': aas.append('N')
		elif codon == 'GGT': aas.append('G')
		elif codon == 'GGC': aas.append('G')
		elif codon == 'GGA': aas.append('G')
		elif codon == 'GGG': aas.append('G')
		elif codon == 'GCT': aas.append('A')
		elif codon == 'GCC': aas.append('A')
		elif codon == 'GCA': aas.append('A')
		elif codon == 'GCG': aas.append('A')
		elif codon == 'GAT': aas.append('D')
		elif codon == 'GAC': aas.append('D')
		elif codon == 'GAA': aas.append('E')
		elif codon == 'GAG': aas.append('E')
		elif codon == 'CAA': aas.append('Q')
		elif codon == 'CAG': aas.append('Q')
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGA': aas.append('*')	
		else:				aas.append('X')
	return ''.join(aas)

def gc_comp(seq):
	return(seq.count('C') + seq.count('G')) / len(seq)

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)

def entropy(a, c, g, t):
	total = a + c + g + t
	per_a = a / total
	per_c = c / total 
	per_g = g / total 
	per_t = t / total
	H = 0
	if a > 0: H = H + per_c * math.log2(per_a)
	if c > 0: H = H + per_c * math.log2(per_c)
	if g > 0: H = H + per_g * math.log2(per_g)
	if t > 0: H = H + per_t * math.log2(per_t)
	return(-H)

def kdh(aa):
	if aa == 'A': return 1.80
	if aa == 'C': return 2.50
	if aa == 'D': return -3.50
	if aa == 'E': return -3.50
	if aa == 'F': return 2.80
	if aa == 'G': return -0.40
	if aa == 'H': return -3.20
	if aa == 'I': return 4.50
	if aa == 'K': return -3.90
	if aa == 'L': return 3.80
	if aa == 'M': return 1.90
	if aa == 'N': return -3.50
	if aa == 'P': return -1.60
	if aa == 'Q': return -3.50
	if aa == 'R': return -4.50
	if aa == 'S': return -0.80
	if aa == 'T': return -0.70
	if aa == 'V': return 4.20
	if aa == 'W': return -0.90
	if aa == 'Y': return -1.30
	else: return 0
	
def avg_kdh(dna):
	score = 0
	for aa in dna:
		score += kdh(aa)
	return score / len(dna)
	
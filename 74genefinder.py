
import mcb185
import sys
import dogma

minorf = int(sys.argv[2])

def find_orf(seq, mini):
	orf = {}
	n = 0
	
	while n < len(seq):
		codon = seq[n:n+3]
		if codon != 'ATG':
			n += 3
			continue
		begin = n + 1 + frame
		
		for i in range(n, len(seq) - 2, 3):
			codon = seq[i:i+3]
			
			if codon == 'TGA' or codon == 'TAA' or codon == 'TAG':
				end = i + 3 + frame
				
				if end - begin >= minorf:
					orf[begin] = end
		
				n = i
				break
			
		n += 3
		
	return orf
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split()
	name = words[0]
	rev = dogma.revcomp(seq)
	
	for frame in range(3):
		print('frame ', frame)
		fseq = seq[frame:]
		rseq = rev[frame:]
		
		for begin, end in find_orf(fseq, minorf).items():
			print(f'{name}\t{begin}\t{end}\t pos')
		for begin, end in find_orf(rseq, minorf).items():
			print(f'{name}\t{begin}\t{end}\t neg')

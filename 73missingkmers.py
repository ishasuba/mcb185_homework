# class 2/29 unit6, similar to hw62
# start k at 1, increase until missing kmers
# only report missing kmers
# stop after finding k value with missing k mers
# search both strands
# kmer = sequence of length k

import sys
import itertools
import mcb185
import dogma

kcount = {}

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(f'>{defline}')
	rev = dogma.revcomp(seq)
	
	for k in range(len(seq)):
			for i in range(len(seq) - k + 1):
				kmer = seq[i:i+k]
				if kmer not in kcount:
					kcount[kmer] = 0
				kcount[kmer] += 1
	
				revkmer = rev[i:i+k]
				if revkmer not in kcount:
					kcount[revkmer] = 0
				kcount[revkmer] += 1
			
			x = 1
		
			for nts in itertools.product('ACGT', repeat=k):
				kmer = ''.join(nts)
				if kmer not in kcount:
					x += 1
					print(kmer)
						
			if x >= 2:
				break
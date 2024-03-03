
import sys
import dogma
import mcb185

path = sys.argv[1]
minlen = int(sys.argv[2])

def sixframe_translation(dna):
	translatedseq = []
	
	for n in range(3):
		fwd = dogma.translate(dna[n:])
		translatedseq.append(fwd)
		
		revseq = dogma.revcomp(dna)
		rev = dogma.translate(revseq[n:])
		translatedseq.append(rev)
		
	return translatedseq
	
	
def protein_finder(seq, minlen):
	proteins = []
	final_translation = sixframe_translation(seq)
	
	for frames in final_translation:
		begin = False
		aa_list = ''
		
		for aa in frames:
			if begin: 
				if aa == '*':
					if len(aa_list) > minlen: 
						proteins.append(aa_list)
					aa_list = ''						
					begin = False
				else:
					aa_list += aa
			elif aa == 'M':
				begin = True
		return proteins


for defline, seq, in mcb185.read_fasta(path):
	words = defline.split()
	name = words[0]
	count = 0
	final_aas = protein_finder(seq, minlen)
	for protein in final_aas:
		print(f'{name}-prot-{count}')
		print(protein)
		count += 1	
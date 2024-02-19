
# indexes
seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq: print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])

# slices
s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s, s[::], s[::1], s[::-1])

# tuples 
tax = ('Homo', 'sapiens', 9606)
print(tax)
print(tax[0])
print(tax[::-1])

# enumerate() and zip()
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)

names = ('adenine', 'cysteine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	
# lists
nts = ['A', 'T', 'C']
print(nts)

nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)

aas = list(alph)
print(aas)

# split() and join()
text = 'good day  to you'
words = text.split()
print(words)

line = '1.41, 2.72, 3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('find G?', alph.index('G'))


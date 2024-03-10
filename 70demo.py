d = {}
d = {'dog': 'woof', 'cat': 'meow'}
print(d)
print(d['cat'])

# add new item
d['pig']  = 'oink'
print(d)

# change an item
d['cat'] = 'mew'
print(d)

# delete an item
del d['cat']
print(d)

# error
# print(d['rat'])

# check if key exists
if 'dog' in d: print(d['dog'])

# iterate

# for loop goes through keys in the order they were created
for key in d: print({f'{key} says {d[key]}'})

# common way to iterate
for k, v in d.items(): print(k, 'says', v)

# only keys: dict.keys(), only values: dict.values()
# can coerce them with list()
print(d.keys(), d.values(), list(d.values()))

#better way to count nt
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1

# sort output by name
# python3 71countgff.py ecoli.gff.gz | sort

# sort output numerically
# python3 71countgff.py ecoli.gff.gz | sort -n -k -2

# sort the keys
for k in sorted(count): print(k, count[k])

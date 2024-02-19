# report count, min, max, mean, std dev, median

import gzip
import sys

gffpath = sys.argv[1]
feature = sys.argv[2]


distance = []
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] == feature:
			beg = int(words[3])
			end = int(words[4])
			distance.append(end - beg + 1)
print('Count:', len(distance))
	
def mean(vals):
	total = 0
	for val in vals: 
		total += val
	return total / len(vals)
print('Mean:', round(mean(distance)))

def std_dev(vals):
	mean_vals = mean(vals)
	deviation = 0
	total = 0
	for val in vals:
		deviation = (val - mean_vals) ** 2
		total += deviation
	total = (total / len(vals)) ** 0.5
	return total
print('Stdev:', round(std_dev(distance)))	

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
print('Min:', round(minimum(distance)))

def maximum(vals):
	maxi = vals[0]
	for val in vals:
		if val > maxi: maxi = val
	return maxi
print('Max:', round(maximum(distance)))
	
def median(vals):
	vals.sort()
	middle = len(vals) // 2
	if len(vals) % 2 == 0:
		return (vals[middle] + vals[middle - 1]) / 2
	else: 
		return middle
print('Med:', round(median(distance)))
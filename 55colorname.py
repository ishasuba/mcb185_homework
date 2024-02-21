import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

min_diff = 1000000
with open(colorfile) as fp:
	for line in fp:
		words = line.split()
		num = words[2].split(',')
		red = int(num[0])
		green = int(num[1])
		blue = int(num[2])
		diff = abs(R - red) + abs(G - green) + abs(B - blue)
		if diff < min_diff:
			min_diff = diff
			closest_color = words[0]
print(closest_color)
			
		
		
		
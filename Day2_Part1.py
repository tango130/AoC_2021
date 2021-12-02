inputs = open('data2.in','r')

horziontal = 0
depth = 0

for line in inputs:
	line = line.split()
	direction = str(line[0])
	value = int(line[1])
	
	if direction == 'forward':
		horziontal = horziontal + value

	if direction == 'up':
		depth = depth - value

	if direction == 'down':
		depth = depth + value

total = horziontal * depth
print(total)
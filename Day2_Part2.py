inputs = open('data2.in','r')

horziontal = 0
depth = 0
aim = 0

for line in inputs:
	line = line.split()
	direction = str(line[0])
	value = int(line[1])
	
	if direction == 'forward':
		horziontal = horziontal + value
		depth = depth + (aim * value)

	if direction == 'up':
		aim = aim - value

	if direction == 'down':
		aim = aim + value

total = horziontal * depth
print(total)
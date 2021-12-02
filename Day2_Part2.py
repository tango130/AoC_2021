inputs = open('data2.in','r')

horziontal = 0
depth = 0
aim = 0

for line in inputs:
	line = line.split()
	direction = str(line[0])
	value = int(line[1])
	
	if direction == 'forward':
		horziontal += value
		depth += (aim * value)

	if direction == 'up':
		aim -= value

	if direction == 'down':
		aim += value

total = horziontal * depth
print(total)

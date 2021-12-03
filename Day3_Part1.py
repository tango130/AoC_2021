inputs = list(map(str, open('data3.in').readlines()))

count1 = 0
count0 = 0
gamma = ''
epsilon = ''

for bit in range(12):
	for x in range(len(inputs)):
		string = inputs[x]
		n_char = string[bit]
		count1 += n_char.count('1')
		count0 += n_char.count('0')

	if count1 > count0:
		gamma += '1'
		epsilon += '0'
	else:
		gamma += '0'
		epsilon += '1'

	count0 = 0
	count1 = 0

print(gamma)
print(epsilon)

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
total = gamma * epsilon

print(total)
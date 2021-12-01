inputs = list(map(int, open('data1.in').readlines()))

n = 0

for x in range(len(inputs)-3):
	a = inputs[x] + inputs[x+1] + inputs[x+2]
	b = inputs[x+1] + inputs[x+2] + inputs[x+3]
	if a < b:
		n += 1

print(n)
inputs = list(map(int, open('data1.in').readlines()))

n = 0

for x in range(len(inputs)-1):
	if inputs[x] < inputs[x+1]:
		n += 1

print(n)
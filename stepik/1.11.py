a, b, c, d = [int(input()) for i in range(4)]

print(' ', end = '\t')
x = c

for i in range (d - c + 1):
	print(x, end = '\t')
	x += 1

print(' ')

for i in range(b - a + 1):
	print(a, end="\t")
	x = c
	for i in range (d - c + 1):
		print(a * x, end='\t')
		x += 1
	a += 1
	print(' ')	
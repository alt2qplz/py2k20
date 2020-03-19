a = int(input())
s = 0

while a % 5 != 0:
	s += a
	a = int(input())
else:
	print(s)
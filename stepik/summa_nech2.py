a, b = [int(input()) for i in range(2)]

s = 0

if a % 2 == 0:
	a+=1

for i in range (a, b + 1, 2):
	s+=i

print(s)

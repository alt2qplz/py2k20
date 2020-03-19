a = [int(i) for i in input().split()]

#print(a)
a.sort()


#print(len(a))
s = 0
b = ''

while s < (len(a) - 1):
	if a[s] == a[s + 1]:
		b += str(a[s]) + ' '
		s += 1
		if s < (len(a) - 1):
			#print(s)
			while a[s] == a[s + 1] and s < (len(a) - 2):
				s += 1
	s += 1
	#print(s)
print(b)
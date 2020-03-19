a = [int(i) for i in input().split()]

if len(a) > 1:
	b = [0 for i in range(len(a))]
	s = 0
	for i in a:
		if s == 0:
			b[0] = a[1] + a[-1]
			s += 1
		elif s != 0 and s != (len(a) - 1):
			b[s] = a[s-1] + a[s+1]
			s +=1
		else:
			b[s] = a[s - 1] + a [0]
	#print(a)
	#print(b)
	print(*b)
else:
	print(a[0])
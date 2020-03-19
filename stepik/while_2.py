a = int(input())
b = int(input())


if a == b:
	print(a)
elif a % b == 0:
	print(a)
elif b % a == 0:
	print(b)
else:
	if a > b:
		c = a
	else:
		c = b
	while (c % a) != 0 or (c % b) != 0:
		c = c + 1
	print(c)

'''


d = a
while d % b:
    d += a
print(d)


'''





'''
	if a > b:
		c = a
		while c % a != 0 and c % b != 0: НЕПРАВИЛЬНОЕ ИСПОЛЬЗОВАНИЕ AND
			c += 1
		print(c)
	elif b > a:
		c = b
		while c % a == 0 and c % b == 0: НЕПРАВИЛЬНОЕ ИСПОЛЬЗОВАНИЕ AND
			c += 1
		print(c)
	else:
		print('net takogo')

'''


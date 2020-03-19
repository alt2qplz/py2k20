#s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

a = input()

s = 0
x = 1
m = str('')

#for i in range (len(a)):
#	if s < len(a) - 1:
#		if a[s] == a[s + 1]:
#			while a[s] == a[s + 1]:
#				x+=1
#				print('a')
#				if s < (len(a) - 2):
#					s+=1
#			m += (str(x) + a[s])	
#		else:
#			x = 1
#			s += 1

a = input()

s = 0
x = 1
m = str('')

while s != len(a) - 1:
	if a[s] == a[s + 1]:
		x += 1
		s += 1
		print(s)
	else:
		m += (str(x) + a[s])
		x = 1
		if s < len(a) - 1:
			s += 1
else:
	m += (str(x) + a[s])






print(m)
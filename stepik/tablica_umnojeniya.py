a, b, c, d = [int(input()) for i in range(4)] #Вводим четыре числа

print(' ', end = '\t') #Отступ перед первой строкой
x = c

for i in range (d - c + 1): #Выводим верхнюю строку таблицы
	print(x, end = '\t')
	x += 1

print(' ') #Перенос на следующую строку

for i in range(b - a + 1): #Цикл выодящий строки по очереди
	print(a, end="\t")
	x = c 
	for i in range (d - c + 1): #Цикл результаты умножения
		print(a * x, end='\t')
		x += 1
	a += 1
	print(' ')	
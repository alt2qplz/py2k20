'''
10.8. Кошки и собаки: создайте два файла с именами cats.txt и dogs.txt. Сохраните 
по крайней мере три клички кошек в первом файле и три клички собак во втором. 
Напишите программу, которая пытается прочитать эти файлы и выводит их содержимое на экран. 
Заключите свой код в блок try-except для перехвата исключения FileNotFoundError и вывода
понятного сообщения об отсутствии файла. Переместите один из файлов в другое место
файловой системы; убедитесь в том, что код блока except выполняется как положено
'''

cat_names = 'cats.txt'
dog_names = 'dogs.txt'

def file_read(name):
	try:
		with open(name, 'r') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f'Нет файла {name}')
	
	else:
		print(contents)

file_read(cat_names)
print()
file_read(dog_names)
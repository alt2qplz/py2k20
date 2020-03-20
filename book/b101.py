'''
10.1. Изучение Python: откройте пустой файл в текстовом редакторе и напишите 
несколько строк текста о возможностях Python. Каждая строка должна начинаться с фразы «In
Python you can…». Сохраните файл под именем learning_python.txt в каталоге, 
использованном для примеров этой главы. Напишите программу, которая читает файл и выводит текст
три раза: 
с чтением всего файла, 
с перебором строк объекта файла и 
с сохранением строк в списке с последующим выводом списка вне блока with.
'''

file_name = 'res/learning_python.txt'


with open(file_name) as file_object:
	contents = file_object.read()
	print(contents)


with open(file_name) as file_object:
	for line in file_object:
		print(line)


with open(file_name) as file_object:
	lines = file_object.readlines()


for line in lines:
	print(line)


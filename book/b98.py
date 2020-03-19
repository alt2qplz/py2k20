'''
9.8. Привилегии: напишите класс Privileges. Класс должен содержать всего один 
атрибут privileges со списком строк из упражнения 9.7. Переместите метод show_privileges()
в этот класс. 

Создайте экземпляр Privileges как атрибут класса Admin. 

Создайте новый экземпляр Admin и используйте свой метод для вывода списка привилегий.
'''

class User():
	'''Пользователь'''

	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.login_attempts = 0

	def describe_user(self):
		print(f'Name: {self.first_name.title()} {self.last_name.title()}')
		print(f'Age: {self.age}')
		print(f'Location: {self.location}', end='\n\n')

	def greet_user(self):
		print(f'Hello, {self.first_name}, how are you?', end='\n\n')

	def increment_login_attempts(self):
		'''Добавляет попытку входа'''
		self.login_attempts += 1

	def reset_login_attempts(self):
		'''Обнуляет попытки входа'''
		self.login_attempts = 0

class Admin(User):
	'''Созание администратора на основе пользователя'''

	def __init__(self, first_name, last_name, age, location, privileges):
		'''берем значения из класса-родителя'''
		super().__init__(first_name, last_name, age, location)
		self.privileges = privileges

class Privileges():
	'''Привелегии админа'''

	def __init__(self, privileges):
		self.privileges = privileges

	def show_privileges(self):
		'''Показывает привелегии администратора'''
		print(alex.first_name)
		print('Администратор может:')
		for privilege in self.privileges:
			print(f'- {privilege}')

standartPriveleges = Privileges(['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей'])

alex = Admin('Alexander', 'Savelichev', '25', 'Kazan', standartPriveleges)

alex.privileges.show_privileges()
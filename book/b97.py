'''
9.7. Администратор: администратор — особая разновидность пользователя. Напишите
класс с именем Admin, наследующий от класса User из упражнения 9.3 или упражнения 9.5
(с. 180). 

Добавьте атрибут privileges для хранения списка строк вида "разрешено добавлять
сообщения", "разрешено удалять пользователей", "разрешено банить пользователей" 
и т. д. 

Напишите метод show_privileges() для вывода набора привилегий администратора. 

Создайте экземпляр Admin и вызовите свой метод.
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

	def show_privileges(self):
		'''Показывает привелегии администратора'''
		print('Администратор может:')
		for privilege in self.privileges:
			print(f'- {privilege}')


user1 = Admin('Alexander', 'Savelichev', '25', 'Kazan',	['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей'])

user1.show_privileges()
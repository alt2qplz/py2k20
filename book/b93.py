'''
9.3. Пользователи: создайте класс с именем User. Создайте два атрибута first_name и last_
name, а затем еще несколько атрибутов, которые обычно хранятся в профиле пользователя.
Напишите метод describe_user(), который выводит сводку с информацией о пользователе.
Создайте еще один метод greet_user() для вывода персонального приветствия для пользователя.
Создайте несколько экземпляров, представляющих разных пользователей. Вызовите оба
метода для каждого пользователя.
'''

class User():
	'''Пользователь'''

	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location

	def describe_user(self):
		print(f'Name: {self.first_name.title()} {self.last_name.title()}')
		print(f'Age: {self.age}')
		print(f'Location: {self.location}', end='\n\n')

	def greet_user(self):
		print(f'Hello, {self.first_name}, how are you?', end='\n\n')

user1 = User('Alexander', 'Savelichev', '25', 'Kazan')
user2 = User('Anna', 'Muraveva', '23', 'Kazan')
user3 = User('Konstantin', 'Volkov', '24', 'Kazan')

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()
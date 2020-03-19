'''
9.5. Попытки входа: добавьте атрибут login_attempts в класс User из упражнения 9.3
(с. 175). Напишите метод increment_login_attempts(), увеличивающий значение login_
attempts на 1. Напишите другой метод с именем reset_login_attempts(), обнуляющий 
значение login_attempts.

Создайте экземпляр класса User и вызовите increment_login_attempts() несколько раз.

Выведите значение login_attempts, чтобы убедиться в том, что значение было изменено 
правильно, а затем вызовите reset_login_attempts(). Снова выведите login_attempts
и убедитесь в том, что значение обнулилось.
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

user1 = User('Alexander', 'Savelichev', '25', 'Kazan')
user2 = User('Anna', 'Muraveva', '23', 'Kazan')
user3 = User('Konstantin', 'Volkov', '24', 'Kazan')

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(user1.login_attempts)

user1.reset_login_attempts()

print(user1.login_attempts)

user1.increment_login_attempts()
user1.increment_login_attempts()

print(user1.login_attempts)
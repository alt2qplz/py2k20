'''
9.6. Киоск с мороженым: киоск с мороженым — особая разновидность ресторана. 
Напишите класс IceCreamStand, наследующий от класса Restaurant из упражнения 9.1 (с. 175) или
упражнения 9.4 (с. 180). Подойдет любая версия класса; просто выберите ту, которая вам
больше нравится. 

Добавьте атрибут с именем flavors для хранения списка сортов 
мороженого. Напишите метод, который выводит этот список. Создайте экземпляр IceCreamStand
и вызовите этот метод.
'''

class Restaurant():
	'''Созадем класс Ресторан'''
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)

	def open_restuarant(self):
		print(f'Now {self.restaurant_name} is open!')

	def set_number_served(self, people):
		'''Устанваливает количество обслуженных посетителей'''
		self.number_served = people

	def increment_number_served(self, plusPeople):
		'''Добавляет количество посетителей'''
		self.number_served += plusPeople

class IceCreamStand(Restaurant):
	'''Подкласс ресторана - мороженное'''
	def __init__(self, restaurant_name, cuisine_type, flavors):
		'''инициализируем атрибуты класса-родителя'''
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def describe_flavors(self):
		print(f'flavors: {self.flavors}')


my_icecream = IceCreamStand('name', 'type', ['one', 'two', 'three'])

my_icecream.open_restuarant()

my_icecream.increment_number_served(30)

print(my_icecream.number_served)

my_icecream.describe_flavors()
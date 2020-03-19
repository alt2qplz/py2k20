'''
9.1. Ресторан: создайте класс с именем Restaurant. Метод __init__() класса Restaurant
должен содержать два атрибута: restaurant_name и cuisine_type. Создайте метод describe_
restaurant(), который выводит два атрибута, и метод open_restaurant(), который выводит
сообщение о том, что ресторан открыт.
Создайте на основе своего класса экземпляр с именем restaurant. Выведите два атрибута
по отдельности, затем вызовите оба метода
'''

class Restaurant():
	'''Созадем класс Ресторан'''
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)

	def open_restuarant(self):
		print(f'Now {self.restaurant_name} is open!')


my_r = Restaurant('Yakitoria', 'Japan')

my_r.describe_restaurant()
my_r.open_restuarant()
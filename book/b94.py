'''
9.4. Посетители: начните с программы из упражнения 9.1 (с. 175). Добавьте атрибут
number_served со значением по умолчанию 0; он представляет количество обслуженных
посетителей. Создайте экземпляр с именем restaurant. Выведите значение number_served,
потом измените и выведите снова.

Добавьте метод с именем set_number_served(), позволяющий задать количество обслуженных 
посетителей. Вызовите метод с новым числом, снова выведите значение.

Добавьте метод с именем increment_number_served(), который увеличивает количество 
обслуженных посетителей на заданную величину. Вызовите этот метод с любым числом, 
которое могло бы представлять количество обслуженных клиентов, — скажем, за один день
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


my_r = Restaurant('Yakitoria', 'Japan')

my_r.number_served = 20

print(my_r.number_served)

my_r.set_number_served(30)

print(my_r.number_served)

my_r.increment_number_served(20)

print(my_r.number_served)
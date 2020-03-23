import unittest

from city_functions import city_country

class city_test(unittest.TestCase):
	'''Тест для проверки city_country'''

	def test_city_county(self):
		'''Данные вида 'казань, россия' работают правильно?'''
		formatted_cc = city_country('KAZAN', 'Russia')
		self.assertEqual(formatted_cc, 'Kazan, Russia')

	def test_city_county1(self):
		'''Данные вида 'казань, россия' работают правильно?'''
		formatted_cc = city_country('kazan', 'russia', '500')
		self.assertEqual(formatted_cc, 'Kazan, Russia - Population 500')

	def test_city_county2(self):
		'''Данные вида 'казань, россия' работают правильно?'''
		formatted_cc = city_country('самара', 'Россия')
		self.assertEqual(formatted_cc, 'Самара, Россия')

	def test_city_county3(self):
		'''Данные вида 'казань, россия' работают правильно?'''
		formatted_cc = city_country('самара', 'Россия', 700)
		self.assertEqual(formatted_cc, 'Самара, Россия - Population 700')

if __name__ == '__main__':
	unittest.main()
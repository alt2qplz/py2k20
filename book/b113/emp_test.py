import unittest

from employee import Employee

class testEmployee(unittest.TestCase):
	'''Тестировани класса работник'''

	def setUp(self):
		'''Описание стандартного работника'''
		self.emp = Employee('f_name', 'l_name', 1000)

	def test_give_default_raise(self):
		'''тестирование дефолтного повышения'''
		self.emp.give_raise()
		self.assertEqual(self.emp.salary, 6000)

	def test_give_custom_raise(self):
		'''тестирование кастомного повышения'''
		self.emp.give_raise(my_raise=1000)
		self.assertEqual(self.emp.salary, 2000)





if __name__ == '__main__':
 unittest.main()
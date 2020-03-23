'''
11.3. Работник: напишите класс Employee, представляющий работника. Метод __init__()
должен получать имя, фамилию и ежегодный оклад; все эти значения должны сохраняться
в атрибутах. 

Напишите метод give_raise(), который по умолчанию увеличивает ежегодный 
оклад на $5000 — но при этом может получать другую величину прибавки.

Напишите тестовый сценарий для Employee. Напишите два тестовых метода, test_give_
default_raise() и test_give_custom_raise(). Используйте метод setUp(), чтобы вам не
приходилось заново создавать экземпляр Employee в каждом тестовом метода. Запустите
свой тестовый сценарий и убедитесь в том, что оба теста прошли успешно.
'''

class Employee():
	'''Работник обыкновенный'''

	def __init__(self, f_name, l_name, salary):
		'''Добавляет экземпляру имя, фамилию, зарплату'''
		self.f_name = f_name
		self.l_name = l_name
		self.salary = salary

	def give_raise(self, my_raise=5000):
		self.salary += my_raise

	def about(self):
		return(f'Name: {self.f_name.title()} {self.l_name.title()}, Salary: {self.salary} $')


x = Employee('f_name', 'l_name', '1000')

print(x.about())


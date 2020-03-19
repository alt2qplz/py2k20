'''
8.13. Профиль: начните с копии программы user_profile.py (с. 162). Создайте собственный
профиль вызовом build_profile(), укажите имя, фамилию и три другие пары «ключзначение» для вашего описания.
'''

def build_profile(first, last, **user_info):
	'''Стройит словарь с информацией о пользователе'''
	user_info['first_name'] = first
	user_info['last_name'] = last
	return(user_info)

savelichev = build_profile('Alexander', 'Savelichev', location='Kazan', age='25')

print(savelichev)
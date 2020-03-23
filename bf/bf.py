from generator import get_pass
from perebor import get_sim
from passlist import password_list


password_list = password_list()


p = get_pass(password_list, 3)


print(p)
print()


x = ['0'] * len(p)

y = ''

'''
А что если сделать через цикл FOR
а на y == p назначить break
'''


while y != p:

	# if x[-3] == '_':
	# 	x[-1] = get_sim(x[-1], password_list)
	# 	x[-2] = get_sim(x[-2], password_list)
	# 	x[-3] = get_sim(x[-3], password_list)
	# 	x[-4] = get_sim(x[-4], password_list)
	# else:
	if x[-2] == '9' and x[-1] == '9':
		x[-1] = get_sim(x[-1], password_list)
		x[-2] = get_sim(x[-2], password_list)
		x[-3] = get_sim(x[-3], password_list)
	else:
		if x[-1] == '9':
			x[-1] = get_sim(x[-1], password_list)
			x[-2] = get_sim(x[-2], password_list)
		else:
			x[-1] = get_sim(x[-1], password_list)

	y = ''.join(x)
	print(y, end='\r')

print(f'Password: {y}')
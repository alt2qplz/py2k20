from generator import get_pass
from perebor import get_sim
from passlist import password_list

p = get_pass(password_list(), 1)

print(p)


x = ''
while x != p:
	x = get_sim(x, password_list())
	print(x)
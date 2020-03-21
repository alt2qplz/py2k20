from generator import get_pass
from perebor import get_sim
from passlist import password_list

print(get_pass(password_list(), 3))
print(get_sim('', password_list()))
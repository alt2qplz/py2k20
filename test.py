from random import randint

numbers = [i for i in range(0, 10)]

print(numbers.pop(randint(0, (len(numbers)-1))))
import random

num = random.randint(1, 9999)
num_str = str(num)


first = int(num_str[0])

last = int(num_str[-1])


print(num)
print(first)
print(last)

print(type(num_str))
print(type(first))


a = 2
b = 5

print("a = " + str(a))
print("b = " + str(b))

a,b = b,a

print("a = " + str(a))
print("b = " + str(b))

a = 8741 ** 0.5

a = (-12) // 5
b = (-12) % 5

print(a)
print(b)


a = 500
b = 1.05

print(b ** 10)
print(a * b ** 10)

d = 0x15


print (bin(d))

print('Введите число')
x = int(input())

print('Введите основание')
base = int(input())

while x > 0:
	digit = x % base
	print(digit, end='')
	x //= base


x, y = float(input()), float(input())
z = str(input())

if z == "*":
	print(x * y)
elif z == "+":
	print(x + y)
elif z == "-":
	print(x - y)
elif z == "pow":
	print(x ** y)
elif z == "/":
	if y == 0:
		print("Деление на 0!")
	else:
		print(x / y)
elif z == "div":
	if y == 0:
		print("Деление на 0!")
	else:
		print(x // y)
elif z == "mod":
	if y == 0:
		print("Деление на 0!")
	else:
		print(x % y)
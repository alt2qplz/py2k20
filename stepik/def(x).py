

def func():
	x = float(input())
	if x <= -2:
		print(1 - (x + 2) ** 2)
	elif x <= 2:
		print(-(x / 2))
	print((x - 2) ** 2 + 1)

func()
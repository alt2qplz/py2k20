type = input()

if type == "треугольник":
    a, b, c = [int(input()) for i in range(3)]
    print(float(((a + b + c) / 2 * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c)) ** 0.5))
elif type == "прямоугольник":
    a, b = [int(input()) for i in range(2)]
    print(float(a * b))
elif type == "круг":
    r = int(input())
    print(float(3.14 * r ** 2))
else:
    print("Неизвестный формат комнаты")
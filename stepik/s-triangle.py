a, b, c = [int(input()) for i in range(3)]


p = (a+b+c)/2
s = (p*(p-a)*(p-b)*(p-c)) ** 0.5

print(s)
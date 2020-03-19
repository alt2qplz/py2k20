a, b, c = [int(input()) for i in range(3)]

'''
if a > b:
    max = a
    min = b
else:
    max = b
    min = a

if c < min:
    other = min
    min = c
else:
    if max > c:
        other = c
        max = max
    else:
        other = max
        max = c

print(max)
print(min)
print(other)
'''


if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b > c:
    b, c = c, b


print(a)
print(b)
print(c)
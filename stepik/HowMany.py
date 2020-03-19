n = str(input())

if  len(n) > 1 and int(n[-2]) == 1:
        print(n, "программистов")
else:
    if int(n[-1]) == 1:
        print(n, "программист")
    elif 2 <= int(n[-1]) <= 4:
        print(n, "программиста")
    else:
        print(n, "программистов")
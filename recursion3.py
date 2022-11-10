user = int(input("Введите число "))

def revers(x, c):
    if x == 0:
        return c
    elif x > 0:
        d = x % 10
        print(d)
        print(x)
        print(c)
        return revers(x // 10, c * 10 + d)

print(revers(user, 0))
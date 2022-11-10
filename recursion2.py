user = int(input("Введите число "))

def summ(x):
    if x == 0:
        return 0
    elif x > 0:
        return x % 10 + summ(x // 10)

print(summ(user))
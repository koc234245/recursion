arr = [110, 604, 905, 310, 659, 229, 527, 113, 645, 798, 243, 584, 904, 553, 178, 510, 184, 368, 116, 469, 955, 795, 549, 703, 32, 63, 935, 258, 732]
print("должно быть", sum(arr))
def recursion(x):
    if x == []:
        return 0
    else:
        x[0]
        print(x[0])
        return x[0] + recursion(x[1:])

def recursionBack(x):
    if not x:
        return
    else:
        x[-1]
        print(x[-1])
        return recursionBack(x[:-1])

print("поочередно выведенные значения из списка и их сумма")
print(recursion(arr))
print("в обратном порядке")
recursionBack(arr)
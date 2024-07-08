n = int(input())

def func(x):
    res = 0
    for i in range(1 , x + 1):
            res = res * (10  ** len(str(i))) + i
    return res

print(func(n))

        
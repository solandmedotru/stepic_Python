def f(x):
    return x**2

n = int(input())

dic = {}

for n in range(0, n):
    n = int(input())
    if dic.get(n) == None:
        dic.setdefault(n, f(n))
    print(dic[n])
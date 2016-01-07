a = int(input())
sum=a
l = []
l.append(a)
s=0
while sum != 0:
    a = int(input())
    sum = sum + a
    l.append(a)

for i in l:
    s = s + i**2

print(s)
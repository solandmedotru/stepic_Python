a = [int(i) for i in input().split(" ")]
a.sort()
a2 = []
i = 0
while i in range(0, len(a)):
    if a.count(a[i]) > 1:
        a2.append(a[i])
        i = i+a.count(a[i])
    else:
        i+=1

for i in a2:
    print(i, end=" ")
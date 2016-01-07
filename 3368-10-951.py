a = [int(i) for i in input().split(" ")]
a2=[]
if len(a) == 1:
    a2 = a
else:
    for i in range(0,len(a)):
        if i < len(a)-1:
            a2.append(a[i-1]+a[i+1])
        else:
            a2.append(a[i-1]+a[0])
for i in a2:
    print(i, end=" ")
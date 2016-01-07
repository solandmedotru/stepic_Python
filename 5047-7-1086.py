num = input()
n0,n1,n2,n3,n4,n5 = int(num[0]),int(num[1]),int(num[2]),int(num[3]),int(num[4]),int(num[5])

if n0+n1+n2 == n3+n4+n5:
    print("Счастливый")
else:
    print("Обычный")
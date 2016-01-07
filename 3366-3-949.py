a,b,c,d = int(input()),int(input()),int(input()),int(input())

if a<=10 and b<=10 and c<=10 and d<=10 and a<=b and c<=d:
    print("", end='\t')
    for i in range(c, d+1):
        print(i, end='\t')
    print()

    for j in range(a, b+1):
        print(j, end='\t')
        for i in range(c,d+1):
            print(i*j, end='\t')
        print()
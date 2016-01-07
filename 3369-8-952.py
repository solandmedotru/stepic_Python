a = int(input())
col = 0
k = 0
i=1
while col < a:
    for i in range(1, k+1):
        print(k, end=" ")
        col+=1
        if col>=a:
            break
    k+=1
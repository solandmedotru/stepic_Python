a,b = int(input()),int(input())
sum = 0
col = 0
for i in range(a, b+1):
    if i%3==0:
        sum += i
        col +=1
print(sum/col)
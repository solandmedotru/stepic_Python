lst = [int(i) for i in input().split(" ")]
x = int(input())
pos = 0
pos_lst = []
while pos < len(lst):
    if x in lst:
        for i in lst:
            if int(i) == x:
               pos_lst.append(pos)
            pos+=1
    else:
        pos_lst.append("Отсутствует")
        break
for i in pos_lst:
    print(i, end=" ")
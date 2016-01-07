num = 0
while num < 100:
    num = int(input())
    if num < 10:
        continue
    if num > 100:
        break
    print(num)
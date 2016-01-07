num = int(input())
val = num%100
if (val > 10 and val < 20):
    print(num, "программистов")
else:
    val = num%10
    if (val == 1):
        print(num, "программист")
    elif (val > 1 and val < 5):
        print(num, "программиста")
    else:
        print(num, "программистов")
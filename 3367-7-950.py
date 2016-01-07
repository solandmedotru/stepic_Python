dnc = input()
dnc2 = ""
i=1
j=1
while i <= len(dnc):
    count = 1
    while (i<=len(dnc)-1) and (dnc[i] == dnc[i-1]):
        count = count + 1
        i+=1
    dnc2 = dnc2 + dnc[i-1] + str(count)
    i+=1
print(dnc2)
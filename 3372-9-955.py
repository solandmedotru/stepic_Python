def modify_list(l):
    l2 = []
    for k in l:
        if k % 2 == 0:
            l2.append(int(k//2))
    l.clear()
    for i in l2:
        l.append(i)
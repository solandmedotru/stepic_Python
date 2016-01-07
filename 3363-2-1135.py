text = []
col=[]
c=""
with open('dataset_3363_2.txt') as inf:
    st = str(inf.readline().strip())
    for w in st:
        if w.isalpha():
            if c != "":
                col.append(c)
            text.append(w)
            c=""
        elif w.isdigit():
            c = c+w
    col.append(c)

with open('text2.txt', 'w') as ouf:
    for t in range(0, len(text)):
        ouf.write(str(text[t]*int(col[t])).strip())
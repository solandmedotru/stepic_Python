words = input().lower().split(" ")

word={}

for w in words:

    if word.get(w) != None:
        word[w] = word[w] + 1
    else:
        word.setdefault(w,1)

for key, value in word.items():
    print(key, value)
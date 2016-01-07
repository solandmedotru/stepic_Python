def update_dictionary(d, key, value):
    if d.get(key) != None:
        d[key].append(value)
    elif d.get(key*2) != None:
        d[key*2].append(value)
    else:
        d[key*2] = [value]

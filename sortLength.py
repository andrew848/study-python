def sortLength(list):
    list.sort(key=lambda l: len(l))
    alphabetical = sorted(list, key=lambda l: (len(l), l))
    return alphabetical

print(sortLength(['abc','abcdefg','aaa']))